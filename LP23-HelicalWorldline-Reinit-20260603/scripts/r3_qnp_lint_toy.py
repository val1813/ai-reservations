"""LP23-R3 QNP-Lint finite-matrix toy/adversarial stress test.

The toy is a small cochain complex

    C0 --D0--> C1 --D1--> C2

with D1 @ D0 = 0.  A candidate residual r is first checked for closure
under D1, then projected away from exact/template/nuisance/history columns
in a whitened metric.  The remaining norm is the finite-dimensional
"residual cohomology" class norm used for QNP-Lint labels.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


TOL = 1e-9


@dataclass(frozen=True)
class LintResult:
    label: str
    rank: int
    residual_norm: float
    closed_norm: float


def incidence_matrix(nodes: int, edges: list[tuple[int, int]]) -> np.ndarray:
    d0 = np.zeros((len(edges), nodes), dtype=float)
    for row, (source, target) in enumerate(edges):
        d0[row, source] = -1.0
        d0[row, target] = 1.0
    return d0


def cycle_row(edge_count: int, signed_edges: list[tuple[int, float]]) -> np.ndarray:
    row = np.zeros(edge_count, dtype=float)
    for edge_index, sign in signed_edges:
        row[edge_index] = sign
    return row


def matrix_rank(a: np.ndarray, tol: float = TOL) -> int:
    if a.size == 0:
        return 0
    return int(np.linalg.matrix_rank(a, tol=tol))


def whitened_project_residual(
    columns: np.ndarray,
    r: np.ndarray,
    sigma: np.ndarray,
    tol: float = TOL,
) -> tuple[int, float, np.ndarray]:
    """Project r away from columns using the metric diag(1 / sigma^2)."""

    rw = r / sigma
    if columns.size == 0 or columns.shape[1] == 0:
        return 0, float(np.linalg.norm(rw)), rw

    aw = columns / sigma[:, None]
    u, s, _ = np.linalg.svd(aw, full_matrices=False)
    rank = int(np.sum(s > tol))
    if rank == 0:
        return 0, float(np.linalg.norm(rw)), rw

    q = u[:, :rank]
    residual = rw - q @ (q.T @ rw)
    return rank, float(np.linalg.norm(residual)), residual


def hstack(*blocks: np.ndarray) -> np.ndarray:
    nonempty = [b for b in blocks if b.size and b.shape[1] > 0]
    if not nonempty:
        rows = blocks[0].shape[0] if blocks else 0
        return np.zeros((rows, 0), dtype=float)
    return np.column_stack(nonempty)


def classify(
    d0: np.ndarray,
    d1: np.ndarray,
    r: np.ndarray,
    sigma: np.ndarray,
    template: np.ndarray,
    nuisance: np.ndarray,
    history: np.ndarray,
    contract_complete: bool = True,
    tol: float = TOL,
) -> LintResult:
    closed_norm = float(np.linalg.norm(d1 @ r))
    if not contract_complete:
        base = hstack(d0)
        rank, residual_norm, _ = whitened_project_residual(base, r, sigma, tol)
        return LintResult("UNDECIDED", rank, residual_norm, closed_norm)

    if closed_norm > 1e-7:
        base = hstack(d0)
        rank, residual_norm, _ = whitened_project_residual(base, r, sigma, tol)
        return LintResult("UNDECIDED", rank, residual_norm, closed_norm)

    rank_d0, norm_d0, _ = whitened_project_residual(d0, r, sigma, tol)
    if norm_d0 <= 1e-7:
        return LintResult("REPRESENTATIVE_LEAK", rank_d0, norm_d0, closed_norm)

    rank_t, norm_t, _ = whitened_project_residual(hstack(d0, template), r, sigma, tol)
    if norm_t <= 1e-7:
        return LintResult("TEMPLATE_RESIDUAL", rank_t, norm_t, closed_norm)

    rank_n, norm_n, _ = whitened_project_residual(hstack(d0, template, nuisance), r, sigma, tol)
    if norm_n <= 1e-7:
        return LintResult("NUISANCE_DIAGNOSTIC", rank_n, norm_n, closed_norm)

    rank_all, norm_all, _ = whitened_project_residual(hstack(d0, template, nuisance, history), r, sigma, tol)
    if norm_all <= 1e-7:
        return LintResult("HISTORY_DIAGNOSTIC", rank_all, norm_all, closed_norm)

    return LintResult("PASS_OBSTRUCTION", rank_all, norm_all, closed_norm)


def null_vector_orthogonal_to(columns: np.ndarray, d1: np.ndarray) -> np.ndarray:
    """Return a closed unit vector not spanned by the supplied columns."""

    constraints = hstack(columns).T
    if d1.size:
        constraints = np.vstack([constraints, d1])
    _, _, vh = np.linalg.svd(constraints, full_matrices=True)
    candidate = vh[-1, :]
    return candidate / np.linalg.norm(candidate)


def print_result(name: str, result: LintResult) -> None:
    print(
        f"{name:24s} label={result.label:22s} "
        f"rank={result.rank:2d} residual_norm={result.residual_norm:.10g} "
        f"closed_norm={result.closed_norm:.3g}"
    )


def run() -> None:
    nodes = 5
    edges = [
        (0, 1),  # e0
        (1, 2),  # e1
        (2, 0),  # e2: filled triangle closes here
        (0, 2),  # e3
        (2, 3),  # e4
        (3, 0),  # e5: second loop, intentionally unfilled
        (0, 3),  # e6
        (3, 4),  # e7
        (4, 0),  # e8: third loop, intentionally unfilled
    ]
    d0 = incidence_matrix(nodes, edges)
    d1 = cycle_row(len(edges), [(0, 1.0), (1, 1.0), (2, 1.0)])[None, :]
    sigma = np.array([1.0, 1.3, 0.8, 1.2, 0.9, 1.1, 1.4, 0.95, 1.15], dtype=float)

    template = null_vector_orthogonal_to(d0, d1)[:, None]
    nuisance = null_vector_orthogonal_to(hstack(d0, template), d1)[:, None]
    history = null_vector_orthogonal_to(hstack(d0, template, nuisance), d1)[:, None]

    chain_error = float(np.linalg.norm(d1 @ d0))
    print("QNP-Lint finite-matrix toy")
    print(f"D0 shape={d0.shape} D1 shape={d1.shape} ||D1@D0||={chain_error:.3g}")
    print("")

    exact_r = d0 @ np.array([0.0, 0.35, -0.10, 0.20, -0.25])
    template_r = exact_r + 0.7 * template[:, 0]
    nuisance_r = exact_r + 0.5 * nuisance[:, 0]
    obstruction_r = 0.9 * null_vector_orthogonal_to(hstack(d0, template, nuisance, history), d1)
    undecided_r = obstruction_r.copy()

    cases = [
        ("representative_leak", exact_r, True),
        ("template_residual", template_r, True),
        ("nuisance_diagnostic", nuisance_r, True),
        ("pass_obstruction", obstruction_r, True),
        ("missing_contract", undecided_r, False),
    ]

    print("base classification")
    for name, r, contract_complete in cases:
        result = classify(d0, d1, r, sigma, template, nuisance, history, contract_complete)
        print_result(name, result)

    print("")
    print("adversarial expansion on pass_obstruction")
    base_result = classify(d0, d1, obstruction_r, sigma, template, nuisance, history)
    print_result("base", base_result)

    attacks = [
        ("+one_template_col", obstruction_r[:, None], np.zeros((len(edges), 0)), np.zeros((len(edges), 0))),
        ("+one_nuisance_col", np.zeros((len(edges), 0)), obstruction_r[:, None], np.zeros((len(edges), 0))),
        ("+one_history_col", np.zeros((len(edges), 0)), np.zeros((len(edges), 0)), obstruction_r[:, None]),
    ]
    for label, t_extra, n_extra, h_extra in attacks:
        result = classify(
            d0,
            d1,
            obstruction_r,
            sigma,
            hstack(template, t_extra),
            hstack(nuisance, n_extra),
            hstack(history, h_extra),
        )
        print_result(label, result)

    print("")
    print("raw residual vectors")
    print("obstruction_r=", np.array2string(obstruction_r, precision=6, suppress_small=True))


if __name__ == "__main__":
    run()

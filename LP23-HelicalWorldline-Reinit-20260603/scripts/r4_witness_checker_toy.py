"""LP23-R4 Round2 witness-checker toy.

Round1 used hand-written constrained columns.  This script upgrades the toy to
proof-carrying extension columns: a column is admitted only if its witness
passes independent checkers for support-locality, protocol partial order, and
passive/decaying history kernels.  The finite matrices are a stress test, not a
physical derivation.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum

import numpy as np


TOL = 1e-9


class SourceKind(str, Enum):
    LOCAL_STENCIL = "local_stencil"
    HISTORY_KERNEL = "history_kernel"
    ORACLE = "oracle"


@dataclass(frozen=True)
class ColumnWitness:
    label: str
    source: SourceKind
    preregistered: bool
    support: tuple[int, ...]
    max_support_diameter: int
    dependencies: tuple[tuple[int, tuple[int, ...]], ...]
    kernel: tuple[float, ...] = ()
    kernel_edges: tuple[int, ...] = ()


@dataclass(frozen=True)
class CandidateColumn:
    values: np.ndarray
    witness: ColumnWitness


@dataclass(frozen=True)
class CheckResult:
    accepted: bool
    failures: tuple[str, ...]


@dataclass(frozen=True)
class ClosureResult:
    label: str
    rank: int
    residual_norm: float
    accepted_columns: tuple[str, ...]
    rejected_columns: tuple[str, ...]


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


def vector(edge_count: int, entries: list[tuple[int, float]]) -> np.ndarray:
    out = np.zeros(edge_count, dtype=float)
    for index, value in entries:
        out[index] = value
    return out


def hstack(*blocks: np.ndarray) -> np.ndarray:
    nonempty = [b for b in blocks if b.size and b.shape[1] > 0]
    if nonempty:
        return np.column_stack(nonempty)
    rows = blocks[0].shape[0] if blocks else 0
    return np.zeros((rows, 0), dtype=float)


def support(values: np.ndarray) -> tuple[int, ...]:
    return tuple(int(i) for i in np.nonzero(np.abs(values) > TOL)[0])


def shortest_path_lengths(edges: list[tuple[int, int]]) -> np.ndarray:
    edge_count = len(edges)
    distances = np.full((edge_count, edge_count), edge_count + 1, dtype=int)
    for i in range(edge_count):
        distances[i, i] = 0
    for i, (a0, a1) in enumerate(edges):
        a = {a0, a1}
        for j, (b0, b1) in enumerate(edges):
            if i != j and a.intersection({b0, b1}):
                distances[i, j] = 1
    for k in range(edge_count):
        for i in range(edge_count):
            for j in range(edge_count):
                distances[i, j] = min(distances[i, j], distances[i, k] + distances[k, j])
    return distances


def support_diameter(indices: tuple[int, ...], distances: np.ndarray) -> int:
    if len(indices) <= 1:
        return 0
    return int(max(distances[i, j] for i in indices for j in indices))


def check_support_locality(
    column: CandidateColumn,
    distances: np.ndarray,
    max_diameter: int = 1,
) -> str | None:
    actual = support(column.values)
    claimed = tuple(sorted(column.witness.support))
    if actual != claimed:
        return f"support mismatch actual={actual} witness={claimed}"
    diameter = support_diameter(actual, distances)
    if diameter > max_diameter:
        return f"nonlocal support diameter={diameter} max={max_diameter}"
    if column.witness.max_support_diameter < diameter:
        return (
            "witness understates support diameter "
            f"claimed={column.witness.max_support_diameter} actual={diameter}"
        )
    return None


def check_protocol_order(column: CandidateColumn, protocol_rank: dict[int, int]) -> str | None:
    for target, sources in column.witness.dependencies:
        if target not in protocol_rank:
            return f"unknown target edge e{target}"
        for source in sources:
            if source not in protocol_rank:
                return f"unknown dependency edge e{source}"
            if protocol_rank[source] > protocol_rank[target]:
                return f"future dependence e{target} <- e{source}"
    return None


def check_passive_decaying_kernel(column: CandidateColumn) -> str | None:
    if column.witness.source != SourceKind.HISTORY_KERNEL:
        return None
    kernel = np.array(column.witness.kernel, dtype=float)
    if kernel.size == 0:
        return "history kernel witness is empty"
    if len(column.witness.kernel_edges) != kernel.size:
        return "kernel edge list length does not match kernel"
    if np.any(kernel < -TOL):
        return f"kernel has negative weight {kernel.tolist()}"
    if np.any(np.diff(kernel) > TOL):
        return f"kernel is not decaying {kernel.tolist()}"
    nonzero = np.array([column.values[i] for i in column.witness.kernel_edges], dtype=float)
    if not np.allclose(nonzero, kernel, atol=1e-9):
        return "kernel witness does not match column amplitudes"
    return None


def check_preregistration(column: CandidateColumn) -> str | None:
    if column.witness.source == SourceKind.ORACLE:
        return "oracle/residual-shaped source is not an allowed measurement source"
    if not column.witness.preregistered:
        return "column source was not preregistered before seeing residual"
    return None


def check_column(
    column: CandidateColumn,
    distances: np.ndarray,
    protocol_rank: dict[int, int],
) -> CheckResult:
    checks = (
        check_support_locality(column, distances),
        check_protocol_order(column, protocol_rank),
        check_passive_decaying_kernel(column),
        check_preregistration(column),
    )
    failures = tuple(failure for failure in checks if failure is not None)
    return CheckResult(accepted=not failures, failures=failures)


def whitened_project_residual(
    columns: np.ndarray,
    residual: np.ndarray,
    sigma: np.ndarray,
    tol: float = TOL,
) -> tuple[int, float]:
    rw = residual / sigma
    if columns.size == 0 or columns.shape[1] == 0:
        return 0, float(np.linalg.norm(rw))

    aw = columns / sigma[:, None]
    u, s, _ = np.linalg.svd(aw, full_matrices=False)
    rank = int(np.sum(s > tol))
    if rank == 0:
        return 0, float(np.linalg.norm(rw))

    q = u[:, :rank]
    remainder = rw - q @ (q.T @ rw)
    return rank, float(np.linalg.norm(remainder))


def unit_null_vector(constraints: np.ndarray, tol: float = TOL) -> np.ndarray:
    _, s, vh = np.linalg.svd(constraints, full_matrices=True)
    rank = int(np.sum(s > tol))
    candidate = vh[rank, :]
    norm = float(np.linalg.norm(candidate))
    if norm <= tol:
        raise ValueError("no null vector available")
    return candidate / norm


def closure_with_checked_columns(
    label: str,
    d0: np.ndarray,
    candidates: list[CandidateColumn],
    residual: np.ndarray,
    sigma: np.ndarray,
    distances: np.ndarray,
    protocol_rank: dict[int, int],
) -> tuple[ClosureResult, dict[str, CheckResult]]:
    accepted: list[CandidateColumn] = []
    rejected: list[str] = []
    checks: dict[str, CheckResult] = {}
    for column in candidates:
        result = check_column(column, distances, protocol_rank)
        checks[column.witness.label] = result
        if result.accepted:
            accepted.append(column)
        else:
            rejected.append(column.witness.label)

    extra = np.column_stack([column.values for column in accepted]) if accepted else np.zeros((d0.shape[0], 0))
    rank, residual_norm = whitened_project_residual(hstack(d0, extra), residual, sigma)
    if residual_norm <= 1e-7:
        outcome = "WITNESS_ACCEPTED_ABSORBED"
    else:
        outcome = "WITNESS_OBSTRUCTION"
    return (
        ClosureResult(
            label=f"{label}:{outcome}",
            rank=rank,
            residual_norm=residual_norm,
            accepted_columns=tuple(column.witness.label for column in accepted),
            rejected_columns=tuple(rejected),
        ),
        checks,
    )


def legal_columns(edge_count: int) -> list[CandidateColumn]:
    local_loop = CandidateColumn(
        values=vector(edge_count, [(3, 1.0), (4, 1.0), (5, 1.0)]),
        witness=ColumnWitness(
            label="local_loop",
            source=SourceKind.LOCAL_STENCIL,
            preregistered=True,
            support=(3, 4, 5),
            max_support_diameter=2,
            dependencies=((3, (3,)), (4, (3, 4)), (5, (3, 4, 5))),
        ),
    )
    history_fast = CandidateColumn(
        values=vector(edge_count, [(6, 1.0), (7, 0.45), (8, 0.20)]),
        witness=ColumnWitness(
            label="history_fast",
            source=SourceKind.HISTORY_KERNEL,
            preregistered=True,
            support=(6, 7, 8),
            max_support_diameter=2,
            dependencies=((6, (6,)), (7, (6, 7)), (8, (6, 7, 8))),
            kernel=(1.0, 0.45, 0.20),
            kernel_edges=(6, 7, 8),
        ),
    )
    return [local_loop, history_fast]


def residual_oracle_column(residual: np.ndarray) -> CandidateColumn:
    return CandidateColumn(
        values=residual.copy(),
        witness=ColumnWitness(
            label="residual_oracle",
            source=SourceKind.ORACLE,
            preregistered=False,
            support=support(residual),
            max_support_diameter=99,
            dependencies=tuple((i, tuple(range(len(residual)))) for i in support(residual)),
        ),
    )


def print_column_checks(checks: dict[str, CheckResult]) -> None:
    for name, result in checks.items():
        verdict = "PASS" if result.accepted else "FAIL"
        print(f"  {name:16s} {verdict}")
        for failure in result.failures:
            print(f"    - {failure}")


def print_closure(result: ClosureResult) -> None:
    print(
        f"{result.label:44s} rank={result.rank:2d} "
        f"residual_norm={result.residual_norm:.10g} "
        f"accepted={list(result.accepted_columns)} rejected={list(result.rejected_columns)}"
    )


def run() -> None:
    nodes = 5
    edges = [
        (0, 1),  # e0
        (1, 2),  # e1
        (2, 0),  # e2
        (0, 2),  # e3
        (2, 3),  # e4
        (3, 0),  # e5
        (0, 3),  # e6
        (3, 4),  # e7
        (4, 0),  # e8
    ]
    protocol_order = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    protocol_rank = {edge: rank for rank, edge in enumerate(protocol_order)}
    distances = shortest_path_lengths(edges)

    d0 = incidence_matrix(nodes, edges)
    d1 = cycle_row(len(edges), [(0, 1.0), (1, 1.0), (2, 1.0)])[None, :]
    sigma = np.array([1.0, 1.3, 0.8, 1.2, 0.9, 1.1, 1.4, 0.95, 1.15], dtype=float)

    columns = legal_columns(len(edges))
    legal_matrix = hstack(d0, np.column_stack([column.values for column in columns]))

    constraints = np.vstack([legal_matrix.T, d1])
    residual = unit_null_vector(constraints)
    oracle = residual_oracle_column(residual)

    algebraic_rank, algebraic_residual_norm = whitened_project_residual(
        hstack(legal_matrix, oracle.values[:, None]),
        residual,
        sigma,
    )
    legal_closure, legal_checks = closure_with_checked_columns(
        "legal_only",
        d0,
        columns,
        residual,
        sigma,
        distances,
        protocol_rank,
    )
    challenged_closure, challenged_checks = closure_with_checked_columns(
        "with_residual_oracle",
        d0,
        [*columns, oracle],
        residual,
        sigma,
        distances,
        protocol_rank,
    )

    print("R4 witness-checker toy")
    print(f"D0 shape={d0.shape} D1 shape={d1.shape} ||D1@D0||={float(np.linalg.norm(d1 @ d0)):.3g}")
    print(f"candidate closedness={float(np.linalg.norm(d1 @ residual)):.3g}")
    print(f"candidate residual={np.array2string(residual, precision=6, suppress_small=True)}")
    print("")
    print("witness checks for legal columns:")
    print_column_checks(legal_checks)
    print("")
    print("witness checks with residual-shaped oracle column:")
    print_column_checks(challenged_checks)
    print("")
    print("closure comparison:")
    print_closure(legal_closure)
    print_closure(challenged_closure)
    print(
        f"algebraic_open_if_oracle_ignored_checks       rank={algebraic_rank:2d} "
        f"residual_norm={algebraic_residual_norm:.10g}"
    )
    print("")
    if challenged_checks["residual_oracle"].accepted:
        print("verdict=R4_DEAD: residual-shaped oracle passed the witness checker")
    elif challenged_closure.residual_norm > 1e-7 and algebraic_residual_norm <= 1e-7:
        print(
            "verdict=TOY_SURVIVES_CHECKER: oracle would absorb algebraically, "
            "but fails locality/order/source witnesses before entering closure"
        )
    else:
        print("verdict=UNDECIDED: checker result and projection result did not split cleanly")


if __name__ == "__main__":
    run()

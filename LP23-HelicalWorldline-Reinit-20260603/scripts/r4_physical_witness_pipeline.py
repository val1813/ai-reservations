"""LP23-R4 Round3 physical witness pipeline.

The pipeline order is deliberately fixed:

1. write/read a preregistered column registry;
2. verify witnesses without seeing the residual;
3. rank accepted columns;
4. project the training residual;
5. score prediction on held-out channels.

Candidate columns are never generated from the residual.  The residual is a
synthetic probe used only after witness verification.

Round3 revision: the synthetic probe is explicitly generated from the same
accepted columns that are later evaluated.  Therefore the holdout score is not
independent validation evidence.  The script keeps the score as a smoke-test
diagnostic, but the verdict is hard-downgraded unless an independent holdout
generator is supplied.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Any

import numpy as np


TOL = 1e-9
ROOT = Path(__file__).resolve().parents[1]
PRE_REGISTRY = ROOT / "scripts" / "columns_pre.json"
SYNTHETIC_RESIDUAL_PROVENANCE = (
    "synthetic residual = gauge + 0.55*local_loop_stencil "
    "+ 1.35*passive_tail_pr + deterministic_probe_noise"
)
HOLDOUT_INDEPENDENT = False


class SourceKind(str, Enum):
    LOCAL_STENCIL = "local_stencil"
    PASSIVE_REALIZATION = "passive_realization"
    ORACLE = "oracle"


@dataclass(frozen=True)
class ColumnSpec:
    label: str
    source: SourceKind
    preregistered: bool
    support: tuple[int, ...]
    values: tuple[float, ...]
    max_support_diameter: int
    dependencies: tuple[tuple[int, tuple[int, ...]], ...]
    poles: tuple[float, ...] = ()
    residues: tuple[float, ...] = ()
    direct: float = 0.0
    sample_edges: tuple[int, ...] = ()
    sample_frequencies: tuple[float, ...] = ()


@dataclass(frozen=True)
class CheckResult:
    accepted: bool
    failures: tuple[str, ...]


def incidence_matrix(nodes: int, edges: list[tuple[int, int]]) -> np.ndarray:
    d0 = np.zeros((len(edges), nodes), dtype=float)
    for row, (source, target) in enumerate(edges):
        d0[row, source] = -1.0
        d0[row, target] = 1.0
    return d0


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


def vector(edge_count: int, entries: list[tuple[int, float]]) -> tuple[float, ...]:
    out = np.zeros(edge_count, dtype=float)
    for index, value in entries:
        out[index] = value
    return tuple(float(x) for x in out)


def passive_stieltjes_samples(
    poles: tuple[float, ...],
    residues: tuple[float, ...],
    direct: float,
    frequencies: tuple[float, ...],
) -> tuple[float, ...]:
    values = []
    for frequency in frequencies:
        response = direct
        for pole, residue in zip(poles, residues):
            response += residue / (frequency + pole)
        values.append(float(response))
    return tuple(values)


def preregistered_specs(edge_count: int) -> list[ColumnSpec]:
    poles = (0.45, 1.6)
    residues = (1.25, 0.35)
    direct = 0.04
    frequencies = (1.0, 2.0, 3.0)
    passive_values = passive_stieltjes_samples(poles, residues, direct, frequencies)

    return [
        ColumnSpec(
            label="local_loop_stencil",
            source=SourceKind.LOCAL_STENCIL,
            preregistered=True,
            support=(3, 4, 5),
            values=vector(edge_count, [(3, 1.0), (4, 1.0), (5, 1.0)]),
            max_support_diameter=2,
            dependencies=((3, (3,)), (4, (3, 4)), (5, (3, 4, 5))),
        ),
        ColumnSpec(
            label="passive_tail_pr",
            source=SourceKind.PASSIVE_REALIZATION,
            preregistered=True,
            support=(6, 7, 8),
            values=vector(
                edge_count,
                [(6, passive_values[0]), (7, passive_values[1]), (8, passive_values[2])],
            ),
            max_support_diameter=2,
            dependencies=((6, (6,)), (7, (6, 7)), (8, (6, 7, 8))),
            poles=poles,
            residues=residues,
            direct=direct,
            sample_edges=(6, 7, 8),
            sample_frequencies=frequencies,
        ),
        ColumnSpec(
            label="oracle_source_challenge",
            source=SourceKind.ORACLE,
            preregistered=False,
            support=tuple(range(edge_count)),
            values=vector(edge_count, [(i, 0.25 + 0.03 * i) for i in range(edge_count)]),
            max_support_diameter=99,
            dependencies=tuple((i, tuple(range(edge_count))) for i in range(edge_count)),
        ),
        ColumnSpec(
            label="future_leak_challenge",
            source=SourceKind.LOCAL_STENCIL,
            preregistered=True,
            support=(0, 1),
            values=vector(edge_count, [(0, 1.0), (1, -1.0)]),
            max_support_diameter=1,
            dependencies=((0, (1,)), (1, (1,))),
        ),
    ]


def write_pre_registry(path: Path, specs: list[ColumnSpec]) -> None:
    serializable: list[dict[str, Any]] = []
    for spec in specs:
        item = {
            "label": spec.label,
            "source": spec.source.value,
            "preregistered": spec.preregistered,
            "support": list(spec.support),
            "values": list(spec.values),
            "max_support_diameter": spec.max_support_diameter,
            "dependencies": [
                {"target": target, "sources": list(sources)}
                for target, sources in spec.dependencies
            ],
            "poles": list(spec.poles),
            "residues": list(spec.residues),
            "direct": spec.direct,
            "sample_edges": list(spec.sample_edges),
            "sample_frequencies": list(spec.sample_frequencies),
        }
        serializable.append(item)
    path.write_text(json.dumps(serializable, indent=2, sort_keys=True), encoding="utf-8")


def load_pre_registry(path: Path) -> list[ColumnSpec]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    specs = []
    for item in raw:
        specs.append(
            ColumnSpec(
                label=item["label"],
                source=SourceKind(item["source"]),
                preregistered=bool(item["preregistered"]),
                support=tuple(int(x) for x in item["support"]),
                values=tuple(float(x) for x in item["values"]),
                max_support_diameter=int(item["max_support_diameter"]),
                dependencies=tuple(
                    (int(dep["target"]), tuple(int(x) for x in dep["sources"]))
                    for dep in item["dependencies"]
                ),
                poles=tuple(float(x) for x in item.get("poles", [])),
                residues=tuple(float(x) for x in item.get("residues", [])),
                direct=float(item.get("direct", 0.0)),
                sample_edges=tuple(int(x) for x in item.get("sample_edges", [])),
                sample_frequencies=tuple(float(x) for x in item.get("sample_frequencies", [])),
            )
        )
    return specs


def check_preregistration(spec: ColumnSpec) -> str | None:
    if not spec.preregistered:
        return "column was not preregistered before residual was opened"
    return None


def check_source_kind(spec: ColumnSpec) -> str | None:
    if spec.source == SourceKind.ORACLE:
        return "oracle/residual-shaped source is not an allowed physical source"
    return None


def check_support_locality(spec: ColumnSpec, distances: np.ndarray) -> str | None:
    values = np.array(spec.values, dtype=float)
    actual = tuple(int(i) for i in np.nonzero(np.abs(values) > TOL)[0])
    if actual != tuple(sorted(spec.support)):
        return f"support mismatch actual={actual} witness={spec.support}"
    diameter = support_diameter(actual, distances)
    if diameter > spec.max_support_diameter:
        return f"nonlocal support diameter={diameter} max={spec.max_support_diameter}"
    return None


def check_order(spec: ColumnSpec, protocol_rank: dict[int, int]) -> str | None:
    for target, sources in spec.dependencies:
        for source in sources:
            if protocol_rank[source] > protocol_rank[target]:
                return f"future dependence e{target} <- e{source}"
    return None


def check_physical_source(spec: ColumnSpec) -> str | None:
    if spec.source == SourceKind.LOCAL_STENCIL:
        return None
    if spec.source != SourceKind.PASSIVE_REALIZATION:
        return None

    poles = np.array(spec.poles, dtype=float)
    residues = np.array(spec.residues, dtype=float)
    if poles.size == 0 or residues.size == 0 or poles.size != residues.size:
        return "passive-real witness needs paired positive poles and residues"
    if np.any(poles <= TOL):
        return f"passive-real poles must be positive {poles.tolist()}"
    if np.any(residues < -TOL) or spec.direct < -TOL:
        return "passive-real residues/direct term must be nonnegative"

    expected = passive_stieltjes_samples(
        spec.poles,
        spec.residues,
        spec.direct,
        spec.sample_frequencies,
    )
    observed = tuple(float(spec.values[edge]) for edge in spec.sample_edges)
    if not np.allclose(observed, expected, atol=1e-9):
        return f"passive-real samples do not match column values {observed} != {expected}"
    if np.any(np.diff(np.array(observed, dtype=float)) > TOL):
        return f"passive-real samples are not decaying {observed}"
    return None


def verify_specs(
    specs: list[ColumnSpec],
    distances: np.ndarray,
    protocol_rank: dict[int, int],
) -> dict[str, CheckResult]:
    results = {}
    for spec in specs:
        failures = tuple(
            failure
            for failure in (
                check_preregistration(spec),
                check_source_kind(spec),
                check_support_locality(spec, distances),
                check_order(spec, protocol_rank),
                check_physical_source(spec),
            )
            if failure is not None
        )
        results[spec.label] = CheckResult(accepted=not failures, failures=failures)
    return results


def hstack(*blocks: np.ndarray) -> np.ndarray:
    nonempty = [block for block in blocks if block.size and block.shape[1] > 0]
    if nonempty:
        return np.column_stack(nonempty)
    rows = blocks[0].shape[0] if blocks else 0
    return np.zeros((rows, 0), dtype=float)


def fit_train_predict_holdout(
    columns: np.ndarray,
    residual: np.ndarray,
    train_idx: np.ndarray,
    holdout_idx: np.ndarray,
    sigma: np.ndarray,
) -> tuple[int, float, float]:
    aw = columns[train_idx, :] / sigma[train_idx, None]
    rw = residual[train_idx] / sigma[train_idx]
    _, singular_values, _ = np.linalg.svd(aw, full_matrices=False)
    rank = int(np.sum(singular_values > TOL))
    coeffs, *_ = np.linalg.lstsq(aw, rw, rcond=None)
    train_remainder = rw - aw @ coeffs

    predicted_holdout = columns[holdout_idx, :] @ coeffs
    holdout_remainder = (residual[holdout_idx] - predicted_holdout) / sigma[holdout_idx]
    return rank, float(np.linalg.norm(train_remainder)), float(np.linalg.norm(holdout_remainder))


def synthetic_residual(d0: np.ndarray, specs: list[ColumnSpec]) -> np.ndarray:
    by_label = {spec.label: np.array(spec.values, dtype=float) for spec in specs}
    gauge = d0 @ np.array([0.15, -0.05, 0.08, -0.03, 0.12], dtype=float)
    residual = (
        gauge
        + 0.55 * by_label["local_loop_stencil"]
        + 1.35 * by_label["passive_tail_pr"]
    )
    deterministic_probe_noise = np.array(
        [0.002, -0.001, 0.0015, -0.002, 0.001, -0.001, 0.001, -0.0015, 0.0],
        dtype=float,
    )
    return residual + deterministic_probe_noise


def verdict(
    train_residual_norm: float,
    holdout_error: float,
    oracle_rejected: bool,
    holdout_independent: bool,
) -> str:
    if not oracle_rejected:
        return "R4_DEAD_ORACLE_ADMITTED"
    if not holdout_independent:
        return "R4_TOOL_NOT_VALIDATED_BY_HOLDOUT"
    if train_residual_norm <= 5e-3 and holdout_error <= 5e-3:
        return "R4_TOOL_SURVIVES_TOY_PHYSICAL_PIPELINE"
    return "R4_DOWNGRADE_TOY_RULES_OR_NO_HOLDOUT_POWER"


def run() -> dict[str, Any]:
    edges = [
        (0, 1),
        (1, 2),
        (2, 0),
        (0, 2),
        (2, 3),
        (3, 0),
        (0, 3),
        (3, 4),
        (4, 0),
    ]
    protocol_rank = {edge: rank for rank, edge in enumerate(range(len(edges)))}
    distances = shortest_path_lengths(edges)
    d0 = incidence_matrix(5, edges)

    write_pre_registry(PRE_REGISTRY, preregistered_specs(len(edges)))
    specs = load_pre_registry(PRE_REGISTRY)
    checks = verify_specs(specs, distances, protocol_rank)
    accepted_specs = [spec for spec in specs if checks[spec.label].accepted]

    accepted_matrix = (
        np.column_stack([np.array(spec.values, dtype=float) for spec in accepted_specs])
        if accepted_specs
        else np.zeros((len(edges), 0), dtype=float)
    )
    closure = hstack(d0, accepted_matrix)
    residual = synthetic_residual(d0, specs)
    sigma = np.array([1.0, 1.3, 0.8, 1.2, 0.9, 1.1, 1.4, 0.95, 1.15], dtype=float)
    train_idx = np.array([0, 1, 2, 3, 4, 5, 6, 7], dtype=int)
    holdout_idx = np.array([8], dtype=int)
    rank, train_residual_norm, holdout_error = fit_train_predict_holdout(
        closure,
        residual,
        train_idx,
        holdout_idx,
        sigma,
    )
    oracle_rejected = not checks["oracle_source_challenge"].accepted
    result = {
        "pre_registry": str(PRE_REGISTRY),
        "accepted_columns": [spec.label for spec in accepted_specs],
        "rejected_columns": [
            {"label": label, "failures": list(check.failures)}
            for label, check in checks.items()
            if not check.accepted
        ],
        "rank": rank,
        "train_residual_norm": train_residual_norm,
        "holdout_error": holdout_error,
        "holdout_independent": HOLDOUT_INDEPENDENT,
        "holdout_evidence_status": "not_independent_synthetic_smoke_test_only",
        "synthetic_residual_provenance": SYNTHETIC_RESIDUAL_PROVENANCE,
        "blocked_claims": [
            "holdout_error is independent prediction-power evidence",
            "holdout_error validates the physical witness checker",
        ],
        "oracle_rejected": oracle_rejected,
        "verdict": verdict(
            train_residual_norm,
            holdout_error,
            oracle_rejected,
            HOLDOUT_INDEPENDENT,
        ),
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return result


if __name__ == "__main__":
    run()

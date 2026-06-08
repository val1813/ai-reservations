"""Two-terminal single-particle transport ledger for NSF-FCS-1.

This script is a minimal falsification harness for the rewritten NSF-FCS-1
transport question.  It intentionally rejects bare reservoir-exchange
observables: only a channel-resolved two-terminal transport current can enter
the keep/kill ledger.
"""

from __future__ import annotations

import argparse
import csv
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import numpy as np


@dataclass(frozen=True)
class Edge:
    src: int
    dst: int
    rate: float
    g: float
    channel: str


@dataclass(frozen=True)
class ReservoirSpec:
    reservoir_id: str
    alpha_kernel: float
    c_bulk: float = 1.0
    c_left: float = 1.0
    c_right: float = 1.0
    rho0: float = 0.5
    rho_left: float | None = None
    rho_right: float | None = None
    kind: str = "tail"
    m_tail: int = 4000
    l_prefactor: str = "none"
    observable_kind: str = "left_transport_current"
    affinity_mode: str = "two_terminal_symmetric"
    affinity_split: float = 0.5
    activity_mode: str = "none"
    activity_bias: float = 0.0
    sector: str = "single"

    @property
    def alpha_tail_effective(self) -> float:
        return self.alpha_kernel


def reservoir_tail_rate(
    x: int, L: int, alpha: float, c: float, side: str, m_tail: int
) -> float:
    if alpha <= 0:
        raise ValueError("alpha_kernel must be positive")
    if side == "right":
        # z = L+1, ..., L+m_tail, plus integral tail.
        finite = sum((z - x) ** (-(1.0 + alpha)) for z in range(L + 1, L + m_tail + 1))
        tail_start = L + m_tail + 1 - x
    elif side == "left":
        # z = -m_tail, ..., 0, plus integral tail to -infinity.
        finite = sum((x - z) ** (-(1.0 + alpha)) for z in range(-m_tail, 1))
        tail_start = x + m_tail + 1
    else:
        raise ValueError(f"unknown side {side!r}")
    return c * (finite + tail_start ** (-alpha) / alpha)


def eta_values(F: float, mode: str, split: float) -> tuple[float, float]:
    if mode == "two_terminal_symmetric":
        return -(1.0 - split) * F, split * F
    if mode == "right_only_transport":
        return 0.0, F
    raise ValueError(f"unknown affinity mode {mode!r}")


def centered_site_coordinate(x: int, L: int) -> float:
    if L <= 1:
        return 0.0
    return (x - 0.5 * (L + 1)) / L


def activity_factors(x: int, L: int, side: str, spec: ReservoirSpec) -> tuple[float, float]:
    """Return multiplicative in/out factors for activity controls."""
    phi = centered_site_coordinate(x, L)
    bias = spec.activity_bias
    if spec.activity_mode == "none" or bias == 0.0:
        return 1.0, 1.0
    if spec.activity_mode == "reversible_side":
        side_sign = +1.0 if side == "left" else -1.0
        traffic = math.exp(side_sign * bias * phi)
        return traffic, traffic
    if spec.activity_mode == "nonLDB_site_skew":
        side_sign = +1.0 if side == "left" else -1.0
        eta = side_sign * bias * phi
        return math.exp(+0.5 * eta), math.exp(-0.5 * eta)
    raise ValueError(f"unknown activity mode {spec.activity_mode!r}")


def reservoir_rates(x: int, L: int, spec: ReservoirSpec) -> tuple[float, float]:
    if spec.kind == "tail":
        r_left = reservoir_tail_rate(
            x, L, spec.alpha_kernel, spec.c_left, "left", spec.m_tail
        )
        r_right = reservoir_tail_rate(
            x, L, spec.alpha_kernel, spec.c_right, "right", spec.m_tail
        )
        return r_left, r_right
    if spec.kind == "contact":
        return (spec.c_left if x == 1 else 0.0, spec.c_right if x == L else 0.0)
    raise ValueError(f"unknown reservoir kind {spec.kind!r}")


def build_single_edges(L: int, spec: ReservoirSpec, F: float = 0.0) -> list[Edge]:
    if spec.l_prefactor != "none":
        raise ValueError("L-dependent reservoir prefactors are not valid for this fast-boundary ledger")

    eta_left, eta_right = eta_values(F, spec.affinity_mode, spec.affinity_split)
    rho_left = spec.rho0 if spec.rho_left is None else spec.rho_left
    rho_right = spec.rho0 if spec.rho_right is None else spec.rho_right
    edges: list[Edge] = []
    empty = 0

    # Bulk occupied-state jumps. State x is represented by integer x.
    for x in range(1, L + 1):
        for y in range(1, L + 1):
            if x == y:
                continue
            rate = spec.c_bulk / abs(x - y) ** (1.0 + spec.alpha_kernel)
            edges.append(Edge(x, y, rate, 0.0, "bulk"))

    # Channel-resolved source/sink edges. Do not merge left/right e<->x edges:
    # the current labels differ even when source and destination coincide.
    for x in range(1, L + 1):
        r_left, r_right = reservoir_rates(x, L, spec)
        left_in_activity, left_out_activity = activity_factors(x, L, "left", spec)
        right_in_activity, right_out_activity = activity_factors(x, L, "right", spec)

        left_in = rho_left * r_left * math.exp(+0.5 * eta_left) * left_in_activity
        left_out = (1.0 - rho_left) * r_left * math.exp(-0.5 * eta_left) * left_out_activity
        right_in = rho_right * r_right * math.exp(+0.5 * eta_right) * right_in_activity
        right_out = (1.0 - rho_right) * r_right * math.exp(-0.5 * eta_right) * right_out_activity

        if spec.observable_kind == "left_transport_current":
            g_left_in, g_left_out = -1.0, +1.0
            g_right_in, g_right_out = 0.0, 0.0
        elif spec.observable_kind == "bare_right_exchange":
            g_left_in, g_left_out = 0.0, 0.0
            g_right_in, g_right_out = +1.0, -1.0
        else:
            raise ValueError(f"unknown observable kind {spec.observable_kind!r}")

        edges.extend(
            [
                Edge(empty, x, left_in, g_left_in, "left"),
                Edge(x, empty, left_out, g_left_out, "left"),
                Edge(empty, x, right_in, g_right_in, "right"),
                Edge(x, empty, right_out, g_right_out, "right"),
            ]
        )

    return [edge for edge in edges if edge.rate > 0.0]


def has_particle(mask: int, site: int) -> bool:
    return bool(mask & (1 << site))


def flip_particle(mask: int, site: int) -> int:
    return mask ^ (1 << site)


def move_particle(mask: int, src_site: int, dst_site: int) -> int:
    return (mask ^ (1 << src_site)) | (1 << dst_site)


def build_exclusion_edges(L: int, spec: ReservoirSpec, F: float = 0.0) -> list[Edge]:
    if spec.l_prefactor != "none":
        raise ValueError("L-dependent reservoir prefactors are not valid for this fast-boundary ledger")

    eta_left, eta_right = eta_values(F, spec.affinity_mode, spec.affinity_split)
    rho_left = spec.rho0 if spec.rho_left is None else spec.rho_left
    rho_right = spec.rho0 if spec.rho_right is None else spec.rho_right
    edges: list[Edge] = []

    for mask in range(1 << L):
        for i in range(L):
            if not has_particle(mask, i):
                continue
            for j in range(L):
                if i == j or has_particle(mask, j):
                    continue
                physical_i = i + 1
                physical_j = j + 1
                rate = spec.c_bulk / abs(physical_i - physical_j) ** (1.0 + spec.alpha_kernel)
                edges.append(Edge(mask, move_particle(mask, i, j), rate, 0.0, "bulk"))

        for i in range(L):
            physical_x = i + 1
            r_left, r_right = reservoir_rates(physical_x, L, spec)
            left_in_activity, left_out_activity = activity_factors(physical_x, L, "left", spec)
            right_in_activity, right_out_activity = activity_factors(physical_x, L, "right", spec)
            occupied = has_particle(mask, i)

            left_in = rho_left * r_left * math.exp(+0.5 * eta_left) * left_in_activity
            left_out = (1.0 - rho_left) * r_left * math.exp(-0.5 * eta_left) * left_out_activity
            right_in = rho_right * r_right * math.exp(+0.5 * eta_right) * right_in_activity
            right_out = (1.0 - rho_right) * r_right * math.exp(-0.5 * eta_right) * right_out_activity

            if spec.observable_kind == "left_transport_current":
                g_left_in, g_left_out = -1.0, +1.0
                g_right_in, g_right_out = 0.0, 0.0
            elif spec.observable_kind == "bare_right_exchange":
                g_left_in, g_left_out = 0.0, 0.0
                g_right_in, g_right_out = +1.0, -1.0
            else:
                raise ValueError(f"unknown observable kind {spec.observable_kind!r}")

            if not occupied:
                dst = flip_particle(mask, i)
                edges.append(Edge(mask, dst, left_in, g_left_in, "left"))
                edges.append(Edge(mask, dst, right_in, g_right_in, "right"))
            else:
                dst = flip_particle(mask, i)
                edges.append(Edge(mask, dst, left_out, g_left_out, "left"))
                edges.append(Edge(mask, dst, right_out, g_right_out, "right"))

    return [edge for edge in edges if edge.rate > 0.0]


def build_edges(L: int, spec: ReservoirSpec, F: float = 0.0) -> list[Edge]:
    if spec.sector == "single":
        return build_single_edges(L, spec, F)
    if spec.sector == "exclusion":
        return build_exclusion_edges(L, spec, F)
    raise ValueError(f"unknown sector {spec.sector!r}")


def state_count(L: int, spec: ReservoirSpec) -> int:
    if spec.sector == "single":
        return L + 1
    if spec.sector == "exclusion":
        return 1 << L
    raise ValueError(f"unknown sector {spec.sector!r}")


def generator_from_edges(n: int, edges: Iterable[Edge], chi: float | None = None) -> np.ndarray:
    mat = np.zeros((n, n), dtype=float)
    escape = np.zeros(n, dtype=float)
    for edge in edges:
        factor = math.exp(chi * edge.g) if chi is not None else 1.0
        mat[edge.src, edge.dst] += edge.rate * factor
        escape[edge.src] += edge.rate
    for i, rate in enumerate(escape):
        mat[i, i] = -rate
    return mat


def stationary(Lmat: np.ndarray) -> tuple[np.ndarray, dict[str, float]]:
    n = Lmat.shape[0]
    system = Lmat.T.copy()
    rhs = np.zeros(n)
    system[-1, :] = 1.0
    rhs[-1] = 1.0
    pi = np.linalg.solve(system, rhs)
    resid = float(np.linalg.norm(pi @ Lmat, ord=1) / max(1.0, np.linalg.norm(Lmat, ord=1)))
    return pi, {
        "pi_resid": resid,
        "pi_norm_error": float(abs(np.sum(pi) - 1.0)),
        "min_pi": float(np.min(pi)),
    }


def fields(n: int, edges: Iterable[Edge], pi: np.ndarray) -> dict[str, np.ndarray | float]:
    b = np.zeros(n, dtype=float)
    a = np.zeros(n, dtype=float)
    for edge in edges:
        b[edge.src] += edge.rate * edge.g
        a[edge.src] += edge.rate * edge.g * edge.g
    J = float(pi @ b)
    h = b - J
    return {"b": b, "a": a, "J": J, "h": h, "a_mean": float(pi @ a)}


def weighted_norm(vec: np.ndarray, pi: np.ndarray) -> float:
    return float(math.sqrt(max(0.0, np.sum(pi * vec * vec))))


def solve_poisson(Lmat: np.ndarray, pi: np.ndarray, h: np.ndarray) -> tuple[np.ndarray, dict[str, float]]:
    n = Lmat.shape[0]
    augmented = np.zeros((n + 1, n + 1), dtype=float)
    augmented[:n, :n] = -Lmat
    augmented[:n, n] = 1.0
    augmented[n, :n] = pi
    rhs = np.zeros(n + 1, dtype=float)
    rhs[:n] = h
    solution = np.linalg.solve(augmented, rhs)
    phi = solution[:n]
    residual = -Lmat @ phi - h
    phi_norm = weighted_norm(phi, pi)
    h_norm = weighted_norm(h, pi)
    return phi, {
        "phi_resid": weighted_norm(residual, pi) / max(1.0, h_norm),
        "phi_gauge": abs(float(pi @ phi)) / max(1.0, phi_norm),
    }


def principal_lambda(Lchi: np.ndarray) -> complex:
    eigvals = np.linalg.eigvals(Lchi)
    return complex(eigvals[np.argmax(eigvals.real)])


def relative_spread(values: list[float]) -> float:
    if not values:
        return math.inf
    scale = max(1.0e-300, abs(float(np.mean(values))))
    return float((max(values) - min(values)) / scale)


def lambda_tilt_second(n: int, edges0: list[Edge], eps_grid: Iterable[float]) -> tuple[float, dict[str, float]]:
    lam0 = principal_lambda(generator_from_edges(n, edges0, chi=0.0))
    estimates: list[float] = []
    max_imag = abs(lam0.imag)
    for eps in eps_grid:
        plus = principal_lambda(generator_from_edges(n, edges0, chi=eps))
        minus = principal_lambda(generator_from_edges(n, edges0, chi=-eps))
        max_imag = max(max_imag, abs(plus.imag), abs(minus.imag))
        estimates.append(float(((plus - 2.0 * lam0 + minus) / (eps * eps)).real))
    return float(estimates[-1]), {
        "lambda_tilt_rel_spread": relative_spread(estimates),
        "lambda_tilt_max_imag": float(max_imag),
        "lambda0_abs": float(abs(lam0)),
    }


def current_for_affinity(L: int, spec: ReservoirSpec, F: float) -> float:
    edges = build_edges(L, spec, F=F)
    n = state_count(L, spec)
    Lmat = generator_from_edges(n, edges)
    pi, _ = stationary(Lmat)
    return float(fields(n, edges, pi)["J"])


def conductance(L: int, spec: ReservoirSpec, delta_grid: Iterable[float]) -> tuple[float, dict[str, float]]:
    estimates: list[float] = []
    for delta in delta_grid:
        jp = current_for_affinity(L, spec, +delta)
        jm = current_for_affinity(L, spec, -delta)
        estimates.append((jp - jm) / (2.0 * delta))
    return float(estimates[-1]), {
        "G_rel_spread": relative_spread(estimates),
        "G_min": float(min(estimates)),
        "G_max": float(max(estimates)),
    }


def coboundary_residual(n: int, edges: list[Edge]) -> float:
    # Least-squares solve psi[src] - psi[dst] = g, with psi[0]=0 gauge.
    rows = []
    rhs = []
    for edge in edges:
        row = np.zeros(n, dtype=float)
        row[edge.src] = 1.0
        row[edge.dst] -= 1.0
        rows.append(row)
        rhs.append(edge.g)
    gauge = np.zeros(n, dtype=float)
    gauge[0] = 1.0
    rows.append(gauge)
    rhs.append(0.0)
    A = np.vstack(rows)
    y = np.asarray(rhs, dtype=float)
    psi, *_ = np.linalg.lstsq(A, y, rcond=None)
    residual = A @ psi - y
    return float(np.linalg.norm(residual) / max(1.0, np.linalg.norm(y)))


def ledger_row(L: int, spec: ReservoirSpec, eps_grid: list[float], delta_grid: list[float]) -> dict[str, object]:
    n = state_count(L, spec)
    edges0 = build_edges(L, spec, F=0.0)
    L0 = generator_from_edges(n, edges0)
    pi, pi_diag = stationary(L0)
    field = fields(n, edges0, pi)
    phi, phi_diag = solve_poisson(L0, pi, field["h"])  # type: ignore[arg-type]
    corrector = 2.0 * float(pi @ (field["h"] * phi))  # type: ignore[operator]
    lam2, lam_diag = lambda_tilt_second(n, edges0, eps_grid)
    G, G_diag = conductance(L, spec, delta_grid)
    cob_resid = coboundary_residual(n, edges0)

    observable_status = (
        "coboundary" if cob_resid <= 1.0e-8 or spec.observable_kind == "bare_right_exchange"
        else "transport_non_coboundary"
    )

    status = "ok"
    if observable_status == "coboundary":
        status = "invalid_coboundary_observable"
    elif pi_diag["pi_resid"] > 1e-10 or pi_diag["pi_norm_error"] > 1e-12 or pi_diag["min_pi"] < -1e-12:
        status = "pi_failed"
    elif phi_diag["phi_resid"] > 1e-9 or phi_diag["phi_gauge"] > 1e-10:
        status = "poisson_failed"
    elif lam_diag["lambda_tilt_rel_spread"] > 3.0e-2:
        status = "lambda_tilt_unstable"
    elif G_diag["G_rel_spread"] > 2.0e-2 or G <= 0.0:
        status = "G_uncontrolled"

    S: float | None = None
    verdict = "ROW_VALID"
    if status == "invalid_coboundary_observable":
        verdict = "INVALID_BARE_EXCHANGE_NOT_TRANSPORT"
    elif status != "ok":
        verdict = "INVALID_ROW"
    else:
        S = lam2 / G

    two_c_residual = lam2 - float(field["a_mean"]) - corrector

    row: dict[str, object] = {
        "L": L,
        "reservoir_id": spec.reservoir_id,
        "alpha_kernel": spec.alpha_kernel,
        "alpha_tail_effective": spec.alpha_tail_effective,
        "reservoir_kind": spec.kind,
        "sector": spec.sector,
        "observable_kind": spec.observable_kind,
        "observable_status": observable_status,
        "affinity_mode": spec.affinity_mode,
        "affinity_split": spec.affinity_split,
        "activity_mode": spec.activity_mode,
        "activity_bias": spec.activity_bias,
        "rho_left": spec.rho0 if spec.rho_left is None else spec.rho_left,
        "rho_right": spec.rho0 if spec.rho_right is None else spec.rho_right,
        "n_state": n,
        "pi_resid": pi_diag["pi_resid"],
        "phi_resid": phi_diag["phi_resid"],
        "phi_gauge": phi_diag["phi_gauge"],
        "coboundary_resid": cob_resid,
        "a_mean": float(field["a_mean"]),
        "corrector_2hphi": corrector,
        "two_C_explicit": "NA",
        "two_C_residual": two_c_residual,
        "C_status": "C_from_tilted_residual",
        "lambda_tilt_second": lam2,
        "lambda_tilt_rel_spread": lam_diag["lambda_tilt_rel_spread"],
        "G_R": G,
        "G_rel_spread": G_diag["G_rel_spread"],
        "S_R": "NA" if S is None else S,
        "J0": float(field["J"]),
        "FDT_residual_R2": lam2 - 2.0 * G,
        "status": status,
        "verdict": verdict,
    }
    return row


def parse_float_list(text: str) -> list[float]:
    return [float(part.strip()) for part in text.split(",") if part.strip()]


def parse_int_list(text: str) -> list[int]:
    return [int(part.strip()) for part in text.split(",") if part.strip()]


def write_rows(path: Path, rows: list[dict[str, object]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fields = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--L", default="16,24,32,48,64", help="comma-separated system sizes")
    parser.add_argument("--alpha", default="0.5,1.0,1.5", help="comma-separated alpha_kernel values")
    parser.add_argument("--observable", choices=["left_transport_current", "bare_right_exchange"], default="left_transport_current")
    parser.add_argument("--kind", choices=["tail", "contact"], default="tail")
    parser.add_argument("--sector", choices=["single", "exclusion"], default="single")
    parser.add_argument("--rho-left", type=float, default=None)
    parser.add_argument("--rho-right", type=float, default=None)
    parser.add_argument("--affinity-split", type=float, default=0.5)
    parser.add_argument("--activity-mode", choices=["none", "reversible_side", "nonLDB_site_skew"], default="none")
    parser.add_argument("--activity-bias", type=float, default=0.0)
    parser.add_argument("--m-tail", type=int, default=4000)
    parser.add_argument("--eps", default="1e-2,5e-3,2.5e-3,1.25e-3")
    parser.add_argument("--delta", default="1e-2,5e-3,2.5e-3")
    parser.add_argument("--out", default="current/plan/nsf_fcs_transport_ledger.csv")
    args = parser.parse_args()

    rows: list[dict[str, object]] = []
    for alpha in parse_float_list(args.alpha):
        spec = ReservoirSpec(
            reservoir_id=f"{args.kind}_alpha_{alpha:g}_{args.observable}",
            alpha_kernel=alpha,
            kind=args.kind,
            m_tail=args.m_tail,
            observable_kind=args.observable,
            rho_left=args.rho_left,
            rho_right=args.rho_right,
            affinity_split=args.affinity_split,
            activity_mode=args.activity_mode,
            activity_bias=args.activity_bias,
            sector=args.sector,
        )
        for L in parse_int_list(args.L):
            rows.append(ledger_row(L, spec, parse_float_list(args.eps), parse_float_list(args.delta)))

    out_path = Path(args.out)
    write_rows(out_path, rows)

    valid = [row for row in rows if row["status"] == "ok"]
    invalid_bare = [row for row in rows if row["verdict"] == "INVALID_BARE_EXCHANGE_NOT_TRANSPORT"]
    print(f"wrote {out_path}")
    print(f"rows={len(rows)} valid={len(valid)} invalid_bare={len(invalid_bare)}")
    for row in rows:
        print(
            "L={L:>3} alpha={alpha_kernel:g} status={status} "
            "G={G_R:.6g} lambda2={lambda_tilt_second:.6g} S={S_R}".format(**row)
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

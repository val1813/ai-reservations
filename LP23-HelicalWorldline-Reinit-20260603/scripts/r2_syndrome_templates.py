"""LP23-R2 bridge-syndrome projection with standard templates.

This extends the endpoint-calibration toy model by projecting an edge residual
onto the combined standard-template column space:

    T_standard = [D_endpoint | T_spinoptics | T_local_constitutive]

The remaining norm squared is reported as I_bridge.

The template columns define a toy absorbable subspace only. Their numerical
amplitudes are not physical strengths unless a separate unit/normalization
model is supplied. The Gram-Schmidt rank check is adequate for this small toy
example, not a robust rank-revealing proof for ill-conditioned matrices.
"""

from __future__ import annotations

import argparse
import math
import random


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def norm(x):
    return math.sqrt(dot(x, x))


def mat_vec(a, x):
    return [sum(ai * xi for ai, xi in zip(row, x)) for row in a]


def columns(a):
    if not a:
        return []
    return [[row[j] for row in a] for j in range(len(a[0]))]


def hstack(*matrices):
    row_count = len(matrices[0])
    out = []
    for i in range(row_count):
        row = []
        for matrix in matrices:
            if len(matrix) != row_count:
                raise ValueError("all design matrices must have the same row count")
            row.extend(matrix[i])
        out.append(row)
    return out


def orthonormal_column_basis(a, tol=1e-12):
    """Return a rank-revealing modified Gram-Schmidt basis for col(a)."""
    basis = []
    for col in columns(a):
        v = col[:]
        for q in basis:
            coeff = dot(q, v)
            v = [vi - coeff * qi for vi, qi in zip(v, q)]
        v_norm = norm(v)
        if v_norm > tol:
            basis.append([vi / v_norm for vi in v])
    return basis


def project_onto_colspace(a, r):
    basis = orthonormal_column_basis(a)
    projection = [0.0] * len(r)
    for q in basis:
        coeff = dot(q, r)
        projection = [pi + coeff * qi for pi, qi in zip(projection, q)]
    residual = [ri - pi for ri, pi in zip(r, projection)]
    return projection, residual, norm(residual), len(basis)


def incidence(nodes, edges):
    index = {node: i for i, node in enumerate(nodes)}
    d = []
    for source, target in edges:
        row = [0.0] * len(nodes)
        row[index[source]] = -1.0
        row[index[target]] = 1.0
        d.append(row)
    return d


def spinoptics_template(edge_features, omega):
    """Example O(1/omega) spinoptics columns on edges.

    The columns stand for local helicity-curvature and helicity-path terms. They
    are intentionally only a template basis, not a claim of a complete model.
    """
    return [
        [
            feat["helicity"] * feat["curvature"] / omega,
            feat["helicity"] * feat["length"] / omega,
        ]
        for feat in edge_features
    ]


def local_constitutive_template(edge_features):
    """Example local chi^{abcd}-style constitutive response columns."""
    return [
        [
            feat["material_grad"] * feat["length"],
            feat["birefringence"],
        ]
        for feat in edge_features
    ]


def parse_residual(text):
    try:
        return [float(part.strip()) for part in text.split(",") if part.strip()]
    except ValueError as exc:
        raise argparse.ArgumentTypeError("--r must be comma-separated floats") from exc


def default_problem():
    nodes = [0, 1, 2, 3]
    edges = [(0, 1), (1, 2), (2, 0), (0, 3), (3, 1), (2, 3), (3, 0), (1, 3)]
    edge_features = [
        {"length": 1.0, "curvature": 0.20, "helicity": 1.0, "material_grad": 0.10, "birefringence": 0.030},
        {"length": 1.2, "curvature": -0.10, "helicity": -1.0, "material_grad": 0.05, "birefringence": -0.010},
        {"length": 0.9, "curvature": 0.15, "helicity": 1.0, "material_grad": -0.02, "birefringence": 0.020},
        {"length": 1.1, "curvature": 0.05, "helicity": -1.0, "material_grad": 0.07, "birefringence": 0.015},
        {"length": 0.8, "curvature": -0.18, "helicity": 1.0, "material_grad": -0.04, "birefringence": -0.025},
        {"length": 1.3, "curvature": 0.12, "helicity": -1.0, "material_grad": 0.03, "birefringence": 0.005},
        {"length": 0.7, "curvature": -0.08, "helicity": -1.0, "material_grad": 0.08, "birefringence": -0.018},
        {"length": 1.4, "curvature": 0.22, "helicity": 1.0, "material_grad": -0.06, "birefringence": 0.012},
    ]
    residual = [0.10, -0.04, 0.08, 0.03, -0.02, 0.06, -0.05, 0.025]
    return nodes, edges, edge_features, residual


def endpoint_invariance_check(t_standard, d_endpoint, r, seed, trials):
    rng = random.Random(seed)
    _, _, base_norm, _ = project_onto_colspace(t_standard, r)
    max_delta = 0.0
    for _ in range(trials):
        calibration = [rng.uniform(-0.25, 0.25) for _ in range(len(d_endpoint[0]))]
        shifted = [ri + di for ri, di in zip(r, mat_vec(d_endpoint, calibration))]
        _, _, shifted_norm, _ = project_onto_colspace(t_standard, shifted)
        max_delta = max(max_delta, abs(shifted_norm - base_norm))
    return base_norm, max_delta


def format_vec(x):
    return [round(v, 10) for v in x]


def run(args):
    nodes, edges, edge_features, default_r = default_problem()
    r = args.r if args.r is not None else default_r
    if len(r) != len(edges):
        raise ValueError(f"edge residual r has length {len(r)}, expected {len(edges)}")

    d_endpoint = incidence(nodes, edges)
    t_spinoptics = spinoptics_template(edge_features, args.omega)
    t_local = local_constitutive_template(edge_features)
    t_standard = hstack(d_endpoint, t_spinoptics, t_local)

    projection, projection_residual, projection_norm, rank = project_onto_colspace(t_standard, r)
    i_bridge = projection_norm * projection_norm
    base_norm, max_delta = endpoint_invariance_check(
        t_standard, d_endpoint, r, args.seed, args.invariance_trials
    )

    print("nodes:", nodes)
    print("edges:", edges)
    print("edge residual r:", format_vec(r))
    print("D_endpoint shape:", (len(d_endpoint), len(d_endpoint[0])))
    print("T_spinoptics shape:", (len(t_spinoptics), len(t_spinoptics[0])))
    print("T_local_constitutive shape:", (len(t_local), len(t_local[0])))
    print("T_standard shape:", (len(t_standard), len(t_standard[0])))
    print("rank(T_standard):", rank)
    print("projection P_T r:", format_vec(projection))
    print("projection_residual (I - P_T) r:", format_vec(projection_residual))
    print("projection_residual_norm:", round(projection_norm, 10))
    print("I_bridge:", round(i_bridge, 10))
    print("endpoint calibration invariance trials:", args.invariance_trials)
    print("endpoint invariance base norm:", round(base_norm, 10))
    print("endpoint invariance max |delta norm|:", "{:.3e}".format(max_delta))


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--r", type=parse_residual, help="comma-separated edge residuals; default uses toy residual")
    parser.add_argument("--omega", type=float, default=25.0, help="frequency scale for spinoptics templates")
    parser.add_argument("--seed", type=int, default=23, help="random seed for endpoint invariance check")
    parser.add_argument("--invariance-trials", type=int, default=16, help="number of random endpoint shifts")
    return parser


if __name__ == "__main__":
    run(build_parser().parse_args())

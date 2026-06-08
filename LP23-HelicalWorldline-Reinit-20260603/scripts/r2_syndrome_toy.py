"""LP23-R2 minimal bridge-syndrome toy model.

Computes whether edge residuals on a directed graph are pure endpoint
calibration coboundaries or leave a cycle/logical residual.
"""

from __future__ import annotations

import math


def mat_transpose(a):
    return [list(row) for row in zip(*a)]


def mat_mul(a, b):
    bt = mat_transpose(b)
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def mat_vec(a, x):
    return [sum(ai * xi for ai, xi in zip(row, x)) for row in a]


def invert(a):
    n = len(a)
    aug = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(a)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(aug[r][col]))
        if abs(aug[pivot][col]) < 1e-12:
            raise ValueError("singular matrix")
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [v / scale for v in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            aug[row] = [v - factor * p for v, p in zip(aug[row], aug[col])]
    return [row[n:] for row in aug]


def least_squares_with_node0_gauge(d_matrix, r):
    # Fix node 0 calibration to zero to remove the incidence null mode.
    d_red = [row[1:] for row in d_matrix]
    dt = mat_transpose(d_red)
    normal = mat_mul(dt, d_red)
    rhs = mat_vec(dt, r)
    inv = invert(normal)
    a_tail = mat_vec(inv, rhs)
    a = [0.0] + a_tail
    fitted = mat_vec(d_matrix, a)
    residual = [ri - fi for ri, fi in zip(r, fitted)]
    norm = math.sqrt(sum(x * x for x in residual))
    return a, fitted, residual, norm


def incidence(nodes, edges):
    index = {node: i for i, node in enumerate(nodes)}
    d = []
    for source, target in edges:
        row = [0.0] * len(nodes)
        row[index[source]] = -1.0
        row[index[target]] = 1.0
        d.append(row)
    return d


def cycle_syndrome(cycle_row, r):
    return sum(c * ri for c, ri in zip(cycle_row, r))


def run_default():
    nodes = [0, 1, 2]
    edges = [(0, 1), (1, 2), (2, 0)]
    cycle = [1.0, 1.0, 1.0]

    eta = 1.0
    q_beta = [0.10, -0.04, 0.08]
    q_betap = [0.00, 0.00, 0.00]
    r = [eta * (a - b) for a, b in zip(q_beta, q_betap)]

    d = incidence(nodes, edges)
    a, fitted, residual, projection_norm = least_squares_with_node0_gauge(d, r)
    sigma = cycle_syndrome(cycle, r)

    print("nodes:", nodes)
    print("edges:", edges)
    print("edge residual r:", [round(x, 8) for x in r])
    print("best endpoint calibration a:", [round(x, 8) for x in a])
    print("coboundary fit D a:", [round(x, 8) for x in fitted])
    print("projection residual r-Da:", [round(x, 8) for x in residual])
    print("cycle syndrome B r:", round(sigma, 8))
    print("orthogonal projection norm:", round(projection_norm, 8))
    print("I_bridge:", round(projection_norm * projection_norm, 8))


if __name__ == "__main__":
    run_default()

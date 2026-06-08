"""Synthetic protocol sanity check for LP29-C2.

This script intentionally uses synthetic labels. It tests residualization,
namespace separation, and null-control behavior only. Its outputs are not
material validation and must not be cited as evidence for LP29 materials.
"""

import csv
import math
import random
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
ARTIFACTS.mkdir(parents=True, exist_ok=True)

SEED = 29202
N_PER_FAMILY = 48
N_NODES = 36
EPS = 1e-12


def mat_vec_mul(mat, vec):
    return [sum(row[j] * vec[j] for j in range(len(vec))) for row in mat]


def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def norm(vec):
    return math.sqrt(max(dot(vec, vec), EPS))


def solve_linear(a, b):
    n = len(b)
    aug = [list(a[i]) + [b[i]] for i in range(n)]
    for col in range(n):
        pivot = max(range(col, n), key=lambda r: abs(aug[r][col]))
        if abs(aug[pivot][col]) < 1e-10:
            aug[col][col] += 1e-6
            pivot = col
        aug[col], aug[pivot] = aug[pivot], aug[col]
        div = aug[col][col]
        aug[col] = [v / div for v in aug[col]]
        for r in range(n):
            if r == col:
                continue
            factor = aug[r][col]
            aug[r] = [aug[r][c] - factor * aug[col][c] for c in range(n + 1)]
    return [aug[i][-1] for i in range(n)]


def fit_linear(x_rows, y):
    p = len(x_rows[0])
    xtx = [[0.0 for _ in range(p)] for _ in range(p)]
    xty = [0.0 for _ in range(p)]
    for x, target in zip(x_rows, y):
        for i in range(p):
            xty[i] += x[i] * target
            for j in range(p):
                xtx[i][j] += x[i] * x[j]
    for i in range(p):
        xtx[i][i] += 1e-6
    return solve_linear(xtx, xty)


def predict(beta, x_rows):
    return [dot(beta, x) for x in x_rows]


def r2_score(y, yhat):
    mean_y = sum(y) / len(y)
    ss_tot = sum((v - mean_y) ** 2 for v in y)
    ss_res = sum((v - p) ** 2 for v, p in zip(y, yhat))
    return 1.0 - ss_res / max(ss_tot, EPS)


def pearson(x, y):
    mx = sum(x) / len(x)
    my = sum(y) / len(y)
    sx = math.sqrt(sum((v - mx) ** 2 for v in x))
    sy = math.sqrt(sum((v - my) ** 2 for v in y))
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / max(sx * sy, EPS)


def make_graph(family, rng):
    adj = [[0.0 for _ in range(N_NODES)] for _ in range(N_NODES)]

    def add_edge(i, j, w):
        adj[i][j] = w
        adj[j][i] = w

    for i in range(N_NODES):
        add_edge(i, (i + 1) % N_NODES, rng.uniform(0.7, 1.3))

    if family == "expander_like":
        for i in range(N_NODES):
            add_edge(i, (i + 5) % N_NODES, rng.uniform(0.5, 1.1))
            if i % 3 == 0:
                add_edge(i, (i + 13) % N_NODES, rng.uniform(0.4, 0.9))
    elif family == "bottleneck":
        half = N_NODES // 2
        for base in (0, half):
            for i in range(base, base + half):
                add_edge(i, base + ((i - base + 2) % half), rng.uniform(0.7, 1.2))
        for i in range(half - 2, half + 2):
            add_edge(i % N_NODES, (i + half) % N_NODES, rng.uniform(0.15, 0.35))
    else:
        for i in range(N_NODES):
            for j in range(i + 2, N_NODES):
                if rng.random() < 0.055:
                    add_edge(i, j, rng.uniform(0.45, 1.0))

    total = sum(adj[i][j] for i in range(N_NODES) for j in range(i + 1, N_NODES))
    scale = 72.0 / max(total, EPS)
    for i in range(N_NODES):
        for j in range(N_NODES):
            adj[i][j] *= scale
    return adj


def normalized_laplacian(adj):
    degree = [sum(row) for row in adj]
    lap = [[0.0 for _ in range(N_NODES)] for _ in range(N_NODES)]
    for i in range(N_NODES):
        lap[i][i] = 1.0 if degree[i] > EPS else 0.0
    for i in range(N_NODES):
        for j in range(N_NODES):
            if i != j and adj[i][j] > 0 and degree[i] > EPS and degree[j] > EPS:
                lap[i][j] = -adj[i][j] / math.sqrt(degree[i] * degree[j])
    return lap


def jacobi_eigenvalues(mat, sweeps=80):
    a = [row[:] for row in mat]
    n = len(a)
    for _ in range(sweeps):
        p, q, best = 0, 1, 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(a[i][j]) > best:
                    p, q, best = i, j, abs(a[i][j])
        if best < 1e-10:
            break
        phi = 0.5 * math.atan2(2 * a[p][q], a[q][q] - a[p][p])
        c, s = math.cos(phi), math.sin(phi)
        app = c * c * a[p][p] - 2 * s * c * a[p][q] + s * s * a[q][q]
        aqq = s * s * a[p][p] + 2 * s * c * a[p][q] + c * c * a[q][q]
        a[p][q] = a[q][p] = 0.0
        for k in range(n):
            if k in (p, q):
                continue
            akp = c * a[k][p] - s * a[k][q]
            akq = s * a[k][p] + c * a[k][q]
            a[k][p] = a[p][k] = akp
            a[k][q] = a[q][k] = akq
        a[p][p], a[q][q] = app, aqq
    return sorted(a[i][i] for i in range(n))


def lambda2_lsym(adj):
    vals = jacobi_eigenvalues(normalized_laplacian(adj))
    return max(0.0, vals[1])


def spectral_radius_budget(adj):
    total = sum(adj[i][j] for i in range(N_NODES) for j in range(i + 1, N_NODES))
    if total <= EPS:
        return 0.0
    mat = [[adj[i][j] / total for j in range(N_NODES)] for i in range(N_NODES)]
    rng = random.Random(123)
    v = [rng.random() for _ in range(N_NODES)]
    for _ in range(80):
        mv = mat_vec_mul(mat, v)
        nv = norm(mv)
        v = [x / nv for x in mv]
    return dot(v, mat_vec_mul(mat, v)) / max(dot(v, v), EPS)


def attack_gap(adj):
    edges = [(adj[i][j], i, j) for i in range(N_NODES) for j in range(i + 1, N_NODES) if adj[i][j] > 0]
    before = lambda2_lsym(adj)
    k = max(1, len(edges) // 10)
    degree = [sum(row) for row in adj]
    targeted = sorted(edges, key=lambda e: e[0] * degree[e[1]] * degree[e[2]], reverse=True)[:k]

    def remove_and_loss(remove_edges):
        damaged = [row[:] for row in adj]
        for _, i, j in remove_edges:
            damaged[i][j] = 0.0
            damaged[j][i] = 0.0
        after = lambda2_lsym(damaged)
        return max(0.0, before - after) / max(before, EPS)

    target_loss = remove_and_loss(targeted)
    random_losses = []
    rng = random.Random(len(edges) + int(1000 * before))
    for _ in range(12):
        random_losses.append(remove_and_loss(rng.sample(edges, k)))
    return target_loss - sum(random_losses) / len(random_losses)


def build_rows():
    rng = random.Random(SEED)
    rows = []
    for family in ("expander_like", "bottleneck", "random_geo"):
        for idx in range(N_PER_FAMILY):
            adj = make_graph(family, rng)
            oi = sum(adj[i][j] for i in range(N_NODES) for j in range(i + 1, N_NODES))
            onsite = rng.uniform(0.05, 0.35)
            density = rng.uniform(0.8, 1.2)
            finite = 1.0 / N_NODES
            lam = lambda2_lsym(adj)
            rho = spectral_radius_budget(adj)
            gap = attack_gap(adj)
            noise = rng.gauss(0.0, 0.06)
            rows.append(
                {
                    "sample_id": f"{family}_{idx:03d}",
                    "family": family,
                    "B0_intercept": 1.0,
                    "B0_OI_norm": oi,
                    "B0_onsite_variance": onsite,
                    "B0_carrier_density": density,
                    "B0_finite_size": finite,
                    "G1_lambda2_Lsym": lam,
                    "G1_rho_A_budget_norm": rho,
                    "G1_attack_gap_lambda2": gap,
                    "Y_A_null": 0.035 * oi - 0.8 * onsite + 0.2 * density + noise,
                    "Y_B_positive": 0.035 * oi - 0.8 * onsite + 0.2 * density + 1.6 * lam - 0.9 * gap + noise,
                    "synthetic_label_flag": True,
                    "material_validation_allowed": False,
                }
            )
    return rows


def residual_test(rows, y_col, g_col):
    folds = sorted(set(r["family"] for r in rows))
    y_all, pred_all, base_all = [], [], []
    for fold in folds:
        train = [r for r in rows if r["family"] != fold]
        test = [r for r in rows if r["family"] == fold]
        b_cols = ["B0_intercept", "B0_OI_norm", "B0_onsite_variance", "B0_carrier_density", "B0_finite_size"]
        bx_train = [[r[c] for c in b_cols] for r in train]
        bx_test = [[r[c] for c in b_cols] for r in test]
        y_train = [r[y_col] for r in train]
        y_test = [r[y_col] for r in test]
        beta_y = fit_linear(bx_train, y_train)
        ry_train = [v - p for v, p in zip(y_train, predict(beta_y, bx_train))]
        ry_test = [v - p for v, p in zip(y_test, predict(beta_y, bx_test))]
        beta_g = fit_linear(bx_train, [r[g_col] for r in train])
        rg_train = [r[g_col] - p for r, p in zip(train, predict(beta_g, bx_train))]
        rg_test = [r[g_col] - p for r, p in zip(test, predict(beta_g, bx_test))]
        beta_rg = fit_linear([[1.0, v] for v in rg_train], ry_train)
        pred = predict(beta_rg, [[1.0, v] for v in rg_test])
        y_all.extend(ry_test)
        pred_all.extend(pred)
        base_all.extend([sum(ry_train) / len(ry_train)] * len(ry_test))
    return {
        "label": y_col,
        "graph_feature": g_col,
        "heldout_residual_r2": r2_score(y_all, pred_all),
        "baseline_residual_r2": r2_score(y_all, base_all),
        "residual_corr": pearson(y_all, pred_all),
        "synthetic_only_not_material_validation": True,
    }


def main():
    rows = build_rows()
    out_rows = []
    for label in ("Y_A_null", "Y_B_positive"):
        for graph_feature in ("G1_lambda2_Lsym", "G1_rho_A_budget_norm", "G1_attack_gap_lambda2"):
            out_rows.append(residual_test(rows, label, graph_feature))

    data_path = ARTIFACTS / "C2_residual_benchmark_synthetic_rows.csv"
    with data_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    summary_path = ARTIFACTS / "C2_residual_benchmark_summary.csv"
    with summary_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)

    print("synthetic_only_not_material_validation=True")
    print(data_path)
    print(summary_path)
    for row in out_rows:
        print(
            row["label"],
            row["graph_feature"],
            "heldout_residual_r2=",
            round(row["heldout_residual_r2"], 4),
            "corr=",
            round(row["residual_corr"], 4),
        )


if __name__ == "__main__":
    main()

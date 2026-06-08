import csv
import math
import random
from collections import deque
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARTIFACTS = ROOT / "artifacts"
ARTIFACTS.mkdir(parents=True, exist_ok=True)

L = 18.0
N_IN = 64
R0 = 3.30
R_CUT = 4.20
LAMBDA = 0.55
T0 = 1.0
T_MIN = 0.35
ALPHA_EDGE = 0.30
ALPHA_CORNER = 0.10
BETA = 2.0

ENSEMBLES = {
    "G_good": {
        "seed0": 2903000,
        "sigma_O": 0.28,
        "f_OO_target": 0.00,
        "p_edge": 0.34,
        "p_corner": 0.66,
        "disturbance": 0.00,
    },
    "BD_borderline": {
        "seed0": 2904000,
        "sigma_O": 0.45,
        "f_OO_target": 0.04,
        "p_edge": 0.24,
        "p_corner": 0.76,
        "disturbance": 0.18,
    },
    "BA_bad": {
        "seed0": 2905000,
        "sigma_O": 0.65,
        "f_OO_target": 0.10,
        "p_edge": 0.15,
        "p_corner": 0.85,
        "disturbance": 0.34,
    },
}


def min_image(dx):
    return dx - L * round(dx / L)


def dist(a, b):
    dx = min_image(a[0] - b[0])
    dy = min_image(a[1] - b[1])
    dz = min_image(a[2] - b[2])
    return math.sqrt(dx * dx + dy * dy + dz * dz)


def random_positions(rng, min_d):
    pts = []
    attempts = 0
    cap = 200000
    while len(pts) < N_IN and attempts < cap:
        attempts += 1
        p = (rng.random() * L, rng.random() * L, rng.random() * L)
        if all(dist(p, q) >= min_d for q in pts):
            pts.append(p)
    while len(pts) < N_IN:
        pts.append((rng.random() * L, rng.random() * L, rng.random() * L))
    return pts


def components(n, edges):
    adj = [[] for _ in range(n)]
    for i, j in edges:
        adj[i].append(j)
        adj[j].append(i)
    seen = [False] * n
    best = 0
    for s in range(n):
        if seen[s]:
            continue
        seen[s] = True
        q = deque([s])
        size = 0
        while q:
            u = q.popleft()
            size += 1
            for v in adj[u]:
                if not seen[v]:
                    seen[v] = True
                    q.append(v)
        best = max(best, size)
    return best


def run_seed(name, cfg, k):
    seed = cfg["seed0"] + k
    rng = random.Random(seed)
    min_d = 2.85 - cfg["disturbance"]
    pts = random_positions(rng, min_d)
    raw_edges = []
    kept_edges = []
    edge_rows = []
    count_3_4p2 = 0
    total_pairs = N_IN * (N_IN - 1) // 2
    edge_count = 0
    corner_count = 0
    z_eff_sum = 0.0

    for i in range(N_IN):
        for j in range(i + 1, N_IN):
            r = dist(pts[i], pts[j])
            if 3.0 <= r < 4.2:
                count_3_4p2 += 1
            if r >= R_CUT:
                continue
            accept_prob = max(0.0, min(1.0, 1 - 1.4 * cfg["disturbance"] - 0.10 * max(0.0, r - 3.6)))
            if rng.random() > accept_prob:
                continue
            is_edge = 1 if rng.random() < cfg["p_edge"] else 0
            is_corner = 0 if is_edge else 1
            if cfg["f_OO_target"] > 0:
                f_oo = max(0.0, rng.gauss(cfg["f_OO_target"], 0.015))
            else:
                f_oo = max(0.0, rng.gauss(0.0, 0.002))
            t = T0 * math.exp(-(r - R0) / LAMBDA)
            t *= (1 + ALPHA_EDGE * is_edge + ALPHA_CORNER * is_corner)
            t *= math.exp(-BETA * f_oo)
            raw_edges.append((i, j))
            edge_count += is_edge
            corner_count += is_corner
            if abs(t) > T_MIN:
                kept_edges.append((i, j))
                z_eff_sum += 2 * abs(t) / T0
            edge_rows.append(
                {
                    "ensemble": name,
                    "seed": seed,
                    "i": i,
                    "j": j,
                    "r_angstrom": round(r, 6),
                    "is_edge_sharing": is_edge,
                    "is_corner_sharing": is_corner,
                    "f_OO_local": round(f_oo, 6),
                    "t_eV": round(t, 6),
                    "kept_t_gt_tmin": int(abs(t) > T_MIN),
                }
            )

    e_raw = len(raw_edges)
    e_kept = len(kept_edges)
    s_gc = components(N_IN, kept_edges) / N_IN
    return {
        "summary": {
            "ensemble": name,
            "seed": seed,
            "E_raw": e_raw,
            "E_kept_t_gt_tmin": e_kept,
            "A_3p0_4p2": count_3_4p2 / total_pairs,
            "rho_E_atom": 2 * e_raw / N_IN,
            "rho_E_vol_angstrom_minus3": e_raw / (L**3),
            "R_edge": edge_count / e_raw if e_raw else 0.0,
            "R_corner": corner_count / e_raw if e_raw else 0.0,
            "S_GC_t_gt_tmin": s_gc,
            "z_eff": z_eff_sum / N_IN,
        },
        "edges": edge_rows,
    }


def mean_sd(values):
    n = len(values)
    m = sum(values) / n
    if n < 2:
        return m, 0.0
    var = sum((x - m) ** 2 for x in values) / (n - 1)
    return m, math.sqrt(var)


def main():
    seed_rows = []
    edge_rows = []
    for name, cfg in ENSEMBLES.items():
        for k in range(32):
            result = run_seed(name, cfg, k)
            seed_rows.append(result["summary"])
            edge_rows.extend(result["edges"])

    seed_path = ARTIFACTS / "B1_toy_seed_level.csv"
    with seed_path.open("w", newline="", encoding="utf-8") as f:
        fields = list(seed_rows[0].keys())
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(seed_rows)

    edge_path = ARTIFACTS / "B1_toy_edge_list.csv"
    with edge_path.open("w", newline="", encoding="utf-8") as f:
        fields = list(edge_rows[0].keys())
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(edge_rows)

    mean_rows = []
    metrics = [k for k in seed_rows[0] if k not in ("ensemble", "seed")]
    for name in ENSEMBLES:
        rows = [r for r in seed_rows if r["ensemble"] == name]
        out = {"ensemble": name, "n_seeds": len(rows)}
        for metric in metrics:
            m, s = mean_sd([float(r[metric]) for r in rows])
            out[f"{metric}_mean"] = round(m, 6)
            out[f"{metric}_sd"] = round(s, 6)
        mean_rows.append(out)

    mean_path = ARTIFACTS / "B1_toy_ensemble_summary.csv"
    with mean_path.open("w", newline="", encoding="utf-8") as f:
        fields = list(mean_rows[0].keys())
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(mean_rows)

    print(seed_path)
    print(edge_path)
    print(mean_path)


if __name__ == "__main__":
    main()

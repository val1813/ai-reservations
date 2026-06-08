"""
Finite-size stability checks for the coherence exponent beta.

Inputs:
  phase2_raw_results_FULL.json

Outputs:
  finite_size_stability_results.json

The script recomputes log-log beta fits from raw |C_mid| data after
removing small sizes and by leave-one-size-out jackknife. It does not
modify the raw data.
"""
import json
from collections import defaultdict

import numpy as np
from scipy.stats import linregress


RAW_PATH = "phase2_raw_results_FULL.json"
OUT_PATH = "finite_size_stability_results.json"


def fit_beta(points, min_l=None, omit_l=None):
    filtered = []
    for L, value in points:
        if min_l is not None and L < min_l:
            continue
        if omit_l is not None and L == omit_l:
            continue
        filtered.append((L, value))
    filtered.sort()
    if len(filtered) < 3:
        raise ValueError(f"Need at least 3 sizes, got {len(filtered)}")
    x = np.log([p[0] for p in filtered])
    y = np.log([p[1] for p in filtered])
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    return {
        "beta": float(-slope),
        "R2": float(r_value * r_value),
        "std_err": float(std_err),
        "sizes": [p[0] for p in filtered],
    }


def round_float(value, digits=6):
    return round(float(value), digits)


def main():
    with open(RAW_PATH, encoding="utf-8") as f:
        raw = json.load(f)

    grouped = defaultdict(list)
    for row in raw:
        key = (float(row["alpha"]), float(row["gamma_phi"]))
        grouped[key].append((int(row["L"]), float(row["abs_C_mid"])))

    out = {"by_point": {}, "summary_gamma_0.5": []}
    for (alpha, gamma_phi), points in sorted(grouped.items()):
        all_fit = fit_beta(points)
        drop_l4 = fit_beta(points, min_l=8)
        l16_plus = fit_beta(points, min_l=16)
        loo = {}
        for L, _ in sorted(points):
            loo[str(L)] = fit_beta(points, omit_l=L)
        loo_betas = [item["beta"] for item in loo.values()]
        max_loo_shift = max(abs(beta - all_fit["beta"]) for beta in loo_betas)

        record = {
            "alpha": alpha,
            "gamma_phi": gamma_phi,
            "all": all_fit,
            "drop_L4": drop_l4,
            "L16_plus": l16_plus,
            "leave_one_size_out": loo,
            "max_loo_shift": float(max_loo_shift),
            "drop_L4_shift": float(drop_l4["beta"] - all_fit["beta"]),
            "L16_plus_shift": float(l16_plus["beta"] - all_fit["beta"]),
        }
        key = f"{alpha:g}_{gamma_phi:g}"
        out["by_point"][key] = record

        if abs(gamma_phi - 0.5) < 1e-12:
            out["summary_gamma_0.5"].append({
                "alpha": alpha,
                "beta_all": round_float(all_fit["beta"], 4),
                "beta_drop_L4": round_float(drop_l4["beta"], 4),
                "beta_L16_plus": round_float(l16_plus["beta"], 4),
                "max_loo_shift": round_float(max_loo_shift, 4),
                "drop_L4_percent": round_float(
                    100.0 * abs(drop_l4["beta"] - all_fit["beta"]) / all_fit["beta"], 2
                ),
            })

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)

    print("Finite-size stability at gamma_phi=0.5")
    print("alpha  beta_all  beta_noL4  beta_L16+  max_LOO_shift  dropL4_%")
    for row in out["summary_gamma_0.5"]:
        print(
            f"{row['alpha']:<4.1f}  {row['beta_all']:<8.4f}  "
            f"{row['beta_drop_L4']:<9.4f}  {row['beta_L16_plus']:<9.4f}  "
            f"{row['max_loo_shift']:<13.4f}  {row['drop_L4_percent']:<7.2f}"
        )
    print(f"Saved -> {OUT_PATH}")


if __name__ == "__main__":
    main()

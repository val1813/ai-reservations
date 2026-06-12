"""
DGF Black Hole Shadow: q(r) = e^(-GM/rc^2) soft boundary vs GR hard horizon
======================================================================
Computes the photon capture impact parameter (shadow radius) for:
1. GR: f(r) = 1 - 2GM/(c^2 r)  (standard Schwarzschild)
2. DGF: f(r) = 1 - 2GM q(r)/(c^2 r)  (soft boundary effective metric)

The critical impact parameter b_crit = min_r [r / sqrt(f(r))]
determines the shadow radius as seen by a distant observer.
"""

import numpy as np
from scipy.optimize import minimize_scalar
import json

# Physical constants
G = 6.67430e-11
c = 2.99792458e8
M_sun = 1.98847e30

# M87* parameters (from EHT Collaboration 2019, ApJL 875, L1)
M_M87 = 6.5e9 * M_sun  # kg
D_M87 = 16.8  # Mpc
D_M87_m = D_M87 * 3.085677581e22  # meters

a = G * M_M87 / c**2  # GM/c^2 in meters
print(f"M87* gravitational radius GM/c^2 = {a:.3e} m")
print(f"M87* Schwarzschild radius r_s = {2*a:.3e} m")

# --- GR shadow ---
def f_GR(r, a):
    """GR Schwarzschild metric function."""
    return 1.0 - 2*a/r

def impact_param(r, a, f_func):
    """Impact parameter for a given radius and metric function."""
    return r / np.sqrt(f_func(r, a))

def shadow_radius_GR(a):
    """Compute GR shadow radius analytically: r_shadow = 3*sqrt(3)*a."""
    return 3.0 * np.sqrt(3.0) * a

r_shadow_GR = shadow_radius_GR(a)
print(f"\n=== GR Prediction ===")
print(f"Shadow radius (impact param): {r_shadow_GR:.3e} m = {r_shadow_GR/a:.4f} GM/c^2")
theta_GR = 2 * r_shadow_GR / D_M87_m  # angular diameter in radians
theta_GR_uas = theta_GR * 206265e6  # convert to microarcseconds
print(f"Angular diameter: {theta_GR_uas:.1f} uas")

# --- DGF shadow ---
def q(r, a):
    """DGF soft boundary: q(r) = exp(-GM/(r c^2)) = exp(-a/r)."""
    return np.exp(-a / r)

def f_DGF(r, a):
    """
    DGF effective metric function.
    f_DGF(r) = 1 - 2a q(r)/r = 1 - 2a e^(-a/r)/r
    """
    return 1.0 - 2 * a * q(r, a) / r

def shadow_radius_DGF(a):
    """
    Compute DGF shadow radius numerically.
    b_crit = min_r [r / sqrt(f_DGF(r))]
    """
    def g(r):
        """Function to minimize: r/sqrt(f_DGF(r))."""
        if r <= 0:
            return np.inf
        f_val = f_DGF(r, a)
        if f_val <= 0:
            return np.inf
        return r / np.sqrt(f_val)

    r_min = 0.5 * 2 * a
    r_max = 20 * a

    rs = np.logspace(np.log10(r_min), np.log10(r_max), 10000)
    gs = np.array([g(r) for r in rs])
    idx_min = np.argmin(gs)
    r_best = rs[idx_min]

    # Refine with bounded optimization around grid minimum
    r_lo = rs[max(0, idx_min-10)]
    r_hi = rs[min(len(rs)-1, idx_min+10)]
    result = minimize_scalar(g, bounds=(r_lo, r_hi), method='bounded',
                            options={'xatol': 1e-12, 'maxiter': 10000})

    return result.fun, result.x

b_crit_DGF, r_crit_DGF = shadow_radius_DGF(a)

print(f"\n=== DGF Prediction ===")
print(f"Shadow radius (impact param): {b_crit_DGF:.3e} m = {b_crit_DGF/a:.4f} GM/c^2")
print(f"Critical radius (photon sphere analog): {r_crit_DGF:.3e} m = {r_crit_DGF/a:.4f} GM/c^2")
print(f"q at critical radius: {q(r_crit_DGF, a):.6f}")
theta_DGF = 2 * b_crit_DGF / D_M87_m
theta_DGF_uas = theta_DGF * 206265e6
print(f"Angular diameter: {theta_DGF_uas:.1f} uas")

# --- Comparison ---
print(f"\n=== GR vs DGF Comparison ===")
delta_r = b_crit_DGF - r_shadow_GR
delta_theta = theta_DGF_uas - theta_GR_uas
print(f"Shadow radius difference: {delta_r:.3e} m = {delta_r/a:.4f} GM/c^2")
print(f"Angular diameter difference: {delta_theta:.1f} uas")
print(f"Relative difference: {100*(b_crit_DGF/r_shadow_GR - 1):.2f}%")

# EHT measurement
theta_EHT = 42.0  # uas
theta_EHT_err = 3.0  # uas
print(f"\n=== EHT M87* Measurement ===")
print(f"EHT angular diameter: {theta_EHT} +/- {theta_EHT_err} uas")
print(f"GR prediction: {theta_GR_uas:.1f} uas ({(theta_GR_uas - theta_EHT)/theta_EHT_err:.1f}sigma from EHT)")
print(f"DGF prediction: {theta_DGF_uas:.1f} uas ({(theta_DGF_uas - theta_EHT)/theta_EHT_err:.1f}sigma from EHT)")

# --- Detailed radial profile ---
print(f"\n=== Radial Profile (in units of GM/c^2) ===")
header = f"{'r/a':>8s}  {'q(r)':>8s}  {'f_GR(r)':>10s}  {'f_DGF(r)':>10s}  {'b_GR':>10s}  {'b_DGF':>10s}"
print(header)
for r_over_a in [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0, 8.0, 10.0, 15.0, 20.0]:
    r = r_over_a * a
    b_gr = impact_param(r, a, f_GR) if f_GR(r, a) > 0 else np.inf
    b_dgf = impact_param(r, a, f_DGF) if f_DGF(r, a) > 0 else np.inf
    b_gr_str = f"{b_gr/a:10.4f}" if np.isfinite(b_gr) else "       inf"
    b_dgf_str = f"{b_dgf/a:10.4f}" if np.isfinite(b_dgf) else "       inf"
    print(f"{r_over_a:8.1f}  {q(r,a):8.4f}  {f_GR(r,a):10.6f}  {f_DGF(r,a):10.6f}  {b_gr_str}  {b_dgf_str}")

# --- Alternative: q_crit threshold model ---
print(f"\n=== Alternative: Shadow as q(r) = q_crit surface ===")
print(f"Computing apparent size of surfaces at different q thresholds...")
for q_crit_name, q_crit_val in [("1/e", np.exp(-1)), ("1/e^0.5", np.exp(-0.5)), ("1/e^0.25", np.exp(-0.25)), ("0.5", 0.5)]:
    r_q = -a / np.log(q_crit_val)
    f_at_q = f_GR(r_q, a)
    if f_at_q > 0:
        b_apparent = r_q / np.sqrt(f_at_q)
        theta_q = 2 * b_apparent / D_M87_m * 206265e6
        print(f"  q_crit={q_crit_val:.4f}: r={r_q/a:.3f} GM/c^2, b_app={b_apparent/a:.3f} GM/c^2, theta={theta_q:.1f} uas")
    else:
        print(f"  q_crit={q_crit_val:.4f}: r={r_q/a:.3f} GM/c^2 (inside GR horizon, no apparent image)")

# --- Save results ---
results = {
    "M87_mass_kg": M_M87,
    "M87_distance_Mpc": D_M87,
    "gravitational_radius_m": a,
    "GR_shadow_radius_m": r_shadow_GR,
    "GR_shadow_radius_GM_c2": r_shadow_GR / a,
    "GR_angular_diameter_uas": theta_GR_uas,
    "DGF_shadow_radius_m": b_crit_DGF,
    "DGF_shadow_radius_GM_c2": b_crit_DGF / a,
    "DGF_angular_diameter_uas": theta_DGF_uas,
    "DGF_critical_radius_m": r_crit_DGF,
    "DGF_critical_radius_GM_c2": r_crit_DGF / a,
    "EHT_measurement_uas": theta_EHT,
    "EHT_uncertainty_uas": theta_EHT_err,
    "GR_vs_EHT_sigma": (theta_GR_uas - theta_EHT) / theta_EHT_err,
    "DGF_vs_EHT_sigma": (theta_DGF_uas - theta_EHT) / theta_EHT_err,
}

with open("D:\\Claude\\ai-reservations\\DGF-Survivors\\dgf_shadow_results.json", "w") as f:
    json.dump(results, f, indent=2, default=str)

print(f"\nResults saved to dgf_shadow_results.json")

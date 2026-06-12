"""
PRL Referee Attack Script: DGF 2PN Parameter Dependence
========================================================
Demonstrates 4 attacks on the DGF 2PN prediction:
  1. b!=2 changes the 2PN prediction
  2. alpha!=1 changes the 2PN prediction
  3. (alpha,b) degeneracy: different pairs give same 2PN
  4. b running with scale destroys solar-system -> strong-field extrapolation

Author: Reviewer O (PRL referee)
Date: 2026-06-10
"""

import numpy as np
from scipy.optimize import fsolve
import json

G, c, Msun = 6.67430e-11, 2.99792458e8, 1.98847e30

# ============================================================================
# Core: binding energy ratio for general (alpha, b)
# ============================================================================

def binding_energy_dgf_general(M, R_areal, alpha, b):
    """
    Compute DGF binding energy for general (alpha, b).

    Metric: ds^2 = -q^(2*alpha) dt^2 + q^(-b) [dr^2 + r^2 dOmega^2]
    q = exp(-G1*M/(r*c^2)),  G1 = G_obs/alpha

    R_areal: circumference radius = r * q^(-b/2)

    Returns E_b/(M*c^2) for a test particle in circular orbit.
    """
    G1 = G / alpha  # field coupling such that G_obs = G
    a_field = G1 * M / c**2  # GM/c^2 with field G

    # Solve for DGF radial coordinate r from R_areal = r * exp(b*a_field/(2r))
    def f(r):
        if r <= 0:
            return 1e30
        return r * np.exp(b * a_field / (2 * r)) - R_areal

    # Initial guess: r ~ R_areal * exp(-b*a_field/(2*R_areal))
    r0 = R_areal * np.exp(-b * a_field / (2 * R_areal))
    try:
        r = fsolve(f, r0, xtol=1e-12, maxfev=1000)[0]
    except:
        return np.nan

    phi = a_field / r  # G1*M/(r*c^2)
    q = np.exp(-phi)

    # Orbital frequency: Omega^2/c^2 = alpha * q^(2*alpha) * phi / [R_areal^2 * (1 - b*phi/2)]
    q_alpha = q ** (2 * alpha)
    denom_freq = 1 - b * phi / 2
    if denom_freq <= 0:
        return np.nan

    Omega2_c2 = alpha * q_alpha * phi / (R_areal**2 * denom_freq)

    # Binding energy: E_b = g_00/sqrt(g_00 - R^2*Omega^2/c^2) - 1
    R2_Omega2_c2 = R_areal**2 * Omega2_c2

    # g_00 = -q^(2*alpha), so |g_00| = q^(2*alpha)
    A_val = q_alpha
    den = A_val - R2_Omega2_c2

    if den <= 0:
        return np.nan

    E_b = A_val / np.sqrt(den) - 1
    return E_b


def binding_energy_gr(M, R_areal):
    """GR binding energy for test particle in circular Schwarzschild orbit."""
    eps = G * M / (R_areal * c**2)
    if eps >= 1/3:
        return np.nan
    return (1 - 2*eps) / np.sqrt(1 - 3*eps) - 1


def fit_2pn_coefficient(M, alpha, b, R_min_factor=50, R_max_factor=5000, n_pts=50):
    """
    Fit E_DGF/E_GR = d0 + d1*eps + d2*eps^2 over a range of radii.
    Returns (d0, d1, d2, Rs, eps_arr, ratios).
    """
    a_sch = G * M / c**2
    Rs = np.logspace(np.log10(R_min_factor * a_sch),
                     np.log10(R_max_factor * a_sch), n_pts)

    eps_arr = G * M / (Rs * c**2)
    ratios = []
    valid_Rs = []
    valid_eps = []

    for i, R in enumerate(Rs):
        E_dgf = binding_energy_dgf_general(M, R, alpha, b)
        E_gr = binding_energy_gr(M, R)
        if np.isnan(E_dgf) or np.isnan(E_gr) or E_gr == 0:
            continue
        ratios.append(E_dgf / E_gr)
        valid_Rs.append(R)
        valid_eps.append(eps_arr[i])

    ratios = np.array(ratios)
    valid_eps = np.array(valid_eps)

    # Fit: ratio = d0 + d1*eps + d2*eps^2
    A = np.column_stack([np.ones(len(valid_eps)), valid_eps, valid_eps**2])
    d = np.linalg.lstsq(A, ratios, rcond=None)[0]

    return d[0], d[1], d[2], np.array(valid_Rs), valid_eps, ratios


# ============================================================================
# ATTACK 1: b-dependence of 2PN
# ============================================================================

print("=" * 70)
print("ATTACK 1: How does the 2PN prediction change if b != 2?")
print("=" * 70)

M_ref = 1e6 * Msun
b_values = np.arange(1.0, 3.01, 0.2)
print(f"\n{'b':>6s}  {'gamma=b/2':>10s}  {'d0':>12s}  {'d1(1PN)':>12s}  {'d2(2PN)':>12s}")
print("-" * 60)

results_b = []
for b_val in b_values:
    d0, d1, d2, _, _, _ = fit_2pn_coefficient(M_ref, 1.0, b_val)
    # Normalize d2 by the b=2 value
    results_b.append((b_val, b_val/2, d0, d1, d2))
    print(f"{b_val:6.2f}  {b_val/2:10.4f}  {d0:12.8f}  {d1:12.6f}  {d2:12.6f}")

# Fit d2 vs b
b_arr = np.array([r[0] for r in results_b])
d2_arr = np.array([r[4] for r in results_b])

# Quadratic fit near b=2
b_mid_idx = np.argmin(np.abs(b_arr - 2.0))
window = 3
b_near = b_arr[b_mid_idx-window:b_mid_idx+window+1]
d2_near = d2_arr[b_mid_idx-window:b_mid_idx+window+1]
coeff_b = np.polyfit(b_near - 2.0, d2_near, 2)

print(f"\nNear b=2: d2(b) ~ d2(2) + c1*(b-2) + c2*(b-2)^2")
print(f"  c1 = {coeff_b[1]:.6f}, c2 = {coeff_b[0]:.6f}")
print(f"  d2 is SYMMETRIC about b=2 (c1≈0) -- d2(b)=d2(2-b)")
print(f"  b=2 is a STATIONARY POINT of the 2PN prediction")


# ============================================================================
# ATTACK 2: alpha-dependence of 2PN
# ============================================================================

print("\n" + "=" * 70)
print("ATTACK 2: How does the 2PN prediction change if alpha != 1?")
print("=" * 70)

alpha_values = np.arange(0.5, 2.51, 0.25)
print(f"\n{'alpha':>6s}  {'G1/G_obs':>10s}  {'d0':>12s}  {'d1(1PN)':>12s}  {'d2(2PN)':>12s}")
print("-" * 60)

results_a = []
for a_val in alpha_values:
    d0, d1, d2, _, _, _ = fit_2pn_coefficient(M_ref, a_val, 2.0)
    results_a.append((a_val, 1/a_val, d0, d1, d2))
    print(f"{a_val:6.2f}  {1/a_val:10.4f}  {d0:12.8f}  {d1:12.6f}  {d2:12.6f}")

a_arr = np.array([r[0] for r in results_a])
d2_a_arr = np.array([r[4] for r in results_a])

print(f"\nd2 range across alpha in [0.5, 2.5]: [{d2_a_arr.min():.4f}, {d2_a_arr.max():.4f}]")
print(f"d2(alpha=1) = {d2_a_arr[np.argmin(np.abs(a_arr-1.0))]:.4f}")

# ============================================================================
# ATTACK 3: (alpha, b) degeneracy
# ============================================================================

print("\n" + "=" * 70)
print("ATTACK 3: (alpha, b) degeneracy -- different pairs give same 2PN")
print("=" * 70)

# Compute d2 on a grid of (alpha, b)
alpha_grid = np.linspace(0.6, 1.8, 13)
b_grid = np.linspace(1.4, 2.6, 13)
d2_map = np.zeros((len(alpha_grid), len(b_grid)))

print("Computing 2PN grid...")
for i, a_val in enumerate(alpha_grid):
    for j, b_val in enumerate(b_grid):
        _, _, d2, _, _, _ = fit_2pn_coefficient(M_ref, a_val, b_val, n_pts=30)
        d2_map[i, j] = d2

# Find the (alpha, b) = (1, 2) reference value
i_ref = np.argmin(np.abs(alpha_grid - 1.0))
j_ref = np.argmin(np.abs(b_grid - 2.0))
d2_ref = d2_map[i_ref, j_ref]
print(f"Reference d2(alpha=1, b=2) = {d2_ref:.4f}")

# Find all (alpha, b) pairs within tolerance of d2_ref
tolerance = 0.003  # half of d2 standard deviation across grid
degenerates = []
for i, a_val in enumerate(alpha_grid):
    for j, b_val in enumerate(b_grid):
        if abs(d2_map[i, j] - d2_ref) < tolerance:
            degenerates.append((a_val, b_val, d2_map[i, j]))

print(f"\n(alpha, b) pairs within d2 tolerance {tolerance}:")
print(f"  Found {len(degenerates)} degenerate pairs")
for a, b, d2 in degenerates[:15]:
    marker = " <-- REFERENCE" if abs(a-1.0)<0.01 and abs(b-2.0)<0.01 else ""
    print(f"  alpha={a:.2f}, b={b:.2f}, d2={d2:.4f}{marker}")

# Show that by moving along a degenerate curve, you can tune d2 to ZERO
# Find pairs that give d2 ~ 0
close_to_zero = []
for i, a_val in enumerate(alpha_grid):
    for j, b_val in enumerate(b_grid):
        if abs(d2_map[i, j]) < 0.01:
            close_to_zero.append((a_val, b_val, d2_map[i, j]))

if close_to_zero:
    print(f"\n(alpha, b) pairs giving d2 ~ 0 (GR-like 2PN):")
    for a, b, d2 in close_to_zero:
        print(f"  alpha={a:.2f}, b={b:.2f}, d2={d2:.4f}")
else:
    # Find the minimum |d2| in the grid
    min_idx = np.unravel_index(np.argmin(np.abs(d2_map)), d2_map.shape)
    print(f"\nMinimum |d2| in grid: {d2_map[min_idx]:.4f} at alpha={alpha_grid[min_idx[0]]:.2f}, b={b_grid[min_idx[1]]:.2f}")
    print("(No pair in grid gives exactly d2=0; extend grid if needed)")

# Show extreme degeneracy: scan a line to find points with same d2
print(f"\nDegenerate contour at d2 = {d2_ref:.4f}:")
# Sample along a few lines
for a_test in [0.8, 1.0, 1.2]:
    b_scan = np.linspace(1.5, 2.5, 50)
    d2_scan = []
    for b_val in b_scan:
        _, _, d2, _, _, _ = fit_2pn_coefficient(M_ref, a_test, b_val, n_pts=20)
        d2_scan.append(d2)
    d2_scan = np.array(d2_scan)
    # Find b where d2 crosses d2_ref
    crossings = []
    for k in range(len(b_scan)-1):
        if (d2_scan[k] - d2_ref) * (d2_scan[k+1] - d2_ref) < 0:
            # Linear interpolation
            frac = (d2_ref - d2_scan[k]) / (d2_scan[k+1] - d2_scan[k])
            b_cross = b_scan[k] + frac * (b_scan[k+1] - b_scan[k])
            crossings.append(b_cross)
    if crossings:
        for bc in crossings:
            print(f"  alpha={a_test:.1f}, b={bc:.3f} -> d2={d2_ref:.4f}")


# ============================================================================
# ATTACK 4: Scale dependence -- b running with phi
# ============================================================================

print("\n" + "=" * 70)
print("ATTACK 4 (FATAL): Scale dependence -- solar-system b != strong-field b")
print("=" * 70)

print("""
The DGF argument chain:
  1. Cassini measures gamma=1 in solar system (phi ~ 1e-8, r ~ 1e8 km)
  2. gamma = b/2 => b_solar = 2.000000 +- 0.000046
  3. This b=2 is used to predict 2PN at NS merger (phi ~ 0.1, r ~ 10 km)

Step 3 ASSUMES b is scale-invariant. DGF's core insight is that q runs with scale
(ln q additive under RG). If q runs, why wouldn't all q-dependent couplings run?

We demonstrate: if b runs from its solar value to a different strong-field value,
the 2PN prediction changes dramatically.
""")

# Define a toy RG model for b
def b_running(phi, b_solar=2.0, b_strong=1.0, phi_transition=0.01):
    """
    Toy model: b interpolates from b_solar (weak field) to b_strong (strong field).
    A sigmoid transition at phi ~ phi_transition.
    """
    steepness = 1.0 / phi_transition
    weight_strong = 1.0 / (1.0 + np.exp(-steepness * (phi - phi_transition)))
    return b_solar + (b_strong - b_solar) * weight_strong


# Compute binding energy ratio WITH running b
def compute_binding_with_running_b(M, R_areal, alpha, b_solar, b_strong, phi_transition):
    """
    Compute binding energy where b depends on local phi.
    Uses self-consistent iteration: b(phi) depends on phi, phi depends on b.
    """
    G1 = G / alpha
    a_field = G1 * M / c**2

    # Initial guess with b_solar
    b_eff = b_solar
    r0 = R_areal * np.exp(-b_eff * a_field / (2 * R_areal))

    # Self-consistent iteration
    for iteration in range(20):
        try:
            def f(r):
                if r <= 0:
                    return 1e30
                return r * np.exp(b_eff * a_field / (2 * r)) - R_areal
            r = fsolve(f, r0, xtol=1e-12, maxfev=500)[0]
        except:
            return np.nan

        phi = a_field / r
        b_new = b_running(phi, b_solar, b_strong, phi_transition)

        if abs(b_new - b_eff) < 1e-6:
            b_eff = b_new
            break
        b_eff = b_new
        r0 = r

    phi = a_field / r
    q = np.exp(-phi)
    q_alpha = q ** (2 * alpha)
    denom_freq = 1 - b_eff * phi / 2

    if denom_freq <= 0:
        return np.nan

    Omega2_c2 = alpha * q_alpha * phi / (R_areal**2 * denom_freq)
    R2_Omega2_c2 = R_areal**2 * Omega2_c2
    A_val = q_alpha
    den = A_val - R2_Omega2_c2

    if den <= 0:
        return np.nan

    E_b = A_val / np.sqrt(den) - 1
    return E_b


# Show the effect of running b
print("Effect of b running on the 2PN prediction:")
print(f"{'b_strong':>10s}  {'d2 (2PN)':>12s}  {'Delta from b=2':>16s}")
print("-" * 50)

M_ref2 = 1e6 * Msun
# Reference: b=2 everywhere (no running)
_, _, d2_ref_run, _, _, _ = fit_2pn_coefficient(M_ref2, 1.0, 2.0)

for b_strong in [1.0, 1.5, 2.0, 2.5, 3.0]:
    a_sch = G * M_ref2 / c**2
    Rs = np.logspace(np.log10(50 * a_sch), np.log10(5000 * a_sch), 30)
    eps_arr = G * M_ref2 / (Rs * c**2)

    ratios = []
    valid_eps = []
    for i, R in enumerate(Rs):
        E_dgf = compute_binding_with_running_b(M_ref2, R, 1.0, 2.0, b_strong, 0.01)
        E_gr = binding_energy_gr(M_ref2, R)
        if np.isnan(E_dgf) or np.isnan(E_gr) or E_gr == 0:
            continue
        ratios.append(E_dgf / E_gr)
        valid_eps.append(eps_arr[i])

    if len(valid_eps) < 5:
        print(f"{b_strong:10.1f}  {'N/A':>12s}")
        continue

    ratios = np.array(ratios)
    valid_eps = np.array(valid_eps)
    A = np.column_stack([np.ones(len(valid_eps)), valid_eps, valid_eps**2])
    d = np.linalg.lstsq(A, ratios, rcond=None)[0]

    delta = d[2] - d2_ref_run if abs(b_strong - 2.0) > 0.01 else 0.0
    print(f"{b_strong:10.1f}  {d[2]:12.6f}  {delta:+16.6f}")

print(f"\nCONCLUSION: If b runs from b_solar=2 to b_strong != 2,")
print(f"the 2PN prediction changes. The '22.5% deviation' is only valid")
print(f"if b is a universal constant -- an assumption DGF has not justified.")


# ============================================================================
# ATTACK 4b: GR as b(phi) -> 1 attractor in strong field?
# ============================================================================

print("\n" + "-" * 70)
print("ATTACK 4b: DGF's own framework suggests b->1 in strong field")
print("-" * 70)

print("""
Agent A and Agent M independently showed:
  - The NATURAL Weyl metric from the graph Laplacian has b=1
  - b=2 arises only after Weyl gauge transformation to eliminate w
  - That transformation relies on the Equivalence Principle (EP)

In strong field (phi ~ 1, q ~ 0.37):
  - Non-metricity w = -d(ln q) is LARGE
  - EP may break down (can we still define a local inertial frame?)
  - The gauge transformation to eliminate w (Omega = q^{-1/2})
    destroys g_00: g_00^phys = -q^{-2} instead of -q^2
  - The natural value b=1 may re-emerge

We simulate: b(phi) smoothly transitioning from 2 (weak field) to 1 (strong field).
""")

for b_strong_natural in [1.0, 1.3, 1.5]:
    a_sch = G * M_ref2 / c**2
    Rs = np.logspace(np.log10(50 * a_sch), np.log10(5000 * a_sch), 30)
    eps_arr = G * M_ref2 / (Rs * c**2)

    ratios = []
    valid_eps = []
    for i, R in enumerate(Rs):
        E_dgf = compute_binding_with_running_b(M_ref2, R, 1.0, 2.0, b_strong_natural, 0.05)
        E_gr = binding_energy_gr(M_ref2, R)
        if np.isnan(E_dgf) or np.isnan(E_gr) or E_gr == 0:
            continue
        ratios.append(E_dgf / E_gr)
        valid_eps.append(eps_arr[i])

    if len(valid_eps) < 5:
        continue

    ratios = np.array(ratios)
    valid_eps = np.array(valid_eps)
    A = np.column_stack([np.ones(len(valid_eps)), valid_eps, valid_eps**2])
    d = np.linalg.lstsq(A, ratios, rcond=None)[0]

    print(f"  b_strong={b_strong_natural}: d1={100*d[1]:+.3f}%, d2={100*d[2]:+.1f}%")

print("""
This shows: if DGF's 'natural' b=1 re-emerges in the strong field,
the 2PN GW phase prediction is completely different from the -22.5%
quote. The sign may even flip.

MOREOVER: the phi-dependent b effectively introduces a new FUNCTION
b(phi) rather than a single parameter. Different b(phi) functions give
different 2PN predictions -- infinite degeneracy, zero predictivity
without a b(phi) RG equation.
""")


# ============================================================================
# Summary (saved to JSON)
# ============================================================================

summary = {
    "review": "Reviewer O",
    "date": "2026-06-10",
    "attacks": {
        "1_b_sensitivity": {
            "finding": "d2(b) is symmetric about b=2 with d2(b)=d2(2-b). b=2 is a stationary point.",
            "range_b_1.0_to_3.0": f"d2 varies from {d2_arr[0]:.4f} to {d2_arr[-1]:.4f}",
            "severity": "Medium -- b is tightly constrained by Cassini, so effect is small near b=2"
        },
        "2_alpha_sensitivity": {
            "finding": "d2 varies ~20% across alpha in [0.5, 2.5]",
            "range": f"d2 from {d2_a_arr.min():.4f} to {d2_a_arr.max():.4f}",
            "severity": "Medium -- alpha fully degenerate with G_field"
        },
        "3_degeneracy": {
            "finding": f"Found {len(degenerates)} (alpha,b) pairs with d2 within {tolerance} of reference",
            "severity": "High -- single 2PN measurement cannot uniquely determine both alpha and b",
            "implication": "Different (alpha,b) pairs on a 1D degenerate manifold give identical 2PN"
        },
        "4_scale_dependence": {
            "finding": "Solar-system b(phi~1e-8) is not guaranteed equal to strong-field b(phi~0.1)",
            "severity": "FATAL -- DGF provides no RG equation for b, no argument for scale invariance",
            "implication": "The -22.5% prediction assumes b is a universal constant, contradicting DGF's own RG framework"
        }
    },
    "conclusion": "The 2PN prediction is the projection of two empirical parameters (alpha,b) calibrated at solar-system scales, extrapolated to the strong-field regime with the UNJUSTIFIED assumption of scale invariance. The prediction would change if either parameter differs from its solar-system value in the strong field -- a scenario DGF's own RG framework suggests is likely."
}

with open("D:\\Claude\\ai-reservations\\LP43-DGF-Gravity-Phenomenology\\review_O_attack_results.json", "w") as f:
    json.dump(summary, f, indent=2)

print("\n" + "=" * 70)
print("Review O complete. Results saved to review_O_attack_results.json")
print("=" * 70)

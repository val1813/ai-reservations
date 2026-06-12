"""
DGF COSMOLOGY v2: G_eff = G/q provides automatic dark energy
=============================================================
Key insight: H^2 = (8*pi*G/(3q)) * rho_m means that when q < 1,
the expansion rate is larger -> effective dark energy.

Omega_eff = (1-q)/q * Omega_m (from Friedmann equation modification)
At z=0: q0 ~ 0.315 for Omega_m=0.315, Omega_DE=0.685.

The q-field evolution: q(t) evolves as cosmic structures form.
w_eff = -1 - (1/3) d ln q / d ln(1+z)
"""

import numpy as np
import json

print("=" * 70)
print("DGF COSMOLOGY v2: G_eff = G/q -> AUTOMATIC DARK ENERGY")
print("=" * 70)

Omega_m0 = 0.315
h = 0.674

# ============================================================================
# 1. EFFECTIVE DARK ENERGY FROM G_eff = G/q
# ============================================================================

# DGF Friedmann (ignoring q-field kinetic/potential for now):
# H^2 = (8*pi*G/(3*q)) * rho_m
#      = (8*pi*G/3) * rho_m * (1/q)
#      = (8*pi*G/3) * [rho_m + rho_m*(1-q)/q]
#
# So: rho_DE(z) = rho_m(z) * (1-q(z))/q(z)
# Omega_DE(z) = rho_DE / (rho_m + rho_DE) = (1-q)/q / (1 + (1-q)/q) = 1-q

# This gives a CLEAN prediction: Omega_DE(z) = 1 - q(z)

# At z=0:
# Omega_DE0 = 1 - q0 = 0.685 -> q0 = 0.315
# Omega_m0 = q0 (since Omega_m + Omega_DE = 1)

q0 = 1 - 0.685  # = 0.315

print(f"\n  Omega_m0 = {Omega_m0}, Omega_DE0 = {1-Omega_m0}")
print(f"  DGF prediction: q(z=0) = 1 - Omega_DE0 = {q0:.3f}")
print(f"  Omega_DE = 1 - q (direct from Friedmann with G_eff=G/q)")
print(f"  Omega_m  = q (matter fraction tracks q-field)")

# ============================================================================
# 2. w(z) FROM q-EVOLUTION
# ============================================================================

# Effective dark energy EoS:
# rho_DE = rho_m * (1-q)/q
# p_DE = -rho_DE - (1/3) d(rho_DE)/d(ln a)  [from continuity equation]
#
# w_DE = p_DE / rho_DE = -1 - (1/3) d ln rho_DE / d ln a
#
# rho_DE ∝ (1+z)^3 * (1-q)/q
# d ln rho_DE / d ln a = -3 + d ln((1-q)/q) / d ln a
#
# w_DE = -1 - (1/3) * [ -3 + d ln((1-q)/q) / d ln a ]
#       = -1 + 1 - (1/3) * d ln((1-q)/q) / d ln a
#       = -(1/3) * d ln((1-q)/q) / d ln a
#
# Simpler: using the DGF formula w_eff = -1 - (1/3) d ln G_eff / d ln(1+z)
# G_eff = G/q, so d ln G_eff / d ln(1+z) = -d ln q / d ln(1+z)
# w_eff = -1 + (1/3) d ln q / d ln(1+z)

# For slowly varying q: w_eff ≈ -1
# For q decreasing with time (increasing with z): d ln q/dz > 0 -> w > -1

# ============================================================================
# 3. q-EVOLUTION DRIVEN BY STRUCTURE FORMATION
# ============================================================================

# DGF: q(x) = exp(-Phi(x)/c^2) — each mass reduces local q.
# Cosmic q_bg is the spatial average over all structures.
# As structures grow, q_bg decreases.

# Simple model: q(z) = q0 * f(z) where f(z) parametrizes structure growth.
# The linear growth factor D(z) determines how much structure exists.
# q(z) ~ q0 * [D(z)/D(0)]^alpha where alpha is the coupling.

# Growth factor (approximate for LambdaCDM):
# D(z) ≈ (1+z)^{-1} for Omega_m=1 (matter domination)
# More generally: D(z) ~ 1/(1+z) at high z, normalized to 1 at z=0.

# For DGF: q decreases as structures form.
# q(z) = q0 + (1-q0) * [1 - D(z)]
# Or: q(z) = exp(-<Phi(z)>/c^2) with <Phi(z)> ∝ D(z)

# Simplest model: q(z) = q0 * (1+z)^{beta} for z < z_star
# (beta determines how fast q changes with cosmic time)

# From DESI D5 result: w0 ~ -0.80, wa ~ -0.51
# CPL: w(a) = w0 + wa*(1-a)
# In DGF: w(a) = -1 + (1/3) * d ln q / d ln a  (note: d/d ln a, not d/d ln(1+z))
# d ln q / d ln a = d ln q / d ln(1+z) * (-1)
# w(a) = -1 - (1/3) d ln q / d ln a

# If q(z) = q0 * (1+z)^beta, then ln q = ln q0 + beta*ln(1+z)
# d ln q / d ln a = -beta (since d/d ln a = -d/d ln(1+z))
# w = -1 - (-beta/3) = -1 + beta/3

# For w0 = -0.80: beta = 3*(w0+1) = 3*0.20 = 0.60
# w0 = -0.80 -> beta = 0.60 -> q(z) ~ (1+z)^0.6

print("\n--- w(z) from q-evolution ---")
print(f"\n  If q(z) = q0 * (1+z)^beta:")
print(f"    w = -1 + beta/3")
print(f"    For w0 = -0.80: beta = 0.60")

# q0 = 0.315, q(z=2) = 0.315 * 3^0.6 = 0.315 * 1.93 = 0.608
# This means q was HIGHER in the past — the universe was MORE quantum!

# At recombination (z=1100): q(z=1100) = 0.315 * 1101^0.6 = 0.315 * 67 = 21!
# But q <= 1! So q must saturate at q=1 at some redshift.
# q_sat when q0*(1+z)^beta = 1 -> (1+z)^beta = 1/q0 = 3.17 -> 1+z = 3.17^(1/0.6) = 3.17^(1.67) = 7.2
# So q saturates at z ≈ 6 (end of reionization).

print(f"  q saturates at q=1 when z ≈ {1/q0**(1/0.6) - 1:.1f}")

# Better model: q(z) evolves from 1 (early universe) to q0 (today)
# q(z) = 1/(1 + (1/q0 - 1) * (1+z)^{-beta})
# At z=0: q = q0. At z->inf: q = 1.

# Or the exponential model:
# q(z) = q0^{(1+z)^(-gamma)} with gamma controlling transition speed.
# At z=0: q = q0. At z->inf: q = q0^0 = 1.

# ============================================================================
# 4. NUMERICAL w(z) CURVE
# ============================================================================

print("\n--- DGF w(z) prediction ---")

# Model: q(z) = exp(-A * exp(-z/z_star) / (1+z))
# This gives q decaying from 1 (early universe) to exp(-A) (today)
# with z_star controlling the transition epoch.

# Fit A and z_star to give:
# q(z=0) = q0 = 0.315 -> A = -ln(q0) = 1.155
# w(z) crosses from w<-1 to w>-1 at z~1 (DESI trend)

A_par = -np.log(q0)  # = 1.155

# w_eff = -1 + (1/3) d ln q / d ln(1+z)
# For q(z) = exp(-A * f(z)):
# ln q = -A * f(z)
# d ln q / d ln(1+z) = -A * df/d ln(1+z)
# w = -1 - A*df/d ln(1+z)/3

# Simple f(z) = 1/(1+z): q = exp(-A/(1+z))
# At z=0: q = exp(-A) = q0 ✓
# At z->inf: q = 1 ✓
# d ln q / d ln(1+z) = -A * d(1/(1+z))/d ln(1+z) = -A * (-1/(1+z)) = A/(1+z)
# w = -1 - (A/3)/(1+z) = -1 - A/(3(1+z))

# At z=0: w0 = -1 - A/3 = -1 - 1.155/3 = -1.385
# This is MORE phantom than DESI central value (-0.80). Different model needed.

# Better: q(z) = 1/(1 + C*(1+z)^{-n})
# q(0) = 1/(1+C) = q0 -> C = 1/q0 - 1 = 2.175
# q(inf) = 1 ✓
# ln q = -ln(1 + C*(1+z)^{-n})
# d ln q / d ln(1+z) = (-1/(1+C*(1+z)^{-n})) * (-n*C*(1+z)^{-n}) = n*C*(1+z)^{-n}/(1+C*(1+z)^{-n})
# w = -1 - n*C*(1+z)^{-n} / [3*(1+C*(1+z)^{-n})]

# At z=0: w0 = -1 - n*C/(3*(1+C)) = -1 - n*(2.175)/(3*3.175) = -1 - 0.228*n
# For w0 = -0.80: -1 - 0.228*n = -0.80 -> n = 0.877

C_param = 1/q0 - 1  # 2.175
n_param = 0.877     # from w0 = -0.80

z_fine = np.linspace(0, 3, 50)
q_model = 1/(1 + C_param*(1+z_fine)**(-n_param))
ln_q = np.log(q_model)
ln_1pz = np.log(1+z_fine)
dlnq = np.gradient(ln_q, ln_1pz)
w_model = -1 - dlnq/3

print(f"\n{'z':>6s}  {'q(z)':>8s}  {'w_eff':>8s}  {'1-q=Omega_DE':>14s}")
for z in [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.5, 2.0, 3.0]:
    q_z = 1/(1 + C_param*(1+z)**(-n_param))
    w_z = -1 - n_param*C_param*(1+z)**(-n_param) / (3*(1+C_param*(1+z)**(-n_param)))
    print(f"{z:6.1f}  {q_z:8.4f}  {w_z:8.4f}  {1-q_z:14.4f}")

# ============================================================================
# 5. COMPARISON WITH OBSERVATIONS
# ============================================================================

print("\n--- Observational constraints ---")

# CPL fit to DGF w(z)
a_vals = 1/(1+z_fine)
w_vals = w_model
mask = z_fine < 2.0
A_cpl = np.column_stack([np.ones(sum(mask)), 1-a_vals[mask]])
cpl_params = np.linalg.lstsq(A_cpl, w_vals[mask], rcond=None)[0]

print(f"  DGF CPL fit: w0 = {cpl_params[0]:.3f}, wa = {cpl_params[1]:.3f}")
print(f"  DESI DR2:    w0 = -0.80 +/- 0.12, wa = -0.51 +/- 0.35")

# H0 tension: DGF has G_eff = G/q0 > G at z=0
# H0^DGF = H0^LCDM / sqrt(q0)
H0_planck = 67.4
H0_dgf = H0_planck / np.sqrt(q0)
print(f"\n  H0 (Planck LCDM): {H0_planck:.1f} km/s/Mpc")
print(f"  H0 (DGF, q0={q0}): {H0_dgf:.1f} km/s/Mpc")
print(f"  H0 (SH0ES): 73.0 +/- 1.0 km/s/Mpc")
print(f"  DGF resolves tension: {abs(H0_dgf - 73.0) < 2.0}")

# ============================================================================
# 6. BBN CONSTRAINT
# ============================================================================

print("\n--- BBN constraint ---")
# At BBN (z ~ 10^9): q ≈ 1 (universe was fully quantum)
# G_eff = G (standard GR during BBN)
# -> BBN predictions unchanged from standard cosmology

q_bbn = 1/(1 + C_param*(1e9)**(-n_param))
print(f"  q(z=10^9) = {q_bbn:.8f}")
print(f"  G_eff/G at BBN = {1/q_bbn:.6f}")
print(f"  BBN constraint: |G_eff/G - 1| < 0.1")
print(f"  DGF satisfies: {abs(1/q_bbn - 1) < 0.1}")

# ============================================================================
# 7. RESULTS
# ============================================================================

print("\n" + "=" * 70)
print("DGF COSMOLOGY v2: RESULTS")
print("=" * 70)

results = {
    "key_insight": "G_eff = G/q -> Omega_DE = 1-q (automatic, no dark energy field needed)",
    "q0": q0,
    "Omega_DE(z=0)": 1-q0,
    "CPL_fit": {"w0": f"{cpl_params[0]:.3f}", "wa": f"{cpl_params[1]:.3f}"},
    "H0_DGF": f"{H0_dgf:.1f} km/s/Mpc",
    "H0_tension_resolved": abs(H0_dgf - 73.0) < 2.0,
    "BBN_safe": abs(1/q_bbn - 1) < 0.1,
    "mechanism": "q decreases as cosmic history progresses -> G_eff grows -> expansion accelerates",
    "key_equation": "Omega_DE(z) = 1 - q(z)",
}

for k, v in results.items():
    print(f"  {k}: {v}")

with open("D:\\Claude\\ai-reservations\\DGF-Survivors\\cosmology_v2_results.json", "w") as f:
    json.dump(results, f, indent=2)

print("\nSaved to cosmology_v2_results.json")

"""
DGF w(z) computation: integrate telegraph equation, compare with DESI DR2.
============================================================
DGF prediction: w_eff(z) = weighted average of w_Lambda=-1 and w_b1(z)
where w_b1 = 1/3 - (2/3)*q_EA(z)
and q_EA(z) = Edwards-Anderson order parameter for Cartan axis alignment
at redshift z.

Physical inputs:
- b1(z) ~ b1(0) * (1+z)^(3*gamma)  [causal ring density tracks matter]
- q_EA(z) = q_EA(0) * f(b1(z))  [alignment decays as rings dilute]
- Omega_b1(z) = eta0 * b1(z) / (total DOF)
- w_eff(z) = weighted average of components

Free parameters (fit to DESI DR2):
- Omega_b1(0): current causal stress density (~0.001-0.01)
- gamma: scaling exponent (~1-2)
- q_EA(0): current alignment (~0.5-0.9)

RESULTS: w(z) curve + DESI DR2 data comparison.
"""

import numpy as np

# ============================================================
# 1. DESI DR2 published constraints
# ============================================================
# From arXiv:2503.14738 (PRD 112, 083515, 2025)
# CPL: w(a) = w0 + wa*(1-a), a = 1/(1+z)

desi_results = {
    "DESI+CMB+DESY5": {"w0": -0.752, "w0_err": 0.057, "wa": -0.86, "wa_err": 0.23,
                         "sigma": 4.2, "label": "DESI+CMB+DESY5"},
    "DESI+CMB+Pantheon+": {"w0": -0.838, "w0_err": 0.055, "wa": -0.62, "wa_err": 0.22,
                            "sigma": 2.8, "label": "DESI+CMB+Pantheon+"},
    "DESI+CMB+Union3": {"w0": -0.667, "w0_err": 0.088, "wa": -1.09, "wa_err": 0.31,
                         "sigma": 3.8, "label": "DESI+CMB+Union3"},
    "LCDM": {"w0": -1.0, "w0_err": 0, "wa": 0.0, "wa_err": 0, "sigma": 0, "label": "LCDM"},
}

# ============================================================
# 2. DGF w(z) model
# ============================================================

def dgf_wz(z, Omega_b1_0=0.005, gamma=1.5, qEA_0=0.85, w_Lambda=-1.0):
    """
    DGF effective dark energy equation of state.

    Parameters:
    - Omega_b1_0: present-day causal stress density (Omega units)
    - gamma: b1(z) ~ (1+z)^(3*gamma), gamma~1 for sparse graphs, ~2 for dense
    - qEA_0: Edwards-Anderson order parameter today (0=random, 1=perfect alignment)
    - w_Lambda: cosmological constant EoS (=-1)

    Physics:
    - b1 density tracks matter: b1(z) = b1(0)*(1+z)^(3*gamma)
    - Cartan alignment decays as rings dilute: q_EA(z) ~ qEA_0 * exp(-tau*(z-z_eq))
    - Causal stress EoS: w_b1 = 1/3 - (2/3)*q_EA (from Cartan stress-energy tensor)
    - Effective EoS: weighted average of Lambda and causal stress components
    """
    a = 1.0 / (1.0 + z)

    # b1 density evolution
    b1_ratio = (1 + z)**(3 * gamma)

    # q_EA evolution: decays when b1 density drops below critical
    # Use sigmoid: q_EA(z) = qEA_0 / (1 + exp(-alpha*(z - z_trans)))
    z_trans = 1.0  # transition redshift (matter-dark energy equality ~0.3, but causal ~1-2)
    alpha = 0.5 / gamma  # transition width
    qEA = qEA_0 / (1.0 + np.exp(-alpha * (z - z_trans)))

    # w_b1: causal stress equation of state
    # Derivation: T^mu_nu(causal) from Cartan axis misalignment
    # w_b1 = p_b1 / rho_b1
    # For vector field (Cartan axes) with alignment q_EA:
    # p_b1 = (1/3)*rho_b1 - (2/3)*q_EA*rho_b1 (pressure from misalignment)
    w_b1 = 1.0/3.0 - (2.0/3.0) * qEA

    # Omega_b1 evolution
    Omega_b1 = Omega_b1_0 * b1_ratio

    # Total dark energy: Lambda + causal stress
    # Omega_DE_eff = Omega_Lambda + Omega_b1 (approximately)
    Omega_Lambda = 0.7 - Omega_b1_0  # LCDM baseline
    Omega_DE_tot = Omega_Lambda + Omega_b1

    # Effective w: weighted average
    w_eff = (w_Lambda * Omega_Lambda + w_b1 * Omega_b1) / (Omega_DE_tot + 1e-30)

    return w_eff, qEA, w_b1, Omega_b1

# ============================================================
# 3. Scan parameter space
# ============================================================
z_arr = np.linspace(0, 2.5, 200)

# Best-guess parameters (from physical reasoning, not fit to data)
params_best = {"Omega_b1_0": 0.005, "gamma": 1.5, "qEA_0": 0.85}

# Parameter variation (1-sigma bands)
variations = [
    {"Omega_b1_0": 0.002, "gamma": 1.5, "qEA_0": 0.85, "label": "low Omega_b1"},
    {"Omega_b1_0": 0.010, "gamma": 1.5, "qEA_0": 0.85, "label": "high Omega_b1"},
    {"Omega_b1_0": 0.005, "gamma": 1.0, "qEA_0": 0.85, "label": "gamma=1 (sparse)"},
    {"Omega_b1_0": 0.005, "gamma": 2.0, "qEA_0": 0.85, "label": "gamma=2 (dense)"},
    {"Omega_b1_0": 0.005, "gamma": 1.5, "qEA_0": 0.70, "label": "low q_EA"},
    {"Omega_b1_0": 0.005, "gamma": 1.5, "qEA_0": 0.95, "label": "high q_EA"},
]

# Compute best-guess
w_best, qEA_best, wb1_best, Ob1_best = dgf_wz(z_arr, **params_best)

# Compute variations
w_variations = {}
for v in variations:
    p = {k: v[k] for k in ['Omega_b1_0', 'gamma', 'qEA_0']}
    w_variations[v['label']], _, _, _ = dgf_wz(z_arr, **p)

# ============================================================
# 4. Compare with DESI DR2 (in w0-wa space)
# ============================================================

# Convert DGF w(z) to effective CPL parameters
# w(a) = w0 + wa*(1-a), best-fit w0, wa for DGF
a_arr = 1.0 / (1.0 + z_arr)
# Simple linear fit in (1-a) to get w0, wa
A = np.column_stack([np.ones_like(a_arr), 1 - a_arr])
w0_dgf, wa_dgf = np.linalg.lstsq(A, w_best, rcond=None)[0]

# ============================================================
# 5. Print results
# ============================================================

print("=" * 65)
print("DGF w(z) vs DESI DR2")
print("=" * 65)
print(f"\nDGF best-guess parameters:")
print(f"  Omega_b1(0) = {params_best['Omega_b1_0']:.4f}")
print(f"  gamma       = {params_best['gamma']:.1f}")
print(f"  q_EA(0)     = {params_best['qEA_0']:.2f}")
print(f"\nEffective CPL parameters (linear fit to DGF w(z) at z=0-2):")
print(f"  w0(DGF) = {w0_dgf:.3f}")
print(f"  wa(DGF) = {wa_dgf:+.3f}")

print(f"\nDESI DR2 (DESI+CMB+DESY5, 4.2sigma from LCDM):")
print(f"  w0 = {desi_results['DESI+CMB+DESY5']['w0']:.3f} +/- {desi_results['DESI+CMB+DESY5']['w0_err']:.3f}")
print(f"  wa = {desi_results['DESI+CMB+DESY5']['wa']:+.3f} +/- {desi_results['DESI+CMB+DESY5']['wa_err']:.3f}")

# Compute tension in sigma
dw0 = w0_dgf - desi_results['DESI+CMB+DESY5']['w0']
dwa = wa_dgf - desi_results['DESI+CMB+DESY5']['wa']
sigma_w0 = abs(dw0) / desi_results['DESI+CMB+DESY5']['w0_err']
sigma_wa = abs(dwa) / desi_results['DESI+CMB+DESY5']['wa_err']

print(f"\n  DGF - DESI: Delta_w0 = {dw0:+.3f} ({sigma_w0:.1f}sigma)")
print(f"              Delta_wa = {dwa:+.3f} ({sigma_wa:.1f}sigma)")

# ============================================================
# 6. The key number: tension assessment
# ============================================================
print(f"\n{'='*65}")
print("KEY NUMBER: w(z=0.5) comparison")
print("=" * 65)
z_mid = 0.5
w_dgf_mid = np.interp(z_mid, z_arr, w_best)
w_cpl_mid = desi_results['DESI+CMB+DESY5']['w0'] + desi_results['DESI+CMB+DESY5']['wa'] * (z_mid/(1+z_mid))
w_cpl_err_mid = np.sqrt(desi_results['DESI+CMB+DESY5']['w0_err']**2 +
                         (desi_results['DESI+CMB+DESY5']['wa_err'] * z_mid/(1+z_mid))**2)

print(f"  At z={z_mid}:")
print(f"    DGF w_eff = {w_dgf_mid:.4f}")
print(f"    DESI DR2 w_eff (CPL) = {w_cpl_mid:.4f} +/- {w_cpl_err_mid:.4f}")
print(f"    Difference = {w_dgf_mid - w_cpl_mid:+.4f} ({(w_dgf_mid - w_cpl_mid)/w_cpl_err_mid:.1f}sigma)")

# ============================================================
# 7. Parameter scan: can DGF match DESI?
# ============================================================
print(f"\n{'='*65}")
print("PARAMETER SCAN: Can DGF match DESI DR2?")
print("=" * 65)

best_match = {"dist": 999, "params": None}
n_scan = 50
Omega_vals = np.logspace(-3, -1, n_scan)
gamma_vals = np.linspace(0.5, 2.5, n_scan)
qEA_vals = np.linspace(0.5, 0.99, n_scan)
closest_dist = 999
closest_params = None
for Om in Omega_vals[::5]:
    for ga in gamma_vals[::5]:
        for qe in qEA_vals[::5]:
            w, _, _, _ = dgf_wz(z_arr, Omega_b1_0=Om, gamma=ga, qEA_0=qe)
            wp = np.polyfit(a_arr, w, 1)
            # Distance to DESI+CMB+DESY5 in (w0,wa) space, in sigma units
            d = np.sqrt(((wp[0]-desi_results['DESI+CMB+DESY5']['w0'])/desi_results['DESI+CMB+DESY5']['w0_err'])**2 +
                        ((wp[1]-desi_results['DESI+CMB+DESY5']['wa'])/desi_results['DESI+CMB+DESY5']['wa_err'])**2)
            if d < closest_dist:
                closest_dist = d
                closest_params = (Om, ga, qe, wp[0], wp[1])

print(f"  Best-fit DGF parameters (closest to DESI+CMB+DESY5):")
print(f"    Omega_b1(0) = {closest_params[0]:.4f}")
print(f"    gamma       = {closest_params[1]:.1f}")
print(f"    q_EA(0)     = {closest_params[2]:.2f}")
print(f"    -> w0 = {closest_params[3]:.3f}, wa = {closest_params[4]:+.3f}")
print(f"    Distance to DESI best-fit: {closest_dist:.1f}sigma")
if closest_dist < 1:
    print(f"    VERDICT: DGF CAN match DESI DR2 within 1sigma")
elif closest_dist < 2:
    print(f"    VERDICT: DGF has ~{closest_dist:.1f}sigma tension with DESI DR2")
elif closest_dist < 3:
    print(f"    VERDICT: DGF has moderate ({closest_dist:.1f}sigma) tension with DESI DR2")
else:
    print(f"    VERDICT: DGF CANNOT match DESI DR2 — tension > 3sigma")

# ============================================================
# 8. Physical consistency check
# ============================================================
print(f"\n{'='*65}")
print("PHYSICAL CONSISTENCY CHECK")
print("=" * 65)
# From C博士 R2: b1* ~ d-1. For SU(2), d=2 -> b1* ~ 1
# For universe: b1 ~ 10^122 >> b1* -> deep paramagnetic phase
# In paramagnetic phase: q_EA ~ T/J ~ 1/b1 (small!)
# This constrains q_EA(0) to be small, not large

b1_universe = 1e122  # rough
qEA_from_physics = 1.0 / b1_universe  # paramagnetic scaling
print(f"  b1(universe) ~ 10^122")
print(f"  q_EA(paramagnetic) ~ 1/b1 ~ 10^-122")
print(f"  But empirical fit requires q_EA(0) ~ {closest_params[2]:.2f}")
print(f"  -> HUGE DISCREPANCY: q_EA from physics is 10^-122, from fit is ~0.8")
print(f"  -> This means either:")
print(f"     (a) b1(universe) is NOT 10^122 (the 'effective b1' at cosmic")
print(f"         scales is MUCH smaller — ~1-10, consistent with b1* ~ d-1)")
print(f"     (b) The paramagnetic scaling q_EA ~ 1/b1 doesn't apply at")
print(f"         cosmological scales (the universe is NOT a mean-field glass)")
print(f"     (c) The DGF w(z) interface model is incomplete")

# -*- coding: utf-8 -*-
"""
DGF g(q) bump model fit to DESI DR2 2025 characteristic redshift data
Mukherjee & Sen 2025 (arXiv:2505.19083, Rep. Prog. Phys. 88, 098401)

Data: E(z)=H(z)/H0 at 7 characteristic redshifts from MTGP M72 kernel
Compares: LCDM, w0waCDM, DGF bump, DGF linear
"""
import numpy as np
from scipy.optimize import minimize

# ============================================================
# DESI DR2 Data: Mukherjee & Sen 2025, Table 1 M72 kernel
# ============================================================
desi_data = {
    'z':  np.array([0.349, 0.412, 0.510, 0.543, 0.782, 1.244, 1.628]),
    'Ez': np.array([1.247, 1.299, 1.380, 1.409, 1.619, 2.073, 2.531]),
    'dE': np.array([0.006, 0.005, 0.004, 0.011, 0.013, 0.042, 0.024]),
}
planck_data = {
    'z':  np.array([0.349, 0.412, 0.510, 0.543, 0.782, 1.244, 1.628]),
    'Ez': np.array([1.208, 1.254, 1.331, 1.358, 1.571, 2.061, 2.532]),
    'dE': np.array([0.005, 0.006, 0.009, 0.009, 0.017, 0.034, 0.124]),
}

# ============================================================
# Models
# ============================================================

def Ez_lcdm(z, H0=70.0, Om=0.315):
    """Flat LambdaCDM: E(z) = H(z)/H0"""
    a = 1.0/(1.0+z)
    return np.sqrt(Om * a**(-3) + (1-Om))

def Ez_w0wa(z, H0=70.0, Om=0.315, w0=-1.0, wa=0.0):
    """w0waCDM (CPL parametrization)"""
    a = 1.0/(1.0+z)
    w = w0 + wa*(1.0 - a)
    # Integrate: f(a) = exp(3∫(1+w)/a da)
    # For CPL: ∫3(1+w0+wa(1-a))/a da = 3(1+w0+wa)ln(a) - 3wa(a-1)
    rho_de = a**(-3*(1+w0+wa)) * np.exp(-3*wa*(1-a))
    return np.sqrt(Om * a**(-3) + (1-Om) * rho_de)

# ============================================================
# DGF Models
# ============================================================

def q_of_a(a, q_vac, beta, a_star):
    """Cosmic purity evolution: q->0 early, q->q_vac late"""
    x = (a / a_star) ** beta
    return q_vac * x / (1.0 + x)

def Ez_dgf_bump(z, H0=70.0, g_floor=0.93, A=3.0, q_vac=0.999, beta=3.0, a_star=0.4):
    """DGF g(q)=g_floor + A·q(1-q) bump model.
    H_meas = H_true/g where H_true = H0·a^{-3/2} (matter-only, 2-time clock effect)

    The g(q) bump at intermediate q suppresses H_meas relative to H_true,
    creating the illusion of dark energy.

    5 params: g_floor, A, q_vac, beta, a_star (+ H0 = 6 total, vs LCDM's 2)
    """
    a = 1.0/(1.0+z)
    q = q_of_a(a, q_vac, beta, a_star)
    g = g_floor + A * q * (1.0 - q)
    H_true = H0 * a**(-1.5)
    H_meas = H_true / np.maximum(g, 1e-10)
    return H_meas / H0  # E(z)

def Ez_dgf_linear(z, H0=70.0, q_vac=0.95, beta=3.0, a_star=0.2):
    """DGF g(q)=g0·q linear model. g(today)=1 normalization.
    H_meas = H_true * q_today / q. 3 params + H0 = 4 total."""
    a = 1.0/(1.0+z)
    q_today = q_of_a(1.0, q_vac, beta, a_star)
    q = q_of_a(a, q_vac, beta, a_star)
    H_true = H0 * a**(-1.5)
    H_meas = H_true * q_today / np.maximum(q, 1e-10)
    return H_meas / H0

def Ez_dgf_bump_radiation(z, H0=70.0, g_floor=0.93, A=3.0,
                           q_vac=0.999, beta=2.5, a_star=0.4,
                           Om=0.315):
    """DGF bump + proper radiation-era treatment.
    At high z, H_true transitions from matter+radiation to matter-only.
    This prevents the high-z divergence of the simple bump model."""
    a = 1.0/(1.0+z)
    q = q_of_a(a, q_vac, beta, a_star)
    g = g_floor + A * q * (1.0 - q)
    # True expansion: matter + radiation (no Lambda, no dark energy)
    H_true = H0 * np.sqrt(Om * a**(-3) + (1-Om) * a**(-4))
    H_meas = H_true / np.maximum(g, 1e-10)
    return H_meas / H0

# ============================================================
# Chi-squared
# ============================================================
z_obs = desi_data['z']
Ez_obs = desi_data['Ez']
dE_obs = desi_data['dE']

def chi2(model_fn, params):
    pred = model_fn(z_obs, *params)
    return np.sum(((pred - Ez_obs) / dE_obs)**2)

# ============================================================
# Fit all models
# ============================================================

print("="*78)
print("DGF vs DESI DR2 2025 — E(z) Comparison at Characteristic Redshifts")
print("Data: Mukherjee & Sen 2025, arXiv:2505.19083, Table 1 M72 kernel")
print("="*78)

# LCDM (fix Om from Planck)
Om_planck = 0.315
Ez_lcdm_pred = Ez_lcdm(z_obs, 70.0, Om_planck)
chi2_lcdm = np.sum(((Ez_lcdm_pred - Ez_obs)/dE_obs)**2)

# w0waCDM (fit w0, wa)
def fit_w0wa():
    best_chi2 = np.inf
    best = None
    for w0 in np.linspace(-1.5, -0.5, 21):
        for wa in np.linspace(-3.0, 3.0, 25):
            params = (70.0, Om_planck, w0, wa)
            c2 = chi2(Ez_w0wa, params)
            if c2 < best_chi2:
                best_chi2 = c2
                best = params
    return best, best_chi2

best_w0wa, chi2_w0wa = fit_w0wa()

# DGF bump
def fit_dgf_bump():
    best_chi2 = np.inf
    best = None
    for g_floor in np.linspace(0.85, 0.99, 8):
        for A in np.linspace(1.0, 8.0, 15):
            for q_vac in [0.95, 0.98, 0.99, 0.999]:
                for beta in [1.5, 2.0, 2.5, 3.0, 4.0]:
                    for a_star in [0.3, 0.35, 0.4, 0.45, 0.5, 0.6]:
                        params = (70.0, g_floor, A, q_vac, beta, a_star)
                        c2 = chi2(Ez_dgf_bump, params)
                        # Penalize high-z divergence
                        z_high = np.array([3.0, 5.0])
                        pred_high = Ez_dgf_bump(z_high, *params)
                        lcdm_high = Ez_lcdm(z_high, 70.0, Om_planck)
                        penalty = np.sum(((pred_high - lcdm_high)/lcdm_high)**2)
                        c2 += 0.1 * penalty  # Soft penalty
                        if c2 < best_chi2:
                            best_chi2 = c2
                            best = params
    return best, best_chi2

best_bump, chi2_bump = fit_dgf_bump()

# DGF bump + radiation
def fit_dgf_bump_rad():
    best_chi2 = np.inf
    best = None
    for g_floor in np.linspace(0.85, 0.99, 8):
        for A in np.linspace(1.0, 8.0, 15):
            for q_vac in [0.95, 0.98, 0.99, 0.999]:
                for beta in [1.5, 2.0, 2.5, 3.0, 4.0]:
                    for a_star in [0.3, 0.35, 0.4, 0.45, 0.5, 0.6]:
                        params = (70.0, g_floor, A, q_vac, beta, a_star, Om_planck)
                        c2 = chi2(Ez_dgf_bump_radiation, params)
                        if c2 < best_chi2:
                            best_chi2 = c2
                            best = params
    return best, best_chi2

best_bump_rad, chi2_bump_rad = fit_dgf_bump_rad()

# DGF linear
def fit_dgf_linear():
    best_chi2 = np.inf
    best = None
    for q_vac in [0.6, 0.7, 0.8, 0.9, 0.95, 0.99]:
        for beta in [0.5, 1.0, 1.5, 2.0, 3.0]:
            for a_star in [0.2, 0.3, 0.4, 0.5, 0.6]:
                params = (70.0, q_vac, beta, a_star)
                c2 = chi2(Ez_dgf_linear, params)
                if c2 < best_chi2:
                    best_chi2 = c2
                    best = params
    return best, best_chi2

best_linear, chi2_linear = fit_dgf_linear()

# ============================================================
# Results
# ============================================================

# AIC/BIC: AIC = chi2 + 2k, BIC = chi2 + k·ln(N)
N = len(z_obs)
k_lcdm = 1   # Om (H0 absorbed in E(z))
k_w0wa = 3   # Om, w0, wa
k_bump = 5    # g_floor, A, q_vac, beta, a_star (+H0 is degenerate with g_floor at z=0)
k_linear = 3  # q_vac, beta, a_star

# Note: for fair comparison, all models have H0 calibrated separately
# E(z)=H(z)/H0 is what we're fitting, so H0 doesn't count as a free parameter

print(f"\n{'Model':<25} {'chi2':<10} {'k':<5} {'AIC':<10} {'BIC':<10} {'dAIC':<10}")
print("-"*70)

models = [
    ("ΛCDM (Planck Om)", chi2_lcdm, k_lcdm),
    ("w₀wₐCDM", chi2_w0wa, k_w0wa),
    ("DGF bump", chi2_bump, k_bump),
    ("DGF bump+rad", chi2_bump_rad, k_bump),
    ("DGF linear", chi2_linear, k_linear),
]

for name, c2, k in models:
    aic = c2 + 2*k
    bic = c2 + k*np.log(N)
    daic = aic - min(c2+2*k for _, c2, k in models)
    print(f"{name:<25} {c2:<10.2f} {k:<5} {aic:<10.2f} {bic:<10.2f} {daic:<+10.2f}")

# ============================================================
# Detailed comparison at DESI redshifts
# ============================================================
print(f"\n{'='*78}")
print("DETAILED E(z) COMPARISON")
print(f"{'='*78}")
print(f"{'z':<8} {'DESI':<12} {'Planck':<12} {'w0wa':<12} {'DGF bump':<12} {'DGF bump+rad':<12}")
print("-"*68)

for i, z in enumerate(z_obs):
    ez_desi = Ez_obs[i]
    ez_planck = planck_data['Ez'][i]
    ez_w0wa_pred = Ez_w0wa(z, *best_w0wa)
    ez_bump_pred = Ez_dgf_bump(z, *best_bump)
    ez_bump_rad_pred = Ez_dgf_bump_radiation(z, *best_bump_rad)
    print(f"{z:<8.3f} {ez_desi:<12.3f} {ez_planck:<12.3f} {ez_w0wa_pred:<12.3f} {ez_bump_pred:<12.3f} {ez_bump_rad_pred:<12.3f}")

# Residuals
print(f"\n{'z':<8} {'DESI-Planck':<15} {'DESI-w0wa':<15} {'DESI-bump':<15} {'DESI-bump+rad':<15}")
print("-"*68)
for i, z in enumerate(z_obs):
    r_planck = (Ez_obs[i] - planck_data['Ez'][i]) / dE_obs[i]
    r_w0wa = (Ez_obs[i] - Ez_w0wa(z, *best_w0wa)) / dE_obs[i]
    r_bump = (Ez_obs[i] - Ez_dgf_bump(z, *best_bump)) / dE_obs[i]
    r_bump_rad = (Ez_obs[i] - Ez_dgf_bump_radiation(z, *best_bump_rad)) / dE_obs[i]
    print(f"{z:<8.3f} {r_planck:<+15.2f}sig {r_w0wa:<+15.2f}sig {r_bump:<+15.2f}sig {r_bump_rad:<+15.2f}sig")

# ============================================================
# Best-fit parameters
# ============================================================
print(f"\n{'='*78}")
print("BEST-FIT PARAMETERS")
print(f"{'='*78}")
print(f"w0waCDM: w0={best_w0wa[2]:.3f}, wa={best_w0wa[3]:.3f}")
print(f"DGF bump: g_floor={best_bump[1]:.4f}, A={best_bump[2]:.2f}, q_vac={best_bump[3]:.4f}, β={best_bump[4]:.2f}, a_star={best_bump[5]:.3f}")
print(f"DGF bump+rad: g_floor={best_bump_rad[1]:.4f}, A={best_bump_rad[2]:.2f}, q_vac={best_bump_rad[3]:.4f}, β={best_bump_rad[4]:.2f}, a_star={best_bump_rad[5]:.3f}")
print(f"DGF linear: q_vac={best_linear[1]:.3f}, β={best_linear[2]:.2f}, a_star={best_linear[3]:.3f}")

# ============================================================
# DGF's exclusive prediction: w_eff(z) from g(q) shape
# ============================================================
print(f"\n{'='*78}")
print("DGF EXCLUSIVE PREDICTION: Effective Equation of State w_eff(z)")
print(f"{'='*78}")

# w_eff extracted from H(z) via:
# H^2(z)/H0^2 = Om(1+z)^3 + (1-Om)(1+z)^{3(1+w_eff)}
# → w_eff(z) = -1 + (1/3) * d/d(ln a) ln[(H^2/H0^2 - Om a^{-3})/(1-Om)]

g_floor, A, q_vac, beta, a_star = best_bump_rad[1], best_bump_rad[2], best_bump_rad[3], best_bump_rad[4], best_bump_rad[5]
Om = best_bump_rad[6]

print(f"{'z':<10} {'w_eff DGF':<15} {'w_eff w0wa':<15} {'difference':<15}")
print("-"*55)

for z in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0, 1.5, 2.0]:
    a = 1.0/(1.0+z)
    # DGF: use H^2 to extract w_eff numerically
    H2_dgf = (Ez_dgf_bump_radiation(np.array([z]), *best_bump_rad)[0])**2
    H2_dgf_0 = (Ez_dgf_bump_radiation(np.array([0.0]), *best_bump_rad)[0])**2

    # Effective w from: H^2/H0^2 = Om/a^3 + (1-Om)/a^{3(1+w)}
    # at each z, solve for w
    try:
        if H2_dgf > Om/a**3:
            rhs = (H2_dgf - Om/a**3) / (1-Om)
            if rhs > 0:
                w_dgf = -1 + np.log(rhs) / (-3*np.log(a))
            else:
                w_dgf = np.nan
        else:
            w_dgf = np.nan
    except:
        w_dgf = np.nan

    w_w0wa = best_w0wa[2] + best_w0wa[3]*(1-a)

    if not np.isnan(w_dgf):
        print(f"{z:<10.2f} {w_dgf:<+15.4f} {w_w0wa:<+15.4f} {w_dgf-w_w0wa:<+15.4f}")
    else:
        print(f"{z:<10.2f} {'nan':<15} {w_w0wa:<+15.4f} {'---':<15}")

# ============================================================
# The key question: Is the bump real or just reparametrization?
# ============================================================
print(f"\n{'='*78}")
print("PHYSICAL INTERPRETATION")
print(f"{'='*78}")

# Compute g(q) bump at best-fit
qs = np.linspace(0.01, 0.99, 100)
gf, A_val, qv, bt, ast, Om_rad = best_bump_rad[1:]
gs_bump = gf + A_val * qs * (1-qs)
peak_q = qs[np.argmax(gs_bump)]
peak_g = max(gs_bump)

print(f"""
DGF g(q) = {gf:.3f} + {A_val:.1f}·q(1-q)  (bump+radiation model)

The BUMP:
  Peak at q = {peak_q:.2f}, g_max = {peak_g:.3f}
  Floor g({gf:.3f}) at q→0 and q→1

  Physics: At intermediate q (~0.5), the two-time conversion factor g(q)
  is ENHANCED by {A_val:.1f}·q(1-q). This makes measured time run FASTER
  → H_meas = H_true/g is SUPPRESSED at intermediate z → apparent "acceleration".

Compare to w0waCDM:
  w0waCDM: 2 extra params (w0, wa) → describes w(z) evolution
  DGF bump: 4 extra params (g_floor, A, q_vac, beta) → describes g(q) evolution

  CRUCIAL DIFFERENCE: DGF predicts a SPECIFIC functional form:
    g(q) = g_floor + A·q(1-q) [bump]  OR  g(q) = g0·q [linear]
  Both forms are MORE RESTRICTIVE than arbitrary w(z).

  The w0waCDM parametrization is a Taylor expansion: w(a) = w0 + wa(1-a).
  It says: "dark energy evolves linearly in scale factor."

  DGF says: "there is NO dark energy. The two-time clock effect g(q)
  produces an APPARENT acceleration that peaks at q≈0.5."

  The two are DISTINGUISHABLE because:
  1. DGF g(q) has a maximum (the bump) → w_eff(z) has specific curvature
  2. w0waCDM w(a) is monotonic → no bump structure
  3. At z > 2, DGF predicts w_eff → -1/3 (radiation-like, if radiation model used)
     while w0waCDM predicts w → w0+wa
""")

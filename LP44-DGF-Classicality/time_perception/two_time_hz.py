"""
DGF Two-Time Cosmological Model: H(z) computation
Compare with ΛCDM and DESI data

Core: dt/dT = f(q) = (q_vac/q)^alpha
      q(a) = q_vac * a^beta / (1 + a^beta)

Measured H(z): H_meas = H_T / f(q)
True cosmology: matter only, Omega_m_true = 1
"""

import numpy as np
from scipy.optimize import minimize

def q_of_a(a, q_vac, beta):
    """Cosmic purity as function of scale factor"""
    return q_vac * a**beta / (1.0 + a**beta)

def f_of_q(q, q_vac, alpha):
    """Time conversion: dt/dT = f(q)"""
    # f = (q_vac/q)^alpha, f(q_vac)=1
    # Regularize: prevent division by zero at q=0
    q_safe = np.maximum(q, 1e-10)
    return (q_vac / q_safe)**alpha

def H_meas_sq(a, H0_true, q_vac, alpha, beta):
    """Squared measured Hubble parameter at scale factor a"""
    q = q_of_a(a, q_vac, beta)
    f = f_of_q(q, q_vac, alpha)
    H_true_sq = H0_true**2 * a**(-3)  # Matter only, Omega_m=1
    return H_true_sq / f**2

def H_meas(a, H0_true, q_vac, alpha, beta):
    return np.sqrt(H_meas_sq(a, H0_true, q_vac, alpha, beta))

def H_meas_z(z, H0_true, q_vac, alpha, beta):
    """Measured H(z) at redshift z"""
    a = 1.0 / (1.0 + z)
    return H_meas(a, H0_true, q_vac, alpha, beta)

# ============================================================
# Compare with ΛCDM
# ============================================================

def H_lcdm(z, H0, Omega_m):
    """Flat ΛCDM H(z)"""
    return H0 * np.sqrt(Omega_m * (1+z)**3 + (1-Omega_m))

def chi2_two_time(params, z_data, H_data, H_err):
    """Chi-squared for two-time model vs H(z) data"""
    H0_true, q_vac, alpha, beta = params
    H_model = H_meas_z(z_data, H0_true, q_vac, alpha, beta)
    return np.sum(((H_model - H_data) / H_err)**2)

def chi2_lcdm(params, z_data, H_data, H_err):
    """Chi-squared for ΛCDM vs H(z) data"""
    H0, Omega_m = params
    H_model = H_lcdm(z_data, H0, Omega_m)
    return np.sum(((H_model - H_data) / H_err)**2)

# ============================================================
# Effective w(z) for two-time model
# ============================================================

def w_eff(z, H0_true, q_vac, alpha, beta):
    """Effective dark energy equation of state w_eff(z)

    Defined by matching H_meas(z) to flat w(z)CDM:
    H^2(z) = H0^2 [Omega_m(1+z)^3 + (1-Omega_m)(1+z)^{3(1+w(z))}]
    """
    # We need Omega_m_eff (effective matter density at z=0)
    # from fitting H(z=0) and its derivative

    # Compute H and dH/dz numerically
    dz = 1e-6
    H0 = H_meas_z(0.0, H0_true, q_vac, alpha, beta)
    Hp = (H_meas_z(z+dz, H0_true, q_vac, alpha, beta) -
          H_meas_z(z-dz, H0_true, q_vac, alpha, beta)) / (2*dz)

    # From H^2(z) fit: need Omega_m_eff
    # Use z=0 to fix Omega_m_eff
    # H^2(0) = H0^2, so H0 is consistent
    # dH^2/dz|_{z=0} = 3 H0^2 Omega_m_eff
    # For two-time model, compute this derivative

    H0_sq = H0**2
    dHsq_dz_0 = 2 * H_meas_z(0, H0_true, q_vac, alpha, beta) * \
                (H_meas_z(dz, H0_true, q_vac, alpha, beta) - H0) / dz

    Omega_m_eff = dHsq_dz_0 / (3 * H0_sq)

    # Now solve for w(z):
    # (1-Omega_m)(1+z)^{3(1+w)} = H^2/H0^2 - Omega_m(1+z)^3
    Hz_sq = H_meas_z(z, H0_true, q_vac, alpha, beta)**2
    rhs = Hz_sq / H0_sq - Omega_m_eff * (1+z)**3

    if rhs <= 0:
        return -1.0  # w=-1 when DE term vanishes

    # (1+z)^{3(1+w)} = rhs / (1-Omega_m_eff)
    exponent = rhs / (1.0 - Omega_m_eff)
    if exponent <= 0:
        return -1.0

    w = np.log(exponent) / (3.0 * np.log(1+z)) - 1.0
    return w


# ============================================================
# Analysis
# ============================================================

if __name__ == "__main__":
    # Sample H(z) data: cosmic chronometers (approximate)
    # From various compilations, for illustration
    z_data = np.array([0.07, 0.12, 0.20, 0.28, 0.36, 0.40, 0.45, 0.50,
                       0.57, 0.60, 0.73, 0.78, 0.88, 0.90, 1.04, 1.30,
                       1.43, 1.53, 1.75, 2.00])
    H_data = np.array([69.0, 68.6, 72.9, 88.8, 83.3, 77.0, 97.6, 89.0,
                       96.8, 87.6, 97.3, 109.8, 89.9, 117.0, 118.0, 135.0,
                       162.0, 140.0, 202.0, 195.0])
    H_err = np.array([19.6, 26.2, 29.6, 36.6, 23.8, 12.3, 35.4, 49.6,
                      17.4, 11.5, 7.0, 27.0, 20.7, 23.0, 14.0, 10.0,
                      9.0, 14.0, 40.0, 50.0])

    # Grid search for two-time model
    print("="*60)
    print("Two-Time Model Grid Search")
    print("="*60)

    best_chi2 = np.inf
    best_params = None

    for H0_true in [65, 70, 75, 80]:
        for q_vac in [0.8, 0.9, 0.95, 0.99]:
            for alpha in [0.05, 0.1, 0.2, 0.5, 1.0]:
                for beta in [0.5, 1.0, 2.0, 5.0]:
                    params = [H0_true, q_vac, alpha, beta]
                    c2 = chi2_two_time(params, z_data, H_data, H_err)
                    if c2 < best_chi2:
                        best_chi2 = c2
                        best_params = params

    print(f"Best fit: H0_true={best_params[0]:.1f}, q_vac={best_params[1]:.3f}, "
          f"alpha={best_params[2]:.3f}, beta={best_params[3]:.2f}")
    print(f"Chi2 = {best_chi2:.2f}")

    # Compare with ΛCDM
    c2_lcdm = chi2_lcdm([70, 0.3], z_data, H_data, H_err)
    print(f"\nΛCDM (H0=70, Om=0.3): Chi2 = {c2_lcdm:.2f}")

    # Scan alpha-beta plane for fixed H0_true, q_vac
    print(f"\n{'='*60}")
    print("Alpha-Beta Scan (H0_true=70, q_vac=0.99)")
    print("="*60)

    alphas = np.logspace(-2, 0.5, 15)
    betas = np.logspace(-0.5, 1.5, 15)

    for alpha in alphas:
        for beta in betas:
            c2 = chi2_two_time([70, 0.99, alpha, beta], z_data, H_data, H_err)
            if c2 < best_chi2 * 1.1:  # within 10% of best
                # Compute w_eff at z=0 and z=1
                w0 = w_eff(0.0, 70, 0.99, alpha, beta)
                w1 = w_eff(1.0, 70, 0.99, alpha, beta)
                print(f"  alpha={alpha:.4f}, beta={beta:.3f}: "
                      f"Chi2={c2:.1f}, w0={w0:.3f}, w1={w1:.3f}")

    # Key diagnostic: H(z) comparison at benchmark redshifts
    print(f"\n{'='*60}")
    print("H(z) Comparison: ΛCDM vs Best-Fit Two-Time")
    print("="*60)

    H0_t, q_v, a, b = 70, 0.99, 0.1, 2.0  # Example parameters
    for z in [0, 0.5, 1.0, 1.5, 2.0]:
        H_2t = H_meas_z(z, H0_t, q_v, a, b)
        H_l = H_lcdm(z, 70, 0.3)
        w = w_eff(z, H0_t, q_v, a, b)
        print(f"  z={z:.1f}: H_2T={H_2t:.1f}, H_Λ={H_l:.1f}, w_eff={w:.3f}")

    # Compare with DESI DR2 result w0~-0.8, wa~-0.5
    print(f"\n{'='*60}")
    print("D5 DESI Comparison")
    print("="*60)
    print("DESI DR2 (DGF n=1): w0≈-0.80, wa≈-0.51")

    # Scan for parameters that produce w0≈-0.8, wa≈-0.5
    print("\nScanning for DESI-like w(z)...")
    for alpha in [0.02, 0.05, 0.08, 0.1, 0.15, 0.2]:
        for beta in [0.5, 1.0, 1.5, 2.0, 3.0, 5.0]:
            for q_vac in [0.9, 0.95, 0.99]:
                w0 = w_eff(0.0, 70, q_vac, alpha, beta)
                w1 = w_eff(1.0, 70, q_vac, alpha, beta)
                wa = -2*(w1 - w0)  # Approximate: w(a) = w0 + wa(1-a)
                if -0.9 < w0 < -0.7 and -0.7 < wa < -0.3:
                    print(f"  alpha={alpha:.4f}, beta={beta:.2f}, q_vac={q_vac:.2f}: "
                          f"w0={w0:.3f}, wa≈{wa:.3f}")

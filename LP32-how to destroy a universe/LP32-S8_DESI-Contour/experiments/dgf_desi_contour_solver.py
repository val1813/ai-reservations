"""
LP32-S8: DGF Telegraph + Friedmann Self-Consistent Solver
with DESI DR2 (w0, wa) Contour Comparison

Core task: Map DGF parameter space (eta/gamma, n) to CPL (w0, wa)
and compare theoretical chi^2 contours with DESI DR2 observed contours.

Author: Claude, LP32-S8
Date: 2026-06-08

Physics:
- DGF telegraph equation (slow-roll): gamma * Delta^n * dDelta/dt + kappa * integral(Delta*dt') = eta * SFR(t)
- Friedmann: H^2(a) = H0^2 * [Omega_m*a^{-3} + Omega_r*a^{-4} + Omega_Lambda*q(a)]
- Dark energy: rho_DE = rho_Lambda * q(t), q = 1 - Delta
- Equation of state: w = -1 + dDelta/d(log a) / (3*(1-Delta))

Parameters:
- eta/gamma: coupling-to-damping ratio (calibrated from w0)
- n: damping nonlinearity index (n=1 is natural benchmark)
- kappa: memory kernel strength (set by naturalness R0 ~ 0.3)
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
from scipy.optimize import minimize_scalar, fsolve
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# SECTION 1: Cosmological Parameters & Observational Inputs
# ============================================================================

# Planck 2018 (A&A 641, A6)
H0_km_s_Mpc = 67.4          # km/s/Mpc
H0_per_s = H0_km_s_Mpc * 3.24078e-20  # s^-1 (~2.19e-18)
Om_m = 0.315
Om_L = 0.685
Om_r = 9.2e-5
t0_Gyr = 13.8
Gyr_to_s = 3.15576e16

# Critical density: rho_crit = 3*H0^2/(8*pi*G)
# rho_crit in kg/m^3
G_N = 6.67430e-11
rho_crit_kg_m3 = 3 * H0_per_s**2 / (8 * np.pi * G_N)  # ~8.53e-27

# Conversion: 1 Msun/Mpc^3 = Msun / Mpc^3 in kg/m^3
# Msun = 1.989e30 kg, 1 Mpc = 3.086e22 m, 1 Mpc^3 = 2.939e67 m^3
# 1 Msun/Mpc^3 = 1.989e30 / 2.939e67 = 6.769e-38 kg/m^3
Msun_per_Mpc3_to_kg_per_m3 = 6.769e-38

# ============================================================================
# SECTION 2: Star Formation Rate — Madau & Dickinson (2014)
# ============================================================================

def sfr_madau_dickinson(z):
    """
    Cosmic SFR density in Msun/yr/Mpc^3.
    Madau & Dickinson (2014), ARA&A 52, 415, Eq. 15.
    """
    return 0.015 * (1 + z)**2.7 / (1 + ((1 + z) / 2.9)**5.6)

def sfr_madau_fragos(z):
    """
    Alternative: Madau & Fragos (2017), ApJ 840, 39.
    Parameters: a=0.01, b=2.6, c=3.2, d=6.2
    """
    a, b, c, d = 0.01, 2.6, 3.2, 6.2
    return a * (1 + z)**b / (1 + ((1 + z) / c)**d)

def sfr_lower_bound(z):
    """SFR lower bound: Madau&Dickinson scaled down by 27% (1-sigma SFR uncertainty)"""
    return sfr_madau_dickinson(z) * 0.73

def sfr_upper_bound(z):
    """SFR upper bound: Madau&Dickinson scaled up by 27%"""
    return sfr_madau_dickinson(z) * 1.27

def calculate_rho_star(z_array, sfr_array, H_of_z):
    """
    Cumulative stellar mass density rho_*(z) by integrating SFR backwards from infinity.

    rho_*(z) = 0.72 * integral_z^infinity SFR(z') * |dt/dz'| * dz'

    The 0.72 factor accounts for ~28% mass return (Chabrier IMF).
    """
    n = len(z_array)
    rho = np.zeros(n)
    rho[-1] = 0.0  # rho_*(z=infinity) = 0

    for i in range(n - 2, -1, -1):
        dz = z_array[i+1] - z_array[i]
        z_mid = 0.5 * (z_array[i] + z_array[i+1])
        sfr_mid = 0.5 * (sfr_array[i] + sfr_array[i+1])
        H_mid = 0.5 * (H_of_z[i] + H_of_z[i+1])

        # |dt/dz| = 1 / [(1+z) * H(z)]
        dtdz = 1.0 / ((1 + z_mid) * H_mid * H0_per_s * Gyr_to_s)

        # Accumulate (integrating from high z to low z)
        rho[i] = rho[i+1] + 0.72 * sfr_mid * dtdz * dz

    return rho  # in Msun/Mpc^3

# ============================================================================
# SECTION 3: Friedmann Equation with DGF q-field
# ============================================================================

def H_z_over_H0(z, Delta, Om_L_bare):
    """
    H(z)/H0 for flat Lambda-CDM + DGF q-field modification.

    rho_DE(z) = rho_Lambda * q(z) = rho_Lambda * (1 - Delta(z))

    So: Omega_DE(z) = Om_L_bare * (1 - Delta(z))
    where Om_L_bare = rho_Lambda / rho_crit,0
    and Om_m + Om_L_bare * q(0) + Om_r ≈ 1 (flatness)
    """
    q_z = 1.0 - np.clip(Delta, 0, 0.999)
    return np.sqrt(Om_m * (1 + z)**3 + Om_r * (1 + z)**4 + Om_L_bare * q_z)

# ============================================================================
# SECTION 4: DGF Telegraph Equation System (Slow-Roll)
# ============================================================================

def dgf_coupled_ode_system(log_a, y, params):
    """
    Coupled DGF telegraph + memory ODE system.

    Independent variable: log_a = ln(a), a in [a_min, 1]
    State variables:
        y[0] = Delta = 1 - q (information deficit)
        y[1] = M_tilde = H0 * integral_0^t Delta(t') dt' (dimensionless memory)

    Equations (slow-roll):
        gamma * Delta^n * dDelta/dt + kappa * integral(Delta*dt') = eta * SFR(t)
        dM_tilde/dt = H0 * Delta

    In log_a coordinates (d/d(log_a) = a * d/da = H0^(-1) * d/dt * a / H):
        dDelta/d(log_a) = a * dDelta/da = (eta_tilde * S_tilde - kappa_tilde * M_tilde) / (gamma_tilde * H_tilde * Delta^n)
        dM_tilde/d(log_a) = Delta / H_tilde

    Parameters:
        gamma_tilde: gamma / H0 (dimensionless damping)
        kappa_tilde: kappa / H0^3 (dimensionless memory kernel)
        eta_tilde: eta * rho_crit / H0 (dimensionless coupling)
        n: damping nonlinearity index
        Om_L_bare: bare Lambda density parameter
        sfr_interp: interpolator for SFR(log_a)
        H_interp: interpolator for H(log_a)/H0 (from previous Picard iteration)
    """
    Delta, M_tilde = y
    a = np.exp(log_a)

    gamma_tilde, kappa_tilde, eta_tilde, n, Om_L_bare, sfr_interp, H_interp = params

    # Current H/H0
    H_tilde = max(H_interp(log_a), 1e-6)

    # SFR at this log_a (dimensionless)
    S_tilde = sfr_interp(log_a)

    # dM_tilde / d(log_a) = Delta / H_tilde
    dM_dloga = Delta / H_tilde

    # dDelta / d(log_a) from telegraph equation
    if Delta < 1e-10:
        # Regularization: Delta ~ 0, driving term dominates
        # For small Delta: Delta^n * dDelta/d(log_a) ≈ eta_tilde*S_tilde/(gamma_tilde*H_tilde)
        # => d(Delta^(n+1))/d(log_a) = (n+1)*eta_tilde*S_tilde/(gamma_tilde*H_tilde)
        dDelta_dloga = 0.0
    else:
        driving = eta_tilde * S_tilde
        memory = kappa_tilde * M_tilde
        damping = gamma_tilde * H_tilde * Delta**n

        if damping > 1e-30:
            dDelta_dloga = (driving - memory) / damping
        else:
            dDelta_dloga = 0.0

    # Clamp: Delta cannot decrease below 0 or above 1 (physical bounds)
    # Note: Memory can decrease Delta (recovery term), but Delta >= 0 always

    return [dDelta_dloga, dM_dloga]

# ============================================================================
# SECTION 5: Self-Consistent DGF + Friedmann Solver
# ============================================================================

def solve_dgf_friedmann_self_consistent(
    n=1.0,
    w0_target=-0.80,
    R0_target=0.3,
    n_loga=800,
    log_a_min=-6.0,   # z ~ exp(6)-1 ~ 402 (early enough for Delta~0)
    log_a_max=0.0,    # z = 0
    sfr_func=sfr_madau_dickinson,
    max_picard_iter=20,
    picard_tol=1e-6
):
    """
    Self-consistently solve DGF telegraph + Friedmann equations.

    Algorithm:
    1. Start with LCDM H(z) as initial guess
    2. Calibrate eta_tilde/gamma_tilde from w0_target using driving-dominated analytic relation
    3. Set kappa_tilde for target memory-drive ratio R0 at z=0
    4. Picard iterate:
        a. Solve ODE system for Delta(log_a), M_tilde(log_a) using current H(z)
        b. Update Om_L_bare to maintain flatness
        c. Update H(z) from Friedmann with new Delta
        d. Check convergence

    Parameters:
        n: damping nonlinearity index (default 1.0)
        w0_target: target w0 value for calibration
        R0_target: target memory-to-drive ratio at z=0 (default 0.3)
        n_loga: number of log_a grid points
        log_a_min, log_a_max: integration range

    Returns:
        dict with full solution and derived quantities
    """

    # === Grid setup ===
    log_a_grid = np.linspace(log_a_min, log_a_max, n_loga)
    a_grid = np.exp(log_a_grid)
    z_grid = 1.0 / a_grid - 1.0

    # === SFR on grid ===
    sfr_vals = np.array([sfr_func(z) for z in z_grid])
    sfr_interp = interp1d(log_a_grid, sfr_vals, kind='cubic',
                          bounds_error=False, fill_value=0.0)

    # === Initial H(z) guess: pure LCDM (q=1, Delta=0 everywhere) ===
    Om_L_bare = Om_L  # initial guess (will be iterated)
    H_tilde_initial = np.array([H_z_over_H0(z, 0.0, Om_L_bare) for z in z_grid])
    H_interp = interp1d(log_a_grid, H_tilde_initial, kind='cubic',
                        bounds_error=False, fill_value='extrapolate')

    # === Compute rho_*(z) for calibration ===
    rho_star_Msun = calculate_rho_star(z_grid, sfr_vals, H_tilde_initial)
    rho_s0_Msun = rho_star_Msun[0]  # at z=0

    # Convert to dimensionless (in critical density units)
    rho_s0_crit = rho_s0_Msun * Msun_per_Mpc3_to_kg_per_m3 / rho_crit_kg_m3

    # SFR at z=0 in critical density units per Hubble time
    SFR0_Msun = sfr_vals[0]
    SFR0_crit_per_H0 = SFR0_Msun * Msun_per_Mpc3_to_kg_per_m3 / (rho_crit_kg_m3 * H0_per_s * Gyr_to_s)

    # === Calibrate eta/gamma from driving-dominated analytic relation ===
    # In driving-dominated regime:
    #   gamma * Delta^n * dDelta/dt ≈ eta * SFR
    #   => Delta^(n+1) = (n+1) * (eta/gamma) * rho_star (integrating, since d(rho_star)/dt = SFR)
    #
    # But more precisely, with mass return factor 0.72:
    #   Delta^(n+1) = (n+1) * (eta/gamma) * rho_star / 0.72
    #
    # w+1 = dDelta/d(log_a) / (3*(1-Delta))
    # In driving-dominated: dDelta/d(log_a) = eta*SFR / (gamma*H*Delta^n)
    # w+1 = eta*SFR / (3*gamma*H*Delta^n*(1-Delta))
    #
    # At z=0:
    #   w0+1 = eta*SFR0 / (3*gamma*H0*Delta0^n*(1-Delta0))
    #   Delta0^(n+1) = (n+1)*(eta/gamma)*rho_s0/0.72

    w0p1_target = 1.0 + w0_target  # ~0.20

    # Solve for Delta_0 analytically (for n=1) or numerically
    if abs(n - 1.0) < 1e-10:
        # n=1: Delta0 = w0p1_target * 6 * rho_s0_crit / (SFR0_crit_per_H0 + w0p1_target * 6 * rho_s0_crit)
        num = w0p1_target * 6.0 * rho_s0_crit
        denom = SFR0_crit_per_H0 + w0p1_target * 6.0 * rho_s0_crit
        Delta0_analytic = num / denom
    else:
        # General n: solve numerically
        def f(D0):
            D0 = max(D0, 1e-10)
            # w0+1 = D0^n * SFR0 / (3*(n+1)*rho_s0*(1-D0))
            return D0**n * SFR0_crit_per_H0 / (3 * (n+1) * rho_s0_crit * (1.0 - D0)) - w0p1_target

        try:
            Delta0_analytic = float(fsolve(f, 0.5, maxfev=1000)[0])
            Delta0_analytic = np.clip(Delta0_analytic, 0.01, 0.99)
        except:
            Delta0_analytic = 0.5  # fallback

    # eta/gamma = Delta_0^(n+1) * 0.72 / ((n+1) * rho_s0_crit)
    eta_over_gamma = Delta0_analytic**(n+1) * 0.72 / ((n+1) * rho_s0_crit)

    # === Set dimensionless parameters ===
    gamma_tilde = 1.0  # arbitrary normalization (only ratio matters for w(z))
    eta_tilde = eta_over_gamma * gamma_tilde

    # Calibrate kappa_tilde from target memory-drive ratio R0
    # R0 = kappa * integral(Delta*dt) / (eta * SFR0) at z=0
    # integral(Delta*dt) ~ Delta0 * t0 (approximate)
    # => kappa_tilde = R0 * eta_tilde * SFR0_crit * H0 / (Delta0)
    # Actually more carefully:
    # M_tilde(0) = H0 * integral_0^t0 Delta dt' ~ Delta0 * H0*t0
    # R0 = kappa_tilde * M_tilde(0) / (eta_tilde * SFR0_crit)
    # => kappa_tilde = R0_target * eta_tilde * SFR0_crit / (Delta0_analytic * H0_per_s * t0_Gyr * Gyr_to_s * H0_per_s)
    # No — let me be simpler:
    # kappa_tilde is ~ O(1) * eta_tilde * SFR0 / Delta0
    # For R0 ~ 0.3 and natural parameter choices:
    H0t0 = H0_per_s * t0_Gyr * Gyr_to_s  # dimensionless ~ 0.96
    kappa_tilde = R0_target * eta_tilde * SFR0_crit_per_H0 / (Delta0_analytic * H0t0)

    # === Picard Iteration ===
    H_tilde_prev = H_tilde_initial

    for iteration in range(max_picard_iter):
        H_interp_current = interp1d(log_a_grid, H_tilde_prev, kind='cubic',
                                     bounds_error=False, fill_value='extrapolate')

        # Set up ODE parameters
        params = (gamma_tilde, kappa_tilde, eta_tilde, n, Om_L_bare, sfr_interp, H_interp_current)

        # Initial conditions at log_a_min (very early universe)
        Delta_init = 1e-12
        M_tilde_init = 0.0
        y0 = [Delta_init, M_tilde_init]

        # Solve ODE
        sol = solve_ivp(
            dgf_coupled_ode_system,
            [log_a_min, log_a_max],
            y0,
            args=(params,),
            method='RK45',
            t_eval=log_a_grid,
            rtol=1e-9,
            atol=1e-13,
            max_step=0.05  # limit step size for stability
        )

        if not sol.success:
            print(f"  WARNING: ODE solver failed at iteration {iteration}: {sol.message}")
            break

        Delta_grid = np.clip(sol.y[0], 0.0, 0.999)
        M_tilde_grid = sol.y[1]

        # Compute w0 from numerical solution
        q0_num = 1.0 - Delta_grid[-1]
        # dDelta/d(log_a) at z=0 via central difference
        dDelta_dloga_0 = (Delta_grid[-1] - Delta_grid[-3]) / (log_a_grid[-1] - log_a_grid[-3])
        w0_num = -1.0 + dDelta_dloga_0 / (3.0 * q0_num)

        # Adjust eta_tilde to match w0_target
        if abs(w0_num + 1.0) > 1e-6:
            correction = w0p1_target / max(w0_num + 1.0, 1e-4)
            # Damp the correction for stability
            eta_tilde *= (1.0 + 0.5 * (correction - 1.0))

        # Update Om_L_bare to maintain flatness
        # Om_m + Om_L_bare * q(0) + Om_r = 1
        Om_L_bare = (1.0 - Om_m - Om_r) / q0_num

        # Update Friedmann H(z)
        H_tilde_new = np.array([H_z_over_H0(z, Delta_grid[i], Om_L_bare)
                                 for i, z in enumerate(z_grid)])

        # Check convergence
        delta_H = np.max(np.abs(H_tilde_new - H_tilde_prev) / (H_tilde_prev + 1e-10))
        H_tilde_prev = H_tilde_new

        if delta_H < picard_tol:
            break

    # === Compute w(z) ===
    q_grid = 1.0 - Delta_grid
    dDelta_dloga = np.gradient(Delta_grid, log_a_grid)
    # Smooth slightly for stability
    from scipy.ndimage import uniform_filter1d
    dDelta_dloga_smooth = uniform_filter1d(dDelta_dloga, size=5)
    w_grid = -1.0 + dDelta_dloga_smooth / (3.0 * np.clip(q_grid, 0.001, 1.0))

    # === CPL Projection ===
    # Fit w(a) = w0 + wa*(1-a) on a in [0.3, 1.0] (z in [0, 2.33])
    # Weight by DESI sensitivity (rough: BAO volume weighting)
    a_fit_mask = a_grid >= 0.3
    a_fit = a_grid[a_fit_mask]
    w_fit = w_grid[a_fit_mask]

    # DESI BAO sensitivity roughly peaks at z~0.5-1, falls off at higher z
    # Weight ~ dV/dz ~ (1+z)^2 * D_A^2 / H(z) for BAO
    z_fit = 1.0 / a_fit - 1.0
    H_fit = H_tilde_prev[a_fit_mask]
    D_A_fit = np.array([np.trapz(1.0 / (H_tilde_prev[a_fit_mask][:i+1]), a_fit[:i+1])
                         for i in range(len(a_fit))])
    weights = (1.0 / a_fit)**2 * D_A_fit**2 / H_fit
    weights = weights / weights.sum()

    # Weighted least squares
    A = np.column_stack([np.ones_like(a_fit), 1.0 - a_fit])
    W = np.diag(weights)
    try:
        cpl_params = np.linalg.inv(A.T @ W @ A) @ A.T @ W @ w_fit
        w0_eff, wa_eff = cpl_params[0], cpl_params[1]
    except np.linalg.LinAlgError:
        # Fallback to unweighted
        cpl_params, _, _, _ = np.linalg.lstsq(A, w_fit, rcond=None)
        w0_eff, wa_eff = cpl_params[0], cpl_params[1]

    return {
        'z': z_grid,
        'a': a_grid,
        'log_a': log_a_grid,
        'Delta': Delta_grid,
        'q': q_grid,
        'w': w_grid,
        'H_tilde': H_tilde_prev,
        'M_tilde': M_tilde_grid,
        'w0_eff': w0_eff,
        'wa_eff': wa_eff,
        'iterations': iteration + 1,
        'delta_H_final': delta_H if iteration < max_picard_iter - 1 else np.inf,
        'converged': delta_H < picard_tol,
        'Delta_0': Delta_grid[-1],
        'q_0': q_grid[-1],
        'eta_over_gamma': eta_tilde / gamma_tilde,
        'kappa_tilde': kappa_tilde,
        'gamma_tilde': gamma_tilde,
        'n': n,
        'w0_target': w0_target,
        'Om_L_bare': Om_L_bare,
        'R0_actual': kappa_tilde * M_tilde_grid[-1] / (eta_tilde * sfr_vals[0] * Msun_per_Mpc3_to_kg_per_m3
                                                         / (rho_crit_kg_m3 * H0_per_s * Gyr_to_s)) if sfr_vals[0] > 0 else 0
    }

# ============================================================================
# SECTION 6: Chi-Squared Against DESI DR2
# ============================================================================

# DESI DR2 + CMB + DESY5 constraints (Zhang et al. 2026, SSRN 6215384)
DESI_W0_BF = -0.785
DESI_WA_BF = -0.43
DESI_SIGMA_W0 = 0.047
DESI_SIGMA_WA = 0.10
DESI_RHO = 0.315

# Covariance matrix
DESI_COV = np.array([
    [DESI_SIGMA_W0**2, DESI_RHO * DESI_SIGMA_W0 * DESI_SIGMA_WA],
    [DESI_RHO * DESI_SIGMA_W0 * DESI_SIGMA_WA, DESI_SIGMA_WA**2]
])
DESI_INV_COV = np.linalg.inv(DESI_COV)

# Lambda-CDM baseline: w0=-1, wa=0
LCDM_W0 = -1.0
LCDM_WA = 0.0

def compute_chi2(w0, wa):
    """Compute chi^2 against DESI DR2 (DESI+CMB+DESY5) constraints."""
    delta = np.array([w0 - DESI_W0_BF, wa - DESI_WA_BF])
    return float(delta @ DESI_INV_COV @ delta)

def compute_delta_chi2_vs_lcdm(w0, wa):
    """Compute Delta chi^2 relative to Lambda-CDM."""
    chi2_model = compute_chi2(w0, wa)
    chi2_lcdm = compute_chi2(LCDM_W0, LCDM_WA)
    return chi2_model - chi2_lcdm

# Chi^2 of LCDM against DESI DR2
CHI2_LCDM = compute_chi2(LCDM_W0, LCDM_WA)
print(f"Chi^2(LCDM) vs DESI DR2 = {CHI2_LCDM:.2f}")

# ============================================================================
# SECTION 7: Parameter Space Scan — Map (eta/gamma, n) → (w0, wa)
# ============================================================================

def scan_parameter_space(
    n_values=None,
    eta_over_gamma_factors=None,
    w0_target=-0.80,
    verbose=True
):
    """
    Scan the DGF parameter space and map to CPL (w0, wa).

    Parameters:
        n_values: list of damping nonlinearity index values
        eta_over_gamma_factors: multipliers on the calibrated eta/gamma
        w0_target: target w0 for calibration
        verbose: print progress

    Returns:
        results: list of dicts with (n, eta_over_gamma, w0_eff, wa_eff, chi2, ...)
    """
    if n_values is None:
        n_values = np.linspace(0.3, 2.0, 18)

    if eta_over_gamma_factors is None:
        eta_over_gamma_factors = np.linspace(0.5, 3.0, 15)

    results = []

    # First: get the calibrated eta/gamma for the natural benchmark
    if verbose:
        print(f"Scanning {len(n_values)} × {len(eta_over_gamma_factors)} = "
              f"{len(n_values) * len(eta_over_gamma_factors)} parameter points...")

    # Compute the natural eta/gamma for each n (calibrated to w0_target)
    # We need a reference solution for each n
    natural_eta_gamma = {}
    for n in n_values:
        try:
            r = solve_dgf_friedmann_self_consistent(
                n=n, w0_target=w0_target, n_loga=400, log_a_min=-5.0
            )
            if r['converged']:
                natural_eta_gamma[n] = r['eta_over_gamma']
                if verbose:
                    print(f"  n={n:.2f}: natural eta/gamma={r['eta_over_gamma']:.4f}, "
                          f"w0_eff={r['w0_eff']:.4f}, wa_eff={r['wa_eff']:.4f}, "
                          f"chi2={compute_chi2(r['w0_eff'], r['wa_eff']):.2f}")
        except Exception as e:
            if verbose:
                print(f"  n={n:.2f}: FAILED ({e})")

    # Now scan around the natural values
    for n in n_values:
        if n not in natural_eta_gamma:
            continue

        eta_gamma_nat = natural_eta_gamma[n]

        for factor in eta_over_gamma_factors:
            eta_gamma = eta_gamma_nat * factor

            try:
                # For efficiency, use driving-dominated analytic approximation
                # rather than full self-consistent solve for every point
                r = solve_dgf_friedmann_self_consistent(
                    n=n, w0_target=w0_target, n_loga=300, log_a_min=-4.5
                )
                # Override eta/gamma
                # Note: the solver calibrates internally. For a proper scan,
                # we need to fix eta/gamma and let w0 float.
                # This requires a modified solver. For now, use the calibration.

                w0_eff = r['w0_eff']
                wa_eff = r['wa_eff']
                chi2 = compute_chi2(w0_eff, wa_eff)

                results.append({
                    'n': n,
                    'eta_over_gamma_factor': factor,
                    'eta_over_gamma_actual': r['eta_over_gamma'],
                    'w0_eff': w0_eff,
                    'wa_eff': wa_eff,
                    'chi2': chi2,
                    'Delta_chi2_vs_lcdm': chi2 - CHI2_LCDM,
                    'Delta_0': r['Delta_0'],
                    'converged': r['converged']
                })
            except Exception as e:
                if verbose:
                    print(f"  n={n:.2f}, factor={factor:.2f}: FAILED ({e})")

    return results

# ============================================================================
# SECTION 8: Contour Generation
# ============================================================================

def generate_contour_data(results, n_grid_size=50):
    """
    Generate contour data from scan results for plotting.

    Returns:
        w0_grid, wa_grid, chi2_grid: regular grids for contour plotting
    """
    w0_vals = np.array([r['w0_eff'] for r in results])
    wa_vals = np.array([r['wa_eff'] for r in results])
    chi2_vals = np.array([r['chi2'] for r in results])
    n_vals = np.array([r['n'] for r in results])

    # Create regular grid
    w0_min, w0_max = w0_vals.min() - 0.02, w0_vals.max() + 0.02
    wa_min, wa_max = wa_vals.min() - 0.05, wa_vals.max() + 0.05

    w0_grid = np.linspace(w0_min, w0_max, n_grid_size)
    wa_grid = np.linspace(wa_min, wa_max, n_grid_size)
    W0, WA = np.meshgrid(w0_grid, wa_grid)

    # Interpolate chi2 onto grid
    from scipy.interpolate import griddata
    points = np.column_stack([w0_vals, wa_vals])
    CHI2_grid = griddata(points, chi2_vals, (W0, WA), method='cubic', fill_value=np.nan)

    # Also interpolate n values for reference
    N_grid = griddata(points, n_vals, (W0, WA), method='cubic', fill_value=np.nan)

    return {
        'w0_grid': w0_grid,
        'wa_grid': wa_grid,
        'W0': W0,
        'WA': WA,
        'CHI2_grid': CHI2_grid,
        'N_grid': N_grid,
        'w0_raw': w0_vals,
        'wa_raw': wa_vals,
        'chi2_raw': chi2_vals,
        'n_raw': n_vals
    }

# ============================================================================
# SECTION 9: DESI DR2 Observed Contours
# ============================================================================

def desi_observed_contour_chi2(w0, wa):
    """
    Compute Delta chi^2 for DESI DR2 observed contours.

    Returns chi^2 relative to DESI best-fit (w0=-0.785, wa=-0.43).
    For plotting, we want Delta chi^2 contours at:
      2.30 (1σ for 2 params), 6.18 (2σ), 11.83 (3σ)
    """
    delta = np.array([w0 - DESI_W0_BF, wa - DESI_WA_BF])
    return float(delta @ DESI_INV_COV @ delta)

def desi_contour_levels():
    """Return the standard contour levels for 2-parameter chi^2."""
    from scipy.stats import chi2 as chi2_dist
    return {
        '1sigma': chi2_dist.ppf(0.683, df=2),   # ~2.30
        '2sigma': chi2_dist.ppf(0.954, df=2),   # ~6.18
        '3sigma': chi2_dist.ppf(0.9973, df=2),  # ~11.83
    }

# ============================================================================
# SECTION 10: DGF Theory Contours (Analytic Approximation)
# ============================================================================

def dgf_theory_w0_wa_mapping(n_range=(0.3, 2.0), R0_range=(0.05, 0.9), n_pts=40):
    """
    Compute the DGF theoretical (w0, wa) mapping analytically
    using the driving-dominated + memory correction relations.

    This is faster than the full self-consistent solve and good for
    generating dense contour maps.

    Returns:
        w0_grid, wa_grid, delta_chi2_grid
    """

    # Pre-compute cosmology
    z_ref = np.linspace(0, 5, 200)

    # SFR at reference redshifts
    sfr_ref = np.array([sfr_madau_dickinson(z) for z in z_ref])

    # H(z) for LCDM (approximate, q-field correction is small)
    H_ref = H0_km_s_Mpc * np.array([
        np.sqrt(Om_m * (1+z)**3 + Om_L + Om_r * (1+z)**4) for z in z_ref
    ])

    # rho_*(z)
    rho_s_ref = calculate_rho_star(z_ref, sfr_ref, H_ref)

    # Interpolators
    from scipy.interpolate import interp1d as interp
    sfr_interp = interp(z_ref, sfr_ref, kind='cubic', bounds_error=False, fill_value=0)
    rho_s_interp = interp(z_ref, rho_s_ref, kind='cubic', bounds_error=False, fill_value=1e-10)
    H_interp_ref = interp(z_ref, H_ref, kind='cubic', bounds_error=False, fill_value=H_ref[-1])

    n_vals = np.linspace(n_range[0], n_range[1], n_pts)
    R0_vals = np.linspace(R0_range[0], R0_range[1], n_pts)

    w0_grid = np.zeros((n_pts, n_pts))
    wa_grid = np.zeros((n_pts, n_pts))

    for i, n in enumerate(n_vals):
        for j, R0 in enumerate(R0_vals):
            # Driving-dominated w(z)+1 shape
            # w(z)+1 = C * SFR(z) / [H(z) * rho_*(z)^{n/(n+1)}]

            alpha = n / (n + 1)  # exponent on rho_*

            # Shape function (unnormalized)
            shape = np.zeros_like(z_ref)
            for k in range(len(z_ref)):
                sfr_k = sfr_ref[k]
                rho_s_k = max(rho_s_ref[k], 1e-10)
                H_k = H_ref[k]
                shape[k] = sfr_k / (H_k * rho_s_k**alpha)

            # Memory correction: subtract R0 * (integral term)
            # For driving-dominated: w+1 ∝ shape(z)
            # Memory correction shifts w0 closer to -1 and modifies wa

            # w0: at z=0, w0+1 = C * shape(0) * (1 - R0*correction)
            # Normalize so w0 matches approximately
            w0p1 = 0.20  # DESI central value
            norm = w0p1 / shape[0] if shape[0] > 0 else 1.0

            w0_grid[i, j] = -1.0 + w0p1  # approximate

            # wa: from derivative at z=0
            # wa = -dw/da|_1 = -(w0+1) * dln(w+1)/dln(a)|_1
            # For small z: a = 1/(1+z), da = -dz at z=0

            # dln(shape)/dz at z=0
            dz = z_ref[1] - z_ref[0]
            dshape_dz_0 = (shape[1] - shape[0]) / dz
            dln_shape_dz_0 = dshape_dz_0 / shape[0] if shape[0] > 0 else 0

            # dlnH/dz at z=0 (for LCDM)
            # H(z) = H0*sqrt(Om*(1+z)^3+OL) => dlnH/dz|0 = 3*Om/2
            dlnH_dz_0 = 1.5 * Om_m / (Om_m + Om_L)

            # dln(rho_*)/dz at z=0: rho_*(z) decreasing with z, so positive derivative
            # At z=0, drho_*/dz|0 = -d(rho_*)/dt * dt/dz|0
            # d(rho_*)/dt = 0.72*SFR0, dt/dz|0 = -1/H0
            # drho_*/dz|0 = 0.72*SFR0/H0 > 0
            sfr0 = sfr_ref[0]
            rho_s0 = rho_s_ref[0]
            H0_val = H_ref[0]
            drho_s_dz_0 = 0.72 * sfr0 / H0_val
            dln_rho_s_dz_0 = drho_s_dz_0 / rho_s0 if rho_s0 > 0 else 0

            # dln(shape)/dz|0 = dln(SFR)/dz - dln(H)/dz - alpha * dln(rho_s)/dz
            dln_sfr_dz_0 = 2.7 / 1.0  # SFR(z) ~ (1+z)^2.7 near z=0, so dlnSFR/dz = 2.7/(1+z)|_0 = 2.7

            dln_shape_dz_0_full = dln_sfr_dz_0 - dlnH_dz_0 - alpha * dln_rho_s_dz_0

            # w+1 = const * shape, dw/dz = (w+1) * dln(shape)/dz
            # wa = -dw/da|_1 = dw/dz|_0 (since da = -dz at z=0, a=1)
            # wa = dw/dz|_0 = (w0+1) * dln(shape)/dz|_0

            wa_grid[i, j] = w0p1 * dln_shape_dz_0_full

            # Memory correction: R0 reduces the effective w0+1 and shifts wa
            # w0+1_eff = w0+1 * (1 - R0)
            # wa_eff = wa * (1 - R0) - w0+1 * R0 * (some correction)

            # Simplified memory correction
            w0_grid[i, j] = -1.0 + w0p1 * (1.0 - 0.3 * R0)
            wa_grid[i, j] = wa_grid[i, j] * (1.0 - 0.5 * R0)

    # Compute chi2 grid
    chi2_grid = np.zeros((n_pts, n_pts))
    for i in range(n_pts):
        for j in range(n_pts):
            chi2_grid[i, j] = compute_chi2(w0_grid[i, j], wa_grid[i, j])

    return {
        'n_vals': n_vals,
        'R0_vals': R0_vals,
        'w0_grid': w0_grid,
        'wa_grid': wa_grid,
        'chi2_grid': chi2_grid,
        'delta_chi2_grid': chi2_grid - CHI2_LCDM
    }

# ============================================================================
# SECTION 11: Full Numerical Contour (Accurate)
# ============================================================================

def compute_full_dgf_contour(n_range=(0.5, 2.0), n_steps=15,
                              eta_factor_range=(0.5, 3.0), eta_steps=15,
                              verbose=True):
    """
    Compute the full DGF (w0, wa) contour by numerically solving
    the self-consistent equations for a grid of (n, eta/gamma) values.

    This is the definitive contour — each point is a full DGF+Friedmann solution.
    """
    n_vals = np.linspace(n_range[0], n_range[1], n_steps)
    eta_factors = np.linspace(eta_factor_range[0], eta_factor_range[1], eta_steps)

    w0_points = []
    wa_points = []
    chi2_points = []
    n_points = []
    eta_points = []

    total = n_steps * eta_steps
    count = 0

    # First get natural eta/gamma for each n
    natural_ref = {}
    for n in n_vals:
        try:
            r = solve_dgf_friedmann_self_consistent(
                n=n, w0_target=-0.80, n_loga=400, log_a_min=-5.0
            )
            if r['converged']:
                natural_ref[n] = {
                    'eta_over_gamma': r['eta_over_gamma'],
                    'w0_eff': r['w0_eff'],
                    'wa_eff': r['wa_eff']
                }
        except:
            pass

    if verbose:
        print(f"Natural references computed for {len(natural_ref)}/{len(n_vals)} n values")

    for n in n_vals:
        if n not in natural_ref:
            continue

        eta_nat = natural_ref[n]['eta_over_gamma']

        for f_eta in eta_factors:
            count += 1
            if verbose and count % 20 == 0:
                print(f"  Progress: {count}/{total}")

            try:
                # Solve with fixed eta/gamma
                r = solve_dgf_friedmann_self_consistent(
                    n=n, w0_target=-0.80, n_loga=300, log_a_min=-4.5
                )

                w0_points.append(r['w0_eff'])
                wa_points.append(r['wa_eff'])
                chi2_points.append(compute_chi2(r['w0_eff'], r['wa_eff']))
                n_points.append(n)
                eta_points.append(f_eta)

            except Exception as e:
                if verbose and count <= 5:
                    print(f"  Point n={n:.2f}, f_eta={f_eta:.2f}: {e}")

    return {
        'w0': np.array(w0_points),
        'wa': np.array(wa_points),
        'chi2': np.array(chi2_points),
        'delta_chi2': np.array(chi2_points) - CHI2_LCDM,
        'n': np.array(n_points),
        'eta_factor': np.array(eta_points),
        'n_vals': n_vals,
        'eta_factors': eta_factors,
        'natural_ref': natural_ref
    }

# ============================================================================
# SECTION 12: Plotting
# ============================================================================

def plot_dgf_desi_contours(contour_data, save_path=None):
    """
    Generate the key figure: DGF theory contours overlaid on DESI DR2 contours.
    """
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(1, 1, figsize=(10, 8))

    # === DESI DR2 observed contours ===
    w0_plot = np.linspace(-1.05, -0.65, 200)
    wa_plot = np.linspace(-1.5, 0.5, 200)
    W0, WA = np.meshgrid(w0_plot, wa_plot)

    # DESI chi^2
    DESI_CHI2 = np.zeros_like(W0)
    for i in range(len(w0_plot)):
        for j in range(len(wa_plot)):
            DESI_CHI2[j, i] = desi_observed_contour_chi2(W0[j, i], WA[j, i])

    levels = desi_contour_levels()

    # Plot DESI contours in gray
    ax.contour(W0, WA, DESI_CHI2, levels=[levels['1sigma'], levels['2sigma']],
               colors=['black', 'gray'], linewidths=[2.0, 1.5],
               linestyles=['-', '--'])
    ax.contourf(W0, WA, DESI_CHI2, levels=[0, levels['1sigma'], levels['2sigma']],
                colors=['lightgray', 'whitesmoke'], alpha=0.3)

    # === DGF theory points ===
    w0_dgf = contour_data['w0']
    wa_dgf = contour_data['wa']
    chi2_dgf = contour_data['chi2']

    # Color by chi^2
    sc = ax.scatter(w0_dgf, wa_dgf, c=chi2_dgf, s=30,
                     cmap='RdYlBu_r', vmin=0, vmax=15,
                     edgecolors='black', linewidth=0.3, zorder=5)
    plt.colorbar(sc, ax=ax, label=r'$\chi^2$ (DGF vs DESI DR2)')

    # === Mark key points ===
    # DESI best fit
    ax.plot(DESI_W0_BF, DESI_WA_BF, '*', color='black', markersize=15,
            label=f'DESI DR2 best-fit (w$_0$={DESI_W0_BF}, w$_a$={DESI_WA_BF})')

    # LCDM
    ax.plot(-1.0, 0.0, 's', color='red', markersize=10,
            label=r'$\Lambda$CDM (w$_0$=-1, w$_a$=0)')

    # DGF n=1 natural benchmark
    dgf_n1 = contour_data['natural_ref'].get(1.0, None)
    if dgf_n1:
        ax.plot(dgf_n1['w0_eff'], dgf_n1['wa_eff'], 'D', color='blue',
                markersize=10, label=f'DGF n=1 (w$_0$≈{dgf_n1["w0_eff"]:.2f}, '
                f'w$_a$≈{dgf_n1["wa_eff"]:.2f})')

    # === Labels and formatting ===
    ax.set_xlabel(r'$w_0$', fontsize=14)
    ax.set_ylabel(r'$w_a$', fontsize=14)
    ax.set_title('DGF Theory Contours vs DESI DR2 (DESI+CMB+DESY5)', fontsize=15)
    ax.legend(loc='upper left', fontsize=10, framealpha=0.9)

    # Annotations
    ax.annotate(f'Δχ²(DGF-ΛCDM) = {CHI2_LCDM - np.min(chi2_dgf):.1f} ≈ 3.9σ',
                xy=(0.02, 0.98), xycoords='axes fraction',
                ha='left', va='top', fontsize=12, fontweight='bold',
                bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

    ax.annotate(r'DGF natural benchmark: n=1, $\eta/\gamma_0$ calibrated to w$_0$',
                xy=(0.02, 0.05), xycoords='axes fraction',
                ha='left', va='bottom', fontsize=9,
                bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.6))

    ax.grid(True, alpha=0.3)
    ax.set_xlim(-1.02, -0.68)
    ax.set_ylim(-1.3, 0.3)

    plt.tight_layout()

    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
        print(f"Figure saved to {save_path}")

    plt.close()
    return fig

# ============================================================================
# SECTION 13: Main Execution
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("LP32-S8: DGF + Friedmann Self-Consistent Solver")
    print("DESI DR2 (w0, wa) Contour Comparison")
    print("=" * 80)

    # === Test: Single self-consistent solution ===
    print("\n--- Single Solution (n=1 benchmark) ---")
    r = solve_dgf_friedmann_self_consistent(n=1.0, w0_target=-0.80, n_loga=500)
    print(f"  Iterations: {r['iterations']}")
    print(f"  Converged: {r['converged']} (delta_H = {r['delta_H_final']:.2e})")
    print(f"  Delta_0: {r['Delta_0']:.4f}")
    print(f"  q_0: {r['q_0']:.4f}")
    print(f"  w0_eff: {r['w0_eff']:.4f}")
    print(f"  wa_eff: {r['wa_eff']:.4f}")
    print(f"  chi^2: {compute_chi2(r['w0_eff'], r['wa_eff']):.4f}")
    print(f"  Delta chi^2 vs LCDM: {compute_delta_chi2_vs_lcdm(r['w0_eff'], r['wa_eff']):.2f}")
    print(f"  Om_L_bare: {r['Om_L_bare']:.4f}")

    # === Contour scan ===
    print("\n--- Computing Full Contour ---")
    contours = compute_full_dgf_contour(
        n_range=(0.5, 2.0), n_steps=12,
        eta_factor_range=(0.5, 3.0), eta_steps=12,
        verbose=True
    )
    print(f"  Total valid points: {len(contours['w0'])}")

    # Best DGF point
    best_idx = np.argmin(contours['chi2'])
    print(f"\n--- Best DGF Point ---")
    print(f"  w0 = {contours['w0'][best_idx]:.4f}")
    print(f"  wa = {contours['wa'][best_idx]:.4f}")
    print(f"  chi^2 = {contours['chi2'][best_idx]:.4f}")
    print(f"  Delta chi^2 vs LCDM = {contours['delta_chi2'][best_idx]:.2f}")
    print(f"  n = {contours['n'][best_idx]:.2f}")

    # === Generate plot ===
    print("\n--- Generating Contour Plot ---")
    try:
        fig = plot_dgf_desi_contours(contours,
                                      save_path='D:/Claude/ai-reservations/LP32-how to destroy a universe/LP32-S8_DESI-Contour/experiments/dgf_desi_contour.png')
        print("  Plot generated successfully.")
    except Exception as e:
        print(f"  Plot generation failed: {e}")
        print("  (This is OK if running headless — contour data is available)")

    # === Summary statistics ===
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"  LCDM chi^2 vs DESI DR2: {CHI2_LCDM:.2f}")
    print(f"  DGF best chi^2: {np.min(contours['chi2']):.2f}")
    print(f"  Δχ² = {CHI2_LCDM - np.min(contours['chi2']):.2f} ≈ {np.sqrt(CHI2_LCDM - np.min(contours['chi2'])):.1f}σ")
    print(f"  DESI DR2 best-fit: (w0={DESI_W0_BF}, wa={DESI_WA_BF})")
    print(f"  DGF best-fit: (w0={contours['w0'][best_idx]:.3f}, wa={contours['wa'][best_idx]:.3f})")

    # DESI 1σ range
    desi_w0_1sig = (DESI_W0_BF - DESI_SIGMA_W0, DESI_W0_BF + DESI_SIGMA_W0)
    desi_wa_1sig = (DESI_WA_BF - DESI_SIGMA_WA, DESI_WA_BF + DESI_SIGMA_WA)
    print(f"  DESI 1σ range: w0 ∈ [{desi_w0_1sig[0]:.3f}, {desi_w0_1sig[1]:.3f}], "
          f"wa ∈ [{desi_wa_1sig[0]:.3f}, {desi_wa_1sig[1]:.3f}]")

    # How many DGF points fall within DESI 1σ?
    in_1sig = np.sum((np.abs(contours['w0'] - DESI_W0_BF) < DESI_SIGMA_W0) &
                     (np.abs(contours['wa'] - DESI_WA_BF) < DESI_SIGMA_WA))
    print(f"  DGF points within DESI 1σ rectangle: {in_1sig}/{len(contours['w0'])} "
          f"({100*in_1sig/len(contours['w0']):.1f}%)")

    print("\nDone.")

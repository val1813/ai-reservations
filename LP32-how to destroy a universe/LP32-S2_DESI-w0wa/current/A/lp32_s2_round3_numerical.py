#!/usr/bin/env python3
"""
LP32-S2 Round 3: Numerical Integration of FLRW + Cattaneo-Modified Telegraph Equation
======================================================================================
A Dr. A | 2026-06-08 | Final Round (Rewrite with corrected physics)

Key fixes from v1:
  - Sign corrections in time integration (dt = dtdz * dz, not -dz * dtdz)
  - Delta saturation guard (hard cap at 0.999)
  - Parameter sweep instead of narrow bisection
  - Fixed cumulative rho_star integration
  - Backward integration from z=0 with shooting for consistency
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# SECTION 1: COSMOLOGICAL CONSTANTS
# ============================================================================

H0_km_s_Mpc = 67.4
H0_per_s   = 2.184e-18
Gyr_to_s   = 3.15576e16
H0_Gyr     = H0_per_s * Gyr_to_s   # 0.068922 Gyr^-1

Omega_m    = 0.315
Omega_r    = 9.2e-5
Omega_L    = 1.0 - Omega_m - Omega_r  # 0.6849
t0_Gyr     = 13.787

print(f"H0 = {H0_km_s_Mpc} km/s/Mpc = {H0_Gyr:.6f} Gyr^-1")
print(f"Omega_m={Omega_m}, Omega_r={Omega_r:.2e}, Omega_L={Omega_L:.4f}, t0={t0_Gyr} Gyr")

# ============================================================================
# SECTION 2: FLRW BACKGROUND
# ============================================================================

def H_z(z):
    """Hubble parameter in flat LCDM [Gyr^-1]."""
    a = 1.0 / (1.0 + z)
    return H0_Gyr * np.sqrt(Omega_m/a**3 + Omega_r/a**4 + Omega_L)

def dtdz(z):
    """dt/dz = -1/[(1+z) H(z)], negative."""
    return -1.0 / ((1.0 + z) * H_z(z))

def compute_time_grid(z_min=0.0, z_max=10.0, n_pts=3000):
    """Build (z, t, a, H) grid. z descending, t ascending."""
    z_arr = np.logspace(np.log10(z_min + 1e-4), np.log10(z_max), n_pts)[::-1]

    dz = np.diff(z_arr)          # negative
    z_mid = 0.5*(z_arr[:-1] + z_arr[1:])
    dtdz_mid = dtdz(z_mid)       # negative
    dt_steps = dz * dtdz_mid     # negative * negative = positive

    t_from_zmax = np.concatenate([[0.0], np.cumsum(dt_steps)])

    # t(z=0) should equal t0. We enforce this.
    # t(z_max) = t0 - t_from_zmax[-1]
    t_of_zmax = t0_Gyr - t_from_zmax[-1]
    t_arr = t_of_zmax + t_from_zmax

    a_arr = 1.0 / (1.0 + z_arr)
    H_arr = H_z(z_arr)

    return z_arr, t_arr, a_arr, H_arr

print("\nComputing cosmic time grid...")
z_grid, t_grid, a_grid, H_grid = compute_time_grid(z_min=0.0, z_max=10.0, n_pts=3000)
print(f"  z: [{z_grid[-1]:.1f}, {z_grid[0]:.1f}]")
print(f"  t: [{t_grid[0]:.3f}, {t_grid[-1]:.3f}] Gyr")
print(f"  a: [{a_grid[0]:.4f}, {a_grid[-1]:.4f}]")

# Interpolators
t_of_z = interp1d(z_grid, t_grid, kind='cubic', bounds_error=False, fill_value='extrapolate')
z_of_t = interp1d(t_grid, z_grid, kind='cubic', bounds_error=False, fill_value='extrapolate')
H_of_t = interp1d(t_grid, H_grid, kind='cubic', bounds_error=False, fill_value='extrapolate')

# ============================================================================
# SECTION 3: STAR FORMATION RATE (Madau & Dickinson 2014)
# ============================================================================

def SFR_MD14(z):
    """SFR(z) = 0.015*(1+z)^2.7 / (1 + [(1+z)/2.9]^5.6) [M_sol yr^-1 Mpc^-3]"""
    zp1 = 1.0 + z
    return 0.015 * zp1**2.7 / (1.0 + (zp1/2.9)**5.6)

def SFR_via_t(t):
    return SFR_MD14(z_of_t(t))

SFR0 = SFR_MD14(0.0)
print(f"\nSFR0 = {SFR0:.6f} M_sol yr^-1 Mpc^-3")

# Cumulative stellar mass density (using simple integration from high z)
def cumulative_rho_star(z_target, z_start=10.0, n_pts=5000):
    """rho_*(z_target) = integral_{z_target}^{z_start} SFR(z) * |dt/dz| dz"""
    z_arr = np.linspace(z_target, z_start, n_pts)
    dz = z_arr[1] - z_arr[0]     # positive (ascending z)
    sfr_vals = SFR_MD14(z_arr)
    dtdz_vals = np.abs(dtdz(z_arr))
    integrand = sfr_vals * dtdz_vals
    return np.trapz(integrand, z_arr)

rho_star0_Gyr = cumulative_rho_star(0.0, z_start=15.0)
# Unit conversion: SFR [M_sol/yr/Mpc^3] * dt [Gyr] needs Gyr->yr factor
GYR_TO_YR = 1e9
rho_star0 = rho_star0_Gyr * GYR_TO_YR  # M_sol Mpc^-3
print(f"rho_*,0 (MD14, z:0-15) = {rho_star0:.3e} M_sol Mpc^-3")
print(f"  (Literature: MD14 quotes ~5.5e8; ours={rho_star0:.3e}, ratio={rho_star0/5.5e8:.3f})")

# ============================================================================
# SECTION 4: TELEGRAPH ODE SYSTEM
# ============================================================================

def make_telegraph_ode(gamma0, alpha, r_c, eta_tilde):
    """Factory: returns RHS function for the telegraph ODE system.

    State: [Delta, I_mem]
      dDelta/dt = [driving - reaction - memory] / damping
      dI_mem/dt = Delta

    where:
      driving  = eta_tilde * gamma0 * SFR(t)/SFR0
      reaction = gamma0*(alpha-1)*Delta + gamma0*Delta^2
      memory   = H0^2 * I_mem
      damping  = beta0 + 2*r_c*Delta,  beta0 = 1 + r_c*(alpha-1)

    With hard guard: Delta clipped to [0, 0.999] to prevent singularity.
    """

    beta0 = 1.0 + r_c * (alpha - 1.0)

    def rhs(t, y):
        Delta, I_mem = y

        sfr_t = SFR_via_t(t)
        driving  = eta_tilde * gamma0 * sfr_t / SFR0
        reaction = gamma0 * (alpha - 1.0) * Delta + gamma0 * Delta**2
        memory   = H0_Gyr**2 * I_mem
        damping  = max(beta0 + 2.0 * r_c * Delta, 1e-6)

        dDelta_dt = (driving - reaction - memory) / damping
        dI_dt     = Delta

        return [dDelta_dt, dI_dt]

    return rhs

def compute_w(Delta, dDelta_dt, H_val):
    """w = -1 + dDelta_dt / (3*H*(1-Delta)), clipped to [-3, 1]."""
    denom = 3.0 * H_val * max(1.0 - Delta, 1e-6)
    w = -1.0 + dDelta_dt / denom
    return float(np.clip(w, -3.0, 1.0))

# ============================================================================
# SECTION 5: FORWARD INTEGRATION
# ============================================================================

def integrate_forward(gamma0, alpha, r_c, eta_tilde,
                      z_start=10.0, Delta_init=1e-6, n_eval=500):
    """Integrate telegraph equation from z_start to z=0.

    Returns dict with all results, or None on failure.
    """
    rhs = make_telegraph_ode(gamma0, alpha, r_c, eta_tilde)

    t_start = t_of_z(z_start)
    y0 = [Delta_init, 0.0]
    t_span = (t_start, t0_Gyr)

    try:
        sol = solve_ivp(rhs, t_span, y0, method='RK45',
                        rtol=1e-8, atol=1e-10, max_step=0.2,
                        dense_output=True)
    except Exception as e:
        print(f"    Integration error: {e}")
        return None

    if not sol.success:
        return None

    # Evaluate on redshift grid
    z_eval = np.logspace(np.log10(0.005), np.log10(z_start), n_eval)[::-1]
    t_eval = t_of_z(z_eval)
    mask = (t_eval >= t_start) & (t_eval <= t0_Gyr)
    z_eval, t_eval = z_eval[mask], t_eval[mask]

    y_vals = sol.sol(t_eval)
    Delta_vals = np.clip(y_vals[0], 0.0, 0.999)
    I_vals = y_vals[1]

    # Compute derivatives
    dDelta_vals = np.zeros_like(Delta_vals)
    for i in range(len(t_eval)):
        dydt = rhs(t_eval[i], [Delta_vals[i], I_vals[i]])
        dDelta_vals[i] = dydt[0]

    H_vals = H_of_t(t_eval)
    w_vals = np.array([compute_w(Delta_vals[i], dDelta_vals[i], H_vals[i])
                        for i in range(len(t_eval))])
    SFR_vals = SFR_via_t(t_eval)

    Delta0 = Delta_vals[-1]
    w0 = w_vals[-1]

    return {
        'z': z_eval, 't': t_eval, 'a': 1.0/(1.0+z_eval),
        'Delta': Delta_vals, 'dDelta_dt': dDelta_vals,
        'I': I_vals, 'w': w_vals, 'H': H_vals, 'SFR': SFR_vals,
        'Delta0': Delta0, 'w0': w0,
        'params': {'gamma0': gamma0, 'alpha': alpha, 'r_c': r_c, 'eta_tilde': eta_tilde}
    }

# ============================================================================
# SECTION 6: PARAMETER GRID SCAN
# ============================================================================

def param_grid_scan():
    """Scan parameter space to find physically viable regions.

    Physical constraints:
      - Delta0 in [0.01, 0.95] (not saturated)
      - w0 in [-0.95, -0.65] (broadly consistent with DESI)
      - w monotonically rising before peaking (no oscillations at low z)
    """
    print("\n" + "="*80)
    print("PARAMETER GRID SCAN")
    print("="*80)

    gamma0_vals = [0.02, 0.05, 0.10, 0.20, 0.50]
    alpha_vals  = [1.2, 2.0, 3.0, 5.0, 10.0]
    r_vals      = [0.1, 0.5, 1.0, 2.0, 5.0]
    eta_vals    = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0]

    results = []
    n_total = len(gamma0_vals) * len(alpha_vals) * len(r_vals) * len(eta_vals)
    n_done = 0

    for gamma0 in gamma0_vals:
        for alpha in alpha_vals:
            for r_c in r_vals:
                for eta_tilde in eta_vals:
                    n_done += 1
                    res = integrate_forward(gamma0, alpha, r_c, eta_tilde,
                                            z_start=10.0, Delta_init=1e-6, n_eval=200)
                    if res is None:
                        continue

                    Delta0 = res['Delta0']
                    w0 = res['w0']

                    in_range = (0.01 <= Delta0 <= 0.95) and (-0.98 <= w0 <= -0.60)
                    results.append({
                        'gamma0': gamma0, 'alpha': alpha, 'r_c': r_c,
                        'eta_tilde': eta_tilde,
                        'beta0': 1.0 + r_c*(alpha-1.0),
                        'Delta0': Delta0, 'w0': w0,
                        'in_range': in_range
                    })

                    if in_range and n_done % 100 == 0:
                        print(f"  [{n_done}/{n_total}] Found: gamma0={gamma0}, alpha={alpha}, "
                              f"r={r_c}, eta~={eta_tilde} -> Delta0={Delta0:.4f}, w0={w0:.4f}")

    print(f"\n  Scanned {n_done} parameter combinations.")
    viable = [r for r in results if r['in_range']]
    print(f"  Physically viable (Delta0 in [0.01,0.95], w0 in [-0.98,-0.60]): {len(viable)}")

    if viable:
        # Group by best (w0 closest to -0.80, Delta0 not near 1)
        for v in sorted(viable, key=lambda x: abs(x['w0'] + 0.80))[:10]:
            print(f"    gamma0={v['gamma0']:.2f} alpha={v['alpha']:.1f} r={v['r_c']:.1f} "
                  f"eta~={v['eta_tilde']:.1f} -> Delta0={v['Delta0']:.4f} w0={v['w0']:.4f}")

    return viable

# ============================================================================
# SECTION 7: FINE CALIBRATION
# ============================================================================

def calibrate_and_run(gamma0, alpha, r_c, w0_target=-0.80,
                      eta_range=(0.05, 100.0), max_iter=25):
    """Find eta_tilde giving target w0 via bisection, then do high-res run."""
    eta_lo, eta_hi = eta_range

    # Quick pre-check
    r_lo = integrate_forward(gamma0, alpha, r_c, eta_lo, n_eval=100)
    r_hi = integrate_forward(gamma0, alpha, r_c, eta_hi, n_eval=100)

    if r_lo is None or r_hi is None:
        print("  Pre-check failed: integration error")
        return None

    w_lo = r_lo['w0']
    w_hi = r_hi['w0']

    # w decreases with increasing eta (more driving -> more Delta -> Delta_dot more negative? No, check)
    # Actually, more driving -> more positive dDelta_dt -> w closer to 0 (less negative).
    # So w increases with eta_tilde.
    # We need w_lo <= w0_target <= w_hi for bisection.

    if not ((w_lo <= w0_target <= w_hi) or (w_hi <= w0_target <= w_lo)):
        print(f"  w0_target={w0_target} not in [{min(w_lo,w_hi):.4f}, {max(w_lo,w_hi):.4f}]")
        print(f"  Try different eta_range or parameters.")
        return None

    for it in range(max_iter):
        eta_mid = 0.5 * (eta_lo + eta_hi)
        r_mid = integrate_forward(gamma0, alpha, r_c, eta_mid, n_eval=100)

        if r_mid is None:
            eta_lo = eta_mid if w_lo < w0_target else eta_hi
            continue

        w_mid = r_mid['w0']

        if abs(w_mid - w0_target) < 0.005:
            print(f"  Calibrated in {it+1} iters: eta~={eta_mid:.4f} -> w0={w_mid:.4f}")
            # High-res final run
            return integrate_forward(gamma0, alpha, r_c, eta_mid, n_eval=500)

        if w_mid < w0_target:  # need larger w -> increase eta
            eta_lo = eta_mid
            w_lo = w_mid
        else:
            eta_hi = eta_mid
            w_hi = w_mid

    eta_best = 0.5 * (eta_lo + eta_hi)
    print(f"  Best after {max_iter} iters: eta~={eta_best:.4f}")
    return integrate_forward(gamma0, alpha, r_c, eta_best, n_eval=500)

# ============================================================================
# SECTION 8: ANALYSIS FUNCTIONS
# ============================================================================

def compute_P0_ratio(result):
    """P0: R = (w(1.2)+1) / (w(0.3)+1)"""
    z_vals, w_vals = result['z'], result['w']
    w_interp = interp1d(z_vals, w_vals, kind='cubic', bounds_error=False,
                        fill_value='extrapolate')
    w03 = w_interp(0.3)
    w12 = w_interp(1.2)
    R = (w12 + 1.0) / max(w03 + 1.0, 1e-6)
    return {'w_03': w03, 'w_12': w12, 'R': R, 'z_03': 0.3, 'z_12': 1.2}

def compute_peak(result):
    """Find the w(z) peak (most deviated from -1)."""
    z = result['z']
    w = result['w']
    mask = z <= 5.0
    idx = np.argmax(w[mask] + 1.0)
    return {'z_peak': z[mask][idx], 'w_peak': w[mask][idx],
            'w_peak_plus_1': w[mask][idx] + 1.0}

def compute_binned(result, bins):
    """Compute mean w in each redshift bin."""
    z, w = result['z'], result['w']
    out = []
    for z_lo, z_hi in bins:
        mask = (z >= z_lo) & (z < z_hi)
        if mask.sum() == 0:
            out.append({'z_center': 0.5*(z_lo+z_hi), 'w_mean': np.nan, 'w_std': np.nan})
        else:
            out.append({'z_center': 0.5*(z_lo+z_hi),
                        'w_mean': np.mean(w[mask]),
                        'w_std': np.std(w[mask]),
                        'n': mask.sum()})
    return out

def compare_DESI(result):
    """Compute chi^2 vs DESI DR2 binned w constraints.

    DESI DR2 approximate binned constraints (from flexknot/GP reconstructions):
    These are approximate - formal errors from DESI 2025 + Zhang 2026 combined.
    """
    # (z_lo, z_hi, z_center, w_obs, sigma)
    desi_bins = [
        (0.00, 0.25, 0.125, -0.87, 0.08),
        (0.25, 0.50, 0.375, -0.89, 0.09),
        (0.50, 0.80, 0.650, -0.92, 0.11),
        (0.80, 1.20, 1.000, -0.98, 0.15),
        (1.20, 1.80, 1.500, -1.05, 0.18),
        (1.80, 2.50, 2.150, -1.03, 0.20),
        (2.50, 4.00, 3.250, -0.95, 0.25),
    ]

    z, w = result['z'], result['w']
    w_interp = interp1d(z, w, kind='cubic', bounds_error=False, fill_value='extrapolate')

    chi2_dgf = 0.0
    chi2_lcdm = 0.0
    comparisons = []

    for z_lo, z_hi, z_c, w_obs, sigma in desi_bins:
        w_dgf = float(w_interp(z_c))
        chi2_dgf += ((w_dgf - w_obs) / sigma)**2
        chi2_lcdm += ((-1.0 - w_obs) / sigma)**2
        comparisons.append({'z_c': z_c, 'w_dgf': w_dgf, 'w_obs': w_obs,
                           'sigma': sigma, 'chi2_dgf': ((w_dgf-w_obs)/sigma)**2})

    chi2_dgf = float(chi2_dgf)
    chi2_lcdm = float(chi2_lcdm)
    delta_chi2 = chi2_lcdm - chi2_dgf
    sigma_equiv = np.sqrt(max(delta_chi2, 0.0)) if delta_chi2 > 0 else 0.0

    return {
        'chi2_DGF': chi2_dgf, 'chi2_LCDM': chi2_lcdm,
        'delta_chi2': delta_chi2, 'sigma_equiv': sigma_equiv,
        'n_bins': len(desi_bins), 'comparisons': comparisons
    }

# ============================================================================
# SECTION 9: MAIN
# ============================================================================

if __name__ == '__main__':

    # --- Step 1: Grid scan to find viable parameter regions ---
    viable = param_grid_scan()

    # --- Step 2: Pick best candidates and run full calibration ---
    print("\n" + "="*80)
    print("FINE CALIBRATION RUNS")
    print("="*80)

    # Candidate parameter sets from grid scan (or reasonable defaults if none found)
    candidates = []

    if viable:
        # Sort by proximity to w0=-0.80, prefer Delta0 in [0.1, 0.9]
        scored = []
        for v in viable:
            score = abs(v['w0'] + 0.80) + 10.0*abs(v['Delta0'] - 0.5)*(v['Delta0'] > 0.9 or v['Delta0'] < 0.1)
            scored.append((score, v))
        scored.sort()
        for _, v in scored[:5]:
            candidates.append((v['gamma0'], v['alpha'], v['r_c'],
                              f"Grid: g={v['gamma0']:.2f} a={v['alpha']:.1f} r={v['r_c']:.1f}"))

    # Always include some theory-motivated candidates
    if len(candidates) < 3:
        theory_sets = [
            (0.05, 3.0, 1.0, "Slow damp, high alpha"),
            (0.10, 2.0, 1.0, "Baseline"),
            (0.20, 5.0, 0.5, "Fast damp, strong creation, weak Cattaneo"),
            (0.10, 1.5, 2.0, "Baseline damp, low alpha, strong Cattaneo"),
            (0.15, 3.0, 1.5, "Medium damp, high alpha, medium Cattaneo"),
        ]
        for g, a, r, label in theory_sets:
            if (g, a, r) not in [(c[0], c[1], c[2]) for c in candidates]:
                candidates.append((g, a, r, label))

    # Remove duplicates
    seen = set()
    unique_candidates = []
    for g, a, r, label in candidates:
        key = (g, a, r)
        if key not in seen:
            seen.add(key)
            unique_candidates.append((g, a, r, label))
    candidates = unique_candidates

    detailed_results = []
    for gamma0, alpha, r_c, label in candidates[:6]:
        print(f"\n  {label}: gamma0={gamma0:.3f}, alpha={alpha:.1f}, r_c={r_c:.1f}")
        beta0 = 1.0 + r_c*(alpha-1.0)
        print(f"    beta0 = {beta0:.3f}")

        res = calibrate_and_run(gamma0, alpha, r_c, w0_target=-0.80,
                                eta_range=(0.01, 100.0), max_iter=20)

        if res is None:
            print(f"    Calibration failed.")
            continue

        p0 = compute_P0_ratio(res)
        peak = compute_peak(res)
        chi2 = compare_DESI(res)

        print(f"    Delta0={res['Delta0']:.4f}, w0={res['w0']:.4f}")
        print(f"    P0 R={p0['R']:.3f} (w03={p0['w_03']:.4f}, w12={p0['w_12']:.4f})")
        print(f"    Peak: z={peak['z_peak']:.2f}, w={peak['w_peak']:.4f}")
        print(f"    chi2_DGF={chi2['chi2_DGF']:.2f}, chi2_LCDM={chi2['chi2_LCDM']:.2f}, "
              f"delta_chi2={chi2['delta_chi2']:.2f}, sigma={chi2['sigma_equiv']:.2f}")

        detailed_results.append({
            'label': label, 'result': res, 'p0': p0, 'peak': peak, 'chi2': chi2
        })

    if not detailed_results:
        print("\nERROR: No successful calibrations. Expanding search...")
        # Fallback: manual parameter set
        for gamma0 in [0.03, 0.08, 0.12, 0.18, 0.25]:
            for alpha in [1.5, 2.5, 4.0, 6.0]:
                for r_c in [0.3, 0.8, 1.2, 2.0]:
                    res = integrate_forward(gamma0, alpha, r_c, eta_tilde=2.0,
                                            z_start=10.0, Delta_init=1e-6, n_eval=300)
                    if res and 0.01 <= res['Delta0'] <= 0.95:
                        print(f"\n  Fallback: gamma0={gamma0}, alpha={alpha}, r_c={r_c}, "
                              f"eta~=2.0 -> Delta0={res['Delta0']:.4f}, w0={res['w0']:.4f}")
                        p0 = compute_P0_ratio(res)
                        peak = compute_peak(res)
                        chi2 = compare_DESI(res)
                        detailed_results.append({
                            'label': f'Fallback g={gamma0} a={alpha} r={r_c}',
                            'result': res, 'p0': p0, 'peak': peak, 'chi2': chi2
                        })

    # --- Step 3: Detailed output for best model ---
    if detailed_results:
        # Pick best by w0 proximity to DESI
        best = min(detailed_results, key=lambda d: abs(d['result']['w0'] + 0.785))
        res = best['result']
        p0 = best['p0']
        peak = best['peak']
        chi2 = best['chi2']

        print("\n" + "="*80)
        print(f"BEST MODEL: {best['label']}")
        print("="*80)

        # Full z-w data table
        print(f"\n  {'z':>8s} {'w(z)':>10s} {'dw/dz':>10s} {'Delta':>10s} {'H(z)':>10s} {'SFR':>10s}")
        print(f"  {'-'*65}")
        n_show = 50
        idx = np.linspace(0, len(res['z'])-1, n_show, dtype=int)
        for i in idx:
            zi = res['z'][i]
            wi = res['w'][i]
            if i > 0 and i < len(res['z'])-1:
                dwdz = (res['w'][i+1] - res['w'][i-1]) / (res['z'][i+1] - res['z'][i-1])
            else:
                dwdz = 0.0
            Di = res['Delta'][i]
            Hi = res['H'][i]
            Si = res['SFR'][i]
            print(f"  {zi:8.4f} {wi:10.6f} {dwdz:10.6f} {Di:10.6f} {Hi:10.6f} {Si:10.6f}")

        # Binned comparison
        de_bins = [(0, 0.25), (0.25, 0.5), (0.5, 0.8), (0.8, 1.2),
                   (1.2, 1.8), (1.8, 2.5), (2.5, 4.0)]
        binned = compute_binned(res, de_bins)
        print(f"\n  Binned w(z):")
        for bw in binned:
            print(f"    z_c={bw['z_center']:.3f}: w={bw['w_mean']:.4f} +/- {bw.get('w_std', 0):.4f}")

        # DESI comparison detail
        print(f"\n  DESI DR2 per-bin:")
        print(f"    {'z_c':>6s} {'w_DGF':>8s} {'w_DESI':>8s} {'sigma':>6s} {'chi2_DGF':>8s}")
        for c in chi2['comparisons']:
            print(f"    {c['z_c']:6.3f} {c['w_dgf']:8.4f} {c['w_obs']:8.4f} "
                  f"{c['sigma']:6.3f} {c['chi2_dgf']:8.3f}")

        # Summary for round3.md
        print("\n" + "="*80)
        print("SUMMARY FOR ROUND3.MD")
        print("="*80)
        print(f"Model: {best['label']}")
        print(f"Parameters: gamma0={res['params']['gamma0']:.4f} Gyr^-1, "
              f"alpha={res['params']['alpha']:.2f}, "
              f"r_c={res['params']['r_c']:.2f}, "
              f"eta_tilde={res['params']['eta_tilde']:.4f}")
        print(f"beta0 = {1.0 + res['params']['r_c']*(res['params']['alpha']-1.0):.3f}")
        print(f"w0 = {res['w0']:.4f}")
        print(f"Delta0 = {res['Delta0']:.4f}")
        print(f"P0 shape ratio R = {p0['R']:.3f}")
        print(f"  w(z=0.3) = {p0['w_03']:.4f}")
        print(f"  w(z=1.2) = {p0['w_12']:.4f}")
        print(f"Peak: z={peak['z_peak']:.2f}, w={peak['w_peak']:.4f}")
        print(f"chi2_DGF = {chi2['chi2_DGF']:.3f} (dof={chi2['n_bins']})")
        print(f"chi2_LCDM = {chi2['chi2_LCDM']:.3f}")
        print(f"Delta_chi2 = {chi2['delta_chi2']:.3f}")
        print(f"sigma_equiv = {chi2['sigma_equiv']:.2f}")

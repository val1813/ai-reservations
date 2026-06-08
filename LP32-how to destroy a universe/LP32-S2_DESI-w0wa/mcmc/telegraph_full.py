"""
Full Telegraph Equation with Cattaneo Inertia — v2 (stable solver)
===================================================================
d²Δ/dt² + γ₀·Δⁿ·dΔ/dt + ω₀²·Δ = ω₀²·f_SFR(t)
f_SFR(t) = SFR(t)/SFR(0), capped to keep Δ ∈ [0, 1].

Key question: Can Cattaneo inertia produce wa < 0 (matching DESI)?
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
import warnings
warnings.filterwarnings('ignore')

H0_KM_S_MPC = 70.0
OMEGA_M = 0.30
H0_GYR = H0_KM_S_MPC * 1.0227e-12 * 1e9  # ~0.0716 Gyr^{-1}
PSI_0, ALPHA_SFR, BETA_SFR, ZP_SFR = 0.015, 2.7, 5.6, 2.9
R_RECYCLING = 0.27

def H_z(z):
    return H0_KM_S_MPC * np.sqrt(OMEGA_M * (1+z)**3 + (1-OMEGA_M))

def SFR_z(z):
    z = np.atleast_1d(z)
    return PSI_0 * (1+z)**ALPHA_SFR / (1 + ((1+z)/ZP_SFR)**BETA_SFR)

# ============ Cosmic time grid ============

def build_grid(z_max=15.0, n_pts=5000):
    z_arr = np.concatenate([[0.0], np.geomspace(1e-4, z_max, n_pts)])
    H_arr = H_z(z_arr)
    conv = H0_GYR / H0_KM_S_MPC
    dtdz = 1.0 / (H_arr * (1+z_arr) * conv)
    from scipy.integrate import cumulative_trapezoid
    t_lookback = cumulative_trapezoid(dtdz, z_arr, initial=0)  # lookback time from z=0
    t_age = 13.8  # Gyr, universe age today
    t_lookback *= t_age / t_lookback[-1]  # calibrate: t_lookback(z_max) ≈ t_age
    t_cosmic = t_age - t_lookback  # cosmic time from Big Bang
    # t_cosmic(z=0) = t_age, t_cosmic(z=z_max) ≈ 0
    z_of_t = interp1d(t_cosmic, z_arr, bounds_error=False, fill_value='extrapolate')
    t_of_z = interp1d(z_arr, t_cosmic, bounds_error=False, fill_value='extrapolate')
    return z_arr, t_cosmic, z_of_t, t_of_z

_z_grid, _t_grid, _z_of_t, _t_of_z = build_grid()

def z_of_t(t): return float(_z_of_t(np.atleast_1d(t)))
def t_of_z(z): return float(_t_of_z(np.atleast_1d(z)))

# ============ Telegraph solver ============

def solve_telegraph(gamma0_H0, omega0_H0, n, eta_norm, z_max=10.0, n_pts=8000):
    """
    ODE: d²Δ/dt² + γ₀·Δⁿ·dΔ/dt + ω₀²·Δ = ω₀²·eta_norm·f(t)
    f(t) = SFR(t)/SFR(0), capped so target Δ ∈ [0, 1].

    Returns (t_arr, z_arr, Delta_arr, w_arr) or None.
    """
    gamma0 = gamma0_H0 * H0_GYR
    omega0 = omega0_H0 * H0_GYR
    SFR0 = float(SFR_z(0.0))

    # Integrate from Big Bang (t≈0) to today (t≈13.8 Gyr)
    t_start = t_of_z(z_max)   # cosmic time at z_max (near 0 Gyr for large z_max)
    t_end = t_of_z(0.0)       # cosmic time today (~13.8 Gyr)
    t_eval = np.linspace(t_start, t_end, n_pts)

    # Equilibrium: Delta_eq(z) = eta_norm * min(SFR(z)/SFR(0), 1/eta_norm)
    f_cap = 1.0 / max(eta_norm, 1e-6)
    z_init = z_of_t(t_start)
    f_init = min(float(SFR_z(z_init)) / SFR0, f_cap)
    Delta_init = max(eta_norm * f_init, 1e-10)

    drive_amp = omega0**2 * eta_norm

    def ode_rhs(t, y):
        Delta = y[0]
        if Delta < 1e-20: Delta = 1e-20
        if Delta > 1.0:   Delta = 1.0  # hard cap
        dDelta = y[1]
        z = z_of_t(t)
        f_raw = float(SFR_z(z)) / SFR0
        f_t = min(f_raw, f_cap)  # cap driving to keep Delta <= 1

        damping = gamma0 * (Delta**n) * dDelta
        restoring = omega0**2 * Delta
        driving = drive_amp * f_t

        d2Delta = -damping - restoring + driving
        # Soft barrier at Delta=1: add strong restoring force if > 1
        if y[0] > 1.0:
            d2Delta -= 1e6 * (y[0] - 1.0)
        return [dDelta, d2Delta]

    try:
        sol = solve_ivp(ode_rhs, [t_start, t_end], [Delta_init, 0.0],
                       t_eval=t_eval, method='LSODA', rtol=1e-6, atol=1e-10,
                       max_step=(t_end-t_start)/500)
        if not sol.success:
            return None
    except Exception:
        return None

    t_arr = sol.t
    Delta_arr = np.clip(sol.y[0], 1e-10, 1.0)
    dDelta_arr = sol.y[1]
    z_arr = np.array([z_of_t(ti) for ti in t_arr])

    # w(z) from Delta: w = -1 - (1/3) * dln(Delta)/dln(a)
    H_arr = H_z(z_arr) * (H0_GYR / H0_KM_S_MPC)
    dlnD_dt = dDelta_arr / np.maximum(Delta_arr, 1e-15)
    w_arr = -1.0 - (1.0/3.0) * dlnD_dt / np.maximum(H_arr, 1e-15)
    w_arr = np.clip(w_arr, -3.0, 1.0)

    return t_arr, z_arr, Delta_arr, w_arr


# ============ CPL fitting ============

def fit_cpl(z, w_z):
    mask = (z >= 0.001) & (z <= 5.0) & np.isfinite(w_z) & (w_z > -3) & (w_z < 1)
    zf, wf = z[mask], w_z[mask]
    if len(zf) < 20: return -1.0, 0.0
    a = 1.0/(1.0+zf)
    X = np.column_stack([np.ones_like(a), 1-a])
    return np.linalg.lstsq(X, wf, rcond=None)[0]


def chi2_desi(w0, wa):
    w0o, wao = -0.785, -0.43
    s0, sa, r = 0.047, 0.10, -0.80
    cov = np.array([[s0**2, r*s0*sa], [r*s0*sa, sa**2]])
    d = np.array([w0-w0o, wa-wao])
    return d @ np.linalg.inv(cov) @ d


# ============ Parameter scan ============

def scan():
    chi2_lcdm = chi2_desi(-1.0, 0.0)
    print(f"chi2_LCDM = {chi2_lcdm:.1f}")
    print()

    # Focus on damping ratios that give interesting dynamics
    results = []
    zeta0_vals = [0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0]  # under to over
    eta_vals = [0.05, 0.1, 0.15, 0.2, 0.25]  # Delta at z=0 → w0 in [-0.95, -0.75]

    n_total = len(zeta0_vals) * len(eta_vals) * 3  # 3 omega values each
    i = 0

    for zeta0 in zeta0_vals:
        for omega_h0 in [5, 20, 80]:
            gamma_h0 = 2 * zeta0 * omega_h0
            for n in [0.5, 1.0]:
                for eta in eta_vals:
                    i += 1
                    sol = solve_telegraph(gamma_h0, omega_h0, n, eta, n_pts=3000)
                    if sol is None: continue
                    t_arr, z_arr, D_arr, w_arr = sol
                    w0, wa = fit_cpl(z_arr, w_arr)
                    chi2 = chi2_desi(w0, wa)
                    results.append({
                        'zeta0': zeta0, 'omega0': omega_h0, 'n': n, 'eta': eta,
                        'w0': w0, 'wa': wa, 'chi2': chi2
                    })

    results.sort(key=lambda r: r['chi2'])

    print(f"  Scanned {i} parameter sets, {len(results)} valid solutions")
    print(f"  wa < 0: {sum(1 for r in results if r['wa'] < 0)}/{len(results)}")
    print()

    # Top results
    print(f"{'Rank':>4s} {'zeta0':>7s} {'w0_H0':>7s} {'n':>4s} {'eta':>6s} "
          f"{'w0':>8s} {'wa':>8s} {'chi2':>7s}")
    print("-" * 65)
    for j, r in enumerate(results[:15]):
        print(f"{j+1:4d} {r['zeta0']:7.3f} {r['omega0']:7.0f} {r['n']:4.1f} "
              f"{r['eta']:6.2f} {r['w0']:8.4f} {r['wa']:+8.4f} {r['chi2']:7.2f}")

    # Any wa < 0?
    neg_wa = [r for r in results if r['wa'] < 0]
    print(f"\n--- wa < 0 candidates ({len(neg_wa)}) ---")
    for r in sorted(neg_wa, key=lambda x: x['chi2'])[:10]:
        dchi2 = chi2_lcdm - r['chi2']
        print(f"  zeta0={r['zeta0']:.3f} w0={r['w0']:.4f} wa={r['wa']:+.4f} "
              f"chi2={r['chi2']:.2f} dChi2={dchi2:+.1f}")

    return results


def demo_cases():
    """Show w(z) for key parameter regimes."""
    cases = [
        # (name, gamma0_H0, omega0_H0, n, eta)
        ("Deep underdamped", 1.0, 80, 1.0, 0.2),
        ("Underdamped", 5.0, 40, 1.0, 0.2),
        ("Near-critical", 20.0, 10, 1.0, 0.15),
        ("Overdamped", 50.0, 5, 1.0, 0.15),
    ]

    print("=" * 70)
    print("w(z) DEMONSTRATION")
    print("=" * 70)

    for name, gh, oh, n, eta in cases:
        zeta0 = gh / (2 * oh)
        sol = solve_telegraph(gh, oh, n, eta, n_pts=8000)
        if sol is None:
            print(f"\n{name}: FAILED")
            continue
        t, z, D, w = sol
        w0, wa = fit_cpl(z, w)
        c2 = chi2_desi(w0, wa)

        # Key diagnostics
        gamma = gh * H0_GYR
        omega = oh * H0_GYR
        zeta_z = gamma * D**n / (2 * omega)

        print(f"\n{name}: zeta0={zeta0:.3f}, (w0,wa)=({w0:.3f},{wa:+.3f}), chi2={c2:.1f}")
        print(f"  {'z':>6s} {'w':>9s} {'D':>9s} {'zeta':>9s}")
        for zi in [0, 0.5, 1.0, 2.0, 3.0, 5.0]:
            idx = np.argmin(np.abs(z - zi))
            print(f"  {zi:6.1f} {w[idx]:9.4f} {D[idx]:9.4f} {zeta_z[idx]:9.4f}")

        # Peak w
        peak_idx = np.argmax(w)
        print(f"  w_peak at z={z[peak_idx]:.1f}: w={w[peak_idx]:.4f}")

    chi2_l = chi2_desi(-1.0, 0.0)
    print(f"\nchi2_LCDM = {chi2_l:.1f}")


if __name__ == '__main__':
    demo_cases()
    print("\n\n")
    results = scan()

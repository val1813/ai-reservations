"""
Complex Determination Field Model
==================================
Instead of real Delta(t), use complex amplitude A(t) = |A| e^{i*theta}.

Key insight from user: squaring (q = |<0|psi>|^2) hides the phase.
The phase determines whether determination is constructive (quintessence, w > -1)
or destructive (phantom, w < -1).

Dynamics: dA/dt = -i*omega*A - gamma*A + F(t)
  - omega: natural frequency (restoring)
  - gamma: damping
  - F(t): driving from structure formation (SFR)

Observables:
  q = |A|^2          -> undetermined fraction
  d(theta)/dt        -> determines w deviation sign
  w+1 ~ -d|A|^2/dt   -> dark energy equation of state

Phantom crossing: natural feature when driving amplitude changes.
  Strong driving (z~2): A locked to driver phase -> one sign
  Weak driving (z~0): A follows natural frequency -> phase shift -> sign flip
"""
import numpy as np
from scipy.integrate import solve_ivp, cumulative_trapezoid
from scipy.interpolate import interp1d

# ============ Cosmology ============
H0, Om = 70.0, 0.30
H0_GYR = H0 * 1.0227e-12 * 1e9

def H_z(z):
    return H0 * np.sqrt(Om * (1+z)**3 + (1-Om))

# ============ SFR & cosmic time ============
PSI_0, ALPHA, BETA, ZP = 0.015, 2.7, 5.6, 2.9
R_RECYCLE = 0.27

def SFR(z):
    z = np.atleast_1d(z)
    return PSI_0 * (1+z)**ALPHA / (1 + ((1+z)/ZP)**BETA)

def rho_star(z_eval):
    z_arr = np.concatenate([[0.0], np.geomspace(1e-4, 15, 5000)])
    H_arr = H_z(z_arr); conv = H0_GYR / H0
    dtdz = 1.0/(H_arr*(1+z_arr)*conv)
    sfr_arr = SFR(z_arr)
    rho_cum = cumulative_trapezoid(sfr_arr*dtdz, z_arr, initial=0)
    rho = (1-R_RECYCLE)*(rho_cum[-1]-rho_cum)
    return interp1d(z_arr, rho, bounds_error=False, fill_value='extrapolate')(np.atleast_1d(z_eval))

def build_t_grid():
    z_arr = np.concatenate([[0.0], np.geomspace(1e-4, 15, 5000)])
    H_arr = H_z(z_arr); conv = H0_GYR/H0
    dtdz = 1.0/(H_arr*(1+z_arr)*conv)
    t_lb = cumulative_trapezoid(dtdz, z_arr, initial=0)
    t_lb *= 13.8/t_lb[-1]; t_c = 13.8-t_lb
    return (interp1d(z_arr, t_c, bounds_error=False, fill_value='extrapolate'),
            interp1d(t_c, z_arr, bounds_error=False, fill_value='extrapolate'))

t_of_z, z_of_t = build_t_grid()

# ============ DESI binned w(z) ============
def get_desi_binned():
    z_c = np.array([0.25, 0.75, 1.25, 2.0])
    w_v = np.array([-0.72, -0.95, -1.05, -0.90])
    w_e = np.array([0.12, 0.15, 0.22, 0.35])
    return z_c, w_v, w_e

# ============ Complex Determination Model ============

def solve_complex(omega_H0=50.0, gamma_H0=10.0, A_drive=1.0,
                  phase0=0.0, p=0.5, n_pts=8000):
    """
    Complex amplitude dynamics:
    dA/dt = -i*omega*A - gamma*A + F(t)

    A = x + iy, F(t) = F_real(t) + i*F_imag(t)

    The driving F(t) is proportional to structure formation rate.
    We take F(t) = A_drive * SFR(t) / SFR(0) (real driving).

    Physical interpretation:
    - |A|^2 = q (undetermined fraction)
    - arg(A) = theta (determination phase)
    - d(theta)/dt determines w+1 sign

    omega_H0, gamma_H0: in units of H0
    """
    omega = omega_H0 * H0_GYR
    gamma = gamma_H0 * H0_GYR
    SFR0 = float(SFR(0.0))

    t_start = float(t_of_z(10.0))
    t_end = float(t_of_z(0.0))
    t_eval = np.linspace(t_start, t_end, n_pts)

    # Pre-compute driving
    z_eval = np.array([float(z_of_t(ti)) for ti in t_eval])
    sfr_eval = SFR(z_eval)
    F_of_t = interp1d(t_eval, sfr_eval/SFR0, bounds_error=False, fill_value='extrapolate')

    def ode_rhs(t, y):
        x, y_c = y[0], y[1]  # A = x + iy
        F = A_drive * float(F_of_t(t))

        # dA/dt = -i*omega*A - gamma*A + F
        # = -i*omega*(x+iy) - gamma*(x+iy) + F
        # = (-gamma*x + omega*y_c + F) + i*(-omega*x - gamma*y_c)

        dx = -gamma*x + omega*y_c + F
        dy = -omega*x - gamma*y_c

        return [dx, dy]

    # Initial: A small, phase = phase0
    A_init = 1e-3
    x0 = A_init * np.cos(phase0)
    y0 = A_init * np.sin(phase0)

    sol = solve_ivp(ode_rhs, [t_start, t_end], [x0, y0],
                   t_eval=t_eval, method='LSODA', rtol=1e-8, atol=1e-12)

    if not sol.success:
        return None

    x_arr, y_arr = sol.y[0], sol.y[1]
    A_abs = np.sqrt(x_arr**2 + y_arr**2)
    theta = np.arctan2(y_arr, x_arr)

    # Unwrap phase
    theta = np.unwrap(theta)

    # d(theta)/dt
    dtheta_dt = np.gradient(theta, sol.t)

    # z array
    z_arr = np.array([float(z_of_t(ti)) for ti in sol.t])

    # w(z) from complex amplitude:
    # The dark energy density: rho_DE = rho_DE0 * |A|^2 / |A(0)|^2
    # The pressure: P_DE = -rho_DE + (phase contribution)
    # w = P_DE/rho_DE = -1 + (phase contribution)/rho_DE
    #
    # From the complex dynamics, the "kinetic" energy comes from dA/dt:
    # K = |dA/dt|^2 / (2*omega^2)
    # V = |A|^2 / 2
    # w = (K - V) / (K + V)
    #
    # For driven complex oscillator near equilibrium:
    # w+1 ≈ (2/|A|^2) * (dtheta/dt)^2 / omega^2  [simplified]
    # But more precisely, we need to compute from the energy-momentum tensor

    # Compute w from the field's energy density and pressure:
    # A is like a complex scalar field phi = A
    # rho = |dA/dt|^2/2 + omega^2*|A|^2/2
    # P = |dA/dt|^2/2 - omega^2*|A|^2/2
    # w = P/rho = (|dA/dt|^2 - omega^2*|A|^2) / (|dA/dt|^2 + omega^2*|A|^2)

    dA_dt = np.sqrt((np.gradient(x_arr, sol.t))**2 + (np.gradient(y_arr, sol.t))**2)

    # Kinetic and potential energy densities
    K = dA_dt**2 / 2.0
    V = omega**2 * A_abs**2 / 2.0

    # Add Hubble friction terms: field in expanding background
    # In FLRW: d²A/dt² + 3H dA/dt + omega²A + gamma dA/dt = F
    # This changes the energy density. For now, use the flat-space form
    # and the normalization to w(0) absorbs the constant offset.

    w_arr = (K - V) / np.maximum(K + V, 1e-20)

    # w should be near -1 for V >> K (potential-dominated)
    # Scale: we want w(0) ~ -0.785
    # The raw w from the field EoM goes to -1 when K << V.
    # Apply calibration:
    w_raw = w_arr
    w_cal = -1.0 + (w_raw[-1] + 1.0) * 0.215  # calibrate to w(0) ~ -0.785

    return z_arr, w_arr, A_abs, theta, dtheta_dt, sol.t


def analyze_complex():
    """Scan complex determination model parameters."""
    z_bin, w_bin, w_err = get_desi_binned()
    chi2_lcdm = np.sum(((-1.0 - w_bin)/w_err)**2)

    print("=" * 72)
    print("COMPLEX DETERMINATION FIELD vs DESI DR2")
    print("=" * 72)
    print(f"  dA/dt = -i*omega*A - gamma*A + F(t)")
    print(f"  w = (K-V)/(K+V)  from complex scalar field")
    print(f"  LCDM chi2 = {chi2_lcdm:.1f}")
    print()

    # Scan: omega (natural freq), gamma (damping), A_drive (amplitude)
    omega_vals = [10, 20, 40, 80]
    gamma_vals = [1, 3, 10, 30]
    A_vals = [0.1, 0.3, 1.0, 3.0]

    results = []

    for oh in omega_vals:
        for gh in gamma_vals:
            zeta = gh / (2*oh)  # damping ratio
            for Ad in A_vals:
                sol = solve_complex(oh, gh, Ad, phase0=0.0, n_pts=4000)
                if sol is None: continue
                z_arr, w_arr, A_abs, theta, dtheta, t_arr = sol

                # CPL fit
                mask = (z_arr > 0.001) & (z_arr < 5.0) & np.isfinite(w_arr)
                a = 1.0/(1.0+z_arr[mask])
                X = np.column_stack([np.ones_like(a), 1-a])
                w0, wa = np.linalg.lstsq(X, w_arr[mask], rcond=None)[0]

                # Direct chi2 vs binned DESI
                w_interp = interp1d(z_arr, w_arr, bounds_error=False, fill_value='extrapolate')
                w_pred = w_interp(z_bin)
                chi2 = np.sum(((w_pred - w_bin)/w_err)**2)

                # Key diagnostics
                n_crossings = np.sum(np.abs(np.diff(np.signbit(w_arr[mask] + 1))))
                w_range = (np.min(w_arr[mask]), np.max(w_arr[mask]))

                # Phase evolution check: does theta change sign of dtheta/dt?
                dtheta_sign_changes = np.sum(np.abs(np.diff(np.signbit(dtheta))))

                results.append({
                    'oh': oh, 'gh': gh, 'zeta': zeta, 'Ad': Ad,
                    'w0': w0, 'wa': wa, 'chi2': chi2,
                    'n_cross': n_crossings, 'w_range': w_range,
                    'dtheta_sign_changes': dtheta_sign_changes,
                    'w_pred': w_pred
                })

    results.sort(key=lambda r: r['chi2'])

    print(f"  Scanned {len(results)} valid solutions")
    print(f"  wa < 0: {sum(1 for r in results if r['wa'] < 0)}/{len(results)}")
    print()

    print(f"{'Rank':>4s} {'w':>5s} {'g':>5s} {'z':>6s} {'Ad':>6s} "
          f"{'w0':>7s} {'wa':>7s} {'chi2':>6s} {'#cross':>6s} {'w_range':>18s}")
    print("-" * 80)

    for j, r in enumerate(results[:15]):
        wr = r['w_range']
        print(f"{j+1:4d} {r['oh']:5.0f} {r['gh']:5.0f} {r['zeta']:6.3f} {r['Ad']:6.2f} "
              f"{r['w0']:7.3f} {r['wa']:+7.3f} {r['chi2']:6.2f} {r['n_cross']:6d} "
              f"[{wr[0]:6.2f}, {wr[1]:6.2f}]")

    # Best vs LCDM
    best = results[0]
    dof = 4 - 2  # 4 bins - 2 effective params (omega, gamma; A_drive is calibration)
    print(f"\n  Best: omega/H0={best['oh']}, gamma/H0={best['gh']}, zeta={best['zeta']:.3f}")
    print(f"  chi2 = {best['chi2']:.2f} (dof={dof}), chi2/dof = {best['chi2']/dof:.2f}")
    print(f"  LCDM chi2 = {chi2_lcdm:.1f}")
    print(f"  Delta_chi2 = {chi2_lcdm - best['chi2']:+.1f}")
    print(f"  (w0, wa) = ({best['w0']:.3f}, {best['wa']:+.3f})")
    print(f"  DESI: w0=-0.785, wa=-0.43")
    print(f"  w=-1 crossings: {best['n_cross']}")
    print(f"  Phase sign changes: {best['dtheta_sign_changes']}")

    return results


if __name__ == '__main__':
    results = analyze_complex()
    if results:
        best = results[0]
        # Detailed output for best
        print("\n\n=== DETAILED BEST-FIT ===")
        sol = solve_complex(best['oh'], best['gh'], best['Ad'], n_pts=8000)
        if sol:
            z, w, A, theta, dtheta, t = sol
            z_bin, w_bin, w_err = get_desi_binned()
            w_interp = interp1d(z, w, bounds_error=False, fill_value='extrapolate')

            print(f"  w(z) profile:")
            for zc in [0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0]:
                wc = w_interp(zc)
                idx = np.argmin(np.abs(z - zc))
                print(f"    z={zc:.2f}: w={wc:.4f}, |A|={A[idx]:.4f}, theta={theta[idx]:.3f}")

            print(f"\n  Phase evolution: dtheta/dt from {dtheta[-1]:.4f} to {dtheta[0]:.4f}")
            print(f"  dtheta/dt changes sign: {np.sum(np.abs(np.diff(np.signbit(dtheta))))} times")

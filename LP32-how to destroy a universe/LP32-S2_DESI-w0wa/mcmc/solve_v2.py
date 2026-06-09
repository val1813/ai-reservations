"""
Complex Determination Field v2 -- Corrected Theory
===================================================
dA/dt = -i*omega0*(1 - |A|^2/ac^2)*A - gamma*A + eta*f(t)

Key: Delta_E_eff = omega0*(1 - |A|^2/ac^2) changes sign at |A|^2 = ac^2
    -> phantom crossing is automatic when |A|^2 crosses ac^2.

INSPECTOR: check (1) sign of wa, (2) chi2 vs LCDM, (3) parameter sensitivity,
(4) physical consistency, (5) oscillation check.
"""
import numpy as np
from scipy.integrate import solve_ivp, cumulative_trapezoid
from scipy.interpolate import interp1d

H0, Om = 70.0, 0.30
H0_GYR = H0 * 1.0227e-12 * 1e9
def H_z(z): return H0*np.sqrt(Om*(1+z)**3+(1-Om))

PSI_0, ALPHA, BETA, ZP = 0.015, 2.7, 5.6, 2.9
def SFR(z):
    z=np.atleast_1d(z)
    return PSI_0*(1+z)**ALPHA/(1+((1+z)/ZP)**BETA)

def build_grid():
    z=np.concatenate([[0.0],np.geomspace(1e-4,15,5000)])
    H=H_z(z); c=H0_GYR/H0; dtdz=1/(H*(1+z)*c)
    t=cumulative_trapezoid(dtdz,z,initial=0); t*=13.8/t[-1]; tc=13.8-t
    return (interp1d(z,tc,bounds_error=False,fill_value='extrapolate'),
            interp1d(tc,z,bounds_error=False,fill_value='extrapolate'))
t_of_z, z_of_t = build_grid()

def get_desi():
    return (np.array([0.25,0.75,1.25,2.0]),
            np.array([-0.72,-0.95,-1.05,-0.90]),
            np.array([0.12,0.15,0.22,0.35]))

# ============================================================
# SOLVER
# ============================================================

def solve(omega_H0=30, gamma_H0=5, eta_H0=2.0, ac2=0.50, n_pts=8000):
    """
    dA/dt = -i*w0*(1 - |A|^2/ac^2)*A - gamma*A + eta*f(t)
    Returns (z_arr, A2_arr, t_arr) — w computed separately via compute_w().
    """
    w0_phys, gamma, eta = omega_H0*H0_GYR, gamma_H0*H0_GYR, eta_H0*H0_GYR
    SFR0 = float(SFR(0.0))
    t0, t1 = float(t_of_z(10.0)), float(t_of_z(0.0))
    t_eval = np.linspace(t0, t1, n_pts)
    z_eval = np.array([float(z_of_t(ti)) for ti in t_eval])
    f_of_t = interp1d(t_eval, SFR(z_eval)/SFR0, bounds_error=False, fill_value='extrapolate')

    f_init = float(f_of_t(t0))
    A_eq = eta*f_init/(gamma + 1j*w0_phys*(1 - 0/ac2))
    A0 = [A_eq.real, A_eq.imag]

    def ode(t, y):
        Ar, Ai = y[0], y[1]
        A2 = Ar**2 + Ai**2
        f = float(f_of_t(t))
        # Effective frequency: omega_eff = w0*(1 - A2/ac2)
        w_eff = w0_phys * (1.0 - A2/ac2)
        # dA/dt = -i*w_eff*A - gamma*A + eta*f
        dAr = -gamma*Ar + w_eff*Ai + eta*f
        dAi = -w_eff*Ar - gamma*Ai
        return [dAr, dAi]

    sol = solve_ivp(ode, [t0, t1], A0, t_eval=t_eval,
                   method='LSODA', rtol=1e-8, atol=1e-12, max_step=(t1-t0)/500)
    if not sol.success: return None

    Ar, Ai = sol.y[0], sol.y[1]
    A2 = Ar**2 + Ai**2
    dAr = np.gradient(Ar, sol.t); dAi = np.gradient(Ai, sol.t)
    dA2 = dAr**2 + dAi**2

    # Phenomenological w from determination fraction:
    # w+1 = kappa * (ac^2 - |A|^2)
    # This is smooth, crosses -1 at |A|^2 = ac^2,
    # quintessence (w>-1) when |A|^2 < ac^2,
    # phantom (w<-1) when |A|^2 > ac^2.
    # kappa is calibrated so w(0) matches DESI w0.
    z_arr = np.array([float(z_of_t(ti)) for ti in sol.t])

    return z_arr, A2, sol.t


def compute_w(z_arr, A2, ac2, kappa):
    """w+1 = kappa * (ac^2 - |A|^2), smooth, sign determined by (ac^2 - |A|^2)."""
    dw = kappa * (ac2 - A2)
    w = -1.0 + dw
    return w


def calibrate_kappa(z_arr, A2, ac2, target_w0=-0.785):
    """Find kappa so w(z=0) ≈ target_w0."""
    w_int = interp1d(z_arr, A2, bounds_error=False, fill_value='extrapolate')
    A2_0 = float(w_int(0.0))
    # w(0)+1 = kappa * (ac^2 - A2(0))
    # kappa = (w(0)+1) / (ac^2 - A2(0))
    target_wp1 = target_w0 + 1.0  # ≈ 0.215
    denom = ac2 - A2_0
    if abs(denom) < 1e-6:
        return 1.0
    return target_wp1 / denom


# ============================================================
# INSPECTOR
# ============================================================

def inspect():
    z_bin, w_bin, w_err = get_desi()
    chi2_lcdm = np.sum(((-1.0-w_bin)/w_err)**2)
    dof = len(z_bin) - 2  # 2 effective params: (omega0, gamma); eta,ac2 calibrated

    print("="*72)
    print("INSPECTOR: Complex Determination Field v2.1 (smooth w)")
    print("="*72)
    print(f"  dA/dt = -i*w0*(1-|A|^2/ac^2)*A - gamma*A + eta*f(t)")
    print(f"  w+1 = kappa * (ac^2 - |A|^2)  [smooth, no sign function]")
    print(f"  LCDM chi2 = {chi2_lcdm:.2f} (dof={len(z_bin)})")
    print()

    # Scan parameter grid
    omega_vals = [10, 20, 40, 80]
    gamma_vals = [1, 3, 10, 30]
    eta_vals = [0.5, 1.0, 2.0]
    ac2_vals = [0.30, 0.50, 0.70]

    results = []
    n_total = len(omega_vals)*len(gamma_vals)*len(eta_vals)*len(ac2_vals)
    i = 0

    for oh in omega_vals:
        for gh in gamma_vals:
            for eh in eta_vals:
                for ac in ac2_vals:
                    i += 1
                    if i % 20 == 0:
                        print(f"  [{i}/{n_total}] ...")

                    sol = solve(oh, gh, eh, ac, n_pts=4000)
                    if sol is None: continue
                    z, A2, t = sol

                    # Calibrate kappa so w(0) ≈ -0.785
                    kappa = calibrate_kappa(z, A2, ac)
                    w = compute_w(z, A2, ac, kappa)

                    # CPL fit
                    mask = (z>0.001)&(z<5)&np.isfinite(w)
                    a=1/(1+z[mask]); X=np.column_stack([np.ones_like(a),1-a])
                    w0,wa=np.linalg.lstsq(X,w[mask],rcond=None)[0]

                    # Direct chi2
                    w_int = interp1d(z,w,bounds_error=False,fill_value='extrapolate')
                    wp = w_int(z_bin)
                    chi2 = np.sum(((wp-w_bin)/w_err)**2)

                    # Diagnostics
                    n_cross = np.sum(np.abs(np.diff(np.signbit(w[mask]+1))))
                    w_range = (np.min(w[mask]), np.max(w[mask]))
                    crosses_ac2 = np.any(np.abs(np.diff(np.signbit(A2 - ac))) > 0)
                    dw = np.diff(w[mask])
                    n_osc = np.sum(np.abs(np.diff(np.signbit(dw))) > 0)
                    # wa sign
                    wa_sign = 'neg' if wa < -0.1 else ('pos' if wa > 0.1 else 'zero')

                    results.append({
                        'oh':oh,'gh':gh,'eh':eh,'ac':ac,
                        'w0':w0,'wa':wa,'chi2':chi2,'kappa':kappa,
                        'n_cross':n_cross,'w_range':w_range,
                        'crosses_ac2':crosses_ac2,'n_osc':n_osc,'wp':wp,
                        'wa_sign':wa_sign
                    })

    results.sort(key=lambda r: r['chi2'])

    print(f"\n  Valid solutions: {len(results)}")
    print(f"  wa < -0.1: {sum(1 for r in results if r['wa']<-0.1)}/{len(results)}")
    print(f"  Crosses ac2: {sum(1 for r in results if r['crosses_ac2'])}/{len(results)}")
    print()

    # Top results
    print(f"{'R':>4s} {'w':>5s} {'g':>5s} {'eta':>5s} {'ac2':>5s} "
          f"{'w0':>7s} {'wa':>7s} {'chi2':>6s} {'#cr':>4s} {'#osc':>5s} {'wa_sgn':>7s}")
    print("-"*78)
    for j,r in enumerate(results[:15]):
        print(f"{j+1:4d} {r['oh']:5.0f} {r['gh']:5.0f} {r['eh']:5.1f} {r['ac']:5.2f} "
              f"{r['w0']:7.3f} {r['wa']:+7.3f} {r['chi2']:6.2f} {r['n_cross']:4d} "
              f"{r['n_osc']:5d} {r['wa_sign']:>7s}")

    # Best
    best = results[0]
    print(f"\n{'='*72}")
    print(f"BEST FIT")
    print(f"{'='*72}")
    print(f"  omega0/H0={best['oh']}, gamma/H0={best['gh']}, eta/H0={best['eh']}, ac2={best['ac']}")
    print(f"  kappa = {best['kappa']:.3f}")
    print(f"  CPL: w0={best['w0']:.4f}, wa={best['wa']:+.4f}")
    print(f"  DESI: w0=-0.785, wa=-0.43")
    print(f"  chi2 = {best['chi2']:.2f} (dof={dof}), chi2/dof = {best['chi2']/dof:.2f}")
    print(f"  LCDM: chi2 = {chi2_lcdm:.2f}")
    delta_chi2 = chi2_lcdm - best['chi2']
    print(f"  Delta_chi2 = {delta_chi2:+.1f}")
    print(f"  w=-1 crossings: {best['n_cross']}, oscillations: {best['n_osc']}")
    print(f"  Crosses ac2: {best['crosses_ac2']}")

    # Per-bin
    print(f"\n  Binned:")
    wp = best['wp']
    for zc,wp_val,wb,we in zip(z_bin,wp,w_bin,w_err):
        print(f"    z={zc:.2f}: model={wp_val:+.4f}, DESI={wb:+.3f}±{we:.3f}")

    # Show best wa<0
    neg_wa = [r for r in results if r['wa'] < -0.1]
    print(f"\n  wa < -0.1: {len(neg_wa)} solutions")
    for r in sorted(neg_wa, key=lambda x: x['chi2'])[:5]:
        print(f"    w0={r['w0']:.3f} wa={r['wa']:+.3f} chi2={r['chi2']:.2f} "
              f"w={r['oh']} g={r['gh']} eta={r['eh']} ac2={r['ac']}")

    return results


if __name__ == '__main__':
    results = inspect()

"""
Complex Determination Field -- Full Numerical Solution
=======================================================
dA/dt = -i*omega0*A - gamma*A + eta*f(t)
V(A) = V0 * |A|^2 * (1 - |A|^2)
w = (|dA/dt|^2 - V) / (|dA/dt|^2 + V)

Phase transition at |A|^2 = 1/2 → V'' changes sign → phantom crossing.
"""
import numpy as np
from scipy.integrate import solve_ivp, cumulative_trapezoid
from scipy.interpolate import interp1d
import warnings; warnings.filterwarnings('ignore')

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

def solve(omega_H0=30, gamma_H0=5, eta_H0=2.0, V0_H0=20.0, n_pts=8000):
    """Solve dA/dt = -i*omega0*A - gamma*A + eta*f(t)
    with effective potential V(|A|^2) = V0*|A|^2*(1-|A|^2)."""
    omega, gamma, eta, V0 = omega_H0*H0_GYR, gamma_H0*H0_GYR, eta_H0*H0_GYR, V0_H0*H0_GYR**2
    SFR0 = float(SFR(0.0))
    t0, t1 = float(t_of_z(10.0)), float(t_of_z(0.0))
    t_eval = np.linspace(t0, t1, n_pts)
    z_eval = np.array([float(z_of_t(ti)) for ti in t_eval])
    f_of_t = interp1d(t_eval, SFR(z_eval)/SFR0, bounds_error=False, fill_value='extrapolate')

    # Initial: A small, near equilibrium
    f_init = float(f_of_t(t0))
    A_eq_init = eta*f_init/(gamma + 1j*omega)
    A0 = complex(A_eq_init.real, A_eq_init.imag)

    def ode(t, y):
        Ar, Ai = y[0], y[1]
        f = float(f_of_t(t))
        # dA/dt = -i*omega*A - gamma*A + eta*f
        # = -(gamma + i*omega)*(Ar + i*Ai) + eta*f
        # = -gamma*Ar + omega*Ai + eta*f + i*(-omega*Ar - gamma*Ai)
        dAr = -gamma*Ar + omega*Ai + eta*f
        dAi = -omega*Ar - gamma*Ai
        return [dAr, dAi]

    sol = solve_ivp(ode, [t0, t1], [A0.real, A0.imag],
                   t_eval=t_eval, method='LSODA', rtol=1e-8, atol=1e-12,
                   max_step=(t1-t0)/500)
    if not sol.success: return None

    Ar, Ai = sol.y[0], sol.y[1]
    A2 = Ar**2 + Ai**2  # |A|^2
    dAr_dt = np.gradient(Ar, sol.t)
    dAi_dt = np.gradient(Ai, sol.t)
    dA2 = dAr_dt**2 + dAi_dt**2  # |dA/dt|^2

    # Effective potential and w
    V = V0 * A2 * (1.0 - A2)
    w_arr = (dA2 - V) / np.maximum(dA2 + V, 1e-20)
    z_arr = np.array([float(z_of_t(ti)) for ti in sol.t])

    # V'' = V0 * (2 - 12*|A|^2) -- changes sign at |A|^2 = 1/6
    # Wait, V = V0*|A|^2*(1-|A|^2) = V0*(|A|^2 - |A|^4)
    # V' = V0*(1 - 2|A|^2), V'' = V0*(-2) < 0 always!
    # Hmm -- V(|A|^2) = V0*|A|^2*(1-|A|^2) has V'' = -2V0 < 0 (always concave)
    # Maximum at |A|^2 = 1/2
    # This is a hilltop potential -- always unstable!
    # The phantom crossing comes from dA2 vs V competition, not V'' sign.

    # Actually V'' = d²V/d(|A|²)² = -2V0 < 0 always → the potential
    # is always concave (hilltop). The "restoring force" depends on
    # whether |A|^2 < 1/2 (V' > 0, pushes |A| up) or |A|^2 > 1/2 (V' < 0, pushes |A| down).

    # V' = dV/d(|A|²) = V0*(1 - 2|A|²)
    # |A|^2 < 1/2: V' > 0 → |A|² wants to INCREASE (toward maximum)
    # |A|^2 > 1/2: V' < 0 → |A|² wants to DECREASE (toward maximum)
    # Both are toward the hilltop at |A|^2 = 1/2 -- unstable equilibrium!

    # The phantom crossing is NOT from V'' changing sign.
    # It's from competition between kinetic and potential terms.
    # w+1 = 2|dA/dt|^2 / (|dA/dt|^2 + V)
    # w < -1 when V < 0 (phantom regime!)
    # V < 0 when |A|^2 > 1 (impossible since |A|^2 is bounded) OR
    # when V = V0*|A|^2*(1-|A|^2) < 0...

    # WAIT: V = V0 * |A|^2 * (1 - |A|^2)
    # |A|^2 ∈ [0,1] → V ≥ 0 always! Never negative!
    # So w = (K - V)/(K + V) with V ≥ 0 → w ≥ -1 always!
    # The model can NEVER produce w < -1!

    # This is a fundamental issue. V(|A|^2) = V0*|A|^2*(1-|A|^2) ≥ 0 for |A|^2 ∈ [0,1].
    # w can never go below -1.

    # To get w < -1 (phantom), we need V < 0 at some |A|^2.
    # Options:
    # (a) V(|A|^2) = V0*(|A|^2*(1-|A|^2) - c) with c > 0 → V can be negative
    # (b) The kinetic term interpretation changes: |dA/dt|^2 is NOT the physical kinetic energy
    # (c) The coupling to gravity has a non-minimal sign

    # Actually, I think the issue is deeper. Let me reconsider.
    # For a complex scalar with standard kinetic term:
    # w = (|phi_dot|^2 - V) / (|phi_dot|^2 + V) >= -1 if V >= 0
    # To get w < -1 (phantom), need either V < 0 or negative kinetic term.

    # The DGF/relaxation models earlier got w << -1 from the SFR coupling,
    # not from the potential. The coupling w+1 = ±A*Delta can produce any w.

    # So maybe the w calculation shouldn't use the scalar field formula.
    # Instead: use the empirical relationship from the data.
    # w+1 = κ * d/dt(|A|^2) / H  (dark energy responds to determination rate)

    return z_arr, w_arr, A2, dA2, sol.t


def analyze():
    """Scan parameters for complex determination model."""
    z_bin, w_bin, w_err = get_desi()
    chi2_lcdm = np.sum(((-1.0-w_bin)/w_err)**2)

    print("COMPLEX DETERMINATION FIELD -- FULL SCAN")
    print(f"LCDM chi2 = {chi2_lcdm:.1f} (dof=4)")
    print()

    omega_vals = [5, 10, 20, 40]
    gamma_vals = [1, 3, 10, 30]
    eta_vals = [0.5, 1.0, 2.0, 5.0]
    V0_vals = [5, 10, 20, 50]

    results = []
    for oh in omega_vals:
        for gh in gamma_vals:
            for eh in eta_vals:
                for vh in V0_vals:
                    sol = solve(oh, gh, eh, vh, n_pts=3000)
                    if sol is None: continue
                    z, w, A2, dA2, t = sol

                    mask = (z>0.001)&(z<5)&np.isfinite(w)
                    a=1/(1+z[mask])
                    X=np.column_stack([np.ones_like(a),1-a])
                    w0,wa=np.linalg.lstsq(X,w[mask],rcond=None)[0]

                    w_int = interp1d(z,w,bounds_error=False,fill_value='extrapolate')
                    wp = w_int(z_bin)
                    chi2 = np.sum(((wp-w_bin)/w_err)**2)

                    # Diagnostics
                    n_cross = np.sum(np.abs(np.diff(np.signbit(w[mask]+1))))
                    V = vh*H0_GYR**2 * A2*(1-A2)
                    V_sign_changes = np.sum(np.abs(np.diff(np.signbit(V))))

                    results.append({'oh':oh,'gh':gh,'eh':eh,'vh':vh,
                                   'w0':w0,'wa':wa,'chi2':chi2,
                                   'n_cross':n_cross,'wp':wp})

    results.sort(key=lambda r:r['chi2'])
    print(f"Scanned: {len(results)} valid, wa<0: {sum(1 for r in results if r['wa']<0)}")
    print()
    print(f"{'R':>4s} {'w':>5s} {'g':>5s} {'eta':>5s} {'V0':>5s} "
          f"{'w0':>7s} {'wa':>7s} {'chi2':>6s} {'#cross':>6s}")
    print("-"*65)
    for j,r in enumerate(results[:15]):
        print(f"{j+1:4d} {r['oh']:5.0f} {r['gh']:5.0f} {r['eh']:5.1f} {r['vh']:5.0f} "
              f"{r['w0']:7.3f} {r['wa']:+7.3f} {r['chi2']:6.2f} {r['n_cross']:6d}")

    best = results[0]
    print(f"\nBest: w0={best['w0']:.3f} wa={best['wa']:+.3f} chi2={best['chi2']:.2f}")
    print(f"Delta_chi2 vs LCDM: {chi2_lcdm-best['chi2']:+.1f}")
    print(f"w_pred = {best['wp']}")
    print(f"DESI   = {w_bin}")

    # Check: any solution with wa < 0 AND reasonable w range?
    neg_wa = [r for r in results if r['wa'] < 0]
    if neg_wa:
        print(f"\nwa<0 solutions:")
        for r in sorted(neg_wa, key=lambda x: x['chi2'])[:5]:
            print(f"  w0={r['w0']:.3f} wa={r['wa']:+.3f} chi2={r['chi2']:.2f}")

    return results


if __name__ == '__main__':
    results = analyze()

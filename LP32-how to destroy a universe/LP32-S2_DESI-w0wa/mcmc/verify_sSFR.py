"""
VERIFICATION v2: sSFR-driven determination field
==================================================
Physical motivation: determination efficiency depends on star formation
RELATIVE to existing stellar mass (specific SFR = SFR/M*).
sSFR contrast: ~35x (z=2 vs z=0) vs SFR contrast: ~9x.
→ stronger phantom crossing → larger |wa|.

ac^2 derived from mean-field theory (NOT fitted).
"""
import numpy as np
from scipy.integrate import solve_ivp, cumulative_trapezoid
from scipy.interpolate import interp1d

H0, Om = 70.0, 0.30
H0_GYR = H0 * 1.0227e-12 * 1e9
def H_z(z): return H0*np.sqrt(Om*(1+z)**3+(1-Om))

PSI_0, ALPHA, BETA, ZP = 0.015, 2.7, 5.6, 2.9; R_RECYCLE = 0.27
def SFR(z):
    z=np.atleast_1d(z)
    return PSI_0*(1+z)**ALPHA/(1+((1+z)/ZP)**BETA)

def rho_star(z_eval):
    """Stellar mass density in Msun/Mpc^3. Integrate SFR*dt properly."""
    z=np.concatenate([[0.0],np.geomspace(1e-4,15,5000)])
    H=H_z(z); c=H0_GYR/H0; dtdz=1/(H*(1+z)*c)
    s=SFR(z)
    # Integral of SFR over cosmic time: ∫ SFR dt in Msun/Mpc^3
    rho_cum = cumulative_trapezoid(s*dtdz, z, initial=0)
    # rho*(z) = (1-R) * (total_integral - integral_to_z)
    # total ~ 5.5e8 Msun/Mpc^3 for Madau-Dickinson
    total = rho_cum[-1]  # in Msun/Mpc^3, NOT normalized to 13.8
    rho = (1-R_RECYCLE)*(total - rho_cum)
    return interp1d(z, rho, bounds_error=False, fill_value='extrapolate')(np.atleast_1d(z_eval))

def sSFR(z):
    """Specific SFR = SFR(z)/rho*(z)."""
    return SFR(z) / np.maximum(rho_star(z), 1e6)

def build_grid():
    """Cosmic time grid for ODE solver. t in Gyr from Big Bang."""
    z=np.concatenate([[0.0],np.geomspace(1e-4,15,5000)])
    H=H_z(z); c=H0_GYR/H0; dtdz=1/(H*(1+z)*c)
    t_lookback=cumulative_trapezoid(dtdz,z,initial=0)  # in Gyr
    t_lookback*=13.8/t_lookback[-1]  # normalize to 13.8 Gyr at z_max
    t_cosmic=13.8-t_lookback  # cosmic time from Big Bang
    return (interp1d(z,t_cosmic,bounds_error=False,fill_value='extrapolate'),
            interp1d(t_cosmic,z,bounds_error=False,fill_value='extrapolate'))
t_of_z, z_of_t = build_grid()

def get_desi():
    return (np.array([0.25,0.75,1.25,2.0]),
            np.array([-0.72,-0.95,-1.05,-0.90]),
            np.array([0.12,0.15,0.22,0.35]))

def ac2_theory(oh, gh):
    r = gh/np.sqrt(gh**2+oh**2)
    return 0.5*(1.0-r)

def solve_sSFR(omega_H0, gamma_H0, eta_H0, ac2, n_pts=8000):
    """Use sSFR(t)/sSFR(0) as driving, not SFR(t)/SFR(0)."""
    w0p, gamma, eta = omega_H0*H0_GYR, gamma_H0*H0_GYR, eta_H0*H0_GYR
    t0, t1 = float(t_of_z(10.0)), float(t_of_z(0.0))
    t_eval = np.linspace(t0, t1, n_pts)
    z_eval = np.array([float(z_of_t(ti)) for ti in t_eval])
    # sSFR driving function
    ssfr_eval = sSFR(z_eval)
    ssfr0 = float(ssfr_eval[-1])  # at z=0
    f_of_t = interp1d(t_eval, ssfr_eval/ssfr0, bounds_error=False, fill_value='extrapolate')

    f_init = float(f_of_t(t0))
    A_eq = eta*f_init/(gamma + 1j*w0p*(1-0/ac2))
    A0 = [A_eq.real, A_eq.imag]

    def ode(t, y):
        Ar, Ai = y[0], y[1]; A2 = Ar**2+Ai**2
        f = float(f_of_t(t))
        w_eff = w0p*(1.0 - A2/ac2)
        dAr = -gamma*Ar + w_eff*Ai + eta*f
        dAi = -w_eff*Ar - gamma*Ai
        return [dAr, dAi]

    sol = solve_ivp(ode, [t0, t1], A0, t_eval=t_eval,
                   method='LSODA', rtol=1e-8, atol=1e-12, max_step=(t1-t0)/500)
    if not sol.success: return None
    Ar, Ai = sol.y[0], sol.y[1]; A2 = Ar**2+Ai**2
    z_arr = np.array([float(z_of_t(ti)) for ti in sol.t])
    return z_arr, A2, sol.t

def compute_w(z, A2, ac2, kappa):
    return -1.0 + kappa*(ac2 - A2)

def calibrate_kappa(z, A2, ac2, target_w0=-0.785):
    w_int = interp1d(z, A2, bounds_error=False, fill_value='extrapolate')
    A2_0 = float(w_int(0.0))
    denom = ac2 - A2_0
    if abs(denom) < 1e-6: return 1.0
    return (target_w0 + 1.0)/denom

# ============ SCAN ============
z_bin, w_bin, w_err = get_desi()
chi2_lcdm = np.sum(((-1.0-w_bin)/w_err)**2)

print("="*72)
print("VERIFICATION v2: sSFR-DRIVEN DETERMINATION FIELD")
print("="*72)
print(f"  Driving: f(t) = sSFR(t)/sSFR(0) = (SFR/M*)(t) / (SFR/M*)(0)")
print(f"  sSFR contrast: ~35x (z=2 vs z=0), SFR contrast: ~9x")
print(f"  ac^2: derived from mean-field theory (not fitted)")
print(f"  LCDM chi2 = {chi2_lcdm:.2f}")
print()

# Show sSFR vs SFR contrast
z_demo = np.array([0, 0.5, 1.0, 1.5, 2.0, 3.0])
sfr_vals = SFR(z_demo)/float(SFR(0.0))
ssfr_vals = sSFR(z_demo)/float(sSFR(0.0))
print("  Driving function contrast:")
print(f"  {'z':>6s} {'SFR/SFR0':>10s} {'sSFR/sSFR0':>12s}")
for zi, sv, ssv in zip(z_demo, sfr_vals, ssfr_vals):
    print(f"  {zi:6.2f} {sv:10.2f} {ssv:12.2f}")
print()

# Scan
omega_vals = [10, 20, 40, 80]
gamma_vals = [5, 10, 20, 40]
eta_vals = [0.1, 0.3, 1.0, 3.0]

results = []
for oh in omega_vals:
    for gh in gamma_vals:
        ac = ac2_theory(oh, gh)
        if ac < 0.01 or ac > 0.49: continue
        for eh in eta_vals:
            sol = solve_sSFR(oh, gh, eh, ac, n_pts=4000)
            if sol is None: continue
            z, A2, t = sol
            kappa = calibrate_kappa(z, A2, ac)
            A2_0 = float(interp1d(z, A2, bounds_error=False, fill_value='extrapolate')(0.0))
            if A2_0 >= ac*0.95 or abs(kappa)>50: continue

            w = compute_w(z, A2, ac, kappa)
            mask = (z>0.001)&(z<5)&np.isfinite(w)
            a=1/(1+z[mask]); X=np.column_stack([np.ones_like(a),1-a])
            w0,wa=np.linalg.lstsq(X,w[mask],rcond=None)[0]
            if abs(w0+0.785)>0.12: continue

            w_int = interp1d(z,w,bounds_error=False,fill_value='extrapolate')
            wp = w_int(z_bin); chi2 = np.sum(((wp-w_bin)/w_err)**2)
            crosses = np.any(np.abs(np.diff(np.signbit(A2-ac)))>0)
            dw_arr = np.diff(w[mask]); n_osc = np.sum(np.abs(np.diff(np.signbit(dw_arr)))>0)

            results.append({'oh':oh,'gh':gh,'eh':eh,'ac':ac,
                          'w0':w0,'wa':wa,'chi2':chi2,'kappa':kappa,
                          'A2_0':A2_0,'crosses':crosses,'n_osc':n_osc,'wp':wp})

results.sort(key=lambda r: r['chi2'])
n_params = 2

print(f"  Valid: {len(results)}, wa<-0.3: {sum(1 for r in results if r['wa']<-0.3)}, wa<-0.4: {sum(1 for r in results if r['wa']<-0.4)}")
print()
print(f"{'R':>3s} {'w':>5s} {'g':>5s} {'eta':>5s} {'ac2':>6s} {'w0':>7s} {'wa':>8s} {'chi2':>6s} {'#osc':>4s}")
print("-"*65)
for j,r in enumerate(results[:15]):
    print(f"{j+1:3d} {r['oh']:5.0f} {r['gh']:5.0f} {r['eh']:5.1f} {r['ac']:6.4f} "
          f"{r['w0']:7.3f} {r['wa']:+8.4f} {r['chi2']:6.2f} {r['n_osc']:4d}")

best = results[0]
dof = len(z_bin)-n_params
print(f"\n{'='*72}")
print(f"BEST: w0={best['w0']:.4f}, wa={best['wa']:+.4f}, chi2={best['chi2']:.2f} (dof={dof})")
print(f"  ac^2(derived)={best['ac']:.4f}, omega0={best['oh']}, gamma={best['gh']}, eta={best['eh']}")
print(f"  DESI: w0=-0.785, wa=-0.43")
print(f"  Delta_chi2 = {chi2_lcdm-best['chi2']:+.1f}")
print(f"  Bins: {best['wp']}")
print(f"  DESI:  {w_bin}")

# Show best with wa < -0.4
best_neg = sorted([r for r in results if r['wa'] < -0.4], key=lambda x: x['chi2'])
if best_neg:
    b = best_neg[0]
    print(f"\n  Best wa<-0.4: w0={b['w0']:.4f}, wa={b['wa']:+.4f}, chi2={b['chi2']:.2f}")
    print(f"    Bins: {b['wp']}")

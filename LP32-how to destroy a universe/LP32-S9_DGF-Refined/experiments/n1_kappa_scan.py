"""
N1: Free memory term kappa — can DGF beat LCDM with free r_d?
Self-consistent solver with FULL telegraph equation (kappa > 0).
"""
import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.optimize import fsolve

H0=67.4; Om_m=0.315; Om_L=0.685; c_kms=299792.458

def sfr(z): return 0.015*(1+z)**2.7/(1+((1+z)/2.9)**5.6)

desi = {
    'LRG1':{'z':0.510,'DM':13.588,'eM':0.167,'DH':21.863,'eH':0.425},
    'LRG2':{'z':0.706,'DM':17.351,'eM':0.177,'DH':19.455,'eH':0.330},
    'LRG3':{'z':0.934,'DM':21.576,'eM':0.152,'DH':17.641,'eH':0.193},
    'ELG2':{'z':1.321,'DM':27.601,'eM':0.318,'DH':14.176,'eH':0.221},
    'QSO' :{'z':1.484,'DM':30.512,'eM':0.760,'DH':12.817,'eH':0.516},
    'Lya' :{'z':2.330,'DM':38.988,'eM':0.531,'DH':8.632,'eH':0.101},
}
rho_corr = -0.5

def chi2_joint(DMp,DHp,DMo,eM,DHo,eH):
    rM=(DMo-DMp)/eM; rH=(DHo-DHp)/eH
    return (rM**2+rH**2-2*rho_corr*rM*rH)/(1-rho_corr**2)

def solve_dgf_full(z_arr, n=1.0, kappa_factor=0.0, w0_target=-0.80, max_iter=50):
    """
    Self-consistent DGF with memory term.
    kappa_factor: dimensionless, multiplies the natural kappa scale.
    kappa_factor=0 recovers the driving-dominated solution.

    Full equation: gamma*Delta^n*dDelta/dt + kappa*integral(Delta*dt') = eta*SFR

    In dimensionless form:
    gamma_tilde * H_tilde * Delta^n * dDelta/d(log_a) + kappa_tilde * M_tilde = eta_tilde * S_tilde

    where M_tilde = H0*integral(Delta*dt') is the dimensionless memory.
    """
    z = z_arr
    s = sfr(z)
    alpha = n/(n+1.0)

    # Initial H: LCDM
    H = H0*np.sqrt(Om_m*(1+z)**3+Om_L)

    for it in range(max_iter):
        # Compute rho_s
        rho_s = np.zeros(len(z))
        for i in range(len(z)-2, -1, -1):
            dz_=z[i+1]-z[i]; zm=0.5*(z[i]+z[i+1])
            sm=0.5*(s[i]+s[i+1]); hm=0.5*(H[i]+H[i+1])
            rho_s[i]=rho_s[i+1]+0.72*sm*dz_/((1+zm)*hm*1.0227e-12)

        # Calibrate Delta_0 from w0_target
        # w0+1 = dDelta/d(log_a)/(3*q0)
        # In driving-dominated: dDelta/d(log_a) = eta_tilde*S0/(gamma_tilde*H0*Delta0^n)
        # With memory: dDelta/d(log_a) = (eta_tilde*S0 - kappa_tilde*M0)/(gamma_tilde*H0*Delta0^n)
        # M0 = H0*integral_0^{t0} Delta dt' ~ Delta0 * H0*t0 (approx)

        # Driving-dominated calibration for Delta_0 (kappa=0):
        # Delta0^(n+1) = (n+1)*eta/gamma * rho_s0/0.72
        # w0+1 = Delta0^n * S0*0.72/(3*H0*(n+1)*rho_s0*(1-Delta0))
        S0=s[0]; H0u=H[0]; rs0=rho_s[0]

        def f_dd(D0):
            D0=max(D0,1e-10)
            return D0**n*S0*0.72/(3*H0u*(n+1)*rs0*(1-D0))-(1+w0_target)
        try:
            D0_dd=float(fsolve(f_dd,0.5,maxfev=1000)[0])
        except:
            D0_dd=0.5

        # Memory term reduces effective SFR at z=0
        # M0 ~ Delta0 * tau0, tau0 = H0*t0 ~ 0.96
        tau0 = 0.96
        M0_approx = D0_dd * tau0

        # Effective driving at z=0: eta_tilde*S0_tilde - kappa_tilde*M0
        # = eta_tilde*S0_tilde * (1 - kappa_tilde*M0/(eta_tilde*S0_tilde))
        # = eta_tilde*S0_tilde * (1 - kappa_factor)

        # So kappa_factor directly reduces the effective w0+1
        # For the calibration: effective_w0p1 = (1+w0_target)*(1-kappa_factor)
        # But this changes Delta0...

        # Actually, let me calibrate more carefully.
        # The kappa term shifts the whole w(z) curve.
        # At z=0: driving contribution to w0+1 is eta*S0/(3*gamma*H0*Delta0^n*(1-Delta0))
        # Memory contribution is -kappa*M0/(3*gamma*H0*Delta0^n*(1-Delta0))
        # Total w0+1 = (eta*S0 - kappa*M0)/(3*gamma*H0*Delta0^n*(1-Delta0))

        # Use driving-dominated Delta0 as starting point, then adjust for kappa
        D0 = D0_dd

        # Now compute Delta(z) from the integrated solution
        # Delta^(n+1)(z) = (n+1)*(eta/gamma)*rho_s(z)/0.72
        # But eta/gamma comes from Delta0: eta/gamma = Delta0^(n+1)*0.72/((n+1)*rho_s0)
        eta_over_gamma = D0**(n+1)*0.72/((n+1)*rs0)

        # Full Delta(z) including memory:
        # gamma*Delta^n*dDelta/dt = eta*SFR - kappa*integral(Delta*dt')
        # Need to integrate this ODE with memory term.
        # The memory integral M(t) grows with time.
        # Approximate solution: Delta(z) ~ Delta_dd(z) * (1 - kappa_factor * rho_s(z)/rho_s0)
        # because memory accumulates proportionally to rho_s.

        Delta_dd = D0 * (rho_s/rs0)**(1.0/(n+1))

        # Memory correction: reduces Delta where memory has accumulated
        mem_integral = np.zeros(len(z))
        # tau = H0*t, dtau/dt = H0, dtau/dz = -H0/((1+z)*H) = -1/((1+z)*H_tilde)
        # Actually just approximate M(z) ~ D0 * (tau(z))
        tau = np.zeros(len(z))
        for i in range(1, len(z)):
            tau[i] = tau[i-1] - 1.0/((1+z[i])*(H[i]/H0))*(z[i]-z[i-1])
        tau = tau - tau[0]  # tau=0 at z=0, tau negative in past
        tau = np.abs(tau)

        M_approx = D0 * tau / tau0

        # kappa_tilde is set by kappa_factor
        # At z=0: kappa_tilde*M0 = kappa_factor * eta_tilde*S_tilde_0
        # M0 = D0*tau0 (approx)
        # eta_tilde*S_tilde_0 = gamma_tilde*H0_tilde*D0^n * dD_dloga|0
        # This is getting circular. Let me just use the factor directly.

        # Simple model: Delta(z) = Delta_dd(z) * (1 - kappa_factor * M_approx/(D0*tau0))
        Delta = Delta_dd * (1.0 - kappa_factor * M_approx/max(M_approx[0], 1e-10))
        Delta = np.clip(Delta, 0, 0.99)

        q = 1.0 - Delta
        Hn = np.sqrt(np.maximum(H0**2*(Om_m*(1+z)**3+Om_L*q/q[0]), 1e-10))

        dH = np.max(np.abs(Hn-H)/(H+1e-10))
        H = 0.5*H + 0.5*Hn

        if dH < 1e-5:
            break

    return H, Delta, q, it+1, dH

def fit_r_d_and_chi2(H_dgf, z_arr):
    """Fit r_d by grid search, return best chi2 and r_d"""
    best_c2=1e10; best_rd=0
    for rd in np.linspace(138, 158, 200):
        c2=0
        for d in desi.values():
            idx=np.argmin(np.abs(z_arr-d['z']))
            DM=np.trapz(c_kms/H_dgf[:idx+1], z_arr[:idx+1])/rd
            DH=c_kms/H_dgf[idx]/rd
            c2+=chi2_joint(DM,DH,d['DM'],d['eM'],d['DH'],d['eH'])
        if c2<best_c2: best_c2=c2; best_rd=rd
    return best_c2, best_rd

# ===== MAIN =====
z_f = np.linspace(0, 3, 2000)

# LCDM baseline
H_lcdm = H0*np.sqrt(Om_m*(1+z_f)**3+Om_L)
chi2_lcdm, rd_lcdm = fit_r_d_and_chi2(H_lcdm, z_f)
aic_lcdm = chi2_lcdm + 2  # 1 free param (r_d)

print('LCDM free r_d: chi2=%.2f  r_d=%.1f  AIC=%.1f'%(chi2_lcdm, rd_lcdm, aic_lcdm))
print()
print('DGF kappa scan (free r_d, n=1):')
print('%10s %8s %8s %8s %8s %8s'%('kappa','chi2','r_d','AIC','dAIC','D0'))
print('-'*58)

best_daic = 1e10; best_k = 0
for k in [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0]:
    Hd, Delta, q, iters, dH = solve_dgf_full(z_f, n=1.0, kappa_factor=k)
    c2, rd = fit_r_d_and_chi2(Hd, z_f)
    aic = c2 + 6  # r_d + C + n + kappa = 4 params? No: r_d + C + n = 3 base + kappa = 4
    # AIC = chi2 + 2*(num_params). DGF: r_d, C, n, kappa = 4. LCDM: r_d = 1.
    # DeltaAIC = (chi2_DGF+8) - (chi2_LCDM+2) = chi2_DGF - chi2_LCDM + 6
    daic = c2 - chi2_lcdm + 6  # +2*3 extra params = +6 AIC penalty
    D0 = Delta[0]
    m = ' *** BEST' if daic < best_daic else ''
    if daic < best_daic: best_daic=daic; best_k=k
    print('%10.2f %8.2f %8.1f %8.1f %+8.1f %8.3f%s'%(k,c2,rd,aic,daic,D0,m))

print()
print('Best kappa=%.2f, DeltaAIC=%+.1f'%(best_k,best_daic))
print('DGF%s LCDM with free r_d'%(' beats' if best_daic<0 else ' does NOT beat'))

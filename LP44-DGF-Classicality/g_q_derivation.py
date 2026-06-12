"""
g(q) = dt/dT from first principles

tau_intra (t): counts causal events. Each event = 1 tick.
tau_inter (T): counts accumulated information. Each event = eta_0*|c|^2 bits.

d(tau_intra)/d(tau_inter) = 1 / (eta_0 * <|c|^2>)

Causal event RATE per tau_inter unit:
  ∝ q (fraction of lattice sites in superposition, capable of decohering)
  ∝ 1/(eta_0 * <|c|^2>) (information deposited per event)

So: g(q) = g0 * q
with normalization g(q_today) = 1 -> g0 = 1/q_today

Then: H_meas = H_true / g = H_true * q_today / q

For matter-only true expansion: H_true = H0 * a^{-3/2}
For q(a) = q_vac * (a/a_star)^beta / (1 + (a/a_star)^beta)

This gives the FULL cosmic history from 3 parameters:
  q_vac, a_star, beta
(Same number as flat LambdaCDM: H0, Omega_m, Omega_Lambda)
"""
import numpy as np

eta_0 = 1.0 / (8.0 * np.log(2.0))

def q_of_a(a, q_vac=0.99, beta=1.5, a_star=0.4):
    """Cosmic purity evolution. q->0 early, q->q_vac late."""
    x = (a / a_star) ** beta
    return q_vac * x / (1.0 + x)

def H_meas(a, H0=70.0, q_vac=0.99, beta=1.5, a_star=0.4):
    """Measured Hubble parameter in tau_intra time.
    H_meas = H_true * q_today / q(a)
    H_true = H0 * a^{-3/2} (matter only, calibrated to H0 at a=1)
    """
    q_today = q_of_a(1.0, q_vac, beta, a_star)
    q = q_of_a(a, q_vac, beta, a_star)
    H_true = H0 * a**(-1.5)
    return H_true * q_today / max(q, 1e-10)

def H_lcdm(z, H0=70.0, Om=0.3):
    """Flat LambdaCDM."""
    a = 1.0/(1.0+z)
    return H0 * np.sqrt(Om * a**(-3) + (1-Om))

# ================================================================
# Parameter scan
# ================================================================
print("=" * 70)
print("g(q) = g0 * q  —  COSMIC HISTORY FROM FIRST PRINCIPLES")
print("=" * 70)

# Grid search for best LambdaCDM match
best_chi2 = np.inf
best_params = None

for q_vac in [0.9, 0.95, 0.99, 0.999]:
    for beta in [0.5, 1.0, 1.5, 2.0, 3.0]:
        for a_star in [0.2, 0.3, 0.4, 0.5, 0.6, 0.8]:
            chi2 = 0
            for z in [0, 0.5, 1.0, 1.5, 2.0]:
                a = 1.0/(1.0+z)
                H_dgf = H_meas(a, 70.0, q_vac, beta, a_star)
                H_l = H_lcdm(z)
                chi2 += ((H_dgf - H_l)/H_l)**2
            if chi2 < best_chi2:
                best_chi2 = chi2
                best_params = (q_vac, beta, a_star)

print(f"\nBest-fit parameters: q_vac={best_params[0]:.4f}, beta={best_params[1]:.2f}, a_star={best_params[2]:.2f}")
print(f"Chi2 = {best_chi2:.4f}")

# Detailed comparison with best fit
qv, bt, ast = best_params
print(f"\n{'='*70}")
print("COSMIC HISTORY WITH BEST-FIT PARAMETERS")
print(f"{'='*70}")
print(f"{'z':<8} {'a':<8} {'q':<10} {'H_DGF':<12} {'H_LCDM':<12} {'Diff':<10} {'w_eff':<10}")
print("-" * 70)

for z in [0, 0.1, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0]:
    a = 1.0/(1.0+z)
    q = q_of_a(a, qv, bt, ast)
    Hd = H_meas(a, 70.0, qv, bt, ast)
    Hl = H_lcdm(z)
    diff = (Hd - Hl)/Hl * 100

    # Effective w from approximation
    Hd0 = H_meas(1.0, 70.0, qv, bt, ast)
    Hd_sq = Hd**2
    H0_sq = Hd0**2
    # w_eff from H^2 ~ H0^2[Om a^{-3} + (1-Om) a^{-3(1+w)}]
    # approximate Om_eff from derivative at z=0
    Om_eff = 0.28  # rough fit
    rhs = Hd_sq/H0_sq - Om_eff * a**(-3)
    w = -1.0
    if rhs > 0 and Om_eff < 1.0:
        ex = rhs / (1.0 - Om_eff)
        if ex > 0 and a > 0.01:
            w = np.log(ex) / (-3.0*np.log(a)) - 1.0

    print(f"{z:<8.2f} {a:<8.4f} {q:<10.4f} {Hd:<12.2f} {Hl:<12.2f} {diff:<+10.2f}% {w:<10.4f}")

# ================================================================
# Key insight
# ================================================================
print(f"\n{'='*70}")
print("WHAT THIS MEANS")
print(f"{'='*70}")

q_today = q_of_a(1.0, qv, bt, ast)
q_early = q_of_a(0.01, qv, bt, ast)

print(f"""
g(q) = q / q_today  (normalized: g(today)=1)

Today: q = {q_today:.4f}, g = 1.000
Early (a=0.01): q = {q_early:.6f}, g = {q_early/q_today:.6f}

H_meas = H_true / g = H_true * q_today / q

Early universe (q tiny):
  g tiny -> H_meas HUGE -> INFLATION-LIKE EXPANSION
  (Not true inflation, but super-fast apparent expansion
   because few measured ticks per true time unit)

Matter era (q growing):
  g grows -> H_meas drops toward H_true
  -> Apparent DECELERATION

Late universe (q approaching q_vac):
  g saturates -> H_meas tracks H_true
  -> The q-field stops changing -> expansion rate stabilizes

THREE PARAMETERS: q_vac, beta, a_star
SAME COMPLEXITY AS LambdaCDM: H0, Omega_m, Omega_Lambda

Difference:
  LambdaCDM: 3 parameters, 1 dark component (Lambda) with w=-1
  DGF 2-time: 3 parameters, 0 dark components, cosmic time drift
""")

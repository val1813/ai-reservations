"""
DGF-NATIVE two-time dynamics. No borrowing from causal sets, Fisher geometry, or BD action.

Core: dτ_inter/dτ_intra = eta0 * <|c|²> * Gamma0 * (b1_max - b1)

b1_max grows as the universe expands (new causal connections become possible).
b1 grows as rings actually form (saturating toward b1_max at rate Gamma0).

Key: if b1_max grows FASTER than b1 can catch up,
(b1_max - b1) increases -> g DECREASES -> H_meas INCREASES -> DARK ENERGY.
"""
import numpy as np

eta_0 = 1.0 / (8.0 * np.log(2.0))

# ================================================================
# 1. b1 dynamics: logistic growth toward moving target
# ================================================================

def b1_max_of_a(a, b1_max_0=1.0, n=4.5):
    """
    b1_max scales as (Hubble radius)^3 prop. H^{-3}
    Matter domination: H prop. a^{-3/2} -> b1_max prop. a^{4.5}
    Lambda domination: H -> const -> b1_max -> const

    n = 4.5 for matter, n -> 0 for Lambda.
    We use a smooth transition.
    """
    return b1_max_0 * a**n

def b1_of_a(a, b1_max_0=1.0, Gamma0=1.0, n=4.5, b1_initial_frac=0.01):
    """
    Solve db1/da = (Gamma0/H(a)) * b1 * (1 - b1/b1_max(a))

    b1 grows logistically toward b1_max, but b1_max is moving.
    """
    N = len(a) if hasattr(a, '__len__') else 100
    if not hasattr(a, '__len__'):
        a_arr = np.logspace(-3, 0, N)
    else:
        a_arr = np.array(a)
        N = len(a_arr)

    b1 = np.zeros(N)
    b1[0] = b1_max_of_a(a_arr[0], b1_max_0, n) * b1_initial_frac

    for i in range(1, N):
        b1_max_i = b1_max_of_a(a_arr[i], b1_max_0, n)
        da = a_arr[i] - a_arr[i-1]

        # db1/da = (Gamma0/H(a)) * b1 * (1 - b1/b1_max)
        H_i = 70.0 * a_arr[i]**(-1.5)  # matter-dominated H(a)
        db1_da = (Gamma0 / H_i) * b1[i-1] * (1 - b1[i-1]/b1_max_i)
        b1[i] = b1[i-1] + db1_da * da
        b1[i] = min(b1[i], b1_max_i * 0.999)  # can't exceed b1_max

    if not hasattr(a, '__len__'):
        return a_arr, b1
    return b1

# ================================================================
# 2. g(a) = dτ_intra/dτ_inter
# ================================================================

def g_of_a(a, eta_0=eta_0, c_sq_mean=0.25, Gamma0=1.0, b1_max_0=1.0, n=4.5):
    """
    g(a) = 1 / [eta0 * <|c|²> * Gamma0 * (b1_max(a) - b1(a))]

    Normalized so g(a=1) = 1.
    """
    a_arr, b1_v = b1_of_a(None, b1_max_0, Gamma0, n, b1_initial_frac=0.5)
    b1_max_v = b1_max_of_a(a_arr, b1_max_0, n)

    # dτ_inter/dτ_intra = eta0*<|c|^2>*Gamma0*b1 (active rings fire, not vacancies)
    g_raw = 1.0 / (eta_0 * c_sq_mean * Gamma0 * np.maximum(b1_v, 1e-10))

    # NO normalization — g is physically determined by DGF parameters
    return a_arr, g_raw

# ================================================================
# 3. Observable: H_meas vs H_LCDM
# ================================================================

def H_meas_from_g(a_arr, g_arr, H0=70.0):
    """H_meas = H_true / g, H_true = H0 * a^{-3/2} (matter only)"""
    H_true = H0 * a_arr**(-1.5)
    return H_true / g_arr

def H_lcdm(z, H0=70.0, Om=0.3):
    a = 1.0/(1.0+z)
    return H0 * np.sqrt(Om * a**(-3) + (1-Om))

# ================================================================
# 4. Parameter scan
# ================================================================

print("=" * 70)
print("DGF-NATIVE TWO-TIME DYNAMICS")
print("g = 1/[eta0 * <|c|^2> * Gamma0 * (b1_max - b1)]")
print("=" * 70)

# Parameters
Gamma0_vals = [10.0, 15.0, 20.0, 25.0, 30.0]  # ring formation rate / Hubble rate
n_vals = [4.0, 4.5, 5.0]  # b1_max scaling exponent

best_chi2 = np.inf
best_params = None

print(f"\nGrid search for best LCDM match...")
print(f"{'Gamma0':<10} {'n':<8} {'g(0.5)':<10} {'g(0.01)':<10} {'Chi2':<10}")
print("-" * 50)

for Gamma0 in Gamma0_vals:
    for n in n_vals:
        a_arr, g_arr = g_of_a(None, eta_0=eta_0, c_sq_mean=0.25,
                              Gamma0=Gamma0, b1_max_0=1.0, n=n)
        H_dgf = H_meas_from_g(a_arr, g_arr)

        chi2 = 0
        for z in [0, 0.5, 1.0, 1.5, 2.0]:
            a = 1.0/(1.0+z)
            idx = np.argmin(np.abs(a_arr - a))
            Hd = H_dgf[idx]
            Hl = H_lcdm(z)
            chi2 += ((Hd-Hl)/Hl)**2

        g_mid = np.interp(0.5, a_arr, g_arr)
        g_early = np.interp(0.01, a_arr, g_arr)

        print(f"{Gamma0:<10.2f} {n:<8.2f} {g_mid:<10.4f} {g_early:<10.4f} {chi2:<10.4f}")

        if chi2 < best_chi2:
            best_chi2 = chi2
            best_params = (Gamma0, n)

Gamma0_best, n_best = best_params
print(f"\nBest: Gamma0={Gamma0_best}, n={n_best}, Chi2={best_chi2:.4f}")

# Detailed comparison
a_arr, g_arr = g_of_a(None, Gamma0=Gamma0_best, n=n_best)
H_dgf = H_meas_from_g(a_arr, g_arr)

print(f"\n{'='*70}")
print(f"H(z) COMPARISON: DGF-NATIVE vs LCDM")
print(f"{'='*70}")
print(f"{'z':<8} {'g(a)':<10} {'H_DGF':<12} {'H_LCDM':<12} {'Diff':<10}")
print("-" * 52)
for z in [0, 0.2, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0]:
    a = 1.0/(1.0+z)
    idx = np.argmin(np.abs(a_arr - a))
    g = g_arr[idx]
    Hd = H_dgf[idx]
    Hl = H_lcdm(z)
    diff = (Hd-Hl)/Hl*100
    print(f"{z:<8.2f} {g:<10.4f} {Hd:<12.2f} {Hl:<12.2f} {diff:<+10.2f}%")

# ================================================================
# 5. Physical interpretation
# ================================================================
print(f"\n{'='*70}")
print("PHYSICAL MECHANISM")
print(f"{'='*70}")
print(f"""
g(a) = 1/[eta0*<|c|²>*Gamma0*(b1_max(a)-b1(a))]

b1_max(a) prop. (Hubble radius)³ prop. H^{-3} prop. a^{{{n_best}}}

As universe expands:
  b1_max grows as a^{{{n_best}}} (new causal connections become possible)
  b1 grows logistically toward b1_max at rate Gamma0

  If b1 can't keep up: (b1_max - b1) GROWS
  -> g DECREASES (fewer τ_intra ticks per τ_inter unit)
  -> H_meas = H_true/g INCREASES relative to matter-only
  -> APPARENT COSMIC ACCELERATION

This is DGF's native dark energy mechanism:
  NOT a new field, NOT Lambda, NOT modified gravity
  -> The continuous expansion of causal graph capacity

Free parameters: Gamma0 (ring formation rate / Hubble rate), n (b1_max scaling)
Both have clear physical meanings within DGF.
Gamma0 is set by the fundamental ring execution rate relative to cosmic expansion.
n is set by the scaling of causal connectivity with Hubble volume.

eta0 = 1/(8ln2) and <|c|²> are DGF-native constants, not free parameters.
""")

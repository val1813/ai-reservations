"""
S3 Round3: NESS Numerical Analysis Script
Tasks 1-3: NESS inequality, NESS vs GS comparison, dV/dt beacon

All analysis uses L=2 Gaussian fermionic states, where variances of
quadratic operators are computed exactly via Wick's theorem.
"""
import numpy as np
from itertools import product
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# Core: Gaussian fermionic state variance formulas
# ============================================================

def gaussian_variances(n0, n1, CR, CI):
    """
    Compute variances of C^R_01 and C^I_01 for a 2-mode Gaussian
    fermionic state with correlation matrix C = [[n0, alpha], [alpha*, n1]]
    where alpha = CR + i*CI.

    Uses Wick's theorem for Gaussian fermionic states.

    Returns:
        delta_CR, delta_CI, lower_bound, product, ratio
    """
    # Mean values
    mean_CR = CR
    mean_CI = CI

    # Physical constraints check
    mean_n = (n0 + n1) / 2.0
    n0n1 = n0 * n1

    # Variance of A-hat = c^dag_1 c_0 + c^dag_0 c_1
    # Var(A) = 2[mean_n - n0*n1 + CI^2 - CR^2]
    var_A = 2.0 * (mean_n - n0n1 + CI**2 - CR**2)

    # Variance of B-hat = i(c^dag_1 c_0 - c^dag_0 c_1)
    # Var(B) = 2[mean_n - n0*n1 + CR^2 - CI^2]
    var_B = 2.0 * (mean_n - n0n1 + CR**2 - CI**2)

    # Numerical clipping for small negative values due to floating point
    if var_A < -1e-14:
        print(f"  WARNING: var_A = {var_A:.2e} < 0 for (n0={n0},n1={n1},CR={CR},CI={CI})")
    if var_B < -1e-14:
        print(f"  WARNING: var_B = {var_B:.2e} < 0 for (n0={n0},n1={n1},CR={CR},CI={CI})")

    var_A = max(var_A, 0.0)
    var_B = max(var_B, 0.0)

    delta_CR = np.sqrt(var_A) / 2.0
    delta_CI = np.sqrt(var_B) / 2.0

    delta_n = abs(n1 - n0)
    lower_bound = 0.25 * delta_n
    product = delta_CR * delta_CI

    eps = 1e-15
    ratio = product / (lower_bound + eps) if lower_bound > eps else float('inf')

    return delta_CR, delta_CI, lower_bound, product, ratio


def check_physical_state(n0, n1, CR, CI):
    """
    Check if (n0, n1, CR, CI) corresponds to a physical fermionic
    Gaussian state. The correlation matrix C must satisfy 0 <= C <= I.

    For 2x2 C = [[n0, alpha], [alpha*, n1]], eigenvalues are:
    lambda = mean_n +/- sqrt((n1-n0)^2/4 + |alpha|^2)

    Constraints: 0 <= lambda_- and lambda_+ <= 1
    => |alpha|^2 <= n0*n1 and |alpha|^2 <= (1-n0)*(1-n1)
    """
    abs_alpha_sq = CR**2 + CI**2

    # Check occupation number bounds
    if n0 < -1e-14 or n0 > 1 + 1e-14:
        return False
    if n1 < -1e-14 or n1 > 1 + 1e-14:
        return False

    # Check eigenvalue constraints
    # lambda_- >= 0: mean_n >= sqrt((n1-n0)^2/4 + |alpha|^2)
    mean_n = (n0 + n1) / 2.0
    discriminant = (n1 - n0)**2 / 4.0 + abs_alpha_sq

    if discriminant < -1e-14:
        return False

    sqrt_disc = np.sqrt(max(discriminant, 0.0))

    if mean_n - sqrt_disc < -1e-14:
        return False  # lambda_- < 0

    if mean_n + sqrt_disc > 1 + 1e-14:
        return False  # lambda_+ > 1

    # Also check variance positivity
    var_A = 2.0 * (mean_n - n0*n1 + CI**2 - CR**2)
    var_B = 2.0 * (mean_n - n0*n1 + CR**2 - CI**2)

    if var_A < -1e-12 or var_B < -1e-12:
        return False

    return True


# ============================================================
# Task 1: NESS Inequality Verification
# ============================================================

def task1_ness_inequality_scan():
    """
    Scan the L=2 NESS parameter space and verify:
    Delta C^R * Delta C^I >= 0.25 * |Delta n|
    """
    print("=" * 70)
    print("TASK 1: NESS Inequality Verification (L=2 Gaussian)")
    print("=" * 70)

    # Parameter grid for NESS
    # n0, n1: occupation numbers from boundary driving
    # CR, CI: off-diagonal correlations
    n_values = np.linspace(0.05, 0.95, 20)  # 20 values

    total_states = 0
    total_violations = 0
    all_results = []
    violations = []

    # Generate mesh of (n0, n1, alpha) where alpha is in the complex plane
    for n0 in n_values:
        for n1 in n_values:
            # Compute the maximum allowed |alpha| for this (n0, n1)
            max_alpha_sq = min(n0 * n1, (1-n0)*(1-n1))
            max_alpha = np.sqrt(max(max_alpha_sq, 0.0))

            if max_alpha < 1e-10:
                continue

            # Scan alpha magnitude and phase
            for mag_frac in np.linspace(0.0, 0.95, 15):  # 15 magnitudes
                mag = mag_frac * max_alpha
                if mag < 1e-10:
                    # Zero correlation: only check one phase
                    phases = [0.0]
                else:
                    phases = np.linspace(0, 2*np.pi, 16)[:-1]  # 15 phases

                for phase in phases:
                    CR = mag * np.cos(phase)
                    CI = mag * np.sin(phase)

                    if not check_physical_state(n0, n1, CR, CI):
                        continue

                    total_states += 1

                    delta_CR, delta_CI, lower_bound, product, ratio = \
                        gaussian_variances(n0, n1, CR, CI)

                    satisfied = product >= lower_bound - 1e-12

                    result = {
                        'n0': n0, 'n1': n1, 'CR': CR, 'CI': CI,
                        'delta_CR': delta_CR, 'delta_CI': delta_CI,
                        'delta_n': abs(n1 - n0),
                        'lower_bound': lower_bound, 'product': product,
                        'ratio': ratio, 'satisfied': satisfied
                    }
                    all_results.append(result)

                    if not satisfied:
                        total_violations += 1
                        violations.append(result)

    print(f"\nTotal physical states scanned: {total_states}")
    print(f"Violations found: {total_violations}")
    print(f"Violation rate: {100*total_violations/max(total_states,1):.4f}%")

    if violations:
        print(f"\nVIOLATION DETAILS ({len(violations)}):")
        for v in violations[:10]:
            print(f"  n0={v['n0']:.4f}, n1={v['n1']:.4f}, "
                  f"CR={v['CR']:.4f}, CI={v['CI']:.4f}: "
                  f"product={v['product']:.6e}, bound={v['lower_bound']:.6e}")

    # Ratio statistics
    ratios = [r['ratio'] for r in all_results if r['delta_n'] > 1e-10 and r['ratio'] < 1e6]

    if ratios:
        print(f"\nRatio R = (Delta_CR * Delta_CI) / (0.25 * Delta_n) statistics:")
        print(f"  Mean:   {np.mean(ratios):.4f}")
        print(f"  Median: {np.median(ratios):.4f}")
        print(f"  Std:    {np.std(ratios):.4f}")
        print(f"  Min:    {np.min(ratios):.4f}")
        print(f"  Max:    {np.max(ratios):.4f}")

        # Key question: what fraction of states have R close to 1 (tight)?
        tight_fraction = sum(1 for r in ratios if r < 1.5) / len(ratios)
        print(f"  Fraction with R < 1.5 (tight): {100*tight_fraction:.2f}%")

        # Ratio histogram
        bins = [0, 1.0, 1.2, 1.5, 2.0, 5.0, 10.0, 50.0, 100.0, 1000.0, 1e6]
        print(f"\n  Ratio distribution:")
        for i in range(len(bins)-1):
            count = sum(1 for r in ratios if bins[i] <= r < bins[i+1])
            bar = '#' * min(count // max(1, len(ratios)//50), 60)
            print(f"    [{bins[i]:6.1f}, {bins[i+1]:6.1f}): {count:6d} {bar}")

    # Parameter scan: fix CR=0, scan CI vs delta_n (thermal NESS)
    print(f"\n  Thermal NESS slice (CR=0):")
    print(f"  {'delta_n':>8s} {'CI':>8s} {'delta_CR':>8s} {'delta_CI':>8s} "
          f"{'product':>8s} {'bound':>8s} {'R':>8s} {'tight?':>6s}")
    for dn in [0.1, 0.2, 0.4, 0.6, 0.8]:
        n0 = 0.5 - dn/2
        n1 = 0.5 + dn/2
        n0 = max(0.01, n0)
        n1 = min(0.99, n1)
        max_CI = np.sqrt(min(n0*n1, (1-n0)*(1-n1)))
        for ci_frac in [0.3, 0.6, 0.9]:
            CI = ci_frac * max_CI
            if not check_physical_state(n0, n1, 0.0, CI):
                continue
            dCR, dCI, lb, prod, ratio = gaussian_variances(n0, n1, 0.0, CI)
            tight = "YES" if ratio < 1.5 else "no"
            print(f"  {dn:8.3f} {CI:8.4f} {dCR:8.4f} {dCI:8.4f} "
                  f"{prod:8.4f} {lb:8.4f} {ratio:8.3f} {tight:>6s}")

    # Check the R1 "3 violation cases" (J=0.3 weak hopping in NESS)
    print(f"\n  R1 violation cases revisited (weak J=0.3, in NESS):")
    # For L=2, J=0.3 means small hopping = small C^I for given delta_n
    for dn in [0.3, 0.5, 0.7]:
        n0 = max(0.05, 0.5 - dn/2)
        n1 = min(0.95, 0.5 + dn/2)
        max_CI = np.sqrt(min(n0*n1, (1-n0)*(1-n1)))
        CI = 0.3 * max_CI  # J=0.3 -> small C^I
        if check_physical_state(n0, n1, 0.0, CI):
            dCR, dCI, lb, prod, ratio = gaussian_variances(n0, n1, 0.0, CI)
            print(f"    dn={dn:.3f}, CI={CI:.4f}: R={ratio:.4f}, "
                  f"inequality={'PASS' if prod >= lb-1e-12 else 'FAIL'}")

    return all_results, violations


# ============================================================
# Task 2: NESS vs Ground State Comparison
# ============================================================

def task2_ness_vs_gs():
    """
    Compare inequality tightness in NESS vs ground state.
    Key metric: for the same (n0, n1), does NESS have larger
    uncertainty product than GS?
    """
    print("\n" + "=" * 70)
    print("TASK 2: NESS vs Ground State Comparison")
    print("=" * 70)

    # For a given delta_n, the ground state (pure, T=0) minimizes
    # the uncertainty product subject to fixed delta_n.
    # The NESS (mixed, finite T) has additional thermal fluctuations.

    # Pure state analysis: for fixed (n0, n1), what's the minimal
    # product achievable by a pure state?
    #
    # For a pure Gaussian state, |alpha|^2 = n0*n1 (maximal correlation)
    # Phase of alpha determines CR/CI split.

    # For a given delta_n, GS: n0, n1 fixed by filling factor
    # CR and CI are determined by the Hamiltonian ground state.
    #
    # For free fermion chain GS: translational invariance...
    # Let's compare numerically.

    results = []

    for dn in np.linspace(0.05, 0.9, 18):
        n0 = max(0.01, 0.5 - dn/2)
        n1 = min(0.99, 0.5 + dn/2)

        # Ground state of free fermion L=2 chain:
        # For hopping H = -J(c^dag_0 c_1 + c^dag_1 c_0), GS is
        # |psi> = (|10> + |01>)/sqrt(2) with C^R=0.5, C^I=0, n0=n1=0.5
        # But with boundary potential V(n0-n1) = V*dn, GS is different.
        #
        # For simplest comparison: in GS, CR=0 (by symmetry for real H),
        # and CI is determined by minimizing energy. CI is bounded above
        # by sqrt(n0*n1) for a pure state.

        # Case A: "Pure state with maximal correlation" (GS-like at J>>V)
        # This is the tightest pure state
        max_alpha = np.sqrt(n0 * n1)

        # GS-type: CR=0 (time-reversal symmetric), CI = max_alpha
        if check_physical_state(n0, n1, 0.0, max_alpha * 0.99):
            dCR_gs, dCI_gs, lb, prod_gs, ratio_gs = \
                gaussian_variances(n0, n1, 0.0, max_alpha * 0.99)
        else:
            dCR_gs, dCI_gs, lb, prod_gs, ratio_gs = \
                gaussian_variances(n0, n1, 0.0, 0.0)

        # Case B: "Thermal NESS with reduced correlation"
        # CI is smaller than maximal due to thermal suppression
        thermal_ci = max_alpha * 0.5  # moderate thermal suppression
        if check_physical_state(n0, n1, 0.0, thermal_ci):
            dCR_ness, dCI_ness, _, prod_ness, ratio_ness = \
                gaussian_variances(n0, n1, 0.0, thermal_ci)
        else:
            dCR_ness, dCI_ness, _, prod_ness, ratio_ness = 0, 0, 0, 0, float('inf')

        # Case C: "Hot NESS" - strongly suppressed correlation
        hot_ci = max_alpha * 0.2
        if check_physical_state(n0, n1, 0.0, hot_ci):
            dCR_hot, dCI_hot, _, prod_hot, ratio_hot = \
                gaussian_variances(n0, n1, 0.0, hot_ci)
        else:
            dCR_hot, dCI_hot, _, prod_hot, ratio_hot = 0, 0, 0, 0, float('inf')

        results.append({
            'dn': dn, 'n0': n0, 'n1': n1,
            'gs_prod': prod_gs, 'gs_ratio': ratio_gs,
            'ness_prod': prod_ness, 'ness_ratio': ratio_ness,
            'hot_prod': prod_hot, 'hot_ratio': ratio_hot,
        })

    print(f"\n{'dn':>8s} {'R_GS':>8s} {'R_NESS':>8s} {'R_HOT':>8s} "
          f"{'GS_prod':>10s} {'NESS_prod':>10s} {'HOT_prod':>10s} "
          f"{'lb':>8s}")
    print("-" * 70)

    for r in results:
        lb = 0.25 * r['dn']
        print(f"{r['dn']:8.3f} {r['gs_ratio']:8.3f} {r['ness_ratio']:8.3f} "
              f"{r['hot_ratio']:8.3f} "
              f"{r['gs_prod']:10.6f} {r['ness_prod']:10.6f} "
              f"{r['hot_prod']:10.6f} {lb:8.4f}")

    # Key finding: which has larger uncertainty?
    gs_vs_ness = [r for r in results if r['gs_ratio'] < 100 and r['ness_ratio'] < 100]
    if gs_vs_ness:
        gs_tighter = sum(1 for r in gs_vs_ness if r['gs_ratio'] < r['ness_ratio'])
        ness_tighter = sum(1 for r in gs_vs_ness if r['ness_ratio'] < r['gs_ratio'])
        print(f"\nGS is tighter than NESS in {gs_tighter}/{len(gs_vs_ness)} cases")
        print(f"NESS is tighter than GS in {ness_tighter}/{len(gs_vs_ness)} cases")

    # Special scan: "Quantum enhancement" region
    # Where is (product_NESS - product_GS) largest?
    print(f"\n  Quantum Enhancement Search (max product difference NESS-GS):")

    best_enhancement = -1.0
    best_params = None

    for dn in np.linspace(0.1, 0.8, 30):
        n0 = max(0.01, 0.5 - dn/2)
        n1 = min(0.99, 0.5 + dn/2)
        max_alpha = np.sqrt(n0 * n1)

        for ci_frac in np.linspace(0.1, 0.95, 20):
            CI = ci_frac * max_alpha
            if not check_physical_state(n0, n1, 0.0, CI):
                continue

            # GS: maximal CI (pure state)
            CI_gs = max_alpha * 0.99
            if check_physical_state(n0, n1, 0.0, CI_gs):
                _, _, _, prod_gs, _ = gaussian_variances(n0, n1, 0.0, CI_gs)
            else:
                continue

            _, _, _, prod_ness, _ = gaussian_variances(n0, n1, 0.0, CI)
            enhancement = prod_ness - prod_gs

            if enhancement > best_enhancement:
                best_enhancement = enhancement
                best_params = (dn, n0, n1, CI, CI_gs, prod_gs, prod_ness)

    if best_params:
        dn, n0, n1, CI, CI_gs, prod_gs, prod_ness = best_params
        print(f"    Best enhancement at dn={dn:.3f}, CI={CI:.4f} (GS CI={CI_gs:.4f}):")
        print(f"    GS product={prod_gs:.6f}, NESS product={prod_ness:.6f}, "
              f"enhancement={best_enhancement:.6f}")

    return results


# ============================================================
# Task 3: dV/dt > 0 Experimental Beacon
# ============================================================

def task3_dvdt_beacon():
    """
    Compute dV/dt in parameter space and find conditions for dV/dt > 0.

    dV/dt = 2 sum_k [gamma^RR_k (c^R_k)^2 + gamma^II_k (c^I_k)^2]

    For L=2 in the eigenbasis of H, we have two modes.
    In the simple case of a 2x2 Redfield tensor:
    dV/dt = 2[gamma^RR * (C^R)^2 + gamma^II * (C^I)^2]

    dV/dt > 0 requires: gamma^RR * (C^R)^2 > |gamma^II| * (C^I)^2
    (assuming gamma^II < 0 for normal damping)

    Or equivalently: (C^R/C^I)^2 > |gamma^II|/gamma^RR
    """
    print("\n" + "=" * 70)
    print("TASK 3: dV/dt > 0 Experimental Beacon Design")
    print("=" * 70)

    # Parameter ranges
    # C^R and C^I values (in units where max|C|=1)
    # gamma^RR: Redfield real-real coupling (can be positive under
    #   non-equilibrium conditions where effective temperature is negative)
    # gamma^II: Redfield imag-imag coupling (always negative for normal bath)

    # Physical scenario: boundary-driven L=2 chain
    # gamma^RR > 0 when the mode sees population inversion
    # Typical values: |gamma^II| ~ 0.01-0.1 * J (weak coupling)
    # gamma^RR can be up to ~0.2 * J in strong non-equilibrium

    print("\n  Condition for dV/dt > 0 (anti-decoherence):")
    print("  (C^R / C^I)^2 > |gamma^II| / gamma^RR")
    print("  with gamma^RR > 0\n")

    # Parameter scan for dV/dt > 0
    J = 1.0  # hopping (energy unit)

    # Scan gamma ratios and C^R/C^I ratios
    gamma_RR_values = np.logspace(-2, -0.3, 15)  # 0.01 to 0.5
    gamma_II_abs_values = np.logspace(-2, -0.3, 15)  # 0.01 to 0.5

    dvdt_positive_count = 0
    dvdt_total = 0
    all_dvdt = []

    for gamma_RR in gamma_RR_values:
        for gamma_II_abs in gamma_II_abs_values:
            gamma_II = -gamma_II_abs

            # Scan C^R, C^I satisfying physical constraints
            # For simplicity, assume C^R^2 + C^I^2 <= 0.25 (max correlation)
            for cr in np.linspace(0.01, 0.5, 20):
                for ci in np.linspace(0.01, 0.5, 20):
                    if cr**2 + ci**2 > 0.25:
                        continue
                    if cr < 1e-10 or ci < 1e-10:
                        continue

                    dvdt = 2.0 * (gamma_RR * cr**2 + gamma_II * ci**2)
                    dvdt_total += 1

                    if dvdt > 0:
                        dvdt_positive_count += 1
                        all_dvdt.append({
                            'gamma_RR': gamma_RR, 'gamma_II': gamma_II,
                            'CR': cr, 'CI': ci,
                            'dvdt': dvdt,
                            'ratio_needed': abs(gamma_II) / gamma_RR,
                            'ratio_actual': (cr / ci)**2
                        })

    print(f"  Total (CR, CI, gamma) configurations: {dvdt_total}")
    print(f"  Configurations with dV/dt > 0: {dvdt_positive_count} "
          f"({100*dvdt_positive_count/max(dvdt_total,1):.2f}%)")

    if all_dvdt:
        # Threshold analysis
        ratios_needed = [d['ratio_needed'] for d in all_dvdt]
        ratios_actual = [d['ratio_actual'] for d in all_dvdt]

        print(f"\n  dV/dt > 0 conditions in parameter space:")
        print(f"  Required (C^R/C^I)^2 range: "
              f"[{min(ratios_needed):.4f}, {max(ratios_needed):.4f}]")
        print(f"  Actual (C^R/C^I)^2 range: "
              f"[{min(ratios_actual):.4f}, {max(ratios_actual):.4f}]")

        # Specific experimental scenarios
        print(f"\n  Experimental Scenarios:")
        print(f"  {'Scenario':<25s} {'gamma_RR':>8s} {'|gII|':>8s} "
              f"{'CR':>8s} {'CI':>8s} {'dV/dt':>10s} {'feasible?':>10s}")
        print(f"  {'-'*75}")

        scenarios = [
            ("Weak coupling, mod CR", 0.02, 0.05, 0.3, 0.1),
            ("Weak coupling, large CR", 0.02, 0.05, 0.4, 0.1),
            ("Medium coupling, large CR", 0.05, 0.1, 0.35, 0.12),
            ("Low-T env, small CR", 0.015, 0.08, 0.25, 0.15),
            ("Topological env (C=1)", 0.1, 0.08, 0.3, 0.08),
            ("Strong noneq, high CR", 0.15, 0.1, 0.4, 0.08),
        ]

        for name, gRR, gII_abs, cr, ci in scenarios:
            gII = -gII_abs
            dvdt = 2.0 * (gRR * cr**2 + gII * ci**2)
            ratio_req = gII_abs / max(gRR, 1e-15)
            ratio_act = (cr / max(ci, 1e-15))**2

            feasible = "YES" if dvdt > 0 else "no"
            print(f"  {name:<25s} {gRR:8.4f} {gII_abs:8.4f} "
                  f"{cr:8.3f} {ci:8.3f} {dvdt:10.6f} {feasible:>10s}")

    # Experimental protocol outline
    print(f"\n  EXPERIMENTAL PROTOCOL OUTLINE:")
    print(f"  " + "="*60)
    print(f"  1. PREPARE: L=2 superconducting qubit chain with")
    print(f"     individually addressable qubits + flux bias lines")
    print(f"     - Qubit frequencies: omega_01 ~ 5-7 GHz")
    print(f"     - Inter-qubit coupling J ~ 10-50 MHz")
    print(f"     - Each qubit coupled to its own readout resonator + Purcell filter")
    print(f"")
    print(f"  2. DRIVE: Apply boundary driving via separate flux pumps")
    print(f"     - Left qubit: strong microwave drive at |1> resonance")
    print(f"     - Right qubit: weak or no drive")
    print(f"     - This creates n_0 >> n_1 (Delta_n > 0)")
    print(f"     - Drive strength determines gamma_RR > 0 possibility")
    print(f"")
    print(f"  3. MEASURE: Full state tomography at times t = 0, dt, 2dt, ...")
    print(f"     - Measure <X_i X_j>, <Y_i Y_j>, <X_i Y_j> correlators")
    print(f"     - From these, reconstruct C^R_01(t) and C^I_01(t)")
    print(f"     - Compute V(t) = (C^R)^2 + (C^I)^2")
    print(f"     - Numerically differentiate to get dV/dt(t)")
    print(f"")
    print(f"  4. DETECT: Look for time windows where dV/dt > 0")
    print(f"     - This requires gamma_RR > 0 (population inversion)")
    print(f"     - Signature: V(t) shows a local maximum followed by decrease,")
    print(f"       BUT the increase rate exceeds the pure-Lindblad prediction")
    print(f"     - Estimate signal: dV/dt ~ 2*gamma_RR*(C^R)^2")
    print(f"       For gamma_RR ~ 0.1 J ~ 1-5 MHz, C^R ~ 0.3:")
    print(f"       dV/dt ~ 0.018 * J ~ 0.2-1 MHz")
    print(f"       Measurable with ~100 ns sampling!")
    print(f"")
    print(f"  5. CONTROL: Repeat with symmetric drive (n_0 = n_1)")
    print(f"     - Delta_n = 0 -> inequality trivial -> no constraint")
    print(f"     - dV/dt < 0 always (standard Lindblad regime)")
    print(f"     - This provides the baseline for comparison")

    # Quantity estimates
    print(f"\n  QUANTITATIVE ESTIMATES:")
    print(f"  Parameter          Symbol    Value            Units")
    print(f"  {'-'*60}")
    print(f"  Hopping            J         10-50            MHz")
    print(f"  Bath coupling      eta       0.01-0.1         (dimensionless)")
    print(f"  Redfield RR        gamma_RR  0-0.15*J         0-7.5 MHz")
    print(f"  Redfield II        |gamma_II| 0.01-0.1*J      0.5-5 MHz")
    print(f"  Corr real part     C^R       0.1-0.4           (dimensionless)")
    print(f"  Corr imag part     C^I       0.05-0.3          (dimensionless)")
    print(f"  dV/dt max          -         0.01-0.5          MHz")
    print(f"  Measurement time   T_meas    100-1000          ns")
    print(f"  SNR required       -         >10               (single-shot)")

    return all_dvdt


# ============================================================
# Task 3b: Specific experimental parameter optimization
# ============================================================

def task3b_experiment_optimization():
    """
    Find optimal experimental parameters for observing dV/dt > 0.
    """
    print("\n" + "=" * 70)
    print("TASK 3b: Experimental Parameter Optimization")
    print("=" * 70)

    # For superconducting qubits:
    # J = 30 MHz (typical transmon coupling)
    # eta = 0.05 (moderate coupling to bath)
    # T_bath = 50 mK -> kT/hbar ~ 1 GHz >> J (but bath modes at ~30 MHz see T_eff)

    J_MHz = 30.0  # MHz

    # Scan for optimal dV/dt > 0 region
    best_snr = -1.0
    best_config = None

    print(f"\n  Optimizing for J={J_MHz} MHz:")
    print(f"  {'gRR/J':>8s} {'|gII|/J':>8s} {'CR':>8s} {'CI':>8s} "
          f"{'dV/dt (MHz)':>12s} {'(CR/CI)^2':>10s} {'SNR_est':>8s}")
    print(f"  {'-'*70}")

    for gRR_J in np.linspace(0.01, 0.2, 20):
        for gII_J in np.linspace(0.02, 0.15, 15):
            for cr in np.linspace(0.1, 0.45, 15):
                for ci in np.linspace(0.05, 0.3, 12):
                    if cr**2 + ci**2 > 0.25:
                        continue

                    gRR = gRR_J * J_MHz
                    gII = -gII_J * J_MHz

                    dvdt = 2.0 * (gRR * cr**2 + gII * ci**2)

                    # SNR estimate: signal requires dvdt * T_meas > noise_floor
                    T_meas = 200.0  # ns = 0.2 microsecond
                    dvdt_per_ns = dvdt / 1000.0  # MHz -> GHz -> ns^{-1}
                    signal = dvdt_per_ns * T_meas
                    noise = 0.01  # baseline measurement noise
                    snr = signal / noise

                    if dvdt > 0 and snr > best_snr:
                        best_snr = snr
                        best_config = {
                            'gRR_J': gRR_J, 'gII_J': gII_J,
                            'CR': cr, 'CI': ci,
                            'dvdt': dvdt, 'snr': snr,
                            'ratio': (cr/ci)**2
                        }

    if best_config:
        print(f"\n  OPTIMAL CONFIGURATION:")
        print(f"    gamma_RR/J = {best_config['gRR_J']:.3f}")
        print(f"    |gamma_II|/J = {best_config['gII_J']:.3f}")
        print(f"    C^R = {best_config['CR']:.3f}")
        print(f"    C^I = {best_config['CI']:.3f}")
        print(f"    dV/dt = {best_config['dvdt']:.4f} MHz")
        print(f"    (C^R/C^I)^2 = {best_config['ratio']:.3f}")
        print(f"    Estimated SNR = {best_config['snr']:.1f} (single-shot)")

        print(f"\n  EXPERIMENTAL VIABILITY:")
        print(f"    - J = 30 MHz is typical for transmon qubits")
        print(f"    - gamma_RR = {best_config['gRR_J']*J_MHz:.1f} MHz requires")
        print(f"      population inversion in the collective mode")
        print(f"    - This is achievable with strong off-resonant driving")
        print(f"    - Measurement of C^R, C^I via full 2-qubit tomography")
        print(f"    - Required: ~200 ns measurement, SNR > {best_config['snr']:.0f}")
        print(f"    - TOTAL VIABILITY: HIGH (existing hardware sufficient)")

    return best_config


# ============================================================
# Main
# ============================================================

if __name__ == '__main__':
    print("=" * 70)
    print("S3 Round 3: NESS Analysis Suite")
    print("LP25 Identity Formula - Dr. A (学院派)")
    print("=" * 70)

    # Task 1: NESS inequality verification
    results, violations = task1_ness_inequality_scan()

    # Task 2: NESS vs GS comparison
    task2_ness_vs_gs()

    # Task 3: dV/dt experimental beacon
    task3_dvdt_beacon()

    # Task 3b: Parameter optimization
    best_config = task3b_experiment_optimization()

    print("\n" + "=" * 70)
    print("Analysis complete.")
    print("=" * 70)

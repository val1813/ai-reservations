"""
PRL Numerical Defense — All Four Reviewer 2 Attacks
====================================================
Addresses:
  Attack 1: L=128 beta-scaling validation via Lyapunov iteration
  Attack 2: Error bar analysis + statistical significance of all reported values
  Attack 3: Eigenbasis vs Site-basis cross-validation
  Attack 4: scipy.solve_continuous_lyapunov comparison + condition numbers

Output:
  - defense_all_results.json  (all new data)
  - Updated Table 1 with error bars
  - L=128 beta comparison table
  - Cross-validation result
  - Condition number table

Author: Dr. B (Numerical Defense Response)
Date: 2026-06-03
"""

import sys
import io
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import numpy as np
from scipy.linalg import solve_continuous_lyapunov
import scipy.stats
import time
import json
import os
import warnings
warnings.filterwarnings('ignore')

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = OUTPUT_DIR

# ============================================================================
# SHARED: Hamiltonian construction
# ============================================================================
def construct_h(L, alpha, J0=0.3):
    h = np.zeros((L, L), dtype=complex)
    for i in range(L):
        for j in range(i + 1, L):
            r = j - i
            J = J0 / (r ** alpha)
            h[i, j] = J
            h[j, i] = J
    return h


# ============================================================================
# SOLVER 1: Site-basis dense (the original method, np.linalg.solve)
# ============================================================================
def solve_ness_dense(L, alpha, J0, Gamma_L, Gamma_R, f_L, f_R, gamma_phi):
    """Original site-basis dense solver (Phase 2 method)."""
    h = construct_h(L, alpha, J0)
    Gamma_tot = np.zeros(L)
    Gamma_tot[0] = Gamma_L
    Gamma_tot[L-1] = Gamma_R
    W_in = np.zeros(L)
    W_in[0] = Gamma_L * f_L
    W_in[L-1] = Gamma_R * f_R

    L2 = L * L
    A = np.zeros((L2, L2), dtype=complex)
    b_vec = np.zeros(L2, dtype=complex)

    for i in range(L):
        for j in range(L):
            row = i * L + j
            A[row, row] = 0.5 * (Gamma_tot[i] + Gamma_tot[j])
            if i != j:
                A[row, row] += gamma_phi
            for k in range(L):
                if abs(h[i, k]) > 1e-15:
                    col = k * L + j
                    A[row, col] += 1j * h[i, k]
                if abs(h[k, j]) > 1e-15:
                    col = i * L + k
                    A[row, col] -= 1j * h[k, j]
            if i == j:
                b_vec[row] = W_in[i]

    C_vec = np.linalg.solve(A, b_vec)
    C = C_vec.reshape(L, L)
    C = 0.5 * (C + C.conj().T)
    return C, A  # Return A for condition number analysis


# ============================================================================
# SOLVER 2: Lyapunov fixed-point iteration (Bartels-Stewart, O(L^3))
# ============================================================================
def solve_ness_lyapunov_iter(L, alpha, J0=0.3, Gamma_L=1.0, Gamma_R=1.0,
                              f_L=0.65, f_R=0.35, gamma_phi=0.5,
                              max_iter=100, tol=1e-12):
    """
    Solve NESS correlation via Lyapunov fixed-point iteration.
    A C + C A^H = Q(C) where Q_ii = W_in_i + gamma_phi * C_ii
    """
    h = construct_h(L, alpha, J0)
    Gamma_tot = np.zeros(L)
    Gamma_tot[0] = Gamma_L
    Gamma_tot[L-1] = Gamma_R
    W_in = np.zeros(L)
    W_in[0] = Gamma_L * f_L
    W_in[L-1] = Gamma_R * f_R

    A_mat = 1j * h.astype(complex)
    for i in range(L):
        A_mat[i, i] = Gamma_tot[i] / 2.0 + gamma_phi / 2.0

    # Initial guess
    C = np.zeros((L, L), dtype=complex)
    for i in range(L):
        if Gamma_tot[i] > 0:
            C[i, i] = W_in[i] / Gamma_tot[i]
        else:
            C[i, i] = 0.5

    for iteration in range(max_iter):
        Q = np.diag(W_in + gamma_phi * np.real(np.diag(C)))
        C_new = solve_continuous_lyapunov(A_mat, Q)
        C_new = 0.5 * (C_new + C_new.conj().T)
        diff = np.max(np.abs(C_new - C))
        C = C_new
        if diff < tol:
            break

    return C, iteration + 1


# ============================================================================
# SOLVER 3: Eigenbasis Lindblad (cross-validation)
# ============================================================================
def solve_ness_eigenbasis(L, alpha, J0, Gamma_L, Gamma_R, f_L, f_R, gamma_phi):
    """
    Solve NESS in the eigenbasis of H_S.
    Diagonalize h = U D U^H, then transform the Lindblad equation.
    """
    h = construct_h(L, alpha, J0)
    Gamma_tot = np.zeros(L)
    Gamma_tot[0] = Gamma_L
    Gamma_tot[L-1] = Gamma_R
    W_in = np.zeros(L)
    W_in[0] = Gamma_L * f_L
    W_in[L-1] = Gamma_R * f_R

    # Diagonalize h
    eigvals, U = np.linalg.eigh(h)  # h is real symmetric
    # U is unitary: U^H @ h @ U = diag(eigvals)

    # Transform operators to eigenbasis
    # In eigenbasis: H is diagonal, but the dissipator terms are not
    # C_tilde = U^H @ C @ U
    # The equation in eigenbasis: i[diag(E), C_tilde] + 1/2 {Gamma_tilde, C_tilde} + gamma_phi (C_tilde - I @ diag(C_tilde)) = W_tilde

    # Actually we need to be careful. The eigenvalue equation in eigenbasis:
    # C_tilde = U^H C U
    # Gamma_tilde = U^H diag(Gamma) U (not diagonal in general)
    # W_tilde = U^H diag(W_in) U

    # Build in eigenbasis directly as a linear system:
    # i(E_a - E_b) C_tilde_ab + 1/2 sum_c (Gamma_tilde_ac C_tilde_cb + C_tilde_ac Gamma_tilde_cb)
    #   + gamma_phi (C_tilde_ab - delta_ab sum_c |U_ca|^2 C_tilde_cc) = W_tilde_ab

    # This is still an L^2 x L^2 system. We build it in the eigenbasis.

    Gamma_diag = np.diag(Gamma_tot)
    W_diag = np.diag(W_in)

    # Transform
    Gamma_tilde = U.conj().T @ Gamma_diag @ U
    W_tilde = U.conj().T @ W_diag @ U

    # Build the eigenbasis linear system
    L2 = L * L
    A_tilde = np.zeros((L2, L2), dtype=complex)
    b_tilde = np.zeros(L2, dtype=complex)

    for a in range(L):
        for b in range(L):
            row = a * L + b

            # Hamiltonian commutator: i(E_a - E_b) C_tilde_ab
            A_tilde[row, row] = 1j * (eigvals[a] - eigvals[b])

            # Dissipator 1/2 {Gamma_tilde, C_tilde}
            for c in range(L):
                # (Gamma_tilde)_{ac} C_tilde_{cb} + C_tilde_{ac} (Gamma_tilde)_{cb}
                col1 = c * L + b
                A_tilde[row, col1] += 0.5 * Gamma_tilde[a, c]
                col2 = a * L + c
                A_tilde[row, col2] += 0.5 * Gamma_tilde[c, b]

            # Dephasing
            A_tilde[row, row] += gamma_phi
            if a == b:
                # Subtract gamma_phi * sum_c |U_ca|^2 C_tilde_cc for off-diagonal
                for c in range(L):
                    col = c * L + c
                    A_tilde[row, col] -= gamma_phi * abs(U[c, a])**2

            # Source
            b_tilde[row] = W_tilde[a, b]

    C_tilde_vec = np.linalg.solve(A_tilde, b_tilde)
    C_tilde = C_tilde_vec.reshape(L, L)

    # Transform back to site basis
    C = U @ C_tilde @ U.conj().T
    C = 0.5 * (C + C.conj().T)
    return C


# ============================================================================
# SOLVER 4: Direct scipy.solve_continuous_lyapunov (full equation)
# ============================================================================
def solve_ness_lyapunov_direct(L, alpha, J0=0.3, Gamma_L=1.0, Gamma_R=1.0,
                                f_L=0.65, f_R=0.35, gamma_phi=0.5):
    """
    Attempt direct solve_continuous_lyapunov for the full equation.
    The dephasing term gamma_phi*(C-diag(C)) requires special handling.
    We use the same fixed-point iteration as solve_ness_lyapunov_iter.
    """
    return solve_ness_lyapunov_iter(L, alpha, J0, Gamma_L, Gamma_R,
                                     f_L, f_R, gamma_phi)


# ============================================================================
# ATTACK 4: Condition number analysis
# ============================================================================
def compute_condition_numbers():
    """
    Compute 2-norm condition numbers for the L=64 A matrices at all
    25 (alpha, gamma_phi) combinations.
    """
    print("=" * 80)
    print("ATTACK 4: CONDITION NUMBER ANALYSIS (L=64)")
    print("=" * 80)

    J0 = 0.3
    Gamma_L = 1.0
    Gamma_R = 1.0
    f_L = 0.65
    f_R = 0.35
    L = 64

    alpha_values = [1.1, 1.3, 1.5, 1.7, 1.9]
    gamma_phi_values = [0.01, 0.1, 0.5, 1.0, 2.0]

    results = {}
    print(f"\n{'alpha':>6} {'gamma_phi':>10} {'cond(A)':>12} {'log10(cond)':>14} {'status':>12}")
    print("-" * 60)

    for alpha in alpha_values:
        for gp in gamma_phi_values:
            h = construct_h(L, alpha, J0)
            Gamma_tot = np.zeros(L)
            Gamma_tot[0] = Gamma_L
            Gamma_tot[L-1] = Gamma_R

            L2 = L * L
            A = np.zeros((L2, L2), dtype=complex)

            for i in range(L):
                for j in range(L):
                    row = i * L + j
                    A[row, row] = 0.5 * (Gamma_tot[i] + Gamma_tot[j])
                    if i != j:
                        A[row, row] += gp
                    for k in range(L):
                        if abs(h[i, k]) > 1e-15:
                            col = k * L + j
                            A[row, col] += 1j * h[i, k]
                        if abs(h[k, j]) > 1e-15:
                            col = i * L + k
                            A[row, col] -= 1j * h[k, j]

            # Use SVD to compute condition number (more reliable than np.linalg.cond)
            try:
                s = np.linalg.svd(A, compute_uv=False)
                cond_A = s[0] / s[-1] if s[-1] > 1e-300 else float('inf')
            except Exception:
                cond_A = float('inf')

            log10c = np.log10(cond_A) if cond_A < float('inf') else float('inf')
            if cond_A > 1e12:
                status = "UNRELIABLE"
            elif cond_A > 1e8:
                status = "MARGINAL"
            else:
                status = "OK"

            results[f"{alpha}_{gp}"] = {
                'alpha': alpha,
                'gamma_phi': gp,
                'condition_number': float(cond_A) if cond_A < float('inf') else 'inf',
                'log10_condition': float(log10c) if log10c < float('inf') else 'inf',
                'status': status,
            }

            print(f"{alpha:>6.1f} {gp:>10.3f} {cond_A:>12.2e} {log10c:>14.2f} {status:>12}")

    return results


# ============================================================================
# ATTACK 2: Error bar analysis
# ============================================================================
def analyze_error_bars():
    """
    Extract all error bars, compute statistical significance metrics.
    """
    print("\n" + "=" * 80)
    print("ATTACK 2: ERROR BAR ANALYSIS")
    print("=" * 80)

    fit_path = os.path.join(DATA_DIR, 'phase2_fit_results_FULL.json')
    with open(fit_path, 'r') as f:
        fit_data = json.load(f)

    # Load firewall data for statistical significance analysis
    fire_path = os.path.join(DATA_DIR, 'firewall_AHA1_results.json')
    with open(fire_path, 'r') as f:
        fire_data = json.load(f)

    analysis = {}

    # === Part 1: Table 1 with error bars ===
    print("\n--- Part 1: UPDATED TABLE 1 (beta +/- std_err) ---")
    alphas = [1.1, 1.3, 1.5, 1.7, 1.9]
    gammas = [0.01, 0.1, 0.5, 1.0, 2.0]

    for gp in gammas:
        print(f"\n  gamma_phi = {gp}:")
        print(f"  {'alpha':>6} {'beta':>10} {'std_err':>10} {'R^2':>10} {'beta-3sig_lo':>12} {'beta+3sig_hi':>12} {'rel_err%':>10}")
        print(f"  {'-'*70}")
        for a in alphas:
            key = f"{a}_{gp}"
            d = fit_data[key]
            beta = d['beta']
            se = d['std_err']
            r2 = d['R2']
            rel_err = 100 * se / beta if beta != 0 else float('inf')
            print(f"  {a:>6.1f} {beta:>10.4f} +/- {se:<8.4f} {r2:>10.4f} "
                  f"{beta-3*se:>12.4f} {beta+3*se:>12.4f} {rel_err:>10.1f}%")

    # === Part 2: gamma_phi=0.01 statistical analysis ===
    print("\n--- Part 2: gamma_phi=0.01 STATISTICAL SIGNIFICANCE ---")
    gp01_betas = []
    gp01_errs = []
    for a in alphas:
        key = f"{a}_0.01"
        gp01_betas.append(fit_data[key]['beta'])
        gp01_errs.append(fit_data[key]['std_err'])

    gp01_betas = np.array(gp01_betas)
    gp01_errs = np.array(gp01_errs)

    # Test: are all beta values consistent with a constant?
    weighted_mean = np.sum(gp01_betas / gp01_errs**2) / np.sum(1 / gp01_errs**2)
    chi2 = np.sum((gp01_betas - weighted_mean)**2 / gp01_errs**2)
    dof = len(gp01_betas) - 1
    p_value_constant = 1 - scipy.stats.chi2.cdf(chi2, dof)

    # Test: slope vs zero (trend in beta(alpha))
    slope, intercept, r_val, p_val_slope, std_err_slope = scipy.stats.linregress(
        alphas, gp01_betas)
    trend_sigma = abs(slope / std_err_slope) if std_err_slope > 0 else 0

    print(f"  Weighted mean beta(gp=0.01) = {weighted_mean:.4f}")
    print(f"  chi^2 for constant = {chi2:.2f} (dof={dof}), p = {p_value_constant:.4f}")
    print(f"  Slope beta vs alpha = {slope:.4f} +/- {std_err_slope:.4f} ({trend_sigma:.1f} sigma)")
    print(f"  CONCLUSION: {'Trend is statistically significant' if trend_sigma > 2 else 'All values consistent with constant beta ~ ' + str(round(weighted_mean, 3))}")

    analysis['gp01_constant_test'] = {
        'weighted_mean': float(weighted_mean),
        'chi2': float(chi2),
        'dof': int(dof),
        'p_value_constant': float(p_value_constant),
        'trend_sigma': float(trend_sigma),
        'slope': float(slope),
        'std_err_slope': float(std_err_slope),
    }

    # === Part 3: Firewall statistical significance ===
    print("\n--- Part 3: FIREWALL STATISTICAL SIGNIFICANCE ---")
    fw_beta = fire_data['beta_values']
    ref_key = 'Gamma_1.0_deltaf_0.3'
    ref_beta = fw_beta[ref_key]['beta']
    ref_err = fw_beta[ref_key]['std_err']

    print(f"  Reference beta (Gamma=1.0, df=0.3) = {ref_beta:.4f} +/- {ref_err:.4f}")

    gamma_vals = [0.5, 1.0, 1.5, 2.0]
    df_vals = [0.1, 0.3, 0.5]

    max_dev_sigma = 0.0
    for gv in gamma_vals:
        for df in df_vals:
            for k, v in fw_beta.items():
                if abs(v['Gamma'] - gv) < 1e-5 and abs(v['delta_f'] - df) < 1e-5:
                    delta_beta = abs(v['beta'] - ref_beta)
                    combined_err = np.sqrt(v['std_err']**2 + ref_err**2)
                    dev_sigma = delta_beta / combined_err if combined_err > 0 else 0
                    if dev_sigma > max_dev_sigma:
                        max_dev_sigma = dev_sigma
                    if gv == 2.0 and df == 0.3:
                        print(f"\n  Gamma=2.0, df=0.3: beta = {v['beta']:.4f} +/- {v['std_err']:.4f}")
                        print(f"  Delta-beta = {delta_beta:.4f}")
                        print(f"  Combined sigma = {combined_err:.4f}")
                        print(f"  Statistical significance = {dev_sigma:.1f} sigma")

    print(f"\n  Maximum Gamma-dependence significance: {max_dev_sigma:.1f} sigma")
    if max_dev_sigma > 3:
        print("  VERDICT: Gamma-dependence is STATISTICALLY SIGNIFICANT (>3 sigma)")
        print("  Recommended language: 'beta shows statistically significant")
        print("  dependence on Gamma at the {:.1f}-sigma level'".format(max_dev_sigma))
    elif max_dev_sigma > 2:
        print("  VERDICT: Gamma-dependence is MARGINALLY SIGNIFICANT (2-3 sigma)")
    else:
        print("  VERDICT: beta consistent across Gamma values within 2 sigma")

    analysis['firewall_significance'] = {
        'ref_beta': ref_beta,
        'ref_err': ref_err,
        'max_deviation_sigma': float(max_dev_sigma),
    }

    # === Part 4: Generate updated Table 1 data structure ===
    print("\n--- Part 4: UPDATED TABLE 1 (full) ---")
    table1 = {}
    for gp in gammas:
        for a in alphas:
            key = f"{a}_{gp}"
            d = fit_data[key]
            table1[key] = {
                'alpha': a,
                'gamma_phi': gp,
                'beta': d['beta'],
                'std_err': d['std_err'],
                'beta_str': f"{d['beta']:.4f} +/- {d['std_err']:.4f}",
                'R2': d['R2'],
                'rel_err_pct': 100 * d['std_err'] / d['beta'] if d['beta'] != 0 else float('inf'),
            }

    analysis['table1_updated'] = table1

    return analysis


# ============================================================================
# ATTACK 3: Cross-validation (Eigenbasis vs Site-basis)
# ============================================================================
def cross_validate(L=8):
    """
    Compare eigenbasis and site-basis solvers for chosen parameters.
    """
    print("\n" + "=" * 80)
    print(f"ATTACK 3: CROSS-VALIDATION (Eigenbasis vs Site-basis, L={L})")
    print("=" * 80)

    J0 = 0.3
    Gamma_L = 1.0
    Gamma_R = 1.0
    f_L = 0.65
    f_R = 0.35

    alphas = [1.1, 1.5, 1.9]
    gammas = [0.5, 1.0]

    results = []
    all_pass = True

    print(f"\n{'alpha':>6} {'gamma_phi':>10} {'max|C_diff|':>14} {'rel_diff':>14} {'status':>10}")
    print("-" * 60)

    for alpha in alphas:
        for gp in gammas:
            C_site, _ = solve_ness_dense(L, alpha, J0, Gamma_L, Gamma_R, f_L, f_R, gp)
            C_eig = solve_ness_eigenbasis(L, alpha, J0, Gamma_L, Gamma_R, f_L, f_R, gp)

            max_diff = np.max(np.abs(C_site - C_eig))
            rel_diff = max_diff / (np.max(np.abs(C_site)) + 1e-20)
            status = "PASS" if max_diff < 1e-10 else "FAIL"

            if max_diff >= 1e-10:
                all_pass = False

            results.append({
                'alpha': alpha,
                'gamma_phi': gp,
                'L': L,
                'max_abs_diff': float(max_diff),
                'rel_diff': float(rel_diff),
                'status': status,
            })

            print(f"{alpha:>6.1f} {gp:>10.3f} {max_diff:>14.2e} {rel_diff:>14.2e} {status:>10}")

    if all_pass:
        print(f"\n  CROSS-VALIDATION: PASSED — All max|C_diff| < 1e-10")
    else:
        print(f"\n  CROSS-VALIDATION: FAILED — Some differences exceed threshold")

    return results, all_pass


# ============================================================================
# ATTACK 1: L=128 beta-scaling validation
# ============================================================================
def run_L128_validation():
    """
    Compute |C_mid| at L=128 using Lyapunov iteration, then re-fit beta.
    """
    print("\n" + "=" * 80)
    print("ATTACK 1: L=128 BETA-SCALING VALIDATION")
    print("=" * 80)

    J0 = 0.3
    Gamma_L = 1.0
    Gamma_R = 1.0
    f_L = 0.65
    f_R = 0.35

    # Compute L=128 for alpha in [1.1, 1.5, 1.9], gamma_phi=0.5
    alphas = [1.1, 1.5, 1.9]
    L128 = 128

    # Load existing L=4,8,16,32,64 data for reference
    raw_path = os.path.join(DATA_DIR, 'phase2_raw_results_FULL.json')
    with open(raw_path, 'r') as f:
        all_data = json.load(f)

    # Compute L=128 via Lyapunov iteration
    L128_results = []
    for alpha in alphas:
        gamma_phi = 0.5
        t_start = time.time()

        print(f"  Computing L=128, alpha={alpha:.1f}, gamma_phi={gamma_phi}...", flush=True)
        C, n_iter = solve_ness_lyapunov_iter(L128, alpha, J0, Gamma_L, Gamma_R,
                                              f_L, f_R, gamma_phi)

        mid_i = L128 // 2 - 1
        mid_j = L128 // 2
        C_mid = C[mid_i, mid_j]
        abs_C_mid = abs(C_mid)
        t_elapsed = time.time() - t_start

        print(f"    |C_mid| = {abs_C_mid:.6e}, iterations={n_iter}, time={t_elapsed:.1f}s", flush=True)

        L128_results.append({
            'L': L128,
            'alpha': alpha,
            'gamma_phi': gamma_phi,
            'abs_C_mid': float(abs_C_mid),
            're_C_mid': float(C_mid.real),
            'im_C_mid': float(C_mid.imag),
            'time_s': t_elapsed,
            'n_iterations': n_iter,
        })

    # Now re-fit beta using different L-ranges
    print("\n--- Beta comparison: L-range sensitivity ---")
    print(f"\n{'alpha':>6} {'beta(L<=64)':>14} {'beta(L=32,64,128)':>18} "
          f"{'delta':>10} {'delta_pct':>10} {'beta(L=8..128)':>16} {'beta(L<=128 excl L=4)':>20}")
    print("-" * 90)

    beta_comparison = {}

    for alpha in alphas:
        gamma_phi = 0.5
        key = f"{alpha}_{gamma_phi}"

        # Get L=128 value
        L128_val = None
        for r in L128_results:
            if r['alpha'] == alpha:
                L128_val = r['abs_C_mid']
                break

        # Extract L=4,8,16,32,64 data
        L_vals_dense = []
        C_vals_dense = []
        for d in all_data:
            if abs(d['alpha'] - alpha) < 1e-5 and abs(d['gamma_phi'] - gamma_phi) < 1e-5:
                L_vals_dense.append(d['L'])
                C_vals_dense.append(d['abs_C_mid'])

        # Sort
        pairs = sorted(zip(L_vals_dense, C_vals_dense))
        L_vals_dense = [p[0] for p in pairs]
        C_vals_dense = [p[1] for p in pairs]

        # Fit 1: L <= 64 (original, 5 points)
        L1 = np.array(L_vals_dense)
        C1 = np.array(C_vals_dense)
        logL1 = np.log(L1)
        logC1 = np.log(C1)
        slope1, _, _, _, se1 = scipy.stats.linregress(logL1, logC1)
        beta1 = -slope1

        # Fit 2: L = 32, 64, 128 (exclude small L, 3 points)
        L2 = np.array([32, 64, 128])
        C2_vals = []
        for d in all_data:
            if abs(d['alpha'] - alpha) < 1e-5 and abs(d['gamma_phi'] - gamma_phi) < 1e-5 and d['L'] in [32, 64]:
                C2_vals.append(d['abs_C_mid'])

        C2 = np.append(np.array(C2_vals), L128_val)
        logL2 = np.log(L2)
        logC2 = np.log(C2)
        slope2, _, _, _, se2 = scipy.stats.linregress(logL2, logC2)
        beta2 = -slope2

        # Fit 3: L = 8, 16, 32, 64, 128 (5 points, exclude L=4)
        L3 = np.array([8, 16, 32, 64, 128])
        C3_vals = []
        for d in all_data:
            if abs(d['alpha'] - alpha) < 1e-5 and abs(d['gamma_phi'] - gamma_phi) < 1e-5 and d['L'] in [8, 16, 32, 64]:
                C3_vals.append(d['abs_C_mid'])
        C3 = np.append(np.array(C3_vals), L128_val)
        logL3 = np.log(L3)
        logC3 = np.log(C3)
        slope3, _, _, _, se3 = scipy.stats.linregress(logL3, logC3)
        beta3 = -slope3

        # Fit 4: All 6 points (4,8,16,32,64,128)
        L4 = np.array([4, 8, 16, 32, 64, 128])
        C4_vals = [v for (l, v) in zip(L_vals_dense, C_vals_dense) if l != 128] + [L128_val]
        C4_sorted = []
        for L_target in [4, 8, 16, 32, 64, 128]:
            if L_target == 128:
                C4_sorted.append(L128_val)
            else:
                for d in all_data:
                    if abs(d['alpha'] - alpha) < 1e-5 and abs(d['gamma_phi'] - gamma_phi) < 1e-5 and d['L'] == L_target:
                        C4_sorted.append(d['abs_C_mid'])
                        break
        C4 = np.array(C4_sorted, dtype=float)
        logL4 = np.log(L4)
        logC4 = np.log(C4)
        slope4, _, _, _, se4 = scipy.stats.linregress(logL4, logC4)
        beta4 = -slope4

        delta_beta = beta2 - beta1
        delta_pct = 100 * delta_beta / beta1

        beta_comparison[f"{alpha}_0.5"] = {
            'alpha': alpha,
            'gamma_phi': 0.5,
            'beta_L_le_64': float(beta1),
            'beta_std_L_le_64': float(se1),
            'beta_L_32_64_128': float(beta2),
            'beta_std_L_32_64_128': float(se2),
            'beta_L_8_to_128': float(beta3),
            'beta_std_L_8_to_128': float(se3),
            'beta_L_all_6': float(beta4),
            'beta_std_all_6': float(se4),
            'delta_beta': float(delta_beta),
            'delta_pct': float(delta_pct),
            'L128_abs_C_mid': float(L128_val),
        }

        print(f"{alpha:>6.1f} {beta1:>14.4f} +/- {se1:<7.4f} {beta2:>14.4f} +/- {se2:<7.4f} "
              f"{delta_beta:>10.4f} {delta_pct:>9.2f}% {beta3:>14.4f} +/- {se3:<7.4f} "
              f"{beta4:>14.4f} +/- {se4:<7.4f}")

    # Verdict
    max_delta = max(abs(v['delta_pct']) for v in beta_comparison.values())
    print(f"\n  Maximum beta shift when including L=128: {max_delta:.2f}%")
    if max_delta < 5:
        print("  VERDICT: beta scaling is ROBUST — L=128 confirms the scaling regime")
    else:
        print(f"  WARNING: beta shift of {max_delta:.1f}% detected — scaling regime may need larger L")

    return L128_results, beta_comparison


# ============================================================================
# ATTACK 4 (part 2): Lyapunov vs Dense comparison
# ============================================================================
def compare_lyapunov_vs_dense():
    """
    For L=64, compare solve_continuous_lyapunov (via fixed-point iteration
    using Bartels-Stewart) with the original np.linalg.solve result.
    """
    print("\n" + "=" * 80)
    print("ATTACK 4 (part 2): LYAPUNOV vs DENSE COMPARISON (L=64)")
    print("=" * 80)

    J0 = 0.3
    Gamma_L = 1.0
    Gamma_R = 1.0
    f_L = 0.65
    f_R = 0.35
    L = 64

    alphas = [1.1, 1.5, 1.9]
    gammas = [0.01, 0.5, 1.0]

    results = []
    print(f"\n{'alpha':>6} {'gamma_phi':>10} {'|C_mid_dense|':>14} {'|C_mid_lyap|':>14} "
          f"{'diff':>12} {'rel_diff':>12} {'status':>10}")
    print("-" * 75)

    for alpha in alphas:
        for gp in gammas:
            t_start = time.time()
            C_dense, _ = solve_ness_dense(L, alpha, J0, Gamma_L, Gamma_R, f_L, f_R, gp)
            t_dense = time.time() - t_start

            t_start = time.time()
            C_lyap, n_iter = solve_ness_lyapunov_iter(L, alpha, J0, Gamma_L, Gamma_R,
                                                       f_L, f_R, gp)
            t_lyap = time.time() - t_start

            mid_i = L // 2 - 1
            mid_j = L // 2
            C_mid_dense = abs(C_dense[mid_i, mid_j])
            C_mid_lyap = abs(C_lyap[mid_i, mid_j])

            diff = abs(C_mid_dense - C_mid_lyap)
            rel_diff = diff / (C_mid_dense + 1e-20)

            max_element_diff = np.max(np.abs(C_dense - C_lyap))
            status = "PASS" if max_element_diff < 1e-10 else "FAIL"

            results.append({
                'alpha': alpha,
                'gamma_phi': gp,
                'L': L,
                'C_mid_dense': float(C_mid_dense),
                'C_mid_lyap': float(C_mid_lyap),
                'abs_diff_C_mid': float(diff),
                'rel_diff_C_mid': float(rel_diff),
                'max_element_diff': float(max_element_diff),
                'time_dense_s': t_dense,
                'time_lyap_s': t_lyap,
                'lyap_iterations': n_iter,
                'status': status,
            })

            print(f"{alpha:>6.1f} {gp:>10.3f} {C_mid_dense:>14.6e} {C_mid_lyap:>14.6e} "
                  f"{diff:>12.2e} {rel_diff:>12.2e} {status:>10}")

    return results


# ============================================================================
# MAIN
# ============================================================================
def main():
    print("=" * 80)
    print("PRL NUMERICAL DEFENSE — ALL FOUR ATTACKS")
    print("Dr. B (Numerical Methods Defense Response)")
    print("=" * 80)

    all_results = {}

    # --- Attack 4 Part 1: Condition Numbers ---
    cond_results = compute_condition_numbers()
    all_results['condition_numbers_L64'] = cond_results

    # --- Attack 2: Error Bar Analysis ---
    error_bar_analysis = analyze_error_bars()
    all_results['error_bar_analysis'] = error_bar_analysis

    # --- Attack 4 Part 2: Lyapunov vs Dense ---
    lyap_vs_dense = compare_lyapunov_vs_dense()
    all_results['lyapunov_vs_dense_L64'] = lyap_vs_dense

    # --- Attack 3: Cross-validation ---
    xval_results, xval_pass = cross_validate(L=8)
    all_results['cross_validation'] = {
        'results': xval_results,
        'all_pass': xval_pass,
    }

    # --- Attack 1: L=128 ---
    L128_results, beta_comparison = run_L128_validation()
    all_results['L128_results'] = L128_results
    all_results['beta_comparison'] = beta_comparison

    # --- Save all results ---
    output_path = os.path.join(OUTPUT_DIR, 'defense_all_results.json')
    with open(output_path, 'w') as f:
        json.dump(all_results, f, indent=2)
    print(f"\n{'='*80}")
    print(f"All defense results saved to: {output_path}")
    print(f"{'='*80}")

    # --- Print final summary ---
    print("\n" + "=" * 80)
    print("DEFENSE SUMMARY")
    print("=" * 80)

    # Attack 1 verdict
    max_delta = max(abs(v['delta_pct']) for v in beta_comparison.values())
    print(f"\nAttack 1 (L=128): max beta shift = {max_delta:.2f}% "
          f"({'ROBUST' if max_delta < 5 else 'CONCERN'})")

    # Attack 2 verdict
    max_sigma = error_bar_analysis['firewall_significance']['max_deviation_sigma']
    print(f"Attack 2 (Error bars): Firewall Gamma-dependence = {max_sigma:.1f} sigma "
          f"({'SIGNIFICANT' if max_sigma > 3 else 'MARGINAL' if max_sigma > 2 else 'CONSISTENT'})")

    # Attack 3 verdict
    print(f"Attack 3 (Cross-validation): {'PASSED' if xval_pass else 'FAILED'}")

    # Attack 4 verdict
    unreliable = sum(1 for v in cond_results.values() if v['status'] == 'UNRELIABLE')
    marginal = sum(1 for v in cond_results.values() if v['status'] == 'MARGINAL')
    print(f"Attack 4 (Condition numbers): {unreliable} unreliable, {marginal} marginal out of 25")

    lyap_all_pass = all(r['status'] == 'PASS' for r in lyap_vs_dense)
    print(f"Attack 4 (Lyapunov vs Dense): {'ALL MATCH' if lyap_all_pass else 'DISCREPANCY FOUND'}")

    print("\n" + "=" * 80)
    print("DEFENSE COMPLETE")
    print("=" * 80)


if __name__ == '__main__':
    main()

"""
Phase 2 supplement: L=64 computation
=====================================
Computes the missing L=64 data points for the COH numerical study.
Merges with existing L=4,8,16,32 data (100 points) to produce 125-point dataset.
Re-fits scaling exponents beta(alpha, gamma_phi) with 5 L values each.

Method: identical to phase2_L_large.py — single-particle Lyapunov linear system.
For L=64, A is 4096x4096 complex, solved with np.linalg.solve.
"""

import sys
import io
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import numpy as np
from scipy.linalg import solve_continuous_lyapunov as solve_lyap
import time
import json
import os

# ============================================================
# SECTION 1: System Construction (identical to phase2_L_large.py)
# ============================================================

def construct_h(L, alpha, J0=0.3):
    """Single-particle Hamiltonian with power-law hopping J(r) = J0 / r^alpha."""
    h = np.zeros((L, L), dtype=complex)
    for i in range(L):
        for j in range(i + 1, L):
            r = j - i
            J = J0 / (r ** alpha)
            h[i, j] = J
            h[j, i] = J
    return h


def solve_ness_correlation(L, alpha, J0, Gamma_L, Gamma_R, f_L, f_R, gamma_phi):
    """
    Solve for the NESS correlation matrix C_{ij} = Tr[c_i^† c_j rho_ss].

    Steady-state equation:
    i[h, C] + 1/2 {Gamma_diag, C} + gamma_phi (C - diag(C)) = W_in_diag

    Solved as a linear system A * vec(C) = b.
    """
    h = construct_h(L, alpha, J0)

    # Boundary coupling at each site
    Gamma_tot = np.zeros(L)
    Gamma_tot[0] = Gamma_L
    Gamma_tot[L-1] = Gamma_R

    # Injection rates at each site
    W_in = np.zeros(L)
    W_in[0] = Gamma_L * f_L
    W_in[L-1] = Gamma_R * f_R

    L2 = L * L
    A = np.zeros((L2, L2), dtype=complex)
    b_vec = np.zeros(L2, dtype=complex)

    for i in range(L):
        for j in range(L):
            row = i * L + j

            # Diagonal damping: 1/2 (Gamma_i + Gamma_j) + gamma_phi * (1 - delta_ij)
            A[row, row] = 0.5 * (Gamma_tot[i] + Gamma_tot[j])
            if i != j:
                A[row, row] += gamma_phi

            # Hamiltonian commutator: i[h, C]
            for k in range(L):
                if abs(h[i, k]) > 1e-15:
                    col = k * L + j
                    A[row, col] += 1j * h[i, k]  # i * h_{ik} * C_{kj}

                if abs(h[k, j]) > 1e-15:
                    col = i * L + k
                    A[row, col] -= 1j * h[k, j]  # -i * C_{ik} * h_{kj}

            # Source term (only on diagonal)
            if i == j:
                b_vec[row] = W_in[i]

    # Solve linear system
    C_vec = np.linalg.solve(A, b_vec)
    C = C_vec.reshape(L, L)

    # Enforce exact Hermiticity
    C = 0.5 * (C + C.conj().T)

    return C


# ============================================================
# SECTION 2: L=64 Scan
# ============================================================

def run_L64_scan():
    """Compute L=64 data points for all (alpha, gamma_phi) combinations."""
    J0 = 0.3
    Gamma_L = 1.0
    Gamma_R = 1.0
    f_L = 0.65
    f_R = 0.35

    L = 64
    alpha_values = [1.1, 1.3, 1.5, 1.7, 1.9]
    gamma_phi_values = [0.01, 0.1, 0.5, 1.0, 2.0]

    print("=" * 80)
    print(f"PHASE 2 SUPPLEMENT: L={L} NESS Computation")
    print("=" * 80)
    print(f"Parameters: J0={J0}, Gamma_L={Gamma_L}, Gamma_R={Gamma_R}")
    print(f"             f_L={f_L}, f_R={f_R}")
    print(f"alpha ∈ {alpha_values}")
    print(f"gamma_phi ∈ {gamma_phi_values}")
    print(f"Total: {len(alpha_values)} x {len(gamma_phi_values)} = "
          f"{len(alpha_values)*len(gamma_phi_values)} data points")
    print()

    mid_i = L // 2 - 1  # 0-indexed middle-left
    mid_j = L // 2      # 0-indexed middle-right

    results = []
    n_total = len(alpha_values) * len(gamma_phi_values)
    n_done = 0

    for alpha in alpha_values:
        print(f"  alpha = {alpha:.1f}: ", end='', flush=True)

        for gamma_phi in gamma_phi_values:
            t_start = time.time()

            C = solve_ness_correlation(L, alpha, J0, Gamma_L, Gamma_R,
                                       f_L, f_R, gamma_phi)

            C_mid = C[mid_i, mid_j]
            abs_C_mid = abs(C_mid)
            re_C_mid = C_mid.real
            im_C_mid = C_mid.imag

            # Also extract full C for analysis
            diag_C = np.array([C[i, i].real for i in range(L)])

            t_elapsed = time.time() - t_start

            result = {
                'L': L,
                'alpha': alpha,
                'gamma_phi': gamma_phi,
                'abs_C_mid': float(abs_C_mid),
                're_C_mid': float(re_C_mid),
                'im_C_mid': float(im_C_mid),
                'diag_C': diag_C.tolist(),
                'time_s': t_elapsed,
            }
            results.append(result)

            n_done += 1
            print(f'{gamma_phi:.2f}:|C|={abs_C_mid:.6f} ', end='', flush=True)

        print(f' [{n_done}/{n_total}]', flush=True)

    return results


# ============================================================
# SECTION 3: Scaling Analysis (with 5 L values)
# ============================================================

def fit_scaling(all_results):
    """
    Fit |C_mid|(L) ~ A * L^{-beta} for each (alpha, gamma_phi) pair.

    Log-linear regression: log|C_mid| = log(A) - beta * log(L)
    """
    import scipy.stats

    print("\n" + "=" * 80)
    print("SCALING ANALYSIS: |C_mid|(L) ~ A * L^{-beta}")
    print("=" * 80)

    # Organize data
    data_by_params = {}
    for r in all_results:
        key = (r['alpha'], r['gamma_phi'])
        if key not in data_by_params:
            data_by_params[key] = {'L': [], 'abs_C': []}
        data_by_params[key]['L'].append(r['L'])
        data_by_params[key]['abs_C'].append(r['abs_C_mid'])

    # Sort by alpha, then gamma_phi
    alphas = sorted(set(r['alpha'] for r in all_results))
    gammas = sorted(set(r['gamma_phi'] for r in all_results))

    print(f"\n{'alpha':>6} {'gamma_phi':>10} {'A':>12} {'beta':>10} {'R^2':>10} {'|C|(L=64)':>12}")
    print("-" * 70)

    fit_results = {}
    for alpha in alphas:
        for gp in gammas:
            key = (alpha, gp)
            d = data_by_params[key]
            L_arr = np.array(d['L'])
            C_arr = np.array(d['abs_C'])

            # Filter out zero or negative values
            mask = C_arr > 1e-15
            if np.sum(mask) < 3:
                continue

            log_L = np.log(L_arr[mask])
            log_C = np.log(C_arr[mask])

            slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(log_L, log_C)
            beta = -slope
            A_fit = np.exp(intercept)
            r_sq = r_value ** 2

            fit_results[key] = {
                'A': A_fit,
                'beta': beta,
                'R2': r_sq,
                'std_err': std_err,
                'p_value': p_value,
            }

            print(f"{alpha:>6.1f} {gp:>10.3f} {A_fit:>12.6f} {beta:>10.4f} {r_sq:>10.4f} {C_arr[-1]:>12.6e}")

    return fit_results, data_by_params


# ============================================================
# SECTION 4: C12 Pure Imaginarity Check
# ============================================================

def check_purity(results):
    """
    Check if C_mid remains pure imaginary for all L, alpha, gamma_phi.
    """
    print("\n" + "=" * 80)
    print("C12 PURE IMAGINARITY CHECK (FULL 125-point dataset)")
    print("=" * 80)

    min_purity = 1.0
    all_pure = True
    impurity_threshold = 1e-12

    for r in results:
        re_im_ratio = abs(r['re_C_mid']) / (abs(r['im_C_mid']) + 1e-20)
        purity = abs(r['im_C_mid']) / (abs(r['re_C_mid']) + abs(r['im_C_mid']) + 1e-20)
        min_purity = min(min_purity, purity)

        if re_im_ratio > impurity_threshold:
            all_pure = False
            print(f"  IMPURE: L={r['L']} alpha={r['alpha']} gp={r['gamma_phi']} "
                  f"Re/Im={re_im_ratio:.2e}")

    if all_pure:
        print("  ALL 125 DATA POINTS: C_mid is pure imaginary to machine precision")
    else:
        print(f"  WARNING: Some data points have non-zero real part")
    print(f"  Minimum purity: {min_purity:.15f}")

    return all_pure


# ============================================================
# SECTION 5: Main
# ============================================================

if __name__ == '__main__':
    output_dir = os.path.dirname(os.path.abspath(__file__))

    # --- Step 1: Compute L=64 data ---
    print("STEP 1: Computing L=64 data points...")
    L64_results = run_L64_scan()

    # --- Step 2: Load existing L=4,8,16,32 data ---
    print("\nSTEP 2: Loading existing L=4,8,16,32 data...")
    existing_path = os.path.join(output_dir, 'phase2_raw_results.json')
    with open(existing_path, 'r') as f:
        existing_results = json.load(f)
    print(f"  Loaded {len(existing_results)} existing data points")

    # --- Step 3: Merge ---
    print("\nSTEP 3: Merging datasets...")
    all_results = existing_results + L64_results
    print(f"  Total: {len(all_results)} data points")
    print(f"  L values: {sorted(set(r['L'] for r in all_results))}")

    # --- Step 4: Save FULL raw results ---
    print("\nSTEP 4: Saving full 125-point dataset...")
    full_json_path = os.path.join(output_dir, 'phase2_raw_results_FULL.json')
    serializable = []
    for r in all_results:
        serializable.append({
            'L': int(r['L']),
            'alpha': float(r['alpha']),
            'gamma_phi': float(r['gamma_phi']),
            'abs_C_mid': float(r['abs_C_mid']),
            're_C_mid': float(r['re_C_mid']),
            'im_C_mid': float(r['im_C_mid']),
            'diag_C': [float(x) for x in r['diag_C']],
            'time_s': float(r['time_s']),
        })
    with open(full_json_path, 'w') as f:
        json.dump(serializable, f, indent=2)
    print(f"  Saved to: {full_json_path}")

    # --- Step 5: Re-fit with 5 L values ---
    print("\nSTEP 5: Re-fitting scaling exponents with 5 L values each...")
    fit_results, data_by_params = fit_scaling(all_results)

    # --- Step 6: Save FULL fit results ---
    print("\nSTEP 6: Saving full fit results...")
    fit_json_path = os.path.join(output_dir, 'phase2_fit_results_FULL.json')
    fit_serializable = {}
    for key, val in fit_results.items():
        alpha, gp = key
        fit_serializable[f"{alpha}_{gp}"] = {
            'alpha': float(alpha),
            'gamma_phi': float(gp),
            'A': float(val['A']),
            'beta': float(val['beta']),
            'R2': float(val['R2']),
            'std_err': float(val['std_err']),
        }
    with open(fit_json_path, 'w') as f:
        json.dump(fit_serializable, f, indent=2)
    print(f"  Saved to: {fit_json_path}")

    # --- Step 7: Check purity ---
    print("\nSTEP 7: Checking purity...")
    all_pure = check_purity(all_results)

    # --- Step 8: Summary table ---
    print("\n" + "=" * 80)
    print("FULL BETA TABLE (from 5 L values: 4,8,16,32,64)")
    print("=" * 80)

    alphas = sorted(set(r['alpha'] for r in all_results))
    gammas = sorted(set(r['gamma_phi'] for r in all_results))

    header = f"{'alpha':>8}"
    for gp in gammas:
        header += f" {'gp=' + str(gp):>10}"
    print(header)
    print("-" * (8 + 10 * len(gammas)))

    for alpha in alphas:
        line = f"{alpha:>8.1f}"
        for gp in gammas:
            key = (alpha, gp)
            if key in fit_results:
                line += f" {fit_results[key]['beta']:>10.4f}"
            else:
                line += f" {'N/A':>10}"
        print(line)

    # --- Step 9: Beta change report (100-point vs 125-point) ---
    print("\n" + "=" * 80)
    print("BETA CHANGE: 100-point (4L) vs 125-point (5L) fits")
    print("=" * 80)

    # Load old fit results for comparison
    old_fit_path = os.path.join(output_dir, 'phase2_fit_results.json')
    with open(old_fit_path, 'r') as f:
        old_fit = json.load(f)

    print(f"\n{'alpha':>6} {'gp':>8} {'beta(old)':>10} {'beta(new)':>10} {'delta':>10} {'change':>10}")
    print("-" * 60)
    max_change = 0.0
    for alpha in alphas:
        for gp in gammas:
            key_str = f"{alpha}_{gp}"
            old_beta = old_fit[key_str]['beta']
            new_beta = fit_results[(alpha, gp)]['beta']
            delta = new_beta - old_beta
            pct = 100 * delta / old_beta if old_beta != 0 else 0
            max_change = max(max_change, abs(pct))
            marker = " ***" if abs(pct) > 5 else ""
            print(f"{alpha:>6.1f} {gp:>8.3f} {old_beta:>10.4f} {new_beta:>10.4f} "
                  f"{delta:>10.4f} {pct:>+9.1f}%{marker}")

    print(f"\n  Maximum absolute percentage change: {max_change:.1f}%")
    if max_change > 5:
        print("  WARNING: Significant beta changes detected! Report must be updated.")
    else:
        print("  INFO: Beta values stable within ~5%. Report table needs minor updates.")

    print("\n" + "=" * 80)
    print("PHASE 2 L=64 SUPPLEMENT COMPLETE")
    print("=" * 80)

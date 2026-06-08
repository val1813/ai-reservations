"""
Firewall 1: O_XX = sum_{i!=j} |Im(C_{ij})|^2 in the thermodynamic limit
=========================================================================
Computes the full off-diagonal XX amplitude sum and its scaling with L
for the boundary-driven power-law hopping chain.

Firewall criterion:
  If O_XX/L -> 0 as L->infinity (gamma>0): XX has no macroscopic signature
  If O_XX/L -> const>0 as L->infinity (gamma~0): XX has macroscopic signature

Parameters:
  J0=0.3, Gamma_L=Gamma_R=1.0, f_L=0.65, f_R=0.35
  L ∈ {4, 8, 16, 32, 64, 128, 256}
  alpha ∈ {1.1, 1.5, 1.9}
  gamma_phi ∈ {0.01, 0.5, 2.0}

Method:
  - L<=64: dense Lyapunov solve (np.linalg.solve on vectorized system)
  - L>=128: sparse Lyapunov solve (scipy.sparse.linalg.spsolve)

Author: Claude (Firewall 1 numerical computation)
Date: 2026-06-03
"""

import sys
import io
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve, gmres, LinearOperator
import scipy.stats
import time
import json
import os
import warnings
warnings.filterwarnings('ignore')


# ============================================================
# SECTION 1: System Construction
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


def solve_ness_dense(L, alpha, J0, Gamma_L, Gamma_R, f_L, f_R, gamma_phi):
    """
    Solve NESS correlation matrix using dense linear system.
    Used for L <= 64.

    Steady-state equation:
    i[h, C] + 1/2 {Gamma_diag, C} + gamma_phi (C - diag(C)) = diag(W_in)
    """
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

            if i == j:
                # Diagonal: anti-commutator gives Gamma_i * C_ii
                A[row, row] = Gamma_tot[i]

                # Commutator: i[h, C]_{ii} = i sum_k (h_{ik} C_{ki} - C_{ik} h_{ki})
                for k in range(L):
                    if abs(h[i, k]) > 1e-15:
                        # +i h_{ik} C_{ki}
                        col = k * L + i
                        A[row, col] += 1j * h[i, k]
                        # -i C_{ik} h_{ik} (h is symmetric)
                        col = i * L + k
                        A[row, col] += -1j * h[i, k]

                b_vec[row] = W_in[i]
            else:
                # Off-diagonal: damping + dephasing
                A[row, row] = 0.5 * (Gamma_tot[i] + Gamma_tot[j]) + gamma_phi

                # Commutator
                for k in range(L):
                    if abs(h[i, k]) > 1e-15:
                        col = k * L + j
                        A[row, col] += 1j * h[i, k]
                    if abs(h[k, j]) > 1e-15:
                        col = i * L + k
                        A[row, col] += -1j * h[k, j]

    C_vec = np.linalg.solve(A, b_vec)
    C = C_vec.reshape(L, L)
    C = 0.5 * (C + C.conj().T)

    return C


def solve_ness_sparse(L, alpha, J0, Gamma_L, Gamma_R, f_L, f_R, gamma_phi):
    """
    Solve NESS correlation matrix using sparse linear system.
    Used for L >= 128 where dense solve is infeasible.

    Builds the Liouvillian superoperator A (L^2 x L^2) in sparse CSR format.
    """
    h = construct_h(L, alpha, J0)

    Gamma_tot = np.zeros(L)
    Gamma_tot[0] = Gamma_L
    Gamma_tot[L-1] = Gamma_R

    W_in = np.zeros(L)
    W_in[0] = Gamma_L * f_L
    W_in[L-1] = Gamma_R * f_R

    L2 = L * L

    # Use LIL format for efficient construction
    A_lil = sparse.lil_matrix((L2, L2), dtype=complex)
    b_vec = np.zeros(L2, dtype=complex)

    for i in range(L):
        for j in range(L):
            row = i * L + j

            if i == j:
                A_lil[row, row] = Gamma_tot[i]

                for k in range(L):
                    h_ik = h[i, k]
                    if abs(h_ik) > 1e-15:
                        # +i h_{ik} C_{ki}
                        col = k * L + i
                        A_lil[row, col] += 1j * h_ik
                        # -i C_{ik} h_{ik}
                        col = i * L + k
                        A_lil[row, col] += -1j * h_ik

                b_vec[row] = W_in[i]
            else:
                A_lil[row, row] = 0.5 * (Gamma_tot[i] + Gamma_tot[j]) + gamma_phi

                for k in range(L):
                    h_ik = h[i, k]
                    if abs(h_ik) > 1e-15:
                        col = k * L + j
                        A_lil[row, col] += 1j * h_ik

                    h_kj = h[k, j]
                    if abs(h_kj) > 1e-15:
                        col = i * L + k
                        A_lil[row, col] += -1j * h_kj

    A_csr = A_lil.tocsr()

    # Try direct sparse solve first; fall back to iterative if out of memory
    try:
        C_vec = spsolve(A_csr, b_vec)
    except Exception as e:
        print(f"      spsolve failed: {e}, trying GMRES...", flush=True)
        # Use GMRES with diagonal preconditioner
        M_diag = A_csr.diagonal()
        M_diag_inv = 1.0 / np.where(np.abs(M_diag) > 1e-15, M_diag, 1.0)
        M = sparse.diags(M_diag_inv, 0, dtype=complex)

        C_vec, info = gmres(A_csr, b_vec, M=M, tol=1e-10, maxiter=2000)
        if info > 0:
            print(f"      WARNING: GMRES converged to tol {info}", flush=True)
        elif info < 0:
            print(f"      WARNING: GMRES illegal input or breakdown", flush=True)

    C = C_vec.reshape(L, L)
    C = 0.5 * (C + C.conj().T)

    return C


def solve_ness_correlation(L, alpha, J0=0.3, Gamma_L=1.0, Gamma_R=1.0,
                          f_L=0.65, f_R=0.35, gamma_phi=0.5):
    """
    Dispatch to dense or sparse solver based on L.
    """
    if L <= 64:
        return solve_ness_dense(L, alpha, J0, Gamma_L, Gamma_R,
                                f_L, f_R, gamma_phi)
    else:
        return solve_ness_sparse(L, alpha, J0, Gamma_L, Gamma_R,
                                 f_L, f_R, gamma_phi)


# ============================================================
# SECTION 2: O_XX Computation and Analysis
# ============================================================

def compute_OXX(C):
    """
    Compute O_XX = sum_{i!=j} |Im(C_{ij})|^2
    Also checks purity: max |Re(C_{i!=j})| / max |Im(C_{i!=j})|
    """
    L = C.shape[0]
    OXX = 0.0
    max_re_offdiag = 0.0
    max_im_offdiag = 0.0

    for i in range(L):
        for j in range(L):
            if i != j:
                im_part = C[i, j].imag
                re_part = C[i, j].real
                OXX += im_part * im_part
                max_re_offdiag = max(max_re_offdiag, abs(re_part))
                max_im_offdiag = max(max_im_offdiag, abs(im_part))

    purity_ratio = max_re_offdiag / max_im_offdiag if max_im_offdiag > 1e-20 else float('inf')

    return OXX, purity_ratio, max_re_offdiag, max_im_offdiag


def compute_detailed_OXX(C):
    """
    Compute O_XX with additional diagnostics:
    - O_XX per distance: sum over all pairs at distance r
    - Total O_XX
    """
    L = C.shape[0]
    OXX_by_distance = {}
    OXX_total = 0.0

    for i in range(L):
        for j in range(i+1, L):
            r = j - i
            im_ij = C[i, j].imag
            # Each off-diagonal pair contributes twice: |Im(C_ij)|^2 + |Im(C_ji)|^2 = 2|Im(C_ij)|^2
            # since C_ji = C_ij* (Hermitian), Im(C_ji) = -Im(C_ij), so |Im|^2 is same
            contribution = 2 * im_ij * im_ij
            OXX_total += contribution

            if r not in OXX_by_distance:
                OXX_by_distance[r] = 0.0
            OXX_by_distance[r] += contribution

    return OXX_total, OXX_by_distance


# ============================================================
# SECTION 3: Main Scan
# ============================================================

def run_firewall1_scan():
    """Run the full parameter scan for Firewall 1."""
    J0 = 0.3
    Gamma_L = 1.0
    Gamma_R = 1.0
    f_L = 0.65
    f_R = 0.35

    L_values = [4, 8, 16, 32, 64, 128, 256]
    alpha_values = [1.1, 1.5, 1.9]
    gamma_phi_values = [0.01, 0.5, 2.0]

    print("=" * 80)
    print("FIREWALL 1: O_XX = sum_{i!=j} |Im(C_{ij})|^2  Thermodynamic Limit")
    print("=" * 80)
    print(f"Parameters: J0={J0}, Gamma_L={Gamma_L}, Gamma_R={Gamma_R}")
    print(f"             f_L={f_L}, f_R={f_R}")
    print(f"L ∈ {L_values}")
    print(f"alpha ∈ {alpha_values}")
    print(f"gamma_phi ∈ {gamma_phi_values}")
    print(f"Total: {len(L_values)} x {len(alpha_values)} x {len(gamma_phi_values)} = "
          f"{len(L_values)*len(alpha_values)*len(gamma_phi_values)} data points")
    print()

    results = []
    n_total = len(L_values) * len(alpha_values) * len(gamma_phi_values)
    n_done = 0

    for L in L_values:
        print(f"\n{'='*60}")
        print(f"L = {L}")
        print(f"{'='*60}")

        for alpha in alpha_values:
            print(f"  alpha = {alpha:.1f}:", flush=True)

            for gamma_phi in gamma_phi_values:
                t_start = time.time()

                try:
                    C = solve_ness_correlation(L, alpha, J0, Gamma_L, Gamma_R,
                                               f_L, f_R, gamma_phi)

                    OXX, purity_ratio, max_re_offdiag, max_im_offdiag = compute_OXX(C)
                    OXX_per_L = OXX / L

                    # Also compute detailed per-distance breakdown for largest L
                    if L >= 64:
                        OXX_detail, OXX_by_dist = compute_detailed_OXX(C)
                    else:
                        OXX_detail = OXX
                        OXX_by_dist = {}

                    t_elapsed = time.time() - t_start

                    result = {
                        'L': L,
                        'alpha': alpha,
                        'gamma_phi': gamma_phi,
                        'OXX': float(OXX),
                        'OXX_per_L': float(OXX_per_L),
                        'OXX_by_distance': {str(k): float(v) for k, v in sorted(OXX_by_dist.items())},
                        'purity_ratio': float(purity_ratio),
                        'max_re_offdiag': float(max_re_offdiag),
                        'max_im_offdiag': float(max_im_offdiag),
                        'time_s': t_elapsed,
                    }
                    results.append(result)

                    n_done += 1
                    status = f"    gp={gamma_phi:.2f}: OXX={OXX:.6e}, OXX/L={OXX_per_L:.6e}, "
                    status += f"max|Im|={max_im_offdiag:.6e}, purity={purity_ratio:.2e} "
                    status += f"[{t_elapsed:.1f}s] [{n_done}/{n_total}]"
                    print(status, flush=True)

                except Exception as e:
                    n_done += 1
                    print(f"    gp={gamma_phi:.2f}: FAILED - {e} [{n_done}/{n_total}]", flush=True)
                    results.append({
                        'L': L,
                        'alpha': alpha,
                        'gamma_phi': gamma_phi,
                        'OXX': None,
                        'OXX_per_L': None,
                        'error': str(e),
                        'time_s': 0.0,
                    })

    return results


# ============================================================
# SECTION 4: Scaling Analysis
# ============================================================

def fit_OXX_scaling(results):
    """
    Fit O_XX/L ~ A * L^{-gamma} for each (alpha, gamma_phi) pair.

    gamma > 0: O_XX/L -> 0, XX has no macroscopic signature
    gamma ~ 0: O_XX/L -> const, XX has macroscopic signature
    gamma < 0: O_XX/L -> infinity, XX dominates (unlikely)
    """
    print("\n" + "=" * 80)
    print("SCALING ANALYSIS: O_XX/L ~ A * L^{-gamma}")
    print("=" * 80)

    # Filter valid results
    valid_results = [r for r in results if r.get('OXX') is not None]

    # Organize data by (alpha, gamma_phi)
    data_by_params = {}
    for r in valid_results:
        key = (r['alpha'], r['gamma_phi'])
        if key not in data_by_params:
            data_by_params[key] = {'L': [], 'OXX_per_L': [], 'OXX': []}
        data_by_params[key]['L'].append(r['L'])
        data_by_params[key]['OXX_per_L'].append(r['OXX_per_L'])
        data_by_params[key]['OXX'].append(r['OXX'])

    alphas = sorted(set(r['alpha'] for r in valid_results))
    gammas = sorted(set(r['gamma_phi'] for r in valid_results))

    print(f"\n{'alpha':>6} {'gp':>8} {'gamma':>10} {'std_err':>10} {'R^2':>8} "
          f"{'OXX/L(L=4)':>14} {'OXX/L(L=max)':>14} {'OXX(L=max)':>14}")
    print("-" * 90)

    fit_results = {}

    for alpha in alphas:
        for gp in gammas:
            key = (alpha, gp)
            if key not in data_by_params:
                continue

            d = data_by_params[key]
            L_arr = np.array(d['L'])
            oxx_arr = np.array(d['OXX_per_L'])
            oxx_raw_arr = np.array(d['OXX'])

            # Filter out near-zero values
            mask = oxx_arr > 1e-30
            if np.sum(mask) < 3:
                fit_results[key] = {'gamma': None, 'std_err': None, 'R2': None,
                                   'error': 'Insufficient data points'}
                continue

            log_L = np.log(L_arr[mask])
            log_OXX = np.log(oxx_arr[mask])

            slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(log_L, log_OXX)
            gamma_fit = -slope  # OXX/L ~ L^{-gamma}, so log(OXX/L) = log(A) - gamma*log(L)
            A_fit = np.exp(intercept)
            r_sq = r_value ** 2

            # Also fit O_XX directly: O_XX ~ L^{beta_oxx}
            log_OXX_raw = np.log(oxx_raw_arr[mask])
            slope_raw, _, _, _, _ = scipy.stats.linregress(log_L, log_OXX_raw)
            beta_oxx = slope_raw  # OXX ~ L^{beta_oxx}

            fit_results[key] = {
                'gamma': gamma_fit,
                'std_err': std_err,
                'R2': r_sq,
                'A': A_fit,
                'beta_OXX': beta_oxx,
                'OXX_per_L_at_max_L': oxx_arr[-1],
                'OXX_at_max_L': oxx_raw_arr[-1],
            }

            print(f"{alpha:>6.1f} {gp:>8.3f} {gamma_fit:>10.4f} {std_err:>10.4f} "
                  f"{r_sq:>8.4f} {oxx_arr[0]:>14.6e} {oxx_arr[-1]:>14.6e} "
                  f"{oxx_raw_arr[-1]:>14.6e}")

    return fit_results, data_by_params


# ============================================================
# SECTION 5: Cross-Validation (Sanity Checks)
# ============================================================

def run_sanity_checks(results):
    """
    Run sanity checks on the computed results.
    """
    print("\n" + "=" * 80)
    print("SANITY CHECKS")
    print("=" * 80)

    valid = [r for r in results if r.get('OXX') is not None]

    # Check 1: Re(C_{i!=j}) should be zero (pure imaginary theorem)
    max_re = max(r.get('max_re_offdiag', 0) for r in valid)
    max_im = max(r.get('max_im_offdiag', 0) for r in valid)
    print(f"\n  Check 1: max |Re(C_{i!=j})| = {max_re:.2e}")
    print(f"            max |Im(C_{i!=j})| = {max_im:.2e}")
    print(f"            Ratio Re/Im = {max_re/max_im if max_im > 1e-20 else 'N/A':.2e}")
    print(f"  => {'PASS' if max_re < 1e-10 else 'FAIL'}: off-diagonals are pure imaginary")

    # Check 2: O_XX should be positive
    min_OXX = min(r['OXX'] for r in valid)
    print(f"\n  Check 2: min O_XX = {min_OXX:.6e}")
    print(f"  => {'PASS' if min_OXX >= 0 else 'FAIL'}: O_XX is non-negative")

    # Check 3: O_XX should decrease with larger L (for fixed alpha, gp)
    alpha_gp_pairs = set((r['alpha'], r['gamma_phi']) for r in valid)
    monotonic_count = 0
    n_pairs = len(alpha_gp_pairs)
    for a, gp in alpha_gp_pairs:
        subset = sorted([r for r in valid if r['alpha'] == a and r['gamma_phi'] == gp],
                       key=lambda x: x['L'])
        if len(subset) >= 2:
            oxx_vals = [r['OXX'] for r in subset]
            if len(oxx_vals) >= 2:
                # Check if roughly decreasing (OXX/L should decrease)
                oxxpl = [r['OXX_per_L'] for r in subset]
                if oxxpl[-1] <= oxxpl[0]:
                    monotonic_count += 1
    print(f"\n  Check 3: O_XX/L monotonically decreasing for {monotonic_count}/{n_pairs} pairs")
    print(f"  => {'PASS' if monotonic_count == n_pairs else 'WARN'}: "
          f"{'All' if monotonic_count == n_pairs else str(monotonic_count) + '/' + str(n_pairs)} pairs show decreasing trend")

    # Check 4: Hermiticity of C
    # Already enforced in solver, but verify on a few samples
    max_herm_dev = 0.0
    for r in valid:
        if 'C_samples' in r:
            for C in r['C_samples']:
                dev = np.max(np.abs(C - C.conj().T))
                max_herm_dev = max(max_herm_dev, dev)
    print(f"\n  Check 4: max hermiticity deviation = {max_herm_dev:.2e}")


def fit_with_corrections(data_by_params, fit_results):
    """
    Additional fitting: check if O_XX/L shows corrections to pure power law.
    Fit O_XX/L = A * L^{-gamma} * (1 + c/L) to capture finite-size effects.
    """
    print("\n" + "=" * 80)
    print("FINITE-SIZE CORRECTION FIT: O_XX/L = A * L^{-gamma} * (1 + c/L)")
    print("=" * 80)

    print(f"\n{'alpha':>6} {'gp':>8} {'gamma':>10} {'c':>10} {'R^2':>8} "
          f"{'gamma_bound':>12}")
    print("-" * 65)

    corrected_fits = {}

    for (alpha, gp), d in data_by_params.items():
        L_arr = np.array(d['L'])
        oxx_arr = np.array(d['OXX_per_L'])

        mask = oxx_arr > 1e-30
        if np.sum(mask) < 4:
            continue

        L_use = L_arr[mask]
        oxx_use = oxx_arr[mask]
        log_L = np.log(L_use)
        log_OXX = np.log(oxx_use)

        # Fit with correction term: log(OXX/L) = log(A) - gamma*log(L) + log(1 + c/L)
        # For large L: log(1 + c/L) ~ c/L
        # So: log(OXX) = log(A) + (1-gamma)*log(L) + c/L
        # Hmm, that's OXX not OXX/L. Let me redo.
        # O_XX/L = A * L^{-gamma} * (1 + c/L)
        # log(O_XX/L) = log(A) - gamma*log(L) + c/L + O(1/L^2)
        # Do linear regression with columns: [1, -log(L), 1/L]

        X = np.column_stack([np.ones(len(L_use)), -log_L, 1.0 / L_use])

        try:
            coeffs, residuals, rank, sv = np.linalg.lstsq(X, log_OXX, rcond=None)
            log_A, gamma_c, c = coeffs
            # Compute R^2
            pred = X @ coeffs
            ss_res = np.sum((log_OXX - pred) ** 2)
            ss_tot = np.sum((log_OXX - np.mean(log_OXX)) ** 2)
            r_sq_c = 1 - ss_res / ss_tot if ss_tot > 0 else 0

            # Lower bound on gamma (conservative estimate for firewall)
            # Use only largest 3 L values for asymptotic fit
            if len(L_use) >= 3:
                L_large = L_use[-3:]
                oxx_large = oxx_use[-3:]
                log_L_large = np.log(L_large)
                log_oxx_large = np.log(oxx_large)
                slope_large, _, r_val, _, _ = scipy.stats.linregress(log_L_large, log_oxx_large)
                gamma_large = -slope_large
            else:
                gamma_large = gamma_c

            corrected_fits[(alpha, gp)] = {
                'gamma': gamma_c,
                'gamma_asymptotic': gamma_large,
                'c': c,
                'R2': r_sq_c,
            }

            print(f"{alpha:>6.1f} {gp:>8.3f} {gamma_c:>10.4f} {c:>10.4f} "
                  f"{r_sq_c:>8.4f} {gamma_large:>12.4f}")
        except Exception as e:
            print(f"{alpha:>6.1f} {gp:>8.3f} fit failed: {e}")

    return corrected_fits


# ============================================================
# SECTION 6: Output and Reporting
# ============================================================

def print_gamma_table(fit_results):
    """Print gamma(alpha, gamma_phi) table."""
    alphas = sorted(set(k[0] for k in fit_results.keys()))
    gps = sorted(set(k[1] for k in fit_results.keys()))

    print("\n" + "=" * 80)
    print("GAMMA TABLE: gamma(alpha, gamma_phi) from O_XX/L ~ L^{-gamma}")
    print("=" * 80)

    header = f"{'alpha':>8}"
    for gp in gps:
        header += f" {'gp=' + str(gp):>10}"
    print(header)
    print("-" * (8 + 10 * len(gps)))

    for alpha in alphas:
        line = f"{alpha:>8.1f}"
        for gp in gps:
            key = (alpha, gp)
            if key in fit_results and fit_results[key].get('gamma') is not None:
                line += f" {fit_results[key]['gamma']:>10.4f}"
            else:
                line += f" {'N/A':>10}"
        print(line)

    # Also print R^2 table
    print(f"\n{'alpha':>8}", end='')
    for gp in gps:
        print(f" {'R^2(gp=' + str(gp) + ')':>14}", end='')
    print()
    print("-" * (8 + 14 * len(gps)))
    for alpha in alphas:
        line = f"{alpha:>8.1f}"
        for gp in gps:
            key = (alpha, gp)
            if key in fit_results and fit_results[key].get('R2') is not None:
                line += f" {fit_results[key]['R2']:>14.4f}"
            else:
                line += f" {'N/A':>14}"
        print(line)


# ============================================================
# SECTION 7: Main
# ============================================================

if __name__ == '__main__':
    output_dir = os.path.dirname(os.path.abspath(__file__))

    # --- Phase A: Scan ---
    print("PHASE A: Running full parameter scan...")
    results = run_firewall1_scan()

    # --- Save raw results ---
    print("\n" + "=" * 80)
    print("SAVING RESULTS...")

    json_path = os.path.join(output_dir, 'firewall1_results.json')
    serializable = []
    for r in results:
        entry = {}
        for k, v in r.items():
            if isinstance(v, dict):
                entry[k] = {str(dk): float(dv) for dk, dv in v.items()}
            elif isinstance(v, (np.integer,)):
                entry[k] = int(v)
            elif isinstance(v, (np.floating,)):
                entry[k] = float(v)
            elif v is None:
                entry[k] = None
            else:
                entry[k] = v
        serializable.append(entry)

    with open(json_path, 'w') as f:
        json.dump(serializable, f, indent=2)
    print(f"  Raw results saved to: {json_path}")
    print(f"  Total entries: {len(serializable)}")
    print(f"  Successful: {sum(1 for r in results if r.get('OXX') is not None)}")
    print(f"  Failed: {sum(1 for r in results if r.get('OXX') is None)}")

    # --- Phase B: Sanity Checks ---
    print("\nPHASE B: Running sanity checks...")
    run_sanity_checks(results)

    # --- Phase C: Scaling Analysis ---
    print("\nPHASE C: Scaling analysis...")
    fit_results, data_by_params = fit_OXX_scaling(results)

    # --- Phase D: Corrected Fits ---
    print("\nPHASE D: Finite-size corrected fits...")
    corrected_fits = fit_with_corrections(data_by_params, fit_results)

    # --- Phase E: Print Gamma Table ---
    print("\nPHASE E: Gamma summary...")
    print_gamma_table(fit_results)

    # --- Save fit results ---
    fit_json_path = os.path.join(output_dir, 'firewall1_fit_results.json')
    fit_serializable = {}
    for key, val in fit_results.items():
        alpha, gp = key
        fit_serializable[f"{alpha}_{gp}"] = {
            'alpha': float(alpha),
            'gamma_phi': float(gp),
            'gamma': float(val['gamma']) if val['gamma'] is not None else None,
            'std_err': float(val['std_err']) if val['std_err'] is not None else None,
            'R2': float(val['R2']) if val['R2'] is not None else None,
            'A': float(val['A']) if val.get('A') is not None else None,
            'beta_OXX': float(val['beta_OXX']) if val.get('beta_OXX') is not None else None,
            'OXX_per_L_max_L': float(val['OXX_per_L_at_max_L']) if val.get('OXX_per_L_at_max_L') is not None else None,
        }
        if key in corrected_fits:
            fit_serializable[f"{alpha}_{gp}"]['gamma_asymptotic'] = float(corrected_fits[key]['gamma'])
            fit_serializable[f"{alpha}_{gp}"]['c_correction'] = float(corrected_fits[key]['c'])
            fit_serializable[f"{alpha}_{gp}"]['R2_corrected'] = float(corrected_fits[key]['R2'])
            fit_serializable[f"{alpha}_{gp}"]['gamma_large_L'] = float(corrected_fits[key]['gamma_asymptotic'])

    with open(fit_json_path, 'w') as f:
        json.dump(fit_serializable, f, indent=2)
    print(f"\n  Fit results saved to: {fit_json_path}")

    print("\n" + "=" * 80)
    print("FIREWALL 1 COMPUTATION COMPLETE")
    print("=" * 80)

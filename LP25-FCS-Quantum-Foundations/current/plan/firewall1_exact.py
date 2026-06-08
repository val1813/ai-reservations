"""
Firewall 1: Exact Analytic Reduction
=====================================
Key insight: For the boundary-driven free fermion chain with dephasing,
the NESS correlation matrix C has the structure:
  C_{ii} = D_i (real, given by LxL linear system)
  C_{ij} = i * h_{ij} (D_i - D_j) / ((Gamma_i+Gamma_j)/2 + gamma_phi)  for i!=j

Derivation:
1. The steady-state equation: i[h,C] + 1/2{Gamma,C} + gamma_phi(C - diag(C)) = diag(W_in)
2. Assume C_{ij} = i * C_im_{ij} (pure imaginary off-diagonal)
3. Imaginary part of off-diagonal equation gives:
   C_im_{ij} = h_{ij} (D_i - D_j) / ((Gamma_i+Gamma_j)/2 + gamma_phi)
4. Diagonal equation reduces to LxL linear system for D_i:
   2 * sum_{k!=i} h_{ik}^2 (D_i - D_k) / ((Gamma_i+Gamma_k)/2 + gamma_phi) + Gamma_i D_i = W_in_i

This is O(L^3) instead of O(L^6), enabling L up to thousands.
"""

import sys
import io
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import numpy as np
import scipy.stats
import time
import json
import os


def construct_h(L, alpha, J0=0.3):
    """Single-particle Hamiltonian with power-law hopping."""
    h = np.zeros((L, L), dtype=float)
    for i in range(L):
        for j in range(i + 1, L):
            r = j - i
            J = J0 / (r ** alpha)
            h[i, j] = J
            h[j, i] = J
    return h


def solve_ness_exact(L, alpha, J0=0.3, Gamma_L=1.0, Gamma_R=1.0,
                     f_L=0.65, f_R=0.35, gamma_phi=0.5):
    """
    Solve NESS correlation matrix using exact analytic reduction.

    Returns:
      C: LxL complex correlation matrix
      D: L vector of diagonal occupations
      C_im: LxL real anti-symmetric matrix where C_{ij} = i * C_im_{ij} (i!=j)
    """
    h = construct_h(L, alpha, J0)

    # Boundary coupling
    Gamma = np.zeros(L)
    Gamma[0] = Gamma_L
    Gamma[L-1] = Gamma_R

    W_in = np.zeros(L)
    W_in[0] = Gamma_L * f_L
    W_in[L-1] = Gamma_R * f_R

    # Build LxL linear system for diagonal occupations D_i
    M = np.zeros((L, L))

    for i in range(L):
        # Diagonal term
        M[i, i] = Gamma[i]

        for k in range(L):
            if k != i and abs(h[i, k]) > 1e-15:
                denom = (Gamma[i] + Gamma[k]) / 2.0 + gamma_phi
                coeff = 2.0 * h[i, k] * h[i, k] / denom
                M[i, i] += coeff
                M[i, k] = -coeff

    # Solve M D = W_in
    D = np.linalg.solve(M, W_in)

    # Build off-diagonal imaginary correlation
    C_im = np.zeros((L, L))
    for i in range(L):
        for j in range(i + 1, L):
            denom = (Gamma[i] + Gamma[j]) / 2.0 + gamma_phi
            if denom > 1e-15:
                C_im[i, j] = h[i, j] * (D[i] - D[j]) / denom
                C_im[j, i] = -C_im[i, j]  # anti-symmetric

    # Assemble full C
    C = np.zeros((L, L), dtype=complex)
    for i in range(L):
        C[i, i] = D[i]
    for i in range(L):
        for j in range(i + 1, L):
            C[i, j] = 1j * C_im[i, j]
            C[j, i] = -1j * C_im[i, j]  # Hermitian conjugate

    return C, D, C_im


def compute_OXX(C_im):
    """
    O_XX = sum_{i!=j} |Im(C_{ij})|^2 = sum_{i!=j} C_im_{ij}^2

    Since C_im is anti-symmetric, C_im_{ji} = -C_im_{ij},
    so |Im(C_{ij})|^2 = C_im_{ij}^2 for both (i,j) and (j,i).
    """
    L = C_im.shape[0]
    OXX = 0.0
    for i in range(L):
        for j in range(i + 1, L):
            OXX += 2.0 * C_im[i, j] * C_im[i, j]
    return OXX


def compute_OXX_by_distance(C_im):
    """Compute O_XX per distance r."""
    L = C_im.shape[0]
    oxx_by_r = {}

    for r in range(1, L):
        total = 0.0
        for i in range(L - r):
            j = i + r
            total += 2.0 * C_im[i, j] * C_im[i, j]
        oxx_by_r[r] = total

    return oxx_by_r


def validate_against_dense():
    """Validate exact reduction against dense Lyapunov solver."""
    from firewall1_OXX import solve_ness_dense, compute_OXX as compute_OXX_full

    print("=" * 60)
    print("VALIDATION: Exact reduction vs dense solver (L=8)")
    print("=" * 60)

    params = [
        (1.1, 0.01), (1.1, 0.5), (1.1, 2.0),
        (1.5, 0.01), (1.5, 0.5), (1.5, 2.0),
        (1.9, 0.01), (1.9, 0.5), (1.9, 2.0),
    ]

    all_pass = True
    for alpha, gp in params:
        C_dense = solve_ness_dense(8, alpha, 0.3, 1.0, 1.0, 0.65, 0.35, gp)
        C_exact, D, C_im = solve_ness_exact(8, alpha, 0.3, 1.0, 1.0, 0.65, 0.35, gp)

        max_diff = np.max(np.abs(C_dense - C_exact))
        _, _, max_re, max_im = compute_OXX_full(C_dense)
        OXX_exact = compute_OXX(C_im)
        # Compute OXX from dense
        OXX_dense = 0.0
        for i in range(8):
            for j in range(i+1, 8):
                OXX_dense += 2.0 * C_dense[i, j].imag ** 2

        status = "PASS" if max_diff < 1e-12 else "FAIL"
        if max_diff >= 1e-12:
            all_pass = False
        print(f"  alpha={alpha:.1f} gp={gp:.2f}: diff={max_diff:.2e} "
              f"OXX_diff={abs(OXX_dense-OXX_exact):.2e} [{status}]")

    print(f"\n  All validations {'PASSED' if all_pass else 'HAD FAILURES'}")
    return all_pass


def main():
    output_dir = os.path.dirname(os.path.abspath(__file__))

    # --- Validate ---
    validate_against_dense()

    # --- Full scan ---
    J0 = 0.3
    Gamma_L = 1.0
    Gamma_R = 1.0
    f_L = 0.65
    f_R = 0.35

    L_values = [4, 8, 16, 32, 64, 128, 256]
    alpha_values = [1.1, 1.5, 1.9]
    gamma_phi_values = [0.01, 0.5, 2.0]

    print()
    print("=" * 80)
    print("FIREWALL 1: EXACT REDUCTION — FULL SCAN")
    print("=" * 80)
    print(f"L ∈ {L_values}")
    print(f"alpha ∈ {alpha_values}")
    print(f"gamma_phi ∈ {gamma_phi_values}")
    print(f"Total: {len(L_values)*len(alpha_values)*len(gamma_phi_values)} data points")
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

                C, D, C_im = solve_ness_exact(L, alpha, J0, Gamma_L, Gamma_R,
                                               f_L, f_R, gamma_phi)

                OXX = compute_OXX(C_im)
                OXX_per_L = OXX / L

                # Per-distance breakdown
                oxx_by_r = compute_OXX_by_distance(C_im)

                # Check purity: C_im_{ij} should be the only non-zero off-diagonal
                max_im = 0.0 if L <= 1 else np.max(np.abs(C_im))
                # For the exact solution, Re(C_{ij}) = 0 by construction

                t_elapsed = time.time() - t_start

                result = {
                    'L': L,
                    'alpha': alpha,
                    'gamma_phi': gamma_phi,
                    'OXX': float(OXX),
                    'OXX_per_L': float(OXX_per_L),
                    'max_im_offdiag': float(max_im),
                    'OXX_by_distance': {str(k): float(v) for k, v in sorted(oxx_by_r.items())},
                    'D_boundary': [float(D[0]), float(D[-1])],
                    'time_s': t_elapsed,
                }
                results.append(result)

                n_done += 1
                print(f"    gp={gamma_phi:.2f}: OXX={OXX:.6e}, OXX/L={OXX_per_L:.6e} "
                      f"max|Im|={max_im:.6e} [{t_elapsed:.3f}s] [{n_done}/{n_total}]",
                      flush=True)

    # Save raw results
    json_path = os.path.join(output_dir, 'firewall1_results.json')
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to: {json_path}")

    # --- Scaling Analysis ---
    print()
    print("=" * 80)
    print("SCALING ANALYSIS: O_XX/L ~ A * L^{-gamma}")
    print("=" * 80)

    data_by_params = {}
    for r in results:
        key = (r['alpha'], r['gamma_phi'])
        if key not in data_by_params:
            data_by_params[key] = {'L': [], 'OXX_per_L': [], 'OXX': []}
        data_by_params[key]['L'].append(r['L'])
        data_by_params[key]['OXX_per_L'].append(r['OXX_per_L'])
        data_by_params[key]['OXX'].append(r['OXX'])

    print(f"\n{'alpha':>6} {'gp':>8} {'gamma_all':>10} {'R^2_all':>8} "
          f"{'gamma_3pt':>10} {'R^2_3pt':>8} {'OXX/L(L=256)':>14} {'beta_OXX':>10}")
    print("-" * 85)

    fit_table = []

    for alpha in alpha_values:
        for gp in gamma_phi_values:
            key = (alpha, gp)
            d = data_by_params[key]
            L_arr = np.array(d['L'])
            oxx_arr = np.array(d['OXX_per_L'])
            oxx_raw = np.array(d['OXX'])

            # All-points fit
            log_L = np.log(L_arr)
            log_OXX = np.log(oxx_arr)
            slope, _, r_val, _, std_err = scipy.stats.linregress(log_L, log_OXX)
            gamma_all = -slope
            r_sq_all = r_val ** 2

            # 3 largest L values fit (asymptotic)
            log_L_3 = np.log(L_arr[-3:])
            log_OXX_3 = np.log(oxx_arr[-3:])
            slope_3, _, r_val_3, _, std_err_3 = scipy.stats.linregress(log_L_3, log_OXX_3)
            gamma_3 = -slope_3
            r_sq_3 = r_val_3 ** 2

            # OXX direct fit: OXX ~ L^{beta}
            log_OXX_raw = np.log(oxx_raw)
            slope_raw, _, _, _, _ = scipy.stats.linregress(log_L, log_OXX_raw)
            beta_oxx = slope_raw

            print(f"{alpha:>6.1f} {gp:>8.2f} {gamma_all:>10.4f} {r_sq_all:>8.4f} "
                  f"{gamma_3:>10.4f} {r_sq_3:>8.4f} {oxx_arr[-1]:>14.6e} {beta_oxx:>10.4f}")

            fit_table.append({
                'alpha': alpha, 'gamma_phi': gp,
                'gamma_all': gamma_all, 'gamma_3pt': gamma_3,
                'R2_all': r_sq_all, 'R2_3pt': r_sq_3,
                'std_err_all': std_err, 'std_err_3pt': std_err_3,
                'beta_OXX': beta_oxx,
                'OXX_per_L_256': oxx_arr[-1],
                'OXX_256': oxx_raw[-1],
            })

    # --- Firewall Verdict ---
    print()
    print("=" * 80)
    print("FIREWALL VERDICT")
    print("=" * 80)
    print("Firewall criterion: O_XX/L ~ L^{-gamma}")
    print("  gamma > 0  => O_XX/L -> 0  => XX has NO macroscopic signature")
    print("  gamma ~ 0  => O_XX/L -> const > 0 => XX HAS macroscopic signature")
    print()

    all_no_macro = True
    for ft in fit_table:
        a = ft['alpha']
        gp = ft['gamma_phi']
        gamma = ft['gamma_3pt']
        se = ft['std_err_3pt']
        gamma_min = gamma - 2 * se  # conservative lower bound

        if gamma_min <= 0.01:
            verdict = f"BORDERLINE (gamma_min={gamma_min:.4f} <= 0.01)"
            all_no_macro = False
        elif gamma_min > 0.1:
            verdict = f"NO MACRO (gamma_min={gamma_min:.4f} >> 0)"
        else:
            verdict = f"WEAK MACRO? (gamma_min={gamma_min:.4f} small)"

        print(f"  alpha={a:.1f} gp={gp:.2f}: gamma_3pt={gamma:.4f} "
              f"+/-{2*se:.4f}, gamma_min={gamma_min:.4f} -> {verdict}")

    print()
    if all_no_macro:
        print("  FINAL VERDICT: For ALL parameter combinations tested,")
        print("  O_XX/L -> 0 in the thermodynamic limit.")
        print("  XX amplitude has NO macroscopic signature.")
        print("  The XX framework is WEAKENED by Firewall 1.")
    else:
        print("  FINAL VERDICT: Some parameter combinations show")
        print("  possible macroscopic XX signatures.")
        print("  Further investigation needed.")

    # --- Save fit results ---
    fit_json_path = os.path.join(output_dir, 'firewall1_fit_results.json')
    with open(fit_json_path, 'w') as f:
        json.dump(fit_table, f, indent=2)
    print(f"\nFit results saved to: {fit_json_path}")

    # --- O_XX/L table ---
    print()
    print("=" * 80)
    print("O_XX/L TABLE (all data points)")
    print("=" * 80)

    header = f"{'L':>6}"
    for a in alpha_values:
        for gp in gamma_phi_values:
            header += f" {'a='+str(a)+',g='+str(gp):>18}"
    print(header)
    print("-" * (6 + 18 * len(alpha_values) * len(gamma_phi_values)))

    for L in L_values:
        line = f"{L:>6}"
        for a in alpha_values:
            for gp in gamma_phi_values:
                for r in results:
                    if r['L'] == L and abs(r['alpha']-a) < 1e-10 and abs(r['gamma_phi']-gp) < 1e-10:
                        line += f" {r['OXX_per_L']:>18.6e}"
                        break
                else:
                    line += f" {'N/A':>18}"
        print(line)

    print()
    print("=" * 80)
    print("FIREWALL 1 COMPLETE")
    print("=" * 80)


if __name__ == '__main__':
    main()

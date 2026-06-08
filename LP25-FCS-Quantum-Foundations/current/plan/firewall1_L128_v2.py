"""
Firewall 1 Supplement v2: L=128 via Lyapunov Iteration
=======================================================
Key insight: The steady-state equation can be written as:
    A C + C A^H = Q(C)
where A = ih + diag(Gamma_i/2) + (gamma_phi/2)*I
and Q depends on C's diagonal: Q_ii = W_in_i + gamma_phi * C_ii, Q_ij=0 (i!=j)

Method: Fixed-point iteration on the diagonal correction.
Each iteration solves a Lyapunov equation (Bartels-Stewart, O(L^3) — very fast).
"""

import sys
import io
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import numpy as np
from scipy.linalg import solve_continuous_lyapunov
import time
import json
import os


def construct_h(L, alpha, J0=0.3):
    """Single-particle Hamiltonian with power-law hopping."""
    h = np.zeros((L, L), dtype=complex)
    for i in range(L):
        for j in range(i + 1, L):
            r = j - i
            J = J0 / (r ** alpha)
            h[i, j] = J
            h[j, i] = J
    return h


def solve_ness_lyapunov_iter(L, alpha, J0=0.3, Gamma_L=1.0, Gamma_R=1.0,
                              f_L=0.65, f_R=0.35, gamma_phi=0.5,
                              max_iter=100, tol=1e-12):
    """
    Solve NESS correlation via Lyapunov fixed-point iteration.

    Equation: A C + C A^H = Q(C)
    where:
      A = ih + diag(Gamma_i/2 + gamma_phi/2)
      Q(C)_ii = W_in_i + gamma_phi * C_ii
      Q(C)_ij = 0 for i != j
    """
    h = construct_h(L, alpha, J0)

    Gamma_tot = np.zeros(L)
    Gamma_tot[0] = Gamma_L
    Gamma_tot[L-1] = Gamma_R

    W_in = np.zeros(L)
    W_in[0] = Gamma_L * f_L
    W_in[L-1] = Gamma_R * f_R

    # Build A = i*h + diag(Gamma/2 + gamma_phi/2)
    A = 1j * h
    for i in range(L):
        A[i, i] = Gamma_tot[i] / 2.0 + gamma_phi / 2.0

    # Initial guess: diagonal solution ignoring commutator
    C = np.zeros((L, L), dtype=complex)
    for i in range(L):
        if Gamma_tot[i] > 0:
            # For boundary sites: W_in_i / (Gamma_i + gamma_phi) adjusts for the extra term
            # Actually, the Lyapunov eq gives:
            # (A C + C A^H)_ii = Gamma_i C_ii + gamma_phi C_ii + i[h,C]_ii (but last is 0 for initial guess)
            # = W_in_i + gamma_phi C_ii
            # So: Gamma_i C_ii = W_in_i, C_ii = W_in_i / Gamma_i
            C[i, i] = W_in[i] / Gamma_tot[i]
        else:
            # Bulk site: set to average of boundary occupations
            C[i, i] = 0.5

    # Fixed-point iteration
    for iteration in range(max_iter):
        # Form Q from current diagonal estimate
        Q = np.diag(W_in + gamma_phi * np.real(np.diag(C)))

        # Solve Lyapunov equation
        C_new = solve_continuous_lyapunov(A, Q)

        # Enforce Hermiticity
        C_new = 0.5 * (C_new + C_new.conj().T)

        # Check convergence
        diff = np.max(np.abs(C_new - C))
        C = C_new

        if diff < tol:
            print(f"      Lyapunov iter converged at iteration {iteration+1}, diff={diff:.2e}", flush=True)
            break
    else:
        print(f"      Lyapunov iter max_iter={max_iter} reached, final diff={diff:.2e}", flush=True)

    return C


def compute_OXX(C):
    """Compute O_XX = sum_{i!=j} |Im(C_{ij})|^2."""
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


def compute_OXX_by_distance(C):
    """Compute O_XX per distance r = |i-j|."""
    L = C.shape[0]
    oxx_by_r = {}

    for r in range(1, L):
        total = 0.0
        for i in range(L - r):
            j = i + r
            im_ij = C[i, j].imag
            total += 2 * im_ij * im_ij
        oxx_by_r[r] = total

    return oxx_by_r


def validate_against_dense(L=8):
    """Validate Lyapunov iteration against dense solve for small L."""
    from firewall1_OXX import solve_ness_dense

    print("=" * 60)
    print("VALIDATION: Lyapunov iteration vs dense solver")
    print("=" * 60)

    J0 = 0.3
    Gamma_L = 1.0
    Gamma_R = 1.0
    f_L = 0.65
    f_R = 0.35

    for alpha in [1.1, 1.5, 1.9]:
        for gp in [0.01, 0.5, 2.0]:
            C_dense = solve_ness_dense(L, alpha, J0, Gamma_L, Gamma_R,
                                       f_L, f_R, gp)
            C_iter = solve_ness_lyapunov_iter(L, alpha, J0, Gamma_L, Gamma_R,
                                              f_L, f_R, gp)

            max_diff = np.max(np.abs(C_dense - C_iter))
            oxx_dense, _, _, _ = compute_OXX(C_dense)
            oxx_iter, _, _, _ = compute_OXX(C_iter)

            status = "PASS" if max_diff < 1e-10 else "FAIL"
            print(f"  alpha={alpha:.1f} gp={gp:.2f}: diff={max_diff:.2e} "
                  f"OXX_diff={abs(oxx_dense-oxx_iter):.2e} [{status}]")


def main():
    J0 = 0.3
    Gamma_L = 1.0
    Gamma_R = 1.0
    f_L = 0.65
    f_R = 0.35

    output_dir = os.path.dirname(os.path.abspath(__file__))

    # --- Validate ---
    validate_against_dense(L=8)

    # --- Compute L=128 ---
    L = 128
    alpha_values = [1.1, 1.5, 1.9]
    gamma_phi_values = [0.01, 0.5, 2.0]

    print()
    print("=" * 80)
    print(f"FIREWALL 1: L={L} LYAPUNOV ITERATION")
    print("=" * 80)
    print(f"alpha ∈ {alpha_values}")
    print(f"gamma_phi ∈ {gamma_phi_values}")
    print()

    results = []

    for alpha in alpha_values:
        print(f"  alpha = {alpha:.1f}:", flush=True)

        for gamma_phi in gamma_phi_values:
            t_start = time.time()

            C = solve_ness_lyapunov_iter(
                L, alpha, J0, Gamma_L, Gamma_R, f_L, f_R, gamma_phi
            )

            OXX, purity_ratio, max_re, max_im = compute_OXX(C)
            OXX_per_L = OXX / L

            # Per-distance breakdown
            oxx_by_r = compute_OXX_by_distance(C)

            t_elapsed = time.time() - t_start

            result = {
                'L': L,
                'alpha': alpha,
                'gamma_phi': gamma_phi,
                'OXX': float(OXX),
                'OXX_per_L': float(OXX_per_L),
                'purity_ratio': float(purity_ratio),
                'max_re_offdiag': float(max_re),
                'max_im_offdiag': float(max_im),
                'OXX_by_distance': {str(k): float(v) for k, v in sorted(oxx_by_r.items())},
                'time_s': t_elapsed,
            }
            results.append(result)

            print(f"    gp={gamma_phi:.2f}: OXX={OXX:.6e}, OXX/L={OXX_per_L:.6e}", flush=True)
            print(f"      |Im|_max={max_im:.6e}, purity Re/Im={purity_ratio:.2e}, {t_elapsed:.1f}s", flush=True)

    # Save results
    json_path = os.path.join(output_dir, 'firewall1_L128_results.json')
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to: {json_path}")

    # Asymptotic gamma fits using L=32,64,128
    print()
    print("=" * 80)
    print("ASYMPTOTIC GAMMA FITS (L=32, 64, 128) — 3 largest L values")
    print("=" * 80)

    # OXX_per_L data from L=32,64 (from the earlier dense run)
    L32_L64 = {
        (1.1, 0.01): [3.628061e-03, 2.544420e-03],
        (1.1, 0.50): [1.232773e-04, 5.374321e-05],
        (1.1, 2.00): [2.153173e-05, 9.001053e-06],
        (1.5, 0.01): [4.369971e-03, 3.084166e-03],
        (1.5, 0.50): [1.062987e-04, 3.839792e-05],
        (1.5, 2.00): [1.044494e-05, 3.283132e-06],
        (1.9, 0.01): [4.860627e-03, 3.451476e-03],
        (1.9, 0.50): [8.021456e-05, 2.376431e-05],
        (1.9, 2.00): [6.297445e-06, 1.681671e-06],
    }

    import scipy.stats

    print(f"\n{'alpha':>6} {'gp':>8} {'gamma_5pt':>10} {'gamma_3pt':>10} "
          f"{'R^2_3pt':>8} {'OXX/L(128)':>14}")
    print("-" * 65)

    for r in results:
        a = r['alpha']
        gp = r['gamma_phi']

        oxx_vals = L32_L64[(a, gp)] + [r['OXX_per_L']]
        L_vals = [32, 64, 128]

        log_L = np.log(L_vals)
        log_oxx = np.log(oxx_vals)
        slope, _, r_val, _, _ = scipy.stats.linregress(log_L, log_oxx)
        gamma_3pt = -slope
        r_sq = r_val ** 2

        gamma_5pt = {1.1: {0.01: 0.2104, 0.5: 1.1907, 2.0: 1.2824},
                    1.5: {0.01: 0.1928, 0.5: 1.3176, 2.0: 1.5978},
                    1.9: {0.01: 0.1799, 0.5: 1.4952, 2.0: 1.8104}}[a][gp]

        print(f"{a:>6.1f} {gp:>8.2f} {gamma_5pt:>10.4f} {gamma_3pt:>10.4f} "
              f"{r_sq:>8.4f} {r['OXX_per_L']:>14.6e}")

    print()
    print("=" * 80)
    print("FIREWALL VERDICT (asymptotic gamma from L=32,64,128):")
    print("=" * 80)
    for r in results:
        a = r['alpha']
        gp = r['gamma_phi']
        oxx_vals = L32_L64[(a, gp)] + [r['OXX_per_L']]
        log_L = np.log([32, 64, 128])
        log_oxx = np.log(oxx_vals)
        slope, _, _, _, std_err = scipy.stats.linregress(log_L, log_oxx)
        gamma = -slope
        # 95% CI
        gamma_lo = gamma - 2 * std_err
        verdict = "NO MACRO (gamma>>0)" if gamma > 0.1 else ("BORDERLINE" if gamma > 0.01 else "MACRO! (gamma~0)")
        print(f"  alpha={a:.1f} gp={gp:.2f}: gamma={gamma:.4f}+/-{2*std_err:.4f} [{verdict}]")


if __name__ == '__main__':
    main()

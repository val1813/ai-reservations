"""
Firewall 1: Sparse Direct Solver for L=128, L=256
==================================================
Uses scipy.sparse.linalg.spsolve (SuperLU) on the vectorized
Liouvillian. The sparse matrix is built in COO format.
"""

import sys
import io
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import spsolve
import time
import json
import os
import gc


def construct_h(L, alpha, J0=0.3):
    h = np.zeros((L, L), dtype=complex)
    for i in range(L):
        for j in range(i+1, L):
            r = j - i
            J = J0 / (r ** alpha)
            h[i, j] = J
            h[j, i] = J
    return h


def solve_ness_sparse_direct(L, alpha, J0=0.3, Gamma_L=1.0, Gamma_R=1.0,
                              f_L=0.65, f_R=0.35, gamma_phi=0.5):
    """Solve NESS using sparse COO + SuperLU direct factorization."""
    h = construct_h(L, alpha, J0)

    Gamma_tot = np.zeros(L)
    Gamma_tot[0] = Gamma_L
    Gamma_tot[L-1] = Gamma_R

    W_in = np.zeros(L)
    W_in[0] = Gamma_L * f_L
    W_in[L-1] = Gamma_R * f_R

    L2 = L * L

    # Pre-count nonzeros
    nnz_est = 0
    for i in range(L):
        if i == 0 or i == L-1:
            nnz_per_row = 1 + 2 * (L - 1)  # boundary
        else:
            nnz_per_row = 1 + 2 * (L - 1)  # all rows have ~2L entries
        nnz_est += nnz_per_row * L
    # Actually each row has 1 + 2*(L-1) entries approx
    nnz_est = L2 * (1 + 2*(L-1))
    print(f"      Estimated nnz: {nnz_est}", flush=True)

    # Build in COO
    rows_list = []
    cols_list = []
    data_list = []
    b_vec = np.zeros(L2, dtype=complex)

    batch_size = 1000000  # flush to COO every million entries

    for i in range(L):
        G_i = Gamma_tot[i]
        for j in range(L):
            row = i * L + j
            G_j = Gamma_tot[j]

            if i == j:
                # Diagonal
                rows_list.append(row)
                cols_list.append(row)
                data_list.append(G_i)

                # Commutator
                for k in range(L):
                    h_ik = h[i, k]
                    if abs(h_ik) > 1e-15:
                        rows_list.append(row)
                        cols_list.append(k * L + i)
                        data_list.append(1j * h_ik)
                        rows_list.append(row)
                        cols_list.append(i * L + k)
                        data_list.append(-1j * h_ik)

                b_vec[row] = W_in[i]
            else:
                # Off-diagonal
                rows_list.append(row)
                cols_list.append(row)
                data_list.append(0.5 * (G_i + G_j) + gamma_phi)

                # Commutator
                for k in range(L):
                    h_ik = h[i, k]
                    if abs(h_ik) > 1e-15:
                        rows_list.append(row)
                        cols_list.append(k * L + j)
                        data_list.append(1j * h_ik)
                    h_kj = h[k, j]
                    if abs(h_kj) > 1e-15:
                        rows_list.append(row)
                        cols_list.append(i * L + k)
                        data_list.append(-1j * h_kj)

    print(f"      Actual nnz: {len(rows_list)}", flush=True)

    # Build sparse matrix
    A = sparse.coo_matrix((data_list, (rows_list, cols_list)),
                         shape=(L2, L2), dtype=complex).tocsr()

    # Free COO arrays
    del rows_list, cols_list, data_list
    gc.collect()

    print(f"      CSR nnz: {A.nnz}", flush=True)

    # Direct sparse solve
    C_vec = spsolve(A, b_vec)

    C = C_vec.reshape(L, L)
    C = 0.5 * (C + C.conj().T)

    return C


def compute_OXX(C):
    L = C.shape[0]
    OXX = 0.0
    max_re_offdiag = 0.0
    max_im_offdiag = 0.0
    for i in range(L):
        for j in range(i+1, L):
            im_val = C[i, j].imag
            re_val = C[i, j].real
            OXX += 2.0 * im_val * im_val
            max_re_offdiag = max(max_re_offdiag, abs(re_val))
            max_im_offdiag = max(max_im_offdiag, abs(im_val))
    purity = max_re_offdiag / max_im_offdiag if max_im_offdiag > 1e-20 else float('inf')
    return OXX, purity, max_re_offdiag, max_im_offdiag


def main():
    J0 = 0.3
    Gamma_L = 1.0
    Gamma_R = 1.0
    f_L = 0.65
    f_R = 0.35

    L_values = [128, 256]
    alpha_values = [1.1, 1.5, 1.9]
    gamma_phi_values = [0.01, 0.5, 2.0]

    output_dir = os.path.dirname(os.path.abspath(__file__))

    print("=" * 80)
    print("FIREWALL 1: SPARSE DIRECT SOLVER (L=128, 256)")
    print("=" * 80)
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

                try:
                    C = solve_ness_sparse_direct(
                        L, alpha, J0, Gamma_L, Gamma_R, f_L, f_R, gamma_phi
                    )

                    OXX, purity, max_re, max_im = compute_OXX(C)
                    OXX_per_L = OXX / L

                    t_elapsed = time.time() - t_start
                    n_done += 1

                    result = {
                        'L': L, 'alpha': alpha, 'gamma_phi': gamma_phi,
                        'OXX': float(OXX), 'OXX_per_L': float(OXX_per_L),
                        'purity': float(purity),
                        'max_re_offdiag': float(max_re),
                        'max_im_offdiag': float(max_im),
                        'time_s': t_elapsed,
                    }
                    results.append(result)

                    print(f"    gp={gamma_phi:.2f}: OXX={OXX:.6e}, OXX/L={OXX_per_L:.6e} "
                          f"purity={purity:.2e} [{t_elapsed:.1f}s] [{n_done}/{n_total}]",
                          flush=True)

                except Exception as e:
                    import traceback
                    traceback.print_exc()
                    n_done += 1
                    print(f"    gp={gamma_phi:.2f}: FAILED - {e} [{n_done}/{n_total}]", flush=True)
                    results.append({
                        'L': L, 'alpha': alpha, 'gamma_phi': gamma_phi,
                        'error': str(e),
                    })

    # Save
    json_path = os.path.join(output_dir, 'firewall1_sparse_results.json')
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved to: {json_path}")

    # Summary
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    for r in results:
        if 'error' not in r:
            print(f"  L={r['L']} a={r['alpha']} gp={r['gamma_phi']}: "
                  f"OXX/L={r['OXX_per_L']:.6e} [{r['time_s']:.1f}s]")


if __name__ == '__main__':
    main()

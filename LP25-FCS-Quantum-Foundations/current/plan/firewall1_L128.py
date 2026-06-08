"""
Firewall 1 Supplement: L=128 Sparse Computation
================================================
Optimized sparse solver using GMRES for L=128.
Computes C, then O_XX for all (alpha, gamma_phi) combinations.

Method: COO-format sparse construction + GMRES with diagonal preconditioner.
"""

import sys
import io
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import gmres
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


def solve_ness_sparse_gmres(L, alpha, J0=0.3, Gamma_L=1.0, Gamma_R=1.0,
                             f_L=0.65, f_R=0.35, gamma_phi=0.5):
    """
    Solve NESS correlation using sparse COO construction + GMRES.

    The steady-state equation:
    i[h, C] + 1/2{Gamma_diag, C} + gamma_phi(C - diag(C)) = diag(W_in)

    Vectorized as A * vec(C) = b, where A is L^2 x L^2 sparse.
    """
    h = construct_h(L, alpha, J0)

    Gamma_tot = np.zeros(L)
    Gamma_tot[0] = Gamma_L
    Gamma_tot[L-1] = Gamma_R

    W_in = np.zeros(L)
    W_in[0] = Gamma_L * f_L
    W_in[L-1] = Gamma_R * f_R

    L2 = L * L

    # Estimate nnz: each of L^2 rows has ~2L entries from commutator + 1 diagonal
    # But power-law hopping means h is dense, so each row gets ~2L entries
    # Total: L^2 * (2L + 1) ≈ 2L^3
    est_nnz = L2 * (2 * L + 1)

    # Use COO format for fast construction
    rows = []
    cols = []
    data = []
    b_vec = np.zeros(L2, dtype=complex)

    for i in range(L):
        for j in range(L):
            row = i * L + j

            if i == j:
                # Diagonal element: damping Gamma_i
                rows.append(row)
                cols.append(row)
                data.append(Gamma_tot[i])

                # Commutator i[h, C]_{ii} = i * sum_k (h_{ik} C_{ki} - C_{ik} h_{ki})
                for k in range(L):
                    h_ik = h[i, k]
                    if abs(h_ik) > 1e-15:
                        # +i * h_{ik} * C_{ki}
                        rows.append(row)
                        cols.append(k * L + i)
                        data.append(1j * h_ik)
                        # -i * C_{ik} * h_{ik}
                        rows.append(row)
                        cols.append(i * L + k)
                        data.append(-1j * h_ik)

                b_vec[row] = W_in[i]
            else:
                # Off-diagonal: damping + dephasing
                rows.append(row)
                cols.append(row)
                data.append(0.5 * (Gamma_tot[i] + Gamma_tot[j]) + gamma_phi)

                # Commutator
                for k in range(L):
                    h_ik = h[i, k]
                    if abs(h_ik) > 1e-15:
                        rows.append(row)
                        cols.append(k * L + j)
                        data.append(1j * h_ik)

                    h_kj = h[k, j]
                    if abs(h_kj) > 1e-15:
                        rows.append(row)
                        cols.append(i * L + k)
                        data.append(-1j * h_kj)

    # Build CSR matrix
    A = sparse.coo_matrix((data, (rows, cols)), shape=(L2, L2), dtype=complex).tocsr()
    print(f"      A: {L2}x{L2}, nnz={A.nnz} ({A.nnz/L2:.1f}/row)", flush=True)

    # Diagonal preconditioner
    M_diag = A.diagonal()
    # Avoid division by zero for nearly-zero diagonal entries
    diag_abs = np.abs(M_diag)
    M_inv_diag = np.where(diag_abs > 1e-15, 1.0 / M_diag, 0.0)
    M = sparse.diags(M_inv_diag, 0, dtype=complex)

    # Solve with GMRES
    # Use a reasonable initial guess: diagonal solution
    x0 = np.zeros(L2, dtype=complex)
    # Set diagonal elements of x0 to W_in_i / Gamma_i
    for i in range(L):
        if Gamma_tot[i] > 0:
            x0[i * L + i] = W_in[i] / Gamma_tot[i]
        else:
            x0[i * L + i] = 0.5  # default guess for bulk sites

    C_vec, info = gmres(A, b_vec, x0=x0, M=M, tol=1e-10, maxiter=3000, restart=200)

    if info > 0:
        print(f"      GMRES converged to tolerance (iterations={info})", flush=True)
    elif info < 0:
        print(f"      WARNING: GMRES illegal input or breakdown (info={info})", flush=True)
    else:
        print(f"      GMRES converged (info=0)", flush=True)

    C = C_vec.reshape(L, L)
    C = 0.5 * (C + C.conj().T)

    return C


def compute_OXX(C):
    """Compute O_XX = sum_{i!=j} |Im(C_{ij})|^2."""
    L = C.shape[0]
    OXX = 0.0
    max_re_offdiag = 0.0
    max_im_offdiag = 0.0
    n_offdiag = 0

    for i in range(L):
        for j in range(L):
            if i != j:
                im_part = C[i, j].imag
                re_part = C[i, j].real
                OXX += im_part * im_part
                max_re_offdiag = max(max_re_offdiag, abs(re_part))
                max_im_offdiag = max(max_im_offdiag, abs(im_part))
                n_offdiag += 1

    purity_ratio = max_re_offdiag / max_im_offdiag if max_im_offdiag > 1e-20 else float('inf')

    return OXX, purity_ratio, max_re_offdiag, max_im_offdiag, n_offdiag


def compute_OXX_by_distance(C):
    """Compute O_XX per distance r = |i-j|."""
    L = C.shape[0]
    oxx_by_r = {}

    for r in range(1, L):
        total = 0.0
        count = 0
        for i in range(L - r):
            j = i + r
            im_ij = C[i, j].imag
            total += 2 * im_ij * im_ij  # both (i,j) and (j,i) contribute
            count += 2
        oxx_by_r[r] = total

    return oxx_by_r


def main():
    J0 = 0.3
    Gamma_L = 1.0
    Gamma_R = 1.0
    f_L = 0.65
    f_R = 0.35

    L = 128
    alpha_values = [1.1, 1.5, 1.9]
    gamma_phi_values = [0.01, 0.5, 2.0]

    output_dir = os.path.dirname(os.path.abspath(__file__))

    print("=" * 80)
    print(f"FIREWALL 1 SUPPLEMENT: L={L} SPARSE GMRES COMPUTATION")
    print("=" * 80)
    print(f"Parameters: J0={J0}, Gamma_L={Gamma_L}, Gamma_R={Gamma_R}")
    print(f"             f_L={f_L}, f_R={f_R}")
    print(f"alpha ∈ {alpha_values}")
    print(f"gamma_phi ∈ {gamma_phi_values}")
    print()

    results = []

    for alpha in alpha_values:
        print(f"  alpha = {alpha:.1f}:", flush=True)

        for gamma_phi in gamma_phi_values:
            t_start = time.time()

            try:
                print(f"    gp={gamma_phi:.2f}: building sparse system...", flush=True)
                C = solve_ness_sparse_gmres(
                    L, alpha, J0, Gamma_L, Gamma_R, f_L, f_R, gamma_phi
                )

                print(f"      computing O_XX...", flush=True)
                OXX, purity_ratio, max_re, max_im, n_offdiag = compute_OXX(C)
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

                print(f"      OXX={OXX:.6e}, OXX/L={OXX_per_L:.6e}", flush=True)
                print(f"      |Im|_max={max_im:.6e}, purity Re/Im={purity_ratio:.2e}", flush=True)
                print(f"      time={t_elapsed:.1f}s", flush=True)

            except Exception as e:
                import traceback
                traceback.print_exc()
                print(f"      FAILED: {e}", flush=True)
                results.append({
                    'L': L,
                    'alpha': alpha,
                    'gamma_phi': gamma_phi,
                    'error': str(e),
                })

    # Save results
    json_path = os.path.join(output_dir, 'firewall1_L128_results.json')
    serializable = []
    for r in results:
        entry = {}
        for k, v in r.items():
            if isinstance(v, dict):
                entry[k] = {str(dk): float(dv) for dk, dv in v.items()}
            elif isinstance(v, float):
                entry[k] = float(v)
            elif isinstance(v, int):
                entry[k] = int(v)
            elif v is None:
                entry[k] = None
            else:
                entry[k] = v
        serializable.append(entry)

    with open(json_path, 'w') as f:
        json.dump(serializable, f, indent=2)
    print(f"\nResults saved to: {json_path}")
    print(f"Successful: {sum(1 for r in results if 'error' not in r)}/{len(results)}")

    # Quick fit with previous data
    print("\n" + "=" * 80)
    print("GAMMA FIT WITH L=128 APPENDED (using L=32,64,128)")
    print("=" * 80)

    # Previous OXX_per_L values for L=32,64
    prev_data = {
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

    print(f"\n{'alpha':>6} {'gp':>8} {'gamma_5pt':>10} {'gamma_3pt':>10} "
          f"{'OXX/L(L=128)':>14}")
    print("-" * 60)

    for r in results:
        if 'error' in r:
            continue
        a = r['alpha']
        gp = r['gamma_phi']

        # 3-point fit: L=32, 64, 128
        oxx_vals = prev_data.get((a, gp), []) + [r['OXX_per_L']]
        L_vals = [32, 64, 128]

        if len(oxx_vals) == 3:
            log_L = np.log(L_vals)
            log_OXX = np.log(oxx_vals)
            import scipy.stats
            slope, _, r_val, _, _ = scipy.stats.linregress(log_L, log_OXX)
            gamma_3pt = -slope
            # 5-point gamma from earlier fit
            gamma_5pt = {1.1: {0.01: 0.2104, 0.5: 1.1907, 2.0: 1.2824},
                        1.5: {0.01: 0.1928, 0.5: 1.3176, 2.0: 1.5978},
                        1.9: {0.01: 0.1799, 0.5: 1.4952, 2.0: 1.8104}}[a][gp]

            print(f"{a:>6.1f} {gp:>8.2f} {gamma_5pt:>10.4f} {gamma_3pt:>10.4f} "
                  f"{r['OXX_per_L']:>14.6e}")

    print("\n" + "=" * 80)
    print("DONE")
    print("=" * 80)


if __name__ == '__main__':
    main()

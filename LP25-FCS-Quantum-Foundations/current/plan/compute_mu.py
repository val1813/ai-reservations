"""
compute_mu.py — Self-consistent transport exponent from current J(L).
Uses the same solver as fss_compute.py, extracts full C matrix,
computes current J = sum_r 2*J0/r^alpha * Im[C_{i,i+r}] (bulk average).
Fits J(L) ~ L^{-mu} for each (alpha, gamma_phi).

Usage: python compute_mu.py
Output: compute_mu_results.json
"""
import numpy as np
from scipy import sparse
from scipy.sparse.linalg import gmres
import scipy.stats
import time, json, os, sys, warnings
warnings.filterwarnings('ignore')

BASE = os.path.dirname(os.path.abspath(__file__))

# ============================================================
def make_system(L, alpha, gamma_phi, J0=0.3, Gamma_L=1.0, Gamma_R=1.0,
                f_L=0.65, f_R=0.35, hop_tol=1e-10):
    h = np.zeros((L, L))
    for i in range(L):
        for j in range(i + 1, L):
            J = J0 / (j - i) ** alpha
            if J > hop_tol:
                h[i, j] = h[j, i] = J

    Gamma_tot = np.zeros(L)
    Gamma_tot[0] = Gamma_L
    Gamma_tot[L - 1] = Gamma_R
    W_in = np.zeros(L)
    W_in[0] = Gamma_L * f_L
    W_in[L - 1] = Gamma_R * f_R

    L2 = L * L
    rows, cols, data_vals = [], [], []
    b = np.zeros(L2, dtype=complex)

    for i in range(L):
        for j in range(L):
            row = i * L + j
            damp = 0.5 * (Gamma_tot[i] + Gamma_tot[j])
            if i != j:
                damp += gamma_phi
            rows.append(row); cols.append(row); data_vals.append(damp)

            for k in range(L):
                if abs(h[i, k]) > hop_tol:
                    rows.append(row); cols.append(k * L + j)
                    data_vals.append(1j * h[i, k])
                if abs(h[k, j]) > hop_tol:
                    rows.append(row); cols.append(i * L + k)
                    data_vals.append(-1j * h[k, j])
            if i == j:
                b[row] = W_in[i]

    A = sparse.coo_matrix((data_vals, (rows, cols)), shape=(L2, L2)).tocsr()
    return A, b, h


def solve_ness(L, alpha, gamma_phi, **kwargs):
    """Solve NESS, return full C matrix."""
    A, b, h = make_system(L, alpha, gamma_phi, **kwargs)

    diag = A.diagonal()
    diag[diag == 0] = 1.0
    M = sparse.diags(1.0 / np.abs(diag))

    t0 = time.time()
    x, info = gmres(A, b, M=M, rtol=1e-10, maxiter=3000,
                    restart=min(200, L * L))
    elapsed = time.time() - t0

    if info != 0:
        print(f"  WARNING: GMRES info={info}, L={L}, alpha={alpha}")

    C = x.reshape(L, L)
    C = 0.5 * (C + C.conj().T)
    return C, h, elapsed, info


def compute_current(C, L, Gamma_L=1.0, f_L=0.65):
    """
    Steady-state current from boundary injection.
    J = Gamma_L * (f_L - D_1) = Gamma_R * (D_L - f_R)
    where D_1 = C[0,0] (real) is the occupation of site 1.
    This follows from the diagonal Lindblad equation.
    Also returns bulk check: J_bulk from average occupation gradient.
    """
    D_1 = np.real(C[0, 0])
    J_boundary = Gamma_L * (f_L - D_1)
    # Cross-check: bulk midchain gradient proxy
    mid = L // 2
    D_mid_left = np.real(C[mid - 1, mid - 1])
    D_mid_right = np.real(C[mid, mid])
    J_bulk_proxy = abs(D_mid_left - D_mid_right)  # occupation gradient at midchain
    return J_boundary, J_bulk_proxy, D_1


# ============================================================
def main():
    alphas = [1.1, 1.3, 1.5, 1.7, 1.9]
    gamma_phis = [0.1, 0.5, 1.0, 2.0]  # skip 0.01 (too slow)
    L_vals_small = [8, 16, 32, 64]      # dense solver range
    L_vals_large = [8, 16, 32, 64, 128]  # extended for key gamma

    results = {}

    for gp in gamma_phis:
        print(f"\n{'='*50}")
        print(f"gamma_phi = {gp}")
        print(f"{'='*50}")

        L_vals = L_vals_large if gp == 0.5 else L_vals_small

        for alpha in alphas:
            print(f"  alpha={alpha}...", end=" ", flush=True)
            J_vals, L_used = [], []

            for L in L_vals:
                if L <= 64:
                    # Use dense solver for L<=64 (faster)
                    C, h, elapsed, info = solve_ness(L, alpha, gp)
                else:
                    C, h, elapsed, info = solve_ness(L, alpha, gp)

                J_mean, J_bulk, D1 = compute_current(C, L)
                J_vals.append(J_mean)
                L_used.append(L)
                print(f"L={L}:{elapsed:.0f}s", end=" ", flush=True)

            # Fit J ~ L^{-mu}
            log_L = np.log(L_used)
            log_J = np.log(np.abs(J_vals))
            slope, intercept, r, p, se = scipy.stats.linregress(log_L, log_J)
            mu = -slope

            key = f"{alpha}_{gp}"
            results[key] = {
                "alpha": alpha, "gamma_phi": gp,
                "L_values": L_used,
                "J_values": J_vals,
                "mu": mu,
                "std_err": se,
                "R2": r**2,
                "n_points": len(L_used)
            }
            print(f"-> mu={mu:.4f}+/-{se:.4f} R2={r**2:.4f}")

    # Save
    out_path = os.path.join(BASE, "compute_mu_results.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {out_path}")

    # Summary table
    print("\n=== SUMMARY: mu(alpha, gamma_phi) ===")
    print(f"{'alpha':<8}", end="")
    for gp in gamma_phis:
        print(f"{'gp='+str(gp):>16}", end="")
    print()
    for alpha in alphas:
        print(f"{alpha:<8}", end="")
        for gp in gamma_phis:
            key = f"{alpha}_{gp}"
            if key in results:
                print(f"{results[key]['mu']:>12.4f}+/-{results[key]['std_err']:.4f}", end="  ")
            else:
                print(f"{'N/A':>16}", end="  ")
        print()


if __name__ == "__main__":
    main()

"""
P0 Verification: b1 -> c(b1) numerical test
============================================
Verify DGF core prediction: causal graph Betti number b1 maps to
Virasoro central charge c(b1).

Method: XXZ spin chain exact diagonalization + Calabrese-Cardy fit.

Theory predictions:
  b1=1 -> Delta=-1/2 -> c=1/2  (Ising CFT)
  b1=2 -> Delta=-1/sqrt(2)~-0.707 -> c=7/10 (Tricritical Ising)
  b1=3 -> Delta=-cos(pi/5)~-0.809 -> c=4/5 (3-state Potts)

Fit: S(L) = (c/3) log((N/pi) sin(pi*L/N)) + const
"""
import numpy as np
from scipy import linalg
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# Pauli matrices
# ============================================================
SX = np.array([[0,1],[1,0]], dtype=complex)
SY = np.array([[0,-1j],[1j,0]], dtype=complex)
SZ = np.array([[1,0],[0,-1]], dtype=complex)
I2 = np.eye(2, dtype=complex)

# ============================================================
# DGF predictions
# ============================================================
def delta_from_b1(b1):
    """DGF: b1 -> TL parameter delta -> XXZ anisotropy Delta.
    delta = 2*cos(pi/(b1+2)), Delta = -delta/2 = -cos(pi/(b1+2))"""
    return -np.cos(np.pi / (b1 + 2))

def c_prediction(b1):
    """DGF: c(b1) = 1 - 6/((b1+2)(b1+3)).
    A-series unitary Virasoro minimal models M(b1+2, b1+3)."""
    return 1.0 - 6.0 / ((b1 + 2) * (b1 + 3))

# ============================================================
# XXZ Hamiltonian
# ============================================================
def xxz_hamiltonian(N, Delta, periodic=True):
    """H = sum_i [X_i X_{i+1} + Y_i Y_{i+1} + Delta * Z_i Z_{i+1}]"""
    H = np.zeros((2**N, 2**N), dtype=complex)
    for i in range(N):
        j = (i + 1) % N
        if not periodic and j == 0:
            continue
        # Build XX + YY + Delta*ZZ operator
        op_xx = np.ones(1, dtype=complex)
        op_yy = np.ones(1, dtype=complex)
        op_zz = np.ones(1, dtype=complex)
        for k in range(N):
            if k == i:
                op_xx = np.kron(op_xx, SX)
                op_yy = np.kron(op_yy, SY)
                op_zz = np.kron(op_zz, SZ)
            elif k == j:
                op_xx = np.kron(op_xx, SX)
                op_yy = np.kron(op_yy, SY)
                op_zz = np.kron(op_zz, SZ)
            else:
                op_xx = np.kron(op_xx, I2)
                op_yy = np.kron(op_yy, I2)
                op_zz = np.kron(op_zz, I2)
        H += op_xx + op_yy + Delta * op_zz
    return H

# ============================================================
# Entanglement entropy
# ============================================================
def entanglement_entropy(psi, L, N):
    """von Neumann entropy S = -Tr(rho_A log rho_A) for first L spins."""
    psi_matrix = psi.reshape(2**L, 2**(N-L))
    rho_A = psi_matrix @ psi_matrix.conj().T
    evals = np.linalg.eigvalsh(rho_A)
    evals = evals[evals > 1e-15]
    return -np.sum(evals * np.log(evals))

# ============================================================
# Main verification for a given b1
# ============================================================
def verify_b1(b1, N_max=12, periodic=True):
    """Verify c(b1) prediction via exact diagonalization."""
    Delta = delta_from_b1(b1)
    c_theory = c_prediction(b1)

    print(f"\n{'='*60}")
    print(f"b1={b1}: Delta={Delta:.6f}, c_theory={c_theory:.4f}")
    print(f"{'='*60}")

    results = []
    for N in range(6, N_max+1, 2):
        print(f"\n  N={N}:")
        H = xxz_hamiltonian(N, Delta, periodic=periodic)
        eigenvalues, eigenvectors = linalg.eigh(H)
        psi_gs = eigenvectors[:, 0]
        E0 = eigenvalues[0]
        print(f"    E0/N = {E0/N:.6f}")

        L_vals = np.arange(1, N)
        S_vals = np.zeros(len(L_vals))
        for idx, L in enumerate(L_vals):
            S_vals[idx] = entanglement_entropy(psi_gs, L, N)

        # Calabrese-Cardy fit: S = (c/3)*log((N/pi)*sin(pi*L/N)) + S0
        d_vals = (N/np.pi) * np.sin(np.pi * L_vals / N)
        log_d = np.log(d_vals)

        # Use middle region to avoid boundary effects
        mid_start = max(1, N//6)
        mid_end = N - mid_start
        mask = (L_vals >= mid_start) & (L_vals <= mid_end)

        if np.sum(mask) >= 3:
            fit_x = log_d[mask]
            fit_y = S_vals[mask]
            coeffs = np.polyfit(fit_x, fit_y, 1)
            c_extracted = 3.0 * coeffs[0]
            S_fit = np.polyval(coeffs, fit_x)
            ss_res = np.sum((fit_y - S_fit)**2)
            ss_tot = np.sum((fit_y - np.mean(fit_y))**2)
            r_sq = 1 - ss_res/ss_tot if ss_tot > 0 else 0

            results.append({'N': N, 'c': c_extracted, 'S0': coeffs[1], 'R2': r_sq})
            print(f"    c_extracted = {c_extracted:.4f} (theory: {c_theory:.4f})")
            print(f"    R^2 = {r_sq:.4f},  fit region L in [{mid_start}, {mid_end}]")
        else:
            print(f"    Not enough fit points (need >=3)")

    if results:
        c_vals = [r['c'] for r in results]
        c_avg = np.mean(c_vals)
        c_std = np.std(c_vals)
        error = abs(c_avg - c_theory)
        print(f"\n  Summary: c_extracted = {c_avg:.4f} +/- {c_std:.4f}")
        print(f"  Theory: c = {c_theory:.4f}")
        print(f"  Error: {error:.4f} ({error/c_theory*100:.1f}%)")
        if error < 0.05:
            print(f"  >> PASS (error < 0.05)")
        elif error < 0.10:
            print(f"  >> MARGINAL (error < 0.10)")
        else:
            print(f"  >> FAIL (error >= 0.10)")
        return {'c_theory': c_theory, 'c_extracted': c_avg, 'c_std': c_std,
                'error': error, 'passed': error < 0.10}
    return None

# ============================================================
# Main
# ============================================================
def main():
    print("=" * 60)
    print("  DGF LP41 P0: b1 -> c(b1) numerical verification")
    print("  XXZ chain + exact diagonalization + CC fit")
    print("=" * 60)

    all_results = {}
    for b1 in [1, 2]:
        N_max = 10 if b1 == 2 else 12
        result = verify_b1(b1, N_max=N_max, periodic=True)
        if result:
            all_results[b1] = result

    # Try b1=3 with smaller system
    print(f"\n\nb1=3: N_max=8 (limited by Hilbert space size)")
    result = verify_b1(3, N_max=8, periodic=True)
    if result:
        all_results[3] = result

    # Final summary
    print(f"\n\n{'='*60}")
    print(f"FINAL SUMMARY")
    print(f"{'='*60}")
    print(f"{'b1':>4s}  {'c_theory':>10s}  {'c_extracted':>14s}  {'error':>8s}  {'verdict':>8s}")
    print(f"{'-'*52}")
    for b1 in sorted(all_results.keys()):
        r = all_results[b1]
        status = "PASS" if r['passed'] else "FAIL"
        print(f"{b1:4d}  {r['c_theory']:10.4f}  {r['c_extracted']:>8.4f} +/- {r['c_std']:.4f}  "
              f"{r['error']:8.4f}  {status:>8s}")

    # Discrete spectrum test
    if len(all_results) >= 2:
        print(f"\n--- Discrete Spectrum Test ---")
        b1s = sorted(all_results.keys())
        for i in range(len(b1s)-1):
            a, b = b1s[i], b1s[i+1]
            ratio_theory = c_prediction(b) / c_prediction(a)
            ratio_expt = all_results[b]['c_extracted'] / all_results[a]['c_extracted']
            print(f"  c({b})/c({a}) = {ratio_theory:.4f} (theory) vs {ratio_expt:.4f} (extracted)")

    print(f"\nP0 verification complete.")

if __name__ == "__main__":
    main()

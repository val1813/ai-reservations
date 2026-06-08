"""
Analyze the structure of the Lyapunov equation solution
to guide analytical derivation of beta(alpha).

Key questions:
1. What is the relationship between C_{ij} and occupation gradient D_j - D_i?
2. Does the interior occupation satisfy a fractional diffusion equation?
3. What is the scaling of the midpoint gradient with L?
"""
import sys, io
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import numpy as np
from scipy.linalg import solve_continuous_lyapunov
import json

J0 = 0.3
Gamma_L = 1.0
Gamma_R = 1.0
f_L = 0.65
f_R = 0.35

def construct_h(L, alpha):
    h = np.zeros((L, L), dtype=complex)
    for i in range(L):
        for j in range(i+1, L):
            r = j - i
            J = J0 / (r ** alpha)
            h[i, j] = J
            h[j, i] = J
    return h

def solve_ness(L, alpha, gamma_phi):
    h = construct_h(L, alpha)
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
    return C, h

def analyze_structure(L=32, alpha=1.5, gamma_phi=0.5):
    """Analyze the structure of the NESS solution."""
    C, h = solve_ness(L, alpha, gamma_phi)

    # Decompose C = D + iO where D is diagonal (real) and O is off-diagonal (real antisymmetric)
    D = np.diag(np.diag(C.real))
    O = C.imag  # purely off-diagonal, antisymmetric

    print(f"=== L={L}, alpha={alpha}, gamma_phi={gamma_phi} ===")
    print(f"Max |Re(C_offdiag)|: {np.max(np.abs(C.real - D)):.2e}")
    print(f"Max |Im(C_diag)|: {np.max(np.abs(np.diag(C.imag))):.2e}")
    print(f"O antisymmetric check: max|O+O^T| = {np.max(np.abs(O + O.T)):.2e}")

    # === Check 1: Off-diagonal equation for interior ===
    # i[h, C]_{ij} + gamma_phi C_{ij} = 0 for interior i,j
    comm = 1j * (h @ C - C @ h)  # i[h, C]
    interior_mask = np.ones((L, L), dtype=bool)
    interior_mask[0, :] = False
    interior_mask[-1, :] = False
    interior_mask[:, 0] = False
    interior_mask[:, -1] = False
    np.fill_diagonal(interior_mask, False)

    # Check: i[h,C] + gamma_phi C should be ~0 for interior off-diagonal
    residual = comm + gamma_phi * C
    interior_residual = residual[interior_mask]
    max_residual = np.max(np.abs(interior_residual))
    print(f"\n=== Check 1: Off-diagonal equation for interior ===")
    print(f"Max |i[h,C] + gamma_phi*C| for interior off-diag: {max_residual:.2e}")

    # === Check 2: First-order relation O_{ij} = -h_{ij}(D_j-D_i)/gamma_phi ===
    O_first_order = np.zeros((L, L))
    for i in range(L):
        for j in range(L):
            if i != j:
                O_first_order[i, j] = -h[i, j].real * (D[j, j] - D[i, i]) / gamma_phi

    O_diff = O - O_first_order
    # Check interior elements
    interior_offdiag = ~np.eye(L, dtype=bool)
    interior_offdiag[0, :] = False
    interior_offdiag[-1, :] = False
    interior_offdiag[:, 0] = False
    interior_offdiag[:, -1] = False

    rel_error = np.abs(O_diff[interior_offdiag]) / (np.abs(O[interior_offdiag]) + 1e-15)
    print(f"\n=== Check 2: First-order approximation O = -h*(D_j-D_i)/gamma_phi ===")
    print(f"Mean |O - O_1st| / |O| for interior: {np.mean(rel_error):.4f}")
    print(f"Max |O - O_1st| / |O| for interior: {np.max(rel_error):.4f}")

    # === Check 3: Occupation profile and its gradient ===
    diag_D = np.diag(D)
    gradient = np.diff(diag_D)

    print(f"\n=== Check 3: Occupation profile ===")
    print(f"D_1 = {diag_D[0]:.6f}, D_L = {diag_D[-1]:.6f}, Delta D = {diag_D[0]-diag_D[-1]:.6f}")
    print(f"Midpoint gradient D_{L//2+1} - D_{L//2} = {gradient[L//2-1]:.6e}")

    # Check if D satisfies fractional diffusion equation
    # Sum_j (D_j - D_i)/|i-j|^{2alpha} should be ~0 for interior
    FD_residual = np.zeros(L)
    for i in range(1, L-1):  # interior sites
        for j in range(L):
            if i != j:
                r = abs(i - j)
                FD_residual[i] += (diag_D[j] - diag_D[i]) / (r ** (2*alpha))

    print(f"\n=== Check 4: Fractional diffusion equation ===")
    print(f"FD residual (interior): max = {np.max(np.abs(FD_residual[1:-1])):.2e}")
    print(f"FD residual at midpoint: {FD_residual[L//2-1]:.2e}")

    # === Check 5: Relationship between C_mid and gradient ===
    mid_i = L // 2 - 1
    mid_j = L // 2
    C_mid = C[mid_i, mid_j]
    grad_mid = diag_D[mid_j] - diag_D[mid_i]
    h_mid = h[mid_i, mid_j].real

    # First-order: C_mid ~ -i h_mid * grad_mid / gamma_phi
    C_mid_1st = -1j * h_mid * grad_mid / gamma_phi
    print(f"\n=== Check 5: C_mid vs gradient ===")
    print(f"C_mid (exact) = {C_mid:.10f}")
    print(f"C_mid (1st)   = {C_mid_1st:.10f}")
    print(f"Ratio |C_exact/C_1st| = {np.abs(C_mid/C_mid_1st):.6f}")
    print(f"Phase diff (deg) = {np.angle(C_mid/C_mid_1st)*180/np.pi:.4f}")

    # === Check 6: Higher-order contributions ===
    # C = D + iO
    # [h, D + iO] = [h, D] + i[h, O]
    # i[h, D+iO] = i[h, D] - [h, O]
    # i[h,D] contributes to O (imaginary off-diagonal)
    # -[h,O] contributes to D (real diagonal) and real off-diagonal

    # Check [h, O]_{ii} for interior sites
    hO_comm = h @ O - O @ h  # [h, O]
    diag_hO = np.diag(hO_comm)
    print(f"\n=== Check 6: [h, O] on diagonal ===")
    print(f"[h,O] at interior diagonal: max = {np.max(np.abs(diag_hO[1:-1])):.2e}")
    print("[h,O]_mid: {:.2e}".format(diag_hO[L//2-1]))

    # Check if [h,O]_{ii} = 0 is the equation that determines D
    # For exact solution: should be 0 for interior sites (with gamma_phi correction)
    # Actually from: -[h,O]_{ii} + Gamma_i(D_i - f_i) = 0
    # For interior: -[h,O]_{ii} = 0 -> [h,O]_{ii} = 0

    print(f"\n=== Check 7: Full diagonal equation ===")
    Gamma_tot = np.zeros(L)
    Gamma_tot[0] = Gamma_L
    Gamma_tot[L-1] = Gamma_R
    for i in [0, L//2-1, L-1]:
        src = f_L if i == 0 else (f_R if i == L-1 else 0)
        val = -diag_hO[i] + Gamma_tot[i] * (diag_D[i] - src)
        print(f"Site {i}: -[h,O] + Gamma*(D-f) = {val:.2e}")

    return C, h, D, O, gradient

# Run analysis
for alpha in [1.1, 1.5, 1.9]:
    for L in [16, 32]:
        print("\n" + "="*80)
        C, h, D, O, gradient = analyze_structure(L=L, alpha=alpha, gamma_phi=0.5)

# Now do a systematic scaling analysis
print("\n" + "="*80)
print("SYSTEMATIC SCALING ANALYSIS")
print("="*80)

for gamma_phi in [0.5]:
    print(f"\ngamma_phi = {gamma_phi}")
    print(f"{'alpha':>8} {'L':>6} {'|C_mid|':>14} {'grad_mid':>14} {'ratio':>14} {'h_mid':>10}")

    for alpha in [1.1, 1.3, 1.5, 1.7, 1.9]:
        for L in [4, 8, 16, 32]:
            C, h = solve_ness(L, alpha, gamma_phi)
            mid_i = L // 2 - 1
            mid_j = L // 2
            C_mid = C[mid_i, mid_j]
            D = np.diag(C.real)
            grad_mid = D[mid_j] - D[mid_i]
            h_mid = h[mid_i, mid_j].real

            # The ratio C_mid / (-i h_mid grad_mid / gamma_phi)
            denom = h_mid * abs(grad_mid) / gamma_phi
            ratio_val = np.abs(C_mid) / denom if denom > 1e-15 else 0

            print("{:>8.1f} {:>6d} {:>14.6e} {:>14.6e} {:>14.6f} {:>10.6f}".format(
                alpha, L, np.abs(C_mid), grad_mid, ratio_val, h_mid))

# Check if the occupation gradient itself satisfies a simple scaling
print("\n" + "="*80)
print("OCCUPATION GRADIENT SCALING")
print("="*80)

for gamma_phi in [0.5]:
    print("\ngamma_phi = {}: grad_mid ~ L^{{-nu}}".format(gamma_phi))
    header = "{:>8s} {:>14s} {:>14s} {:>14s} {:>14s} {:>10s}".format(
        'alpha', 'L=4', 'L=8', 'L=16', 'L=32', 'nu')
    print(header)

    for alpha in [1.1, 1.3, 1.5, 1.7, 1.9]:
        grads = []
        for L in [4, 8, 16, 32]:
            C, h = solve_ness(L, alpha, gamma_phi)
            mid_i = L // 2 - 1
            mid_j = L // 2
            D = np.diag(C.real)
            grad_mid = D[mid_j] - D[mid_i]
            grads.append(grad_mid)

        # Log-log fit
        Ls = np.array([4, 8, 16, 32])
        logL = np.log(Ls)
        logG = np.log(np.abs(grads))
        slope = -np.polyfit(logL, logG, 1)[0]

        print(f"{alpha:>8.1f} {grads[0]:>14.6e} {grads[1]:>14.6e} {grads[2]:>14.6e} {grads[3]:>14.6e} {slope:>10.4f}")

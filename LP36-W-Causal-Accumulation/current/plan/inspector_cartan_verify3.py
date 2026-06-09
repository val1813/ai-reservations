"""
CRITICAL CHECK: Do sigmaI-vanishing configurations actually give A1=mu*A0?
And more systematic search for A1=mu*A0 solutions with non-zero |c1|, |c2|.
"""
import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize, differential_evolution

sx = np.array([[0,1],[1,0]], dtype=complex)
sy = np.array([[0,-1j],[1j,0]], dtype=complex)
sz = np.array([[1,0],[0,-1]], dtype=complex)
I2 = np.eye(2, dtype=complex)
pauli_1q = [I2, sx, sy, sz]

def build_H1(c1):
    H = np.zeros((8,8), dtype=complex)
    for k in range(3):
        H += c1[k] * np.kron(np.kron(pauli_1q[k+1], pauli_1q[k+1]), I2)
    return H

def build_H2(c2):
    H = np.zeros((8,8), dtype=complex)
    for k in range(3):
        H += c2[k] * np.kron(np.kron(I2, pauli_1q[k+1]), pauli_1q[k+1])
    return H

def compute_Aa(c1, c2, gamma0, gamma1, a):
    H1 = build_H1(c1)
    H2 = build_H2(c2)
    D1 = expm(1j * H1)
    D2 = expm(1j * H2)
    U = D2 @ D1
    gamma_tilde = np.array([np.sqrt(gamma0), np.sqrt(gamma1)], dtype=complex)
    A = np.zeros((4,4), dtype=complex)
    for qa in range(2):
        for qb in range(2):
            for qap in range(2):
                for qbp in range(2):
                    bra_idx = qa*4 + a*2 + qb
                    total = 0
                    for e1 in range(2):
                        ket_idx = qap*4 + e1*2 + qbp
                        total += gamma_tilde[e1] * U[bra_idx, ket_idx]
                    A[qa*2+qb, qap*2+qbp] = total
    return A

gamma0, gamma1 = 0.7, 0.3
mu = np.sqrt(gamma1 / gamma0)

def check_A1_equals_muA0(c1, c2):
    A0 = compute_Aa(c1, c2, gamma0, gamma1, 0)
    A1 = compute_Aa(c1, c2, gamma0, gamma1, 1)
    return np.max(np.abs(A1 - mu * A0))

# ============================================================
# Check the sigmaI-vanishing points found earlier
# ============================================================
print("=" * 80)
print("CHECK: Do sigmaI-vanishing points satisfy A1=mu*A0?")
print("=" * 80)

sigmaI_zero_points = [
    ([1.5117, 1.6491, 1.5361], [1.5708, -3.1416, -0.2457]),
    ([2.6710, 0.9312, -0.8070], [2.8680, 1.5708, -3.1416]),
    ([-1.5708, 1.5708, 1.5708], [0.1349, 0.0245, 1.5710]),
    ([1.5708, -1.5708, 1.5708], [-1.6149, 0.2048, 0.2044]),
    ([-1.5708, -1.5708, -1.5708], [-0.2207, -2.7121, 2.7888]),
    ([0.0000, -3.1416, 3.1416], [-1.5170, 0.1974, 0.2678]),
]

print(f"\ngamma0={gamma0}, gamma1={gamma1}, mu={mu:.6f}")
for i, (c1, c2) in enumerate(sigmaI_zero_points):
    c1a = np.array(c1)
    c2a = np.array(c2)
    diff = check_A1_equals_muA0(c1a, c2a)
    c1n = np.sqrt(np.sum(c1a**2))
    c2n = np.sqrt(np.sum(c2a**2))
    print(f"\n  Point {i}: |c1|={c1n:.4f}, |c2|={c2n:.4f}")
    print(f"    c1=({c1[0]:.4f},{c1[1]:.4f},{c1[2]:.4f}), c2=({c2[0]:.4f},{c2[1]:.4f},{c2[2]:.4f})")
    print(f"    ||A1 - mu*A0||_max = {diff:.4e}")
    if diff < 1e-6:
        print(f"    *** COUNTEREXAMPLE: A1 = mu*A0 with non-zero Cartan coefficients! ***")

# Check specific Cartan values more systematically
print("\n" + "=" * 80)
print("SYSTEMATIC: Check Cartan coefficient special values")
print("=" * 80)

# The Cartan domain is [0, pi/4] (after Weyl fixing)
# Check all combinations of 0 and pi/2 for each coefficient
special_vals = [0.0, np.pi/4, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
print("\n  Special value combinations:")
for ax in special_vals:
    for ay in special_vals:
        for az in special_vals:
            c1 = np.array([ax, ay, az])
            c2 = np.array([ax, ay, az])  # symmetric case
            c1n = np.sqrt(np.sum(c1**2))
            diff = check_A1_equals_muA0(c1, c2)
            if diff < 1e-8:
                print(f"    c1=c2=({ax/np.pi:.2f}pi,{ay/np.pi:.2f}pi,{az/np.pi:.2f}pi): diff={diff:.2e}, |c1|={c1n:.4f}")

# Check asymmetric c1, c2
print("\n  Asymmetric cases (c1 fixed, c2 varied):")
for ax in [0.0, np.pi/2, np.pi]:
    c1 = np.array([ax, 0.0, 0.0])
    for bx in [0.0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]:
        c2 = np.array([bx, 0.0, 0.0])
        diff = check_A1_equals_muA0(c1, c2)
        if diff < 1e-8:
            print(f"    c1=({ax/np.pi:.2f}pi,0,0), c2=({bx/np.pi:.2f}pi,0,0): diff={diff:.2e}")

# ============================================================
# GLOBAL OPTIMIZATION for counterexamples
# ============================================================
print("\n" + "=" * 80)
print("GLOBAL OPTIMIZATION: Minimize ||A1 - mu*A0||")
print("=" * 80)

def objective_global(params):
    c1 = params[:3]
    c2 = params[3:]
    # Add penalty to push away from zero
    c1_norm = np.sqrt(np.sum(c1**2))
    c2_norm = np.sqrt(np.sum(c2**2))
    diff = check_A1_equals_muA0(c1, c2)
    # We want to minimize diff while keeping norms non-negligible
    # Use barrier approach: minimize diff + tiny penalty for small norms
    return diff + 1e-6 / (c1_norm + c2_norm + 1e-6)

# Run many random starts with Nelder-Mead
np.random.seed(42)
best_overall = float('inf')
best_params = None
for trial in range(100):
    x0 = np.random.uniform(-3.0, 3.0, 6)
    result = minimize(objective_global, x0, method='Nelder-Mead',
                     options={'maxiter': 10000, 'xatol': 1e-14, 'fatol': 1e-14})
    c1_n = np.sqrt(np.sum(result.x[:3]**2))
    c2_n = np.sqrt(np.sum(result.x[3:]**2))
    if c1_n + c2_n > 0.1 and result.fun < best_overall:
        best_overall = result.fun
        best_params = result.x.copy()
    if trial < 5 or (c1_n + c2_n > 0.1 and result.fun < 1e-6):
        actual_diff = check_A1_equals_muA0(result.x[:3], result.x[3:])
        print(f"  Start {trial}: diff={actual_diff:.4e}, |c1|={c1_n:.4f}, |c2|={c2_n:.4f}")

print(f"\n  Best overall: diff={best_overall:.4e}, |c1|={np.sqrt(np.sum(best_params[:3]**2)):.4f}, |c2|={np.sqrt(np.sum(best_params[3:]**2)):.4f}")

# ============================================================
# Also check: does A1 = mu*A0 impose conditions beyond sigmaI sector?
# ============================================================
print("\n" + "=" * 80)
print("ANALYSIS: Full A1 = mu*A0 condition decomposition")
print("=" * 80)

# Pick a generic non-zero c1, c2
c1_test = np.array([0.5, 0.3, 0.2])
c2_test = np.array([0.4, 0.1, 0.3])
A0 = compute_Aa(c1_test, c2_test, gamma0, gamma1, 0)
A1 = compute_Aa(c1_test, c2_test, gamma0, gamma1, 1)

print(f"\n  c1 = ({c1_test[0]:.4f},{c1_test[1]:.4f},{c1_test[2]:.4f}), c2 = ({c2_test[0]:.4f},{c2_test[1]:.4f},{c2_test[2]:.4f})")
print(f"  ||A1 - mu*A0||_max = {np.max(np.abs(A1 - mu*A0)):.4e}")

# Decompose A1 - mu*A0 in Pauli basis
pauli_labels = ['II','IX','IY','IZ','XI','XX','XY','XZ','YI','YX','YY','YZ','ZI','ZX','ZY','ZZ']
pauli_basis_4x4 = []
for i in range(4):
    for j in range(4):
        pauli_basis_4x4.append(np.kron(pauli_1q[i], pauli_1q[j]))

diff_mat = A1 - mu * A0
print("\n  Pauli decomposition of A1 - mu*A0:")
for i, label in enumerate(pauli_labels):
    c = np.trace(pauli_basis_4x4[i].conj().T @ diff_mat) / 4.0
    if abs(c) > 1e-8:
        print(f"    {label}: {c:.6e}")

# Critical question: does each sector independently force zero?
# Check: if we fix sigmaI=0 (by choosing appropriate c), are other sectors forced to zero?
print("\n" + "=" * 80)
print("CRITICAL: Does sigmaI=0 force full A1=mu*A0?")
print("=" * 80)

def objective_full(params):
    """Minimize max norm of A1 - mu*A0"""
    c1 = params[:3]
    c2 = params[3:]
    return check_A1_equals_muA0(c1, c2)

# Restrict to sigmaI=0 configurations and check full diff
print("\n  From sigmaI=0 configurations, checking full A1-mu*A0:")
for i, (c1_v, c2_v) in enumerate(sigmaI_zero_points):
    c1a = np.array(c1_v)
    c2a = np.array(c2_v)
    diff = check_A1_equals_muA0(c1a, c2a)
    A0 = compute_Aa(c1a, c2a, gamma0, gamma1, 0)
    # Check sigmaI sector specifically
    sigI_coeffs = []
    for i_p, label in enumerate(pauli_labels):
        if label in ['XI','YI','ZI']:
            c = np.trace(pauli_basis_4x4[i_p].conj().T @ A0) / 4.0
            sigI_coeffs.append(abs(c))
    print(f"  Point {i}: sigmaI_max={max(sigI_coeffs):.2e}, full_diff={diff:.4e}")

print("\n" + "=" * 80)
print("COMPLETE")
print("=" * 80)

"""
INSPECTOR deep verification: Systematic search for counterexamples
and detailed coefficient structure analysis.
"""
import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize

sx = np.array([[0,1],[1,0]], dtype=complex)
sy = np.array([[0,-1j],[1j,0]], dtype=complex)
sz = np.array([[1,0],[0,-1]], dtype=complex)
I2 = np.eye(2, dtype=complex)
pauli_1q = [I2, sx, sy, sz]

def build_H1(c1):
    H = np.zeros((8,8), dtype=complex)
    pauli = [sx, sy, sz]
    for k in range(3):
        H += c1[k] * np.kron(np.kron(pauli[k], pauli[k]), I2)
    return H

def build_H2(c2):
    H = np.zeros((8,8), dtype=complex)
    pauli = [sx, sy, sz]
    for k in range(3):
        H += c2[k] * np.kron(np.kron(I2, pauli[k]), pauli[k])
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

# Pauli basis for 4x4
pauli_labels = ['II','IX','IY','IZ','XI','XX','XY','XZ','YI','YX','YY','YZ','ZI','ZX','ZY','ZZ']
pauli_basis_4x4 = []
for i in range(4):
    for j in range(4):
        pauli_basis_4x4.append(np.kron(pauli_1q[i], pauli_1q[j]))

def decompose_pauli(M):
    coeffs = {}
    for i, label in enumerate(pauli_labels):
        coeffs[label] = np.trace(pauli_basis_4x4[i].conj().T @ M) / 4.0
    return coeffs

gamma0, gamma1 = 0.7, 0.3
mu = np.sqrt(gamma1 / gamma0)

# ============================================================
# Systematic search for counterexamples
# ============================================================
print("=" * 80)
print("SYSTEMATIC COUNTEREXAMPLE SEARCH")
print("=" * 80)

def check_A1_equals_muA0(c1, c2):
    A0 = compute_Aa(c1, c2, gamma0, gamma1, 0)
    A1 = compute_Aa(c1, c2, gamma0, gamma1, 1)
    diff = np.max(np.abs(A1 - mu * A0))
    return diff

# Search 1: Collinear c1, c2 (all point in same Cartan direction)
print("\n--- Search 1: Collinear c1, c2 ---")
for direction, name in enumerate(['x','y','z']):
    for a_val in np.linspace(0.1, np.pi/2, 10):
        for b_val in np.linspace(0.1, np.pi/2, 10):
            c1 = np.zeros(3); c1[direction] = a_val
            c2 = np.zeros(3); c2[direction] = b_val
            diff = check_A1_equals_muA0(c1, c2)
            if diff < 1e-8:
                print(f"  FOUND: direction={name}, c1_{name}={a_val:.4f}, c2_{name}={b_val:.4f}, diff={diff:.2e}")
print("  Search complete.")

# Search 2: Small perturbations
print("\n--- Search 2: Small perturbations (1000 random) ---")
np.random.seed(9999)
best_diff = float('inf')
best_c1 = best_c2 = None
for trial in range(1000):
    c1 = np.random.uniform(-np.pi/2, np.pi/2, 3)
    c2 = np.random.uniform(-np.pi/2, np.pi/2, 3)
    diff = check_A1_equals_muA0(c1, c2)
    if diff < best_diff:
        best_diff = diff
        best_c1 = c1.copy()
        best_c2 = c2.copy()
print(f"  Best: diff={best_diff:.4e}, c1=({best_c1[0]:.4f},{best_c1[1]:.4f},{best_c1[2]:.4f}), c2=({best_c2[0]:.4f},{best_c2[1]:.4f},{best_c2[2]:.4f})")

# Search 3: Optimization to find minimum
print("\n--- Search 3: Optimization (gradient descent from random starts) ---")
def objective(params):
    c1 = params[:3]
    c2 = params[3:]
    return check_A1_equals_muA0(c1, c2)

for start_idx in range(20):
    x0 = np.random.uniform(-1.0, 1.0, 6)
    result = minimize(objective, x0, method='Nelder-Mead', options={'maxiter': 5000, 'xatol': 1e-12, 'fatol': 1e-12})
    if start_idx < 5 or result.fun < 1e-6:
        c1_opt = result.x[:3]
        c2_opt = result.x[3:]
        print(f"  Start {start_idx}: diff={result.fun:.4e}, c1=({c1_opt[0]:.4f},{c1_opt[1]:.4f},{c1_opt[2]:.4f}), c2=({c2_opt[0]:.4f},{c2_opt[1]:.4f},{c2_opt[2]:.4f})")

# ============================================================
# DETAILED STRUCTURE ANALYSIS
# ============================================================
print("\n" + "=" * 80)
print("DETAILED STRUCTURE: Where do sigma_l x I contributions come from?")
print("=" * 80)

# Check: with c1 = (a, 0, 0), what sigma_l x I terms appear?
print("\n--- c1 = (a, 0, 0) pure X ---")
for a_val in [0.1, 0.3, 0.5, 0.7]:
    c1 = np.array([a_val, 0.0, 0.0])
    c2 = np.array([0.2, 0.2, 0.2])
    A0 = compute_Aa(c1, c2, gamma0, gamma1, 0)
    coeffs = decompose_pauli(A0)
    print(f"  a={a_val:.1f}: XI={coeffs['XI']:.4e}, YI={coeffs['YI']:.4e}, ZI={coeffs['ZI']:.4e}")

print("\n--- c1 = (a, b, 0) with fixed a, varying b ---")
for b_val in [0.0, 0.2, 0.4, 0.6]:
    c1 = np.array([0.3, b_val, 0.0])
    c2 = np.array([0.2, 0.2, 0.2])
    A0 = compute_Aa(c1, c2, gamma0, gamma1, 0)
    coeffs = decompose_pauli(A0)
    print(f"  b={b_val:.1f}: XI={coeffs['XI']:.4e}, YI={coeffs['YI']:.4e}, ZI={coeffs['ZI']:.4e}")

# Does the cross-term from c1_y affect XI?
# In H1^2: c1_x c1_y sigma_x sigma_y = c1_x c1_y * i sigma_z -- this gives ZI
# In H1^3: c1_x c1_y c1_z sigma_x sigma_y sigma_z = c1_x c1_y c1_z * (i sigma_z) sigma_z * ...
# hmm, actually the cross-contributions are complex.

# Check: which H1^n terms contribute sigma_x on Q_a?
print("\n--- Contribution analysis: H1^n terms ---")
c1_test = np.array([0.3, 0.4, 0.5])
H1 = build_H1(c1_test)
D1 = expm(1j * H1)
# Check: what sigma_l x I terms appear in D1 alone (without D2, without E1 projection)?
# This is checking the Q_a operator structure after partial trace over E1
# Tr_E1(D1) = sum of terms in Pauli expansion with I on E1

print(f"\n  c1 = ({c1_test[0]:.2f},{c1_test[1]:.2f},{c1_test[2]:.2f})")
# D1 on Q_a x E1 (4x4). Take partial trace over E1:
D1_4x4 = expm(1j * sum(c1_test[k] * np.kron(pauli_1q[k+1], pauli_1q[k+1]) for k in range(3)))
# Partial trace over second qubit (E1): Tr_E1(D1)
rho_Qa = np.zeros((2,2), dtype=complex)
for e1 in range(2):
    for qa in range(2):
        for qap in range(2):
            rho_Qa[qa, qap] += D1_4x4[qa*2+e1, qap*2+e1]
# Decompose rho_Qa in Pauli basis
print(f"  Tr_E1(D1) on Q_a: I={np.trace(rho_Qa)/2:.4e}, X={np.trace(sx@rho_Qa)/2:.4e}, Y={np.trace(sy@rho_Qa)/2:.4e}, Z={np.trace(sz@rho_Qa)/2:.4e}")

# Now include E1 projection: <0|_E1 D1 |gamma_tilde>_E1
# This is the Q_a operator from D1 alone
A0_D1only = np.zeros((2,2), dtype=complex)
gamma_tilde = np.array([np.sqrt(gamma0), np.sqrt(gamma1)], dtype=complex)
for qa in range(2):
    for qap in range(2):
        total = 0
        for e1 in range(2):
            for e1p in range(2):
                total += gamma_tilde[e1p] * D1_4x4[qa*2 + 0, qap*2 + e1p]
                # Wait, this is not right. Let me think again.
                pass

# Actually compute: <0|_E1 D1 |gamma_tilde>_E1 as a 2x2 matrix on Q_a
A0_D1 = np.zeros((2,2), dtype=complex)
for qa in range(2):
    for qap in range(2):
        total = 0
        for e1p in range(2):
            # <0, qa| D1 |qap, e1p> * <e1p|gamma_tilde>
            total += gamma_tilde[e1p] * D1_4x4[0*2 + qa, qap*2 + e1p]
        A0_D1[qa, qap] = total

# Pauli decomposition of A0_D1
print(f"  <0|_E1 D1 |gamma> on Q_a: I={np.trace(A0_D1)/2:.4e}, X={np.trace(sx@A0_D1)/2:.4e}, Y={np.trace(sy@A0_D1)/2:.4e}, Z={np.trace(sz@A0_D1)/2:.4e}")

# Compare with c1 components: c1_x=0.3, c1_y=0.4, c1_z=0.5
# The X,Y,Z coefficients should ideally be proportional to (c1_x, c1_y, c1_z)
# But let's check the exact relationship

# ============================================================
# CRITICAL TEST: Can G_l = 0 while c^(1)_l != 0?
# ============================================================
print("\n" + "=" * 80)
print("CRITICAL TEST: Can sigma_l x I sector vanish with non-zero c1?")
print("=" * 80)

def check_sigmaI_sector(c1, c2):
    """Check if sigma_l x I sector coefficients are zero for all l"""
    A0 = compute_Aa(c1, c2, gamma0, gamma1, 0)
    coeffs = decompose_pauli(A0)
    sigmaI_vals = [abs(coeffs['XI']), abs(coeffs['YI']), abs(coeffs['ZI'])]
    return max(sigmaI_vals)

# Can we find non-zero c1 such that all sigma_l x I coeffs vanish?
print("\n  Searching for c1, c2 where sigma x I vanishes...")

# Try special symmetries
# Case: c1 all equal, c2 all equal
for val in np.linspace(0.1, np.pi, 20):
    c1 = np.array([val, val, val])
    c2 = np.array([0.0, 0.0, 0.0])
    v = check_sigmaI_sector(c1, c2)
    if v < 1e-8:
        print(f"  FOUND: c1=({val:.4f},{val:.4f},{val:.4f}), c2=(0,0,0): sigmaI max={v:.2e}")

    c2 = np.array([val, val, val])
    v = check_sigmaI_sector(c1, c2)
    if v < 1e-8:
        print(f"  FOUND: c1=c2=({val:.4f},{val:.4f},{val:.4f}): sigmaI max={v:.2e}")

# Optimize to minimize sigma x I sector
print("\n  Optimizing to minimize sigma x I sector...")
def obj_sigmaI(params):
    c1 = params[:3]
    c2 = params[3:]
    return check_sigmaI_sector(c1, c2)

for start_idx in range(30):
    x0 = np.random.uniform(-np.pi, np.pi, 6)
    result = minimize(obj_sigmaI, x0, method='Nelder-Mead', options={'maxiter': 5000, 'xatol': 1e-14, 'fatol': 1e-14})
    if result.fun < 1e-4:
        c1_opt = result.x[:3]
        c2_opt = result.x[3:]
        c1_norm = np.sqrt(np.sum(c1_opt**2))
        c2_norm = np.sqrt(np.sum(c2_opt**2))
        print(f"    Start {start_idx}: sigmaI_max={result.fun:.2e}, |c1|={c1_norm:.4f}, |c2|={c2_norm:.4f}")
        if c1_norm > 0.01 or c2_norm > 0.01:
            print(f"      *** NON-TRIVIAL: c1=({c1_opt[0]:.4f},{c1_opt[1]:.4f},{c1_opt[2]:.4f}), c2=({c2_opt[0]:.4f},{c2_opt[1]:.4f},{c2_opt[2]:.4f})")

print("\n" + "=" * 80)
print("COMPLETE")
print("=" * 80)

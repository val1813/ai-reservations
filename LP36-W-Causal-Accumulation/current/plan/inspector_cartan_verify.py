"""
INSPECTOR numerical verification of B-Dr's Cartan proof.
FOCUS-1: Verify coefficient structure coeff_l^(a) ~ c^(1)_l * v_l(a)
"""
import numpy as np
from scipy.linalg import expm

# Pauli matrices
sx = np.array([[0,1],[1,0]], dtype=complex)
sy = np.array([[0,-1j],[1j,0]], dtype=complex)
sz = np.array([[1,0],[0,-1]], dtype=complex)
I2 = np.eye(2, dtype=complex)

pauli_1q = [I2, sx, sy, sz]
pauli_names_1q = ['I', 'X', 'Y', 'Z']

# Pauli basis labels for 2-qubit Q_a x Q_b
pauli_labels = ['II','IX','IY','IZ','XI','XX','XY','XZ',
                'YI','YX','YY','YZ','ZI','ZX','ZY','ZZ']

def build_pauli_basis_4x4():
    basis = []
    for i in range(4):
        for j in range(4):
            basis.append(np.kron(pauli_1q[i], pauli_1q[j]))
    return basis

pauli_basis_4x4 = build_pauli_basis_4x4()

def decompose_pauli(M):
    coeffs = {}
    for i, label in enumerate(pauli_labels):
        coeffs[label] = np.trace(pauli_basis_4x4[i].conj().T @ M) / 4.0
    return coeffs

def build_H1(c1):
    """H1 = sum_k c1_k * sigma_k^Qa x sigma_k^E1 x I^Qb (8x8)"""
    H = np.zeros((8,8), dtype=complex)
    pauli = [sx, sy, sz]
    for k in range(3):
        term = np.kron(np.kron(pauli[k], pauli[k]), I2)
        H += c1[k] * term
    return H

def build_H2(c2):
    """H2 = sum_k c2_k * I^Qa x sigma_k^E1 x sigma_k^Qb (8x8)"""
    H = np.zeros((8,8), dtype=complex)
    pauli = [sx, sy, sz]
    for k in range(3):
        term = np.kron(np.kron(I2, pauli[k]), pauli[k])
        H += c2[k] * term
    return H

def compute_Aa(c1, c2, gamma0, gamma1, a):
    """Compute A_a = <a|_E1 D2 D1 |gamma_tilde>_E1 as 4x4 matrix"""
    H1 = build_H1(c1)
    H2 = build_H2(c2)
    D1 = expm(1j * H1)
    D2 = expm(1j * H2)
    U = D2 @ D1  # 8x8 in Q_a x E1 x Q_b

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

def compute_v(gamma0, gamma1):
    """Compute v_k(a) = <a|sigma_k|gamma_tilde>"""
    gamma_tilde = np.array([np.sqrt(gamma0), np.sqrt(gamma1)], dtype=complex)
    v = {}
    pauli = [sx, sy, sz]
    names = ['x','y','z']
    for a in [0, 1]:
        v[a] = {}
        for k, name in enumerate(names):
            v[a][name] = np.sum(pauli[k][a,:] * gamma_tilde)
    return v

def verify_closed_form(c, tol=1e-10):
    """Verify D = exp(iH) equals cos|c|*I + i*(sin|c|/|c|)*H"""
    H = sum(c[k]*np.kron(pauli_1q[k+1], pauli_1q[k+1]) for k in range(3))
    D_exact = expm(1j * H)
    cn = np.sqrt(np.sum(c**2))
    if cn < 1e-12:
        D_closed = np.eye(4, dtype=complex)
    else:
        D_closed = np.cos(cn) * np.eye(4) + 1j * np.sin(cn)/cn * H
    diff = np.max(np.abs(D_exact - D_closed))
    H2 = H @ H
    is_scalar = np.max(np.abs(H2 - cn**2 * np.eye(4))) < 1e-10
    return diff < tol, diff, is_scalar

print("=" * 80)
print("INSPECTOR: Numerical Verification of Cartan Proof")
print("=" * 80)

# 0. Verify Lemma 0 (H^2 = |c|^2 I?)
print("\n--- 0. VERIFY LEMMA 0 (H^2 = |c|^2 I?) ---")
test_cases = [
    np.array([0.3, 0.0, 0.0]),
    np.array([0.0, 0.3, 0.0]),
    np.array([0.0, 0.0, 0.3]),
    np.array([0.3, 0.4, 0.0]),
    np.array([0.3, 0.0, 0.4]),
    np.array([0.0, 0.3, 0.4]),
    np.array([0.3, 0.4, 0.5]),
    np.array([0.5, 0.5, 0.5]),
    np.array([0.1, 0.2, 0.7]),
]
for c in test_cases:
    passed, diff, is_scalar = verify_closed_form(c)
    status = "PASS" if passed else "FAIL"
    cn = np.sqrt(np.sum(c**2))
    print(f"  c=({c[0]:.3f},{c[1]:.3f},{c[2]:.3f}), |c|={cn:.3f}: {status} (diff={diff:.2e}, H^2 scaled I? {is_scalar})")

print("\n  Eigenvalue check:")
for c in [np.array([0.3,0.4,0.5])]:
    H = sum(c[k]*np.kron(pauli_1q[k+1], pauli_1q[k+1]) for k in range(3))
    eigvals = np.linalg.eigvalsh(H)
    print(f"  c=({c[0]:.3f},{c[1]:.3f},{c[2]:.3f}): eigenvalues = {eigvals}")
    print(f"    H^2 eigenvalues = {eigvals**2}")
    print(f"    |c|^2 = {np.sum(c**2):.6f}")
    print(f"    Are all H^2 eigvals equal? {np.allclose(eigvals**2, eigvals[0]**2)}")

# 1. FOCUS-1: Coefficient structure
print("\n" + "=" * 80)
print("--- FOCUS-1: Coefficient Structure in sigma_l x I sector ---")

gamma0, gamma1 = 0.7, 0.3
v = compute_v(gamma0, gamma1)
mu = np.sqrt(gamma1/gamma0)

print(f"\ngamma0={gamma0}, gamma1={gamma1}, mu={mu:.6f}")
print("\nv_k(a) table:")
for k in ['x','y','z']:
    r = v[1][k] / v[0][k]
    print(f"  k={k}: v_k(0)={v[0][k]:.8f}, v_k(1)={v[1][k]:.8f}, ratio={r:.8f}")

print(f"\nmu = {mu:.8f}")
for k in ['x','y','z']:
    r = v[1][k] / v[0][k]
    print(f"  r_{k} = {r:.8f}, |r_{k} - mu| = {abs(r - mu):.8f}")

# Test 1: Random c1, c2
print("\n--- Test 1: Random c1, c2 (20 trials) ---")
np.random.seed(12345)
all_pass = True
for trial in range(20):
    c1 = np.random.uniform(0.1, np.pi/4, 3)
    c2 = np.random.uniform(0.1, np.pi/4, 3)

    A0 = compute_Aa(c1, c2, gamma0, gamma1, 0)
    A1 = compute_Aa(c1, c2, gamma0, gamma1, 1)

    coeffs0 = decompose_pauli(A0)
    coeffs1 = decompose_pauli(A1)

    sigmaI_labels = ['XI', 'YI', 'ZI']
    c1_names = ['x', 'y', 'z']

    trial_pass = True
    for label, cname in zip(sigmaI_labels, c1_names):
        c0 = coeffs0[label]
        c1v = coeffs1[label]

        if abs(c0) > 1e-10 and abs(c1v) > 1e-10:
            ratio = c1v / c0
            expected_ratio = v[1][cname] / v[0][cname]
            diff_r = abs(ratio - expected_ratio)
            if diff_r > 1e-10:
                all_pass = False
                trial_pass = False
                print(f"  Trial {trial}: {label}: ratio={ratio:.6f}, expected={expected_ratio:.6f}, DIFF={diff_r:.2e}")

    if trial_pass and trial < 5:
        print(f"  Trial {trial}: PASS")

if all_pass:
    print("  RESULT: All sigma x I ratios match v_l(1)/v_l(0) -- STRUCTURE CONFIRMED")
else:
    print("  RESULT: Some ratios DO NOT match -- STRUCTURE FAILS")

# Test 2: Verify proportionality to c^(1)_l specifically
print("\n--- Test 2: Verify coeff_l proportional to c^(1)_l ---")
c2_fixed = np.array([0.5, 0.3, 0.2])

for l_idx, cname in enumerate(['x', 'y', 'z']):
    print(f"\n  Varying c1_{cname}:")
    label = ['XI', 'YI', 'ZI'][l_idx]
    values = []
    c1_vals = []
    for factor in [0.0, 0.3, 0.6, 0.9, 1.2]:
        c1 = np.array([0.3, 0.3, 0.3])
        c1[l_idx] = factor
        c1_vals.append(c1[l_idx])
        A0 = compute_Aa(c1, c2_fixed, gamma0, gamma1, 0)
        coeffs0 = decompose_pauli(A0)
        values.append(abs(coeffs0[label]))

    if c1_vals[1] > 1e-10:
        ratios_check = [values[i] / c1_vals[i] if c1_vals[i] > 1e-10 else 0 for i in range(len(c1_vals))]
        print(f"    {label} coeffs: {[f'{v:.6e}' for v in values]}")
        non_zero = [(i, ratios_check[i]) for i in range(len(ratios_check)) if c1_vals[i] > 1e-10]
        if len(non_zero) >= 2:
            valid_r = [r[1] for r in non_zero]
            ratio_spread = max(valid_r) - min(valid_r)
            base_ratio = abs(valid_r[0])
            rel_spread = ratio_spread / base_ratio if base_ratio > 1e-10 else ratio_spread
            status = "PASS" if rel_spread < 0.05 else f"CHECK (rel spread={rel_spread:.4f})"
            print(f"    Proportionality: {status}")

# Test 3: Cross-l factor comparison
print("\n--- Test 3: Cross-l factorization ---")
c1 = np.array([0.2, 0.3, 0.4])
c2 = np.array([0.15, 0.25, 0.35])

A0 = compute_Aa(c1, c2, gamma0, gamma1, 0)
A1 = compute_Aa(c1, c2, gamma0, gamma1, 1)
coeffs0 = decompose_pauli(A0)
coeffs1 = decompose_pauli(A1)

print(f"  c1 = ({c1[0]:.4f}, {c1[1]:.4f}, {c1[2]:.4f})")
print(f"  c2 = ({c2[0]:.4f}, {c2[1]:.4f}, {c2[2]:.4f})")
print(f"\n  Sigma x I sector coefficients:")
sigmaI_labels = ['XI', 'YI', 'ZI']
c1_names = ['x', 'y', 'z']

ratios_check = []
for label, cname in zip(sigmaI_labels, c1_names):
    l_idx = c1_names.index(cname)
    c0 = coeffs0[label]
    c1v = coeffs1[label]
    r0 = c0 / (c1[l_idx] * v[0][cname])
    r1 = c1v / (c1[l_idx] * v[1][cname])
    print(f"  {label}: coeff0={c0:.6e}, coeff1={c1v:.6e}")
    print(f"    coeff0/(c1_{cname}*v_{cname}(0)) = {r0}")
    print(f"    coeff1/(c1_{cname}*v_{cname}(1)) = {r1}")

    if abs(r0 - r1) / max(abs(r0), abs(r1), 1e-15) < 1e-10:
        print(f"    Ratio match: PASS")
    else:
        print(f"    Ratio match: DIFFER (rel diff={abs(r0-r1)/max(abs(r0),abs(r1),1e-15):.2e})")
    ratios_check.append(r0)

# Are all r0 the same factor?
if len(ratios_check) >= 2:
    spread = max(abs(r - ratios_check[0]) for r in ratios_check)
    rel_spread = spread / max(abs(ratios_check[0]), 1e-15)
    status = "PASS (single common factor)" if rel_spread < 1e-10 else f"DIFFER (rel spread={rel_spread:.2e})"
    print(f"\n  Common factor across l: {status}")

# 4. DECISIVE TEST
print("\n" + "=" * 80)
print("--- FOCUS-1 DECISIVE: Does A1 = mu*A0 => c^(1) = 0? ---")
print("(Using correct matrix exponential)")

def check_A1_equals_muA0(c1, c2):
    A0 = compute_Aa(c1, c2, gamma0, gamma1, 0)
    A1 = compute_Aa(c1, c2, gamma0, gamma1, 1)
    diff = np.max(np.abs(A1 - mu * A0))
    return diff < 1e-10, diff

c1_zero = np.zeros(3)
c2_zero = np.zeros(3)
pass_zero, diff_zero = check_A1_equals_muA0(c1_zero, c2_zero)
print(f"\n  c1=c2=0: A1=mu*A0? {pass_zero} (diff={diff_zero:.2e})")

print("\n  Testing non-zero random coefficients:")
found_counter = False
for trial in range(50):
    c1 = np.random.uniform(0.05, np.pi/6, 3)
    c2 = np.random.uniform(0.05, np.pi/6, 3)
    passed, diff_v = check_A1_equals_muA0(c1, c2)
    if trial < 10 or passed:
        print(f"    Trial {trial}: c1=({c1[0]:.4f},{c1[1]:.4f},{c1[2]:.4f}), c2=({c2[0]:.4f},{c2[1]:.4f},{c2[2]:.4f}): A1=mu*A0? {passed} (diff={diff_v:.2e})")
    if passed:
        found_counter = True
        print(f"      *** COUNTEREXAMPLE: non-zero c give A1=mu*A0 ***")
        break

if not found_counter:
    print("  RESULT: No counterexample found -- A1=mu*A0 requires c^(1)=c^(2)=0")
else:
    print("  RESULT: Counterexample EXISTS -- the proof has a gap")

# 5. Test B-Dr's SA-2: the magic basis structure
print("\n" + "=" * 80)
print("--- MAGIC BASIS ANALYSIS ---")
print("(Verifying SA-2: D_i diagonalization structure)")

# Magic basis for Q_a x E1 pair
# |Phi+> = (|00>+|11>)/sqrt(2), |Phi-> = (|00>-|11>)/sqrt(2)
# |Psi+> = (|01>+|10>)/sqrt(2), |Psi-> = (|01>-|10>)/sqrt(2)
magic_basis_2q = np.zeros((4,4), dtype=complex)
magic_basis_2q[:, 0] = np.array([1,0,0,1]) / np.sqrt(2)    # |Phi+>
magic_basis_2q[:, 1] = np.array([1,0,0,-1]) / np.sqrt(2)   # |Phi->
magic_basis_2q[:, 2] = np.array([0,1,1,0]) / np.sqrt(2)    # |Psi+>
magic_basis_2q[:, 3] = np.array([0,1,-1,0]) / np.sqrt(2)   # |Psi->

# Verify that sigma_k x sigma_k are diagonal in magic basis
for k, name in enumerate(['x','y','z']):
    sigma_k = pauli_1q[k+1]
    op = np.kron(sigma_k, sigma_k)
    op_magic = magic_basis_2q.conj().T @ op @ magic_basis_2q
    is_diag = np.max(np.abs(op_magic - np.diag(np.diag(op_magic)))) < 1e-10
    print(f"  sigma_{name} x sigma_{name} diagonal in magic basis? {is_diag}")
    if is_diag:
        print(f"    eigenvalues: {np.diag(op_magic)}")

print("\n" + "=" * 80)
print("VERIFICATION COMPLETE")
print("=" * 80)

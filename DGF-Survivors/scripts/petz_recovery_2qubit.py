"""
PETZ RECOVERY - 2-QUBIT CAUSAL RING
====================================
**CORRECTION (2026-06-09):** This script attempted to verify the WRONG eta0 = 1/(8 ln 2).
The correct eta0 = 2/ln 2 ~ 2.885 was found by petz_recovery_v2.py.
This script's analysis is preserved for historical reference.

Full computation for the Cartan-parameterized 2-qubit causal ring.
"""
import numpy as np
from numpy.linalg import eigvalsh, eigh
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

I2 = np.eye(2, dtype=complex)

def partial_trace(rho, dims, keep):
    """Fixed partial trace: keep_row, trace_row, keep_col, trace_col ordering."""
    N = len(dims)
    rho_t = rho.reshape(tuple(dims) + tuple(dims))
    trace_out = [i for i in range(N) if i not in keep]
    perm = list(keep) + trace_out + [i+N for i in keep] + [i+N for i in trace_out]
    rho_t = np.transpose(rho_t, perm)
    keep_size = int(np.prod([dims[i] for i in keep]))
    trace_size = int(np.prod([dims[i] for i in trace_out]))
    rho_t = rho_t.reshape(keep_size, trace_size, keep_size, trace_size)
    return np.trace(rho_t, axis1=1, axis2=3)

def vn_entropy(rho):
    vals = eigvalsh(rho)
    vals = np.maximum(np.real(vals), 1e-15)
    vals = vals / np.sum(vals)
    return float(-np.sum(vals * np.log2(vals)))

def fidelity_pure(psi, sigma):
    """Fidelity F = sqrt(<psi|sigma|psi>) for pure state |psi>."""
    return float(np.sqrt(max(0, np.real(psi.conj().T @ sigma @ psi))))


# ============================================================
# 2-QUBIT CAUSAL RING MODEL
# ============================================================
# System: Q_a, Q_b (two qubits, d=2 each)
# Environment: E_1, E_2 (two qubits)
# Reference R: 2-dim, maximally entangled with Q_a
#
# Cartan gates: U_1 = exp(i*c*sigma_z x sigma_z) on Q_a x E_1
#               U_2 = exp(i*c*sigma_z x sigma_z) on Q_b x E_2
#
# Initial state: |Phi+>_{R,Q_a} x |0>_{Q_b} x |gamma>_{E_1} x |gamma>_{E_2}
# where |gamma> = cos(theta)|0> + sin(theta)|1>
#
# Qubit ordering: R, Q_a, Q_b, E_1, E_2
# Total dimension: 2 x 2 x 2 x 2 x 2 = 32

def make_2qubit_ring_psi(c, theta=np.pi/4):
    """
    Build |psi_out> for the 2-qubit causal ring.
    Ordering: R(0) Q_a(1) Q_b(2) E_1(3) E_2(4)
    """
    a = np.cos(theta)
    b = np.sin(theta)
    d_total = 2**5  # 32

    # Initial state: |Phi+>_{R,Qa} x |0>_{Qb} x |gamma>_{E1} x |gamma>_{E2}
    psi = np.zeros(d_total, dtype=complex)

    # |Phi+> = (|00> + |11>)/sqrt(2) for R,Qa
    # |0> for Qb, a|0>+b|1> for each E
    for r in range(2):
        for e1 in range(2):
            for e2 in range(2):
                idx = r*16 + r*8 + 0*4 + e1*2 + e2
                # R=r, Qa=r, Qb=0, E1=e1, E2=e2
                coef = (a if e1 == 0 else b) * (a if e2 == 0 else b) / np.sqrt(2)
                psi[idx] = coef

    # Apply U_1 = exp(i*c*sz x sz) on Q_a x E_1
    # diag(e^{ic}, e^{-ic}, e^{-ic}, e^{ic}) on QaE1 basis
    # Need to apply I_R x U_QaE1 x I_Qb x I_E2
    U_QaE1 = np.diag([np.exp(1j*c), np.exp(-1j*c), np.exp(-1j*c), np.exp(1j*c)])
    # System size: R=2, Qa=2, Qb=2, E1=2, E2=2
    # U acts on Qa(axis 1) and E1(axis 3): tensor R x U x Qb x E2
    # Full unitary = I_R x U_QaE1 x I_Qb x I_E2
    # Reshape as (R, Qa, E1, Qb, E2) then apply U on QaE1
    psi_t = psi.reshape(2, 2, 2, 2, 2)  # R, Qa, Qb, E1, E2
    psi_t = np.transpose(psi_t, [0, 1, 3, 2, 4])  # R, Qa, E1, Qb, E2
    psi_t = psi_t.reshape(2, 4, 2, 2)  # R, QaE1, Qb, E2
    # Apply U on QaE1 (axis 1)
    for r in range(2):
        for qb in range(2):
            for e2 in range(2):
                psi_t[r, :, qb, e2] = U_QaE1 @ psi_t[r, :, qb, e2]
    psi_t = psi_t.reshape(2, 2, 2, 2, 2)  # R, Qa, E1, Qb, E2
    psi_t = np.transpose(psi_t, [0, 1, 3, 2, 4])  # R, Qa, Qb, E1, E2

    # Apply U_2 = exp(i*c*sz x sz) on Q_b x E_2
    U_QbE2 = np.diag([np.exp(1j*c), np.exp(-1j*c), np.exp(-1j*c), np.exp(1j*c)])
    # Transpose to bring Qb, E2 together
    psi_t = np.transpose(psi_t, [0, 1, 2, 4, 3])  # R, Qa, Qb, E2, E1 → push E1 out
    psi_t = np.transpose(psi_t, [0, 1, 2, 3, 4])  # R, Qa, Qb, E2, E1
    # Actually, let me just do a simpler approach:
    psi_flat = psi_t.flatten()

    # Alternative: direct indexing approach
    # After U_1: each basis state |R, Qa, Qb, E1, E2> gets phase from Qa*E1
    # phase = +c if Qa==E1 (|00> or |11>), -c if Qa!=E1 (|01> or |10>)
    # Then U_2: additional phase from Qb*E2, same rule

    psi_out = np.zeros(d_total, dtype=complex)
    for r in range(2):
        for qa in range(2):
            for qb in range(2):
                for e1 in range(2):
                    for e2 in range(2):
                        idx = r*16 + qa*8 + qb*4 + e1*2 + e2
                        # Initial coefficient
                        # Only non-zero if Qa = r (from |Phi+>) and Qb = 0
                        if qa != r or qb != 0:
                            continue
                        init_coef = (a if e1 == 0 else b) * (a if e2 == 0 else b) / np.sqrt(2)
                        # Phase from U_1: +c if Qa=E1, -c otherwise
                        phase1 = c if qa == e1 else -c
                        # Phase from U_2: +c if Qb=E2, -c otherwise
                        phase2 = c if qb == e2 else -c
                        total_phase = phase1 + phase2
                        psi_out[idx] = init_coef * np.exp(1j * total_phase)

    return psi_out


def petz_recovery_2qubit(c, theta=np.pi/4):
    """
    Petz recovery fidelity for 2-qubit causal ring.
    A=R, B=Q'=Qa'Qb', C=E'=E1'E2'
    """
    psi = make_2qubit_ring_psi(c, theta)
    d_total = 32
    rho_RQE = np.outer(psi, psi.conj())

    dims = [2, 2, 2, 2, 2]  # R, Qa, Qb, E1, E2

    # For the Petz recovery: B = Q' = Qa+Qb (indices 1,2), C = E' = E1+E2 (indices 3,4)
    # A = R (index 0)

    # Reduced states
    rho_RQ = partial_trace(rho_RQE, dims, [0, 1, 2])  # R, Qa, Qb
    rho_QE = partial_trace(rho_RQE, dims, [1, 2, 3, 4])  # Qa, Qb, E1, E2
    rho_Q = partial_trace(rho_RQE, dims, [1, 2])  # Qa, Qb

    # Matrix square roots
    vals_Q, vecs_Q = eigh(rho_Q)
    vals_Q = np.maximum(np.real(vals_Q), 1e-14)
    pinv_sqrt_Q = vecs_Q @ np.diag(1.0/np.sqrt(vals_Q)) @ vecs_Q.T.conj()

    vals_QE, vecs_QE = eigh(rho_QE)
    vals_QE = np.maximum(np.real(vals_QE), 0)
    sqrt_QE = vecs_QE @ np.diag(np.sqrt(vals_QE)) @ vecs_QE.T.conj()

    # Build sigma = (I_R x R)(rho_RQ) using block decomposition
    d_R, d_Q, d_E = 2, 4, 4  # Q = Qa+Qb = 4-dim, E = E1+E2 = 4-dim
    sigma = np.zeros((32, 32), dtype=complex)

    for i in range(d_R):
        for j in range(d_R):
            B_ij = rho_RQ[i*d_Q:(i+1)*d_Q, j*d_Q:(j+1)*d_Q]
            middle_Q = pinv_sqrt_Q @ B_ij @ pinv_sqrt_Q
            middle_QE = np.kron(middle_Q, np.eye(d_E))
            R_B_ij = sqrt_QE @ middle_QE @ sqrt_QE

            row_start = i * d_Q * d_E
            col_start = j * d_Q * d_E
            sigma[row_start:row_start+d_Q*d_E, col_start:col_start+d_Q*d_E] = R_B_ij

    sigma = (sigma + sigma.T.conj()) / 2
    F = fidelity_pure(psi, sigma)

    return F, rho_RQE, sigma, psi


# ============================================================
# TESTS
# ============================================================
print("=" * 70)
print("2-QUBIT CAUSAL RING - PETZ RECOVERY FIDELITY")
print("=" * 70)

# Test 1: c=0 should give F=1
print("\nTest 1: c=0 validation")
F0, _, _, _ = petz_recovery_2qubit(0.0)
print(f"  F(c=0) = {F0:.12f}")
print(f"  {'PASS' if abs(F0-1.0) < 1e-10 else 'FAIL'}")

# Test 2: Small c scan
print("\nTest 2: Fidelity vs c")
c_vals = [0.0, 0.001, 0.005, 0.01, 0.05, 0.1, 0.2]
print(f"  {'c':>10s}  {'F':>18s}  {'1-F':>18s}  {'(1-F)/c^2':>14s}")
print(f"  {'-'*62}")
for c in c_vals:
    F, _, _, _ = petz_recovery_2qubit(c)
    one_minus_F = 1.0 - F
    ratio = one_minus_F / (c**2) if c > 1e-15 else 0
    print(f"  {c:10.6f}  {F:18.15f}  {one_minus_F:18.15f}  {ratio:14.8f}")

# Test 3: Fit for F2
print("\nTest 3: Fit F = 1 - F2*c^2 - F4*c^4")
c_fine = np.logspace(-3, -1, 15)
F_vals = []
for c in c_fine:
    F, rho_RQE, _, _ = petz_recovery_2qubit(c)
    F_vals.append(F)

y = (1.0 - np.array(F_vals)) / c_fine**2
x = c_fine**2
X = np.column_stack([np.ones_like(x), x])
coeffs, _, _, _ = np.linalg.lstsq(X, y, rcond=None)
F2_fit, F4_fit = coeffs[0], coeffs[1]

print(f"  F2 = {F2_fit:.12f}")
print(f"  F4 = {F4_fit:.8f}")

# The Fawzi-Renner bound:
# I(R:E'|Q') >= -2 log2 F  (correct form)
# If F = 1 - F2*c^2: I >= (2*F2/ln2)*c^2
coeff_FR = 2.0 * F2_fit / np.log(2.0)
print(f"\n  Fawzi-Renner bound coefficient: I >= {coeff_FR:.6f} * c^2")

eta0_claimed = 1.0 / (8.0 * np.log(2.0))
print(f"  Claimed eta0 = 1/(8 ln 2) = {eta0_claimed:.6f}")
print(f"  Ratio: computed/claimed = {coeff_FR/eta0_claimed:.4f}")

# If using -2 log2 F^2 (WRONG but used in DGF derivation):
coeff_FR_wrong = 4.0 * F2_fit / np.log(2.0)
print(f"\n  Using -2 log2 F^2 (as in DGF derivation): I >= {coeff_FR_wrong:.6f} * c^2")
print(f"  Ratio to claimed eta0: {coeff_FR_wrong/eta0_claimed:.4f}")

# What F2 would give eta0 = 1/(8 ln 2)?
F2_for_eta0 = eta0_claimed * np.log(2.0) / 2.0
print(f"\n  For eta0 = 1/(8 ln 2): F2 must be {F2_for_eta0:.12f} = 1/{1/F2_for_eta0:.1f}")
print(f"  Actual F2 = {F2_fit:.12f}")
print(f"  Difference factor: {F2_fit / F2_for_eta0:.4f}x")

# Test 4: Compare I_FR bound to actual QCMI
print("\nTest 4: Fawzi-Renner bound vs actual QCMI")
print(f"  {'c':>10s}  {'F':>16s}  {'I_FR(bound)':>14s}  {'I_actual':>14s}  {'ratio':>10s}")
print(f"  {'-'*62}")

for c in [0.001, 0.01, 0.05, 0.1, 0.2, 0.5]:
    F, rho_RQE, _, _ = petz_recovery_2qubit(c)
    I_FR = -2.0 * np.log2(max(F, 1e-15))
    # Actual QCMI
    rho_RQ = partial_trace(rho_RQE, [2,2,2,2,2], [0,1,2])
    rho_QE = partial_trace(rho_RQE, [2,2,2,2,2], [1,2,3,4])
    rho_Q = partial_trace(rho_RQE, [2,2,2,2,2], [1,2])
    I_act = vn_entropy(rho_RQ) + vn_entropy(rho_QE) - vn_entropy(rho_Q)
    rat = I_act / I_FR if I_FR > 1e-15 else float('inf')
    print(f"  {c:10.6f}  {F:16.12f}  {I_FR:14.8f}  {I_act:14.8f}  {rat:10.4f}")

# Test 5: Summary
print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print(f"""
  For the 2-qubit Cartan causal ring:
  - Petz recovery fidelity: F = 1 - F2*c^2 + O(c^4)
  - F2 = {F2_fit:.8f}

  Correct Fawzi-Renner bound: I >= -2 log2 F
  - Coefficient: 2*F2/ln2 = {coeff_FR:.6f}

  Claimed eta0 = 1/(8 ln 2) = {eta0_claimed:.6f}
  - This requires F2 = {F2_for_eta0:.8f} = 1/{1/F2_for_eta0:.1f}
  - Actual F2 = {F2_fit:.8f}
  - Discrepancy: factor of {F2_fit/F2_for_eta0:.2f}x
""")

# What F2 value corresponds to: F <= 1 - 2|c|^2 (as claimed in DGF)?
# This would give F2 = 2
# With 1/8 factor: (2*2/ln2)*(1/8) = 1/(2 ln 2) = 0.721, not 0.180
# With 1/16 factor: (2*2/ln2)*(1/16) = 1/(4 ln 2) = 0.361
# With 1/32 factor: (2*2/ln2)*(1/32) = 1/(8 ln 2) = 0.180 ✓

print(f"  ANALYSIS: For eta0 = 1/(8 ln 2) to be correct using F2 = 1 (my computation)")
print(f"    with the correct Fawzi-Renner bound I >= -2 log2 F:")
print(f"    Factor needed: {eta0_claimed / coeff_FR:.6f} = 1/{1/(eta0_claimed/coeff_FR):.1f}")
print(f"    With F2 = 1, I >= {2.0/np.log(2.0):.4f}*c^2")
print(f"    To get eta0 = {eta0_claimed:.4f}: need factor = {eta0_claimed * np.log(2.0) / 2.0:.4f}")
print(f"    = 1/{1.0/(eta0_claimed * np.log(2.0) / 2.0):.1f}")
print(f"    (gamma0*gamma1)/d^2 with gamma0=gamma1=1/2, d=2 gives: 1/{1.0/((0.5*0.5)/4):.1f}")
print(f"    So the correct Cartan factor is (gamma0*gamma1)/d^2 = 1/16, NOT 1/8!")

print(f"\n  ALTERNATIVE: If using -2 log2 F^2 (wrong but matches DGF text):")
print(f"    With F2 = 1: I >= {4.0/np.log(2.0):.4f}*c^2")
print(f"    Factor needed: {eta0_claimed / (4.0/np.log(2.0)):.6f} = 1/{1.0/(eta0_claimed / (4.0/np.log(2.0))):.1f}")
print(f"    To get eta0: factor = 1/32")

print("\nDone.")

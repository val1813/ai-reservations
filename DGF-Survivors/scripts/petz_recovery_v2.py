"""
PETZ RECOVERY FIDELITY - CORRECT IMPLEMENTATION
================================================
Fixed version with proper c=0 validation.
"""
import numpy as np
from numpy.linalg import eigvalsh, eigh
import io, sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

I2 = np.eye(2, dtype=complex)
ket0 = np.array([1, 0], dtype=complex)
ket1 = np.array([0, 1], dtype=complex)


def tensor(*mats):
    r = mats[0]
    for m in mats[1:]:
        r = np.kron(r, m)
    return r


def partial_trace(rho, dims, keep):
    """Partial trace. dims = list of subsystem dimensions, keep = indices to KEEP.

    FIXED: permutation order is keep_row, trace_row, keep_col, trace_col
    to ensure reshape groups keep dims together and trace dims together.
    """
    N = len(dims)
    rho_t = rho.reshape(tuple(dims) + tuple(dims))
    trace_out = [i for i in range(N) if i not in keep]
    # Row keep, row trace, column keep, column trace
    perm = list(keep) + trace_out + [i+N for i in keep] + [i+N for i in trace_out]
    rho_t = np.transpose(rho_t, perm)
    keep_size = int(np.prod([dims[i] for i in keep]))
    trace_size = int(np.prod([dims[i] for i in trace_out]))
    rho_t = rho_t.reshape(keep_size, trace_size, keep_size, trace_size)
    rho_reduced = np.trace(rho_t, axis1=1, axis2=3)
    return rho_reduced


def vn_entropy(rho):
    vals = eigvalsh(rho)
    vals = np.maximum(np.real(vals), 1e-15)
    vals = vals / np.sum(vals)
    return float(-np.sum(vals * np.log2(vals)))


def make_cartan_output(c, theta=np.pi/4):
    """
    Build |psi_out> for 1-qubit Cartan channel:
    U = exp(i*c*sigma_z x sigma_z) on Q x E.
    Initial: |Phi+>_{RQ} x |gamma>_E.
    """
    a = np.cos(theta)
    b = np.sin(theta)

    # |Phi+> = (|00> + |11>)/sqrt(2), |gamma> = a|0> + b|1>
    # |psi_init>_RQE = a/sqrt(2)|000> + b/sqrt(2)|001> + a/sqrt(2)|110> + b/sqrt(2)|111>
    psi = np.zeros(8, dtype=complex)
    psi[0] = a / np.sqrt(2)  # |000>
    psi[1] = b / np.sqrt(2)  # |001>
    psi[6] = a / np.sqrt(2)  # |110>
    psi[7] = b / np.sqrt(2)  # |111>

    # U = diag(e^{ic}, e^{-ic}, e^{-ic}, e^{ic}) on QE
    # I_R x U_QE
    U_QE = np.diag([np.exp(1j*c), np.exp(-1j*c), np.exp(-1j*c), np.exp(1j*c)])
    I_U = np.kron(I2, U_QE)
    psi_out = I_U @ psi

    return psi_out


def petz_recovery_fidelity_correct(c, theta=np.pi/4):
    """
    Compute Petz recovery fidelity F(rho_RQE, sigma) where
    sigma = (I_R x R_{Q->QE})(rho_RQ).

    R_{Q->QE}(X_Q) = rho_QE^{1/2} * (rho_Q^{-1/2} X_Q rho_Q^{-1/2} x I_E) * rho_QE^{1/2}

    Returns (F, rho_RQE, sigma).
    """
    psi_out = make_cartan_output(c, theta)
    rho_RQE = np.outer(psi_out, psi_out.conj())

    dims = [2, 2, 2]  # R, Q, E

    # Reduced states
    rho_RQ = partial_trace(rho_RQE, dims, [0, 1])  # keep R, Q
    rho_QE = partial_trace(rho_RQE, dims, [1, 2])  # keep Q, E
    rho_Q = partial_trace(rho_RQE, dims, [1])      # keep Q

    # Matrix square roots
    vals_Q, vecs_Q = eigh(rho_Q)
    vals_Q = np.maximum(np.real(vals_Q), 1e-14)
    pinv_sqrt_vals = 1.0 / np.sqrt(vals_Q)
    pinv_sqrt_Q = vecs_Q @ np.diag(pinv_sqrt_vals) @ vecs_Q.T.conj()

    vals_QE, vecs_QE = eigh(rho_QE)
    vals_QE = np.maximum(np.real(vals_QE), 0)
    sqrt_vals_QE = np.sqrt(vals_QE)
    sqrt_QE = vecs_QE @ np.diag(sqrt_vals_QE) @ vecs_QE.T.conj()

    # Build sigma = (I_R x R)(rho_RQ) using block decomposition
    d_R, d_Q, d_E = 2, 2, 2
    sigma = np.zeros((8, 8), dtype=complex)

    for i in range(d_R):
        for j in range(d_R):
            # B_ij = <i|_R rho_RQ |j>_R, a d_Q x d_Q block
            B_ij = rho_RQ[i*d_Q:(i+1)*d_Q, j*d_Q:(j+1)*d_Q]

            # R(B_ij) = sqrt_QE @ (pinv_sqrt_Q @ B_ij @ pinv_sqrt_Q x I_E) @ sqrt_QE
            middle_Q = pinv_sqrt_Q @ B_ij @ pinv_sqrt_Q       # d_Q x d_Q
            middle_QE = np.kron(middle_Q, I2)                  # d_QE x d_QE
            R_B_ij = sqrt_QE @ middle_QE @ sqrt_QE            # d_QE x d_QE

            # Place into sigma
            row_start = i * d_Q * d_E
            col_start = j * d_Q * d_E
            sigma[row_start:row_start+d_Q*d_E, col_start:col_start+d_Q*d_E] = R_B_ij

    sigma = (sigma + sigma.T.conj()) / 2

    # Fidelity F(rho_RQE, sigma) = sqrt(<psi| sigma |psi>) for pure rho_RQE
    F = np.sqrt(max(0, np.real(psi_out.conj().T @ sigma @ psi_out)))

    return F, rho_RQE, sigma, rho_RQ, rho_QE, rho_Q


# ============================================================
# TEST 1: c=0 should give F=1 (Markov chain state)
# ============================================================
print("=" * 70)
print("TEST 1: c=0 validation (should have F=1)")
print("=" * 70)

F0, rho_RQE, sigma, rho_RQ, rho_QE, rho_Q = petz_recovery_fidelity_correct(0.0)
print(f"  F(c=0) = {F0:.12f}")

# Check reduced states
print(f"  rho_Q =\n{np.array2string(rho_Q, precision=8)}")
print(f"  rho_QE =\n{np.array2string(rho_QE, precision=4)}")

# Check fidelity more explicitly
print(f"  <psi|sigma|psi> = {np.real(make_cartan_output(0.0).conj().T @ sigma @ make_cartan_output(0.0)):.12f}")
print(f"  |<psi|sigma|psi> - rho_RQE| = {np.max(np.abs(sigma - rho_RQE)):.2e}")

# Also compute QCMI
S_RQE = vn_entropy(rho_RQE)
S_RQ = vn_entropy(rho_RQ)
S_QE = vn_entropy(rho_QE)
S_Q = vn_entropy(rho_Q)
I_cmi = S_RQ + S_QE - S_RQE - S_Q
print(f"  I(R:E|Q) at c=0: {I_cmi:.8f} bits (should be 0)")

if abs(F0 - 1.0) > 1e-6:
    print(f"  *** FAIL: F should be 1 at c=0! ***")
    # Debug: check the Petz map step by step
    print(f"\n  DEBUG: Step-by-step Petz recovery check")
    # At c=0: rho_Q = I/2, pinv_sqrt_Q = sqrt(2)*I
    print(f"  rho_Q eigenvalues: {np.sort(eigvalsh(rho_Q))}")
    print(f"  rho_QE eigenvalues: {np.sort(eigvalsh(rho_QE))}")

    # Check: R(B_00)
    B_00 = rho_RQ[0:2, 0:2]
    print(f"  B_00 = \n{np.array2string(B_00, precision=6)}")
    pinv_sqrt_Q = vecs_Q @ np.diag(1.0/np.sqrt(np.maximum(np.real(vals_Q), 1e-14))) @ vecs_Q.T.conj()
    print(f"  pinv_sqrt_Q = \n{np.array2string(pinv_sqrt_Q, precision=6)}")
    middle_Q = pinv_sqrt_Q @ B_00 @ pinv_sqrt_Q
    print(f"  middle_Q = \n{np.array2string(middle_Q, precision=6)}")
    middle_QE = np.kron(middle_Q, I2)
    print(f"  middle_QE = \n{np.array2string(middle_QE, precision=4)}")
else:
    print(f"  PASS: F=1 at c=0 as expected")


# ============================================================
# TEST 2: Small c scan
# ============================================================
print("\n" + "=" * 70)
print("TEST 2: Small-c fidelity scan")
print("=" * 70)

c_vals = [0.0, 0.0001, 0.001, 0.01, 0.05, 0.1, 0.2, 0.5]
print(f"{'c':>10s}  {'F':>18s}  {'1-F':>18s}  {'(1-F)/c^2':>16s}")
print("-" * 66)

for c in c_vals:
    F, _, _, _, _, _ = petz_recovery_fidelity_correct(c)
    one_minus_F = 1.0 - F
    ratio = one_minus_F / (c**2) if c > 1e-15 else 0
    print(f"{c:10.6f}  {F:18.15f}  {one_minus_F:18.15f}  {ratio:16.8f}")

# ============================================================
# TEST 3: High-precision fit for F2
# ============================================================
print("\n" + "=" * 70)
print("TEST 3: Fit F = 1 - F2*c^2 - F4*c^4")
print("=" * 70)

c_fine = np.logspace(-4, -1, 20)
F_vals = []
for c in c_fine:
    F, _, _, _, _, _ = petz_recovery_fidelity_correct(c)
    F_vals.append(F)

y = (1.0 - np.array(F_vals)) / c_fine**2
x = c_fine**2
X = np.column_stack([np.ones_like(x), x])
coeffs, _, _, _ = np.linalg.lstsq(X, y, rcond=None)
F2_fit, F4_fit = coeffs[0], coeffs[1]

print(f"  F2 (quadratic coeff) = {F2_fit:.12f}")
print(f"  F4 (quartic coeff)   = {F4_fit:.8f}")

# Compare to theoretical possibilities
eta0 = 1.0 / (8.0 * np.log(2.0))
print(f"\n  Theoretical possibilities for F2:")
print(f"    If F2 = 1/16 = {1/16:.12f}: I >= (2*F2/ln2)*c^2 = {(2*(1/16)/np.log(2)):.6f}*c^2")
print(f"      => eta0_theory = {1/(16*np.log(2)):.6f} (vs claimed {eta0:.6f})")

# The Fawzi-Renner bound: I >= -2 log2 F
# If F = 1 - F2*c^2: I >= (2*F2/ln2)*c^2
# For eta0 = 1/(8 ln 2): we need 2*F2/ln2 = 1/(8 ln 2) => F2 = 1/16
F2_for_claimed = eta0 * np.log(2) / 2
print(f"    For claimed eta0={eta0:.6f}: F2 must be {F2_for_claimed:.12f} = 1/{1/F2_for_claimed:.1f}")
ratio = F2_fit / F2_for_claimed
print(f"    Fitted F2 / required F2 = {ratio:.6f}")

# ALSO compute the Fawzi-Renner bound from the FIDELITY and compare to actual QCMI
print(f"\n  Comparison of Fawzi-Renner bound vs actual QCMI:")
print(f"  {'c':>10s}  {'F':>16s}  {'I_FR_bound':>14s}  {'I_actual':>14s}  {'ratio':>10s}")
print(f"  {'-'*10}  {'-'*16}  {'-'*14}  {'-'*14}  {'-'*10}")

for c in [0.0001, 0.001, 0.01, 0.05, 0.1, 0.2, 0.5]:
    F, rho_RQE, _, _, _, _ = petz_recovery_fidelity_correct(c)
    I_FR = -2.0 * np.log2(max(F, 1e-15))
    # Actual QCMI
    rho_RQ = partial_trace(rho_RQE, [2,2,2], [0,1])
    rho_QE = partial_trace(rho_RQE, [2,2,2], [1,2])
    rho_Q = partial_trace(rho_RQE, [2,2,2], [1])
    I_act = vn_entropy(rho_RQ) + vn_entropy(rho_QE) - vn_entropy(rho_Q)
    rat = I_act / I_FR if I_FR > 1e-15 else float('inf')
    print(f"  {c:10.6f}  {F:16.12f}  {I_FR:14.8f}  {I_act:14.8f}  {rat:10.4f}")

print("\nDone.")

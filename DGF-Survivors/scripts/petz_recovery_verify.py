"""
FIRST-PRINCIPLES PETZ RECOVERY FIDELITY COMPUTATION
====================================================

**CORRECTION (2026-06-09):** OLD derivation chain DISPROVEN. Correct: eta0 = 2/ln 2 ~ 2.885.
Errors: (1) -2log2(F^2) should be -2log2(F), (2) F<=1-2|c|^2 should be F=1-|c|^2.
See petz_recovery_v2.py for correct computation.

ORIGINAL (now known wrong): Verifies the derivation chain:
Fawzi-Renner(2015) -> Petz recovery -> Cartan expansion -> d=2, gamma0=gamma1=1/2 -> eta0 = 1/(8 ln 2)

KEY: This computes F = F(rho_{RQ'E'}, Petz_recovery(rho_{RQ'})) directly,
not just the QCMI.

The Fawzi-Renner bound: I(A:C|B) >= -2 log2 F^2 where F is fidelity of recovery.
For small |c|: F = 1 - F2*|c|^2 + O(|c|^4)
Then: -2 log2 F^2 approx= (4*F2/ln2)*|c|^2

If F2 = 1/16: I >= 1/(4 ln 2) * |c|^2 = 0.3607 * |c|^2
If F2 = 1/64: I >= 1/(16 ln 2) * |c|^2 = 0.0902 * |c|^2

The claimed eta0 = 1/(8 ln 2) approx= 0.180 * |c|^2
This corresponds to F2 = 1/32, not 1/16 or 1/64!

Wait, need to be VERY careful about the algebra. Let me re-derive from the paper.

Theorem 5.1 (Fawzi-Renner 2015):
  F(rho_ABC, sigma_ABC) >= 2^{-1/2 * I(A:C|B)}
where sigma_ABC = T_{B->BC}(rho_AB) for some channel T.

Taking -2 log2 of both sides:
  -2 log2 F >= I(A:C|B)
So: I(A:C|B) <= -2 log2 F  (this is an UPPER bound on I, not lower!)

Wait, that's the OPPOSITE of what I thought. Let me re-read...

F >= 2^{-I/2}
Taking -2 log2: -2 log2 F <= I

YES! -2 log2 F <= I, meaning I >= -2 log2 F. This IS a lower bound.

For F = 1 - F2*c^2:
-2 log2 F = -2 log2(1 - F2*c^2) approx= 2*F2/ln2 * c^2

So: I >= (2*F2/ln2) * c^2

If F2 = 1/16: I >= 1/(8 ln 2) * c^2 = eta0 * c^2
If F2 = 1/64: I >= 1/(32 ln 2) * c^2 = 0.0451 * c^2

So the DERIVATION CLAIM is that F2 = 1/16, NOT 1/64!

But the "1/8 factor from d=2, gamma0=gamma1=1/2" that's mentioned in 01-established-results.md
says something different. Let me re-read:

"Petz恢复保真度满足 F <= 1 - 2|c|^2 + O(|c|^4)，因此 -2 log2 F^2 >= (8/ln2)·|c|^2 · (1 + O(|c|^2))。
取d=2, gamma0=gamma1=1/2因子的1/8后得 eta0 = 1/(8 ln 2)。"

OK so their derivation says:
1. F <= 1 - 2|c|^2 (Petz recovery fidelity, where |c| is the Cartan parameter)
2. Therefore F^2 <= (1 - 2|c|^2)^2 = 1 - 4|c|^2 + O(|c|^4)
   (but 1 - 2|c|^2 is an upper bound, not equality, so this is tricky)
3. -2 log2 F^2 >= -2 log2(1 - 4|c|^2) approx= (8/ln2) * |c|^2
4. Then they apply a 1/8 factor from d=2, gamma0=gamma1=1/2:
   eta0 = (1/8) * (8/ln2) = 1/ln2...? No, that's not right.

Wait, I think the factor of 1/8 means they're saying the F should actually be:
F <= 1 - (1/8)*2|c|^2 = 1 - |c|^2/4 ...? No, that's even more confusing.

Let me re-read more carefully. The text says:
"取d=2, gamma0=gamma1=1/2因子的1/8后得 eta0 = 1/(8 ln 2)"

Hmm, "取d=2, gamma0=gamma1=1/2因子的1/8后" — "after applying the 1/8 factor from d=2, gamma0=gamma1=1/2"
"得 eta0 = 1/(8 ln 2)" — "we get eta0 = 1/(8 ln 2)"

So the 1/8 factor appears in the DENOMINATOR of eta0. And the final result is 1/(8 ln 2).

If the pre-factor was 1/ln2 and we multiply by 1/8, we get 1/(8 ln 2). So:
eta0 = 1/(8 ln 2) = (1/8) * (1/ln2)

This means the Fawzi-Renner bound WITHOUT the Cartan specialization gives a coefficient of 1/ln2,
and the Cartan specialization introduces an extra factor of 1/8 (from d=2, gamma0=gamma1=1/2).

But HOW? The Fawzi-Renner bound already gives a coefficient that depends on the state...

I think the chain is:
1. General Fawzi-Renner: I >= -2 log2 F
2. For small deviation from Markovianity: F approx= 1 - K*eps where eps = |c|^2
3. I >= (2K/ln2)*eps
4. For the Cartan channel, K = 1/16 (so 2K/ln2 = 1/(8 ln 2))

OR:
1. General Fawzi-Renner: I >= -2 log2 F
2. F <= 1 - 2|c|^2 for some universal bound on the Petz recovery
3. But the Cartan specialization REDUCES this to F <= 1 - (1/4)|c|^2
   (because of d=2, gamma0=gamma1=1/2 giving factor 1/8 applied to the 2|c|^2 term)
4. So F^2 <= 1 - |c|^2/2
5. I >= (1/(2 ln 2)) * |c|^2... no, that gives 1/(2 ln 2)

I'm going in circles. Let me just COMPUTE IT.

I'll compute the Petz recovery fidelity numerically for the Cartan channel and see what F2 comes out.
"""

import numpy as np
from numpy.linalg import eigvalsh, eigh
from scipy.linalg import sqrtm
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# ============================================================
# Pauli matrices and tensor product helpers
# ============================================================
I2 = np.eye(2, dtype=complex)
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
sp = np.array([[0, 1], [0, 0]], dtype=complex)  # |0><1|
sm = np.array([[0, 0], [1, 0]], dtype=complex)  # |1><0|
ket0 = np.array([1, 0], dtype=complex)
ket1 = np.array([0, 1], dtype=complex)

def tensor(*mats):
    """Kronecker product of multiple matrices."""
    r = mats[0]
    for m in mats[1:]:
        r = np.kron(r, m)
    return r

def partial_trace(rho, dims, keep):
    """Partial trace. rho is on product space with dimensions dims.
    keep: list of subsystem indices to KEEP."""
    N = len(dims)
    # Reshape to N x N index form
    shape = tuple(dims) + tuple(dims)
    rho_t = rho.reshape(shape)
    # Determine which axes to trace out
    trace_out = [i for i in range(N) if i not in keep]
    # Build permutation: keep axes first, then trace axes, for both row and column
    keep_plus = keep + [i + N for i in keep]
    trace_plus = trace_out + [i + N for i in trace_out]
    perm = keep_plus + trace_plus
    rho_t = np.transpose(rho_t, perm)
    # Reshape to separate keep and trace dimensions
    keep_dims = [dims[i] for i in keep]
    trace_dims = [dims[i] for i in trace_out]
    keep_size = int(np.prod(keep_dims))
    trace_size = int(np.prod(trace_dims))
    rho_t = rho_t.reshape(keep_size, trace_size, keep_size, trace_size)
    # Trace over the environment axes (axes 1 and 3)
    rho_reduced = np.trace(rho_t, axis1=1, axis2=3)
    return rho_reduced

def fidelity(rho, sigma):
    """Uhlmann fidelity F(rho, sigma) = Tr(sqrt(sqrt(rho) sigma sqrt(rho)))."""
    vals, vecs = eigh(rho)
    vals = np.maximum(np.real(vals), 0)
    sqrt_rho = vecs @ np.diag(np.sqrt(vals)) @ vecs.T.conj()
    inner = sqrt_rho @ sigma @ sqrt_rho
    inner = (inner + inner.T.conj()) / 2  # ensure Hermitian
    vals_inner = eigvalsh(inner)
    vals_inner = np.maximum(np.real(vals_inner), 0)
    return float(np.sum(np.sqrt(vals_inner)))

def fidelity_pure_rho(rho_pure, sigma):
    """Fidelity when rho_pure = |psi><psi| is a pure state.
    F = sqrt(<psi| sigma |psi>)."""
    # Find the eigenvector with eigenvalue 1
    vals, vecs = eigh(rho_pure)
    idx = np.argmax(np.real(vals))
    psi = vecs[:, idx]
    val = np.real(psi.conj().T @ sigma @ psi)
    return float(np.sqrt(max(val, 0)))

def matrix_sqrt_pinv(rho, eps=1e-12):
    """Compute matrix square root and pseudo-inverse square root of rho.
    Returns (sqrt_rho, pinv_sqrt_rho)."""
    vals, vecs = eigh(rho)
    vals = np.real(vals)
    # sqrt
    sqrt_vals = np.sqrt(np.maximum(vals, 0))
    sqrt_rho = vecs @ np.diag(sqrt_vals) @ vecs.T.conj()
    # pseudo-inverse sqrt
    pinv_vals = np.zeros_like(vals)
    mask = vals > eps
    pinv_vals[mask] = 1.0 / np.sqrt(vals[mask])
    pinv_sqrt_rho = vecs @ np.diag(pinv_vals) @ vecs.T.conj()
    return sqrt_rho, pinv_sqrt_rho

# ============================================================
# Model 1: SINGLE QUBIT Cartan channel
# ============================================================
# System: Q (1 qubit)
# Reference: R (1 qubit), maximally entangled with Q
# Environment: E (1 qubit), initial state |gamma>
# Cartan gate: U = exp(i*c*sigma_z x sigma_z) on QE

def single_qubit_cartan_rho(c, theta_gamma=np.pi/4):
    """
    Compute rho_{RQ'E'} for single-qubit Cartan channel.

    Parameters:
    - c: Cartan parameter (interaction strength)
    - theta_gamma: env state parameter |gamma> = cos(theta)|0> + sin(theta)|1>
                   pi/4 gives equal superposition (gamma0=gamma1=1/2)

    Returns:
    - rho_RQE: full output density matrix (R, Q', E')
    """
    a = np.cos(theta_gamma)
    b = np.sin(theta_gamma)

    # Initial state: |Phi+>_{RQ} x |gamma>_E
    # |Phi+> = (|00> + |11>)/sqrt(2)
    # |gamma> = a|0> + b|1>
    psi_init = np.zeros(8, dtype=complex)
    psi_init[0] = a / np.sqrt(2)  # |000>: R=0, Q=0, E=0
    psi_init[1] = b / np.sqrt(2)  # |001>: R=0, Q=0, E=1
    psi_init[6] = a / np.sqrt(2)  # |110>: R=1, Q=1, E=0
    psi_init[7] = b / np.sqrt(2)  # |111>: R=1, Q=1, E=1

    # Cartan gate U = exp(i*c*sigma_z x sigma_z) on QE
    # diag(e^{ic}, e^{-ic}, e^{-ic}, e^{ic})
    U_QE = np.diag([np.exp(1j*c), np.exp(-1j*c), np.exp(-1j*c), np.exp(1j*c)])

    # Apply (I_R x U_QE) to psi_init
    # I_R x U_QE: 2 x 4 = 8 dimensions
    I_U = np.kron(I2, U_QE)
    psi_out = I_U @ psi_init

    rho = np.outer(psi_out, psi_out.conj())
    return rho, psi_out


def petz_recovery_fidelity_single(c, theta_gamma=np.pi/4):
    """
    Compute the Petz recovery fidelity for single-qubit Cartan channel.

    Tripartite system: A=R, B=Q', C=E'

    Petz recovery map R_{B->BC}(X_B) = rho_BC^{1/2} rho_B^{-1/2} X_B rho_B^{-1/2} rho_BC^{1/2}

    Applied to rho_AB = rho_RQ':
    sigma = (I_A x R_{B->BC})(rho_AB)

    Fidelity: F = F(rho_ABC, sigma)
    """
    rho_ABC, psi_out = single_qubit_cartan_rho(c, theta_gamma)

    # Dimensions: R=2, Q'=2, E'=2
    dims = [2, 2, 2]

    # Reduced states
    rho_RQ = partial_trace(rho_ABC, dims, [0, 1])  # trace out E' (index 2)
    rho_QE = partial_trace(rho_ABC, dims, [1, 2])  # trace out R (index 0)
    rho_Q = partial_trace(rho_ABC, dims, [1])      # trace out R and E' (indices 0,2)

    # Check ranks
    vals_RQ = eigvalsh(rho_RQ)
    vals_QE = eigvalsh(rho_QE)
    vals_Q = eigvalsh(rho_Q)

    # Compute Petz recovery
    # NOTE: sqrt_QE = sqrt(rho_QE) [4x4], pinv_sqrt_Q = rho_Q^{-1/2} [2x2]
    sqrt_QE, _ = matrix_sqrt_pinv(rho_QE, eps=1e-12)
    _, pinv_sqrt_Q = matrix_sqrt_pinv(rho_Q, eps=1e-12)

    # R_{Q'->Q'E'}(X_Q') = rho_QE^{1/2} rho_Q^{-1/2} X_Q' rho_Q^{-1/2} rho_QE^{1/2}
    # Applied to rho_RQ': (I_R x R)(rho_RQ')
    #
    # First, apply rho_Q^{-1/2} to the Q' part of rho_RQ'
    # This means: (I_R x rho_Q^{-1/2}) * rho_RQ' * (I_R x rho_Q^{-1/2})
    I_x_pinv = np.kron(I2, pinv_sqrt_Q)
    middle = I_x_pinv @ rho_RQ @ I_x_pinv

    # Then embed: (I_R x rho_QE^{1/2}) * middle * (I_R x rho_QE^{1/2})
    # But rho_QE^{1/2} is on QE, which is a 4x4 matrix
    # We need to embed this into the RQE space
    # The embedding is: I_R x rho_QE^{1/2}, which is 8x8

    # However, middle is on RQ (4x4), and we need to tensor with E
    # Actually, the Petz map construction needs to be more careful.
    # The map R_{Q'->Q'E'} when applied to a state on RQ':
    # It acts as: id_R x R on rho_RQ'
    # Where R(X_Q') = rho_QE^{1/2} rho_Q^{-1/2} X_Q' rho_Q^{-1/2} rho_QE^{1/2}

    # So (I_R x R)(rho_RQ'):
    # = (I_R x rho_QE^{1/2}) (I_R x rho_Q^{-1/2}) rho_RQ' (I_R x rho_Q^{-1/2}) (I_R x rho_QE^{1/2})
    # But wait, I_R x rho_QE^{1/2} acts on R x QE, not on R x Q.
    # And rho_Q^{-1/2} acts on Q only.

    # The correct construction:
    # 1. Start with rho_RQ' on R x Q
    # 2. Apply rho_Q^{-1/2} to Q part: (I_R x rho_Q^{-1/2}) rho_RQ' (I_R x rho_Q^{-1/2})
    #    This gives a state still on R x Q
    # 3. Apply rho_QE^{1/2} to embed Q -> QE:
    #    This is trickier because rho_QE^{1/2} is on QE, not just Q.

    # The standard Petz construction embeds as:
    # rho_QE^{1/2} (rho_Q^{-1/2} x I_E) rho_RQE (rho_Q^{-1/2} x I_E) rho_QE^{1/2}
    # where rho_RQE is tensor with identity on E

    # For rho_RQ' (which doesn't have E), we extend:
    # sigma_RQE = (I_R x rho_QE^{1/2}) (I_R x rho_Q^{-1/2} x I_E) (rho_RQ' x I_E/d_E)
    #                                      (I_R x rho_Q^{-1/2} x I_E) (I_R x rho_QE^{1/2})

    # where we embed rho_RQ' into RQE by tensoring with I_E/d_E (maximally mixed on E)
    # OR we can use the rotated Petz map formulation.

    # ALTERNATIVELY, the Petz recovery can be written directly as:
    # sigma_ABC = rho_ABC^{1/2} rho_AB^{-1/2} rho_B^{1/2} ...
    # No, that's for a different construction.

    # Let me use the standard formula for the Petz recovery fidelity:
    # F^2 = || rho_BC^{-1/4} rho_ABC^{1/2} rho_AB^{-1/4} rho_B^{1/4} ||_1^2

    # Actually, the rotated Petz recovery (Berta+Tomamichel) uses:
    # sigma = rho_ABC^{1/2} rho_C^{-1/2} rho_BC^{1/2} (?)

    # Let me use the most standard formulation.
    # The Petz recovery map for tripartite rho_ABC:
    # R_{B->BC}(X_B) = rho_BC^{1/2} rho_B^{-1/2} X_B rho_B^{-1/2} rho_BC^{1/2}
    #
    # Applied to rho_AB:
    # (I_A x R)(rho_AB) = (I_A x rho_BC^{1/2}) (I_A x rho_B^{-1/2}) rho_AB (I_A x rho_B^{-1/2}) (I_A x rho_BC^{1/2})

    # Now (I_A x rho_B^{-1/2}) maps A x B -> A x B (acting only on B)
    # And (I_A x rho_BC^{1/2}) maps A x B -> A x BC (embedding B into BC)

    # So:
    # sigma = (I_A x rho_BC^{1/2}) (I_A x (rho_B^{-1/2} x I_C)) ... no

    # Actually, I think the correct embedding is simpler:
    # (I_A x rho_B^{-1/2}) acts on rho_AB, giving a state on A x B
    # Then (I_A x rho_BC^{1/2}) takes this state on A x B and maps it to A x BC
    # by acting with rho_BC^{1/2} on the BC part, but we only have a B part...

    # The solution: the Petz map acts on operators on B, outputting operators on BC.
    # When extended to A x B: it acts as I_A on A and the map on B.
    # The map takes a B operator X_B and outputs a BC operator:
    # R(X_B) = rho_BC^{1/2} rho_B^{-1/2} (I_A x X_B) rho_B^{-1/2} rho_BC^{1/2}  <- no

    # WAIT: the Petz map is defined on B only!
    # R_{B->BC}(X_B) = rho_BC^{1/2} rho_B^{-1/2} X_B rho_B^{-1/2} rho_BC^{1/2}
    # This takes a d_B x d_B matrix X_B and produces a d_BC x d_BC matrix.

    # To apply to rho_AB, we write rho_AB in the form sum_i L_i x R_i
    # where L_i is on A and R_i is on B.
    # Then (I_A x R)(rho_AB) = sum_i L_i x R(R_i)

    # For a matrix rho_AB on A x B, we can use the partial transpose trick:
    # rho_AB = sum_{i,j} |i><j|_A x B_{ij}
    # where B_{ij} = <i|_A rho_AB |j>_A (an operator on B)

    # Then (I_A x R)(rho_AB) = sum_{i,j} |i><j|_A x R(B_{ij})

    # Let me implement this directly!

    d_A, d_B, d_C = 2, 2, 2

    # Build the Petz recovery applied to rho_RQ
    sigma = np.zeros((d_A*d_B*d_C, d_A*d_B*d_C), dtype=complex)

    for i in range(d_A):
        for j in range(d_A):
            # B_{ij} = <i|_A rho_AB |j>_A
            # This is a d_B x d_B block of rho_AB
            B_ij = rho_RQ[i*d_B:(i+1)*d_B, j*d_B:(j+1)*d_B]

            # R(B_ij) = rho_BC^{1/2} rho_B^{-1/2} B_ij rho_B^{-1/2} rho_BC^{1/2}
            # rho_B^{-1/2} is d_B x d_B, B_ij is d_B x d_B
            # rho_BC^{1/2} is d_BC x d_BC = d_B*d_C x d_B*d_C

            middle_B = pinv_sqrt_Q @ B_ij @ pinv_sqrt_Q  # d_B x d_B, still on B space

            # Now embed into BC: rho_BC^{1/2} (middle_B x I_C) rho_BC^{1/2}
            # middle_B is on B, we tensor with I_C to put on BC
            middle_BC = np.kron(middle_B, I2)

            R_B_ij = sqrt_QE @ middle_BC @ sqrt_QE  # d_BC x d_BC

            # Place back: |i><j|_A x R(B_ij)
            sigma[i*d_B*d_C:(i+1)*d_B*d_C, j*d_B*d_C:(j+1)*d_B*d_C] = R_B_ij

    # Ensure Hermitian
    sigma = (sigma + sigma.T.conj()) / 2

    # Compute fidelity F(rho_ABC, sigma)
    # rho_ABC is pure, so use pure-state formula
    F = fidelity_pure_rho(rho_ABC, sigma)

    return F, rho_ABC, sigma, psi_out


def petz_recovery_analytical_expansion(c, theta_gamma=np.pi/4, order=2):
    """
    Analytical expansion of the Petz recovery fidelity in c.

    Uses perturbation theory to compute F(c) = 1 - F2*c^2 + O(c^4).

    This avoids numerical precision issues at very small c.
    """
    a = np.cos(theta_gamma)
    b = np.sin(theta_gamma)

    # The output state |psi'> = (I x U) |psi>
    # |psi'> = (a e^{ic}|000> + b e^{-ic}|001> + a e^{-ic}|110> + b e^{ic}|111>) / sqrt(2)

    # Expand e^{ic} = 1 + ic - c^2/2 - ic^3/6 + c^4/24 + ...

    # |psi'> = |psi_0> + ic|psi_1> - c^2/2 |psi_2> + O(c^3)
    # where:
    # |psi_0> = (a|000> + b|001> + a|110> + b|111>)/sqrt(2)
    # |psi_1> = (a|000> - b|001> - a|110> + b|111>)/sqrt(2)
    # |psi_2> = (a|000> + b|001> + a|110> + b|111>)/sqrt(2) = |psi_0>

    # Actually let me be more careful:
    # e^{ic} = 1 + ic - c^2/2 - i c^3/6 + c^4/24 + O(c^5)
    # e^{-ic} = 1 - ic - c^2/2 + i c^3/6 + c^4/24 + O(c^5)

    # Term a*e^{ic}|000>: a(1 + ic - c^2/2 - i c^3/6)|000>
    # Term b*e^{-ic}|001>: b(1 - ic - c^2/2 + i c^3/6)|001>
    # Term a*e^{-ic}|110>: a(1 - ic - c^2/2 + i c^3/6)|110>
    # Term b*e^{ic}|111>: b(1 + ic - c^2/2 - i c^3/6)|111>

    # |psi'> = |psi_0> + ic|psi_1> - c^2/2|psi_2> - i c^3/6|psi_3> + c^4/24|psi_4> + O(c^5)
    # |psi_0> = (a|000> + b|001> + a|110> + b|111>)/sqrt(2)  [O(1)]
    # |psi_1> = (a|000> - b|001> - a|110> + b|111>)/sqrt(2)  [O(c)]
    # |psi_2> = (a|000> + b|001> + a|110> + b|111>)/sqrt(2) = |psi_0>  [O(c^2)]
    # |psi_3> = (a|000> - b|001> - a|110> + b|111>)/sqrt(2) = |psi_1>  [O(c^3)]
    # |psi_4> = (a|000> + b|001> + a|110> + b|111>)/sqrt(2) = |psi_0>  [O(c^4)]

    # So the expansion is actually very structured:
    # |psi(c)> = |psi_0> (1 - c^2/2 + c^4/24 + ...) + i|psi_1> (c - c^3/6 + ...)
    #          = cos(c)|psi_0> + i sin(c)|psi_1>

    # Interesting! The output is just a rotation between |psi_0> and |psi_1>.
    # Let me check: cos(c) = 1 - c^2/2 + c^4/24, sin(c) = c - c^3/6, matches!

    # But wait, are |psi_0> and |psi_1> orthogonal?
    # <psi_0|psi_1> = (a^2 - b^2 - a^2 + b^2)/2 = 0 ✓ (assuming real a,b)

    # So |psi(c)> = cos(c)|psi_0> + i sin(c)|psi_1> with <psi_0|psi_0> = <psi_1|psi_1> = 1

    # Check norms: <psi_0|psi_0> = (a^2+b^2+a^2+b^2)/2 = 1 ✓
    # <psi_1|psi_1> = (a^2+b^2+a^2+b^2)/2 = 1 ✓

    # Great! So rho_ABC = |psi(c)><psi(c)| is a pure state.

    # Now I need to compute the reduced states and Petz recovery analytically.
    # This is a 3-qubit pure state with a simple structure.

    # |psi(c)> = cos(c)|psi_0> + i sin(c)|psi_1>

    # Let me write |psi_0> and |psi_1> in Schmidt form.
    # Actually, let me compute the reduced density matrices directly.

    # |psi_0> = (a|000> + b|001> + a|110> + b|111>)/sqrt(2)
    #         = 1/sqrt(2) * (|0>_R x (a|00>+b|01>) + |1>_R x (a|10>+b|11>))
    #         = 1/sqrt(2) * (|0>_R x |0>_Q x |gamma>_E + |1>_R x |1>_Q x |gamma>_E)

    # |psi_1> = (a|000> - b|001> - a|110> + b|111>)/sqrt(2)
    #         = 1/sqrt(2) * (|0>_R x (a|00>-b|01>) + |1>_R x (-a|10>+b|11>))
    #         = 1/sqrt(2) * (|0>_R x |0>_Q x sigma_z|gamma>_E - |1>_R x |1>_Q x sigma_z|gamma>_E)
    #         = (sigma_z)_R? No, let me not go down this path.

    # Let me directly compute the reduced states using vectorization.
    psi_0 = np.zeros(8, dtype=complex)
    psi_0[0] = a / np.sqrt(2)
    psi_0[1] = b / np.sqrt(2)
    psi_0[6] = a / np.sqrt(2)
    psi_0[7] = b / np.sqrt(2)

    psi_1 = np.zeros(8, dtype=complex)
    psi_1[0] = a / np.sqrt(2)
    psi_1[1] = -b / np.sqrt(2)
    psi_1[6] = -a / np.sqrt(2)
    psi_1[7] = b / np.sqrt(2)

    # Verify orthogonality
    # print(f"<psi_0|psi_1> = {np.dot(psi_0.conj(), psi_1):.10f}")

    # |psi(c)> = cos(c)|psi_0> + i sin(c)|psi_1>
    # rho_ABC = cos^2(c) |psi_0><psi_0| + sin^2(c) |psi_1><psi_1|
    #           + i cos(c)sin(c) (|psi_0><psi_1| - |psi_1><psi_0|)

    # Wait, i*|psi_0><psi_1| conjugate is -i*|psi_1><psi_0|, so:
    # rho_ABC = cos^2(c)|psi_0><psi_0| + sin^2(c)|psi_1><psi_1|
    #           - i cos(c)sin(c) (|psi_1><psi_0| - |psi_0><psi_1|)

    # Let me compute reduced states numerically for a specific c, then fit.
    pass  # Use the numerical method below


# ============================================================
# Numerical computation for various c values
# ============================================================
print("=" * 80)
print("PETZ RECOVERY FIDELITY VERIFICATION")
print("Single-qubit Cartan channel")
print("=" * 80)

eta0_claimed = 1.0 / (8.0 * np.log(2.0))
print(f"\nClaimed eta0 = 1/(8 ln 2) = {eta0_claimed:.10f}")

# If I >= (2*F2/ln2)*c^2 and eta0 = 2*F2/ln2:
# F2 = eta0 * ln2 / 2
F2_if_claim_correct = eta0_claimed * np.log(2.0) / 2.0
print(f"If claim correct: F = 1 - F2*c^2 with F2 = {F2_if_claim_correct:.10f} = {1.0/F2_if_claim_correct:.1f}^(-1)")
print(f"  (F2 = 1/{1/F2_if_claim_correct:.1f})")

# If the pre-factor from the established results is: F <= 1 - 2|c|^2, then F2 = 2
# and -2 log2 F approx= (4/ln2)*c^2, then after 1/8 factor: 1/(2 ln 2) approx= 0.72
# That gives a DIFFERENT eta0.

print(f"\nChecking: if F <= 1 - 2|c|^2, then -2 log2 F approx= {4.0/np.log(2):.4f}*c^2")
print(f"  With 1/8 factor: {(4.0/np.log(2))/8:.4f}*c^2")
print(f"  This is {1/(2*np.log(2)):.4f}, NOT 1/(8 ln 2)")

# Compute Petz recovery fidelity for various c
print("\n" + "-" * 80)
print("Numerical Petz recovery fidelity vs c:")
print("-" * 80)

c_values = []
for n in range(4, 17):
    c_values.append(2.0**(-n))  # 1/16, 1/32, ..., 1/65536

c_values.append(0.05)
c_values.append(0.1)
c_values.sort()

print(f"{'c':>12s}  {'1-F':>16s}  {'(1-F)/c^2':>14s}  {'F2 = (1-F)/c^2':>16s}")
print("-" * 62)

for c in c_values:
    try:
        F, rho, sigma, psi = petz_recovery_fidelity_single(c)
        one_minus_F = 1.0 - F
        F2_est = one_minus_F / (c**2) if c > 1e-15 else 0
        print(f"{c:12.8f}  {one_minus_F:16.12f}  {one_minus_F/(c*c):14.8f}  {F2_est:16.10f}")
    except Exception as e:
        print(f"{c:12.8f}  ERROR: {e}")


# Analytical approach using perturbation theory
print("\n" + "=" * 80)
print("ANALYTICAL DERIVATION USING PERTURBATION THEORY")
print("=" * 80)

# For |psi(c)> = cos(c)|psi_0> + i sin(c)|psi_1>:
# rho_ABC = cos^2(c)|psi_0><psi_0| + sin^2(c)|psi_1><psi_1|
#           - i cos(c)sin(c) (|psi_1><psi_0| - |psi_0><psi_1|)
#
# For small c: cos(c) approx= 1 - c^2/2, sin(c) approx= c
# rho_ABC = |psi_0><psi_0| + c^2 (|psi_1><psi_1| - |psi_0><psi_0|)
#           - ic (|psi_1><psi_0| - |psi_0><psi_1|)
#           + O(c^3)

# The reduced state rho_Q: after applying the channel, we have
# rho_Q' = Tr_{RE}(rho_ABC)
# For c=0: rho_Q'(0) = Tr_{RE}(|psi_0><psi_0|) = Tr_R(|Phi+><Phi+|) = I/2 (maximally mixed)
# This is important for inversion.

# Let me compute all reduced states analytically to O(c^2)
a = np.cos(np.pi/4)
b = np.sin(np.pi/4)

psi_0 = np.zeros(8, dtype=complex)
psi_0[0] = a / np.sqrt(2); psi_0[1] = b / np.sqrt(2)
psi_0[6] = a / np.sqrt(2); psi_0[7] = b / np.sqrt(2)

psi_1 = np.zeros(8, dtype=complex)
psi_1[0] = a / np.sqrt(2); psi_1[1] = -b / np.sqrt(2)
psi_1[6] = -a / np.sqrt(2); psi_1[7] = b / np.sqrt(2)

# rho_ABC to O(c^2):
# rho_ABC = rho0 + c * rho1 + c^2 * rho2 + O(c^3)
rho0 = np.outer(psi_0, psi_0.conj())
rho1 = -1j * (np.outer(psi_1, psi_0.conj()) - np.outer(psi_0, psi_1.conj()))
rho2 = np.outer(psi_1, psi_1.conj()) - rho0

# Check: rho_ABC(c=0.001) from numerical vs perturbative
c_test = 0.001
rho_exact, _ = single_qubit_cartan_rho(c_test)
rho_pert = rho0 + c_test * rho1 + c_test**2 * rho2
diff = np.max(np.abs(rho_exact - rho_pert))
print(f"\nPerturbation accuracy at c={c_test}: max|rho_exact - rho_pert| = {diff:.2e}")

# Reduced states
dims = [2, 2, 2]

# rho_Q(c) = Tr_{RE}(rho_ABC)
rho_Q0 = partial_trace(rho0, dims, [1])
rho_Q1 = partial_trace(rho1, dims, [1])
rho_Q2 = partial_trace(rho2, dims, [1])

print(f"\nrho_Q(0) = {np.diag(rho_Q0)} (should be [0.5, 0.5])")
print(f"rho_Q1 = {np.array2string(rho_Q1, precision=6)}")

# rho_QE(c) = Tr_R(rho_ABC)
rho_QE0 = partial_trace(rho0, dims, [1, 2])
rho_QE1 = partial_trace(rho1, dims, [1, 2])
rho_QE2 = partial_trace(rho2, dims, [1, 2])

# rho_RQ(c) = Tr_E(rho_ABC)
rho_RQ0 = partial_trace(rho0, dims, [0, 1])
rho_RQ1 = partial_trace(rho1, dims, [0, 1])
rho_RQ2 = partial_trace(rho2, dims, [0, 1])

# For the Petz recovery:
# R_{Q'->Q'E'}(X) = rho_QE^{1/2} rho_Q^{-1/2} X rho_Q^{-1/2} rho_QE^{1/2}
# We need rho_Q^{-1/2} and rho_QE^{1/2}
# At c=0: rho_Q = I/2, so rho_Q^{-1/2} = sqrt(2) * I

print(f"\nAt c=0: rho_Q = I/2, rho_Q^{-1/2} = sqrt(2) * I")
print(f"At c=0: rho_QE is...")

# Let me compute rho_QE0 explicitly and print it
print(f"rho_QE(0) =")
for i in range(4):
    row = ""
    for j in range(4):
        row += f" {rho_QE0[i,j]:8.4f}"
    print(f"  {row}")

# Now I need to do the perturbation expansion of the Petz recovery.
#
# rho_Q(c) = rho_Q0 + c * rho_Q1 + c^2 * rho_Q2 + O(c^3)
# rho_QE(c) = rho_QE0 + c * rho_QE1 + c^2 * rho_QE2 + O(c^3)
#
# rho_Q^{-1/2}(c) = (rho_Q0 + c*rho_Q1 + c^2*rho_Q2)^{-1/2}
#
# For rho_Q0 = I/2:
# rho_Q^{-1/2}(c) = sqrt(2) * (I + c*2*rho_Q1 + c^2*2*rho_Q2)^{-1/2}
# Let X = c*2*rho_Q1 + c^2*2*rho_Q2
# (I+X)^{-1/2} = I - X/2 + 3X^2/8 + O(X^3)
# = I - c*rho_Q1 - c^2*rho_Q2 + (3/2)*c^2*rho_Q1^2 + O(c^3)
# (since (2*rho_Q1)^2/8 * (3/4?) ... let me be more careful)
# Actually: (a*I + X)^{-1/2} = a^{-1/2} (I + X/a)^{-1/2}
# = a^{-1/2} (I - X/(2a) + 3X^2/(8a^2) + ...)
# Here a=1/2, so a^{-1/2} = sqrt(2)
# X = c*rho_Q1 + c^2*rho_Q2 (no factor of 2)
# Wait, let me redo:
# rho_Q = I/2 + c*rho_Q1 + c^2*rho_Q2
# = (1/2)(I + 2c*rho_Q1 + 2c^2*rho_Q2)
# rho_Q^{-1/2} = sqrt(2) * (I + 2c*rho_Q1 + 2c^2*rho_Q2)^{-1/2}
# = sqrt(2) * [I - c*rho_Q1 - c^2*rho_Q2 + (3/2)c^2*(2*rho_Q1)^2/4 + ...]
# No, (I + Y)^{-1/2} where Y = 2c*rho_Q1 + 2c^2*rho_Q2
# = I - Y/2 + 3Y^2/8 + O(Y^3)
# Y = 2c*rho_Q1 + 2c^2*rho_Q2
# Y/2 = c*rho_Q1 + c^2*rho_Q2
# Y^2 = 4c^2*rho_Q1^2 + O(c^3)
# 3Y^2/8 = (3/2)c^2*rho_Q1^2

# So: rho_Q^{-1/2} = sqrt(2) * [I - c*rho_Q1 - c^2*rho_Q2 + (3/2)c^2*rho_Q1^2 + O(c^3)]

# rho_QE^{1/2} = (rho_QE0 + c*rho_QE1 + c^2*rho_QE2)^{1/2}
# This is more complicated because rho_QE0 is NOT proportional to identity.

# Let me just do all of this numerically with high precision instead.
# The analytical perturbation theory is getting too complex to do by hand.

print("\n" + "=" * 80)
print("HIGH-PRECISION NUMERICAL FIT: F(c) = 1 - F2*c^2 - F4*c^4 + ...")
print("=" * 80)

# Use very small c values with high precision
c_fine = np.logspace(-5, -1, 30)
F_vals = []
for c in c_fine:
    F, _, _, _ = petz_recovery_fidelity_single(c)
    F_vals.append(F)

# Fit F = 1 - F2*c^2
y = (1.0 - np.array(F_vals)) / c_fine**2
x = c_fine**2

# Fit y = F2 + F4*x
X = np.column_stack([np.ones_like(x), x])
coeffs, residuals, rank, sv = np.linalg.lstsq(X, y, rcond=None)
F2_fit, F4_fit = coeffs[0], coeffs[1]

print(f"\nFit: (1-F)/c^2 = F2 + F4*c^2")
print(f"  F2 = {F2_fit:.12f}")
print(f"  F4 = {F4_fit:.8f}")

# Print data for verification
print(f"\n{'c':>12s}  {'F':>18s}  {'1-F':>18s}  {'(1-F)/c^2':>14s}  {'fit':>14s}")
for i in range(0, len(c_fine), 3):
    c = c_fine[i]
    F = F_vals[i]
    pred = F2_fit + F4_fit * c**2
    print(f"{c:12.2e}  {F:18.15f}  {1-F:18.15f}  {(1-F)/(c*c):14.8f}  {pred:14.8f}")

# Key conclusion
print(f"\n{'='*80}")
print(f"KEY RESULTS:")
print(f"{'='*80}")
print(f"  Fitted F2 = {F2_fit:.12f}")
print(f"  Theoretical for eta0=1/(8ln2): F2 should be 1/32 = {1/32:.12f}")
print(f"  Ratio: F2 / (1/32) = {F2_fit / (1.0/32.0):.6f}")
print(f"  Theoretical for F <= 1-2|c|^2: F2 should be 2")
print(f"  Ratio: F2 / 2 = {F2_fit / 2.0:.6f}")
print(f"  Theoretical F2 = 1/16 = {1/16:.12f}")
print(f"  Ratio: F2 / (1/16) = {F2_fit / (1.0/16.0):.6f}")

# Also compute the ACTUAL QCMI and compare
print(f"\n{'='*80}")
print(f"COMPARISON: Actual QCMI vs Fawzi-Renner bound")
print(f"{'='*80}")

for c_test in [0.001, 0.01, 0.05, 0.1, 0.5]:
    F, rho, _, _ = petz_recovery_fidelity_single(c_test)
    # Fawzi-Renner bound: I >= -2 log2 F
    I_bound = -2.0 * np.log2(max(F, 1e-15))
    # Actual QCMI from Gram matrix method
    # For single qubit case: I(R:E|Q) = S(RQ) + S(QE) - S(RQE) - S(Q)
    # For pure rho_RQE: S(RQE) = 0, S(RQ) = S(E), S(QE) = S(R)
    # So I = S(RQ) + S(QE) - S(Q)
    # But we can compute directly

    print(f"  c={c_test:.4f}: F={F:.10f}, I_FR = {-2*np.log2(F):.8f} bits")

    # For comparison: compute actual I
    dims = [2, 2, 2]
    rho_RQ = partial_trace(rho, dims, [0, 1])
    rho_QE = partial_trace(rho, dims, [1, 2])
    rho_Q = partial_trace(rho, dims, [1])

    def vn_entropy(rho_mat):
        vals = eigvalsh(rho_mat)
        vals = np.maximum(np.real(vals), 1e-15)
        s = np.sum(vals)
        vals = vals / s
        return -np.sum(vals * np.log2(vals))

    S_RQ = vn_entropy(rho_RQ)
    S_QE = vn_entropy(rho_QE)
    S_Q = vn_entropy(rho_Q)
    I_actual = S_RQ + S_QE - S_Q  # S_RQE = 0 for pure state

    print(f"          Actual I = {I_actual:.8f} bits, I/I_bound = {I_actual/I_bound:.4f}x" if I_bound > 1e-15 else "")
    print(f"          I/c^2 = {I_actual/(c_test**2):.4f} bit/rad^2, I_bound/c^2 = {I_bound/(c_test**2):.4f} bit/rad^2")
    print()

print("Done.")

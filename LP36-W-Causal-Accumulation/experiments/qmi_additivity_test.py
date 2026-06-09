"""
LP37 Lemma Test: QCMI additivity over independent causal channels.

Core question: Is I(R;E'|Q'F) additive over independent system-environment pairs?

If yes: η is fixed per causal cycle, not a free parameter → LP37 has a theorem.
If no:  η is system-dependent → LP37 has a conjecture at best.

Strategy: Construct N independent copies of the same Q-E interaction.
Compute I(R_total; E'_total | Q'_total) for the joint system.
Compare to N × I(R_single; E'_single | Q'_single).

Additivity holds iff they're equal.

Buscemi framework reminder:
- t₀: ρ_RQE = Phi+_RQ x gamma_E  (R maximally entangled with Q, E in fixed state)
- t_1: sigma_RQ'E' = U_QE ρ_RQE U_QE†  (after first unitary)
- The key quantity: I(R;E'|Q')_1  (QCMI at t_1, without inert extension F)
"""

import numpy as np
from scipy.linalg import sqrtm, logm
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# §1. Quantum information utilities
# ============================================================

def von_neumann_entropy(rho, eps=1e-12):
    """H(ρ) = -Tr(ρ log ρ) with numerical stability."""
    eigvals = np.linalg.eigvalsh(rho)
    eigvals = np.maximum(eigvals, eps)  # clip negative/zero
    eigvals = eigvals / np.sum(eigvals)  # renormalize
    return -np.sum(eigvals * np.log2(eigvals))

def partial_trace(rho, keep_dims, total_dims):
    """Trace out all subsystems except those in keep_dims (0-indexed).

    Args:
        rho: density matrix in tensor product basis
        keep_dims: list of indices to keep
        total_dims: list of dimensions for each subsystem

    Returns:
        Reduced density matrix
    """
    # Use numpy reshape + trace
    n = len(total_dims)
    # Reshape to multi-index
    shape = list(total_dims) + list(total_dims)  # [d0, d1, ..., d0, d1, ...]
    rho_tensor = rho.reshape(shape)

    # Axes to trace out
    trace_axes = [i for i in range(n) if i not in keep_dims]
    trace_axes_bra = [i + n for i in trace_axes]

    # Sort axes for consistent ordering after trace
    all_trace_axes = sorted(trace_axes + trace_axes_bra, reverse=True)

    for ax in all_trace_axes:
        rho_tensor = np.trace(rho_tensor, axis1=ax, axis2=ax + (0 if ax < len(rho_tensor.shape)//2 else ...))

    # Hmm, this approach with dynamic axes is tricky. Let me use a simpler method.
    # Actually, let me just use explicit index manipulation.
    pass


def partial_trace_simple(rho, keep, dims):
    """Simpler partial trace using einsum.

    Args:
        rho: full density matrix (product basis)
        keep: indices of subsystems to KEEP
        dims: list of dimensions

    Returns:
        Reduced density matrix on kept subsystems
    """
    n = len(dims)
    # Build the index string for einsum
    # ρ has indices i0,i1,...,i_{n-1}, j0,j1,...,j_{n-1}
    # We want to trace out by contracting i_k with j_k for k not in keep

    indices_in = ''.join([chr(97 + i) for i in range(2*n)])  # a,b,c,..., a',b',c',...

    # Build the output indices: keep the kept ones, sum over the rest
    indices_out = []
    for i in range(n):
        if i in keep:
            indices_out.append(chr(97 + i))  # keep bra index
            indices_out.append(chr(97 + n + i))  # keep ket index
        # else: these get summed (contracted) and don't appear in output

    # But einsum can't do partial trace directly this way with different bra/ket indices.
    # Let me use a different approach: explicitly trace out subsystems.

    d_keep = np.prod([dims[i] for i in keep])
    # Reshape to separate kept and traced dimensions
    kept_dims_list = [dims[i] for i in keep]
    trace_dims_list = [dims[i] for i in range(n) if i not in keep]

    # Reshape ρ to (kept_bra, trace_bra, kept_ket, trace_ket)
    perm_bra = list(keep) + [i for i in range(n) if i not in keep]
    perm_ket = [i + n for i in perm_bra]
    perm = perm_bra + perm_ket

    shape_in = dims + dims
    rho_perm = rho.reshape(shape_in).transpose(perm)

    # Now reshape to (prod(kept), prod(trace), prod(kept), prod(trace))
    d_trace = np.prod(trace_dims_list)
    rho_reshaped = rho_perm.reshape(d_keep, d_trace, d_keep, d_trace)

    # Trace over the trace dimensions (contract axis 1 with axis 3)
    # rho_reduced[i, k] = sum_j rho_reshaped[i, j, k, j]
    rho_reduced = np.einsum('ij kj -> ik', rho_reshaped.reshape(d_keep, d_trace * d_keep * d_trace),
                            np.eye(d_trace).flatten())
    # Hmm that's not right either. Let me just do it manually.

    # Actually, let me do it the straightforward way:
    rho_reduced = np.trace(rho_reshaped, axis1=1, axis2=3)
    return rho_reduced


def partial_trace_bruteforce(rho, keep, dims):
    """Partial trace using explicit basis enumeration. Works for small systems."""
    n = len(dims)
    d_total = np.prod(dims)
    d_keep = np.prod([dims[i] for i in keep])

    rho_reduced = np.zeros((d_keep, d_keep), dtype=complex)

    # We need to sum over traced-out indices
    trace_indices = [i for i in range(n) if i not in keep]

    # Build basis indices
    # For each pair (bra, ket) of kept system basis states,
    # sum over all traced-out basis states

    # This is O(d_total^2 * d_keep^2) — fine for small systems
    for bra_full in range(d_total):
        # Decode bra_full into subsystem indices
        bra_subs = []
        temp = bra_full
        for d in reversed(dims):
            bra_subs.insert(0, temp % d)
            temp //= d

        for ket_full in range(d_total):
            ket_subs = []
            temp = ket_full
            for d in reversed(dims):
                ket_subs.insert(0, temp % d)
                temp //= d

            # Check if traced-out indices match
            match = all(bra_subs[i] == ket_subs[i] for i in trace_indices)
            if match:
                # Compute kept-system basis indices
                bra_keep = sum(bra_subs[i] * int(np.prod([dims[j] for j in keep if keep.index(j) > keep.index(i)]))
                              if False else 0 for i in keep)
                # This multi-index encoding is getting complex, let me just use a different approach
                pass

    # OK this brute force is getting unwieldy. Let me use the standard method.
    return rho_reduced


# Let me use a clean, well-tested partial trace implementation.
def ptrace(rho, keep, dims):
    """Partial trace: trace out all subsystems except those in `keep`.

    Uses the standard method: permute + reshape + trace.

    Args:
        rho: Density matrix on n subsystems, shape (D, D) where D = prod(dims)
        keep: List of subsystem indices to keep
        dims: List of subsystem dimensions

    Returns:
        Reduced density matrix on kept subsystems, shape (D_keep, D_keep)
    """
    n = len(dims)
    keep = sorted(keep)
    trace_out = [i for i in range(n) if i not in keep]

    # Permute so kept subsystems come first, then traced-out
    perm = keep + trace_out

    # Reshape to (d0_bra, d1_bra, ..., dn_bra, d0_ket, d1_ket, ..., dn_ket)
    shape = tuple(dims) + tuple(dims)
    rho_tensor = rho.reshape(shape)

    # Transpose: bring kept dims to front for both bra and ket
    # New order: kept_bra..., trace_bra..., kept_ket..., trace_ket...
    new_order = list(perm) + [p + n for p in perm]
    rho_permuted = rho_tensor.transpose(new_order)

    # Reshape to (d_keep, d_trace, d_keep, d_trace)
    d_keep = int(np.prod([dims[i] for i in keep]))
    d_trace = int(np.prod([dims[i] for i in trace_out]))
    rho_reshaped = rho_permuted.reshape(d_keep, d_trace, d_keep, d_trace)

    # Trace over the trace dimensions: sum over axis1=axis3
    rho_reduced = np.trace(rho_reshaped, axis1=1, axis2=3)

    return rho_reduced


def quantum_mutual_information(rho_AB, dims_A, dims_B):
    """I(A:B) = H(A) + H(B) - H(AB)."""
    H_AB = von_neumann_entropy(rho_AB)
    rho_A = ptrace(rho_AB, [0], [np.prod(dims_A), np.prod(dims_B)]) if len(dims_A) == 1 else ptrace(rho_AB, list(range(len(dims_A))), list(dims_A) + list(dims_B))
    rho_B = ptrace(rho_AB, list(range(len(dims_A), len(dims_A)+len(dims_B))), list(dims_A) + list(dims_B))
    H_A = von_neumann_entropy(rho_A)
    H_B = von_neumann_entropy(rho_B)
    return H_A + H_B - H_AB


def conditional_mutual_information(rho_ABC, dims_A, dims_B, dims_C):
    """I(A:C|B) = H(AB) + H(BC) - H(B) - H(ABC)."""
    H_ABC = von_neumann_entropy(rho_ABC)

    rho_AB = ptrace(rho_ABC, list(range(len(dims_A) + len(dims_B))),
                    list(dims_A) + list(dims_B) + list(dims_C))
    rho_BC = ptrace(rho_ABC, list(range(len(dims_A), len(dims_A) + len(dims_B) + len(dims_C))),
                    list(dims_A) + list(dims_B) + list(dims_C))
    rho_B = ptrace(rho_ABC, list(range(len(dims_A), len(dims_A) + len(dims_B))),
                   list(dims_A) + list(dims_B) + list(dims_C))

    H_AB = von_neumann_entropy(rho_AB)
    H_BC = von_neumann_entropy(rho_BC)
    H_B = von_neumann_entropy(rho_B)

    return H_AB + H_BC - H_B - H_ABC


# ============================================================
# §2. Buscemi process construction
# ============================================================

def maximally_entangled_state(d):
    """|Phi+⟩ = (1/√d) Σ_i |ii⟩."""
    psi = np.zeros(d * d, dtype=complex)
    for i in range(d):
        psi[i * d + i] = 1.0 / np.sqrt(d)
    return np.outer(psi, psi.conj())


def random_unitary(d, seed=None):
    """Generate a random unitary matrix of dimension d."""
    rng = np.random.RandomState(seed)
    # Use QR decomposition of random complex matrix
    A = rng.randn(d, d) + 1j * rng.randn(d, d)
    Q, R = np.linalg.qr(A)
    # Ensure det = 1 (make it exactly unitary with proper phase)
    return Q


def run_buscemi_process(U_QE, gamma_E, d_Q, d_E, return_full_state=False):
    """
    Run one step of Buscemi process: t₀ → t_1.

    Args:
        U_QE: unitary matrix of shape (d_Q * d_E, d_Q * d_E)
        gamma_E: initial environment state, shape (d_E, d_E)
        d_Q: system Hilbert space dimension
        d_E: environment Hilbert space dimension

    Returns:
        sigma_RQ'E': the Choi state at t_1
        Also computes I(R;E'|Q')_1
    """
    d_R = d_Q  # reference is isomorphic to system

    # t₀: ρ_RQE = Phi+_RQ x gamma_E
    phi_RQ = maximally_entangled_state(d_Q)
    rho_RQE = np.kron(phi_RQ, gamma_E)

    # t_1: sigma_RQ'E' = (I_R x U_QE) ρ_RQE (I_R x U_QE)†
    I_R = np.eye(d_R, dtype=complex)
    U_total = np.kron(I_R, U_QE)
    sigma_RQpEp = U_total @ rho_RQE @ U_total.conj().T

    # Compute I(R;E'|Q')_1
    # dims: [d_R, d_Q, d_E]
    cmi = conditional_mutual_information(sigma_RQpEp, [d_R], [d_Q], [d_E])
    qmi_RQ = quantum_mutual_information(
        ptrace(sigma_RQpEp, [0, 1], [d_R, d_Q, d_E]),
        [d_R], [d_Q]
    )
    qmi_RE = quantum_mutual_information(
        ptrace(sigma_RQpEp, [0, 2], [d_R, d_Q, d_E]),
        [d_R], [d_E]
    )

    if return_full_state:
        return sigma_RQpEp, cmi, qmi_RQ, qmi_RE
    return cmi, qmi_RQ, qmi_RE


# ============================================================
# §3. Single copy baseline
# ============================================================

print("=" * 70)
print("LP37 Lemma Test: QCMI Additivity over Independent Channels")
print("=" * 70)

# Single qubit system + single qubit environment
d_Q = 2
d_E = 2

# Random unitary for Q-E interaction
U_QE = random_unitary(d_Q * d_E, seed=42)
# Initial environment: mixed state (allows non-zero QCMI)
gamma_E = np.array([[0.7, 0.0], [0.0, 0.3]])  # thermal-like

cmi_single, qmi_RQ_single, qmi_RE_single = run_buscemi_process(U_QE, gamma_E, d_Q, d_E)

print(f"\n--- Single copy ---")
print(f"d_Q = {d_Q}, d_E = {d_E}")
print(f"I(R;E'|Q')_1 = {cmi_single:.6f}")
print(f"I(R;Q')_1     = {qmi_RQ_single:.6f}")
print(f"I(R;E')_1     = {qmi_RE_single:.6f}")
print(f"I(R;Q'E')_1   = {qmi_RQ_single + cmi_single:.6f}")  # chain rule
print(f"Check: 2*log2(d_Q) = {2*np.log2(d_Q):.6f} (should = I(R;Q'E')_1)")

# ============================================================
# §4. Two independent copies (test additivity)
# ============================================================

print(f"\n--- Two independent copies ---")

# System: Q_1 x Q_2, each d=2 → d_Q_total = 4
# Environment: E_1 x E_2, each d=2 → d_E_total = 4
d_Q2 = d_Q * d_Q  # 4
d_E2 = d_E * d_E  # 4

# Independent unitary: U_QE x U_QE (but we need to reorder tensor factors)
# Hilbert space ordering: Q_1 x Q_2 x E_1 x E_2
# U_QE acts on Q_1xE_1, same U_QE on Q_2xE_2
# We need a swap to bring Q_1-E_1 together, Q_2-E_2 together

# U_total = SWAP_{Q_2↔E_1} · (U_QE x U_QE) · SWAP_{Q_2↔E_1}
# where SWAP_{Q_2↔E_1} permutes the Hilbert space ordering:
#   Q_1xQ_2xE_1xE_2 → Q_1xE_1xQ_2xE_2

# Build permutation matrix for Q_1xQ_2xE_1xE_2 → Q_1xE_1xQ_2xE_2
dims_in = [d_Q, d_Q, d_E, d_E]
dims_mid = [d_Q, d_E, d_Q, d_E]

# Explicit construction of the permutation (swap subsystems 1 and 2)
# where indices: 0=Q_1, 1=Q_2, 2=E_1, 3=E_2 → 0=Q_1, 1=E_1, 2=Q_2, 3=E_2
perm = [0, 2, 1, 3]  # Q_1 stays, E_1 moves to pos 1, Q_2 moves to pos 2, E_2 stays
D = int(np.prod(dims_in))
P = np.zeros((D, D), dtype=complex)
for i0 in range(dims_in[0]):
    for i1 in range(dims_in[1]):
        for i2 in range(dims_in[2]):
            for i3 in range(dims_in[3]):
                idx_in = ((i0 * dims_in[1] + i1) * dims_in[2] + i2) * dims_in[3] + i3
                # Permuted indices
                idx_list = [i0, i1, i2, i3]
                p0, p1, p2, p3 = [idx_list[p] for p in perm]
                idx_out = ((p0 * dims_mid[1] + p1) * dims_mid[2] + p2) * dims_mid[3] + p3
                P[idx_out, idx_in] = 1.0

# Total unitary for two copies
U_independent = np.kron(U_QE, U_QE)  # acts on Q_1xE_1 x Q_2xE_2 ordering
U_total2 = P.conj().T @ U_independent @ P  # bring to Q_1xQ_2xE_1xE_2 ordering

# Initial state: Phi+_{R_1Q_1} x Phi+_{R_2Q_2} x gamma_{E_1} x gamma_{E_2}
phi_R1Q1 = maximally_entangled_state(d_Q)
phi_R2Q2 = maximally_entangled_state(d_Q)
rho_RQE_2 = np.kron(np.kron(np.kron(phi_R1Q1, phi_R2Q2), gamma_E), gamma_E)

# Reference dimensions: 4 (R_1xR_2)
d_R2 = d_Q * d_Q

# Apply unitary
I_R2 = np.eye(d_R2, dtype=complex)
U_total_full = np.kron(I_R2, U_total2)
sigma2 = U_total_full @ rho_RQE_2 @ U_total_full.conj().T

# Compute QCMI for two copies
# dims: [R=4, Q=4, E=4]
cmi_two = conditional_mutual_information(sigma2, [d_R2], [d_Q2], [d_E2])

# Also compute per-copy QCMI by tracing out the other copy
# Copy 1: trace out R_2, Q_2, E_2
sigma_copy1 = ptrace(sigma2, [0, 1, 2], [d_Q, d_Q, d_Q, d_Q, d_E, d_E])
# Wait, dims are: R_1(d_Q), R_2(d_Q), Q_1(d_Q), Q_2(d_Q), E_1(d_E), E_2(d_E)
# keep indices 0 (R_1), 2 (Q_1), 4 (E_1)
sigma_copy1 = ptrace(sigma2, [0, 2, 4], [d_Q, d_Q, d_Q, d_Q, d_E, d_E])
cmi_copy1 = conditional_mutual_information(sigma_copy1, [d_Q], [d_Q], [d_E])

sigma_copy2 = ptrace(sigma2, [1, 3, 5], [d_Q, d_Q, d_Q, d_Q, d_E, d_E])
cmi_copy2 = conditional_mutual_information(sigma_copy2, [d_Q], [d_Q], [d_E])

print(f"d_Q_total = {d_Q2}, d_E_total = {d_E2}")
print(f"I(R_1R_2;E_1'E_2'|Q_1'Q_2')_1 = {cmi_two:.6f}")
print(f"I(R_1;E_1'|Q_1')_1 (copy 1)  = {cmi_copy1:.6f}")
print(f"I(R_2;E_2'|Q_2')_1 (copy 2)  = {cmi_copy2:.6f}")
print(f"Sum of single copies         = {cmi_copy1 + cmi_copy2:.6f}")
print(f"Deviation from additivity    = {cmi_two - (cmi_copy1 + cmi_copy2):.6f}")

# ============================================================
# §5. Test with correlated environment (non-product gamma_E1E2)
# ============================================================

print(f"\n--- Correlated environment test ---")
# This tests: when E_1 and E_2 are initially CORRELATED (not independent),
# does the additivity break? This simulates a "shared causal node".

# Correlated initial environment state:
# gamma_E1E2 = classical mixture with correlation
gamma_corr = np.zeros((4, 4), dtype=complex)
gamma_corr[0, 0] = 0.35  # |00⟩
gamma_corr[1, 1] = 0.15  # |01⟩
gamma_corr[2, 2] = 0.15  # |10⟩
gamma_corr[3, 3] = 0.35  # |11⟩
# This gives I(E_1;E_2) > 0 (correlated but not maximally)

rho_RQE_corr = np.kron(np.kron(np.kron(phi_R1Q1, phi_R2Q2),
                                np.zeros((4,4), dtype=complex)), np.zeros((1,1)))
# Actually, let me just do it properly
rho_RQE_corr = np.kron(np.kron(phi_R1Q1, phi_R2Q2), gamma_corr)

sigma_corr = U_total_full @ rho_RQE_corr @ U_total_full.conj().T

cmi_corr = conditional_mutual_information(sigma_corr, [d_R2], [d_Q2], [d_E2])
sigma_corr_copy1 = ptrace(sigma_corr, [0, 2, 4], [d_Q, d_Q, d_Q, d_Q, d_E, d_E])
sigma_corr_copy2 = ptrace(sigma_corr, [1, 3, 5], [d_Q, d_Q, d_Q, d_Q, d_E, d_E])
cmi_corr1 = conditional_mutual_information(sigma_corr_copy1, [d_Q], [d_Q], [d_E])
cmi_corr2 = conditional_mutual_information(sigma_corr_copy2, [d_Q], [d_Q], [d_E])

print(f"I(R_1R_2;E_1'E_2'|Q_1'Q_2')_1 = {cmi_corr:.6f}")
print(f"I(R_1;E_1'|Q_1')_1 (copy 1)  = {cmi_corr1:.6f}")
print(f"I(R_2;E_2'|Q_2')_1 (copy 2)  = {cmi_corr2:.6f}")
print(f"Sum of marginals             = {cmi_corr1 + cmi_corr2:.6f}")
print(f"Deviation from additivity    = {cmi_corr - (cmi_corr1 + cmi_corr2):.6f}")

# ============================================================
# §6. Scan: does additivity hold for different unitaries?
# ============================================================

print(f"\n--- Additivity scan (10 random unitaries) ---")
print(f"{'Seed':>5s}  {'Single':>10s}  {'Two-copy':>10s}  {'Sum-single':>12s}  {'Δ':>10s}  {'2×Single':>10s}")
print("-" * 65)

for seed in range(10):
    U = random_unitary(d_Q * d_E, seed=seed + 100)
    cmi_s, _, _ = run_buscemi_process(U, gamma_E, d_Q, d_E)

    U_indep = np.kron(U, U)
    U_tot = P.conj().T @ U_indep @ P
    U_tot_full = np.kron(I_R2, U_tot)
    sig = U_tot_full @ np.kron(np.kron(np.kron(phi_R1Q1, phi_R2Q2), gamma_E), gamma_E) @ U_tot_full.conj().T
    cmi_2 = conditional_mutual_information(sig, [d_R2], [d_Q2], [d_E2])

    delta = cmi_2 - 2 * cmi_s
    print(f"{seed+100:5d}  {cmi_s:10.6f}  {cmi_2:10.6f}  {2*cmi_s:12.6f}  {delta:10.6f}  {'ADDITIVE' if abs(delta) < 1e-10 else '*** BROKEN ***'}")

# ============================================================
# §7. The real test: causal diamond (b_1=1) vs chain (b_1=0)
# ============================================================

print(f"\n{'='*70}")
print(f"§7. Causal structure test: chain (b_1=0) vs diamond (b_1=1)")
print(f"{'='*70}")

# We need 3 subsystems to form a Hasse cycle.
# Simplest: Q_a, Q_b (two system qubits), E_1, E_2 (two environment qubits)
#
# Chain (b_1=0): Q_a → E_1 → Q_b → E_2  (linear, no cycle)
#   U_chain = U_{Q_a,E_1} · U_{E_1,Q_b} · U_{Q_b,E_2}
#
# Diamond (b_1=1): Q_a → E_1, Q_a → E_2, E_1 → Q_b, E_2 → Q_b (K_{2,2}, b_1=1)
#   U_diamond: Q_a interacts with both E_1,E_2; both E_1,E_2 interact with Q_b

# System: Q_a (d=2), Q_b (d=2) → total d_Q = 4
# Environment: E_1 (d=2), E_2 (d=2) → total d_E = 4
# Reference: R_a (d=2), R_b (d=2) → total d_R = 4

# --- Chain unitary ---
# Hilbert space order: R_a x R_b x Q_a x Q_b x E_1 x E_2
# Chain: Q_a↔E_1, E_1↔Q_b, Q_b↔E_2

# Build chain unitary: U = U_{Q_b,E_2} · U_{E_1,Q_b} · U_{Q_a,E_1}
# Each two-qubit unitary acts on specific subsystems

def build_two_qubit_unitary_on_subsystem(U_2q, target_a, target_b, dims):
    """
    Embed a 4x4 two-qubit unitary acting on subsystems target_a and target_b
    into the full Hilbert space with dimensions dims.
    """
    n = len(dims)
    D = int(np.prod(dims))
    U_full = np.eye(D, dtype=complex)

    # We need to permute so target_a and target_b are adjacent at the front,
    # apply U_2q x I_rest, then permute back

    # Permutation to bring targets to front
    remaining = [i for i in range(n) if i != target_a and i != target_b]
    perm = [target_a, target_b] + remaining

    # Build permutation matrix
    P = np.zeros((D, D), dtype=complex)
    for indices in np.ndindex(*dims):
        idx_in = 0
        stride = 1
        for i in range(n-1, -1, -1):
            idx_in += indices[i] * stride
            stride *= dims[i]

        # Permute
        perm_indices = [indices[p] for p in perm]
        idx_out = 0
        stride = 1
        permed_dims = [dims[p] for p in perm]
        for i in range(n-1, -1, -1):
            idx_out += perm_indices[i] * stride
            stride *= permed_dims[i]

        P[idx_out, idx_in] = 1.0

    # U_2q x I on remaining subsystems
    d_rest = int(D / (dims[target_a] * dims[target_b]))
    U_lifted = np.kron(U_2q, np.eye(d_rest, dtype=complex))

    return P.conj().T @ U_lifted @ P


# Random 2-qubit unitaries
U_qa_e1 = random_unitary(4, seed=201)
U_e1_qb = random_unitary(4, seed=202)
U_qb_e2 = random_unitary(4, seed=203)

# Subsystem indices: 0=R_a, 1=R_b, 2=Q_a, 3=Q_b, 4=E_1, 5=E_2
all_dims = [d_Q, d_Q, d_Q, d_Q, d_E, d_E]

# Chain unitaries
U_chain_qa_e1 = build_two_qubit_unitary_on_subsystem(U_qa_e1, 2, 4, all_dims)  # Q_a, E_1
U_chain_e1_qb = build_two_qubit_unitary_on_subsystem(U_e1_qb, 4, 3, all_dims)  # E_1, Q_b
U_chain_qb_e2 = build_two_qubit_unitary_on_subsystem(U_qb_e2, 3, 5, all_dims)  # Q_b, E_2

# Chain total: apply sequentially (note order: Q_a→E_1, then E_1→Q_b, then Q_b→E_2)
U_chain_total = U_chain_qb_e2 @ U_chain_e1_qb @ U_chain_qa_e1

# Diamond: add Q_a↔E_2 interaction (already have Q_a↔E_1 and E_1↔Q_b and E_2↔Q_b)
U_qa_e2 = random_unitary(4, seed=204)
U_diamond_qa_e2 = build_two_qubit_unitary_on_subsystem(U_qa_e2, 2, 5, all_dims)  # Q_a, E_2

# Diamond total: Q_a interacts with both E_1 and E_2 (in either order), then both feed to Q_b
# U_diamond = U_{E_1,Q_b} · U_{Q_b,E_2} · U_{Q_a,E_2} · U_{Q_a,E_1}
# Note: U_{Q_a,E_1} and U_{Q_a,E_2} don't commute in general
U_diamond_total = U_chain_e1_qb @ U_chain_qb_e2 @ U_diamond_qa_e2 @ U_chain_qa_e1

# Initial state: Phi+_{R_a,Q_a} x Phi+_{R_b,Q_b} x gamma_{E_1,E_2}
# For chain: gamma is product
gamma_chain = np.kron(gamma_E, gamma_E)  # E_1 ⊥ E_2
rho_RQE_chain = np.kron(np.kron(phi_R1Q1, phi_R2Q2), gamma_chain)

# For diamond: same initial state
rho_RQE_diamond = np.kron(np.kron(phi_R1Q1, phi_R2Q2), gamma_chain)

# Apply unitaries (R is not acted on, identity on R_a,R_b)
I_R_total = np.eye(d_Q * d_Q, dtype=complex)
U_chain_full = np.kron(I_R_total, U_chain_total)
U_diamond_full = np.kron(I_R_total, U_diamond_total)

sigma_chain = U_chain_full @ rho_RQE_chain @ U_chain_full.conj().T
sigma_diamond = U_diamond_full @ rho_RQE_diamond @ U_diamond_full.conj().T

# Compute QCMI for each
# State ordering: R_a,R_b, Q_a,Q_b, E_1,E_2
# dims: [2, 2, 2, 2, 2, 2]

# QCMI = I(R;E|Q) where R=(R_a,R_b), Q=(Q_a,Q_b), E=(E_1,E_2)
d_R_ab = d_Q * d_Q  # 4
d_Q_ab = d_Q * d_Q  # 4
d_E_ab = d_E * d_E  # 4

cmi_chain = conditional_mutual_information(sigma_chain, [d_R_ab], [d_Q_ab], [d_E_ab])
cmi_diamond = conditional_mutual_information(sigma_diamond, [d_R_ab], [d_Q_ab], [d_E_ab])

print(f"\nChain (b_1=0):   I(R;E'|Q')_1 = {cmi_chain:.6f}")
print(f"Diamond (b_1=1): I(R;E'|Q')_1 = {cmi_diamond:.6f}")
print(f"Difference (diamond - chain)  = {cmi_diamond - cmi_chain:.6f}")

# Also compute per-channel decomposition for diamond
# Channel 1: Q_a → E_1 → Q_b
# Channel 2: Q_a → E_2 → Q_b
# Check if diamond QCMI ≈ sum of two "half-diamond" QCMIs

print(f"\n--- Per-channel decomposition ---")

# "Half-diamond 1": only Q_a↔E_1↔Q_b active (E_2 idle)
U_half1 = U_chain_e1_qb @ U_chain_qa_e1  # remove Q_a↔E_2 and Q_b↔E_2
U_half1_full = np.kron(I_R_total, U_half1)
sigma_half1 = U_half1_full @ rho_RQE_chain @ U_half1_full.conj().T
cmi_half1 = conditional_mutual_information(sigma_half1, [d_R_ab], [d_Q_ab], [d_E_ab])

# "Half-diamond 2": only Q_a↔E_2↔Q_b active (E_1 idle)
U_half2 = U_chain_qb_e2 @ U_diamond_qa_e2
U_half2_full = np.kron(I_R_total, U_half2)
sigma_half2 = U_half2_full @ rho_RQE_chain @ U_half2_full.conj().T
cmi_half2 = conditional_mutual_information(sigma_half2, [d_R_ab], [d_Q_ab], [d_E_ab])

print(f"Half1 (Q_a→E_1→Q_b): I(R;E'|Q')_1 = {cmi_half1:.6f}")
print(f"Half2 (Q_a→E_2→Q_b): I(R;E'|Q')_1 = {cmi_half2:.6f}")
print(f"Sum of halves               = {cmi_half1 + cmi_half2:.6f}")
print(f"Full diamond                = {cmi_diamond:.6f}")
print(f"Deviation                   = {cmi_diamond - (cmi_half1 + cmi_half2):.6f}")

# ============================================================
# §8. Summary
# ============================================================

print(f"\n{'='*70}")
print(f"SUMMARY")
print(f"{'='*70}")
print(f"1. Independent copies (product env): additivity test")
print(f"2. Independent copies (correlated env): correlation breaks additivity?")
print(f"3. Chain (b_1=0) vs Diamond (b_1=1): causal topology effect on QCMI")
print(f"4. Per-channel sum vs full diamond: independent-channel additivity")

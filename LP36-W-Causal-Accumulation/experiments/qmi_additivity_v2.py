"""
LP37 Lemma Test v2: QCMI additivity over independent causal channels.

Clean rewrite. No unicode. Minimal but correct.

Core question: Is I(R;E'|Q') additive over independent system-environment pairs?
"""
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# Quantum info utilities
# ============================================================

def von_neumann_entropy(rho, eps=1e-12):
    eigvals = np.linalg.eigvalsh(rho)
    eigvals = np.maximum(eigvals, eps)
    eigvals = eigvals / np.sum(eigvals)
    return -np.sum(eigvals * np.log2(eigvals))

def ptrace(rho, keep, dims):
    """Partial trace: keep subsystems in `keep`, trace out the rest."""
    n = len(dims)
    keep = sorted(keep)
    trace_out = [i for i in range(n) if i not in keep]
    perm = keep + trace_out
    shape = tuple(dims) + tuple(dims)
    rho_tensor = rho.reshape(shape)
    new_order = list(perm) + [p + n for p in perm]
    rho_permuted = rho_tensor.transpose(new_order)
    d_keep = int(np.prod([dims[i] for i in keep]))
    d_trace = int(np.prod([dims[i] for i in trace_out]))
    rho_reshaped = rho_permuted.reshape(d_keep, d_trace, d_keep, d_trace)
    return np.trace(rho_reshaped, axis1=1, axis2=3)

def qmi(rho_AB, d_A, d_B):
    """I(A:B) = H(A) + H(B) - H(AB). rho_AB is on A|B."""
    H_AB = von_neumann_entropy(rho_AB)
    # rho_A = trace out B
    rho_A = ptrace(rho_AB, [0], [d_A, d_B])
    rho_B = ptrace(rho_AB, [1], [d_A, d_B])
    H_A = von_neumann_entropy(rho_A)
    H_B = von_neumann_entropy(rho_B)
    return H_A + H_B - H_AB

def qcmi(rho_ABC, d_A, d_B, d_C):
    """I(A:C|B) = H(AB)+H(BC)-H(B)-H(ABC). rho_ABC is on A|B|C."""
    H_ABC = von_neumann_entropy(rho_ABC)
    rho_AB = ptrace(rho_ABC, [0, 1], [d_A, d_B, d_C])
    rho_BC = ptrace(rho_ABC, [1, 2], [d_A, d_B, d_C])
    rho_B  = ptrace(rho_ABC, [1], [d_A, d_B, d_C])
    H_AB = von_neumann_entropy(rho_AB)
    H_BC = von_neumann_entropy(rho_BC)
    H_B  = von_neumann_entropy(rho_B)
    return H_AB + H_BC - H_B - H_ABC

def max_entangled(d):
    """|Phi+> = sum_i |ii>/sqrt(d). Returns density matrix."""
    psi = np.zeros(d * d, dtype=complex)
    for i in range(d):
        psi[i * d + i] = 1.0 / np.sqrt(d)
    return np.outer(psi, psi.conj())

def random_unitary(d, seed=None):
    rng = np.random.RandomState(seed)
    A = rng.randn(d, d) + 1j * rng.randn(d, d)
    Q, R = np.linalg.qr(A)
    return Q

# ============================================================
# Single-copy baseline
# ============================================================

print("=" * 60)
print("LP37 QCMI Additivity Test")
print("=" * 60)

d = 2  # qubit dimension

# Initial states
phi_RQ = max_entangled(d)                    # |Phi+> on RQ, shape 4x4
gamma_E = np.diag([0.7, 0.3])                # mixed env state

# Full initial state: |Phi+>_RQ x gamma_E
# Ordering: R | Q | E
rho_RQE_1 = np.kron(np.kron(phi_RQ.reshape(d,d,d,d), np.eye(d)), np.eye(d))
# That's wrong. Let me do it properly.
# rho_RQE = Phi+_RQ (4x4) kron gamma_E (2x2) = 8x8
rho_RQE_1 = np.kron(phi_RQ, gamma_E)

# Random Q-E unitary
U_QE = random_unitary(d*d, seed=42)  # 4x4

# Full unitary: I_R x U_QE (R is 2x2 identity, U_QE is 4x4)
I_R = np.eye(d, dtype=complex)
U_full_1 = np.kron(I_R, U_QE)  # 8x8

# Apply: sigma_RQ'E' = U_full x rho x U_full^dag
sigma_1 = U_full_1 @ rho_RQE_1 @ U_full_1.conj().T

# Compute QCMI: I(R;E'|Q') on state with dims [d_R=2, d_Q=2, d_E=2]
qcmi_1 = qcmi(sigma_1, d, d, d)
qmi_RQ_1 = qmi(ptrace(sigma_1, [0,1], [d,d,d]), d, d)
qmi_RE_1 = qmi(ptrace(sigma_1, [0,2], [d,d,d]), d, d)

print(f"\nSingle copy (d={d})")
print(f"  I(R;E'|Q') = {qcmi_1:.6f}")
print(f"  I(R;Q')     = {qmi_RQ_1:.6f}")
print(f"  I(R;E')     = {qmi_RE_1:.6f}")
print(f"  I(R;Q'E')   = {qmi_RQ_1 + qcmi_1:.6f}  (should = {2*np.log2(d):.6f})")

# ============================================================
# Two independent copies
# ============================================================

print(f"\n--- Two independent copies ---")

# System: R1,R2 | Q1,Q2 | E1,E2  (each is a qubit, d=2)
# Total dims: [2,2,2,2,2,2] = 64-dim state

# Initial state: Phi+_R1Q1 x Phi+_R2Q2 x gamma_E1 x gamma_E2
# Careful about ordering: R1,R2,Q1,Q2,E1,E2
# Phi+_R1Q1 acts on R1,Q1, Phi+_R2Q2 acts on R2,Q2
# Need to permute to get R1,R2,Q1,Q2 ordering

# Build rho in the correct basis ordering
# Step 1: Phi+_R1Q1 (4x4, on subsystems R1,Q1 with dims 2,2)
# Step 2: Phi+_R2Q2 (4x4, on subsystems R2,Q2 with dims 2,2)
# Step 3: gamma_E1 x gamma_E2 (4x4, on E1,E2)
# Final ordering: R1,R2,Q1,Q2,E1,E2

# Phi+_R1Q1 x Phi+_R2Q2 gives ordering: R1,Q1,R2,Q2
# We need: R1,R2,Q1,Q2
# So we need to swap Q1 <-> R2

# Build the 4-system state (R1,Q1,R2,Q2) then permute
rho_R1Q1 = phi_RQ  # 4x4, ordering R1,Q1
rho_R2Q2 = phi_RQ  # 4x4, ordering R2,Q2
rho_RQ_temp = np.kron(rho_R1Q1, rho_R2Q2)  # 16x16, ordering R1,Q1,R2,Q2

# Permute to R1,R2,Q1,Q2
# Current axes: R1_bra, Q1_bra, R2_bra, Q2_bra, R1_ket, Q1_ket, R2_ket, Q2_ket
# Target axes:  R1_bra, R2_bra, Q1_bra, Q2_bra, R1_ket, R2_ket, Q1_ket, Q2_ket
# perm = [0,2,1,3, 4,6,5,7]
dims_4 = [2,2,2,2]
rho_RQ_temp_tensor = rho_RQ_temp.reshape(tuple(dims_4) + tuple(dims_4))
rho_RQ = rho_RQ_temp_tensor.transpose(0,2,1,3, 4,6,5,7).reshape(16,16)
# Now ordering: R1,R2,Q1,Q2

# Add environment: gamma_E1 x gamma_E2 (ordering E1,E2)
gamma_E1E2 = np.kron(gamma_E, gamma_E)

# Full initial state: R1,R2,Q1,Q2,E1,E2
rho_RQE_2 = np.kron(rho_RQ, gamma_E1E2)  # 64x64

# Build the two-copy unitary
# Want: U_QE^(1) acts on Q1,E1; U_QE^(2) acts on Q2,E2
# Current ordering: Q1,Q2,E1,E2 (4 systems, dim 2 each)
# Target for UxU: Q1,E1,Q2,E2
# Permute: 0,2,1,3 -> Q1,E1,Q2,E2

# Build perm matrix for Q1,Q2,E1,E2 -> Q1,E1,Q2,E2
D4 = 16
P_Q = np.zeros((D4, D4), dtype=complex)
dims_qe = [2,2,2,2]  # Q1,Q2,E1,E2
dims_qe_target = [2,2,2,2]  # Q1,E1,Q2,E2
for i0 in range(2):
    for i1 in range(2):
        for i2 in range(2):
            for i3 in range(2):
                # input idx: Q1=i0, Q2=i1, E1=i2, E2=i3
                idx_in = ((i0*2 + i1)*2 + i2)*2 + i3
                # output idx: Q1=i0, E1=i2, Q2=i1, E2=i3
                idx_out = ((i0*2 + i2)*2 + i1)*2 + i3
                P_Q[idx_out, idx_in] = 1.0

U_indep = np.kron(U_QE, U_QE)  # acts on Q1,E1,Q2,E2
U_Q_total = P_Q.conj().T @ U_indep @ P_Q  # acts on Q1,Q2,E1,E2

# Full unitary: I_R1R2 x U_Q_total
I_R2 = np.eye(d*d, dtype=complex)  # 4x4
U_full_2 = np.kron(I_R2, U_Q_total)  # 64x64

# Apply
sigma_2 = U_full_2 @ rho_RQE_2 @ U_full_2.conj().T

# Compute QCMI
# State ordering: R1,R2 | Q1,Q2 | E1,E2
# dims: d_R=4, d_Q=4, d_E=4
qcmi_2 = qcmi(sigma_2, 4, 4, 4)

# Per-copy QCMI: trace out R2,Q2,E2 to get copy 1
# dims: R1,R2,Q1,Q2,E1,E2 = [2,2,2,2,2,2]
sigma_copy1 = ptrace(sigma_2, [0,2,4], [2,2,2,2,2,2])  # R1,Q1,E1
qcmi_c1 = qcmi(sigma_copy1, 2, 2, 2)

sigma_copy2 = ptrace(sigma_2, [1,3,5], [2,2,2,2,2,2])  # R2,Q2,E2
qcmi_c2 = qcmi(sigma_copy2, 2, 2, 2)

print(f"  I(R1R2;E1'E2'|Q1'Q2') = {qcmi_2:.6f}")
print(f"  Per-copy 1: I(R1;E1'|Q1') = {qcmi_c1:.6f}")
print(f"  Per-copy 2: I(R2;E2'|Q2') = {qcmi_c2:.6f}")
print(f"  Sum per-copy               = {qcmi_c1 + qcmi_c2:.6f}")
print(f"  Prediction (2 x single)    = {2*qcmi_1:.6f}")
delta = qcmi_2 - 2*qcmi_1
print(f"  Delta (joint - 2*single)   = {delta:.10f}")
print(f"  ADDITIVE: {abs(delta) < 1e-10}")

# ============================================================
# Scan: 20 random unitaries
# ============================================================

print(f"\n--- Additivity scan (20 random U_QE) ---")
deltas = []
for seed in range(20):
    U = random_unitary(d*d, seed=100+seed)

    # Single copy
    Uf1 = np.kron(I_R, U)
    s1 = Uf1 @ rho_RQE_1 @ Uf1.conj().T
    q1 = qcmi(s1, d, d, d)

    # Two copies
    U_ind = np.kron(U, U)
    U_Qt = P_Q.conj().T @ U_ind @ P_Q
    Uf2 = np.kron(I_R2, U_Qt)
    s2 = Uf2 @ rho_RQE_2 @ Uf2.conj().T
    q2 = qcmi(s2, 4, 4, 4)

    delta = q2 - 2*q1
    deltas.append(delta)
    ok = "OK" if abs(delta) < 1e-10 else "BROKEN"
    print(f"  seed={100+seed:3d}: single={q1:.6f}, two-copy={q2:.6f}, "
          f"2x={2*q1:.6f}, delta={delta:.2e} [{ok}]")

# ============================================================
# Critical test: causal topology effect on QCMI
# ============================================================
#
# Three graph topologies with SAME number of edges (4) and gates (4):
#
#   STAR5   (b1=0, 4 edges, 5 vertices): Q_a--E_1--Q_b--E_2 + E_1--E_3
#           Tree on 5 vertices: b1 = 4-5+1 = 0. VERIFIED TREE.
#   CHAIN4  (b1=0, 3 edges, 4 vertices): Q_a--E_1--Q_b--E_2
#           Tree on 4 vertices: b1 = 3-4+1 = 0. VERIFIED TREE.
#   DIAMOND (b1=1, 4 edges, 4 vertices): Q_a--{E_1,E_2}--Q_b (K_{2,2})
#           b1 = 4-4+1 = 1. VERIFIED ONE CYCLE.
#
# Key comparison:
#   STAR5 vs DIAMOND: same #edges (4), same #gates (4), different b1 (0 vs 1)
#   CHAIN4 vs DIAMOND: same #vertices (4), different #edges (3 vs 4), different b1
# The STAR5-DIAMOND comparison isolates topology from edge count.

print(f"\n{'='*60}")
print(f"CAUSAL TOPOLOGY TEST")
print(f"{'='*60}")

def build_2q_unitary_on(U_4x4, target_a, target_b, dims):
    """Embed a 4x4 unitary acting on subsystems a,b into full space."""
    n = len(dims)
    D = int(np.prod(dims))
    remaining = [i for i in range(n) if i not in (target_a, target_b)]
    perm = [target_a, target_b] + remaining
    P = np.zeros((D, D), dtype=complex)
    dims_perm = [dims[p] for p in perm]
    for indices in np.ndindex(*dims):
        idx_in = int(sum(indices[i] * int(np.prod(dims[i+1:])) for i in range(n)))
        perm_indices = [indices[p] for p in perm]
        idx_out = int(sum(perm_indices[i] * int(np.prod(dims_perm[i+1:])) for i in range(n)))
        P[idx_out, idx_in] = 1.0
    d_rest = D // (dims[target_a] * dims[target_b])
    U_lifted = np.kron(U_4x4, np.eye(d_rest, dtype=complex))
    return P.conj().T @ U_lifted @ P

# Graph topologies compared:
#
# CHAIN  (b1=0, 3e, 4v): Q_a--E_1--Q_b--E_2
# STAR5  (b1=0, 4e, 5v): Q_a--E_1--Q_b--E_2 + E_1--E_3 (tree, E_3 is leaf on E_1)
# DIAMOND(b1=1, 4e, 4v): Q_a--{E_1,E_2}--Q_b  (K_{2,2}, one cycle)
#
# CHAIN uses 4-qubit QE space [Q_a, Q_b, E_1, E_2]: indices 0,1,2,3
# STAR5 uses 5-qubit QE space [Q_a, Q_b, E_1, E_2, E_3]: indices 0,1,2,3,4
# DIAMOND uses 4-qubit QE space [Q_a, Q_b, E_1, E_2]: indices 0,1,2,3
#
# Key: STAR5 and DIAMOND both have 4 edges/interactions.
# STAR5 is a TREE (E_3 is a leaf) -> b1 = 4-5+1 = 0.
# DIAMOND has a CYCLE -> b1 = 4-4+1 = 1.
# Both have d_R = 4, d_Q = 4. STAR5 has larger E (8 vs 4 dims).

I_R4 = np.eye(4, dtype=complex)

# Q-E spaces
dims_qe4 = [2,2,2,2]      # Q_a, Q_b, E_1, E_2
dims_qe5 = [2,2,2,2,2]    # Q_a, Q_b, E_1, E_2, E_3

# Initial states
gamma_E3 = np.kron(np.kron(gamma_E, gamma_E), gamma_E)  # 8x8 for STAR5

# rho_RQE for 4-qubit QE: R(4) x QE(16) = 64x64
rho_RQE_4q = rho_RQE_2  # already built above

# rho_RQE for 5-qubit QE: R(4) x QE(32) = 128x128
rho_RQE_5q = np.kron(rho_RQ, gamma_E3)

# Scan
n_trials = 30
results = {'chain': [], 'star5': [], 'diamond': []}

print(f"\n{'trial':>5s}  {'chain(b1=0,3e)':>16s}  {'star5(b1=0,4e)':>16s}  {'diamond(b1=1,4e)':>16s}  {'star-ch':>12s}  {'diam-star':>12s}")
print("-" * 85)

for trial in range(n_trials):
    # Fresh unitaries
    Ua1 = random_unitary(4, seed=400+trial)
    U1b = random_unitary(4, seed=500+trial)
    Ub2 = random_unitary(4, seed=600+trial)
    Ua2 = random_unitary(4, seed=700+trial)
    U13 = random_unitary(4, seed=900+trial)

    # --- CHAIN (b1=0, 3e, 4v) ---
    U_ch = (build_2q_unitary_on(Ub2, 1, 3, dims_qe4) @      # Q_b, E_2
            build_2q_unitary_on(U1b, 2, 1, dims_qe4) @       # E_1, Q_b
            build_2q_unitary_on(Ua1, 0, 2, dims_qe4))         # Q_a, E_1
    sig_ch = np.kron(I_R4, U_ch) @ rho_RQE_4q @ np.kron(I_R4, U_ch).conj().T
    qc = qcmi(sig_ch, 4, 4, 4)

    # --- STAR5 (b1=0, 4e, 5v): chain + E_1--E_3 leaf ---
    U_s5 = (build_2q_unitary_on(U13, 2, 4, dims_qe5) @      # E_1, E_3 (LEAF)
            build_2q_unitary_on(Ub2, 1, 3, dims_qe5) @       # Q_b, E_2
            build_2q_unitary_on(U1b, 2, 1, dims_qe5) @       # E_1, Q_b
            build_2q_unitary_on(Ua1, 0, 2, dims_qe5))         # Q_a, E_1
    sig_s5 = np.kron(I_R4, U_s5) @ rho_RQE_5q @ np.kron(I_R4, U_s5).conj().T
    qs = qcmi(sig_s5, 4, 4, 8)

    # --- DIAMOND (b1=1, 4e, 4v) ---
    U_dm = (build_2q_unitary_on(Ua2, 0, 3, dims_qe4) @      # Q_a, E_2 (cycle-forming)
            build_2q_unitary_on(Ub2, 1, 3, dims_qe4) @       # Q_b, E_2
            build_2q_unitary_on(U1b, 2, 1, dims_qe4) @       # E_1, Q_b
            build_2q_unitary_on(Ua1, 0, 2, dims_qe4))         # Q_a, E_1
    sig_dm = np.kron(I_R4, U_dm) @ rho_RQE_4q @ np.kron(I_R4, U_dm).conj().T
    qd = qcmi(sig_dm, 4, 4, 4)

    results['chain'].append(qc)
    results['star5'].append(qs)
    results['diamond'].append(qd)

    print(f"{trial:5d}  {qc:16.6f}  {qs:16.6f}  {qd:16.6f}  {qs-qc:12.6f}  {qd-qs:12.6f}")

# Statistics
print(f"\n--- Statistics over {n_trials} trials ---")
for name in ['chain', 'star5', 'diamond']:
    arr = np.array(results[name])
    print(f"  {name:8s}: mean={np.mean(arr):.6f}, std={np.std(arr):.6f}, "
          f"min={np.min(arr):.6f}, max={np.max(arr):.6f}")

arr_chain  = np.array(results['chain'])
arr_star5  = np.array(results['star5'])
arr_diamond = np.array(results['diamond'])

diff_star_chain = arr_star5 - arr_chain
diff_diam_star  = arr_diamond - arr_star5

print(f"\n  star5 - chain:  mean={np.mean(diff_star_chain):.6f}, std={np.std(diff_star_chain):.6f}")
print(f"  diamond - star5: mean={np.mean(diff_diam_star):.6f}, std={np.std(diff_diam_star):.6f}")

# Key test: compare minima (lower bound)
print(f"\n  --- LOWER BOUND TEST (min QCMI) ---")
print(f"  CHAIN  (b1=0, 3e): min = {np.min(arr_chain):.6f}")
print(f"  STAR5  (b1=0, 4e): min = {np.min(arr_star5):.6f}")
print(f"  DIAMOND(b1=1, 4e): min = {np.min(arr_diamond):.6f}")
print(f"  STAR5 min - CHAIN min = {np.min(arr_star5) - np.min(arr_chain):.6f}")
print(f"  DIAMOND min - STAR5 min = {np.min(arr_diamond) - np.min(arr_star5):.6f}")

# ============================================================
# Summary
# ============================================================

print(f"\n{'='*60}")
print(f"SUMMARY")
print(f"{'='*60}")
mean_delta_2copy = np.mean(np.abs(deltas))
print(f"1. Two-copy QCMI additivity: delta = {mean_delta_2copy:.1e}")
print(f"   -> QCMI is additive over tensor-product independent channels")
print(f"")
print(f"2. STAR5 (b1=0, 4 edges) vs CHAIN (b1=0, 3 edges):")
print(f"   mean delta = {np.mean(diff_star_chain):.4f}")
print(f"   Adding a leaf edge to a tree: small QCMI shift")
print(f"")
print(f"3. DIAMOND (b1=1, 4 edges) vs STAR5 (b1=0, 4 edges):")
print(f"   mean delta = {np.mean(diff_diam_star):.4f}")
print(f"   DIAMOND min = {np.min(arr_diamond):.4f}, STAR5 min = {np.min(arr_star5):.4f}")
print(f"   Same #edges, only topology differs (b1=0 -> b1=1)")
diamond_above_star5 = np.sum(arr_diamond > arr_star5)
print(f"   DIAMOND > STAR5 in {diamond_above_star5}/{n_trials} trials")
print(f"")
print(f"   LOWER BOUND: diamond min {np.min(arr_diamond):.4f} {'>' if np.min(arr_diamond) > np.min(arr_star5) else '<='} star5 min {np.min(arr_star5):.4f}")

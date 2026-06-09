"""
b1 scan: QCMI scaling with first Betti number.
Wall 2 hypothesis test: I(R:QE) - I(R:Q) ∝ b1^α

Extended from b1_scaling.py with:
- b1 = 0, 1, 2, 3, 4 (with different cycle topologies)
- Statistical analysis (mean, std, min, max)
- Power-law fitting QCMI ∝ b1^α
- Output to markdown file

Key question: Does QCMI grow linearly with b1 (supporting Wall 2),
or saturate/decline (requiring fundamental revision)?
"""
import numpy as np
from scipy.optimize import curve_fit
import sys

# ========== Quantum information utilities ==========

def vn_entropy(rho, eps=1e-12):
    """von Neumann entropy S(rho) = -Tr(rho log2 rho)"""
    eigvals = np.linalg.eigvalsh(rho)
    eigvals = np.maximum(eigvals, eps)
    eigvals = eigvals / np.sum(eigvals)
    return -np.sum(eigvals * np.log2(eigvals))

def ptrace(rho, keep, dims):
    """Partial trace: keep specified qubit indices, trace out the rest."""
    n = len(dims)
    d_total = int(np.prod(dims))
    trace_out = [i for i in range(n) if i not in keep]
    dk = int(np.prod([dims[i] for i in keep]))
    result = np.zeros((dk, dk), dtype=complex)
    for bra in range(d_total):
        bra_bits = [(bra >> i) & 1 for i in range(n)]
        bt = tuple(bra_bits[i] for i in trace_out)
        bk = tuple(bra_bits[i] for i in keep)
        bki = sum(bk[i] * (2**i) for i in range(len(keep)))
        for ket in range(d_total):
            ket_bits = [(ket >> i) & 1 for i in range(n)]
            if tuple(ket_bits[i] for i in trace_out) == bt:
                kk = tuple(ket_bits[i] for i in keep)
                kki = sum(kk[i] * (2**i) for i in range(len(keep)))
                result[bki, kki] += rho[bra, ket]
    return result

def embed_lsb(U2q, a, b, nq):
    """Embed a 2-qubit gate on qubits (a,b) into nq-qubit Hilbert space.
    LSB encoding: qubit 0 is LSB (rightmost bit)."""
    D = 2**nq
    P = np.zeros((D, D), dtype=complex)
    rem = [i for i in range(nq) if i not in (a, b)]
    for i in range(D):
        bi = [(i >> k) & 1 for k in range(nq)]
        pb = [bi[a], bi[b]] + [bi[r] for r in rem]
        j = sum(pb[k] * (1 << k) for k in range(nq))
        P[j, i] = 1.0
    return P.conj().T @ np.kron(np.eye(2**(nq-2), dtype=complex), U2q) @ P

def random_u(d, s):
    """Haar-random unitary of dimension d using QR decomposition."""
    rng = np.random.RandomState(s)
    A = rng.randn(d, d) + 1j * rng.randn(d, d)
    Q, R = np.linalg.qr(A)
    return Q

def make_mixed_rho(n_E, p=0.7):
    """Buscemi mixed state: Phi+_{RQ} ⊗ γ_E^{⊗n_E}

    R = (R_a, R_b) is two-qubit reference purifying Q = (Q_a, Q_b).
    γ_E = diag(p, 1-p) is the single-qubit environment state.
    n_E = number of environment qubits.

    Returns rho_RQE after tracing out the F purifying system.
    Total system size before trace: 2 + 2 + n_E + n_E = 4 + 2*n_E qubits.
    After F trace: 4 + n_E qubits.
    """
    n_qe = 2 + n_E
    n_total = 2 + n_qe  # R_a,R_b + Q_a,Q_b + E_1..E_nE
    n_with_f = n_total + n_E  # + F_1..F_nE
    dim_F = 2**n_with_f
    psi = np.zeros(dim_F, dtype=complex)
    sp, sq = np.sqrt(p), np.sqrt(1 - p)

    for a in [0, 1]:
        for b in [0, 1]:
            for e_val in range(2**n_E):
                f_val = e_val  # F mirrors E for |psi_p> purification
                # Bit layout: R_a:0, R_b:1, Q_a:2, Q_b:3, E:4.., F:4+n_E..
                idx = (a << 0) | (b << 1) | (a << 2) | (b << 3) | (e_val << 4) | (f_val << (4 + n_E))
                amp = 0.5
                for i in range(n_E):
                    bit = (e_val >> i) & 1
                    amp *= (sp if bit == 0 else sq)
                psi[idx] = amp

    rho_full = np.outer(psi, psi.conj())
    keep = list(range(n_total))
    return ptrace(rho_full, keep, [2] * (n_total + n_E))

def compute(rho_RQE, U_QE):
    """Compute QCMI = I(R:QE) - I(R:Q).

    QCMI = S(ρ_R) + S(ρ_QE) - S(ρ_RQE) - [S(ρ_R) + S(ρ_Q) - S(ρ_RQ)]
         = S(ρ_QE) + S(ρ_RQ) - S(ρ_RQE) - S(ρ_Q)

    Args:
        rho_RQE: Initial state on R+Q+E (after F traceout)
        U_QE: Unitary on Q+E subsystem
    Returns:
        QCMI value
    """
    d_R = 4
    I_R = np.eye(d_R, dtype=complex)

    # Apply U_QE on QE system, identity on R
    # Tensor product ordering: kron(U_QE, I_R) puts U_QE on slow qubits, I_R on fast
    sigma = np.kron(U_QE, I_R) @ rho_RQE @ np.kron(U_QE, I_R).conj().T

    n_qe = int(np.log2(U_QE.shape[0]))
    n_tot = 2 + n_qe
    dims = [2] * n_tot

    # Partial traces
    # Layout: qubits 0,1 = R_a,R_b (fast); 2,3 = Q_a,Q_b; 4+ = E
    rR = ptrace(sigma, [0, 1], dims)
    rQ = ptrace(sigma, [2, 3], dims)
    rRQ = ptrace(sigma, [0, 1, 2, 3], dims)
    rQE_all = ptrace(sigma, list(range(2, n_tot)), dims)

    SR = vn_entropy(rR)
    SQ = vn_entropy(rQ)
    SRQ = vn_entropy(rRQ)
    SQE = vn_entropy(rQE_all)
    Sall = vn_entropy(sigma)

    qcmi = (SR + SQE - Sall) - (SR + SQ - SRQ)
    return qcmi, SR, SQ, SRQ


# ========== Graph constructions ==========
# Qubit indexing convention:
#   Fast bits (qubits 0,1): R_a, R_b
#   QE system starts at qubit 2:
#     qubit 0 in QE = Q_a
#     qubit 1 in QE = Q_b
#     qubit 2+ in QE = E_1, E_2, ...
# So in embed_lsb(a, b, nq), a,b are QE-internal indices: 0=Q_a, 1=Q_b, 2+=E

def build_b0_tree(rng_seed):
    """b1=0: Tree on 5 QE qubits (Q_a,Q_b,E1,E2,E3).
    Edges: Q_a-E1, E1-Q_b, Q_b-E2, E2-E3.
    5V, 4E, b1 = 4-5+1 = 0.
    """
    U1 = embed_lsb(random_u(4, rng_seed),     0, 2, 5)  # Q_a(0)-E1(2)
    U2 = embed_lsb(random_u(4, rng_seed + 1), 2, 1, 5)  # E1(2)-Q_b(1)
    U3 = embed_lsb(random_u(4, rng_seed + 2), 1, 3, 5)  # Q_b(1)-E2(3)
    U4 = embed_lsb(random_u(4, rng_seed + 3), 3, 4, 5)  # E2(3)-E3(4)
    return U4 @ U3 @ U2 @ U1

def build_b1_4cycle(rng_seed):
    """b1=1: 4-cycle Q_a-E1-Q_b-E2-Q_a.
    4V, 4E, b1 = 4-4+1 = 1.
    """
    U1 = embed_lsb(random_u(4, rng_seed),     0, 2, 4)  # Q_a(0)-E1(2)
    U2 = embed_lsb(random_u(4, rng_seed + 1), 2, 1, 4)  # E1(2)-Q_b(1)
    U3 = embed_lsb(random_u(4, rng_seed + 2), 1, 3, 4)  # Q_b(1)-E2(3)
    U4 = embed_lsb(random_u(4, rng_seed + 3), 0, 3, 4)  # Q_a(0)-E2(3)
    return U4 @ U3 @ U2 @ U1

def build_b1_3cycle(rng_seed):
    """b1=1: 3-cycle Q_a-E1-Q_b-Q_a (for consistency check with b1=2).
    3V, 3E, b1 = 3-3+1 = 1.
    """
    U1 = embed_lsb(random_u(4, rng_seed),     0, 2, 3)  # Q_a(0)-E1(2)
    U2 = embed_lsb(random_u(4, rng_seed + 1), 2, 1, 3)  # E1(2)-Q_b(1)
    U3 = embed_lsb(random_u(4, rng_seed + 2), 0, 1, 3)  # Q_a(0)-Q_b(1)
    return U3 @ U2 @ U1

def build_b2_disjoint(rng_seed):
    """b1=2: Two vertex-disjoint 3-cycles.

    Cycle A: Q_a(0)-E1(2)-E2(3)-Q_a(0)  [3 edges, involves Q_a]
    Cycle B: Q_b(1)-E3(4)-E4(5)-Q_b(1)  [3 edges, involves Q_b]

    6V, 6E, C=2 (disconnected), b1 = 6-6+2 = 2.
    Key property: zero shared vertices between the two cycles.
    This is the simplest strict multi-cycle case (two independent loops).
    """
    # Cycle A: Q_a - E1 - E2 - Q_a
    UA1 = embed_lsb(random_u(4, rng_seed),     0, 2, 6)  # Q_a(0)-E1(2)
    UA2 = embed_lsb(random_u(4, rng_seed + 1), 2, 3, 6)  # E1(2)-E2(3)
    UA3 = embed_lsb(random_u(4, rng_seed + 2), 0, 3, 6)  # Q_a(0)-E2(3)
    # Cycle B: Q_b - E3 - E4 - Q_b
    UB1 = embed_lsb(random_u(4, rng_seed + 3), 1, 4, 6)  # Q_b(1)-E3(4)
    UB2 = embed_lsb(random_u(4, rng_seed + 4), 4, 5, 6)  # E3(4)-E4(5)
    UB3 = embed_lsb(random_u(4, rng_seed + 5), 1, 5, 6)  # Q_b(1)-E4(5)

    return UB3 @ UB2 @ UB1 @ UA3 @ UA2 @ UA1

def build_b3_shared(rng_seed):
    """b1=3: Two 4-cycles sharing both Q_a and Q_b.

    Cycle A: Q_a(0)-E1(2)-Q_b(1)-E2(3)-Q_a(0)  [4 edges]
    Cycle B: Q_a(0)-E3(4)-Q_b(1)-E4(5)-Q_a(0)  [4 edges]

    6V, 8E, b1 = 8-6+1 = 3.
    Cycles share Q nodes → tests interference between cycles.
    """
    # Cycle A
    UA1 = embed_lsb(random_u(4, rng_seed),     0, 2, 6)  # Q_a(0)-E1(2)
    UA2 = embed_lsb(random_u(4, rng_seed + 1), 2, 1, 6)  # E1(2)-Q_b(1)
    UA3 = embed_lsb(random_u(4, rng_seed + 2), 1, 3, 6)  # Q_b(1)-E2(3)
    UA4 = embed_lsb(random_u(4, rng_seed + 3), 0, 3, 6)  # Q_a(0)-E2(3)
    # Cycle B
    UB1 = embed_lsb(random_u(4, rng_seed + 4), 0, 4, 6)  # Q_a(0)-E3(4)
    UB2 = embed_lsb(random_u(4, rng_seed + 5), 4, 1, 6)  # E3(4)-Q_b(1)
    UB3 = embed_lsb(random_u(4, rng_seed + 6), 1, 5, 6)  # Q_b(1)-E4(5)
    UB4 = embed_lsb(random_u(4, rng_seed + 7), 0, 5, 6)  # Q_a(0)-E4(5)

    return UB4 @ UB3 @ UB2 @ UB1 @ UA4 @ UA3 @ UA2 @ UA1

def build_b4_extra_edge(rng_seed):
    """b1=4: b1=3 graph + one extra edge (E2-E4).

    Adds edge E2(3)-E4(5) to the b1=3 construction.
    6V, 9E, b1 = 9-6+1 = 4.
    Tests whether adding more edges to a saturated graph increases QCMI.
    """
    # Same as b1=3 cycles
    UA1 = embed_lsb(random_u(4, rng_seed),     0, 2, 6)
    UA2 = embed_lsb(random_u(4, rng_seed + 1), 2, 1, 6)
    UA3 = embed_lsb(random_u(4, rng_seed + 2), 1, 3, 6)
    UA4 = embed_lsb(random_u(4, rng_seed + 3), 0, 3, 6)
    UB1 = embed_lsb(random_u(4, rng_seed + 4), 0, 4, 6)
    UB2 = embed_lsb(random_u(4, rng_seed + 5), 4, 1, 6)
    UB3 = embed_lsb(random_u(4, rng_seed + 6), 1, 5, 6)
    UB4 = embed_lsb(random_u(4, rng_seed + 7), 0, 5, 6)
    # Extra edge
    UX1 = embed_lsb(random_u(4, rng_seed + 8), 3, 5, 6)  # E2(3)-E4(5)

    return UX1 @ UB4 @ UB3 @ UB2 @ UB1 @ UA4 @ UA3 @ UA2 @ UA1

# Registry: b1 -> (label, n_qe, builder_function)
BUILDERS = {
    0: ('tree (5QE)',          5, build_b0_tree),
    1: ('4-cycle (4QE)',       4, build_b1_4cycle),
    2: ('2x C3 disjoint (6QE)', 6, build_b2_disjoint),
    3: ('2x C4 shared-Q (6QE)', 6, build_b3_shared),
    4: ('2x C4 + edge (6QE)',  6, build_b4_extra_edge),
}

# ========== Main scan ==========
p = 0.7
N_trials = 30

print("=" * 72)
print("QCMI vs b1 SCALING EXPERIMENT")
print(f"Buscemi mixed state, p={p}, {N_trials} Haar-random configs per b1")
print("=" * 72)

all_results = {}
all_details = {}  # Store (SR, SQ, SRQ) for diagnostics

for b1 in [0, 1, 2, 3, 4]:
    label, n_qe, builder = BUILDERS[b1]
    n_E = n_qe - 2
    rho = make_mixed_rho(n_E, p)

    vals = []
    detail_list = []

    print(f"\n{'='*60}")
    print(f"Running b1={b1} ({label})...")
    print(f"  n_qe={n_qe}, n_E={n_E}, rho_RQE dim={rho.shape[0]}")

    for t in range(N_trials):
        seed = 1000 + t * 13
        U = builder(seed)
        qcmi, SR, SQ, SRQ = compute(rho, U)
        vals.append(qcmi)
        detail_list.append((SR, SQ, SRQ))

        if (t + 1) % 10 == 0:
            print(f"  [{t+1}/{N_trials}] running mean={np.mean(vals):.6f}")

    vals = np.array(vals)
    all_results[b1] = vals
    all_details[b1] = detail_list

    print(f"\n  FINAL: mean={np.mean(vals):.6f}  std={np.std(vals):.6f}")
    print(f"          min={np.min(vals):.6f}  max={np.max(vals):.6f}")
    if b1 > 0:
        print(f"          QCMI/b1 = {np.mean(vals)/b1:.6f}")

    # Also print entropy diagnostics for first trial
    SRs = [d[0] for d in detail_list]
    SQs = [d[1] for d in detail_list]
    SRQs = [d[2] for d in detail_list]
    print(f"  S(R) mean={np.mean(SRs):.4f} (expect 2.0, invariant)")
    print(f"  S(Q) mean={np.mean(SQs):.4f}")
    print(f"  S(RQ) mean={np.mean(SRQs):.4f}")


# ========== Consistency check: b1=1 with 3-cycle ==========
print(f"\n{'='*60}")
print("CONSISTENCY CHECK: b1=1 with 3-cycle (to match b1=2 cycle size)")
print(f"{'='*60}")

rho_3c = make_mixed_rho(1, p)  # n_E=1, total n_qe=3
vals_3c = []
for t in range(N_trials):
    U = build_b1_3cycle(1000 + t * 13)
    qcmi, _, _, _ = compute(rho_3c, U)
    vals_3c.append(qcmi)
vals_3c = np.array(vals_3c)
print(f"  b1=1 3-cycle: mean={np.mean(vals_3c):.6f}  std={np.std(vals_3c):.6f}")


# ========== Fitting QCMI ∝ b1^α ==========
print(f"\n{'='*60}")
print("POWER-LAW FIT: QCMI = A * b1^alpha")
print(f"{'='*60}")

b1_arr = np.array([0, 1, 2, 3, 4])
means = np.array([np.mean(all_results[b]) for b in b1_arr])
stds = np.array([np.std(all_results[b]) for b in b1_arr])

# Fit on b1 >= 1 (b1=0 is tree, fundamentally different topology)
b1_fit = np.array([1, 2, 3, 4])
means_fit = np.array([np.mean(all_results[b]) for b in b1_fit])
stds_fit = np.array([np.std(all_results[b]) for b in b1_fit])

def power_law(x, A, alpha):
    return A * np.abs(x)**alpha

try:
    popt, pcov = curve_fit(power_law, b1_fit, means_fit, sigma=stds_fit,
                           absolute_sigma=True, maxfev=10000)
    A_fit, alpha_fit = popt
    A_err, alpha_err = np.sqrt(np.diag(pcov))

    residuals = means_fit - power_law(b1_fit, *popt)
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((means_fit - np.mean(means_fit))**2)
    r_squared = 1 - ss_res / ss_tot

    print(f"  A = {A_fit:.6f} +/- {A_err:.6f}")
    print(f"  alpha = {alpha_fit:.4f} +/- {alpha_err:.4f}")
    print(f"  R^2 = {r_squared:.4f}")

    # Predictions
    print(f"\n  Predictions from fit:")
    for bx in [1, 2, 3, 4]:
        pred = power_law(bx, A_fit, alpha_fit)
        actual = means_fit[bx-1]
        print(f"    b1={bx}: predicted={pred:.6f}, actual={actual:.6f}, diff={pred-actual:+.6f}")
except Exception as e:
    print(f"  Fit failed: {e}")
    A_fit, alpha_fit, r_squared = np.nan, np.nan, np.nan


# ========== Output to Markdown ==========
output_path = r'D:\Claude\ai-reservations\LP36-W-Causal-Accumulation\experiments\b1_scan_results.md'

with open(output_path, 'w', encoding='utf-8') as f:
    f.write("# QCMI vs b1 Scaling Experiment Results\n\n")
    f.write(f"**Date**: 2026-06-09\n\n")
    f.write(f"**State**: Buscemi mixed, p={p}\n\n")
    f.write(f"**Gates**: Haar random (QR decomposition of random complex 4x4 matrices), sampling uniformly from SU(4) Cartan manifold\n\n")
    f.write(f"**Trials**: {N_trials} independent gate configurations per b1 value\n\n")

    f.write("## 1. Method\n\n")
    f.write("We compute QCMI = I(R:QE) - I(R:Q) for quantum circuits on increasingly "
            "complex graphs parameterized by the first Betti number b1 = E - V + C.\n\n")
    f.write("The Q-system has 2 qubits (Q_a, Q_b) and is purified by "
            "an R-register of 2 qubits. The E-environment consists of n_E qubits "
            "initialized in a product mixed state gamma_E = diag(p,1-p)^{⊗n_E} with p=0.7.\n\n")

    f.write("### Graph constructions\n\n")
    f.write("| b1 | Label | V | E | C | n_qe | Description |\n")
    f.write("|-----|-------|---|---|---|------|-------------|\n")

    desc_map = {
        0: ("5", "4", "1", "5", "Tree: Q_a-E1-Q_b-E2-E3, spanning tree with no cycles"),
        1: ("4", "4", "1", "4", "4-cycle: Q_a-E1-Q_b-E2-Q_a"),
        2: ("6", "6", "2", "6", "Two vertex-disjoint 3-cycles (C3×2). Cycle A: Q_a-E1-E2-Q_a. Cycle B: Q_b-E3-E4-Q_b. Zero shared vertices."),
        3: ("6", "8", "1", "6", "Two 4-cycles sharing Q_a and Q_b (C4×2). Tests cycle interference."),
        4: ("6", "9", "1", "6", "b1=3 graph + extra edge E2-E4. Tests saturation at higher b1."),
    }

    for b1 in [0, 1, 2, 3, 4]:
        V, E, C, nq, desc = desc_map[b1]
        label = BUILDERS[b1][0]
        f.write(f"| {b1} | {label} | {V} | {E} | {C} | {nq} | {desc} |\n")

    f.write("\n## 2. Results\n\n")
    f.write("### Primary data\n\n")
    f.write("| b1 | Label | n_qe | mean(QCMI) | std | min | max | QCMI/b1 |\n")
    f.write("|-----|-------|------|------------|-----|-----|-----|---------|\n")

    for b1 in [0, 1, 2, 3, 4]:
        vals = all_results[b1]
        label = BUILDERS[b1][0]
        n_qe = BUILDERS[b1][1]
        qpb = f"{np.mean(vals)/b1:.6f}" if b1 > 0 else "N/A"
        f.write(f"| {b1} | {label} | {n_qe} | {np.mean(vals):.6f} | {np.std(vals):.6f} | "
                f"{np.min(vals):.6f} | {np.max(vals):.6f} | {qpb} |\n")

    f.write(f"\n### Consistency check: b1=1 with 3-cycle\n\n")
    f.write(f"To control for cycle-size confounding (b1=2 uses 3-cycles, b1=1 uses 4-cycle):\n\n")
    f.write(f"- b1=1 (3-cycle Q_a-E1-Q_b-Q_a): mean={np.mean(vals_3c):.6f}, std={np.std(vals_3c):.6f}\n")
    f.write(f"- b1=1 (4-cycle Q_a-E1-Q_b-E2-Q_a): mean={means[1]:.6f}, std={stds[1]:.6f}\n")
    f.write(f"- Ratio (3-cycle/4-cycle) = {np.mean(vals_3c)/means[1]:.4f}\n\n")

    f.write("### Entropy diagnostics (mean across trials)\n\n")
    f.write("| b1 | S(R) | S(Q) | S(RQ) |\n")
    f.write("|-----|------|------|-------|\n")
    for b1 in [0, 1, 2, 3, 4]:
        SRs = [d[0] for d in all_details[b1]]
        SQs = [d[1] for d in all_details[b1]]
        SRQs = [d[2] for d in all_details[b1]]
        f.write(f"| {b1} | {np.mean(SRs):.4f} | {np.mean(SQs):.4f} | {np.mean(SRQs):.4f} |\n")
    f.write(f"\nNote: S(R) should be ~2.0 (invariant under QE unitary). Deviation indicates numerical error.\n")

    f.write(f"\n## 3. Power-Law Fit\n\n")
    f.write(f"Fitting QCMI = A * b1^alpha on b1 in {{1,2,3,4}} (excluding b1=0 tree):\n\n")

    if not np.isnan(A_fit):
        f.write(f"- **A** = {A_fit:.6f} +/- {A_err:.6f}\n")
        f.write(f"- **alpha** = {alpha_fit:.4f} +/- {alpha_err:.4f}\n")
        f.write(f"- **R^2** = {r_squared:.4f}\n\n")
    else:
        f.write("- Fit failed\n\n")

    f.write("## 4. Raw Data Points\n\n")
    f.write("```\n")
    for b1 in [0, 1, 2, 3, 4]:
        vals = all_results[b1]
        f.write(f"b1={b1}: {np.array2string(vals, precision=6, separator=', ', max_line_width=120)}\n")
    f.write("```\n\n")

    f.write("## 5. Interpretation\n\n")

    # Determine key findings
    b0_mean = means[0]
    b1_mean = means[1]
    b2_mean = means[2]
    b3_mean = means[3]
    b4_mean = means[4]

    delta_01 = b1_mean - b0_mean
    delta_12 = b2_mean - b1_mean
    delta_23 = b3_mean - b2_mean
    delta_34 = b4_mean - b3_mean

    qpb1 = b1_mean / 1.0
    qpb2 = b2_mean / 2.0  # QCMI per cycle for disjoint case
    qpb3 = b3_mean / 3.0
    qpb4 = b4_mean / 4.0

    f.write("### Scaling behavior\n\n")

    if not np.isnan(alpha_fit):
        if alpha_fit > 0.8:
            f.write(f"The fitted exponent alpha = {alpha_fit:.3f} +/- {alpha_err:.3f} supports "
                    f"**near-linear scaling** of QCMI with b1. This is consistent with Wall 2's "
                    f"core claim that the first Betti number acts as a topological control parameter "
                    f"for quantum causal accumulation. Each additional independent cycle contributes "
                    f"roughly linearly to the QCMI.\n\n")
        elif alpha_fit > 0.4:
            f.write(f"The fitted exponent alpha = {alpha_fit:.3f} +/- {alpha_err:.3f} shows "
                    f"**sub-linear scaling**, indicating that while QCMI grows with b1, there is "
                    f"significant saturation or interference between cycles. Wall 2's linear "
                    f"hypothesis is partially supported but the saturation suggests that Cartan "
                    f"axis alignment or cycle interference plays a non-negligible role.\n\n")
        else:
            f.write(f"The fitted exponent alpha = {alpha_fit:.3f} +/- {alpha_err:.3f} shows "
                    f"**little to no growth** of QCMI with b1. This is a severe challenge to "
                    f"Wall 2's core claim: b1 does NOT act as a topological control parameter "
                    f"in this regime. The QCMI appears dominated by other factors such as "
                    f"Cartan axis alignment or gate commutativity.\n\n")

    f.write("### Key comparisons\n\n")
    f.write(f"1. **Tree → Cycle (b1=0→1)**: Delta = {delta_01:+.6f}. ")
    if delta_01 > 0:
        f.write("Adding the first cycle increases QCMI.\n")
    else:
        f.write("Adding the first cycle does NOT increase QCMI -- unexpected.\n")

    f.write(f"2. **Disjoint cycles (b1=1→2)**: Delta = {delta_12:+.6f}. ")
    if delta_12 > 0:
        f.write("Adding a second independent cycle increases QCMI.\n")
    else:
        f.write("Adding a second independent cycle DECREASES QCMI -- problematic for linear hypothesis.\n")

    f.write(f"3. **Shared-Q cycles (b1=2→3)**: Delta = {delta_23:+.6f}. ")
    if delta_23 > 0:
        f.write("Going from disjoint to shared cycles increases QCMI.\n")
    else:
        f.write("Going from disjoint to shared cycles DECREASES QCMI -- interference suppression?\n")

    f.write(f"4. **Extra edge (b1=3→4)**: Delta = {delta_34:+.6f}. ")
    if abs(delta_34) < 1e-3:
        f.write("Adding an extra edge has negligible effect -- saturation behavior.\n")
    elif delta_34 > 0:
        f.write("Adding an extra edge still increases QCMI.\n")
    else:
        f.write("Adding an extra edge DECREASES QCMI.\n")

    f.write(f"\n5. **QCMI per b1 ratio**: {qpb1:.6f} → {qpb2:.6f} → {qpb3:.6f} → {qpb4:.6f}\n")
    f.write(f"   If linear, this should stay constant. ")
    ratios = [qpb2/qpb1 if qpb1 > 0 else 0, qpb3/qpb2 if qpb2 > 0 else 0, qpb4/qpb3 if qpb3 > 0 else 0]
    f.write(f"Ratios: {ratios[0]:.4f}, {ratios[1]:.4f}, {ratios[2]:.4f}\n")
    if all(abs(r - 1.0) < 0.15 for r in ratios):
        f.write("   → Near-constant ratio supports linear scaling.\n")
    elif all(r < 1.0 for r in ratios if r > 0):
        f.write("   → Consistently declining ratio suggests sub-linear/saturating behavior.\n")
    else:
        f.write("   → Irregular ratio pattern.\n")

    f.write("\n### Verdict\n\n")

    # Determine overall verdict
    if not np.isnan(alpha_fit):
        if alpha_fit > 0.7 and r_squared > 0.8:
            f.write("**WALL 2 SUPPORTED**: The b1 scaling experiment supports the claim that QCMI ∝ b1. "
                    f"The first Betti number acts as a valid topological control parameter. "
                    f"Wall 2's core argument is quantitatively consistent with numerical data.\n\n")
        elif alpha_fit > 0.4:
            f.write("**PARTIAL SUPPORT**: QCMI grows with b1 but sub-linearly. "
                    f"Wall 2's qualitative claim (b1 controls accumulation) is supported, "
                    f"but the quantitative claim (linear scaling) needs refinement. "
                    f"Inter-cycle interference or Cartan axis alignment may provide "
                    f"a correction factor.\n\n")
        else:
            f.write("**WALL 2 CHALLENGED**: QCMI does not grow significantly with b1. "
                    f"The data suggests that b1 is NOT the primary control parameter for QCMI. "
                    f"Cartan axis alignment, gate commutativity, or cycle topology may be "
                    f"more important. Wall 2's core claim requires fundamental revision.\n\n")

    f.write("## 6. Limitations\n\n")
    f.write("- Classical simulation limited to n_qe <= 6 (Hilbert space dim 64)\n")
    f.write("- Haar random gates sample SU(4) uniformly; specific Cartan subalgebra parameterizations not tested\n")
    f.write("- b1=2 uses 3-cycles while b1=1,3,4 use 4-cycles → cycle-size confound\n")
    f.write("- p=0.7 fixed; p→1/2 (maximally mixed environment) would reduce QCMI magnitudes\n")
    f.write("- Graph isomorphism: different topologies with same b1 may yield different QCMI\n")
    f.write("- Small Hilbert space (max 1024x1024) may miss large-N effects\n")

print(f"\n\n{'='*60}")
print(f"Results written to: {output_path}")
print(f"{'='*60}")

# Print summary table for console
print(f"\nSummary Table:")
print(f"{'b1':>4s} {'mean(QCMI)':>12s} {'std':>10s} {'QCMI/b1':>10s}")
print(f"{'='*40}")
for b1 in [0, 1, 2, 3, 4]:
    vals = all_results[b1]
    qpb = f"{np.mean(vals)/b1:.6f}" if b1 > 0 else "N/A"
    print(f"{b1:4d} {np.mean(vals):12.6f} {np.std(vals):10.6f} {qpb:>10s}")

sys.exit(0)

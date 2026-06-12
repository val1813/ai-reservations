"""
CFOL sufficiency: QCMI landscape scan for 4-node aligned causal ring.

Computes QCMI = I(R;E'|Q') for the CFOL setup:
  Q_a -> E_1 -> Q_b -> E_2 -> Q_a
All edges aligned to same Pauli direction (n̂ = z).
Parameters: c1, c2, c3, c4 (Cartan magnitudes), p (environment purity).
"""

import numpy as np
from scipy.linalg import sqrtm, logm

# Pauli matrices
I2 = np.eye(2, dtype=complex)
X = np.array([[0,1],[1,0]], dtype=complex)
Y = np.array([[0,-1j],[1j,0]], dtype=complex)
Z = np.array([[1,0],[0,-1]], dtype=complex)


def tensor(*ops):
    """Kronecker product of operators."""
    result = np.array([[1]], dtype=complex)
    for op in ops:
        result = np.kron(result, op)
    return result


def von_neumann_entropy(rho, eps=1e-12):
    """von Neumann entropy S(rho) = -Tr(rho log rho) in bits."""
    evals = np.linalg.eigvalsh(rho)
    evals = np.maximum(evals, eps)  # clip negative eigenvalues from numerics
    evals = evals / evals.sum()  # renormalize
    return -np.sum(evals * np.log2(evals))


def build_channel(c1, c2, c3, c4, p):
    """
    Build the Kraus operators for the aligned 4-node causal ring.

    All edges aligned to sigma_z direction.
    c_i: Cartan parameter magnitude for edge i.
    p: probability of |0> in environment (sigma_z basis).

    Returns: list of 4 Kraus operators K_{s2,s4}, each 4x4 on Q_a⊗Q_b.
    """
    alpha0 = np.sqrt(p)
    alpha1 = np.sqrt(1 - p)

    # K_{s2,s4} are diagonal in the computational basis |s1,s3>
    # (since sigma_z eigenbasis = computational basis)
    # s1, s3 ∈ {+1(0), -1(1)}

    K = {}
    for s2, a2 in [('+', alpha0), ('-', alpha1)]:
        for s4, a4 in [('+', alpha0), ('-', alpha1)]:
            s2v = 1 if s2 == '+' else -1
            s4v = 1 if s4 == '+' else -1

            K_op = np.zeros((4, 4), dtype=complex)
            for idx, (s1, s3) in enumerate([(1, 1), (1, -1), (-1, 1), (-1, -1)]):
                # λ = c1*s1*s2 + c2*s2*s3 + c3*s3*s4 + c4*s4*s1
                lam = (c1 * s1 * s2v + c2 * s2v * s3 +
                       c3 * s3 * s4v + c4 * s4v * s1)
                K_op[idx, idx] = a2 * a4 * np.exp(1j * lam)

            K[(s2, s4)] = K_op

    return [K[('+', '+')], K[('+', '-')], K[('-', '+')], K[('-', '-')]]


def qcmi_from_kraus(K_list):
    """
    Compute QCMI = I(R;E'|Q') for channel with Kraus operators K_list.

    Channel N: ρ_Q → Σ_k K_k ρ_Q K_k†
    Output: (I_R ⊗ N)(|Φ⁺⟩⟨Φ⁺|) on R ⊗ E'Q'.

    R is a 4-dim reference (matching Q = 4-dim).
    E' is 4-dim (2 environment qubits after channel).
    Q' is 4-dim (Q_a⊗Q_b output).
    """
    d = 4  # dimension of Q = Q_a ⊗ Q_b

    # Bell state |Φ⁺⟩_{RQ} = (1/√d) Σ_i |i⟩_R|i⟩_Q
    phi_plus = np.zeros((d * d,), dtype=complex)
    for i in range(d):
        phi_plus[i * d + i] = 1.0 / np.sqrt(d)

    rho_RQ = np.outer(phi_plus, phi_plus.conj())  # d^2 × d^2

    # Apply channel: (I ⊗ N)(rho_RQ)
    # Channel acts on Q only: ρ → Σ_k (I⊗K_k) ρ (I⊗K_k)†
    rho_out = np.zeros_like(rho_RQ)
    for K in K_list:
        # I_R ⊗ K acts on R⊗Q
        IK = np.kron(np.eye(d), K)
        rho_out += IK @ rho_RQ @ IK.conj().T

    # Now we have rho_{R, E'Q'} because the Kraus operators map
    # Q to Q' while also encoding the E' index.
    # But the Kraus sum gives a state on R ⊗ Q' (tracing E').
    # We need ρ_{RE'Q'} to compute I(R;E'|Q').

    # Actually, I need to construct the full output state with E'.
    # The Stinespring: |Ψ⟩ = (1/√d) Σ_i |i⟩_R ⊗ Σ_k |k⟩_E' ⊗ K_k|i⟩_Q

    # Build the full pure state |Ψ⟩_{RE'Q'}
    d_e = len(K_list)  # 4
    psi = np.zeros((d, d_e, d), dtype=complex)
    for i in range(d):
        qi = np.zeros(d, dtype=complex)
        qi[i] = 1.0
        for k_idx, K in enumerate(K_list):
            psi[i, k_idx, :] = K @ qi

    # Flatten to vector
    psi_vec = psi.reshape(-1) / np.sqrt(d)

    # Full density matrix ρ_{RE'Q'}
    rho_REQ = np.outer(psi_vec, psi_vec.conj())

    # Reduced states using einsum for proper partial trace
    # rho_tensor[a, k, i, b, l, j] where a,b in R, k,l in E', i,j in Q'
    rho_tensor = rho_REQ.reshape(d, d_e, d, d, d_e, d)

    # ρ_{RQ'} = Tr_{E'} ρ: sum over k=l (axes 1 and 4)
    rho_RQ = np.einsum('akibkj->aibj', rho_tensor).reshape(d*d, d*d)

    # ρ_{E'Q'} = Tr_R ρ: sum over a=b (axes 0 and 3)
    rho_EQ_4t = np.einsum('akialj->kilj', rho_tensor)
    rho_EQ = rho_EQ_4t.reshape(d_e*d, d_e*d)

    # ρ_{Q'} = Tr_{RE'} ρ: trace over both R (a=b) and E' (k=l)
    rho_Q = np.einsum('akiakj->ij', rho_tensor)

    # Entropies — these are already matrices of the right size
    S_RQ = von_neumann_entropy(rho_RQ)
    S_EQ = von_neumann_entropy(rho_EQ)
    S_Q = von_neumann_entropy(rho_Q)

    QCMI = S_RQ + S_EQ - S_Q  # S(ρ_{RE'Q'}) = 0 (pure)

    return QCMI, S_RQ, S_EQ, S_Q


def gram_matrix(c1, c2, c3, c4, p):
    """Compute the Gram matrix G_{s,t} = ⟨φ(s)|φ(t)⟩."""
    alpha0 = np.sqrt(p)
    alpha1 = np.sqrt(1 - p)

    states = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # (s1, s3)

    def phi_vec(s1, s3):
        vec = np.zeros(4, dtype=complex)
        for idx2, (s2, a2) in enumerate([(1, alpha0), (-1, alpha1)]):
            for idx4, (s4, a4) in enumerate([(1, alpha0), (-1, alpha1)]):
                e_idx = idx2 * 2 + idx4
                lam = (c1 * s1 * s2 + c2 * s2 * s3 +
                       c3 * s3 * s4 + c4 * s4 * s1)
                vec[e_idx] = a2 * a4 * np.exp(1j * lam)
        return vec

    G = np.zeros((4, 4), dtype=complex)
    for i, s in enumerate(states):
        phi_s = phi_vec(s[0], s[1])
        for j, t in enumerate(states):
            phi_t = phi_vec(t[0], t[1])
            G[i, j] = np.dot(phi_s.conj(), phi_t)

    return G


# ============================================================
# Main analysis
# ============================================================

if __name__ == '__main__':
    print("=" * 70)
    print("CFOL Sufficiency: QCMI Landscape Scan")
    print("=" * 70)

    # Test 1: CNOT case (c1=c2=c3=c4=π/4) with varying p
    print("\n--- Test 1: CNOT (all ci=π/4), varying p ---")
    print(f"{'p':>6s}  {'QCMI':>10s}  {'S(RQ)':>10s}  {'S(EQ)':>10s}  {'S(Q)':>10s}  {'G off-diag':>12s}")
    for p in [0.5, 0.6, 0.7, 0.8, 0.9]:
        K_list = build_channel(np.pi/4, np.pi/4, np.pi/4, np.pi/4, p)
        qcmi, S_RQ, S_EQ, S_Q = qcmi_from_kraus(K_list)
        G = gram_matrix(np.pi/4, np.pi/4, np.pi/4, np.pi/4, p)
        off_diag = np.max(np.abs(G - np.eye(4)))
        print(f" {p:5.2f}  {qcmi:10.6f}  {S_RQ:10.6f}  {S_EQ:10.6f}  {S_Q:10.6f}  {off_diag:12.6f}")

    # Test 2: c_j in (π/2)Z — should all give QCMI=0
    print("\n--- Test 2: c_j in (pi/2)Z (predicted QCMI=0) ---")
    test_cases = [
        ([0, 0, 0, 0], "all zero"),
        ([np.pi/2, np.pi/2, np.pi/2, np.pi/2], "all π/2"),
        ([np.pi/2, 0, np.pi/2, 0], "π/2, 0, π/2, 0"),
        ([np.pi/2, np.pi/2, np.pi, -np.pi], "INSPECTOR ex"),
        ([np.pi, np.pi, np.pi, np.pi], "all π"),
    ]
    for c_list, label in test_cases:
        for p in [0.5, 0.7]:
            K_list = build_channel(*c_list, p)
            qcmi, _, _, _ = qcmi_from_kraus(K_list)
            G = gram_matrix(*c_list, p)
            off_diag = np.max(np.abs(G - np.eye(4)))
            print(f"  {label:30s} p={p:.1f}: QCMI={qcmi:.8f}, off-diag={off_diag:.2e}")

    # Test 3: c_j = π/4 uniform, QCMI vs p
    print("\n--- Test 3: CNOT with scaled c ---")
    for scale in [0.5, 1.0, 1.5]:  # c = scale * π/4
        c_val = scale * np.pi / 4
        for p in [0.5, 0.7, 0.9]:
            K_list = build_channel(c_val, c_val, c_val, c_val, p)
            qcmi, _, _, _ = qcmi_from_kraus(K_list)
            G = gram_matrix(c_val, c_val, c_val, c_val, p)
            evals = np.linalg.eigvalsh(G)
            print(f"  c={scale}π/4, p={p:.1f}: QCMI={qcmi:.6f}, G-evals={np.sort(evals)[::-1]}")

    # Test 4: Search for QCMI=0 configurations (p=0.7 fixed)
    print("\n--- Test 4: Systematic scan for QCMI=0 at p=0.5 ---")
    p = 0.5
    found_zero = []
    for n1 in range(5):
        for n2 in range(5):
            for n3 in range(5):
                for n4 in range(5):
                    c_list = [n * np.pi / 4 for n in [n1, n2, n3, n4]]
                    K_list = build_channel(*c_list, p)
                    qcmi, _, _, _ = qcmi_from_kraus(K_list)
                    if qcmi < 1e-10:
                        found_zero.append((n1, n2, n3, n4))
    print(f"  Found {len(found_zero)} zero-QCMI configs at p=0.5 (c_j ∈ π/4 · {{0,1,2,3,4}}):")
    for config in found_zero:
        print(f"    c/π·4 = {config}")

    # Test 5: Search for QCMI=0 at p=0.7
    print("\n--- Test 5: Search for QCMI=0 at p=0.7 ---")
    p = 0.7
    found_zero = []
    found_near_zero = []
    for n1 in range(9):
        for n2 in range(9):
            for n3 in range(9):
                for n4 in range(9):
                    c_list = [n * np.pi / 8 for n in [n1, n2, n3, n4]]
                    K_list = build_channel(*c_list, p)
                    qcmi, _, _, _ = qcmi_from_kraus(K_list)
                    if qcmi < 1e-10:
                        found_zero.append((n1, n2, n3, n4))
                    elif qcmi < 1e-6:
                        found_near_zero.append((n1, n2, n3, n4, qcmi))
    print(f"  Found {len(found_zero)} zero-QCMI configs at p=0.7 (c_j ∈ π/8 · {{0..8}}):")
    for config in found_zero:
        print(f"    c/π·8 = {config}")
    if found_near_zero:
        print(f"  Near-zero (<1e-6):")
        for config in found_near_zero[:10]:
            print(f"    c/π·8 = {config}")

    # Test 6: Analytic check — does QCMI=0 ⇔ G=I hold?
    print("\n--- Test 6: Verifying QCMI=0 ⇔ G is identity ---")
    for n1 in range(5):
        for n2 in range(5):
            c_list = [n1 * np.pi / 4, n2 * np.pi / 4, 0, 0]
            for p in [0.3, 0.5, 0.7]:
                G = gram_matrix(*c_list, p)
                rho_RQ = G / 4  # from the Gram matrix derivation
                evals = np.linalg.eigvalsh(rho_RQ)
                evals = np.maximum(evals, 1e-15)
                evals = evals / evals.sum()
                S_gram = -np.sum(evals * np.log2(evals))
                # Compare with direct QCMI
                K_list = build_channel(*c_list, p)
                qcmi_direct, _, _, _ = qcmi_from_kraus(K_list)
                diff = abs(S_gram - qcmi_direct)
                if diff > 1e-10:
                    print(f"  MISMATCH: c={c_list}, p={p}: S(G/4)={S_gram:.6f}, QCMI={qcmi_direct:.6f}, diff={diff:.2e}")

    print("\nDone.")

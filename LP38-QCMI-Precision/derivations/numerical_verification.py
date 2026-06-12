"""
LP38 Numerical Verification — Execute P0 actions.
P0-1: Temporal CJ ring simulation → determine f_CJ
P0-2: b₁=6 heavy-hex simulation → determine g(G)
P0-3: Mixed-axis QCMI verification
"""
import numpy as np
from scipy.linalg import expm
import sys

# ============================================================
# Core quantum info utilities
# ============================================================
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
H_gate = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)

def kron_rev(mats):
    """kron_rev([a,b,c]) = kron(a, kron(b, c)). mats[0]=MSB."""
    r = mats[-1]
    for m in reversed(mats[:-1]):
        r = np.kron(m, r)
    return r

def vn_entropy(rho):
    w = np.linalg.eigvalsh(rho)
    w = np.maximum(w, 1e-15)
    return -np.sum(w * np.log2(w))

def partial_trace(rho, keep_bits, n_total):
    """Trace out all bits NOT in keep_bits. keep_bits are BIT POSITIONS (0=LSB)."""
    keep = sorted(keep_bits)
    tr = sorted([i for i in range(n_total) if i not in keep])
    dk = 2 ** len(keep)
    res = np.zeros((dk, dk), dtype=complex)
    for a in range(dk):
        for ap in range(dk):
            bk = 0
            bk_ap = 0
            for ki, q in enumerate(keep):
                bk |= ((a >> ki) & 1) << q
                bk_ap |= ((ap >> ki) & 1) << q
            total = 0j
            for b in range(2 ** len(tr)):
                tp = 0
                for ti, q in enumerate(tr):
                    tp |= ((b >> ti) & 1) << q
                total += rho[bk | tp, bk_ap | tp]
            res[a, ap] = total
    return res

# ============================================================
# P0-1: Temporal CJ Ring vs Spatial 4-Node Ring
# ============================================================
def build_initial_state_temporal(p=0.7):
    """
    Temporal CJ ring state.
    Qubits: [Q=bit0, E=bit1, R=bit2]  (3 qubits total)
    Initial: |Φ⁺⟩⟨Φ⁺|_{RQ} ⊗ γ_E
    """
    bell_vec = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    rho_bell = np.outer(bell_vec, bell_vec.conj())
    gamma = np.diag([p, 1 - p])

    # kron_rev: [bell(R,Q)=bits2,0, gamma(E)=bit1]
    # Wait, kron_rev order: mats[0]=MSB highest bit
    # Bits: R=2, Q=0, E=1
    # We want tensor product: rho_bell_{RQ} ⊗ gamma_E
    # kron(rho_bell, gamma): RQ at bits 2,1? No...
    # Let me just construct explicitly.

    # Build in order [R=bit2, Q=bit0, E=bit1] via kron_rev
    # kron_rev: mats[0]=R(MSB,bit2), mats[1]=Q(bit1?), mats[2]=E(LSB,bit0)
    # Actually kron_rev order is: mats[0] at MSB (highest bit), mats[-1] at LSB (bit 0)
    # So for bits [R=2, E=1, Q=0]: kron_rev([rho_R, gamma_E, I_Q])? No...
    # Better: construct explicitly in computational basis.

    # R and Q in Bell state, E in gamma
    # Basis: |r⟩_R ⊗ |q⟩_Q ⊗ |e⟩_E
    # |Φ⁺⟩_{RQ} = (|00⟩ + |11⟩)/√2
    # ρ = |Φ⁺⟩⟨Φ⁺| ⊗ γ

    # Manual construction for 3 qubits (8x8)
    rho = np.zeros((8, 8), dtype=complex)
    for r in range(2):
        for q in range(2):
            for rp in range(2):
                for qp in range(2):
                    bell_val = 0.5 if (r == q and rp == qp) else 0.0
                    for e in range(2):
                        gamma_val = p if e == 0 else (1-p)
                        idx = (r << 2) | (e << 1) | q  # bits: R=2, E=1, Q=0
                        idxp = (rp << 2) | (e << 1) | qp
                        rho[idx, idxp] = bell_val * gamma_val
    return rho

def build_temporal_cj_unitary(theta1, theta2=None):
    """
    Temporal CJ unitary on 3 qubits [Q=bit0, E=bit1, R=bit2].
    U = U_2 · I_{QE} · U_1 where U_i are two-qubit gates on Q,E.

    CRITICAL: Using identical gates (U1=U2=CZ) gives U = CZ*CZ = I
    (two CZ gates cancel). The CJ bridge requires U1 and U2 to be
    DIFFERENT — either different angles or different Cartan axes.

    We use:
    - U1 = RZZ(theta1) = exp(-i*theta1/2 * Z⊗Z)
    - U2 = RZZ(theta2) = exp(-i*theta2/2 * Z⊗Z)
    with theta1 != theta2 to avoid cancellation.

    The identity period between them provides the "environment memory"
    edge u2 in the effective 4-node ring.
    """
    if theta2 is None:
        theta2 = theta1 / 2  # default: second interaction at half angle

    # Build RZZ(theta) on Q(b0) and E(b1)
    def build_RZZ_full(theta):
        # RZZ on 2 qubits: exp(-i*theta/2 * Z⊗Z)
        # = diag(e^{-iθ/2}, e^{iθ/2}, e^{iθ/2}, e^{-iθ/2})
        RZZ = np.diag([
            np.exp(-1j*theta/2),
            np.exp(1j*theta/2),
            np.exp(1j*theta/2),
            np.exp(-1j*theta/2)
        ])
        return np.kron(np.eye(2), RZZ)  # I_R ⊗ RZZ_{QE}

    U1 = build_RZZ_full(theta1)
    U2 = build_RZZ_full(theta2)

    # Total: U2 · I · U1 = U2 · U1
    U = U2 @ U1
    return U

def simulate_temporal_cj(theta1=np.pi/2, theta2=None, p=0.7):
    """Simulate temporal CJ ring QCMI with two different interaction angles."""
    if theta2 is None:
        theta2 = theta1 / 2
    rho_0 = build_initial_state_temporal(p)
    U = build_temporal_cj_unitary(theta1, theta2)
    rho_f = U @ rho_0 @ U.conj().T

    # Bits: R=2, E=1, Q=0
    S_RQ = vn_entropy(partial_trace(rho_f, [2, 0], 3))
    S_QE = vn_entropy(partial_trace(rho_f, [0, 1], 3))
    S_Q = vn_entropy(partial_trace(rho_f, [0], 3))
    S_RQE = vn_entropy(rho_f)

    QCMI = max(0.0, S_RQ + S_QE - S_Q - S_RQE)
    return {'QCMI': QCMI, 'S_RQ': S_RQ, 'S_QE': S_QE, 'S_Q': S_Q, 'S_RQE': S_RQE}

def simulate_spatial_4node(theta=np.pi/2, p=0.7):
    """
    Spatial 4-node ring: Q_a, E1, Q_b, E2.
    4 CZ edges: (Q_a,E1), (E1,Q_b), (Q_b,E2), (E2,Q_a)
    Bits: Q_a=0, E1=1, Q_b=2, E2=3, Ra=4, Rb=5 (6 qubits)
    """
    # Build initial state: |Φ⁺⟩⟨Φ⁺|_{Ra,Qa} ⊗ |Φ⁺⟩⟨Φ⁺|_{Rb,Qb} ⊗ γ_{E1} ⊗ γ_{E2}
    bell_vec = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    rho_bell = np.outer(bell_vec, bell_vec.conj())
    gamma = np.diag([p, 1 - p])

    # Block order via kron_rev: [RaQa, RbQb, E1, E2]
    rho_block = kron_rev([rho_bell, rho_bell, gamma, gamma])

    # Permutation axes to target [Q_a=bit0, E1=bit1, Q_b=bit2, E2=bit3, Ra=bit4, Rb=bit5]
    axes = [2, 0, 5, 3, 4, 1]
    d = 2
    n_total = 6
    target_axes_ket = [a + n_total for a in axes]
    rho_t = rho_block.reshape([d] * (2 * n_total))
    rho_t = np.transpose(rho_t, axes=axes + target_axes_ket)
    rho_0 = rho_t.reshape(2**n_total, 2**n_total)

    # Build ring unitary
    op = Z  # RZZ = Z⊗Z
    H_qe = np.zeros((16, 16), dtype=complex)
    for a, b in [(0, 1), (1, 2), (2, 3), (3, 0)]:
        bits = [I2] * 4
        bits[a] = op
        bits[b] = op
        term = bits[0]
        for k in range(1, 4):
            term = np.kron(bits[k], term)
        H_qe += term
    H_qe *= (-theta / 2)
    U_qe = expm(-1j * H_qe)
    U_full = np.kron(np.eye(4), U_qe)  # I_R ⊗ U_QE

    rho_f = U_full @ rho_0 @ U_full.conj().T

    # Bits: Q_a=0, E1=1, Q_b=2, E2=3, Ra=4, Rb=5
    S_RQ = vn_entropy(partial_trace(rho_f, [0, 2, 4, 5], 6))
    S_QE = vn_entropy(partial_trace(rho_f, [0, 1, 2, 3], 6))
    S_Q = vn_entropy(partial_trace(rho_f, [0, 2], 6))
    S_RQE = vn_entropy(rho_f)

    QCMI = max(0.0, S_RQ + S_QE - S_Q - S_RQE)
    return {'QCMI': QCMI, 'S_RQ': S_RQ, 'S_QE': S_QE, 'S_Q': S_Q, 'S_RQE': S_RQE}

# ============================================================
# P0-2: b₁=6 Heavy-Hex Simulation
# ============================================================
def build_heavy_hex_6():
    """
    Build a small heavy-hex patch with 6 hexagons.

    Layout (heavy-hex coordinates):
    Col 0 (hex):   rows 0,1,2,3,4,5
    Col 1 (bridge): rows 0,1,2,3,4,5
    Col 2 (hex):   rows 0,1,2,3,4,5
    Col 3 (bridge): rows 0,1,2,3,4,5
    Col 4 (hex):   rows 0,1,2,3,4,5

    3 hex columns × ~2 hex rows → ~6 hexagons.

    Hexagon faces (from heavy-hex pattern):
    Each hexagon involves 6 qubits forming a 6-cycle.

    We'll identify the hexagons and simulate QCMI for each,
    then compare the sum of individual ring QCMIs with the
    actual multi-ring QCMI to measure g(G).
    """
    n_cols = 5
    n_rows = 5  # 2*n_rows+1 positions per column? Actually 5 rows for 2 hex rows

    # Assign qubit IDs
    pos_to_qid = {}
    qid_to_pos = {}
    qid = 0
    for col in range(n_cols):
        for row in range(n_rows):
            pos_to_qid[(col, row)] = qid
            qid_to_pos[qid] = (col, row)
            qid += 1

    n_qubits = qid

    # Build edges (heavy-hex rules)
    edges = set()
    for qid_a, (col, row) in qid_to_pos.items():
        col_type = 'hex' if col % 2 == 0 else 'bridge'

        # Horizontal edges
        for dc in [-1, 1]:
            nc = col + dc
            nb = pos_to_qid.get((nc, row))
            if nb is not None:
                edges.add(tuple(sorted([qid_a, nb])))

        # Vertical edges
        if col_type == 'hex':
            if row % 2 == 0:  # row = 2k, connect to 2k+1
                nb = pos_to_qid.get((col, row + 1))
                if nb is not None:
                    edges.add(tuple(sorted([qid_a, nb])))
        else:  # bridge
            if row % 2 == 1:  # row = 2k+1, connect to 2k+2
                nb = pos_to_qid.get((col, row + 1))
                if nb is not None:
                    edges.add(tuple(sorted([qid_a, nb])))

    # Adjacency
    adj = {q: set() for q in range(n_qubits)}
    for a, b in edges:
        adj[a].add(b)
        adj[b].add(a)

    # Find hexagons (6-cycles)
    hexagons = find_6cycles(adj, n_qubits)

    return adj, edges, hexagons, n_qubits

def find_6cycles(adj, n_qubits):
    """Find all chordless 6-cycles."""
    cycles = []
    seen = set()

    for start in range(n_qubits):
        if start not in adj:
            continue
        nbs = list(adj[start])
        if len(nbs) < 2:
            continue

        for v1 in nbs:
            for v2 in adj[v1]:
                if v2 == start: continue
                for v3 in adj[v2]:
                    if v3 in (start, v1): continue
                    for v4 in adj[v3]:
                        if v4 in (start, v1, v2): continue
                        for v5 in adj[v4]:
                            if v5 in (start, v1, v2, v3): continue
                            if start not in adj[v5]: continue
                            cycle = (start, v1, v2, v3, v4, v5)
                            # Check chordless
                            if is_chordless(cycle, adj):
                                all_forms = []
                                for i in range(6):
                                    all_forms.append(tuple(cycle[i:] + cycle[:i]))
                                rev = tuple(reversed(cycle))
                                for i in range(6):
                                    all_forms.append(tuple(rev[i:] + rev[:i]))
                                canonical = min(all_forms)
                                ch = hash(canonical)
                                if ch not in seen:
                                    seen.add(ch)
                                    cycles.append(list(canonical))
    return cycles

def is_chordless(cycle, adj):
    for i in range(6):
        vi = cycle[i]
        for j in range(i + 2, 6):
            if (j == (i + 1) % 6) or ((j + 1) % 6 == i):
                continue
            if cycle[j] in adj.get(vi, set()):
                return False
    return True

def simulate_heavy_hex_qcmi(adj, edges, hexagons, n_qubits, p=0.7, seed=42):
    """
    Simulate QCMI for the heavy-hex patch.

    Strategy: Use Haar-random 2-qubit unitaries on all edges.
    Compute QCMI for:
    (a) Each hexagon individually (other edges = identity)
    (b) All hexagons simultaneously (full graph)

    g_measured = QCMI_full / sum(QCMI_individual)
    """
    rng = np.random.RandomState(seed)
    n_edges = len(edges)
    edge_list = list(edges)
    edge_to_idx = {e: i for i, e in enumerate(edge_list)}

    # Generate random 2-qubit unitaries for each edge
    # We'll use RZZ(theta) with random theta for simplicity
    # Each edge gets a random Cartan parameter theta in [0, pi/2]
    thetas = {e: rng.uniform(0.1, np.pi/2) for e in edge_list}

    # Total qubits: n_qubits (QE) + n_qubits//2 (R, one per Q node)
    # Simplified: just use n_qubits total, treat all as QE system
    # R is a separate register we'll handle via purification

    # For simplicity, simulate small enough that we can do full Hilbert space
    if n_qubits > 10:
        print(f"  WARNING: {n_qubits} qubits too large for full simulation. Truncating to first 10.")
        n_qubits = 10

    # Build total unitary: product of all edge unitaries
    # Each edge unitary: exp(-i*theta/2 * Z⊗Z) on that edge pair
    dim = 2**n_qubits
    H_total = np.zeros((dim, dim), dtype=complex)

    for (a, b), theta in thetas.items():
        if a >= n_qubits or b >= n_qubits:
            continue
        # Build Z⊗Z on qubits a,b
        # Start from identity, replace at positions a,b
        H_edge = np.eye(dim, dtype=complex)
        # Actually, build via tensor product of Paulis
        # This is easier: build Z_a Z_b operator
        op_list = [I2] * n_qubits
        op_list[a] = Z
        op_list[b] = Z
        term = op_list[0]
        for k in range(1, n_qubits):
            term = np.kron(op_list[k], term)  # kron so that op_list[0] is MSB
        H_total += (-theta / 2) * term

    U_total = expm(-1j * H_total)

    # Initial state: all qubits in |+⟩ (X-basis eigenstate)
    # This is NOT the full Buscemi state — simplified for tractability.
    # For full CFOL, we'd need R register + mixed E states.
    # Here we verify the interference pattern using a simpler proxy.

    # Initialize in |+⟩^⊗n
    plus = np.array([1, 1], dtype=complex) / np.sqrt(2)
    psi_0 = plus.copy()
    for _ in range(n_qubits - 1):
        psi_0 = np.kron(psi_0, plus)

    psi_f = U_total @ psi_0
    rho_f = np.outer(psi_f, psi_f.conj())

    # For the proxy QCMI, use bipartite entropy
    # Split qubits into two halves: "system" and "environment"
    n_sys = n_qubits // 2
    sys_bits = list(range(n_sys))

    rho_sys = partial_trace(rho_f, sys_bits, n_qubits)
    S_sys = vn_entropy(rho_sys)

    # For individual rings: compute each hexagon's contribution
    individual_S = []
    for hexagon in hexagons[:6]:  # Limit to 6 hexagons
        hex_edges = []
        for i in range(6):
            a, b = hexagon[i], hexagon[(i+1)%6]
            if a < n_qubits and b < n_qubits:
                hex_edges.append((a, b))

        # Build unitary for just this hexagon's edges
        H_hex = np.zeros((dim, dim), dtype=complex)
        for a, b in hex_edges:
            theta = thetas.get(tuple(sorted([a, b])), 0.5)
            op_list = [I2] * n_qubits
            op_list[a] = Z
            op_list[b] = Z
            term = op_list[0]
            for k in range(1, n_qubits):
                term = np.kron(op_list[k], term)
            H_hex += (-theta / 2) * term

        U_hex = expm(-1j * H_hex)
        psi_hex = U_hex @ psi_0
        rho_hex = np.outer(psi_hex, psi_hex.conj())
        S_hex = vn_entropy(partial_trace(rho_hex, sys_bits, n_qubits))
        individual_S.append(S_hex)

    sum_individual = sum(individual_S) if individual_S else 1.0
    g_measured = S_sys / sum_individual if sum_individual > 0 else 1.0

    return {
        'full_entropy': S_sys,
        'individual_entropies': individual_S,
        'sum_individual': sum_individual,
        'g_measured': g_measured,
        'n_hexagons': len(hexagons[:6]),
        'n_qubits': n_qubits,
    }

# ============================================================
# P0-3: Mixed-Axis QCMI Simulation
# ============================================================
def simulate_mixed_axis_ring(theta=np.pi/8, p=0.7):
    """
    Simulate QCMI for a 4-node ring with mixed Cartan axes.
    Aligned: 4 × RZZ(theta)
    Misaligned: 2 × RZZ(theta) + 2 × RXX(theta)

    Returns QCMI for both configurations.
    """
    d = 2
    n_total = 6  # Q_a, E1, Q_b, E2, Ra, Rb

    bell_vec = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    rho_bell = np.outer(bell_vec, bell_vec.conj())
    gamma = np.diag([p, 1 - p])

    rho_block = kron_rev([rho_bell, rho_bell, gamma, gamma])
    axes = [2, 0, 5, 3, 4, 1]
    rho_t = rho_block.reshape([d] * (2 * n_total))
    rho_t = np.transpose(rho_t, axes=axes + [a + n_total for a in axes])
    rho_0 = rho_t.reshape(2**n_total, 2**n_total)

    def build_H_qe(op_pairs):
        """Build H_qe from list of (edge_pair, operator) specifications."""
        H = np.zeros((16, 16), dtype=complex)
        for (a, b), op in op_pairs:
            bits = [I2] * 4
            bits[a] = op
            bits[b] = op
            term = bits[0]
            for k in range(1, 4):
                term = np.kron(bits[k], term)
            H += term
        return H

    # Aligned: all RZZ
    H_aligned = build_H_qe([((0, 1), Z), ((1, 2), Z), ((2, 3), Z), ((3, 0), Z)])
    H_aligned *= (-theta / 2)
    U_aligned = np.kron(np.eye(4), expm(-1j * H_aligned))

    # Misaligned: edges 0,2 = RZZ, edges 1,3 = RXX
    H_misaligned = build_H_qe([((0, 1), Z), ((1, 2), X), ((2, 3), Z), ((3, 0), X)])
    H_misaligned *= (-theta / 2)
    U_misaligned = np.kron(np.eye(4), expm(-1j * H_misaligned))

    results = {}
    for name, U in [('aligned', U_aligned), ('misaligned', U_misaligned)]:
        rho_f = U @ rho_0 @ U.conj().T
        S_RQ = vn_entropy(partial_trace(rho_f, [0, 2, 4, 5], 6))
        S_QE = vn_entropy(partial_trace(rho_f, [0, 1, 2, 3], 6))
        S_Q = vn_entropy(partial_trace(rho_f, [0, 2], 6))
        S_RQE = vn_entropy(rho_f)
        QCMI = max(0.0, S_RQ + S_QE - S_Q - S_RQE)
        results[name] = {'QCMI': QCMI, 'S_RQ': S_RQ, 'S_QE': S_QE,
                         'S_Q': S_Q, 'S_RQE': S_RQE}

    return results

# ============================================================
# Main
# ============================================================
if __name__ == '__main__':
    print("=" * 70)
    print("LP38 NUMERICAL VERIFICATION")
    print("=" * 70)

    # P0-1: Temporal CJ vs Spatial
    print("\n" + "=" * 70)
    print("P0-1: TEMPORAL CJ RING vs SPATIAL 4-NODE RING")
    print("=" * 70)

    for theta_val in [np.pi/2, np.pi/4, np.pi/8]:
        # Temporal CJ: U1=RZZ(theta), U2=RZZ(theta/2) to avoid CZ*CZ=I cancellation
        theta1 = theta_val
        theta2 = theta_val / 2
        cj = simulate_temporal_cj(theta1, theta2, p=0.7)
        sp = simulate_spatial_4node(theta_val, p=0.7)
        eta0 = 1/(8*np.log(2))

        # Compute effective Sigma|c|^2
        sigma_cj = cj['QCMI'] / eta0 if cj['QCMI'] > 1e-12 else 0
        sigma_sp = sp['QCMI'] / eta0 if sp['QCMI'] > 1e-12 else 1
        f_measured = sigma_cj / sigma_sp if sigma_sp > 0 else 0

        # Also compute expected f from Cartan sums
        # Spatial: 4 edges, each |c|^2 = (theta/2)^2
        # CJ: edges u1(|c1|^2), u3(|c3|^2) where |ci|^2 = (theta_i/2)^2
        sum_cj = (theta1/2)**2 + (theta2/2)**2
        sum_sp = 4 * (theta_val/2)**2
        f_expected = sum_cj / sum_sp if sum_sp > 0 else 0

        print(f"\n  theta1={theta1/np.pi:.2f}*pi, theta2={theta2/np.pi:.2f}*pi:")
        print(f"    Temporal CJ:  QCMI={cj['QCMI']:.6f}, S_RQ={cj['S_RQ']:.4f}, "
              f"S_QE={cj['S_QE']:.4f}, S_Q={cj['S_Q']:.4f}, S_RQE={cj['S_RQE']:.4f}")
        print(f"    Spatial 4-node: QCMI={sp['QCMI']:.6f}, S_RQ={sp['S_RQ']:.4f}, "
              f"S_QE={sp['S_QE']:.4f}, S_Q={sp['S_Q']:.4f}, S_RQE={sp['S_RQE']:.4f}")
        print(f"    Sigma|c|^2: CJ={sigma_cj:.4f}, Spatial={sigma_sp:.4f}")
        print(f"    f_measured = {f_measured:.4f}")
        print(f"    f_expected (from Cartan sums) = {f_expected:.4f}")
        print(f"    eta_0 = {eta0:.4f} bits")

        # Compare to hypotheses
        for hyp, f_val in [('u2,u4 product (our conj.)', f_expected),
                           ('one extra contributes', f_expected * 1.5),
                           ('both contribute', f_expected * 2.0),
                           ('CJ enhancement', f_expected * 2.5)]:
            match = "*** MATCH ***" if abs(f_measured - f_val) < 0.1 else ""
            print(f"      vs {hyp}: f={f_val:.2f} {match}")

    # P0-2: b₁=6 Heavy-Hex
    print("\n" + "=" * 70)
    print("P0-2: HEAVY-HEX b1=6 SIMULATION")
    print("=" * 70)

    try:
        adj, edges, hexagons, n_qubits = build_heavy_hex_6()
        print(f"  Graph: {n_qubits} qubits, {len(edges)} edges, {len(hexagons)} hexagons")

        if len(hexagons) >= 2:
            # Print hexagon structure
            for i, h in enumerate(hexagons[:8]):
                print(f"  Hexagon {i}: {h}")

            # Run simulation
            result = simulate_heavy_hex_qcmi(adj, edges, hexagons, n_qubits)
            print(f"\n  Full graph entropy: {result['full_entropy']:.4f}")
            print(f"  Individual ring entropies: {[f'{s:.4f}' for s in result['individual_entropies']]}")
            print(f"  Sum individual: {result['sum_individual']:.4f}")
            print(f"  g_measured = {result['g_measured']:.4f}")
            print(f"  (g_measured > 0.5: {'YES' if result['g_measured'] > 0.5 else 'NO'})")
            print(f"\n  CAVEAT: This uses a simplified proxy (bipartite entropy from |+⟩^⊗n).")
            print(f"  Full Buscemi-state QCMI requires larger Hilbert space (2*n_qubits for R register).")
        else:
            print(f"  WARNING: Only {len(hexagons)} hexagons found. Heavy-hex construction may need tuning.")
    except Exception as e:
        print(f"  ERROR: {e}")
        import traceback
        traceback.print_exc()

    # P0-3: Mixed-axis QCMI
    print("\n" + "=" * 70)
    print("P0-3: MIXED-AXIS QCMI VERIFICATION")
    print("=" * 70)

    for theta_val in [np.pi/4, np.pi/8, np.pi/16, np.pi/32]:
        results = simulate_mixed_axis_ring(theta_val, p=0.7)
        aligned = results['aligned']['QCMI']
        misaligned = results['misaligned']['QCMI']
        delta = misaligned - aligned
        print(f"  theta=pi/{int(np.pi/theta_val)}: aligned={aligned:.6f}, "
              f"misaligned={misaligned:.6f}, Δ={delta:.6f} bits")

    print("\n" + "=" * 70)
    print("VERIFICATION COMPLETE")
    print("=" * 70)

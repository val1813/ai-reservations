"""
Wall A: b1 > 1 multi-ring QCMI scaling.

Tests three topologies:
  T1: Edge-disjoint rings (predicted additive, alpha=1 from sQNM)
  T2: Vertex-sharing chain of rings
  T3: Edge-sharing chain of rings

All Cartan-aligned (same sigma_n direction).
"""
import numpy as np
from itertools import product

def von_neumann_entropy(rho, eps=1e-12):
    evals = np.linalg.eigvalsh(rho)
    evals = np.maximum(evals, eps)
    evals = evals / evals.sum()
    return -np.sum(evals * np.log2(evals))


class CausalGraph:
    """General causal graph with Cartan-aligned edges."""

    def __init__(self, n_qubits, edges, sys_qubits, env_qubits):
        """
        n_qubits: total number of qubits
        edges: list of (u, v, c) where u,v are qubit indices, c is Cartan parameter
        sys_qubits: list of system qubit indices (Q)
        env_qubits: list of environment qubit indices (E)
        """
        self.V = n_qubits
        self.edges = edges  # (u, v, c)
        self.S = sys_qubits
        self.E = env_qubits
        self.d_s = 2 ** len(sys_qubits)
        self.d_e = 2 ** len(env_qubits)

    def diagonal_phase(self, basis_state):
        """Compute total phase exp(i * sum_e c_e * s_u * s_v) for basis state."""
        phase = 0.0
        for u, v, c in self.edges:
            phase += c * basis_state[u] * basis_state[v]
        return phase

    def build_kraus(self, p):
        """Build all Kraus operators K_{env_config}."""
        alpha = {1: np.sqrt(p), -1: np.sqrt(1-p)}
        n_e = len(self.E)

        K_list = []
        for env_config in product([1, -1], repeat=n_e):
            # Build Kraus operator as diagonal matrix on system Hilbert space
            K = np.zeros((self.d_s, self.d_s), dtype=complex)

            # Iterate over all full basis states (S + E)
            env_tuple = tuple(env_config)

            for sys_config in product([1, -1], repeat=len(self.S)):
                # Build full basis state
                full_state = np.zeros(self.V, dtype=int)
                for idx, q in enumerate(self.S):
                    full_state[q] = sys_config[idx]
                for idx, q in enumerate(self.E):
                    full_state[q] = env_config[idx]

                phase = self.diagonal_phase(full_state)

                # Amplitude from environment projection
                amp = 1.0
                for idx, q in enumerate(self.E):
                    amp *= alpha[env_config[idx]]

                # Map system config to index
                sys_idx = sum((1 if s == 1 else 0) << (len(self.S)-1-i)
                             for i, s in enumerate(sys_config))
                K[sys_idx, sys_idx] = amp * np.exp(1j * phase)

            K_list.append(K)

        return K_list

    def gram_matrix(self, p):
        """
        Compute Gram matrix G_{a,b} = <phi(a)|phi(b)> where
        |phi(a)> = sum_k kappa_k(a) |k>_E' is the E' state conditioned
        on system basis state |a>.

        For diagonal Kraus operators, this captures ALL information
        needed for QCMI, without building the full rho_{RE'Q'}.
        """
        alpha = {1: np.sqrt(p), -1: np.sqrt(1-p)}
        d_s = self.d_s
        n_e = len(self.E)

        # Precompute all kappa_k(a) values
        # kappa[k_idx, a_idx] = alpha_k * exp(i * phase(k, a))
        n_kraus = 2 ** n_e
        kappa = np.zeros((n_kraus, d_s), dtype=complex)

        for k_idx, env_config in enumerate(product([1, -1], repeat=n_e)):
            for a_idx, sys_config in enumerate(product([1, -1], repeat=len(self.S))):
                # Full basis state
                full_state = np.zeros(self.V, dtype=int)
                for idx, q in enumerate(self.S):
                    full_state[q] = sys_config[idx]
                for idx, q in enumerate(self.E):
                    full_state[q] = env_config[idx]

                phase = self.diagonal_phase(full_state)
                amp = 1.0
                for ev in env_config:
                    amp *= alpha[ev]
                kappa[k_idx, a_idx] = amp * np.exp(1j * phase)

        # Gram matrix: G[a,b] = sum_k kappa*[k,a] * kappa[k,b]
        G = kappa.conj().T @ kappa  # (d_s, n_kraus) @ (n_kraus, d_s) = (d_s, d_s)

        return G

    def qcmi(self, p):
        """Compute QCMI = I(R;E'|Q') using Gram matrix approach (memory-efficient)."""
        d_s = self.d_s
        G = self.gram_matrix(p)

        # Verify: G_{a,a} should = 1 for trace-preserving channel
        # (off by numerical error, but we can check)

        # S(RQ): rho_RQ on correlated subspace = G/d_s
        rho_RQ_sub = G / d_s
        S_RQ = von_neumann_entropy(rho_RQ_sub)

        # S(Q): diagonal of G/d_s (eigenvalues of reduced Q state)
        # Actually, rho_Q = diag(G_{a,a}/d_s). Since G_{a,a} = 1:
        S_Q = np.log2(d_s)

        # S(EQ): same as S(Q) for the Gram matrix structure
        # (each |phi(a)> is a pure state on E', orthogonal blocks in Q')
        # rho_EQ has eigenvalues = G_{a,a}/d_s = 1/d_s for each a
        S_EQ = np.log2(d_s)

        return S_RQ + S_EQ - S_Q, S_RQ, S_EQ, S_Q


def make_disjoint_rings(b1, c_val=None):
    """b1 independent 4-node rings (edge-disjoint)."""
    if c_val is None:
        c_val = [0.5] * b1  # non-Clifford for nonzero QCMI

    edges = []
    sys_q = []
    env_q = []

    for r in range(b1):
        base = 4 * r
        Qa, E1, Qb, E2 = base, base+1, base+2, base+3
        c = c_val[r] if isinstance(c_val, list) else c_val

        edges.append((Qa, E1, c))
        edges.append((E1, Qb, c))
        edges.append((Qb, E2, c))
        edges.append((E2, Qa, c))

        sys_q.extend([Qa, Qb])
        env_q.extend([E1, E2])

    V = 4 * b1
    return CausalGraph(V, edges, sys_q, env_q)


def make_vertex_sharing_chain(b1, c_val=0.5):
    """Chain of b1 rings, each sharing one system qubit with the next."""
    # Ring 1: Q_0 -> E_0 -> Q_1 -> E'_0 -> Q_0
    # Ring 2: Q_1 -> E_1 -> Q_2 -> E'_1 -> Q_1
    # ...
    # Each ring adds 1 system qubit + 2 environment qubits
    # Total: (b1+1) system + 2*b1 environment = 3*b1 + 1 qubits

    edges = []
    sys_q = list(range(b1 + 1))  # Q_0 ... Q_b1
    env_q = []

    for r in range(b1):
        Qa = r        # Q_r
        Qb = r + 1    # Q_{r+1}
        E1 = b1 + 1 + 2*r      # E_r
        E2 = b1 + 1 + 2*r + 1  # E'_r

        edges.append((Qa, E1, c_val))
        edges.append((E1, Qb, c_val))
        edges.append((Qb, E2, c_val))
        edges.append((E2, Qa, c_val))

        env_q.extend([E1, E2])

    V = (b1 + 1) + 2 * b1
    return CausalGraph(V, edges, sys_q, env_q)


def make_edge_sharing_chain(b1, c_val=0.5):
    """Chain of b1 rings, each sharing one EDGE with the next."""
    # Ring 1: Q_0 -> E_0 -> Q_1 -> E_1 -> Q_0
    # Ring 2: Q_0 -> E_0 -> Q_2 -> E_2 -> Q_0  (shares edge Q_0->E_0)
    # ... all share the same Q_0 -> E_0 edge
    # Total: 1 + 1 + b1 + b1 = 2*b1 + 2 qubits
    # System: Q_0, Q_1, ..., Q_b1
    # Env: E_0 (shared), E_1, E_2, ..., E_b1

    edges = []
    sys_q = list(range(b1 + 1))  # Q_0 ... Q_b1
    env_q = [b1 + 1]  # E_0 is the shared environment qubit

    # Shared edge Q_0 -> E_0 (common to all rings)
    # Each ring r: Q_0 -> E_0 -> Q_{r+1} -> E_{r+1} -> Q_0
    # But note Q_0->E_0 is shared, and each ring has Q_0->E_{r+1} and E_{r+1}->Q_{r+1}

    for r in range(b1):
        Qb = r + 1           # Q_{r+1}
        E_ring = b1 + 2 + r  # E_{r+1}

        edges.append((0, b1 + 1, c_val))     # Q_0 -> E_0 (shared!)
        edges.append((b1 + 1, Qb, c_val))    # E_0 -> Q_{r+1}
        edges.append((Qb, E_ring, c_val))    # Q_{r+1} -> E_{r+1}
        edges.append((E_ring, 0, c_val))     # E_{r+1} -> Q_0

        env_q.append(E_ring)

    V = (b1 + 1) + 1 + b1  # sys + E_0 + ring envs
    # Remove duplicate edges (the shared Q_0->E_0 appears b1 times)
    # Keep only unique edges
    unique_edges = []
    seen = set()
    for u, v, c in edges:
        key = (min(u,v), max(u,v))
        if key not in seen:
            seen.add(key)
            unique_edges.append((u, v, c))

    return CausalGraph(V, unique_edges, sys_q, env_q)


# ============================================================
if __name__ == '__main__':
    print("=" * 60)
    print("Wall A: b1 > 1 QCMI Scaling")
    print("=" * 60)

    # Test 1: Single ring baseline
    print("\n--- Baseline: b1=1 single ring ---")
    for c_test in [0.5, np.pi/4, np.pi/2]:
        g = make_disjoint_rings(1, c_val=c_test)
        qcmi, Srq, Seq, Sq = g.qcmi(0.5)
        clifford = "CLIFFORD" if abs(c_test - np.pi/2) < 1e-10 or abs(c_test) < 1e-10 else ""
        print(f"  c={c_test:.4f}: QCMI={qcmi:.6f} S_RQ={Srq:.4f} {clifford}")

    # Test 2: Edge-disjoint rings (should be additive)
    print("\n--- T1: Edge-disjoint rings (predicted additive, alpha=1) ---")
    for b1 in [1, 2, 3]:
        g = make_disjoint_rings(b1, c_val=0.5)
        qcmi, Srq, Seq, Sq = g.qcmi(0.5)
        per_ring = qcmi / b1
        print(f"  b1={b1}: QCMI={qcmi:.6f} per_ring={per_ring:.6f} S_RQ={Srq:.4f} S_EQ={Seq:.4f} S_Q={Sq:.4f}")

    # Test 3: Vertex-sharing chain
    print("\n--- T2: Vertex-sharing chain ---")
    for b1 in [1, 2, 3, 4]:
        g = make_vertex_sharing_chain(b1, c_val=0.5)
        qcmi, Srq, Seq, Sq = g.qcmi(0.5)
        per_ring = qcmi / b1
        print(f"  b1={b1}: QCMI={qcmi:.6f} per_ring={per_ring:.6f} V={g.V} dim={2**g.V}")

    # Test 4: Edge-sharing chain
    print("\n--- T3: Edge-sharing chain ---")
    for b1 in [1, 2, 3]:
        g = make_edge_sharing_chain(b1, c_val=0.5)
        qcmi, Srq, Seq, Sq = g.qcmi(0.5)
        per_ring = qcmi / b1
        print(f"  b1={b1}: QCMI={qcmi:.6f} per_ring={per_ring:.6f} V={g.V} dim={2**g.V}")

    # Test 5: Scan c for vertex-sharing b1=2
    print("\n--- T2 b1=2: QCMI vs Cartan angle ---")
    for c_n in range(0, 17):
        c = c_n * np.pi / 16
        g = make_vertex_sharing_chain(2, c_val=c)
        qcmi, _, _, _ = g.qcmi(0.5)
        marker = " <-- ZERO" if qcmi < 1e-8 else ""
        print(f"  c={c_n:2d}pi/16: QCMI={qcmi:.8f}{marker}")

    print("\nDone.")

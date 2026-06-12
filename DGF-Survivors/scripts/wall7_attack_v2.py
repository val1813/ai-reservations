"""
Wall #7 Attack v2: T2 Reflux Bound Quantum Monotonicity Test
=============================================================
CRITICAL FIX: System qubits start in |+> = (|0>+|1>)/sqrt(2),
NOT in |0>. This ensures U=exp(ic*sigma_z*sigma_z) creates
non-trivial entanglement rather than degenerating to local phases.

Also adds: X-gates, Y-gates, mixed-axis gates, and non-Clifford
angle scans beyond just sigma_z.

The DGF q-value is the normalized uncertainty:
q_i = S(rho_i) / log(2) where rho_i is the reduced state of qubit i.
"Transition 0->1" = entropy increase of any qubit.
Monotonicity claim: S_i(t) never decreases.
"""

import numpy as np
from itertools import product
import sys
from datetime import datetime

# ============================================================
# UTILITIES
# ============================================================

def von_neumann_entropy(rho, eps=1e-12):
    """Compute von Neumann entropy of a density matrix."""
    evals = np.linalg.eigvalsh(rho)
    evals = np.maximum(np.real(evals), eps)
    evals = evals / evals.sum()
    S = -np.sum(evals * np.log2(np.maximum(evals, eps)))
    return float(S)

def partial_trace(rho, keep_qubits, n_total):
    """Trace out all qubits except keep_qubits."""
    d_total = 2 ** n_total
    d_keep = 2 ** len(keep_qubits)
    rho_reduced = np.zeros((d_keep, d_keep), dtype=complex)
    sorted_keep = sorted(keep_qubits)

    for i in range(d_total):
        i_keep = 0
        for pos, q in enumerate(sorted_keep):
            bit = (i >> (n_total - 1 - q)) & 1
            i_keep |= (bit << (len(keep_qubits) - 1 - pos))

        for j in range(d_total):
            j_keep = 0
            for pos, q in enumerate(sorted_keep):
                bit = (j >> (n_total - 1 - q)) & 1
                j_keep |= (bit << (len(keep_qubits) - 1 - pos))
            rho_reduced[i_keep, j_keep] += rho[i, j]

    return rho_reduced

# ============================================================
# PAULI GATE CONSTRUCTORS
# ============================================================

# Pauli matrices
sx = np.array([[0, 1], [1, 0]], dtype=complex)
sy = np.array([[0, -1j], [1j, 0]], dtype=complex)
sz = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)

# |+> state: (|0> + |1>)/sqrt(2) -> density = [[0.5, 0.5], [0.5, 0.5]]
rho_plus = np.array([[0.5, 0.5], [0.5, 0.5]], dtype=complex)

# |-> state: (|0> - |1>)/sqrt(2) -> density = [[0.5, -0.5], [-0.5, 0.5]]
rho_minus = np.array([[0.5, -0.5], [-0.5, 0.5]], dtype=complex)

# |0> state: density = [[1, 0], [0, 0]]
rho_zero = np.array([[1, 0], [0, 0]], dtype=complex)

# Environment mixed state: p|+><+| + (1-p)|-><-|
def rho_env(p):
    """rho_E = p*|+><+| + (1-p)*|-><-|
    In computational basis: [[0.5, p-0.5], [p-0.5, 0.5]]
    """
    return np.array([[0.5, p - 0.5], [p - 0.5, 0.5]], dtype=complex)

class QuantumRingSimulatorV2:
    """Full density matrix simulation with configurable initial states
    and Pauli axis for gates.

    Parameters:
    - b1: number of rings
    - p_env: env qubit parameter (p in |gamma> = sqrt(p)|+> + sqrt(1-p)|->)
    - sys_init: 'plus' | 'zero' | 'mixed(p)' | 'bell'(entangled)
    - gate_axis: 'Z' | 'X' | 'Y' | 'mixed'
    - c_val: Cartan coupling parameter
    """

    def __init__(self, b1, p_env=0.5, sys_init='plus', gate_axis='Z', c_val=0.5,
                 sys_p=None):
        self.b1 = b1
        self.p_env = p_env
        self.sys_init = sys_init
        self.gate_axis = gate_axis
        self.c_val = c_val
        self.n_sys = b1 + 1
        self.n_env = 2 * b1
        self.n_total = self.n_sys + self.n_env
        self.d_total = 2 ** self.n_total

        self.sys_qubits = list(range(self.n_sys))
        self.env_qubits = list(range(self.n_sys, self.n_total))

        # Build ring topology
        self.rings = []
        for r in range(b1):
            Q_a, Q_b = r, r + 1
            E_1, E_2 = self.n_sys + 2*r, self.n_sys + 2*r + 1
            self.rings.append({
                'Q_a': Q_a, 'E_1': E_1, 'Q_b': Q_b, 'E_2': E_2,
                'edges': [(Q_a, E_1), (E_1, Q_b), (Q_b, E_2), (E_2, Q_a)]
            })

        # Initialize density matrix
        self.rho = self._init_rho(sys_p)
        self.step = 0
        self.history = []

    def _init_rho(self, sys_p=None):
        """Build initial density matrix."""
        if self.sys_init == 'plus':
            rho_sys = rho_plus
        elif self.sys_init == 'zero':
            rho_sys = rho_zero
        elif self.sys_init == 'minus':
            rho_sys = rho_minus
        elif self.sys_init == 'mixed':
            p_s = sys_p if sys_p is not None else 0.5
            rho_sys = rho_env(p_s)
        elif self.sys_init == 'bell':
            # Bell state: (|00>+|11>)/sqrt(2) for pairs of system qubits
            # For simplicity, start with |+> for unpaired and build rho
            # Actually, build the full N_sys-qubit Bell-pair state
            return self._init_bell()
        else:
            rho_sys = rho_plus

        rho = np.array([[1.0]], dtype=complex)
        for q in range(self.n_total):
            if q in self.sys_qubits:
                rho = np.kron(rho, rho_sys)
            else:
                rho = np.kron(rho, rho_env(self.p_env))
        return rho

    def _init_bell(self):
        """Initialize system qubits in chain of Bell pairs with reference.
        For small b1, we implement the Bell pair between adjacent system qubits.
        Q_0 and Q_1 share |Phi+> = (|00>+|11>)/sqrt(2)
        """
        # This is complex for b1>1. Start with all sys qubits in |+>
        # then apply CNOTs between adjacent pairs to create entanglement.
        # For b1=1: Q_0, Q_1 in Bell state |Phi+>
        # For b1>1: Q_i and Q_{i+1} share Bell pairs (pairwise)

        if self.b1 == 1:
            # |Phi+> = (|00>+|11>)/sqrt(2) for Q_0, Q_1
            bell = np.array([[1, 0, 0, 1],
                              [0, 0, 0, 0],
                              [0, 0, 0, 0],
                              [1, 0, 0, 1]], dtype=complex) / 2.0
            # Add env qubits
            rho = bell.copy()
            for _ in range(self.n_env):
                rho = np.kron(rho, rho_env(self.p_env))
            return rho

        # For b1>1, start ALL system qubits in |+> and add pairwise Bell
        # This is a simplification - true DGF uses reference R
        rho = np.array([[1.0]], dtype=complex)
        for q in range(self.n_total):
            if q in self.sys_qubits:
                rho = np.kron(rho, rho_plus)
            else:
                rho = np.kron(rho, rho_env(self.p_env))
        return rho

    def _get_pauli_for_axis(self, axis):
        """Return the Pauli matrix for given axis character."""
        if axis.upper() == 'X':
            return sx
        elif axis.upper() == 'Y':
            return sy
        elif axis.upper() == 'Z':
            return sz
        else:
            raise ValueError(f"Unknown gate axis: {axis}")

    def _compute_gate_matrix_2q(self, c, axis):
        """Compute the 4x4 two-qubit gate matrix U = exp(i*c*P⊗P)."""
        P = self._get_pauli_for_axis(axis)
        # P⊗P has eigenvalues +1 (degenerate) and -1 (degenerate)
        # exp(i*c*P⊗P) = cos(c)*I + i*sin(c)*P⊗P
        P_otimes = np.kron(P, P)
        U = np.cos(c) * np.eye(4, dtype=complex) + 1j * np.sin(c) * P_otimes
        return U

    def _get_2q_gate_full(self, u, v, c, axis):
        """Get full d_total x d_total gate matrix for gate on qubits u,v.

        For Z-axis (sigma_z), we can use the efficient diagonal method.
        For X/Y axes, we need the full matrix exponential.
        """
        if axis == 'Z' or axis == 'z':
            # Efficient diagonal implementation for sigma_z
            return None  # Signal to use _apply_gate_z

        # For X/Y: construct full matrix
        U_2q = self._compute_gate_matrix_2q(c, axis)

        # Embed into full Hilbert space
        # We need to permute qubits so that u, v are the first two
        # Build the full unitary by expanding to n_total qubits

        # Simpler approach: apply directly using computational basis
        # U_2q has 4x4 matrix elements between |uv> states
        # In the full space, U[b0...bu...bv...bn-1, b0'...bu'...bv'...bn-1']
        # = delta(other_qubits_same) * U_2q[bu,bv][bu',bv']

        U_full = np.zeros((self.d_total, self.d_total), dtype=complex)

        for i in range(self.d_total):
            i_u = (i >> (self.n_total - 1 - u)) & 1
            i_v = (i >> (self.n_total - 1 - v)) & 1
            idx_uv = (i_u << 1) | i_v  # 2-bit index for u,v

            for j in range(self.d_total):
                j_u = (j >> (self.n_total - 1 - u)) & 1
                j_v = (j >> (self.n_total - 1 - v)) & 1
                idx_uv_j = (j_u << 1) | j_v

                # Check that all OTHER qubits match
                mask = (1 << self.n_total) - 1
                mask_uv = ((1 << (self.n_total - 1 - u)) |
                            (1 << (self.n_total - 1 - v)))
                if (i & ~mask_uv) == (j & ~mask_uv):
                    U_full[i, j] = U_2q[idx_uv, idx_uv_j]

        return U_full

    def apply_gate(self, u, v, c=None, axis=None, label="gate"):
        """Apply gate U=exp(i*c*P⊗P) on qubits (u,v)."""
        if c is None:
            c = self.c_val
        if axis is None:
            axis = self.gate_axis

        if axis == 'Z' or axis == 'z':
            # Efficient diagonal implementation
            phases = np.zeros(self.d_total, dtype=complex)
            for idx in range(self.d_total):
                b_u = (idx >> (self.n_total - 1 - u)) & 1
                b_v = (idx >> (self.n_total - 1 - v)) & 1
                z_u = 1.0 if b_u == 0 else -1.0
                z_v = 1.0 if b_v == 0 else -1.0
                phases[idx] = np.exp(1j * c * z_u * z_v)
            phase_diff = phases[:, None] * np.conj(phases[None, :])
            self.rho = self.rho * phase_diff
        else:
            # Full matrix multiplication for X/Y
            U_full = self._get_2q_gate_full(u, v, c, axis)
            self.rho = U_full @ self.rho @ U_full.conj().T

        self.step += 1
        self.history.append((self.step, f"U_{axis}({u},{v}) c={c:.4f}", self.rho.copy()))

    def compute_qubit_entropies(self, rho=None):
        """Compute von Neumann entropy for each qubit's reduced state."""
        if rho is None:
            rho = self.rho
        entropies = {}
        for q in range(self.n_total):
            rho_q = partial_trace(rho, [q], self.n_total)
            entropies[q] = von_neumann_entropy(rho_q)
        return entropies

    def compute_entropy_history(self):
        """Recompute entropy for each qubit at each history step."""
        entropy_history = {}
        for q in range(self.n_total):
            entropy_history[q] = []
            for step, desc, rho_step in self.history:
                entropies = self.compute_qubit_entropies(rho_step)
                entropy_history[q].append(entropies[q])
        return entropy_history

    def check_monotonicity(self, tol=1e-10):
        """Check if any qubit shows non-monotonic entropy evolution.
        Returns list of violations where S decreases.
        """
        entropy_history = self.compute_entropy_history()
        violations = []

        for q in range(self.n_total):
            S_q = np.array(entropy_history[q])
            for t in range(len(S_q) - 1):
                delta = S_q[t+1] - S_q[t]
                if delta < -tol:
                    violations.append({
                        'qubit': q,
                        'qubit_type': 'sys' if q < self.n_sys else 'env',
                        'step': t + 1,
                        'S_before': float(S_q[t]),
                        'S_after': float(S_q[t+1]),
                        'delta_S': float(delta)
                    })

        return violations, entropy_history


# ============================================================
# SCAN FUNCTIONS
# ============================================================

def get_forward_edges(b1, n_sys):
    """Get forward edge ordering for b1 rings."""
    all_edges = []
    for r in range(b1):
        Q_a, Q_b = r, r + 1
        E_1, E_2 = n_sys + 2*r, n_sys + 2*r + 1
        all_edges.extend([(Q_a, E_1), (E_1, Q_b), (Q_b, E_2), (E_2, Q_a)])
    return all_edges


def scan_single_ring_v2():
    """Comprehensive scan of single ring with |+> initial system state."""
    print("=" * 70)
    print("V2 SCAN: Single Ring with |+> system initial state")
    print("=" * 70)

    c_values = np.linspace(0.1, 1.5, 15)
    p_values = [0.1, 0.2, 0.3, 0.5, 0.7, 0.8, 0.9]
    axes = ['Z', 'X', 'Y']
    n_rounds_list = [1, 2, 3, 5, 8]

    all_results = {}
    real_violations = []  # Violations with |delta| > 1e-8

    total = len(c_values) * len(p_values) * len(axes) * len(n_rounds_list)
    count = 0

    for axis in axes:
        for p_val in p_values:
            for c_val in c_values:
                for n_rounds in n_rounds_list:
                    count += 1

                    sim = QuantumRingSimulatorV2(
                        b1=1, p_env=p_val, sys_init='plus',
                        gate_axis=axis, c_val=c_val
                    )

                    edges = get_forward_edges(1, 2)
                    for rnd in range(n_rounds):
                        for u, v in edges:
                            sim.apply_gate(u, v, c_val, axis, f"R{rnd}_{u}{v}")

                    violations, entropy_hist = sim.check_monotonicity(tol=1e-8)
                    real_v = [v for v in violations if abs(v['delta_S']) > 1e-8]

                    config_key = f"{axis}_p={p_val:.2f}_c={c_val:.4f}_R={n_rounds}"
                    all_results[config_key] = {
                        'axis': axis, 'p': p_val, 'c': float(c_val),
                        'rounds': n_rounds, 'n_violations': len(real_v),
                        'violations': real_v
                    }

                    if real_v:
                        real_violations.append((config_key, real_v))

                    if count % 100 == 0:
                        print(f"  Progress: {count}/{total} ({len(real_violations)} real violations)")

    print(f"\n  Total configs: {len(all_results)}")
    print(f"  Real violations (|delta|>1e-8): {len(real_violations)}")

    # Summarize by axis
    for axis in axes:
        axis_configs = [k for k in all_results if k.startswith(axis)]
        axis_violations = [v for k, vl in real_violations if k.startswith(axis)]
        print(f"  {axis}-axis: {len(axis_configs)} configs, {len(axis_violations)} violations")

    # Show sample real violations
    if real_violations:
        print(f"\n  Sample real violations:")
        for key, vl in real_violations[:10]:
            print(f"    {key}:")
            for v in vl[:3]:
                print(f"      Q{v['qubit']}({v['qubit_type']}): S={v['S_before']:.6f} -> {v['S_after']:.6f}, "
                      f"delta={v['delta_S']:.6f}")

    return all_results, real_violations


def scan_mixed_init_states():
    """Scan with system qubits having non-trivial initial entropy."""
    print("\n" + "=" * 70)
    print("V2: Mixed Initial System States")
    print("=" * 70)

    # System qubits start in mixed state: p_sys|+><+| + (1-p_sys)|-><-|
    # This gives them initial entropy, allowing reflux detection.
    sys_p_values = [0.3, 0.5, 0.7]  # Initial system uncertainty
    env_p_values = [0.1, 0.3, 0.5, 0.7, 0.9]  # Initial env uncertainty
    axes = ['Z', 'X']
    c_values = [0.2, 0.5, 0.8, 1.0, np.pi/4]
    n_rounds_list = [2, 5, 10]

    results = {}
    real_violations = []

    total = len(sys_p_values) * len(env_p_values) * len(axes) * len(c_values) * len(n_rounds_list)
    count = 0

    for axis in axes:
        for sys_p in sys_p_values:
            for env_p in env_p_values:
                for c_val in c_values:
                    for n_rounds in n_rounds_list:
                        count += 1

                        sim = QuantumRingSimulatorV2(
                            b1=1, p_env=env_p, sys_init='mixed',
                            gate_axis=axis, c_val=c_val, sys_p=sys_p
                        )

                        edges = get_forward_edges(1, 2)
                        for rnd in range(n_rounds):
                            for u, v in edges:
                                sim.apply_gate(u, v, c_val, axis, f"R{rnd}")

                        violations, entropy_hist = sim.check_monotonicity(tol=1e-8)
                        real_v = [v for v in violations if abs(v['delta_S']) > 1e-8]

                        config_key = f"{axis}_Sp={sys_p:.2f}_Ep={env_p:.2f}_c={c_val:.4f}_R={n_rounds}"
                        results[config_key] = {
                            'axis': axis, 'sys_p': sys_p, 'env_p': env_p,
                            'c': float(c_val), 'rounds': n_rounds,
                            'n_violations': len(real_v), 'violations': real_v
                        }

                        if real_v:
                            real_violations.append((config_key, real_v))

                        if count % 100 == 0:
                            print(f"  Progress: {count}/{total} ({len(real_violations)} violations)")

    print(f"\n  Total configs: {len(results)}")
    print(f"  Real violations: {len(real_violations)}")

    if real_violations:
        print(f"\n  Violation details:")
        for key, vl in real_violations[:15]:
            print(f"    {key}: {len(vl)} violations")
            for v in vl[:3]:
                print(f"      Q{v['qubit']}({v['qubit_type']}): {v['S_before']:.4f} -> {v['S_after']:.4f}")

    return results, real_violations


def scan_bell_init():
    """Scan with Bell-state initialization (DGF-like)."""
    print("\n" + "=" * 70)
    print("V2: Bell State Initialization (DGF-like)")
    print("=" * 70)

    axes = ['Z', 'X']
    p_values = [0.1, 0.3, 0.5, 0.7, 0.9]
    c_values = [0.2, 0.5, 0.8, 1.0, np.pi/4, np.pi/2]
    n_rounds_list = [1, 2, 3, 5]

    results = {}
    real_violations = []

    for axis in axes:
        for p_val in p_values:
            for c_val in c_values:
                for n_rounds in n_rounds_list:
                    sim = QuantumRingSimulatorV2(
                        b1=1, p_env=p_val, sys_init='bell',
                        gate_axis=axis, c_val=c_val
                    )

                    edges = get_forward_edges(1, 2)
                    for rnd in range(n_rounds):
                        for u, v in edges:
                            sim.apply_gate(u, v, c_val, axis, f"R{rnd}")

                    violations, entropy_hist = sim.check_monotonicity(tol=1e-8)
                    real_v = [v for v in violations if abs(v['delta_S']) > 1e-8]

                    config_key = f"BELL_{axis}_p={p_val:.2f}_c={c_val:.4f}_R={n_rounds}"
                    results[config_key] = {
                        'init': 'bell', 'axis': axis, 'p': p_val,
                        'c': float(c_val), 'rounds': n_rounds,
                        'n_violations': len(real_v), 'violations': real_v
                    }

                    if real_v:
                        real_violations.append((config_key, real_v))

    print(f"\n  Total configs: {len(results)}")
    print(f"  Real violations: {len(real_violations)}")

    if real_violations:
        print(f"\n  Bell-state violations:")
        for key, vl in real_violations[:10]:
            print(f"    {key}: {len(vl)} violations")
            for v in vl[:3]:
                print(f"      Q{v['qubit']}({v['qubit_type']}): {v['S_before']:.4f} -> {v['S_after']:.4f}")

    return results, real_violations


def scan_multi_ring_v2(b1_values=[2]):
    """Multi-ring scan with |+> initialization."""
    print("\n" + "=" * 70)
    print(f"V2: Multi-Ring Scan (b1={b1_values})")
    print("=" * 70)

    results = {}
    real_violations = []

    for b1 in b1_values:
        n_total = (b1 + 1) + 2 * b1
        d_total = 2 ** n_total
        if d_total > 256:
            print(f"  b1={b1}: matrix {d_total}x{d_total} too large, skipping")
            continue

        print(f"  b1={b1}: {n_total} qubits, {d_total}x{d_total} matrix")

        axes = ['Z', 'X']
        p_values = [0.3, 0.5, 0.7]
        c_values = [0.3, 0.5, 0.8, 1.0]
        n_rounds_list = [1, 2, 3]

        for axis in axes:
            for p_val in p_values:
                for c_val in c_values:
                    for n_rounds in n_rounds_list:
                        sim = QuantumRingSimulatorV2(
                            b1=b1, p_env=p_val, sys_init='plus',
                            gate_axis=axis, c_val=c_val
                        )

                        edges = get_forward_edges(b1, b1+1)
                        for rnd in range(n_rounds):
                            for u, v in edges:
                                sim.apply_gate(u, v, c_val, axis, f"R{rnd}")

                        violations, _ = sim.check_monotonicity(tol=1e-8)
                        real_v = [v for v in violations if abs(v['delta_S']) > 1e-8]

                        config_key = f"b1={b1}_{axis}_p={p_val}_c={c_val:.4f}_R={n_rounds}"
                        results[config_key] = {
                            'b1': b1, 'axis': axis, 'p': p_val,
                            'c': float(c_val), 'rounds': n_rounds,
                            'n_violations': len(real_v), 'violations': real_v
                        }

                        if real_v:
                            real_violations.append((config_key, real_v))

    print(f"\n  Total: {len(results)}, Violations: {len(real_violations)}")
    return results, real_violations


def deep_entropy_tracking():
    """Detailed entropy tracking for representative configurations."""
    print("\n" + "=" * 70)
    print("V2: Deep Entropy Tracking")
    print("=" * 70)

    configs = [
        # (name, b1, sys_init, sys_p, env_p, axis, c, rounds)
        ("Z_plus", 1, 'plus', None, 0.5, 'Z', 0.5, 3),
        ("X_plus", 1, 'plus', None, 0.5, 'X', 0.5, 3),
        ("Y_plus", 1, 'plus', None, 0.5, 'Y', 0.5, 3),
        ("Z_bell_p05", 1, 'bell', None, 0.5, 'Z', 0.5, 3),
        ("Z_bell_p03", 1, 'bell', None, 0.3, 'Z', 0.5, 3),
        ("X_bell_p05", 1, 'bell', None, 0.5, 'X', 0.5, 3),
        ("Z_mixed", 1, 'mixed', 0.5, 0.5, 'Z', 0.5, 3),
        ("X_mixed", 1, 'mixed', 0.5, 0.5, 'X', 0.5, 3),
        ("Z_c_small", 1, 'plus', None, 0.5, 'Z', 0.2, 5),
        ("Z_c_large", 1, 'plus', None, 0.5, 'Z', np.pi/4, 5),
        ("X_c_large", 1, 'plus', None, 0.5, 'X', np.pi/4, 5),
        ("Z_b1=2", 2, 'plus', None, 0.5, 'Z', 0.5, 2),
        ("X_b1=2", 2, 'plus', None, 0.5, 'X', 0.5, 2),
    ]

    analysis = {}

    for name, b1, sys_init, sys_p, env_p, axis, c, rounds in configs:
        n_total = (b1 + 1) + 2 * b1
        if 2 ** n_total > 256:
            continue

        sim = QuantumRingSimulatorV2(
            b1=b1, p_env=env_p, sys_init=sys_init,
            gate_axis=axis, c_val=c, sys_p=sys_p
        )

        # Record initial state
        init_entropies = sim.compute_qubit_entropies()

        edges = get_forward_edges(b1, b1+1)
        for rnd in range(rounds):
            for u, v in edges:
                sim.apply_gate(u, v, c, axis, f"R{rnd}")

        violations, entropy_hist = sim.check_monotonicity(tol=1e-8)
        real_v = [v for v in violations if abs(v['delta_S']) > 1e-8]
        final_entropies = sim.compute_qubit_entropies()

        # Track max entropy change
        max_increase = 0
        max_decrease = 0
        for q in range(n_total):
            S_q = np.array(entropy_hist[q])
            for t in range(len(S_q) - 1):
                delta = float(S_q[t+1] - S_q[t])
                if delta > max_increase:
                    max_increase = delta
                if delta < max_decrease:
                    max_decrease = delta

        analysis[name] = {
            'b1': b1, 'axis': axis, 'sys_init': sys_init,
            'p_env': env_p, 'c': c, 'rounds': rounds,
            'n_steps': sim.step,
            'init_entropies': {str(k): round(float(v), 6) for k, v in init_entropies.items()},
            'final_entropies': {str(k): round(float(v), 6) for k, v in final_entropies.items()},
            'n_violations': len(real_v),
            'max_S_increase': round(max_increase, 6),
            'max_S_decrease': round(max_decrease, 6),
            'violations': real_v[:5]
        }

        # Print
        sys_init_S = np.mean([v for k, v in init_entropies.items() if int(k) < sim.n_sys])
        env_init_S = np.mean([v for k, v in init_entropies.items() if int(k) >= sim.n_sys])
        sys_final_S = np.mean([v for k, v in final_entropies.items() if int(k) < sim.n_sys])
        env_final_S = np.mean([v for k, v in final_entropies.items() if int(k) >= sim.n_sys])

        print(f"\n  {name}: b1={b1}, axis={axis}, init={sys_init}, p_env={env_p}, c={c:.4f}, rounds={rounds}")
        print(f"    Steps: {sim.step}")
        print(f"    S_sys: {sys_init_S:.4f} -> {sys_final_S:.4f}  (max_delta: +{analysis[name]['max_S_increase']:.4f}/{analysis[name]['max_S_decrease']:.4f})")
        print(f"    S_env: {env_init_S:.4f} -> {env_final_S:.4f}")

        if real_v:
            print(f"    *** {len(real_v)} REAL MONOTONICITY VIOLATIONS ***")
            for v in real_v[:5]:
                print(f"        Q{v['qubit']}({v['qubit_type']}): t={v['step']}: {v['S_before']:.6f} -> {v['S_after']:.6f} (delta={v['delta_S']:.6f})")
        else:
            print(f"    No real violations")

    return analysis


def compute_reflux_analysis():
    """Quantify reflux: track entropy flow between system and environment."""
    print("\n" + "=" * 70)
    print("V2: Reflux Quantification (Entropy Flow)")
    print("=" * 70)

    # Use mixed initial states so both sys and env have non-zero entropy
    b1 = 1
    n_sys = 2
    n_env = 2
    n_total = 4

    configs = [
        ("Z_balanced", 'Z', 0.6, 0.5, 0.5, 5),
        ("X_balanced", 'X', 0.6, 0.5, 0.5, 5),
        ("Z_skewed", 'Z', 0.8, 0.2, 0.5, 5),
        ("X_skewed", 'X', 0.8, 0.2, 0.5, 5),
        ("Z_rev", 'Z', 0.2, 0.8, 0.5, 5),
    ]

    results = {}

    for name, axis, sys_p, env_p, c, rounds in configs:
        n_sys_init = 2
        n_env_init = 2

        sim = QuantumRingSimulatorV2(
            b1=1, p_env=env_p, sys_init='mixed',
            gate_axis=axis, c_val=c, sys_p=sys_p
        )

        init_entropies = sim.compute_qubit_entropies()

        edges = get_forward_edges(1, 2)
        for rnd in range(rounds):
            for u, v in edges:
                sim.apply_gate(u, v, c, axis, f"R{rnd}")

        final_entropies = sim.compute_qubit_entropies()

        # Track total entropy per subsystem
        S_sys_init = sum(init_entropies[q] for q in range(n_sys))
        S_env_init = sum(init_entropies[q] for q in range(n_sys, n_total))
        S_sys_final = sum(final_entropies[q] for q in range(n_sys))
        S_env_final = sum(final_entropies[q] for q in range(n_sys, n_total))

        # Count entropy-increase and entropy-decrease events per subsystem
        sys_inc = 0
        sys_dec = 0
        env_inc = 0
        env_dec = 0

        entropy_hist = sim.compute_entropy_history()
        for q in range(n_sys):
            S_q = np.array(entropy_hist[q])
            for t in range(len(S_q) - 1):
                delta = S_q[t+1] - S_q[t]
                if delta > 1e-10:
                    sys_inc += 1
                elif delta < -1e-10:
                    sys_dec += 1

        for q in range(n_sys, n_total):
            S_q = np.array(entropy_hist[q])
            for t in range(len(S_q) - 1):
                delta = S_q[t+1] - S_q[t]
                if delta > 1e-10:
                    env_inc += 1
                elif delta < -1e-10:
                    env_dec += 1

        # Reflux: env decreases (losing entropy to system) / system increases
        # This represents information flowing back from env to sys
        reflux = env_dec
        forward = env_inc
        total_events = reflux + forward

        # Classical DGF bound: P_reflux <= N_S*q_S / (N_E*q_E)
        q_S_initial = np.mean([init_entropies[q] for q in range(n_sys)]) / np.log2(2)
        q_E_initial = np.mean([init_entropies[q] for q in range(n_sys, n_total)]) / np.log2(2)
        classical_bound = (n_sys * q_S_initial) / (n_env * q_E_initial) if q_E_initial > 1e-10 else float('inf')
        actual_p_reflux = reflux / total_events if total_events > 0 else 0

        results[name] = {
            'axis': axis, 'sys_p': sys_p, 'env_p': env_p, 'c': c,
            'S_sys_init': float(S_sys_init), 'S_sys_final': float(S_sys_final),
            'S_env_init': float(S_env_init), 'S_env_final': float(S_env_final),
            'sys_inc': sys_inc, 'sys_dec': sys_dec,
            'env_inc': env_inc, 'env_dec': env_dec,
            'total_events': total_events,
            'actual_P_reflux': float(actual_p_reflux),
            'classical_bound': float(classical_bound),
            'q_S_init': float(q_S_initial),
            'q_E_init': float(q_E_initial)
        }

        print(f"\n  {name}: axis={axis}, sys_p={sys_p}, env_p={env_p}, c={c}")
        print(f"    S_sys: {S_sys_init:.4f} -> {S_sys_final:.4f}")
        print(f"    S_env: {S_env_init:.4f} -> {S_env_final:.4f}")
        print(f"    Sys: +{sys_inc}/-{sys_dec}, Env: +{env_inc}/-{env_dec}")
        print(f"    P_reflux(actual) = {actual_p_reflux:.4f}")
        print(f"    P_reflux(bound) <= {classical_bound:.4f}")
        print(f"    q_S_initial={q_S_initial:.4f}, q_E_initial={q_E_initial:.4f}")

        if actual_p_reflux > classical_bound + 1e-10:
            print(f"    *** CLASSICAL BOUND VIOLATED! ***")

    return results


# ============================================================
# MAIN
# ============================================================

def main():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("=" * 70)
    print(f"WALL #7 ATTACK v2: T2 Reflux Bound Quantum Monotonicity")
    print(f"Started: {timestamp}")
    print("=" * 70)
    print()
    print("Key improvements over v1:")
    print("  - System qubits start in |+> (not |0>) to enable entanglement")
    print("  - X, Y, Z Pauli axes tested (not just Z)")
    print("  - Mixed and Bell initial states included")
    print("  - Proper entropy tolerance (1e-8) for real vs numerical violations")
    print()

    all_data = {'timestamp': timestamp}

    # 1. Basic |+> scan
    r1, v1 = scan_single_ring_v2()
    all_data['scan_plus'] = {'configs': len(r1), 'real_violations': len(v1)}

    # 2. Mixed initial states
    r2, v2 = scan_mixed_init_states()
    all_data['scan_mixed'] = {'configs': len(r2), 'real_violations': len(v2)}

    # 3. Bell initialization
    r3, v3 = scan_bell_init()
    all_data['scan_bell'] = {'configs': len(r3), 'real_violations': len(v3)}

    # 4. Multi-ring
    r4, v4 = scan_multi_ring_v2([2])
    all_data['scan_multi'] = {'configs': len(r4), 'real_violations': len(v4)}

    # 5. Deep tracking
    deep = deep_entropy_tracking()
    all_data['deep_analysis'] = {k: {'n_violations': d['n_violations']} for k, d in deep.items()}

    # 6. Reflux quantification
    reflux = compute_reflux_analysis()
    all_data['reflux'] = reflux

    # ============================================================
    # FINAL SUMMARY
    # ============================================================
    print("\n" + "=" * 70)
    print("FINAL VERDICT")
    print("=" * 70)

    total_configs = (len(r1) + len(r2) + len(r3) + len(r4))
    total_violations = len(v1) + len(v2) + len(v3) + len(v4)

    print(f"\n  Total configurations tested: {total_configs}")
    print(f"  Configurations with REAL monotonicity violations: {total_violations}")

    # Check reflux bounds
    bound_violations = [k for k, v in reflux.items() if v['actual_P_reflux'] > v['classical_bound'] + 1e-10]
    print(f"  Reflux bound violations: {len(bound_violations)}")

    if total_violations > 0:
        print(f"\n  *** MONOTONICITY VIOLATIONS FOUND ***")
        print(f"  Quantum dynamics DOES NOT respect per-node monotonicity.")
        print(f"  The classical T2 proof assumption fails in quantum domain.")
    else:
        print(f"\n  *** NO MONOTONICITY VIOLATIONS FOUND ***")
        print(f"  After {total_configs} configurations, no evidence of")
        print(f"  non-monotonic per-qubit entropy evolution was detected.")
        print(f"  This is consistent with monotonicity holding in the")
        print(f"  quantum domain for the DGF causal ring.")

    if bound_violations:
        print(f"\n  *** REFLUX BOUND VIOLATIONS IN: {bound_violations} ***")
    else:
        print(f"\n  All reflux rates satisfy the classical bound.")

    return all_data


if __name__ == '__main__':
    main()

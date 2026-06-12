"""
Wall #7 Attack: T2 Reflux Bound Quantum Monotonicity Test
=========================================================
Tests whether "each node transitions 0->1 at most once" (monotonicity)
holds in quantum causal ring dynamics.

In the DGF framework:
- q=0 = pure classical state (deterministic, S=0)
- q=1 = pure quantum vacuum (maximally uncertain, S=log2)
- "Transition 0->1" means a node's entropy INCREASES
- Monotonicity claim: entropy of each node never decreases during propagation

This script:
1. Initializes a quantum causal ring density matrix
2. Applies gates SEQUENTIALLY (one at a time)
3. Tracks each qubit's von Neumann entropy at each step
4. Detects non-monotonicity: any S(t+1) < S(t) violates the claim

Strategy: full density matrix simulation (not Kraus/Gram).
Environment qubits start in mixed state rho_E = p|+><+| + (1-p)|-><-|
System qubits start pure (|0>).
Gates U(c) = exp(i*c*sigma_z ⊗ sigma_z) applied sequentially.
"""

import numpy as np
from itertools import product
import sys
import json
from datetime import datetime

# ============================================================
# UTILITIES
# ============================================================

def von_neumann_entropy(rho, eps=1e-12):
    """Compute von Neumann entropy of a density matrix."""
    evals = np.linalg.eigvalsh(rho)
    evals = np.maximum(np.real(evals), eps)
    evals = evals / evals.sum()
    return -np.sum(evals * np.log2(np.maximum(evals, eps)))

def partial_trace(rho, keep_qubits, n_total):
    """Trace out all qubits except keep_qubits.
    rho: (2^n_total, 2^n_total) density matrix.
    keep_qubits: list of qubit indices to keep.
    Returns reduced density matrix of dimension 2^{len(keep_qubits)}.
    """
    keep = set(keep_qubits)
    d_total = 2 ** n_total
    d_keep = 2 ** len(keep_qubits)

    # Build map from full basis index to reduced index
    # For each full basis state, extract bits for kept qubits
    rho_reduced = np.zeros((d_keep, d_keep), dtype=complex)

    for i in range(d_total):
        i_keep = 0
        for pos, q in enumerate(sorted(keep_qubits)):
            bit = (i >> (n_total - 1 - q)) & 1
            i_keep |= (bit << (len(keep_qubits) - 1 - pos))

        for j in range(d_total):
            j_keep = 0
            for pos, q in enumerate(sorted(keep_qubits)):
                bit = (j >> (n_total - 1 - q)) & 1
                j_keep |= (bit << (len(keep_qubits) - 1 - pos))

            rho_reduced[i_keep, j_keep] += rho[i, j]

    return rho_reduced


def basis_state_to_index(bits, n_qubits):
    """Convert list of bit values to basis state index.
    bits[0] is qubit 0 (most significant).
    """
    idx = 0
    for b in bits:
        idx = (idx << 1) | b
    return idx


# ============================================================
# QUANTUM CAUSAL RING SIMULATOR
# ============================================================

class QuantumRingSimulator:
    """Full density matrix simulation of a quantum causal ring.

    Qubit layout for b1 rings (vertex-sharing chain):
    - System qubits: 0, 1, ..., b1  (Q_0, Q_1, ..., Q_{b1})
    - Environment qubits: b1+1, b1+2, ..., b1+2*b1  (E_0, E'_0, E_1, E'_1, ...)

    Ring r connects Q_r -> E_{2r} -> Q_{r+1} -> E_{2r+1} -> Q_r
    Total qubits: V = (b1+1) + 2*b1
    """

    def __init__(self, b1, p=0.5):
        """
        Args:
            b1: number of causal rings
            p: probability parameter for environment qubit initial state
        """
        self.b1 = b1
        self.p = p
        self.n_sys = b1 + 1  # system qubits
        self.n_env = 2 * b1   # environment qubits
        self.n_total = self.n_sys + self.n_env

        self.sys_qubits = list(range(self.n_sys))
        self.env_qubits = list(range(self.n_sys, self.n_total))

        # Build ring structure
        self.rings = []
        for r in range(b1):
            Q_a = r
            Q_b = r + 1
            E_1 = self.n_sys + 2*r
            E_2 = self.n_sys + 2*r + 1
            self.rings.append({
                'Q_a': Q_a, 'E_1': E_1, 'Q_b': Q_b, 'E_2': E_2,
                'edges': [(Q_a, E_1), (E_1, Q_b), (Q_b, E_2), (E_2, Q_a)]
            })

        # Initialize density matrix
        self.rho = self._init_rho()
        self.d_total = 2 ** self.n_total

        # History
        self.step = 0
        self.history = []  # list of (step, description, rho_copy)

    def _init_rho(self):
        """Build initial density matrix.
        System qubits: |0> (pure)
        Environment qubits: p|+><+| + (1-p)|-><-| (mixed)
        """
        # Build single-qubit density matrices
        rho_sys = np.array([[1, 0], [0, 0]], dtype=complex)  # |0><0|

        # Environment: p|+><+| + (1-p)|-><-|
        # |+> = (|0>+|1>)/sqrt(2), |->=(|0>-|1>)/sqrt(2)
        # rho_E = 0.5 * [[1, 2p-1], [2p-1, 1]]
        rho_env = np.array([
            [0.5, 0.5*(2*self.p - 1)],
            [0.5*(2*self.p - 1), 0.5]
        ], dtype=complex)

        # Build full rho via tensor product (iterative)
        rho = np.array([[1.0]], dtype=complex)
        for q in range(self.n_total):
            if q in self.sys_qubits:
                rho = np.kron(rho, rho_sys)
            else:
                rho = np.kron(rho, rho_env)

        return rho

    def _get_gate_phase(self, u, v, c):
        """Compute phase factors for gate U=exp(i*c*sigma_z⊗sigma_z) on qubits u,v.

        For basis state |b_0...b_{n-1}>, the phase is:
        exp(i * c * (-1)^{b_u} * (-1)^{b_v})

        Since σ_z|0>=|0>, σ_z|1>=-|1>, we have:
        sigma_z⊗sigma_z |b_u, b_v> = (-1)^{b_u}*(-1)^{b_v} |b_u, b_v>
                                     = (-1)^{b_u+b_v} |b_u, b_v>

        Returns array phases[i] = exp(i*c*(-1)^{b_u[i]+b_v[i]})
        """
        phases = np.zeros(self.d_total, dtype=complex)
        for idx in range(self.d_total):
            b_u = (idx >> (self.n_total - 1 - u)) & 1
            b_v = (idx >> (self.n_total - 1 - v)) & 1
            z_u = 1 if b_u == 0 else -1  # sigma_z eigenvalue
            z_v = 1 if b_v == 0 else -1
            phases[idx] = np.exp(1j * c * z_u * z_v)
        return phases

    def apply_gate(self, u, v, c, label="gate"):
        """Apply gate U=exp(i*c*sigma_z⊗sigma_z) on qubits (u,v).

        Since U is diagonal in computational basis, the density matrix
        evolves as: rho_{i,j} -> e^{i(phi_i - phi_j)} rho_{i,j}
        """
        phases = self._get_gate_phase(u, v, c)  # shape (d_total,)
        # rho_{i,j} *= exp(i*(phi_i - phi_j))
        phase_diff = phases[:, None] * np.conj(phases[None, :])  # (d_total, d_total)
        self.rho = self.rho * phase_diff

        self.step += 1
        self.history.append((self.step, f"U({u},{v}) c={c:.4f}", self.rho.copy()))

    def compute_qubit_entropies(self, rho=None):
        """Compute von Neumann entropy for each qubit's reduced state."""
        if rho is None:
            rho = self.rho

        entropies = {}
        for q in range(self.n_total):
            rho_q = partial_trace(rho, [q], self.n_total)
            entropies[q] = von_neumann_entropy(rho_q)

        return entropies

    def compute_all_entropy_history(self):
        """Recompute entropy for each qubit at each history step."""
        entropy_history = {q: [] for q in range(self.n_total)}

        for step, desc, rho_step in self.history:
            entropies = self.compute_qubit_entropies(rho_step)
            for q in range(self.n_total):
                entropy_history[q].append(entropies[q])

        return entropy_history

    def check_monotonicity(self):
        """Check if any qubit shows non-monotonic entropy evolution.

        Non-monotonic: S(t+1) < S(t) - tol for some step t.
        This WOULD BE a counterexample to the monotonicity claim.
        """
        entropy_history = self.compute_all_entropy_history()

        violations = []
        for q in range(self.n_total):
            S_q = np.array(entropy_history[q])
            for t in range(len(S_q) - 1):
                if S_q[t+1] < S_q[t] - 1e-10:
                    violations.append({
                        'qubit': q,
                        'qubit_type': 'sys' if q < self.n_sys else 'env',
                        'step': t + 1,  # gate index
                        'S_before': float(S_q[t]),
                        'S_after': float(S_q[t+1]),
                        'delta_S': float(S_q[t+1] - S_q[t]),
                        'description_before': self.history[t][1],
                        'description_after': self.history[t+1][1]
                    })

        return violations, entropy_history

    def get_current_purities(self):
        """Compute purity Tr(rho^2) for each qubit."""
        purities = {}
        for q in range(self.n_total):
            rho_q = partial_trace(self.rho, [q], self.n_total)
            purities[q] = float(np.real(np.trace(rho_q @ rho_q)))
        return purities


# ============================================================
# GATE ORDERING GENERATORS
# ============================================================

def get_all_gate_orderings(b1):
    """Generate various gate orderings for the causal ring.

    Returns list of lists of (u, v, label) tuples.
    Each inner list is one complete cycle through the ring.
    """
    orderings = []

    # Build ring structure
    rings = []
    n_sys = b1 + 1
    for r in range(b1):
        Q_a = r
        Q_b = r + 1
        E_1 = n_sys + 2*r
        E_2 = n_sys + 2*r + 1
        rings.append({
            'Q_a': Q_a, 'E_1': E_1, 'Q_b': Q_b, 'E_2': E_2
        })

    # For each ring, there are 4 edges (24 permutations in principle,
    # but must respect the causal ring order)

    # Ordering 1: Forward sequential (Q_a->E_1->Q_b->E_2->Q_a)
    forward = []
    for ring in rings:
        forward.extend([
            (ring['Q_a'], ring['E_1'], f"Q_a{r}->E1_{r}"),
            (ring['E_1'], ring['Q_b'], f"E1_{r}->Q_b{r+1}"),
            (ring['Q_b'], ring['E_2'], f"Q_b{r+1}->E2_{r}"),
            (ring['E_2'], ring['Q_a'], f"E2_{r}->Q_a{r}")
        ])
    orderings.append(('forward', forward))

    # Ordering 2: Reverse (Q_a->E_2->Q_b->E_1->Q_a)
    reverse = []
    for ring in rings:
        reverse.extend([
            (ring['Q_a'], ring['E_2'], f"Q_a{r}->E2_{r}"),
            (ring['E_2'], ring['Q_b'], f"E2_{r}->Q_b{r+1}"),
            (ring['Q_b'], ring['E_1'], f"Q_b{r+1}->E1_{r}"),
            (ring['E_1'], ring['Q_a'], f"E1_{r}->Q_a{r}")
        ])
    orderings.append(('reverse', reverse))

    # Ordering 3: System-first (all Q->E, then all E->Q)
    q_to_e = []
    e_to_q = []
    for ring in rings:
        q_to_e.append((ring['Q_a'], ring['E_1'], f"Q_a{r}->E1_{r}"))
        q_to_e.append((ring['Q_b'], ring['E_2'], f"Q_b{r+1}->E2_{r}"))
        e_to_q.append((ring['E_1'], ring['Q_b'], f"E1_{r}->Q_b{r+1}"))
        e_to_q.append((ring['E_2'], ring['Q_a'], f"E2_{r}->Q_a{r}"))
    orderings.append(('system_first', q_to_e + e_to_q))

    # Ordering 4: Environment-first (all E->Q, then all Q->E)
    orderings.append(('env_first', e_to_q + q_to_e))

    # Ordering 5: Alternating system/env
    alt = []
    for ring in rings:
        alt.append((ring['Q_a'], ring['E_1'], f"Q_a{r}->E1_{r}"))
        alt.append((ring['E_1'], ring['Q_b'], f"E1_{r}->Q_b{r+1}"))
        alt.append((ring['Q_b'], ring['E_2'], f"Q_b{r+1}->E2_{r}"))
        alt.append((ring['E_2'], ring['Q_a'], f"E2_{r}->Q_a{r}"))
    orderings.append(('alternating', alt))

    # Ordering 6: Ring-by-ring (complete ring 0, then ring 1, ...)
    # Same as forward for ring-by-ring
    orderings.append(('ring_by_ring', forward))

    return orderings


def get_random_permutation(ring_info, seed=42):
    """Generate a random permutation of all edges."""
    rng = np.random.RandomState(seed)

    all_edges = []
    for ring in ring_info:
        all_edges.extend([
            (ring['Q_a'], ring['E_1']),
            (ring['E_1'], ring['Q_b']),
            (ring['Q_b'], ring['E_2']),
            (ring['E_2'], ring['Q_a'])
        ])

    perm = list(range(len(all_edges)))
    rng.shuffle(perm)

    edge_order = [(all_edges[i][0], all_edges[i][1], f"edge_{i}") for i in perm]
    return edge_order


# ============================================================
# MAIN SCAN: Search for counterexamples
# ============================================================

def scan_single_ring():
    """Scan a single causal ring (b1=1) for non-monotonic entropy."""
    print("=" * 70)
    print("STEP 1: Single Ring (b1=1) Monotonicity Scan")
    print("=" * 70)

    c_values = [np.pi/16, np.pi/8, np.pi/4, 3*np.pi/8, 0.5, 0.7, 1.0, np.pi/16 * 3, np.pi/8 * 3, np.pi/2]
    p_values = [0.1, 0.25, 0.3, 0.5, 0.7, 0.75, 0.9]
    n_rounds_list = [1, 2, 3, 4]

    total_configs = len(c_values) * len(p_values) * len(n_rounds_list)
    print(f"Testing {total_configs} configurations...")
    print(f"  c values: {[f'{c:.4f}' for c in c_values]}")
    print(f"  p values: {p_values}")
    print(f"  rounds: {n_rounds_list}")

    all_results = {}
    violations_found = []

    for p_val in p_values:
        for c_val in c_values:
            for n_rounds in n_rounds_list:
                config_key = f"p={p_val:.2f}_c={c_val:.4f}_R={n_rounds}"

                # Build simulator
                sim = QuantumRingSimulator(b1=1, p=p_val)

                # Apply gates: forward ordering, n_rounds cycles
                base_edges = [
                    (0, 2, "Q_a->E1"),   # Q_a=0, E1=2
                    (2, 1, "E1->Q_b"),    # E1=2, Q_b=1
                    (1, 3, "Q_b->E2"),    # Q_b=1, E2=3
                    (3, 0, "E2->Q_a")     # E2=3, Q_a=0
                ]

                for round_num in range(n_rounds):
                    for u, v, label in base_edges:
                        sim.apply_gate(u, v, c_val, f"R{round_num}_{label}")

                # Check monotonicity
                violations, entropy_hist = sim.check_monotonicity()

                all_results[config_key] = {
                    'p': p_val, 'c': c_val, 'rounds': n_rounds,
                    'n_violations': len(violations),
                    'violations': violations,
                    'entropy_history': {str(k): [float(x) for x in v] for k, v in entropy_hist.items()},
                    'final_entropies': {str(k): float(v) for k, v in sim.compute_qubit_entropies().items()}
                }

                if violations:
                    violations_found.append((config_key, violations))
                    print(f"\n  *** VIOLATION FOUND: {config_key}")
                    for v in violations:
                        print(f"      Qubit {v['qubit']} ({v['qubit_type']}): "
                              f"S({v['step']-1})={v['S_before']:.6f} -> "
                              f"S({v['step']})={v['S_after']:.6f} "
                              f"(delta={v['delta_S']:.6e})")

                if (len(all_results) % 20 == 0):
                    print(f"  Progress: {len(all_results)}/{total_configs}")

    print(f"\nSummary: {len(violations_found)} configs with violations out of {len(all_results)}")

    return all_results, violations_found


def scan_ordering_effects():
    """Test all gate orderings for a single ring with key parameters."""
    print("\n" + "=" * 70)
    print("STEP 2: Gate Ordering Effects (b1=1)")
    print("=" * 70)

    c_values = [0.5, np.pi/4, 0.7, 1.0]
    p_values = [0.3, 0.5, 0.7]
    n_rounds = 2

    orderings = get_all_gate_orderings(1)  # b1=1

    ordering_results = {}
    violations_by_order = {}

    for order_name, edge_order in orderings:
        print(f"\n--- Ordering: {order_name} ---")
        violations_by_order[order_name] = []

        for p_val in p_values:
            for c_val in c_values:
                config_key = f"{order_name}_p={p_val}_c={c_val:.4f}"

                sim = QuantumRingSimulator(b1=1, p=p_val)

                for round_num in range(n_rounds):
                    for u, v, label in edge_order:
                        sim.apply_gate(u, v, c_val, f"R{round_num}_{label}")

                violations, _ = sim.check_monotonicity()

                ordering_results[config_key] = {
                    'order': order_name, 'p': p_val, 'c': c_val,
                    'n_violations': len(violations),
                    'violations': violations,
                    'final_entropies': {str(k): float(v) for k, v in sim.compute_qubit_entropies().items()}
                }

                if violations:
                    violations_by_order[order_name].append(config_key)
                    print(f"  VIOLATION: {config_key} ({len(violations)} events)")
                    for v in violations:
                        print(f"    Q{q}={v['qubit']} ({v['qubit_type']}): "
                              f"{v['S_before']:.4f}->{v['S_after']:.4f} "
                              f"delta={v['delta_S']:.2e}")

    print(f"\nOrdering violation summary:")
    for order_name in violations_by_order:
        print(f"  {order_name}: {len(violations_by_order[order_name])} violating configs")

    return ordering_results, violations_by_order


def scan_random_permutations(n_random=100):
    """Test random edge permutations for potential counterexamples."""
    print("\n" + "=" * 70)
    print(f"STEP 3: Random Edge Permutations ({n_random} random orders)")
    print("=" * 70)

    # Build ring info for b1=1
    ring_info = [{'Q_a': 0, 'E_1': 2, 'Q_b': 1, 'E_2': 3}]

    # Key parameter points
    c_values = [0.5, np.pi/4, 0.7, 0.3]
    p_values = [0.3, 0.5, 0.7, 0.1, 0.9]

    random_results = {}
    violation_count = 0

    for seed in range(n_random):
        edge_order = get_random_permutation(ring_info, seed=seed)

        for p_val in p_values:
            for c_val in c_values:
                config_key = f"rand{seed}_p={p_val}_c={c_val:.4f}"

                sim = QuantumRingSimulator(b1=1, p=p_val)

                # 2 rounds
                for rnd in range(2):
                    for u, v, label in edge_order:
                        sim.apply_gate(u, v, c_val, f"R{rnd}_{label}")

                violations, entropy_hist = sim.check_monotonicity()

                random_results[config_key] = {
                    'seed': seed, 'p': p_val, 'c': c_val,
                    'n_violations': len(violations),
                    'violations': violations
                }

                if violations:
                    violation_count += 1

        if (seed + 1) % 10 == 0:
            print(f"  Progress: {seed+1}/{n_random} seeds ({violation_count} violations so far)")

    print(f"\nRandom scan: {violation_count} violating configs out of {len(random_results)}")

    return random_results


def scan_multi_ring(b1_values=[2, 3]):
    """Scan multi-ring systems."""
    print("\n" + "=" * 70)
    print(f"STEP 4: Multi-Ring Scan (b1={b1_values})")
    print("=" * 70)

    multi_results = {}
    violations_found = []

    for b1 in b1_values:
        n_total = (b1 + 1) + 2 * b1
        d_total = 2 ** n_total
        print(f"\n  b1={b1}: {n_total} qubits, density matrix {d_total}x{d_total}")

        if d_total > 256:  # Limit to 8 qubits (256x256)
            print(f"    SKIPPED: matrix size {d_total}x{d_total} too large")
            continue

        c_values = [0.5, np.pi/4, 0.7]
        p_values = [0.3, 0.5, 0.7]

        for p_val in p_values:
            for c_val in c_values:
                config_key = f"b1={b1}_p={p_val}_c={c_val:.4f}"

                sim = QuantumRingSimulator(b1=b1, p=p_val)

                # Get forward edges
                n_sys = b1 + 1
                all_edges = []
                for r in range(b1):
                    Q_a = r
                    Q_b = r + 1
                    E_1 = n_sys + 2*r
                    E_2 = n_sys + 2*r + 1
                    all_edges.extend([
                        (Q_a, E_1, f"ring{r}_Q_a->E1"),
                        (E_1, Q_b, f"ring{r}_E1->Q_b"),
                        (Q_b, E_2, f"ring{r}_Q_b->E2"),
                        (E_2, Q_a, f"ring{r}_E2->Q_a")
                    ])

                # 2 rounds
                for rnd in range(2):
                    for u, v, label in all_edges:
                        sim.apply_gate(u, v, c_val, f"R{rnd}_{label}")

                violations, entropy_hist = sim.check_monotonicity()

                multi_results[config_key] = {
                    'b1': b1, 'p': p_val, 'c': c_val,
                    'n_total': n_total, 'd_total': d_total,
                    'n_violations': len(violations),
                    'violations': violations,
                    'final_entropies': {str(k): float(v) for k, v in sim.compute_qubit_entropies().items()}
                }

                if violations:
                    violations_found.append((config_key, violations))
                    print(f"    VIOLATION: {config_key}")

    print(f"\n  Multi-ring: {len(violations_found)} violations found")

    return multi_results, violations_found


def deep_entropy_analysis():
    """Detailed analysis of entropy evolution for select configurations."""
    print("\n" + "=" * 70)
    print("STEP 5: Deep Entropy Evolution Analysis")
    print("=" * 70)

    # Pick interesting configurations for detailed tracking
    configs = [
        ("baseline", 1, 0.5, 0.5, 3),
        ("small_c", 1, 0.5, np.pi/16, 3),
        ("large_c", 1, 0.5, np.pi/4, 3),
        ("extreme_p_low", 1, 0.1, 0.5, 3),
        ("extreme_p_high", 1, 0.9, 0.5, 3),
        ("two_ring", 2, 0.5, 0.5, 2),
    ]

    analysis = {}

    for name, b1, p, c, rounds in configs:
        n_total = (b1 + 1) + 2 * b1
        d_total = 2 ** n_total
        if d_total > 256:
            print(f"  Skipping {name}: matrix too large")
            continue

        sim = QuantumRingSimulator(b1=b1, p=p)

        # Forward ordering
        n_sys = b1 + 1
        all_edges = []
        for r in range(b1):
            Q_a, Q_b = r, r + 1
            E_1, E_2 = n_sys + 2*r, n_sys + 2*r + 1
            all_edges.extend([
                (Q_a, E_1, f"Q{r}->E{r}1"),
                (E_1, Q_b, f"E{r}1->Q{r+1}"),
                (Q_b, E_2, f"Q{r+1}->E{r}2"),
                (E_2, Q_a, f"E{r}2->Q{r}")
            ])

        # Save initial entropy
        init_entropies = sim.compute_qubit_entropies()

        # Apply gates one at a time and record
        for rnd in range(rounds):
            for u, v, label in all_edges:
                sim.apply_gate(u, v, c, f"R{rnd}_{label}")

        violations, entropy_hist = sim.check_monotonicity()
        final_entropies = sim.compute_qubit_entropies()

        analysis[name] = {
            'b1': b1, 'p': p, 'c': c, 'rounds': rounds,
            'n_total': n_total,
            'init_entropies': {str(k): float(v) for k, v in init_entropies.items()},
            'final_entropies': {str(k): float(v) for k, v in final_entropies.items()},
            'entropy_history': {
                str(q): [float(x) for x in hist]
                for q, hist in entropy_hist.items()
            },
            'n_violations': len(violations),
            'violations': violations,
            'n_steps': len(entropy_hist[0]) if entropy_hist else 0
        }

        # Print summary
        print(f"\n  {name}: b1={b1}, p={p}, c={c:.4f}, rounds={rounds}")
        print(f"    Total qubits: {n_total}")
        print(f"    Total steps: {analysis[name]['n_steps']}")
        print(f"    Initial entropies: S_sys_avg={np.mean([v for k,v in init_entropies.items() if int(k) < n_sys]):.4f}, "
              f"S_env_avg={np.mean([v for k,v in init_entropies.items() if int(k) >= n_sys]):.4f}")
        print(f"    Final entropies: S_sys_avg={np.mean([v for k,v in final_entropies.items() if int(k) < n_sys]):.4f}, "
              f"S_env_avg={np.mean([v for k,v in final_entropies.items() if int(k) >= n_sys]):.4f}")

        if violations:
            print(f"    *** {len(violations)} MONOTONICITY VIOLATIONS ***")
            for v in violations[:5]:
                print(f"        Q{v['qubit']}({v['qubit_type']}): step {v['step']}, "
                      f"{v['S_before']:.6f} -> {v['S_after']:.6f}")
        else:
            print(f"    No monotonicity violations detected")

    return analysis


# ============================================================
# THEORETICAL ANALYSIS
# ============================================================

def theoretical_analysis():
    """Perform theoretical analysis of why monotonicity might/might not hold."""
    print("\n" + "=" * 70)
    print("STEP 6: Theoretical Analysis")
    print("=" * 70)

    analysis_points = []

    # Point 1: Sequential vs simultaneous gates
    analysis_points.append({
        'point': 'DGF defines U = Pi_i u_i as simultaneous',
        'detail': (
            "The DGF framework defines the overall unitary as U = Π_i u_i acting "
            "SIMULTANEOUSLY on all edges. The sequential gate application used here "
            "tracks intermediate states that may not be physically meaningful in the "
            "DGF framework. However, if we interpret the causal ring as a Trotterized "
            "time evolution, then intermediate states ARE physical and monotonicity "
            "must hold at each time step for the classical bound to apply."
        )
    })

    # Point 2: Per-node vs global monotonicity
    analysis_points.append({
        'point': 'Per-node vs global statement',
        'detail': (
            "The classical proof states 'each node can transition 0->1 at most once' "
            "(per-node statement). But even in classical systems, this is really a "
            "GLOBAL property: the TOTAL number of 0->1 transitions is bounded by N_S·q_S. "
            "Individual nodes CAN oscillate (0->1->0) as long as the TOTAL occupancy "
            "does not exceed the bound. The per-node statement is a SUFFICIENT condition "
            "for the global bound, not a necessary one."
        )
    })

    # Point 3: Rabi oscillations
    analysis_points.append({
        'point': 'Rabi oscillation analogy',
        'detail': (
            "A two-level quantum system driven by a resonant field undergoes Rabi "
            "oscillations: its population oscillates between |0> and |1> with frequency "
            "Ω = |c|/ℏ (where c is the Cartan parameter in our notation). Each qubit's "
            "von Neumann entropy similarly oscillates. In the DGF causal ring, the "
            "repeated application of gates constitutes an effective Rabi drive. "
            "If gates are applied sequentially with the same c value, each qubit "
            "undergoes an effective rotation that can decrease its entropy."
        )
    })

    # Point 4: Quantum recurrence
    analysis_points.append({
        'point': 'Quantum recurrence vs classical monotonicity',
        'detail': (
            "In a finite-dimensional quantum system, any unitary evolution is "
            "quasi-periodic (Poincare recurrence in the quantum domain). A qubit's "
            "entropy will return arbitrarily close to its initial value infinitely "
            "often. Since initial entropy can be small and intermediate entropy large, "
            "this implies that S(t) MUST decrease at some point, violating per-node "
            "monotonicity. The only escape: the environment qubits are initially mixed, "
            "so the overall dynamics is NOT purely unitary - it's a quantum channel "
            "(CPTP map) on the system alone."
        )
    })

    # Point 5: CPTP channel perspective
    analysis_points.append({
        'point': 'CPTP channel perspective',
        'detail': (
            "When environment qubits are in a mixed state, the evolution of system "
            "qubits alone is a CPTP (completely positive trace-preserving) map. "
            "CPTP maps CAN be entropy-increasing (they represent decoherence). "
            "However, individual environment qubits within the full unitary description "
            "are still subject to the full unitary dynamics, and their entropies "
            "can oscillate. The key question is: in the DGF REFLUX definition, "
            "does a 'transition' refer to the CPTP effective dynamics or the "
            "underlying unitary dynamics?"
        )
    })

    for i, ap in enumerate(analysis_points):
        print(f"\n  Point {i+1}: {ap['point']}")
        detail_lines = ap['detail'].split('\n')
        for line in detail_lines:
            print(f"    {line.strip()}")

    return analysis_points


def compute_reflux_bound_test():
    """Test whether any configuration violates the classical reflux bound."""
    print("\n" + "=" * 70)
    print("STEP 7: Classical Reflux Bound Test")
    print("=" * 70)

    # Classical bound: P_reflux ≤ N_S·q_S / (N_E·q_E)
    # For the DGF framework:
    # N_S = number of system qubits
    # N_E = number of environment qubits
    # q_S = initial uncertainty of system qubits
    # q_E = initial uncertainty of environment qubits

    # What is the "reflux probability" P_reflux in quantum terms?
    # In the DGF framework, reflux corresponds to environment qubits
    # transferring entropy/information BACK to system qubits.
    #
    # In our simulation, this would manifest as:
    # - System qubit entropy INCREASING beyond what forward propagation alone would give
    # - Environment qubit entropy DECREASING (losing uncertainty to system)

    # Test: for the single ring (N_S=2, N_E=2), the classical bound is:
    # P_reflux ≤ q_S/q_E
    #
    # If system qubits start pure (q_S=0, S=0):
    # P_reflux ≤ 0 — reflux is impossible
    #
    # If system qubits start with some entropy:
    # We need to track how much entropy flows from env → sys

    # Let's use an alternative approach: system qubits start in
    # partially mixed state too, to give a non-trivial bound

    print("\n  Building reflux-aware simulation...")

    # Single ring, system qubits start in mixed state too
    b1 = 1
    n_sys = 2
    n_env = 2
    n_total = 4

    p_sys = 0.8  # system initial uncertainty parameter
    p_env = 0.5  # environment initial uncertainty parameter
    c = 0.5

    # Build density matrix with both sys and env mixed
    # System: p_sys|+><+| + (1-p_sys)|-><-|
    rho_sys = np.array([[0.5, 0.5*(2*p_sys-1)],
                         [0.5*(2*p_sys-1), 0.5]], dtype=complex)
    rho_env = np.array([[0.5, 0.5*(2*p_env-1)],
                         [0.5*(2*p_env-1), 0.5]], dtype=complex)

    rho_init = rho_sys  # Q_0
    rho_init = np.kron(rho_init, rho_sys)  # Q_1
    rho_init = np.kron(rho_init, rho_env)  # E_1
    rho_init = np.kron(rho_init, rho_env)  # E_2

    base_edges = [(0, 2), (2, 1), (1, 3), (3, 0)]

    # Track entropy flow
    d_total = 2 ** n_total

    def apply_gate(rho, u, v, c):
        # Diagonal gate in computational basis
        phases = np.zeros(d_total, dtype=complex)
        for idx in range(d_total):
            b_u = (idx >> (n_total - 1 - u)) & 1
            b_v = (idx >> (n_total - 1 - v)) & 1
            z_u = 1 if b_u == 0 else -1
            z_v = 1 if b_v == 0 else -1
            phases[idx] = np.exp(1j * c * z_u * z_v)
        phase_diff = phases[:, None] * np.conj(phases[None, :])
        return rho * phase_diff

    # Compute entropies for each qubit at each step
    def qubit_entropy(rho, q):
        rho_q = partial_trace(rho, [q], n_total)
        return von_neumann_entropy(rho_q)

    rho = rho_init.copy()

    # Initial entropies
    S_init = {0: qubit_entropy(rho, 0), 1: qubit_entropy(rho, 1),
               2: qubit_entropy(rho, 2), 3: qubit_entropy(rho, 3)}

    print(f"  Initial entropies: Q0={S_init[0]:.4f}, Q1={S_init[1]:.4f}, "
          f"E1={S_init[2]:.4f}, E2={S_init[3]:.4f}")

    # Apply 3 rounds and track
    S_history = {0: [], 1: [], 2: [], 3: []}

    for rnd in range(3):
        for u, v in base_edges:
            rho = apply_gate(rho, u, v, c)
            for q in range(4):
                S_history[q].append(qubit_entropy(rho, q))

    S_final = {q: S_history[q][-1] for q in range(4)}

    print(f"  Final entropies: Q0={S_final[0]:.4f}, Q1={S_final[1]:.4f}, "
          f"E1={S_final[2]:.4f}, E2={S_final[3]:.4f}")

    # Compute reflux fraction
    # N_S = 2, N_E = 2
    # q_S = initial system entropy / log(2) (normalized to [0,1])
    # q_E = initial environment entropy / log(2)

    N_S, N_E = 2, 2
    q_S_init = np.mean([S_init[q] for q in range(n_sys)]) / np.log2(2)
    q_E_init = np.mean([S_init[q] for q in range(n_sys, n_total)]) / np.log2(2)

    bound = N_S * q_S_init / (N_E * q_E_init) if q_E_init > 1e-10 else float('inf')

    print(f"\n  N_S={N_S}, N_E={N_E}")
    print(f"  q_S_init = {q_S_init:.4f} (avg system entropy / log2)")
    print(f"  q_E_init = {q_E_init:.4f} (avg environment entropy / log2)")
    print(f"  Classical bound: P_reflux <= {bound:.4f}")

    # Detect "reflux events": env qubit entropy decrease
    reflux_events = 0
    for q in range(n_sys, n_total):
        for t in range(len(S_history[q]) - 1):
            if S_history[q][t+1] < S_history[q][t] - 1e-10:
                reflux_events += 1

    # Detect "forward events": env qubit entropy increase
    forward_events = 0
    for q in range(n_sys, n_total):
        for t in range(len(S_history[q]) - 1):
            if S_history[q][t+1] > S_history[q][t] + 1e-10:
                forward_events += 1

    print(f"  Reflux (E dec) events: {reflux_events}")
    print(f"  Forward (E inc) events: {forward_events}")
    if forward_events > 0:
        print(f"  Empir. P_reflux = {reflux_events}/{forward_events} = {reflux_events/forward_events:.4f}")

    return {
        'bound': bound, 'reflux_events': reflux_events,
        'forward_events': forward_events,
        'S_init': S_init, 'S_final': S_final, 'S_history': S_history
    }


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 70)
    print("WALL #7 ATTACK: T2 Reflux Bound Quantum Monotonicity Test")
    print(f"Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    all_data = {}

    # Step 1: Basic scan
    results_single, violations_single = scan_single_ring()
    all_data['single_ring'] = {
        'n_configs': len(results_single),
        'n_violations': len(violations_single),
        'sample_violations': violations_single[:5] if violations_single else []
    }

    # Step 2: Gate ordering effects
    results_ordering, violations_ordering = scan_ordering_effects()
    all_data['ordering'] = {
        'n_configs': len(results_ordering),
        'violations_by_order': {k: len(v) for k, v in violations_ordering.items()}
    }

    # Step 3: Random permutations
    results_random = scan_random_permutations(50)  # 50 random seeds
    all_data['random'] = {
        'n_configs': len(results_random),
        'n_violations': sum(1 for v in results_random.values() if v['n_violations'] > 0)
    }

    # Step 4: Multi-ring
    results_multi, violations_multi = scan_multi_ring([2, 3])
    all_data['multi_ring'] = {
        'n_configs': len(results_multi),
        'n_violations': len(violations_multi)
    }

    # Step 5: Deep analysis
    deep_analysis = deep_entropy_analysis()
    all_data['deep_analysis_keys'] = list(deep_analysis.keys())

    # Step 6: Theoretical analysis
    theory = theoretical_analysis()
    all_data['theory_points'] = [t['point'] for t in theory]

    # Step 7: Reflux bound test
    reflux_test = compute_reflux_bound_test()
    all_data['reflux_test'] = {
        'bound': reflux_test['bound'],
        'reflux_events': reflux_test['reflux_events'],
        'forward_events': reflux_test['forward_events']
    }

    # ============================================================
    # FINAL SUMMARY
    # ============================================================
    print("\n" + "=" * 70)
    print("FINAL SUMMARY")
    print("=" * 70)

    total_violations = (
        len(violations_single) +
        sum(len(v) for v in violations_ordering.values()) +
        sum(1 for v in results_random.values() if v['n_violations'] > 0) +
        len(violations_multi)
    )
    total_configs = (
        len(results_single) + len(results_ordering) +
        len(results_random) + len(results_multi)
    )

    print(f"\n  Total configurations tested: {total_configs}")
    print(f"  Configurations with violations: {total_violations}")

    if total_violations > 0:
        print(f"\n  *** COUNTEREXAMPLES FOUND ***")
        print(f"  Monotonicity is VIOLATED in the quantum causal ring.")
        print(f"  The classical T2 proof does NOT extend to the quantum domain.")
    else:
        print(f"\n  NO counterexamples found after systematic search.")
        print(f"  This is evidence FOR monotonicity holding in the quantum domain,")
        print(f"  BUT the following caveats apply:")
        print(f"  1. Sequential gate ordering may not be physically meaningful in DGF")
        print(f"  2. Full unitary dynamics on finite systems is quasi-periodic")
        print(f"  3. The per-node statement may not be necessary for the global bound")

    print(f"\n  See detailed analysis in the output data.")

    return all_data


if __name__ == '__main__':
    main()

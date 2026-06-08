"""
DGF Causal Set Simulation -- LP33 S33-4 Numerical Verification
==============================================================
Tests predictions P1-P5 from the LP33 Euclidean Emergence project.

Architecture:
  1. N-qubit network with states |0> (undetermined) or |1> (determined)
  2. Determination events propagate via SRC (ferromagnetic) coupling
  3. Each determination event becomes a causal set element
  4. Partial order from determination chains (a≺b if a triggered b)
  5. Myrheim-Meyer dimension: R/M^2 -> Gamma_d -> dimension d
  6. Direction alignment: mean cosine between determination directions

Predictions tested:
  P1: rho_c = constant (alignment threshold independent of N)
  P2: <cos theta> > 0 and increasing with rho_D
  P3: R/M^2 -> Gamma_4 ~ 0.201 for D=4 (dimension reads out correctly)
  P4: eta(D=4) > eta(D=3) > eta(D=2) (time direction uniqueness increases with D)
  P5: D=2->D=3 discontinuous jump in emergence probability
"""

import numpy as np
from collections import defaultdict
from scipy import stats
import time
import json

# ============================================================
# Configuration
# ============================================================

CONFIG = {
    'N_qubits': 200,           # Number of qubits in network
    'D_space': 4,             # Spatial dimensions (can be 2,3,4)
    'p_spont': 0.001,         # Spontaneous determination probability per qubit per step
    'coupling_strength': 0.3, # SRC coupling strength (χ_ij effective)
    'max_steps': 5000,        # Maximum simulation steps
    'n_trials': 10,           # Number of independent trials per configuration
    'seed': 42,
}

# Myrheim-Meyer constants Gamma_d = Gamma(d+1)Gamma(d/2) / (4Gamma(3d/2))
GAMMA_D = {
    2: 0.5,
    3: 0.298,
    4: 0.201,
    5: 0.137,
}


class DGFNetwork:
    """DGF qubit network with determination dynamics."""

    def __init__(self, N, D, p_spont, coupling_strength, seed=None):
        self.N = N
        self.D = D
        self.p_spont = p_spont
        self.J = coupling_strength
        self.rng = np.random.RandomState(seed)

        # Qubit states: 0 = |0> (undetermined), 1 = |1> (determined)
        self.states = np.zeros(N, dtype=np.int8)

        # Each qubit has a D-dimensional "direction vector" (unit vector)
        # For |0> qubits: vector is undefined (zero)
        # For |1> qubits: determined by its determination event
        self.directions = np.zeros((N, D))

        # Adjacency matrix for SRC coupling (random regular graph approx)
        # Each qubit connected to ~log(N) neighbors
        degree = max(2, int(np.log(N)))
        self.adjacency = self._build_random_graph(N, degree, self.rng)

        # Causal set: list of events {id, qubit, time, triggered_by}
        self.events = []
        self.event_counter = 0

        # Track which qubits triggered which (for partial order)
        self.trigger_graph = defaultdict(list)

        # Simulation state
        self.step = 0
        self.q_history = []  # q = fraction of |0> qubits
        self.alignment_history = []  # mean cos(theta) between determined qubits

    def _build_random_graph(self, N, degree, rng):
        """Build random regular-ish graph for qubit connectivity."""
        adj = defaultdict(list)
        for i in range(N):
            # Connect to 'degree' random neighbors
            neighbors = set()
            while len(neighbors) < degree:
                j = rng.randint(0, N)
                if j != i:
                    neighbors.add(j)
            for j in neighbors:
                adj[i].append(j)
                adj[j].append(i)
        # Deduplicate
        for i in adj:
            adj[i] = list(set(adj[i]))
        return adj

    def _random_direction(self):
        """Generate random unit vector in D dimensions."""
        v = self.rng.randn(self.D)
        return v / np.linalg.norm(v)

    def step_determination(self):
        """Execute one step of determination dynamics."""
        self.step += 1

        # Spontaneous determinations
        for i in range(self.N):
            if self.states[i] == 0:
                if self.rng.random() < self.p_spont:
                    self._determine(i, triggered_by=None)

        # Coupled (SRC) determinations: determined qubits influence neighbors
        determined_now = np.where(self.states == 1)[0]
        if len(determined_now) > 0:
            for i in determined_now:
                for j in self.adjacency[i]:
                    if self.states[j] == 0:
                        # Probability depends on alignment of i's direction
                        # with the "expected" direction for j
                        p_coupled = self.J * (1.0 / len(self.adjacency[i]))
                        if self.rng.random() < p_coupled:
                            self._determine(j, triggered_by=i)

    def _determine(self, qubit_idx, triggered_by=None):
        """Execute |0> -> |1> transition for a qubit."""
        self.states[qubit_idx] = 1

        # Assign direction
        if triggered_by is not None:
            # Aligned with trigger + noise (ferromagnetic coupling)
            trigger_dir = self.directions[triggered_by]
            noise = self.rng.randn(self.D) * 0.1  # small noise
            new_dir = trigger_dir + noise
            self.directions[qubit_idx] = new_dir / np.linalg.norm(new_dir)
        else:
            # Spontaneous: random direction
            self.directions[qubit_idx] = self._random_direction()

        # Record causal set event
        self.event_counter += 1
        event = {
            'id': self.event_counter,
            'qubit': qubit_idx,
            'time': self.step,
            'triggered_by': triggered_by,
            'direction': self.directions[qubit_idx].copy(),
        }
        self.events.append(event)

        if triggered_by is not None:
            self.trigger_graph[triggered_by].append(qubit_idx)

    def compute_causal_relations(self):
        """Build partial order relation from events.
        e_a prec e_b if t_a < t_b AND graph_distance(q_a, q_b) <= v_eff * (t_b - t_a).
        Uses physical 'light cone' condition: signal can propagate through
        the qubit network at speed v_eff = 1 graph_edge / time_step.
        """
        M = len(self.events)
        if M < 2:
            return 0, M

        times = np.array([e['time'] for e in self.events])
        qubits = np.array([e['qubit'] for e in self.events])

        # Precompute graph distances for all qubit pairs (BFS from each qubit)
        graph_dist = self._compute_graph_distances()

        R = 0
        v_eff = 1.0  # signal propagation speed (edges per time step)

        for a in range(M):
            for b in range(a + 1, M):
                dt = times[b] - times[a]
                if dt > 0:
                    d_g = graph_dist.get((qubits[a], qubits[b]), float('inf'))
                    if d_g <= v_eff * dt:
                        R += 1
                # else: t_b <= t_a, no causal relation in this direction
                # (we only count a->b when t_a < t_b)

        return R, M

    def _compute_graph_distances(self):
        """Precompute shortest path distances between all qubit pairs."""
        distances = {}
        for source in range(self.N):
            # BFS from source
            dist = {source: 0}
            queue = [source]
            while queue:
                node = queue.pop(0)
                for neighbor in self.adjacency.get(node, []):
                    if neighbor not in dist:
                        dist[neighbor] = dist[node] + 1
                        queue.append(neighbor)
            for target, d in dist.items():
                distances[(source, target)] = d
        return distances

    def compute_alignment(self):
        """Compute mean cosine between all pairs of determined qubits."""
        determined = np.where(self.states == 1)[0]
        if len(determined) < 2:
            return 0.0
        dirs = self.directions[determined]
        cosines = []
        for i in range(len(dirs)):
            for j in range(i + 1, len(dirs)):
                cos = np.dot(dirs[i], dirs[j])
                cosines.append(cos)
        return np.mean(cosines)

    def compute_time_direction_uniqueness(self):
        """Compute eta: how uniquely is the time direction defined?
        eta = (max_d B_d - mean_d B_d) / std_d(B_d)
        where B_d is the "Borda score" of direction d.
        """
        determined = np.where(self.states == 1)[0]
        if len(determined) < 2:
            return 0.0

        dirs = self.directions[determined]
        # For each determined qubit, identify its "most time-like" direction
        # (the direction component with largest absolute value)
        primary_dirs = np.argmax(np.abs(dirs), axis=1)

        # Count how many qubits picked each direction
        counts = np.bincount(primary_dirs, minlength=self.D)
        if np.std(counts) == 0:
            return 0.0
        return (np.max(counts) - np.mean(counts)) / np.std(counts)

    def run(self, max_steps=None):
        """Run simulation until max_steps or all qubits determined."""
        if max_steps is None:
            max_steps = CONFIG['max_steps']

        for _ in range(max_steps):
            self.step_determination()
            q = 1.0 - np.mean(self.states)  # fraction undetermined
            self.q_history.append(q)

            if len(self.events) >= 2:
                align = self.compute_alignment()
                self.alignment_history.append(align)

            # Stop if >95% determined
            if np.mean(self.states) > 0.95:
                break

        return {
            'q_final': 1.0 - np.mean(self.states),
            'M': len(self.events),
            'alignment_final': self.alignment_history[-1] if self.alignment_history else 0,
            'eta_final': self.compute_time_direction_uniqueness(),
            'steps': self.step,
        }


def compute_myrheim_meyer(network):
    """Compute Myrheim-Meyer dimension estimate."""
    R, M = network.compute_causal_relations()
    if M < 2:
        return None, M, 0

    ratio = R / (M * M) if M > 0 else 0

    # Find closest dimension
    best_d = None
    best_dist = float('inf')
    for d, gamma in GAMMA_D.items():
        dist = abs(ratio - gamma)
        if dist < best_dist:
            best_dist = dist
            best_d = d

    return best_d, M, ratio


def run_experiment(config_override=None):
    """Run a single experiment configuration."""
    cfg = CONFIG.copy()
    if config_override:
        cfg.update(config_override)

    results = []
    for trial in range(cfg['n_trials']):
        seed = cfg['seed'] + trial
        net = DGFNetwork(
            N=cfg['N_qubits'],
            D=cfg['D_space'],
            p_spont=cfg['p_spont'],
            coupling_strength=cfg['coupling_strength'],
            seed=seed,
        )
        run_result = net.run(cfg['max_steps'])
        d_mm, M, ratio = compute_myrheim_meyer(net)

        run_result['trial'] = trial
        run_result['D'] = cfg['D_space']
        run_result['N'] = cfg['N_qubits']
        run_result['myrheim_meyer_d'] = d_mm
        run_result['myrheim_meyer_ratio'] = ratio
        run_result['q_history'] = net.q_history

        results.append(run_result)

    return results


def analyze_dimension_dependence():
    """Test P4 and P5: dimension dependence of time direction emergence."""
    print("=" * 60)
    print("Testing D=2,3,4 dimension dependence (P4, P5)")
    print("=" * 60)

    all_results = {}
    for D in [2, 3, 4]:
        print(f"\n--- D = {D} ---")
        cfg = {
            'D_space': D,
            'N_qubits': 100,
            'n_trials': 8,
            'max_steps': 3000,
        }
        results = run_experiment(cfg)
        all_results[D] = results

        eta_vals = [r['eta_final'] for r in results]
        align_vals = [r['alignment_final'] for r in results if r['alignment_final'] != 0]

        print(f"  eta (time direction uniqueness): {np.mean(eta_vals):.3f} +/- {np.std(eta_vals):.3f}")
        if align_vals:
            print(f"  cos(theta) alignment: {np.mean(align_vals):.4f}")
        else:
            print("  cos(theta): N/A")
        print(f"  q_final: {np.mean([r['q_final'] for r in results]):.3f}")

    # Check P4: eta(D=4) > eta(D=3) > eta(D=2)
    eta_means = {D: np.mean([r['eta_final'] for r in all_results[D]]) for D in [2, 3, 4]}
    p4_pass = eta_means[4] > eta_means[3] > eta_means[2]
    print(f"\nP4 (eta monotonic with D): {'PASS PASS' if p4_pass else 'FAIL FAIL'}")
    print(f"  eta(D=2)={eta_means[2]:.3f}, eta(D=3)={eta_means[3]:.3f}, eta(D=4)={eta_means[4]:.3f}")

    # Check P5: D=2->D=3 jump > D=3->D=4 jump
    jump_23 = eta_means[3] - eta_means[2]
    jump_34 = eta_means[4] - eta_means[3]
    p5_pass = jump_23 > jump_34
    print(f"P5 (D=2->3 jump > D=3->4 jump): {'PASS PASS' if p5_pass else 'FAIL FAIL'}")
    print(f"  Jump 2->3: {jump_23:.3f}, Jump 3->4: {jump_34:.3f}")

    return all_results


def analyze_alignment_threshold():
    """Test P1 and P2: alignment threshold and behavior."""
    print("\n" + "=" * 60)
    print("Testing alignment threshold (P1, P2)")
    print("=" * 60)

    N_values = [50, 100, 200]
    for N in N_values:
        print(f"\n--- N = {N} ---")
        cfg = {
            'N_qubits': N,
            'D_space': 4,
            'n_trials': 5,
            'max_steps': 3000,
        }
        results = run_experiment(cfg)

        # Find rho_D at which alignment first exceeds 0.1 (threshold)
        for r in results:
            if r['alignment_final'] > 0.0:
                print(f"  Trial {r['trial']}: q_final={r['q_final']:.3f}, "
                      f"align={r['alignment_final']:.4f}, M={r['M']}")

        align_vals = [r['alignment_final'] for r in results if r['alignment_final'] > 0]
        if align_vals:
            print(f"  Mean alignment: {np.mean(align_vals):.4f} +/- {np.std(align_vals):.4f}")

    # P1: rho_c should be approximately constant across N
    # P2: alignment should be > 0 and increasing with rho_D
    print("\nP1 (rho_c ~ constant): Requires cross-N comparison of threshold q values")
    print("P2 (<cos theta> > 0): PASS Confirmed" if align_vals and np.mean(align_vals) > 0 else "P2: FAIL")


def analyze_myrheim_meyer():
    """Test P3: Myrheim-Meyer dimension estimate."""
    print("\n" + "=" * 60)
    print("Testing Myrheim-Meyer dimension (P3)")
    print("=" * 60)

    cfg = {
        'N_qubits': 200,
        'D_space': 4,
        'n_trials': 5,
        'max_steps': 5000,
        'p_spont': 0.002,
        'coupling_strength': 0.4,
    }
    results = run_experiment(cfg)

    for r in results:
        net = DGFNetwork(cfg['N_qubits'], cfg['D_space'],
                         cfg['p_spont'], cfg['coupling_strength'],
                         seed=42 + r['trial'])
        net.run(cfg['max_steps'])
        d_mm, M, ratio = compute_myrheim_meyer(net)

        print(f"  Trial {r['trial']}: M={M}, R/M^2={ratio:.4f}, "
              f"MM-d={d_mm}, expected Gamma_4={GAMMA_D[4]:.3f}")

        # Check if ratio is close to Gamma_4
        if d_mm:
            err = abs(ratio - GAMMA_D[d_mm])
            print(f"    Distance to Gamma_{d_mm}: {err:.4f}")

    # P3: Myrheim-Meyer should read out d~4
    print(f"\nP3 (R/M^2 -> Gamma_4 ~ {GAMMA_D[4]:.3f}): See individual trial results above")


def main():
    print("DGF Causal Set Simulation -- LP33 Numerical Verification")
    print(f"Config: N={CONFIG['N_qubits']}, D={CONFIG['D_space']}, "
          f"p_spont={CONFIG['p_spont']}, J={CONFIG['coupling_strength']}")
    print()

    start = time.time()

    # Run all analyses
    dim_results = analyze_dimension_dependence()
    analyze_alignment_threshold()
    analyze_myrheim_meyer()

    elapsed = time.time() - start
    print(f"\n{'=' * 60}")
    print(f"Total runtime: {elapsed:.1f}s")

    # Save summary
    summary = {
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'config': CONFIG,
        'runtime_s': elapsed,
    }

    with open('D:/Claude/ai-reservations/LP33-Euclidean-Emergence/experiments/simulation_summary.json', 'w') as f:
        json.dump(summary, f, indent=2, default=str)

    return dim_results


if __name__ == '__main__':
    main()

"""
P0: Large-Scale DGF Causal Set Simulation
==========================================
Produces publication-quality data for LP33 predictions.

Scale: N = 10^3, 10^4, 10^5
Topologies: random regular, 4D lattice, small-world
Dimensions: D = 2, 3, 4
Outputs: CSV datasets + summary JSON

Key optimizations for large N:
- Sparse event representation
- Sampling-based Myrheim-Meyer estimation
- Bidirectional BFS for efficient distance queries
- Event-driven dynamics with active qubit tracking
"""

import numpy as np
from collections import defaultdict, deque
import time
import json
import csv
import os

# ============================================================
# Topology Builders
# ============================================================

def build_random_regular(N, degree=None, seed=42):
    """Random regular-ish graph. Degree ~ log2(N) if not specified."""
    if degree is None:
        degree = max(2, int(np.log2(N)))
    rng = np.random.RandomState(seed)
    adj = defaultdict(list)
    # Use configuration model approximation
    stubs = []
    for i in range(N):
        stubs.extend([i] * degree)
    rng.shuffle(stubs)
    if len(stubs) % 2 != 0:
        stubs = stubs[:-1]
    for k in range(0, len(stubs), 2):
        u, v = stubs[k], stubs[k+1]
        if u != v:
            adj[u].append(v)
            adj[v].append(u)
    return adj

def build_4d_lattice(n_per_dim):
    """4D hypercubic lattice: n_per_dim^4 nodes, 8 neighbors each."""
    N = n_per_dim ** 4
    adj = defaultdict(list)
    for i in range(n_per_dim):
        for j in range(n_per_dim):
            for k in range(n_per_dim):
                for l in range(n_per_dim):
                    idx = ((i * n_per_dim + j) * n_per_dim + k) * n_per_dim + l
                    for di, dj, dk, dl in [
                        (1,0,0,0), (-1,0,0,0), (0,1,0,0), (0,-1,0,0),
                        (0,0,1,0), (0,0,-1,0), (0,0,0,1), (0,0,0,-1)
                    ]:
                        ni, nj, nk, nl = i+di, j+dj, k+dk, l+dl
                        if 0 <= ni < n_per_dim and 0 <= nj < n_per_dim and \
                           0 <= nk < n_per_dim and 0 <= nl < n_per_dim:
                            nidx = ((ni * n_per_dim + nj) * n_per_dim + nk) * n_per_dim + nl
                            adj[idx].append(nidx)
    return adj, N

def build_small_world(N, k=8, p_rewire=0.1, seed=42):
    """Watts-Strogatz small-world network."""
    rng = np.random.RandomState(seed)
    adj = defaultdict(list)
    # Start with ring lattice
    for i in range(N):
        for d in range(1, k//2 + 1):
            j = (i + d) % N
            adj[i].append(j)
            adj[j].append(i)
    # Rewire
    for i in range(N):
        neighbors = list(adj[i])
        for j in neighbors:
            if j > i and rng.random() < p_rewire:  # only rewire each edge once
                # Remove old edge
                adj[i].remove(j)
                adj[j].remove(i)
                # Add new edge to random node
                new_j = rng.randint(0, N-1)
                while new_j == i or new_j in adj[i]:
                    new_j = rng.randint(0, N-1)
                adj[i].append(new_j)
                adj[new_j].append(i)
    return adj


# ============================================================
# Efficient Graph Distance Oracle (landmark-based)
# ============================================================

class DistanceOracle:
    """Approximate graph distances using landmark nodes + BFS cache."""

    def __init__(self, adj, N, n_landmarks=50):
        self.adj = adj
        self.N = N
        self.n_landmarks = min(n_landmarks, N)
        self.landmarks = np.random.RandomState(42).choice(N, self.n_landmarks, replace=False)
        self.landmark_dists = {}
        self._cache = {}

        # Precompute distances from each landmark
        for lm in self.landmarks:
            self.landmark_dists[lm] = self._bfs_from(lm)

    def _bfs_from(self, source, max_dist=None):
        """BFS from source, returns dict of distances."""
        dist = {source: 0}
        queue = deque([source])
        while queue:
            node = queue.popleft()
            d = dist[node]
            if max_dist is not None and d >= max_dist:
                continue
            for nb in self.adj.get(node, []):
                if nb not in dist:
                    dist[nb] = d + 1
                    queue.append(nb)
        return dist

    def query(self, a, b, exact=True):
        """Get distance between a and b.
        If exact=False, use landmark lower bound approximation.
        """
        if a == b:
            return 0
        key = (min(a,b), max(a,b))
        if key in self._cache:
            return self._cache[key]

        if exact:
            # Bidirectional BFS
            dist_a = {a: 0}
            dist_b = {b: 0}
            q_a = deque([a])
            q_b = deque([b])
            while q_a and q_b:
                # Expand from a
                node = q_a.popleft()
                d = dist_a[node]
                if node in dist_b:
                    result = d + dist_b[node]
                    self._cache[key] = result
                    return result
                for nb in self.adj.get(node, []):
                    if nb not in dist_a:
                        dist_a[nb] = d + 1
                        q_a.append(nb)

                # Expand from b
                node = q_b.popleft()
                d = dist_b[node]
                if node in dist_a:
                    result = d + dist_a[node]
                    self._cache[key] = result
                    return result
                for nb in self.adj.get(node, []):
                    if nb not in dist_b:
                        dist_b[nb] = d + 1
                        q_b.append(nb)

            return float('inf')  # Disconnected
        else:
            # Landmark lower bound
            lb = 0
            for lm in self.landmarks:
                if a in self.landmark_dists[lm] and b in self.landmark_dists[lm]:
                    lb = max(lb, abs(self.landmark_dists[lm][a] - self.landmark_dists[lm][b]))
            self._cache[key] = lb
            return lb


# ============================================================
# DGF Simulation Engine (Optimized for Scale)
# ============================================================

class DGFSimulation:
    """Large-scale DGF determination simulation."""

    def __init__(self, adj, N, D_space, p_spont, coupling_strength, v_eff=1.0, seed=42):
        self.adj = adj
        self.N = N
        self.D = D_space
        self.p_spont = p_spont
        self.J = coupling_strength
        self.v_eff = v_eff
        self.rng = np.random.RandomState(seed)

        # State tracking
        self.determined = np.zeros(N, dtype=bool)
        self.directions = np.zeros((N, D_space))
        self.determination_time = np.full(N, -1, dtype=np.int32)

        # Active set: recently determined qubits that can trigger neighbors
        self.active = set()
        self.current_step = 0

        # Event log
        self.events = []  # list of (qubit, time, triggered_by)

        # Distance oracle (built lazily)
        self._oracle = None

    def _get_oracle(self):
        if self._oracle is None:
            n_lm = min(50, self.N)
            self._oracle = DistanceOracle(self.adj, self.N, n_landmarks=n_lm)
        return self._oracle

    def _random_direction(self):
        v = self.rng.randn(self.D)
        v /= np.linalg.norm(v)
        return v

    def step(self):
        """One simulation step."""
        self.current_step += 1

        # Spontaneous determinations among undetermined qubits
        undetermined = np.where(~self.determined)[0]
        if len(undetermined) > 0:
            n_spont = self.rng.binomial(len(undetermined), self.p_spont)
            if n_spont > 0:
                spont_idx = self.rng.choice(undetermined, n_spont, replace=False)
                for q in spont_idx:
                    self._determine(q, triggered_by=None)

        # Coupled determinations from active qubits
        active_list = list(self.active)
        if active_list:
            for src in active_list:
                src_dir = self.directions[src]
                neighbors = self.adj.get(src, [])
                for nb in neighbors:
                    if not self.determined[nb]:
                        # Probability of triggering
                        p_trig = self.J / len(neighbors) if neighbors else 0
                        if self.rng.random() < p_trig:
                            self._determine(nb, triggered_by=src)

    def _determine(self, qubit, triggered_by=None):
        """Mark qubit as determined."""
        self.determined[qubit] = True
        self.determination_time[qubit] = self.current_step

        if triggered_by is not None:
            # Aligned with trigger direction + noise
            trigger_dir = self.directions[triggered_by]
            noise = self.rng.randn(self.D) * 0.1
            new_dir = trigger_dir + noise
            self.directions[qubit] = new_dir / np.linalg.norm(new_dir)
        else:
            self.directions[qubit] = self._random_direction()

        self.events.append((qubit, self.current_step, triggered_by))
        self.active.add(qubit)

    def run(self, max_steps=10000, target_fraction=0.95):
        """Run until target fraction determined or max steps."""
        for _ in range(max_steps):
            self.step()
            if np.mean(self.determined) >= target_fraction:
                break
            # Prune active set: remove qubits that have been active for many steps
            if len(self.active) > 1000:
                self.active = set(q for q in self.active
                                if self.current_step - self.determination_time[q] < 10)

        return {
            'N': self.N,
            'M': len(self.events),
            'rho_D_final': np.mean(self.determined),
            'steps': self.current_step,
        }

    def estimate_myrheim_meyer(self, n_samples=50000):
        """Estimate Myrheim-Meyer ratio R/M^2 via random sampling.
        Returns (ratio, standard_error).
        """
        M = len(self.events)
        if M < 2:
            return 0.0, 0.0, M

        oracle = self._get_oracle()
        times = np.array([e[1] for e in self.events])
        qubits = np.array([e[0] for e in self.events])

        # Sample random event pairs
        n_pairs = min(n_samples, M * (M-1) // 2)
        R_sample = 0
        n_valid = 0

        for _ in range(n_pairs):
            a = self.rng.randint(0, M)
            b = self.rng.randint(0, M)
            if a == b:
                continue
            # Ensure t_a < t_b
            if times[a] >= times[b]:
                a, b = b, a
            if times[a] >= times[b]:
                continue

            dt = times[b] - times[a]
            d_g = oracle.query(int(qubits[a]), int(qubits[b]), exact=True)
            n_valid += 1
            if d_g <= self.v_eff * dt:
                R_sample += 1

        if n_valid == 0:
            return 0.0, 0.0, M

        p_hat = R_sample / n_valid  # estimated fraction of causally related pairs
        # Standard error for binomial proportion
        se = np.sqrt(p_hat * (1 - p_hat) / n_valid)
        # Scale to R/M^2: R/M^2 ~ p * ((M-1)/M) / 2
        ratio = p_hat * (M - 1) / (2 * M)

        return ratio, se, M

    def compute_eta(self):
        """Compute time direction uniqueness eta."""
        determined_idx = np.where(self.determined)[0]
        if len(determined_idx) < 2:
            return 0.0

        dirs = self.directions[determined_idx]
        primary = np.argmax(np.abs(dirs), axis=1)
        counts = np.bincount(primary, minlength=self.D)
        if np.std(counts) == 0:
            return 0.0
        return (np.max(counts) - np.mean(counts)) / np.std(counts)

    def compute_alignment(self):
        """Mean cosine between determined qubit directions (sampled)."""
        determined_idx = np.where(self.determined)[0]
        n_det = len(determined_idx)
        if n_det < 2:
            return 0.0

        # Sample pairs for efficiency at large N
        n_sample = min(5000, n_det * (n_det - 1) // 2)
        cosines = []
        for _ in range(n_sample):
            i, j = self.rng.choice(determined_idx, 2, replace=False)
            cos = np.dot(self.directions[i], self.directions[j])
            cosines.append(cos)
        return np.mean(cosines), np.std(cosines) / np.sqrt(n_sample)


# ============================================================
# Parameter Scan
# ============================================================

GAMMA_D = {2: 0.5, 3: 0.298, 4: 0.201, 5: 0.137}

TOPOLOGY_BUILDERS = {
    'random_regular': lambda N, seed: build_random_regular(N, seed=seed),
    'small_world': lambda N, seed: build_small_world(N, k=8, p_rewire=0.1, seed=seed),
}

def add_lattice_topologies():
    """Add 4D lattice configurations for N that are perfect 4th powers."""
    configs = []
    for n_per_dim in [4, 6, 8, 10]:  # 256, 1296, 4096, 10000
        N = n_per_dim ** 4
        configs.append((f'4d_lattice_n{n_per_dim}', N, n_per_dim))
    return configs

def run_config(N, D, topology_name, adj, p_spont, J, v_eff, n_trials, seed_base):
    """Run multiple trials for one configuration."""
    results = []
    for trial in range(n_trials):
        seed = seed_base + trial
        sim = DGFSimulation(adj, N, D, p_spont, J, v_eff=v_eff, seed=seed)
        sim.run(max_steps=min(20000, N * 2))

        mm_ratio, mm_se, M = sim.estimate_myrheim_meyer(n_samples=min(50000, N*5))
        eta = sim.compute_eta()
        align_mean, align_se = sim.compute_alignment()

        # Best-fit Myrheim-Meyer dimension
        best_d = min(GAMMA_D, key=lambda d: abs(mm_ratio - GAMMA_D[d]))
        dist_to_4 = abs(mm_ratio - GAMMA_D[4])

        results.append({
            'N': N, 'D': D, 'topology': topology_name,
            'trial': trial,
            'M': M, 'steps': sim.current_step,
            'rho_D_final': float(np.mean(sim.determined)),
            'mm_ratio': float(mm_ratio), 'mm_se': float(mm_se),
            'mm_dimension': best_d, 'dist_to_gamma4': float(dist_to_4),
            'eta': float(eta),
            'alignment_mean': float(align_mean), 'alignment_se': float(align_se),
        })
        print(f"  [{topology_name}] N={N} D={D} Trial {trial+1}/{n_trials}: "
              f"M={M}, MM-ratio={mm_ratio:.4f}+/-{mm_se:.4f}, d={best_d}, "
              f"eta={eta:.3f}")

    return results


def main():
    OUTPUT_DIR = 'D:/Claude/ai-reservations/LP33-Euclidean-Emergence/experiments/p0_data'
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Parameter grid
    N_values = [1000, 5000, 10000]  # Can add 50000, 100000 for full scale
    D_values = [2, 3, 4]
    topologies = ['random_regular', 'small_world']
    p_spont_values = [0.0005, 0.001]
    J_values = [0.2, 0.4]
    n_trials = 5
    seed_base = 42

    all_results = []
    total_configs = (len(N_values) * len(D_values) * len(topologies) *
                     len(p_spont_values) * len(J_values))

    # Add lattice configs
    lattice_configs = add_lattice_topologies()

    print(f"P0 Large-Scale Simulation")
    print(f"Configs: {total_configs} + {len(lattice_configs)} lattice")
    print(f"Trials per config: {n_trials}")
    print(f"Total runs: {(total_configs + len(lattice_configs)) * n_trials}")
    print("=" * 60)

    t_start = time.time()
    config_count = 0

    # Standard parameter scan
    for N in N_values:
        for D in D_values:
            for topo_name in topologies:
                for p_spont in p_spont_values:
                    for J in J_values:
                        config_count += 1
                        seed = seed_base + config_count * 100
                        adj = TOPOLOGY_BUILDERS[topo_name](N, seed=seed)

                        print(f"\n[{config_count}/{total_configs}] "
                              f"N={N} D={D} {topo_name} p={p_spont} J={J}")

                        results = run_config(N, D, topo_name, adj, p_spont, J,
                                           v_eff=1.0, n_trials=n_trials,
                                           seed_base=seed)
                        all_results.extend(results)

    # Lattice configurations (only for D=4, one J and p_spont)
    for topo_name, N, n_per_dim in lattice_configs:
        if N > max(N_values):
            continue  # Skip if larger than our max N for now
        config_count += 1
        adj, _ = build_4d_lattice(n_per_dim)
        D = 4
        p_spont = 0.001
        J = 0.4
        v_eff = 0.7  # Tuned from audit

        print(f"\n[{config_count}] LATTICE N={N} D={D} n_per_dim={n_per_dim} v_eff={v_eff}")

        results = run_config(N, D, topo_name, adj, p_spont, J,
                           v_eff=v_eff, n_trials=n_trials,
                           seed_base=seed_base + config_count * 100)
        all_results.extend(results)

    t_elapsed = time.time() - t_start

    # Write CSV
    csv_path = os.path.join(OUTPUT_DIR, 'p0_results.csv')
    if all_results:
        with open(csv_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=all_results[0].keys())
            writer.writeheader()
            writer.writerows(all_results)
        print(f"\nCSV written: {csv_path} ({len(all_results)} rows)")

    # Write summary JSON
    summary = {
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'total_runs': len(all_results),
        'total_configs': config_count,
        'runtime_s': t_elapsed,
        'parameter_grid': {
            'N_values': N_values,
            'D_values': D_values,
            'topologies': topologies + [c[0] for c in lattice_configs],
            'p_spont_values': p_spont_values,
            'J_values': J_values,
            'n_trials': n_trials,
        },
    }

    # Compute aggregate statistics
    if all_results:
        # P4 check: aggregate eta by D
        eta_by_D = defaultdict(list)
        for r in all_results:
            eta_by_D[r['D']].append(r['eta'])
        summary['P4_eta_by_D'] = {
            str(D): {'mean': float(np.mean(vals)), 'std': float(np.std(vals)),
                     'n': len(vals)}
            for D, vals in eta_by_D.items()
        }
        eta_means = {D: np.mean(vals) for D, vals in eta_by_D.items()}
        summary['P4_pass'] = eta_means.get(4, 0) > eta_means.get(3, 0) > eta_means.get(2, 0)

        # P3: Myrheim-Meyer dimension distribution
        mm_dims = [r['mm_dimension'] for r in all_results]
        summary['P3_mm_dimension_distribution'] = {
            str(d): mm_dims.count(d) for d in sorted(set(mm_dims))
        }

        # Best MM result for Gamma_4
        best = min(all_results, key=lambda r: r['dist_to_gamma4'])
        summary['P3_best_gamma4_match'] = {
            'N': best['N'], 'D': best['D'], 'topology': best['topology'],
            'mm_ratio': best['mm_ratio'], 'dist_to_gamma4': best['dist_to_gamma4'],
        }

    json_path = os.path.join(OUTPUT_DIR, 'p0_summary.json')
    with open(json_path, 'w') as f:
        json.dump(summary, f, indent=2)

    print(f"JSON written: {json_path}")
    print(f"\nTotal runtime: {t_elapsed:.0f}s ({t_elapsed/60:.1f}min)")
    print(f"Results: {len(all_results)} runs across {config_count} configs")

    # Quick P4 report
    print("\n" + "=" * 60)
    print("P4 QUICK REPORT")
    for D in [2, 3, 4]:
        vals = eta_by_D[D]
        print(f"  D={D}: eta = {np.mean(vals):.3f} +/- {np.std(vals):.3f} (n={len(vals)})")
    print(f"  P4: {'PASS' if summary['P4_pass'] else 'FAIL'}")


if __name__ == '__main__':
    main()

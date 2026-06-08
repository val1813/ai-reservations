"""
Kinetic Monte Carlo simulation of DGF jump dynamics on 2D lattice.
B博士 Round 3 — LP32-S7 χ-braking numerical verification.
Optimized with active-edge list (NW5 fix).
"""

import numpy as np
import sys
import time as walltime
from collections import deque

class DGFKMC:
    """Optimized DGF Kinetic Monte Carlo with active-edge list."""

    def __init__(self, L=30, gamma0=1.0, seed=42):
        self.L = L
        self.N = L * L
        self.gamma0 = gamma0
        self.rng = np.random.RandomState(seed)

        # spins: +1 = |1> (causal), -1 = |0> (unoccupied)
        self.spins = np.zeros(self.N, dtype=np.int8)

        # Pre-build edge lists
        self.out_edges = self._build_edges()
        self.in_edges = self._build_in_edges()

        # Active-edge optimization (NW5): maintain list of active edges
        # active_edges: list of (i, j) tuples where s_i=+1, s_j=-1
        self.active_edges = []  # list of (i, j)
        self._active_edge_set = set()  # for O(1) membership check

        # For each node, track which outgoing edges are active
        self._node_active_out = [set() for _ in range(self.N)]

        self.t = 0.0
        self.total_jumps = 0

        # Recording
        self.jump_times = []  # record each jump time for burst analysis

    def _build_edges(self):
        """Build directed edges on 2D square lattice with PBC."""
        L = self.L
        edges = [[] for _ in range(self.N)]
        for x in range(L):
            for y in range(L):
                i = x * L + y
                edges[i].append(((x+1)%L)*L + y)
                edges[i].append(((x-1)%L)*L + y)
                edges[i].append(x*L + (y+1)%L)
                edges[i].append(x*L + (y-1)%L)
        return edges

    def _build_in_edges(self):
        """Build reverse adjacency."""
        L = self.L
        in_edges = [[] for _ in range(self.N)]
        for i in range(self.N):
            for j in self.out_edges[i]:
                in_edges[j].append(i)
        return in_edges

    def initialize(self, p0=0.5, mode='random'):
        """Initialize spin configuration."""
        L = self.L
        if mode == 'random':
            self.spins = np.where(self.rng.random(self.N) < p0, -1, 1)
        elif mode == 'anticorrelated':
            self.spins = np.where(self.rng.random(self.N) < p0, -1, 1)
            for i in range(self.N):
                if self.spins[i] == 1:
                    for j in self.out_edges[i]:
                        if self.spins[j] == 1 and self.rng.random() < 0.5:
                            self.spins[j] = -1
        elif mode == 'seed':
            self.spins = np.where(self.rng.random(self.N) < p0, -1, 1)
            c = L // 2
            half_w = 2
            for x in range(c-half_w, c+half_w+1):
                for y in range(c-half_w, c+half_w+1):
                    self.spins[x*L + y] = 1
        elif mode == 'stripes':
            stripe_w = 5
            for x in range(L):
                for y in range(L):
                    i = x * L + y
                    stripe_idx = x // stripe_w
                    self.spins[i] = 1 if stripe_idx % 2 == 0 else -1

        # Build initial active edge list (NW5 optimization)
        self._rebuild_active_edges()

    def _rebuild_active_edges(self):
        """Full rebuild of active edge list (used at initialization)."""
        self.active_edges = []
        self._active_edge_set = set()
        self._node_active_out = [set() for _ in range(self.N)]

        for i in range(self.N):
            if self.spins[i] != 1:
                continue
            for j in self.out_edges[i]:
                if self.spins[j] == -1:
                    self.active_edges.append((i, j))
                    self._active_edge_set.add((i, j))
                    self._node_active_out[i].add(j)

    def _update_active_edges_after_jump(self, i, j):
        """Update active edge list after jump at (i,j): s_j: -1 -> +1.

        Affected edges:
        1. All incoming edges to j (k -> j): j is now +1, so these deactivate
        2. All outgoing edges from j (j -> k): j is now +1, so check k status
        3. Outgoing edges FROM i: since we just used one, check if i has other |0> targets
        """
        # 1. Deactivate all incoming edges to j (j is now |1>, no longer a valid target)
        for k in self.in_edges[j]:
            edge = (k, j)
            if edge in self._active_edge_set:
                self._active_edge_set.discard(edge)
                self._node_active_out[k].discard(j)
        # Remove from active_edges list (batch removal later, or use set-based)

        # 2. Activate outgoing edges from j (j is now |1>, can trigger its neighbors)
        for k in self.out_edges[j]:
            if self.spins[k] == -1:
                edge = (j, k)
                if edge not in self._active_edge_set:
                    self._active_edge_set.add(edge)
                    self._node_active_out[j].add(k)

        # 3. The edge (i, j) we just used is now deactivated (j became +1)
        self._active_edge_set.discard((i, j))
        self._node_active_out[i].discard(j)

        # active_edges list is rebuilt from _active_edge_set in step() each call

    def step(self):
        """Execute one KMC step. Returns True if a jump occurred."""
        # Always rebuild from set to avoid stale-list bug
        self.active_edges = list(self._active_edge_set)

        if len(self.active_edges) == 0:
            return False

        n_active = len(self.active_edges)

        # Each active edge has rate gamma0
        R_total = self.gamma0 * n_active

        # Draw time increment
        dt = self.rng.exponential(1.0 / R_total)
        self.t += dt

        # Choose which edge fires (uniform random among active edges)
        idx = self.rng.randint(0, n_active)
        i, j = self.active_edges[idx]

        # Execute jump
        self.spins[j] = 1  # |0>_j -> |1>_j
        self.total_jumps += 1
        self.jump_times.append(self.t)

        # Update active edges incrementally
        self._update_active_edges_after_jump(i, j)

        return True

    def measure_observables(self):
        """Compute Q, chi_bar, and R from current configuration."""
        # Q: global |0> fraction
        Q = np.mean(self.spins == -1)

        # bar_chi: average edge correlation (spatial average)
        chi_sum = 0.0
        total_edges = 0
        for i in range(self.N):
            for j in self.out_edges[i]:
                chi_sum += self.spins[i] * self.spins[j]
                total_edges += 1
        s_mean = np.mean(self.spins)
        chi_bar = chi_sum / total_edges - s_mean * s_mean

        # R: active edge count normalized
        R = len(self._active_edge_set) / self.N

        return Q, chi_bar, R

    def measure_v(self):
        """Compute Lyapunov function V = sum[4(1-qi)qj - chi_ij]."""
        # For instantaneous config, estimate qi as fraction of |0>
        # Use local neighborhood averages for qi, qj
        V_total = 0.0
        total_edges = 0

        # Need local q estimates: use 3x3 window average
        q_local = np.zeros(self.N)
        for i in range(self.N):
            xi, yi = i // self.L, i % self.L
            count_0 = 0
            count_total = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx = (xi + dx) % self.L
                    ny = (yi + dy) % self.L
                    ni = nx * self.L + ny
                    if self.spins[ni] == -1:
                        count_0 += 1
                    count_total += 1
            q_local[i] = count_0 / count_total

        for i in range(self.N):
            for j in self.out_edges[i]:
                # V_ij = 4*(1-qi)*qj - chi_ij
                # chi_ij estimate: s_i*s_j - (2*1-qi-1)*(2*qj-1)? No...
                # Better: chi_ij = s_i*s_j - m_i*m_j
                # m_i = 1 - 2*q_local[i]
                mi = 1 - 2*q_local[i]
                mj = 1 - 2*q_local[j]
                chi_ij = self.spins[i] * self.spins[j] - mi * mj
                V_ij = 4 * (1 - q_local[i]) * q_local[j] - chi_ij
                V_total += V_ij
                total_edges += 1

        return V_total / total_edges  # average V per edge

    def compute_chi_distance(self, d_max=15):
        """Compute χ as function of Manhattan distance d."""
        L = self.L
        s = self.spins.astype(np.float64)
        s_mean = np.mean(s)

        chi_d = np.zeros(d_max)
        count_d = np.zeros(d_max, dtype=int)

        for i in range(self.N):
            xi, yi = i // L, i % L
            for j in range(i+1, self.N):
                xj, yj = j // L, j % L
                dx = min(abs(xi - xj), L - abs(xi - xj))
                dy = min(abs(yi - yj), L - abs(yi - yj))
                d = dx + dy
                if d < d_max:
                    chi_d[d] += s[i] * s[j] - s_mean * s_mean
                    count_d[d] += 1

        for d in range(d_max):
            if count_d[d] > 0:
                chi_d[d] /= count_d[d]

        return chi_d


def run_simulation(L=30, p0=0.5, mode='random', max_jumps=2_000_000,
                   measure_every=5000, stop_if_dead=50000, seed=42,
                   verbose=True):
    """Run a full KMC simulation and return history."""

    sim = DGFKMC(L=L, gamma0=1.0, seed=seed)
    sim.initialize(p0=p0, mode=mode)

    if verbose:
        print(f"Initialized {L}x{L} lattice ({sim.N} sites)")
        print(f"Mode: {mode}, p0: {p0}")
        print(f"Initial active edges: {len(sim._active_edge_set)}")
        print(f"Initial Q: {np.mean(sim.spins == -1):.4f}")
        print("-" * 60)

    history = {
        't': [], 'Q': [], 'chi_bar': [], 'R': [], 'V': [],
        'jumps': [], 'step_count': []
    }

    steps_since_last_jump = 0
    next_measure = 0
    start_wall = walltime.time()

    for step_count in range(max_jumps * 2):  # allow for dead steps
        jumped = sim.step()

        if not jumped:
            steps_since_last_jump += 1
            if steps_since_last_jump > stop_if_dead:
                if verbose:
                    print(f"System dead at step {step_count}")
                break
        else:
            steps_since_last_jump = 0

        if sim.total_jumps >= next_measure:
            Q, chi_bar, R = sim.measure_observables()
            V = sim.measure_v()
            history['t'].append(sim.t)
            history['Q'].append(Q)
            history['chi_bar'].append(chi_bar)
            history['R'].append(R)
            history['V'].append(V)
            history['jumps'].append(sim.total_jumps)
            history['step_count'].append(step_count)

            next_measure += measure_every

            if verbose and sim.total_jumps % (measure_every * 10) == 0:
                wall_elapsed = walltime.time() - start_wall
                print(f"  jumps={sim.total_jumps:>8d}  t={sim.t:.4f}  Q={Q:.4f}  "
                      f"chi_bar={chi_bar:.4f}  R={R:.4f}  wall={wall_elapsed:.1f}s")

        if sim.total_jumps >= max_jumps:
            if verbose:
                print(f"Reached max_jumps={max_jumps}")
            break

    wall_elapsed = walltime.time() - start_wall
    if verbose:
        print(f"\nSimulation complete: {sim.total_jumps} jumps in {wall_elapsed:.1f}s")
        print(f"Final state: Q={history['Q'][-1]:.4f}, chi_bar={history['chi_bar'][-1]:.4f}")
        print(f"Final R={history['R'][-1]:.6f}, V={history['V'][-1]:.6f}")

    return sim, history


if __name__ == '__main__':
    import json

    L = 30
    if len(sys.argv) > 1:
        L = int(sys.argv[1])

    max_jumps = 2_000_000
    if len(sys.argv) > 2:
        max_jumps = int(sys.argv[2])

    # Run IC-A with p0=0.5
    print("=" * 60)
    print(f"B博士 Round 3 — DGF KMC Simulation")
    print(f"Lattice: {L}x{L}, max_jumps: {max_jumps}")
    print("=" * 60)

    sim, hist = run_simulation(L=L, p0=0.5, mode='random',
                               max_jumps=max_jumps, measure_every=5000, seed=42)

    # Compute final chi(d)
    print("\nComputing chi(d)...")
    chi_d = sim.compute_chi_distance(d_max=15)
    print("chi(d):", np.array2string(chi_d, precision=4, max_line_width=120))

    # Save results
    results = {
        'L': L,
        'N': L*L,
        'p0': 0.5,
        'mode': 'random',
        'total_jumps': int(sim.total_jumps),
        't_final': float(sim.t),
        't': [float(x) for x in hist['t']],
        'Q': [float(x) for x in hist['Q']],
        'chi_bar': [float(x) for x in hist['chi_bar']],
        'R': [float(x) for x in hist['R']],
        'V': [float(x) for x in hist['V']],
        'jumps': [int(x) for x in hist['jumps']],
        'chi_d': [float(x) for x in chi_d],
    }

    outpath = f"/d/Claude/ai-reservations/LP32-how to destroy a universe/LP32-S7_Causal-Creation/current/B/kmc_results_L{L}.json"
    with open(outpath, 'w') as f:
        json.dump(results, f)
    print(f"\nResults saved to {outpath}")

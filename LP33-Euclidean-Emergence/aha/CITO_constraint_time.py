"""
CITO: Constraint-Induced Temporal Order
========================================
A non-circular approach to time emergence.

NO: steps, events, happening, before/after, dynamics
YES: variables, constraints, solutions, partial order

Core idea:
- N boolean variables x_i in {0,1}
- Constraints: x_i <= x_j (if i is 1, j must be 1)
- The set of all satisfying assignments induces a partial order
- "Time direction" = gradient from constrained to unconstrained
- This exists WITHOUT any notion of time or dynamics
"""

import numpy as np
from collections import defaultdict, deque
import itertools

class ConstraintGraph:
    """Static constraint satisfaction problem. No time. No dynamics."""

    def __init__(self, N, D, topology='grid', seed=42):
        """
        N: number of variables
        D: dimensionality of the constraint graph
        topology: 'grid' (D-dimensional lattice), 'random', 'smallworld'
        """
        self.N = N
        self.D = D
        self.rng = np.random.RandomState(seed)

        # Build constraint graph (undirected adjacency)
        if topology == 'grid':
            self.adj = self._build_grid()
        elif topology == 'random':
            self.adj = self._build_random()
        else:
            self.adj = self._build_smallworld()

        # Each undirected edge becomes a directed constraint x_i <= x_j
        # Direction: randomly chosen, representing "i being 1 forces j to be 1"
        self.constraints = []
        for i in self.adj:
            for j in self.adj[i]:
                if i < j:  # each edge once
                    if self.rng.random() < 0.5:
                        self.constraints.append((i, j))  # i->j
                    else:
                        self.constraints.append((j, i))  # j->i

    def _build_grid(self):
        """D-dimensional grid. n_per_dim^D = N."""
        n_per_dim = max(2, int(round(self.N ** (1.0 / self.D))))
        actual_N = n_per_dim ** self.D
        # Use actual_N nodes
        adj = defaultdict(list)
        # Map D-dimensional coords to 1D index
        for idx in range(actual_N):
            # Decode index to D-dimensional coordinates
            coords = []
            tmp = idx
            for d in range(self.D):
                coords.append(tmp % n_per_dim)
                tmp //= n_per_dim
            # Connect to neighbors in each dimension
            for d in range(self.D):
                for delta in [-1, 1]:
                    nc = list(coords)
                    nc[d] += delta
                    if 0 <= nc[d] < n_per_dim:
                        # Encode back
                        nidx = 0
                        for dd in range(self.D-1, -1, -1):
                            nidx = nidx * n_per_dim + nc[dd]
                        adj[idx].append(nidx)
        self.N = actual_N
        return adj

    def _build_random(self):
        """Random regular-ish graph."""
        degree = max(2, int(np.log2(self.N)))
        adj = defaultdict(list)
        stubs = [i for i in range(self.N) for _ in range(degree)]
        self.rng.shuffle(stubs)
        if len(stubs) % 2:
            stubs = stubs[:-1]
        for k in range(0, len(stubs), 2):
            u, v = stubs[k], stubs[k+1]
            if u != v:
                adj[u].append(v)
                adj[v].append(u)
        return adj

    def _build_smallworld(self):
        """Watts-Strogatz small-world."""
        k = 4
        p_rewire = 0.1
        adj = defaultdict(list)
        for i in range(self.N):
            for d in range(1, k//2 + 1):
                j = (i + d) % self.N
                adj[i].append(j)
                adj[j].append(i)
        for i in range(self.N):
            neighbors = list(adj[i])
            for j in neighbors:
                if j > i and self.rng.random() < p_rewire:
                    adj[i].remove(j)
                    adj[j].remove(i)
                    new_j = self.rng.randint(0, self.N-1)
                    while new_j == i or new_j in adj[i]:
                        new_j = self.rng.randint(0, self.N-1)
                    adj[i].append(new_j)
                    adj[new_j].append(i)
        return adj

    def compute_partial_order(self):
        """
        Compute the partial order induced by constraints.

        For each variable i, compute:
        - ancestors(i): variables that MUST be 1 if i is 1 (via constraint chains)
        - descendants(i): variables that MUST be 0 if i is 0

        This is purely structural — no time, no dynamics.
        """
        N = self.N

        # Build directed constraint graph
        children = defaultdict(list)   # i -> j means: if i=1 then j=1
        parents = defaultdict(list)    # j's parents: who forces j to 1

        for (src, dst) in self.constraints:
            children[src].append(dst)
            parents[dst].append(src)

        # Transitive closure: ancestors = all nodes reachable going UPSTREAM
        ancestors = {}
        for i in range(N):
            # BFS from i following parents (who must be 1 before i can be 1)
            anc = set()
            queue = deque([i])
            while queue:
                node = queue.popleft()
                for p in parents.get(node, []):
                    if p not in anc:
                        anc.add(p)
                        queue.append(p)
            ancestors[i] = anc

        # Descendants: all nodes reachable going DOWNSTREAM
        descendants = {}
        for i in range(N):
            desc = set()
            queue = deque([i])
            while queue:
                node = queue.popleft()
                for c in children.get(node, []):
                    if c not in desc:
                        desc.add(c)
                        queue.append(c)
            descendants[i] = desc

        # Compute "determination level" = size of ancestor set
        # Variables with many ancestors are "more determined" (closer to "past")
        determination = {i: len(ancestors[i]) for i in range(N)}

        # Normalize to [0,1]
        max_det = max(determination.values()) if determination else 1
        determination_norm = {i: d/max_det for i, d in determination.items()} if max_det > 0 else determination

        # "Time direction": constraints src->dst means dst inherits src's ancestors
        # ancestors[dst] includes ancestors[src] + {src} + ...
        # So len(ancestors[dst]) >= len(ancestors[src]) + 1
        # dst has MORE ancestors = more constrained = "later in time"
        # Time flows: src (past, fewer constraints) -> dst (future, more constraints)
        edge_directions = []
        violations = 0
        for (src, dst) in self.constraints:
            if determination[src] < determination[dst]:
                edge_directions.append(1)   # aligned: past -> future
            elif determination[src] == determination[dst]:
                edge_directions.append(0)   # same time layer
            else:
                edge_directions.append(-1)  # violation (shouldn't happen in DAG)
                violations += 1

        # Fraction of edges aligned with global time direction
        frac_aligned = sum(1 for d in edge_directions if d == 1) / len(edge_directions) if edge_directions else 0

        return {
            'determination': determination,
            'determination_norm': determination_norm,
            'frac_aligned': frac_aligned,
            'max_ancestors': max_det,
            'mean_ancestors': np.mean(list(determination.values())),
        }


def analyze_cito():
    """Test CITO framework: how does partial order richness depend on D?"""
    print("CITO: Constraint-Induced Temporal Order")
    print("=" * 60)
    print("NO time. NO dynamics. NO events. Just constraints + partial order.")
    print()

    for D in [1, 2, 3, 4]:
        print(f"\n--- D = {D} ---")
        results = []
        for trial in range(5):
            # Grid topology: N ~ 100-256 depending on D
            n_per_dim = {1: 100, 2: 10, 3: 5, 4: 4}[D]
            N = n_per_dim ** D
            cg = ConstraintGraph(N, D, topology='grid', seed=42+trial)
            po = cg.compute_partial_order()
            results.append(po)

        frac = np.mean([r['frac_aligned'] for r in results])
        max_anc = np.mean([r['max_ancestors'] for r in results])
        mean_anc = np.mean([r['mean_ancestors'] for r in results])

        print(f"  N = {N} ({n_per_dim}^{D})")
        print(f"  Fraction of constraints aligned with time: {frac:.3f}")
        print(f"  Max ancestors (time depth): {max_anc:.0f}")
        print(f"  Mean ancestors: {mean_anc:.1f}")

    # Test: random constraints vs grid constraints
    print("\n--- Topology comparison (D=3, N=125) ---")
    for topo in ['grid', 'random', 'smallworld']:
        results = []
        for trial in range(5):
            cg = ConstraintGraph(125, 3, topology=topo, seed=42+trial)
            po = cg.compute_partial_order()
            results.append(po)
        frac = np.mean([r['frac_aligned'] for r in results])
        max_anc = np.mean([r['max_ancestors'] for r in results])
        print(f"  {topo:12s}: frac_aligned={frac:.3f}, max_ancestors={max_anc:.0f}")

    # Key test: does constraint graph dimensionality create a global time direction?
    print("\n--- KEY TEST: Global time direction from constraints alone ---")
    for D in [1, 2, 3, 4]:
        n_per_dim = {1: 100, 2: 10, 3: 5, 4: 4}[D]
        N = n_per_dim ** D
        cg = ConstraintGraph(N, D, topology='grid', seed=42)
        po = cg.compute_partial_order()

        # Distribution of determination levels
        det_vals = list(po['determination'].values())
        print(f"  D={D}: determination range=[{min(det_vals)}, {max(det_vals)}], "
              f"std={np.std(det_vals):.1f}, unique levels={len(set(det_vals))}")

    print()
    print("INTERPRETATION:")
    print("  frac_aligned = fraction of constraints pointing from past to future")
    print("  max_ancestors = how many 'layers' of time exist")
    print("  More unique determination levels = richer temporal structure")
    print()
    print("This framework has ZERO temporal assumptions:")
    print("  - No steps, no events, no dynamics")
    print("  - Just: N boolean variables + pairwise constraints")
    print("  - Time = partial order induced by constraint chains")
    print("  - Space = pairs of variables with no constraint relation")


if __name__ == '__main__':
    analyze_cito()

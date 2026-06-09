"""
LP36 R4 — DGF Causal Graph Monte Carlo: Betti number survival under cyclic reset
Tests the Goldilocks hypothesis:  beta₁ survives in a density window, dies outside.
"""
import numpy as np
from collections import defaultdict
import itertools
import warnings
warnings.filterwarnings('ignore')

# --- 1. Causal DAG generation (1+1D Minkowski sprinkling) ---
def generate_causal_dag(N, rho_factor=1.0):
    """
    Generate causal DAG via Poisson sprinkling in 1+1D Minkowski.
    rho_factor scales density: 1.0 = baseline rho₀.
    """
    L = (N / rho_factor) ** (1/2)  # box size
    points = np.random.uniform(0, L, (N, 2))  # (x, t)

    edges = []
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            dt = points[j, 1] - points[i, 1]
            dx = abs(points[j, 0] - points[i, 0])
            # Causal if within light cone and future-directed
            if dt > 0 and dx < dt:
                edges.append((i, j))

    # Build Hasse diagram (transitive reduction)
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)

    # Transitive reduction: remove edge u→v if exists u→w→v
    hasse_edges = []
    for u, v in edges:
        # Check if there's an intermediate w
        transitive = False
        for w in adj[u]:
            if w != v and v in adj[w]:
                transitive = True
                break
        if not transitive:
            hasse_edges.append((u, v))

    return hasse_edges, N

# --- 2. Clique complex and Betti numbers ---
def edges_to_adj_matrix(edges, N):
    """Build undirected adjacency from Hasse edges."""
    A = np.zeros((N, N), dtype=int)
    for u, v in edges:
        A[u, v] = 1
        A[v, u] = 1  # undirected for clique complex
    return A

def compute_clique_complex_betti(edges, N, k=1):
    """
    Compute Betti numbers via clique complex.
    For k=1: count cycles in the 1-skeleton, considering 2-simplices.

    Simplified approach for small N:
    - Build 1-skeleton (edges as undirected)
    - Find 2-simplices (triangles = 3-cliques)
    - b_0 = number of connected components
    - b_1 = dim(ker(∂₁)/im(∂₂)) simplified = |E| - |V| + |C| - |T|
      where |T| = number of independent triangles
    """
    A = edges_to_adj_matrix(edges, N)

    # b_0: connected components
    visited = set()
    b0 = 0
    for i in range(N):
        if i not in visited:
            b0 += 1
            stack = [i]
            while stack:
                v = stack.pop()
                if v in visited:
                    continue
                visited.add(v)
                for u in range(N):
                    if A[v, u]:
                        stack.append(u)

    # Find triangles (3-cliques)
    triangles = set()
    for i, j in edges:
        for k in range(N):
            if k != i and k != j:
                if A[i, k] and A[j, k]:
                    tri = tuple(sorted([i, j, k]))
                    triangles.add(tri)

    # b_1 = dim(H₁) = |E| - |V| + b₀ - rank_of_triangle_boundary
    # rank_of_triangle_boundary ≈ number of independent triangles
    # For simplicity: b1 ≈ |E| - N + b₀ - |T|
    # But each triangle contributes at most 1 to rank reduction

    actual_edges = len(edges)
    b1 = actual_edges - N + b0  # cyclomatic number (cycles in 1-skeleton)

    # Subtract triangles that reduce cyclomatic number
    # Each triangle = 3-cycle, if independent, reduces b1 by 1
    # But triangles can share edges. We estimate: independent triangles.
    b1 -= len(triangles)
    b1 = max(0, b1)

    return b0, b1, len(triangles)

# --- 3. Propagation simulation (DGF-style) ---
def simulate_propagation(edges, N, q0=0.95):
    """
    Simulate DGF propagation:
    - Start with fraction q0 of nodes undetermined (d=0)
    - At each step, one node with determined predecessor becomes determined
    - Continue until no more nodes can be determined
    """
    # Initial state: random q0 fraction undetermined
    determined = np.zeros(N, dtype=bool)
    undetermined_count = int(N * q0)
    undetermined_idx = np.random.choice(N, undetermined_count, replace=False)
    # determined[i] = False means undetermined

    # Build predecessor map
    preds = defaultdict(list)
    for u, v in edges:
        preds[v].append(u)

    # Set all to determined except selected ones
    determined[:] = True
    for idx in undetermined_idx:
        determined[idx] = False

    # Also mark nodes with no predecessors as determined initially
    # (they can't become determined via causal enablement alone)
    # Actually in DGF: q0 fraction are undetermined, rest are determined
    # This means a q0 fraction start at d=0

    # Propagation: activate nodes
    N_R, N_F = 0, 0
    changed = True
    step = 0
    max_steps = N * 2

    # For simplicity: alternate between checking S and E
    half = N // 2
    S_nodes = set(range(half))
    E_nodes = set(range(half, N))

    while changed and step < max_steps:
        changed = False
        step += 1

        # Check all undetermined nodes
        candidates = []
        for v in range(N):
            if not determined[v]:  # undetermined
                # Check if any predecessor is determined
                for u in preds.get(v, []):
                    if determined[u]:
                        candidates.append(v)
                        break

        if candidates:
            # Pick one at random (can be generalized)
            v = np.random.choice(candidates)
            determined[v] = True
            changed = True

            if v in S_nodes:
                N_R += 1
            else:
                N_F += 1

    return N_R, N_F

# --- 4. Reset simulation ---
def simulate_reset(edges, N, r=0.3, f_cluster=0.7, N_R=0, N_F=0):
    """
    Simulate causal-clustered reset.
    r: reset strength (fraction of edges to potentially cut)
    f_cluster: clustering factor (f_cluster<1 = enhancement, i.e. clustered survival)

    Returns: (new_edges, survival_fraction)
    """
    if len(edges) == 0:
        return [], 1.0

    A = edges_to_adj_matrix(edges, N)

    # Determine which nodes survive
    # Each node has individual survival prob = 1 - r
    # But causally connected nodes have correlated survival
    node_survives = np.zeros(N, dtype=bool)

    # Phase 1: independent baseline survival
    for i in range(N):
        node_survives[i] = np.random.random() > r

    # Phase 2: causal clustering enhancement
    # For nodes with high degree, increase survival if neighbors survive
    for _ in range(3):  # 3 rounds of reinforcement
        new_survival = node_survives.copy()
        for i in range(N):
            if not node_survives[i]:
                # Check if many neighbors survived
                neighbors = [j for j in range(N) if A[i, j]]
                if len(neighbors) > 0:
                    surviving_neighbors = sum(node_survives[j] for j in neighbors)
                    # Enhanced survival probability
                    boost = (1 - f_cluster) * surviving_neighbors / len(neighbors)
                    if np.random.random() < boost:
                        new_survival[i] = True
        node_survives = new_survival

    # Build new edges: keep only edges connecting two surviving nodes
    new_edges = [(u, v) for u, v in edges if node_survives[u] and node_survives[v]]

    # Map to new indices
    old_to_new = {}
    new_idx = 0
    for i in range(N):
        if node_survives[i]:
            old_to_new[i] = new_idx
            new_idx += 1

    mapped_edges = [(old_to_new[u], old_to_new[v]) for u, v in new_edges]
    survival_frac = new_idx / N

    return mapped_edges, survival_frac

# --- 5. Main experiment ---
def run_single_experiment(N, rho_factor, r, f_cluster, q0, seed):
    """Run one complete cycle: generate → propagate → compute b1 → reset → compute b1'"""
    np.random.seed(seed)

    # Generate
    edges, N_actual = generate_causal_dag(N, rho_factor)
    if len(edges) < 2:
        return None

    # Initial Betti
    b0_before, b1_before, tri_before = compute_clique_complex_betti(edges, N_actual)

    # Propagate
    N_R, N_F = simulate_propagation(edges, N_actual, q0)

    # Reset
    new_edges, survival_frac = simulate_reset(edges, N_actual, r, f_cluster, N_R, N_F)

    if len(new_edges) < 1:
        return {
            'b1_before': b1_before,
            'b1_after': 0,
            'r1': 0.0 if b1_before > 0 else 1.0,
            'b0_before': b0_before,
            'N': N_actual,
            'N_survive': int(N_actual * survival_frac),
            'n_edges_before': len(edges),
            'n_edges_after': len(new_edges),
            'rho_factor': rho_factor,
            'r': r,
            'f_cluster': f_cluster,
            'q0': q0,
            'seed': seed
        }

    new_N = max(old_to_new_idx for _, old_to_new_idx in
                [(0, 0)] + [(u, v) for u, v in new_edges for _ in (1,)]) if new_edges else N_actual
    # Actually recompute properly
    max_idx = 0
    for u, v in new_edges:
        max_idx = max(max_idx, u, v)
    new_N = max_idx + 1 if new_edges else 1

    b0_after, b1_after, tri_after = compute_clique_complex_betti(new_edges, new_N)

    r1 = b1_after / b1_before if b1_before > 0 else 1.0
    r1 = min(r1, 1.0)  # cap at 1 (physical bound)

    return {
        'b1_before': b1_before,
        'b1_after': b1_after,
        'r1': r1,
        'b0_before': b0_before,
        'b0_after': b0_after,
        'N': N_actual,
        'N_survive': new_N,
        'n_edges_before': len(edges),
        'n_edges_after': len(new_edges),
        'triangles_before': tri_before,
        'triangles_after': tri_after,
        'rho_factor': rho_factor,
        'r': r,
        'f_cluster': f_cluster,
        'q0': q0,
        'seed': seed
    }

# --- 6. Parameter sweep ---
def run_experiment_sweep():
    """Run full parameter sweep for Goldilocks test."""
    N = 500  # nodes per graph (reduced from 1000 for speed, scale up later)

    # Parameter grid
    rho_factors = [0.3, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0, 8.0, 12.0]
    r_values = [0.1, 0.3, 0.5, 0.7]
    f_cluster_values = [0.3, 0.5, 0.7, 1.0]  # f_cluster<1 = clustering enhancement
    q0_values = [0.9, 0.95]  # high q0 = mostly undetermined (near cycle start)
    seeds = [42, 123, 456]

    total = len(rho_factors) * len(r_values) * len(f_cluster_values) * len(q0_values) * len(seeds)
    print(f"Parameter sweep: {total} configurations")
    print(f"N={N}, rho∈{rho_factors}, r∈{r_values}, f_cluster∈{f_cluster_values}, q0∈{q0_values}")
    print("-" * 60)

    results = []
    count = 0
    skipped = 0

    for rho in rho_factors:
        for r_val in r_values:
            for fc in f_cluster_values:
                for q0 in q0_values:
                    for seed in seeds:
                        count += 1
                        res = run_single_experiment(N, rho, r_val, fc, q0, seed)
                        if res is None:
                            skipped += 1
                            continue
                        results.append(res)

                        if count % 50 == 0:
                            r1_mean = np.mean([r['r1'] for r in results[-50:]])
                            b1_mean = np.mean([r['b1_before'] for r in results[-50:]])
                            print(f"  [{count}/{total}] rho={rho:.1f} r={r_val:.1f} fc={fc:.1f} "
                                  f"| b1_before={b1_mean:.1f} r1_avg={r1_mean:.3f} | "
                                  f"skipped={skipped}")

    print(f"\nDone: {len(results)} valid / {skipped} skipped / {total} total")
    return results

def analyze_results(results):
    """Analyze Goldilocks hypothesis."""
    if not results:
        print("No results to analyze.")
        return

    print("\n" + "=" * 60)
    print("GOLDILOCKS ANALYSIS")
    print("=" * 60)

    # Group by rho_factor
    from collections import defaultdict
    by_rho = defaultdict(list)
    for res in results:
        by_rho[res['rho_factor']].append(res)

    print(f"\n{'rho':>6s} {'b1_before':>10s} {'r1_mean':>10s} {'r1_std':>8s} {'survive%':>8s}")
    print("-" * 50)

    for rho in sorted(by_rho.keys()):
        group = by_rho[rho]
        b1_before = np.mean([r['b1_before'] for r in group])
        r1_mean = np.mean([r['r1'] for r in group])
        r1_std = np.std([r['r1'] for r in group])
        survive_pct = np.mean([r['N_survive']/r['N'] for r in group]) * 100
        print(f"{rho:6.1f} {b1_before:10.2f} {r1_mean:10.4f} {r1_std:8.4f} {survive_pct:8.1f}")

    # Goldilocks: which rho gives highest b1_before?
    b1_by_rho = {rho: np.mean([r['b1_before'] for r in group])
                 for rho, group in by_rho.items()}
    best_rho = max(b1_by_rho, key=b1_by_rho.get)

    print(f"\n--- Goldilocks verdict ---")
    print(f"Peak b1 at rho/rho₀ = {best_rho:.1f} (b1 = {b1_by_rho[best_rho]:.1f})")

    # Check high-density extinction
    high_rho = max(b1_by_rho.keys())
    low_rho = min(b1_by_rho.keys())
    b1_high = b1_by_rho[high_rho]
    b1_low = b1_by_rho[low_rho]
    b1_peak = b1_by_rho[best_rho]

    print(f"b1(rho_min={low_rho:.1f}) = {b1_low:.1f}")
    print(f"b1(rho_max={high_rho:.1f}) = {b1_high:.1f}")

    if b1_peak > 2 * b1_high and b1_peak > 2 * b1_low:
        print(f"✅ Goldilocks CONFIRMED: peak b1 is > 2× low/high extremes")
    elif b1_peak > b1_high and b1_peak > b1_low:
        print(f"⚠️ Goldilocks WEAK: peak exists but ratio < 2")
    else:
        print(f"❌ Goldilocks REJECTED: no significant peak")

    # Clustering effect
    print(f"\n--- Causal clustering effect ---")
    by_fc = defaultdict(list)
    for res in results:
        by_fc[res['f_cluster']].append(res['r1'])

    for fc in sorted(by_fc.keys()):
        r1_vals = by_fc[fc]
        print(f"  f_cluster={fc:.1f}: r1 = {np.mean(r1_vals):.4f} ± {np.std(r1_vals):.4f}")

    # Key: does f_cluster < 1 (enhanced survival) increase r1?
    fc_strong = np.mean(by_fc[min(by_fc.keys())])  # strongest clustering
    fc_weak = np.mean(by_fc[max(by_fc.keys())])    # weakest clustering
    print(f"  Clustering boost: r1(fc={min(by_fc.keys()):.1f}) / r1(fc={max(by_fc.keys()):.1f}) = {fc_strong/fc_weak:.3f}")

    if fc_strong > 1.1 * fc_weak:
        print("  ✅ Causal clustering significantly enhances b1 survival")
    else:
        print("  ⚠️ Causal clustering effect weak or absent")

    return b1_by_rho

if __name__ == '__main__':
    results = run_experiment_sweep()
    analyze_results(results)

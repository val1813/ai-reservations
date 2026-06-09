"""
LP40-A: Causal Graph Renormalization Group — Numerical Implementation
======================================================================

Core question: Under coarse-graining (N^d cells → 1 effective cell),
does the causal graph flow to a d=3 isotropic continuum limit?

Experiment design:
1. Generate random causal graphs in d=2,3,4 with controlled b1 density
2. Apply iterative blocking transformation
3. Track: b1 density, q-field distribution, Laplacian spectrum
4. Extract scaling exponents and spectral dimension ds
"""

import numpy as np
from scipy import sparse
from scipy.sparse import linalg as spla
from scipy import stats
from collections import defaultdict
import warnings

# ─── 1. Causal Graph Generation ───────────────────────────────────

def generate_causal_graph(L, d, p_edge=0.3, seed=None):
    """
    Generate a random causal graph on a d-dimensional hypercubic lattice.

    Parameters
    ----------
    L : int
        Linear size (L^d nodes)
    d : int
        Spatial dimension
    p_edge : float
        Probability of a causal edge between neighbors
    seed : int or None
        Random seed

    Returns
    -------
    adj : sparse.csr_matrix (N, N)
        Adjacency matrix (directed, causal edges point from lower to higher q)
    coords : np.ndarray (N, d)
        Spatial coordinates of each node
    q_values : np.ndarray (N,)
        Initial q-field values (sampled around q_eq=0.5)
    """
    rng = np.random.default_rng(seed)
    N = L**d

    # Coordinates on a d-dimensional grid
    coords = np.array(np.meshgrid(*[np.arange(L) for _ in range(d)])).reshape(d, -1).T

    # Build adjacency: each node connects to neighbors with prob p_edge
    # Causal edges: directed from node i to j if they are neighbors
    # Convention: edge i→j means information flows i→j (i causally influences j)

    rows, cols = [], []

    for i in range(N):
        # Find spatial neighbors (within 1 step in any direction, Manhattan distance 1)
        for j in range(i+1, N):
            dist = np.sum(np.abs(coords[i] - coords[j]))
            if dist == 1:  # nearest neighbor
                if rng.random() < p_edge:
                    # Directed causal edge i->j; j->i added separately if also passes
                    if rng.random() < 0.5:
                        rows.append(i); cols.append(j)
                    if rng.random() < 0.5:
                        rows.append(j); cols.append(i)

    adj = sparse.csr_matrix(
        (np.ones(len(rows)), (rows, cols)),
        shape=(N, N)
    )

    # Initial q-field: sample around q_eq=1/2 with small fluctuations
    # q ∈ (0, 1), centered at 1/2, std ~ 0.1
    q_values = 0.5 + 0.1 * rng.normal(size=N)
    q_values = np.clip(q_values, 0.01, 0.99)

    return adj, coords, q_values


# ─── 2. Graph Analysis Tools ──────────────────────────────────────

def compute_betti_numbers(adj, k_max=2):
    """
    Compute Betti numbers b0, b1, b2 via graph Laplacian rank.

    b0 = number of connected components
    b1 = rank(nullspace of Hodge Laplacian L1)
       ≈ number of independent cycles
       For sparse graphs: b1 ≈ |E| - |V| + b0

    Uses the combinatorial formula for graphs:
    b1 = |E| - |V| + b0  (for undirected underlying graph)
    """
    N = adj.shape[0]
    # Make undirected for cycle counting
    undirected = (adj + adj.T).sign()
    E = undirected.nnz // 2
    n_components = sparse.csgraph.connected_components(undirected)[0]
    b0 = n_components
    b1 = max(0, E - N + b0)
    return b0, b1


def compute_laplacian_spectrum(adj, k=100):
    """
    Compute the first k eigenvalues of the graph Laplacian.

    Uses the combinatorial Laplacian L = D - A (undirected).
    For directed causal graphs, we analyze the undirected skeleton.
    """
    undirected = (adj + adj.T).sign()
    D = sparse.diags(np.array(undirected.sum(axis=1)).flatten())
    L = D - undirected

    # Compute k smallest eigenvalues
    if k >= L.shape[0] - 1:
        k = L.shape[0] - 2
    try:
        evals = spla.eigsh(L.astype(float), k=k, which='SM', return_eigenvectors=False)
    except:
        # Fallback: dense for small graphs
        evals = np.linalg.eigvalsh(L.toarray())[:k]
    return evals[evals > 1e-12]  # Exclude zero modes


def spectral_dimension(evals, eps=0.1):
    """
    Estimate spectral dimension ds from eigenvalue density.

    For a d-dimensional Euclidean lattice: ρ(λ) ~ λ^{d/2 - 1}
    So ds = 2 * (1 + d(log ρ)/d(log λ))

    We use the cumulative density: N(λ) ~ λ^{ds/2}
    → ds = 2 * d(log N)/d(log λ)
    """
    if len(evals) < 10:
        return np.nan

    sorted_evals = np.sort(evals)
    # Use the low-energy regime
    low_mask = sorted_evals < np.median(sorted_evals)
    if np.sum(low_mask) < 5:
        return np.nan

    log_N = np.log(np.arange(1, np.sum(low_mask)+1))
    log_lam = np.log(sorted_evals[low_mask])

    slope, _, _, _, _ = stats.linregress(log_lam[-10:], log_N[-10:])
    return max(0, 2 * slope)


def compute_q_statistics(q_values):
    """Compute statistics of q-field distribution."""
    return {
        'mean': np.mean(q_values),
        'std': np.std(q_values),
        'skew': stats.skew(q_values),
        'q_05': np.percentile(q_values, 5),
        'q_95': np.percentile(q_values, 95),
    }


# ─── 3. Blocking Transformation ───────────────────────────────────

def block_coarse_grain(adj, coords, q_values, block_size=2):
    """
    Kadanoff-style blocking: group N^d cells → 1 effective cell.

    Algorithm:
    1. Partition nodes into blocks of size block_size^d
    2. Effective q_B = mean(q_i in block)
    3. Effective adj: cells A and B connected if any node in A
       connected to any node in B (preserving direction)

    Returns: (adj_new, coords_new, q_new)
    """
    N, d = coords.shape
    # Compute block index for each node
    block_idx = np.floor(coords / block_size).astype(int)
    # Unique block identifiers
    block_ids = np.unique(block_idx, axis=0)
    n_blocks = len(block_ids)

    # Map each node to its block
    block_map = {}
    for i, bid in enumerate(map(tuple, block_ids)):
        block_map[bid] = i

    node_to_block = np.array([block_map[tuple(bid)] for bid in block_idx])

    # Compute block q-values (mean of member q-values)
    q_new = np.array([np.mean(q_values[node_to_block == b]) for b in range(n_blocks)])

    # Build block-level adjacency
    rows, cols = [], []
    adj_coo = adj.tocoo()

    for r, c in zip(adj_coo.row, adj_coo.col):
        b_r = node_to_block[r]
        b_c = node_to_block[c]
        if b_r != b_c:
            rows.append(b_r)
            cols.append(b_c)

    # Deduplicate and build sparse matrix
    if len(rows) > 0:
        data = np.ones(len(rows))
        adj_new = sparse.csr_matrix(
            (data, (rows, cols)),
            shape=(n_blocks, n_blocks)
        )
        # Remove duplicate edges (keep max weight = 1)
        adj_new.data = np.ones_like(adj_new.data)
    else:
        adj_new = sparse.csr_matrix((n_blocks, n_blocks))

    # Block coordinates (use block_ids directly as integer coordinates)
    coords_new = np.array(list(block_ids))

    return adj_new, coords_new, q_new


# ─── 4. RG Flow Experiment ────────────────────────────────────────

def run_rg_flow(L0=16, d=3, p_edge=0.3, n_iterations=4, block_size=2, seed=42):
    """
    Run full RG flow experiment.

    Parameters
    ----------
    L0 : int
        Initial linear size
    d : int
        Spatial dimension
    p_edge : float
        Edge probability
    n_iterations : int
        Number of RG steps
    block_size : int
        Block size for coarse-graining
    seed : int
        Random seed

    Returns
    -------
    results : dict
        RG flow data at each step
    """
    print(f"=== LP40-A: Causal Graph RG Flow ===")
    print(f"d={d}, L0={L0}, p_edge={p_edge}, n_iter={n_iterations}\n")

    adj, coords, q = generate_causal_graph(L0, d, p_edge, seed=seed)
    results = []

    for step in range(n_iterations):
        N = adj.shape[0]
        print(f"Step {step}: N={N}, cells")

        b0, b1 = compute_betti_numbers(adj)
        evals = compute_laplacian_spectrum(adj, k=min(100, N-2))
        ds = spectral_dimension(evals)
        q_stats = compute_q_statistics(q)

        # Edge density
        E = adj.nnz
        edge_density = E / (N * (N - 1)) if N > 1 else 0
        # b1 density (cycles per node)
        b1_density = b1 / N if N > 0 else 0

        entry = {
            'step': step,
            'N': N,
            'E': E,
            'edge_density': edge_density,
            'b0': b0,
            'b1': b1,
            'b1_density': b1_density,
            'ds': ds,
            'n_evals': len(evals),
            'q_mean': q_stats['mean'],
            'q_std': q_stats['std'],
            'q_skew': q_stats['skew'],
            'q_05': q_stats['q_05'],
            'q_95': q_stats['q_95'],
        }
        results.append(entry)

        print(f"  b0={b0}, b1={b1}, b1/N={b1_density:.4f}, "
              f"ds={ds:.2f}, q_mean={q_stats['mean']:.3f}")

        if N <= block_size**d * 2:
            print(f"  Graph too small to continue. Stopping.\n")
            break

        adj, coords, q = block_coarse_grain(adj, coords, q, block_size=block_size)

    return results


# ─── 5. Analysis ──────────────────────────────────────────────────

def analyze_flow(results, d_target=3):
    """Analyze RG flow results: scaling exponents, ds convergence."""
    steps = [r['step'] for r in results]
    Ns = np.array([r['N'] for r in results])
    b1_dens = np.array([r['b1_density'] for r in results])
    ds_vals = np.array([r['ds'] for r in results])
    q_means = np.array([r['q_mean'] for r in results])

    analysis = {'steps': len(results), 'converged_ds': None}

    print(f"\n=== Flow Analysis ===")
    print(f"Steps: {len(results)}")

    # b1 density scaling: b1/N ~ N^{-gamma}
    # If gamma > 0: b1 irrelevant in IR → continuum limit possible
    if len(Ns) >= 2:
        log_N = np.log(Ns)
        log_b1 = np.log(b1_dens + 1e-30)
        gamma, _, r, _, _ = stats.linregress(log_N, log_b1)
        analysis['b1_scaling_exponent'] = gamma
        print(f"b1 density scaling: b1/N ~ N^{-gamma:.3f} (R2={r**2:.3f})")
        if gamma > 0:
            print(f"  -> b1 IR-irrelevant (continuum limit viable)")
        else:
            print(f"  -> b1 IR-relevant WARNING (continuum limit may not exist)")

    # Spectral dimension convergence
    valid_ds = ds_vals[~np.isnan(ds_vals)]
    if len(valid_ds) >= 2:
        analysis['ds_final'] = valid_ds[-1]
        analysis['ds_initial'] = valid_ds[0]
        analysis['ds_shift'] = valid_ds[-1] - valid_ds[0]
        print(f"Spectral dimension: {valid_ds[0]:.2f} → {valid_ds[-1]:.2f}")
        print(f"  Target d={d_target}, deviation: {abs(valid_ds[-1]-d_target):.2f}")

    return analysis


# ─── 6. Multi-Dimensional Scan ────────────────────────────────────

def scan_dimensions(L0s=(16, 12, 8), dims=(2, 3, 4), p_edge=0.3, seed=42):
    """Scan across spatial dimensions d=2,3,4."""
    all_results = {}
    for d in dims:
        L0 = L0s[d-2] if isinstance(L0s, tuple) else L0s
        print(f"\n{'='*60}")
        print(f"Scanning d={d}, L0={L0}")
        print(f"{'='*60}")
        results = run_rg_flow(L0=L0, d=d, p_edge=p_edge, n_iterations=4, seed=seed+d)
        analysis = analyze_flow(results, d_target=d)
        all_results[d] = {'results': results, 'analysis': analysis}
    return all_results


# ─── Main ──────────────────────────────────────────────────────────

if __name__ == '__main__':
    warnings.filterwarnings('ignore')

    # Multi-dimensional scan
    print("LP40-A: Causal Graph RG — Multi-Dimensional Scan\n")
    all_results = scan_dimensions(L0s=(16, 12, 8), dims=(2, 3, 4), p_edge=0.7, seed=42)

    # Summary
    print(f"\n{'='*60}")
    print("FINAL SUMMARY")
    print(f"{'='*60}")
    for d, data in all_results.items():
        results = data['results']
        if len(results) >= 2:
            ds_init = results[0].get('ds', np.nan)
            ds_final = results[-1].get('ds', np.nan)
            b1_init = results[0]['b1_density']
            b1_final = results[-1]['b1_density']
            print(f"d={d}: ds {ds_init:.2f}->{ds_final:.2f}, "
                  f"b1/N {b1_init:.4f}->{b1_final:.4f}")

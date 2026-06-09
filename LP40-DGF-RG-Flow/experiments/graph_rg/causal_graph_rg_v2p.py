"""
LP40-A v0.2p: Parallel version using all CPU cores.
Each seed runs independently — trivial parallelism.
"""
import numpy as np
from scipy import sparse
from scipy.sparse import linalg as spla
from scipy import stats
import json
import os
import warnings
from datetime import datetime
from multiprocessing import Pool, cpu_count
from functools import partial

warnings.filterwarnings('ignore')

# ─── All functions identical to v0.2, just refactored for pickling ─────

def generate_lattice_graph(L, d, p_edge, seed):
    rng = np.random.default_rng(seed)
    N = L**d
    coords = np.array(np.meshgrid(*[np.arange(L) for _ in range(d)])).reshape(d, -1).T
    rows, cols = [], []
    for i in range(N):
        for j in range(i+1, N):
            if np.sum(np.abs(coords[i] - coords[j])) == 1:
                if rng.random() < p_edge:
                    if rng.random() < 0.5: rows.append(i); cols.append(j)
                    if rng.random() < 0.5: rows.append(j); cols.append(i)
    adj = sparse.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(N, N))
    q = np.clip(0.5 + 0.1 * rng.normal(size=N), 0.01, 0.99)
    return adj, coords, q

def generate_control_graph(N, avg_degree, seed):
    rng = np.random.default_rng(seed)
    p = avg_degree / (N - 1)
    rows, cols = [], []
    for i in range(N):
        for j in range(N):
            if i != j and rng.random() < p:
                if rng.random() < 0.5: rows.append(i); cols.append(j)
    adj = sparse.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(N, N))
    q = np.clip(0.5 + 0.1 * rng.normal(size=N), 0.01, 0.99)
    return adj, np.random.default_rng(seed).random((N, 3)), q

def compute_b1(adj):
    undirected = (adj + adj.T).sign()
    N = adj.shape[0]
    E = undirected.nnz // 2
    b0 = sparse.csgraph.connected_components(undirected)[0]
    return max(0, E - N + b0)

def compute_ds(adj, k=100, min_pts=20):
    undirected = (adj + adj.T).sign()
    D = sparse.diags(np.array(undirected.sum(axis=1)).flatten())
    L = D - undirected
    N = adj.shape[0]
    k_eff = min(k, N - 2)
    if k_eff < 10: return None, 0, 0
    try:
        evals = spla.eigsh(L.astype(float), k=k_eff, which='SM', return_eigenvectors=False)
    except: return None, 0, 0
    evals = evals[evals > 1e-12]
    low = evals[evals < np.median(evals)]
    if len(low) < min_pts: return None, 0, 0
    log_N = np.log(np.arange(1, len(low)+1))
    log_lam = np.log(np.sort(low))
    slope, _, r, _, _ = stats.linregress(log_lam, log_N)
    return max(0, 2*slope), r**2, len(low)

def compute_graph_stats(adj, q):
    N = adj.shape[0]; E = adj.nnz
    b0 = sparse.csgraph.connected_components((adj + adj.T).sign())[0]
    b1 = compute_b1(adj)
    ds_tup = compute_ds(adj)
    return {
        'N': N, 'E': E, 'b0': b0, 'b1': b1,
        'b1_density': b1/N if N>0 else 0,
        'ds': float(ds_tup[0]) if ds_tup[0] is not None else None,
        'ds_r2': float(ds_tup[1]), 'ds_n': ds_tup[2],
        'q_mean': float(np.mean(q)), 'q_std': float(np.std(q))
    }

def block_coarse_grain(adj, coords, q, block_size=2):
    N, d = coords.shape
    block_idx = np.floor(coords / block_size).astype(int)
    block_ids = np.unique(block_idx, axis=0)
    n_blocks = len(block_ids)
    block_map = {tuple(bid): i for i, bid in enumerate(block_ids)}
    node_to_block = np.array([block_map[tuple(bid)] for bid in block_idx])
    q_new = np.array([np.mean(q[node_to_block==b]) for b in range(n_blocks)])
    coords_new = np.array(list(block_ids))
    adj_coo = adj.tocoo(); rows, cols = [], []
    for r, c in zip(adj_coo.row, adj_coo.col):
        br, bc = node_to_block[r], node_to_block[c]
        if br != bc: rows.append(br); cols.append(bc)
    if rows:
        adj_new = sparse.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n_blocks, n_blocks))
        adj_new.data = np.ones_like(adj_new.data)
    else:
        adj_new = sparse.csr_matrix((n_blocks, n_blocks))
    return adj_new, coords_new, q_new


# ─── Single seed runner (pickleable) ──────────────────────────

def run_one_seed(args):
    """Run one RG flow. args = (d, L0, p_edge, n_steps, block_size, graph_type, seed)"""
    d, L0, p_edge, n_steps, block_size, graph_type, seed = args

    if graph_type == 'lattice':
        adj, coords, q = generate_lattice_graph(L0, d, p_edge, seed)
    else:
        adj, coords, q = generate_control_graph(L0**d, avg_degree=3*d, seed=seed)

    steps = []
    for step in range(n_steps):
        stats = compute_graph_stats(adj, q)
        stats['step'] = step; stats['seed'] = seed
        stats['d'] = d; stats['graph_type'] = graph_type
        steps.append(stats)
        if adj.shape[0] <= block_size**d + 1: break
        adj, coords, q = block_coarse_grain(adj, coords, q, block_size)
    return steps


# ─── Main ────────────────────────────────────────────────────────

def main():
    config = {
        'dims': [2, 3, 4],
        'L0s': {2: 20, 3: 14, 4: 10},
        'p_edge': 0.7,
        'n_seeds': 10,
        'n_steps': 5,
        'block_size': 2,
    }

    # Build task list
    tasks = []
    for d in config['dims']:
        L0 = config['L0s'][d]
        for s in range(config['n_seeds']):
            seed = 42 + d*100 + s
            tasks.append((d, L0, config['p_edge'], config['n_steps'],
                         config['block_size'], 'lattice', seed))
        for s in range(config['n_seeds']):
            seed = 42 + d*100 + s
            tasks.append((d, L0, config['p_edge'], config['n_steps'],
                         config['block_size'], 'control', seed))

    n_workers = min(cpu_count(), len(tasks))
    print(f"LP40-A v0.2p: {len(tasks)} tasks on {n_workers} cores")
    print(f"Config: {config}")
    print(f"{'='*60}")

    start = datetime.now()
    with Pool(n_workers) as pool:
        all_results = pool.map(run_one_seed, tasks)

    elapsed = (datetime.now() - start).total_seconds()
    print(f"\nAll done in {elapsed:.0f}s ({elapsed/60:.1f} min)")

    # Aggregate by dimension and graph type
    from collections import defaultdict
    by_key = defaultdict(list)
    for result in all_results:
        for step_data in result:
            key = (step_data['d'], step_data['graph_type'], step_data['step'])
            by_key[key].append(step_data)

    def aggregate(items):
        def stat(key):
            vals = [x[key] for x in items if x[key] is not None]
            if not vals: return {'mean': None, 'std': 0, 'n': 0}
            return {'mean': float(np.mean(vals)), 'std': float(np.std(vals)), 'n': len(vals)}
        return {'N': stat('N'), 'b1_density': stat('b1_density'),
                'ds': stat('ds'), 'q_mean': stat('q_mean'),
                'n_runs': len(items)}

    # Print summary
    print(f"\n{'='*60}")
    print("FINAL SUMMARY (mean +/- std)")
    print(f"{'='*60}")

    for d in config['dims']:
        for gtype in ['lattice', 'control']:
            print(f"\n--- d={d} [{gtype}] ---")
            for step in range(config['n_steps']):
                key = (d, gtype, step)
                if key in by_key:
                    agg = aggregate(by_key[key])
                    ds = agg['ds']
                    b1 = agg['b1_density']
                    ds_str = f"{ds['mean']:.2f}+/-{ds['std']:.2f}" if ds['mean'] else 'None'
                    print(f"  Step{step}: N={agg['N']['mean']:.0f}, n={agg['n_runs']}, "
                          f"ds={ds_str}, b1/N={b1['mean']:.3f}+/-{b1['std']:.3f}")

    # Save
    outfile = f'/d/Claude/ai-reservations/LP40-DGF-RG-Flow/experiments/graph_rg/rg_results_v2p_{datetime.now().strftime("%Y%m%d_%H%M")}.json'
    serializable = {}
    for key, items in by_key.items():
        d, gtype, step = key
        skey = f'd={d}_{gtype}_step={step}'
        agg = aggregate(items)
        # Convert numpy types
        serializable[skey] = {
            'd': d, 'graph_type': gtype, 'step': step,
            'n_runs': agg['n_runs'],
            'N': agg['N'], 'b1_density': agg['b1_density'],
            'ds': agg['ds'], 'q_mean': agg['q_mean']
        }

    with open(outfile, 'w') as f:
        json.dump({'config': config, 'elapsed_s': elapsed, 'data': serializable}, f, indent=2)
    print(f"\nSaved: {outfile}")


if __name__ == '__main__':
    main()

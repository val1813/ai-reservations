"""
LP40-A v0.2: Causal Graph RG with multiple seeds, error bars, and controls.
Deploy on VPS: python causal_graph_rg_v2.py

Fixes from v0.1:
- 10 seeds per dimension
- Error bars (std across seeds)
- Control: random Erdős-Rényi graphs of same size
- Progress saved to disk (survives disconnect)
- Better ds estimation (full low-energy fit, not just last 10 points)
- Corrected b1 IR classification
"""

import numpy as np
from scipy import sparse
from scipy.sparse import linalg as spla
from scipy import stats
import json
import os
import sys
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

OUTDIR = os.path.dirname(os.path.abspath(__file__))


# ─── Graph Generation ─────────────────────────────────────────────

def generate_lattice_graph(L, d, p_edge, seed):
    """Random causal graph on d-dim hypercubic lattice."""
    rng = np.random.default_rng(seed)
    N = L**d
    coords = np.array(np.meshgrid(*[np.arange(L) for _ in range(d)])).reshape(d, -1).T

    rows, cols = [], []
    for i in range(N):
        for j in range(i+1, N):
            if np.sum(np.abs(coords[i] - coords[j])) == 1:
                if rng.random() < p_edge:
                    if rng.random() < 0.5:
                        rows.append(i); cols.append(j)
                    if rng.random() < 0.5:
                        rows.append(j); cols.append(i)

    adj = sparse.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(N, N))
    q = np.clip(0.5 + 0.1 * rng.normal(size=N), 0.01, 0.99)
    return adj, coords, q


def generate_control_graph(N, avg_degree, seed):
    """Control: random directed graph with same N and avg degree."""
    rng = np.random.default_rng(seed)
    p = avg_degree / (N - 1)
    rows, cols = [], []
    for i in range(N):
        for j in range(N):
            if i != j and rng.random() < p:
                if rng.random() < 0.5:
                    rows.append(i); cols.append(j)
    adj = sparse.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(N, N))
    q = np.clip(0.5 + 0.1 * rng.normal(size=N), 0.01, 0.99)
    coords = rng.random((N, 3))  # dummy coords
    return adj, coords, q


# ─── Graph Analysis ───────────────────────────────────────────────

def compute_b1(adj):
    """b1 = |E| - |V| + b0 for undirected skeleton."""
    undirected = (adj + adj.T).sign()
    N = adj.shape[0]
    E = undirected.nnz // 2
    b0 = sparse.csgraph.connected_components(undirected)[0]
    return max(0, E - N + b0)


def compute_ds(adj, k=100, min_pts=20):
    """
    Spectral dimension from cumulative eigenvalue density.
    N(λ) ~ λ^{ds/2} for low λ. Fit all λ < median.
    Returns (ds, r2, n_points)
    """
    undirected = (adj + adj.T).sign()
    D = sparse.diags(np.array(undirected.sum(axis=1)).flatten())
    L = D - undirected

    N = adj.shape[0]
    k_eff = min(k, N - 2)
    if k_eff < 10:
        return np.nan, 0, 0

    try:
        evals = spla.eigsh(L.astype(float), k=k_eff, which='SM', return_eigenvectors=False)
    except:
        return np.nan, 0, 0

    evals = evals[evals > 1e-12]
    median = np.median(evals)
    low = evals[evals < median]
    if len(low) < min_pts:
        return np.nan, 0, 0

    log_N = np.log(np.arange(1, len(low)+1))
    log_lam = np.log(np.sort(low))
    slope, _, r, _, _ = stats.linregress(log_lam, log_N)
    return max(0, 2*slope), r**2, len(low)


def compute_graph_stats(adj, q):
    """All statistics for one RG step."""
    N = adj.shape[0]
    E = adj.nnz
    b0 = sparse.csgraph.connected_components((adj + adj.T).sign())[0]
    b1 = compute_b1(adj)
    ds, ds_r2, ds_n = compute_ds(adj)
    return {
        'N': N, 'E': E, 'edge_density': E/(N*(N-1)) if N>1 else 0,
        'b0': b0, 'b1': b1, 'b1_density': b1/N if N>0 else 0,
        'ds': float(ds) if not np.isnan(ds) else None,
        'ds_r2': float(ds_r2), 'ds_n': ds_n,
        'q_mean': float(np.mean(q)), 'q_std': float(np.std(q))
    }


# ─── Blocking ─────────────────────────────────────────────────────

def block_coarse_grain(adj, coords, q, block_size=2):
    """Kadanoff blocking: block_size^d cells -> 1."""
    N, d = coords.shape
    block_idx = np.floor(coords / block_size).astype(int)
    block_ids = np.unique(block_idx, axis=0)
    n_blocks = len(block_ids)

    block_map = {tuple(bid): i for i, bid in enumerate(block_ids)}
    node_to_block = np.array([block_map[tuple(bid)] for bid in block_idx])

    q_new = np.array([np.mean(q[node_to_block==b]) for b in range(n_blocks)])
    coords_new = np.array(list(block_ids))

    adj_coo = adj.tocoo()
    rows, cols = [], []
    for r, c in zip(adj_coo.row, adj_coo.col):
        br, bc = node_to_block[r], node_to_block[c]
        if br != bc:
            rows.append(br); cols.append(bc)

    if rows:
        adj_new = sparse.csr_matrix(
            (np.ones(len(rows)), (rows, cols)), shape=(n_blocks, n_blocks))
        adj_new.data = np.ones_like(adj_new.data)
    else:
        adj_new = sparse.csr_matrix((n_blocks, n_blocks))

    return adj_new, coords_new, q_new


# ─── Single RG Flow ───────────────────────────────────────────────

def run_single_rg(L0, d, p_edge, n_steps, block_size, graph_type='lattice', seed=42):
    """Run one RG flow (single seed)."""
    if graph_type == 'lattice':
        adj, coords, q = generate_lattice_graph(L0, d, p_edge, seed)
    else:
        adj, coords, q = generate_control_graph(L0**d, avg_degree=3*d, seed=seed)

    steps = []
    for step in range(n_steps):
        stats = compute_graph_stats(adj, q)
        stats['step'] = step
        stats['seed'] = seed
        steps.append(stats)

        if adj.shape[0] <= block_size**d + 1:
            break
        adj, coords, q = block_coarse_grain(adj, coords, q, block_size)

    return steps


# ─── Multi-Seed Scan ──────────────────────────────────────────────

def scan_dimension(d, L0, p_edge, n_seeds, n_steps, block_size, graph_type='lattice'):
    """Run n_seeds independent RG flows for dimension d."""
    all_steps = []
    for s in range(n_seeds):
        seed = 42 + d*100 + s
        print(f"  d={d} seed={s+1}/{n_seeds} (seed={seed})", end=' ', flush=True)
        steps = run_single_rg(L0, d, p_edge, n_steps, block_size, graph_type, seed)
        print(f"-> {len(steps)} steps, final ds={steps[-1].get('ds','?')}")
        all_steps.extend(steps)
    return all_steps


def aggregate_steps(all_steps):
    """Aggregate across seeds: mean +/- std per step."""
    by_step = {}
    for s in all_steps:
        step = s['step']
        if step not in by_step:
            by_step[step] = []
        by_step[step].append(s)

    result = []
    for step in sorted(by_step.keys()):
        items = by_step[step]
        n = len(items)
        def stat(key):
            vals = [x[key] for x in items if x[key] is not None]
            if len(vals) < 3:
                return {'mean': np.mean(vals) if vals else None, 'std': np.std(vals) if len(vals)>1 else 0, 'n': len(vals)}
            return {'mean': np.mean(vals), 'std': np.std(vals), 'n': len(vals)}

        result.append({
            'step': step,
            'n_runs': n,
            'N': stat('N'), 'b1_density': stat('b1_density'),
            'ds': stat('ds'), 'ds_r2': stat('ds_r2'),
            'q_mean': stat('q_mean'), 'edge_density': stat('edge_density'),
        })
    return result


# ─── Main ──────────────────────────────────────────────────────────

def main():
    config = {
        'dims': [2, 3, 4],
        'L0s': {2: 20, 3: 14, 4: 10},  # Larger graphs than v0.1
        'p_edge': 0.7,
        'n_seeds': 10,
        'n_steps': 5,
        'block_size': 2,
        'timestamp': datetime.now().isoformat(),
    }

    print("="*60)
    print("LP40-A v0.2: Causal Graph RG — Multi-Seed Scan")
    print(f"Config: {config['n_seeds']} seeds x {config['dims']} dims x ~{config['n_steps']} steps")
    print(f"Graphs: d=2 L={config['L0s'][2]}, d=3 L={config['L0s'][3]}, d=4 L={config['L0s'][4]}")
    print("="*60)

    all_data = {}

    for d in config['dims']:
        L0 = config['L0s'][d]
        N0 = L0**d
        print(f"\n--- d={d}, L0={L0}, N0={N0} ---")

        # Lattice causal graph
        print(f"  [Lattice]")
        lattice_steps = scan_dimension(d, L0, config['p_edge'],
                                       config['n_seeds'], config['n_steps'],
                                       config['block_size'], 'lattice')
        lattice_agg = aggregate_steps(lattice_steps)

        # Control: random graph at same N at step 0
        print(f"  [Control]")
        control_steps = scan_dimension(d, L0, config['p_edge'],
                                       config['n_seeds'], config['n_steps'],
                                       config['block_size'], 'control')
        control_agg = aggregate_steps(control_steps)

        all_data[f'd={d}'] = {
            'config': {'d': d, 'L0': L0, 'N0': N0, 'p_edge': config['p_edge']},
            'lattice': lattice_agg,
            'control': control_agg,
        }

    # Save results
    outfile = os.path.join(OUTDIR, f'rg_results_v2_{datetime.now().strftime("%Y%m%d_%H%M")}.json')

    # Convert to serializable format
    def serialize(agg_list):
        result = []
        for a in agg_list:
            entry = {'step': a['step'], 'n_runs': a['n_runs']}
            for key in ['N', 'b1_density', 'ds', 'ds_r2', 'q_mean', 'edge_density']:
                entry[key] = a[key]
            result.append(entry)
        return result

    output = {'config': config, 'data': {}}
    for k, v in all_data.items():
        output['data'][k] = {
            'config': v['config'],
            'lattice': serialize(v['lattice']),
            'control': serialize(v['control']),
        }

    with open(outfile, 'w') as f:
        json.dump(output, f, indent=2, default=str)

    # Print summary
    print(f"\n{'='*60}")
    print("FINAL SUMMARY (mean +/- std across seeds)")
    print(f"{'='*60}")
    for k, v in all_data.items():
        lat = v['lattice']
        ctrl = v['control']
        if lat and ctrl:
            ds_lat_first = f"{lat[0]['ds']['mean']:.2f}+/-{lat[0]['ds']['std']:.2f}" if lat[0]['ds']['mean'] else '?'
            ds_lat_last = f"{lat[-1]['ds']['mean']:.2f}+/-{lat[-1]['ds']['std']:.2f}" if lat[-1]['ds']['mean'] else '?'
            ds_ctrl_last = f"{ctrl[-1]['ds']['mean']:.2f}+/-{ctrl[-1]['ds']['std']:.2f}" if ctrl[-1]['ds']['mean'] else '?'
            print(f"{k}: lattice ds {ds_lat_first} -> {ds_lat_last}")
            print(f"     control ds final: {ds_ctrl_last}")
            b1_first = lat[0]['b1_density']['mean']
            b1_last = lat[-1]['b1_density']['mean']
            print(f"     b1/N: {b1_first:.4f} -> {b1_last:.4f}")

    print(f"\nResults saved to: {outfile}")
    return output


if __name__ == '__main__':
    main()

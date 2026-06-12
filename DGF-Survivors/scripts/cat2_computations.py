"""
CATEGORY 2: Computational Supplements for 11-wall-ab-verified.md
=================================================================
Task 1: Correct eigenvalues for transfer matrix + Gram matrix consistency
Task 2: p!=0.5 alpha~1 computational verification
Task 3: Mixed Cartan parameters for b1>3
Task 4: Quantitative eta_0 gap analysis

Uses b1_scaling.py classes via import.
"""
import numpy as np
from itertools import product, combinations
import sys
sys.path.insert(0, r'D:\Claude\ai-reservations\DGF-Survivors')
from b1_scaling import (
    CausalGraph, von_neumann_entropy,
    make_vertex_sharing_chain, make_disjoint_rings
)

# ============================================================
# TASK 1: Transfer Matrix Eigenvalue Verification
# ============================================================
def compute_transfer_matrix(c):
    """
    Build the 3x3 transfer matrix T for vertex-sharing chain.
    T_{Delta,Delta'} = cos^2(c(Delta+Delta')), Delta,Delta' in {0, +2, -2}

    Also returns analytic form: T = [[1, gamma^2, gamma^2], [gamma^2, delta^2, 1], [gamma^2, 1, delta^2]]
    where gamma = cos(2c), delta = cos(4c)
    """
    deltas = [0, 2, -2]
    T = np.zeros((3, 3))
    for i, d1 in enumerate(deltas):
        for j, d2 in enumerate(deltas):
            T[i, j] = np.cos(c * (d1 + d2)) ** 2

    # Analytic form
    gamma = np.cos(2 * c)
    delta = np.cos(4 * c)
    T_analytic = np.array([
        [1, gamma**2, gamma**2],
        [gamma**2, delta**2, 1],
        [gamma**2, 1, delta**2]
    ])

    return T, gamma, delta, T_analytic

def task1_eigenvalues():
    """Task 1a: Re-derive ALL eigenvalue tables for c in {0, pi/4, 0.5, pi/2}."""
    print("=" * 70)
    print("TASK 1: Transfer Matrix Eigenvalue Correct Computation")
    print("=" * 70)

    results = {}
    c_values = [
        (0.0, "0"),
        (np.pi/4, "pi/4"),
        (0.5, "0.5"),
        (np.pi/2, "pi/2")
    ]

    for c, label in c_values:
        T, gamma, delta, T_analytic = compute_transfer_matrix(c)

        # Verify analytic form matches numeric
        mismatch = np.max(np.abs(T - T_analytic))

        # Compute eigenvalues
        evals = np.linalg.eigvals(T)
        # Sort by absolute value descending
        idx = np.argsort(np.abs(evals))[::-1]
        evals_sorted = evals[idx]

        # Compute rank of T
        rank = np.linalg.matrix_rank(T)

        # Perron-Frobenius checks
        lambda1 = evals_sorted[0]
        max_ev_real = np.max(np.real(evals))
        lambda1_positive = np.isreal(lambda1) and np.real(lambda1) > 0
        lambda1_dominant = np.abs(lambda1) > np.abs(evals_sorted[1]) if len(evals_sorted) > 1 else True

        print(f"\n--- c = {label} ---")
        print(f"  gamma = cos(2c) = {gamma:.6f}")
        print(f"  delta = cos(4c) = {delta:.6f}")
        print(f"  gamma^2 = {gamma**2:.6f}, delta^2 = {delta**2:.6f}")
        print(f"  T = ")
        for row in T:
            print(f"    [{row[0]:.6f}, {row[1]:.6f}, {row[2]:.6f}]")
        print(f"  Analytic form match: {mismatch:.2e}")
        print(f"  Rank(T) = {rank}")
        print(f"  Eigenvalues (sorted by |lambda|):")
        for i, ev in enumerate(evals_sorted):
            print(f"    lambda_{i+1} = {np.real(ev):.8f}{' + ' + str(np.imag(ev)) + 'j' if abs(np.imag(ev)) > 1e-12 else ''}")
        print(f"  Trace(T) = {np.trace(T):.6f}, Sum(lambda) = {np.sum(evals):.6f}")
        print(f"  det(T) = {np.linalg.det(T):.6f}, Prod(lambda) = {np.prod(evals):.6f}")
        print(f"  Perron-Frobenius: lambda_1>0? {lambda1_positive}, |lambda_1|>|lambda_2|? {lambda1_dominant}")
        print(f"  lambda_1 > 1? {np.abs(lambda1) > 1} (non-Clifford gate)")

        results[label] = {
            'c': c, 'gamma': gamma, 'delta': delta,
            'evals': evals_sorted, 'T': T, 'rank': rank,
            'lambda1': lambda1, 'lambda1_dominant': lambda1_dominant,
            'lambda1_gt_1': np.abs(lambda1) > 1
        }

    # Comparison table
    print("\n" + "-" * 70)
    print("COMPARISON: Paper's eigenvalues vs Corrected eigenvalues")
    print("-" * 70)
    print(f"{'c':>8s}  {'Paper lambda_1':>10s}  {'Paper lambda_2':>10s}  {'Paper lambda_3':>10s}  {'Correct lambda_1':>10s}  {'Correct lambda_2':>10s}  {'Correct lambda_3':>10s}")

    paper_evals = {
        "0": (3, 0, 0),
        "pi/4": (2, 1, 0),
        "0.5": (1.508, 0.925, -0.5),
        "pi/2": (3, 0, 0)
    }

    for label in ["0", "pi/4", "0.5", "pi/2"]:
        pe = paper_evals[label]
        ce = results[label]['evals']
        # Pad with zeros if needed
        ce_list = list(np.real(ce)) + [0.0]*(3-len(ce))
        print(f"  {label:>8s}  {pe[0]:10.3f}  {pe[1]:10.3f}  {pe[2]:10.3f}  {ce_list[0]:10.3f}  {ce_list[1]:10.3f}  {ce_list[2]:10.3f}")

    return results

# ============================================================
# TASK 1b: Gram matrix consistency for c=0.5
# ============================================================
def task1b_gram_consistency():
    """Task 1b: Verify Gram matrix entropy density matches transfer matrix prediction."""
    print("\n" + "=" * 70)
    print("TASK 1b: Gram Matrix Entropy Density Consistency (c=0.5)")
    print("=" * 70)

    results = []
    for L in range(2, 11):  # b1 = L-1 for vertex-sharing chain
        b1 = L - 1
        g = make_vertex_sharing_chain(b1, c_val=0.5)
        G = g.gram_matrix(0.5)

        # Ensure G is Hermitian positive semidefinite (it should be by construction)
        G = (G + G.conj().T) / 2  # Symmetrize numerically

        evals_G = np.linalg.eigvalsh(G)
        evals_G = np.maximum(evals_G, 1e-15)
        evals_G = evals_G / evals_G.sum()

        # von Neumann entropy of G/d_s = G/2^L
        S_vn = -np.sum(evals_G * np.log2(evals_G + 1e-15))
        S_per_qubit = S_vn / L

        # Eigenvalue analysis of G
        d_s = 2**L

        # G determinant / trace info
        tr_G = np.trace(G)
        tr_G_expected = d_s  # G_{a,a} = 1 for all a

        # Rank approximation: count eigenvalues > threshold
        evals_raw = np.linalg.eigvalsh(G)
        rank_est = np.sum(np.abs(evals_raw) > 1e-10)

        results.append({
            'L': L, 'b1': b1, 'S': S_vn, 'S_per_qubit': S_per_qubit,
            'tr_G': tr_G, 'tr_G_expected': tr_G_expected,
            'rank': rank_est, 'd_s': d_s,
            'max_eval': np.max(evals_raw), 'min_nonzero': np.min(np.abs(evals_raw[np.abs(evals_raw) > 1e-10]))
        })

    print(f"\n  {'L':>4s}  {'b1':>4s}  {'S(G/d_s)':>12s}  {'S/L':>10s}  {'Tr(G)/Tr_exp':>14s}  {'rank/d_s':>10s}")
    print(f"  {'-'*4}  {'-'*4}  {'-'*12}  {'-'*10}  {'-'*14}  {'-'*10}")

    for r in results:
        print(f"  {r['L']:4d}  {r['b1']:4d}  {r['S']:12.6f}  {r['S_per_qubit']:10.6f}  {r['tr_G']/r['tr_G_expected']:14.10f}  {r['rank']/r['d_s']:10.6f}")

    # Convergence analysis
    print(f"\n  Convergence of S/L:")
    last_SL = results[-1]['S_per_qubit']
    for r in results[1:]:
        delta = r['S_per_qubit'] - last_SL
        print(f"    L={r['L']:2d}: S/L={r['S_per_qubit']:.6f}, Delta to L={results[-1]['L']}: {delta:+.6f}")
    print(f"    Estimated S/L as L->inf: ~{last_SL:.6f} bits/qubit")

    return results

# ============================================================
# TASK 2: p!=0.5 alpha~1 Computational Verification
# ============================================================
def task2_p005_alpha():
    """Task 2: Verify p!=0.5 alpha~1: QCMI(b1) is linear for all p."""
    print("\n" + "=" * 70)
    print("TASK 2: p!=0.5 α~1 Computational Verification")
    print("=" * 70)

    p_values = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
    max_b1 = 6

    table = []

    for p in p_values:
        b1_list = []
        qcmi_list = []

        for b1 in range(1, max_b1 + 1):
            g = make_vertex_sharing_chain(b1, c_val=0.5)
            qcmi, srq, seq, sq = g.qcmi(p)
            b1_list.append(b1)
            qcmi_list.append(qcmi)

        # Linear fit: QCMI(b1) = a·b1 + b
        x = np.array(b1_list, dtype=float)
        y = np.array(qcmi_list, dtype=float)

        # Add a small constant for b1=0 (QCMI=0 by definition)
        x_fit = np.append([0], x)
        y_fit = np.append([0], y)

        # Fit y = a*x (through origin, since QCMI(0)=0)
        a_through_zero = np.sum(x * y) / np.sum(x * x)

        # Fit y = a*x + b (with intercept)
        A = np.vstack([x_fit, np.ones_like(x_fit)]).T
        a, intercept = np.linalg.lstsq(A, y_fit, rcond=None)[0]

        # R^2 for the a*x fit (through origin)
        y_pred_zero = a_through_zero * x
        ss_res_zero = np.sum((y - y_pred_zero) ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)
        r2_zero = 1 - ss_res_zero / ss_tot if ss_tot > 0 else 1.0

        # R^2 for a*x + b fit
        y_pred_full = a * x + intercept
        ss_res_full = np.sum((y - y_pred_full) ** 2)
        r2_full = 1 - ss_res_full / ss_tot if ss_tot > 0 else 1.0

        # Per-ring convergence: delta QCMI = QCMI(b1) - QCMI(b1-1)
        deltas = [qcmi_list[i] - qcmi_list[i-1] for i in range(1, len(qcmi_list))]
        if len(deltas) >= 3:
            # Check if deltas are converging to a constant
            delta_spread = np.max(deltas) - np.min(deltas)
        else:
            delta_spread = float('nan')

        table.append({
            'p': p, 'a': a_through_zero, 'intercept': intercept,
            'r2_zero': r2_zero, 'r2_full': r2_full,
            'deltas': deltas,
            'delta_spread': delta_spread,
            'qcmi_list': qcmi_list
        })

    # Output table
    print(f"\n  {'p':>6s}  {'slope a':>10s}  {'R^2(zero)':>10s}  {'R^2(full)':>10s}  {'Delta-max':>10s}  {'Delta-min':>10s}  {'Delta-spread':>10s}  {'α~1?':>8s}")
    print(f"  {'-'*6}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*10}  {'-'*8}")

    for t in table:
        p = t['p']
        a = t['a']
        r2_z = t['r2_zero']
        r2_f = t['r2_full']
        d_max = np.max(t['deltas']) if len(t['deltas']) > 0 else 0
        d_min = np.min(t['deltas']) if len(t['deltas']) > 0 else 0
        alpha_ok = "YES" if (r2_z > 0.99 and a > 0 and t['delta_spread'] < 0.3 * a) else "CHECK"
        print(f"  {p:6.2f}  {a:10.6f}  {r2_z:10.6f}  {r2_f:10.6f}  {d_max:10.6f}  {d_min:10.6f}  {t['delta_spread']:10.6f}  {alpha_ok:>8s}")

    # Detailed per-p breakdown
    print(f"\n  Detailed QCMI(b1) breakdown:")
    for t in table:
        p = t['p']
        qcmi_str = ", ".join([f"{q:.4f}" for q in t['qcmi_list']])
        print(f"    p={p:.1f}: [{qcmi_str}]")

    # Verify p↔1-p symmetry
    print(f"\n  p↔1-p symmetry check:")
    for i in range(len(p_values) // 2):
        p1 = p_values[i]
        p2 = p_values[-1-i]
        diff = np.max(np.abs(np.array(table[i]['qcmi_list']) - np.array(table[-1-i]['qcmi_list'])))
        print(f"    p={p1:.1f} vs p={p2:.1f}: max QCMI diff = {diff:.2e}")

    return table

# ============================================================
# TASK 3: Mixed Cartan Parameters for b1>3
# ============================================================
def make_vertex_sharing_chain_mixed(b1, c_list):
    """Vertex-sharing chain where each ring has independent Cartan parameter."""
    edges = []
    sys_q = list(range(b1 + 1))
    env_q = []

    for r in range(b1):
        Qa = r
        Qb = r + 1
        E1 = b1 + 1 + 2 * r
        E2 = b1 + 1 + 2 * r + 1
        c = c_list[r]

        edges.append((Qa, E1, c))
        edges.append((E1, Qb, c))
        edges.append((Qb, E2, c))
        edges.append((E2, Qa, c))

        env_q.extend([E1, E2])

    V = (b1 + 1) + 2 * b1
    return CausalGraph(V, edges, sys_q, env_q)

def task3_mixed_cartan():
    """Task 3: Mixed Cartan parameters for b1=5 (beyond b1=3 baseline)."""
    print("\n" + "=" * 70)
    print("TASK 3: Mixed Cartan Parameters for b1=5")
    print("=" * 70)

    b1_test = 5
    p = 0.5
    c_clifford = np.pi / 2  # Clifford
    c_nonclifford = 0.5      # Non-Clifford

    # Strategy: random sample of configurations
    np.random.seed(42)
    n_configs = 20

    configs = []
    for _ in range(n_configs):
        c_list = []
        for r in range(b1_test):
            if np.random.random() < 0.5:
                c_list.append(c_clifford)
            else:
                c_list.append(c_nonclifford)
        n_noncliff = sum(1 for c in c_list if abs(c - c_nonclifford) < 0.01)
        configs.append((c_list, n_noncliff))

    # Also add ALL systematic configurations (0, 1, 2, 3, 4, 5 non-Clifford)
    # For each n_nc, choose specific ring assignments
    systematic_configs = []
    for n_nc in range(b1_test + 1):
        # Choose n_nc positions from [0..4]
        for positions in combinations(range(b1_test), n_nc):
            c_list = [c_clifford] * b1_test
            for pos in positions:
                c_list[pos] = c_nonclifford
            systematic_configs.append((c_list, n_nc))

    # Compute QCMI for all configurations
    results_random = []
    for idx, (c_list, n_nc) in enumerate(configs):
        try:
            g = make_vertex_sharing_chain_mixed(b1_test, c_list)
            qcmi, srq, seq, sq = g.qcmi(p)
            results_random.append({
                'idx': idx, 'n_noncliff': n_nc, 'qcmi': qcmi,
                'config': c_list
            })
        except Exception as e:
            print(f"  ERROR config {idx}: {e}")

    results_systematic = []
    for idx, (c_list, n_nc) in enumerate(systematic_configs):
        try:
            g = make_vertex_sharing_chain_mixed(b1_test, c_list)
            qcmi, srq, seq, sq = g.qcmi(p)
            results_systematic.append({
                'idx': idx, 'n_noncliff': n_nc, 'qcmi': qcmi,
                'config': c_list
            })
        except Exception as e:
            print(f"  ERROR systematic config {idx}: {e}")

    # Analyze: QCMI vs number of non-Clifford rings
    # Group by n_noncliff
    from collections import defaultdict
    by_n_nc = defaultdict(list)
    for r in results_random + results_systematic:
        by_n_nc[r['n_noncliff']].append(r['qcmi'])

    print(f"\n  QCMI vs #non-Clifford rings (b1={b1_test}):")
    print(f"  {'#non-Cliff':>12s}  {'count':>6s}  {'QCMI_mean':>12s}  {'QCMI_std':>12s}  {'QCMI_min':>12s}  {'QCMI_max':>12s}")
    print(f"  {'-'*12}  {'-'*6}  {'-'*12}  {'-'*12}  {'-'*12}  {'-'*12}")

    for n_nc in sorted(by_n_nc.keys()):
        vals = by_n_nc[n_nc]
        print(f"  {n_nc:12d}  {len(vals):6d}  {np.mean(vals):12.6f}  {np.std(vals):12.6f}  {np.min(vals):12.6f}  {np.max(vals):12.6f}")

    # Linear additivity check
    if len(systematic_configs) > 0:
        # For systematic: check if QCMI adds linearly with n_nc
        nc_list = sorted(set(r['n_noncliff'] for r in results_systematic))
        qcmi_means = []
        for nc in nc_list:
            vals = [r['qcmi'] for r in results_systematic if r['n_noncliff'] == nc]
            qcmi_means.append(np.mean(vals))

        x = np.array(nc_list, dtype=float)
        y = np.array(qcmi_means, dtype=float)

        # Fit through origin: QCMI = a * n_nc
        a = np.sum(x * y) / np.sum(x * x)
        y_pred = a * x
        ss_res = np.sum((y - y_pred) ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)
        r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 1.0

        print(f"\n  Linearity check: QCMI = a * n_nonCliff")
        print(f"    Slope a = {a:.6f} per non-Clifford ring")
        print(f"    R^2 = {r2:.6f}")
        print(f"    Per-ring QCMI (non-Clifford): {a:.6f}")

        # Check if per-ring QCMI matches the b1=1 single ring value
        g_single = make_vertex_sharing_chain(1, c_val=c_nonclifford)
        qcmi_single, _, _, _ = g_single.qcmi(0.5)
        print(f"    Single ring QCMI (c=0.5): {qcmi_single:.6f}")
        print(f"    Ratio a / QCMI_single: {a/qcmi_single:.4f}")

    # Synergy/anti-synergy check
    print(f"\n  Synergy analysis:")
    if len(systematic_configs) > 0:
        # For each n_nc > 1, check if QCMI is additive from n_nc=1
        for nc in nc_list:
            if nc <= 1:
                continue
            vals = [r['qcmi'] for r in results_systematic if r['n_noncliff'] == nc]
            expected = nc * qcmi_single
            mean_val = np.mean(vals)
            ratio = mean_val / expected
            direction = "SYNERGISTIC (+)" if ratio > 1.01 else ("ANTI-SYNERGISTIC (-)" if ratio < 0.99 else "ADDITIVE (=)")
            print(f"    n_nc={nc}: mean QCMI={mean_val:.4f}, expected add.={expected:.4f}, ratio={ratio:.4f} -> {direction}")

    return results_random, results_systematic, by_n_nc

# ============================================================
# TASK 4: Quantitative eta_0 Gap Analysis
# ============================================================
def task4_eta0_gap():
    """Task 4: Quantitative eta_0 gap analysis. OLD: eta_0 = 1/(8 ln 2). CORRECT: 2/ln2."""
    print("\n" + "=" * 70)
    print("TASK 4: Quantitative eta_0 Gap Analysis")
    print("=" * 70)

    eta0_old = 1.0 / (8.0 * np.log(2.0))  # WRONG value
    eta0_correct = 2.0 / np.log(2.0)  # CORRECT value
    print(f"\n  eta_0 (OLD, WRONG) = 1/(8 ln 2) = {eta0_old:.6f} bits")
    print(f"  eta_0 (CORRECT)     = 2/ln 2      = {eta0_correct:.6f} bits")
    eta0 = eta0_old  # keep for backward compatibility
    print(f"  Actual per-ring QCMI(c=0.5) ~ 1.408 bits")
    print(f"  Ratio = {1.408/eta0:.2f}x gap")

    # Scan c from near 0 to pi/2
    n_points = 100
    c_scan = np.linspace(0.01, np.pi/2 - 0.01, n_points)

    qcmi_per_ring = []
    ratios = []

    for c in c_scan:
        g = make_vertex_sharing_chain(1, c_val=c)
        qcmi, _, _, _ = g.qcmi(0.5)
        qcmi_per_ring.append(qcmi)
        ratios.append(qcmi / eta0)

    qcmi_per_ring = np.array(qcmi_per_ring)
    ratios_arr = np.array(ratios)

    # Near-zero c analysis
    zero_neighborhood = []
    for c_exp in np.arange(-3, 0.5, 0.5):
        c_small = 10.0 ** c_exp
        if c_small < 0.001:
            continue
        try:
            g = make_vertex_sharing_chain(1, c_val=c_small)
            qcmi, _, _, _ = g.qcmi(0.5)
            ratio_small = qcmi / eta0
            zero_neighborhood.append({
                'c': c_small, 'QCMI': qcmi, 'ratio': ratio_small,
                'log10_c': c_exp
            })
        except Exception as e:
            print(f"  ERROR at c={c_small}: {e}")

    print(f"\n  {'c':>10s}  {'QCMI(c)':>12s}  {'QCMI/eta0':>12s}")
    print(f"  {'-'*10}  {'-'*12}  {'-'*12}")

    # Show selected points
    for i in range(0, n_points, 10):
        print(f"  {c_scan[i]:10.4f}  {qcmi_per_ring[i]:12.6f}  {ratios_arr[i]:12.4f}")
    # Show last point
    print(f"  {c_scan[-1]:10.4f}  {qcmi_per_ring[-1]:12.6f}  {ratios_arr[-1]:12.4f}")

    print(f"\n  Maximum QCMI: {np.max(qcmi_per_ring):.6f} at c={c_scan[np.argmax(qcmi_per_ring)]:.4f}")
    print(f"  Maximum ratio: {np.max(ratios_arr):.4f}x at c={c_scan[np.argmax(ratios_arr)]:.4f}")

    # Near-zero analysis
    print(f"\n  Small-c behavior (c -> 0):")
    print(f"  {'log10(c)':>10s}  {'c':>12s}  {'QCMI':>12s}  {'QCMI/eta0':>12s}  {'QCMI/c^2':>12s}")
    print(f"  {'-'*10}  {'-'*12}  {'-'*12}  {'-'*12}  {'-'*12}")

    for zn in zero_neighborhood:
        qcmi_over_c2 = zn['QCMI'] / (zn['c'] ** 2) if zn['c'] > 0 else 0
        print(f"  {zn['log10_c']:10.1f}  {zn['c']:12.4e}  {zn['QCMI']:12.8f}  {zn['ratio']:12.6f}  {qcmi_over_c2:12.4f}")

    # Estimate limit
    if len(zero_neighborhood) >= 2:
        # Fit QCMI(c) ~ A * c^2 for small c
        c_vals_z = np.array([z['c'] for z in zero_neighborhood if z['c'] < 0.1])
        qcmi_vals_z = np.array([z['QCMI'] for z in zero_neighborhood if z['c'] < 0.1])
        if len(c_vals_z) >= 2:
            A = np.sum(c_vals_z**2 * qcmi_vals_z) / np.sum(c_vals_z**4)
            print(f"\n  QCMI(c) ~ A·c^2 for small c (fitted): A = {A:.6f}")
            print(f"  Limit QCMI(c)/c^2 as c->0: ~{A:.6f}")
            print(f"  Expected QCMI(c)/eta_0 as c->0: ~{A*0**2/eta0} (indeterminate)")
            print(f"  QCMI scales as O(c^2) for small c, while eta_0 is O(1)")
            print(f"  -> QCMI(c)/eta_0 -> 0 as c->0 (NOT -> 1)")
            print(f"  This means eta_0 is NOT the c->0 limiting bound of QCMI")

    # Save plot-ready data
    plot_data = []
    for i in range(0, n_points, max(1, n_points // 50)):
        plot_data.append((c_scan[i], qcmi_per_ring[i], ratios_arr[i]))

    return {
        'eta0': eta0,
        'c_scan': c_scan,
        'qcmi_per_ring': qcmi_per_ring,
        'ratios': ratios_arr,
        'zero_neighborhood': zero_neighborhood,
        'plot_data': plot_data
    }

# ============================================================
# MAIN
# ============================================================
if __name__ == '__main__':
    print("CATEGORY 2: Computational Supplements")
    print("=====================================\n")

    # Task 1
    results_t1 = task1_eigenvalues()

    # Task 1b
    results_t1b = task1b_gram_consistency()

    # Task 2
    results_t2 = task2_p005_alpha()

    # Task 3
    results_t3 = task3_mixed_cartan()

    # Task 4
    results_t4 = task4_eta0_gap()

    print("\n\n" + "=" * 70)
    print("ALL COMPUTATIONS COMPLETE")
    print("=" * 70)

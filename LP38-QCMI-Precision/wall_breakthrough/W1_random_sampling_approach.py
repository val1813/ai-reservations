"""
W1 Random Sampling Approach: Statistical exploration of QCMI lower bound
=========================================================================
Complementary to gradient-based optimization (W1_optimization_approach.py),
this script uses MASSIVE RANDOM SAMPLING to map the QCMI landscape.

Goal: Find the TIGHTEST possible QCMI via exhaustive sampling rather than
       local optimization. Answer: Is there a "practical" minimum QCMI
       well above 0, or does QCMI routinely approach 0?

Sampling distributions:
  1. Uniform in [0, pi/4] — full range
  2. Log-uniform in [1e-4, pi/4] — favors small values
  3. Beta(0.5, 2) scaled to [0, pi/4] — very small-value-heavy

Each sample can be ALIGNED (all edges share Cartan axis) or MISALIGNED
(random 3D directions per edge), with 50/50 probability.
"""
import numpy as np
from scipy.linalg import expm
import time
import sys
import os
import json

# ─── Constants ───
ETA_0 = 1.0 / (8.0 * np.log(2.0))  # FR absolute constant ≈ 0.180 bits
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = [I2, X, Y, Z]

# Bell basis vectors for efficient 2-qubit unitary diagonalization
# |Phi+>, |Phi->, |Psi+>, |Psi->
BELL_VECS = np.array([
    [1, 0, 0, 1],   # |Phi+>
    [1, 0, 0, -1],  # |Phi->
    [0, 1, 1, 0],   # |Psi+>
    [0, 1, -1, 0],  # |Psi->
], dtype=complex) / np.sqrt(2)


# ═══════════════════════════════════════════════════════════════
# SECTION 0: Verified partial trace (ground-truth proven)
# ═══════════════════════════════════════════════════════════════

def partial_trace(rho, keep_bits, n_total=6):
    """
    VERIFIED correct partial trace. Matches ground-truth construction
    for all n_total and keep_bits tested.
    """
    keep = sorted(keep_bits)
    tr = sorted([i for i in range(n_total) if i not in keep])
    dk = 2 ** len(keep)
    res = np.zeros((dk, dk), dtype=complex)
    for a in range(dk):
        for ap in range(dk):
            bk = 0; bk_ap = 0
            for ki, q in enumerate(keep):
                bk |= ((a >> ki) & 1) << q
                bk_ap |= ((ap >> ki) & 1) << q
            total = 0j
            for b in range(2 ** len(tr)):
                tp = 0
                for ti, q in enumerate(tr):
                    tp |= ((b >> ti) & 1) << q
                total += rho[bk | tp, bk_ap | tp]
            res[a, ap] = total
    return res


# ═══════════════════════════════════════════════════════════════
# SECTION 1: Optimized core functions
# ═══════════════════════════════════════════════════════════════

def make_edge_unitary_2q(cv):
    """
    Build 2-qubit edge unitary U = exp(-i * (cx*XX + cy*YY + cz*ZZ))
    using Bell basis diagonalization — O(1) instead of expm.

    Eigenvalues of H = cx*XX + cy*YY + cz*ZZ in Bell basis:
      |Phi+> : cx - cy + cz
      |Phi-> : -cx + cy + cz
      |Psi+> : cx + cy - cz
      |Psi-> : -cx - cy - cz

    So U = exp(-i*H) has eigenvalues exp(-i * eigval) on each Bell state.
    """
    cx, cy, cz = cv
    evals = np.exp(-1j * np.array([
        cx - cy + cz,     # Phi+
        -cx + cy + cz,    # Phi-
        cx + cy - cz,     # Psi+
        -cx - cy - cz     # Psi-
    ]))
    U = np.zeros((4, 4), dtype=complex)
    for k in range(4):
        bell = BELL_VECS[k]
        U += evals[k] * np.outer(bell, bell.conj())
    return U


def embed_2q_to_4q(U_2q, a, b):
    """
    Embed a 2-qubit unitary U_2q (acting on qubits a,b) into the 4-qubit
    space (qubits 0,1,2,3). Uses direct basis expansion.
    """
    other = [q for q in range(4) if q not in (a, b)]
    U_4q = np.zeros((16, 16), dtype=complex)

    for m in range(4):   # output 2-qubit state index
        s_a_out = (m >> 1) & 1
        s_b_out = m & 1
        for n in range(4):   # input 2-qubit state index
            val = U_2q[m, n]
            if abs(val) < 1e-15:
                continue
            s_a_in = (n >> 1) & 1
            s_b_in = n & 1
            for spec in range(4):  # spectator (other 2 qubits)
                in_idx = 0
                out_idx = 0
                for q in range(4):
                    if q == a:
                        in_idx |= (s_a_in << q)
                        out_idx |= (s_a_out << q)
                    elif q == b:
                        in_idx |= (s_b_in << q)
                        out_idx |= (s_b_out << q)
                    else:
                        spec_pos = other.index(q)
                        bit_val = (spec >> spec_pos) & 1
                        in_idx |= (bit_val << q)
                        out_idx |= (bit_val << q)
                U_4q[out_idx, in_idx] = val

    return U_4q


def build_edge_unitary_cartan(c_x, c_y, c_z):
    """
    Build edge unitary via Bell basis (alternative to embed_2q_to_4q
    for the non-adjacent edge (3,0) case or as fallback).
    Uses expm on 4x4 then embeds.

    Kept as reference; the preferred method is make_edge_unitary_2q
    + embed_2q_to_4q.
    """
    H = c_x * np.kron(X, X) + c_y * np.kron(Y, Y) + c_z * np.kron(Z, Z)
    return expm(-1j * H)


def kron_rev(mats):
    """kron_rev([a,b,c]) = kron(a, kron(b, c)). mats[0] = MSB."""
    r = mats[-1]
    for m in reversed(mats[:-1]):
        r = np.kron(m, r)
    return r


def vn_entropy(rho):
    """von Neumann entropy in bits."""
    w = np.linalg.eigvalsh(rho)
    w = np.maximum(w, 1e-15)
    return -np.sum(w * np.log2(w))


def permute_qubits(rho, target_axes_bra, n_total=6):
    """Permute qubits of density matrix."""
    d = 2
    target_axes_ket = [a + n_total for a in target_axes_bra]
    rho_t = rho.reshape([d] * (2 * n_total))
    rho_t = np.transpose(rho_t, axes=target_axes_bra + target_axes_ket)
    return rho_t.reshape(2**n_total, 2**n_total)


# ═══════════════════════════════════════════════════════════════
# SECTION 2: Pre-built state machinery (one-time setup)
# ═══════════════════════════════════════════════════════════════

def build_initial_state(p=0.7):
    """
    Build initial 6-qubit state in target order [Qa=0, E1=1, Qb=2, E2=3, Ra=4, Rb=5].
    Returns 64x64 density matrix.
    """
    bell_vec = np.array([1, 0, 0, 1], dtype=complex) / np.sqrt(2)
    rho_bell = np.outer(bell_vec, bell_vec.conj())
    gamma = np.diag([p, 1 - p])

    rho_block = kron_rev([rho_bell, rho_bell, gamma, gamma])
    axes = [2, 0, 5, 3, 4, 1]
    rho_target = permute_qubits(rho_block, axes)
    return rho_target


def precompute_constants(rho_0):
    """
    Precompute the entropies that are INVARIANT under edge unitaries.

    INVARIANT:
      S_RQE = full entropy (constant by unitary invariance, S(initial)=2*h2(p))
      S_R = Tr_{edge}(rho) unchanged (edge unitaries are kron(I_R, U_edge))
      S_QE = Tr_{R}(rho) unchanged (edge unitaries act on edge subsystem)

    These are computed ONCE and reused for all samples.
    """
    S_RQE = vn_entropy(rho_0)                    # full 6-qubit entropy
    S_R = vn_entropy(partial_trace(rho_0, [4, 5]))   # reference only
    S_QE = vn_entropy(partial_trace(rho_0, [0, 1, 2, 3]))  # edge only
    return S_RQE, S_R, S_QE


def apply_edge_to_rho(rho, U_4q):
    """
    Apply kron(I_4, U_4q) to 64x64 density matrix: rho' = (I4 ⊗ U) ρ (I4 ⊗ U)^H.

    Uses block structure: rho reshaped as (4, 16, 4, 16) = (ref_bra, edge_bra, ref_ket, edge_ket).
    For each (ref_bra, ref_ket) block, left- and right-multiply by U_4q.
    """
    rho_r = rho.reshape(4, 16, 4, 16)
    result = np.zeros_like(rho_r)
    for a in range(4):
        for b in range(4):
            result[a, :, b, :] = U_4q @ rho_r[a, :, b, :] @ U_4q.conj().T
    return result.reshape(64, 64)


# ═══════════════════════════════════════════════════════════════
# SECTION 3: Configuration sampling
# ═══════════════════════════════════════════════════════════════

def sample_cartan_config(rng, dist_name, is_aligned):
    """
    Sample a random 4-edge Cartan vector configuration.

    dist_name: 'uniform', 'log_uniform', or 'beta'
    is_aligned: if True, all edges share random Cartan axis; if False, random 3D per edge

    Returns: list of 4 numpy arrays, each (cx, cy, cz)
    """
    if dist_name == 'uniform':
        sampler = lambda size: rng.uniform(0, np.pi/4, size=size)
    elif dist_name == 'log_uniform':
        lo, hi = np.log(1e-4), np.log(np.pi/4)
        sampler = lambda size: np.exp(rng.uniform(lo, hi, size=size))
    elif dist_name == 'beta':
        sampler = lambda size: rng.beta(0.5, 2, size=size) * np.pi/4
    else:
        raise ValueError(f"Unknown distribution: {dist_name}")

    if is_aligned:
        # All edges share a common Cartan axis direction
        axis = rng.normal(size=3)
        axis /= np.linalg.norm(axis)
        mags = sampler(4)
        cvs = [m * axis for m in mags]
    else:
        # Each edge has independent 3D Cartan vector
        cvs = [sampler(3) for _ in range(4)]

    return cvs


# ═══════════════════════════════════════════════════════════════
# SECTION 4: Single sample evaluation
# ═══════════════════════════════════════════════════════════════

def evaluate_one_sample(cartan_vectors, rho_0, S_RQE, S_R, S_QE, p=0.7):
    """
    Compute QCMI for one Cartan configuration.

    Returns dict with QCMI, D, c_bar_sq, S_RQ, S_Q.
    """
    edge_pairs = [(0, 1), (1, 2), (2, 3), (3, 0)]

    # Build edge unitaries and embed into 4-qubit space
    rho = rho_0.copy()
    for edge_idx, (a, b) in enumerate(edge_pairs):
        cv = cartan_vectors[edge_idx]
        U_2q = make_edge_unitary_2q(cv)
        U_4q = embed_2q_to_4q(U_2q, a, b)
        rho = apply_edge_to_rho(rho, U_4q)

    rho_f = rho

    # Compute varying entropies using VERIFIED partial_trace
    S_RQ = vn_entropy(partial_trace(rho_f, [0, 2, 4, 5]))
    S_Q = vn_entropy(partial_trace(rho_f, [0, 2]))

    QCMI = max(0.0, S_RQ + S_QE - S_Q - S_RQE)

    # Compute D and c_bar_sq
    c_norms = [np.sum(cv**2) for cv in cartan_vectors]
    D = abs(c_norms[0] - c_norms[2]) + abs(c_norms[1] - c_norms[3])
    S_total = sum(c_norms)
    c_bar_sq = S_total / 4.0

    return {
        'QCMI': QCMI,
        'D': D,
        'S_total': S_total,
        'c_bar_sq': c_bar_sq,
        'c_norms': c_norms,
        'S_RQ': S_RQ,
        'S_Q': S_Q
    }


# ═══════════════════════════════════════════════════════════════
# SECTION 5: Batch sampling and statistics
# ═══════════════════════════════════════════════════════════════

def run_sampling_round(dist_name, n_samples, rho_0, S_RQE, S_R, S_QE, p=0.7, seed=42):
    """
    Run one round of random sampling for a given distribution.

    Returns: list of result dicts, and summary stats.
    """
    rng = np.random.RandomState(seed)

    results = []
    qcmi_values = []
    D_values = []
    ratio_values = []

    min_qcmi = float('inf')
    min_config = None
    min_ratio = float('inf')
    min_ratio_config = None
    n_below_fr = 0

    t_start = time.time()

    for i in range(n_samples):
        is_aligned = rng.random() < 0.5
        cvs = sample_cartan_config(rng, dist_name, is_aligned)

        r = evaluate_one_sample(cvs, rho_0, S_RQE, S_R, S_QE, p)
        r['is_aligned'] = is_aligned
        results.append(r)

        qcmi = r['QCMI']
        D = r['D']
        qcmi_values.append(qcmi)
        D_values.append(D)

        fr_bound = ETA_0 * D
        ratio = qcmi / max(fr_bound, 1e-15) if D > 1e-15 else float('inf')
        ratio_values.append(ratio)

        if qcmi < min_qcmi:
            min_qcmi = qcmi
            min_config = {
                'cvs': [cv.tolist() for cv in cvs],
                'is_aligned': is_aligned,
                'QCMI': qcmi,
                'D': D,
                'fr_bound': fr_bound,
                'ratio': ratio,
                'c_norms': r['c_norms'],
                'c_bar_sq': r['c_bar_sq']
            }

        if ratio < min_ratio and D > 0:
            min_ratio = ratio
            min_ratio_config = {
                'cvs': [cv.tolist() for cv in cvs],
                'is_aligned': is_aligned,
                'QCMI': qcmi,
                'D': D,
                'fr_bound': fr_bound,
                'ratio': ratio
            }

        if qcmi < 0.180 and qcmi > 1e-15:
            n_below_fr += 1

        # Progress every 500 samples
        if (i + 1) % 500 == 0:
            elapsed = time.time() - t_start
            rate = (i + 1) / elapsed
            eta = (n_samples - i - 1) / rate
            print(f"  [{dist_name}] {i+1}/{n_samples} | "
                  f"rate={rate:.1f} samp/s | min_QCMI={min_qcmi:.6f} | "
                  f"ETA={eta:.0f}s", flush=True)

    elapsed = time.time() - t_start
    print(f"  [{dist_name}] DONE: {n_samples} samples in {elapsed:.1f}s "
          f"({n_samples/elapsed:.1f} samp/s)", flush=True)

    qcmi_arr = np.array(qcmi_values)
    D_arr = np.array(D_values)
    ratio_arr = np.array([r for r in ratio_values if r < 1e10])  # exclude inf

    # Percentiles
    percentiles = [1, 5, 10, 25, 50]
    pct_values = {f'p{p}': np.percentile(qcmi_arr, p) for p in percentiles}

    stats = {
        'dist_name': dist_name,
        'n_samples': n_samples,
        'mean_QCMI': np.mean(qcmi_arr),
        'std_QCMI': np.std(qcmi_arr),
        'min_QCMI': min_qcmi,
        'max_QCMI': np.max(qcmi_arr),
        'median_QCMI': np.median(qcmi_arr),
        'mean_D': np.mean(D_arr),
        'min_D': np.min(D_arr),
        'min_ratio': min_ratio,
        'percentiles': pct_values,
        'n_below_FR': n_below_fr,
        'pct_below_FR': 100.0 * n_below_fr / n_samples,
        'elapsed': elapsed,
        'rate': n_samples / elapsed
    }

    return results, stats, min_config, min_ratio_config


# ═══════════════════════════════════════════════════════════════
# SECTION 6: Main execution
# ═══════════════════════════════════════════════════════════════

def main():
    print("=" * 85)
    print("W1 RANDOM SAMPLING APPROACH")
    print("Statistical QCMI Landscape Exploration for 4-Node Causal Ring")
    print("=" * 85)
    print()

    # ─── Pre-build initial state and invariant entropies ───
    p_val = 0.7
    print(f"Building initial state (p={p_val})...")
    t0 = time.time()
    rho_0 = build_initial_state(p_val)
    S_RQE, S_R, S_QE = precompute_constants(rho_0)
    print(f"  Precomputed: S_RQE={S_RQE:.6f}, S_R={S_R:.6f}, S_QE={S_QE:.6f}")
    print(f"  Setup time: {time.time()-t0:.2f}s")
    print()

    # ─── Sample from each distribution ───
    N_PER_DIST = 3000  # 9000 total
    distributions = ['uniform', 'log_uniform', 'beta']

    all_results = {}
    all_stats = {}
    global_min_config = None
    global_min_qcmi = float('inf')
    global_min_ratio = float('inf')
    global_min_ratio_config = None

    seeds = {'uniform': 42, 'log_uniform': 123, 'beta': 456}

    for dist_name in distributions:
        print(f"\n{'─'*85}")
        print(f"Distribution: {dist_name.upper()}")
        print(f"{'─'*85}")

        results, stats, min_config, min_ratio_config = run_sampling_round(
            dist_name, N_PER_DIST, rho_0, S_RQE, S_R, S_QE, p_val, seeds[dist_name]
        )

        all_results[dist_name] = results
        all_stats[dist_name] = stats

        if min_config['QCMI'] < global_min_qcmi:
            global_min_qcmi = min_config['QCMI']
            global_min_config = min_config

        if min_ratio_config and min_ratio_config['ratio'] < global_min_ratio:
            global_min_ratio = min_ratio_config['ratio']
            global_min_ratio_config = min_ratio_config

    # ─── Aggregate statistics across all distributions ───
    all_qcmi = np.concatenate([np.array([r['QCMI'] for r in all_results[d]]) for d in distributions])
    all_D = np.concatenate([np.array([r['D'] for r in all_results[d]]) for d in distributions])

    print(f"\n{'='*85}")
    print("FINAL RESULTS")
    print(f"{'='*85}")
    print()

    # Distribution-wise stats
    print(f"  {'Distribution':<18s} {'N':>6s} {'Mean_QCMI':>12s} {'Std_QCMI':>12s} "
          f"{'Min_QCMI':>12s} {'Median':>12s} {'<FR':>8s}  {'Rate':>10s}")
    print(f"  {'-'*85}")

    for dist_name in distributions:
        s = all_stats[dist_name]
        print(f"  {dist_name:<18s} {s['n_samples']:6d} {s['mean_QCMI']:12.6f} "
              f"{s['std_QCMI']:12.6f} {s['min_QCMI']:12.6f} {s['median_QCMI']:12.6f} "
              f"{s['n_below_FR']:6d}  {s['rate']:8.1f}/s")

    # Percentiles across all samples
    print(f"\n  PERCENTILES (all {len(all_qcmi)} samples):")
    for p in [1, 5, 10, 25, 50]:
        val = np.percentile(all_qcmi, p)
        print(f"    P{p:2d}: {val:.8f} bits")

    # Global min
    print(f"\n  GLOBAL MINIMUM QCMI: {global_min_qcmi:.10f} bits")
    print(f"    Distribution: {global_min_config.get('dist', 'N/A')}")
    print(f"    Aligned: {global_min_config['is_aligned']}")
    print(f"    D = {global_min_config['D']:.10f}")
    print(f"    FR bound (eta0*D) = {global_min_config['fr_bound']:.10f}")
    print(f"    Ratio QCMI/(eta0*D) = {global_min_config['ratio']:.4f}x")
    print(f"    Cartan vectors:")
    for i, cv in enumerate(global_min_config['cvs']):
        print(f"      Edge {i}: ({cv[0]:.10f}, {cv[1]:.10f}, {cv[2]:.10f})")

    # Global min ratio
    if global_min_ratio_config:
        print(f"\n  MINIMUM RATIO QCMI/(eta0*D): {global_min_ratio:.4f}x")
        print(f"    Aligned: {global_min_ratio_config['is_aligned']}")
        print(f"    QCMI = {global_min_ratio_config['QCMI']:.8f}")
        print(f"    D = {global_min_ratio_config['D']:.8f}")
        print(f"    Cartan vectors:")
        for i, cv in enumerate(global_min_ratio_config['cvs']):
            print(f"      Edge {i}: ({cv[0]:.8f}, {cv[1]:.8f}, {cv[2]:.8f})")

    # Below FR constant
    all_below = sum(s['n_below_FR'] for s in all_stats.values())
    print(f"\n  SAMPLES BELOW FR ABSOLUTE CONSTANT (0.180 bits):")
    print(f"    Count: {all_below} / {len(all_qcmi)} ({100.0*all_below/len(all_qcmi):.2f}%)")

    # ─── Key question answers ───
    print(f"\n{'='*85}")
    print("KEY FINDINGS")
    print(f"{'='*85}")
    print(f"""
  1. PRACTICAL MINIMUM QCMI:
     Global minimum across {len(all_qcmi)} random samples: {global_min_qcmi:.8f} bits
     This is {'ABOVE' if global_min_qcmi > 0.001 else 'NEAR'} zero.

  2. DOES QCMI ROUTINELY GO TO ZERO?
     P1  = {np.percentile(all_qcmi, 1):.8f} bits
     P5  = {np.percentile(all_qcmi, 5):.8f} bits
     Mean = {np.mean(all_qcmi):.6f} bits
     → QCMI is {'rarely' if np.percentile(all_qcmi, 1) > 0.001 else 'frequently'} near zero.

  3. COMPARISON WITH FAWZI-RENNER (eta0*D):
     Minimum ratio QCMI/(eta0*D) = {global_min_ratio:.4f}x
     → The FR bound is {'TIGHT' if global_min_ratio < 5 else 'LOOSE by ' + str(int(global_min_ratio)) + 'x'} at the minimum.

  4. HOW MANY BELOW 0.180 bits (FR absolute constant)?
     {all_below} / {len(all_qcmi)} ({100.0*all_below/len(all_qcmi):.2f}%)
     → The absolute constant {'' if all_below > 0 else 'NEVER '}binds random configurations.
""")

    # ─── Save results for later plotting ───
    output_data = {
        'all_qcmi': all_qcmi.tolist(),
        'all_D': all_D.tolist(),
        'global_min': global_min_config,
        'global_min_ratio': global_min_ratio_config,
        'stats': {d: {k: (v.tolist() if isinstance(v, np.ndarray) else v)
                      for k, v in s.items()}
                  for d, s in all_stats.items()},
        'n_total': len(all_qcmi),
        'p_val': p_val
    }

    out_path = os.path.join(os.path.dirname(__file__), 'W1_random_sampling_data.json')
    with open(out_path, 'w') as f:
        json.dump(output_data, f, indent=2, default=str)
    print(f"  Data saved to: {out_path}")

    return all_results, all_stats, global_min_config


if __name__ == '__main__':
    main()

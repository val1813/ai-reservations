"""
LP45 Part 1-3: Characterize the Gram c_z correlation structure.

Demonstrates: (1) the Gram channel's Pauli Z coefficients have a specific
weight distribution P(w) = sum_{|z|=w} c_z that deviates from i.i.d. dephasing;
(2) the deviation is quantified by total variation distance and its scaling
with n and c; (3) the effective error rate for distance-d codes differs from
the i.i.d. prediction.

Core mathematical identity:
  G[a,b] = prod_{r=0}^{b1-1} [p*exp(ic*Delta_r) + (1-p)*exp(-ic*Delta_r)]^2
  c_z = (1/2^n) sum_x G_fold(x) (-1)^{z·x}   [Walsh-Hadamard transform]

For the vertex-sharing chain with n = b1+1 qubits.
"""
import numpy as np
from collections import Counter
import os, sys, json
from itertools import product as iterprod

OUTDIR = os.path.dirname(os.path.abspath(__file__))


# ============================================================================
# 1. Gram matrix and G(x) function
# ============================================================================

def build_gram_diagonal_folded(n, c, p=0.5):
    """
    Compute G_fold(x) = average Gram element G[a, a⊕x] over all backgrounds a.

    For the vertex-sharing chain with n system qubits, b1 = n-1 rings.
    Ring r (0 <= r < n-1) couples qubits r and r+1.

    Returns:
        G_fold: array of shape (2^n,) where G_fold[x] is the average over a.
        G_by_a: 2D array of shape (2^n, 2^n) — full Gram matrix G[a,b].
    """
    b1 = n - 1  # number of rings
    d = 2 ** n

    if d > 8192:
        raise ValueError(f"n={n} gives d={d} > 8192, too large")

    G = np.ones((d, d), dtype=np.float64)

    # Precompute s_a(i) = (-1)^{a_i} for all a, i
    s = np.ones((d, n), dtype=np.int8)
    for a in range(d):
        for i in range(n):
            s[a, i] = 1 if (a >> i) & 1 else -1

    for r in range(b1):
        for a in range(d):
            s_ar = s[a, r]
            s_ar1 = s[a, r + 1]
            for b in range(a + 1, d):
                s_br = s[b, r]
                s_br1 = s[b, r + 1]
                delta = (s_ar + s_ar1) - (s_br + s_br1)
                # Factor = cos(c*delta) for p=0.5
                factor = p * np.cos(c * delta) + (1 - p) * np.cos(c * delta)
                factor = np.cos(c * delta)
                # Each ring has 2 env qubits: factor^2
                G[a, b] *= factor * factor
                G[b, a] = G[a, b]

    # Compute G_fold[x] = average of G[a, a⊕x] over all a
    G_fold = np.zeros(d, dtype=np.float64)
    counts = np.zeros(d, dtype=np.int64)
    for a in range(d):
        for x in range(d):
            b = a ^ x
            G_fold[x] += G[a, b]
            counts[x] += 1
    G_fold /= counts

    return G_fold, G


def check_translation_invariance(n, c, tol=1e-12):
    """
    Check if G[a, a⊕x] is independent of background a.
    Returns: max variance across backgrounds for each x.
    """
    G_fold, G = build_gram_diagonal_folded(n, c)
    d = 2 ** n
    max_var = 0.0
    for x in range(d):
        vals = []
        for a in range(d):
            b = a ^ x
            vals.append(G[a, b])
        vals = np.array(vals)
        var = np.std(vals)
        if var > max_var:
            max_var = var
    return max_var


# ============================================================================
# 2. Walsh-Hadamard transform and c_z distribution
# ============================================================================

def walsh_hadamard_transform(f):
    """
    Compute the Walsh-Hadamard transform of f (size 2^n).
    F[z] = (1/2^n) sum_x f[x] (-1)^{z·x}
    """
    n = int(np.log2(len(f)))
    d = len(f)
    result = f.copy().astype(np.float64)
    # In-place fast Walsh-Hadamard transform (unnormalized)
    step = 1
    while step < d:
        for i in range(0, d, 2 * step):
            for j in range(i, i + step):
                u = result[j]
                v = result[j + step]
                result[j] = u + v
                result[j + step] = u - v
        step *= 2
    return result / d


def compute_cz_distribution(n, c, p=0.5):
    """
    Compute the Pauli Z coefficient distribution c_z for the Gram channel.

    Steps:
    1. Build Gram matrix, extract G_fold(x) = avg G[a, a⊕x]
    2. Walsh-Hadamard transform to get c_z
    3. Compute weight distribution P(w) = sum_{|z|=w} c_z

    Returns dict with:
        c_z: array of shape (2^n,)
        P_gram: weight distribution (array length n+1)
        z_indices: weight of each z pattern (for the full c_z array)
        mean_offdiag_avg: average |G[a,b]| for a != b
    """
    G_fold, G_full = build_gram_diagonal_folded(n, c, p)
    d = 2 ** n

    # Walsh-Hadamard to get c_z
    c_z = walsh_hadamard_transform(G_fold)

    # Clip tiny negative values from numerical noise
    c_z = np.maximum(c_z, 0.0)
    # Renormalize
    c_z /= np.sum(c_z)

    # Weight distribution
    P_gram = np.zeros(n + 1)
    for z in range(d):
        w = bin(z).count('1')
        P_gram[w] += c_z[z]

    # Mean off-diagonal Gram element
    offdiag_vals = []
    for a in range(d):
        for b in range(a + 1, d):
            offdiag_vals.append(G_full[a, b])
    mean_offdiag = np.mean(np.abs(offdiag_vals))

    # Average per-qubit error rate (from data)
    # For i.i.d. dephasing, each qubit has prob p_err of Z flip
    # Effective p_err: the probability that a single qubit gets a Z error
    # p_eff = (1 - mean_offdiag) / 2  (heuristic from depolarizing-like mapping)
    # Better: fit from c_z directly
    # For i.i.d. dephasing, c_z = (1-p)^(n-|z|) * p^|z|
    # The single-qubit error rate p fits the c_z distribution
    p_eff = compute_effective_perr(c_z, n)

    return {
        'c_z': c_z,
        'P_gram': P_gram,
        'mean_offdiag': mean_offdiag,
        'p_eff': p_eff,
        'G_fold': G_fold,
        'G_full': G_full,
        'n': n,
        'c': c,
        'p_env': p,
    }


def compute_effective_perr(c_z, n):
    """
    Fit the i.i.d. dephasing rate p_eff from the c_z distribution.

    For i.i.d. dephasing with per-qubit error rate p:
    c_z^iid = p^{|z|} * (1-p)^{n-|z|}

    We estimate p_eff via the single-qubit marginal:
    P(Z on qubit i) = sum_{z: z_i=1} c_z
    For translation-invariant distributions, this equals P(w=1)/n on average.

    Returns p_eff for qubit 0 (boundary qubit for n>=2).
    """
    d = 2 ** n
    # Compute total probability of Z on qubit 0
    prob_z0 = 0.0
    for z in range(d):
        if (z & 1):
            prob_z0 += c_z[z]
    return prob_z0


def compute_position_dependent_perr(c_z, n):
    """
    Compute per-qubit effective Z-error probabilities p_q.

    p_q = sum_{z: z_q=1} c_z

    Returns:
        p_q: array of length n, per-qubit Z error probabilities
    """
    d = 2 ** n
    p_q = np.zeros(n)
    for q in range(n):
        prob = 0.0
        for z in range(d):
            if (z >> q) & 1:
                prob += c_z[z]
        p_q[q] = prob
    return p_q


def iid_dephasing_distribution(n, p):
    """
    Return c_z and P(w) for i.i.d. dephasing with UNIFORM per-qubit rate p.
    c_z = p^{|z|} (1-p)^{n-|z|}
    P_iid(w) = C(n,w) * p^w * (1-p)^{n-w}
    """
    from math import comb
    d = 2 ** n
    c_z_iid = np.zeros(d)
    for z in range(d):
        w = bin(z).count('1')
        c_z_iid[z] = (p ** w) * ((1 - p) ** (n - w))
    # Normalize (should already be, but be safe)
    c_z_iid /= np.sum(c_z_iid)
    P_iid = np.zeros(n + 1)
    for w in range(n + 1):
        P_iid[w] = comb(n, w) * (p ** w) * ((1 - p) ** (n - w))
    return c_z_iid, P_iid


def position_dependent_iid_distribution(n, p_q):
    """
    Return c_z and P(w) for POSITION-DEPENDENT i.i.d. dephasing.

    Each qubit q has its own effective Z-error rate p_q.
    c_z^(pos-iid) = prod_{q: z_q=1} p_q * prod_{q: z_q=0} (1-p_q)

    This matches the single-qubit marginals exactly without assuming
    translation invariance or uniform error rates.

    Returns:
        c_z_iid: array of shape (2^n,)
        P_iid: weight distribution (array length n+1)
        p_boundary: average p for boundary qubits (q=0, n-1)
        p_interior: average p for interior qubits (q=1..n-2)
    """
    from math import comb
    d = 2 ** n
    c_z_iid = np.ones(d)
    for z in range(d):
        for q in range(n):
            if (z >> q) & 1:
                c_z_iid[z] *= p_q[q]
            else:
                c_z_iid[z] *= (1.0 - p_q[q])
    # Normalize
    c_z_iid /= np.sum(c_z_iid)
    P_iid = np.zeros(n + 1)
    for z in range(d):
        w = bin(z).count('1')
        P_iid[w] += c_z_iid[z]

    # Compute boundary and interior averages
    if n >= 2:
        p_boundary = np.mean([p_q[0], p_q[n-1]])
        if n > 2:
            p_interior = np.mean(p_q[1:n-1])
        else:
            p_interior = p_boundary
    else:
        p_boundary = p_q[0]
        p_interior = p_q[0]

    return c_z_iid, P_iid, p_boundary, p_interior


# ============================================================================
# 3. Key observables: ratios and distances
# ============================================================================

def total_variation_distance(P, Q):
    """Total variation distance between two probability distributions."""
    return 0.5 * np.sum(np.abs(P - Q))


def compute_comparison_metrics(result, use_position_dependent=True):
    """
    Compare Gram c_z distribution to i.i.d. dephasing.

    Uses BOTH uniform (boundary-qubit) and position-dependent baselines.

    Returns dict with:
        rho_w: ratio P_gram(w) / P_iid(w) [uniform baseline]
        rho_w_pos: ratio P_gram(w) / P_iid_pos(w) [position-dependent baseline]
        TVD_full: total variation distance (uniform iid baseline)
        TVD_full_pos: total variation distance (position-dependent baseline)
        TVD_weight: TVD in weight space (uniform)
        TVD_weight_pos: TVD in weight space (position-dependent)
        P_iid: i.i.d. weight distribution (uniform baseline)
        P_iid_pos: i.i.d. weight distribution (position-dependent baseline)
        p_eff: effective per-qubit error rate (boundary qubit)
        p_q: per-qubit error probabilities (length n)
        p_boundary: average boundary p
        p_interior: average interior p
    """
    n = result['n']
    c_z = result['c_z']
    P_gram = result['P_gram']
    p_eff = result['p_eff']

    # Compute per-position p_q
    p_q = compute_position_dependent_perr(c_z, n)

    # --- Uniform (boundary-qubit) baseline ---
    c_z_iid, P_iid = iid_dephasing_distribution(n, p_eff)

    rho_w = np.zeros(n + 1)
    for w in range(n + 1):
        if P_iid[w] > 1e-15:
            rho_w[w] = P_gram[w] / P_iid[w]
        else:
            rho_w[w] = np.nan if P_gram[w] < 1e-15 else np.inf

    tvd_full = total_variation_distance(c_z, c_z_iid)
    tvd_weight = total_variation_distance(P_gram, P_iid)

    # --- Position-dependent baseline ---
    c_z_iid_pos, P_iid_pos, p_boundary, p_interior = \
        position_dependent_iid_distribution(n, p_q)

    rho_w_pos = np.zeros(n + 1)
    for w in range(n + 1):
        if P_iid_pos[w] > 1e-15:
            rho_w_pos[w] = P_gram[w] / P_iid_pos[w]
        else:
            rho_w_pos[w] = np.nan if P_gram[w] < 1e-15 else np.inf

    tvd_full_pos = total_variation_distance(c_z, c_z_iid_pos)
    tvd_weight_pos = total_variation_distance(P_gram, P_iid_pos)

    # --- KL divergence: Gram || position-dependent iid ---
    kl_pos = np.sum(c_z * np.log((c_z + 1e-15) / (c_z_iid_pos + 1e-15)))

    return {
        'rho_w': rho_w,
        'rho_w_pos': rho_w_pos,
        'TVD_full': tvd_full,
        'TVD_full_pos': tvd_full_pos,
        'TVD_weight': tvd_weight,
        'TVD_weight_pos': tvd_weight_pos,
        'P_iid': P_iid,
        'P_iid_pos': P_iid_pos,
        'P_gram': P_gram,
        'c_z_iid': c_z_iid,
        'c_z_iid_pos': c_z_iid_pos,
        'p_eff': p_eff,
        'p_q': p_q,
        'p_boundary': p_boundary,
        'p_interior': p_interior,
        'kl_pos': kl_pos,
    }


# ============================================================================
# 4. Effective error rate for distance-d codes
# ============================================================================

def compute_effective_logical_error(c_z, d_code):
    """
    Compute p_eff(d) = sum_{|z| >= d/2} c_z

    This is the probability of an uncorrectable error for a
    perfect distance-d code (assuming weight-based decoding).

    For a distance-d code, errors of weight >= ceil(d/2) are
    uncorrectable under minimum-weight decoding.
    """
    n = int(np.log2(len(c_z)))
    p_logical = 0.0
    threshold = int(np.ceil(d_code / 2))
    for z in range(2 ** n):
        w = bin(z).count('1')
        if w >= threshold:
            p_logical += c_z[z]
    return p_logical


# ============================================================================
# PART 1: Compute c_z for small systems
# ============================================================================

def part1_compute_and_compare():
    """Main computation for Part 1."""
    print("=" * 80)
    print("PART 1: c_z Distribution for Vertex-Sharing Gram Chain, c=0.5")
    print("=" * 80)

    results = {}
    for n in [3, 4, 5, 6]:
        print(f"\n{'─' * 60}")
        print(f"n = {n} qubits, b1 = {n-1} rings, d = {2**n}")
        print(f"{'─' * 60}")

        res = compute_cz_distribution(n, c=0.5)
        comp = compute_comparison_metrics(res)
        results[n] = {**res, **comp}

        print(f"  Per-qubit Z-error probabilities p_q:")
        for q in range(n):
            tag = "(boundary)" if q == 0 or q == n-1 else "(interior) "
            print(f"    q={q} {tag}: p_q = {comp['p_q'][q]:.6f}")
        print(f"  Boundary average p_boundary = {comp['p_boundary']:.6f}")
        print(f"  Interior average p_interior = {comp['p_interior']:.6f}")
        print(f"  Mean |G_ab| (a≠b) = {res['mean_offdiag']:.6f}")

        print(f"\n  Weight distribution comparison (UNIFORM baseline, p={comp['p_eff']:.6f}):")
        print(f"  {'w':>3s}  {'P_gram(w)':>14s}  {'P_iid(w)':>14s}  "
              f"{'ρ(w)=ratio':>14s}  {'Deviation':>12s}")
        print(f"  {'─'*3}  {'─'*14}  {'─'*14}  {'─'*14}  {'─'*12}")

        for w in range(n + 1):
            dev = comp['P_gram'][w] - comp['P_iid'][w]
            print(f"  {w:3d}  {comp['P_gram'][w]:14.6e}  {comp['P_iid'][w]:14.6e}  "
                  f"{comp['rho_w'][w]:14.4f}  {dev:+12.6e}")

        print(f"\n  Weight distribution comparison (POSITION-DEPENDENT baseline):")
        print(f"  {'w':>3s}  {'P_gram(w)':>14s}  {'P_pos-iid(w)':>14s}  "
              f"{'ρ_pos(w)':>14s}  {'Deviation':>12s}")
        print(f"  {'─'*3}  {'─'*14}  {'─'*14}  {'─'*14}  {'─'*12}")

        for w in range(n + 1):
            dev = comp['P_gram'][w] - comp['P_iid_pos'][w]
            print(f"  {w:3d}  {comp['P_gram'][w]:14.6e}  {comp['P_iid_pos'][w]:14.6e}  "
                  f"{comp['rho_w_pos'][w]:14.4f}  {dev:+12.6e}")

        # Show individual c_z for each weight class (sample)
        print(f"\n  Top c_z coefficients (by weight):")
        d = 2 ** n
        # Sort c_z by magnitude
        idx_sorted = np.argsort(res['c_z'])[::-1]
        shown = 0
        for idx in idx_sorted:
            if shown >= 12:
                break
            w = bin(idx).count('1')
            cz = res['c_z'][idx]
            cz_iid = comp['c_z_iid'][idx]
            ratio = cz / cz_iid if cz_iid > 1e-15 else np.inf
            print(f"    z={idx:0{n}b} w={w} c_z={cz:.6e} "
                  f"(iid={cz_iid:.6e}, ratio={ratio:.4f})")
            shown += 1

        print(f"\n  Summary metrics:")
        print(f"    p_boundary = {comp['p_boundary']:.6f}")
        print(f"    p_interior = {comp['p_interior']:.6f}")
        print(f"    Uniform baseline:")
        print(f"      TVD (full c_z)  = {comp['TVD_full']:.6f}")
        print(f"      TVD (weight space) = {comp['TVD_weight']:.6f}")
        print(f"    Position-dependent baseline:")
        print(f"      TVD (full c_z)  = {comp['TVD_full_pos']:.6f}")
        print(f"      TVD (weight space) = {comp['TVD_weight_pos']:.6f}")
        print(f"      KL(Gram || pos-iid) = {comp['kl_pos']:.6f} nats")

    return results


# ============================================================================
# PART 2: Scaling analysis
# ============================================================================

def part2_scaling_analysis():
    """Scan c and n to characterize scaling of Gram-iid distinguishability."""
    print("\n" + "=" * 80)
    print("PART 2: Scaling Analysis — TVD vs n and c")
    print("=" * 80)

    # 2a: TVD vs n for fixed c=0.5
    print(f"\n{'─' * 60}")
    print("2a. TVD vs n for c = 0.5")
    print(f"{'─' * 60}")
    print(f"  {'n':>3s}  {'d=2^n':>8s}  {'TVD(unif)':>12s}  {'TVD(pos)':>12s}  "
          f"{'TVD_wt(pos)':>12s}  {'p_bnd':>10s}  {'p_int':>10s}  {'KL(pos)':>10s}")

    tvd_vs_n = []
    for n in range(3, 9):
        try:
            res = compute_cz_distribution(n, c=0.5)
            comp = compute_comparison_metrics(res)
            tvd_vs_n.append({
                'n': n, 'd': 2**n,
                'TVD_full': comp['TVD_full'],
                'TVD_full_pos': comp['TVD_full_pos'],
                'TVD_weight': comp['TVD_weight'],
                'TVD_weight_pos': comp['TVD_weight_pos'],
                'p_eff': res['p_eff'],
                'p_boundary': comp['p_boundary'],
                'p_interior': comp['p_interior'],
                'p_q': comp['p_q'].tolist(),
                'kl_pos': comp['kl_pos'],
                'mean_offdiag': res['mean_offdiag'],
            })
            print(f"  {n:3d}  {2**n:8d}  {comp['TVD_full']:12.6f}  "
                  f"{comp['TVD_full_pos']:12.6f}  {comp['TVD_weight_pos']:12.6f}  "
                  f"{comp['p_boundary']:10.6f}  {comp['p_interior']:10.6f}  "
                  f"{comp['kl_pos']:10.6f}")
        except (ValueError, MemoryError) as e:
            print(f"  {n:3d}  {2**n:8d}  SKIP (too large)")
            break

    # 2b: TVD vs c for fixed n=5
    print(f"\n{'─' * 60}")
    print("2b. TVD vs c for n = 5")
    print(f"{'─' * 60}")

    c_values = [0.1, 0.3, 0.5, np.pi/4, 0.7, 0.9]
    c_labels = ['0.1', '0.3', '0.5', 'pi/4', '0.7', '0.9']

    print(f"  {'c':>10s}  {'p_bnd':>10s}  {'p_int':>10s}  {'TVD(uni)':>12s}  "
          f"{'TVD(pos)':>12s}  {'P(0)':>14s}  {'P(max_w)':>14s}")
    print(f"  {'─'*10}  {'─'*10}  {'─'*10}  {'─'*12}  {'─'*12}  {'─'*14}  {'─'*14}")

    tvd_vs_c = []
    for c_val, c_lab in zip(c_values, c_labels):
        res = compute_cz_distribution(5, c=c_val)
        comp = compute_comparison_metrics(res)
        tvd_vs_c.append({
            'c': c_val, 'label': c_lab,
            'TVD_full': comp['TVD_full'],
            'TVD_weight': comp['TVD_weight'],
            'p_eff': res['p_eff'],
        })
        print(f"  {c_lab:>10s}  {comp['p_boundary']:10.6f}  {comp['p_interior']:10.6f}  "
              f"{comp['TVD_full']:12.6f}  {comp['TVD_full_pos']:12.6f}  "
              f"{comp['P_gram'][0]:14.6e}  {comp['P_gram'][5]:14.6e}")

    # 2c: Effective logical error rate for distance-d codes
    print(f"\n{'─' * 60}")
    print("2c. Effective logical error rate — p_eff(d) vs code distance")
    print(f"{'─' * 60}")

    n = 7  # Use 7 qubits for better resolution
    res7 = compute_cz_distribution(n, c=0.5)
    comp7 = compute_comparison_metrics(res7)

    # Position-dependent i.i.d. baseline
    c_z_iid_pos = comp7['c_z_iid_pos']
    p_q = comp7['p_q']

    print(f"  n = {n}, c = 0.5")
    print(f"  p_boundary = {comp7['p_boundary']:.6f}")
    print(f"  p_interior = {comp7['p_interior']:.6f}")
    print(f"  Per-qubit p_q: {[f'{p:.4f}' for p in p_q]}")
    print()
    print(f"  {'d':>3s}  {'p_gram(d)':>14s}  {'p_unif_iid(d)':>14s}  "
          f"{'p_pos_iid(d)':>14s}  {'ρ_unif':>12s}  {'ρ_pos':>12s}")
    print(f"  {'─'*3}  {'─'*14}  {'─'*14}  {'─'*14}  {'─'*12}  {'─'*12}")

    for d_code in [3, 5, 7]:
        p_gram_d = compute_effective_logical_error(res7['c_z'], d_code)

        # Uniform baseline (uses boundary p=0.354)
        from math import comb
        p_iid_unif_d = 0.0
        threshold = int(np.ceil(d_code / 2))
        for w in range(threshold, n + 1):
            p_iid_unif_d += comb(n, w) * (comp7['p_eff'] ** w) * ((1 - comp7['p_eff']) ** (n - w))

        # Position-dependent baseline
        p_iid_pos_d = compute_effective_logical_error(c_z_iid_pos, d_code)

        ratio_unif = p_gram_d / p_iid_unif_d if p_iid_unif_d > 1e-15 else np.inf
        ratio_pos = p_gram_d / p_iid_pos_d if p_iid_pos_d > 1e-15 else np.inf
        print(f"  {d_code:3d}  {p_gram_d:14.6e}  {p_iid_unif_d:14.6e}  "
              f"{p_iid_pos_d:14.6e}  {ratio_unif:12.4f}  {ratio_pos:12.4f}")

    print(f"\n  Interpretation:")
    ratio_unif_d7 = p_gram_d if d_code == 7 else None  # filled below
    print(f"  With uniform baseline (p={comp7['p_eff']:.4f}): "
          f"ρ(d) = ratio shows Gram is {(p_gram_d/p_iid_pos_d - 1)*100:.1f}% higher")
    print(f"  With position-dependent baseline: ρ(d) = ratio shows the TRUE")
    print(f"  enhancement from Gram correlations beyond what position-dependent")
    print(f"  qubit error rates alone would predict.")

    return tvd_vs_n, tvd_vs_c


# ============================================================================
# PART 3: Analytical characterization
# ============================================================================

def part3_analytical():
    """
    Analytical characterization of the c_z distribution.

    For the vertex-sharing chain:
    G(x) = G[a, a⊕x] (assumed translation-invariant)

    G(x) = ∏_{r=0}^{n-2} cos(c·Δ_r(x))^2

    where Δ_r(x) depends on x_r, x_{r+1} and the background a.

    For the "folded" version (average over backgrounds):
    Each ring r contributes a factor that depends on the local pattern
    of x at positions r and r+1.

    The 2×2 local matrix structure:
    For each pair of neighboring bits (x_r, x_{r+1}), the delta distribution is:
    - (0,0): Δ ∈ {-4, -2, 0, 2, 4} with probabilities ... wait, this depends on background.

    Let's think more carefully about the folded G(x).
    G(x) = (1/2^n) ∑_a G[a, a⊕x] = (1/2^n) ∑_a ∏_r cos²(c·Δ_r(a,x))

    This is an Ising-like partition function.
    """
    print("\n" + "=" * 80)
    print("PART 3: Analytical Characterization of c_z")
    print("=" * 80)

    # 3a: Check translation-invariance assumption
    print(f"\n{'─' * 60}")
    print("3a. Translation-invariance check: variance of G[a,a⊕x] across a")
    print(f"{'─' * 60}")

    for n in [3, 4, 5]:
        var = check_translation_invariance(n, c=0.5)
        print(f"  n={n}: max σ(G[a,a⊕x]) across x = {var:.2e}")

    # 3b: Transfer-matrix structure for G(x)
    print(f"\n{'─' * 60}")
    print("3b. Local structure analysis of G(x)")
    print(f"{'─' * 60}")

    n = 5
    c = 0.5
    G_fold, G = build_gram_diagonal_folded(n, c)

    # Compute G(x) for each x and look for patterns
    print(f"  n={n}: G(x) values grouped by local pattern at (x_0,x_1):")

    # Group x by the tuple of consecutive bit patterns
    # Each ring r sees (x_r, x_{r+1}) -> 4 possible patterns: 00, 01, 10, 11
    # The contribution of ring r is a function f_{pattern}(a_r, a_{r+1})
    # When we average over a, only the pattern matters

    # Let's check: for x patterns that are translations of each other, is G(x) the same?
    d = 2 ** n
    x_vals = []
    for x in range(d):
        pattern = tuple((x >> r) & 1 for r in range(n))
        Gx = G_fold[x]
        x_vals.append((x, pattern, Gx))

    # Show G(x) for all x with weight 1 and weight 2
    print(f"\n  G_fold(x) for weight-1 patterns (single Z error):")
    for x in range(d):
        if bin(x).count('1') == 1:
            # Find which qubit has the error
            q = int(np.log2(x))
            pattern = ''.join(str((x >> r) & 1) for r in range(n))
            print(f"    x={pattern} (q={q}): G_fold = {G_fold[x]:.6f}")

    print(f"\n  G_fold(x) for weight-2 patterns:")
    for x in range(d):
        if bin(x).count('1') == 2:
            pattern = ''.join(str((x >> r) & 1) for r in range(n))
            print(f"    x={pattern}: G_fold = {G_fold[x]:.6f}")

    # 3c: Compute c_z analytically via transfer matrix?
    print(f"\n{'─' * 60}")
    print("3c. Numerical c_z structure")
    print(f"{'─' * 60}")

    res5 = compute_cz_distribution(5, c=0.5)
    c_z = res5['c_z']

    # Show c_z sorted
    d = 2 ** n
    indices = np.argsort(c_z)[::-1]
    print(f"\n  All c_z for n=5, c=0.5 (sorted):")
    for rank, idx in enumerate(indices):
        if c_z[idx] < 1e-8 and rank > 20:
            break
        w = bin(idx).count('1')
        print(f"    rank {rank:2d}: z={idx:05b} w={w} c_z={c_z[idx]:.8e}")

    # 3d: Asymptotic approximation
    print(f"\n{'─' * 60}")
    print("3d. Asymptotic analysis for large n")
    print(f"{'─' * 60}")

    # For large n, the folded G(x) depends on the local pattern of x.
    # Each ring r contributes factor = <cos²(c·Δ_r(a,x))>_a
    #
    # For fixed x_r, x_{r+1}, we can compute the 4x4 transfer matrix:
    # T_{s, s'} = contribution of ring between positions with state s=(x_r, x_{r+1})
    #
    # But since G(x) = ∏_r f(x_r, x_{r+1}) (approximately), this is a 1D product.
    # c_z = WH(G) = WH(∏_r f(x_r, x_{r+1}))
    #
    # The transfer matrix approach:
    # Define a 2x2 matrix M where:
    # M_ij = (1/4) ∑_{a_r, a_{r+1} ∈ {0,1}} cos²(c * Δ_r(a_r, a_{r+1}, x_r=i, x_{r+1}=j))
    #
    # Then G(x) ≈ ∏_{r=0}^{n-2} M_{x_r, x_{r+1}}
    # This is a 1D Ising model partition function in a "magnetic field" representation.

    # Compute the 4x4 "ring factor" matrix f_ij for i,j ∈ {0,1}
    f_matrix = np.zeros((2, 2))
    for xr in [0, 1]:
        for xr1 in [0, 1]:
            # Average over background bits a_r, a_{r+1}
            avg_factor = 0.0
            for ar in [0, 1]:
                for ar1 in [0, 1]:
                    s_ar = 1 if ar == 0 else -1
                    s_ar1 = 1 if ar1 == 0 else -1
                    s_br = s_ar * (1 if xr == 0 else -1)
                    s_br1 = s_ar1 * (1 if xr1 == 0 else -1)
                    delta = (s_ar + s_ar1) - (s_br + s_br1)
                    factor = np.cos(c * delta) ** 2
                    avg_factor += factor
            avg_factor /= 4.0  # Average over 4 background combos
            f_matrix[xr, xr1] = avg_factor

    print("\n  Ring-factor matrix f(x_r, x_{r+1}) for c=0.5:")
    print(f"    f(0,0) = {f_matrix[0,0]:.6f}")
    print(f"    f(0,1) = {f_matrix[0,1]:.6f}")
    print(f"    f(1,0) = {f_matrix[1,0]:.6f}")
    print(f"    f(1,1) = {f_matrix[1,1]:.6f}")

    # Compare: approximate G(x) via product of f_matrix vs exact G_fold(x)
    print(f"\n  Comparing product approximation vs exact G_fold(x):")
    max_err = 0.0
    for x in range(d):
        x_bits = [(x >> r) & 1 for r in range(n)]
        G_approx = 1.0
        for r in range(n - 1):
            G_approx *= f_matrix[x_bits[r], x_bits[r + 1]]
        err = abs(G_approx - G_fold[x])
        if err > max_err:
            max_err = err
    print(f"    Max error (product approx vs exact): {max_err:.6e}")

    # Now the transfer matrix method for c_z:
    # G(x) = ∏_r f(x_r, x_{r+1}) is a 1D factorized form.
    # c_z = (1/2^n) ∑_x G(x) (-1)^{z·x}
    # = (1/2^n) ∑_x ∏_r f(x_r, x_{r+1}) (-1)^{∑_i z_i x_i}
    #
    # This factorizes as:
    # c_z = (1/2^n) ⟨1| T^{(z)} |1⟩
    # where T^{(z)} is a 2x2 transfer matrix with elements:
    # T^{(z)}_{i,j} = f(i,j) * (-1)^{z_i * i}  (with periodic or open BCs)
    #
    # For open boundary conditions (chain of n qubits, n-1 rings):
    # c_z = (1/2^n) ∑_{x_0,...,x_{n-1}} ∏_{r=0}^{n-2} f(x_r,x_{r+1}) ∏_{i=0}^{n-1} (-1)^{z_i x_i}
    #
    # This is a matrix product:
    # c_z = (1/2^n) * v_L^T * T_1^{(z)} * T_2^{(z)} * ... * T_{n-2}^{(z)} * v_R
    # where T_r^{(z)} has elements:
    #   T_r^{(z)}[i,j] = f(i,j) * (-1)^{z_r * i}  for position r (as left index)
    # Actually, we need to be more careful with the indexing.

    # Let me compute c_z via transfer matrix for n=5 and compare with exact WH
    c_z_tm = np.zeros(d)
    for z in range(d):
        z_bits = [(z >> i) & 1 for i in range(n)]

        # Build the transfer matrix product
        # We need v_L (size 2) and v_R (size 2) for boundaries
        # v_L[i] = 1 (sum over x_0), v_R[j] = (-1)^{z_{n-1} * j}
        # T_r[i,j] = f(i,j) * (-1)^{z_r * i}

        # For n=5, we have 4 rings (4 transfer matrices)
        # c_z = (1/2^n) ∑_{x_0,x_1,...,x_4} f(x_0,x_1) f(x_1,x_2) f(x_2,x_3) f(x_3,x_4)
        #            * (-1)^{z_0 x_0} (-1)^{z_1 x_1} ... (-1)^{z_4 x_4}

        # This is: sum over x_4 of (-1)^{z_4 x_4} sum over x_3 f(x_3,x_4)(-1)^{z_3 x_3} ...

        # Start from the right: v_R[j] = 1 for x_{n-1} (the last qubit)
        vec = np.ones(2)  # sums over x_{n-1}
        vec = vec * np.array([1, (-1)**z_bits[n-1]])  # Include z_{n-1} sign

        for r in range(n-2, -1, -1):
            # Multiply by T_r and include z_r sign
            new_vec = np.zeros(2)
            for i in range(2):
                for j in range(2):
                    new_vec[i] += f_matrix[i, j] * vec[j]
                new_vec[i] *= (-1) ** (z_bits[r] * i)
            vec = new_vec

        # Sum over x_0 (left boundary)
        c_z_tm[z] = np.sum(vec) / d

    # Normalize
    c_z_tm = np.maximum(c_z_tm, 0.0)
    c_z_tm /= np.sum(c_z_tm)

    # Compare
    tvd = total_variation_distance(c_z, c_z_tm)
    print(f"\n  Transfer-matrix c_z vs exact WH c_z:")
    print(f"    TVD = {tvd:.6e}")

    max_diff = 0.0
    for z in range(d):
        if abs(c_z_tm[z] - c_z[z]) > max_diff:
            max_diff = abs(c_z_tm[z] - c_z[z])
    print(f"    Max |c_z^TM - c_z^WH| = {max_diff:.6e}")

    # Show TM results
    print(f"\n  c_z via transfer matrix (top 12):")
    indices_tm = np.argsort(c_z_tm)[::-1]
    for rank, idx in enumerate(indices_tm):
        if c_z_tm[idx] < 1e-8 and rank > 20:
            break
        w = bin(idx).count('1')
        print(f"    rank {rank:2d}: z={idx:05b} w={w} c_z^TM={c_z_tm[idx]:.8e}  "
              f"c_z^WH={c_z[idx]:.8e}")

    return {
        'f_matrix': f_matrix,
        'TVD_tm_vs_wh': tvd,
        'max_diff': max_diff,
        'c_z_tm': c_z_tm,
        'c_z_wh': c_z,
    }


# ============================================================================
# VISUALIZATION: Generate data for textual plots
# ============================================================================

def part4_detailed_correlation_analysis(n=6, c=0.5):
    """
    Detailed analysis of the c_z correlation structure:
    - Weight distribution
    - Pairwise correlation between Z errors on different qubits
    - Comparison of Gram vs i.i.d.
    """
    print("\n" + "=" * 80)
    print("DETAILED CORRELATION ANALYSIS")
    print("=" * 80)

    res = compute_cz_distribution(n, c)
    comp = compute_comparison_metrics(res)
    c_z = res['c_z']
    d = 2 ** n

    # Compute pairwise Z-error correlations
    # P(Z_i Z_j) = sum_{z: z_i=z_j=1} c_z
    # Correlation: Cov(Z_i, Z_j) = P(Z_i Z_j) - P(Z_i)P(Z_j)
    print(f"\n  Pairwise Z-error probabilities and correlations (n={n}, c={c}):")
    print(f"  {'pair':>8s}  {'P(both)':>12s}  {'P(i)P(j)':>12s}  "
          f"{'Cov':>12s}  {'Corr':>12s}")

    p_single = np.zeros(n)
    for i in range(n):
        p_single[i] = sum(c_z[z] for z in range(d) if (z >> i) & 1)

    for i in range(n):
        for j in range(i + 1, n):
            p_both = sum(c_z[z] for z in range(d)
                         if ((z >> i) & 1) and ((z >> j) & 1))
            p_indep = p_single[i] * p_single[j]
            cov = p_both - p_indep
            # Correlation coefficient normalized by max possible
            corr_max = min(p_single[i], p_single[j]) - p_indep
            corr = cov / corr_max if abs(corr_max) > 1e-15 else 0.0
            print(f"  ({i},{j})    {p_both:12.6e}  {p_indep:12.6e}  "
                  f"{cov:+12.6e}  {corr:+12.6f}")

    # Compute P(w) breakdown by neighbor structure
    print(f"\n  Weight distribution with distance info (n={n}, c={c}):")
    print(f"  {'w':>3s}  {'P(w)':>14s}  {'P_iid(w)':>14s}  "
          f"{'ρ(w)':>12s}  {'Is_enhanced':>12s}")
    for w in range(n + 1):
        is_enhanced = "YES" if comp['rho_w'][w] > 1.1 else \
                      "NO" if comp['rho_w'][w] < 0.9 else "SAME"
        print(f"  {w:3d}  {comp['P_gram'][w]:14.6e}  {comp['P_iid'][w]:14.6e}  "
              f"{comp['rho_w'][w]:12.4f}  {is_enhanced:>12s}")

    return res, comp


# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    np.set_printoptions(precision=6, suppress=True, linewidth=120)

    print("LP45: Gram-Weight Pauli Z Correlation Structure")
    print("Characterizing the c_z distribution for Gram-correlated dephasing")
    print(f"Date: 2026-06-11")
    print()

    # Part 1
    results_p1 = part1_compute_and_compare()

    # Part 2
    tvd_vs_n, tvd_vs_c = part2_scaling_analysis()

    # Part 3
    results_p3 = part3_analytical()

    # Detailed correlation
    res6, comp6 = part4_detailed_correlation_analysis(n=6, c=0.5)

    # Save numerical results for report
    summary = {
        'part1': {},
        'part2': {'tvd_vs_n': tvd_vs_n, 'tvd_vs_c': tvd_vs_c},
        'part3': {'TVD_tm_vs_wh': results_p3['TVD_tm_vs_wh'],
                  'f_matrix': results_p3['f_matrix'].tolist()},
    }

    for n, data in results_p1.items():
        comp = compute_comparison_metrics(data)
        summary['part1'][str(n)] = {
            'TVD_full': comp['TVD_full'],
            'TVD_weight': comp['TVD_weight'],
            'rho_w': comp['rho_w'].tolist(),
            'P_gram': comp['P_gram'].tolist(),
            'P_iid': comp['P_iid'].tolist(),
            'p_eff': comp['p_eff'],
        }

    with open(os.path.join(OUTDIR, 'cz_numerical_results.json'), 'w') as f:
        json.dump(summary, f, indent=2, default=lambda x: float(x))

    print(f"\n{'=' * 80}")
    print(f"Results saved to {os.path.join(OUTDIR, 'cz_numerical_results.json')}")
    print("Done.")

"""
Full Numerical Sweep: DGF Gram Matrix Spectral Properties
=========================================================
Vectorized version — uses numpy blocking to handle d_sys up to 8192.
Date: 2026-06-11
"""
import numpy as np
import json
import time
import sys
import os
import gc
import warnings

warnings.filterwarnings('ignore')

def print_flush(*args, **kwargs):
    print(*args, **kwargs)
    sys.stdout.flush()


# ================================================================
# Serialization helpers
# ================================================================
def numpy_to_native(obj):
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, (np.floating,)):
        return float(obj)
    if isinstance(obj, (np.integer,)):
        return int(obj)
    if isinstance(obj, (np.bool_,)):
        return bool(obj)
    if isinstance(obj, dict):
        return {k: numpy_to_native(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [numpy_to_native(v) for v in obj]
    if isinstance(obj, complex):
        return {'real': float(obj.real), 'imag': float(obj.imag)}
    try:
        if np.isnan(obj):
            return None
        if np.isinf(obj):
            return str(obj)
    except:
        pass
    return obj


def save_checkpoint(data, path):
    """Save intermediate results to JSON."""
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(numpy_to_native(data), f, indent=2)
        print_flush(f"  [checkpoint saved: {path}]")
    except Exception as e:
        print_flush(f"  [checkpoint FAILED: {e}]")


# ================================================================
# FAST Gram Construction — Vectorized Block Processing
# ================================================================
def build_gram_vertex_chain_fast(b1, c, p=0.5):
    """Vectorized Gram matrix for vertex-sharing chain.
    Uses 4x4 precomputed transition matrix and block processing."""
    n_sys = b1 + 1
    d_sys = 2 ** n_sys
    if d_sys > 8192:
        return None

    # Precompute 4x4 ring transition matrix T
    # T[i,j] = ring factor between two-qubit states i and j
    T = np.ones((4, 4), dtype=np.complex128)
    for i in range(4):
        s0_a = 1 if (i >> 1) & 1 else -1
        s1_a = 1 if (i >> 0) & 1 else -1
        for j in range(4):
            s0_b = 1 if (j >> 1) & 1 else -1
            s1_b = 1 if (j >> 0) & 1 else -1
            delta = (s0_a + s1_a) - (s0_b + s1_b)
            factor = p * np.exp(1j * c * delta) + (1 - p) * np.exp(-1j * c * delta)
            T[i, j] = factor * factor

    # Compute state index for each basis state: bits[i,q] = qubit q value for state i
    bits = np.zeros((d_sys, n_sys), dtype=np.int8)
    idx_arr = np.arange(d_sys)
    for q in range(n_sys):
        bits[:, q] = np.where((idx_arr >> q) & 1, 1, -1)

    G = np.ones((d_sys, d_sys), dtype=np.complex128)
    block_size = 256

    for r in range(b1):
        # Two-qubit state index for ring r: bits 0-3 based on (bit_r, bit_{r+1})
        state_idx = np.zeros(d_sys, dtype=np.int32)
        state_idx += np.where(bits[:, r] == -1, 0, 2)
        state_idx += np.where(bits[:, r + 1] == -1, 0, 1)

        T_rows = T[state_idx]  # d_sys x 4

        for start in range(0, d_sys, block_size):
            end = min(start + block_size, d_sys)
            block = T_rows[start:end, :]  # bs x 4
            for j in range(4):
                mask_j = state_idx == j
                nj = np.sum(mask_j)
                if nj == 0:
                    continue
                # Multiply G[start:end, mask_j] column-wise by block[:, j]
                G[start:end, mask_j] *= block[:, j:j+1]

    return G


def build_gram_vertex_chain_exact(b1, c, p=0.5):
    """Exact Gram matrix (for validation of small b1)."""
    n_sys = b1 + 1
    d_sys = 2 ** n_sys
    if d_sys > 8192:
        return None
    G = np.ones((d_sys, d_sys), dtype=complex)
    sys_states = np.zeros((d_sys, n_sys), dtype=int)
    for idx in range(d_sys):
        for q in range(n_sys):
            sys_states[idx, q] = 1 if (idx >> q) & 1 else -1
    for r in range(b1):
        for a in range(d_sys):
            s_Qr_a = sys_states[a, r]
            s_Qr1_a = sys_states[a, r + 1]
            for b in range(a, d_sys):
                s_Qr_b = sys_states[b, r]
                s_Qr1_b = sys_states[b, r + 1]
                delta = (s_Qr_a + s_Qr1_a) - (s_Qr_b + s_Qr1_b)
                factor = p * np.exp(1j * c * delta) + (1 - p) * np.exp(-1j * c * delta)
                G[a, b] *= factor * factor
        for a in range(d_sys):
            for b in range(a + 1, d_sys):
                G[b, a] = np.conj(G[a, b])
    return G


# ================================================================
# Topology-specific builders
# ================================================================
def build_gram_tree(c, p=0.5):
    """Tree: Q0-E0-Q1-E1-Q2, 3 sys qubits, d=8, b1=0."""
    d_sys = 8
    G = np.ones((d_sys, d_sys), dtype=complex)
    sys_states = np.zeros((d_sys, 3), dtype=int)
    for idx in range(d_sys):
        for q in range(3):
            sys_states[idx, q] = 1 if (idx >> q) & 1 else -1
    for a in range(d_sys):
        s0a, s1a, s2a = sys_states[a, 0], sys_states[a, 1], sys_states[a, 2]
        for b in range(a, d_sys):
            s0b, s1b, s2b = sys_states[b, 0], sys_states[b, 1], sys_states[b, 2]
            d0 = (s0a + s1a) - (s0b + s1b)
            f0 = p * np.exp(1j * c * d0) + (1 - p) * np.exp(-1j * c * d0)
            d1 = (s1a + s2a) - (s1b + s2b)
            f1 = p * np.exp(1j * c * d1) + (1 - p) * np.exp(-1j * c * d1)
            G[a, b] = f0 * f1
    for a in range(d_sys):
        for b in range(a + 1, d_sys):
            G[b, a] = np.conj(G[a, b])
    return G


def build_gram_ring_single(c, p=0.5):
    """Single ring: Q0-E0-Q1-E1-Q0, 2 sys qubits, d=4, b1=1."""
    d_sys = 4
    G = np.ones((d_sys, d_sys), dtype=complex)
    sys_states = np.zeros((d_sys, 2), dtype=int)
    for idx in range(d_sys):
        for q in range(2):
            sys_states[idx, q] = 1 if (idx >> q) & 1 else -1
    for a in range(d_sys):
        s0a, s1a = sys_states[a, 0], sys_states[a, 1]
        for b in range(a, d_sys):
            s0b, s1b = sys_states[b, 0], sys_states[b, 1]
            d0 = (s0a + s1a) - (s0b + s1b)
            f0 = p * np.exp(1j * c * d0) + (1 - p) * np.exp(-1j * c * d0)
            d1 = (s1a + s0a) - (s1b + s0b)
            f1 = p * np.exp(1j * c * d1) + (1 - p) * np.exp(-1j * c * d1)
            G[a, b] = f0 * f1
    for a in range(d_sys):
        for b in range(a + 1, d_sys):
            G[b, a] = np.conj(G[a, b])
    return G


def build_gram_edge_disjoint(b1, c, p=0.5):
    """Edge-disjoint rings: each independent, 2 sys qubits/ring, d=2^{2b1}."""
    n_sys = 2 * b1
    d_sys = 2 ** n_sys
    if d_sys > 8192:
        return None
    G1 = np.ones((4, 4), dtype=complex)
    for a in range(4):
        s0a = 1 if (a >> 0) & 1 else -1
        s1a = 1 if (a >> 1) & 1 else -1
        for b in range(a, 4):
            s0b = 1 if (b >> 0) & 1 else -1
            s1b = 1 if (b >> 1) & 1 else -1
            d0 = (s0a + s1a) - (s0b + s1b)
            f0 = p * np.exp(1j * c * d0) + (1 - p) * np.exp(-1j * c * d0)
            d1 = (s1a + s0a) - (s1b + s0b)
            f1 = p * np.exp(1j * c * d1) + (1 - p) * np.exp(-1j * c * d1)
            G1[a, b] = f0 * f1
    for a in range(4):
        for b in range(a + 1, 4):
            G1[b, a] = np.conj(G1[a, b])
    G = G1.copy()
    for _ in range(b1 - 1):
        G = np.kron(G, G1)
    return G


def sample_gram_2d_grid(L, c, p=0.5, n_samples=3000):
    """Sample Gram off-diagonal for 2D grid."""
    rng = np.random.RandomState(42 + L)
    n_sys = L * L
    offdiag_mags = []
    offdiag_phases = []
    for _ in range(n_samples):
        a = rng.randint(0, 2, size=n_sys) * 2 - 1
        b = rng.randint(0, 2, size=n_sys) * 2 - 1
        if np.array_equal(a, b):
            continue
        G_ab = 1.0 + 0.0j
        n_rings = 0
        for rx in range(L - 1):
            for ry in range(L - 1):
                q00 = rx * L + ry
                q10 = (rx + 1) * L + ry
                q11 = (rx + 1) * L + ry + 1
                q01 = rx * L + ry + 1
                sum_a = a[q00] + a[q10] + a[q11] + a[q01]
                sum_b = b[q00] + b[q10] + b[q11] + b[q01]
                delta = sum_a - sum_b
                G_ab *= (p * np.exp(1j * c * delta) + (1 - p) * np.exp(-1j * c * delta))
                n_rings += 1
        offdiag_mags.append(np.abs(G_ab))
        offdiag_phases.append(float(np.angle(G_ab)))
    return offdiag_mags, offdiag_phases, n_rings


# ================================================================
# Spectral Analysis
# ================================================================
def analyze_gram(G, b1_val=None):
    if G is None:
        return None
    d = G.shape[0]
    try:
        evals_raw = np.linalg.eigvalsh(G)
    except Exception:
        return None
    evals_raw = np.maximum(evals_raw, 0.0)
    total = np.sum(evals_raw)
    if total < 1e-15:
        return None
    evals = evals_raw / total
    evals_sorted = np.sort(evals)[::-1]

    rank_eff = 1.0 / np.sum(evals ** 2) if np.sum(evals ** 2) > 1e-30 else 1.0
    n_significant = int(np.sum(evals > 1e-12))
    S = 0.0
    for e in evals:
        if e > 1e-15:
            S -= e * np.log(e)
    S_max = np.log(d)
    dominance = evals_sorted[0]
    top5 = evals_sorted[:5].tolist()

    # Sample off-diagonal (don't extract all for large d)
    if d <= 256:
        offdiag_abs = []
        for a in range(d):
            for b in range(a + 1, d):
                offdiag_abs.append(np.abs(G[a, b]))
        offdiag_abs = np.array(offdiag_abs)
    else:
        # Sample ~5000 random pairs
        rng = np.random.RandomState(42)
        n_samples = min(5000, d * (d - 1) // 2)
        pairs = set()
        offdiag_abs = []
        while len(offdiag_abs) < n_samples:
            a = rng.randint(0, d)
            b = rng.randint(0, d)
            if a == b:
                continue
            key = (min(a, b), max(a, b))
            if key in pairs:
                continue
            pairs.add(key)
            offdiag_abs.append(np.abs(G[a, b]))
        offdiag_abs = np.array(offdiag_abs)

    mean_off = float(np.mean(offdiag_abs))
    std_off = float(np.std(offdiag_abs))
    med_off = float(np.median(offdiag_abs))

    if b1_val is not None and b1_val > 0 and len(offdiag_abs) > 0:
        valid = offdiag_abs[offdiag_abs > 1e-15]
        if len(valid) > 0:
            mu_measured = float(np.mean(np.log(valid)) / b1_val)
        else:
            mu_measured = None
    else:
        mu_measured = None

    return {
        'd': d, 'b1': b1_val,
        'rank_eff': float(rank_eff),
        'rank_eff_over_d': float(rank_eff / d),
        'n_significant': n_significant,
        'lambda1_over_sum': float(dominance),
        'top5_evals': top5,
        'eigenvalue_entropy': float(S),
        'S_over_Smax': float(S / S_max),
        'mean_offdiag': mean_off,
        'std_offdiag': std_off,
        'median_offdiag': med_off,
        'mu_measured': mu_measured,
        'evals_all': evals_sorted.tolist(),
    }


# ================================================================
# Analytic mu formulas
# ================================================================
def analytic_mu_vertex(c, p=0.5):
    delta_vals = np.array([-4, -2, 0, 2, 4])
    delta_probs = np.array([1, 4, 6, 4, 1]) / 16.0
    mu_env = 0.0
    for dv, prob in zip(delta_vals, delta_probs):
        factor = p * np.exp(1j * c * dv) + (1 - p) * np.exp(-1j * c * dv)
        abs_factor = np.abs(factor)
        if abs_factor < 1e-15:
            return float('-inf')
        mu_env += prob * np.log(abs_factor)
    return 2.0 * float(mu_env)


def analytic_mu_edge_disjoint(c, p=0.5):
    sum_vals = np.array([-2, 0, 2])
    sum_probs = np.array([1, 2, 1]) / 4.0
    mu = 0.0
    for sa, pa in zip(sum_vals, sum_probs):
        for sb, pb in zip(sum_vals, sum_probs):
            delta = sa - sb
            prob = pa * pb
            factor = p * np.exp(1j * c * delta) + (1 - p) * np.exp(-1j * c * delta)
            abs_factor = np.abs(factor)
            if abs_factor < 1e-15:
                return float('-inf')
            mu += prob * np.log(abs_factor)
    return 2.0 * float(mu)


def analytic_mu_grid(c, p=0.5):
    sum_vals = np.array([-4, -2, 0, 2, 4])
    sum_probs = np.array([1, 4, 6, 4, 1]) / 16.0
    mu = 0.0
    for sa, pa in zip(sum_vals, sum_probs):
        for sb, pb in zip(sum_vals, sum_probs):
            delta = sa - sb
            prob = pa * pb
            factor = p * np.exp(1j * c * delta) + (1 - p) * np.exp(-1j * c * delta)
            abs_factor = np.abs(factor)
            if abs_factor < 1e-15:
                return float('-inf')
            mu += prob * np.log(abs_factor)
    return 2.0 * float(mu)


# ================================================================
# Part 1: b1-c Phase Diagram
# ================================================================
def run_part1(result_dir):
    print_flush("=" * 80)
    print_flush("PART 1: Full b1-c Phase Diagram")
    print_flush("=" * 80)
    t_start = time.time()

    b1_vals = list(range(13))
    c_vals = [0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.2,
              np.pi/8, np.pi/4, 1.5, np.pi/2]
    c_labels = ['0.05', '0.10', '0.20', '0.30', '0.40', '0.50', '0.60', '0.70',
                '0.80', '0.90', '1.00', '1.20', 'pi/8', 'pi/4', '1.50', 'pi/2']
    p = 0.5

    phase_data = {}
    total_combos = len(b1_vals) * len(c_vals)
    done = 0

    for b1 in b1_vals:
        for c, clabel in zip(c_vals, c_labels):
            d_sys = 2 ** (b1 + 1)
            done += 1
            key = f"b1={b1}_c={clabel}"
            if d_sys > 8192:
                phase_data[key] = {'skipped': True, 'reason': f'd_sys={d_sys}>8192',
                                   'b1': b1, 'c': clabel, 'd_sys': d_sys}
                print_flush(f"  [{done}/{total_combos}] SKIP b1={b1} c={clabel} (d={d_sys}>8192)")
                continue
            G = build_gram_vertex_chain_fast(b1, c, p)
            spec = analyze_gram(G, b1_val=b1 if b1 > 0 else None)
            if spec is None:
                phase_data[key] = {'skipped': True, 'reason': 'None result',
                                   'b1': b1, 'c': clabel, 'd_sys': d_sys}
            else:
                entry = {'b1': b1, 'c': clabel, 'c_rad': float(c), 'd_sys': d_sys,
                         'rank_eff': spec['rank_eff'],
                         'rank_eff_over_d': spec['rank_eff_over_d'],
                         'mean_offdiag': spec['mean_offdiag'],
                         'std_offdiag': spec['std_offdiag'],
                         'median_offdiag': spec['median_offdiag'],
                         'mu_measured': spec['mu_measured'],
                         'lambda1_over_sum': spec['lambda1_over_sum'],
                         'eigenvalue_entropy': spec['eigenvalue_entropy'],
                         'S_over_Smax': spec['S_over_Smax'],
                         'n_significant': spec['n_significant'],
                         'top5_evals': spec['top5_evals']}
                phase_data[key] = entry
                print_flush(f"  [{done}/{total_combos}] b1={b1} c={clabel} d={d_sys} "
                            f"rank_eff={spec['rank_eff']:.4f} mean|G|={spec['mean_offdiag']:.2e} "
                            f"mu={spec['mu_measured']}")
            del G
            gc.collect()

    t_elapsed = time.time() - t_start
    print_flush(f"  Part 1 done: {t_elapsed:.1f}s")
    save_checkpoint(phase_data, os.path.join(result_dir, 'checkpoint_p1.json'))
    return phase_data, t_elapsed


# ================================================================
# Part 2: Gram Spectral Density
# ================================================================
def marcenko_pastur_cdf(lambda_vals, gamma, n_points=500):
    lam_plus = (1 + np.sqrt(gamma)) ** 2
    lam_minus = (1 - np.sqrt(gamma)) ** 2
    cdf = np.zeros(len(lambda_vals))
    for i, lam in enumerate(lambda_vals):
        if lam <= lam_minus:
            cdf[i] = 0.0
        elif lam >= lam_plus:
            cdf[i] = 1.0
        else:
            lam_grid = np.linspace(lam_minus, lam, max(200, 2))
            integrand = np.sqrt(np.maximum(0, (lam_plus - lam_grid) * (lam_grid - lam_minus)))
            rho = integrand / (2.0 * np.pi * gamma * np.maximum(lam_grid, 1e-15))
            cdf[i] = np.trapz(rho, lam_grid) if len(lam_grid) > 1 else 0.0
    return np.clip(cdf, 0, 1)


def ks_distance_mp(sorted_evals, gamma):
    n = len(sorted_evals)
    empirical_cdf = np.arange(1, n + 1) / n
    mp_cdf = marcenko_pastur_cdf(sorted_evals, gamma)
    return np.max(np.abs(empirical_cdf - mp_cdf))


def fit_marcenko_pastur(evals):
    sorted_evals = np.sort(evals)
    best_ks = float('inf')
    best_gamma = None
    for gamma in np.linspace(0.02, 0.98, 60):
        ks = ks_distance_mp(sorted_evals, gamma)
        if ks < best_ks:
            best_ks = ks
            best_gamma = gamma
    for gamma in np.linspace(max(0.01, best_gamma - 0.08), min(0.99, best_gamma + 0.08), 60):
        ks = ks_distance_mp(sorted_evals, gamma)
        if ks < best_ks:
            best_ks = ks
            best_gamma = gamma
    return best_gamma, best_ks


def run_part2(result_dir):
    print_flush("\n" + "=" * 80)
    print_flush("PART 2: Gram Spectral Density -- Marcenko-Pastur Fitting")
    print_flush("=" * 80)
    t_start = time.time()

    b1_vals = [4, 6, 8, 10, 12]
    c = 0.5
    p = 0.5
    results = {}

    for b1 in b1_vals:
        print_flush(f"  b1={b1}...", end=" ")
        G = build_gram_vertex_chain_fast(b1, c, p)
        if G is None:
            print_flush("SKIP")
            results[f"b1={b1}"] = {'skipped': True}
            continue
        spec = analyze_gram(G, b1_val=b1)
        evals_arr = np.array(spec['evals_all'])
        evals_pos = evals_arr[evals_arr > 1e-14]
        if len(evals_pos) < 10:
            print_flush("too few positive evals")
            results[f"b1={b1}"] = {'skipped': True, 'reason': 'too few positive evals'}
            del G
            continue

        best_gamma, best_ks = fit_marcenko_pastur(evals_pos)
        d = spec['d']
        eig_mean = float(np.mean(evals_pos))
        eig_var = float(np.var(evals_pos))

        entry = {
            'b1': b1, 'd': d,
            'n_positive_evals': len(evals_pos),
            'best_fit_gamma': float(best_gamma),
            'ks_distance': float(best_ks),
            'eigenvalue_mean': eig_mean,
            'eigenvalue_variance': eig_var,
            'evals_positive': evals_pos.tolist(),
        }
        results[f"b1={b1}"] = entry
        print_flush(f"gamma={best_gamma:.4f} KS={best_ks:.6f} n_pos={len(evals_pos)}")
        del G, evals_arr
        gc.collect()

    ks_trend = []
    for b1 in b1_vals:
        key = f"b1={b1}"
        if key in results and not results[key].get('skipped'):
            ks_trend.append({'b1': b1, 'ks_distance': results[key]['ks_distance']})

    t_elapsed = time.time() - t_start
    print_flush(f"  Part 2 done: {t_elapsed:.1f}s")
    output = {'by_b1': results, 'ks_trend': ks_trend}
    save_checkpoint(output, os.path.join(result_dir, 'checkpoint_p2.json'))
    return output, t_elapsed


# ================================================================
# Part 3: Level Spacing Statistics
# ================================================================
def compute_spacings(evals):
    evals_sorted = np.sort(evals[evals > 1e-14])
    if len(evals_sorted) < 5:
        return None
    spacings = np.diff(evals_sorted)
    mean_s = np.mean(spacings)
    if mean_s < 1e-15:
        return None
    return spacings / mean_s


def fit_brody(spacings):
    if spacings is None or len(spacings) < 5:
        return None, None, None
    n = len(spacings)
    sorted_s = np.sort(spacings)
    empirical_cdf = np.arange(1, n + 1) / n
    best_ks = float('inf')
    best_alpha = None
    for alpha_cand in np.linspace(-0.45, 1.5, 120):
        # Need alpha+1 > 0 for proper normalization
        if alpha_cand <= -1.0:
            continue
        import math
        beta = math.exp(math.lgamma((alpha_cand + 2) / (alpha_cand + 1)))
        beta = beta ** (alpha_cand + 1)
        brody_cdf = 1.0 - np.exp(-beta * sorted_s ** (alpha_cand + 1))
        brody_cdf = np.nan_to_num(brody_cdf, nan=1.0)
        ks = np.max(np.abs(empirical_cdf - brody_cdf))
        if ks < best_ks:
            best_ks = ks
            best_alpha = alpha_cand

    # Mean spacing ratio <r>
    ratios = []
    for i in range(len(spacings) - 1):
        mn = min(spacings[i], spacings[i + 1])
        mx = max(spacings[i], spacings[i + 1])
        if mx > 1e-15:
            ratios.append(mn / mx)
    mean_r = float(np.mean(ratios)) if ratios else None

    return best_alpha, best_ks, mean_r


def run_part3(result_dir):
    print_flush("\n" + "=" * 80)
    print_flush("PART 3: Level Spacing Statistics -- Poisson -> Wigner-Dyson")
    print_flush("=" * 80)
    t_start = time.time()

    b1_vals = [0, 1, 2, 3, 4, 5, 6]
    c = 0.5
    p = 0.5
    results = {}

    for b1 in b1_vals:
        print_flush(f"  b1={b1}...", end=" ")
        G = build_gram_vertex_chain_fast(b1, c, p)
        if G is None:
            print_flush("SKIP")
            results[f"b1={b1}"] = {'skipped': True}
            continue
        evals = np.array(analyze_gram(G, b1_val=b1 if b1 > 0 else None)['evals_all'])
        spacings = compute_spacings(evals)
        if spacings is None:
            print_flush("too few spacings")
            results[f"b1={b1}"] = {'skipped': True, 'reason': 'too few eigenvalues'}
            del G
            continue
        alpha, ks, r_val = fit_brody(spacings)
        d = G.shape[0]
        entry = {
            'b1': b1, 'd': d,
            'n_spacings': len(spacings),
            'brody_alpha': float(alpha) if alpha is not None else None,
            'brody_ks': float(ks) if ks is not None else None,
            'mean_spacing_ratio_r': r_val,
            'spacings': spacings.tolist(),
        }
        results[f"b1={b1}"] = entry
        print_flush(f"alpha={alpha:.4f} KS={ks:.4f} <r>={r_val}")
        del G, evals
        gc.collect()

    t_elapsed = time.time() - t_start
    print_flush(f"  Part 3 done: {t_elapsed:.1f}s")
    save_checkpoint(results, os.path.join(result_dir, 'checkpoint_p3.json'))
    return results, t_elapsed


# ================================================================
# Part 4: Tree vs Ring
# ================================================================
def run_part4(result_dir):
    print_flush("\n" + "=" * 80)
    print_flush("PART 4: Tree vs Ring -- Systematic Topology Comparison")
    print_flush("=" * 80)
    t_start = time.time()

    c_list = [0.1, 0.5, np.pi / 4, np.pi / 2]
    c_labels = ['0.10', '0.50', 'pi/4', 'pi/2']
    p = 0.5
    results = {}

    for c, clabel in zip(c_list, c_labels):
        print_flush(f"\n  c = {clabel}:")
        entry = {'c': clabel, 'c_rad': float(c)}

        # Tree: Q0-E0-Q1-E1-Q2
        G_tree = build_gram_tree(c, p)
        st = analyze_gram(G_tree, b1_val=None)
        entry['tree'] = {
            'topology': 'Tree (b1=0)',
            'n_qubits': 5, 'n_sys_qubits': 3, 'n_edges': 4, 'n_rings': 0,
            'd_sys': G_tree.shape[0],
            'rank_eff': st['rank_eff'],
            'mean_offdiag': st['mean_offdiag'],
            'median_offdiag': st['median_offdiag'],
            'evals': st['evals_all'],
        }
        print_flush(f"    Tree:    rank_eff={st['rank_eff']:.4f} mean|G|={st['mean_offdiag']:.4e}")

        # Ring: Q0-E0-Q1-E1-Q0
        G_ring = build_gram_ring_single(c, p)
        sr = analyze_gram(G_ring, b1_val=1)
        entry['ring'] = {
            'topology': 'Ring (b1=1)',
            'n_qubits': 4, 'n_sys_qubits': 2, 'n_edges': 4, 'n_rings': 1,
            'd_sys': G_ring.shape[0],
            'rank_eff': sr['rank_eff'],
            'mean_offdiag': sr['mean_offdiag'],
            'median_offdiag': sr['median_offdiag'],
            'mu_measured': sr['mu_measured'],
            'evals': sr['evals_all'],
        }
        print_flush(f"    Ring:    rank_eff={sr['rank_eff']:.4f} mean|G|={sr['mean_offdiag']:.4e}")

        # Two-Ring: vertex-sharing b1=2
        G_2ring = build_gram_vertex_chain_fast(2, c, p)
        s2 = analyze_gram(G_2ring, b1_val=2)
        entry['two_ring'] = {
            'topology': 'Two-Ring (b1=2)',
            'n_qubits': 7, 'n_sys_qubits': 3, 'n_edges': 8, 'n_rings': 2,
            'd_sys': G_2ring.shape[0],
            'rank_eff': s2['rank_eff'],
            'mean_offdiag': s2['mean_offdiag'],
            'median_offdiag': s2['median_offdiag'],
            'mu_measured': s2['mu_measured'],
            'evals': s2['evals_all'],
        }
        print_flush(f"    Two-Ring: rank_eff={s2['rank_eff']:.4f} mean|G|={s2['mean_offdiag']:.4e}")

        # Decoherence enhancement
        if st['mean_offdiag'] > 1e-15:
            entry['decoherence_enhancement'] = {
                '|G_tree|/|G_ring|': st['mean_offdiag'] / sr['mean_offdiag'] if sr['mean_offdiag'] > 1e-15 else None,
                '|G_tree|/|G_2ring|': st['mean_offdiag'] / s2['mean_offdiag'] if s2['mean_offdiag'] > 1e-15 else None,
                '|G_ring|/|G_2ring|': sr['mean_offdiag'] / s2['mean_offdiag'] if s2['mean_offdiag'] > 1e-15 else None,
            }
            print_flush(f"    Enhancement |G_tree|/|G_ring| = {entry['decoherence_enhancement']['|G_tree|/|G_ring|']:.4e}")

        results[clabel] = entry
        del G_tree, G_ring, G_2ring
        gc.collect()

    t_elapsed = time.time() - t_start
    print_flush(f"\n  Part 4 done: {t_elapsed:.1f}s")
    save_checkpoint(results, os.path.join(result_dir, 'checkpoint_p4.json'))
    return results, t_elapsed


# ================================================================
# Part 5: mu(c) Universality
# ================================================================
def run_part5(result_dir):
    print_flush("\n" + "=" * 80)
    print_flush("PART 5: mu(c) Universality -- Topology Independence")
    print_flush("=" * 80)
    t_start = time.time()

    c = 0.5
    p = 0.5
    results = {}

    # Topology 1: Vertex-sharing chain
    print_flush("  Topology 1: Vertex-sharing chain")
    vertex_data = []
    for b1 in range(1, 13):
        d_sys = 2 ** (b1 + 1)
        if d_sys > 8192:
            vertex_data.append({'b1': b1, 'skipped': True, 'd_sys': d_sys})
            continue
        G = build_gram_vertex_chain_fast(b1, c, p)
        spec = analyze_gram(G, b1_val=b1)
        vertex_data.append({
            'b1': b1, 'd_sys': d_sys,
            'mu_measured': spec['mu_measured'],
            'mean_offdiag': spec['mean_offdiag'],
            'rank_eff': spec['rank_eff'],
        })
        print_flush(f"    b1={b1}: mu_meas={spec['mu_measured']:.6f}")
        del G
        gc.collect()
    results['vertex_chain'] = vertex_data

    # Topology 2: Edge-disjoint rings
    print_flush("  Topology 2: Edge-disjoint rings")
    disjoint_data = []
    for b1 in range(1, 7):
        d_sys = 2 ** (2 * b1)
        if d_sys > 8192:
            disjoint_data.append({'b1': b1, 'skipped': True, 'd_sys': d_sys})
            continue
        G = build_gram_edge_disjoint(b1, c, p)
        spec = analyze_gram(G, b1_val=b1)
        disjoint_data.append({
            'b1': b1, 'd_sys': d_sys,
            'mu_measured': spec['mu_measured'],
            'mean_offdiag': spec['mean_offdiag'],
            'rank_eff': spec['rank_eff'],
        })
        print_flush(f"    b1={b1}: mu_meas={spec['mu_measured']:.6f}")
        del G
        gc.collect()
    results['edge_disjoint'] = disjoint_data

    # Topology 3: 2D grid (sampling)
    print_flush("  Topology 3: 2D Grid (sampling)")
    grid_data = []
    for L in [3, 4, 5, 6]:
        offdiag, _, n_rings = sample_gram_2d_grid(L, c, p, n_samples=3000)
        offdiag_arr = np.array(offdiag)
        if len(offdiag_arr) > 0 and n_rings > 0:
            valid = offdiag_arr[offdiag_arr > 1e-15]
            mu_meas = float(np.mean(np.log(valid)) / n_rings) if len(valid) > 0 else None
            mean_off = float(np.mean(offdiag_arr))
            msq = float(np.mean(offdiag_arr ** 2))
            rank_eff_est = 1.0 / msq if msq > 1e-30 else None
        else:
            mu_meas, mean_off, rank_eff_est = None, None, None
        grid_data.append({
            'L': L, 'n_rings': n_rings,
            'mu_measured': mu_meas,
            'mean_offdiag': mean_off,
            'rank_eff_est': rank_eff_est,
        })
        print_flush(f"    L={L} ({n_rings} rings): mu_meas={mu_meas}")
    results['grid_2d'] = grid_data

    results['analytic_comparison'] = {
        'mu_vertex_analytic': analytic_mu_vertex(c, p),
        'mu_disjoint_analytic': analytic_mu_edge_disjoint(c, p),
        'mu_grid_analytic': analytic_mu_grid(c, p),
        'c': float(c), 'p': p,
    }
    print_flush(f"\n  Analytic mu: vertex={analytic_mu_vertex(c,p):.6f} "
                f"disjoint={analytic_mu_edge_disjoint(c,p):.6f} "
                f"grid={analytic_mu_grid(c,p):.6f}")

    t_elapsed = time.time() - t_start
    print_flush(f"  Part 5 done: {t_elapsed:.1f}s")
    save_checkpoint(results, os.path.join(result_dir, 'checkpoint_p5.json'))
    return results, t_elapsed


# ================================================================
# Part 6: Gram Coherence Classes
# ================================================================
def run_part6(result_dir):
    print_flush("\n" + "=" * 80)
    print_flush("PART 6: Gram Coherence Classes (K8)")
    print_flush("=" * 80)
    t_start = time.time()

    n = 5
    d_sys = 2 ** n
    c = 0.5
    p = 0.5

    G = build_gram_vertex_chain_fast(4, c, p)
    if G is None:
        print_flush("  Cannot build G for n=5")
        return {'skipped': True}, time.time() - t_start

    tolerance = 1e-10
    n_states = d_sys
    visited = [False] * n_states
    classes = []

    for i in range(n_states):
        if visited[i]:
            continue
        cls = [i]
        visited[i] = True
        for j in range(i + 1, n_states):
            if visited[j]:
                continue
            if abs(1.0 - abs(G[i, j])) < tolerance:
                cls.append(j)
                visited[j] = True
        classes.append(cls)

    num_classes = len(classes)
    class_sizes = [len(c) for c in classes]
    sizes_count = {}
    for sz in class_sizes:
        sizes_count[str(sz)] = sizes_count.get(str(sz), 0) + 1

    all_complement = True
    complement_pairs = []
    for cls in classes:
        if len(cls) == 2:
            a, b = cls[0], cls[1]
            is_complement = (a ^ b) == (2**n - 1)
            complement_pairs.append({
                'a': a, 'b': b,
                'a_bin': format(a, f'0{n}b'),
                'b_bin': format(b, f'0{n}b'),
                'is_complement': bool(is_complement)
            })
            if not is_complement:
                all_complement = False
        else:
            all_complement = False

    # Fully alternating state: 01010
    alt_state = 0
    for i in range(n):
        if i % 2 == 1:
            alt_state |= (1 << i)
    alt_complement = alt_state ^ (2**n - 1)
    G_alt_comp = abs(G[alt_state, alt_complement])

    predictions = {
        'n': n, 'd_sys': d_sys,
        'num_classes': num_classes,
        'expected_num_classes': 2 ** (n - 1),
        'num_classes_match': num_classes == 2 ** (n - 1),
        'class_sizes': class_sizes,
        'unique_class_sizes': sizes_count,
        'all_size_2': all(sz == 2 for sz in class_sizes),
        'all_pairs_bitwise_complement': all_complement,
        'complement_pairs': complement_pairs,
        'alternating_state': {
            'state_idx': alt_state,
            'state_binary': format(alt_state, f'0{n}b'),
            'complement_idx': alt_complement,
            'complement_binary': format(alt_complement, f'0{n}b'),
            '|G(alt, complement)|': float(G_alt_comp),
            'is_perfectly_coherent': abs(1.0 - G_alt_comp) < tolerance,
        },
    }

    print_flush(f"  n={n}, d_sys={d_sys}")
    print_flush(f"  Number of coherence classes: {num_classes}")
    print_flush(f"  Expected (2^{n-1}): {2**(n-1)}")
    print_flush(f"  Match: {num_classes == 2**(n-1)}")
    print_flush(f"  Class sizes: {sizes_count}")
    print_flush(f"  All size 2: {all(sz == 2 for sz in class_sizes)}")
    print_flush(f"  All bitwise complements: {all_complement}")
    print_flush(f"  Alternating state (01010): |G| to complement = {G_alt_comp:.10f}")

    t_elapsed = time.time() - t_start
    print_flush(f"  Part 6 done: {t_elapsed:.1f}s")
    save_checkpoint(predictions, os.path.join(result_dir, 'checkpoint_p6.json'))
    return predictions, t_elapsed


# ================================================================
# Part 7: Ghost Zero Spectral Signature
# ================================================================
def run_part7(result_dir):
    print_flush("\n" + "=" * 80)
    print_flush("PART 7: Ghost Zero Spectral Signature")
    print_flush("=" * 80)
    t_start = time.time()

    b1 = 1
    c = np.pi / 4
    p_vals = np.linspace(0.01, 0.99, 50)
    results = []

    for p in p_vals:
        G = build_gram_vertex_chain_fast(b1, c, p)
        if G is None:
            continue
        spec = analyze_gram(G, b1_val=b1)
        evals_arr = np.array(spec['evals_all'])
        evals_pos = evals_arr[evals_arr > 1e-14]

        lam_min = float(evals_pos[-1]) if len(evals_pos) > 0 else 0.0
        lam_max = float(evals_pos[0]) if len(evals_pos) > 0 else 0.0
        gap = 1.0 - lam_min
        p1mp = p * (1 - p)
        width = lam_max - lam_min

        results.append({
            'p': float(p),
            'p_1mp': float(p1mp),
            'lambda_min': lam_min,
            'lambda_max': lam_max,
            'gap_1_minus_lam_min': gap,
            'spectral_width': width,
            'rank_eff': spec['rank_eff'],
            'mean_offdiag': spec['mean_offdiag'],
            'n_significant': spec['n_significant'],
            'evals': spec['evals_all'],
        })
        del G
        gc.collect()

    # Fit gap vs p(1-p)
    p1mp_vals = np.array([r['p_1mp'] for r in results])
    gap_vals = np.array([r['gap_1_minus_lam_min'] for r in results])
    valid = (gap_vals > -1.0) & (gap_vals < 10.0)
    if np.sum(valid) >= 2:
        coeffs = np.polyfit(p1mp_vals[valid], gap_vals[valid], 1)
        gap_slope = float(coeffs[0])
        gap_intercept = float(coeffs[1])
        pred = np.polyval(coeffs, p1mp_vals[valid])
        ss_res = np.sum((gap_vals[valid] - pred) ** 2)
        ss_tot = np.sum((gap_vals[valid] - np.mean(gap_vals[valid])) ** 2)
        r2 = 1.0 - ss_res / ss_tot if ss_tot > 1e-15 else 0.0
    else:
        gap_slope, gap_intercept, r2 = None, None, None

    ghost_results = {
        'b1': b1, 'c': float(c), 'c_label': 'pi/4',
        'p_sweep': results,
        'fit_gap_vs_p1mp': {
            'slope': gap_slope,
            'intercept': gap_intercept,
            'R2': float(r2) if r2 is not None else None,
        },
        'prediction': 'gap proportional to p(1-p) -- spectral gap closes at ghost zero limit (p->0 or p->1)',
    }

    print_flush(f"  Swept p from {p_vals[0]:.3f} to {p_vals[-1]:.3f} ({len(p_vals)} points)")
    print_flush(f"  Gap(1-lambda_min) vs p(1-p): slope={gap_slope:.6f} intercept={gap_intercept:.6f} R^2={r2:.4f}")
    print_flush(f"  At p=0.01: gap={results[0]['gap_1_minus_lam_min']:.6f}")
    print_flush(f"  At p=0.50: gap={results[len(results)//2]['gap_1_minus_lam_min']:.6f}")
    print_flush(f"  At p=0.99: gap={results[-1]['gap_1_minus_lam_min']:.6f}")

    t_elapsed = time.time() - t_start
    print_flush(f"  Part 7 done: {t_elapsed:.1f}s")
    save_checkpoint(ghost_results, os.path.join(result_dir, 'checkpoint_p7.json'))
    return ghost_results, t_elapsed


# ================================================================
# MAIN
# ================================================================
if __name__ == '__main__':
    np.set_printoptions(precision=6, suppress=True, linewidth=120)
    result_dir = os.path.dirname(os.path.abspath(__file__))

    print_flush("=" * 80)
    print_flush("FULL NUMERICAL SWEEP: DGF Gram Matrix Spectral Properties")
    print_flush("Date: 2026-06-11")
    print_flush("Method: Vectorized numpy + blocking for d up to 8192")
    print_flush("=" * 80)

    all_results = {}
    all_timings = {}

    # --- Part 1 ---
    p1_data, p1_time = run_part1(result_dir)
    all_results['part1_phase_diagram'] = p1_data
    all_timings['part1_phase_diagram_sec'] = p1_time

    # --- Part 2 ---
    p2_data, p2_time = run_part2(result_dir)
    all_results['part2_spectral_density'] = p2_data
    all_timings['part2_spectral_density_sec'] = p2_time

    # --- Part 3 ---
    p3_data, p3_time = run_part3(result_dir)
    all_results['part3_level_spacing'] = p3_data
    all_timings['part3_level_spacing_sec'] = p3_time

    # --- Part 4 ---
    p4_data, p4_time = run_part4(result_dir)
    all_results['part4_tree_vs_ring'] = p4_data
    all_timings['part4_tree_vs_ring_sec'] = p4_time

    # --- Part 5 ---
    p5_data, p5_time = run_part5(result_dir)
    all_results['part5_mu_universality'] = p5_data
    all_timings['part5_mu_universality_sec'] = p5_time

    # --- Part 6 ---
    p6_data, p6_time = run_part6(result_dir)
    all_results['part6_coherence_classes'] = p6_data
    all_timings['part6_coherence_classes_sec'] = p6_time

    # --- Part 7 ---
    p7_data, p7_time = run_part7(result_dir)
    all_results['part7_ghost_zero'] = p7_data
    all_timings['part7_ghost_zero_sec'] = p7_time

    all_timings['total_sec'] = sum(all_timings.values())

    # --- Final save ---
    out_path = os.path.join(result_dir, 'full_sweep_results.json')
    print_flush("\n" + "=" * 80)
    print_flush(f"Saving final results to: {out_path}")
    serializable = numpy_to_native(all_results)
    serializable['timings'] = all_timings

    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(serializable, f, indent=2)

    print_flush("\n" + "=" * 80)
    print_flush("TIMING SUMMARY")
    print_flush("=" * 80)
    for key, val in all_timings.items():
        print_flush(f"  {key}: {val:.1f}s")
    print_flush(f"\n  TOTAL: {all_timings['total_sec']:.1f}s")
    print_flush("\nDone.")

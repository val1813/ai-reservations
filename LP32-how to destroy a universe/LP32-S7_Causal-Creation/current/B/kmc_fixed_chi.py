"""
Fixed KMC with corrected local chi estimation + multi-L scaling.
Scene 4 fix: _local_chi now computes proper local edge-ensemble average
instead of single-edge product (which was always -1 for active edges).
"""
import numpy as np
import json, sys, os, time as walltime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kmc_simulation import DGFKMC

def local_chi_fixed(spins, L, i, j, window=2):
    """FIXED: compute chi as local edge-ensemble average of s_a*s_b,
    minus local magnetization product. This gives proper correlation
    that can be positive OR negative depending on local structure."""
    xi, yi = i // L, i % L
    xj, yj = j // L, j % L
    mx, my = (xi + xj) // 2, (yi + yj) // 2

    # Collect all spins in window
    s_vals = []
    for dx in range(-window, window+1):
        for dy in range(-window, window+1):
            nx = (mx + dx) % L
            ny = (my + dy) % L
            s_vals.append(spins[nx * L + ny])

    s_mean = np.mean(s_vals)

    # Collect edge products in window (horizontal + vertical neighbor pairs)
    edge_products = []
    for dx in range(-window, window+1):
        for dy in range(-window, window+1):
            nx = (mx + dx) % L
            ny = (my + dy) % L
            a = nx * L + ny
            # right neighbor
            b = nx * L + (ny + 1) % L
            edge_products.append(spins[a] * spins[b])
            # down neighbor
            c = ((nx + 1) % L) * L + ny
            edge_products.append(spins[a] * spins[c])

    s_s_mean = np.mean(edge_products)
    # Proper chi = <s_a s_b>_local - <s>_local^2
    return s_s_mean - s_mean * s_mean


def local_q_fixed(spins, L, i, window=2):
    """Local |0> fraction estimate."""
    xi, yi = i // L, i % L
    count_0 = 0
    count_total = 0
    for dx in range(-window, window+1):
        for dy in range(-window, window+1):
            nx = (xi + dx) % L
            ny = (yi + dy) % L
            if spins[nx * L + ny] == -1:
                count_0 += 1
            count_total += 1
    return count_0 / count_total


def run_chi_dependent_fixed(L=30, p0=0.5, mode='random',
                              window=2, seed=42, max_jumps=None,
                              measure_every=None, verbose=True):
    """FIXED chi-dependent KMC with proper local chi estimation."""
    if max_jumps is None:
        max_jumps = L * L * 3
    if measure_every is None:
        measure_every = max(1, max_jumps // 200)

    sim = DGFKMC(L=L, gamma0=1.0, seed=seed)
    sim.initialize(p0=p0, mode=mode)

    history = {'t': [], 'Q': [], 'chi_bar': [], 'R': [],
               'jumps': [], 'chi_local_mean': [], 'n_active': []}

    steps_since_last_jump = 0
    next_measure = 0
    max_steps = max_jumps * 50

    if verbose:
        Q0 = np.mean(sim.spins == -1)
        print(f"  FIXED chi-dependent KMC: L={L}, p0={p0}, Q0={Q0:.4f}, "
              f"active={len(sim._active_edge_set)}")

    for step_count in range(max_steps):
        active = list(sim._active_edge_set)
        if len(active) == 0:
            steps_since_last_jump += 1
            if steps_since_last_jump > max(L*L, 2000):
                break
            continue

        # Compute chi-dependent rates using FIXED local chi
        rates = []
        local_chis = []
        for i_edge, j_edge in active:
            qi = local_q_fixed(sim.spins, L, i_edge, window)
            qj = local_q_fixed(sim.spins, L, j_edge, window)
            chi_loc = local_chi_fixed(sim.spins, L, i_edge, j_edge, window)
            local_chis.append(chi_loc)
            # Rate = gamma0 * max(0, q_j*(1-q_i) - chi/4)
            rate = sim.gamma0 * max(0.0, qj * (1 - qi) - chi_loc / 4.0)
            rates.append(rate)

        rates = np.array(rates)
        R_total = rates.sum()
        if R_total <= 0:
            steps_since_last_jump += 1
            if steps_since_last_jump > max(L*L, 2000):
                break
            continue

        steps_since_last_jump = 0
        dt = sim.rng.exponential(1.0 / R_total)
        sim.t += dt

        # Choose edge proportional to rate
        cumsum = rates.cumsum()
        idx = np.searchsorted(cumsum, sim.rng.random() * R_total)
        i_edge, j_edge = active[idx]
        sim.spins[j_edge] = 1
        sim.total_jumps += 1
        sim._update_active_edges_after_jump(i_edge, j_edge)

        if sim.total_jumps >= next_measure:
            Q, chi_bar, R = sim.measure_observables()
            history['t'].append(sim.t)
            history['Q'].append(Q)
            history['chi_bar'].append(chi_bar)
            history['R'].append(R)
            history['jumps'].append(sim.total_jumps)
            history['chi_local_mean'].append(float(np.mean(local_chis)))
            history['n_active'].append(len(active))
            next_measure += measure_every

        if sim.total_jumps >= max_jumps:
            break

    # Final measurement
    Q, chi_bar, R = sim.measure_observables()
    history['t'].append(sim.t)
    history['Q'].append(Q)
    history['chi_bar'].append(chi_bar)
    history['R'].append(R)
    history['jumps'].append(sim.total_jumps)
    history['final_jumps'] = int(sim.total_jumps)
    history['final_Q'] = float(Q)
    history['final_chi'] = float(chi_bar)

    if verbose:
        print(f"    Done: {sim.total_jumps} jumps, Q_final={Q:.4f}, "
              f"chi_final={chi_bar:.4f}")

    return history


def run_uniform_rate(L=30, p0=0.5, mode='random', seed=42,
                     max_jumps=None, measure_every=None, verbose=False):
    """Run uniform-rate KMC (scenes 1-3 baseline)."""
    if max_jumps is None:
        max_jumps = L * L * 3
    if measure_every is None:
        measure_every = max(1, max_jumps // 200)

    sim = DGFKMC(L=L, gamma0=1.0, seed=seed)
    sim.initialize(p0=p0, mode=mode)

    history = {'t': [], 'Q': [], 'chi_bar': [], 'R': [],
               'jumps': [], 'n_active': []}
    steps_since_last_jump = 0
    next_measure = 0

    for step_count in range(max_jumps * 20):
        jumped = sim.step()
        if not jumped:
            steps_since_last_jump += 1
            if steps_since_last_jump > max(L*L, 2000):
                break
        else:
            steps_since_last_jump = 0

        if sim.total_jumps >= next_measure:
            Q, chi_bar, R = sim.measure_observables()
            history['t'].append(sim.t)
            history['Q'].append(Q)
            history['chi_bar'].append(chi_bar)
            history['R'].append(R)
            history['jumps'].append(sim.total_jumps)
            history['n_active'].append(len(sim._active_edge_set))
            next_measure += measure_every

        if sim.total_jumps >= max_jumps:
            break

    Q, chi_bar, R = sim.measure_observables()
    history['final_jumps'] = int(sim.total_jumps)
    history['final_Q'] = float(Q)
    history['final_chi'] = float(chi_bar)
    return history


if __name__ == '__main__':
    L_values = [20, 30, 50]
    if len(sys.argv) > 1:
        L_values = [int(x) for x in sys.argv[1:]]

    base_dir = os.path.dirname(os.path.abspath(__file__))
    all_results = {}

    print("=" * 70)
    print("FIXED χ-dependent KMC + Multi-L Scaling")
    print(f"L values: {L_values}")
    print("=" * 70)

    for L in L_values:
        print(f"\n{'='*70}")
        print(f"L = {L} ({L*L} sites)")
        print(f"{'='*70}")

        t0 = walltime.time()

        # Uniform rate (baseline)
        print("  [1/3] Uniform rate baseline...")
        h_uniform = run_uniform_rate(L=L, p0=0.5, mode='random',
                                     max_jumps=L*L*2, seed=42+hash(L)%1000)

        # Chi-dependent (fixed) - multiple seeds for error bars
        print("  [2/3] FIXED chi-dependent (3 seeds)...")
        chi_hists = []
        for s in range(3):
            seed = 100 + hash(L) % 1000 + s*137
            h = run_chi_dependent_fixed(L=L, p0=0.5, mode='random',
                                         window=2, seed=seed, max_jumps=L*L*2)
            chi_hists.append(h)

        # Compute chi-dependent ensemble averages
        min_jumps = min(h['final_jumps'] for h in chi_hists)
        common_jumps = np.linspace(0, min_jumps, 100).astype(int)
        chi_ens = {'jumps': common_jumps.tolist(),
                   'Q_mean': [], 'Q_std': [],
                   'chi_mean': [], 'chi_std': []}
        for j in common_jumps:
            q_vals, c_vals = [], []
            for h in chi_hists:
                hj = np.array(h['jumps'])
                idx = np.searchsorted(hj, j)
                if idx >= len(hj): idx = len(hj) - 1
                q_vals.append(h['Q'][idx])
                c_vals.append(h['chi_bar'][idx])
            chi_ens['Q_mean'].append(float(np.mean(q_vals)))
            chi_ens['Q_std'].append(float(np.std(q_vals)))
            chi_ens['chi_mean'].append(float(np.mean(c_vals)))
            chi_ens['chi_std'].append(float(np.std(c_vals)))

        all_results[f'L{L}'] = {
            'L': L, 'N': L*L,
            'uniform': h_uniform,
            'chi_dependent_sample': chi_hists[0],
            'chi_dependent_ensemble': chi_ens,
        }

        elapsed = walltime.time() - t0
        print(f"  [3/3] L={L} done in {elapsed:.1f}s")
        print(f"    Uniform:     Q_final={h_uniform['final_Q']:.4f}")
        print(f"    Chi-dep(avg): Q_final={chi_ens['Q_mean'][-1]:.4f} "
              f"+- {chi_ens['Q_std'][-1]:.4f}")

    # Scaling analysis
    print(f"\n{'='*70}")
    print("SCALING ANALYSIS: χ_max vs L")
    print(f"{'='*70}")
    print(f"{'L':>6s} {'N':>8s} {'Q_final(uniform)':>16s} "
          f"{'Q_final(chi-dep)':>16s} {'χ_max':>10s}")
    print("-" * 60)

    for L in L_values:
        r = all_results[f'L{L}']
        q_u = r['uniform']['final_Q']
        q_c = r['chi_dependent_ensemble']['Q_mean'][-1]
        chi_max = max(r['uniform']['chi_bar']) if r['uniform']['chi_bar'] else 0
        print(f"{L:>6d} {L*L:>8d} {q_u:>16.4f} {q_c:>16.4f} {chi_max:>10.4f}")

    # Save
    def convert(obj):
        if isinstance(obj, dict):
            return {k: convert(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [convert(v) for v in obj]
        elif isinstance(obj, (np.integer,)): return int(obj)
        elif isinstance(obj, (np.floating,)): return float(obj)
        elif isinstance(obj, np.ndarray): return obj.tolist()
        return obj

    outpath = f"{base_dir}/kmc_fixed_chi_results.json"
    with open(outpath, 'w') as f:
        json.dump(convert(all_results), f)
    print(f"\nSaved: {outpath}")

"""
Multi-simulation KMC runner for B博士 Round 3.
Runs multiple ICs, ensemble averages, and chi-dependent rate simulations.
"""

import numpy as np
import json
import time as walltime
import sys
import os
# Add current directory for import
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kmc_simulation import DGFKMC


def run_single_realization(L=30, p0=0.5, mode='random', max_jumps=None,
                           measure_every=None, seed=None):
    """Run one realization and return history dict."""
    if max_jumps is None:
        max_jumps = L * L  # at most all sites become |1>
    if measure_every is None:
        measure_every = max(1, max_jumps // 100)

    sim = DGFKMC(L=L, gamma0=1.0, seed=seed)
    sim.initialize(p0=p0, mode=mode)

    history = {'t': [], 'Q': [], 'chi_bar': [], 'R': [], 'jumps': []}
    steps_since_last_jump = 0
    next_measure = 0
    max_steps = max_jumps * 20  # allow dead steps

    for step_count in range(max_steps):
        jumped = sim.step()

        if not jumped:
            steps_since_last_jump += 1
            if steps_since_last_jump > max(L*L, 1000):
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
            next_measure += measure_every

        if sim.total_jumps >= max_jumps:
            break

    # Record final state
    Q, chi_bar, R = sim.measure_observables()
    history['t'].append(sim.t)
    history['Q'].append(Q)
    history['chi_bar'].append(chi_bar)
    history['R'].append(R)
    history['jumps'].append(sim.total_jumps)
    history['final_spins'] = sim.spins.copy().tolist()
    history['total_jumps'] = int(sim.total_jumps)

    return history


def run_ensemble(L=30, p0=0.5, mode='random', n_realizations=50,
                 max_jumps=None, measure_every=None, base_seed=42):
    """Run ensemble of realizations and compute averages."""
    if max_jumps is None:
        max_jumps = L * L

    all_histories = []
    for k in range(n_realizations):
        seed = base_seed + k
        hist = run_single_realization(L=L, p0=p0, mode=mode,
                                       max_jumps=max_jumps,
                                       measure_every=measure_every,
                                       seed=seed)
        all_histories.append(hist)
        if k % 10 == 0:
            print(f"  Realization {k+1}/{n_realizations} done ({hist['total_jumps']} jumps)")

    # Ensemble average: interpolate all histories to common jump grid
    max_jumps_achieved = min(h['total_jumps'] for h in all_histories)
    common_jumps = np.linspace(0, max_jumps_achieved, 100)
    common_jumps = common_jumps.astype(int)

    ensemble = {'jumps': common_jumps.tolist(), 'Q_mean': [], 'Q_std': [],
                'chi_mean': [], 'chi_std': [], 'R_mean': [], 'R_std': []}

    for j in common_jumps:
        q_vals = []
        chi_vals = []
        r_vals = []
        for hist in all_histories:
            # Find nearest measurement
            hj = np.array(hist['jumps'])
            idx = np.searchsorted(hj, j)
            if idx >= len(hj):
                idx = len(hj) - 1
            q_vals.append(hist['Q'][idx])
            chi_vals.append(hist['chi_bar'][idx])
            r_vals.append(hist['R'][idx])

        ensemble['Q_mean'].append(float(np.mean(q_vals)))
        ensemble['Q_std'].append(float(np.std(q_vals)))
        ensemble['chi_mean'].append(float(np.mean(chi_vals)))
        ensemble['chi_std'].append(float(np.std(chi_vals)))
        ensemble['R_mean'].append(float(np.mean(r_vals)))
        ensemble['R_std'].append(float(np.std(r_vals)))

    return ensemble, all_histories


def compute_local_chi(spins, L, i, j):
    """Compute local chi_ij from single config using local neighborhood."""
    # Use 5x5 window around i and j for local statistics
    window = 2
    s_mean_local = 0
    count = 0
    xi, yi = i // L, i % L
    for dx in range(-window, window+1):
        for dy in range(-window, window+1):
            nx = (xi + dx) % L
            ny = (yi + dy) % L
            s_mean_local += spins[nx * L + ny]
            count += 1
    s_mean_local /= count
    # chi_ij = s_i*s_j - s_mean_local^2 (approximate)
    return spins[i] * spins[j] - s_mean_local * s_mean_local


def run_chi_dependent_single(L=30, p0=0.5, mode='random',
                              window=3, seed=42, verbose=True):
    """Run KMC with chi-dependent jump rates.

    Instead of constant gamma0 per active edge, use:
    rate = gamma0 * max(0, q_j*(1-q_i) - chi_ij/4)
    where q_i, q_j are local estimates and chi_ij is local correlation.
    """
    sim = DGFKMC(L=L, gamma0=1.0, seed=seed)
    sim.initialize(p0=p0, mode=mode)

    max_jumps = L * L * 2
    history = {'t': [], 'Q': [], 'chi_bar': [], 'R': [], 'jumps': [],
               'local_chi_mean': []}
    measure_every = max(1, max_jumps // 200)

    steps_since_last_jump = 0
    next_measure = 0
    max_steps = max_jumps * 50

    if verbose:
        print(f"Chi-dependent KMC: L={L}, p0={p0}, mode={mode}, window={window}")
        print(f"Initial active edges: {len(sim._active_edge_set)}")
        print(f"Initial Q: {np.mean(sim.spins == -1):.4f}")

    for step_count in range(max_steps):
        # Rebuild active edge list
        active = list(sim._active_edge_set)
        if len(active) == 0:
            steps_since_last_jump += 1
            if steps_since_last_jump > max(L*L, 2000):
                break
            if sim.total_jumps >= next_measure:
                Q, chi_bar, R = sim.measure_observables()
                history['t'].append(sim.t)
                history['Q'].append(Q)
                history['chi_bar'].append(chi_bar)
                history['R'].append(R)
                history['jumps'].append(sim.total_jumps)
                history['local_chi_mean'].append(0.0)
                next_measure += measure_every
            continue

        # Compute rates for each active edge using local chi estimate
        rates = []
        for i, j in active:
            # Local q estimates from window
            qi_local = _local_q(sim.spins, L, i, window)
            qj_local = _local_q(sim.spins, L, j, window)
            chi_local = _local_chi(sim.spins, L, i, j, window)
            rate = sim.gamma0 * max(0.0, qj_local * (1 - qi_local) - chi_local / 4.0)
            rates.append(rate)

        rates = np.array(rates)
        R_total = rates.sum()
        if R_total <= 0:
            steps_since_last_jump += 1
            if steps_since_last_jump > max(L*L, 2000):
                break
            continue

        steps_since_last_jump = 0

        # Time increment
        dt = sim.rng.exponential(1.0 / R_total)
        sim.t += dt

        # Choose edge proportional to rate
        cumsum = rates.cumsum()
        idx = np.searchsorted(cumsum, sim.rng.random() * R_total)
        i, j = active[idx]

        # Execute jump
        sim.spins[j] = 1
        sim.total_jumps += 1
        sim.jump_times.append(sim.t)
        sim._update_active_edges_after_jump(i, j)

        if sim.total_jumps >= next_measure:
            Q, chi_bar, R = sim.measure_observables()
            history['t'].append(sim.t)
            history['Q'].append(Q)
            history['chi_bar'].append(chi_bar)
            history['R'].append(R)
            history['jumps'].append(sim.total_jumps)
            # Average local chi over all edges
            local_chis = []
            for ii, jj in active:
                local_chis.append(_local_chi(sim.spins, L, ii, jj, window))
            history['local_chi_mean'].append(float(np.mean(local_chis)) if local_chis else 0.0)
            next_measure += measure_every

            if verbose and sim.total_jumps % (measure_every * 20) == 0:
                print(f"  jumps={sim.total_jumps:>6d}  t={sim.t:.4f}  Q={Q:.4f}  "
                      f"chi_bar={chi_bar:.4f}  R={R:.4f}")

        if sim.total_jumps >= max_jumps:
            break

    if verbose:
        print(f"Done: {sim.total_jumps} jumps, final Q={history['Q'][-1]:.4f}, "
              f"chi_bar={history['chi_bar'][-1]:.4f}")

    return sim, history


def _local_q(spins, L, i, window):
    """Estimate local q = fraction of |0> in window around i."""
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


def _local_chi(spins, L, i, j, window):
    """Estimate local chi_ij from local statistics."""
    xi, yi = i // L, i % L
    xj, yj = j // L, j % L
    # Use window around midpoint
    mx, my = (xi + xj) // 2, (yi + yj) // 2

    # Compute local means
    s_vals = []
    for dx in range(-window, window+1):
        for dy in range(-window, window+1):
            nx = (mx + dx) % L
            ny = (my + dy) % L
            s_vals.append(spins[nx * L + ny])

    s_mean = np.mean(s_vals)
    # Local chi = s_i*s_j - s_mean*s_mean (approximate, ignoring s_i*s_j correlation with mean)
    return spins[i] * spins[j] - s_mean * s_mean


if __name__ == '__main__':
    L = 30
    import os
    base_dir = os.path.dirname(os.path.abspath(__file__))

    print("=" * 70)
    print("B博士 Round 3 — Multi-Scenario KMC Simulations")
    print("=" * 70)

    results = {}

    # === SCENARIO 1: IC-A p0=0.5, ensemble ===
    print("\n" + "=" * 70)
    print("SCENARIO 1: IC-A (random, p0=0.5), 50-realization ensemble")
    print("=" * 70)
    t0 = walltime.time()
    ens1, hists1 = run_ensemble(L=L, p0=0.5, mode='random', n_realizations=50,
                                 max_jumps=L*L, base_seed=100)
    results['scenario1_ensemble'] = ens1
    # Keep one sample trajectory
    results['scenario1_sample'] = {
        't': hists1[0]['t'], 'Q': hists1[0]['Q'],
        'chi_bar': hists1[0]['chi_bar'], 'R': hists1[0]['R'],
        'jumps': hists1[0]['jumps']
    }
    print(f"  Time: {walltime.time()-t0:.1f}s")
    print(f"  Final Q_mean: {ens1['Q_mean'][-1]:.4f} +- {ens1['Q_std'][-1]:.4f}")
    print(f"  Final chi_mean: {ens1['chi_mean'][-1]:.4f} +- {ens1['chi_std'][-1]:.4f}")

    # === SCENARIO 2: IC-A p0=0.9, ensemble ===
    print("\n" + "=" * 70)
    print("SCENARIO 2: IC-A (random, p0=0.9), 50-realization ensemble")
    print("=" * 70)
    t0 = walltime.time()
    ens2, hists2 = run_ensemble(L=L, p0=0.9, mode='random', n_realizations=50,
                                 max_jumps=L*L, base_seed=200)
    results['scenario2_ensemble'] = ens2
    results['scenario2_sample'] = {
        't': hists2[0]['t'], 'Q': hists2[0]['Q'],
        'chi_bar': hists2[0]['chi_bar'], 'R': hists2[0]['R'],
        'jumps': hists2[0]['jumps']
    }
    print(f"  Time: {walltime.time()-t0:.1f}s")
    print(f"  Final Q_mean: {ens2['Q_mean'][-1]:.4f} +- {ens2['Q_std'][-1]:.4f}")
    print(f"  Final chi_mean: {ens2['chi_mean'][-1]:.4f} +- {ens2['chi_std'][-1]:.4f}")

    # === SCENARIO 3: IC-B anticorrelated ===
    print("\n" + "=" * 70)
    print("SCENARIO 3: IC-B (anticorrelated, p0=0.5), 20-realization ensemble")
    print("=" * 70)
    t0 = walltime.time()
    ens3, hists3 = run_ensemble(L=L, p0=0.5, mode='anticorrelated', n_realizations=20,
                                 max_jumps=L*L, base_seed=300)
    results['scenario3_ensemble'] = ens3
    results['scenario3_sample'] = {
        't': hists3[0]['t'], 'Q': hists3[0]['Q'],
        'chi_bar': hists3[0]['chi_bar'], 'R': hists3[0]['R'],
        'jumps': hists3[0]['jumps']
    }
    print(f"  Time: {walltime.time()-t0:.1f}s")
    print(f"  Final Q_mean: {ens3['Q_mean'][-1]:.4f} +- {ens3['Q_std'][-1]:.4f}")
    print(f"  Final chi_mean: {ens3['chi_mean'][-1]:.4f} +- {ens3['chi_std'][-1]:.4f}")

    # === SCENARIO 4: Chi-dependent rates ===
    print("\n" + "=" * 70)
    print("SCENARIO 4: Chi-dependent jump rates, p0=0.5")
    print("=" * 70)
    t0 = walltime.time()
    sim4, hist4 = run_chi_dependent_single(L=L, p0=0.5, mode='random',
                                            window=2, seed=42, verbose=True)
    results['scenario4_chidependent'] = {
        't': hist4['t'], 'Q': hist4['Q'], 'chi_bar': hist4['chi_bar'],
        'R': hist4['R'], 'jumps': hist4['jumps'],
        'local_chi_mean': hist4['local_chi_mean']
    }
    print(f"  Time: {walltime.time()-t0:.1f}s")

    # === Save results ===
    outpath = f"{base_dir}/kmc_multi_results_L{L}.json"
    # Convert numpy types for JSON
    def convert(obj):
        if isinstance(obj, dict):
            return {k: convert(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [convert(v) for v in obj]
        elif isinstance(obj, (np.integer,)):
            return int(obj)
        elif isinstance(obj, (np.floating,)):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        return obj

    results = convert(results)
    with open(outpath, 'w') as f:
        json.dump(results, f)
    print(f"\nAll results saved to {outpath}")

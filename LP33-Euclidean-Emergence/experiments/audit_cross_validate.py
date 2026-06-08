"""
LP33 Simulation Audit & Cross-Validation
========================================
1. Validate Myrheim-Meyer against known analytical result (random sprinkling)
2. Test parameter sensitivity (p_spont, J, N, v_eff)
3. 4D lattice test for P3
4. Adversarial check of all 5 predictions
"""

import numpy as np
from collections import defaultdict
import sys
sys.path.insert(0, '.')
from dgf_causal_set_sim import DGFNetwork, GAMMA_D, compute_myrheim_meyer

# ============================================================
# Test 1: Myrheim-Meyer Validation (random sprinkling benchmark)
# ============================================================
print("=" * 60)
print("AUDIT 1: Myrheim-Meyer Validation (Random Sprinkling)")
print("=" * 60)

def random_sprinkling_myrheim_meyer(D, M, L=10, T=100, seed=42):
    """Simulate random sprinkling into D-dim Minkowski spacetime.
    Points uniformly in [0,L]^(D-1) x [0,T].
    Causal relation: (t_b - t_a)^2 >= sum_i (x_i^b - x_i^a)^2.
    """
    rng = np.random.RandomState(seed)
    coords = rng.rand(M, D)  # last coord = time, rest = space
    coords[:, -1] *= T       # scale time
    coords[:, :-1] *= L       # scale space

    R = 0
    for a in range(M):
        for b in range(a+1, M):
            dt = coords[b, -1] - coords[a, -1]
            if dt > 0:
                ds2 = dt**2 - np.sum((coords[b, :-1] - coords[a, :-1])**2)
                if ds2 >= 0:  # timelike or lightlike
                    R += 1

    ratio = R / (M * M)
    return ratio, R, M

# Test random sprinkling for D=2,3,4
print("\nRandom sprinkling into Minkowski spacetime (M=500, L=10, T=100):")
for D in [2, 3, 4]:
    ratios = []
    for trial in range(5):
        ratio, R, M = random_sprinkling_myrheim_meyer(D, 500, L=10, T=100, seed=42+trial)
        ratios.append(ratio)
    mean_r = np.mean(ratios)
    gamma = GAMMA_D[D]
    err = abs(mean_r - gamma)
    status = "PASS" if err < 0.05 else "WARN" if err < 0.10 else "FAIL"
    print(f"  D={D}: R/M^2={mean_r:.4f} +/- {np.std(ratios):.4f}, "
          f"Gamma_{D}={gamma:.3f}, err={err:.3f} [{status}]")

# ============================================================
# Test 2: Parameter Sensitivity
# ============================================================
print("\n" + "=" * 60)
print("AUDIT 2: Parameter Sensitivity")
print("=" * 60)

base_cfg = {'N_qubits': 100, 'D_space': 4, 'p_spont': 0.001,
            'coupling_strength': 0.3, 'max_steps': 3000, 'n_trials': 3}

def test_sensitivity(param_name, values):
    print(f"\n--- Varying {param_name} ---")
    results = []
    for val in values:
        cfg = base_cfg.copy()
        cfg[param_name] = val
        eta_vals = []
        align_vals = []
        for trial in range(cfg['n_trials']):
            net = DGFNetwork(cfg['N_qubits'], cfg['D_space'],
                           cfg['p_spont'], cfg['coupling_strength'],
                           seed=42 + trial + int(val * 100))
            net.run(cfg['max_steps'])
            eta_vals.append(net.compute_time_direction_uniqueness())
            align_vals.append(net.compute_alignment())

        mean_eta = np.mean(eta_vals)
        mean_align = np.mean(align_vals) if align_vals else 0
        print(f"  {param_name}={val}: eta={mean_eta:.3f}+/-{np.std(eta_vals):.3f}, "
              f"align={mean_align:.3f}+/-{np.std(align_vals):.3f}")
        results.append((val, mean_eta, mean_align))
    return results

# Test coupling strength sensitivity
test_sensitivity('coupling_strength', [0.1, 0.3, 0.5, 0.8])

# Test spontaneous probability sensitivity
test_sensitivity('p_spont', [0.0005, 0.001, 0.005, 0.01])

# Test N sensitivity for P4 (dimension dependence) at different N
print("\n--- P4 Robustness: Dimension dependence at N=50,100,200 ---")
for N in [50, 100, 200]:
    eta_d = {}
    for D in [2, 3, 4]:
        cfg = {'N_qubits': N, 'D_space': D, 'p_spont': 0.001,
               'coupling_strength': 0.3, 'max_steps': 3000, 'n_trials': 3}
        eta_vals = []
        for trial in range(cfg['n_trials']):
            net = DGFNetwork(N, D, cfg['p_spont'], cfg['coupling_strength'],
                           seed=42 + trial)
            net.run(cfg['max_steps'])
            eta_vals.append(net.compute_time_direction_uniqueness())
        eta_d[D] = np.mean(eta_vals)

    p4 = eta_d[4] > eta_d[3] > eta_d[2]
    p5 = (eta_d[3] - eta_d[2]) > (eta_d[4] - eta_d[3])
    print(f"  N={N}: D=2:{eta_d[2]:.3f} D=3:{eta_d[3]:.3f} D=4:{eta_d[4]:.3f} "
          f"P4:{'PASS' if p4 else 'FAIL'} P5:{'PASS' if p5 else 'FAIL'}")

# ============================================================
# Test 3: D=2 eta degeneracy explanation
# ============================================================
print("\n" + "=" * 60)
print("AUDIT 3: D=2 eta=1.000 degeneracy check")
print("=" * 60)
# In D=2, only 2 directions exist. If both get equal Borda scores, eta=0.
# If one dominates, eta = (1 - 0.5)/0.5 = 1.0
# Check: is eta=1.000 always, or can it vary?
for trial in range(10):
    net = DGFNetwork(50, 2, 0.001, 0.3, seed=100+trial)
    net.run(3000)
    eta = net.compute_time_direction_uniqueness()
    # Count how many qubits picked each direction
    determined = np.where(net.states == 1)[0]
    if len(determined) >= 2:
        primary = np.argmax(np.abs(net.directions[determined]), axis=1)
        counts = np.bincount(primary, minlength=2)
        print(f"  Trial {trial}: eta={eta:.3f}, dir_counts={counts}, "
              f"dominance={max(counts)/sum(counts):.2f}")

# ============================================================
# Test 4: Adversarial - can we break P4/P5?
# ============================================================
print("\n" + "=" * 60)
print("AUDIT 4: Adversarial Tests")
print("=" * 60)

# Test 4a: Zero coupling (no alignment) - should eta still be monotonic?
print("\n--- Zero coupling (J=0): no SRC, spontaneous only ---")
for D in [2, 3, 4]:
    eta_vals = []
    for trial in range(5):
        net = DGFNetwork(100, D, 0.001, 0.0, seed=50+trial)
        net.run(3000)
        eta_vals.append(net.compute_time_direction_uniqueness())
    print(f"  D={D}: eta={np.mean(eta_vals):.3f}+/-{np.std(eta_vals):.3f}")

# Test 4b: Very small N (N=10) - does P4 still hold?
print("\n--- Tiny network (N=10): does P4 survive? ---")
for D in [2, 3, 4]:
    eta_vals = []
    for trial in range(10):
        net = DGFNetwork(10, D, 0.01, 0.3, seed=200+trial)
        net.run(2000)
        eta_vals.append(net.compute_time_direction_uniqueness())
    print(f"  D={D}: eta={np.mean(eta_vals):.3f}+/-{np.std(eta_vals):.3f}")

# ============================================================
# Test 5: Myrheim-Meyer with tuned v_eff
# ============================================================
print("\n" + "=" * 60)
print("AUDIT 5: P3 - Can we recover d=4 with tuned v_eff or lattice?")
print("=" * 60)

# Test 5a: Try different v_eff values on random graph
print("\n--- Random graph (N=200), varying v_eff ---")
for v_eff in [0.1, 0.3, 0.5, 1.0, 2.0]:
    net = DGFNetwork(200, 4, 0.002, 0.4, seed=42)
    net.run(5000)

    # Compute causal relations with different v_eff
    times = np.array([e['time'] for e in net.events])
    qubits = np.array([e['qubit'] for e in net.events])
    M = len(net.events)

    # Precompute graph distances
    dists = {}
    for source in range(net.N):
        dmap = {source: 0}
        queue = [source]
        while queue:
            node = queue.pop(0)
            for nb in net.adjacency.get(node, []):
                if nb not in dmap:
                    dmap[nb] = dmap[node] + 1
                    queue.append(nb)
        for target, d in dmap.items():
            dists[(source, target)] = d

    R = 0
    for a in range(M):
        for b in range(a+1, M):
            dt = times[b] - times[a]
            if dt > 0:
                d_g = dists.get((qubits[a], qubits[b]), float('inf'))
                if d_g <= v_eff * dt:
                    R += 1

    ratio = R / (M * M)
    best_d = min(GAMMA_D, key=lambda d: abs(ratio - GAMMA_D[d]))
    print(f"  v_eff={v_eff}: M={M}, R/M^2={ratio:.4f}, MM-d={best_d}, "
          f"dist_to_Gamma4={abs(ratio-0.201):.4f}")

# Test 5b: 4D lattice topology with determination dynamics
print("\n--- 4D Lattice (N=4^4=256), determination dynamics ---")
# Build 4D lattice adjacency
def build_lattice_adj(n_per_dim=4):
    N = n_per_dim ** 4
    adj = defaultdict(list)
    for i in range(n_per_dim):
        for j in range(n_per_dim):
            for k in range(n_per_dim):
                for l in range(n_per_dim):
                    idx = i*n_per_dim**3 + j*n_per_dim**2 + k*n_per_dim + l
                    for di,dj,dk,dl in [(1,0,0,0),(-1,0,0,0),(0,1,0,0),(0,-1,0,0),
                                         (0,0,1,0),(0,0,-1,0),(0,0,0,1),(0,0,0,-1)]:
                        ni,nj,nk,nl = i+di, j+dj, k+dk, l+dl
                        if all(0<=x<n_per_dim for x in [ni,nj,nk,nl]):
                            nidx = ni*n_per_dim**3 + nj*n_per_dim**2 + nk*n_per_dim + nl
                            adj[idx].append(nidx)
    return adj, N

adj_4d, N_4d = build_lattice_adj(4)

# Use DGFNetwork but override adjacency
net_4d = DGFNetwork(N_4d, 4, 0.002, 0.4, seed=42)
net_4d.adjacency = adj_4d
net_4d.run(5000)

# Compute Myrheim-Meyer with 4D lattice graph distances
times = np.array([e['time'] for e in net_4d.events])
qubits = np.array([e['qubit'] for e in net_4d.events])
M = len(net_4d.events)

dists_4d = {}
for source in range(N_4d):
    dmap = {source: 0}
    queue = [source]
    while queue:
        node = queue.pop(0)
        for nb in adj_4d.get(node, []):
            if nb not in dmap:
                dmap[nb] = dmap[node] + 1
                queue.append(nb)
    for target, d in dmap.items():
        dists_4d[(source, target)] = d

for v_eff in [0.3, 0.5, 0.7, 1.0, 1.5]:
    R = 0
    for a in range(M):
        for b in range(a+1, M):
            dt = times[b] - times[a]
            if dt > 0:
                d_g = dists_4d.get((qubits[a], qubits[b]), float('inf'))
                if d_g <= v_eff * dt:
                    R += 1
    ratio = R / (M * M)
    best_d = min(GAMMA_D, key=lambda d: abs(ratio - GAMMA_D[d]))
    dist_to_4 = abs(ratio - 0.201)
    print(f"  v_eff={v_eff}: M={M}, R/M^2={ratio:.4f}, MM-d={best_d}, "
          f"dist_to_Gamma4={dist_to_4:.4f} {'<- CLOSE!' if dist_to_4 < 0.05 else ''}")

print("\n" + "=" * 60)
print("AUDIT COMPLETE")
print("=" * 60)

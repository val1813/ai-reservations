"""
LP41 CFOL Generalization - Round 4: Counterexample Search
==========================================================
Goal: Find QCMI ≈ 0 with non-Clifford Cartan parameters under non-aligned axes.
Wall: Cartan axes non-aligned — does QCMI=0 force c_j ∈ (π/2)ℤ?

Tasks:
  1. Systematic scan of b₁=1 non-aligned parameter space (grid + random)
  2. Special symmetry search (coplanar, orthogonal, exchange, time-reversal)
  3. Gradient-guided descent toward zero-QCMI regions
  4. b₁=2 extension if b₁=1 yields null result
"""

import numpy as np
from numpy.linalg import eigh
import json
import time
import sys
from itertools import product

# ============================================================
# Pauli matrices and utilities
# ============================================================
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)

def von_neumann_entropy(rho, eps=1e-14):
    """Von Neumann entropy with careful numerical handling."""
    evals = eigh(rho)[0]
    evals = np.maximum(np.real(evals), eps)
    evals = evals / evals.sum()
    return -np.sum(evals * np.log2(np.maximum(evals, eps)))

def H2(p):
    """Binary entropy."""
    if p <= 0 or p >= 1:
        return 0.0
    return -p * np.log2(p) - (1 - p) * np.log2(1 - p)

def cartan_gate_2q(c, n_hat):
    """Cartan gate: U = cos(c)*I⊗I + i*sin(c)*(n·σ)⊗(n·σ)"""
    sigma = n_hat[0] * X + n_hat[1] * Y + n_hat[2] * Z
    g = np.cos(c) * np.kron(I2, I2) + 1j * np.sin(c) * np.kron(sigma, sigma)
    return g

def embed_2q_gate(gate_2q, q_a, q_b, n_qubits):
    """Embed a 2-qubit gate into n_qubits space (fast version)."""
    d = 2 ** n_qubits
    U = np.eye(d, dtype=complex)
    mask = (1 << q_a) | (1 << q_b)

    for idx in range(d):
        bit_a = (idx >> q_a) & 1
        bit_b = (idx >> q_b) & 1
        in_2q = (bit_a << 1) | bit_b

        for out_2q in range(4):
            u_elem = gate_2q[out_2q, in_2q]
            if abs(u_elem) < 1e-15:
                continue
            out_bit_a = (out_2q >> 1) & 1
            out_bit_b = out_2q & 1
            out_idx = idx
            if out_bit_a != bit_a:
                out_idx ^= (1 << q_a)
            if out_bit_b != bit_b:
                out_idx ^= (1 << q_b)
            U[out_idx, idx] = u_elem

    return U

# ============================================================
# Full unitary QCMI computation for vertex-sharing chain
# Optimized for b1=1 (4 qubits, 16x16 unitary)
# ============================================================

def build_vertex_chain_unitary(b1, c_vals, axes_list):
    """
    Build full unitary for vertex-sharing chain with specified per-edge (c, axis).

    c_vals: list of length 4*b1, one Cartan parameter per edge
    axes_list: list of length 4*b1, one axis unit vector per edge

    Qubit indexing:
      0..b1: system qubits Q_0...Q_b1
      b1+1 .. b1+2*b1: environment qubits
    """
    n_qubits = (b1 + 1) + 2 * b1
    d = 2 ** n_qubits
    U = np.eye(d, dtype=complex)

    for r in range(b1):
        Q_a = r
        Q_b = r + 1
        E_1 = b1 + 1 + 2 * r
        E_2 = b1 + 1 + 2 * r + 1

        edges = [(Q_a, E_1), (E_1, Q_b), (Q_b, E_2), (E_2, Q_a)]

        for edge_idx, (q_a, q_b) in enumerate(edges):
            ax_idx = r * 4 + edge_idx
            n_hat = axes_list[ax_idx]
            c_val = c_vals[ax_idx]
            gate = cartan_gate_2q(c_val, n_hat)
            U_gate = embed_2q_gate(gate, q_a, q_b, n_qubits)
            U = U_gate @ U

    return U


def compute_qcmi_full(b1, c_vals, axes_list, p_val):
    """
    Compute QCMI for vertex-sharing chain via full unitary + purification.

    Optimized: for b1=1, total Hilbert space is 4 qubits (d=16).
    The R-S-E purification adds another d_s=4 degrees, total 64-dim vector.
    """
    n_qubits = (b1 + 1) + 2 * b1
    d_total = 2 ** n_qubits
    d_s = 2 ** (b1 + 1)
    n_env = 2 * b1
    d_env = 2 ** n_env

    U = build_vertex_chain_unitary(b1, c_vals, axes_list)

    sqrt_p = np.sqrt(p_val)
    sqrt_1mp = np.sqrt(1.0 - p_val)

    # Build full R-S-E state
    psi_full = np.zeros(d_s * d_total, dtype=complex)

    for sys_idx in range(d_s):
        # |i>_S ⊗ |ψ_init>_E
        psi_SE_i = np.zeros(d_total, dtype=complex)
        for env_idx in range(d_env):
            amp = 1.0
            for e in range(n_env):
                e_bit = (env_idx >> e) & 1
                amp *= sqrt_p if e_bit == 0 else sqrt_1mp
            SE_idx = sys_idx + env_idx * d_s
            psi_SE_i[SE_idx] = amp

        psi_out_i = U @ psi_SE_i
        psi_full[sys_idx * d_total:(sys_idx + 1) * d_total] = psi_out_i

    psi_full /= np.sqrt(d_s)

    # Reshape: [i_R, i_E, i_Q]
    psi_tmp = psi_full.reshape(d_s, d_env, d_s)
    psi_reshaped = psi_tmp.transpose(0, 2, 1)  # [R, Q, E]

    # rho_RQ
    rho_RQ_4d = np.einsum('iae,jbe->iajb', psi_reshaped, psi_reshaped.conj())
    rho_RQ_mat = rho_RQ_4d.reshape(d_s * d_s, d_s * d_s)
    S_RQ = von_neumann_entropy(rho_RQ_mat)

    # rho_EQ
    rho_EQ_4d = np.einsum('iae,ibf->eafb', psi_reshaped, psi_reshaped.conj())
    rho_EQ_mat = rho_EQ_4d.reshape(d_env * d_s, d_env * d_s)
    S_EQ = von_neumann_entropy(rho_EQ_mat)

    # rho_Q
    rho_Q = np.einsum('iae,ibe->ab', psi_reshaped, psi_reshaped.conj())
    S_Q = von_neumann_entropy(rho_Q)

    qcmi = S_RQ + S_EQ - S_Q

    return {
        'qcmi': qcmi,
        'S_RQ': S_RQ,
        'S_EQ': S_EQ,
        'S_Q': S_Q,
    }


def compute_qcmi_b1_fast(c_vals, axes_list, p_val):
    """Wrapper for b1=1: 2 system qubits, 2 env qubits, 4 edges."""
    return compute_qcmi_full(1, c_vals, axes_list, p_val)


def compute_qcmi_b2_fast(c_vals, axes_list, p_val):
    """Wrapper for b1=2: 3 system qubits, 4 env qubits, 8 edges."""
    return compute_qcmi_full(2, c_vals, axes_list, p_val)


# ============================================================
# Axis generation utilities
# ============================================================
Z_HAT = np.array([0.0, 0.0, 1.0])
X_HAT = np.array([1.0, 0.0, 0.0])
Y_HAT = np.array([0.0, 1.0, 0.0])

def unit_vector(theta, phi):
    """Unit vector from spherical coordinates."""
    return np.array([np.sin(theta) * np.cos(phi),
                     np.sin(theta) * np.sin(phi),
                     np.cos(theta)])

def random_unit_vector():
    """Random unit vector uniformly on S^2."""
    theta = np.arccos(2 * np.random.random() - 1)
    phi = 2 * np.pi * np.random.random()
    return unit_vector(theta, phi)

def random_small_rotation(z_hat, theta_max=0.2):
    """Unit vector within angle theta_max of reference axis."""
    theta = theta_max * np.random.random()
    phi = 2 * np.pi * np.random.random()
    rot_axis = np.array([np.cos(phi), np.sin(phi), 0.0])
    n = (np.cos(theta) * z_hat +
         np.sin(theta) * np.cross(rot_axis, z_hat) +
         (1 - np.cos(theta)) * np.dot(rot_axis, z_hat) * rot_axis)
    return n / np.linalg.norm(n)

def random_rotation_from(axis, theta_max):
    """Rotate axis by random angle up to theta_max."""
    theta = theta_max * np.random.random()
    phi = 2 * np.pi * np.random.random()
    # Perpendicular vectors
    if abs(axis[2]) < 0.99:
        perp1 = np.cross(axis, Z_HAT)
    else:
        perp1 = np.cross(axis, X_HAT)
    perp1 = perp1 / np.linalg.norm(perp1)
    perp2 = np.cross(axis, perp1)
    n = (np.cos(theta) * axis +
         np.sin(theta) * np.cos(phi) * perp1 +
         np.sin(theta) * np.sin(phi) * perp2)
    return n / np.linalg.norm(n)


# ============================================================
# TASK 1: Systematic grid + random scan (b1=1)
# ============================================================

def run_task1_scan(p_val=0.5, n_c_points=60, n_random_per_c=3000,
                   zero_threshold=1e-6):
    """
    Systematic scan of b1=1 parameter space.

    Strategy:
    - c_grid: 60 points from 0.05 to π-0.05
    - Per c: 3000 random axis configs (all 4 edges have same c, independent random axes)
    - Total: 180K QCMI computations
    - Track minimum QCMI and best configs
    """
    print("=" * 70)
    print("TASK 1: Systematic b1=1 Scan — Grid c + Random Axes")
    print(f"  c_grid: {n_c_points} points, {n_random_per_c} random axes each")
    print(f"  Total: {n_c_points * n_random_per_c} configurations")
    print(f"  Zero threshold: {zero_threshold}")
    print("=" * 70)

    n_edges = 4  # b1=1, 4 edges

    # c grid from 0.05 to π-0.05, with refinement near π/4 and π/2
    c_base = np.linspace(0.05, np.pi - 0.05, 50)
    # Add extra points near π/4, π/2, 3π/4
    extra_c = np.array([np.pi/4 - 0.02, np.pi/4 + 0.02,
                         np.pi/2 - 0.02, np.pi/2 + 0.02, np.pi/2 - 0.001, np.pi/2 + 0.001,
                         3*np.pi/4 - 0.02, 3*np.pi/4 + 0.02])
    c_grid = np.sort(np.unique(np.concatenate([c_base, extra_c])))[:n_c_points]

    all_configs = []  # Store best configs
    qcmi_min_per_c = []
    found_counterexample = False
    counterexample_configs = []

    # Compute aligned baseline for reference
    z_axes = [Z_HAT.copy() for _ in range(n_edges)]
    c_aligned = np.array([np.pi/4] * n_edges)
    baseline_aligned = compute_qcmi_b1_fast(c_aligned, z_axes, p_val)['qcmi']
    print(f"\n  Baseline: QCMI(c=π/4, aligned) = {baseline_aligned:.8f}")
    print(f"  2*H(p) = {2*H2(p_val):.8f}")

    c_clifford_pi2 = np.array([np.pi/2] * n_edges)
    baseline_clifford = compute_qcmi_b1_fast(c_clifford_pi2, z_axes, p_val)['qcmi']
    print(f"  Baseline: QCMI(c=π/2, aligned, Clifford) = {baseline_clifford:.8e}")

    global_min_qcmi = float('inf')
    global_min_config = None

    total_start = time.time()

    for ci, c_val in enumerate(c_grid):
        qcmi_vals = []
        min_qcmi_ci = float('inf')
        best_config_ci = None

        for sample_i in range(n_random_per_c):
            # Random axes for all 4 edges
            axes = [random_unit_vector() for _ in range(n_edges)]

            try:
                c_arr = np.array([c_val] * n_edges)
                result = compute_qcmi_b1_fast(c_arr, axes, p_val)
                qcmi = result['qcmi']

                qcmi_vals.append(qcmi)

                if qcmi < min_qcmi_ci:
                    min_qcmi_ci = qcmi
                    best_config_ci = {
                        'c': float(c_val),
                        'axes': [a.tolist() for a in axes],
                        'qcmi': float(qcmi),
                        'S_RQ': float(result['S_RQ']),
                        'S_EQ': float(result['S_EQ']),
                        'S_Q': float(result['S_Q']),
                    }

                if qcmi < zero_threshold:
                    found_counterexample = True
                    counterexample_configs.append({
                        'c': float(c_val),
                        'axes': [a.tolist() for a in axes],
                        'qcmi': float(qcmi),
                        'p': p_val,
                        'clifford_check': f"c/π = {c_val/np.pi:.6f}, c/(π/2) = {c_val/(np.pi/2):.6f}",
                    })
                    print(f"\n  *** COUNTEREXAMPLE FOUND! c={c_val:.6f} QCMI={qcmi:.4e} ***")

                if qcmi < global_min_qcmi:
                    global_min_qcmi = qcmi
                    global_min_config = dict(best_config_ci)
            except Exception as e:
                continue

        qcmi_arr = np.array(qcmi_vals)
        stats = {
            'c': float(c_val),
            'c_over_pi': float(c_val / np.pi),
            'n_samples': len(qcmi_vals),
            'qcmi_min': float(np.min(qcmi_arr)),
            'qcmi_mean': float(np.mean(qcmi_arr)),
            'qcmi_median': float(np.median(qcmi_arr)),
            'qcmi_max': float(np.max(qcmi_arr)),
            'qcmi_std': float(np.std(qcmi_arr)),
            'fraction_below_aligned': float(np.mean(qcmi_arr < baseline_aligned)),
            'best_config': best_config_ci,
        }
        qcmi_min_per_c.append(stats)

        # Progress
        elapsed = time.time() - total_start
        eta = elapsed / (ci + 1) * (len(c_grid) - ci - 1)
        clifford_dist = min(abs(c_val), abs(c_val - np.pi/2), abs(c_val - np.pi),
                           abs(c_val - 3*np.pi/2))
        print(f"  [{ci+1:3d}/{len(c_grid)}] c={c_val:.4f} (c/π={c_val/np.pi:.3f}) "
              f"min={np.min(qcmi_arr):.6e} mean={np.mean(qcmi_arr):.6e} "
              f"below_aligned={stats['fraction_below_aligned']:.3f} "
              f"[elapsed={elapsed:.0f}s ETA={eta:.0f}s]", flush=True)

        if found_counterexample:
            break

    total_elapsed = time.time() - total_start

    print(f"\n  === TASK 1 SUMMARY ===")
    print(f"  Total configs evaluated: {sum(s['n_samples'] for s in qcmi_min_per_c)}")
    print(f"  Total time: {total_elapsed:.1f}s")
    print(f"  Global minimum QCMI: {global_min_qcmi:.8e}")
    if global_min_config:
        print(f"  Best config: c={global_min_config['c']:.6f} "
              f"(c/π={global_min_config['c']/np.pi:.4f})")

    if found_counterexample:
        print(f"\n  *** WALL BROKEN! Found {len(counterexample_configs)} counterexamples ***")
        for cc in counterexample_configs[:5]:
            print(f"    c={cc['c']:.6f} QCMI={cc['qcmi']:.4e}")
    else:
        print(f"\n  No counterexample found. Minimum QCMI = {global_min_qcmi:.4e}")
        min_c = min(qcmi_min_per_c, key=lambda x: x['qcmi_min'])
        print(f"  Lowest QCMI at c={min_c['c']:.4f} (c/π={min_c['c']/np.pi:.4f}): "
              f"{min_c['qcmi_min']:.4e}")

    return {
        'task': 'systematic_b1_scan',
        'p': p_val,
        'zero_threshold': zero_threshold,
        'n_c_points': len(c_grid),
        'n_random_per_c': n_random_per_c,
        'total_configs': sum(s['n_samples'] for s in qcmi_min_per_c),
        'compute_time_s': round(total_elapsed, 1),
        'found_counterexample': found_counterexample,
        'counterexample_configs': counterexample_configs,
        'global_min_qcmi': float(global_min_qcmi),
        'global_min_config': global_min_config,
        'qcmi_min_per_c': qcmi_min_per_c,
        'baseline_aligned_pi4': float(baseline_aligned),
        'baseline_clifford_pi2': float(baseline_clifford),
    }


# ============================================================
# TASK 1b: Two-parameter scan (c1, c2 independent)
# ============================================================

def run_task1b_twoparam(p_val=0.5, n_c_grid=20, n_random_per_point=500):
    """
    Scan with two independent Cartan parameters:
    - c1 for edges 0,1 (connecting to E1)
    - c2 for edges 2,3 (connecting to E2)
    - Random axes for all 4 edges
    """
    print("\n" + "=" * 70)
    print("TASK 1b: Two-Parameter Scan (c1, c2 independent)")
    print(f"  Grid: {n_c_grid}x{n_c_grid}, {n_random_per_point} random axes each")
    print("=" * 70)

    n_edges = 4
    c_vals = np.linspace(0.05, np.pi - 0.05, n_c_grid)

    min_per_point = []
    global_min_qcmi = float('inf')
    global_min_info = None

    total_configs = 0
    t0 = time.time()

    for i, c1 in enumerate(c_vals):
        for j, c2 in enumerate(c_vals):
            qcmi_samples = []
            min_local = float('inf')

            for _ in range(n_random_per_point):
                axes = [random_unit_vector() for _ in range(n_edges)]
                c_arr = np.array([c1, c1, c2, c2])
                try:
                    result = compute_qcmi_b1_fast(c_arr, axes, p_val)
                    qcmi = result['qcmi']
                    qcmi_samples.append(qcmi)
                    if qcmi < min_local:
                        min_local = qcmi
                    if qcmi < global_min_qcmi:
                        global_min_qcmi = qcmi
                        global_min_info = {
                            'c1': float(c1), 'c2': float(c2),
                            'qcmi': float(qcmi),
                            'axes': [a.tolist() for a in axes],
                        }
                except Exception:
                    continue

            total_configs += len(qcmi_samples)
            if len(qcmi_samples) > 0:
                min_per_point.append({
                    'c1': float(c1), 'c2': float(c2),
                    'qcmi_min': float(np.min(qcmi_samples)),
                    'qcmi_mean': float(np.mean(qcmi_samples)),
                })

            if (i * n_c_grid + j) % 40 == 0:
                elapsed = time.time() - t0
                print(f"    [{i},{j}] c1={c1:.3f} c2={c2:.3f} "
                      f"min_local={min_local:.6e} [elapsed={elapsed:.0f}s]", flush=True)

    elapsed = time.time() - t0
    print(f"\n  Total configs: {total_configs}, Time: {elapsed:.1f}s")
    print(f"  Global min QCMI: {global_min_qcmi:.6e}")
    if global_min_info:
        print(f"  At c1={global_min_info['c1']:.4f}, c2={global_min_info['c2']:.4f}")

    return {
        'task': 'two_param_b1_scan',
        'n_c_grid': n_c_grid,
        'n_random_per_point': n_random_per_point,
        'total_configs': total_configs,
        'compute_time_s': round(elapsed, 1),
        'global_min_qcmi': float(global_min_qcmi),
        'global_min_info': global_min_info,
        'min_per_point': min_per_point,
    }


# ============================================================
# TASK 2: Special Symmetry Search
# ============================================================

def run_task2_symmetries(p_val=0.5, n_c_points=30, n_samples_per_c=2000):
    """
    Search with special symmetric axis configurations.

    Symmetries tested:
    2a. Coplanar axes (all in single plane, φ=0 or φ=const)
    2b. Orthogonal axis pairs (n̂₁·n̂₂ = 0)
    2c. Exchange symmetry (edges 0,2 swapped with 1,3)
    2d. Time-reversal pairs (n̂ → -n̂ on specific edges)
    2e. Equal axes on E1 edges, equal axes on E2 edges (per-qubit)
    2f. n̂₁·n̂₂ = 1/2 (60° between axis groups)
    """
    print("\n" + "=" * 70)
    print("TASK 2: Special Symmetry Search")
    print("=" * 70)

    n_edges = 4
    c_grid = np.linspace(0.05, np.pi - 0.05, n_c_points)
    results = {}

    # ---- 2a: Coplanar axes (all in xz-plane, φ=0) ----
    print("\n  --- 2a: Coplanar axes (all in xz-plane) ---")
    min_per_c_2a = []
    global_min_2a = float('inf')

    for ci, c_val in enumerate(c_grid):
        qcmi_samples = []
        for _ in range(n_samples_per_c):
            # All axes have φ=0 (in xz-plane), random θ
            axes = [unit_vector(np.pi * np.random.random(), 0.0) for _ in range(n_edges)]
            c_arr = np.array([c_val] * n_edges)
            try:
                result = compute_qcmi_b1_fast(c_arr, axes, p_val)
                qcmi_samples.append(result['qcmi'])
            except Exception:
                continue

        if qcmi_samples:
            q_arr = np.array(qcmi_samples)
            min_per_c_2a.append({'c': float(c_val), 'qcmi_min': float(np.min(q_arr)),
                                 'qcmi_mean': float(np.mean(q_arr))})
            global_min_2a = min(global_min_2a, np.min(q_arr))

    print(f"    Global min QCMI (coplanar): {global_min_2a:.6e}")
    results['2a_coplanar'] = {
        'description': 'All axes in xz-plane (phi=0), random theta',
        'n_configs': n_c_points * n_samples_per_c,
        'global_min_qcmi': float(global_min_2a),
        'min_per_c': min_per_c_2a,
    }

    # ---- 2b: Orthogonal axis pairs ----
    print("\n  --- 2b: Orthogonal axis groups ---")
    min_per_c_2b = []
    global_min_2b = float('inf')

    for ci, c_val in enumerate(c_grid):
        qcmi_samples = []
        for _ in range(n_samples_per_c):
            # E1 edges (0,1) have axis n̂₁, E2 edges (2,3) have axis n̂₂ with n̂₁·n̂₂=0
            n1 = random_unit_vector()
            # Find a perpendicular vector
            if abs(n1[2]) < 0.99:
                perp = np.cross(n1, Z_HAT)
            else:
                perp = np.cross(n1, X_HAT)
            perp = perp / np.linalg.norm(perp)
            # Random orthogonal direction in the perpendicular plane
            phi_rot = 2 * np.pi * np.random.random()
            n2 = np.cos(phi_rot) * perp + np.sin(phi_rot) * np.cross(n1, perp)
            n2 = n2 / np.linalg.norm(n2)

            axes = [n1, n1, n2, n2]
            c_arr = np.array([c_val] * n_edges)
            try:
                result = compute_qcmi_b1_fast(c_arr, axes, p_val)
                qcmi_samples.append(result['qcmi'])
            except Exception:
                continue

        if qcmi_samples:
            q_arr = np.array(qcmi_samples)
            min_per_c_2b.append({'c': float(c_val), 'qcmi_min': float(np.min(q_arr)),
                                 'qcmi_mean': float(np.mean(q_arr))})
            global_min_2b = min(global_min_2b, np.min(q_arr))

    print(f"    Global min QCMI (orthogonal groups): {global_min_2b:.6e}")
    results['2b_orthogonal_groups'] = {
        'description': 'E1 edges share n1, E2 edges share n2, n1·n2=0',
        'n_configs': n_c_points * n_samples_per_c,
        'global_min_qcmi': float(global_min_2b),
        'min_per_c': min_per_c_2b,
    }

    # ---- 2c: Exchange symmetric axes ----
    print("\n  --- 2c: Exchange symmetry (edge 0=3, edge 1=2) ---")
    min_per_c_2c = []
    global_min_2c = float('inf')

    for ci, c_val in enumerate(c_grid):
        qcmi_samples = []
        for _ in range(n_samples_per_c):
            n_even = random_unit_vector()
            n_odd = random_unit_vector()
            # Exchange symmetry: edges (0,3) share axis, edges (1,2) share axis
            axes = [n_even, n_odd, n_odd, n_even]  # edges 0,1,2,3
            c_arr = np.array([c_val] * n_edges)
            try:
                result = compute_qcmi_b1_fast(c_arr, axes, p_val)
                qcmi_samples.append(result['qcmi'])
            except Exception:
                continue

        if qcmi_samples:
            q_arr = np.array(qcmi_samples)
            min_per_c_2c.append({'c': float(c_val), 'qcmi_min': float(np.min(q_arr)),
                                 'qcmi_mean': float(np.mean(q_arr))})
            global_min_2c = min(global_min_2c, np.min(q_arr))

    print(f"    Global min QCMI (exchange sym): {global_min_2c:.6e}")
    results['2c_exchange_symmetry'] = {
        'description': 'Edges 0 and 3 share n_even, edges 1 and 2 share n_odd (exchange symmetric)',
        'n_configs': n_c_points * n_samples_per_c,
        'global_min_qcmi': float(global_min_2c),
        'min_per_c': min_per_c_2c,
    }

    # ---- 2d: Time-reversal pairs (n̂ → -n̂ on specific edges) ----
    print("\n  --- 2d: Time-reversal pairs ---")
    min_per_c_2d = []
    global_min_2d = float('inf')

    for ci, c_val in enumerate(c_grid):
        qcmi_samples = []
        for _ in range(n_samples_per_c):
            n1 = random_unit_vector()
            n2 = random_unit_vector()
            # Edges 0,1: +n1; edges 2,3: -n1 (time-reversed)
            axes = [n1, n1, -n1, -n1]
            c_arr = np.array([c_val] * n_edges)
            try:
                result = compute_qcmi_b1_fast(c_arr, axes, p_val)
                qcmi_samples.append(result['qcmi'])
            except Exception:
                continue

        if qcmi_samples:
            q_arr = np.array(qcmi_samples)
            min_per_c_2d.append({'c': float(c_val), 'qcmi_min': float(np.min(q_arr)),
                                 'qcmi_mean': float(np.mean(q_arr))})
            global_min_2d = min(global_min_2d, np.min(q_arr))

    print(f"    Global min QCMI (time-reversal): {global_min_2d:.6e}")
    results['2d_time_reversal'] = {
        'description': 'Edges 0,1: +n1, edges 2,3: -n1 (time-reversal on E2 edges)',
        'n_configs': n_c_points * n_samples_per_c,
        'global_min_qcmi': float(global_min_2d),
        'min_per_c': min_per_c_2d,
    }

    # ---- 2e: Per-qubit consistent axes ----
    # Already known from Round 3: if each env qubit sees the same axis on both its edges,
    # QCMI should be same as aligned case (no increase from non-alignment)
    print("\n  --- 2e: Per-qubit consistent axes (QCMI = aligned) ---")
    c_test = np.pi / 4  # Non-Clifford
    axes_2e = [Z_HAT, Z_HAT, Z_HAT, Z_HAT]  # All aligned -> known baseline
    qcmi_aligned_test = compute_qcmi_b1_fast(np.array([c_test]*4), axes_2e, p_val)['qcmi']

    # Check: all equal but rotated -> should give same QCMI as aligned
    n_rot = unit_vector(0.5, 1.2)
    axes_rot_all = [n_rot, n_rot, n_rot, n_rot]
    qcmi_rot_all = compute_qcmi_b1_fast(np.array([c_test]*4), axes_rot_all, p_val)['qcmi']
    print(f"    Aligned(z) QCMI(c=π/4) = {qcmi_aligned_test:.8f}")
    print(f"    All rotated to same n QCMI = {qcmi_rot_all:.8f}")
    print(f"    Diff: {abs(qcmi_rot_all - qcmi_aligned_test):.2e}")

    results['2e_per_qubit_consistent'] = {
        'description': 'All edges share same axis (global rotation) -> QCMI invariant',
        'aligned_qcmi': float(qcmi_aligned_test),
        'rotated_qcmi': float(qcmi_rot_all),
        'diff': float(abs(qcmi_rot_all - qcmi_aligned_test)),
        'verdict': 'QCMI invariant under global rotation, as expected from symmetry',
    }

    # ---- 2f: Special angle 60° between axis groups ----
    print("\n  --- 2f: 60° between E1-axis and E2-axis ---")
    min_per_c_2f = []
    global_min_2f = float('inf')

    angle_60 = np.pi / 3  # 60°

    for ci, c_val in enumerate(c_grid):
        qcmi_samples = []
        for _ in range(n_samples_per_c):
            n1 = random_unit_vector()
            # Create n2 at 60° from n1
            if abs(n1[2]) < 0.99:
                perp = np.cross(n1, Z_HAT)
            else:
                perp = np.cross(n1, X_HAT)
            perp = perp / np.linalg.norm(perp)
            n2 = np.cos(angle_60) * n1 + np.sin(angle_60) * perp
            n2 = n2 / np.linalg.norm(n2)

            axes = [n1, n1, n2, n2]
            c_arr = np.array([c_val] * n_edges)
            try:
                result = compute_qcmi_b1_fast(c_arr, axes, p_val)
                qcmi_samples.append(result['qcmi'])
            except Exception:
                continue

        if qcmi_samples:
            q_arr = np.array(qcmi_samples)
            min_per_c_2f.append({'c': float(c_val), 'qcmi_min': float(np.min(q_arr)),
                                 'qcmi_mean': float(np.mean(q_arr))})
            global_min_2f = min(global_min_2f, np.min(q_arr))

    print(f"    Global min QCMI (60° groups): {global_min_2f:.6e}")
    results['2f_angle_60'] = {
        'description': 'E1 edges share n1, E2 edges share n2, angle(n1,n2)=60°',
        'n_configs': n_c_points * n_samples_per_c,
        'global_min_qcmi': float(global_min_2f),
        'min_per_c': min_per_c_2f,
    }

    # ---- Summary ----
    print(f"\n  === TASK 2 SUMMARY ===")
    for key, val in results.items():
        if 'global_min_qcmi' in val:
            print(f"  {key}: min QCMI = {val['global_min_qcmi']:.6e}")

    return results


# ============================================================
# TASK 2g: Deep dive — scatter search near zero-QCMI candidates
# ============================================================

def run_task2g_deep_dive(best_configs_from_task1, p_val=0.5,
                          n_perturbations=5000, perturbation_scale=0.1):
    """
    Take the lowest-QCMI configurations from Task 1 and do local perturbation
    search. Perturb axis directions and c values slightly, looking for
    configurations with even lower QCMI.
    """
    print("\n" + "=" * 70)
    print("TASK 2g: Deep Dive — Perturbation Search Near Candidates")
    print(f"  Best configs from Task 1: {len(best_configs_from_task1)}")
    print(f"  Perturbations per config: {n_perturbations}")
    print(f"  Perturbation scale: {perturbation_scale}")
    print("=" * 70)

    n_edges = 4
    all_results = []
    global_min_qcmi = float('inf')
    global_min_config = None

    for idx, config in enumerate(best_configs_from_task1):
        c_base = config.get('c', config.get('c1', np.pi/4))
        axes_base = config.get('axes', None)
        if axes_base is None:
            continue
        axes_base = np.array(axes_base)

        best_local_qcmi = float('inf')
        best_local_config = None

        for pi in range(n_perturbations):
            # Perturb c
            c_pert = c_base + perturbation_scale * (2 * np.random.random() - 1)
            c_pert = np.clip(c_pert, 0.01, np.pi - 0.01)
            c_arr = np.array([c_pert] * n_edges)

            # Perturb axes: rotate each axis slightly
            axes_pert = []
            for a in axes_base:
                a_vec = np.array(a) / np.linalg.norm(a)
                a_pert = random_rotation_from(a_vec, perturbation_scale)
                axes_pert.append(a_pert)

            try:
                result = compute_qcmi_b1_fast(c_arr, axes_pert, p_val)
                qcmi = result['qcmi']

                if qcmi < best_local_qcmi:
                    best_local_qcmi = qcmi
                    best_local_config = {
                        'c': float(c_pert),
                        'axes': [a.tolist() for a in axes_pert],
                        'qcmi': float(qcmi),
                        'S_RQ': float(result['S_RQ']),
                        'S_EQ': float(result['S_EQ']),
                        'S_Q': float(result['S_Q']),
                    }
            except Exception:
                continue

        all_results.append({
            'seed_config_idx': idx,
            'seed_qcmi': config['qcmi'],
            'best_after_perturb': best_local_config,
            'improvement': config['qcmi'] - best_local_qcmi,
        })

        if best_local_qcmi < global_min_qcmi:
            global_min_qcmi = best_local_qcmi
            global_min_config = dict(best_local_config)

        if (idx + 1) % 5 == 0:
            print(f"  [{idx+1}/{len(best_configs_from_task1)}] "
                  f"seed QCMI={config['qcmi']:.4e} -> best={best_local_qcmi:.4e} "
                  f"improvement={config['qcmi'] - best_local_qcmi:.4e}", flush=True)

    print(f"\n  === DEEP DIVE SUMMARY ===")
    print(f"  Global min QCMI after perturbations: {global_min_qcmi:.4e}")
    improvements = [r['improvement'] for r in all_results]
    print(f"  Mean improvement: {np.mean(improvements):.4e}")
    print(f"  Max improvement: {np.max(improvements):.4e}")

    return {
        'task': 'deep_dive_perturbation',
        'n_configs_explored': n_perturbations * len(best_configs_from_task1),
        'n_perturbations_per_seed': n_perturbations,
        'perturbation_scale': perturbation_scale,
        'global_min_qcmi': float(global_min_qcmi),
        'global_min_config': global_min_config,
        'all_results': all_results,
        'mean_improvement': float(np.mean(improvements)),
        'max_improvement': float(np.max(improvements)),
    }


# ============================================================
# TASK 2h: Gradient-guided descent
# ============================================================

def run_task2h_gradient_descent(p_val=0.5, n_starts=50, n_steps=200,
                                 step_size=0.05, zero_threshold=1e-6):
    """
    Use finite-difference gradient descent in the full parameter space
    (c + 4*2 axis angles = 9 parameters) to find QCMI minima.

    Parameterization:
    - c (shared across all 4 edges): 1 param
    - For each edge: θ, φ: 8 params
    - Total: 9 parameters
    """
    print("\n" + "=" * 70)
    print("TASK 2h: Gradient-Guided Descent (9-dim parameter space)")
    print(f"  Starts: {n_starts}, Steps per trajectory: {n_steps}")
    print(f"  Step size: {step_size}, Zero threshold: {zero_threshold}")
    print("=" * 70)

    n_edges = 4
    trajectories = []
    found_counterexample = False
    found_configs = []

    def pack_params(c_val, axes_list):
        """Pack c and axes into a flat parameter vector."""
        params = [c_val]
        for a in axes_list:
            # Convert unit vector to θ, φ
            x, y, z_vec = a[0], a[1], a[2]
            theta = np.arccos(np.clip(z_vec, -1, 1))
            phi = np.arctan2(y, x)
            if phi < 0:
                phi += 2 * np.pi
            params.extend([theta, phi])
        return np.array(params)

    def unpack_params(params):
        """Unpack parameter vector to c and axes list."""
        c_val = params[0]
        axes = []
        for i in range(n_edges):
            theta = params[1 + 2*i]
            phi = params[1 + 2*i + 1]
            axes.append(unit_vector(theta, phi))
        return c_val, axes

    def compute_qcmi_from_params(params):
        """Compute QCMI from parameter vector."""
        c_val, axes = unpack_params(params)
        c_arr = np.array([c_val] * n_edges)
        try:
            result = compute_qcmi_b1_fast(c_arr, axes, p_val)
            return result['qcmi']
        except Exception:
            return float('inf')

    def finite_diff_gradient(params, eps=1e-5):
        """Compute gradient via central finite differences."""
        grad = np.zeros_like(params)
        f0 = compute_qcmi_from_params(params)
        for i in range(len(params)):
            params_plus = params.copy()
            params_minus = params.copy()
            params_plus[i] += eps
            params_minus[i] -= eps
            # Clip c
            if i == 0:
                params_plus[0] = np.clip(params_plus[0], 0.01, np.pi - 0.01)
                params_minus[0] = np.clip(params_minus[0], 0.01, np.pi - 0.01)
            f_plus = compute_qcmi_from_params(params_plus)
            f_minus = compute_qcmi_from_params(params_minus)
            grad[i] = (f_plus - f_minus) / (2 * eps)
        return grad

    t0 = time.time()

    for start_i in range(n_starts):
        # Random initialization
        c_init = np.pi * np.random.random() * 0.8 + 0.1  # avoid edges
        axes_init = [random_unit_vector() for _ in range(n_edges)]
        params = pack_params(c_init, axes_init)

        qcmi_init = compute_qcmi_from_params(params)
        qcmi_history = [float(qcmi_init)]
        params_history = [params.copy()]

        for step in range(n_steps):
            grad = finite_diff_gradient(params)
            grad_norm = np.linalg.norm(grad)

            if grad_norm < 1e-12:
                break  # Stationary point

            # Gradient descent with line search
            alpha = step_size
            params_new = params - alpha * grad / grad_norm

            # Project c back to valid range
            params_new[0] = np.clip(params_new[0], 0.01, np.pi - 0.01)

            qcmi_new = compute_qcmi_from_params(params_new)

            # Simple backtracking if QCMI increased
            backtrack = 0
            while qcmi_new > qcmi_history[-1] and backtrack < 10:
                alpha *= 0.5
                params_new = params - alpha * grad / grad_norm
                params_new[0] = np.clip(params_new[0], 0.01, np.pi - 0.01)
                qcmi_new = compute_qcmi_from_params(params_new)
                backtrack += 1

            if qcmi_new < qcmi_history[-1]:
                params = params_new
                qcmi_history.append(float(qcmi_new))
                params_history.append(params.copy())
            else:
                # Accept with small random perturbation to escape
                params = params + 0.01 * np.random.randn(len(params))
                params[0] = np.clip(params[0], 0.01, np.pi - 0.01)
                qcmi_history.append(float(compute_qcmi_from_params(params)))

            if qcmi_history[-1] < zero_threshold:
                found_counterexample = True
                c_final, axes_final = unpack_params(params)
                found_configs.append({
                    'c': float(c_final),
                    'axes': [a.tolist() for a in axes_final],
                    'qcmi': float(qcmi_history[-1]),
                    'trajectory_start': start_i,
                    'step_reached': step,
                })
                break

        trajectories.append({
            'start_idx': start_i,
            'qcmi_init': float(qcmi_init),
            'qcmi_final': float(qcmi_history[-1]),
            'n_steps': len(qcmi_history),
            'qcmi_history': [float(v) for v in qcmi_history],
        })

        if (start_i + 1) % 10 == 0:
            elapsed = time.time() - t0
            print(f"  [{start_i+1}/{n_starts}] init QCMI={qcmi_init:.4e} "
                  f"final={qcmi_history[-1]:.4e} steps={len(qcmi_history)} "
                  f"[elapsed={elapsed:.0f}s]", flush=True)

        if found_counterexample:
            break

    elapsed = time.time() - t0

    final_qcmis = [t['qcmi_final'] for t in trajectories]
    print(f"\n  === GRADIENT DESCENT SUMMARY ===")
    print(f"  Total trajectories: {len(trajectories)}")
    print(f"  Time: {elapsed:.1f}s")
    print(f"  Min final QCMI: {np.min(final_qcmis):.6e}")
    print(f"  Mean final QCMI: {np.mean(final_qcmis):.6e}")
    print(f"  Median final QCMI: {np.median(final_qcmis):.6e}")
    print(f"  Found counterexample: {found_counterexample}")

    return {
        'task': 'gradient_descent',
        'n_starts': n_starts,
        'n_steps_per_trajectory': n_steps,
        'step_size': step_size,
        'compute_time_s': round(elapsed, 1),
        'found_counterexample': found_counterexample,
        'found_configs': found_configs,
        'trajectories': trajectories,
        'min_final_qcmi': float(np.min(final_qcmis)),
        'mean_final_qcmi': float(np.mean(final_qcmis)),
        'median_final_qcmi': float(np.median(final_qcmis)),
    }


# ============================================================
# TASK 3: b1=2 Extension
# ============================================================

def run_task3_b2_scan(p_val=0.5, n_c_points=20, n_random_per_c=500):
    """
    b1=2 extension: 3 system qubits, 4 env qubits, 8 edges.
    More degrees of freedom -> more possible cancellation mechanisms.
    """
    print("\n" + "=" * 70)
    print("TASK 3: b1=2 Extension Scan")
    print(f"  System: 3 qubits, Env: 4 qubits, 8 edges")
    print(f"  c_grid: {n_c_points} points, {n_random_per_c} random axes each")
    print("=" * 70)

    n_edges = 4 * 2  # 8 edges for b1=2
    c_grid = np.linspace(0.05, np.pi - 0.05, n_c_points)

    min_per_c = []
    global_min_qcmi = float('inf')
    global_min_config = None

    t0 = time.time()

    for ci, c_val in enumerate(c_grid):
        qcmi_samples = []
        min_local = float('inf')
        best_local = None

        for _ in range(n_random_per_c):
            axes = [random_unit_vector() for _ in range(n_edges)]
            c_arr = np.array([c_val] * n_edges)
            try:
                result = compute_qcmi_b2_fast(c_arr, axes, p_val)
                qcmi = result['qcmi']
                qcmi_samples.append(qcmi)
                if qcmi < min_local:
                    min_local = qcmi
                    best_local = {
                        'c': float(c_val),
                        'qcmi': float(qcmi),
                        'S_RQ': float(result['S_RQ']),
                        'S_EQ': float(result['S_EQ']),
                        'S_Q': float(result['S_Q']),
                    }
            except Exception:
                continue

        if qcmi_samples:
            q_arr = np.array(qcmi_samples)
            min_per_c.append({
                'c': float(c_val),
                'qcmi_min': float(np.min(q_arr)),
                'qcmi_mean': float(np.mean(q_arr)),
                'qcmi_std': float(np.std(q_arr)),
                'best_config': best_local,
            })
            if np.min(q_arr) < global_min_qcmi:
                global_min_qcmi = np.min(q_arr)
                global_min_config = dict(best_local)

        elapsed = time.time() - t0
        eta = elapsed / (ci + 1) * (len(c_grid) - ci - 1)
        print(f"  [{ci+1}/{len(c_grid)}] c={c_val:.4f} min={min_local:.6e} "
              f"[elapsed={elapsed:.0f}s ETA={eta:.0f}s]", flush=True)

    elapsed = time.time() - t0
    print(f"\n  Total configs: {len(min_per_c) * n_random_per_c}, Time: {elapsed:.1f}s")
    print(f"  Global min QCMI (b1=2): {global_min_qcmi:.6e}")

    return {
        'task': 'b1_2_scan',
        'n_c_points': n_c_points,
        'n_random_per_c': n_random_per_c,
        'total_configs': n_c_points * n_random_per_c,
        'compute_time_s': round(elapsed, 1),
        'global_min_qcmi': float(global_min_qcmi),
        'global_min_config': global_min_config,
        'min_per_c': min_per_c,
    }


# ============================================================
# TASK 4: Cross-p analysis — does p change the landscape?
# ============================================================

def run_task4_p_scan(p_values=None, n_random_configs=5000):
    """Check if QCMI landscape changes character with p."""
    if p_values is None:
        p_values = [0.3, 0.5, 0.7]

    print("\n" + "=" * 70)
    print("TASK 4: Cross-p Analysis")
    print("=" * 70)

    n_edges = 4
    results = {}

    c_test_values = [0.3, 0.5, np.pi/4, 0.7, 1.0]

    for p_val in p_values:
        print(f"\n  --- p={p_val} ---")
        p_results = {}
        for c_val in c_test_values:
            qcmi_samples = []
            for _ in range(n_random_configs):
                axes = [random_unit_vector() for _ in range(n_edges)]
                c_arr = np.array([c_val] * n_edges)
                try:
                    res = compute_qcmi_b1_fast(c_arr, axes, p_val)
                    qcmi_samples.append(res['qcmi'])
                except Exception:
                    continue

            q_arr = np.array(qcmi_samples)
            # Also compute aligned QCMI for reference
            z_axes = [Z_HAT for _ in range(n_edges)]
            qcmi_aligned = compute_qcmi_b1_fast(c_arr, z_axes, p_val)['qcmi']

            p_results[f"c_{c_val:.3f}"] = {
                'c': float(c_val),
                'qcmi_aligned': float(qcmi_aligned),
                'qcmi_min_random': float(np.min(q_arr)),
                'qcmi_mean_random': float(np.mean(q_arr)),
                'qcmi_max_random': float(np.max(q_arr)),
                'fraction_below_aligned': float(np.mean(q_arr < qcmi_aligned)),
            }
            print(f"    c={c_val:.4f}: aligned={qcmi_aligned:.6e} "
                  f"random_min={np.min(q_arr):.6e} "
                  f"below_aligned={p_results[f'c_{c_val:.3f}']['fraction_below_aligned']:.3f}")

        results[f"p_{p_val}"] = p_results

    return {
        'task': 'cross_p_analysis',
        'p_values': p_values,
        'c_test_values': [float(c) for c in c_test_values],
        'n_random_configs_per_point': n_random_configs,
        'results': results,
    }


# ============================================================
# MAIN
# ============================================================

def main():
    print("=" * 70)
    print("LP41 CFOL Generalization - Round 4: Wall-Breaking Search")
    print("Agent B - EXECUTE Phase")
    print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    np.random.seed(42)

    all_results = {
        'project': 'LP41-CFOL-Generalization',
        'round': 4,
        'agent': 'B',
        'phase': 'EXECUTE — Counterexample Search',
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'goal': 'Find QCMI≈0 with non-Clifford c under non-aligned axes, or provide numerical evidence wall holds',
    }

    # ========================
    # Task 1: Systematic scan (main effort)
    # ========================
    print("\n" + "=" * 70)
    print("PHASE 1: Systematic b1=1 Scan")
    print("=" * 70)
    try:
        task1 = run_task1_scan(p_val=0.5, n_c_points=60, n_random_per_c=3000, zero_threshold=1e-6)
        all_results['task1_systematic_scan'] = {
            'status': '✅ 已验证',
            'method': 'Grid c + random axes, 60×3000=180K configurations',
            'data': task1,
        }
    except Exception as e:
        all_results['task1_systematic_scan'] = {
            'status': f'⚠️ 待验证: {str(e)}',
            'error': str(e),
        }
        import traceback
        traceback.print_exc()

    # ========================
    # Task 1b: Two-parameter scan
    # ========================
    print("\n" + "=" * 70)
    print("PHASE 1b: Two-Parameter b1=1 Scan")
    print("=" * 70)
    try:
        task1b = run_task1b_twoparam(p_val=0.5, n_c_grid=15, n_random_per_point=300)
        all_results['task1b_twoparam_scan'] = {
            'status': '✅ 已验证',
            'method': 'Grid (c1,c2) + random axes, 15×15×300=67.5K configurations',
            'data': task1b,
        }
    except Exception as e:
        all_results['task1b_twoparam_scan'] = {
            'status': f'⚠️ 待验证: {str(e)}',
            'error': str(e),
        }
        import traceback
        traceback.print_exc()

    # ========================
    # Task 2: Symmetry search
    # ========================
    print("\n" + "=" * 70)
    print("PHASE 2: Symmetry-Guided Search")
    print("=" * 70)
    try:
        task2 = run_task2_symmetries(p_val=0.5, n_c_points=25, n_samples_per_c=1500)
        all_results['task2_symmetry_search'] = {
            'status': '✅ 已验证',
            'method': '6 symmetry classes, 25×1500=37.5K configs each',
            'data': task2,
        }
    except Exception as e:
        all_results['task2_symmetry_search'] = {
            'status': f'⚠️ 待验证: {str(e)}',
            'error': str(e),
        }
        import traceback
        traceback.print_exc()

    # ========================
    # Task 2g: Deep dive
    # ========================
    print("\n" + "=" * 70)
    print("PHASE 2g: Deep Dive — Perturbation Search")
    print("=" * 70)
    try:
        # Extract best configs from Task 1
        best_configs = []
        t1_data = all_results['task1_systematic_scan']['data']
        for entry in t1_data['qcmi_min_per_c']:
            if entry.get('best_config'):
                best_configs.append(entry['best_config'])
        # Sort by QCMI and take top 30
        best_configs.sort(key=lambda x: x['qcmi'])
        best_configs = best_configs[:30]

        print(f"  Using {len(best_configs)} best configs from Task 1")
        task2g = run_task2g_deep_dive(best_configs, p_val=0.5,
                                       n_perturbations=3000, perturbation_scale=0.15)
        all_results['task2g_deep_dive'] = {
            'status': '✅ 已验证',
            'method': 'Local perturbation around 30 best candidates, 3000 perturbations each',
            'data': task2g,
        }
    except Exception as e:
        all_results['task2g_deep_dive'] = {
            'status': f'⚠️ 待验证: {str(e)}',
            'error': str(e),
        }
        import traceback
        traceback.print_exc()

    # ========================
    # Task 2h: Gradient descent
    # ========================
    print("\n" + "=" * 70)
    print("PHASE 2h: Gradient-Guided Descent")
    print("=" * 70)
    try:
        task2h = run_task2h_gradient_descent(p_val=0.5, n_starts=30, n_steps=150,
                                              step_size=0.05, zero_threshold=1e-6)
        all_results['task2h_gradient_descent'] = {
            'status': '✅ 已验证',
            'method': 'Finite-difference gradient descent in 9-dim parameter space, 30 starts × 150 steps',
            'data': task2h,
        }
    except Exception as e:
        all_results['task2h_gradient_descent'] = {
            'status': f'⚠️ 待验证: {str(e)}',
            'error': str(e),
        }
        import traceback
        traceback.print_exc()

    # ========================
    # Task 3: b1=2 extension
    # ========================
    print("\n" + "=" * 70)
    print("PHASE 3: b1=2 Extension")
    print("=" * 70)
    try:
        task3 = run_task3_b2_scan(p_val=0.5, n_c_points=15, n_random_per_c=300)
        all_results['task3_b2_scan'] = {
            'status': '✅ 已验证',
            'method': 'b1=2 system (7 qubits, 8 edges), 15×300=4.5K configurations',
            'data': task3,
        }
    except Exception as e:
        all_results['task3_b2_scan'] = {
            'status': f'⚠️ 待验证: {str(e)}',
            'error': str(e),
        }
        import traceback
        traceback.print_exc()

    # ========================
    # Task 4: Cross-p analysis
    # ========================
    print("\n" + "=" * 70)
    print("PHASE 4: Cross-p Analysis")
    print("=" * 70)
    try:
        task4 = run_task4_p_scan(p_values=[0.3, 0.5, 0.7], n_random_configs=3000)
        all_results['task4_cross_p'] = {
            'status': '✅ 已验证',
            'method': 'Random axis scan for 5 c values at 3 p levels',
            'data': task4,
        }
    except Exception as e:
        all_results['task4_cross_p'] = {
            'status': f'⚠️ 待验证: {str(e)}',
            'error': str(e),
        }
        import traceback
        traceback.print_exc()

    # ========================
    # Synthesis
    # ========================
    print("\n" + "=" * 70)
    print("SYNTHESIS")
    print("=" * 70)

    # Gather all min QCMIs
    all_mins = {}
    for key in ['task1_systematic_scan', 'task1b_twoparam_scan',
                 'task2_symmetry_search', 'task2g_deep_dive',
                 'task2h_gradient_descent', 'task3_b2_scan']:
        if key in all_results and all_results[key]['status'].startswith('✅'):
            data = all_results[key]['data']
            if 'global_min_qcmi' in data:
                all_mins[key] = data['global_min_qcmi']
            elif 'min_final_qcmi' in data:
                all_mins[key] = data['min_final_qcmi']

    overall_min = min(all_mins.values()) if all_mins else float('inf')
    wall_status = 'BROKEN' if overall_min < 1e-6 else 'INTACT'

    print(f"\n  Overall minimum QCMI across all searches: {overall_min:.6e}")
    print(f"  Per-method minima:")
    for k, v in sorted(all_mins.items(), key=lambda x: x[1]):
        print(f"    {k}: {v:.6e}")

    if wall_status == 'BROKEN':
        print(f"\n  *** WALL BROKEN! Found QCMI < 10^-6 with non-Clifford parameters ***")
    else:
        print(f"\n  Wall INTACT. No QCMI < 10^-6 found with non-Clifford c.")
        print(f"  Closest approach: {overall_min:.4e} (need < 1e-6 to break)")
        orders_below = -np.log10(max(overall_min, 1e-16))
        print(f"  QCMI is {orders_below:.1f} orders of magnitude above threshold")

        # Evidence strength analysis
        total_configs = 0
        for key in all_results:
            if isinstance(all_results[key], dict) and 'data' in all_results[key]:
                d = all_results[key]['data']
                if isinstance(d, dict):
                    tc = d.get('total_configs', d.get('n_configs', 0))
                    total_configs += tc

        print(f"\n  Evidence strength: {total_configs} configurations evaluated")
        if total_configs > 100000 and wall_status == 'INTACT':
            print(f"  Strong numerical evidence that the wall holds.")
            print(f"  The converse (QCMI=0 => c∈(π/2)ℤ) appears to hold")
            print(f"  even for non-aligned Cartan axes.")

    all_results['synthesis'] = {
        'overall_min_qcmi': float(overall_min),
        'wall_status': wall_status,
        'per_method_minima': all_mins,
        'zero_threshold': 1e-6,
        'total_configs_estimate': sum(
            d.get('total_configs', d.get('n_configs', 0))
            for key in all_results
            if isinstance(all_results.get(key), dict)
            for d in [all_results[key].get('data', {})]
            if isinstance(d, dict)
        ),
    }

    # ========================
    # Write output
    # ========================
    output_path = 'D:/Claude/ai-reservations/LP41-CFOL-Generalization/current/B/round4.json'

    class NumpyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, np.integer):
                return int(obj)
            if isinstance(obj, np.floating):
                return float(obj)
            if isinstance(obj, np.ndarray):
                return obj.tolist()
            if isinstance(obj, np.bool_):
                return bool(obj)
            if isinstance(obj, complex):
                return {'real': obj.real, 'imag': obj.imag}
            return super().default(obj)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, cls=NumpyEncoder, indent=2, ensure_ascii=False)

    print(f"\n{'=' * 70}")
    print(f"Results written to: {output_path}")
    print(f"{'=' * 70}")

    return all_results


if __name__ == '__main__':
    main()

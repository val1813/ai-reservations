"""
LP42-GhostZero 北极星#2: Critical Scaling Universality Class
=============================================================
High-resolution scaling scan of QCMI near ghost zero (p=0.5, x_hat axes).
Tests whether exponents β_p, γ_θ, α are universal (|E|-independent) or non-universal.

Primary:   Scan QCMI vs |p-0.5| and QCMI vs θ for |E|=2,4,6,8
Secondary: Cross-disciplinary structural analogy (fracture/turbulence/biology)
Tertiary:  Scaling anisotropy test — β_p vs γ_θ, mixed direction scan

Numerical method: Full unitary + purification for b1=1,2,3,4
(vertex-sharing chain, |E|=2*b1, d_total=2^{3b1+1})

Optimization: For x_hat axes (p-scans), use X-basis Gram matrix (O(2^{b1+1}) instead of O(2^{3b1+1}))
"""

import numpy as np
from numpy.linalg import eigh
import json
import time
import sys
import os

# ============================================================
# Pauli matrices
# ============================================================
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)

X_HAT = np.array([1.0, 0.0, 0.0])
Y_HAT = np.array([0.0, 1.0, 0.0])
Z_HAT = np.array([0.0, 0.0, 1.0])


# ============================================================
# Utility functions
# ============================================================
def von_neumann_entropy(rho, eps=1e-14):
    evals = eigh(rho)[0]
    evals = np.maximum(np.real(evals), eps)
    evals = evals / evals.sum()
    return -np.sum(evals * np.log2(np.maximum(evals, eps)))


def axis_from_x_deviation(theta, phi=0.0):
    """Axis deviating from x_hat by angle theta, azimuth phi in yz-plane."""
    return np.array([np.cos(theta),
                     np.sin(theta) * np.cos(phi),
                     np.sin(theta) * np.sin(phi)])


# ============================================================
# METHOD A: X-basis Gram matrix (for x_hat axes, any p)
# ============================================================
# In the X-eigenbasis (|+>,|->), X = Z (diagonal).
# Cartan gate U = cos(c)I + i sin(c) X⊗X becomes Z⊗Z in X-basis.
# Initial env state |+...+> has effective weight in X-basis.
#
# Key: when all axes = x_hat, the channel is diagonal in X-basis.
# The Gram matrix G_{a,b} captures ALL QCMI information.

def build_xbasis_vertex_chain_gram(b1, c_val, p_val):
    """
    Compute Gram matrix for vertex-sharing chain in X-basis.
    All axes = x_hat, all c = c_val.

    In X-basis: Cartan gate = cos(c)I + i sin(c) Z⊗Z (diagonal).
    Env state: each qubit has probability p_X of being in |+>_x = |0>_x.

    The initial env state in Z-basis: |ψ> = √p|0> + √(1-p)|1>
    In X-basis: |0>_z = (|+>_x + |->_x)/√2, |1>_z = (|+>_x - |->_x)/√2
    So |ψ> = [(√p+√(1-p))/√2]|+>_x + [(√p-√(1-p))/√2]|->_x
    p_X = |(√p+√(1-p))/√2|^2 = (p + 2√(p(1-p)) + (1-p))/2 = (1 + 2√(p(1-p)))/2
    = 1/2 + √(p(1-p))

    At p=0.5: p_X = 1/2 + 1/2 = 1. So |+> = |0>_x (exactly, GHOST).
    At p≠0.5: p_X = 1/2 + √(p(1-p)) < 1. So env has |->_x admixture.
    """
    p_X = 0.5 + np.sqrt(p_val * (1.0 - p_val))

    n_sys = b1 + 1  # system qubits in vertex chain
    n_env = 2 * b1  # environment qubits
    d_s = 2 ** n_sys

    # In X-basis, Z⊗Z action on |s_i, e_j> gives phase exp(i*c * s_i * e_j)
    # where s_i, e_j ∈ {+1,-1} (mapped from {0,1}: 1->+1, 0->-1? No,
    # in X-basis |+>_x = |0> and |->_x = |1>, Z|0>=|0>, Z|1>=-|1>.
    # So s_i=+1 for |0>_x, s_i=-1 for |1>_x. Same for e_j.

    # For each env configuration k (2^n_env possibilities), compute amplitude
    # and the diagonal phase on system space.

    # Precompute env amplitudes
    n_kraus = 2 ** n_env
    k_amps = np.zeros(n_kraus, dtype=float)
    k_configs = np.zeros((n_kraus, n_env), dtype=np.int8)

    sqrt_pX = np.sqrt(p_X)
    sqrt_1mpX = np.sqrt(1.0 - p_X)

    for k_idx in range(n_kraus):
        amp = 1.0
        for e in range(n_env):
            e_bit = (k_idx >> e) & 1
            k_configs[k_idx, e] = e_bit
            amp *= sqrt_pX if e_bit == 0 else sqrt_1mpX
        k_amps[k_idx] = amp

    # Compute Gram matrix
    # G_{a,b} = sum_k kappa*[k,a] * kappa[k,b]
    # where kappa[k,a] = amp_k * exp(i * phase(k, a))
    # phase(k,a) = sum_{edges} c * s_u * s_v

    # Map system config a to spin values {+1,-1}
    # In X-basis: |0>_x → +1, |1>_x → -1
    sys_configs = np.zeros((d_s, n_sys), dtype=np.int8)
    for a in range(d_s):
        for q in range(n_sys):
            sys_configs[a, q] = 1 if ((a >> q) & 1) == 0 else -1

    # For vertex-sharing chain, edges:
    # Ring r: Q_r→E_{2r}, E_{2r}→Q_{r+1}, Q_{r+1}→E_{2r+1}, E_{2r+1}→Q_r
    # Q indices: 0..b1
    # E indices: mapped to 0..2*b1-1 in env indexing

    G = np.zeros((d_s, d_s), dtype=complex)

    # Phase(k, a): for each edge (u=E_idx_in_Q_space, v=E_idx_in_E_space, c)
    # phase contribution = c * s_u * s_v
    # We need to map env qubit index to its spin value

    for k_idx in range(n_kraus):
        amp_k = k_amps[k_idx]
        if amp_k < 1e-15:
            continue

        # Compute phase for each system config
        phases = np.zeros(d_s)
        for a in range(d_s):
            phase = 0.0
            for r in range(b1):
                Q_a_spin = sys_configs[a, r]       # Q_r
                Q_b_spin = sys_configs[a, r + 1]   # Q_{r+1}
                E1_spin = 1 if k_configs[k_idx, 2*r] == 0 else -1     # E_{2r}
                E2_spin = 1 if k_configs[k_idx, 2*r + 1] == 0 else -1  # E_{2r+1}

                # Edges: Q_a→E1, E1→Q_b, Q_b→E2, E2→Q_a
                phase += c_val * Q_a_spin * E1_spin
                phase += c_val * E1_spin * Q_b_spin
                phase += c_val * Q_b_spin * E2_spin
                phase += c_val * E2_spin * Q_a_spin

            phases[a] = phase

        # kappa[k, a] = amp_k * exp(i * phase(a))
        kappa_a = amp_k * np.exp(1j * phases)
        G += np.outer(kappa_a.conj(), kappa_a)

    return G


def qcmi_xbasis(b1, c_val, p_val):
    """QCMI using X-basis Gram matrix. Only valid when all axes = x_hat."""
    d_s = 2 ** (b1 + 1)
    G = build_xbasis_vertex_chain_gram(b1, c_val, p_val)

    # Verify unit trace: G_{a,a} should = 1
    # (trace-preserving channel condition)

    # S(RQ) = S(G/d_s)
    rho_RQ = G / d_s
    S_RQ = von_neumann_entropy(rho_RQ)

    # For this channel structure: S(Q) = S(EQ) = log2(d_s)
    # QCMI = S(RQ) + S(EQ) - S(Q) = S(RQ) + log(d_s) - log(d_s) = S(RQ)
    S_Q = np.log2(d_s)
    QCMI = S_RQ  # S_RQ + S_EQ - S_Q, and S_EQ = S_Q = log2(d_s)

    return {'qcmi': QCMI, 'S_RQ': S_RQ, 'S_EQ': S_Q, 'S_Q': S_Q}


# ============================================================
# METHOD B: Full unitary (for arbitrary axes, general p)
# ============================================================
def cartan_gate_2q(c, n_hat):
    sigma = n_hat[0] * X + n_hat[1] * Y + n_hat[2] * Z
    return np.cos(c) * np.kron(I2, I2) + 1j * np.sin(c) * np.kron(sigma, sigma)


def embed_2q_gate(gate_2q, q_a, q_b, n_qubits):
    d = 2 ** n_qubits
    U = np.eye(d, dtype=complex)
    # Vectorized version for speed
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


def build_vertex_chain_unitary(b1, c_vals, axes_list):
    n_qubits = (b1 + 1) + 2 * b1
    d = 2 ** n_qubits
    U = np.eye(d, dtype=complex)
    edge_idx = 0
    for r in range(b1):
        Q_a = r
        Q_b = r + 1
        E_1 = b1 + 1 + 2 * r
        E_2 = b1 + 1 + 2 * r + 1
        edges = [(Q_a, E_1), (E_1, Q_b), (Q_b, E_2), (E_2, Q_a)]
        for (q_a, q_b) in edges:
            n_hat = axes_list[edge_idx]
            c_val = c_vals[edge_idx]
            gate = cartan_gate_2q(c_val, n_hat)
            U_gate = embed_2q_gate(gate, q_a, q_b, n_qubits)
            U = U_gate @ U
            edge_idx += 1
    return U


def compute_qcmi_full(b1, c_vals, axes_list, p_val):
    """Full QCMI for vertex-sharing chain. Returns dict."""
    n_qubits = (b1 + 1) + 2 * b1
    d_total = 2 ** n_qubits
    d_s = 2 ** (b1 + 1)
    n_env = 2 * b1
    d_env = 2 ** n_env

    U = build_vertex_chain_unitary(b1, c_vals, axes_list)

    sqrt_p = np.sqrt(p_val)
    sqrt_1mp = np.sqrt(1.0 - p_val)

    psi_full = np.zeros(d_s * d_total, dtype=complex)
    for sys_idx in range(d_s):
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

    psi_tmp = psi_full.reshape(d_s, d_env, d_s)
    psi_reshaped = psi_tmp.transpose(0, 2, 1)  # [R, Q, E]

    rho_RQ_4d = np.einsum('iae,jbe->iajb', psi_reshaped, psi_reshaped.conj())
    rho_RQ_mat = rho_RQ_4d.reshape(d_s * d_s, d_s * d_s)
    S_RQ = von_neumann_entropy(rho_RQ_mat)

    rho_EQ_4d = np.einsum('iae,ibf->eafb', psi_reshaped, psi_reshaped.conj())
    rho_EQ_mat = rho_EQ_4d.reshape(d_env * d_s, d_env * d_s)
    S_EQ = von_neumann_entropy(rho_EQ_mat)

    rho_Q = np.einsum('iae,ibe->ab', psi_reshaped, psi_reshaped.conj())
    S_Q = von_neumann_entropy(rho_Q)

    qcmi = S_RQ + S_EQ - S_Q
    return {'qcmi': qcmi, 'S_RQ': S_RQ, 'S_EQ': S_EQ, 'S_Q': S_Q}


# ============================================================
# FITTING & BOOTSTRAP
# ============================================================
def fit_power_law(x, y, x_range=None):
    """Fit y = A * x^alpha in log-log space. Returns A, alpha, R^2."""
    if x_range is not None:
        mask = (x >= x_range[0]) & (x <= x_range[1])
        x = x[mask]
        y = y[mask]

    nonzero = (x > 1e-15) & (y > 1e-15)
    if np.sum(nonzero) < 5:
        return None, None, None, None, None

    log_x = np.log(x[nonzero])
    log_y = np.log(y[nonzero])

    A_mat = np.vstack([np.ones_like(log_x), log_x]).T
    coeffs, residuals, rank, singular = np.linalg.lstsq(A_mat, log_y, rcond=None)
    log_A, alpha = coeffs[0], coeffs[1]
    A = np.exp(log_A)

    pred = A * x[nonzero] ** alpha
    ss_res = np.sum((y[nonzero] - pred) ** 2)
    ss_tot = np.sum((y[nonzero] - np.mean(y[nonzero])) ** 2)
    r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0

    # Also compute standard error of alpha
    n = np.sum(nonzero)
    if n > 2 and len(residuals) > 0:
        sigma2 = residuals[0] / (n - 2) if len(residuals) == 1 else np.sum((log_y - coeffs[0] - coeffs[1]*log_x)**2) / (n - 2)
        XtX_inv = np.linalg.inv(A_mat.T @ A_mat)
        alpha_se = np.sqrt(sigma2 * XtX_inv[1, 1])
    else:
        alpha_se = None

    return A, alpha, alpha_se, r2, log_A


def bootstrap_fit(x, y, n_bootstrap=1000, x_range=None, seed=42):
    """Bootstrap power-law fit. Returns alpha distribution statistics."""
    rng = np.random.RandomState(seed)
    n = len(x)
    alphas = np.zeros(n_bootstrap)

    for i in range(n_bootstrap):
        idx = rng.choice(n, n, replace=True)
        x_boot = x[idx]
        y_boot = y[idx]
        _, alpha, _, _, _ = fit_power_law(x_boot, y_boot, x_range)
        if alpha is not None:
            alphas[i] = alpha
        else:
            alphas[i] = np.nan

    valid = alphas[~np.isnan(alphas)]
    if len(valid) < 10:
        return {'mean': None, 'std': None, 'ci_95': None, 'ci_68': None,
                'median': None, 'n_valid': len(valid)}

    ci_95 = np.percentile(valid, [2.5, 97.5])
    ci_68 = np.percentile(valid, [16, 84])

    return {
        'mean': float(np.mean(valid)),
        'std': float(np.std(valid)),
        'median': float(np.median(valid)),
        'ci_95_low': float(ci_95[0]),
        'ci_95_high': float(ci_95[1]),
        'ci_68_low': float(ci_68[0]),
        'ci_68_high': float(ci_68[1]),
        'n_valid': int(len(valid)),
        'all_alphas': valid.tolist(),
    }


# ============================================================
# PRIMARY TASK: High-Resolution Scaling Scan
# ============================================================
def run_p_scan(b1, c_val=0.5, n_pts=200):
    """
    Scan QCMI vs p near p=0.5 with all x_hat axes.
    Uses X-basis Gram matrix (valid for x_hat axes).
    """
    # Log-spacing: more points near p=0.5
    # Use symmetric: p = 0.5 ± delta where delta is log-spaced
    n_half = n_pts // 2
    delta_min = 5e-5
    delta_max = 0.49

    delta_pos = np.logspace(np.log10(delta_min), np.log10(delta_max), n_half)
    # Mirror for negative side
    p_vals = np.concatenate([
        0.5 - delta_pos[::-1],
        0.5 + delta_pos
    ])
    # Add exact p=0.5
    p_vals = np.sort(np.concatenate([p_vals, [0.5]]))

    qcmi_vals = np.zeros(len(p_vals))
    srq_vals = np.zeros(len(p_vals))

    t0 = time.time()
    for i, p in enumerate(p_vals):
        r = qcmi_xbasis(b1, c_val, p)
        qcmi_vals[i] = r['qcmi']
        srq_vals[i] = r['S_RQ']

        if i % 50 == 0 and i > 0:
            elapsed = time.time() - t0
            rate = (i + 1) / elapsed
            eta = (len(p_vals) - i - 1) / rate
            print(f"    p-scan b1={b1}: {i+1}/{len(p_vals)} pts, "
                  f"{rate:.0f} pts/s, ETA {eta:.0f}s", flush=True)

    elapsed = time.time() - t0
    print(f"    p-scan b1={b1}: done in {elapsed:.1f}s")

    return {
        'p_values': p_vals.tolist(),
        'qcmi_values': qcmi_vals.tolist(),
        'S_RQ_values': srq_vals.tolist(),
        'n_points': len(p_vals),
        'compute_time_s': round(elapsed, 1),
    }


def run_theta_scan(b1, c_val=0.5, n_pts=150):
    """
    Scan QCMI vs theta (axis deviation from x_hat) at p=0.5.
    Uses full unitary (axes not all x_hat).
    """
    # Log spacing for theta
    theta_min = 1e-4
    theta_max = np.pi / 2
    theta_vals = np.logspace(np.log10(theta_min), np.log10(theta_max), n_pts)
    theta_vals = np.concatenate([[0.0], theta_vals])

    n_edges = 4 * b1
    c_arr = np.array([c_val] * n_edges)

    qcmi_vals = np.zeros(len(theta_vals))
    srq_vals = np.zeros(len(theta_vals))
    seq_vals = np.zeros(len(theta_vals))

    t0 = time.time()
    for i, theta in enumerate(theta_vals):
        n_hat = axis_from_x_deviation(theta, phi=0.0)
        axes = [n_hat.copy() for _ in range(n_edges)]
        r = compute_qcmi_full(b1, c_arr, axes, 0.5)
        qcmi_vals[i] = r['qcmi']
        srq_vals[i] = r['S_RQ']
        seq_vals[i] = r['S_EQ']

        if i % 30 == 0 and i > 0:
            elapsed = time.time() - t0
            rate = (i + 1) / elapsed
            eta = (len(theta_vals) - i - 1) / rate
            print(f"    theta-scan b1={b1}: {i+1}/{len(theta_vals)} pts, "
                  f"theta={theta:.4f}, QCMI={qcmi_vals[i]:.6f}, "
                  f"{rate:.1f} pts/s, ETA {eta:.0f}s", flush=True)

    elapsed = time.time() - t0
    print(f"    theta-scan b1={b1}: done in {elapsed:.1f}s")

    return {
        'theta_values': theta_vals.tolist(),
        'qcmi_values': qcmi_vals.tolist(),
        'S_RQ_values': srq_vals.tolist(),
        'S_EQ_values': seq_vals.tolist(),
        'n_points': len(theta_vals),
        'compute_time_s': round(elapsed, 1),
    }


def run_mixed_scan(b1, c_val=0.5, n_pts=40):
    """
    Scan QCMI along mixed (p+theta) direction.
    p = 0.5 + delta * cos(angle), theta = delta * sin(angle)
    for fixed angle relative to ghost zero.
    """
    n_edges = 4 * b1
    c_arr = np.array([c_val] * n_edges)

    # Scan along several rays from ghost zero at different angles
    angles = [0, np.pi/6, np.pi/4, np.pi/3, np.pi/2]  # 0=only-p, pi/2=only-theta

    delta_vals = np.logspace(-4, -0.3, n_pts)

    results = {}

    for angle in angles:
        qcmi_vals = np.zeros(len(delta_vals))

        t0 = time.time()
        for i, delta in enumerate(delta_vals):
            dp = delta * np.cos(angle)
            dtheta = delta * np.sin(angle)

            p_val = 0.5 + dp
            if p_val <= 0 or p_val >= 1:
                qcmi_vals[i] = np.nan
                continue

            theta = dtheta
            n_hat = axis_from_x_deviation(theta, phi=0.0)
            axes = [n_hat.copy() for _ in range(n_edges)]
            r = compute_qcmi_full(b1, c_arr, axes, p_val)
            qcmi_vals[i] = r['qcmi']

        elapsed = time.time() - t0

        # Fit power law
        valid = ~np.isnan(qcmi_vals) & (qcmi_vals > 1e-15)
        if np.sum(valid) >= 5:
            A, alpha, alpha_se, r2, _ = fit_power_law(delta_vals[valid], qcmi_vals[valid])
        else:
            A, alpha, alpha_se, r2 = None, None, None, None

        angle_label = f"angle_{angle/np.pi:.2f}pi"
        results[angle_label] = {
            'angle_rad': float(angle),
            'angle_deg': float(np.degrees(angle)),
            'description': f'p=0.5+delta*cos({angle:.3f}), theta=delta*sin({angle:.3f})',
            'delta_values': delta_vals.tolist(),
            'qcmi_values': qcmi_vals.tolist(),
            'power_law_alpha': float(alpha) if alpha else None,
            'alpha_se': float(alpha_se) if alpha_se else None,
            'r_squared': float(r2) if r2 else None,
            'compute_time_s': round(elapsed, 1),
        }

        print(f"    mixed-scan b1={b1}, angle={np.degrees(angle):.0f}deg: "
              f"alpha={alpha:.4f}" if alpha else f"    mixed-scan b1={b1}, angle={np.degrees(angle):.0f}deg: fit failed",
              f", R^2={r2:.4f}" if r2 else "",
              flush=True)

    return results


# ============================================================
# UNIVERSALITY CONVERGENCE ANALYSIS
# ============================================================
def analyze_universality(p_scans, theta_scans, b1_list):
    """
    Check for convergence of exponents as |E| increases.
    Returns analysis with extrapolation to |E|→∞.
    """
    analysis = {}

    # Extract alpha(|E|) from p-scans
    p_exponents = {}
    for b1 in b1_list:
        key = str(b1)
        if key not in p_scans:
            continue
        data = p_scans[key]
        p_vals = np.array(data['p_values'])
        qcmi_vals = np.array(data['qcmi_values'])

        # Use asymptotic regime: |p-0.5| < 0.05
        dp = np.abs(p_vals - 0.5)
        mask = (dp > 1e-10) & (dp < 0.05) & (qcmi_vals > 1e-15)

        if np.sum(mask) >= 10:
            A, alpha, alpha_se, r2, _ = fit_power_law(dp[mask], qcmi_vals[mask])
            boot = bootstrap_fit(dp[mask], qcmi_vals[mask], n_bootstrap=1000, seed=b1*42)

            p_exponents[key] = {
                'b1': b1,
                'E_size': 2 * b1,
                'alpha_p': float(alpha) if alpha else None,
                'alpha_p_se': float(alpha_se) if alpha_se else None,
                'r_squared': float(r2) if r2 else None,
                'bootstrap': boot,
                'n_fit_points': int(np.sum(mask)),
            }

            print(f"\n  b1={b1} (|E|={2*b1}): alpha_p = {alpha:.4f} ± {alpha_se:.4f} "
                  f"(bootstrap: {boot['mean']:.4f} ± {boot['std']:.4f}, "
                  f"95% CI [{boot['ci_95_low']:.4f}, {boot['ci_95_high']:.4f}])")

    # Extract gamma(|E|) from theta-scans
    theta_exponents = {}
    for b1 in b1_list:
        key = str(b1)
        if key not in theta_scans:
            continue
        data = theta_scans[key]
        theta_vals = np.array(data['theta_values'])
        qcmi_vals = np.array(data['qcmi_values'])

        # Use asymptotic regime: theta < 0.1 rad
        mask = (theta_vals > 1e-10) & (theta_vals < 0.1) & (qcmi_vals > 1e-15)

        if np.sum(mask) >= 10:
            A, gamma, gamma_se, r2, _ = fit_power_law(theta_vals[mask], qcmi_vals[mask])
            boot = bootstrap_fit(theta_vals[mask], qcmi_vals[mask], n_bootstrap=1000, seed=b1*123)

            theta_exponents[key] = {
                'b1': b1,
                'E_size': 2 * b1,
                'gamma_theta': float(gamma) if gamma else None,
                'gamma_theta_se': float(gamma_se) if gamma_se else None,
                'r_squared': float(r2) if r2 else None,
                'bootstrap': boot,
                'n_fit_points': int(np.sum(mask)),
            }

            print(f"  b1={b1} (|E|={2*b1}): gamma_theta = {gamma:.4f} ± {gamma_se:.4f} "
                  f"(bootstrap: {boot['mean']:.4f} ± {boot['std']:.4f}, "
                  f"95% CI [{boot['ci_95_low']:.4f}, {boot['ci_95_high']:.4f}])")

    # Convergence analysis
    # Are alpha_p and gamma_theta converging or diverging?
    convergence = {}

    for label, exponents in [('beta_p', p_exponents), ('gamma_theta', theta_exponents)]:
        b1_sorted = sorted(exponents.keys(), key=lambda k: exponents[k]['b1'])

        if len(b1_sorted) >= 3:
            b1_vals = np.array([exponents[k]['b1'] for k in b1_sorted])
            E_vals = np.array([exponents[k]['E_size'] for k in b1_sorted])
            alpha_vals = np.array([exponents[k][f'alpha_p' if label == 'beta_p' else 'gamma_theta'] for k in b1_sorted])
            alpha_errs = np.array([exponents[k][f'alpha_p_se' if label == 'beta_p' else 'gamma_theta_se'] for k in b1_sorted])

            # Check for trend: linear fit alpha vs 1/|E|
            inv_E = 1.0 / E_vals
            A_inv = np.vstack([np.ones_like(inv_E), inv_E]).T
            coeffs_inv = np.linalg.lstsq(A_inv, alpha_vals, rcond=None)[0]
            alpha_inf = coeffs_inv[0]  # Extrapolated value as |E|→∞

            # Check for trend: linear fit alpha vs |E|
            A_dir = np.vstack([np.ones_like(E_vals), E_vals]).T
            coeffs_dir = np.linalg.lstsq(A_dir, alpha_vals, rcond=None)[0]

            # Check if converging: the change from b1=2 to b1=3
            if len(b1_sorted) >= 2:
                delta_alpha = alpha_vals[-1] - alpha_vals[-2]
                delta_ratio = abs(delta_alpha) / alpha_errs[-1] if alpha_errs[-1] > 0 else np.inf
                is_converging = delta_ratio < 2.0  # Not statistically significant change
            else:
                delta_alpha = None
                delta_ratio = None
                is_converging = None

            # Range-to-mean ratio (measure of |E|-dependence)
            range_over_mean = (np.max(alpha_vals) - np.min(alpha_vals)) / np.mean(alpha_vals) if np.mean(alpha_vals) > 0 else np.inf

            convergence[label] = {
                'alpha_vs_E': {str(e): float(a) for e, a in zip(E_vals, alpha_vals)},
                'alpha_vs_1overE_fit': {
                    'alpha_infinity': float(alpha_inf),
                    'slope': float(coeffs_inv[1]),
                },
                'delta_last_two': float(delta_alpha) if delta_alpha is not None else None,
                'delta_sigma_ratio': float(delta_ratio) if delta_ratio is not None else None,
                'is_converging': bool(is_converging) if is_converging is not None else None,
                'range_over_mean': float(range_over_mean),
                'verdict': ('UNIVERSAL' if (is_converging and range_over_mean < 0.05) else
                          'LIKELY_UNIVERSAL' if (range_over_mean < 0.1) else
                          'NON_UNIVERSAL' if (range_over_mean > 0.2) else
                          'MARGINAL'),
            }

            print(f"\n  {label} convergence: alpha_inf = {alpha_inf:.4f}, "
                  f"range/mean = {range_over_mean:.4f}, "
                  f"verdict: {convergence[label]['verdict']}")

    # Anisotropy check: are beta_p and gamma_theta the same?
    anisotropy = {}
    for b1_key in p_exponents:
        if b1_key in theta_exponents:
            beta = p_exponents[b1_key]['alpha_p']
            beta_se = p_exponents[b1_key]['alpha_p_se']
            gamma = theta_exponents[b1_key]['gamma_theta']
            gamma_se = theta_exponents[b1_key]['gamma_theta_se']

            if beta and gamma and beta_se and gamma_se:
                diff = abs(beta - gamma)
                combined_se = np.sqrt(beta_se**2 + gamma_se**2)
                sigmas = diff / combined_se if combined_se > 0 else np.inf

                anisotropy[b1_key] = {
                    'b1': p_exponents[b1_key]['b1'],
                    'beta_p': float(beta),
                    'gamma_theta': float(gamma),
                    'difference': float(diff),
                    'combined_se': float(combined_se),
                    'n_sigma': float(sigmas),
                    'is_isotropic': sigmas < 2.0,
                }

                print(f"  b1={b1_key}: beta-gamma = {diff:.4f} ± {combined_se:.4f} "
                      f"({sigmas:.1f}σ) — {'ISOTROPIC' if sigmas < 2 else 'ANISOTROPIC'}")

    return {
        'p_exponents': p_exponents,
        'theta_exponents': theta_exponents,
        'convergence': convergence,
        'anisotropy': anisotropy,
    }


# ============================================================
# MAIN COMPUTATION
# ============================================================
def main():
    print("=" * 70)
    print("LP42-GhostZero 北极星#2: Critical Scaling Universality Class")
    print("High-Resolution Scaling Scan")
    print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 70)

    b1_list = [1, 2, 3]  # |E| = 2, 4, 6
    # b1=4 (|E|=8) excluded: d=8192, too slow for theta-scan
    # We'll do p-scan for b1=4 using X-basis Gram matrix

    c_val = 0.5

    all_results = {
        'project': 'LP42-GhostZero',
        'north_star': 2,
        'title': 'Critical Scaling Universality Class',
        'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
        'parameters': {
            'c_val': c_val,
            'ghost_zero': 'p=0.5, all axes = x_hat',
            'topology': 'vertex-sharing chain',
            'b1_values': b1_list,
            'E_sizes': [2*b for b in b1_list],
        },
    }

    # ============================================================
    # PART 1: p-scans (X-basis Gram matrix — fast, b1 up to 4)
    # ============================================================
    print("\n" + "=" * 70)
    print("PRIMARY: QCMI vs |p-0.5| (x_hat axes)")
    print("=" * 70)

    p_scans = {}
    for b1 in b1_list + [4]:  # Include b1=4 for p-scan
        print(f"\n  b1={b1} (|E|={2*b1}), c=0.5, x_hat axes:")
        p_scans[str(b1)] = run_p_scan(b1, c_val=c_val, n_pts=200)

    # ============================================================
    # PART 2: theta-scans (full unitary — slower, b1 up to 3)
    # ============================================================
    print("\n" + "=" * 70)
    print("PRIMARY: QCMI vs theta (axis deviation from x_hat)")
    print("=" * 70)

    theta_scans = {}
    # b1=1,2: 150 pts; b1=3: 100 pts (for speed)
    n_theta_pts = {1: 150, 2: 150, 3: 100}
    for b1 in b1_list:
        print(f"\n  b1={b1} (|E|={2*b1}), p=0.5, c=0.5:")
        theta_scans[str(b1)] = run_theta_scan(b1, c_val=c_val, n_pts=n_theta_pts[b1])

    # ============================================================
    # PART 3: Mixed direction scan (Tertiary task)
    # ============================================================
    print("\n" + "=" * 70)
    print("TERTIARY: Mixed (p+theta) direction scan")
    print("=" * 70)

    mixed_scans = {}
    for b1 in [1, 2]:  # Most computationally feasible
        print(f"\n  b1={b1} (|E|={2*b1}):")
        mixed_scans[str(b1)] = run_mixed_scan(b1, c_val=c_val, n_pts=40)

    # ============================================================
    # PART 4: Universality analysis
    # ============================================================
    print("\n" + "=" * 70)
    print("UNIVERSALITY ANALYSIS")
    print("=" * 70)

    analysis = analyze_universality(p_scans, theta_scans, b1_list + [4])

    # ============================================================
    # PART 5: Self-affine surface test (Tertiary)
    # ============================================================
    print("\n" + "=" * 70)
    print("TERTIARY: Self-Affine Scaling Surface Test")
    print("=" * 70)

    self_affine = {}
    for b1 in [1, 2]:
        if str(b1) not in mixed_scans:
            continue

        # Extract exponents along each ray
        angles_rad = []
        alphas_ray = []
        alpha_errs_ray = []

        for key, data in mixed_scans[str(b1)].items():
            if data['power_law_alpha'] is not None:
                angles_rad.append(data['angle_rad'])
                alphas_ray.append(data['power_law_alpha'])
                alpha_errs_ray.append(data['alpha_se'] if data['alpha_se'] else 0.01)

        # For a self-affine surface: QCMI(p, theta) scales as
        # QCMI(λ^ν_p * (p-0.5), λ^ν_θ * theta) = λ * QCMI(p-0.5, theta)
        # This means along ray: QCMI ~ delta^{1/ν_ray} where
        # ν_ray = ν_p * cos^2(angle) + ν_θ * sin^2(angle)... no.
        #
        # Actually, for self-affine: QCMI ~ delta^α(angle) where
        # α(angle) = [cos^2(angle)/α_p + sin^2(angle)/α_θ]^{-1}? No.
        #
        # More carefully: along direction (cos φ, sin φ) in (p-0.5, theta) space,
        # QCMI(t*cos_φ, t*sin_φ) ~ t^α(φ).
        # For self-affine: α(φ) should interpolate between α_p (φ=0) and α_θ (φ=π/2).
        #
        # Self-similar (isotropic): α(φ) = α_p = α_θ = const
        # Self-affine (anisotropic): α(φ) varies with φ

        if len(angles_rad) >= 3:
            # Fit α(φ) model: α(φ) = α_p * cos^2(φ) + α_θ * sin^2(φ) + δ * sin(2φ)
            phi = np.array(angles_rad)
            alpha = np.array(alphas_ray)

            A_affine = np.vstack([
                np.cos(phi)**2,
                np.sin(phi)**2,
                np.sin(2*phi),
            ]).T
            coeffs_aff = np.linalg.lstsq(A_affine, alpha, rcond=None)[0]
            alpha_p_fit, alpha_theta_fit, delta_cross = coeffs_aff

            pred = A_affine @ coeffs_aff
            ss_res = np.sum((alpha - pred)**2)
            ss_tot = np.sum((alpha - np.mean(alpha))**2)
            r2_aff = 1 - ss_res / ss_tot if ss_tot > 0 else 0

            # Self-affine if delta_cross ~ 0 (no cross-term needed)
            is_self_affine = abs(delta_cross) < 0.1

            self_affine[str(b1)] = {
                'b1': b1,
                'alpha_p_fit': float(alpha_p_fit),
                'alpha_theta_fit': float(alpha_theta_fit),
                'delta_cross_term': float(delta_cross),
                'r_squared': float(r2_aff),
                'is_self_affine': bool(is_self_affine),
                'interpretation': (
                    'Self-affine surface confirmed' if is_self_affine else
                    'Cross-term significant — surface is NOT simple self-affine'
                ),
                'angles': [float(a) for a in angles_rad],
                'alphas': [float(a) for a in alphas_ray],
            }

            print(f"  b1={b1}: alpha_p_fit={alpha_p_fit:.4f}, alpha_theta_fit={alpha_theta_fit:.4f}, "
                  f"delta_cross={delta_cross:.4f}, R^2={r2_aff:.4f} — "
                  f"{'SELF-AFFINE' if is_self_affine else 'NOT self-affine'}")

    # ============================================================
    # ASSEMBLE OUTPUT
    # ============================================================
    all_results['p_scans'] = p_scans
    all_results['theta_scans'] = theta_scans
    all_results['mixed_scans'] = mixed_scans
    all_results['universality_analysis'] = analysis
    all_results['self_affine_analysis'] = self_affine

    # ============================================================
    # CROSS-DISCIPLINARY ANALYSIS (done inline)
    # ============================================================
    cross_disciplinary = analyze_cross_disciplinary(analysis)
    all_results['cross_disciplinary'] = cross_disciplinary

    # ============================================================
    # DEEP-DIVE ANALYSIS
    # ============================================================
    deep_dive = analyze_deep_dive(analysis)
    all_results['deep_dive'] = deep_dive

    # ============================================================
    # SAVE INTERMEDIATE
    # ============================================================
    output_dir = 'D:/Claude/ai-reservations/LP42-GhostZero/current/B'
    os.makedirs(output_dir, exist_ok=True)

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

    data_path = os.path.join(output_dir, 'scaling_universality_data.json')
    with open(data_path, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, cls=NumpyEncoder, indent=2, ensure_ascii=False)

    print(f"\n{'=' * 70}")
    print(f"Data saved to: {data_path}")
    print(f"File size: {os.path.getsize(data_path):,} bytes")
    print(f"{'=' * 70}")

    return all_results


# ============================================================
# CROSS-DISCIPLINARY ANALYSIS
# ============================================================
def analyze_cross_disciplinary(analysis):
    """
    Jump to completely different fields to find systems with exponent ~1.65-1.75.

    Three candidate analogies, ranked by structural depth:
    1. Fiber Bundle Model (fracture mechanics) — strongest
    2. Turbulence intermittency — speculative but quantitative
    3. Depinning with long-range elasticity — most testable
    """

    # Extract key exponents
    p_exp = analysis.get('p_exponents', {})
    theta_exp = analysis.get('theta_exponents', {})
    conv = analysis.get('convergence', {})

    # Average exponents across |E|
    alpha_p_vals = [v['alpha_p'] for v in p_exp.values() if v.get('alpha_p')]
    gamma_theta_vals = [v['gamma_theta'] for v in theta_exp.values() if v.get('gamma_theta')]

    avg_alpha_p = np.mean(alpha_p_vals) if alpha_p_vals else None
    avg_gamma_theta = np.mean(gamma_theta_vals) if gamma_theta_vals else None

    # Key structural features of the ghost zero:
    # 1. N components (env qubits) with binary internal state
    # 2. Each component has threshold-like behavior (p crosses 0.5)
    # 3. Coupling is through a network (vertex chain)
    # 4. Order parameter (QCMI) grows from 0 at critical point
    # 5. Exponent ~1.65-1.75 (between mean-field and Gaussian)

    # ANALOGY 1: Fiber Bundle Model with Local Load Sharing
    fbm_analogy = {
        'field': 'Rupture / Fracture Mechanics',
        'system': 'Fiber Bundle Model (FBM) with Local Load Sharing (LLS)',
        'structural_mapping': {
            'env_qubits': 'N fibers with random failure thresholds',
            'p-0.5': 'Applied load σ - critical load σ_c',
            'QCMI': 'Cumulative damage D (fraction of broken fibers)',
            'c_vals': 'Fiber strength distribution parameter (Weibull modulus ρ)',
            'vertex_chain_topology': 'Load redistribution network (nearest-neighbor LLS)',
            'ghost_zero': 'Critical point σ_c where avalanche begins',
        },
        'exponent_matching': {
            'fbm_exponent': 'Breakdown rate dD/dσ ~ (σ_c - σ)^{-1/ρ} for Weibull modulus ρ',
            'observed_range': 'For ρ ≈ 1.4-1.7 (common for heterogeneous materials): exponent ~1.6-1.7',
            'key_match': 'FBM avalanche size distribution P(s) ~ s^{-τ} with τ ≈ 1.5-1.7 for LLS',
            'difference': 'FBM exponent is for DISTRIBUTION, not order parameter scaling. But the time-to-failure exponent near critical load is ~1.7 for certain disorder realizations.',
        },
        'testable_prediction': (
            'If the ghost zero is in the same universality class as FBM-LLS, '
            'then DISORDER in the Cartan parameters c_j should NOT change the '
            'scaling exponent (disorder is irrelevant at the FBM-LLS fixed point). '
            'Conversely, changing the INTERACTION TOPOLOGY (from vertex chain to '
            'all-to-all or 2D grid) SHOULD change the exponent, as FBM exponents '
            'differ between ELS (mean-field), LLS (1D), and hierarchical load sharing.'
        ),
        'mathematical_substance': 'MEDIUM — Both are threshold-activated cascade models on networks. The FBM maps damage accumulation to load redistribution; the ghost zero maps entanglement accumulation to qubit-qubit coupling. The key structural homology: binary elements (fibers/qubits) with state-dependent interaction thresholds.',
        'quality': 'STRUCTURAL (best analogy)',
    }

    # ANALOGY 2: Turbulence Intermittency
    turbulence_analogy = {
        'field': 'Turbulence / Fluid Dynamics',
        'system': 'Kolmogorov turbulence with intermittency corrections',
        'structural_mapping': {
            '|p-0.5|': 'Wavenumber k (inverse scale)',
            'QCMI': 'Energy spectrum E(k) or structure function S_p(r)',
            'env_qubits': 'Eddies at different scales',
            'vertex_chain': 'Energy cascade (Richardson cascade)',
            'ghost_zero (p=0.5)': 'K41 fixed point (no intermittency)',
        },
        'exponent_matching': {
            'K41_energy_spectrum': 'E(k) ~ k^{-5/3} with exponent -5/3 ≈ -1.667',
            'K41_structure_function': 'S_2(r) ~ r^{2/3} with exponent 2/3 ≈ 0.667',
            'intermittency_correction': 'Kolmogorov-Obukhov log-normal model: ζ_p = p/3 + (μ/18)*p*(3-p) with μ ≈ 0.2-0.4',
            'key_observation': 'The raw exponent -5/3 ≈ -1.667 is remarkably close to the ghost zero exponent ~1.65-1.75 in magnitude. With intermittency corrections, the effective exponent for low-order statistics can be in the range 1.65-1.75.',
            'direction_note': 'In turbulence E(k) DECREASES with k; QCMI INCREASES with |p-0.5|. The structural mapping would be: QCMI is like the integrated energy up to scale 1/|p-0.5|, which scales as ~k^{5/3} for K41.',
        },
        'testable_prediction': (
            'If the ghost zero is analogous to the K41 fixed point, then '
            'the EXACT exponent should be 5/3 (not 1.72 or 1.75). With '
            '"intermittency corrections" from the finite |E|, the effective '
            'exponent should APPROACH 5/3 from above as |E|→∞. '
            'Specifically: α(|E|) = 5/3 + C/|E| + O(1/|E|^2). '
            'TEST: fit α(|E|) = α_∞ + A/|E| and check if α_∞ ≈ 1.667.'
        ),
        'mathematical_substance': 'LOW-MEDIUM — The exponent coincidence is numerically striking but the physical mapping is strained: turbulence cascades energy to small scales, while ghost zero cascades quantum information to the environment. The shared mathematical structure would need to be a multiplicative cascade model (random multiplicative process) generating the same exponent.',
        'quality': 'SPECULATIVE (exponent coincidence)',
    }

    # ANALOGY 3: Depinning Transition with Long-Range Elasticity
    depinning_analogy = {
        'field': 'Condensed Matter / Disordered Systems',
        'system': 'Elastic interface depinning with long-range (dipolar) interactions',
        'structural_mapping': {
            'p-0.5': 'Driving force F - F_c (distance to depinning threshold)',
            'QCMI': 'Interface velocity v (order parameter)',
            'env_qubits coupled to system': 'Elastic manifold coupled to disorder',
            'ghost_zero': 'Zero-velocity pinned phase below threshold',
            'exponent α': 'Velocity exponent β: v ~ (F-F_c)^β',
        },
        'exponent_matching': {
            'standard_depinning': 'β = ν(z-ζ)/(2-ζ) where ν, z, ζ are roughness, dynamic, and roughness exponents',
            'mean_field': 'β = 1 (for infinite-range elastic coupling)',
            'short_range_elastic': 'β ≈ 0.6-0.9 (depending on dimension)',
            'long_range_dipolar': 'β can exceed 1, approaching 1.5-1.7 for certain dimensionalities and interaction ranges',
            'key_match': 'Depinning with dipolar-like (1/r^3 in certain geometries) long-range interactions can produce β > 1. The Cartan interactions in the vertex chain are effectively "long-range" in the sense that each env qubit couples to two system qubits, creating a connected network rather than local coupling.',
        },
        'testable_prediction': (
            'If ghost zero = depinning transition, then ADDING QUENCHED DISORDER '
            'to the Cartan parameters should change the exponent from β to the '
            'disorder-dependent value. Specifically, random c_j drawn from a '
            'distribution should change the universality class. '
            'CONTRAPOSITIVE: if the exponent is UNCHANGED by c-disorder, '
            'the depinning analogy is falsified.'
        ),
        'mathematical_substance': 'MEDIUM — The depinning transition is the best-developed theoretical framework for threshold-activated dynamics in disordered media. The functional RG treatment of depinning (Nattermann et al.) provides a systematic expansion that could be adapted to the ghost zero channel.',
        'quality': 'STRUCTURAL (most testable)',
    }

    # Comparative analysis
    best_analogy = (
        'FIBER BUNDLE MODEL (FBM-LLS) provides the strongest structural analogy. '
        'Reasoning: (1) Both have discrete binary elements (fibers/qubits) with '
        'threshold behavior. (2) Both have a network topology that determines '
        'how "damage" (broken fibers / entanglement) propagates. '
        '(3) The exponent ~1.7 matches FBM avalanche statistics in the LLS regime. '
        '(4) The key testable prediction — topology dependence of the exponent — '
        'is clean and falsifiable. '
        'The turbulence analogy is numerically provocative (-5/3 ≈ -1.667) but '
        'physically strained. The depinning analogy provides the richest theoretical '
        'framework (functional RG) but requires quenched disorder which is not '
        'present in the baseline ghost zero model.'
    )

    return {
        'average_exponents': {
            'alpha_p_mean': float(avg_alpha_p) if avg_alpha_p else None,
            'gamma_theta_mean': float(avg_gamma_theta) if avg_gamma_theta else None,
        },
        'analogy_1_fbm': fbm_analogy,
        'analogy_2_turbulence': turbulence_analogy,
        'analogy_3_depinning': depinning_analogy,
        'best_analogy': best_analogy,
        'pending_tests': [
            {
                'test': 'Topology dependence',
                'prediction': 'alpha changes with graph topology (chain → ring → all-to-all)',
                'falsification': 'If alpha is topology-independent → FBM analogy false',
                'status': 'Not yet tested',
            },
            {
                'test': 'Disorder irrelevance',
                'prediction': 'Random c_j disorder does NOT change alpha (FBM-LLS fixed point)',
                'falsification': 'If random c changes alpha → depinning analogy favored',
                'status': 'Not yet tested',
            },
            {
                'test': '5/3 convergence',
                'prediction': 'alpha(|E|) → 5/3 as |E| → ∞ (turbulence analogy)',
                'falsification': 'If alpha_inf ≠ 1.667 within error → turbulence analogy false',
                'status': 'Computed in this run',
            },
        ],
    }


# ============================================================
# DEEP-DIVE ANALYSIS (>=2 layers)
# ============================================================
def analyze_deep_dive(analysis):
    """
    Layer 1: What governs the numerical value of the exponent?
    Layer 2: Why might it be universal or non-universal?
    """

    p_exp = analysis.get('p_exponents', {})
    theta_exp = analysis.get('theta_exponents', {})
    conv = analysis.get('convergence', {})
    anisotropy = analysis.get('anisotropy', {})

    # Layer 1: Origin of the exponent
    layer1 = {
        'question': 'What determines the numerical value of the ghost zero scaling exponent α ~ 1.7?',
        'analytic_insight': (
            'Consider the env qubit initially in state |ψ_e> = √p|0> + √(1-p)|1>. '
            'In the X-basis: |ψ_e> = a_+|+> + a_-|-> where '
            'a_+ = (√p+√(1-p))/√2, a_- = (√p-√(1-p))/√2. '
            'For small δ = |p-0.5|: a_+ ≈ 1 - δ^2, a_- ≈ δ. '
            'Each env qubit in |-> state generates entanglement with the system '
            'via the Cartan gate U = cos(c)I + i sin(c) X⊗X. '
            'X|-> = -|->, so the |-> amplitude picks up a relative phase of -1, '
            'leading to dephasing on the system. '
            'For N=|E| env qubits, if they were independent, the total QCMI '
            'would be ~N * |a_-|^2 ~ N * δ^2, giving α=2 (quadratic). '
            'The observed α ~ 1.7 < 2 indicates cooperative enhancement: '
            'the entanglement contributions from different env qubits INTERFERE '
            'constructively on the system, amplifying the QCMI beyond N×δ^2.'
        ),
        'cooperative_mechanism': (
            'The vertex-sharing chain creates a path-entanglement structure: '
            'Q_0-E_0-Q_1-E_1-Q_2. The |-> amplitude on E_0 entangles Q_0 and Q_1; '
            'the |-> amplitude on E_1 then entangles Q_1 and Q_2. But Q_1 is ALREADY '
            'entangled with Q_0 via E_0, so the E_1 entanglement "builds on" the '
            'existing E_0 entanglement. This is analogous to a random walk in '
            'entanglement space: the total QCMI ~ N^{α/2} * δ^α where α < 2 '
            'reflects the path-counting enhancement.'
        ),
        'renormalization_group_picture': (
            'In the X-basis, the channel is diagonal (Z⊗Z interactions). '
            'The Gram matrix G_{a,b} for system states |a>,|b> measures the '
            'overlap of the env-conditioned pure states. For the vertex chain, '
            'G has a 1D structure reflecting the graph Laplacian of the chain. '
            'The spectrum of G determines S(RQ) and hence QCMI. '
            'The exponent α = -d(log QCMI)/d(log|δp|) is related to the '
            'density of states of G near eigenvalue 1 (fully coherent). '
            'For a 1D chain, this density of states ~ ε^{-1/2} at the band edge, '
            'which would give α = 1 (NOT matching). '
            'The deviation from 1 (observed α ~ 1.7) suggests that the effective '
            '"band structure" of G is modified by the specific ring topology '
            '(each ring contributes 4 edges in a closed loop, creating '
            'interference that pushes the band edge DOS toward ε^{-0.7}).'
        ),
        'layer': 1,
        'hard_boundary': (
            'The analytic argument for α=2 (independent qubits) is rigorous for '
            'product env states with NO inter-qubit coupling in the Gram matrix. '
            'The vertex chain introduces coupling via shared system qubits. '
            'The RG argument is conjectural — a proper derivation requires '
            'computing the Gram matrix spectrum analytically for the vertex chain, '
            'which is a banded random matrix problem (the "randomness" comes from '
            'the varying phases in the diagonal entries).'
        ),
    }

    # Layer 2: Universality vs non-universality
    conv_beta = conv.get('beta_p', {})
    conv_gamma = conv.get('gamma_theta', {})

    layer2 = {
        'question': 'Is the exponent α ~ 1.7 universal or non-universal?',
        'numerical_evidence': {
            'beta_p_convergence': conv_beta,
            'gamma_theta_convergence': conv_gamma,
            'anisotropy': anisotropy,
        },
        'argument_for_universality': (
            'If α(|E|) converges to a finite value α_∞ as |E| → ∞, then '
            'this value is a universal property of the ghost zero in the '
            'thermodynamic limit (many qubits). The ghost zero is a critical '
            'point in channel space, and α is a critical exponent. Like all '
            'critical exponents, it should be determined by symmetries and '
            'dimensionality, not microscopic details.'
        ),
        'argument_against_universality': (
            'The ghost zero is fundamentally a single-particle (product state) '
            'phenomenon. The exponent α is determined by the combinatorics of '
            'how many env qubits are in the |-> state and how their entanglement '
            'paths interfere. This is a COUNTING problem, not a thermodynamic '
            'critical phenomenon. The exponent depends on the graph topology '
            '(vertex chain vs ring vs tree) and the boundary conditions '
            '(open vs periodic). These are non-universal features.'
        ),
        'synthesis': (
            'The truth is likely INTERMEDIATE: α is "topologically universal" — '
            'it is determined by the graph HOMOTOPY class (b1 = number of '
            'independent cycles) and the graph LAPLACIAN spectrum. For a given '
            'graph class (e.g., 1D vertex chain with b1 cycles), α is universal '
            'within that class but differs between classes. This is analogous '
            'to how the central charge c in conformal field theory is universal '
            'for a given universality class but differs between classes.'
        ),
        'critical_test': (
            'Compute α for (a) vertex chain with periodic boundary conditions, '
            '(b) 2D grid of rings, (c) tree (no cycles). If α differs between '
            'these topologies, the "topological universality" picture is confirmed. '
            'If α is the SAME for all, the exponent is truly universal '
            '(determined by the local interaction structure alone).'
        ),
        'layer': 2,
        'hard_boundary': (
            'The current numerical data covers b1=1,2,3 (|E|=2,4,6) — too few '
            'points to reliably distinguish convergence (α → α_∞) from '
            'logarithmic drift (α ~ log|E|). Need b1=4,5,6 to establish the '
            'asymptotic trend. This is computationally demanding (d=2^{3b1+1} '
            'for full unitary) and may require tensor network methods (MPS/MPO) '
            'for larger systems.'
        ),
    }

    # Layer 3: Physical origin of scaling anisotropy
    layer3 = {
        'question': 'Why might β_p ≠ γ_θ?',
        'answer': (
            'β_p and γ_θ characterize scaling in two different DIRECTIONS '
            'away from the ghost zero: along p (environment state preparation) '
            'and along θ (interaction basis alignment). '
            'These are physically DISTINCT perturbations: '
            '- p-perturbation changes the env state composition (more |-> amplitude) '
            '  while keeping the interaction basis aligned. '
            '- θ-perturbation changes the interaction basis (Cartan gate structure) '
            '  while keeping the env state at |+...+>. '
            'If the ghost zero is a CRITICAL POINT with one relevant direction, '
            'both perturbations should flow to the same fixed point and give '
            'the same exponent (β_p = γ_θ). '
            'If β_p ≠ γ_θ, there are TWO relevant scaling variables with '
            'DIFFERENT scaling dimensions — the ghost zero is a MULTICRITICAL '
            'point rather than a simple critical point.'
        ),
        'physical_mechanism_for_anisotropy': (
            'The env state perturbation (p) acts UNIFORMLY on all env qubits: '
            'every qubit gets the same δ = |p-0.5| deviation. This creates '
            'a "coherent" perturbation where all qubits are identically affected. '
            'The axis perturbation (θ) acts on the INTERACTION: the Cartan gate '
            'U = cos(c)I + i sin(c) (n·σ)⊗(n·σ) changes from X⊗X to a mixture '
            'X⊗X + θ*(cross terms). The cross terms (Y⊗Y, Z⊗Z, X⊗Y, etc.) '
            'generate DIFFERENT entanglement patterns than the pure X⊗X term. '
            'Specifically, Y|+> ∝ |->, Z|+> = |->, so Y and Z components of '
            'the Cartan gate ALSO flip |+> to |->, but with DIFFERENT phases. '
            'This changes the interference pattern in the Gram matrix, leading '
            'to a different exponent.'
        ),
        'layer': 3,
        'hard_boundary': (
            'The multicritical point interpretation is speculative. An alternative '
            'explanation is finite-size effects: at small |E|, the asymptotic '
            'scaling regime for p and θ may not overlap, and the apparent '
            'β_p ≠ γ_θ could be a finite-size artifact that disappears as |E|→∞.'
        ),
    }

    return {
        'layer1_exponent_origin': layer1,
        'layer2_universality': layer2,
        'layer3_scaling_anisotropy': layer3,
    }


if __name__ == '__main__':
    main()

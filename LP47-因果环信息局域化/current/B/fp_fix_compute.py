"""
LP47 fp_fix: Unified partition convention computation
=====================================================
Partition I (big B, A博士 convention): A={0}, C={k}, B=[n]\{0,k}
Partition II (small B, B博士 original): A={0}, B={k}, C={k+1 mod n}

All computations on cluster rings C_n only (periodic boundary).
Perturbations: Hmix (Hadamard mixing) and T-gate superposition.
"""

import numpy as np
from numpy.linalg import eigvalsh
from scipy.linalg import sqrtm
import json
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# Core functions
# ============================================================

def build_cluster_ring_state(n):
    """Build cluster ring state |C_n> with periodic boundary.
    |C_n> = prod_{(i,i+1)} CZ_{i,i+1} |+>^n
    """
    dim = 2**n
    # Start with |+>^n
    psi = np.ones(dim, dtype=complex) / np.sqrt(dim)
    # Apply CZ gates for edges (i, i+1 mod n)
    for i in range(n):
        j = (i + 1) % n
        # CZ = diag(1,1,1,-1) in computational basis
        phase = np.ones(dim, dtype=complex)
        for x in range(dim):
            if ((x >> i) & 1) and ((x >> j) & 1):
                phase[x] = -1.0
        psi = phase * psi
    return psi

def partial_trace(psi, keep_qubits, n_total):
    """Compute rho = Tr_{not keep} |psi><psi|"""
    keep = sorted(keep_qubits)
    trace_out = sorted(set(range(n_total)) - set(keep))

    dim_keep = 2**len(keep)
    rho = np.zeros((dim_keep, dim_keep), dtype=complex)

    # Reshape psi to tensor
    psi_tensor = psi.reshape([2] * n_total)

    # Trace axes in reverse order to maintain correct indexing
    trace_axes = trace_out
    # Build conjugate tensor
    psi_conj = psi_tensor.conj()

    # Contract all trace axes
    for ax in sorted(trace_axes, reverse=True):
        psi_tensor = np.tensordot(np.eye(2), psi_tensor, axes=([1], [ax]))
        # Actually use einsum for correctness
        break  # Use different approach

    # Use einsum approach - more reliable
    # Build einsum subscripts
    all_indices = list(range(n_total))
    # First index set for psi
    psi_subs = []
    conj_subs = []
    for i in range(n_total):
        psi_subs.append(chr(ord('a') + i))
    for i in range(n_total):
        conj_subs.append(chr(ord('a') + n_total + i))

    # Map keep indices to output
    out_map = {}
    for ki in keep:
        out_map[psi_subs[ki]] = psi_subs[ki]
        out_map[conj_subs[ki]] = conj_subs[ki]

    # Contract trace indices
    contract_list = []
    for ti in trace_out:
        contract_list.extend([psi_subs[ti], conj_subs[ti]])

    # Output indices
    out_indices = []
    for ki in keep:
        out_indices.extend([psi_subs[ki], conj_subs[ki]])

    # Build full subscript string
    full_sub = ''.join(psi_subs) + ',' + ''.join(conj_subs) + '->' + ''.join(out_indices)
    # Add contraction
    # Actually let me use a simpler, if less elegant, iterative approach

    # Method: reshape to (2^k, 2^t, 2^k, 2^t) and trace
    # Reorder axes: first keep axes, then trace axes
    axes_order = keep + trace_out
    psi_reordered = np.transpose(psi_tensor, axes=axes_order)

    dim_k = 2**len(keep)
    dim_t = 2**len(trace_out)
    psi_mat = psi_reordered.reshape(dim_k, dim_t)

    rho = psi_mat @ psi_mat.conj().T
    return rho

def von_neumann_entropy(rho, tol=1e-14):
    """Compute von Neumann entropy S(rho) = -Tr(rho ln rho) in nats."""
    evals = eigvalsh(rho)
    # Clamp negative eigenvalues to zero (numerical noise)
    evals = np.maximum(evals, 0)
    # Filter very small eigenvalues
    evals = evals[evals > tol]
    if len(evals) == 0:
        return 0.0
    return -np.sum(evals * np.log(evals))

def compute_qcmi(psi, n, partition):
    """Compute QCMI for given partition.

    partition: dict with 'A', 'B', 'C' keys, each a list of qubit indices
    Returns: (qcmI, S_AB, S_BC, S_B, S_ABC)
    """
    A = partition['A']
    B = partition['B']
    C = partition['C']

    AB = sorted(set(A) | set(B))
    BC = sorted(set(B) | set(C))
    ABC = sorted(set(A) | set(B) | set(C))

    S_AB = von_neumann_entropy(partial_trace(psi, AB, n))
    S_BC = von_neumann_entropy(partial_trace(psi, BC, n))
    S_B = von_neumann_entropy(partial_trace(psi, B, n))
    S_ABC = von_neumann_entropy(partial_trace(psi, ABC, n))

    qcmi = S_AB + S_BC - S_B - S_ABC
    return qcmi, S_AB, S_BC, S_B, S_ABC

def partition_I(n, k):
    """A博士 convention: A={0}, C={k}, B=[n]\{0,k}"""
    return {
        'A': [0],
        'B': sorted(set(range(n)) - {0, k}),
        'C': [k]
    }

def partition_II(n, k):
    """B博士 original: A={0}, B={k}, C={k+1 mod n}"""
    return {
        'A': [0],
        'B': [k],
        'C': [(k + 1) % n]
    }

# ============================================================
# Perturbations
# ============================================================

def apply_hmix(psi, n, q, theta):
    """Apply Hmix perturbation at qubit q: |psi> -> cos(theta)|psi> + sin(theta) H_q|psi>"""
    dim = 2**n
    H = np.array([[1, 1], [1, -1]]) / np.sqrt(2)
    # Build full H_q operator
    Hq_full = np.eye(1, dtype=complex)
    for i in range(n):
        if i == q:
            Hq_full = np.kron(Hq_full, H)
        else:
            Hq_full = np.kron(Hq_full, np.eye(2))

    perturbed = np.cos(theta) * psi + np.sin(theta) * (Hq_full @ psi)
    return perturbed

def apply_T_superposition(psi, n, q, theta):
    """Apply T-gate superposition at qubit q.
    |psi(theta)> = cos(theta)|psi> + sin(theta) |perp>
    where |perp> = (T_q|psi> - <psi|T_q|psi>|psi>) / norm
    """
    T = np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]], dtype=complex)
    # Build full T_q operator
    Tq_full = np.eye(1, dtype=complex)
    for i in range(n):
        if i == q:
            Tq_full = np.kron(Tq_full, T)
        else:
            Tq_full = np.kron(Tq_full, np.eye(2))

    Tpsi = Tq_full @ psi
    overlap = np.vdot(psi, Tpsi)  # <psi|T|psi>

    perp_unnorm = Tpsi - overlap * psi
    perp_norm = np.sqrt(np.vdot(perp_unnorm, perp_unnorm))

    if perp_norm < 1e-14:
        return psi.copy(), overlap, 0.0

    perp = perp_unnorm / perp_norm

    perturbed = np.cos(theta) * psi + np.sin(theta) * perp
    return perturbed, overlap, perp_norm

# ============================================================
# Model fitting
# ============================================================

def fit_M3(theta_vals, qcmi_vals):
    """Fit M3: delta_QCMI = alpha * theta^2 * ln(1/theta) + beta * theta^2"""
    x = np.array(theta_vals)
    y = np.array(qcmi_vals)

    t2 = x**2
    t2_ln = t2 * np.log(1.0 / x)

    X = np.column_stack([t2_ln, t2])
    coeffs, residuals, rank, sv = np.linalg.lstsq(X, y, rcond=None)

    alpha, beta = coeffs
    y_pred = alpha * t2_ln + beta * t2
    rss = np.sum((y - y_pred)**2)

    return alpha, beta, rss

def fit_M4(theta_vals, qcmi_vals):
    """Fit M4: delta_QCMI = alpha * theta^2 * ln(1/theta) + beta * theta^2 + gamma * theta^2 * ln^2(1/theta)"""
    x = np.array(theta_vals)
    y = np.array(qcmi_vals)

    t2 = x**2
    ln_inv = np.log(1.0 / x)
    t2_ln = t2 * ln_inv
    t2_ln2 = t2 * ln_inv**2

    X = np.column_stack([t2_ln, t2, t2_ln2])
    coeffs, residuals, rank, sv = np.linalg.lstsq(X, y, rcond=None)

    alpha, beta, gamma = coeffs
    y_pred = alpha * t2_ln + beta * t2 + gamma * t2_ln2
    rss = np.sum((y - y_pred)**2)

    return alpha, beta, gamma, rss

def compute_AICc(rss, n_points, n_params):
    """Compute corrected AIC: AICc = n * ln(RSS/n) + 2k + 2k(k+1)/(n-k-1)"""
    if rss <= 0 or n_points <= n_params + 1:
        return np.inf
    aic = n_points * np.log(rss / n_points) + 2 * n_params
    correction = 2 * n_params * (n_params + 1) / (n_points - n_params - 1)
    return aic + correction

# ============================================================
# Main computation
# ============================================================

def compute_protection_horizon(n_vals, k_vals, theta_vals, perturbation='Hmix'):
    """Compute protection horizon matrices for given n, k values.
    For each qubit q, compute QCMI under Partition I and II.
    """
    results = {}

    for n in n_vals:
        print(f"\n{'='*60}")
        print(f"Computing n={n}")
        print(f"{'='*60}")

        # Build base cluster ring state
        psi_base = build_cluster_ring_state(n)

        for k in k_vals:
            if k >= n:
                continue
            # For Partition II, check k+1 < n
            if (k + 1) % n == k:  # degenerate case
                continue

            key_I = f"n{n}_k{k}_partition_I"
            key_II = f"n{n}_k{k}_partition_II"

            pI = partition_I(n, k)
            pII = partition_II(n, k)

            # Baseline QCMI
            baseline_I, *_ = compute_qcmi(psi_base, n, pI)
            baseline_II, *_ = compute_qcmi(psi_base, n, pII)

            results[key_I] = {
                'n': n, 'k': k, 'partition': 'I',
                'A': pI['A'], 'B': pI['B'], 'C': pI['C'],
                'baseline': float(baseline_I),
                'by_qubit': {}
            }
            results[key_II] = {
                'n': n, 'k': k, 'partition': 'II',
                'A': pII['A'], 'B': pII['B'], 'C': pII['C'],
                'baseline': float(baseline_II),
                'by_qubit': {}
            }

            for q in range(n):
                print(f"  k={k}, q={q}...", end=' ', flush=True)

                qcmi_I_vals = []
                qcmi_II_vals = []

                for theta in theta_vals:
                    if perturbation == 'Hmix':
                        psi_pert = apply_hmix(psi_base.copy(), n, q, theta)
                    else:
                        psi_pert, _, _ = apply_T_superposition(psi_base.copy(), n, q, theta)

                    qcmi_I, *_ = compute_qcmi(psi_pert, n, pI)
                    qcmi_II, *_ = compute_qcmi(psi_pert, n, pII)

                    qcmi_I_vals.append(float(qcmi_I))
                    qcmi_II_vals.append(float(qcmi_II))

                # M4 fits for small theta
                # Use theta <= 0.10 for protection classification
                small_mask = [t <= 0.10 for t in theta_vals]
                small_thetas = [theta_vals[i] for i in range(len(theta_vals)) if small_mask[i]]
                small_qcmi_I = [qcmi_I_vals[i] for i in range(len(theta_vals)) if small_mask[i]]
                small_qcmi_II = [qcmi_II_vals[i] for i in range(len(theta_vals)) if small_mask[i]]

                # Compute delta QCMI
                delta_I = [v - results[key_I]['baseline'] for v in qcmi_I_vals]
                delta_II = [v - results[key_II]['baseline'] for v in qcmi_II_vals]
                delta_I_small = [v - results[key_I]['baseline'] for v in small_qcmi_I]
                delta_II_small = [v - results[key_II]['baseline'] for v in small_qcmi_II]

                # Fit M4
                alpha_I, beta_I, gamma_I, _ = fit_M4(theta_vals, delta_I)
                alpha_II, beta_II, gamma_II, _ = fit_M4(theta_vals, delta_II)

                # Max delta at theta=0.10
                idx_010 = min(range(len(theta_vals)), key=lambda i: abs(theta_vals[i] - 0.10))
                max_delta_I = abs(delta_I[idx_010])
                max_delta_II = abs(delta_II[idx_010])

                # Protection classification
                protected_I = max_delta_I < 1e-12
                protected_II = max_delta_II < 1e-12

                qdata = {
                    'q': q,
                    'theta_values': [float(t) for t in theta_vals],
                    'qcmi_values_I': [float(v) for v in qcmi_I_vals],
                    'qcmi_values_II': [float(v) for v in qcmi_II_vals],
                    'delta_qcmi_I': [float(v) for v in delta_I],
                    'delta_qcmi_II': [float(v) for v in delta_II],
                    'delta_at_theta_010_I': float(delta_I[idx_010]),
                    'delta_at_theta_010_II': float(delta_II[idx_010]),
                    'M4_alpha_I': float(alpha_I),
                    'M4_beta_I': float(beta_I),
                    'M4_gamma_I': float(gamma_I),
                    'M4_alpha_II': float(alpha_II),
                    'M4_beta_II': float(beta_II),
                    'M4_gamma_II': float(gamma_II),
                    'protected_I': protected_I,
                    'protected_II': protected_II,
                }

                results[key_I]['by_qubit'][str(q)] = qdata
                results[key_II]['by_qubit'][str(q)] = qdata

                status_I = "PROTECTED" if protected_I else "ACTIVE"
                status_II = "PROTECTED" if protected_II else "ACTIVE"
                print(f"I:{status_I} II:{status_II}")

    return results

def compute_magic_correlation_length(n_vals, k_vals, theta_vals):
    """Verify magic correlation length under Partition I with T-gate at qubit 0."""
    results = {}

    for n in n_vals:
        print(f"\n{'='*60}")
        print(f"Magic correlation: n={n}")
        print(f"{'='*60}")

        psi_base = build_cluster_ring_state(n)

        for k in k_vals:
            if k >= n or k == 0:
                continue
            if k > n // 2:
                continue  # Symmetry on ring

            key = f"n{n}_k{k}_T_gate_q0"
            pI = partition_I(n, k)
            pII = partition_II(n, k)

            baseline_I, *_ = compute_qcmi(psi_base, n, pI)
            baseline_II, *_ = compute_qcmi(psi_base, n, pII)

            qcmi_I_vals = []
            qcmi_II_vals = []

            for theta in theta_vals:
                psi_pert, overlap, perp_norm = apply_T_superposition(psi_base.copy(), n, 0, theta)
                qcmi_I, *_ = compute_qcmi(psi_pert, n, pI)
                qcmi_II, *_ = compute_qcmi(psi_pert, n, pII)
                qcmi_I_vals.append(float(qcmi_I))
                qcmi_II_vals.append(float(qcmi_II))

            delta_I = [v - baseline_I for v in qcmi_I_vals]
            delta_II = [v - baseline_II for v in qcmi_II_vals]

            # M4 fit
            alpha_I, beta_I, gamma_I, _ = fit_M4(theta_vals, delta_I)
            alpha_II, beta_II, gamma_II, _ = fit_M4(theta_vals, delta_II)

            # Max delta at theta=0.10
            idx_010 = min(range(len(theta_vals)), key=lambda i: abs(theta_vals[i] - 0.10))
            max_delta_I = abs(delta_I[idx_010])
            max_delta_II = abs(delta_II[idx_010])

            results[key] = {
                'n': n, 'k': k, 'q': 0,
                'overlap_magnitude': float(abs(overlap)),
                'baseline_I': float(baseline_I),
                'baseline_II': float(baseline_II),
                'theta_values': [float(t) for t in theta_vals],
                'qcmi_I': [float(v) for v in qcmi_I_vals],
                'qcmi_II': [float(v) for v in qcmi_II_vals],
                'delta_I': [float(v) for v in delta_I],
                'delta_II': [float(v) for v in delta_II],
                'max_delta_I_theta_010': float(delta_I[idx_010]),
                'max_delta_II_theta_010': float(delta_II[idx_010]),
                'M4_alpha_I': float(alpha_I),
                'M4_beta_I': float(beta_I),
                'M4_gamma_I': float(gamma_I),
                'M4_alpha_II': float(alpha_II),
                'M4_beta_II': float(beta_II),
                'M4_gamma_II': float(gamma_II),
                'is_zero_I': max_delta_I < 1e-12,
                'is_zero_II': max_delta_II < 1e-12
            }

            status = "ZERO" if max_delta_I < 1e-12 else f"NONZERO({max_delta_I:.2e})"
            print(f"  k={k}: delta_I={max_delta_I:.2e} {status}")

    return results

def compute_ln2_AICc(n_vals, theta_vals):
    """Compute AICc model selection (M3 vs M4) for T-gate at q=0, k=1 under Partition I."""
    results = {}

    for n in n_vals:
        print(f"\n{'='*60}")
        print(f"ln^2 AICc: n={n}")
        print(f"{'='*60}")

        psi_base = build_cluster_ring_state(n)
        pI = partition_I(n, 1)
        pII = partition_II(n, 1)

        baseline_I, *_ = compute_qcmi(psi_base, n, pI)
        baseline_II, *_ = compute_qcmi(psi_base, n, pII)

        qcmi_I_vals = []
        qcmi_II_vals = []

        for theta in theta_vals:
            psi_pert, _, _ = apply_T_superposition(psi_base.copy(), n, 0, theta)
            qcmi_I, *_ = compute_qcmi(psi_pert, n, pI)
            qcmi_II, *_ = compute_qcmi(psi_pert, n, pII)
            qcmi_I_vals.append(float(qcmi_I))
            qcmi_II_vals.append(float(qcmi_II))

        delta_I = np.array([v - baseline_I for v in qcmi_I_vals])
        delta_II = np.array([v - baseline_II for v in qcmi_II_vals])

        # M3 and M4 fits
        alpha3_I, beta3_I, rss3_I = fit_M3(theta_vals, delta_I)
        alpha4_I, beta4_I, gamma4_I, rss4_I = fit_M4(theta_vals, delta_I)

        alpha3_II, beta3_II, rss3_II = fit_M3(theta_vals, delta_II)
        alpha4_II, beta4_II, gamma4_II, rss4_II = fit_M4(theta_vals, delta_II)

        n_pts = len(theta_vals)
        aicc3_I = compute_AICc(rss3_I, n_pts, 2)
        aicc4_I = compute_AICc(rss4_I, n_pts, 3)
        aicc3_II = compute_AICc(rss3_II, n_pts, 2)
        aicc4_II = compute_AICc(rss4_II, n_pts, 3)

        delta_aicc_I = aicc3_I - aicc4_I  # Positive = M4 preferred
        delta_aicc_II = aicc3_II - aicc4_II

        results[f"n{n}"] = {
            'n': n,
            'baseline_I': float(baseline_I),
            'baseline_II': float(baseline_II),
            'theta_values': [float(t) for t in theta_vals],
            'delta_qcmi_I': [float(v) for v in delta_I],
            'delta_qcmi_II': [float(v) for v in delta_II],
            'M3_I': {
                'alpha': float(alpha3_I), 'beta': float(beta3_I),
                'RSS': float(rss3_I), 'AICc': float(aicc3_I)
            },
            'M4_I': {
                'alpha': float(alpha4_I), 'beta': float(beta4_I), 'gamma': float(gamma4_I),
                'RSS': float(rss4_I), 'AICc': float(aicc4_I)
            },
            'M3_II': {
                'alpha': float(alpha3_II), 'beta': float(beta3_II),
                'RSS': float(rss3_II), 'AICc': float(aicc3_II)
            },
            'M4_II': {
                'alpha': float(alpha4_II), 'beta': float(beta4_II), 'gamma': float(gamma4_II),
                'RSS': float(rss4_II), 'AICc': float(aicc4_II)
            },
            'delta_AICc_I': float(delta_aicc_I),
            'delta_AICc_II': float(delta_aicc_II),
            'M4_preferred_I': delta_aicc_I > 2,
            'M4_preferred_II': delta_aicc_II > 2,
        }

        print(f"  k=1, T-gate@q=0:")
        print(f"    M3_I:  alpha={alpha3_I:.6f}, beta={beta3_I:.6f}, AICc={aicc3_I:.2f}")
        print(f"    M4_I:  alpha={alpha4_I:.6f}, beta={beta4_I:.6f}, gamma={gamma4_I:.6f}, AICc={aicc4_I:.2f}")
        print(f"    ΔAICc_I = {delta_aicc_I:.2f} -> M4 {'PREFERRED' if delta_aicc_I > 2 else 'NOT PREFERRED'}")

    return results

# ============================================================
# Global T-gate test
# ============================================================

def compute_global_T_test(n_vals, k_vals, theta_val=0.10):
    """Test global T-gate injection: T on ALL qubits, check QCMI at k>=2."""
    results = {}

    for n in n_vals:
        psi_base = build_cluster_ring_state(n)

        # Apply T on all qubits
        T = np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]], dtype=complex)
        dim = 2**n
        T_all = np.eye(dim, dtype=complex)
        for q in range(n):
            Tq = np.eye(1, dtype=complex)
            for i in range(n):
                Tq = np.kron(Tq, T if i == q else np.eye(2))
            T_all = T_all @ Tq

        # Normalize for superposition
        Tpsi = T_all @ psi_base
        overlap = np.vdot(psi_base, Tpsi)
        perp_unnorm = Tpsi - overlap * psi_base
        perp_norm = np.sqrt(np.vdot(perp_unnorm, perp_unnorm).real)

        if perp_norm > 1e-14:
            perp = perp_unnorm / perp_norm
            psi_pert = np.cos(theta_val) * psi_base + np.sin(theta_val) * perp
        else:
            psi_pert = psi_base.copy()

        for k in k_vals:
            if k >= n or k <= 1:
                continue

            pI = partition_I(n, k)
            pII = partition_II(n, k)

            baseline_I, *_ = compute_qcmi(psi_base, n, pI)
            baseline_II, *_ = compute_qcmi(psi_base, n, pII)

            qcmi_I, *_ = compute_qcmi(psi_pert, n, pI)
            qcmi_II, *_ = compute_qcmi(psi_pert, n, pII)

            delta_I = qcmi_I - baseline_I
            delta_II = qcmi_II - baseline_II

            key = f"n{n}_k{k}_global_T"
            results[key] = {
                'n': n, 'k': k,
                'theta': theta_val,
                'baseline_I': float(baseline_I),
                'baseline_II': float(baseline_II),
                'qcmi_I': float(qcmi_I),
                'qcmi_II': float(qcmi_II),
                'delta_I': float(delta_I),
                'delta_II': float(delta_II),
                'is_zero_I': abs(delta_I) < 1e-12,
                'is_zero_II': abs(delta_II) < 1e-12
            }
            print(f"  Global T: n={n}, k={k}: delta_I={delta_I:.2e} zero={abs(delta_I)<1e-12}")

    return results

# ============================================================
# Main execution
# ============================================================

if __name__ == '__main__':
    # Theta values for detailed scan
    theta_fine = [0.005, 0.01, 0.02, 0.03, 0.05, 0.08, 0.10, 0.15, 0.20, 0.25, 0.30]
    theta_small = [0.005, 0.01, 0.02, 0.03, 0.05, 0.08, 0.10]  # For protection classification
    theta_coarse = [0.005, 0.01, 0.03, 0.05, 0.08, 0.10, 0.15, 0.20, 0.30]  # For AICc

    all_results = {
        'metadata': {
            'title': 'LP47 fp_fix: Unified Partition Convention',
            'author': 'B博士',
            'date': '2026-06-12',
            'partition_I': 'A={0}, C={k}, B=[n]\\{0,k} (big B, A博士 convention)',
            'partition_II': 'A={0}, B={k}, C={k+1 mod n} (small B, B博士 original)',
            'perturbations': ['Hmix (Hadamard mixing)', 'T-gate superposition'],
            'system': 'Cluster rings C_n with periodic boundary',
            'unit': 'nats (natural log)',
        },
    }

    # Fix 3: Protection horizon under Partition I+II
    print("=" * 60)
    print("FIX 3: Protection Horizon (n=6,7,8, Hmix at each q, k=1,2,3)")
    print("=" * 60)
    n_protection = [6, 7, 8]
    k_protection = [1, 2, 3]
    protection_results = compute_protection_horizon(n_protection, k_protection, theta_small)
    all_results['fix3_protection_horizon'] = protection_results

    # Fix 4: Magic correlation length (T-gate at q=0, Partition I)
    print("\n" + "=" * 60)
    print("FIX 4: Magic Correlation Length (n=6,7, T-gate@q=0, Partition I)")
    print("=" * 60)
    n_magic = [6, 7]
    k_magic = [1, 2, 3]
    magic_results = compute_magic_correlation_length(n_magic, k_magic, theta_fine)
    all_results['fix4_magic_correlation_length'] = magic_results

    # Fix 4b: Global T-gate test
    print("\n" + "=" * 60)
    print("FIX 4b: Global T-gate injection (n=6,7, T on ALL qubits)")
    print("=" * 60)
    global_T_results = compute_global_T_test(n_magic, k_magic, theta_val=0.10)
    all_results['fix4b_global_T_test'] = global_T_results

    # Fix 5: ln^2 AICc model selection
    print("\n" + "=" * 60)
    print("FIX 5: ln^2 AICc Model Selection (n=5,6,7, T-gate@q=0, k=1)")
    print("=" * 60)
    n_aicc = [5, 6, 7]
    aicc_results = compute_ln2_AICc(n_aicc, theta_coarse)
    all_results['fix5_ln2_AICc'] = aicc_results

    # Custom JSON encoder for numpy types
    class NumpyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, (np.bool_,)):
                return bool(obj)
            if isinstance(obj, (np.integer,)):
                return int(obj)
            if isinstance(obj, (np.floating,)):
                return float(obj)
            if isinstance(obj, np.ndarray):
                return obj.tolist()
            return super().default(obj)

    # Save raw computation results
    output_path = r'D:\Claude\ai-reservations\LP47-因果环信息局域化\current\B\fp_fix_raw.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False, cls=NumpyEncoder)

    print(f"\n\nRaw results saved to: {output_path}")
    print("Done. Now post-process to create fp_fix.json")

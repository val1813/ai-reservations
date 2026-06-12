"""
LP47 R3: Numerical computation of QCMI(theta) for n=5,6,7 rings.
Exact diagonalization with non-Clifford perturbation (Rx rotation + H-mixing).
Two Clifford state families: GHZ-type ring and cluster-type ring.
"""
import numpy as np
from scipy.linalg import expm
import json
import warnings
warnings.filterwarnings('ignore')

# Pauli matrices
I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
H_gate = np.array([[1, 1], [1, -1]], dtype=complex) / np.sqrt(2)
S_gate = np.array([[1, 0], [0, 1j]], dtype=complex)
T_gate = np.array([[1, 0], [0, np.exp(1j * np.pi / 4)]], dtype=complex)
CZ_mat = np.eye(4, dtype=complex)
CZ_mat[3, 3] = -1

def kron(*mats):
    result = mats[0]
    for m in mats[1:]:
        result = np.kron(result, m)
    return result

def apply_gate(state, gate, target, n_qubits):
    ops = [I2] * n_qubits
    ops[target] = gate
    U = kron(*ops)
    return U @ state

def apply_cz_ring(state, q1, q2, n):
    """Apply CZ between q1 and q2 on ring."""
    dim = 2**n
    U = np.eye(dim, dtype=complex)
    for i in range(dim):
        bits = format(i, f'0{n}b')
        if bits[n-1-q1] == '1' and bits[n-1-q2] == '1':
            U[i, i] = -1
    return U @ state

def ghz_ring_state(n):
    """GHZ-type state: (|00...0> + |11...1>)/sqrt(2)."""
    psi = np.zeros(2**n, dtype=complex)
    psi[0] = 1.0
    psi[-1] = 1.0
    return psi / np.sqrt(2)

def cluster_ring_state(n):
    """Cluster-type state on ring: H on all then CZ on ring edges."""
    psi = np.zeros(2**n, dtype=complex)
    psi[0] = 1.0
    for i in range(n):
        psi = apply_gate(psi, H_gate, i, n)
    for i in range(n):
        psi = apply_cz_ring(psi, i, (i+1) % n, n)
    return psi

def rx_perturbed_state(base_state, theta, n, perturb_qubit=0):
    """R_x(pi*theta/2) perturbation. Creates genuine superposition.
    For theta->0: identity. For theta>0: breaks Z-stabilizer structure."""
    angle = np.pi * theta / 2
    Rx = np.array([[np.cos(angle/2), -1j*np.sin(angle/2)],
                   [-1j*np.sin(angle/2), np.cos(angle/2)]], dtype=complex)
    return apply_gate(base_state, Rx, perturb_qubit, n)

def hmix_perturbed_state(base_state, theta, n, perturb_qubit=0):
    """H-mixing perturbation: cos(th*pi/2)|C> + sin(th*pi/2)H_0|C>."""
    cos_a = np.cos(np.pi * theta / 2)
    sin_a = np.sin(np.pi * theta / 2)
    psi_h = apply_gate(base_state, H_gate, perturb_qubit, n)
    psi_new = cos_a * base_state + sin_a * psi_h
    return psi_new / np.linalg.norm(psi_new)

def partial_trace(psi, keep_qubits, n):
    """Reduced density matrix by tracing out non-kept qubits."""
    rho = np.outer(psi, psi.conj())
    keep = sorted(keep_qubits)
    trace_out = sorted(set(range(n)) - set(keep))

    if not keep:
        return np.array([[np.trace(rho)]], dtype=complex)
    if not trace_out:
        return rho.copy()

    keep_dim = 2 ** len(keep)
    rho_red = np.zeros((keep_dim, keep_dim), dtype=complex)

    for i in range(2**n):
        bits_i = format(i, f'0{n}b')
        for j in range(2**n):
            bits_j = format(j, f'0{n}b')
            match = True
            for q in trace_out:
                if bits_i[n-1-q] != bits_j[n-1-q]:
                    match = False
                    break
            if not match:
                continue
            idx_i_bits = ''.join(bits_i[n-1-q] for q in keep)
            idx_j_bits = ''.join(bits_j[n-1-q] for q in keep)
            idx_i = int(idx_i_bits, 2)
            idx_j = int(idx_j_bits, 2)
            rho_red[idx_i, idx_j] += rho[i, j]

    return rho_red

def von_neumann_entropy(rho):
    eigenvals = np.linalg.eigvalsh(rho)
    eigenvals = eigenvals[eigenvals > 1e-15]
    if len(eigenvals) == 0:
        return 0.0
    return -np.sum(eigenvals * np.log(eigenvals))

def qcmi_from_psi(psi, A, B, C, n):
    """I(A:B|C) = S(AC) + S(BC) - S(C) - S(ABC)."""
    AC = sorted(set(A) | set(C))
    BC = sorted(set(B) | set(C))
    ABC = sorted(set(A) | set(B) | set(C))

    S_AC = von_neumann_entropy(partial_trace(psi, AC, n))
    S_BC = von_neumann_entropy(partial_trace(psi, BC, n))
    S_C = von_neumann_entropy(partial_trace(psi, C, n))
    S_ABC = von_neumann_entropy(partial_trace(psi, ABC, n))

    return S_AC + S_BC - S_C - S_ABC

def ring_qcmi(psi, n, k):
    """QCMI on ring: A={0}, B={k}, C={1,...,k-1}."""
    A = [0]
    B = [k % n]
    C = list(range(1, k)) if k > 1 else []
    return qcmi_from_psi(psi, A, B, C, n)

def ring_qcmi_sum(psi, n):
    """Sum of adjacent QCMI: Sigma_j I(j:j+1|rest)."""
    total = 0.0
    for j in range(n):
        A = [j]
        B = [(j + 1) % n]
        C = [q for q in range(n) if q != j and q != (j + 1) % n]
        total += qcmi_from_psi(psi, A, B, C, n)
    return total

def fit_theta_squared_log(y_values, thetas):
    """Fit y = alpha * theta^2 * ln(1/theta) + beta * theta^2."""
    X = np.column_stack([
        thetas**2 * np.log(1.0 / thetas),
        thetas**2
    ])
    y = np.array(y_values)
    coeffs, residuals, rank, sv = np.linalg.lstsq(X, y, rcond=None)
    alpha, beta = coeffs
    y_pred = X @ coeffs
    ss_res = np.sum((y - y_pred)**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0
    return float(alpha), float(beta), float(r_squared)

def compute_rank_increment(psi_base, psi_pert, subsystems, n):
    results = {}
    for name, keep in subsystems.items():
        if not keep:
            results[name] = {'rank_base': 1, 'rank_pert': 1, 'delta_r': 0, 'dim': 1}
            continue
        rho_base = partial_trace(psi_base, keep, n)
        rho_pert = partial_trace(psi_pert, keep, n)
        evals_base = np.linalg.eigvalsh(rho_base)
        evals_pert = np.linalg.eigvalsh(rho_pert)
        rank_base = int(np.sum(evals_base > 1e-12))
        rank_pert = int(np.sum(evals_pert > 1e-12))
        results[name] = {
            'rank_base': rank_base,
            'rank_pert': rank_pert,
            'delta_r': rank_pert - rank_base,
            'dim': 2**len(keep)
        }
    return results

def compute_delta_qcmi(psi_base, n, k, thetas, perturb_fn):
    """Compute delta_QCMI = QCMI(theta) - QCMI(0) and fit."""
    qcmi_0 = ring_qcmi(psi_base, n, k)
    qcmi_vals = []
    delta_vals = []
    for theta in thetas:
        psi_t = perturb_fn(psi_base, theta, n)
        psi_t = psi_t / np.linalg.norm(psi_t)
        qv = max(ring_qcmi(psi_t, n, k), 0.0)
        qcmi_vals.append(qv)
        delta_vals.append(qv - qcmi_0)

    alpha, beta, r_sq = fit_theta_squared_log(delta_vals, thetas)
    return {
        'qcmi_baseline': float(qcmi_0),
        'qcmi_values': qcmi_vals,
        'delta_qcmi': delta_vals,
        'alpha': alpha, 'beta': beta, 'r_sq_theta2ln': r_sq
    }

# ============================================================
# MAIN
# ============================================================
def main():
    print("=" * 70)
    print("LP47 R3: QCMI(theta) Numerical Computation")
    print("n=5,6,7 ring, GHZ-type and cluster-type Clifford states")
    print("Perturbations: Rx-rotation, H-mixing")
    print("=" * 70)

    thetas_fine = np.array([0.005, 0.01, 0.015, 0.02, 0.025, 0.03, 0.04,
                            0.05, 0.06, 0.07, 0.08, 0.09, 0.10,
                            0.12, 0.14, 0.16, 0.18, 0.20])

    thetas_coarse = np.array([0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07,
                              0.08, 0.09, 0.10, 0.12, 0.14, 0.16, 0.18, 0.20])

    results = {}
    perturb_fns = [
        (rx_perturbed_state, "Rx"),
        (hmix_perturbed_state, "H-mix")
    ]

    for n in [5, 6]:
        print(f"\n{'='*70}")
        print(f"n={n} ring (Hilbert dim={2**n})")
        print(f"{'='*70}")

        psi_ghz = ghz_ring_state(n)
        psi_cluster = cluster_ring_state(n)
        k_max = n // 2

        for state_name, psi_base in [("GHZ-ring", psi_ghz), ("cluster-ring", psi_cluster)]:
            for perturb_fn, perturb_name in perturb_fns:
                print(f"\n  [{state_name} + {perturb_name}]")

                for k in range(1, k_max + 1):
                    th = thetas_fine if n <= 6 else thetas_coarse
                    res = compute_delta_qcmi(psi_base, n, k, th, perturb_fn)

                    key = f"n{n}_{state_name}_{perturb_name}_k{k}"
                    results[key] = {'n': n, 'state': state_name,
                                   'perturbation': perturb_name, 'k': k, **res}

                    has_scaling = (res['r_sq_theta2ln'] > 0.85 and abs(res['alpha']) > 1e-4)
                    status = "CONFIRMED" if has_scaling else "ABSENT"
                    print(f"    k={k}: baseline={res['qcmi_baseline']:.4f} "
                          f"alpha={res['alpha']:.4f} R^2={res['r_sq_theta2ln']:.4f} [{status}]")
                    if has_scaling:
                        # Find indices close to 0.05, 0.10, 0.20
                        i5 = np.argmin(np.abs(th - 0.05))
                        i10 = np.argmin(np.abs(th - 0.10))
                        i20 = np.argmin(np.abs(th - 0.20))
                        print(f"      delta(th=0.05)={res['delta_qcmi'][i5]:.6f} "
                              f"th=0.10: {res['delta_qcmi'][i10]:.6f} "
                              f"th=0.20: {res['delta_qcmi'][i20]:.6f}")

        # Rank analysis
        print(f"\n  --- Rank Increment (Rx, theta=0.1) ---")
        for state_name, psi_base in [("GHZ-ring", psi_ghz), ("cluster-ring", psi_cluster)]:
            psi_pert = rx_perturbed_state(psi_base, 0.1, n)
            psi_pert = psi_pert / np.linalg.norm(psi_pert)

            for k in range(1, k_max + 1):
                A = [0]; B = [k % n]
                C = list(range(1, k)) if k > 1 else []
                AC = sorted(set(A) | set(C)); BC = sorted(set(B) | set(C))
                ABC = sorted(set(A) | set(B) | set(C))
                subs = {'C': C if C else [], 'AC': AC, 'BC': BC, 'ABC': ABC}
                ri = compute_rank_increment(psi_base, psi_pert, subs, n)

                alpha_pred = 2 * (ri['AC']['delta_r'] + ri['BC']['delta_r'] - ri['C']['delta_r'])
                print(f"    {state_name} k={k}: dR(C)={ri['C']['delta_r']} "
                      f"dR(AC)={ri['AC']['delta_r']} dR(BC)={ri['BC']['delta_r']} "
                      f"=> alpha_pred={alpha_pred}")
                results[f"n{n}_{state_name}_k{k}_ranks"] = {
                    'n': n, 'state': state_name, 'k': k,
                    'rank_info': {kk: vv for kk, vv in ri.items()},
                    'alpha_predicted': alpha_pred
                }

        # Conservation law
        print(f"\n  --- Conservation Law Sigma_j I(j:j+1|rest) ---")
        for state_name, psi_base in [("GHZ-ring", psi_ghz), ("cluster-ring", psi_cluster)]:
            for perturb_fn, perturb_name in perturb_fns:
                qcmi_sum_0 = ring_qcmi_sum(psi_base, n)
                sum_deltas = []
                for theta in thetas_fine:
                    psi_t = perturb_fn(psi_base, theta, n)
                    psi_t = psi_t / np.linalg.norm(psi_t)
                    sum_deltas.append(ring_qcmi_sum(psi_t, n) - qcmi_sum_0)

                X_s = np.column_stack([thetas_fine**2 * np.log(1.0/thetas_fine)])
                const = np.linalg.lstsq(X_s, sum_deltas, rcond=None)[0][0]
                y_pred = X_s.flatten() * const
                ss_r = np.sum((np.array(sum_deltas) - y_pred)**2)
                ss_t = np.sum((np.array(sum_deltas) - np.mean(sum_deltas))**2)
                r_sq_s = 1 - ss_r/ss_t if ss_t > 0 else 0
                print(f"    {state_name} {perturb_name}: sum0={qcmi_sum_0:.4f} "
                      f"const={const:.4f} R^2={r_sq_s:.4f}")
                results[f"n{n}_{state_name}_{perturb_name}_sum"] = {
                    'n': n, 'state': state_name, 'perturbation': perturb_name,
                    'sum_baseline': float(qcmi_sum_0),
                    'delta_sum_values': sum_deltas,
                    'fit_const': float(const), 'r_squared': float(r_sq_s)
                }

    # n=7: key configs
    print(f"\n{'='*70}")
    print("n=7 ring (Hilbert dim=128, key configs)")
    print(f"{'='*70}")
    n = 7
    psi_ghz_7 = ghz_ring_state(n)
    psi_cluster_7 = cluster_ring_state(n)

    for state_name, psi_base in [("GHZ-ring", psi_ghz_7), ("cluster-ring", psi_cluster_7)]:
        for perturb_fn, perturb_name in perturb_fns:
            print(f"\n  [{state_name} + {perturb_name}]")
            for k in [1, 2, 3]:
                res = compute_delta_qcmi(psi_base, n, k, thetas_coarse, perturb_fn)
                key = f"n{n}_{state_name}_{perturb_name}_k{k}"
                results[key] = {'n': n, 'state': state_name,
                               'perturbation': perturb_name, 'k': k, **res}
                has_scaling = (res['r_sq_theta2ln'] > 0.85 and abs(res['alpha']) > 1e-4)
                status = "CONFIRMED" if has_scaling else "ABSENT"
                print(f"    k={k}: baseline={res['qcmi_baseline']:.4f} "
                      f"alpha={res['alpha']:.4f} R^2={res['r_sq_theta2ln']:.4f} [{status}]")

    # n=3,4: confirm alpha=0
    print(f"\n{'='*70}")
    print("n=3,4: INSPECTOR alpha=0 verification")
    print(f"{'='*70}")
    for n in [3, 4]:
        for state_name, psi_base in [("GHZ-ring", ghz_ring_state(n)),
                                      ("cluster-ring", cluster_ring_state(n))]:
            for k in range(1, n // 2 + 1):
                res = compute_delta_qcmi(psi_base, n, k, thetas_fine, rx_perturbed_state)
                key = f"n{n}_{state_name}_Rx_k{k}_verify"
                results[key] = {'n': n, 'state': state_name, 'k': k, **res}
                pred = "OK (alpha~0)" if abs(res['alpha']) < 0.01 else "SURPRISE"
                print(f"  n={n} {state_name} k={k}: alpha={res['alpha']:.6f} [{pred}]")

    # Save
    class NpEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, (np.floating,)): return float(obj)
            if isinstance(obj, np.integer): return int(obj)
            if isinstance(obj, np.ndarray): return obj.tolist()
            if isinstance(obj, complex): return [float(obj.real), float(obj.imag)]
            return super().default(obj)

    output_path = r"D:\Claude\ai-reservations\LP47-因果环信息局域化\current\A\numerical_results.json"
    with open(output_path, 'w') as f:
        json.dump(results, f, indent=2, cls=NpEncoder)
    print(f"\nSaved to {output_path}")
    return results

if __name__ == "__main__":
    main()

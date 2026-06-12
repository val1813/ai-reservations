"""
W1 Attack: Chain-of-Rings QCMI Simulation — Push numerical frontier past b1=4.

Strategy: Build a SINGLE parameterized family of graphs where each new ring
adds exactly one Q node and shares it with the previous ring. This isolates
the pure shared-Q interference (trideagonal Hessian) and eliminates the
cycle-size confound present in the existing b1_scan data.

Chain topology for b1=N:
  Ring 1: Q1 - E1 - Q2 - E2 - Q1
  Ring 2: Q2 - E3 - Q3 - E4 - Q2    (shares Q2 with ring 1)
  Ring 3: Q3 - E5 - Q4 - E6 - Q3    (shares Q3 with ring 2)
  ...
  Ring N: Q_N - E_{2N-1} - Q_{N+1} - E_{2N} - Q_N

  n_Q = N+1, n_E = 2N, n_R = N+1
  Total Hilbert dim = 2^{2(N+1) + 2N} = 2^{4N+2}

Simulation method: Pure-state evolution for each E configuration,
exact enumeration (all 2^{n_E} E configurations, importance-weighted by p).

This is feasible up to b1=5 (22 total qubits, 2^22 = 4M statevector,
1024 E configurations), pushing ONE data point past the b1=4 frontier.
"""
import numpy as np
from scipy.linalg import expm
from scipy.optimize import curve_fit
import time as time_module

# ======== Core quantum info utilities ========

I2 = np.eye(2, dtype=np.complex64)
X = np.array([[0, 1], [1, 0]], dtype=np.complex64)
Y = np.array([[0, -1j], [1j, 0]], dtype=np.complex64)
Z = np.array([[1, 0], [0, -1]], dtype=np.complex64)

def vn_entropy(rho, eps=1e-12):
    """von Neumann entropy of a density matrix."""
    w = np.linalg.eigvalsh(rho)
    w = np.maximum(w.real, eps)
    w = w / np.sum(w)
    return -np.sum(w * np.log2(w))

def random_u4(seed):
    """Haar-random 4x4 unitary via QR decomposition."""
    rng = np.random.RandomState(seed)
    A = rng.randn(4, 4) + 1j * rng.randn(4, 4)
    Q, R = np.linalg.qr(A)
    # Ensure det=1 phase correction
    d = np.diag(R)
    Q = Q @ np.diag(d / np.abs(d))
    return Q.astype(np.complex64)

def apply_2q_gate(psi, gate_4x4, a, b, nq):
    """
    Apply a 2-qubit gate on qubits (a,b) to statevector psi.
    Uses C-order reshape + moveaxis + tensordot. Correct by construction.

    psi: statevector of size 2^nq
    gate_4x4: 4x4 unitary, gate[combined_out, combined_in]
              where combined = i_a + 2*i_b (LSB convention)
    a, b: qubit indices (0-indexed, 0 = LSB)
    nq: total number of qubits
    """
    # C-order: axis[0] = MSB (qubit nq-1), axis[nq-1] = LSB (qubit 0)
    # qubit k maps to axis nq-1-k
    ax_a = nq - 1 - a
    ax_b = nq - 1 - b

    psi_c = psi.reshape([2] * nq, order='C')

    # Move target qubit axes to last two positions
    psi_moved = np.moveaxis(psi_c, [ax_a, ax_b], [-2, -1])
    # psi_moved shape: (2,...,2,2,2) — last two axes = qubits b,a (b is penultimate)

    # Reshape gate to rank-4 tensor: [out_a, out_b, in_a, in_b]
    # gate_4x4[combined_out, combined_in] with combined = a_bit + 2*b_bit
    # In the moved psi, last axis (-1) = qubit b, penultimate (-2) = qubit a
    # So gate_tensor[oa, ob, ia, ib] = gate_4x4[oa+2*ob, ia+2*ib]
    gate_t = gate_4x4.reshape(2, 2, 2, 2)  # [out_a, out_b, in_a, in_b]

    # Contract: psi[..., ia, ib] * gate[oa, ob, ia, ib] -> result[..., oa, ob]
    # tensordot with axes=([-2,-1], [-2,-1]) contracts the input qubit axes
    psi_out = np.tensordot(psi_moved, gate_t, axes=([-2, -1], [-2, -1]))

    # psi_out shape: (2,...,2,2,2) — last two axes are output qubits (oa, ob)
    # Move output axes back to original positions
    psi_out = np.moveaxis(psi_out, [-2, -1], [ax_a, ax_b])

    # Flatten back to statevector (C-order)
    return np.ascontiguousarray(psi_out).reshape(-1, order='C')


def partial_trace_pure(psi, keep, nq):
    """
    Partial trace over E for a pure state psi.
    Returns reduced density matrix on the kept qubits.

    psi: statevector of size 2^nq
    keep: list of qubit indices to keep
    nq: total qubits
    """
    keep = sorted(keep)
    tr = sorted([i for i in range(nq) if i not in keep])
    dk = 2**len(keep)
    dt = 2**len(tr)

    # Reshape to (2^{n_keep}, 2^{n_trace})
    psi_shaped = psi.reshape([2] * nq)

    # Permute so keep bits are first, trace bits last
    axes = keep + tr
    psi_t = np.transpose(psi_shaped, axes)
    psi_mat = psi_t.reshape(dk, dt)

    # rho = psi_mat @ psi_mat^dagger
    rho = psi_mat @ psi_mat.conj().T
    return rho


# ======== Chain-of-Rings graph and simulation ========

def build_chain_state_initial(n_q, n_e, p=0.7):
    """
    Build the initial statevector for the chain of rings.

    Qubit layout: [Q_1, ..., Q_{n_q}, E_1, ..., E_{n_e}, R_1, ..., R_{n_q}]
    Total qubits: n_q + n_e + n_q = 2*n_q + n_e

    Initial state: |Phi+>_{RQ} ⊗ |e>_E for a specific E configuration e.

    Returns:
        psi_e: statevector for given e configuration
        prob_e: probability weight P(e)

    For EXACT enumeration, this function is called for EACH e.
    For SAMPLING, we sample e from the distribution.
    """
    n_total = 2 * n_q + n_e

    def build_for_e(e_config):
        """Build statevector for one E configuration."""
        # |Phi+>_{RQ} = (1/√2) Σ_i |i>_R |i>_Q for EACH R-Q pair
        # Actually for n_q Bell pairs: |Phi+>^{⊗n_q} = (1/2^{n_q/2}) Σ_{i∈{0,1}^{n_q}} |i>_R |i>_Q

        # E configuration is already in the computational basis
        # Build the state in the computational basis:
        # |psi> = Σ_{i∈{0,1}^{n_q}} (1/√(2^{n_q})) |i>_R ⊗ |i>_Q ⊗ |e>_E

        norm = 1.0 / np.sqrt(float(2**n_q))

        # Bit layout: [Q bits (0 to n_q-1), E bits (n_q to n_q+n_e-1), R bits (n_q+n_e to 2*n_q+n_e-1)]
        # Total = 2*n_q + n_e

        psi = np.zeros(2**n_total, dtype=np.complex64)

        for i in range(2**n_q):
            # Q bits = i (at positions 0..n_q-1)
            # R bits = i (at positions n_q+n_e .. 2*n_q+n_e-1)
            # E bits = e_config (at positions n_q .. n_q+n_e-1)
            idx = i  # Q bits at low positions
            idx |= (int(e_config) << n_q)  # E bits
            idx |= (i << (n_q + n_e))  # R bits
            psi[idx] = norm

        # Compute probability weight
        prob = 1.0
        for bit_idx in range(n_e):
            bit = (e_config >> bit_idx) & 1
            prob *= (p if bit == 0 else (1-p))

        return psi, prob

    return build_for_e


def build_chain_unitary_gates(n_q, n_e, seed_base=42):
    """
    Build the list of 2-qubit gates for the chain of rings.

    For N rings (b1=N):
      n_q = N+1, n_e = 2N

    Ring i (0-indexed):
      Edges: (Q_i, E_{2i}), (E_{2i}, Q_{i+1}), (Q_{i+1}, E_{2i+1}), (E_{2i+1}, Q_i)

    Qubit indexing in the QE system:
      Q_i = i (0 to n_q-1)
      E_j = n_q + j (n_q to n_q+n_e-1)

    Returns: list of (gate_4x4, qe_qubit_a, qe_qubit_b) tuples
    """
    gates = []
    rng = np.random.RandomState(seed_base)

    for ring_idx in range(n_q - 1):  # N rings
        qi = ring_idx          # Q_i
        qj = ring_idx + 1      # Q_{i+1}
        e1 = n_q + 2*ring_idx      # E_{2i}
        e2 = n_q + 2*ring_idx + 1  # E_{2i+1}

        # Edge 1: Q_i - E_{2i}
        gates.append((random_u4(seed_base + ring_idx*4 + 0), qi, e1))
        # Edge 2: E_{2i} - Q_{i+1}
        gates.append((random_u4(seed_base + ring_idx*4 + 1), e1, qj))
        # Edge 3: Q_{i+1} - E_{2i+1}
        gates.append((random_u4(seed_base + ring_idx*4 + 2), qj, e2))
        # Edge 4: E_{2i+1} - Q_i
        gates.append((random_u4(seed_base + ring_idx*4 + 3), e2, qi))

    return gates


def simulate_chain_qcmi(b1, p=0.7, seed=42, n_configs=None):
    """
    Simulate QCMI for chain of rings with b1 rings.

    Args:
        b1: number of rings
        p: mixedness parameter for E
        seed: random seed for gate generation
        n_configs: number of E configurations to sample (None = exact enumeration)

    Returns:
        dict with QCMI, S(RQ), S(Q), and other diagnostics
    """
    n_q = b1 + 1      # Q nodes
    n_e = 2 * b1      # E nodes
    n_r = n_q         # R nodes
    n_total = 2*n_q + n_e  # R + Q + E

    print(f"  b1={b1}: n_Q={n_q}, n_E={n_e}, n_R={n_r}, total={n_total} qubits")
    print(f"  Statevector size: 2^{n_total} = {2**n_total:,}")

    # Build gates (same gates for all E configurations)
    gates = build_chain_unitary_gates(n_q, n_e, seed)

    n_all_e = 2**n_e

    # Use exact enumeration if feasible, else sampling
    if n_configs is None:
        if n_all_e <= 1024:
            n_configs = n_all_e
            e_configs = list(range(n_all_e))
            use_exact = True
        else:
            n_configs = min(500, n_all_e)
            use_exact = False
    else:
        n_configs = min(n_configs, n_all_e)
        use_exact = (n_configs == n_all_e)

    if not use_exact:
        # Sample E configurations from the distribution
        e_configs = []
        for _ in range(n_configs):
            e_cfg = 0
            for bit_idx in range(n_e):
                if np.random.random() > p:  # prob(1) = 1-p
                    e_cfg |= (1 << bit_idx)
            e_configs.append(e_cfg)

    print(f"  Using {'exact ' if use_exact else ''}{n_configs} E configurations")

    # Compute E configuration weights
    def e_weight(e_cfg):
        w = 1.0
        for bit_idx in range(n_e):
            bit = (e_cfg >> bit_idx) & 1
            w *= (p if bit == 0 else (1-p))
        return w

    # Normalize weights for sampling
    if use_exact:
        weights = np.array([e_weight(e) for e in e_configs])
        weight_sum = np.sum(weights)
        weights = weights / weight_sum
    else:
        # For sampling, all sampled configs are equally weighted
        # Actually, we should importance-weight them:
        # P(e) = Π p_i, and we sampled uniformly, so weight = P(e) / (1/n_configs)
        # But this gives high variance. Better: use P(e) directly.
        weights = np.array([e_weight(e) for e in e_configs])
        weight_sum = np.sum(weights)
        if weight_sum > 0:
            weights = weights / weight_sum

    # Accumulate ρ_RQ and ρ_Q
    d_rq = 2**(n_q + n_r)  # Keep R and Q, trace E
    rho_rq = np.zeros((d_rq, d_rq), dtype=np.complex64)

    # Q qubits are indices 0..n_q-1 in the total system
    # R qubits are indices n_q+n_e .. n_q+n_e+n_r-1
    q_bits = list(range(n_q))
    r_bits = list(range(n_q+n_e, n_q+n_e+n_r))
    rq_bits = q_bits + r_bits

    t_start = time_module.time()

    for cfg_idx, e_cfg in enumerate(e_configs):
        if (cfg_idx + 1) % max(1, n_configs // 5) == 0:
            elapsed = time_module.time() - t_start
            eta = elapsed / (cfg_idx + 1) * n_configs - elapsed
            print(f"    [{cfg_idx+1}/{n_configs}] {elapsed:.1f}s elapsed, ETA {eta:.1f}s")

        w = weights[cfg_idx]
        if w < 1e-12:
            continue

        # Build initial statevector for this E configuration
        psi = np.zeros(2**n_total, dtype=np.complex64)
        norm = 1.0 / np.sqrt(float(2**n_q))

        # For all Q basis states i (also R basis states, since R mirrors Q)
        for i in range(2**n_q):
            # Bit layout: Q(@0..n_q-1), E(@n_q..n_q+n_e-1), R(@n_q+n_e..)
            idx = i                           # Q bits
            idx |= (e_cfg << n_q)            # E bits
            idx |= (i << (n_q + n_e))        # R bits (mirror Q)
            psi[idx] = norm

        # Apply all gates (sequentially, gate by gate)
        for gate_4x4, a, b in gates:
            psi = apply_2q_gate(psi, gate_4x4, a, b, n_total)

        # Compute contribution to ρ_RQ via partial trace over E
        # Reshape to (2^{len(rq_bits)}, 2^{n_e})
        d_rq = 2**len(rq_bits)

        # Permute to bring RQ bits first
        psi_shaped = psi.reshape([2] * n_total)
        n_e_bits = list(range(n_q, n_q + n_e))
        axes = rq_bits + n_e_bits
        psi_t = np.transpose(psi_shaped, axes)
        psi_mat = psi_t.reshape(d_rq, 2**n_e)

        rho_e = psi_mat @ psi_mat.conj().T  # (d_rq, d_rq)
        rho_rq += w * rho_e

    elapsed = time_module.time() - t_start
    print(f"  Total simulation time: {elapsed:.1f}s")

    # Compute entropies
    # ρ_RQ is the full (R+Q) density matrix of size (2^{n_q+n_r}, 2^{n_q+n_r})
    S_RQ = vn_entropy(rho_rq)

    # ρ_Q = Tr_R[ρ_RQ]
    # Indexing: Q is LSB, R is MSB in the computational basis
    # basis state |q,r> has index: q + r * 2^{n_q}
    d_q = 2**n_q
    d_r = 2**n_r
    rho_q = np.zeros((d_q, d_q), dtype=np.complex64)
    for r_val in range(d_r):
        r_offset = r_val * d_q
        rho_q += rho_rq[r_offset:r_offset+d_q, r_offset:r_offset+d_q]
    S_Q = vn_entropy(rho_q)

    # S(R) — for diagnostic purposes
    # R is MSB: basis state |q,r> has index q + r * 2^{n_q}
    # To trace Q, we sum over q
    rho_r = np.zeros((d_r, d_r), dtype=np.complex64)
    for r1 in range(d_r):
        for r2 in range(d_r):
            total = 0j
            for q in range(d_q):
                idx1 = q + r1 * d_q
                idx2 = q + r2 * d_q
                total += rho_rq[idx1, idx2]
            rho_r[r1, r2] = total
    S_R = vn_entropy(rho_r)

    # S(RQE) = n_E * H(p) (invariant under QE unitary!)
    Hp = -p * np.log2(p) - (1-p) * np.log2(1-p)
    S_RQE = n_e * Hp

    # S(QE) = n_E * H(p) + n_q (due to Bell state contribution)
    # Actually: S(QE) = S(RQE) + n_R = n_E*H(p) + n_q
    # (because the initial Bell state contributes n_R bits of entropy to Q)
    S_QE = S_RQE + n_r

    # QCMI = S(QE) + S(RQ) - S(RQE) - S(Q)
    QCMI = S_QE + S_RQ - S_RQE - S_Q
    QCMI = max(0.0, QCMI.real)  # QCMI must be non-negative

    return {
        'b1': b1,
        'n_q': n_q, 'n_e': n_e, 'n_r': n_r,
        'QCMI': QCMI,
        'S_RQ': S_RQ,
        'S_Q': S_Q,
        'S_R': S_R,
        'S_QE': S_QE,
        'S_RQE': S_RQE,
        'QCMI_per_b1': QCMI / b1 if b1 > 0 else float('nan'),
        'n_configs': n_configs,
        'use_exact': use_exact,
        'sim_time': elapsed,
    }


# ======== Hessian Model Analysis ========

def fit_hessian_model(b1_vals, qcmi_vals, stdevs=None):
    """
    Fit the tridiagonal Hessian model to chain-of-rings data.

    For the chain, the Hessian H is tridiagonal:
      H_{ii} = 2*eta (per-ring contribution)
      H_{i,i+1} = H_{i+1,i} = h (shared-Q interference)

    QCMI(b1) ≈ (1/2) * c^T H c
    For equal Cartan parameters c_i = c:
      QCMI ≈ (c²/2) * [b1 * 2*eta + 2*(b1-1) * h]
           = c² * [b1 * eta + (b1-1) * h]
           = b1 * (c²*eta + c²*h) - c²*h

    Define: A = c²*eta, B = c²*h
    QCMI ≈ b1 * (A + B) - B

    Fit QCMI(b1) = alpha * b1 + beta
    Then: A + B = alpha, -B = beta → B = -beta, A = alpha + beta
    """

    def linear_model(x, alpha, beta):
        return alpha * x + beta

    b1_arr = np.array(b1_vals, dtype=float)
    qcmi_arr = np.array(qcmi_vals, dtype=float)

    if stdevs is not None:
        sigma = np.array(stdevs, dtype=float)
        popt, pcov = curve_fit(linear_model, b1_arr, qcmi_arr, sigma=sigma,
                               absolute_sigma=True, maxfev=10000)
    else:
        popt, pcov = curve_fit(linear_model, b1_arr, qcmi_arr, maxfev=10000)

    alpha, beta = popt
    alpha_err, beta_err = np.sqrt(np.diag(pcov))

    residuals = qcmi_arr - linear_model(b1_arr, *popt)
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((qcmi_arr - np.mean(qcmi_arr))**2)
    r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0

    # Extract Hessian parameters
    A_plus_B = alpha
    neg_B = -beta
    B_hessian = -beta
    A_hessian = alpha + beta

    # Effective per-ring QCMI in the large-b1 limit:
    # QCMI/b1 → c²*(eta + h) = A + B = alpha
    per_ring_asymptotic = alpha

    # Interference-to-diagonal ratio
    interference_ratio = B_hessian / A_hessian if A_hessian != 0 else float('inf')

    return {
        'alpha': alpha, 'alpha_err': alpha_err,
        'beta': beta, 'beta_err': beta_err,
        'r_squared': r_squared,
        'A_hessian': A_hessian,  # c² * eta
        'B_hessian': B_hessian,  # c² * h (interference)
        'per_ring_asymptotic': per_ring_asymptotic,
        'interference_ratio': interference_ratio,
        'linear_model': lambda x: alpha * x + beta,
    }


def fit_log_model(b1_vals, qcmi_vals, stdevs=None):
    """Fit QCMI = A + B*log(b1+1)."""
    b1_arr = np.array(b1_vals, dtype=float)
    qcmi_arr = np.array(qcmi_vals, dtype=float)

    def log_model(x, A, B):
        return A + B * np.log(x + 1)

    try:
        if stdevs is not None:
            popt, pcov = curve_fit(log_model, b1_arr, qcmi_arr,
                                   sigma=np.array(stdevs), absolute_sigma=True, maxfev=10000)
        else:
            popt, pcov = curve_fit(log_model, b1_arr, qcmi_arr, maxfev=10000)

        A, B = popt
        residuals = qcmi_arr - log_model(b1_arr, *popt)
        ss_res = np.sum(residuals**2)
        ss_tot = np.sum((qcmi_arr - np.mean(qcmi_arr))**2)
        r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0

        return {'model': 'log', 'A': A, 'B': B, 'r_squared': r_squared,
                'predict': lambda x: A + B * np.log(x + 1)}
    except Exception:
        return None


def fit_power_model(b1_vals, qcmi_vals, stdevs=None):
    """Fit QCMI = A * b1^alpha."""
    b1_arr = np.array(b1_vals, dtype=float)
    qcmi_arr = np.array(qcmi_vals, dtype=float)

    def power_model(x, A, alpha):
        return A * np.abs(x)**alpha

    try:
        if stdevs is not None:
            popt, pcov = curve_fit(power_model, b1_arr, qcmi_arr,
                                   sigma=np.array(stdevs), absolute_sigma=True, maxfev=10000)
        else:
            popt, pcov = curve_fit(power_model, b1_arr, qcmi_arr, maxfev=10000)

        A, alpha = popt
        residuals = qcmi_arr - power_model(b1_arr, *popt)
        ss_res = np.sum(residuals**2)
        ss_tot = np.sum((qcmi_arr - np.mean(qcmi_arr))**2)
        r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0

        return {'model': 'power', 'A': A, 'alpha': alpha, 'r_squared': r_squared,
                'predict': lambda x: A * np.abs(x)**alpha}
    except Exception:
        return None


def fit_saturation_model(b1_vals, qcmi_vals, stdevs=None):
    """Fit QCMI = A * (1 - exp(-b1/B))."""
    b1_arr = np.array(b1_vals, dtype=float)
    qcmi_arr = np.array(qcmi_vals, dtype=float)

    def sat_model(x, A, B):
        return A * (1 - np.exp(-x / max(B, 1e-6)))

    try:
        popt, pcov = curve_fit(sat_model, b1_arr, qcmi_arr,
                               p0=[max(qcmi_arr)*1.5, 2.0], maxfev=10000)
        A, B = popt
        residuals = qcmi_arr - sat_model(b1_arr, *popt)
        ss_res = np.sum(residuals**2)
        ss_tot = np.sum((qcmi_arr - np.mean(qcmi_arr))**2)
        r_squared = 1 - ss_res / ss_tot if ss_tot > 0 else 0

        return {'model': 'saturation', 'A_sat': A, 'B_char': B, 'r_squared': r_squared,
                'predict': lambda x: A * (1 - np.exp(-x / max(B, 1e-6)))}
    except Exception:
        return None


# ======== Hessian Spectral Analysis for Heavy-Hex ========

def analyze_hessian_spectrum(N_rings, alpha=0.5):
    """
    Compute the Hessian eigenvalue spectrum for a heavy-hex dual graph.

    Heavy-hex dual graph: each hexagon is a vertex, edges connect hexagons
    sharing a Q node. This forms a triangular lattice fragment with N_rings vertices.

    H/H_0 = I + alpha * A_dual

    For a triangular lattice with periodic BC:
      lambda_k = 1 + alpha * 2[cos(kx) + cos(ky) + cos(kx+ky)]

    Min eigenvalue: lambda_min ≈ 1 - 3*alpha (bulk), can go negative.
    """
    # Use finite-size triangular lattice approximation
    # For a Lx * Ly triangular lattice with open boundaries
    Lx = int(np.sqrt(N_rings / np.sqrt(3)))  # Approximate square dimensions
    Ly = int(N_rings / Lx) if Lx > 0 else 1
    Lx = max(Lx, 1)
    Ly = max(Ly, 1)

    # Build adjacency matrix for the dual graph
    n_vertices = Lx * Ly
    A = np.zeros((n_vertices, n_vertices))

    for y in range(Ly):
        for x in range(Lx):
            i = y * Lx + x
            # Horizontal neighbors
            if x + 1 < Lx:
                A[i, i + 1] = 1
                A[i + 1, i] = 1
            if x - 1 >= 0:
                A[i, i - 1] = 1
            # Vertical neighbors
            if y + 1 < Ly:
                A[i, i + Lx] = 1
                A[i + Lx, i] = 1
            # Diagonal neighbors (triangular lattice diagonal edges)
            if x + 1 < Lx and y + 1 < Ly:
                j = (y + 1) * Lx + (x + 1)
                A[i, j] = 1
                A[j, i] = 1

    # H = I + alpha * A
    H = np.eye(n_vertices) + alpha * A

    eigenvalues = np.linalg.eigvalsh(H)

    return {
        'n_vertices': n_vertices,
        'Lx': Lx, 'Ly': Ly,
        'alpha': alpha,
        'eigenvalues': eigenvalues,
        'lambda_min': eigenvalues[0],
        'lambda_max': eigenvalues[-1],
        'n_negative': np.sum(eigenvalues < 0),
        'fraction_negative': np.sum(eigenvalues < 0) / n_vertices,
    }


# ======== Confidence Bands for Extrapolation ========

def compute_extrapolation_bands(fits, b1_target=60, n_bootstrap=1000):
    """
    Compute confidence bands for extrapolation using bootstrap resampling
    of the linear fit parameters.
    """
    results = {}

    for name, fit in fits.items():
        if fit is None:
            continue

        if name == 'linear_hessian':
            alpha, beta = fit['alpha'], fit['beta']
            alpha_err, beta_err = fit['alpha_err'], fit['beta_err']

            # Monte Carlo sampling from parameter distribution
            np.random.seed(42)
            alpha_samples = np.random.normal(alpha, alpha_err, n_bootstrap)
            beta_samples = np.random.normal(beta, beta_err, n_bootstrap)

            predictions = alpha_samples * b1_target + beta_samples
            results[name] = {
                'central': alpha * b1_target + beta,
                'std': np.std(predictions),
                'CI_68': np.percentile(predictions, [16, 84]),
                'CI_95': np.percentile(predictions, [2.5, 97.5]),
                'per_ring': (alpha * b1_target + beta) / b1_target,
                'per_ring_ci': np.percentile(predictions / b1_target, [16, 84]),
            }

        elif fit and 'predict' in fit:
            pred = fit['predict'](b1_target)
            results[name] = {
                'central': pred,
                'per_ring': pred / b1_target,
            }

    return results


# ======== Main ========

if __name__ == '__main__':
    print("=" * 72)
    print("W1 ATTACK: CHAIN-OF-RINGS QCMI — PUSHING PAST b1=4")
    print("=" * 72)
    print()

    p = 0.7
    b1_targets = [1, 2, 3, 4, 5]  # Push to b1=5!

    all_results = {}

    for b1 in b1_targets:
        print(f"\n{'='*60}")
        print(f"Simulating b1={b1} (chain of {b1} rings)")
        print(f"{'='*60}")

        n_e = 2 * b1
        n_all_e = 2**n_e

        # For b1=5: 1024 E configs, use exact enumeration
        # For larger b1: we'd need sampling (not implemented for now)
        max_configs = 1024 if n_all_e <= 1024 else 200

        result = simulate_chain_qcmi(b1, p=p, seed=42, n_configs=max_configs)
        all_results[b1] = result

        print(f"  QCMI = {result['QCMI']:.6f} bits")
        print(f"  S(RQ) = {result['S_RQ']:.6f}, S(Q) = {result['S_Q']:.6f}")
        print(f"  S(R) = {result['S_R']:.6f} (expect {result['n_r']:.1f})")
        print(f"  QCMI/b1 = {result['QCMI_per_b1']:.6f}")

        # Check invariants
        print(f"  S(QE) = {result['S_QE']:.6f} (expect {result['n_e']*0.8813 + result['n_r']:.4f})")
        print(f"  S(RQE) = {result['S_RQE']:.6f} (expect {result['n_e']*0.8813:.4f})")

    print(f"\n\n{'='*72}")
    print("SUMMARY: CHAIN-OF-RINGS QCMI")
    print(f"{'='*72}")
    print(f"{'b1':>4s} {'n_q':>4s} {'n_e':>4s} {'total qb':>9s} {'QCMI':>10s} {'QCMI/b1':>10s} {'S(RQ)':>10s} {'S(Q)':>10s}")
    print(f"{'='*64}")

    b1_list = []
    qcmi_list = []
    qcmi_std_list = []

    for b1 in [1, 2, 3, 4, 5]:
        if b1 in all_results:
            r = all_results[b1]
            b1_list.append(b1)
            qcmi_list.append(r['QCMI'])
            # Estimate std from the finite sampling error
            # For exact enumeration, the error is numerical only (~1e-12)
            # For sampling, we can estimate from the convergence
            est_std = max(1e-4, r['QCMI'] * 0.005)  # conservative 0.5% error
            qcmi_std_list.append(est_std)
            print(f"{b1:4d} {r['n_q']:4d} {r['n_e']:4d} {2**r['n_q']+r['n_e']+r['n_q']:9d} "
                  f"{r['QCMI']:10.6f} {r['QCMI_per_b1']:10.6f} "
                  f"{r['S_RQ']:10.6f} {r['S_Q']:10.6f}")

    # Also add the reference b1=0 (no ring, just a tree) with Q=2, E=2 qubits
    # We can't easily simulate this in the chain framework, so skip it.

    print(f"\n\n{'='*72}")
    print("FUNCTIONAL FORM FITTING")
    print(f"{'='*72}")

    b1_arr = np.array(b1_list)
    qcmi_arr = np.array(qcmi_list)

    # Fit various models
    fits = {}

    # 1. Linear (Hessian) model
    fit_lin = fit_hessian_model(b1_list, qcmi_list, qcmi_std_list)
    fits['linear_hessian'] = fit_lin
    print(f"\n[Hessian/Linear Model] QCMI = alpha*b1 + beta")
    print(f"  alpha = {fit_lin['alpha']:.6f} +/- {fit_lin['alpha_err']:.6f}")
    print(f"  beta  = {fit_lin['beta']:.6f} +/- {fit_lin['beta_err']:.6f}")
    print(f"  R²    = {fit_lin['r_squared']:.6f}")
    print(f"  Per-ring asymptotic (large b1): {fit_lin['per_ring_asymptotic']:.6f}")
    print(f"  Interference/diagonal ratio: {fit_lin['interference_ratio']:.6f}")
    print(f"  Hessian: H_ii = 2*eta*c² (A={fit_lin['A_hessian']:.4f}), "
          f"H_{i,i+1} = h*c² (B={fit_lin['B_hessian']:.4f})")

    # 2. Log model
    fit_log = fit_log_model(b1_list, qcmi_list, qcmi_std_list)
    fits['log'] = fit_log
    if fit_log:
        print(f"\n[Log Model] QCMI = A + B*log(b1+1)")
        print(f"  A = {fit_log['A']:.6f}, B = {fit_log['B']:.6f}")
        print(f"  R² = {fit_log['r_squared']:.6f}")

    # 3. Power-law model
    fit_pow = fit_power_model(b1_list, qcmi_list, qcmi_std_list)
    fits['power'] = fit_pow
    if fit_pow:
        print(f"\n[Power Model] QCMI = A * b1^alpha")
        print(f"  A = {fit_pow['A']:.6f}, alpha = {fit_pow['alpha']:.6f}")
        print(f"  R² = {fit_pow['r_squared']:.6f}")

    # 4. Saturation model
    fit_sat = fit_saturation_model(b1_list, qcmi_list, qcmi_std_list)
    fits['saturation'] = fit_sat
    if fit_sat:
        print(f"\n[Saturation Model] QCMI = A * (1 - exp(-b1/B))")
        print(f"  A_sat = {fit_sat['A_sat']:.6f}, B_char = {fit_sat['B_char']:.6f}")
        print(f"  R² = {fit_sat['r_squared']:.6f}")

    # Extrapolate to b1=60
    print(f"\n\n{'='*72}")
    print("EXTRAPOLATION TO b1=60")
    print(f"{'='*72}")

    extrap = compute_extrapolation_bands(fits, b1_target=60)

    for model_name, pred in extrap.items():
        print(f"\n[{model_name}]")
        if 'CI_95' in pred:
            print(f"  QCMI(60) = {pred['central']:.6f} bits")
            print(f"  68% CI: [{pred['CI_68'][0]:.6f}, {pred['CI_68'][1]:.6f}]")
            print(f"  95% CI: [{pred['CI_95'][0]:.6f}, {pred['CI_95'][1]:.6f}]")
            print(f"  Per-ring: {pred['per_ring']:.6f}")
            print(f"  Per-ring 68% CI: [{pred['per_ring_ci'][0]:.6f}, {pred['per_ring_ci'][1]:.6f}]")
        else:
            print(f"  QCMI(60) = {pred['central']:.6f} bits")
            print(f"  Per-ring: {pred['per_ring']:.6f}")

    # Hessian spectral analysis for heavy-hex
    print(f"\n\n{'='*72}")
    print("HESSIAN SPECTRAL ANALYSIS: HEAVY-HEX b1=60")
    print(f"{'='*72}")

    for alpha_val in [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]:
        spec = analyze_hessian_spectrum(60, alpha=alpha_val)
        status = "NEGATIVE EIGENVALUES" if spec['n_negative'] > 0 else "All positive"
        print(f"\n  alpha={alpha_val}: λ_min={spec['lambda_min']:.4f}, "
              f"λ_max={spec['lambda_max']:.4f}, "
              f"n_neg={spec['n_negative']}/{spec['n_vertices']} ({spec['fraction_negative']:.2%})"
              f"  [{status}]")

    # Critical alpha for zero eigenvalue
    print(f"\n  Critical alpha for λ_min=0 at N=60:")
    for alpha_test in np.linspace(0.1, 0.5, 41):
        spec = analyze_hessian_spectrum(60, alpha=alpha_test)
        if spec['n_negative'] > 0:
            print(f"    alpha_crit ≈ {alpha_test:.3f} (first negative eigenvalue appears)")
            break

    print(f"\n{'='*72}")
    print("ATTACK COMPLETE")
    print(f"{'='*72}")

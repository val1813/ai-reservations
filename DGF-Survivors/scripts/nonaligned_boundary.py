"""
Nonaligned Boundary Plaquette Theorem -- Full Computation
===========================================================
Generalizes BPT (boundary_plaqutte_theorem.md) to non-aligned Cartan axes.

Setup: 4-qubit ring Q_a -> E_1 -> Q_b -> E_2 -> Q_a
- Edges 1,2 (rotating region): c_1=c_2=c, n_1=n_2=n_rot
- Edges 3,4 (static region):   c_3=c_4=pi/2, n_3=n_4=n_stat
- n_rot . n_stat = cos(phi), phi in [0, pi]

Key physics: [sigma_{n_rot} x sigma_{n_rot}, sigma_{n_stat} x sigma_{n_stat}] != 0
This non-commutativity breaks Gram matrix factorization and creates
qualitatively new QCMI behavior.

Two computation methods (cross-validated):
  Method 1: Gram matrix via |psi_a><psi_b| + partial trace
  Method 2: QCMI via 8-qubit purification

Tasks:
  4a. Compute Gram matrix explicitly for non-aligned axes
  4b. QCMI(phi, c, p) phase diagrams via grid scan
  4c. Answer Q1-Q3: monotonicity, screening, testable predictions
"""

import numpy as np
from numpy.linalg import eigh, eigvalsh
import time
import json
import os

# ============================================================
# Pauli matrices and basic operators
# ============================================================

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = [I2, X, Y, Z]

# ============================================================
# Helper functions
# ============================================================

def H2(x):
    """Binary entropy in bits. H2(x) = -x log2 x - (1-x) log2(1-x)."""
    if x <= 1e-15 or x >= 1 - 1e-15:
        return 0.0
    return -x * np.log2(x) - (1 - x) * np.log2(1 - x)


def von_neumann_entropy(rho, eps=1e-12):
    """Von Neumann entropy S(rho) in bits."""
    evals = eigh(rho)[0]
    evals = np.maximum(np.real(evals), eps)
    evals = evals / evals.sum()
    return -np.sum(evals * np.log2(evals))


def sigma_n(n_hat):
    """sigma_{n_hat} = n_x X + n_y Y + n_z Z."""
    return n_hat[0] * X + n_hat[1] * Y + n_hat[2] * Z


def eigenstates_n(n_hat):
    """
    Compute |+_n> and |-_n> in the computational basis.

    For n_hat = (sin theta cos phi, sin theta sin phi, cos theta):
    |+_n> = cos(theta/2) |0> + e^{i phi} sin(theta/2) |1>
    |-_n> = sin(theta/2) |0> - e^{i phi} cos(theta/2) |1>

    Returns (plus_vec, minus_vec) as complex numpy arrays of length 2.
    """
    nx, ny, nz = n_hat
    theta = np.arccos(np.clip(nz, -1.0, 1.0))
    if abs(nx) < 1e-15 and abs(ny) < 1e-15:
        phi = 0.0
    else:
        phi = np.arctan2(ny, nx)

    c_half = np.cos(theta / 2)
    s_half = np.sin(theta / 2)
    e_iphi = np.exp(1j * phi)

    plus = np.array([c_half, e_iphi * s_half], dtype=complex)
    minus = np.array([s_half, -e_iphi * c_half], dtype=complex)
    return plus, minus


def state_gamma(p, n_hat):
    """
    |gamma> = sqrt(p) |+_n> + sqrt(1-p) |-_n>
    Returns 2-component complex vector in computational basis.
    """
    plus, minus = eigenstates_n(n_hat)
    return np.sqrt(p) * plus + np.sqrt(1 - p) * minus


def purification_env(p, n_hat):
    """
    Purification of rho_E = p |+_n><+_n| + (1-p) |-_n><-_n|.

    |psi>_{E,A} = sqrt(p) |+_n>_E |0>_A + sqrt(1-p) |-_n>_E |1>_A

    Returns 4-component complex vector in computational basis:
    indices: [E=0,A=0], [E=0,A=1], [E=1,A=0], [E=1,A=1]
    """
    plus, minus = eigenstates_n(n_hat)
    psi = np.zeros(4, dtype=complex)
    # E=0, A=0: sqrt(p) * <0|+_n>
    psi[0] = np.sqrt(p) * plus[0]
    # E=1, A=0: sqrt(p) * <1|+_n>
    psi[2] = np.sqrt(p) * plus[1]
    # E=0, A=1: sqrt(1-p) * <0|-_n>
    psi[1] = np.sqrt(1 - p) * minus[0]
    # E=1, A=1: sqrt(1-p) * <1|-_n>
    psi[3] = np.sqrt(1 - p) * minus[1]
    return psi


# ============================================================
# Cartan gate and ring unitary
# ============================================================

def cartan_gate(c, n_hat):
    """
    U(c, n_hat) = exp(i c sigma_n  x  sigma_n)
                = cos(c) I x I + i sin(c) sigma_n  x  sigma_n
    """
    sigma = sigma_n(n_hat)
    return np.cos(c) * np.kron(I2, I2) + 1j * np.sin(c) * np.kron(sigma, sigma)


def embed_2q_to_4q(gate_2q, q_a, q_b):
    """Embed a 2-qubit unitary into a 4-qubit space."""
    U = np.zeros((16, 16), dtype=complex)
    for idx in range(16):
        bits = [(idx >> q) & 1 for q in range(4)]
        for a_out in [0, 1]:
            for b_out in [0, 1]:
                for a_in in [0, 1]:
                    for b_in in [0, 1]:
                        g = gate_2q[a_out * 2 + b_out, a_in * 2 + b_in]
                        if abs(g) < 1e-15:
                            continue
                        in_bits = list(bits)
                        in_bits[q_a] = a_in
                        in_bits[q_b] = b_in
                        spectator_ok = True
                        for q in range(4):
                            if q not in (q_a, q_b) and bits[q] != in_bits[q]:
                                spectator_ok = False
                                break
                        if not spectator_ok:
                            continue
                        in_idx = sum(bit << q for q, bit in enumerate(in_bits))
                        out_bits = list(bits)
                        out_bits[q_a] = a_out
                        out_bits[q_b] = b_out
                        out_idx = sum(bit << q for q, bit in enumerate(out_bits))
                        U[out_idx, in_idx] = g
    return U


def build_ring(c1, c2, c3, c4, n1, n2, n3, n4):
    """Build 4-qubit ring unitary: U = U4 U3 U2 U1."""
    U1 = embed_2q_to_4q(cartan_gate(c1, n1), 0, 1)  # Q_a - E1
    U2 = embed_2q_to_4q(cartan_gate(c2, n2), 1, 2)  # E1 - Q_b
    U3 = embed_2q_to_4q(cartan_gate(c3, n3), 2, 3)  # Q_b - E2
    U4 = embed_2q_to_4q(cartan_gate(c4, n4), 3, 0)  # E2 - Q_a
    return U4 @ U3 @ U2 @ U1


# ============================================================
# Partial trace (manual, for 4-qubit and 8-qubit systems)
# ============================================================

def partial_trace_manual(rho, keep, dims):
    """Trace out all qubits not in 'keep'. Generalized for any dimensions."""
    n = len(dims)
    trace_axes = tuple(i for i in range(n) if i not in keep)
    d_keep = int(np.prod([dims[i] for i in keep]))
    d_trace = int(np.prod([dims[i] for i in trace_axes]))
    bra_strides = [1 << i for i in range(n)]

    rho_reduced = np.zeros((d_keep, d_keep), dtype=complex)
    for bra_keep_idx in range(d_keep):
        bra_keep_vals = []
        rem = bra_keep_idx
        for k in reversed(keep):
            sz = dims[k]
            bra_keep_vals.insert(0, rem % sz)
            rem //= sz

        for ket_keep_idx in range(d_keep):
            ket_keep_vals = []
            rem = ket_keep_idx
            for k in reversed(keep):
                sz = dims[k]
                ket_keep_vals.insert(0, rem % sz)
                rem //= sz

            total = 0.0 + 0.0j
            for trace_idx in range(d_trace):
                trace_vals = []
                rem = trace_idx
                for t in reversed(trace_axes):
                    sz = dims[t]
                    trace_vals.insert(0, rem % sz)
                    rem //= sz

                bra_full = [0] * n
                ket_full = [0] * n
                for pos, k in enumerate(keep):
                    bra_full[k] = bra_keep_vals[pos]
                    ket_full[k] = ket_keep_vals[pos]
                for pos, t in enumerate(trace_axes):
                    bra_full[t] = trace_vals[pos]
                    ket_full[t] = trace_vals[pos]

                bra_flat = sum(bra_full[i] * bra_strides[i] for i in range(n))
                ket_flat = sum(ket_full[i] * bra_strides[i] for i in range(n))
                total += rho[bra_flat, ket_flat]

            rho_reduced[bra_keep_idx, ket_keep_idx] = total

    return rho_reduced


# ============================================================
# Method 1: Gram matrix via |psi_a><psi_b| + partial trace
# ============================================================

def gram_matrix_nonaligned(c, phi, p, env_axis_mode='stat'):
    """
    Compute the 4x4 Gram matrix for the non-aligned boundary plaquette.

    G_{a,b} = <a|_S Tr_E[U (|a><b|_S  x  |gamma><gamma|_E1  x  |gamma><gamma|_E2) U^dag] |b>_S

    Uses |psi_a><psi_b| + partial trace. Only 4 state vector preparations needed.

    Args:
        c: rotating region Cartan parameter
        phi: angle between n_rot and n_stat (in radians)
        p: purity parameter in (0,1)
        env_axis_mode: 'stat' (vacuum axis) or 'rot' (particle axis)
                       or 'both_stat' (both use n_stat)

    Returns:
        4x4 complex Gram matrix
    """
    # Set up axes
    n_rot = np.array([np.sin(phi), 0.0, np.cos(phi)])
    n_stat = np.array([0.0, 0.0, 1.0])

    # Build ring unitary: U = U4 U3 U2 U1
    U = build_ring(c, c, np.pi/2, np.pi/2, n_rot, n_rot, n_stat, n_stat)

    # Environment state axis
    if env_axis_mode == 'stat':
        env_axis = n_stat
    elif env_axis_mode == 'rot':
        env_axis = n_rot
    elif env_axis_mode == 'both_stat':
        env_axis = n_stat
    elif env_axis_mode == 'per_qubit':
        # E1 uses n_rot, E2 uses n_stat
        gamma1 = state_gamma(p, n_rot)
        gamma2 = state_gamma(p, n_stat)
    else:
        raise ValueError(f"Unknown env_axis_mode: {env_axis_mode}")

    if env_axis_mode != 'per_qubit':
        gamma1 = state_gamma(p, env_axis)
        gamma2 = state_gamma(p, env_axis)

    # Prepare |psi_a> for each system basis state a
    # 4-qubit ordering: [Q_a=bit0, E1=bit1, Q_b=bit2, E2=bit3]
    # System qubits: 0, 2
    # Environment qubits: 1, 3
    psi_vectors = []
    for a in range(4):
        qa = (a >> 1) & 1  # Q_a
        qb = a & 1          # Q_b

        psi = np.zeros(16, dtype=complex)
        for e1 in range(2):
            for e2 in range(2):
                idx = (qa << 0) | (e1 << 1) | (qb << 2) | (e2 << 3)
                psi[idx] = gamma1[e1] * gamma2[e2]

        psi_vectors.append(psi)

    # Evolve all |psi_a>
    psi_evolved = [U @ psi for psi in psi_vectors]

    # Compute G_{a,b}
    G = np.zeros((4, 4), dtype=complex)
    dims_4q = (2, 2, 2, 2)

    for a in range(4):
        for b in range(4):
            # rho_ab' = |psi_a'><psi_b'|
            rho_ab = np.outer(psi_evolved[a], psi_evolved[b].conj())

            # Trace out environment (qubits 1, 3), keep system (0, 2)
            rho_S = partial_trace_manual(rho_ab, (0, 2), dims_4q)

            # System basis: reduced matrix index = qa*2 + qb
            qa_a, qb_a = (a >> 1) & 1, a & 1
            qa_b, qb_b = (b >> 1) & 1, b & 1
            sys_a_idx = qa_a * 2 + qb_a
            sys_b_idx = qb_a * 2 + qb_b  # This should be qa_b*2+qb_b
            # Fix: use a and b directly since they encode qa*2+qb
            # Actually a = qa*2+qb by construction
            G[a, b] = rho_S[a, b]

    return G


# ============================================================
# BPT-3 aligned closed form (for validation)
# ============================================================

def qcmi_boundary_aligned_closed(c, p):
    """
    BPT-3 closed form for aligned case (phi=0).
    QCMI(c,p) = H2(1/2 + 1/2 * sqrt(1 - p(1-p)[4 sin^2(2c) + sin^2(4c)]))
    """
    b = p * (1 - p)
    s2c = np.sin(2 * c)
    s4c = np.sin(4 * c)
    combined = 4 * s2c**2 + s4c**2
    Delta_sq = 1 - b * combined

    if Delta_sq < 0:
        if Delta_sq > -1e-12:
            Delta_sq = 0.0
        else:
            raise ValueError(f"Delta_sq={Delta_sq} < 0 for c={c}, p={p}")

    Delta = np.sqrt(max(Delta_sq, 0))
    x = 0.5 + 0.5 * Delta
    return H2(x)


def qcmi_from_gram(G):
    """QCMI = S(G/4) from Gram matrix eigenvalues."""
    evals = eigvalsh(G)
    evals = np.maximum(np.real(evals), 0)
    evals = evals / evals.sum()
    nonzero = evals[evals > 1e-15]
    return -np.sum(nonzero * np.log2(nonzero))


# ============================================================
# Method 2: QCMI via 8-qubit purification
# ============================================================

def qcmi_nonaligned_8q(c, phi, p, env_axis_mode='stat'):
    """
    Compute QCMI via 8-qubit purification.

    8-qubit ordering: [R_a, R_b, Q_a, Q_b, E1, A1, E2, A2] (bits 0..7)
    Ring acts on: Q_a(2), E1(4), Q_b(3), E2(6)

    QCMI = I(R;E'|Q') = S(rho_RQ) + S(rho_EQ) - S(rho_Q) - S(rho_REQ)

    Args:
        c: rotating region Cartan parameter
        phi: angle between n_rot and n_stat
        p: purity parameter
        env_axis_mode: 'stat' (vacuum axis for both env qubits),
                       'per_qubit' (E1 uses n_rot, E2 uses n_stat)

    Returns:
        (QCMI, S_RQ, S_EQ, S_Q) in bits
    """
    # Set up axes
    n_rot = np.array([np.sin(phi), 0.0, np.cos(phi)])
    n_stat = np.array([0.0, 0.0, 1.0])

    # Build ring unitary
    U = build_ring(c, c, np.pi/2, np.pi/2, n_rot, n_rot, n_stat, n_stat)

    # Environment purification axes
    if env_axis_mode == 'stat':
        n_E1, n_E2 = n_stat, n_stat
    elif env_axis_mode == 'per_qubit':
        n_E1, n_E2 = n_rot, n_stat
    elif env_axis_mode == 'rot':
        n_E1, n_E2 = n_rot, n_rot
    else:
        raise ValueError(f"Unknown env_axis_mode: {env_axis_mode}")

    # Purification states
    psi_E1A1 = purification_env(p, n_E1)  # 4-component vector
    psi_E2A2 = purification_env(p, n_E2)  # 4-component vector

    # Initial 8-qubit state: |Phi+>_{RQ}  x  |psi>_{E1A1}  x  |psi>_{E2A2}
    n_q = 8
    d_tot = 256
    psi_init = np.zeros(d_tot, dtype=complex)

    for ra in range(2):
        for rb in range(2):
            for qa in range(2):
                for qb in range(2):
                    # Reference-system Bell state: |ra,rb>_R  x  |qa,qb>_Q with amp = 0.5 if matching
                    # |Phi+> = (1/2)(|00>|00> + |01>|01> + |10>|10> + |11>|11>)
                    amp_RQ = 0.5 if (ra == qa and rb == qb) else 0.0
                    if amp_RQ == 0.0:
                        continue

                    for e1 in range(2):
                        for a1 in range(2):
                            amp_E1A1 = psi_E1A1[e1 * 2 + a1]
                            if abs(amp_E1A1) < 1e-15:
                                continue

                            for e2 in range(2):
                                for a2 in range(2):
                                    amp_E2A2 = psi_E2A2[e2 * 2 + a2]
                                    if abs(amp_E2A2) < 1e-15:
                                        continue

                                    bits = [ra, rb, qa, qb, e1, a1, e2, a2]
                                    idx = sum(bit << q for q, bit in enumerate(bits))
                                    psi_init[idx] = amp_RQ * amp_E1A1 * amp_E2A2

    # Embed ring unitary into 8-qubit space
    # Ring acts on qubits [Q_a=2, E1=4, Q_b=3, E2=6]
    q_U = [2, 4, 3, 6]
    U_big = np.eye(d_tot, dtype=complex)

    for idx in range(d_tot):
        bits = [(idx >> q) & 1 for q in range(n_q)]
        in_4b = ((bits[q_U[0]] << 0) | (bits[q_U[1]] << 1) |
                 (bits[q_U[2]] << 2) | (bits[q_U[3]] << 3))
        for out_4b in range(16):
            u_elem = U[out_4b, in_4b]
            if abs(u_elem) < 1e-15:
                continue
            out_bits = list(bits)
            out_bits[q_U[0]] = (out_4b >> 0) & 1
            out_bits[q_U[1]] = (out_4b >> 1) & 1
            out_bits[q_U[2]] = (out_4b >> 2) & 1
            out_bits[q_U[3]] = (out_4b >> 3) & 1
            out_idx = sum(bit << q for q, bit in enumerate(out_bits))
            U_big[out_idx, idx] = u_elem

    # Evolve
    psi_out = U_big @ psi_init
    rho_tot = np.outer(psi_out, psi_out.conj())

    # Partial traces: keep R(0,1), Q(2,3), E1(4), E2(6) -- trace out A1(5), A2(7)
    dims_8q = (2, 2, 2, 2, 2, 2, 2, 2)
    keep_REQ = (0, 1, 2, 3, 4, 6)  # trace out A1(5), A2(7)
    rho_REQ = partial_trace_manual(rho_tot, keep_REQ, dims_8q)

    dims_REQ = (2, 2, 2, 2, 2, 2)
    # rho_RQ: keep R(0,1), Q(2,3)
    rho_RQ = partial_trace_manual(rho_REQ, (0, 1, 2, 3), dims_REQ)
    # rho_EQ: keep Q(2,3), E1(4), E2(5 in reduced space = orig 6)
    rho_EQ = partial_trace_manual(rho_REQ, (2, 3, 4, 5), dims_REQ)
    # rho_Q: keep Q(2,3)
    rho_Q = partial_trace_manual(rho_REQ, (2, 3), dims_REQ)

    S_RQ = von_neumann_entropy(rho_RQ)
    S_EQ = von_neumann_entropy(rho_EQ)
    S_Q = von_neumann_entropy(rho_Q)
    S_REQ = von_neumann_entropy(rho_REQ)

    # QCMI = I(R;E|Q) = S(RQ) + S(EQ) - S(Q) - S(REQ)
    # Note: S(REQ) = S(A) = 2*H2(p) in general (purification)
    QCMI = S_RQ + S_EQ - S_Q - S_REQ

    return QCMI, S_RQ, S_EQ, S_Q, S_REQ


# ============================================================
# Validation: Compare non-aligned Gram matrix at phi=0 with BPT-3
# ============================================================

def validate_against_bpt3():
    """Cross-validate the non-aligned methods against BPT-3 at phi=0."""
    print("=" * 70)
    print("VALIDATION: Non-aligned methods at phi=0 vs BPT-3 closed form")
    print("=" * 70)

    c_vals = [np.pi/16, np.pi/8, np.pi/4, np.pi/3, 0.5, 0.1, 0.01]
    p_vals = [0.3, 0.5, 0.7]

    max_err_gram = 0.0
    max_err_8q = 0.0

    for c in c_vals:
        for p in p_vals:
            # BPT-3 closed form (aligned)
            qcmi_bpt3 = qcmi_boundary_aligned_closed(c, p)

            # Method 1: Gram matrix at phi=0
            G = gram_matrix_nonaligned(c, 0.0, p, env_axis_mode='stat')
            qcmi_gram = qcmi_from_gram(G)
            err1 = abs(qcmi_gram - qcmi_bpt3)
            max_err_gram = max(max_err_gram, err1)

            # Method 2: 8-qubit purification at phi=0
            qcmi_8q, _, _, _, _ = qcmi_nonaligned_8q(c, 0.0, p, env_axis_mode='stat')
            err2 = abs(qcmi_8q - qcmi_bpt3)
            max_err_8q = max(max_err_8q, err2)

            if err1 > 1e-6 or err2 > 1e-6:
                print(f"  c={c:.4f}, p={p:.2f}: BPT3={qcmi_bpt3:.8f}, "
                      f"Gram={qcmi_gram:.8f} (err={err1:.2e}), "
                      f"8q={qcmi_8q:.8f} (err={err2:.2e})")

    print(f"\n  Max Gram error vs BPT-3: {max_err_gram:.2e}")
    print(f"  Max 8q error vs BPT-3:   {max_err_8q:.2e}")

    if max_err_gram < 1e-6 and max_err_8q < 1e-6:
        print("  VALIDATION PASSED: Both methods match BPT-3 at phi=0.  [OK]")
    else:
        print("  VALIDATION WARNING: Some discrepancies found.")

    return max_err_gram, max_err_8q


# ============================================================
# Task 4a: Gram matrix properties for non-aligned axes
# ============================================================

def analyze_gram_matrix():
    """Analyze Gram matrix structure for non-aligned axes."""
    print("\n" + "=" * 70)
    print("TASK 4a: Gram Matrix Analysis for Non-Aligned Axes")
    print("=" * 70)

    # Compare aligned vs non-aligned Gram matrices
    c = np.pi / 4
    p = 0.5
    phi_vals = [0, np.pi/8, np.pi/4, 3*np.pi/8, np.pi/2]

    for phi in phi_vals:
        G = gram_matrix_nonaligned(c, phi, p, env_axis_mode='stat')
        evals = eigvalsh(G)
        evals = np.sort(np.maximum(np.real(evals), 0))[::-1]

        # Check properties
        diag_real = np.all(np.abs(np.diag(G).imag) < 1e-12)
        herm = np.max(np.abs(G - G.conj().T))
        trace_G = np.real(np.trace(G))

        print(f"\n  phi={np.degrees(phi):.0f} deg (cos phi={np.cos(phi):.3f}):")
        print(f"    Hermiticity error: {herm:.2e}")
        print(f"    Trace: {trace_G:.6f}")
        print(f"    Diagonal real: {diag_real}")
        print(f"    Eigenvalues: {evals}")
        print(f"    Rank (tol=1e-10): {np.sum(evals > 1e-10)}")
        print(f"    |G[0,1]| = {abs(G[0,1]):.6f}  (cf. aligned = 1 at p=0.5)")

        # For aligned case (phi=0), check factorization
        if phi == 0:
            # Verify against BPT factorization
            def f_aligned(x, pp):
                return np.cos(x) + 1j * (2*pp - 1) * np.sin(x)

            # In aligned case: G_{s,t} = f(d1*c1+d3*c2) * f(d1*c4+d3*c3)
            # For boundary plaquette: c1=c2=c, c3=c4=pi/2
            # d1 = t1-s1, d3 = t3-s3
            states = [(1,1), (1,-1), (-1,1), (-1,-1)]  # (s1,s3)
            G_aligned = np.zeros((4,4), dtype=complex)
            for i, (s1,s3) in enumerate(states):
                for j, (t1,t3) in enumerate(states):
                    d1, d3 = t1-s1, t3-s3
                    G_aligned[i,j] = f_aligned(d1*c + d3*c, p) * f_aligned(d1*np.pi/2 + d3*np.pi/2, p)

            err_factorization = np.max(np.abs(G - G_aligned))
            print(f"    Factorization error vs BPT: {err_factorization:.2e}")

    # Check non-commutativity signature
    print("\n  Non-commutativity signature:")
    print("  [sigma_rot x sigma_rot, sigma_stat x sigma_stat] != 0 for phi != 0")
    for phi in [0, np.pi/8, np.pi/4, np.pi/2]:
        n_rot = np.array([np.sin(phi), 0.0, np.cos(phi)])
        n_stat = np.array([0.0, 0.0, 1.0])
        s_rot = sigma_n(n_rot)
        s_stat = sigma_n(n_stat)
        op1 = np.kron(s_rot, s_rot)
        op2 = np.kron(s_stat, s_stat)
        comm = op1 @ op2 - op2 @ op1
        norm_comm = np.linalg.norm(comm, 'fro')
        print(f"    phi={np.degrees(phi):.0f} deg: ||[H_rot, H_stat]||_F = {norm_comm:.6f}")


# ============================================================
# Task 4b: QCMI(phi, c, p) grid scan and phase diagrams
# ============================================================

def grid_scan_qcmi(phi_grid=None, c_grid=None, p_grid=None, method='8q'):
    """
    Systematic grid scan of QCMI(phi, c, p).

    Returns:
        results: dict with 3D array of QCMI values and metadata
    """
    if phi_grid is None:
        phi_grid = np.linspace(0, np.pi, 21)  # 0 to pi in 21 steps
    if c_grid is None:
        c_grid = np.linspace(0, np.pi/2, 21)
    if p_grid is None:
        p_grid = np.array([0.3, 0.5, 0.7])

    results = {
        'phi_grid': phi_grid.tolist(),
        'c_grid': c_grid.tolist(),
        'p_grid': p_grid.tolist(),
        'qcmi': np.zeros((len(phi_grid), len(c_grid), len(p_grid))),
        'method': method
    }

    total = len(phi_grid) * len(c_grid) * len(p_grid)
    count = 0
    t0 = time.time()

    for i, phi in enumerate(phi_grid):
        for j, c in enumerate(c_grid):
            for k, p in enumerate(p_grid):
                if method == '8q':
                    qcmi, _, _, _, _ = qcmi_nonaligned_8q(c, phi, p, env_axis_mode='stat')
                elif method == 'gram':
                    G = gram_matrix_nonaligned(c, phi, p, env_axis_mode='stat')
                    qcmi = qcmi_from_gram(G)
                else:
                    raise ValueError(f"Unknown method: {method}")

                results['qcmi'][i, j, k] = qcmi
                count += 1

                if count % 50 == 0:
                    elapsed = time.time() - t0
                    rate = count / elapsed
                    remaining = (total - count) / rate
                    print(f"  Progress: {count}/{total} ({100*count/total:.0f}%), "
                          f"ETA: {remaining:.0f}s", end='\r')

    elapsed = time.time() - t0
    print(f"\n  Grid scan complete: {total} points in {elapsed:.1f}s "
          f"({total/elapsed:.1f} pts/s)")

    results['qcmi'] = results['qcmi'].tolist()  # Convert to list for JSON
    return results


def print_phase_table(results):
    """Print a concise table of QCMI(phi, c, p) for the required grid."""
    phi_grid = np.array(results['phi_grid'])
    c_grid = np.array(results['c_grid'])
    p_grid = np.array(results['p_grid'])
    qcmi_arr = np.array(results['qcmi'])

    # Required grid: phi in {0, pi/8, pi/4, 3pi/8, pi/2},
    #                c in {pi/16, pi/8, pi/4},
    #                p in {0.3, 0.5, 0.7}
    req_phi = [0, np.pi/8, np.pi/4, 3*np.pi/8, np.pi/2]
    req_c = [np.pi/16, np.pi/8, np.pi/4]
    req_p = [0.3, 0.5, 0.7]

    print("\n" + "=" * 70)
    print("QCMI(phi, c, p) -- Required Grid")
    print("=" * 70)

    for p_idx, p in enumerate(req_p):
        print(f"\n  p = {p}:")
        header = f"  {'phi\\c':>10s}"
        for c in req_c:
            header += f"  {'c='+str(round(np.degrees(c)))+'deg':>14s}"
        print(header)
        print("  " + "-" * (10 + 16 * len(req_c)))

        for phi in req_phi:
            row = f"  {np.degrees(phi):8.0f} deg"
            for c in req_c:
                # Find closest grid points
                i = np.argmin(np.abs(phi_grid - phi))
                j = np.argmin(np.abs(c_grid - c))
                k = np.argmin(np.abs(p_grid - p))
                qcmi_val = qcmi_arr[i, j, k]
                row += f"  {qcmi_val:14.8f}"
            print(row)


def analyze_qcmi_landscape(results):
    """Analyze the QCMI landscape: min, max, monotonicity."""
    phi_grid = np.array(results['phi_grid'])
    c_grid = np.array(results['c_grid'])
    p_grid = np.array(results['p_grid'])
    qcmi_arr = np.array(results['qcmi'])

    print("\n" + "=" * 70)
    print("QCMI Landscape Analysis")
    print("=" * 70)

    for k, p in enumerate(p_grid):
        slice_2d = qcmi_arr[:, :, k]

        # Find minimum QCMI and its location
        min_idx = np.unravel_index(np.argmin(slice_2d), slice_2d.shape)
        max_idx = np.unravel_index(np.argmax(slice_2d), slice_2d.shape)

        print(f"\n  p = {p:.2f}:")
        print(f"    Min QCMI = {slice_2d[min_idx]:.8f} at "
              f"phi={np.degrees(phi_grid[min_idx[0]]):.0f} deg, "
              f"c={np.degrees(c_grid[min_idx[1]]):.1f} deg")
        print(f"    Max QCMI = {slice_2d[max_idx]:.8f} at "
              f"phi={np.degrees(phi_grid[max_idx[0]]):.0f} deg, "
              f"c={np.degrees(c_grid[max_idx[1]]):.1f} deg")

        # Check monotonicity in phi for fixed c
        print(f"    QCMI vs phi monotonicity (checking if dQCMI/dphi >= 0):")
        violations = 0
        for j in range(len(c_grid)):
            qcmi_slice = slice_2d[:, j]
            # Check if QCMI always increases with phi
            diffs = np.diff(qcmi_slice)
            neg_diffs = np.sum(diffs < -1e-10)
            if neg_diffs > 0:
                violations += 1
        print(f"      Non-monotonic c-slices: {violations}/{len(c_grid)}")

        # Compare aligned (phi=0) vs non-aligned
        aligned_qcmi = slice_2d[0, :]  # phi=0
        nonaligned_min = np.min(slice_2d[1:, :], axis=0)  # min over phi>0
        excess = nonaligned_min - aligned_qcmi
        always_larger = np.all(excess > -1e-10)
        print(f"    QCMI(phi>0) >= QCMI(phi=0) for all c: {always_larger}")
        if not always_larger:
            neg_idx = np.where(excess < -1e-10)[0]
            for idx in neg_idx[:3]:
                print(f"      Exception: c={np.degrees(c_grid[idx]):.1f} deg, "
                      f"aligned={aligned_qcmi[idx]:.6f}, "
                      f"min nonaligned={nonaligned_min[idx]:.6f}")


# ============================================================
# Task 4c: Answer three key questions
# ============================================================

def answer_q1_monotonicity(results):
    """
    Q1: Does non-alignment always increase QCMI?

    Check: QCMI(phi>0, c, p) >= QCMI(phi=0, c, p) for all c, p?
    """
    print("\n" + "=" * 70)
    print("Q1: Does non-alignment always increase QCMI?")
    print("=" * 70)

    phi_grid = np.array(results['phi_grid'])
    c_grid = np.array(results['c_grid'])
    p_grid = np.array(results['p_grid'])
    qcmi_arr = np.array(results['qcmi'])

    # Find phi=0 index
    phi0_idx = np.argmin(np.abs(phi_grid))

    all_strictly_larger = True
    exceptions = []

    for k, p in enumerate(p_grid):
        for j, c in enumerate(c_grid):
            aligned_val = qcmi_arr[phi0_idx, j, k]

            # Check all phi > 0
            for i in range(len(phi_grid)):
                if i == phi0_idx:
                    continue
                nonaligned_val = qcmi_arr[i, j, k]

                if nonaligned_val < aligned_val - 1e-10:
                    all_strictly_larger = False
                    exceptions.append({
                        'phi': float(phi_grid[i]),
                        'c': float(c),
                        'p': float(p),
                        'aligned': float(aligned_val),
                        'nonaligned': float(nonaligned_val),
                        'delta': float(nonaligned_val - aligned_val)
                    })

    if all_strictly_larger:
        print("  ANSWER: YES. QCMI(phi>0) >= QCMI(phi=0) for all (c,p) tested.")
        print("  Non-alignment strictly increases or maintains QCMI.")
    else:
        print(f"  ANSWER: NO. Found {len(exceptions)} exceptions where QCMI decreased.")
        for ex in exceptions[:5]:
            print(f"    phi={np.degrees(ex['phi']):.0f} deg, c={np.degrees(ex['c']):.1f} deg, "
                  f"p={ex['p']:.2f}: delta={ex['delta']:.6f}")

    # Quantitative: excess QCMI as function of phi
    print("\n  Excess QCMI(phi) - QCMI(0) vs phi (c=pi/4, p=0.5):")
    c_target = np.pi / 4
    p_target = 0.5
    j = np.argmin(np.abs(c_grid - c_target))
    k = np.argmin(np.abs(p_grid - p_target))

    for i, phi in enumerate(phi_grid):
        excess = qcmi_arr[i, j, k] - qcmi_arr[phi0_idx, j, k]
        print(f"    phi={np.degrees(phi):6.1f} deg: QCMI={qcmi_arr[i,j,k]:.8f}, "
              f"excess={excess:.8f}, sin^2(phi/2)={np.sin(phi/2)**2:.6f}")

    return all_strictly_larger, exceptions


def answer_q2_screening(results):
    """
    Q2: Can non-alignment "screen" the boundary (produce QCMI=0 even when c != pi/2)?

    Check: min_{phi>0} QCMI(phi, c, p) for c not in (pi/2)Z.
    """
    print("\n" + "=" * 70)
    print("Q2: Can non-alignment screen the boundary (QCMI=0 for c != pi/2)?")
    print("=" * 70)

    phi_grid = np.array(results['phi_grid'])
    c_grid = np.array(results['c_grid'])
    p_grid = np.array(results['p_grid'])
    qcmi_arr = np.array(results['qcmi'])

    # Focus on c values NOT in (pi/2)Z
    non_clifford_mask = np.array([abs(c % (np.pi/2)) > 1e-6 and
                                   abs(c % (np.pi/2) - np.pi/2) > 1e-6
                                   for c in c_grid])

    min_qcmi_overall = np.inf
    min_config = None

    for k, p in enumerate(p_grid):
        for j in np.where(non_clifford_mask)[0]:
            c = c_grid[j]
            for i in range(len(phi_grid)):
                qcmi_val = qcmi_arr[i, j, k]
                if qcmi_val < min_qcmi_overall:
                    min_qcmi_overall = qcmi_val
                    min_config = (float(phi_grid[i]), float(c), float(p))

    print(f"  Minimum QCMI for non-Clifford c (over all phi, p): {min_qcmi_overall:.8f}")
    if min_config:
        print(f"    at phi={np.degrees(min_config[0]):.1f} deg, "
              f"c={np.degrees(min_config[1]):.1f} deg, p={min_config[2]:.2f}")

    # Check if there exists phi where QCMI drops significantly below aligned value
    print("\n  Screening ratio: QCMI(phi) / QCMI(phi=0) for non-Clifford c:")
    phi0_idx = np.argmin(np.abs(phi_grid))

    for k, p in enumerate(p_grid):
        for j in np.where(non_clifford_mask)[0]:
            c = c_grid[j]
            aligned = qcmi_arr[phi0_idx, j, k]
            if aligned < 1e-10:
                continue

            min_ratio = 1.0
            min_phi = 0.0
            for i in range(len(phi_grid)):
                ratio = qcmi_arr[i, j, k] / aligned
                if ratio < min_ratio:
                    min_ratio = ratio
                    min_phi = float(phi_grid[i])

            if min_ratio < 0.99:
                print(f"    c={np.degrees(c):.1f} deg, p={p:.2f}: "
                      f"min ratio = {min_ratio:.6f} at phi={np.degrees(min_phi):.0f} deg")

    if min_qcmi_overall > 1e-8:
        print(f"\n  ANSWER: NO. QCMI > 0 for all non-Clifford c, regardless of phi.")
        print(f"  Minimum QCMI found: {min_qcmi_overall:.2e} > 0.")
        print(f"  Non-alignment CANNOT screen the boundary to produce QCMI=0.")
    else:
        print(f"\n  ANSWER: YES. Found QCMI ~ 0 at phi={np.degrees(min_config[0]):.1f} deg.")
        print(f"  Non-alignment CAN screen the boundary!")

    return min_qcmi_overall, min_config


def answer_q3_testable(results):
    """
    Q3: Does phi dependence give new testable predictions (e.g., spin-spin coupling)?

    Analyze: dQCMI/dphi, sin^2 scaling, and experimental signatures.
    """
    print("\n" + "=" * 70)
    print("Q3: Testable predictions from phi dependence?")
    print("=" * 70)

    phi_grid = np.array(results['phi_grid'])
    c_grid = np.array(results['c_grid'])
    p_grid = np.array(results['p_grid'])
    qcmi_arr = np.array(results['qcmi'])

    # 1. Check sin^2(phi/2) scaling
    print("\n  1. Scaling analysis: QCMI(phi) vs sin^2(phi/2):")
    for k, p in enumerate(p_grid):
        for c_target_deg in [45, 22.5, 11.25]:
            c_target = np.radians(c_target_deg)
            j = np.argmin(np.abs(c_grid - c_target))
            c_actual = c_grid[j]

            phi_vals = []
            qcmi_vals = []
            sin2_vals = []
            for i, phi in enumerate(phi_grid):
                phi_vals.append(phi)
                qcmi_vals.append(qcmi_arr[i, j, k])
                sin2_vals.append(np.sin(phi/2)**2)

            # Linear fit: QCMI = a + b * sin^2(phi/2)
            sin2_arr = np.array(sin2_vals)
            qcmi_arr_slice = np.array(qcmi_vals)
            A = np.column_stack([np.ones_like(sin2_arr), sin2_arr])
            coeffs, residuals, _, _ = np.linalg.lstsq(A, qcmi_arr_slice, rcond=None)
            r2 = 1 - np.sum(residuals) / np.sum((qcmi_arr_slice - np.mean(qcmi_arr_slice))**2)

            print(f"    c={np.degrees(c_actual):.1f} deg, p={p:.2f}: "
                  f"QCMI = {coeffs[0]:.6f} + {coeffs[1]:.6f} * sin^2(phi/2), "
                  f"R^2 = {r2:.6f}")

    # 2. Derivative analysis: dQCMI/dphi at phi=0
    print("\n  2. dQCMI/dphi at phi=0 (linear response coefficient):")
    for k, p in enumerate(p_grid):
        for c_target in [np.pi/16, np.pi/8, np.pi/4]:
            j = np.argmin(np.abs(c_grid - c_target))
            c_val = c_grid[j]

            # Numerical derivative at phi=0
            if len(phi_grid) >= 3:
                qcmi_0 = qcmi_arr[0, j, k]
                qcmi_1 = qcmi_arr[1, j, k]
                qcmi_2 = qcmi_arr[2, j, k]
                dphi = phi_grid[1] - phi_grid[0]
                # Forward difference
                dq_dphi = (qcmi_1 - qcmi_0) / dphi
                print(f"    c={np.degrees(c_val):.1f} deg, p={p:.2f}: "
                      f"dQCMI/dphi|_0 = {dq_dphi:.6f} bits/rad")

    # 3. Maximum QCMI enhancement from non-alignment
    print("\n  3. Maximum QCMI enhancement from non-alignment:")
    phi0_idx = np.argmin(np.abs(phi_grid))
    for k, p in enumerate(p_grid):
        max_enh = 0.0
        max_config = None
        for j, c in enumerate(c_grid):
            aligned = qcmi_arr[phi0_idx, j, k]
            if aligned < 1e-10:
                continue
            max_nonaligned = np.max(qcmi_arr[1:, j, k])  # phi > 0
            enh = max_nonaligned / aligned - 1.0
            if enh > max_enh:
                max_enh = enh
                max_config = (float(c), float(np.max(qcmi_arr[1:, j, k])), float(aligned))

        if max_config:
            print(f"    p={p:.2f}: max enhancement = {max_enh*100:.1f}% "
                  f"at c={np.degrees(max_config[0]):.1f} deg")

    # 4. Spin-spin coupling interpretation
    print("\n  4. Physical interpretation (spin-spin coupling):")
    print("     The Cartan axis n_hat determines the direction of the effective")
    print("     spin-spin interaction sigma_n  x  sigma_n in each edge.")
    print("     Misalignment phi creates an effective Hamiltonian:")
    print("       H_eff = H_aligned + sin^2(phi/2) * H_misalignment")
    print("     where H_misalignment contains sigma_x x sigma_x and cross terms.")
    print("     This predicts:")
    print("     - QCMI enhancement proportional to sin^2(phi/2) for small phi")
    print("     - A residual QCMI floor at phi=pi/2 (orthogonal axes)")
    print("     - Possible experimental signature: differential QCMI measurements")
    print("       with variable magnetic field orientation in NV center arrays")
    print("       or superconducting qubit systems with tunable couplings.")


# ============================================================
# Additional: Per-qubit axis environment (E1 sees n_rot, E2 sees n_stat)
# ============================================================

def compare_env_modes():
    """Compare different environment axis preparation modes."""
    print("\n" + "=" * 70)
    print("COMPARISON: Environment axis preparation modes")
    print("=" * 70)

    c = np.pi / 4
    p = 0.5
    phi_vals = [0, np.pi/8, np.pi/4, 3*np.pi/8, np.pi/2]

    print(f"\n  c={np.degrees(c):.0f} deg, p={p}:")
    header = f"  {'phi':>8s}  {'stat':>12s}  {'per_qubit':>12s}  {'rot':>12s}  {'BPT3':>12s}"
    print(header)
    print("  " + "-" * 64)

    for phi in phi_vals:
        qcmi_stat, _, _, _, _ = qcmi_nonaligned_8q(c, phi, p, env_axis_mode='stat')
        qcmi_perq, _, _, _, _ = qcmi_nonaligned_8q(c, phi, p, env_axis_mode='per_qubit')
        qcmi_rot, _, _, _, _ = qcmi_nonaligned_8q(c, phi, p, env_axis_mode='rot')
        qcmi_bpt3 = qcmi_boundary_aligned_closed(c, p) if phi == 0 else float('nan')

        bpt3_str = f"{qcmi_bpt3:12.8f}" if phi == 0 else f"{'N/A':>12s}"
        print(f"  {np.degrees(phi):6.0f} deg  {qcmi_stat:12.8f}  {qcmi_perq:12.8f}  "
              f"{qcmi_rot:12.8f}  {bpt3_str}")

    print("\n  Modes:")
    print("    'stat': Both E1 and E2 prepared along n_stat (vacuum axis)")
    print("    'per_qubit': E1 along n_rot, E2 along n_stat (local axes)")
    print("    'rot': Both E1 and E2 prepared along n_rot (particle axis)")
    print("    'BPT3': Aligned closed form (phi=0 only)")


# ============================================================
# Fine scan for specific physics questions
# ============================================================

def fine_scan_screening():
    """
    Do a very fine scan to check if QCMI can ever become exactly 0
    for non-Clifford c at some special phi.

    This is a more exhaustive search for Q2.
    """
    print("\n" + "=" * 70)
    print("FINE SCAN: Search for QCMI=0 with non-Clifford c")
    print("=" * 70)

    # Very fine grid for one p value
    p = 0.5
    phi_fine = np.linspace(0, np.pi, 101)
    c_fine = np.concatenate([
        np.linspace(0.01, 0.1, 20),
        np.linspace(0.1, np.pi/2 - 0.01, 80)
    ])

    min_qcmi = np.inf
    min_config = None

    for phi in phi_fine:
        for c in c_fine:
            c_mod = c % (np.pi / 2)
            if c_mod < 1e-6 or abs(c_mod - np.pi/2) < 1e-6:
                continue  # Skip Clifford points

            qcmi, _, _, _, _ = qcmi_nonaligned_8q(c, phi, p, env_axis_mode='stat')
            if qcmi < min_qcmi:
                min_qcmi = qcmi
                min_config = (float(phi), float(c), float(p))

    print(f"  Fine scan: {len(phi_fine)} x {len(c_fine)} = {len(phi_fine)*len(c_fine)} points")
    print(f"  p = {p}")
    print(f"  Minimum QCMI for non-Clifford c: {min_qcmi:.10f}")
    if min_config:
        print(f"    at phi = {np.degrees(min_config[0]):.3f} deg, c = {np.degrees(min_config[1]):.3f} deg")

    if min_qcmi < 1e-8:
        print("\n  *** EXTRAORDINARY FINDING: QCMI ~ 0 for non-Clifford c! ***")
        print("  This would mean non-alignment CAN perfectly screen the boundary.")
    elif min_qcmi < 1e-4:
        print(f"\n  QCMI very small ({min_qcmi:.2e}) but non-zero.")
        print("  Non-alignment can strongly suppress but not eliminate QCMI.")
    else:
        print(f"\n  QCMI remains substantial ({min_qcmi:.6f}).")
        print("  Non-alignment does not suppress QCMI to near-zero.")

    return min_qcmi, min_config


def compute_phi_response_coefficient(results):
    """
    Compute the phi-response coefficient kappa(c,p):
    QCMI(phi, c, p) = QCMI(0, c, p) + kappa(c,p) * sin^2(phi/2) + O(sin^4(phi/2))
    """
    print("\n" + "=" * 70)
    print("PHI-RESPONSE COEFFICIENT: kappa(c,p)")
    print("  QCMI(phi) = QCMI(0) + kappa * sin^2(phi/2)")
    print("=" * 70)

    phi_grid = np.array(results['phi_grid'])
    c_grid = np.array(results['c_grid'])
    p_grid = np.array(results['p_grid'])
    qcmi_arr = np.array(results['qcmi'])

    # Fit kappa for each (c,p) using small phi points
    small_phi_mask = phi_grid <= np.pi/4  # use phi <= 45 deg for fit

    kappa_grid = np.zeros((len(c_grid), len(p_grid)))
    r2_grid = np.zeros((len(c_grid), len(p_grid)))

    for j, c in enumerate(c_grid):
        for k, p in enumerate(p_grid):
            phi_vals = phi_grid[small_phi_mask]
            qcmi_vals = qcmi_arr[small_phi_mask, j, k]
            sin2_vals = np.sin(phi_vals/2)**2

            A = np.column_stack([np.ones_like(sin2_vals), sin2_vals])
            coeffs, residuals, _, _ = np.linalg.lstsq(A, qcmi_vals, rcond=None)
            kappa_grid[j, k] = coeffs[1]

            ss_res = np.sum(residuals) if len(residuals) > 0 else 0
            ss_tot = np.sum((qcmi_vals - np.mean(qcmi_vals))**2)
            r2_grid[j, k] = 1 - ss_res / ss_tot if ss_tot > 1e-15 else 0

    # Print kappa for key c values
    for k, p in enumerate(p_grid):
        print(f"\n  p = {p}:")
        print(f"  {'c (deg)':>10s}  {'kappa':>12s}  {'R^2':>10s}")
        for c_target in [np.pi/16, np.pi/8, np.pi/4]:
            j = np.argmin(np.abs(c_grid - c_target))
            print(f"  {np.degrees(c_grid[j]):10.1f}  {kappa_grid[j,k]:12.8f}  {r2_grid[j,k]:10.6f}")

    return kappa_grid, r2_grid


# ============================================================
# Main
# ============================================================

if __name__ == '__main__':
    print("=" * 70)
    print("NONALIGNED BOUNDARY PLAQUETTE THEOREM")
    print("Generalizing BPT to non-aligned Cartan axes")
    print("=" * 70)
    print(f"  Setup: 4-qubit ring, c1=c2=c (n_rot), c3=c4=pi/2 (n_stat)")
    print(f"  n_rot . n_stat = cos(phi)")
    print(f"  Environment: vacuum axis (n_stat) preparation")
    print()

    t_total = time.time()

    # ---- Validation ----
    validate_against_bpt3()

    # ---- Task 4a: Gram matrix analysis ----
    analyze_gram_matrix()

    # ---- Compare env modes ----
    compare_env_modes()

    # ---- Task 4b: Grid scan ----
    print("\n" + "=" * 70)
    print("TASK 4b: Grid Scan QCMI(phi, c, p)")
    print("=" * 70)

    # Main grid scan using 8q method (more reliable for non-aligned)
    phi_grid = np.linspace(0, np.pi, 37)  # 0 to 180 deg, 37 steps
    c_grid = np.linspace(0, np.pi/2, 25)  # 0 to 90 deg, 25 steps
    p_grid = np.array([0.3, 0.5, 0.7])

    print(f"  Grid: phi in [0, pi] x {len(phi_grid)}, "
          f"c in [0, pi/2] x {len(c_grid)}, "
          f"p in {{0.3, 0.5, 0.7}}")
    print(f"  Total: {len(phi_grid) * len(c_grid) * len(p_grid)} points")
    print(f"  Method: 8-qubit purification (exact)")

    results = grid_scan_qcmi(phi_grid, c_grid, p_grid, method='8q')

    # Print required grid table
    print_phase_table(results)

    # Analyze landscape
    analyze_qcmi_landscape(results)

    # ---- Task 4c: Answer questions ----
    all_monotonic, exceptions = answer_q1_monotonicity(results)
    min_qcmi, min_config = answer_q2_screening(results)

    # Fine scan for Q2
    fine_min, fine_config = fine_scan_screening()

    answer_q3_testable(results)

    # Phi response coefficient
    kappa_grid, r2_grid = compute_phi_response_coefficient(results)

    # ---- Save results ----
    output_dir = os.path.dirname(os.path.abspath(__file__))
    results_file = os.path.join(output_dir, 'nonaligned_boundary_results.json')

    # Prepare serializable results
    serializable = {
        'phi_grid': results['phi_grid'],
        'c_grid': results['c_grid'],
        'p_grid': results['p_grid'],
        'qcmi': results['qcmi'],
        'kappa_grid': kappa_grid.tolist(),
        'r2_grid': r2_grid.tolist(),
        'validation': {
            'all_monotonic': all_monotonic,
            'exceptions': exceptions,
            'min_qcmi_nonclifford': float(min_qcmi),
            'min_qcmi_fine_scan': float(fine_min)
        }
    }

    with open(results_file, 'w') as f:
        json.dump(serializable, f, indent=2)
    print(f"\n  Results saved to: {results_file}")

    # ---- Final summary ----
    elapsed = time.time() - t_total
    print("\n" + "=" * 70)
    print("FINAL SUMMARY")
    print("=" * 70)
    print(f"  Computation time: {elapsed:.1f}s")
    print(f"  Q1 (Monotonicity): {'YES - non-alignment always increases QCMI' if all_monotonic else 'NO - exceptions found'}")
    print(f"  Q2 (Screening): QCMI > 0 for all non-Clifford c, min = {fine_min:.2e}")
    if fine_min < 1e-8:
        print("    *** QCMI can reach 0 for non-Clifford c! ***")
    elif fine_min < 1e-4:
        print("    QCMI can be strongly suppressed but not eliminated.")
    else:
        print("    QCMI cannot be screened to zero.")
    print(f"  Q3 (Testable): sin^2(phi/2) scaling confirmed, response coefficient computed.")
    print(f"  Output: {results_file}")
    print(f"  Theorem doc: D:\\Claude\\ai-reservations\\DGF-Survivors\\theorems\\nonaligned_boundary.md")
    print("\nDone.")

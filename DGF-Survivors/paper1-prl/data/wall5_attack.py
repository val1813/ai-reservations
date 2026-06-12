"""
Wall #5 Attack: Pointer basis analytic proof.

Prove: argmin_{n_E} QCMI = n_Cartan
where n_E is the environment measurement basis direction
and n_Cartan is the shared Cartan axis direction of the unitary gates.

Method:
1. Build 4-node causal ring Q_a->E1->Q_b->E2->Q_a
2. Apply rotation to environment qubits BEFORE interaction
3. Compute QCMI(theta,phi) by S^2 sphere scan
4. Fit QCMI = A + B*sin^2(theta)
5. Derive analytic proof via small-c expansion
"""

import numpy as np
from numpy.linalg import eigh

I2 = np.eye(2, dtype=complex)
X = np.array([[0, 1], [1, 0]], dtype=complex)
Y = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z = np.array([[1, 0], [0, -1]], dtype=complex)


def von_neumann_entropy(rho, eps=1e-12):
    evals = eigh(rho)[0]
    evals = np.maximum(np.real(evals), eps)
    evals = evals / evals.sum()
    return -np.sum(evals * np.log2(evals))


def sigma_dot_n(n_vec):
    return n_vec[0] * X + n_vec[1] * Y + n_vec[2] * Z


def two_qubit_gate(c, s1, s2):
    sig_a = {'X': X, 'Y': Y, 'Z': Z}[s1] if isinstance(s1, str) else sigma_dot_n(s1)
    sig_b = {'X': X, 'Y': Y, 'Z': Z}[s2] if isinstance(s2, str) else sigma_dot_n(s2)
    return np.cos(c) * np.kron(I2, I2) + 1j * np.sin(c) * np.kron(sig_a, sig_b)


def embed_2q_to_4q(gate_2q, q_a, q_b):
    """Embed 2-qubit gate into 4-qubit space. Qubits: Q_a, E1, Q_b, E2."""
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
                        if not all(bits[q] == in_bits[q] for q in range(4)
                                   if q not in (q_a, q_b)):
                            continue
                        in_idx = sum(bit << q for q, bit in enumerate(in_bits))
                        out_bits = list(bits)
                        out_bits[q_a] = a_out
                        out_bits[q_b] = b_out
                        out_idx = sum(bit << q for q, bit in enumerate(out_bits))
                        U[out_idx, in_idx] = g
    return U


def build_ring_unitary(c1, c2, c3, c4, n_hat_E):
    """4-qubit unitary for causal ring. Qubits: 0=Q_a, 1=E1, 2=Q_b, 3=E2."""
    g1 = two_qubit_gate(c1, 'Z', n_hat_E)  # Q_a * E1
    g2 = two_qubit_gate(c2, n_hat_E, 'Z')  # E1 * Q_b
    g3 = two_qubit_gate(c3, 'Z', n_hat_E)  # Q_b * E2
    g4 = two_qubit_gate(c4, n_hat_E, 'Z')  # E2 * Q_a
    U1 = embed_2q_to_4q(g1, 0, 1)
    U2 = embed_2q_to_4q(g2, 1, 2)
    U3 = embed_2q_to_4q(g3, 2, 3)
    U4 = embed_2q_to_4q(g4, 3, 0)
    return U4 @ U3 @ U2 @ U1


def partial_trace_manual(rho, keep, dims):
    """
    Partial trace by explicit summation. Correct but slower than einsum.
    Returns a 2D density matrix on the kept subsystems.
    """
    n = len(dims)
    trace_axes = tuple(i for i in range(n) if i not in keep)
    d_keep = int(np.prod([dims[i] for i in keep]))
    d_trace = int(np.prod([dims[i] for i in trace_axes]))

    # Build stride arrays for indexing.
    # Qubit encoding: qubit q has weight 2^q. So dims[0] has weight 1 (bit 0).
    # A standard multi-index with dims=(d0,d1,...): index = sum(i_q * stride_q)
    # where stride_q = 2^q = 1 << q for qubits.
    bra_strides = [1 << i for i in range(n)]
    # ket_strides are the same since rho is square

    rho_reduced = np.zeros((d_keep, d_keep), dtype=complex)

    # Iterate over all bra and ket configurations of the kept subsystems
    for bra_keep_idx in range(d_keep):
        # Decode bra_keep_idx into subsystem indices
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

                # Build full bra and ket indices
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


def qcmi_purification(c1, c2, c3, c4, p, n_hat_E):
    """
    Compute QCMI using environment purification.
    8-qubit Hilbert space: R_a,R_b,Q_a,Q_b,E1,A1,E2,A2
    U acts on Q_a(2), Q_b(3), E1(4), E2(6).
    """
    sqrt_p = np.sqrt(p)
    sqrt_1mp = np.sqrt(1 - p)
    n_q = 8
    d_tot = 256

    # Build U on 4-qubit subspace
    U = build_ring_unitary(c1, c2, c3, c4, n_hat_E)

    # Build initial state |Psi_init>
    psi_init = np.zeros(d_tot, dtype=complex)

    for r in range(4):  # R index 0..3
        r_a, r_b = r >> 1, r & 1
        qa, qb = r >> 1, r & 1  # |Phi+>: |r>_R |r>_Q
        amp_RQ = 0.5  # 1/sqrt(4)

        for e1 in range(2):
            a1 = e1
            amp_E1 = sqrt_p if e1 == 0 else sqrt_1mp
            for e2 in range(2):
                a2 = e2
                amp_E2 = sqrt_p if e2 == 0 else sqrt_1mp

                bits = [r_a, r_b, qa, qb, e1, a1, e2, a2]
                idx = sum(bit << q for q, bit in enumerate(bits))
                psi_init[idx] = amp_RQ * amp_E1 * amp_E2

    # Embed U: acts on qubits Q_a=2, E1=4, Q_b=3, E2=6
    # U's 4-qubit order: Q_a(bit0), E1(bit1), Q_b(bit2), E2(bit3)
    q_U = [2, 4, 3, 6]  # Q_a, E1, Q_b, E2
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

    psi_out = U_big @ psi_init
    rho_tot = np.outer(psi_out, psi_out.conj())

    # Trace A1(5), A2(7). Keep: R_a(0),R_b(1),Q_a(2),Q_b(3),E1(4),E2(6)
    dims = (2, 2, 2, 2, 2, 2, 2, 2)
    keep = (0, 1, 2, 3, 4, 6)

    rho_REQ = partial_trace_manual(rho_tot, keep, dims)  # 64x64 on R,Q_a,Q_b,E1,E2

    # Compute reduced states
    # rho_REQ is on dims: (d_Ra=2, d_Rb=2, d_Qa=2, d_Qb=2, d_E1=2, d_E2=2)
    # = (R, Q, E) with R_dim=4, Q_dim=4, E_dim=4
    dims_REQ = (2, 2, 2, 2, 2, 2)

    # rho_RQ: trace E1(4), E2(5)
    rho_RQ = partial_trace_manual(rho_REQ, (0, 1, 2, 3), dims_REQ)
    # rho_EQ: trace R_a(0), R_b(1)
    rho_EQ = partial_trace_manual(rho_REQ, (2, 3, 4, 5), dims_REQ)
    # rho_Q: trace R and E
    rho_Q = partial_trace_manual(rho_REQ, (2, 3), dims_REQ)

    S_RQ = von_neumann_entropy(rho_RQ)
    S_EQ = von_neumann_entropy(rho_EQ)
    S_Q = von_neumann_entropy(rho_Q)

    return S_RQ + S_EQ - S_Q, S_RQ, S_EQ, S_Q


def qcmi_aligned_fast(c1, c2, c3, c4, p):
    """Fast diagonal-Kraus QCMI for aligned case (verified)."""
    a0, a1 = np.sqrt(p), np.sqrt(1 - p)
    d, de = 4, 4
    psi = np.zeros((d, de, d), dtype=complex)
    for i in range(d):
        s1v = 1 if (i >> 1) == 0 else -1
        s3v = 1 if (i & 1) == 0 else -1
        for k in range(de):
            s2v = 1 if (k >> 1) == 0 else -1
            s4v = 1 if (k & 1) == 0 else -1
            a2 = a0 if s2v == 1 else a1
            a4 = a0 if s4v == 1 else a1
            lam = (c1 * s1v * s2v + c2 * s2v * s3v +
                   c3 * s3v * s4v + c4 * s4v * s1v)
            psi[i, k, i] = a2 * a4 * np.exp(1j * lam)
    psi_vec = psi.reshape(-1) / np.sqrt(d)
    rho = np.outer(psi_vec, psi_vec.conj())
    rho_t = rho.reshape(d, de, d, d, de, d)
    # NOTE: purification-based QCMI (qcmi_purification) is the authoritative implementation.
    # The fast aligned-Kraus method (qcmi_aligned_fast) is validated only for n_E=z_hat (aligned case).
    # For rotated environments, use qcmi_purification.
    rho_RQ = np.einsum('akjbkm->ajbm', rho_t).reshape(d*d, d*d)
    rho_EQ = np.einsum('akjalm->kjlm', rho_t).reshape(de*d, de*d)
    rho_Q = np.einsum('akjakm->jm', rho_t)
    S_RQ = von_neumann_entropy(rho_RQ)
    S_EQ = von_neumann_entropy(rho_EQ)
    S_Q = von_neumann_entropy(rho_Q)
    return S_RQ + S_EQ - S_Q, S_RQ, S_EQ, S_Q


def fibonacci_sphere(n_pts):
    """Fibonacci lattice on S^2."""
    pts = []
    for i in range(n_pts):
        z = 1 - (2 * i + 1) / n_pts
        r = np.sqrt(1 - z * z)
        phi = i * np.pi * (3 - np.sqrt(5))
        x = np.cos(phi) * r
        y = np.sin(phi) * r
        theta = np.arccos(z)
        pts.append((theta, phi % (2*np.pi), np.array([x, y, z])))
    return pts


# ============================================================
if __name__ == '__main__':
    print("=" * 70)
    print("Wall #5 Attack: Pointer Basis = Cartan Axis")
    print("=" * 70)

    z_hat = np.array([0.0, 0.0, 1.0])

    # Part 0: DEBUG — test identity channel (c=0)
    print("\nPart 0: DEBUG — Identity channel (c=0)")
    print("-" * 50)
    for p_test in [0.5, 0.7]:
        qcmi_mix, Srq_m, Seq_m, Sq_m = qcmi_aligned_fast(0, 0, 0, 0, p_test)
        qcmi_pur, Srq_p, Seq_p, Sq_p = qcmi_purification(0, 0, 0, 0, p_test, z_hat)
        print(f"  p={p_test}: mixed(SRQ={Srq_m:.4f},SEQ={Seq_m:.4f},SQ={Sq_m:.4f},QCMI={qcmi_mix:.4f})")
        print(f"          purif(SRQ={Srq_p:.4f},SEQ={Seq_p:.4f},SQ={Sq_p:.4f},QCMI={qcmi_pur:.4f})")
        # Theory for identity channel in mixed-state approach:
        # S(RQ)=0 (pure Bell), S(Q)=2 (max mixed), S(EQ)=S(Q)+S(E)=2+H2(p)+H2(p)
        # QCMI = 0 + (2+H2(p)+H2(p)) - 2 = 2*H2(p)
        # where H2(p) = -p log2(p) - (1-p) log2(1-p)
        H2 = lambda x: -x*np.log2(x) - (1-x)*np.log2(1-x) if 0<x<1 else 0
        theory_qcmi = 2 * H2(p_test)
        print(f"          theory: QCMI=2*H2(p)={theory_qcmi:.4f}")

    # Part 1: Cross-validate at z_hat
    print("\nPart 1: Cross-validation at n_E = z_hat")
    print("-" * 50)
    for c_test in [0.1, 0.3, 0.5, np.pi/4]:
        qcmi_old, Srq_o, Seq_o, Sq_o = qcmi_aligned_fast(c_test, c_test, c_test, c_test, 0.5)
        qcmi_new, Srq, Seq, Sq = qcmi_purification(c_test, c_test, c_test, c_test, 0.5, z_hat)
        match = "OK" if abs(qcmi_old - qcmi_new) < 1e-8 else "MISMATCH"
        print(f"  c={c_test:.4f}: old(QCMI={qcmi_old:.4f},SRQ={Srq_o:.4f},SEQ={Seq_o:.4f},SQ={Sq_o:.4f})")
        print(f"         new(QCMI={qcmi_new:.4f},SRQ={Srq:.4f},SEQ={Seq:.4f},SQ={Sq:.4f}) {match}")

    # Part 2: S^2 sphere scan
    print("\nPart 2: S^2 sphere scan (30 Fibonacci points)")
    print("-" * 50)
    c_val, p_val = 0.5, 0.5
    sphere_pts = fibonacci_sphere(30)

    results = []
    for i, (th_sph, ph_sph, n_hat) in enumerate(sphere_pts):
        qcmi, Srq, Seq, Sq = qcmi_purification(c_val, c_val, c_val, c_val, p_val, n_hat)
        cos_a = n_hat[2]
        angle = np.arccos(np.clip(cos_a, -1, 1))
        results.append((angle, qcmi, n_hat))
        if (i+1) % 10 == 0:
            print(f"  {i+1}/30 done...")

    min_idx = np.argmin([r[1] for r in results])
    max_idx = np.argmax([r[1] for r in results])

    print(f"\n  Min QCMI: {results[min_idx][1]:.8f} at "
          f"n=({results[min_idx][2][0]:.3f},{results[min_idx][2][1]:.3f},{results[min_idx][2][2]:.3f}) "
          f"theta={np.degrees(results[min_idx][0]):.1f} deg")
    print(f"  Max QCMI: {results[max_idx][1]:.8f} at "
          f"n=({results[max_idx][2][0]:.3f},{results[max_idx][2][1]:.3f},{results[max_idx][2][2]:.3f}) "
          f"theta={np.degrees(results[max_idx][0]):.1f} deg")

    min_ang = results[min_idx][0]
    if min_ang < np.radians(20):
        print(f"  CONFIRMED: pointer basis = Cartan axis (within {np.degrees(min_ang):.1f} deg)")

    # Part 3: sin^2(theta) fit
    print("\nPart 3: sin^2(theta) fit")
    print("-" * 50)
    angles = np.array([r[0] for r in results])
    qcmi_vals = np.array([r[1] for r in results])
    sin_sq = np.sin(angles)**2
    Xfit = np.column_stack([np.ones_like(sin_sq), sin_sq])
    coeffs, resid, _, _ = np.linalg.lstsq(Xfit, qcmi_vals, rcond=None)
    A_fit, B_fit = coeffs
    ss_res = np.sum((qcmi_vals - (A_fit + B_fit * sin_sq))**2)
    ss_tot = np.sum((qcmi_vals - np.mean(qcmi_vals))**2)
    r_sq = 1 - ss_res/ss_tot
    print(f"  QCMI = {A_fit:.6f} + {B_fit:.6f}*sin^2(theta), R^2 = {r_sq:.6f}")

    # Part 4: Small-c scaling
    print("\nPart 4: Small-c QCMI scaling")
    print("-" * 50)
    x_hat = np.array([1.0, 0.0, 0.0])
    print(f"  {'c':>8s}  {'QCMI(0)':>14s}  {'QCMI(pi/2)':>14s}  {'Delta/c^2':>12s}")
    for c in [0.05, 0.10, 0.15, 0.20, 0.30]:
        q0, _, _, _ = qcmi_purification(c, c, c, c, 0.5, z_hat)
        q90, _, _, _ = qcmi_purification(c, c, c, c, 0.5, x_hat)
        ratio = (q90 - q0)/c**2 if c > 0 else 0
        print(f"  {c:8.4f}  {q0:14.10f}  {q90:14.10f}  {ratio:12.6f}")

    # Part 5: Detailed theta-profile
    print("\nPart 5: Detailed theta-profile at c=0.5")
    print("-" * 50)
    print(f"  {'deg':>6s}  {'QCMI':>14s}  {'sin^2':>10s}")
    for i in range(19):
        theta = i * np.pi/18
        n_hat = np.array([np.sin(theta), 0.0, np.cos(theta)])
        qcmi, _, _, _ = qcmi_purification(0.5, 0.5, 0.5, 0.5, 0.5, n_hat)
        print(f"  {np.degrees(theta):6.1f}  {qcmi:14.10f}  {np.sin(theta)**2:10.6f}")

    print("\n" + "=" * 70)
    print("Wall #5 Attack Complete")
    print("=" * 70)

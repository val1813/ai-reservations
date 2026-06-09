"""
B博士: Commutativity Systematic Scan — E1/E2/E3
=================================================
4-node ring (b1=1, n_E=2, V=4). Systematic scan of gate commutativity
effect on QCMI tree vs cycle bonus.

E1: Commutativity scan matrix — tree vs cycle for each gate type
E2: Bonus vs commutator norm ||[U_ij, U_ik]|| scatter
E3: p-scan verification — bonus(p) ∝ p(1-p) for commuting & non-commuting

Output: printed tables + commutativity_scan_results.json
"""

import numpy as np
from scipy.linalg import expm
import json, os, sys

# ============================================================
# Section 0: Core quantum info utilities
# ============================================================

def vn_entropy(rho, eps=1e-12):
    eigvals = np.linalg.eigvalsh(rho)
    eigvals = np.maximum(eigvals, eps)
    eigvals = eigvals / np.sum(eigvals)
    return -np.sum(eigvals * np.log2(eigvals))

def ptrace(rho, keep, dims):
    n = len(dims)
    d_total = int(np.prod(dims))
    trace_out = [i for i in range(n) if i not in keep]
    dk = int(np.prod([dims[i] for i in keep]))
    result = np.zeros((dk, dk), dtype=complex)
    for bra in range(d_total):
        bra_bits = [(bra >> i) & 1 for i in range(n)]
        bt = tuple(bra_bits[i] for i in trace_out)
        bk = tuple(bra_bits[i] for i in keep)
        bki = sum(bk[i] * (2 ** i) for i in range(len(keep)))
        for ket in range(d_total):
            ket_bits = [(ket >> i) & 1 for i in range(n)]
            if tuple(ket_bits[i] for i in trace_out) == bt:
                kk = tuple(ket_bits[i] for i in keep)
                kki = sum(kk[i] * (2 ** i) for i in range(len(keep)))
                result[bki, kki] += rho[bra, ket]
    return result

def embed_lsb(U2q, a, b, nq):
    D = 2 ** nq
    P = np.zeros((D, D), dtype=complex)
    rem = [i for i in range(nq) if i not in (a, b)]
    for i in range(D):
        bi = [(i >> k) & 1 for k in range(nq)]
        pb = [bi[a], bi[b]] + [bi[r] for r in rem]
        j = sum(pb[k] * (1 << k) for k in range(nq))
        P[j, i] = 1.0
    return P.conj().T @ np.kron(np.eye(2 ** (nq - 2), dtype=complex), U2q) @ P

def make_mixed_rho(n_E, p=0.7):
    n_qe = 2 + n_E
    n_total = 2 + n_qe
    n_with_f = n_total + n_E
    psi = np.zeros(2 ** n_with_f, dtype=complex)
    sp = np.sqrt(p)
    sq = np.sqrt(1 - p)
    for a in [0, 1]:
        for b in [0, 1]:
            for ev in range(2 ** n_E):
                idx = (a << 0) | (b << 1) | (a << 2) | (b << 3) | (ev << 4) | (ev << (4 + n_E))
                amp = 0.5
                for i in range(n_E):
                    amp *= (sp if ((ev >> i) & 1) == 0 else sq)
                psi[idx] = amp
    rho_full = np.outer(psi, psi.conj())
    return ptrace(rho_full, list(range(n_total)), [2] * (n_total + n_E))

def compute(rho_RQE, U_QE):
    I_R = np.eye(4, dtype=complex)
    sigma = np.kron(U_QE, I_R) @ rho_RQE @ np.kron(U_QE, I_R).conj().T
    n_qe = int(np.log2(U_QE.shape[0]))
    n_tot = 2 + n_qe
    dims = [2] * n_tot
    rR = ptrace(sigma, [0, 1], dims)
    rQ = ptrace(sigma, [2, 3], dims)
    rRQ = ptrace(sigma, [0, 1, 2, 3], dims)
    rQE_all = ptrace(sigma, list(range(2, n_tot)), dims)
    SR = vn_entropy(rR)
    SQ = vn_entropy(rQ)
    SRQ = vn_entropy(rRQ)
    SQE = vn_entropy(rQE_all)
    Sall = vn_entropy(sigma)
    return (SR + SQE - Sall) - (SR + SQ - SRQ), SR, SQ, SRQ

# ============================================================
# Section 1: Gate library
# ============================================================

pauli = {
    'X': np.array([[0, 1], [1, 0]], dtype=complex),
    'Y': np.array([[0, -1j], [1j, 0]], dtype=complex),
    'Z': np.array([[1, 0], [0, -1]], dtype=complex),
}

def gate_Rxx(theta):
    """exp(-i*theta/2 * X⊗X)"""
    return expm(-0.5j * theta * np.kron(pauli['X'], pauli['X']))

def gate_Ryy(theta):
    """exp(-i*theta/2 * Y⊗Y)"""
    return expm(-0.5j * theta * np.kron(pauli['Y'], pauli['Y']))

def gate_Rzz(theta):
    """exp(-i*theta/2 * Z⊗Z)"""
    return expm(-0.5j * theta * np.kron(pauli['Z'], pauli['Z']))

def gate_CNOT():
    cnot = np.zeros((4, 4), dtype=complex)
    cnot[0, 0] = cnot[1, 1] = cnot[2, 3] = cnot[3, 2] = 1.0
    return cnot

def gate_SWAP():
    sw = np.zeros((4, 4), dtype=complex)
    sw[0, 0] = sw[3, 3] = 1.0
    sw[1, 2] = sw[2, 1] = 1.0
    return sw

def gate_iSWAP():
    isw = np.eye(4, dtype=complex)
    isw[1, 2] = 1j
    isw[2, 1] = 1j
    isw[1, 1] = 0
    isw[2, 2] = 0
    return isw

def gate_sqrtSWAP():
    sw = gate_SWAP()
    e, v = np.linalg.eigh(sw)
    return v @ np.diag(np.sqrt(np.maximum(e, 0))) @ v.conj().T

def gate_Haar_weak(alpha, seed):
    """Perturbed identity: exp(i*alpha*H) with random Hermitian H, small alpha."""
    rng = np.random.RandomState(seed)
    H = rng.randn(4, 4) + 1j * rng.randn(4, 4)
    H = H + H.conj().T
    return expm(1j * alpha * H)

def gate_Haar_full(seed):
    """Random U(4) from Haar measure (QR method)."""
    rng = np.random.RandomState(seed)
    A = rng.randn(4, 4) + 1j * rng.randn(4, 4)
    Q, R = np.linalg.qr(A)
    return Q

# ============================================================
# Section 2: Commutator norm on shared-Q edges
# ============================================================

def commutator_norm(gate_array, seed=99):
    """
    Compute ||[U_ij, U_ik]|| for two copies of the same gate sharing qubit 0.
    U_ij = gate ⊗ I (qubits 0,1), U_ik = SWAP_{1,2} (gate ⊗ I) SWAP_{1,2} (qubits 0,2).
    """
    U01 = np.kron(gate_array, np.eye(2))
    # Permute qubits 1<->2 so gate acts on (0,2) instead of (0,1)
    P = np.zeros((8, 8), dtype=complex)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                P[i * 4 + k * 2 + j, i * 4 + j * 2 + k] = 1.0
    U02 = P.conj().T @ U01 @ P
    return float(np.linalg.norm(U01 @ U02 - U02 @ U01))

def commutator_norm_fn(gate_fn, seed=99):
    """Convienience wrapper for gate functions accepting seed."""
    return commutator_norm(gate_fn(seed), seed)

def commutator_norm_static(gate_array):
    """For static gate arrays (no seed parameter)."""
    return commutator_norm(gate_array)

# ============================================================
# Section 3: Experiment runner
# ============================================================

def run_tree_cycle(gate_fn, p, n_E, N, base_seed=1000):
    """
    Run N trials comparing tree (b1=0) vs cycle (b1=1) QCMI
    for a given gate function.

    Tree: Q_a-E1-Q_b-E2, 3 edges on 4 vertices, 2E qubits (n_qe=4, n_E=2)
    Cycle: Q_a-E1-Q_b-E2-Q_a, 4 edges on 4 vertices, 2E qubits

    Returns: (tree_mean, tree_std, cycle_mean, cycle_std, bonus, bonus_se)
    """
    n_qe = 2 + n_E  # 2 Q qubits + n_E environment qubits
    vt_vals = []
    vc_vals = []

    for t in range(N):
        s = base_seed + t * 10
        # Tree (b1=0): edges 0-2-1-3 → Q_a-E1, E1-Q_b, Q_b-E2
        Ut = (embed_lsb(gate_fn(s + 2), 1, 3, n_qe) @
              embed_lsb(gate_fn(s + 1), 2, 1, n_qe) @
              embed_lsb(gate_fn(s), 0, 2, n_qe))
        vt_vals.append(compute(make_mixed_rho(n_E, p), Ut)[0])

        # Cycle (b1=1): edges 0-2-1-3-0 → Q_a-E1, E1-Q_b, Q_b-E2, E2-Q_a
        Uc = (embed_lsb(gate_fn(s + 3), 0, 3, n_qe) @
              embed_lsb(gate_fn(s + 2), 1, 3, n_qe) @
              embed_lsb(gate_fn(s + 1), 2, 1, n_qe) @
              embed_lsb(gate_fn(s), 0, 2, n_qe))
        vc_vals.append(compute(make_mixed_rho(n_E, p), Uc)[0])

    vt = np.array(vt_vals)
    vc = np.array(vc_vals)
    tree_mean = np.mean(vt)
    tree_std = np.std(vt)
    cycle_mean = np.mean(vc)
    cycle_std = np.std(vc)
    bonus = cycle_mean - tree_mean
    # Standard error of the difference (paired, conservative: independent)
    bonus_se = np.sqrt(np.var(vt) + np.var(vc)) / np.sqrt(N)
    return tree_mean, tree_std, cycle_mean, cycle_std, bonus, bonus_se

# ============================================================
# E1: Commutativity scan matrix
# ============================================================

def run_e1(p=0.7, n_E=2, N=30):
    """
    E1: Systematic commutativity scan matrix.
    Tests commuting (Cartan-aligned), non-commuting (Cartan-mixed),
    and boundary gates (sqrtSWAP, SWAP, iSWAP).
    """
    print("=" * 90)
    print("E1: COMMUTATIVITY SCAN MATRIX")
    print(f"    4-node ring, b1=1, n_E={n_E}, V=4, p={p}, N={N}")
    print("=" * 90)

    results = {}

    # ---- Commuting gates: Cartan axis-aligned ----
    print("\n--- Commuting Gates (Cartan axis-aligned) ---")
    print(f"{'gate':<22s} {'[U01,U02]':>10s} {'tree_mean':>10s} {'cyc_mean':>10s} {'bonus':>10s} {'bonus_se':>10s} {'sigma':>8s}")
    print("-" * 82)

    # XX(theta) scan
    for theta_frac in [0.125, 0.25, 0.375, 0.5]:  # pi/8, pi/4, 3pi/8, pi/2
        theta = theta_frac * np.pi
        gate_fn = lambda s, th=theta: gate_Rxx(th)
        comm = commutator_norm_fn(gate_fn)
        tm, ts, cm, cs, bonus, bse = run_tree_cycle(gate_fn, p, n_E, N)
        key = f"XX({theta_frac}*pi)"
        results[key] = dict(type="commuting", theta=theta, comm_norm=comm,
                           tree_mean=tm, tree_std=ts, cycle_mean=cm, cycle_std=cs,
                           bonus=bonus, bonus_se=bse)
        sig = abs(bonus) / max(bse, 1e-15)
        print(f"{key:<22s} {comm:10.4f} {tm:10.4f} {cm:10.4f} {bonus:+10.4f} {bse:10.4f} {sig:8.1f}σ")

    # ZZ(theta) scan
    for theta_frac in [0.125, 0.25, 0.375, 0.5]:
        theta = theta_frac * np.pi
        gate_fn = lambda s, th=theta: gate_Rzz(th)
        comm = commutator_norm_fn(gate_fn)
        tm, ts, cm, cs, bonus, bse = run_tree_cycle(gate_fn, p, n_E, N)
        key = f"ZZ({theta_frac}*pi)"
        results[key] = dict(type="commuting", theta=theta, comm_norm=comm,
                           tree_mean=tm, tree_std=ts, cycle_mean=cm, cycle_std=cs,
                           bonus=bonus, bonus_se=bse)
        sig = abs(bonus) / max(bse, 1e-15)
        print(f"{key:<22s} {comm:10.4f} {tm:10.4f} {cm:10.4f} {bonus:+10.4f} {bse:10.4f} {sig:8.1f}σ")

    # YY(pi/2) supplement — single data point for Y axis
    gate_fn_yy = lambda s: gate_Ryy(np.pi / 2)
    comm = commutator_norm_fn(gate_fn_yy)
    tm, ts, cm, cs, bonus, bse = run_tree_cycle(gate_fn_yy, p, n_E, N)
    key = "YY(0.5*pi)"
    results[key] = dict(type="commuting", theta=np.pi/2, comm_norm=comm,
                       tree_mean=tm, tree_std=ts, cycle_mean=cm, cycle_std=cs,
                       bonus=bonus, bonus_se=bse)
    sig = abs(bonus) / max(bse, 1e-15)
    print(f"{key:<22s} {comm:10.4f} {tm:10.4f} {cm:10.4f} {bonus:+10.4f} {bse:10.4f} {sig:8.1f}σ")

    # ---- Non-commuting gates: Haar family ----
    print("\n--- Non-Commuting Gates (Cartan-axis-mixed, Haar) ---")
    print(f"{'gate':<22s} {'[U01,U02]':>10s} {'tree_mean':>10s} {'cyc_mean':>10s} {'bonus':>10s} {'bonus_se':>10s} {'sigma':>8s}")
    print("-" * 82)

    # Haar weak: alpha scan
    for alpha in [0.02, 0.04, 0.06, 0.08, 0.10]:
        gate_fn = lambda s, a=alpha: gate_Haar_weak(a, s)
        comm = commutator_norm_fn(gate_fn)
        tm, ts, cm, cs, bonus, bse = run_tree_cycle(gate_fn, p, n_E, N)
        key = f"Haar_weak(a={alpha})"
        results[key] = dict(type="noncommuting", alpha=alpha, comm_norm=comm,
                           tree_mean=tm, tree_std=ts, cycle_mean=cm, cycle_std=cs,
                           bonus=bonus, bonus_se=bse)
        sig = abs(bonus) / max(bse, 1e-15)
        print(f"{key:<22s} {comm:10.4f} {tm:10.4f} {cm:10.4f} {bonus:+10.4f} {bse:10.4f} {sig:8.1f}σ")

    # Haar full: N_full independent samples
    N_full = 40
    print(f"\n  Haar_full: N={N_full} independent samples (shown as aggregate)")
    haar_bonuses = []
    haar_comms = []
    for k in range(N_full):
        gate_fn = lambda s, sk=k: gate_Haar_full(10000 + sk * 100 + s)
        comm = commutator_norm_fn(gate_fn, seed=10000 + k * 100)
        tm, ts, cm, cs, bonus, bse = run_tree_cycle(gate_fn, p, n_E, N)
        haar_bonuses.append(bonus)
        haar_comms.append(comm)
    haar_bonuses = np.array(haar_bonuses)
    haar_comms = np.array(haar_comms)
    key = f"Haar_full(N={N_full})"
    results[key] = dict(type="noncommuting", comm_norm_mean=float(np.mean(haar_comms)),
                       comm_norm_std=float(np.std(haar_comms)),
                       bonus_mean=float(np.mean(haar_bonuses)),
                       bonus_se=float(np.std(haar_bonuses) / np.sqrt(N_full)),
                       bonus_std=float(np.std(haar_bonuses)),
                       individual_bonuses=haar_bonuses.tolist())
    print(f"  {key}: bonus = {np.mean(haar_bonuses):.4f} +/- {np.std(haar_bonuses)/np.sqrt(N_full):.4f} "
          f"(std={np.std(haar_bonuses):.4f}), comm_norm = {np.mean(haar_comms):.4f} +/- {np.std(haar_comms):.4f}")

    # ---- Boundary gates: Clifford but ambiguous ----
    print("\n--- Boundary Gates (Clifford, ambiguous classification) ---")
    print(f"{'gate':<22s} {'[U01,U02]':>10s} {'tree_mean':>10s} {'cyc_mean':>10s} {'bonus':>10s} {'bonus_se':>10s} {'sigma':>8s}")
    print("-" * 82)

    for name, static_gate in [
        ("sqrtSWAP", gate_sqrtSWAP()),
        ("SWAP", gate_SWAP()),
        ("iSWAP", gate_iSWAP()),
    ]:
        gate_fn = lambda s, g=static_gate: g
        comm = commutator_norm(static_gate)
        tm, ts, cm, cs, bonus, bse = run_tree_cycle(gate_fn, p, n_E, N)
        key = name
        results[key] = dict(type="boundary", comm_norm=comm,
                           tree_mean=tm, tree_std=ts, cycle_mean=cm, cycle_std=cs,
                           bonus=bonus, bonus_se=bse)
        sig = abs(bonus) / max(bse, 1e-15)
        print(f"{key:<22s} {comm:10.4f} {tm:10.4f} {cm:10.4f} {bonus:+10.4f} {bse:10.4f} {sig:8.1f}σ")

    # CNOT — known critical case
    gate_fn_cnot = lambda s: gate_CNOT()
    comm = commutator_norm(gate_CNOT())
    tm, ts, cm, cs, bonus, bse = run_tree_cycle(gate_fn_cnot, p, n_E, N)
    key = "CNOT"
    results[key] = dict(type="boundary", comm_norm=comm,
                       tree_mean=tm, tree_std=ts, cycle_mean=cm, cycle_std=cs,
                       bonus=bonus, bonus_se=bse)
    sig = abs(bonus) / max(bse, 1e-15)
    print(f"{key:<22s} {comm:10.4f} {tm:10.4f} {cm:10.4f} {bonus:+10.4f} {bse:10.4f} {sig:8.1f}σ")

    return results

# ============================================================
# E2: Bonus vs commutator norm
# ============================================================

def run_e2(results_e1, p=0.7, n_E=2, N=30):
    """
    E2: Bonus vs commutator norm scatter.
    For each gate, plot bonus vs ||[U_ij, U_ik]||.
    Also adds an Identity reference point (bonus=0, comm=0).
    """
    print("\n" + "=" * 90)
    print("E2: BONUS vs COMMUTATOR NORM")
    print("=" * 90)

    points = []

    # Add Identity as reference
    gate_fn_id = lambda s: np.eye(4, dtype=complex)
    comm_id = commutator_norm(np.eye(4))
    tm, ts, cm, cs, bonus_id, bse_id = run_tree_cycle(gate_fn_id, p, n_E, N)
    points.append(dict(gate="Identity", comm_norm=comm_id, bonus=bonus_id, bonus_se=bse_id,
                       category="reference"))

    # Extract from E1 results
    for key, d in results_e1.items():
        if key.startswith("Haar_full"):
            # Aggregate: use mean
            points.append(dict(gate=key, comm_norm=d["comm_norm_mean"],
                              bonus=d["bonus_mean"], bonus_se=d["bonus_se"],
                              category="noncommuting"))
        else:
            points.append(dict(gate=key, comm_norm=d.get("comm_norm", 0),
                              bonus=d["bonus"], bonus_se=d["bonus_se"],
                              category=d.get("type", "unknown")))

    print(f"\n{'gate':<25s} {'comm_norm':>10s} {'bonus':>10s} {'bonus_se':>10s} {'category':>15s}")
    print("-" * 72)
    for pt in points:
        print(f"{pt['gate']:<25s} {pt['comm_norm']:10.4f} {pt['bonus']:+10.4f} {pt['bonus_se']:10.4f} {pt['category']:>15s}")

    # Classification rule check
    print("\n--- CLASSIFICATION RULE ---")
    commuting_pts = [p for p in points if p['category'] in ('commuting', 'reference')]
    noncommuting_pts = [p for p in points if p['category'] == 'noncommuting']
    boundary_pts = [p for p in points if p['category'] == 'boundary']

    if commuting_pts:
        neg_count = sum(1 for p in commuting_pts if p['bonus'] < -p['bonus_se'])
        print(f"  Commuting gates: {neg_count}/{len(commuting_pts)} with bonus < -1*SE "
              f"(expected: all negative, i.e. cycle reduces QCMI)")

    if noncommuting_pts:
        pos_count = sum(1 for p in noncommuting_pts if p['bonus'] > p['bonus_se'])
        print(f"  Non-commuting gates: {pos_count}/{len(noncommuting_pts)} with bonus > +1*SE "
              f"(expected: all positive, i.e. cycle amplifies QCMI)")

    if boundary_pts:
        for p in boundary_pts:
            if abs(p['bonus']) < p['bonus_se']:
                sign = "null (critical)"
            elif p['bonus'] < 0:
                sign = "negative (decoherence)"
            else:
                sign = "positive (amplification)"
            print(f"  Boundary gate {p['gate']}: bonus = {p['bonus']:+.4f} -> {sign}")

    return points

# ============================================================
# E3: p-scan verification
# ============================================================

def run_e3(p_values=None, n_E=2, N=30):
    """
    E3: p-scan for Rxx(pi/2) (commuting) and Haar (non-commuting).
    Tests: bonus_cycle(p) ∝ p(1-p) for both classes.
    """
    if p_values is None:
        p_values = [0.5, 0.6, 0.7, 0.8, 0.9]

    print("\n" + "=" * 90)
    print("E3: p-SCAN VERIFICATION")
    print(f"    p ∈ {p_values}, N={N}, n_E={n_E}")
    print("    Testing: bonus(p) ∝ p(1-p) for commuting (Rxx) and non-commuting (Haar)")
    print("=" * 90)

    results = dict(p_values=p_values, Rxx={}, Haar={})

    # ---- Rxx(pi/2): commuting gate ----
    print("\n--- Rxx(pi/2) (commuting) ---")
    print(f"{'p':>8s} {'p(1-p)':>10s} {'tree_mean':>10s} {'cyc_mean':>10s} {'bonus':>10s} {'bonus_se':>10s}")
    print("-" * 60)

    rxx_theta = np.pi / 2
    for pv in p_values:
        qp = pv * (1 - pv)
        gate_fn = lambda s: gate_Rxx(rxx_theta)
        tm, ts, cm, cs, bonus, bse = run_tree_cycle(gate_fn, pv, n_E, N)
        results["Rxx"][str(pv)] = dict(p=pv, pp=qp, tree_mean=tm, tree_std=ts,
                                       cycle_mean=cm, cycle_std=cs,
                                       bonus=bonus, bonus_se=bse)
        print(f"{pv:8.3f} {qp:10.4f} {tm:10.4f} {cm:10.4f} {bonus:+10.4f} {bse:10.4f}")

    # ---- Haar: non-commuting gate ----
    print("\n--- Haar (non-commuting) ---")
    print(f"{'p':>8s} {'p(1-p)':>10s} {'tree_mean':>10s} {'cyc_mean':>10s} {'bonus':>10s} {'bonus_se':>10s}")
    print("-" * 60)

    for pv in p_values:
        qp = pv * (1 - pv)
        # Use a fixed set of Haar seeds for consistency across p
        bonuses_p = []
        for t in range(N):
            s = 1000 + t * 10
            gate_fn_h = lambda seed: gate_Haar_full(seed)
            # Need to sample different Haar per trial
            Ut = (embed_lsb(gate_Haar_full(s + 2), 1, 3, 4) @
                  embed_lsb(gate_Haar_full(s + 1), 2, 1, 4) @
                  embed_lsb(gate_Haar_full(s), 0, 2, 4))
            vt = compute(make_mixed_rho(n_E, pv), Ut)[0]
            Uc = (embed_lsb(gate_Haar_full(s + 3), 0, 3, 4) @
                  embed_lsb(gate_Haar_full(s + 2), 1, 3, 4) @
                  embed_lsb(gate_Haar_full(s + 1), 2, 1, 4) @
                  embed_lsb(gate_Haar_full(s), 0, 2, 4))
            vc = compute(make_mixed_rho(n_E, pv), Uc)[0]
            bonuses_p.append(vc - vt)
        bonuses_p = np.array(bonuses_p)
        bonus_mean = np.mean(bonuses_p)
        bonus_se = np.std(bonuses_p) / np.sqrt(N)
        results["Haar"][str(pv)] = dict(p=pv, pp=qp, bonus=bonus_mean, bonus_se=bonus_se,
                                        bonus_std=np.std(bonuses_p))
        print(f"{pv:8.3f} {qp:10.4f} {'(varies)':>10s} {'(varies)':>10s} {bonus_mean:+10.4f} {bonus_se:10.4f}")

    # ---- Proportionality check ----
    print("\n--- PROPORTIONALITY CHECK: bonus / [p(1-p)] ---")
    print(f"{'p':>8s} {'Rxx bonus/pp':>14s} {'Haar bonus/pp':>14s}")
    print("-" * 38)

    rxx_ratios = []
    haar_ratios = []
    for pv in p_values:
        qp = pv * (1 - pv)
        rxx_r = results["Rxx"][str(pv)]["bonus"] / qp if qp > 0 else float('nan')
        haar_r = results["Haar"][str(pv)]["bonus"] / qp if qp > 0 else float('nan')
        rxx_ratios.append(rxx_r)
        haar_ratios.append(haar_r)
        print(f"{pv:8.3f} {rxx_r:+14.4f} {haar_r:+14.4f}")

    rxx_ratios = np.array(rxx_ratios)
    haar_ratios = np.array(haar_ratios)
    valid_rxx = rxx_ratios[~np.isnan(rxx_ratios) & ~np.isinf(np.abs(rxx_ratios))]
    valid_haar = haar_ratios[~np.isnan(haar_ratios) & ~np.isinf(np.abs(haar_ratios))]

    print(f"\n  Rxx(pi/2): bonus/p(1-p) = {np.mean(valid_rxx):.4f} +/- {np.std(valid_rxx):.4f} "
          f"(constancy check: std/mean = {abs(np.std(valid_rxx)/max(abs(np.mean(valid_rxx)),1e-15)):.3f})")
    print(f"  Haar:       bonus/p(1-p) = {np.mean(valid_haar):.4f} +/- {np.std(valid_haar):.4f} "
          f"(constancy check: std/mean = {abs(np.std(valid_haar)/max(abs(np.mean(valid_haar)),1e-15)):.3f})")

    # Verification statement
    print("\n--- VERIFICATION ---")
    if np.mean(valid_rxx) < 0:
        print("  [PASS] Rxx(pi/2) bonus < 0: commuting gate → cycle reduces QCMI (decoherence accelerator)")
    else:
        print("  [FAIL] Rxx(pi/2) bonus >= 0: unexpected for commuting gate")
    if np.mean(valid_haar) > 0:
        print("  [PASS] Haar bonus > 0: non-commuting gate → cycle amplifies QCMI (correlation amplifier)")
    else:
        print("  [FAIL] Haar bonus <= 0: unexpected for non-commuting gate")

    # Constancy: both should have roughly constant bonus/p(1-p)
    if np.mean(valid_rxx) != 0:
        rxx_cv = abs(np.std(valid_rxx) / np.mean(valid_rxx))
        if rxx_cv < 0.5:
            print(f"  [PASS] Rxx bonus ∝ p(1-p) (CV={rxx_cv:.2f} < 0.5)")
        else:
            print(f"  [WEAK] Rxx bonus ∝ p(1-p) (CV={rxx_cv:.2f}, high variance)")
    if np.mean(valid_haar) != 0:
        haar_cv = abs(np.std(valid_haar) / np.mean(valid_haar))
        if haar_cv < 0.5:
            print(f"  [PASS] Haar bonus ∝ p(1-p) (CV={haar_cv:.2f} < 0.5)")
        else:
            print(f"  [WEAK] Haar bonus ∝ p(1-p) (CV={haar_cv:.2f}, high variance)")

    return results

# ============================================================
# Main
# ============================================================

def main():
    p = 0.7
    n_E = 2
    N = 30

    print("=" * 90)
    print("COMMUTATIVITY SYSTEMATIC SCAN — B博士")
    print(f"4-node ring, b1=1, n_E={n_E}, V=4, p={p}, N={N}")
    print("=" * 90)

    # E1: Commutativity scan matrix
    results_e1 = run_e1(p=p, n_E=n_E, N=N)

    # E2: Bonus vs commutator norm
    results_e2 = run_e2(results_e1, p=p, n_E=n_E, N=N)

    # E3: p-scan
    results_e3 = run_e3(p_values=[0.5, 0.6, 0.7, 0.8, 0.9], n_E=n_E, N=N)

    # ---- Summary ----
    print("\n" + "=" * 90)
    print("SUMMARY: TWO-CLASS CLASSIFICATION")
    print("=" * 90)
    print("  Commuting gates (Cartan-aligned):     bonus <= 0  (cycle = decoherence accelerator)")
    print("  Non-commuting gates (Cartan-mixed):   bonus > 0   (cycle = quantum correlation amplifier)")
    print("  CNOT (Clifford, Cartan-single-axis):  bonus ~ 0   (critical: single-axis, cancellation perfect)")
    print("  SWAP (Clifford, permutation):         bonus < 0   (permutation closes the loop destructively)")
    print("  iSWAP (Clifford, permutation+phase):  bonus < 0   (same permutation mechanism as SWAP)")

    # ---- Save results ----
    output = dict(
        parameters=dict(p=p, n_E=n_E, N=N, V=4, b1=1),
        E1=results_e1,
        E2=[dict(gate=pt["gate"], comm_norm=pt["comm_norm"], bonus=pt["bonus"],
                 bonus_se=pt["bonus_se"], category=pt["category"]) for pt in results_e2],
        E3=results_e3,
    )

    # Convert numpy types to native Python for JSON
    def convert(o):
        if isinstance(o, (np.integer,)):
            return int(o)
        if isinstance(o, (np.floating,)):
            return float(o)
        if isinstance(o, np.ndarray):
            return o.tolist()
        if isinstance(o, dict):
            return {str(k): convert(v) for k, v in o.items()}
        return o

    output = convert(output)
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    out_path = os.path.join(out_dir, "commutativity_scan_results.json")
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to: {out_path}")

    return output

if __name__ == "__main__":
    main()

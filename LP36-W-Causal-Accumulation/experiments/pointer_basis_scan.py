"""
Pointer Basis Scan v3: Rotate ENVIRONMENT basis, not Q.
For gates with Cartan axis=x (XX), min_QCMI should be when E-basis aligns with x.
For gates with Cartan axis=z (ZZ), min_QCMI should be when E-basis aligns with z.
The pointer basis = the E-basis that minimizes QCMI.
"""
import numpy as np
from scipy.linalg import expm

def vn_entropy(rho, eps=1e-12):
    eigvals = np.linalg.eigvalsh(rho); eigvals = np.maximum(eigvals, eps)
    eigvals /= np.sum(eigvals); return -np.sum(eigvals * np.log2(eigvals))

def ptrace(rho, keep, dims):
    n = len(dims); d_total = int(np.prod(dims))
    trace_out = [i for i in range(n) if i not in keep]
    dk = int(np.prod([dims[i] for i in keep]))
    result = np.zeros((dk, dk), dtype=complex)
    for bra in range(d_total):
        bra_bits = [(bra >> i) & 1 for i in range(n)]
        bt = tuple(bra_bits[i] for i in trace_out)
        bk = tuple(bra_bits[i] for i in keep)
        bki = sum(bk[i] * (2**i) for i in range(len(keep)))
        for ket in range(d_total):
            ket_bits = [(ket >> i) & 1 for i in range(n)]
            if tuple(ket_bits[i] for i in trace_out) == bt:
                kk = tuple(ket_bits[i] for i in keep)
                kki = sum(kk[i] * (2**i) for i in range(len(keep)))
                result[bki, kki] += rho[bra, ket]
    return result

def embed_lsb(U2q, a, b, nq):
    D = 2**nq; P = np.zeros((D, D), dtype=complex)
    rem = [i for i in range(nq) if i not in (a, b)]
    for i in range(D):
        bi = [(i >> k) & 1 for k in range(nq)]
        pb = [bi[a], bi[b]] + [bi[r] for r in rem]
        j = sum(pb[k] * (1 << k) for k in range(nq))
        P[j, i] = 1.0
    return P.conj().T @ np.kron(np.eye(2**(nq-2), dtype=complex), U2q) @ P

def embed_lsb_1q(U1q, qubit, nq):
    D = 2**nq
    P = np.zeros((D, D), dtype=complex)
    for i in range(D):
        bi = [(i >> k) & 1 for k in range(nq)]
        pb = [bi[qubit]] + [bi[k] for k in range(nq) if k != qubit]
        j = sum(pb[k] * (1 << (nq-1-k)) for k in range(nq))
        P[j, i] = 1.0
    U_full = np.kron(U1q, np.eye(2**(nq-1), dtype=complex))
    return P.conj().T @ U_full @ P

def su2_rotation(theta, phi):
    """SU(2) rotation mapping |0> to Bloch vector (theta, phi)."""
    sz = np.array([[1,0],[0,-1]], dtype=complex)
    sy = np.array([[0,-1j],[1j,0]], dtype=complex)
    Rz = lambda a: expm(-0.5j * a * sz)
    Ry = lambda a: expm(-0.5j * a * sy)
    return Rz(phi) @ Ry(theta) @ Rz(-phi)

def make_mixed_rho(n_E, p=0.7):
    n_qe = 2 + n_E; n_total = 2 + n_qe; n_with_f = n_total + n_E
    psi = np.zeros(2**n_with_f, dtype=complex)
    sp, sq = np.sqrt(p), np.sqrt(1-p)
    for a in [0, 1]:
        for b in [0, 1]:
            for ev in range(2**n_E):
                idx = (a<<0)|(b<<1)|(a<<2)|(b<<3)|(ev<<4)|(ev<<(4+n_E))
                amp = 0.5
                for i in range(n_E): amp *= (sp if ((ev>>i)&1)==0 else sq)
                psi[idx] = amp
    rho_full = np.outer(psi, psi.conj())
    return ptrace(rho_full, list(range(n_total)), [2]*(n_total+n_E))

def compute(rho_RQE, U_QE):
    I_R = np.eye(4, dtype=complex)
    sigma = np.kron(U_QE, I_R) @ rho_RQE @ np.kron(U_QE, I_R).conj().T
    n_qe = int(np.log2(U_QE.shape[0])); n_tot = 2 + n_qe; dims = [2]*n_tot
    rR = ptrace(sigma, [0,1], dims); rQ = ptrace(sigma, [2,3], dims)
    rRQ = ptrace(sigma, [0,1,2,3], dims)
    rQE_all = ptrace(sigma, list(range(2, n_tot)), dims)
    SR = vn_entropy(rR); SQ = vn_entropy(rQ); SRQ = vn_entropy(rRQ)
    SQE = vn_entropy(rQE_all); Sall = vn_entropy(sigma)
    return (SR + SQE - Sall) - (SR + SQ - SRQ)

def make_CNOT():
    cnot = np.zeros((4,4), dtype=complex)
    cnot[0,0]=cnot[1,1]=cnot[2,3]=cnot[3,2]=1.0
    return cnot

def make_XX(theta):
    sx = np.array([[0,1],[1,0]], dtype=complex)
    return expm(-0.5j * theta * np.kron(sx, sx))

def make_ZZ(theta):
    sz = np.array([[1,0],[0,-1]], dtype=complex)
    return expm(-0.5j * theta * np.kron(sz, sz))

def make_Haar(seed):
    rng = np.random.RandomState(seed)
    A = rng.randn(4,4) + 1j*rng.randn(4,4)
    Q, R = np.linalg.qr(A)
    return Q

# ===== Main Scan =====
print("=" * 70)
print("POINTER BASIS v3: Rotate E, track min_QCMI vs Cartan axis")
print("Prediction: min_QCMI E-basis aligns with gate's Cartan axis direction")
print("=" * 70)

p = 0.7; n_E = 2; nq = 4
n_pts = 60
phi_golden = np.pi * (3 - np.sqrt(5))

gate_configs = [
    ("Rxx(pi/2) [axis=x]", lambda: make_XX(np.pi/2), np.array([1,0,0])),
    ("Rzz(pi/2) [axis=z]", lambda: make_ZZ(np.pi/2), np.array([0,0,1])),
    ("CNOT [axis=x]", lambda: make_CNOT(), np.array([1,0,0])),
    ("Haar [mixed]", lambda: make_Haar(42), None),
]

for gate_label, gate_fn, cartan_axis in gate_configs:
    print(f"\n{'='*60}")
    print(f"Gate: {gate_label}")
    if cartan_axis is not None:
        print(f"  Cartan axis: [{cartan_axis[0]} {cartan_axis[1]} {cartan_axis[2]}]")
    print(f"{'='*60}")

    gate = gate_fn()

    results = []
    for i in range(n_pts):
        # Bloch direction for E-qubit rotation
        y = 1 - (i / float(n_pts - 1)) * 2
        r = np.sqrt(1 - y*y)
        theta = np.arccos(np.clip(y, -1, 1))
        phi = i * phi_golden

        R = su2_rotation(theta, phi)
        R_dag = R.conj().T

        # Apply R to E1 (qubit 2) and E2 (qubit 3) BEFORE gates
        # Apply R† AFTER gates → rotate E's basis
        R_E1 = embed_lsb_1q(R, 2, nq)
        R_E2 = embed_lsb_1q(R, 3, nq)
        R_E1_dag = embed_lsb_1q(R_dag, 2, nq)
        R_E2_dag = embed_lsb_1q(R_dag, 3, nq)

        # U = R_E† · U_gates · R_E  (Heisenberg picture: rotate E basis)
        U_pre = R_E2 @ R_E1  # apply R to both E qubits
        U_post = R_E1_dag @ R_E2_dag  # undo after gates

        U_cycle_natural = (embed_lsb(gate, 0, 3, nq) @ embed_lsb(gate, 1, 3, nq) @
                           embed_lsb(gate, 2, 1, nq) @ embed_lsb(gate, 0, 2, nq))

        U_cycle_rot = U_post @ U_cycle_natural @ U_pre

        rho = make_mixed_rho(n_E, p)
        qcmi = compute(rho, U_cycle_rot)

        nx = np.sin(theta) * np.cos(phi)
        ny = np.sin(theta) * np.sin(phi)
        nz = np.cos(theta)
        results.append((nx, ny, nz, qcmi))

    results = np.array(results)
    min_idx = np.argmin(results[:, 3])
    max_idx = np.argmax(results[:, 3])
    min_n = results[min_idx, :3]
    max_n = results[max_idx, :3]

    span = results[max_idx,3] - results[min_idx,3]

    print(f"QCMI range: [{results[min_idx,3]:.4f}, {results[max_idx,3]:.4f}] (span={span:.4f})")
    print(f"Min QCMI E-basis: n=({min_n[0]:.3f}, {min_n[1]:.3f}, {min_n[2]:.3f})")
    print(f"Max QCMI E-basis: n=({max_n[0]:.3f}, {max_n[1]:.3f}, {max_n[2]:.3f})")

    if span < 0.001:
        print(">>> NULL: QCMI is invariant under E-basis rotation")
        continue

    if cartan_axis is not None:
        angle_min = np.arccos(np.clip(np.abs(np.dot(min_n, cartan_axis)), -1, 1))
        angle_max = np.arccos(np.clip(np.abs(np.dot(max_n, cartan_axis)), -1, 1))
        print(f"Angle(min_QCMI, Cartan_axis) = {np.degrees(angle_min):.1f} deg")
        print(f"Angle(max_QCMI, Cartan_axis) = {np.degrees(angle_max):.1f} deg")

        if angle_min < 25:
            print(f">>> CONFIRMED: min_QCMI E-basis ALIGNS with Cartan axis [x]")
        elif angle_min < 50:
            print(f">>> WEAK: min_QCMI within 50 deg of Cartan axis")
        else:
            print(f">>> REFUTED: no alignment")

    z_axis = np.array([0, 0, 1])
    angle_min_z = np.arccos(np.clip(np.abs(np.dot(min_n, z_axis)), -1, 1))
    print(f"Angle(min_QCMI, z-axis[comp.basis]) = {np.degrees(angle_min_z):.1f} deg")

print("\nDone.")

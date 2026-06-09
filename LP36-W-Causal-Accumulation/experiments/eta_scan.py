"""
Scan QCMI vs gate entangling power to find analytic lower bound.
Key question: what's the functional form of min QCMI as gates vary?
"""
import numpy as np
import warnings
warnings.filterwarnings('ignore')

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
        bki = sum(bk[i] * (2**i) for i in range(len(keep)))
        for ket in range(d_total):
            ket_bits = [(ket >> i) & 1 for i in range(n)]
            if tuple(ket_bits[i] for i in trace_out) == bt:
                kk = tuple(ket_bits[i] for i in keep)
                kki = sum(kk[i] * (2**i) for i in range(len(keep)))
                result[bki, kki] += rho[bra, ket]
    return result

def random_special_unitary(d, seed=None):
    rng = np.random.RandomState(seed)
    A = rng.randn(d, d) + 1j * rng.randn(d, d)
    Q, R = np.linalg.qr(A)
    return Q

def entangling_power_2q(U_4x4):
    """Operator entanglement: avg entropy when U acts on product state.
    Linear entropy version: 1 - avg purity of reduced state.
    For a 2-qubit gate: e_p = 1 - (1/9) * [sum of 4 invariants]
    Simplified: use operator Schmidt rank / local invariants.
    """
    # Use the linear entropy measure: 1 - Tr[(Tr_A[U|phi+>])^2] averaged
    # For simplicity, use a known formula for 2-qubit gates
    # Convert to the magic basis and compute local invariants
    M = np.array([[1,0,0,1j],[0,1j,1,0],[0,1j,-1,0],[1,0,0,-1j]]) / np.sqrt(2)
    U_m = M.conj().T @ U_4x4 @ M
    # det of U_m in magic basis gives one invariant
    # Full entangling power for 2-qubit:
    # e_p = 5/9 - (|Tr U|^4 + |Tr(U SWAP)|^4 + ...)/something
    # Simpler: use average entropy of Schmidt coefficients
    # Just use the operator entanglement: E(U) = 1 - <purity of Tr_A[U|psi>]>

    # Even simpler: use the distance from product unitaries
    # E(U) = 1 - max_{V,W unitary} |Tr[(VxW) U]|/4
    # But this is hard to compute. Let me just use a simple measure.

    # Simplest: compute S(Tr_B[U |00><00| U^dag]) - this is one component
    psi_00 = np.zeros(4, dtype=complex); psi_00[0] = 1.0
    Upsi = U_4x4 @ psi_00
    rho_U = np.outer(Upsi, Upsi.conj())
    rho_A = np.zeros((2,2), dtype=complex)
    # Trace out second qubit (qubit B, index 1)
    for i in range(2):
        for j in range(2):
            # |i,0> and |i,1> for bra; |j,0> and |j,1> for ket
            rho_A[i,j] = rho_U[i*2, j*2] + rho_U[i*2+1, j*2+1]
    return 1 - np.real(np.trace(rho_A @ rho_A))  # linear entropy

def build_cycle_unitary(theta1, theta2, theta3, theta4, phase1=0, phase2=0, phase3=0, phase4=0):
    """
    Build cycle unitary with tunable entangling strength.
    theta_i = 0 -> identity; theta_i = pi/2 -> CNOT-like; theta_i = pi -> SWAP-like

    U_i = exp(-i * theta_i * H_XX) where H_XX = sigma_x ⊗ sigma_x
    Also add local phases for generality.
    """
    sx = np.array([[0,1],[1,0]], dtype=complex)
    H_XX = np.kron(sx, sx)

    def gate_2q(theta, phase):
        U = np.cos(theta/2) * np.eye(4, dtype=complex) - 1j * np.sin(theta/2) * H_XX
        # Add local phase rotation
        if phase != 0:
            sz = np.array([[1,0],[0,-1]], dtype=complex)
            U = U @ np.kron(np.eye(2), np.cos(phase)*np.eye(2) - 1j*np.sin(phase)*sz)
        return U

    U1 = gate_2q(theta1, phase1)
    U2 = gate_2q(theta2, phase2)
    U3 = gate_2q(theta3, phase3)
    U4 = gate_2q(theta4, phase4)

    # Build full 4-qubit unitaries (Q_a=0, Q_b=1, E1=2, E2=3)
    d = 16
    dims4 = [2,2,2,2]

    def embed(U2q, a, b):
        n, D = 4, 16
        perm = [a, b] + [i for i in range(n) if i not in (a,b)]
        P = np.zeros((D, D), dtype=complex)
        for idx in np.ndindex(*dims4):
            idx_in = sum(idx[i] * (1 << (n-1-i)) for i in range(n))
            perm_idx = [idx[p] for p in perm]
            idx_out = sum(perm_idx[i] * (1 << (n-1-i)) for i in range(n))
            P[idx_out, idx_in] = 1.0
        d_rest = D // 4
        U_lifted = np.kron(U2q, np.eye(d_rest, dtype=complex))
        return P.conj().T @ U_lifted @ P

    U1_full = embed(U1, 0, 2)  # Q_a, E1
    U2_full = embed(U2, 2, 1)  # E1, Q_b
    U3_full = embed(U3, 0, 3)  # Q_a, E2
    U4_full = embed(U4, 1, 3)  # Q_b, E2

    return U4_full @ U3_full @ U2_full @ U1_full, [U1, U2, U3, U4]

def compute_qcmi_for_cycle(U_QE, p=0.7):
    """Compute QCMI for the 4-node cycle given the full 4-qubit unitary."""
    nq, dims = 6, [2]*6  # R_a,R_b,Q_a,Q_b,E1,E2

    psi = np.zeros(64, dtype=complex)
    for a in [0,1]:
        for b in [0,1]:
            idx = (a<<0)|(b<<1)|(a<<2)|(b<<3)
            psi[idx] = 0.5

    rho_init = np.outer(psi, psi.conj())

    # Apply U_QE (acts on Q_a,Q_b,E1,E2, indices 2,3,4,5)
    # Need to embed U_QE (16x16) into full 64x64 space
    # U_QE on indices 2,3,4,5; identity on 0,1
    I_R = np.eye(4, dtype=complex)
    U_full = np.kron(I_R, U_QE)
    rho_final = U_full @ rho_init @ U_full.conj().T

    rho_R = ptrace(rho_final, [0,1], dims)
    rho_Qp = ptrace(rho_final, [2,3], dims)
    rho_RQp = ptrace(rho_final, [0,1,2,3], dims)
    rho_QpEp = ptrace(rho_final, [2,3,4,5], dims)

    SR = vn_entropy(rho_R)
    SQ = vn_entropy(rho_Qp)
    SRQ = vn_entropy(rho_RQp)
    SQE = vn_entropy(rho_QpEp)
    Sall = vn_entropy(rho_final)

    I_RQ = SR + SQ - SRQ
    I_R_QE = SR + SQE - Sall
    return I_R_QE - I_RQ, I_RQ, SRQ

# Test: CNOT-like (theta = pi/2 gives i*H_XX which is entangling but not exactly CNOT)
p = 0.7
thetas = np.linspace(0, np.pi, 20)
print("Theta scan (all gates equal strength):")
print(f"{'theta/pi':>10s}  {'QCMI':>10s}  {'I(R;Q)':>10s}  {'S(RQ)':>10s}")
for t in thetas:
    U_QE, gates = build_cycle_unitary(t, t, t, t)
    qcmi, irq, srq = compute_qcmi_for_cycle(U_QE, p)
    print(f"{t/np.pi:10.4f}  {qcmi:10.6f}  {irq:10.6f}  {srq:10.6f}")

# Test: vary one gate, others at pi/2 (max entangling)
print(f"\nSingle gate scan (vary U1, others at pi/2):")
for t in thetas:
    U_QE, gates = build_cycle_unitary(t, np.pi/2, np.pi/2, np.pi/2)
    qcmi, irq, srq = compute_qcmi_for_cycle(U_QE, p)
    print(f"{t/np.pi:10.4f}  {qcmi:10.6f}  {irq:10.6f}  {srq:10.6f}")

# Scan: Haver-random gates, compute min QCMI vs a measure of "total entangling strength"
print(f"\nRandom gate scan (200 samples):")
print(f"{'E_total':>10s}  {'QCMI':>10s}  {'S(RQ)':>10s}")
for seed in range(200):
    thetas = np.random.uniform(0, np.pi, 4)
    phases = np.random.uniform(0, 2*np.pi, 4)
    U_QE, gates = build_cycle_unitary(*thetas, *phases)
    qcmi, irq, srq = compute_qcmi_for_cycle(U_QE, p)
    E_total = np.sum([np.sin(t/2)**2 for t in thetas])  # ~measure of entangling strength
    print(f"{E_total:10.4f}  {qcmi:10.6f}  {srq:10.6f}")

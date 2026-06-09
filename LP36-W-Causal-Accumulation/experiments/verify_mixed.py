"""
Buscemi setup: rho_RQE = Phi+_RQ (x) gamma_E where gamma_E is MIXED.
NOT a pure state on RQE. This is the correct Buscemi framework.
"""
import numpy as np

def vn_entropy(rho, eps=1e-12):
    eigvals = np.linalg.eigvalsh(rho); eigvals = np.maximum(eigvals, eps)
    eigvals = eigvals / np.sum(eigvals); return -np.sum(eigvals * np.log2(eigvals))

def ptrace(rho, keep, dims):
    n=len(dims); d_total=int(np.prod(dims))
    trace_out=[i for i in range(n) if i not in keep]
    dk=int(np.prod([dims[i] for i in keep]))
    result=np.zeros((dk,dk),dtype=complex)
    for bra in range(d_total):
        bra_bits=[(bra>>i)&1 for i in range(n)]
        bt=tuple(bra_bits[i] for i in trace_out)
        bk=tuple(bra_bits[i] for i in keep)
        bki=sum(bk[i]*(2**i) for i in range(len(keep)))
        for ket in range(d_total):
            ket_bits=[(ket>>i)&1 for i in range(n)]
            if tuple(ket_bits[i] for i in trace_out)==bt:
                kk=tuple(ket_bits[i] for i in keep)
                kki=sum(kk[i]*(2**i) for i in range(len(keep)))
                result[bki,kki]+=rho[bra,ket]
    return result

def embed_lsb(U2q, a, b, nq=4):
    D=2**nq; P=np.zeros((D,D),dtype=complex)
    rem=[i for i in range(nq) if i not in(a,b)]
    for i in range(D):
        bi=[(i>>k)&1 for k in range(nq)]
        pb=[bi[a],bi[b]]+[bi[r] for r in rem]
        j=sum(pb[k]*(1<<k) for k in range(nq))
        P[j,i]=1.0
    return P.conj().T @ np.kron(np.eye(2**(nq-2),dtype=complex),U2q) @ P

CNOT_LSB=np.zeros((4,4),dtype=complex)
CNOT_LSB[0,0]=1;CNOT_LSB[3,1]=1;CNOT_LSB[2,2]=1;CNOT_LSB[1,3]=1
UQE_CNOT = embed_lsb(CNOT_LSB,0,3)@embed_lsb(CNOT_LSB,1,3)@embed_lsb(CNOT_LSB,1,2)@embed_lsb(CNOT_LSB,0,2)
dims=[2]*6; IR4=np.eye(4,dtype=complex)

def bell_state():
    psi = np.zeros(4, dtype=complex); psi[0]=psi[3]=1/np.sqrt(2)
    return np.outer(psi, psi.conj())

print("Buscemi MIXED-state setup: rho_RQE = Phi+_RQ (x) gamma_E")
print("gamma_E = diag(p,1-p) (x) diag(p,1-p) -- MIXED, not pure")
print()

for p in [0.01, 0.1, 0.3, 0.5, 0.7, 0.9, 0.99]:
    q = 1-p
    # Build initial density matrix (MIXED on RQE)
    # Phi+_RaQa (4x4) x Phi+_RbQb (4x4) = RQ state (16x16)
    phi_RaQa = bell_state()
    phi_RbQb = bell_state()
    # Ordering: R_a(0), R_b(1), Q_a(2), Q_b(3)
    # Bell pair on (0,2) and (1,3)
    # kronecker product gives ordering Ra,Qa,Rb,Qb, need to permute to Ra,Rb,Qa,Qb
    rho_RQ_temp = np.kron(phi_RaQa, phi_RbQb)  # Ra,Qa,Rb,Qb ordering
    # Permute: Ra(0),Qa(1),Rb(2),Qb(3) -> Ra(0),Rb(1),Qa(2),Qb(3)
    # Each index is 0 or 1 (qubit), not 0-3
    rho_RQ = np.zeros((16,16), dtype=complex)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    # input index: Ra=i, Qa=j, Rb=k, Qb=l in MSB-first
                    idx_in = i*8 + j*4 + k*2 + l
                    for ip in range(2):
                        for jp in range(2):
                            for kp in range(2):
                                for lp in range(2):
                                    idx_in_p = ip*8 + jp*4 + kp*2 + lp
                                    # output index: Ra=i, Rb=k, Qa=j, Qb=l
                                    idx_out = i*8 + k*4 + j*2 + l
                                    idx_out_p = ip*8 + kp*4 + jp*2 + lp
                                    rho_RQ[idx_out, idx_out_p] = rho_RQ_temp[idx_in, idx_in_p]

    # gamma_E = diag(p,q) x diag(p,q) (mixed, 4x4)
    gamma_E = np.diag([p*p, p*q, q*p, q*q])

    # Full rho_RQE = rho_RQ (x) gamma_E (ordering: R(qubits 0,1), Q(2,3), E(4,5))
    # rho_RQ is 16x16, gamma_E is 4x4, kron gives 64x64
    rho_RQE = np.kron(rho_RQ, gamma_E)
    # Check: this has ordering R_a,R_b,Q_a,Q_b,E1,E2 which matches our convention

    # Verify S(RQE) = S(gamma_E) = 2*h2(p)
    S_RQE = vn_entropy(rho_RQE)
    h2p = -p*np.log2(p) - q*np.log2(q) if 0<p<1 else 0
    # print(f"p={p:.3f}: S(RQE)={S_RQE:.4f}, 2*h2(p)={2*h2p:.4f}")

    # Apply unitary: U_full = I_R (x) U_QE
    U_full = np.kron(IR4, UQE_CNOT)  # I_R on qubits 0,1; U_QE on 2,3,4,5
    sigma = U_full @ rho_RQE @ U_full.conj().T

    # Compute entropies
    rho_R = ptrace(sigma, [0,1], dims)
    rho_Q = ptrace(sigma, [2,3], dims)
    rho_E = ptrace(sigma, [4,5], dims)
    rho_RQ = ptrace(sigma, [0,1,2,3], dims)
    rho_QE = ptrace(sigma, [2,3,4,5], dims)
    Sall = vn_entropy(sigma)

    SR = vn_entropy(rho_R)
    SQ = vn_entropy(rho_Q)
    SE = vn_entropy(rho_E)
    SRQ = vn_entropy(rho_RQ)
    SQE = vn_entropy(rho_QE)

    I_RQ = SR + SQ - SRQ
    I_R_QE = SR + SQE - Sall
    QCMI = I_R_QE - I_RQ
    identity_check = 4 - I_RQ  # should equal QCMI

    print(f"p={p:.3f}: S(E')={SE:.4f} S(RQ')={SRQ:.4f} I(R;Q')={I_RQ:.4f} QCMI={QCMI:.4f} | 4-IRQ={identity_check:.4f}")

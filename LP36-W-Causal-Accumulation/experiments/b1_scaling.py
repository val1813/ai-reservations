"""
Test: QCMI vs b1 scaling. Haar random gates, Buscemi mixed state.
b1=0: tree, b1=1: single cycle, b1=2: two cycles sharing Q nodes.
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

def embed_lsb(U2q, a, b, nq):
    D=2**nq; P=np.zeros((D,D),dtype=complex)
    rem=[i for i in range(nq) if i not in(a,b)]
    for i in range(D):
        bi=[(i>>k)&1 for k in range(nq)]
        pb=[bi[a],bi[b]]+[bi[r] for r in rem]
        j=sum(pb[k]*(1<<k) for k in range(nq))
        P[j,i]=1.0
    return P.conj().T @ np.kron(np.eye(2**(nq-2),dtype=complex),U2q) @ P

def random_u(d,s):
    rng=np.random.RandomState(s); A=rng.randn(d,d)+1j*rng.randn(d,d)
    Q,R=np.linalg.qr(A); return Q

def make_mixed_rho(n_E, p=0.7):
    """rho_RQE = Phi+_RQ (x) gamma_E where gamma_E = (diag(p,1-p))^(x)n_E.
    n_E = number of environment qubits. Q always has 2 qubits (Q_a, Q_b).
    Total QE qubits = 2 + n_E.
    Purification: each E_i paired with F_i via |psi_p> = sqrt(p)|00>+sqrt(q)|11>."""
    n_qe = 2 + n_E
    n_total = 2 + n_qe  # R_a,R_b + Q_a,Q_b + E_1..E_nE
    n_with_f = n_total + n_E  # + F_1..F_nE
    psi = np.zeros(2**n_with_f, dtype=complex)
    sp, sq = np.sqrt(p), np.sqrt(1-p)
    for a in [0,1]:
        for b in [0,1]:
            for e_val in range(2**n_E):
                f_val = e_val  # F mirrors E for |psi_p> purification
                # Index: R_a(0),R_b(1),Q_a(a,2),Q_b(b,3),E(4..),F(4+n_E..)
                idx = (a<<0)|(b<<1)|(a<<2)|(b<<3)|(e_val<<4)|(f_val<<(4+n_E))
                amp = 0.5
                for i in range(n_E):
                    bit = (e_val >> i) & 1
                    amp *= (sp if bit == 0 else sq)
                psi[idx] = amp
    rho_full = np.outer(psi, psi.conj())
    # Trace out F: keep R_a,R_b,Q_a,Q_b,E_1..E_nE
    keep = list(range(n_total))
    return ptrace(rho_full, keep, [2]*(n_total + n_E))

def compute(rho_RQE, U_QE, n_qe):
    d_R = 4; I_R = np.eye(d_R, dtype=complex)
    # LSB encoding: QE is slow (bits 2+), R is fast (bits 0,1)
    # kron(U_QE, I_R) puts U_QE on slow, I_R on fast
    sigma = np.kron(U_QE, I_R) @ rho_RQE @ np.kron(U_QE, I_R).conj().T
    n_tot = 2 + n_qe; dims = [2]*n_tot
    rR = ptrace(sigma, [0,1], dims); rQ = ptrace(sigma, [2,3], dims)
    rRQ = ptrace(sigma, [0,1,2,3], dims)
    rQE = ptrace(sigma, list(range(2,n_tot)), dims)
    SR=vn_entropy(rR); SQ=vn_entropy(rQ); SRQ=vn_entropy(rRQ)
    SQE=vn_entropy(rQE); Sall=vn_entropy(sigma)
    return (SR+SQE-Sall) - (SR+SQ-SRQ)

# ===== Graph constructions =====
# All use Q_a=0, Q_b=1 in the QE qubit indexing
# E qubits are indexed starting from 2

def build_tree_U(rng_seed):
    """b1=0: tree on 5 QE qubits (Q_a,Q_b,E1,E2,E3).
    Edges: Q_a-E1, E1-Q_b, Q_b-E2, E2-E3. 5V, 4E, b1=4-5+1=0."""
    U1=embed_lsb(random_u(4,rng_seed),   0,2,5)  # Q_a(0),E1(2)
    U2=embed_lsb(random_u(4,rng_seed+1), 2,1,5)  # E1(2),Q_b(1)
    U3=embed_lsb(random_u(4,rng_seed+2), 1,3,5)  # Q_b(1),E2(3)
    U4=embed_lsb(random_u(4,rng_seed+3), 3,4,5)  # E2(3),E3(4)
    return U4 @ U3 @ U2 @ U1

def build_cycle_U(rng_seed):
    """b1=1: 4-cycle on 4 QE qubits.
    Q_a-E1-Q_b-E2-Q_a. 4V, 4E, b1=4-4+1=1."""
    U1=embed_lsb(random_u(4,rng_seed),   0,2,4)  # Q_a(0),E1(2)
    U2=embed_lsb(random_u(4,rng_seed+1), 2,1,4)  # E1(2),Q_b(1)
    U3=embed_lsb(random_u(4,rng_seed+2), 1,3,4)  # Q_b(1),E2(3)
    U4=embed_lsb(random_u(4,rng_seed+3), 0,3,4)  # Q_a(0),E2(3)
    return U4 @ U3 @ U2 @ U1

def build_2cycle_U(rng_seed):
    """b1=3: two 4-cycles sharing Q_a,Q_b. 6V, 8E.
    Cycle A: Q_a-E1-Q_b-E2-Q_a (indices 0,1,2,3)
    Cycle B: Q_a-E3-Q_b-E4-Q_a (indices 0,1,4,5)"""
    # Cycle A
    UA1=embed_lsb(random_u(4,rng_seed),   0,2,6)  # Q_a(0),E1(2)
    UA2=embed_lsb(random_u(4,rng_seed+1), 2,1,6)  # E1(2),Q_b(1)
    UA3=embed_lsb(random_u(4,rng_seed+2), 1,3,6)  # Q_b(1),E2(3)
    UA4=embed_lsb(random_u(4,rng_seed+3), 0,3,6)  # Q_a(0),E2(3)
    # Cycle B
    UB1=embed_lsb(random_u(4,rng_seed+4), 0,4,6)  # Q_a(0),E3(4)
    UB2=embed_lsb(random_u(4,rng_seed+5), 4,1,6)  # E3(4),Q_b(1)
    UB3=embed_lsb(random_u(4,rng_seed+6), 1,5,6)  # Q_b(1),E4(5)
    UB4=embed_lsb(random_u(4,rng_seed+7), 0,5,6)  # Q_a(0),E4(5)
    return UB4@UB3@UB2@UB1 @ UA4@UA3@UA2@UA1

print("="*60)
print("QCMI vs b1 scaling (Haar random, Buscemi mixed, p=0.7)")
print("="*60)

p=0.7; N=30

for label, n_qe, builder in [
    ("b1=0  tree  5QE", 5, build_tree_U),
    ("b1=1  cycle 4QE", 4, build_cycle_U),
    ("b1~3  2cycle 6QE", 6, build_2cycle_U),
]:
    n_E = n_qe - 2  # exclude Q_a, Q_b
    rho = make_mixed_rho(n_E, p)
    vals = []
    for t in range(N):
        U = builder(1000+t*10)
        vals.append(compute(rho, U, n_qe))
    vals = np.array(vals)
    print(f"\n{label}:")
    print(f"  mean={np.mean(vals):.4f}  std={np.std(vals):.4f}  min={np.min(vals):.4f}  max={np.max(vals):.4f}")

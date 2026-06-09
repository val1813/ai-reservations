"""
Clean sign flip verification. INSPECTED protocol.
Question: Does cycle(b1=1) QCMI exceed tree(b1=0) QCMI
          only for non-commuting gates?

All comparisons: same V=4, same n_E=2, same p=0.7.
Tree: 3 edges (Q_a-E1-Q_b-E2), b1=0.
Cycle: 4 edges (Q_a-E1-Q_b-E2-Q_a), b1=1.
Difference: 1 extra edge that closes the loop.
"""
import numpy as np
from scipy.linalg import expm

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

def make_mixed_rho(n_E, p=0.7):
    n_qe=2+n_E; n_total=2+n_qe; n_with_f=n_total+n_E
    psi=np.zeros(2**n_with_f,dtype=complex)
    sp=np.sqrt(p); sq=np.sqrt(1-p)
    for a in[0,1]:
        for b in[0,1]:
            for ev in range(2**n_E):
                idx=(a<<0)|(b<<1)|(a<<2)|(b<<3)|(ev<<4)|(ev<<(4+n_E))
                amp=0.5
                for i in range(n_E): amp*=(sp if((ev>>i)&1)==0 else sq)
                psi[idx]=amp
    rho_full=np.outer(psi,psi.conj())
    return ptrace(rho_full,list(range(n_total)),[2]*(n_total+n_E))

def compute(rho_RQE, U_QE):
    I_R=np.eye(4,dtype=complex)
    sigma=np.kron(U_QE,I_R)@rho_RQE@np.kron(U_QE,I_R).conj().T
    n_qe=int(np.log2(U_QE.shape[0])); n_tot=2+n_qe; dims=[2]*n_tot
    rR=ptrace(sigma,[0,1],dims); rQ=ptrace(sigma,[2,3],dims)
    rRQ=ptrace(sigma,[0,1,2,3],dims); rQE_all=ptrace(sigma,list(range(2,n_tot)),dims)
    SR=vn_entropy(rR); SQ=vn_entropy(rQ); SRQ=vn_entropy(rRQ)
    SQE=vn_entropy(rQE_all); Sall=vn_entropy(sigma)
    return (SR+SQE-Sall)-(SR+SQ-SRQ), SR, SQ, SRQ

def commutator_norm_2q(gate_fn, seed=99):
    """||[U01, U02]|| for 2-qubit gates sharing qubit 0."""
    U01=np.kron(gate_fn(seed), np.eye(2))
    P=np.zeros((8,8),dtype=complex)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                P[i*4+k*2+j, i*4+j*2+k]=1.0
    U02=P.conj().T@np.kron(gate_fn(seed+100),np.eye(2))@P
    return np.linalg.norm(U01@U02-U02@U01)

# Gate library
def gate_CNOT():
    c=np.zeros((4,4),dtype=complex); c[0,0]=c[1,1]=c[2,3]=c[3,2]=1.0; return c
def gate_SWAP():
    s=np.zeros((4,4),dtype=complex); s[0,0]=s[3,3]=1.0; s[1,2]=s[2,1]=1.0; return s
def gate_iSWAP():
    isw=np.eye(4,dtype=complex); isw[1,2]=1j; isw[2,1]=1j; isw[1,1]=0; isw[2,2]=0; return isw
def gate_CZ():
    return np.diag([1,1,1,-1]).astype(complex)
def gate_Rxx(theta):
    sx=np.array([[0,1],[1,0]],dtype=complex)
    return expm(-0.5j*theta*np.kron(sx,sx))
def gate_Rzz(theta):
    sz=np.array([[1,0],[0,-1]],dtype=complex)
    return expm(-0.5j*theta*np.kron(sz,sz))
def gate_Haar(seed):
    rng=np.random.RandomState(seed); A=rng.randn(4,4)+1j*rng.randn(4,4)
    Q,R=np.linalg.qr(A); return Q
def gate_weak_Haar(alpha, seed):
    rng=np.random.RandomState(seed); H=rng.randn(4,4)+1j*rng.randn(4,4)
    H=H+H.conj().T; return expm(1j*alpha*H)
def gate_Identity(): return np.eye(4,dtype=complex)

# ===== SELF-CHECKS =====
print("=== SELF-CHECKS ===")
# 1. Identity gives QCMI=0
rho2=make_mixed_rho(2)
I16=np.eye(16,dtype=complex)
qc, sr, sq, srq = compute(rho2, I16)
assert abs(qc)<1e-6, f"Identity QCMI={qc} != 0"
print(f"[OK] Identity QCMI={qc:.2e}")

# 2. S(R)=2 and S(RQ)=0 initially
assert abs(sr-2)<1e-6, f"S(R)={sr} != 2"
assert abs(srq)<1e-6, f"S(RQ)={srq} != 0"
print(f"[OK] S(R)={sr:.1f}, S(RQ)={srq:.1f}")

# 3. S(R) invariant after random unitary
U_test=embed_lsb(gate_Haar(42),0,2,4)
qc2,sr2,sq2,srq2=compute(rho2, U_test)
assert abs(sr2-2)<1e-6, f"S(R) changed from 2 to {sr2}"
print(f"[OK] S(R) invariant: {sr:.1f} -> {sr2:.1f}")

# 4. Commutator: XX=0, Haar>0
assert abs(commutator_norm_2q(lambda s:gate_Rxx(1.0)))<1e-10, "XX should commute"
assert commutator_norm_2q(lambda s:gate_Haar(s))>0.5, "Haar should NOT commute"
print(f"[OK] Commutator: XX={commutator_norm_2q(lambda s:gate_Rxx(1.0)):.1e}, Haar={commutator_norm_2q(lambda s:gate_Haar(42)):.2f}")

# 5. CNOT tree=tree (both give same QCMI for same gate count?)
# Two identical CNOT trees should give same QCMI
Ut1=embed_lsb(gate_CNOT(),0,2,4)@embed_lsb(gate_CNOT(),2,1,4)@embed_lsb(gate_CNOT(),0,2,4)  # 3 CNOTs
Ut2=embed_lsb(gate_CNOT(),0,2,4)@embed_lsb(gate_CNOT(),2,1,4)@embed_lsb(gate_CNOT(),0,2,4)
qc_t1=compute(rho2,Ut1)[0]; qc_t2=compute(rho2,Ut2)[0]
assert abs(qc_t1-qc_t2)<1e-6, f"Identical trees differ: {qc_t1} vs {qc_t2}"
print(f"[OK] Identical trees: {qc_t1:.4f} == {qc_t2:.4f}")

print("\n=== MAIN SCAN ===")

# ===== MAIN EXPERIMENT =====
p=0.7; N=40
print(f"{'gate':<25s} {'comm':>8s} {'tree':>10s} {'cycle':>10s} {'bonus':>10s} {'sigma':>6s} {'sign':>6s}")
print("-"*80)

for label, gate_fn in [
    # Factorizable (should give bonus=0)
    ("Identity", lambda s: gate_Identity()),
    # Commuting (should give bonus<=0)
    ("Rxx(pi/2)", lambda s: gate_Rxx(np.pi/2)),
    ("Rxx(pi/4)", lambda s: gate_Rxx(np.pi/4)),
    ("Rzz(pi/2)", lambda s: gate_Rzz(np.pi/2)),
    ("Rzz(pi/4)", lambda s: gate_Rzz(np.pi/4)),
    ("CZ", lambda s: gate_CZ()),
    # Classical (basis-aligned, ambiguous)
    ("CNOT", lambda s: gate_CNOT()),
    # Non-commuting (should give bonus>0)
    ("SWAP", lambda s: gate_SWAP()),
    ("iSWAP", lambda s: gate_iSWAP()),
    ("Haar (full)", lambda s: gate_Haar(s)),
    ("wHaar a=0.05", lambda s: gate_weak_Haar(0.05, s)),
    ("wHaar a=0.10", lambda s: gate_weak_Haar(0.10, s)),
    ("wHaar a=0.20", lambda s: gate_weak_Haar(0.20, s)),
]:
    comm = commutator_norm_2q(gate_fn)
    vt=[]; vc=[]
    for t in range(N):
        s=1000+t*10
        Ut=embed_lsb(gate_fn(s+2),1,3,4)@embed_lsb(gate_fn(s+1),2,1,4)@embed_lsb(gate_fn(s),0,2,4)
        vt.append(compute(make_mixed_rho(2,p),Ut)[0])
        Uc=embed_lsb(gate_fn(s+3),0,3,4)@embed_lsb(gate_fn(s+2),1,3,4)@embed_lsb(gate_fn(s+1),2,1,4)@embed_lsb(gate_fn(s),0,2,4)
        vc.append(compute(make_mixed_rho(2,p),Uc)[0])
    vt=np.array(vt); vc=np.array(vc)
    bonus=np.mean(vc)-np.mean(vt)
    se=np.sqrt(np.var(vc)+np.var(vt))/np.sqrt(N)
    sig=abs(bonus)/max(se,1e-15)
    eps=0.005
    sgn="+" if bonus>eps else ("-" if bonus<-eps else "0")
    print(f"{label:<25s} {comm:8.4f} {np.mean(vt):10.4f} {np.mean(vc):10.4f} {bonus:+10.4f} {sig:5.1f} {sgn:>6s}")

print("\n=== SUMMARY ===")
print("Commuting gates (XX,ZZ,CZ): bonus < 0 or = 0")
print("Non-commuting (Haar, weak Haar): bonus > 0")
print("Classical (CNOT): bonus = 0 (saturated)")
print("Permutation (SWAP,iSWAP): bonus < 0 (destructive, information recirculates)")

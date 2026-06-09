"""
Clean re-run: Gate quantumness scan, tree vs cycle.
Tests the interference hypothesis: b1 amplifies/suppresses QCMI
depending on gate commutativity.
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
    rRQ=ptrace(sigma,[0,1,2,3],dims)
    rQE_all=ptrace(sigma,list(range(2,n_tot)),dims)
    SR=vn_entropy(rR); SQ=vn_entropy(rQ); SRQ=vn_entropy(rRQ)
    SQE=vn_entropy(rQE_all); Sall=vn_entropy(sigma)
    return (SR+SQE-Sall)-(SR+SQ-SRQ), SR, SQ, SRQ

# ---- Gate factories ----
def make_CNOT():
    cnot = np.zeros((4,4), dtype=complex)
    cnot[0,0]=cnot[1,1]=cnot[2,3]=cnot[3,2]=1.0
    return cnot

def make_XX(theta):
    sx = np.array([[0,1],[1,0]], dtype=complex)
    return expm(-0.5j * theta * np.kron(sx,sx))

def make_ZZ(theta):
    sz = np.array([[1,0],[0,-1]], dtype=complex)
    return expm(-0.5j * theta * np.kron(sz,sz))

def make_rand_Haar(seed):
    rng = np.random.RandomState(seed)
    A = rng.randn(4,4)+1j*rng.randn(4,4)
    Q,R = np.linalg.qr(A)
    return Q

def make_weak_Haar(alpha, seed):
    rng = np.random.RandomState(seed)
    H = rng.randn(4,4)+1j*rng.randn(4,4); H = H+H.conj().T
    return expm(1j*alpha*H)

# ---- Verify commutativity ----
def test_commutativity(label, gate_fn):
    """Test if U_01 and U_02 commute (share qubit 0)."""
    U01 = np.kron(gate_fn(99), np.eye(2))     # qubits 0,1
    # U02 needs permutation: qubits 0,2 adjacent
    P = np.zeros((8,8), dtype=complex)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                idx_in = i*4+j*2+k
                idx_out = i*4+k*2+j
                P[idx_out, idx_in] = 1.0
    U02 = P.conj().T @ np.kron(gate_fn(199), np.eye(2)) @ P
    comm = np.linalg.norm(U01@U02 - U02@U01)
    return comm

def verify_setup():
    """Self-consistency checks."""
    print("=== SETUP VERIFICATION ===")

    # 1. Check initial state
    rho2 = make_mixed_rho(2)
    SR = vn_entropy(ptrace(rho2, [0,1], [2]*6))
    SRQ = vn_entropy(ptrace(rho2, [0,1,2,3], [2]*6))
    print(f"S(R)_init = {SR:.4f} (expect 2.0): {'OK' if abs(SR-2)<1e-6 else 'FAIL'}")
    print(f"S(RQ)_init = {SRQ:.4f} (expect 0.0): {'OK' if abs(SRQ)<1e-6 else 'FAIL'}")

    # 2. Check identity gives QCMI=0
    I16 = np.eye(16, dtype=complex)
    qcmi_id, SR, SQ, SRQ = compute(rho2, I16)
    print(f"QCMI(identity) = {qcmi_id:.6f} (expect 0): {'OK' if abs(qcmi_id)<1e-6 else 'FAIL'}")
    print(f"  S(R)={SR:.4f}(expect 2) S(Q)={SQ:.4f}(expect 2) S(RQ)={SRQ:.4f}(expect 0)")

    # 3. Check gate commutativity
    for label, fn in [("CNOT", lambda s: make_CNOT()),
                       ("XX(pi/2)", lambda s: make_XX(np.pi/2)),
                       ("XX(pi/4)", lambda s: make_XX(np.pi/4)),
                       ("Haar", lambda s: make_rand_Haar(s))]:
        c = test_commutativity(label, fn)
        print(f"[U01, U02] norm for {label}: {c:.4f} {'COMMUTING' if c<1e-10 else 'NON-COMMUTING'}")

    # 4. Verify U_QE is unitary
    def build_cycle(seed):
        U=embed_lsb(make_rand_Haar(seed+3),0,3,4)@embed_lsb(make_rand_Haar(seed+2),1,3,4)@embed_lsb(make_rand_Haar(seed+1),2,1,4)@embed_lsb(make_rand_Haar(seed),0,2,4)
        return U
    U = build_cycle(1000)
    print(f"U_cycle unitary: {np.allclose(U@U.conj().T, np.eye(16))}")

    # 5. Check S(R) invariance
    qcmi, SR, SQ, SRQ = compute(rho2, U)
    print(f"After cycle: S(R)={SR:.4f} (expect 2.0 invariant): {'OK' if abs(SR-2)<1e-6 else 'FAIL'}")

verify_setup()

# ---- Main scan ----
print("\n=== MAIN SCAN: tree vs cycle, varying gate type ===")
print(f"{'gate':<30s} {'tree':>8s} {'cycle':>8s} {'bonus':>8s} {'sig':>6s}")
print("-"*65)

p=0.7; N=40

for label, gate_fn, desc in [
    ("CNOT (classical)", lambda s: make_CNOT(), "Commuting, basis-aligned"),
    ("XX(pi/2) (commuting)", lambda s: make_XX(np.pi/2), "Commuting on shared qubit"),
    ("XX(pi/4) (commuting)", lambda s: make_XX(np.pi/4), "Commuting, weaker"),
    ("ZZ(pi/2) (commuting)", lambda s: make_ZZ(np.pi/2), "Commuting, Z-basis"),
    ("weak Haar a=0.08", lambda s: make_weak_Haar(0.08, s), "Non-commuting, weak"),
    ("weak Haar a=0.12", lambda s: make_weak_Haar(0.12, s), "Non-commuting, medium"),
    ("Haar (full)", lambda s: make_rand_Haar(s), "Non-commuting, full"),
]:
    vals_tree=[]; vals_cycle=[]
    for t in range(N):
        s=1000+t*10
        Uc=embed_lsb(gate_fn(s+3),0,3,4)@embed_lsb(gate_fn(s+2),1,3,4)@embed_lsb(gate_fn(s+1),2,1,4)@embed_lsb(gate_fn(s),0,2,4)
        vals_cycle.append(compute(make_mixed_rho(2,p), Uc)[0])
        Ut=embed_lsb(gate_fn(s+3),3,4,5)@embed_lsb(gate_fn(s+2),1,3,5)@embed_lsb(gate_fn(s+1),2,1,5)@embed_lsb(gate_fn(s),0,2,5)
        vals_tree.append(compute(make_mixed_rho(3,p), Ut)[0])
    vt=np.array(vals_tree); vc=np.array(vals_cycle)
    bonus=np.mean(vc)-np.mean(vt)
    se=np.sqrt(np.var(vc)+np.var(vt))/np.sqrt(N)
    sig=abs(bonus)/max(se,1e-15)
    print(f"{label:<30s} {np.mean(vt):8.4f} {np.mean(vc):8.4f} {bonus:+8.4f} {sig:5.1f}")

print("\nKey: bonus>0 = cycle has MORE QCMI than tree (constructive interference)")
print("      bonus<0 = cycle has LESS QCMI than tree (destructive interference)")
print("      bonus~0 = no interference effect")

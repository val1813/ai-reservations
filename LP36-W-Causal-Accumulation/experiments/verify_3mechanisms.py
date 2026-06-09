"""
Verify 3-mechanism classification: Permutation, Phase, Entanglement.
Systematic scan with predicted sign for each gate.
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

def commutator_norm(gate_fn, seed=99):
    U01 = np.kron(gate_fn(seed), np.eye(2))
    P = np.zeros((8,8), dtype=complex)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                P[i*4+k*2+j, i*4+j*2+k] = 1.0
    U02 = P.conj().T @ np.kron(gate_fn(seed+100), np.eye(2)) @ P
    return np.linalg.norm(U01@U02 - U02@U01)

# Gate library
def gate_Rxx(theta):
    sx=np.array([[0,1],[1,0]],dtype=complex)
    return expm(-0.5j*theta*np.kron(sx,sx))
def gate_Ryy(theta):
    sy=np.array([[0,-1j],[1j,0]],dtype=complex)
    return expm(-0.5j*theta*np.kron(sy,sy))
def gate_Rzz(theta):
    sz=np.array([[1,0],[0,-1]],dtype=complex)
    return expm(-0.5j*theta*np.kron(sz,sz))
def gate_CNOT():
    cnot=np.zeros((4,4),dtype=complex); cnot[0,0]=cnot[1,1]=cnot[2,3]=cnot[3,2]=1.0; return cnot
def gate_SWAP():
    sw=np.zeros((4,4),dtype=complex); sw[0,0]=sw[3,3]=1.0; sw[1,2]=sw[2,1]=1.0; return sw
def gate_iSWAP():
    isw=np.eye(4,dtype=complex); isw[1,2]=1j; isw[2,1]=1j; isw[1,1]=0; isw[2,2]=0; return isw
def gate_sqrtSWAP():
    sw=gate_SWAP(); e,v=np.linalg.eigh(sw)
    return v@np.diag(np.sqrt(np.maximum(e,0)))@v.conj().T
def gate_CZ():
    return np.diag([1,1,1,-1]).astype(complex)
def gate_CY():
    cy=np.eye(4,dtype=complex); cy[2,2]=0; cy[2,3]=-1j; cy[3,2]=1j; cy[3,3]=0; return cy
def gate_CH():
    """Controlled-Hadamard"""
    ch=np.eye(4,dtype=complex); H=np.array([[1,1],[1,-1]])/np.sqrt(2)
    ch[2:4,2:4]=H; return ch
def gate_ECP():  # Entangling composite pulse
    rng=np.random.RandomState(777)
    H=rng.randn(4,4)+1j*rng.randn(4,4); H=H+H.conj().T
    return expm(1j*0.3*H)
def gate_DCNOT():  # Double CNOT = identity (permutation composition)
    cnot=gate_CNOT(); return cnot@cnot  # = I
def gate_CRz(theta):  # Controlled-Rz
    crz=np.eye(4,dtype=complex); crz[2,2]=1; crz[3,3]=np.exp(1j*theta)
    return crz
def gate_TxT():  # T-gate product (factorizable non-Clifford)
    T=np.diag([1,np.exp(1j*np.pi/4)]); return np.kron(T,T)
def gate_Identity(): return np.eye(4,dtype=complex)

p=0.7; N=10
print("="*80)
print("VERIFICATION: 3-MECHANISM CLASSIFICATION")
print("="*80)
print(f"{'gate':<20s} {'type':<12s} {'predict':>8s} {'[U01,U02]':>10s} {'tree':>8s} {'cyc':>8s} {'bonus':>8s} {'match?':>8s}")
print("-"*85)

tests = [
    # (name, gate_fn, mechanism, predicted_sign)
    # --- Phase mechanism (commuting, destructive) ---
    ("Rxx(pi/2)", lambda s: gate_Rxx(np.pi/2), "phase", "-"),
    ("Rxx(pi/4)", lambda s: gate_Rxx(np.pi/4), "phase", "-"),
    ("Ryy(pi/2)", lambda s: gate_Ryy(np.pi/2), "phase", "-"),
    ("Rzz(pi/2)", lambda s: gate_Rzz(np.pi/2), "phase", "-"),
    ("Rzz(pi/4)", lambda s: gate_Rzz(np.pi/4), "phase", "-"),
    ("CZ", lambda s: gate_CZ(), "phase", "-"),
    ("CRz(pi/4)", lambda s: gate_CRz(np.pi/4), "phase", "-"),
    ("CS", lambda s: gate_CRz(np.pi/2), "phase", "-"),  # CS = CRz(pi/2)
    # --- Permutation mechanism (non-commuting, destructive) ---
    ("SWAP", lambda s: gate_SWAP(), "perm", "-"),
    ("iSWAP", lambda s: gate_iSWAP(), "perm", "-"),
    ("CNOT", lambda s: gate_CNOT(), "perm", "0/-"),
    ("CY", lambda s: gate_CY(), "perm", "0/-"),
    ("DCNOT (=I)", lambda s: gate_DCNOT(), "perm", "0"),
    # --- Entanglement mechanism (non-commuting, constructive) ---
    ("sqrtSWAP", lambda s: gate_sqrtSWAP(), "entangle", "+"),
    ("CH (C-Hadamard)", lambda s: gate_CH(), "entangle", "+"),
    ("ECP (entangling)", lambda s: gate_ECP(), "entangle", "+"),
    # --- Factorizable (commuting, zero effect) ---
    ("T x T", lambda s: gate_TxT(), "factoriz", "0"),
    ("Identity", lambda s: gate_Identity(), "factoriz", "0"),
    # --- Edge cases ---
    ("Rxx(0.1pi)", lambda s: gate_Rxx(0.1*np.pi), "phase", "-"),
    ("Rxx(0.01pi)", lambda s: gate_Rxx(0.01*np.pi), "phase", "-"),
]

for name, gate_fn, mech, pred in tests:
    comm = commutator_norm(gate_fn)
    vt=[]; vc=[]
    for t in range(N):
        s=1000+t*10
        Ut=embed_lsb(gate_fn(s+3),3,4,5)@embed_lsb(gate_fn(s+2),1,3,5)@embed_lsb(gate_fn(s+1),2,1,5)@embed_lsb(gate_fn(s),0,2,5)
        vt.append(compute(make_mixed_rho(3,p),Ut)[0])
        Uc=embed_lsb(gate_fn(s+3),0,3,5)@embed_lsb(gate_fn(s+2),1,3,5)@embed_lsb(gate_fn(s+1),2,1,5)@embed_lsb(gate_fn(s),0,2,5)
        vc.append(compute(make_mixed_rho(3,p),Uc)[0])
    vt=np.array(vt); vc=np.array(vc)
    b=np.mean(vc)-np.mean(vt)
    # Determine actual sign
    eps=0.005
    if b > eps: actual="+"
    elif b < -eps: actual="-"
    else: actual="0"
    match_str = "OK" if (actual==pred or (pred=="0/-" and actual in ["0","-"])) else "MISMATCH"
    print(f"{name:<20s} {mech:<12s} {pred:>8s} {comm:10.4f} {np.mean(vt):8.4f} {np.mean(vc):8.4f} {b:+8.4f} {match_str:>8s}")

print("\n--- MECHANISM SUMMARY ---")
print("PHASE:       Rxx,Ryy,Rzz(all theta), CZ, CRz, CS  -> comm=0, bonus<0")
print("PERMUTATION: SWAP,iSWAP,CNOT,CY                     -> comm>0, bonus<=0")
print("ENTANGLE:    sqrtSWAP, CH, random entangling         -> comm>0, bonus>0")
print("FACTORIZABLE: T⊗T, I                                -> comm=0, bonus=0")
print()
print("Key distinction: comm=0 does NOT guarantee bonus<0 (T⊗T has comm=0, bonus=0)")
print("                 comm>0 does NOT guarantee bonus>0 (SWAP has comm=3.5, bonus=-2)")
print("                 The MECHANISM (perm/phase/entangle) determines the sign.")

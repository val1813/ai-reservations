"""
B+D: Gate interference classification.
Systematic scan: Pauli rotations -> Clifford -> non-Clifford.
Map QCMI bonus vs commutator norm vs gate type.
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
    return (SR+SQE-Sall)-(SR+SQ-SRQ)

def commutator_norm(U_fn, seed=99):
    """||[U01, U02]|| for gates sharing qubit 0."""
    U01 = np.kron(U_fn(seed), np.eye(2))
    P = np.zeros((8,8), dtype=complex)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                P[i*4+k*2+j, i*4+j*2+k] = 1.0
    U02 = P.conj().T @ np.kron(U_fn(seed+100), np.eye(2)) @ P
    return np.linalg.norm(U01@U02 - U02@U01)

# Gate factory registry
pauli = {
    'I': np.eye(2), 'X': np.array([[0,1],[1,0]]),
    'Y': np.array([[0,-1j],[1j,0]]), 'Z': np.array([[1,0],[0,-1]])
}

def make_Pauli_rotation(P_label, theta):
    """exp(-i*theta/2 * P⊗P). P_label in {'X','Y','Z'}."""
    P = pauli[P_label]
    H = np.kron(P, P)
    return expm(-0.5j * theta * H)

def make_CNOT():
    cnot = np.zeros((4,4), dtype=complex)
    cnot[0,0]=cnot[1,1]=cnot[2,3]=cnot[3,2]=1.0
    return cnot

def make_SWAP():
    sw = np.zeros((4,4), dtype=complex)
    sw[0,0]=sw[3,3]=1.0; sw[1,2]=sw[2,1]=1.0
    return sw

def make_CZ():
    cz = np.diag([1,1,1,-1])
    return cz.astype(complex)

def make_iSWAP():
    isw = np.eye(4, dtype=complex)
    isw[1,2]=1j; isw[2,1]=1j; isw[1,1]=0; isw[2,2]=0
    return isw

def make_sqrt_SWAP():
    sw = make_SWAP()
    # sqrt via eigen-decomposition
    eigvals, eigvecs = np.linalg.eigh(sw)
    return eigvecs @ np.diag(np.sqrt(np.maximum(eigvals, 0))) @ eigvecs.conj().T

def make_T_gate_2q():
    """T⊗T (non-Clifford)"""
    T = np.diag([1, np.exp(1j*np.pi/4)])
    return np.kron(T, T)

def make_CS():
    """Controlled-S gate (Clifford)"""
    cs = np.eye(4, dtype=complex)
    cs[3,3] = 1j
    return cs

def make_CCZ_3q_reduced():
    """Random non-Clifford 2q gate: exp(i*H_random)"""
    rng = np.random.RandomState(42)
    H = rng.randn(4,4)+1j*rng.randn(4,4); H=H+H.conj().T
    return expm(1j*0.5*H)

def make_random_nonClifford(alpha, seed):
    rng = np.random.RandomState(seed)
    H = rng.randn(4,4)+1j*rng.randn(4,4); H=H+H.conj().T
    return expm(1j*alpha*H)

# Scan
N_trials = 15
p = 0.7

print("="*80)
print("GATE INTERFERENCE CLASSIFICATION MAP")
print("="*80)

# ---- Pauli rotation scan (XX, YY, ZZ at various angles) ----
print("\n--- Pauli rotations: XX, YY, ZZ (theta scan) ---")
print(f"{'gate':>16s} {'theta/pi':>10s} {'[U01,U02]':>12s} {'tree':>10s} {'cycle':>10s} {'bonus':>10s}")
print("-"*70)

for label in ['X', 'Y', 'Z']:
    for theta_frac in [0.1, 0.25, 0.5, 0.75, 1.0]:
        theta = theta_frac * np.pi
        def make_fn(l=label, t=theta):
            return lambda s: make_Pauli_rotation(l, t)
        gate_fn = make_fn()
        comm = commutator_norm(gate_fn)

        vt=[]; vc=[]
        for t in range(N_trials):
            s = 1000+t*10
            Ut=embed_lsb(gate_fn(s+3),3,4,5)@embed_lsb(gate_fn(s+2),1,3,5)@embed_lsb(gate_fn(s+1),2,1,5)@embed_lsb(gate_fn(s),0,2,5)
            vt.append(compute(make_mixed_rho(3,p),Ut))
            Uc=embed_lsb(gate_fn(s+3),0,3,5)@embed_lsb(gate_fn(s+2),1,3,5)@embed_lsb(gate_fn(s+1),2,1,5)@embed_lsb(gate_fn(s),0,2,5)
            vc.append(compute(make_mixed_rho(3,p),Uc))
        vt=np.array(vt); vc=np.array(vc)
        b=np.mean(vc)-np.mean(vt)
        print(f"{label:>16s} {theta_frac:10.2f} {comm:12.4f} {np.mean(vt):10.4f} {np.mean(vc):10.4f} {b:+10.4f}")

# ---- Clifford vs non-Clifford discrete gates ----
print(f"\n--- Discrete gates: Clifford hierarchy ---")
print(f"{'gate':>16s} {'Clifford?':>10s} {'[U01,U02]':>12s} {'tree':>10s} {'cycle':>10s} {'bonus':>10s}")
print("-"*70)

for label, gate_fn, is_clifford in [
    ("CNOT", lambda s: make_CNOT(), "YES"),
    ("SWAP", lambda s: make_SWAP(), "YES"),
    ("CZ", lambda s: make_CZ(), "YES"),
    ("iSWAP", lambda s: make_iSWAP(), "YES"),
    ("sqrtSWAP", lambda s: make_sqrt_SWAP(), "YES"),
    ("CS", lambda s: make_CS(), "YES"),
    ("T x T", lambda s: make_T_gate_2q(), "NO"),
    ("rand NC a=0.3", lambda s: make_random_nonClifford(0.3, s), "NO"),
    ("rand NC a=0.5", lambda s: make_random_nonClifford(0.5, s), "NO"),
]:
    comm = commutator_norm(gate_fn)
    vt=[]; vc=[]
    for t in range(N_trials):
        s = 1000+t*10
        Ut=embed_lsb(gate_fn(s+3),3,4,5)@embed_lsb(gate_fn(s+2),1,3,5)@embed_lsb(gate_fn(s+1),2,1,5)@embed_lsb(gate_fn(s),0,2,5)
        vt.append(compute(make_mixed_rho(3,p),Ut))
        Uc=embed_lsb(gate_fn(s+3),0,3,5)@embed_lsb(gate_fn(s+2),1,3,5)@embed_lsb(gate_fn(s+1),2,1,5)@embed_lsb(gate_fn(s),0,2,5)
        vc.append(compute(make_mixed_rho(3,p),Uc))
    vt=np.array(vt); vc=np.array(vc)
    b=np.mean(vc)-np.mean(vt)
    print(f"{label:>16s} {is_clifford:>10s} {comm:12.4f} {np.mean(vt):10.4f} {np.mean(vc):10.4f} {b:+10.4f}")

print("\n=== CLASSIFICATION RULE ===")
print("Clifford gates: [U01,U02]=0 → bonus ≤ 0 (destructive/null)")
print("Non-Clifford gates: [U01,U02]>0 → bonus > 0 (constructive)")

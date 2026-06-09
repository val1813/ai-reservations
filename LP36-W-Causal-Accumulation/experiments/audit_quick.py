"""Quick audit tests for LP37 interferometer hypothesis."""
import numpy as np
from scipy.linalg import expm
import sys
sys.setrecursionlimit(10000)

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

# Gates
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

def make_weak_CNOT(theta):
    H_cnot = np.zeros((4,4), dtype=complex)
    H_cnot[2,3] = H_cnot[3,2] = 1.0
    return expm(-0.5j * theta * H_cnot)

def make_CZ():
    CZ = np.eye(4, dtype=complex)
    CZ[3,3] = -1.0
    return CZ

def make_SWAP():
    SWAP = np.zeros((4,4), dtype=complex)
    SWAP[0,0]=SWAP[1,2]=SWAP[2,1]=SWAP[3,3]=1.0
    return SWAP

p = 0.7

# Build helpers
def build_tree_nE3(gfn):
    return (embed_lsb(gfn(),3,4,5)@embed_lsb(gfn(),1,3,5)@embed_lsb(gfn(),2,1,5)@embed_lsb(gfn(),0,2,5))

def build_tree_nE3_noEE(gfn):
    return (embed_lsb(gfn(),1,3,5)@embed_lsb(gfn(),2,1,5)@embed_lsb(gfn(),0,2,5))

def build_cycle_nE2(gfn):
    return (embed_lsb(gfn(),0,3,4)@embed_lsb(gfn(),1,3,4)@embed_lsb(gfn(),2,1,4)@embed_lsb(gfn(),0,2,4))

def build_cycle_nE3_spec(gfn):
    return (embed_lsb(gfn(),0,3,5)@embed_lsb(gfn(),1,3,5)@embed_lsb(gfn(),2,1,5)@embed_lsb(gfn(),0,2,5))

print('='*70)
print('TEST 1: Spectator E qubit — does n_E matter?')
print('='*70)
for label, gfn in [('CNOT', make_CNOT), ('XX(pi/2)', lambda: make_XX(np.pi/2)),
                    ('Haar', lambda: make_rand_Haar(999))]:
    U2 = build_cycle_nE2(gfn)
    q2 = compute(make_mixed_rho(2,p), U2)[0]
    U3 = np.kron(U2, np.eye(2))
    q3 = compute(make_mixed_rho(3,p), U3)[0]
    ok = 'OK' if abs(q2-q3) < 1e-4 else 'CONFOUND!!'
    print(f'  {label:15s}: n_E=2 → {q2:.6f}  |  n_E=3(spec) → {q3:.6f}  |  {ok}')

print()
print('='*70)
print('TEST 2: Tree E-E gate — does E2-E3 add spurious QCMI?')
print('='*70)
for label, gfn in [('CNOT', make_CNOT), ('XX(pi/2)', lambda: make_XX(np.pi/2)),
                    ('XX(pi/4)', lambda: make_XX(np.pi/4)),
                    ('ZZ(pi/2)', lambda: make_ZZ(np.pi/2)),
                    ('Haar', lambda: make_rand_Haar(999))]:
    Ut_ee = build_tree_nE3(gfn)
    Ut_noee = build_tree_nE3_noEE(gfn)
    q_ee = compute(make_mixed_rho(3,p), Ut_ee)[0]
    q_noee = compute(make_mixed_rho(3,p), Ut_noee)[0]
    print(f'  {label:15s}: with E2-E3={q_ee:.4f}  without={q_noee:.4f}  delta={q_ee-q_noee:+.4f}')

print()
print('='*70)
print('TEST 3: Fair comparison — BOTH n_E=3, tree vs cycle')
print('='*70)
print('Tree:  Q_a-E1, E1-Q_b, Q_b-E2, E2-E3  (3Q-E+1E-E, b1=0)')
print('Cycle: Q_a-E1, E1-Q_b, Q_b-E2, E2-Q_a  (4Q-E, E3 spectator, b1=1)')
for label, gfn in [('CNOT', make_CNOT), ('XX(pi/2)', lambda: make_XX(np.pi/2)),
                    ('XX(pi/4)', lambda: make_XX(np.pi/4)),
                    ('ZZ(pi/2)', lambda: make_ZZ(np.pi/2)),
                    ('Haar', lambda: make_rand_Haar(999)),
                    ('CZ', make_CZ), ('SWAP', make_SWAP)]:
    Ut = build_tree_nE3(gfn)
    Uc = build_cycle_nE3_spec(gfn)
    qt = compute(make_mixed_rho(3,p), Ut)[0]
    qc = compute(make_mixed_rho(3,p), Uc)[0]
    bonus = qc - qt
    print(f'  {label:15s}: tree={qt:.4f}  cycle={qc:.4f}  bonus={bonus:+.4f}')

print()
print('='*70)
print('TEST 4: Weak CNOT — saturation vs no-interference')
print('='*70)
for theta in [0.05, 0.10, 0.20, 0.50, 1.00]:
    gfn = lambda: make_weak_CNOT(theta)
    Ut = build_tree_nE3(gfn)
    Uc = build_cycle_nE2(gfn)
    qt = compute(make_mixed_rho(3,p), Ut)[0]
    qc = compute(make_mixed_rho(2,p), Uc)[0]
    print(f'  weakCNOT theta={theta:.2f}: tree={qt:.4f}  cycle={qc:.4f}  bonus={qc-qt:+.4f}')

print()
print('='*70)
print('TEST 5: Reproduce XX(pi/2) tree=2.0 cycle=1.0')
print('='*70)
gfn = lambda: make_XX(np.pi/2)
Ut = build_tree_nE3(gfn)
Uc = build_cycle_nE2(gfn)
qt, SRt, SQt, SRQt = compute(make_mixed_rho(3,p), Ut)
qc, SRc, SQc, SRQc = compute(make_mixed_rho(2,p), Uc)
print(f'  Tree:  QCMI={qt:.6f}  S(R)={SRt:.6f}  S(Q)={SQt:.6f}  S(RQ)={SRQt:.6f}')
print(f'  Cycle: QCMI={qc:.6f}  S(R)={SRc:.6f}  S(Q)={SQc:.6f}  S(RQ)={SRQc:.6f}')
IRQt = SRt + SQt - SRQt
IRQc = SRc + SQc - SRQc
print(f'  Tree  4-I(RQ)={4-IRQt:.6f}  (should = QCMI={qt:.6f})')
print(f'  Cycle 4-I(RQ)={4-IRQc:.6f}  (should = QCMI={qc:.6f})')

print()
print('='*70)
print('TEST 6: XX(theta) scan with SAME n_E=3')
print('='*70)
print('If bonus flips when controlling n_E, the interferometer claim collapses.')
for theta in [0.05, 0.10, 0.20, 0.50, 1.00, np.pi/4, np.pi/2]:
    gfn = lambda: make_XX(theta)
    Ut = build_tree_nE3(gfn)
    Uc = build_cycle_nE3_spec(gfn)
    qt = compute(make_mixed_rho(3,p), Ut)[0]
    qc = compute(make_mixed_rho(3,p), Uc)[0]
    print(f'  XX(theta={theta:.2f}): tree={qt:.4f}  cycle={qc:.4f}  bonus={qc-qt:+.4f}')

print()
print('='*70)
print('TEST 7: What drives the tree QCMI?')
print('='*70)
print('Compare: 3-gate tree(noEE) vs 4-gate tree(with EE) vs cycle(n_E=3)')
gfn = lambda: make_XX(np.pi/2)
Ut_noee = build_tree_nE3_noEE(gfn)
Ut_ee = build_tree_nE3(gfn)
Uc = build_cycle_nE3_spec(gfn)
q_noee = compute(make_mixed_rho(3,p), Ut_noee)[0]
q_ee = compute(make_mixed_rho(3,p), Ut_ee)[0]
q_c = compute(make_mixed_rho(3,p), Uc)[0]
print(f'  Tree(3 Q-E gates, no EE): {q_noee:.4f}')
print(f'  Tree(3 Q-E + 1 E-E):      {q_ee:.4f}')
print(f'  Cycle(4 Q-E gates):       {q_c:.4f}')
print(f'  Interpretation: E-E gate contributes {q_ee-q_noee:+.4f} to tree QCMI')
print(f'  If cycle had same E-E gate: cycle QCMI would be ~{q_c+(q_ee-q_noee):.4f}')
print(f'  True bonus (same n_E, same gate types): {q_c-q_noee:+.4f}')
print()
print('NOTE: Original experiment bonus = cycle(n_E=2) - tree(n_E=3, with EE)')
print(f'  Original bonus = {compute(make_mixed_rho(2,p), build_cycle_nE2(gfn))[0]:.4f} - {q_ee:.4f}')
print(f'                  = {compute(make_mixed_rho(2,p), build_cycle_nE2(gfn))[0]-q_ee:+.4f}')
print(f'  Fair bonus     = {q_c:.4f} - {q_noee:.4f} = {q_c-q_noee:+.4f}')

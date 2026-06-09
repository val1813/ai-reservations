"""
Inspector audit verification script for LP37 "causal ring = quantum interferometer" hypothesis.

Tests:
  1. Spectator E qubit: does adding an idle E qubit change QCMI?
  2. E-E gate contribution: does the tree's extra E-E gate inflate its QCMI?
  3. Weak CNOT: saturation vs no-interference discrimination
  4. Commuting gate scan: is bonus always negative for ALL commuting gates?
  5. Fixed-n_E comparison: tree vs cycle with SAME E qubit count
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

def make_YY(theta):
    sy = np.array([[0,-1j],[1j,0]], dtype=complex)
    return expm(-0.5j * theta * np.kron(sy,sy))

def make_XY(theta):
    sx = np.array([[0,1],[1,0]], dtype=complex)
    sy = np.array([[0,-1j],[1j,0]], dtype=complex)
    return expm(-0.5j * theta * np.kron(sx,sy))

def make_rand_Haar(seed):
    rng = np.random.RandomState(seed)
    A = rng.randn(4,4)+1j*rng.randn(4,4)
    Q,R = np.linalg.qr(A)
    return Q

def make_weak_Haar(alpha, seed):
    rng = np.random.RandomState(seed)
    H = rng.randn(4,4)+1j*rng.randn(4,4); H = H+H.conj().T
    return expm(1j*alpha*H)

def make_weak_CNOT(theta):
    """Partial CNOT: exp(-i*theta*H_CNOT) where H_CNOT = |1><1| ⊗ X"""
    H_cnot = np.zeros((4,4), dtype=complex)
    H_cnot[2,3] = H_cnot[3,2] = 1.0
    return expm(-0.5j * theta * H_cnot)

def make_SWAP():
    SWAP = np.zeros((4,4), dtype=complex)
    SWAP[0,0]=SWAP[1,2]=SWAP[2,1]=SWAP[3,3]=1.0
    return SWAP

def make_CZ():
    CZ = np.eye(4, dtype=complex)
    CZ[3,3] = -1.0
    return CZ

def make_iSWAP():
    """iSWAP = exp(i*pi/4*(XX+YY))"""
    sx = np.array([[0,1],[1,0]], dtype=complex)
    sy = np.array([[0,-1j],[1j,0]], dtype=complex)
    H = np.kron(sx,sx) + np.kron(sy,sy)
    return expm(0.25j * np.pi * H)

def build_cycle(U_fn, seed, n_E=2):
    """Build 4-gate cycle on n_qe = 2+n_E qubits.
    Qubits: 0=Q_a, 1=Q_b, 2=E2, 3=E1, 4=E3(if n_E=3, spectator)
    For n_E=3: gate on E2-E3 added at position 5 as spectator gate.
    """
    if n_E == 2:
        Uc = (embed_lsb(U_fn(seed+3), 0, 3, 4)
            @ embed_lsb(U_fn(seed+2), 1, 3, 4)
            @ embed_lsb(U_fn(seed+1), 2, 1, 4)
            @ embed_lsb(U_fn(seed), 0, 2, 4))
    elif n_E == 3:
        # E2(2)-E3(4) spectator gate, same as tree's E2-E3 gate
        Uc = (embed_lsb(U_fn(seed+4), 2, 4, 5)   # E2-E3 spectator (matches tree)
            @ embed_lsb(U_fn(seed+3), 0, 3, 5)   # Q_a-E1
            @ embed_lsb(U_fn(seed+2), 1, 3, 5)   # Q_b-E1
            @ embed_lsb(U_fn(seed+1), 2, 1, 5)   # E2-Q_b
            @ embed_lsb(U_fn(seed), 0, 2, 5))    # Q_a-E2
    return Uc

def build_tree(U_fn, seed, n_E=3):
    """Build 4-gate tree on n_qe = 2+n_E qubits.
    Qubits: 0=Q_a, 1=Q_b, 2=E1, 3=E2, 4=E3
    """
    Ut = (embed_lsb(U_fn(seed+3), 3, 4, 5)   # E2-E3
        @ embed_lsb(U_fn(seed+2), 1, 3, 5)    # Q_b-E2
        @ embed_lsb(U_fn(seed+1), 2, 1, 5)    # E1-Q_b
        @ embed_lsb(U_fn(seed), 0, 2, 5))     # Q_a-E1
    return Ut

def test_commutativity(gate_fn):
    """Test if U_01 and U_02 commute (share qubit 0)."""
    U01 = np.kron(gate_fn(99), np.eye(2))
    P = np.zeros((8,8), dtype=complex)
    for i in range(2):
        for j in range(2):
            for k in range(2):
                idx_in = i*4+j*2+k
                idx_out = i*4+k*2+j
                P[idx_out, idx_in] = 1.0
    U02 = P.conj().T @ np.kron(gate_fn(199), np.eye(2)) @ P
    return np.linalg.norm(U01@U02 - U02@U01)

def run_scan(gate_label, gate_fn, p=0.7, N=40):
    """Run tree (n_E=3) vs cycle (n_E=2) scan - original experiment."""
    vals_tree=[]; vals_cycle=[]
    for t in range(N):
        s=1000+t*10
        Uc = build_cycle(gate_fn, s, n_E=2)
        vals_cycle.append(compute(make_mixed_rho(2, p), Uc)[0])
        Ut = build_tree(gate_fn, s, n_E=3)
        vals_tree.append(compute(make_mixed_rho(3, p), Ut)[0])
    vt=np.array(vals_tree); vc=np.array(vals_cycle)
    bonus=np.mean(vc)-np.mean(vt)
    se=np.sqrt(np.var(vc)+np.var(vt))/np.sqrt(N)
    sig=abs(bonus)/max(se,1e-15)
    return np.mean(vt), np.mean(vc), bonus, sig


print("="*70)
print("AUDIT TEST 1: Spectator E qubit - does n_E affect QCMI?")
print("="*70)
print("If adding a spectator E3 (no gate acts on it) changes QCMI,")
print("then the tree (n_E=3) vs cycle (n_E=2) comparison is confounded.")
print()

p = 0.7
for label, fn in [("CNOT", lambda s: make_CNOT()),
                   ("XX(pi/2)", lambda s: make_XX(np.pi/2)),
                   ("Haar", lambda s: make_rand_Haar(s))]:
    # Cycle with n_E=2 (original)
    Uc2 = build_cycle(fn, 5000, n_E=2)
    qcmi2 = compute(make_mixed_rho(2, p), Uc2)[0]

    # Cycle with n_E=3, E3 as TRUE spectator (NO gate on E3 at all)
    # Build cycle identical to n_E=2 but with extra dimension for spectator
    Uc3_spec = build_cycle(fn, 5000, n_E=2)  # same gates
    Uc3_spec = np.kron(Uc3_spec, np.eye(2))   # tensor with identity on E3
    qcmi3_spec = compute(make_mixed_rho(3, p), Uc3_spec)[0]

    print(f"  {label:20s}: n_E=2 → {qcmi2:.6f}  |  n_E=3(spec) → {qcmi3_spec:.6f}  |  diff={abs(qcmi2-qcmi3_spec):.2e}")
    if abs(qcmi2 - qcmi3_spec) > 1e-4:
        print(f"    *** SPECTATOR CHANGES QCMI! Confound confirmed for {label}")
    else:
        print(f"    Spectator does NOT change QCMI (as expected).")

print()
print("="*70)
print("AUDIT TEST 2: Fair tree-vs-cycle — same n_E, same #gates")
print("="*70)
print("Tree (n_E=3): Q_a-E1, E1-Q_b, Q_b-E2, E2-E3  (3 Q-E + 1 E-E)")
print("Cycle (n_E=3): Q_a-E1, E1-Q_b, Q_b-E2, E2-Q_a, E2-E3  (4 Q-E + 1 E-E)")
print("Cycle has EXTRA Q-E gate. But we test: does the E2-E3 gate")
print("in the tree inflate its QCMI, creating a spurious 'negative bonus'?")
print()

for label, fn in [("CNOT", lambda s: make_CNOT()),
                   ("XX(pi/2)", lambda s: make_XX(np.pi/2)),
                   ("XX(pi/4)", lambda s: make_XX(np.pi/4)),
                   ("ZZ(pi/2)", lambda s: make_ZZ(np.pi/2)),
                   ("Haar(weak 0.12)", lambda s: make_weak_Haar(0.12, s)),
                   ("Haar(full)", lambda s: make_rand_Haar(s))]:
    N = 20
    vals_t3 = []; vals_c3 = []
    for t in range(N):
        s = 5000 + t*10
        Ut3 = build_tree(fn, s, n_E=3)
        vals_t3.append(compute(make_mixed_rho(3, p), Ut3)[0])
        Uc3 = build_cycle(fn, s, n_E=3)  # cycle with E2-E3 spectator gate
        vals_c3.append(compute(make_mixed_rho(3, p), Uc3)[0])
    vt3 = np.mean(vals_t3); vc3 = np.mean(vals_c3)
    bonus3 = vc3 - vt3
    print(f"  {label:20s}: tree={vt3:.4f}  cycle={vc3:.4f}  bonus={bonus3:+.4f}")

print()
print("="*70)
print("AUDIT TEST 3: Weak CNOT scan — saturation vs no-interference")
print("="*70)
print("If CNOT tree=cycle is due to saturation (not 'no interference'),")
print("then weak CNOT (small theta) should show tree != cycle.")
print()

for theta in [0.01, 0.05, 0.10, 0.20, 0.50, 1.00, np.pi/2]:
    N = 40
    vals_t = []; vals_c = []
    for t in range(N):
        s = 3000 + t*10
        Uc2 = build_cycle(lambda sd: make_weak_CNOT(theta), s, n_E=2)
        vals_c.append(compute(make_mixed_rho(2, p), Uc2)[0])
        Ut3 = build_tree(lambda sd: make_weak_CNOT(theta), s, n_E=3)
        vals_t.append(compute(make_mixed_rho(3, p), Ut3)[0])
    vt = np.mean(vals_t); vc = np.mean(vals_c)
    bonus = vc - vt
    se = np.sqrt(np.var(vals_c)+np.var(vals_t))/np.sqrt(N)
    sig = abs(bonus)/max(se,1e-15)
    print(f"  weak CNOT theta={theta:5.2f}: tree={vt:.4f}  cycle={vc:.4f}  bonus={bonus:+7.4f}  {sig:.1f}σ")

print()
print("="*70)
print("AUDIT TEST 4: Systematic commuting gate scan")
print("="*70)
print("The 'interferometer' hypothesis predicts: ALL commuting→negative bonus,")
print("ALL non-commuting→positive bonus. Let's test edge cases.")
print()

for label, fn, desc in [
    ("CNOT", lambda s: make_CNOT(), "basis-aligned"),
    ("CZ", lambda s: make_CZ(), "controlled-Z, commuting?"),
    ("SWAP", lambda s: make_SWAP(), "SWAP, commuting?"),
    ("iSWAP", lambda s: make_iSWAP(), "iSWAP, non-commuting?"),
    ("XX(pi/8)", lambda s: make_XX(np.pi/8), "XX weak"),
    ("XX(pi/2)", lambda s: make_XX(np.pi/2), "XX strong"),
    ("ZZ(pi/8)", lambda s: make_ZZ(np.pi/8), "ZZ weak"),
    ("ZZ(pi/2)", lambda s: make_ZZ(np.pi/2), "ZZ strong"),
    ("YY(pi/8)", lambda s: make_YY(np.pi/8), "YY weak"),
    ("YY(pi/2)", lambda s: make_YY(np.pi/2), "YY strong"),
    ("XY(pi/8)", lambda s: make_XY(np.pi/8), "XY mixed"),
    ("XY(pi/2)", lambda s: make_XY(np.pi/2), "XY mixed"),
]:
    comm = test_commutativity(fn)
    is_comm = comm < 1e-10
    vt, vc, bonus, sig = run_scan(label, fn, p=p, N=30)
    pred = "NEG(bonus<0)" if is_comm else "POS(bonus>0)"
    match = "✓" if (is_comm and bonus < 0) or (not is_comm and bonus > 0) or (abs(bonus) < 3*max(sig, 0.001)) else "✗ MISMATCH"
    print(f"  {label:20s} comm={comm:.1e} [{pred}] tree={vt:.4f} cycle={vc:.4f} bonus={bonus:+7.4f} {sig:.1f}σ {match}")

print()
print("="*70)
print("AUDIT TEST 5: Bonus sign vs physical mechanism")
print("="*70)
print("If the interferometer analogy is correct, the 'phase difference'")
print("between paths should determine sign. For real gates (XX, ZZ),")
print("the phase is 0 or pi - still produces interference in quantum")
print("mechanics (e.g., Mach-Zehnder with pi phase shift).")
print()
print("Check: XX(pi/4)*XX(pi/4) = XX(pi/2). Do both show negative bonus?")
print("If XX(pi/4) bonus sign differs from XX(pi/2), interferometer analogy fails.")

vt, vc, bonus, sig = run_scan("XX(pi/4)", lambda s: make_XX(np.pi/4), p=p, N=40)
print(f"  XX(pi/4): tree={vt:.4f} cycle={vc:.4f} bonus={bonus:+.4f} {sig:.1f}σ")
vt, vc, bonus, sig = run_scan("XX(pi/2)", lambda s: make_XX(np.pi/2), p=p, N=40)
print(f"  XX(pi/2): tree={vt:.4f} cycle={vc:.4f} bonus={bonus:+.4f} {sig:.1f}σ")

print()
print("="*70)
print("AUDIT TEST 6: Does b1 truly matter? b1=0 vs b1=1 with CONTROLS")
print("="*70)
print("Compare: 3-gate tree (b1=0) vs 3-gate triangle (b1=1), same n_E=2")
print("Tree-3:  Q_a-E1, E1-Q_b, Q_b-E2  (3 Q-E gates, 4 nodes, b1=0)")
print("Cycle-3: Q_a-E1, E1-Q_b, Q_b-Q_a  (2 Q-E + 1 Q-Q gate, 3 nodes, b1=1)")
print()

def build_tree3(U_fn, seed):
    """3-gate tree: Q_a-E1, E1-Q_b, Q_b-E2, n_E=2"""
    return (embed_lsb(U_fn(seed+2), 2, 1, 4)   # Q_b-E2
          @ embed_lsb(U_fn(seed+1), 1, 3, 4)    # E1-Q_b
          @ embed_lsb(U_fn(seed), 0, 3, 4))     # Q_a-E1

def build_cycle3(U_fn, seed):
    """3-gate triangle: Q_a-E1, E1-Q_b, Q_b-Q_a, n_E=1"""
    return (embed_lsb(U_fn(seed+2), 1, 0, 3)   # Q_b-Q_a
          @ embed_lsb(U_fn(seed+1), 1, 2, 4)    # E1-Q_b (wait, n_qe=3? Let me fix)
          @ embed_lsb(U_fn(seed), 0, 2, 4))     # Q_a-E1

# Actually the triangle needs different n_qe. Let me skip this and focus on
# the most important test.

# Instead: compare 4-gate tree (n_E=3) vs 4-gate cycle with spectator (n_E=3)
# These have identical n_E and identical gate count
print("FAIR COMPARISON: Both n_E=3, both 4 gates:")
print("  Tree:  Q_a-E1, E1-Q_b, Q_b-E2, E2-E3  (b1=0, 3 Q-E + 1 E-E)")
print("  Cycle: Q_a-E1, E1-Q_b, Q_b-E2, E2-Q_a  (b1=1, 4 Q-E, E3 spectator)")
print()

for label, fn in [("CNOT", lambda s: make_CNOT()),
                   ("XX(pi/2)", lambda s: make_XX(np.pi/2)),
                   ("XX(pi/4)", lambda s: make_XX(np.pi/4)),
                   ("ZZ(pi/2)", lambda s: make_ZZ(np.pi/2)),
                   ("Haar(full)", lambda s: make_rand_Haar(s))]:
    N = 30
    vals_t = []; vals_c = []
    for t in range(N):
        s = 6000 + t*10
        # Tree: n_E=3 original
        Ut = build_tree(fn, s, n_E=3)
        vals_t.append(compute(make_mixed_rho(3, p), Ut)[0])
        # Cycle: n_E=3 with ONLY 4 Q-E gates, E3 as pure spectator (identity)
        # Same n_E, same #Q-E gates, but E3 doesn't participate in any gate
        Uc4 = (embed_lsb(fn(s+3), 0, 3, 5)   # Q_a-E1
             @ embed_lsb(fn(s+2), 1, 3, 5)   # Q_b-E1
             @ embed_lsb(fn(s+1), 2, 1, 5)   # E2-Q_b
             @ embed_lsb(fn(s), 0, 2, 5))    # Q_a-E2
        vals_c.append(compute(make_mixed_rho(3, p), Uc4)[0])
    vt = np.mean(vals_t); vc = np.mean(vals_c)
    bonus = vc - vt
    se = np.sqrt(np.var(vals_c)+np.var(vals_t))/np.sqrt(N)
    sig = abs(bonus)/max(se,1e-15)
    print(f"  {label:20s}: tree={vt:.4f}  cycle(spec)={vc:.4f}  bonus={bonus:+7.4f}  {sig:.1f}σ")

print()
print("="*70)
print("AUDIT TEST 7: Tree-only — does E-E gate add spurious QCMI?")
print("="*70)
print("Compare tree WITH E2-E3 gate vs tree WITHOUT E2-E3 gate.")
print("If the E2-E3 gate adds QCMI, the tree's QCMI is inflated,")
print("which would create a spurious negative bonus (tree > cycle).")
print()

for label, fn in [("CNOT", lambda s: make_CNOT()),
                   ("XX(pi/2)", lambda s: make_XX(np.pi/2)),
                   ("XX(pi/4)", lambda s: make_XX(np.pi/4)),
                   ("ZZ(pi/2)", lambda s: make_ZZ(np.pi/2)),
                   ("Haar(full)", lambda s: make_rand_Haar(s))]:
    N = 30
    vals_ee = []; vals_noee = []
    for t in range(N):
        s = 6000 + t*10
        # Tree WITH E2-E3 gate (original)
        Ut_ee = build_tree(fn, s, n_E=3)
        vals_ee.append(compute(make_mixed_rho(3, p), Ut_ee)[0])
        # Tree WITHOUT E2-E3 gate (only 3 Q-E gates, E3 pure spectator)
        Ut_noee = (embed_lsb(fn(s+2), 1, 3, 5)   # Q_b-E2
                 @ embed_lsb(fn(s+1), 2, 1, 5)    # E1-Q_b
                 @ embed_lsb(fn(s), 0, 2, 5))     # Q_a-E1
        vals_noee.append(compute(make_mixed_rho(3, p), Ut_noee)[0])
    vt_ee = np.mean(vals_ee); vt_noee = np.mean(vals_noee)
    diff = vt_ee - vt_noee
    print(f"  {label:20s}: tree(with E2-E3)={vt_ee:.4f}  tree(no E2-E3)={vt_noee:.4f}  E-E gate adds={diff:+.4f}")

print()
print("="*70)
print("SUMMARY: Key questions for the 'interferometer' hypothesis")
print("="*70)

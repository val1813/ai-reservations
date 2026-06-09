"""Thorough pointer basis verification: YY gate + multi-p + multi-N"""
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

sx = np.array([[0,1],[1,0]], dtype=complex)
sy = np.array([[0,-1j],[1j,0]], dtype=complex)
sz = np.array([[1,0],[0,-1]], dtype=complex)

def make_XX(t): return expm(-0.5j*t*np.kron(sx,sx))
def make_YY(t): return expm(-0.5j*t*np.kron(sy,sy))
def make_ZZ(t): return expm(-0.5j*t*np.kron(sz,sz))

p = 0.7; n_E = 2; nq = 4
n_pts = 80
phi_golden = np.pi * (3 - np.sqrt(5))

print("="*60)
print("POINTER BASIS VERIFICATION: XX, YY, ZZ + multi-p")
print("="*60)

configs = [
    ("XX(pi/2) [axis=x]", lambda: make_XX(np.pi/2), np.array([1,0,0])),
    ("YY(pi/2) [axis=y]", lambda: make_YY(np.pi/2), np.array([0,1,0])),
    ("ZZ(pi/2) [axis=z]", lambda: make_ZZ(np.pi/2), np.array([0,0,1])),
]

for label, fn, axis in configs:
    gate = fn()
    results = []
    for i in range(n_pts):
        y = 1 - (i/(n_pts-1))*2
        theta = np.arccos(np.clip(y,-1,1))
        phi = i * phi_golden
        R = su2_rotation(theta, phi); Rd = R.conj().T
        RE1 = embed_lsb_1q(R, 2, nq); RE2 = embed_lsb_1q(R, 3, nq)
        RE1d = embed_lsb_1q(Rd, 2, nq); RE2d = embed_lsb_1q(Rd, 3, nq)
        U_cycle = (embed_lsb(gate,0,3,nq)@embed_lsb(gate,1,3,nq)@embed_lsb(gate,2,1,nq)@embed_lsb(gate,0,2,nq))
        U_tot = RE1d @ RE2d @ U_cycle @ RE2 @ RE1
        rho = make_mixed_rho(n_E, p)
        qcmi = compute(rho, U_tot)
        nx=np.sin(theta)*np.cos(phi); ny=np.sin(theta)*np.sin(phi); nz=np.cos(theta)
        results.append((nx,ny,nz,qcmi))
    results=np.array(results)
    mi=np.argmin(results[:,3]); ma=np.argmax(results[:,3])
    mn=results[mi,:3]; mx=results[ma,:3]
    ang_min=np.degrees(np.arccos(np.clip(np.abs(np.dot(mn,axis)),-1,1)))
    ang_max=np.degrees(np.arccos(np.clip(np.abs(np.dot(mx,axis)),-1,1)))
    span=results[ma,3]-results[mi,3]
    print(f"\n{label}: span={span:.4f}")
    print(f"  min_n=({mn[0]:.3f},{mn[1]:.3f},{mn[2]:.3f}) ang_to_axis={ang_min:.1f}deg -> {'CONFIRMED' if ang_min<20 else 'WEAK' if ang_min<50 else 'REFUTED'}")
    print(f"  max_n=({mx[0]:.3f},{mx[1]:.3f},{mx[2]:.3f}) ang_to_axis={ang_max:.1f}deg -> {'ORTHOGONAL' if ang_max>70 else 'NOT'}")

print("\n=== Multi-p: XX(pi/2) ===")
for p_test in [0.5, 0.6, 0.7, 0.8, 0.9]:
    gate = make_XX(np.pi/2); axis = np.array([1,0,0])
    results = []
    for i in range(40):
        y=1-(i/39.0)*2; theta=np.arccos(np.clip(y,-1,1)); phi=i*phi_golden
        R=su2_rotation(theta,phi); Rd=R.conj().T
        RE1=embed_lsb_1q(R,2,nq); RE2=embed_lsb_1q(R,3,nq)
        RE1d=embed_lsb_1q(Rd,2,nq); RE2d=embed_lsb_1q(Rd,3,nq)
        U_cycle=(embed_lsb(gate,0,3,nq)@embed_lsb(gate,1,3,nq)@embed_lsb(gate,2,1,nq)@embed_lsb(gate,0,2,nq))
        U_tot=RE1d@RE2d@U_cycle@RE2@RE1
        rho=make_mixed_rho(n_E,p_test)
        qcmi=compute(rho,U_tot)
        nx=np.sin(theta)*np.cos(phi); ny=np.sin(theta)*np.sin(phi); nz=np.cos(theta)
        results.append((nx,ny,nz,qcmi))
    results=np.array(results)
    mi=np.argmin(results[:,3])
    mn=results[mi,:3]
    ang=np.degrees(np.arccos(np.clip(np.abs(np.dot(mn,axis)),-1,1)))
    print(f"p={p_test}: min_QCMI={results[mi,3]:.4f} ang_to_x={ang:.1f}deg -> {'CONFIRMED' if ang<20 else 'WEAK'}")

print("\nDone.")

"""
Settle two referee attacks computationally with an EXACT sparse site-basis solver.
ATTACK 1 (Ref C F1d): Is Re(C_{i!=j})=0 for ALL distances, or only odd? Is 10^-15 real?
ATTACK 2 (Ref A/B/C): Extract midchain beta at L=96,128 to test finite-size convergence.
"""
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.stats import linregress

def construct_h(L, alpha, J0=0.3):
    idx = np.arange(L)
    R = np.abs(idx[:,None]-idx[None,:]).astype(float)
    np.fill_diagonal(R, 1.0)
    h = J0/(R**alpha)
    np.fill_diagonal(h, 0.0)
    return h

def solve_ness_sparse(L, alpha, gamma_phi, J0=0.3, GL=1.0, GR=1.0, fL=0.65, fR=0.35):
    """Exact site-basis steady state of dC/dt: i[h,C] + 0.5{Gamma,C} + gamma_phi*offdiag(C) = source."""
    h = construct_h(L, alpha, J0)
    Gt = np.zeros(L); Gt[0]=GL; Gt[L-1]=GR
    Win = np.zeros(L); Win[0]=GL*fL; Win[L-1]=GR*fR
    rows=[]; cols=[]; vals=[]
    b = np.zeros(L*L, dtype=complex)
    hnz = [np.nonzero(h[i])[0] for i in range(L)]
    for i in range(L):
        for j in range(L):
            row = i*L+j
            diag = 0.5*(Gt[i]+Gt[j]) + (gamma_phi if i!=j else 0.0)
            rows.append(row); cols.append(row); vals.append(diag)
            for k in hnz[i]:
                rows.append(row); cols.append(k*L+j); vals.append(1j*h[i,k])
            for k in hnz[j]:
                rows.append(row); cols.append(i*L+k); vals.append(-1j*h[k,j])
            if i==j:
                b[row] = Win[i]
    A = sp.csr_matrix((vals,(rows,cols)), shape=(L*L,L*L), dtype=complex)
    C = spla.spsolve(A, b).reshape(L,L)
    return C

print("="*70)
print("ATTACK 1: Re(C) vs distance  [alpha=1.1, gamma_phi=0.5]")
print("="*70)
for L in [16,32]:
    C = solve_ness_sparse(L,1.1,0.5)
    m = L//2-1
    print(f"\n L={L}, reference row i={m}:")
    print(f"  {'dist':>5}{'parity':>8}{'|Re|':>14}{'|Im|':>14}")
    for r in range(1,7):
        j = m+r
        if j<L:
            par = 'odd' if r%2 else 'even'
            print(f"  {r:>5}{par:>8}{abs(C[m,j].real):>14.2e}{abs(C[m,j].imag):>14.2e}")
    print(f"  GLOBAL max|Re(offdiag)| = {np.max(np.abs(C.real - np.diag(np.diag(C.real)))):.3e}")

print()
print("="*70)
print("ATTACK 2: midchain beta convergence, gamma_phi=0.5")
print("  |C_mid|=|C_{L/2-1,L/2}| ~ L^-beta")
print("="*70)
alphas=[1.1,1.3,1.5,1.7,1.9]
Ls_small=[4,8,16,32,64]
Ls_big=[4,8,16,32,64,96,128]
for a in alphas:
    cmid={}
    for L in Ls_big:
        C = solve_ness_sparse(L,a,0.5)
        cmid[L]=abs(C[L//2-1,L//2])
    def fit(Ls):
        x=np.log(Ls); y=np.log([cmid[L] for L in Ls])
        s,i,r,p,se=linregress(x,y); return -s, r**2, se
    b5,r5,se5 = fit(Ls_small)
    b7,r7,se7 = fit(Ls_big)
    b_drop4,_,_ = fit([8,16,32,64,96,128])
    print(f" a={a}: beta(L<=64)={b5:.3f}({se5:.3f})  beta(L<=128)={b7:.3f}({se7:.3f})  beta(L8-128,drop L4)={b_drop4:.3f}   shift={b7-b5:+.3f}")

"""ATTACK 1 (Ref C F1d): Is Re(C_{i!=j})=0 for ALL distances or only odd? Dense solve, L<=48."""
import numpy as np
np.set_printoptions(suppress=True)

def construct_h(L, alpha, J0=0.3):
    idx=np.arange(L); R=np.abs(idx[:,None]-idx[None,:]).astype(float)
    np.fill_diagonal(R,1.0); h=J0/(R**alpha); np.fill_diagonal(h,0.0); return h

def solve_dense(L, alpha, gamma_phi, J0=0.3, GL=1.0, GR=1.0, fL=0.65, fR=0.35):
    h=construct_h(L,alpha,J0)
    Gt=np.zeros(L); Gt[0]=GL; Gt[L-1]=GR
    Win=np.zeros(L); Win[0]=GL*fL; Win[L-1]=GR*fR
    n=L*L; A=np.zeros((n,n),dtype=complex); b=np.zeros(n,dtype=complex)
    for i in range(L):
        for j in range(L):
            row=i*L+j
            A[row,row]+=0.5*(Gt[i]+Gt[j])+(gamma_phi if i!=j else 0.0)
            for k in range(L):
                if h[i,k]!=0: A[row,k*L+j]+=1j*h[i,k]
                if h[k,j]!=0: A[row,i*L+k]+=-1j*h[k,j]
            if i==j: b[row]=Win[i]
    return np.linalg.solve(A,b).reshape(L,L)

print("ATTACK 1: Re(C) vs distance  [alpha=1.1, gamma_phi=0.5] -- tests Ref C claim that only odd-distance is protected")
for L in [16,32,48]:
    C=solve_dense(L,1.1,0.5); m=L//2-1
    print(f"\n L={L}, ref row i={m}:   dist  parity     |Re|         |Im|")
    for r in range(1,8):
        j=m+r
        if j<L:
            print(f"            {r:>5} {'odd' if r%2 else 'even':>6} {abs(C[m,j].real):>12.2e} {abs(C[m,j].imag):>12.2e}")
    off=C.real-np.diag(np.diag(C.real))
    print(f"   GLOBAL max|Re(offdiag)|={np.max(np.abs(off)):.3e}   (max|Im offdiag|={np.max(np.abs(C.imag-np.diag(np.diag(C.imag)))):.3e})")

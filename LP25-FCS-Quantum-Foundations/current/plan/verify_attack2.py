"""
ATTACK 1b: Are ALL nearest-neighbor bonds C_{j,j+1} purely imaginary (not just midchain)?
ATTACK 2 : midchain beta at L=96,128 via fast Sylvester iteration. Tests finite-size convergence.
Eq: A C + C A^dag - gamma_phi (C - diag C) + S = 0,  A = i h - 0.5 Gamma.
Iterate Sylvester: (A-gp/2 I) C + C(A^dag-gp/2 I) = -S - gp diag(C_prev).
"""
import numpy as np
from scipy.linalg import solve_sylvester
from scipy.stats import linregress
import sys

def construct_h(L, alpha, J0=0.3):
    idx=np.arange(L); R=np.abs(idx[:,None]-idx[None,:]).astype(float)
    np.fill_diagonal(R,1.0); h=J0/(R**alpha); np.fill_diagonal(h,0.0); return h

def solve_syl(L, alpha, gamma_phi, J0=0.3, GL=1.0, GR=1.0, fL=0.65, fR=0.35, tol=1e-12, maxit=200):
    h=construct_h(L,alpha,J0)
    Gamma=np.zeros((L,L),dtype=complex); Gamma[0,0]=GL; Gamma[L-1,L-1]=GR
    A=1j*h-0.5*Gamma
    S=np.zeros((L,L),dtype=complex); S[0,0]=GL*fL; S[L-1,L-1]=GR*fR
    Asyl=A-0.5*gamma_phi*np.eye(L); Bsyl=A.conj().T-0.5*gamma_phi*np.eye(L)
    C=np.zeros((L,L),dtype=complex); dprev=np.zeros(L)
    for it in range(maxit):
        Q=-S-gamma_phi*np.diag(np.diag(C))
        C=solve_sylvester(Asyl,Bsyl,Q)
        d=np.real(np.diag(C))
        if np.max(np.abs(d-dprev))<tol: break
        dprev=d
    return C,it+1

print("ATTACK 1b: ALL nearest-neighbor bonds purely imaginary? max|Re(C_{j,j+1})| over j")
for (a,gp) in [(1.1,0.5),(1.5,0.5),(1.9,2.0),(1.3,0.1)]:
    C,it=solve_syl(32,a,gp)
    nn_re=np.max([abs(C[j,j+1].real) for j in range(31)])
    d2_re=np.max([abs(C[j,j+2].real) for j in range(30)])
    print(f"  a={a}, gp={gp}: max|Re(NN)|={nn_re:.2e}   max|Re(dist2)|={d2_re:.2e}   (iters={it})")

print()
print("ATTACK 2: midchain beta convergence (gamma_phi=0.5), |C_{L/2-1,L/2}| ~ L^-beta")
print(f"  {'alpha':>6}{'b(L<=64)':>11}{'b(L<=128)':>11}{'b(L16-128)':>12}{'shift_64to128':>14}")
alphas=[1.1,1.3,1.5,1.7,1.9]
Ls=[4,8,16,32,64,96,128]
rows=[]
for a in alphas:
    cmid={}
    for L in Ls:
        C,_=solve_syl(L,a,0.5); cmid[L]=abs(C[L//2-1,L//2])
    def fit(LL):
        x=np.log(LL); y=np.log([cmid[L] for L in LL]); s,i,r,p,se=linregress(x,y); return -s,se
    b64,se64=fit([4,8,16,32,64]); b128,se128=fit([4,8,16,32,64,96,128]); btail,_=fit([16,32,64,96,128])
    rows.append((a,b64,b128,btail))
    print(f"  {a:>6}{b64:>11.3f}{b128:>11.3f}{btail:>12.3f}{b128-b64:>+14.3f}")
import json
json.dump({"attack2":[{"alpha":r[0],"beta_L64":r[1],"beta_L128":r[2],"beta_tail16_128":r[3]} for r in rows]},
          open("referee_response_L128.json","w"),indent=2)
print("\nSaved -> referee_response_L128.json")

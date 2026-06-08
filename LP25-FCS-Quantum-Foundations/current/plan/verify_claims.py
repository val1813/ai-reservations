"""Verify manuscript numerical claims against actual data files.
Recomputes: dbeta/dmu slopes per gamma_phi, AIC for 3 functional forms.
"""
import json, numpy as np
from scipy.stats import linregress

fit = json.load(open('phase2_fit_results_FULL.json'))
alphas = [1.1, 1.3, 1.5, 1.7, 1.9]
gammas = [0.01, 0.1, 0.5, 1.0, 2.0]

print("="*70)
print("CLAIM 1: dbeta/dmu slopes (manuscript: -0.086 g0.1, -0.188 g0.5, -0.144 g2.0)")
print("  mu = 2*alpha-2 (Dhawan domain). Full-range linear fit beta vs mu.")
print("="*70)
for gp in gammas:
    mu = np.array([2*a-2 for a in alphas])
    beta = np.array([fit[f"{a}_{gp}"]["beta"] for a in alphas])
    s, i, r, p, se = linregress(mu, beta)
    print(f"  gamma_phi={gp:<5}: dbeta/dmu = {s:+.4f}  (R2={r**2:.4f})")

print()
print("  --- restricted to Dhawan domain alpha in {1.1,1.3,1.5} ---")
for gp in gammas:
    aa=[1.1,1.3,1.5]
    mu = np.array([2*a-2 for a in aa])
    beta = np.array([fit[f"{a}_{gp}"]["beta"] for a in aa])
    s, i, r, p, se = linregress(mu, beta)
    print(f"  gamma_phi={gp:<5}: dbeta/dmu = {s:+.4f}  (R2={r**2:.4f})")

print()
print("="*70)
print("CLAIM 2: AIC at gamma_phi=0.5 (manuscript: -29.1 [1/a], -19.6 [ln a], -23.9 [linear])")
print("="*70)
gp=0.5
x = np.array(alphas)
y = np.array([fit[f"{a}_{gp}"]["beta"] for a in alphas])
n=len(x)

def aic_c(y, yhat, k):
    rss = np.sum((y-yhat)**2)
    # AIC = n ln(RSS/n) + 2k ; AICc adds correction
    aic = n*np.log(rss/n) + 2*k
    aicc = aic + (2*k*(k+1))/(n-k-1) if n-k-1>0 else aic
    return aic, aicc, rss

# Model 1: beta = a/alpha + b  (k=2 params +variance? use k=params)
A1 = np.vstack([1/x, np.ones(n)]).T
c1,_,_,_ = np.linalg.lstsq(A1, y, rcond=None)
yh1 = A1@c1
# Model 2: beta = a ln(alpha)+b
A2 = np.vstack([np.log(x), np.ones(n)]).T
c2,_,_,_ = np.linalg.lstsq(A2, y, rcond=None)
yh2 = A2@c2
# Model 3: beta = m*alpha + c
A3 = np.vstack([x, np.ones(n)]).T
c3,_,_,_ = np.linalg.lstsq(A3, y, rcond=None)
yh3 = A3@c3
# Model 4: beta = a/alpha^2 + b/alpha + c (k=3)
A4 = np.vstack([1/x**2, 1/x, np.ones(n)]).T
c4,_,_,_ = np.linalg.lstsq(A4, y, rcond=None)
yh4 = A4@c4

for name,yh,k,c in [("1/alpha",yh1,2,c1),("ln alpha",yh2,2,c2),("linear",yh3,2,c3),("1/a^2+1/a",yh4,3,c4)]:
    aic,aicc,rss = aic_c(y,yh,k)
    print(f"  {name:<12}: AIC={aic:7.2f}  AICc={aicc:7.2f}  RSS={rss:.2e}  params={np.round(c,4)}")

print()
print(f"  1/alpha fit: a={c1[0]:.4f}, b={c1[1]:.4f}  (manuscript: a=0.8127, b=0.4218)")
print(f"  RMSE(1/alpha) = {np.sqrt(np.mean((y-yh1)**2)):.4f}  (manuscript: 0.015)")
print(f"  alpha_c (beta=1) = {c1[0]/(1-c1[1]):.4f}  (manuscript: 1.406)")

"""
Model selection + anti-correlation + kappa verification for PRL manuscript.
Reproducible source for all derived numbers in Sec III.B and III.C.

Inputs : phase2_fit_results_FULL.json, phase2_raw_results_FULL.json
Output : model_selection_results.json
Author : LP25 verification pass
Date   : 2026-06-03
"""
import json, numpy as np
from scipy.stats import linregress

fit = json.load(open('phase2_fit_results_FULL.json'))
raw = json.load(open('phase2_raw_results_FULL.json'))
alphas = [1.1, 1.3, 1.5, 1.7, 1.9]
gammas = [0.01, 0.1, 0.5, 1.0, 2.0]
J0 = 0.3

def fit_lin(basis, y):
    A = np.vstack(basis + [np.ones(len(y))]).T
    c, *_ = np.linalg.lstsq(A, y, rcond=None)
    yh = A @ c
    rss = float(np.sum((y - yh)**2))
    return c.tolist(), yh, rss

def info_crit(rss, n, k):
    # k = number of fitted parameters (excluding variance)
    aic = n*np.log(rss/n) + 2*k
    denom = n - k - 1
    aicc = aic + (2*k*(k+1))/denom if denom > 0 else float('inf')
    bic = n*np.log(rss/n) + k*np.log(n)
    return float(aic), float(aicc), float(bic)

out = {"model_selection": {}, "anti_correlation": {}, "kappa": {}}

# ---- Model selection per gamma_phi ----
for gp in gammas:
    x = np.array(alphas)
    y = np.array([fit[f"{a}_{gp}"]["beta"] for a in alphas])
    n = len(x)
    models = {
        "inv_alpha":   ([1/x],            2),   # a/alpha + b
        "ln_alpha":    ([np.log(x)],      2),   # a ln(alpha) + b
        "linear":      ([x],              2),   # m alpha + c
        "inv_alpha2":  ([1/x**2, 1/x],    3),   # a/alpha^2 + b/alpha + c
    }
    res = {}
    for name, (basis, k) in models.items():
        c, yh, rss = fit_lin(basis, y)
        aic, aicc, bic = info_crit(rss, n, k)
        ss_tot = float(np.sum((y - y.mean())**2))
        r2 = 1 - rss/ss_tot
        res[name] = {"params": [round(v,4) for v in c], "rss": rss,
                     "AIC": round(aic,2), "AICc": round(aicc,2), "BIC": round(bic,2),
                     "R2": round(r2,5), "RMSE": round(float(np.sqrt(rss/n)),4)}
    out["model_selection"][str(gp)] = res

# ---- Anti-correlation dbeta/dmu ----
for gp in gammas:
    full = {}
    for label, aa in [("full_range", alphas), ("dhawan_domain", [1.1,1.3,1.5])]:
        mu = np.array([2*a-2 for a in aa])
        beta = np.array([fit[f"{a}_{gp}"]["beta"] for a in aa])
        s, i, r, p, se = linregress(mu, beta)
        full[label] = {"slope": round(float(s),4), "intercept": round(float(i),4),
                       "R2": round(float(r**2),4), "std_err": round(float(se),4)}
    out["anti_correlation"][str(gp)] = full

# ---- kappa = |C_exact| / |C^(1)| at gamma_phi=0.5 ----
kappa_tab = {}
for r in raw:
    if abs(r['gamma_phi']-0.5) > 1e-9: continue
    L = r['L']; a = r['alpha']; D = r['diag_C']
    i, j = L//2-1, L//2
    h_mid = J0/abs(j-i)**a
    C1 = h_mid*abs(D[j]-D[i])/r['gamma_phi']
    kappa_tab[f"a{a}_L{L}"] = round(r['abs_C_mid']/C1, 4) if C1>0 else None
out["kappa"]["gamma_phi_0.5"] = kappa_tab
# summary
k32 = [v for k,v in kappa_tab.items() if k.endswith('_L32')]
k64 = [v for k,v in kappa_tab.items() if k.endswith('_L64')]
out["kappa"]["max_L32"] = max(k32); out["kappa"]["max_L64"] = max(k64)

json.dump(out, open('model_selection_results.json','w'), indent=2)

# ---- console summary ----
print("MODEL SELECTION (gamma_phi=0.5):")
for name, d in out["model_selection"]["0.5"].items():
    print(f"  {name:<11} AICc={d['AICc']:>8}  R2={d['R2']:.4f}  RMSE={d['RMSE']:.4f}  params={d['params']}")
print(f"\nALPHA_c (beta=1, gp=0.5): {out['model_selection']['0.5']['inv_alpha']['params'][0]/(1-out['model_selection']['0.5']['inv_alpha']['params'][1]):.4f}")
print("\nANTI-CORRELATION dbeta/dmu (full range):")
for gp in gammas:
    d = out["anti_correlation"][str(gp)]["full_range"]
    print(f"  gp={gp:<5} slope={d['slope']:+.4f}  R2={d['R2']:.4f}")
print(f"\nKAPPA: max(L=32)={out['kappa']['max_L32']}  max(L=64)={out['kappa']['max_L64']}")
print("\nSaved -> model_selection_results.json")

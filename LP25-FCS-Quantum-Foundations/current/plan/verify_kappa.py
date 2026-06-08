"""Verify kappa = |C_exact|/|C^(1)| where C^(1)_mid = h_mid*(D_j-D_i)/gamma_phi.
Manuscript claims kappa < 1.02 for L>=32 across all alpha (gamma_phi=0.5)."""
import json, numpy as np
raw = json.load(open('phase2_raw_results_FULL.json'))
J0=0.3
print(f"{'alpha':>6}{'gp':>6}{'L':>5}{'kappa':>10}")
for r in raw:
    if r['gamma_phi']!=0.5: continue
    L=r['L']; a=r['alpha']
    D=r['diag_C']
    i=L//2-1; j=L//2   # midchain pair C_{L/2-1,L/2}
    h_mid = J0/abs(j-i)**a  # |i-j|=1
    C1 = h_mid*abs(D[j]-D[i])/r['gamma_phi']
    kappa = r['abs_C_mid']/C1 if C1>0 else float('nan')
    if L>=16:
        print(f"{a:>6}{r['gamma_phi']:>6}{L:>5}{kappa:>10.4f}")

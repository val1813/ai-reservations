"""
CMB Mutual Information Angular Spectrum I_ell
CEP Prediction: slope change at ell ~ 200 (causal phase transition signature)
"""
import numpy as np
from scipy.special import eval_legendre
import camb
import json, os, sys

# Force UTF-8
sys.stdout.reconfigure(encoding='utf-8')

print("=" * 70)
print("CEP CMB I_ell Computation")
print("=" * 70)

# --- 1. Get Planck 2018 LCDM C_ell ---
print("\n[1/5] Computing LCDM C_ell (Planck 2018 best-fit)...")
pars = camb.set_params(H0=67.4, ombh2=0.0224, omch2=0.120, ns=0.965,
                        As=2.1e-9, tau=0.054, lmax=2500)
results = camb.get_results(pars)
powers = results.get_cmb_power_spectra(pars, CMB_unit='muK', raw_cl=True)
ells = np.arange(2, 2501)
Cl_TT = powers['total'][2:2501, 0]

print(f"   ell range: {ells[0]}-{ells[-1]}")
print(f"   C_ell at ell=200: {Cl_TT[198]:.1f} uK^2")

# --- 2. Correlation function rho(theta) ---
print("\n[2/5] Computing rho(theta) from C_ell (Legendre transform)...")
n_theta = 5000
theta = np.logspace(-3, 0.5, n_theta)
cos_theta = np.cos(theta)

# Recurrence for Legendre polynomials (vectorized)
P_ell = np.zeros((len(ells), n_theta))
P_ell[0, :] = 1.0
P_ell[1, :] = cos_theta
for idx in range(2, len(ells)):
    ell = ells[idx]
    P_ell[idx, :] = ((2*ell-1)*cos_theta*P_ell[idx-1, :] - (ell-1)*P_ell[idx-2, :]) / ell
    if idx % 500 == 0:
        print(f"   ... ell={ell}", end='\r')

print()
weights = (2*ells + 1) / (4*np.pi)
rho = np.sum(weights[:, np.newaxis] * Cl_TT[:, np.newaxis] * P_ell, axis=0)

sigma2 = rho[0]
print(f"   sigma^2 = rho(0) = {sigma2:.1f} uK^2")

# --- 3. Mutual information I(theta) ---
print("\n[3/5] Computing I(theta)...")
r2 = np.clip((rho / sigma2) ** 2, 0, 0.999999)
I_theta = -0.5 * np.log(1 - r2)
print(f"   I(theta) range: [{I_theta.min():.6f}, {I_theta.max():.6f}] nats")

# --- 4. I_ell ---
print("\n[4/5] Computing I_ell from I(theta)...")
I_ell_out = np.zeros(2000)
ell_out = np.arange(2, 2002)

for idx, ell in enumerate(ell_out):
    if idx % 200 == 0:
        print(f"   ... ell={ell}", end='\r')
    P_at_theta = eval_legendre(ell, cos_theta)
    integrand = I_theta * P_at_theta * np.sin(theta)
    I_ell_out[idx] = 2 * np.pi * np.trapz(integrand, theta)

print()

# --- 5. Slope analysis at ell ~ 200 ---
print("\n[5/5] Analyzing slope at ell ~ 200...")
dlnI = np.zeros(len(ell_out) - 10)
for i in range(5, len(ell_out) - 5):
    dlnI[i-5] = (np.log(I_ell_out[i+5]) - np.log(I_ell_out[i-5])) / \
                (np.log(ell_out[i+5]) - np.log(ell_out[i-5]))

window = 100
idx200 = 198
before = slice(max(0, idx200-window), idx200-10)
after = slice(idx200+10, min(len(dlnI), idx200+window))

slope_b = np.mean(dlnI[before])
slope_a = np.mean(dlnI[after])
change = slope_a - slope_b
sig = abs(change) / max(np.std(dlnI[before]), 1e-10)

print(f"\n   Slope before ell~200:  {slope_b:.4f}")
print(f"   Slope after  ell~200:  {slope_a:.4f}")
print(f"   Slope change:          {change:.4f}")
print(f"   Significance:          {sig:.1f} sigma")

dlnI_smooth = np.convolve(dlnI, np.ones(20)/20, mode='same')
min_idx = np.argmin(np.abs(dlnI_smooth[150:250]))
print(f"   Smoothed dlnI minimum near ell=200: at ell={150+min_idx}, val={dlnI_smooth[150+min_idx]:.4f}")

# --- Save ---
results = {
    'ells': ell_out.tolist(),
    'I_ell': I_ell_out.tolist(),
    'dlnI': dlnI.tolist(),
    'slope_before_200': float(slope_b),
    'slope_after_200': float(slope_a),
    'slope_change': float(change),
    'sigma': float(sig),
    'theta_deg': np.degrees(theta).tolist(),
    'I_theta': I_theta.tolist(),
    'rho_theta': rho.tolist(),
}

outdir = os.path.dirname(os.path.abspath(__file__))
outpath = os.path.join(outdir, 'cmb_Iell_results.json')
with open(outpath, 'w') as f:
    json.dump(results, f)

print(f"\nResults saved to {outpath}")

# --- Verdict ---
print("\n" + "=" * 70)
print("CEP PREDICTION CHECK")
print("=" * 70)
print(f"CEP predicts: slope change (causal phase transition) at ell ~ 200")
print(f"Data shows:   Delta(dlnI/dlnell) = {change:.4f}")
if abs(change) > 3 * max(np.std(dlnI[before]), 1e-10):
    print("VERDICT: *** Significant slope change -- CEP supported")
elif abs(change) > 1 * max(np.std(dlnI[before]), 1e-10):
    print("VERDICT: **  Marginal signal -- needs deeper analysis")
else:
    print("VERDICT: *   No significant slope change -- phase transition NOT detected at ell~200")
print("=" * 70)

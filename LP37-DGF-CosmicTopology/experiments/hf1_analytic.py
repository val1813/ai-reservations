#!/usr/bin/env python
"""
HF1: Analytic sensitivity of Minkowski functional V2 (genus) to beta1 enhancement.
No simulations needed — all from C_ell power spectrum and cosmic variance.
"""
import numpy as np

# ============================================================
# 1. CMB power spectrum (Planck 2018 best-fit LCDM, approximate)
# ============================================================
lmax = 2500
ells = np.arange(lmax + 1)
# Planck 2018 TT: A_s=2.1e-9, ns=0.965, tau=0.054
# Simplified model: Sachs-Wolfe + acoustic peaks envelope + damping
A_s, ns = 2.1e-9, 0.965
ell_pivot = 0.05  # Mpc^-1

# Approximate C_ell using fitting formula
cl_tt = np.zeros(lmax + 1)
# Low ell: Sachs-Wolfe plateau
cl_tt[2:30] = A_s * 2 * np.pi / (ells[2:30] * (ells[2:30] + 1))
# Mid ell: acoustic oscillations envelope
ell_mid = ells[30:2000]
cl_tt[30:2000] = A_s * (ell_mid / 200.0)**(ns - 1) / (ell_mid * (ell_mid + 1)) * 2 * np.pi
# Acoustic peak modulation (simplified)
cl_tt[30:2000] *= (1 + 0.5 * np.cos(2 * np.pi * ell_mid / 300)**2 *
                    np.exp(-0.5 * ((ell_mid - 800) / 300)**2))
# Damping tail
cl_tt[30:] *= np.exp(-0.5 * (ells[30:] / 1500)**2)
cl_tt[0] = 0; cl_tt[1] = 0

# Normalize to Planck 2018: C_ell ~ 6e-10 at ell=100 (rough)
cl_tt = cl_tt / cl_tt[100] * 6e-10

# ============================================================
# 2. Compute sigma0, sigma1 from C_ell
# ============================================================
prefactor = 1.0 / (4.0 * np.pi)
weights = 2 * ells + 1

sigma0_sq = prefactor * np.sum(weights * cl_tt)
sigma1_sq = prefactor * np.sum(weights * ells * (ells + 1) * cl_tt)
sigma0 = np.sqrt(sigma0_sq)
sigma1 = np.sqrt(sigma1_sq)
sigma_ratio = sigma1 / sigma0

print("=" * 60)
print("CMB Gaussian Field Properties (Planck 2018 LCDM)")
print("=" * 60)
print(f"  sigma0^2 = {sigma0_sq:.2e}")
print(f"  sigma1^2 = {sigma1_sq:.2e}")
print(f"  sigma1/sigma0 (genus amplitude factor) = {sigma_ratio:.2f}")

# ============================================================
# 3. DGF signal: beta1 enhancement in ell band 36-180 (1-5 deg)
# ============================================================
ell_dgf_min, ell_dgf_max = 36, 180

# Contribution of DGF band to sigma1^2
mask_dgf = (ells >= ell_dgf_min) & (ells <= ell_dgf_max)
sigma1_sq_dgf_band = prefactor * np.sum(weights[mask_dgf] *
    ells[mask_dgf] * (ells[mask_dgf] + 1) * cl_tt[mask_dgf])
sigma1_sq_total = sigma1_sq
fraction_dgf = sigma1_sq_dgf_band / sigma1_sq_total

print(f"\n  DGF target band: ell {ell_dgf_min}-{ell_dgf_max} (1-5 deg)")
print(f"  Fraction of sigma1^2 in DGF band: {fraction_dgf*100:.1f}%")

# DGF modifies C_ell in this band: C_ell -> C_ell * (1 + delta_DGF)
# This changes sigma1^2 by delta * sigma1_sq_dgf_band
# Genus amplitude G ∝ sigma1/sigma0, so:
# Delta_G / G = 0.5 * Delta(sigma1^2) / sigma1^2 = 0.5 * delta * fraction_dgf

# ============================================================
# 4. Detection sensitivity
# ============================================================
# Cosmic variance of sigma1^2 from one full-sky map:
# Var(sigma1^2) ~ 2 * sigma1^4 / lmax_eff
# where lmax_eff ~ number of independent modes ~ f_sky * lmax^2 / 4
f_sky = 0.80  # Planck common mask
l_eff = 767   # nside=256 → lmax=3*nside-1
n_modes = f_sky * l_eff**2 / 4.0
frac_err_sigma1_sq = np.sqrt(2.0 / n_modes)
frac_err_genus = 0.5 * frac_err_sigma1_sq  # propagation to genus

print(f"\n{'='*60}")
print(f"DETECTION SENSITIVITY")
print(f"="*60)
print(f"  Effective modes (f_sky={f_sky}, lmax={l_eff}): {n_modes:.0f}")
print(f"  Cosmic variance of sigma1^2 (1 map): {frac_err_sigma1_sq*100:.2f}%")
print(f"  Cosmic variance of genus amplitude (1 map): {frac_err_genus*100:.2f}%")

# ============================================================
# 5. THE KEY NUMBER: what delta is needed for 3sigma?
# ============================================================
# Signal: Delta_G/G = 0.5 * delta * fraction_dgf
# Noise: sigma_G/G = frac_err_genus
# SNR = (0.5 * delta * fraction_dgf) / frac_err_genus
# Required delta for SNR=3:
# delta_3sigma = 3 * frac_err_genus * 2 / fraction_dgf

delta_3sigma_1map = 3 * frac_err_genus * 2 / fraction_dgf
delta_3sigma_4map = delta_3sigma_1map / np.sqrt(4)  # 4 maps: SMICA+Commander+NILC+SEVEM

print(f"\n  DGF band fraction of genus signal: {fraction_dgf*100:.1f}%")
print(f"  Required delta_beta1 for 3sigma (1 map): {delta_3sigma_1map*100:.1f}%")
print(f"  Required delta_beta1 for 3sigma (4 maps combined): {delta_3sigma_4map*100:.1f}%")
print(f"  DGF prediction: 0.2% - 2.0%")

# ============================================================
# 6. Comparison table
# ============================================================
print(f"\n{'='*60}")
print(f"FINAL COMPARISON")
print(f"="*60)

dgf_predictions = [0.2, 0.5, 1.0, 2.0]
print(f"\n  {'delta_beta1':>10s}  {'SNR(1 map)':>12s}  {'SNR(4 maps)':>12s}  {'Detectable?':>12s}")
print(f"  {'-'*10}  {'-'*12}  {'-'*12}  {'-'*12}")
for d in dgf_predictions:
    snr_1 = (0.5 * d/100 * fraction_dgf) / frac_err_genus
    snr_4 = snr_1 * 2
    det = "YES" if snr_4 >= 3 else ("MARGINAL" if snr_4 >= 1 else "NO")
    print(f"  {d:8.1f}%  {snr_1:12.2f}  {snr_4:12.2f}  {det:>12s}")

print(f"\n  Planck 2018 Minkowski functional constraint:")
print(f"  chi^2/dof = 17.4/16 (p=0.36) — consistent with LCDM at <1sigma")
print(f"  This means: |Delta_G/G| < {frac_err_genus*100:.1f}% (1sigma)")
print(f"  This implies: |delta_beta1| < {delta_3sigma_1map*100:.1f}% (3sigma)")

# ============================================================
# 7. The razor
# ============================================================
print(f"\n{'='*60}")
print(f"THE RAZOR")
print(f"="*60)

# How much better would persistent homology be?
# In persistent homology, beta1 is measured DIRECTLY (no beta0 cancellation)
# For Gaussian fields, beta1 peak at nu=0: beta1_max ~ sigma1^2/sigma0^2 * (2*pi)^(-3/2) * Area
# Cosmic variance of beta1: similar to genus (both topological measures)
# BUT: beta1 is not cancelled by beta0 → full signal power
# In genus: Delta_G/G = 0.5 * delta * fraction_dgf
# In persistent homology (beta1): Delta_beta1/beta1 = delta (full multiplication)
# So persistent homology is 2/fraction_dgf ~ 30x MORE sensitive than genus

gain_ph = 2.0 / fraction_dgf
delta_3sigma_ph = delta_3sigma_1map / gain_ph

print(f"\n  Genus (V2): delta_beta1 >= {delta_3sigma_1map*100:.1f}% for 3sigma")
print(f"  Persistent homology: delta_beta1 >= {delta_3sigma_ph*100:.2f}% for 3sigma")
print(f"  Sensitivity gain of persistent homology: {gain_ph:.0f}x")
print(f"  DGF prediction: 0.2% - 2.0%")
if delta_3sigma_ph * 100 < 2.0:
    print(f"\n  VERDICT: Persistent homology CAN detect DGF's full prediction range.")
    print(f"  Genus CANNOT — needs signal {delta_3sigma_1map*100:.0f}x larger than DGF max.")
else:
    print(f"\n  VERDICT: Even persistent homology may need more sensitivity.")
    print(f"  Need larger f_sky or higher lmax.")

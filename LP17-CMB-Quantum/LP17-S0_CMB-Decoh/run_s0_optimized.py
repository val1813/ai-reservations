"""
LP17-S0: Optimized quick experiment
====================================
Tests whether removing ℓ<30 from Planck CMB shifts inferred H₀.
Uses CAMB + emcee with compressed binning for speed.
"""
import numpy as np
import camb
from camb import model, initialpower
import emcee
import json
import os
import sys
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# Build Planck-like synthetic data with realistic errors
# ============================================================
def build_planck_data():
    """Build synthetic data matching Planck 2018 binned TT spectrum."""
    pars = camb.CAMBparams()
    pars.set_cosmology(H0=67.36, ombh2=0.02237, omch2=0.1200, tau=0.0544)
    pars.InitPower.set_params(As=2.1005e-9, ns=0.9649, r=0)
    pars.set_for_lmax(2508)
    results = camb.get_results(pars)
    cl_total = results.get_cmb_power_spectra(pars, CMB_unit='muK')['total']
    cls = cl_total[:, 0]

    # Planck-like binning (aggressive for speed)
    bin_edges = []
    ell = 2
    while ell <= 2508:
        bin_edges.append(ell)
        if ell < 30:
            ell += 1
        elif ell < 100:
            ell += 8
        elif ell < 500:
            ell += 15
        elif ell < 1500:
            ell += 25
        else:
            ell += 40
    if bin_edges[-1] < 2508:
        bin_edges.append(2509)

    bin_c, bin_cl, bin_err = [], [], []
    ell_arr = np.arange(len(cls))
    f_sky = 0.78

    for i in range(len(bin_edges)-1):
        lo, hi = bin_edges[i], bin_edges[i+1]
        idx = np.where((ell_arr >= lo) & (ell_arr < hi))[0]
        if len(idx) == 0:
            continue
        ecent = (lo + hi) / 2.0
        nmodes = hi - lo
        avg = np.mean(cls[idx])
        cv = avg * np.sqrt(2.0 / (2*ecent + 1) / f_sky)
        noise = (30.0 * np.pi / 180.0 / 60.0)**2
        noise_cl = noise * np.exp(ecent * (ecent+1) * (5.0*np.pi/180/60)**2 / (8*np.log(2)))
        err = np.sqrt(cv**2 + (noise_cl/np.sqrt(nmodes))**2)
        bin_c.append(ecent)
        bin_cl.append(avg)
        bin_err.append(err)

    ell_arr = np.array(bin_c)
    cl_arr = np.array(bin_cl)
    err_arr = np.array(bin_err)

    # Add random scatter
    np.random.seed(42)
    cl_arr = cl_arr + np.random.normal(0, 1, len(cl_arr)) * err_arr

    return {'ell': ell_arr, 'cl': cl_arr, 'cl_err': err_arr}

# ============================================================
# CAMB model
# ============================================================
_ell_cache = None
_cl_cache = None

def get_model_cl(theta):
    """Compute CAMB TT spectrum for parameters theta."""
    global _ell_cache, _cl_cache
    H0, ombh2, omch2, tau, logAs, ns = theta
    pars = camb.CAMBparams()
    pars.set_cosmology(H0=H0, ombh2=ombh2, omch2=omch2, tau=tau)
    pars.InitPower.set_params(As=np.exp(logAs)/1e10, ns=ns, r=0)
    pars.set_for_lmax(2508)
    try:
        results = camb.get_results(pars)
        cl = results.get_cmb_power_spectra(pars, CMB_unit='muK')['total'][:, 0]
        ell_camb = np.arange(len(cl))
        return ell_camb, cl
    except:
        return None, None

def model_cl_at_ells(theta, target_ells):
    """Interpolate model C_l to target ell values."""
    ell_camb, cl_camb = get_model_cl(theta)
    if ell_camb is None:
        return np.full(len(target_ells), 1e10)
    res = []
    for lell in target_ells:
        idx = np.argmin(np.abs(ell_camb - lell))
        res.append(cl_camb[idx])
    return np.array(res)

# ============================================================
# Posterior
# ============================================================
def log_prior(theta):
    H0, ombh2, omch2, tau, logAs, ns = theta
    if not (40 < H0 < 100): return -np.inf
    if not (0.005 < ombh2 < 0.040): return -np.inf
    if not (0.05 < omch2 < 0.20): return -np.inf
    if not (0.01 < tau < 0.20): return -np.inf
    if not (2.5 < logAs < 3.5): return -np.inf
    if not (0.8 < ns < 1.1): return -np.inf
    return 0.0

def log_prob(theta, ell_data, cl_data, cl_err):
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    model_cl = model_cl_at_ells(theta, ell_data)
    chi2 = np.sum(((model_cl - cl_data) / cl_err) ** 2)
    return lp - 0.5 * chi2

# ============================================================
# MCMC runner
# ============================================================
def run_mcmc(data, label, n_steps=800, n_walkers=16, ell_cut=None):
    if ell_cut is not None:
        mask = data['ell'] >= ell_cut
        ell_u = data['ell'][mask]
        cl_u = data['cl'][mask]
        err_u = data['cl_err'][mask]
    else:
        ell_u = data['ell']
        cl_u = data['cl']
        err_u = data['cl_err']

    print(f"\n[{label}] {len(ell_u)} bins, ell=[{ell_u[0]:.0f}, {ell_u[-1]:.0f}]")

    init = np.array([67.36, 0.02237, 0.1200, 0.0544, 3.044, 0.9649])
    ndim = len(init)
    pos = init + init * 0.01 * np.random.randn(n_walkers, ndim)

    sampler = emcee.EnsembleSampler(n_walkers, ndim, log_prob,
                                     args=(ell_u, cl_u, err_u))

    for i, _ in enumerate(sampler.sample(pos, iterations=n_steps, progress=False)):
        if (i+1) % 200 == 0:
            print(f"  step {i+1}/{n_steps}")

    burn = int(n_steps * 0.3)
    samples = sampler.get_chain(discard=burn, flat=True)

    names = ['H0', 'ombh2', 'omch2', 'tau', 'ln(10^10 As)', 'ns']
    results = {}
    for i, name in enumerate(names):
        c = samples[:, i]
        results[name] = {
            'mean': float(np.mean(c)),
            'std': float(np.std(c)),
            'median': float(np.median(c)),
            'p16': float(np.percentile(c, 16)),
            'p84': float(np.percentile(c, 84)),
        }
    return results, samples

# ============================================================
# Main
# ============================================================
def main():
    odir = os.path.dirname(__file__)
    print("="*60)
    print("LP17-S0 Experiment: Does ell<30 shift H0?")
    print("="*60)

    # Data
    print("\n[1] Building Planck 2018-like data...")
    data = build_planck_data()
    n_low = np.sum(data['ell'] < 30)
    n_high = np.sum(data['ell'] >= 30)
    print(f"    Total bins: {len(data['ell'])} ({n_low} with ell<30, {n_high} with ell>=30)")

    # Baseline (full)
    print("\n[2] Running BASELINE (full data)...")
    res_full, samp_full = run_mcmc(data, "FULL", n_steps=800, n_walkers=16)

    # Truncated (ell >= 30)
    print("\n[3] Running TRUNCATED (ell>=30)...")
    res_trunc, samp_trunc = run_mcmc(data, "TRUNCATED", n_steps=800, n_walkers=16, ell_cut=30)

    # Compare
    print("\n" + "="*60)
    print("RESULTS")
    print("="*60)
    hf = res_full['H0']
    ht = res_trunc['H0']
    dh0 = ht['mean'] - hf['mean']
    sig = abs(dh0) / np.sqrt(hf['std']**2 + ht['std']**2)

    print(f"  Baseline  H0 = {hf['mean']:.2f} +/- {hf['std']:.2f} km/s/Mpc")
    print(f"  Truncated H0 = {ht['mean']:.2f} +/- {ht['std']:.2f} km/s/Mpc")
    print(f"  Delta H0     = {dh0:+.2f} km/s/Mpc ({sig:.1f} sigma)")
    print(f"  H0 shifts {'TOWARD' if dh0 > 0 else 'AWAY FROM'} SH0ES value (72.7)")

    if sig > 1.0:
        print(f"\n  *** SIGNIFICANT SHIFT: Supports decoherence hypothesis ***")
    elif sig > 0.5:
        print(f"\n  *** MARGINAL: Needs more MCMC steps for precision ***")
    else:
        print(f"\n  *** NO SHIFT: Null result ***")

    # Save
    out = {
        'experiment': 'LP17-S0',
        'baseline_H0': hf,
        'truncated_H0': ht,
        'delta_H0': float(dh0),
        'significance': float(sig),
        'n_bins_full': len(data['ell']),
        'n_bins_trunc': int(np.sum(data['ell'] >= 30)),
    }
    with open(os.path.join(odir, 's0_results.json'), 'w') as f:
        json.dump(out, f, indent=2)
    print(f"\nResults saved to s0_results.json")

    # Plot
    try:
        import matplotlib
        matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        fig, axes = plt.subplots(2, 3, figsize=(14, 9))
        axes = axes.flatten()
        labels = ['H0', 'ombh2', 'omch2', 'tau', 'ln(10^10 As)', 'ns']
        for i, lab in enumerate(labels):
            ax = axes[i]
            ax.hist(samp_full[:, i], bins=40, density=True, alpha=0.6,
                   label='Full', color='steelblue')
            ax.hist(samp_trunc[:, i], bins=40, density=True, alpha=0.6,
                   label='ell>=30', color='darkorange')
            ax.set_xlabel(lab)
            if i == 0:
                ax.legend()
        fig.suptitle('LP17-S0: Full vs ell>=30', fontweight='bold')
        plt.tight_layout()
        fig.savefig(os.path.join(odir, 's0_comparison.png'), dpi=120)
        print("Plot saved to s0_comparison.png")
    except Exception as e:
        print(f"Plot error: {e}")

    return out

if __name__ == '__main__':
    main()

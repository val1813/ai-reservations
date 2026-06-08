"""
LP17-S0: Fast parallel experiment (Windows-compatible)
=======================================================
Tests whether removing ell<30 from Planck CMB shifts inferred H0.
Uses CAMB + emcee with multiprocessing via initializer for Windows.
"""
import numpy as np
import camb
from camb import model, initialpower
import emcee
import json
import os
import sys
import warnings
from multiprocessing import Pool, cpu_count
warnings.filterwarnings('ignore')

# ============================================================
# Global data (set in worker processes via pool initializer)
# ============================================================
_DATA_ELL = None
_DATA_CL = None
_DATA_ERR = None

def _init_worker(ell, cl, err):
    """Pool initializer: set global data in each worker process."""
    global _DATA_ELL, _DATA_CL, _DATA_ERR
    _DATA_ELL = ell
    _DATA_CL = cl
    _DATA_ERR = err

# ============================================================
# Data: Planck 2018 best-fit synthetic data
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

    bin_edges = []
    ell = 2
    while ell <= 2508:
        bin_edges.append(ell)
        if ell < 30: ell += 1
        elif ell < 100: ell += 8
        elif ell < 500: ell += 15
        elif ell < 1500: ell += 25
        else: ell += 40
    if bin_edges[-1] < 2508:
        bin_edges.append(2509)

    bin_c, bin_cl, bin_err = [], [], []
    ell_arr = np.arange(len(cls))
    f_sky = 0.78

    for i in range(len(bin_edges)-1):
        lo, hi = bin_edges[i], bin_edges[i+1]
        idx = np.where((ell_arr >= lo) & (ell_arr < hi))[0]
        if len(idx) == 0: continue
        ecent = (lo + hi) / 2.0
        nmodes = hi - lo
        avg = np.mean(cls[idx])
        cv = avg * np.sqrt(2.0 / (2*ecent + 1) / f_sky)
        noise_rad = 30.0 * np.pi / 180.0 / 60.0
        noise_cl_val = noise_rad**2 * np.exp(ecent*(ecent+1)*(5.0*np.pi/180/60)**2/(8*np.log(2)))
        err = np.sqrt(cv**2 + (noise_cl_val/np.sqrt(nmodes))**2)
        bin_c.append(ecent)
        bin_cl.append(avg)
        bin_err.append(err)

    ell_arr = np.array(bin_c)
    cl_arr = np.array(bin_cl)
    err_arr = np.array(bin_err)

    np.random.seed(42)
    cl_arr = cl_arr + np.random.normal(0, 1, len(cl_arr)) * err_arr
    return {'ell': ell_arr, 'cl': cl_arr, 'cl_err': err_arr}

# ============================================================
# Likelihood
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

def log_prob(theta):
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf

    H0, ombh2, omch2, tau, logAs, ns = theta
    pars = camb.CAMBparams()
    pars.set_cosmology(H0=H0, ombh2=ombh2, omch2=omch2, tau=tau)
    pars.InitPower.set_params(As=np.exp(logAs)/1e10, ns=ns, r=0)
    pars.set_for_lmax(2508)
    try:
        results = camb.get_results(pars)
        cl = results.get_cmb_power_spectra(pars, CMB_unit='muK')['total'][:,0]
    except:
        return -np.inf

    # Interpolate to data ell values (use globals set by pool initializer)
    ell_camb = np.arange(len(cl))
    model_vals = np.interp(_DATA_ELL, ell_camb, cl)
    chi2 = np.sum(((model_vals - _DATA_CL) / _DATA_ERR) ** 2)
    return lp - 0.5 * chi2

# ============================================================
# MCMC runner
# ============================================================
def run_mcmc(data, label, n_steps=400, n_walkers=12, ell_cut=None, n_workers=6):
    if ell_cut is not None:
        mask = data['ell'] >= ell_cut
        ell_u = data['ell'][mask].copy()
        cl_u = data['cl'][mask].copy()
        err_u = data['cl_err'][mask].copy()
    else:
        ell_u = data['ell'].copy()
        cl_u = data['cl'].copy()
        err_u = data['cl_err'].copy()

    # Convert to plain lists for pickling
    ell_list = ell_u.tolist() if hasattr(ell_u, 'tolist') else list(ell_u)
    cl_list = cl_u.tolist() if hasattr(cl_u, 'tolist') else list(cl_u)
    err_list = err_u.tolist() if hasattr(err_u, 'tolist') else list(err_u)

    print(f"\n[{label}] {len(ell_list)} bins, ell=[{ell_list[0]:.0f}, {ell_list[-1]:.0f}]")
    print(f"  MCMC: {n_steps} steps x {n_walkers} walkers, {n_workers} workers")

    init = np.array([67.36, 0.02237, 0.1200, 0.0544, 3.044, 0.9649])
    ndim = len(init)
    np.random.seed(123)
    pos = init + init * 0.008 * np.random.randn(n_walkers, ndim)

    import time
    t0 = time.time()

    # Use pool with initializer to pass data to workers
    with Pool(n_workers, initializer=_init_worker,
              initargs=(ell_list, cl_list, err_list)) as pool:
        sampler = emcee.EnsembleSampler(n_walkers, ndim, log_prob, pool=pool)
        for i, _ in enumerate(sampler.sample(pos, iterations=n_steps, progress=False)):
            if (i+1) % 100 == 0:
                elapsed = time.time() - t0
                print(f"  step {i+1}/{n_steps} ({elapsed:.0f}s)")

    elapsed = time.time() - t0
    print(f"  Done in {elapsed:.0f}s ({elapsed/60:.1f} min)")

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

    h0 = results['H0']
    print(f"  H0 = {h0['mean']:.2f} +/- {h0['std']:.2f} km/s/Mpc")
    print(f"  ns = {results['ns']['mean']:.4f} +/- {results['ns']['std']:.4f}")

    return results, samples

# ============================================================
# Main
# ============================================================
def main():
    odir = os.path.dirname(__file__)
    print("="*60)
    print("LP17-S0: Does removing ell<30 shift H0?")
    print(f"CPU cores: {cpu_count()}")
    print("="*60)

    n_workers = min(6, cpu_count())
    print(f"Using {n_workers} parallel workers")

    # Data
    print("\n[1] Building Planck 2018-like data...")
    data = build_planck_data()
    n_low = np.sum(data['ell'] < 30)
    n_high = np.sum(data['ell'] >= 30)
    print(f"    Total: {len(data['ell'])} bins ({n_low} ell<30, {n_high} ell>=30)")

    # Baseline (full data)
    print("\n[2] BASELINE MCMC (full Planck data)...")
    res_full, samp_full = run_mcmc(data, "FULL", n_steps=400, n_walkers=12, n_workers=n_workers)

    # Truncated (ell >= 30)
    print("\n[3] TRUNCATED MCMC (ell >= 30 only)...")
    res_trunc, samp_trunc = run_mcmc(data, "TRUNCATED", n_steps=400, n_walkers=12,
                                      ell_cut=30, n_workers=n_workers)

    # ============================================================
    # Results
    # ============================================================
    print("\n" + "="*60)
    print("LP17-S0 RESULTS")
    print("="*60)

    hf = res_full['H0']
    ht = res_trunc['H0']
    dh0 = ht['mean'] - hf['mean']
    sig = abs(dh0) / np.sqrt(hf['std']**2 + ht['std']**2)

    print(f"\n  {'Parameter':<20} {'Full data':>15} {'ell>=30':>15} {'Delta':>10}")
    print(f"  {'-'*60}")
    for name in ['H0', 'ombh2', 'omch2', 'tau', 'ln(10^10 As)', 'ns']:
        fv = res_full[name]
        tv = res_trunc[name]
        d = tv['mean'] - fv['mean']
        dsig = abs(d) / np.sqrt(fv['std']**2 + tv['std']**2)
        print(f"  {name:<20} {fv['mean']:10.4f}+/-{fv['std']:.4f}  {tv['mean']:10.4f}+/-{tv['std']:.4f}  {d:+8.4f} ({dsig:.1f}s)")

    print(f"\n  *** Delta H0 = {dh0:+.2f} km/s/Mpc ({sig:.1f} sigma) ***")

    # Scientific interpretation
    h0_full_val = hf['mean']
    h0_trunc_val = ht['mean']
    sh0es = 72.7
    tension_full = (sh0es - h0_full_val) / hf['std']
    tension_trunc = (sh0es - h0_trunc_val) / ht['std']

    print(f"\n  Hubble tension vs SH0ES (72.7 km/s/Mpc):")
    print(f"    Full data:    {tension_full:.1f} sigma")
    print(f"    ell >= 30:    {tension_trunc:.1f} sigma")
    print(f"    Reduction:    {tension_full - tension_trunc:+.1f} sigma")

    print(f"\n  Science interpretation:")
    if sig > 1.0 and dh0 > 1.0:
        print(f"  *** SIGNIFICANT POSITIVE SHIFT: ell<30 removal moves H0 toward SH0ES! ***")
        print(f"  *** This SUPPORTS the quantum decoherence hypothesis. ***")
        verdict = "SUPPORTS — H0 shifts toward SH0ES when removing ell<30"
    elif sig > 1.0 and dh0 < -1.0:
        print(f"  *** SIGNIFICANT NEGATIVE SHIFT: ell<30 removal moves H0 AWAY from SH0ES. ***")
        print(f"  *** This REJECTS the quantum decoherence hypothesis (wrong direction). ***")
        verdict = "REJECTS — H0 shifts AWAY from SH0ES (wrong direction)"
    elif sig > 0.7:
        print(f"  *** MARGINAL: Direction {'toward' if dh0 > 0 else 'away from'} SH0ES, need more precision ***")
        verdict = f"MARGINAL — {dh0:+.1f} km/s/Mpc, {sig:.1f} sigma"
    else:
        print(f"  *** NULL: No significant H0 shift from removing ell<30 ***")
        print(f"  *** Quantum decoherence hypothesis constrained. ***")
        verdict = "NULL — no significant shift"

    # Save results
    out = {
        'experiment': 'LP17-S0',
        'question': 'Does removing ell<30 from Planck CMB shift inferred H0?',
        'date': '2026-06-02',
        'method': 'CAMB v' + camb.__version__ + ' + emcee MCMC, Planck 2018-like binned TT',
        'verdict': verdict,
        'baseline_H0': hf,
        'truncated_H0': ht,
        'delta_H0_km_s_Mpc': float(dh0),
        'significance_sigma': float(sig),
        'tension_full_sigma': float(tension_full),
        'tension_truncated_sigma': float(tension_trunc),
        'tension_reduction_sigma': float(tension_full - tension_trunc),
        'n_bins_full': len(data['ell']),
        'n_bins_low_ell': int(n_low),
        'n_bins_high_ell': int(n_high),
        'all_params_full': res_full,
        'all_params_truncated': res_trunc,
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
        disp = ['H_0', 'Omega_b h^2', 'Omega_c h^2', 'tau', 'ln(10^{10}A_s)', 'n_s']
        for i, lab in enumerate(labels):
            ax = axes[i]
            ax.hist(samp_full[:, i], bins=35, density=True, alpha=0.6,
                   label='Full data', color='steelblue')
            ax.hist(samp_trunc[:, i], bins=35, density=True, alpha=0.6,
                   label='ell >= 30', color='darkorange')
            ax.set_xlabel(disp[i], fontsize=11)
            if i == 0:
                ax.legend(fontsize=10)
        fig.suptitle(f'LP17-S0: Full vs ell>=30 | Delta H0 = {dh0:+.1f} km/s/Mpc ({sig:.1f}sigma)',
                     fontsize=13, fontweight='bold')
        plt.tight_layout()
        fig.savefig(os.path.join(odir, 's0_comparison.png'), dpi=120)
        print("Plot saved to s0_comparison.png")
        plt.close()
    except Exception as e:
        print(f"Plot warning: {e}")

    print("\n" + "="*60)
    print("EXPERIMENT COMPLETE")
    print("="*60)
    return out

if __name__ == '__main__':
    main()

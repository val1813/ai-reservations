"""
Pantheon+ Segmented z_max H0 Analysis
======================================
Tests: H0(z_max) should decrease monotonically (holographic sigmoid prediction)

Data: Pantheon+ SH0ES (1701 SNe)
Columns: CID SURVEY zHD zHDERR zCMB zCMBERR zHEL zHELERR
         m_b_corr m_b_corr_err_DIAG MU_SH0ES MU_SH0ES_ERR_DIAG
         CEPH_DIST IS_CALIBRATOR USED_IN_SH0ES_HF ...
"""
import numpy as np
from scipy.optimize import minimize
from scipy import stats
import os, json, warnings
warnings.filterwarnings('ignore')

# ============================================================
# 1. Read Pantheon+ data
# ============================================================
def read_pantheon(data_dir):
    fpath = os.path.join(data_dir, 'Pantheon+SH0ES.dat')
    with open(fpath, 'r') as f:
        header = f.readline().strip().split()
    # Read: first col is string (CID), rest are floats
    raw = []
    with open(fpath, 'r') as f:
        f.readline()  # skip header
        for line in f:
            parts = line.strip().split()
            if len(parts) < 5:
                continue
            raw.append([parts[0]] + [float(x) for x in parts[1:]])
    data_arr = np.array(raw, dtype=object)
    # Build float matrix for numeric columns (skip col 0 = CID string)
    data = np.array([[float(x) for x in row[1:]] for row in raw])
    # Column indices (shifted by +1 because we dropped CID)
    cols = {h: i for i, h in enumerate(header) if h != 'CID'}
    # Re-index: original col X (1-indexed in header after CID) maps to data[:, X-1]
    # Remap: all cols except CID
    cols = {}
    for i, h in enumerate(header):
        if h == 'CID':
            continue
        cols[h] = len(cols)  # sequential for numeric data
    print(f'Columns: {list(header)}')
    print(f'Total SNe: {len(data)}')

    z_cmb = data[:, cols['zCMB']]
    mu_shoes = data[:, cols['MU_SH0ES']]
    mu_err = data[:, cols['MU_SH0ES_ERR_DIAG']]

    # Use ALL SNe with z > 0.01 (avoid peculiar velocity contamination)
    # NOT just the Hubble flow subset — we want z>0.15 coverage
    mask = z_cmb > 0.01
    print(f'Total SNe: {len(z_cmb)}')
    print(f'SNe with z>0.01: {mask.sum()}')
    print(f'z range: [{z_cmb[mask].min():.4f}, {z_cmb[mask].max():.3f}]')
    # Show z distribution
    for lo in [0.01, 0.05, 0.10, 0.15, 0.20, 0.30, 0.50, 0.80, 1.0]:
        n = np.sum(z_cmb[mask] > lo)
        print(f'  z > {lo:.2f}: {n} SNe')

    return {
        'z': z_cmb[mask],
        'mu': mu_shoes[mask],
        'mu_err': mu_err[mask],
    }

# ============================================================
# 2. Distance modulus
# ============================================================
def dl_integral(z_max, Om=0.315):
    """Integral for comoving distance: int_0^z dz/E(z)."""
    z_arr = np.linspace(0, z_max, 500)
    dz = z_arr[1] - z_arr[0]
    Ez = np.sqrt(Om * (1 + z_arr)**3 + (1 - Om))
    return np.sum(1.0 / Ez) * dz

def mu_model(z, H0, MB, Om=0.315):
    c_kms = 299792.458
    # Vectorize for array input
    z = np.atleast_1d(z)
    result = np.zeros(len(z))
    for i, zi in enumerate(z):
        integral = dl_integral(zi, Om)
        dL = (c_kms / H0) * (1 + zi) * integral
        result[i] = 5 * np.log10(dL / 1e-5) + MB
    return result if len(result) > 1 else result[0]

# ============================================================
# 3. Fit H0 for z_max cut
# ============================================================
def fit_h0(z_data, mu_data, mu_err, z_max, Om=0.315):
    """Fit H0 only using Cepheid-calibrated MU_SH0ES (no M_B degeneracy)."""
    mask = z_data < z_max
    z_use = z_data[mask]
    mu_use = mu_data[mask]
    err_use = mu_err[mask]
    n = len(z_use)
    if n < 20:
        return None

    def mu_th(z, H0):
        c_kms = 299792.458
        result = np.zeros(len(z))
        for i, zi in enumerate(z):
            integral = dl_integral(zi, Om)
            dL = (c_kms / H0) * (1 + zi) * integral
            result[i] = 5 * np.log10(dL / 1e-5)  # no +MB — MU_SH0ES is absolute
        return result

    def chi2(p):
        H0 = p[0]
        if H0 <= 0: return 1e10
        model = mu_th(z_use, H0)
        return np.sum(((mu_use - model) / err_use) ** 2)

    res = minimize(chi2, [73.0], method='Nelder-Mead',
                   options={'xatol': 1e-4, 'fatol': 1e-4})

    H0_b = res.x[0]
    # Error via curvature
    eps = 0.005
    c0 = chi2([H0_b])
    cp = chi2([H0_b*(1+eps)])
    cm = chi2([H0_b*(1-eps)])
    d2 = (cp - 2*c0 + cm) / (H0_b*eps)**2
    h0_err = np.sqrt(2.0/d2) if d2 > 0 else np.std(mu_use)/np.sqrt(n)/5

    return {
        'z_max': z_max, 'n_sne': n,
        'H0': float(H0_b), 'H0_err': float(h0_err),
        'chi2_dof': c0/(n-1),
        'z_mean': float(np.mean(z_use)),
    }

# ============================================================
# 4. Holographic prediction
# ============================================================
def z_to_R(z, H0_ref=70.0, Om=0.315):
    c_kms = 299792.458
    integral = dl_integral(z, Om)
    return c_kms * integral / H0_ref

def h0_pred_cubic(R, H0_true=67.3, dH=0.091, rv=1898):
    ratio = rv / np.sqrt(rv**2 + R**2)
    return H0_true * (1 + dH * ratio**3)

# ============================================================
# 5. Main
# ============================================================
def main():
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    odir = os.path.dirname(__file__)

    print("=" * 60)
    print("Pantheon+ Segmented z_max H0 Analysis")
    print("=" * 60)

    d = read_pantheon(data_dir)

    # z_max grid: dense in 0.01-0.15 where signal is
    z_max_list = np.concatenate([
        np.array([0.01, 0.015, 0.02, 0.023, 0.025, 0.03, 0.035]),
        np.arange(0.04, 0.16, 0.01),
        np.array([0.18, 0.20, 0.23, 0.25, 0.30, 0.35, 0.40, 0.50,
                  0.60, 0.80, 1.00, 1.50, 2.00]),
    ])
    z_max_list = np.unique(np.sort(z_max_list))

    print(f"\nFitting H0 for {len(z_max_list)} z_max cuts...")
    print(f"Fixed Om=0.315 (Planck 2018)")

    results = []
    for zmax in z_max_list:
        r = fit_h0(d['z'], d['mu'], d['mu_err'], zmax)
        if r:
            results.append(r)
            print(f"  z<{zmax:6.4f}  N={r['n_sne']:4d}  "
                  f"H0={r['H0']:6.2f}+/-{r['H0_err']:4.2f}  "
                  f"chi2/dof={r['chi2_dof']:.2f}")

    if len(results) < 3:
        print("ERROR: too few valid fits")
        return

    zz = np.array([r['z_max'] for r in results])
    hh = np.array([r['H0'] for r in results])
    he = np.array([r['H0_err'] for r in results])
    nn = np.array([r['n_sne'] for r in results])
    RR = np.array([z_to_R(z) for z in zz])
    hp = np.array([h0_pred_cubic(R) for R in RR])

    # ---- Print results ----
    print(f"\n{'='*70}")
    print(f"{'z_max':>8s}  {'R(Mpc)':>8s}  {'N':>5s}  {'H0_obs':>10s}  {'H0_pred':>10s}  {'D(s)':>8s}")
    print(f"{'-'*70}")
    for i in range(len(results)):
        ds = (hh[i] - hp[i]) / he[i]
        print(f"{zz[i]:8.4f}  {RR[i]:8.0f}  {nn[i]:5d}  {hh[i]:6.2f}+/-{he[i]:4.2f}"
              f"  {hp[i]:9.2f}  {ds:+7.2f}")

    # ---- Key z slices ----
    print(f"\n=== Key z_max values ===")
    for z_key in [0.023, 0.05, 0.10, 0.15, 0.20, 0.30]:
        idx = np.argmin(np.abs(zz - z_key))
        print(f"  z<{zz[idx]:.3f} R={RR[idx]:.0f}Mpc N={nn[idx]} "
              f"H0={hh[idx]:.2f}+/-{he[idx]:.2f} pred={hp[idx]:.2f} "
              f"D={((hh[idx]-hp[idx])/he[idx]):+.1f}s")

    # ---- Monotonicity ----
    diffs = np.diff(hh)
    n_down = np.sum(diffs < 0)
    rho, pval = stats.spearmanr(zz, hh)
    print(f"\n=== Monotonicity ===")
    print(f"  Decreasing: {n_down}/{len(diffs)} segments")
    print(f"  Spearman rho(H0,z_max) = {rho:.3f} (p={pval:.4f})")
    if rho < -0.5 and pval < 0.05:
        print(f"  *** H0 significantly DECREASES with z_max! ***")
    elif abs(rho) < 0.3:
        print(f"  --- H0 FLAT vs z_max (no trend detected) ---")
    else:
        print(f"  --- Inconclusive ---")

    # ---- Save ----
    out = {
        'z_max': zz.tolist(), 'R_Mpc': RR.tolist(),
        'H0_obs': hh.tolist(), 'H0_err': he.tolist(),
        'H0_pred': hp.tolist(), 'n_sne': nn.tolist(),
        'spearman_rho': float(rho), 'spearman_p': float(pval),
    }
    with open(os.path.join(odir, 'pantheon_segmented_results.json'), 'w') as f:
        json.dump(out, f, indent=2)
    print(f"\nSaved: pantheon_segmented_results.json")

    # ---- Plot ----
    try:
        import matplotlib; matplotlib.use('Agg')
        import matplotlib.pyplot as plt
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5.5))

        ax1.errorbar(zz, hh, yerr=he, fmt='o', color='steelblue', ms=4,
                     capsize=2, alpha=0.8, label='Pantheon+ (this work)')
        zf = np.logspace(-2, 0.3, 200)
        Rf = np.array([z_to_R(z) for z in zf])
        ax1.plot(zf, h0_pred_cubic(Rf), '-', color='darkorange', lw=2,
                label='Holographic cubic sigmoid')
        ax1.axhline(67.4, color='green', ls=':', alpha=0.5, label='Planck CMB')
        ax1.set_xscale('log'); ax1.set_xlabel('z_max'); ax1.set_ylabel('H0')
        ax1.legend(fontsize=8); ax1.grid(alpha=0.3)
        ax1.set_title('Pantheon+ H0 vs z_max', fontweight='bold')

        ax2.errorbar(RR, hh, yerr=he, fmt='o', color='steelblue', ms=4,
                     capsize=2, alpha=0.8)
        R_all = np.logspace(0, 4.5, 300)
        ax2.plot(R_all, h0_pred_cubic(R_all), '-', color='darkorange', lw=2)
        ax2.set_xscale('log'); ax2.set_xlabel('R [Mpc]'); ax2.set_ylabel('H0')
        ax2.grid(alpha=0.3)
        ax2.set_title('H0 vs Effective Screen Radius', fontweight='bold')

        plt.tight_layout()
        fplot = os.path.join(odir, 'pantheon_segmented_h0.png')
        fig.savefig(fplot, dpi=150, bbox_inches='tight')
        print(f"Plot: {fplot}")
        plt.close()
    except Exception as e:
        print(f"Plot error: {e}")

    return out

if __name__ == '__main__':
    main()

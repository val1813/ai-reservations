"""
LP32-S8: DGF-DESI DR2 Contour Comparison — Figure Generation
=============================================================
Generates publication-quality figures for Nature Physics submission.

Figures:
  Fig1: DESI DR2 (w0,wa) contours + DGF theory curve overlay
  Fig2: DGF w(z) shape prediction with SFR uncertainty band
  Fig3: n-parameter chi2 profile showing data preference for n~1

Output: figures/fig1_contour.png, fig2_wz_shape.png, fig3_n_profile.png
Data:   data/contour_package.json (all numerical results)

Usage:  python code/generate_figures.py
"""

import numpy as np
import json
import os
import sys

# Add project root
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(os.path.join(ROOT, 'figures'), exist_ok=True)
os.makedirs(os.path.join(ROOT, 'data'), exist_ok=True)

# ================================================================
# SECTION 1: Core Data
# ================================================================

# DESI DR2 + CMB + DESY5 (Zhang et al. 2026, SSRN 6215384)
DESI = {
    'w0_bf': -0.785, 'wa_bf': -0.43,
    'sigma_w0': 0.047, 'sigma_wa': 0.10, 'rho': 0.315
}
DESI['cov'] = [
    [DESI['sigma_w0']**2, DESI['rho']*DESI['sigma_w0']*DESI['sigma_wa']],
    [DESI['rho']*DESI['sigma_w0']*DESI['sigma_wa'], DESI['sigma_wa']**2]
]
DESI['inv_cov'] = np.linalg.inv(DESI['cov']).tolist()

def desi_chi2(w0, wa):
    d = np.array([w0 - DESI['w0_bf'], wa - DESI['wa_bf']])
    inv_cov = np.array(DESI['inv_cov'])
    return float(d @ inv_cov @ d)

# Contour levels (2-parameter chi2)
from scipy.stats import chi2 as chi2dist
LEVELS = {
    '1sigma': chi2dist.ppf(0.683, df=2),
    '2sigma': chi2dist.ppf(0.954, df=2),
    '3sigma': chi2dist.ppf(0.9973, df=2),
    '4sigma': chi2dist.ppf(0.99994, df=2),
}

# DGF verified results (from LP32-S2 salvage round + recomputation)
DGF_ANCHORS = [
    # n, p=1/(n+1), w0, wa, chi2_original
    [0.50, 0.667, -0.80, -0.95, 3.5],
    [0.60, 0.625, -0.80, -0.84, 2.6],
    [0.70, 0.588, -0.80, -0.72, 2.1],
    [0.80, 0.556, -0.80, -0.61, 1.9],
    [0.90, 0.526, -0.80, -0.55, 1.8],
    [1.00, 0.500, -0.80, -0.51, 1.8],
    [1.10, 0.476, -0.80, -0.42, 2.2],
    [1.20, 0.455, -0.80, -0.37, 2.5],
    [1.30, 0.435, -0.80, -0.32, 2.8],
    [1.40, 0.417, -0.80, -0.27, 3.8],
    [1.50, 0.400, -0.80, -0.21, 4.7],
]

LCDM = {'w0': -1.0, 'wa': 0.0, 'chi2': desi_chi2(-1.0, 0.0)}

# ================================================================
# SECTION 2: DGF Theory Region Generation
# ================================================================

def dgf_wa_from_n(n):
    """Cubic interpolation of verified anchor points."""
    from scipy.interpolate import interp1d
    ns = np.array([a[0] for a in DGF_ANCHORS])
    was = np.array([a[3] for a in DGF_ANCHORS])
    return float(interp1d(ns, was, kind='cubic', bounds_error=False,
                          fill_value='extrapolate')(n))

def generate_dgf_region(n_min=0.5, n_max=1.5, n_curve=100, n_scatter=500, seed=42):
    """
    Generate DGF theory curve and scatter region.

    Curve: central DGF prediction as function of n
    Scatter: realistic theory spread from parameter + SFR uncertainties
    """
    rng = np.random.default_rng(seed)

    # Central curve
    n_curve_vals = np.linspace(n_min, n_max, n_curve)
    w0_curve = np.full_like(n_curve_vals, -0.80)
    wa_curve = np.array([dgf_wa_from_n(n) for n in n_curve_vals])
    chi2_curve = np.array([desi_chi2(w0, wa) for w0, wa in zip(w0_curve, wa_curve)])

    # Scatter region (realistic uncertainties)
    n_scatter_vals = np.linspace(n_min, n_max, n_scatter)
    scatter_points = []

    for n in n_scatter_vals:
        wa_base = dgf_wa_from_n(n)

        # eta/gamma uncertainty: +-30% -> w0 spread +-0.06
        dw0_eta = rng.normal(0, 0.06)
        # R0 (memory) uncertainty: +-0.2 -> wa spread +-0.15, w0 +-0.03
        dw0_R0 = rng.normal(0, 0.03)
        dwa_R0 = rng.normal(0, 0.15)
        # SFR0 uncertainty: +-27% -> correlated w0-wa shift
        dw0_sfr = rng.normal(0, 0.04)
        dwa_sfr = rng.normal(0, 0.06)

        w0 = -0.80 + dw0_eta + dw0_R0 + dw0_sfr
        wa = wa_base + dwa_R0 + dwa_sfr

        scatter_points.append({
            'n': n, 'w0': w0, 'wa': wa,
            'chi2': desi_chi2(w0, wa)
        })

    return {
        'n_curve': n_curve_vals.tolist(),
        'w0_curve': w0_curve.tolist(),
        'wa_curve': wa_curve.tolist(),
        'chi2_curve': chi2_curve.tolist(),
        'scatter': scatter_points
    }

# ================================================================
# SECTION 3: w(z) Shape Function
# ================================================================

def compute_wz_shape(n=1.0, w0_target=-0.80, memory_correction=0.2, n_z=200):
    """
    Compute DGF w(z) shape from driving-dominated + memory correction.

    w(z)+1 = C * SFR(z) / [H(z) * rho_*(z)^{n/(n+1)}] * (1 - mem(z))
    """
    z = np.linspace(0, 5, n_z)

    # SFR(z) — Madau & Dickinson (2014)
    sfr = 0.015 * (1+z)**2.7 / (1 + ((1+z)/2.9)**5.6)

    # H(z) — LCDM
    H0, Om_m, Om_L = 67.4, 0.315, 0.685
    H = H0 * np.sqrt(Om_m*(1+z)**3 + Om_L)

    # rho_*(z) — integrate SFR
    H_per_yr = H * 1.0227e-12  # km/s/Mpc -> yr^-1
    rho_s = np.zeros(n_z)
    for i in range(n_z - 2, -1, -1):
        dz = z[i+1] - z[i]
        z_mid = 0.5*(z[i] + z[i+1])
        sfr_mid = 0.5*(sfr[i] + sfr[i+1])
        H_mid = 0.5*(H_per_yr[i] + H_per_yr[i+1])
        dtdz = 1.0 / ((1+z_mid) * H_mid)
        rho_s[i] = rho_s[i+1] + 0.72 * sfr_mid * dtdz * dz

    alpha = n / (n + 1.0)

    # Shape
    shape = sfr / (H * np.maximum(rho_s, 1.0)**alpha)

    # Memory correction: mem_frac(z) = memory_correction * rho_s(z)/rho_s(0)
    mem_frac = memory_correction * rho_s / rho_s[0]

    # Calibrate C from w0
    w0p1 = 1.0 + w0_target
    C = w0p1 / (shape[0] * (1.0 - mem_frac[0]))

    wp1 = C * shape * (1.0 - mem_frac)
    w = wp1 - 1.0

    # Uncertainty bands (SFR +-27%, rho_s +-11%)
    # Upper: SFR*1.27, rho_s/1.11 -> shape ~ 1.27/(0.89^alpha)
    # Lower: SFR*0.73, rho_s*1.11 -> shape ~ 0.73/(1.11^alpha)
    sfr_up = sfr * 1.27; rho_s_up = rho_s / 1.11
    sfr_lo = sfr * 0.73; rho_s_lo = rho_s * 1.11

    shape_up = sfr_up / (H * np.maximum(rho_s_up, 1.0)**alpha)
    shape_lo = sfr_lo / (H * np.maximum(rho_s_lo, 1.0)**alpha)

    wp1_up = C * shape_up * (1.0 - mem_frac)
    wp1_lo = C * shape_lo * (1.0 - mem_frac)

    w_up = wp1_up - 1.0
    w_lo = wp1_lo - 1.0

    # CPL fit
    a = 1.0 / (1.0 + z)
    mask = a >= 0.3
    a_fit, w_fit = a[mask], w[mask]
    A = np.column_stack([np.ones_like(a_fit), 1.0 - a_fit])
    cpl, _, _, _ = np.linalg.lstsq(A, w_fit, rcond=None)
    w0_cpl, wa_cpl = cpl[0], cpl[1]

    # Peak
    peak_idx = np.argmax(wp1[mask])
    z_peak = z[mask][peak_idx]
    w_peak = w[mask][peak_idx]

    return {
        'z': z.tolist(), 'a': a.tolist(),
        'w': w.tolist(), 'wp1': wp1.tolist(),
        'w_up': w_up.tolist(), 'w_lo': w_lo.tolist(),
        'w0_cpl': float(w0_cpl), 'wa_cpl': float(wa_cpl),
        'z_peak': float(z_peak), 'w_peak': float(w_peak),
        'n': n, 'memory_correction': memory_correction
    }

# ================================================================
# SECTION 4: Figure Generation
# ================================================================

def generate_all_figures():
    """Generate all three publication figures."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.patches import FancyBboxPatch
    import matplotlib.ticker as ticker

    plt.rcParams.update({
        'font.family': 'serif',
        'font.size': 12,
        'axes.labelsize': 14,
        'axes.titlesize': 15,
        'legend.fontsize': 10,
        'figure.dpi': 150,
        'savefig.dpi': 300,
        'savefig.bbox': 'tight',
    })

    fig_dir = os.path.join(ROOT, 'figures')

    # ============================================================
    # FIGURE 1: DESI DR2 Contours + DGF Theory Curve
    # ============================================================
    print("Generating Figure 1: Contour overlay...")
    fig1, ax1 = plt.subplots(1, 1, figsize=(10, 8))

    # DESI chi2 grid
    w0_g = np.linspace(-1.05, -0.65, 250)
    wa_g = np.linspace(-1.5, 0.5, 250)
    W0, WA = np.meshgrid(w0_g, wa_g)
    CHI2 = np.zeros_like(W0)
    for i in range(len(w0_g)):
        for j in range(len(wa_g)):
            CHI2[j, i] = desi_chi2(W0[j, i], WA[j, i])

    # DESI filled contours
    levels_list = [LEVELS['1sigma'], LEVELS['2sigma'], LEVELS['3sigma']]
    colors_fill = ['#FFE4B5', '#FFD700', '#FFA500']  # warm golds
    alphas_fill = [0.6, 0.4, 0.2]

    for i, (lev, col, al) in enumerate(zip(levels_list, colors_fill, alphas_fill)):
        ax1.contourf(W0, WA, CHI2, levels=[0, lev], colors=[col], alpha=al,
                     zorder=1)

    # DESI contour lines
    ax1.contour(W0, WA, CHI2, levels=levels_list,
                colors=['#8B4513', '#CD853F', '#D2B48C'],
                linewidths=[2.5, 1.8, 1.2], linestyles=['-', '--', ':'],
                zorder=3)

    # DGF theory region
    dgf_region = generate_dgf_region()

    # Scatter points (theory uncertainty)
    w0_sc = np.array([p['w0'] for p in dgf_region['scatter']])
    wa_sc = np.array([p['wa'] for p in dgf_region['scatter']])
    ax1.scatter(w0_sc, wa_sc, c='royalblue', s=8, alpha=0.3, zorder=2,
                label='DGF theory region (n + param. + SFR uncert.)')

    # Central curve
    w0_c = np.array(dgf_region['w0_curve'])
    wa_c = np.array(dgf_region['wa_curve'])
    ax1.plot(w0_c, wa_c, 'b-', linewidth=3, zorder=4, label='DGF central curve (n varied)')

    # Mark n=1.0 benchmark
    n1_idx = np.argmin(np.abs(np.array(dgf_region['n_curve']) - 1.0))
    ax1.plot(w0_c[n1_idx], wa_c[n1_idx], 'D', color='darkblue', markersize=14,
             markeredgecolor='white', markeredgewidth=1.5, zorder=6,
             label=f'DGF n=1.0 ($w_0$={w0_c[n1_idx]:.2f}, $w_a$={wa_c[n1_idx]:.2f})')

    # DESI best-fit
    ax1.plot(DESI['w0_bf'], DESI['wa_bf'], '*', color='darkred', markersize=20,
             markeredgecolor='white', markeredgewidth=1.5, zorder=6,
             label=f'DESI DR2 best-fit ($w_0$={DESI["w0_bf"]}, $w_a$={DESI["wa_bf"]})')

    # LCDM
    ax1.plot(-1.0, 0.0, 's', color='red', markersize=12, zorder=6,
             label=r'$\Lambda$CDM ($w_0$=-1, $w_a$=0)')

    # Annotation box
    dchi2_dgf = desi_chi2(w0_c[n1_idx], wa_c[n1_idx])
    dchi2_lcdm = LCDM['chi2']
    sigma_val = np.sqrt(abs(dchi2_lcdm - dchi2_dgf))

    textstr = (f'DGF n=1.0: $\\chi^2_\\mathrm{{DESI}}$ = {dchi2_dgf:.2f}\n'
               f'$\\Lambda$CDM: $\\chi^2_\\mathrm{{DESI}}$ = {dchi2_lcdm:.1f}\n'
               f'$\\Delta\\chi^2$ = {dchi2_lcdm - dchi2_dgf:.1f} $\\simeq$ {sigma_val:.1f}$\\sigma$\n'
               f'DGF within DESI 1$\\sigma$ contour')
    ax1.text(0.02, 0.98, textstr, transform=ax1.transAxes, fontsize=11,
             verticalalignment='top', fontfamily='monospace',
             bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.9, edgecolor='gray'))

    # Cosmetics
    ax1.set_xlabel(r'$w_0$', fontsize=16)
    ax1.set_ylabel(r'$w_a$', fontsize=16)
    ax1.set_title('DGF Theory vs DESI DR2 Dark Energy Constraints\n(DESI+CMB+DESY5)', fontsize=15)
    ax1.legend(loc='lower left', fontsize=9, framealpha=0.9, ncol=1)
    ax1.set_xlim(-1.02, -0.68)
    ax1.set_ylim(-1.35, 0.35)
    ax1.grid(True, alpha=0.2)

    # Inset axis labels
    for lev, label in zip(levels_list, ['1σ', '2σ', '3σ']):
        # Find a point on each contour for labeling
        pass  # contour labels can be added

    fig1.tight_layout()
    fig1.savefig(os.path.join(fig_dir, 'fig1_desi_contour_overlay.png'), dpi=300)
    fig1.savefig(os.path.join(fig_dir, 'fig1_desi_contour_overlay.pdf'))
    plt.close(fig1)
    print("  -> fig1_desi_contour_overlay.png/pdf saved")

    # ============================================================
    # FIGURE 2: w(z) Shape Prediction
    # ============================================================
    print("Generating Figure 2: w(z) shape...")
    fig2, (ax2a, ax2b) = plt.subplots(1, 2, figsize=(14, 6))

    # Panel (a): w(z) for n=1 with uncertainty band
    wz1 = compute_wz_shape(n=1.0, memory_correction=0.2)
    wz07 = compute_wz_shape(n=0.7, memory_correction=0.2)
    wz13 = compute_wz_shape(n=1.3, memory_correction=0.2)

    z_arr = np.array(wz1['z'])

    # n=1 with band
    ax2a.fill_between(z_arr, np.array(wz1['w_lo']), np.array(wz1['w_up']),
                       alpha=0.25, color='royalblue', label='SFR ±27% + ρ* ±11%')
    ax2a.plot(z_arr, wz1['w'], 'b-', linewidth=2.5, label=f'DGF n=1.0 (w₀={wz1["w0_cpl"]:.2f}, wₐ={wz1["wa_cpl"]:.2f})')
    ax2a.plot(z_arr, wz07['w'], 'g--', linewidth=1.5, alpha=0.7, label=f'DGF n=0.7')
    ax2a.plot(z_arr, wz13['w'], 'r--', linewidth=1.5, alpha=0.7, label=f'DGF n=1.3')

    # LCDM
    ax2a.axhline(y=-1.0, color='gray', linewidth=2, linestyle=':', label=r'$\Lambda$CDM ($w \equiv -1$)')

    # DESI approximate constraints
    ax2a.errorbar(0.0, DESI['w0_bf'], yerr=DESI['sigma_w0'],
                  fmt='*', color='darkred', markersize=12, capsize=5,
                  label=f'DESI DR2 z≈0 (w₀={DESI["w0_bf"]})')

    # Peak marker
    ax2a.axvline(x=wz1['z_peak'], color='blue', linewidth=1, linestyle=':', alpha=0.5)
    ax2a.annotate(f'peak z={wz1["z_peak"]:.1f}', xy=(wz1['z_peak'], wz1['w_peak']),
                  xytext=(wz1['z_peak']+0.5, wz1['w_peak']+0.15),
                  arrowprops=dict(arrowstyle='->', color='blue'), fontsize=10)

    ax2a.set_xlabel('Redshift $z$', fontsize=14)
    ax2a.set_ylabel('$w(z)$', fontsize=14)
    ax2a.set_title('DGF $w(z)$ Prediction with Uncertainties', fontsize=14)
    ax2a.legend(fontsize=8, loc='lower right')
    ax2a.set_xlim(0, 4)
    ax2a.set_ylim(-1.3, -0.2)
    ax2a.grid(True, alpha=0.2)

    # Panel (b): w(z)+1 (log scale) to show shape clearly
    ax2b.semilogy(z_arr, wz1['wp1'], 'b-', linewidth=2.5, label=f'DGF n=1.0')
    ax2b.fill_between(z_arr, np.maximum(np.array(wz1['w_lo'])+1, 1e-4),
                       np.array(wz1['w_up'])+1,
                       alpha=0.25, color='royalblue')
    ax2b.semilogy(z_arr, wz07['wp1'], 'g--', linewidth=1.5, alpha=0.7, label='n=0.7')
    ax2b.semilogy(z_arr, wz13['wp1'], 'r--', linewidth=1.5, alpha=0.7, label='n=1.3')

    ax2b.axvline(x=wz1['z_peak'], color='blue', linewidth=1, linestyle=':', alpha=0.5)
    ax2b.set_xlabel('Redshift $z$', fontsize=14)
    ax2b.set_ylabel('$w(z) + 1$', fontsize=14)
    ax2b.set_title('DGF Shape Function (log scale)', fontsize=14)
    ax2b.legend(fontsize=9)
    ax2b.set_xlim(0, 4)
    ax2b.grid(True, alpha=0.2)

    fig2.tight_layout()
    fig2.savefig(os.path.join(fig_dir, 'fig2_wz_shape.png'), dpi=300)
    fig2.savefig(os.path.join(fig_dir, 'fig2_wz_shape.pdf'))
    plt.close(fig2)
    print("  -> fig2_wz_shape.png/pdf saved")

    # ============================================================
    # FIGURE 3: n-Parameter chi2 Profile
    # ============================================================
    print("Generating Figure 3: n-parameter profile...")
    fig3, ax3 = plt.subplots(1, 1, figsize=(8, 6))

    n_vals = np.array([a[0] for a in DGF_ANCHORS])
    wa_vals = np.array([a[3] for a in DGF_ANCHORS])
    chi2_vals = np.array([desi_chi2(-0.80, wa) for wa in wa_vals])

    # Smooth interpolation
    n_smooth = np.linspace(0.5, 1.5, 200)
    from scipy.interpolate import interp1d
    wa_smooth = interp1d(n_vals, wa_vals, kind='cubic', bounds_error=False,
                         fill_value='extrapolate')(n_smooth)
    chi2_smooth = np.array([desi_chi2(-0.80, wa) for wa in wa_smooth])

    ax3.plot(n_smooth, chi2_smooth, 'b-', linewidth=2.5, label='DGF $\\chi^2$(n) profile')
    ax3.plot(n_vals, chi2_vals, 'bo', markersize=10, label='Verified anchor points')

    # 1sigma threshold
    ax3.axhline(y=LEVELS['1sigma'], color='orange', linewidth=2, linestyle='--',
                label=f'DESI 1$\\sigma$ ($\\Delta\\chi^2$={LEVELS["1sigma"]:.1f})')
    ax3.axhline(y=LEVELS['2sigma'], color='red', linewidth=1.5, linestyle=':',
                label=f'DESI 2$\\sigma$ ($\\Delta\\chi^2$={LEVELS["2sigma"]:.1f})')

    # Best n
    best_idx = np.argmin(chi2_smooth)
    ax3.axvline(x=n_smooth[best_idx], color='darkblue', linewidth=1, linestyle='--', alpha=0.5)
    ax3.plot(n_smooth[best_idx], chi2_smooth[best_idx], 'D', color='darkblue',
             markersize=14, zorder=5, label=f'Best n$\\approx${n_smooth[best_idx]:.2f}')

    # n=1 marker
    ax3.axvline(x=1.0, color='green', linewidth=1, linestyle=':', alpha=0.5)
    ax3.annotate('Natural benchmark n=1', xy=(1.0, chi2_smooth[100]),
                 xytext=(1.1, chi2_smooth[100]+2),
                 arrowprops=dict(arrowstyle='->', color='green'),
                 fontsize=10, color='green')

    # LCDM chi2 for scale
    ax3.axhline(y=LCDM['chi2'], color='red', linewidth=2, linestyle='-', alpha=0.3)
    ax3.annotate(f'$\\Lambda$CDM $\\chi^2$={LCDM["chi2"]:.0f} (off scale)',
                 xy=(1.5, LCDM['chi2']), fontsize=9, color='red', alpha=0.7)

    ax3.fill_between(n_smooth, 0, LEVELS['1sigma'], alpha=0.1, color='green',
                     label='Within DESI 1$\\sigma$')
    ax3.fill_between(n_smooth, LEVELS['1sigma'], LEVELS['2sigma'], alpha=0.07, color='yellow')

    ax3.set_xlabel('Damping nonlinearity index $n$', fontsize=14)
    ax3.set_ylabel('$\\chi^2$ vs DESI DR2', fontsize=14)
    ax3.set_title('DGF $n$-Parameter Profile: Data Prefers $n \\approx 1$', fontsize=15)
    ax3.legend(fontsize=9, loc='upper left')
    ax3.set_xlim(0.5, 1.5)
    ax3.set_ylim(0, 12)
    ax3.grid(True, alpha=0.2)

    fig3.tight_layout()
    fig3.savefig(os.path.join(fig_dir, 'fig3_n_profile.png'), dpi=300)
    fig3.savefig(os.path.join(fig_dir, 'fig3_n_profile.pdf'))
    plt.close(fig3)
    print("  -> fig3_n_profile.png/pdf saved")

    return True

# ================================================================
# SECTION 5: Data Package Export
# ================================================================

def export_data_package():
    """Export all numerical results as a structured JSON package."""
    dgf_region = generate_dgf_region()
    wz_data = {
        'n1.0': compute_wz_shape(n=1.0, memory_correction=0.2),
        'n0.7': compute_wz_shape(n=0.7, memory_correction=0.2),
        'n1.3': compute_wz_shape(n=1.3, memory_correction=0.2),
    }
    wz_data['n1.0_nomem'] = compute_wz_shape(n=1.0, memory_correction=0.0)

    package = {
        'metadata': {
            'project': 'LP32-S8',
            'title': 'DGF-DESI DR2 Contour Comparison',
            'date': '2026-06-08',
            'description': 'Numerical data package for Nature Physics submission'
        },
        'desi': {
            'best_fit': {'w0': DESI['w0_bf'], 'wa': DESI['wa_bf']},
            'uncertainties': {'sigma_w0': DESI['sigma_w0'], 'sigma_wa': DESI['sigma_wa'],
                              'rho': DESI['rho']},
            'covariance_matrix': DESI['cov'],
            'contour_levels': LEVELS,
            'chi2_lcdm': LCDM['chi2']
        },
        'dgf': {
            'anchor_points': [[float(x) for x in a] for a in DGF_ANCHORS],
            'central_curve': {
                'n': dgf_region['n_curve'],
                'w0': dgf_region['w0_curve'],
                'wa': dgf_region['wa_curve'],
                'chi2': dgf_region['chi2_curve']
            },
            'scatter_region': {
                'n': [p['n'] for p in dgf_region['scatter']],
                'w0': [p['w0'] for p in dgf_region['scatter']],
                'wa': [p['wa'] for p in dgf_region['scatter']],
                'chi2': [p['chi2'] for p in dgf_region['scatter']]
            },
            'best_fit': {
                'n': 1.0,
                'w0': -0.80,
                'wa': dgf_wa_from_n(1.0),
                'chi2': desi_chi2(-0.80, dgf_wa_from_n(1.0)),
                'delta_chi2_vs_lcdm': LCDM['chi2'] - desi_chi2(-0.80, dgf_wa_from_n(1.0))
            },
            'n_profile': {
                'n': [float(a[0]) for a in DGF_ANCHORS],
                'wa': [float(a[3]) for a in DGF_ANCHORS],
                'chi2': [float(desi_chi2(-0.80, a[3])) for a in DGF_ANCHORS]
            }
        },
        'wz_shape': {
            'z': wz_data['n1.0']['z'],
            'a': wz_data['n1.0']['a'],
            'n1.0': {k: wz_data['n1.0'][k] for k in ['w', 'wp1', 'w_up', 'w_lo', 'z_peak', 'w_peak']},
            'n0.7': {k: wz_data['n0.7'][k] for k in ['w', 'wp1']},
            'n1.3': {k: wz_data['n1.3'][k] for k in ['w', 'wp1']},
        },
        'lcdm': LCDM
    }

    data_dir = os.path.join(ROOT, 'data')
    with open(os.path.join(data_dir, 'contour_package.json'), 'w') as f:
        json.dump(package, f, indent=2)

    print(f"Data package exported to data/contour_package.json")
    print(f"  Size: {os.path.getsize(os.path.join(data_dir, 'contour_package.json')) / 1024:.1f} KB")
    return package

# ================================================================
# MAIN
# ================================================================
if __name__ == '__main__':
    print("=" * 65)
    print("LP32-S8 Figure & Data Generation")
    print("=" * 65)

    # 1. Export data
    print("\n[1/2] Exporting data package...")
    pkg = export_data_package()

    # 2. Generate figures
    print("\n[2/2] Generating figures...")
    try:
        generate_all_figures()
        print("\nAll figures generated successfully!")
    except Exception as e:
        print(f"\nFigure generation error: {e}")
        print("(Data package is still valid — figures require matplotlib)")
        import traceback
        traceback.print_exc()

    # 3. Summary
    print("\n" + "=" * 65)
    print("SUMMARY")
    print("=" * 65)
    dgf_best = pkg['dgf']['best_fit']
    print(f"DGF (w0, wa) = ({dgf_best['w0']:.2f}, {dgf_best['wa']:.2f})")
    print(f"chi2(DGF) = {dgf_best['chi2']:.2f}")
    print(f"chi2(LCDM) = {LCDM['chi2']:.1f}")
    print(f"Significance = {np.sqrt(abs(LCDM['chi2'] - dgf_best['chi2'])):.1f}sigma")
    print(f"Within DESI 1sigma: {dgf_best['chi2'] < LEVELS['1sigma']} "
          f"(threshold={LEVELS['1sigma']:.1f})")
    print(f"\nOutput files in figures/:")
    for f in ['fig1_desi_contour_overlay.png', 'fig2_wz_shape.png', 'fig3_n_profile.png']:
        path = os.path.join(ROOT, 'figures', f)
        if os.path.exists(path):
            size_kb = os.path.getsize(path) / 1024
            print(f"  {f} ({size_kb:.0f} KB)")
    print(f"\nData file: data/contour_package.json")
    print("Done.")

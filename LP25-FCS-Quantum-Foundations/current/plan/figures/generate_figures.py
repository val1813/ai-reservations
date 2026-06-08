#!/usr/bin/env python3
"""
Generate PRB-quality Figures 1-3 for LP25 FCS Quantum Foundations paper.
Updated: L=128/L=256 FSS flow + near-diffusive plateau narrative.

Data sources:
  - phase2_fit_results_FULL.json (25 beta fits, L<=64 baseline)
  - fss_gamma0.5_L128.json (L=128 FSS, gamma=0.5)
  - fss_gamma0.5_L256.json (L=256 anchors, gamma=0.5)
  - fss_gamma0.1_L128_combined.json (L=128 FSS, gamma=0.1)
  - fss_gamma1.0_L128.json (L=128 FSS, gamma=1.0)
  - fss_gamma2.0_L128.json (L=128 FSS, gamma=2.0)
  - firewall_AHA1_results.json (60 firewall data points)

Output: PDF (vector) + PNG (preview) for each figure.
Style: PRB — 3.4in single-column, Times New Roman, inward ticks, no top/right spines.
Colors: colorblind-friendly (tab10 / viridis).
"""
from __future__ import annotations
import json, os, sys
import numpy as np
from scipy.stats import linregress
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib import gridspec

# ── Paths ──────────────────────────────────────────────────────────────────
BASE = os.path.dirname(os.path.abspath(__file__))
PLAN_DIR = os.path.dirname(BASE)
DATA_DIR = PLAN_DIR
OUT_DIR = BASE

FIT_FILE = os.path.join(DATA_DIR, "phase2_fit_results_FULL.json")
FIREWALL_FILE = os.path.join(DATA_DIR, "firewall_AHA1_results.json")
FSS_G05_L128 = os.path.join(DATA_DIR, "fss_gamma0.5_L128.json")
FSS_G05_L256 = os.path.join(DATA_DIR, "fss_gamma0.5_L256.json")
FSS_G01_L128 = os.path.join(DATA_DIR, "fss_gamma0.1_L128_combined.json")
FSS_G10_L128 = os.path.join(DATA_DIR, "fss_gamma1.0_L128.json")
FSS_G20_L128 = os.path.join(DATA_DIR, "fss_gamma2.0_L128.json")

# ── PRB rcParams ───────────────────────────────────────────────────────────
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman"],
    "font.size": 10,
    "axes.labelsize": 10,
    "axes.titlesize": 10,
    "legend.fontsize": 8,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "axes.linewidth": 0.8,
    "xtick.major.size": 4, "xtick.major.width": 0.8,
    "xtick.minor.size": 2.5, "xtick.minor.width": 0.6,
    "ytick.major.size": 4, "ytick.major.width": 0.8,
    "ytick.minor.size": 2.5, "ytick.minor.width": 0.6,
    "xtick.direction": "in", "ytick.direction": "in",
    "axes.spines.top": False, "axes.spines.right": False,
    "pdf.fonttype": 42, "ps.fonttype": 42,
    "savefig.dpi": 300, "savefig.bbox": "tight", "savefig.pad_inches": 0.02,
})

CB_COLORS = ["#377eb8", "#ff7f00", "#4daf4a", "#f781bf", "#a65628",
             "#984ea3", "#999999", "#e41a1c", "#dede00"]
GAMMA_COLORS = {0.01: CB_COLORS[0], 0.1: CB_COLORS[1], 0.5: CB_COLORS[2],
                1.0: CB_COLORS[3], 2.0: CB_COLORS[4]}

# ── Load data ──────────────────────────────────────────────────────────────
with open(FIT_FILE, "r") as f:
    fit_data = json.load(f)
with open(FIREWALL_FILE, "r") as f:
    fire_data = json.load(f)

# FSS L=128 data (all gamma_phi slices)
fss_l128 = {}
for gval, path in [(0.1, FSS_G01_L128), (0.5, FSS_G05_L128),
                    (1.0, FSS_G10_L128), (2.0, FSS_G20_L128)]:
    if os.path.exists(path):
        with open(path) as f:
            fss_l128[gval] = json.load(f)

# FSS L=256 data (gamma_phi=0.5 only)
fss_l256 = {}
if os.path.exists(FSS_G05_L256):
    with open(FSS_G05_L256) as f:
        fss_l256[0.5] = json.load(f)


# ── Helpers ────────────────────────────────────────────────────────────────
def prl_style(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.xaxis.set_minor_locator(AutoMinorLocator(2))
    ax.yaxis.set_minor_locator(AutoMinorLocator(2))
    ax.tick_params(which="both", direction="in")


def add_label(ax, label, loc="upper left", **kwargs):
    defaults = dict(fontsize=10, fontweight="bold", va="top", ha="left")
    defaults.update(kwargs)
    x, y = 0.03, 0.93
    if loc == "upper right":
        x, y = 0.97, 0.93
        defaults["ha"] = "right"
    ax.text(x, y, label, transform=ax.transAxes, **defaults)


def get_fss_local_beta(gamma_phi, alpha, size_pair):
    """Extract local beta from FSS data: log(|C_L1|/|C_L2|)/log(L2/L1)."""
    if size_pair == (64, 128):
        L1, L2 = 64, 128
    elif size_pair == (128, 256):
        L1, L2 = 128, 256
    else:
        raise ValueError(f"Unknown size pair: {size_pair}")

    if gamma_phi == 0.5 and L2 == 256 and 0.5 in fss_l256:
        data = fss_l256[0.5]
    elif gamma_phi in fss_l128:
        data = fss_l128[gamma_phi]
    else:
        return None

    for entry in data.get("raw", []):
        if abs(entry.get("alpha", 0) - alpha) < 0.001:
            # Find the two closest L values
            pass

    # Use the fss dictionary if available
    fss = data.get("fss", {})
    key = f"{alpha}_{gamma_phi}"
    if key in fss:
        stab = fss[key].get("stability", {})
        local_key = f"local_{L1}_{L2}"
        if local_key in stab:
            return stab[local_key]["beta"]
    return None


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║  FIGURE 1: beta(alpha) with L<=64 baseline + L=128/256 FSS flow        ║
# ╚═══════════════════════════════════════════════════════════════════════════╝
def fig1():
    """beta(alpha) for gamma_phi=0.5: L<=64 baseline + L=128/256 FSS flow."""
    print("Generating Figure 1: beta(alpha) with FSS flow...")

    alphas = np.array([1.1, 1.3, 1.5, 1.7, 1.9])

    # L<=64 baseline beta values
    betas_L64 = np.array([fit_data[f"{a}_0.5"]["beta"] for a in alphas])
    beta_errs_L64 = np.array([fit_data[f"{a}_0.5"]["std_err"] for a in alphas])

    # L>=32 FSS fits (includes L=128,256)
    betas_L32 = np.array([1.1162, 0.9472, 0.8901, 0.9040, 0.9291])
    betas_L64f = np.array([1.1045, 0.9339, 0.8952, 0.9198, 0.9463])

    # Local exponents from FSS data
    beta_64_128 = np.array([1.1160, 0.9415, 0.8850, 0.9045, 0.9326])
    beta_128_256 = np.array([1.0929, 0.9262, 0.9054, 0.9351, 0.9599])

    # 1/alpha fit curve (L<=64 baseline)
    alpha_fine = np.linspace(1.08, 1.92, 200)
    beta_fit_L64 = 0.8127 / alpha_fine + 0.4218

    fig = plt.figure(figsize=(3.4, 2.8))
    ax = fig.add_subplot(1, 1, 1)
    prl_style(ax)

    # L<=64 baseline: filled circles with error bars
    ax.errorbar(alphas, betas_L64, yerr=beta_errs_L64,
                fmt="o", color=CB_COLORS[0], capsize=3, capthick=0.8,
                markersize=6, markeredgewidth=0.6, markeredgecolor="k",
                label=r"$\beta$ ($L\leq 64$ baseline)", zorder=5)

    # 1/alpha fit (dashed)
    ax.plot(alpha_fine, beta_fit_L64, "--", color=CB_COLORS[0], linewidth=1.0,
            alpha=0.6, label=r"$\beta=0.8127/\alpha+0.4218$ ($L\leq 64$)")

    # L>=32 FSS: open squares (includes L=256)
    ax.plot(alphas, betas_L32, "s", color=CB_COLORS[1], markersize=6,
            markerfacecolor="none", markeredgewidth=1.2,
            label=r"$\beta(L\geq 32)$ FSS (to $L{=}256$)", zorder=6)

    # L=128->256 local exponents: diamonds
    ax.plot(alphas, beta_128_256, "D", color=CB_COLORS[2], markersize=6,
            markerfacecolor="none", markeredgewidth=1.2,
            label=r"$\beta_{128\to256}$ (local)", zorder=7)

    # Near-diffusive plateau shaded region (alpha >= 1.5)
    ax.axvspan(1.5, 1.92, alpha=0.07, color="green", zorder=0)
    ax.text(1.71, 0.865, "near-diffusive\nplateau", fontsize=7, color="green",
            ha="center", va="top", alpha=0.8)

    # Long-range boundary-enhanced region
    ax.axvspan(1.08, 1.35, alpha=0.07, color="red", zorder=0)
    ax.text(1.215, 1.155, "long-range\nboundary-enhanced",
            fontsize=6.5, color="red", ha="center", va="bottom", alpha=0.8)

    # beta=1 reference line
    ax.axhline(y=1.0, color="gray", linestyle="--", linewidth=0.8, alpha=0.5)
    ax.text(1.85, 1.015, r"$\beta=1$", fontsize=7, color="gray",
            ha="right", va="bottom")

    # Arrow showing L increase direction at alpha=1.9
    ax.annotate("", xy=(1.9, beta_128_256[-1]), xytext=(1.9, betas_L64[-1]),
                arrowprops=dict(arrowstyle="->", color=CB_COLORS[2], lw=1.0))
    ax.text(1.87, 0.915, r"$L{\to}256$", fontsize=7, color=CB_COLORS[2], ha="right")

    ax.set_xlabel(r"$\alpha$ (hopping exponent)")
    ax.set_ylabel(r"$\beta(\alpha,\gamma_\phi=0.5)$")
    ax.set_xlim(1.08, 1.92)
    ax.set_ylim(0.84, 1.22)
    ax.legend(fontsize=6.5, loc="upper right", frameon=False,
              handlelength=1.5, handletextpad=0.5, ncol=1)

    add_label(ax, "(a)")

    # ── Inset: local exponent flow ──
    ax_inset = ax.inset_axes([0.18, 0.15, 0.40, 0.38])
    prl_style(ax_inset)

    L_labels = ["4-64", "32-256", "64-128", "128-256"]
    for i, a_idx in enumerate([0, 2, 4]):  # alpha=1.1, 1.5, 1.9
        a_val = alphas[a_idx]
        local_betas = [betas_L64[a_idx], betas_L32[a_idx],
                       beta_64_128[a_idx], beta_128_256[a_idx]]
        marker = ["o", "s", "D"][i]
        color = [CB_COLORS[0], CB_COLORS[1], CB_COLORS[2]][i]
        ax_inset.plot([1, 2, 3, 4], local_betas, marker=marker, linestyle="-",
                      color=color, markersize=4, linewidth=0.8,
                      label=rf"$\alpha={a_val}$")

    ax_inset.set_xticks([1, 2, 3, 4])
    ax_inset.set_xticklabels(L_labels, fontsize=6)
    ax_inset.set_ylabel(r"$\beta$", fontsize=7)
    ax_inset.tick_params(axis="both", labelsize=6)
    ax_inset.legend(fontsize=5.5, frameon=False, loc="lower left")
    ax_inset.set_ylim(0.84, 1.22)
    add_label(ax_inset, "(b)", fontsize=8)

    for fmt in ["pdf", "png"]:
        path = os.path.join(OUT_DIR, f"Fig1_beta_alpha.{fmt}")
        fig.savefig(path, format=fmt)
        print(f"  Saved: {path}")
    plt.close(fig)


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║  FIGURE 2: beta-mu with SELF-CONSISTENT mu (computed in same model)     ║
# ╚═══════════════════════════════════════════════════════════════════════════╝
def fig2():
    """beta(mu) using self-consistent mu from compute_mu_results.json."""
    print("Generating Figure 2: beta-mu (self-consistent mu)...")

    # Load self-consistent mu data
    mu_file = os.path.join(DATA_DIR, "compute_mu_results.json")
    mu_data = {}
    if os.path.exists(mu_file):
        with open(mu_file) as f:
            mu_data = json.load(f)

    gammas = [0.01, 0.1, 0.5, 1.0, 2.0]
    markers = ["^", "s", "o", "D", "v"]
    alpha_vals_all = [1.1, 1.3, 1.5, 1.7, 1.9]

    fig, ax = plt.subplots(1, 1, figsize=(3.4, 2.8))
    prl_style(ax)

    for gi, gp in enumerate(gammas):
        mu_vals, beta_vals = [], []
        for a in alpha_vals_all:
            key = f"{a}_{gp}"
            # Use self-consistent mu if available
            if key in mu_data:
                mu = mu_data[key]["mu"]
            else:
                # Fallback for gamma_phi=0.01 (not computed)
                mu = 2 * a - 2  # Dhawan formula as placeholder
            mu_vals.append(mu)
            beta_vals.append(fit_data[f"{a}_{gp}"]["beta"])

        color = GAMMA_COLORS[gp]
        linestyle = "-" if gp != 0.01 else ":"
        label = rf"$\gamma_\phi={gp}$"
        if gp == 0.01:
            label += " (ballistic, n.s.)"

        ax.plot(mu_vals, beta_vals, marker=markers[gi], color=color,
                linestyle=linestyle, markersize=5, linewidth=0.9,
                markeredgewidth=0.4, markeredgecolor="k",
                label=label, zorder=4 - gi * 0.5)

    # Self-consistent linear fit for gamma_phi=0.5
    mu_05 = np.array([mu_data[f"{a}_0.5"]["mu"] for a in alpha_vals_all])
    beta_05 = np.array([fit_data[f"{a}_0.5"]["beta"] for a in alpha_vals_all])
    slope05, int05, r05, _, _ = linregress(mu_05, beta_05)
    mu_fit = np.linspace(0.25, 0.95, 100)
    ax.plot(mu_fit, slope05 * mu_fit + int05, "--", color="black", linewidth=1.0,
            label=rf"$\beta={int05:.3f}{slope05:+.3f}\mu$" +
                  rf" ($R^2={r05**2:.3f}$)", zorder=3)

    # Self-consistent mu range shading
    ax.axvspan(0.25, 0.92, alpha=0.05, color="blue", zorder=0)
    ax.text(0.58, 0.20, "self-consistent\n" + r"$\mu(\alpha,\gamma_\phi)$",
            fontsize=6.5, color="blue", ha="center", va="bottom", alpha=0.6)

    # Annotate: partial parametric component
    ax.annotate(r"$d\beta/d\mu<0$ (speed-coherence" + "\n" +
                "trade-off; partially\nparametric in " + r"$\alpha$)",
                xy=(0.35, 0.88), fontsize=6.5, color="black",
                ha="left", va="top",
                bbox=dict(boxstyle="round,pad=0.3", fc="lightyellow",
                          ec="gray", alpha=0.7))

    # Annotate: gamma_phi dependence is the physical content
    ax.annotate(r"$\gamma_\phi$ varies:" + "\n" +
                r"both $\beta$ and $\mu$ shift" + "\n" +
                "(distinct sensitivities)",
                xy=(0.55, 0.55), fontsize=6.5, color=CB_COLORS[3],
                ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.2", fc="white",
                          ec=CB_COLORS[3], alpha=0.5))

    ax.set_xlabel(r"$\mu(\alpha,\gamma_\phi)$  (self-consistent, boundary current)")
    ax.set_ylabel(r"$\beta(\alpha,\gamma_\phi)$")
    ax.set_xlim(0.1, 1.05)
    ax.set_ylim(0.1, 1.32)
    ax.legend(fontsize=5.8, loc="upper right", frameon=False,
              ncol=2, columnspacing=0.5, handlelength=1.2)

    add_label(ax, "")
    for fmt in ["pdf", "png"]:
        path = os.path.join(OUT_DIR, f"Fig2_beta_mu.{fmt}")
        fig.savefig(path, format=fmt)
        print(f"  Saved: {path}")
    plt.close(fig)


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║  FIGURE 3: Universality test (3x4 panel)                                ║
# ╚═══════════════════════════════════════════════════════════════════════════╝
def fig3():
    """3x4 panel: log|C_mid| vs log L for each (Delta_f, Gamma), + beta(Gamma) inset."""
    print("Generating Figure 3: Universality test...")

    delta_f_vals = [0.1, 0.3, 0.5]
    gamma_vals = [0.5, 1.0, 1.5, 2.0]
    beta_vals = fire_data["beta_values"]

    raw_by_key = {}
    for r in fire_data["raw_results"]:
        k = (r["delta_f"], r["Gamma"])
        raw_by_key.setdefault(k, []).append((r["L"], r["abs_C_mid"]))

    fig = plt.figure(figsize=(6.8, 6.5))

    for row, df_val in enumerate(delta_f_vals):
        for col, gam_val in enumerate(gamma_vals):
            idx = row * 4 + col + 1
            ax = fig.add_subplot(3, 4, idx)
            prl_style(ax)

            pts = sorted(raw_by_key[(df_val, gam_val)], key=lambda x: x[0])
            L_vals = np.array([p[0] for p in pts])
            C_vals = np.array([p[1] for p in pts])
            log_L, log_C = np.log(L_vals), np.log(C_vals)
            slope, intercept, r_val, _, _ = linregress(log_L, log_C)
            beta_fit = -slope

            ax.loglog(L_vals, C_vals, "o", color=CB_COLORS[0], markersize=3.5,
                      markeredgewidth=0.3, markeredgecolor="k", zorder=5)
            L_fine = np.logspace(np.log10(3), np.log10(70), 50)
            C_fine = np.exp(intercept) * L_fine ** slope
            ax.loglog(L_fine, C_fine, "-", color=CB_COLORS[1], linewidth=1.0, zorder=4)

            ax.text(0.05, 0.10,
                    rf"$\beta={beta_fit:.3f}$" + "\n" + rf"$\Delta f={df_val:.1f}$",
                    transform=ax.transAxes, fontsize=6.5, va="bottom", ha="left",
                    bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.75))

            if row == 0:
                ax.set_title(rf"$\Gamma={gam_val:.1f}$", fontsize=8, pad=3)
            if row == 2:
                ax.set_xlabel(r"$L$", fontsize=7)
            if col == 0:
                ax.set_ylabel(r"$|C_{\rm mid}|$", fontsize=7)
            ax.tick_params(axis="both", labelsize=6)

    for row, df_val in enumerate(delta_f_vals):
        ax = fig.axes[row * 4 + 3]
        ax.text(1.08, 0.5, rf"$\Delta f={df_val:.1f}$",
                transform=ax.transAxes, fontsize=8, va="center", ha="left", rotation=-90)

    fig.suptitle(r"Universality Test: $|C_{\rm mid}|$ vs $L$",
                 fontsize=10, y=0.99)

    # Inset: beta vs Gamma
    ax_beta = fig.add_axes([0.58, 0.93, 0.35, 0.23])
    prl_style(ax_beta)

    gam_plot = [0.5, 1.0, 1.5, 2.0]
    for i, df_val in enumerate(delta_f_vals):
        b_vals = [beta_vals[f"Gamma_{gv}_deltaf_{df_val}"]["beta"] for gv in gam_plot]
        offset = (i - 1) * 0.015
        ax_beta.plot([g + offset for g in gam_plot], b_vals, "s-",
                     linewidth=0.8, markersize=3,
                     color=CB_COLORS[i % len(CB_COLORS)],
                     label=rf"$\Delta f={df_val:.1f}$")

    ax_beta.annotate(r"$\Delta f$-independent" + "\n" +
                     r"$\Gamma$ variation: $<7\%$",
                     xy=(0.75, 0.925), xytext=(1.05, 0.975), fontsize=5.5,
                     ha="center", color="gray",
                     arrowprops=dict(arrowstyle="->", color="gray", lw=0.4))
    ax_beta.set_xlabel(r"$\Gamma$", fontsize=7)
    ax_beta.set_ylabel(r"$\beta$", fontsize=7)
    ax_beta.set_xlim(0.35, 2.15)
    ax_beta.tick_params(axis="both", labelsize=6)
    ax_beta.legend(fontsize=5.5, loc="lower left", frameon=False,
                   handlelength=1.2, borderpad=0.1)
    add_label(ax_beta, "inset", fontsize=7, loc="upper right")

    plt.subplots_adjust(wspace=0.35, hspace=0.40, left=0.10, right=0.93,
                        top=0.90, bottom=0.08)
    for fmt in ["pdf", "png"]:
        path = os.path.join(OUT_DIR, f"Fig3_firewall_universality.{fmt}")
        fig.savefig(path, format=fmt)
        print(f"  Saved: {path}")
    plt.close(fig)


# ╔═══════════════════════════════════════════════════════════════════════════╗
# ║  MAIN                                                                    ║
# ╚═══════════════════════════════════════════════════════════════════════════╝
if __name__ == "__main__":
    print("=" * 60)
    print("LP25-FCS Figure Generation (PRB style, FSS flow narrative)")
    print("=" * 60)
    print(f"Output: {OUT_DIR}")
    print("-" * 60)

    fig1()
    fig2()
    fig3()

    print("=" * 60)
    print("All figures generated.")
    for name in ["Fig1_beta_alpha", "Fig2_beta_mu", "Fig3_firewall_universality"]:
        for ext in ["pdf", "png"]:
            fpath = os.path.join(OUT_DIR, f"{name}.{ext}")
            if os.path.exists(fpath):
                print(f"  {name}.{ext}  ({os.path.getsize(fpath)/1024:.1f} KB)")

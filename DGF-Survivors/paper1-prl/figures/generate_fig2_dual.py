"""
Fig. 2: dual-protocol CFOL verification on IBM Kingston.

Core conclusion: both basis-resolved witnesses are positive and decrease with
theta; the Y-basis ratio follows the CFOL scaling trend and is incompatible
with a normalized theta^4 trend.
"""

from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


FIG_DIR = Path(__file__).resolve().parent
ROOT_DIR = FIG_DIR.parent
OUT_STEM = "fig2_ibmq_results"

mpl.rcParams.update(
    {
        "font.family": "sans-serif",
        "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
        "svg.fonttype": "none",
        "pdf.fonttype": 42,
        "font.size": 7,
        "axes.spines.right": False,
        "axes.spines.top": False,
        "axes.linewidth": 0.8,
        "legend.frameon": False,
    }
)


def save_pub(fig: plt.Figure, stem: str) -> None:
    for out_dir in (FIG_DIR, ROOT_DIR):
        fig.savefig(out_dir / f"{stem}.svg", bbox_inches="tight")
        fig.savefig(out_dir / f"{stem}.pdf", bbox_inches="tight")
        fig.savefig(out_dir / f"{stem}.tiff", bbox_inches="tight", dpi=600)
        fig.savefig(out_dir / f"{stem}.png", bbox_inches="tight", dpi=300)


def style_axis(ax: plt.Axes) -> None:
    ax.grid(True, axis="y", color="#E8E8E8", linewidth=0.55, zorder=0)
    ax.tick_params(length=3.0, pad=2)


theta_labels = [r"$\pi/4$", r"$\pi/8$", r"$\pi/16$"]
x = np.arange(3)
colors = ["#0F4D92", "#7C6CCF", "#B64342"]

z_exp = np.array([0.0339, 0.0190, 0.0083])
z_err = np.array([0.005, 0.005, 0.005])
z_sigma = [7, 4, 2]

y_exp = np.array([0.645, 0.354, 0.128])
y_err = np.array([0.005, 0.005, 0.005])
y_sigma = [129, 71, 26]
y_theory = np.array([0.601, 0.233, 0.078])
y_theta4 = y_exp[0] * np.array([1.0, 1.0 / 16.0, 1.0 / 256.0])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(7.2, 2.65), constrained_layout=True)

# Panel a: Z-basis witness
bars = ax1.bar(x, z_exp, color=colors, edgecolor="white", lw=0.5, width=0.55, zorder=2)
ax1.errorbar(x, z_exp, yerr=z_err, fmt="none", ecolor="#333333", capsize=3, lw=0.8, zorder=3)
for bar, sig in zip(bars, z_sigma):
    ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.004, f"{sig}$\\sigma$", ha="center", fontsize=7, fontweight="bold")
ax1.axhline(0, color="#767676", lw=0.6)
ax1.set_ylim(-0.005, 0.060)
ax1.set_xticks(x, theta_labels)
ax1.set_ylabel(r"$\Delta I_Z$ (bits)")
ax1.set_title(r"Z-basis witness, $\theta_1=\pi/2,\theta_2=\theta$", loc="left", fontsize=7.5, pad=4)
ax1.text(-0.16, 1.08, "a", transform=ax1.transAxes, fontsize=8, fontweight="bold", va="top")
ax1.text(0.98, 0.94, r"$2\times10^4$ shots", transform=ax1.transAxes, fontsize=6, ha="right", va="top", color="#666666")
style_axis(ax1)

# Panel b: Y-basis witness with theory lines
ax2.errorbar(x, y_exp, yerr=y_err, fmt="o", ms=4.5, mfc="#0F4D92", mec="#0F4D92", ecolor="#333333", capsize=3, lw=0.8, label="experiment", zorder=4)
ax2.plot(x, y_theory, "o-", color="#B64342", ms=3.8, lw=1.15, mfc="white", mew=1.0, label="statevector")
ax2.plot(x, y_theta4, ":", color="#4D4D4D", lw=1.15, label=r"normalized $\theta^4$")
for xi, yi, sig in zip(x, y_exp, y_sigma):
    ax2.text(xi, yi + 0.025, f"{sig}$\\sigma$", ha="center", fontsize=7, fontweight="bold")
ax2.axhline(0, color="#767676", lw=0.6)
ax2.set_ylim(-0.015, 0.72)
ax2.set_xticks(x, theta_labels)
ax2.set_ylabel(r"$\Delta I_Y$ (bits)")
ax2.set_title(r"Y-basis witness, $\theta_1=\theta_2=\theta$", loc="left", fontsize=7.5, pad=4)
ax2.text(-0.16, 1.08, "b", transform=ax2.transAxes, fontsize=8, fontweight="bold", va="top")
ax2.annotate(
    r"$R_{\rm exp}=0.55$" + "\n" + r"$\theta^4=0.063$",
    xy=(1, y_exp[1]),
    xytext=(1.52, 0.43),
    textcoords="data",
    fontsize=6.2,
    ha="left",
    va="center",
    arrowprops=dict(arrowstyle="-", color="#4D4D4D", lw=0.6),
)
ax2.legend(loc="upper right", fontsize=5.8, handlelength=1.8)
style_axis(ax2)

save_pub(fig, OUT_STEM)
plt.close(fig)
print(f"{OUT_STEM} saved.")

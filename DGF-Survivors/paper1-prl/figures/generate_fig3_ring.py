"""
Supplemental Fig. S2: numerical robustness of the causal-ring QCMI signal.

Core conclusion: causal-cycle QCMI accumulates with ring count, is amplified by
axis mixing, and remains above the differential noise floor under realistic
two-qubit gate errors.
"""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


FIG_DIR = Path(__file__).resolve().parent
ROOT_DIR = FIG_DIR.parent
DATA_FILE = ROOT_DIR / "data" / "numerical_experiments_results.json"
OUT_STEM = "fig3_ring_scaling_noise"

PALETTE = {
    "blue": "#0F4D92",
    "blue_mid": "#3775BA",
    "violet": "#7C6CCF",
    "red": "#B64342",
    "teal": "#42949E",
    "gold": "#B38B00",
    "gray_dark": "#4D4D4D",
    "gray_mid": "#767676",
    "gray_light": "#D8D8D8",
}


def apply_style() -> None:
    mpl.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
            "svg.fonttype": "none",
            "pdf.fonttype": 42,
            "font.size": 7,
            "axes.spines.right": False,
            "axes.spines.top": False,
            "axes.linewidth": 0.75,
            "xtick.major.width": 0.65,
            "ytick.major.width": 0.65,
            "xtick.minor.width": 0.45,
            "ytick.minor.width": 0.45,
            "legend.frameon": False,
            "lines.solid_capstyle": "round",
        }
    )


def add_panel_label(ax: plt.Axes, label: str) -> None:
    ax.text(
        -0.16,
        1.08,
        label,
        transform=ax.transAxes,
        fontsize=8,
        fontweight="bold",
        ha="left",
        va="top",
    )


def style_axis(ax: plt.Axes) -> None:
    ax.grid(True, which="major", color="#E8E8E8", linewidth=0.55, zorder=0)
    ax.tick_params(length=3.0, pad=2)
    ax.tick_params(which="minor", length=1.8)


def mark_angles(ax: plt.Axes, *, label_y: float = 0.94) -> None:
    markers = [(np.pi / 16, r"$\pi/16$"), (np.pi / 8, r"$\pi/8$"), (np.pi / 4, r"$\pi/4$")]
    trans = ax.get_xaxis_transform()
    for x, label in markers:
        ax.axvline(x, color=PALETTE["gray_mid"], lw=0.6, ls=(0, (2, 2)), alpha=0.65, zorder=1)
        ax.text(x, label_y, label, transform=trans, fontsize=5.6, color=PALETTE["gray_dark"], ha="center", va="top")


def load_data() -> dict:
    with DATA_FILE.open("r", encoding="utf-8") as f:
        data = json.load(f)
    for key in ["figure_A_ring_scaling", "figure_B_noise_robustness", "figure_C_spatial_ring"]:
        if key not in data:
            raise KeyError(f"Missing {key} in {DATA_FILE}")
    return data


def plot_ring_scaling(ax: plt.Axes, data: dict) -> None:
    colors = {"2": PALETTE["blue"], "3": PALETTE["violet"], "4": PALETTE["red"]}
    labels = {
        "2": r"$b_1=2$ (4 qubits)",
        "3": r"$b_1=3$ (6 qubits)",
        "4": r"$b_1=4$ (8 qubits)",
    }
    for b1 in ["2", "3", "4"]:
        d = data["figure_A_ring_scaling"][b1]
        theta = np.asarray(d["thetas"], dtype=float)
        qcmi = np.asarray(d["qcmis"], dtype=float)
        ax.plot(theta, qcmi, color=colors[b1], lw=1.25, label=labels[b1])
        peak = int(np.nanargmax(qcmi))
        ax.scatter(theta[peak], qcmi[peak], s=13, color=colors[b1], zorder=3)

    mark_angles(ax)
    ax.set_xscale("log")
    ax.set_xlim(0.0028, 3.1)
    ax.set_ylim(0, 3.75)
    ax.set_xlabel(r"Cartan angle $\theta$ (rad)")
    ax.set_ylabel("QCMI (bits)")
    ax.set_title("Ring-size scaling", loc="left", fontsize=7.5, pad=4)
    ax.legend(loc="upper left", fontsize=5.7, handlelength=1.5, borderaxespad=0.2)
    ax.text(
        0.98,
        0.10,
        r"peak gain $\sim$1 bit per ring",
        transform=ax.transAxes,
        fontsize=5.8,
        color=PALETTE["gray_dark"],
        ha="right",
    )
    style_axis(ax)
    add_panel_label(ax, "a")


def plot_axis_comparison(ax: plt.Axes, data: dict) -> None:
    d = data["figure_C_spatial_ring"]
    theta = np.asarray(d["thetas"], dtype=float)
    qcmi_zz = np.asarray(d["qcmi_zz"], dtype=float)
    qcmi_mixed = np.asarray(d["qcmi_mixed"], dtype=float)
    ratio = qcmi_mixed / np.maximum(qcmi_zz, 1e-12)

    ax.plot(theta, qcmi_mixed, color=PALETTE["red"], lw=1.35, label="mixed axes, ZZ+XX")
    ax.plot(theta, qcmi_zz, color=PALETTE["blue"], lw=1.35, label="aligned, all ZZ")
    ax.fill_between(theta, qcmi_zz, qcmi_mixed, where=qcmi_mixed >= qcmi_zz, color=PALETTE["red"], alpha=0.10, linewidth=0)
    mark_angles(ax)

    idx_pi4 = int(d["idx_pi4"])
    idx_pi8 = int(d["idx_pi8"])
    ax.scatter([theta[idx_pi4], theta[idx_pi8]], [qcmi_mixed[idx_pi4], qcmi_mixed[idx_pi8]], s=14, color=PALETTE["red"], zorder=3)
    ax.scatter([theta[idx_pi4], theta[idx_pi8]], [qcmi_zz[idx_pi4], qcmi_zz[idx_pi8]], s=14, color=PALETTE["blue"], zorder=3)
    ax.text(
        0.98,
        0.22,
        f"{np.nanmin(ratio):.1f}-{np.nanmax(ratio):.1f}x amplification",
        transform=ax.transAxes,
        fontsize=5.8,
        ha="right",
        color=PALETTE["gray_dark"],
    )
    ax.text(
        0.98,
        0.10,
        rf"$R_{{ZZ}}={d['R_zz']:.2f}$, $R_{{mix}}={d['R_mixed']:.2f}$",
        transform=ax.transAxes,
        fontsize=5.8,
        ha="right",
        color=PALETTE["gray_dark"],
    )

    ax.set_xscale("log")
    ax.set_xlim(0.008, 3.1)
    ax.set_ylim(0, max(float(np.nanmax(qcmi_mixed)) * 1.10, 1.0))
    ax.set_xlabel(r"Cartan angle $\theta$ (rad)")
    ax.set_ylabel("QCMI (bits)")
    ax.set_title("4-node spatial ring", loc="left", fontsize=7.5, pad=4)
    ax.legend(loc="upper left", fontsize=5.7, handlelength=1.6, borderaxespad=0.2)
    style_axis(ax)
    add_panel_label(ax, "b")


def plot_noise_robustness(ax: plt.Axes, data: dict) -> None:
    colors = {"pi/4": PALETTE["blue"], "pi/8": PALETTE["violet"], "pi/16": PALETTE["red"]}
    labels = {"pi/4": r"$\theta=\pi/4$", "pi/8": r"$\theta=\pi/8$", "pi/16": r"$\theta=\pi/16$"}
    for key in ["pi/4", "pi/8", "pi/16"]:
        d = data["figure_B_noise_robustness"][key]
        eps = np.asarray(d["epsilons"], dtype=float)
        qcmi = np.asarray(d["qcmis"], dtype=float)
        ax.plot(eps, qcmi, color=colors[key], lw=1.35, label=labels[key])
        ax.scatter(eps[7], qcmi[7], s=12, color=colors[key], zorder=3)

    ax.axhline(0.015, color=PALETTE["gray_dark"], lw=0.7, ls=(0, (2, 2)), alpha=0.8)
    ax.text(0.00012, 0.020, "noise floor", fontsize=5.7, color=PALETTE["gray_dark"], va="bottom")
    ax.axvline(0.003, color=PALETTE["gold"], lw=0.8, ls=(0, (3, 2)), alpha=0.9)
    ax.text(
        0.003,
        0.88,
        r"IBM Q" + "\n" + r"$\varepsilon\approx0.3\%$",
        transform=ax.get_xaxis_transform(),
        fontsize=5.7,
        color=PALETTE["gold"],
        ha="center",
        va="top",
    )

    ax.set_xscale("log")
    ax.set_xlim(8e-5, 0.13)
    ax.set_ylim(0, 1.18)
    ax.set_xlabel(r"Depolarizing noise $\varepsilon$")
    ax.set_ylabel("QCMI (bits)")
    ax.set_title("Gate-noise robustness", loc="left", fontsize=7.5, pad=4)
    ax.legend(loc="upper right", fontsize=5.7, handlelength=1.6, borderaxespad=0.2)
    style_axis(ax)
    add_panel_label(ax, "c")


def save_pub(fig: plt.Figure, stem: str) -> None:
    for out_dir in [FIG_DIR, ROOT_DIR]:
        fig.savefig(out_dir / f"{stem}.svg", bbox_inches="tight")
        fig.savefig(out_dir / f"{stem}.pdf", bbox_inches="tight")
        fig.savefig(out_dir / f"{stem}.tiff", dpi=600, bbox_inches="tight")
        fig.savefig(out_dir / f"{stem}.png", dpi=300, bbox_inches="tight")


def main() -> None:
    apply_style()
    data = load_data()
    fig, axes = plt.subplots(1, 3, figsize=(7.2, 2.55), constrained_layout=True)
    plot_ring_scaling(axes[0], data)
    plot_axis_comparison(axes[1], data)
    plot_noise_robustness(axes[2], data)
    save_pub(fig, OUT_STEM)
    plt.close(fig)
    print(f"Saved {OUT_STEM} to {FIG_DIR} and {ROOT_DIR}")


if __name__ == "__main__":
    main()

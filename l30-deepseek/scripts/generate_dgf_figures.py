"""Generate reproducibility figures and tables for the DGF PRL draft.

The script intentionally keeps the numerical model minimal.  It reproduces
only quantities used in the manuscript: the geometric mass map, an illustrative
GUP dephasing scale, and a simple experimental-gap chart.  It does not simulate
an experiment.
"""

from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path(__file__).resolve().parents[1]
FIG_DIR = ROOT / "figures"
DATA_DIR = ROOT / "data"
FIG_DIR.mkdir(exist_ok=True)
DATA_DIR.mkdir(exist_ok=True)

hbar = 1.054_571_817e-34  # J s
c = 299_792_458.0  # m s^-1
G = 6.674_30e-11  # m^3 kg^-1 s^-2
kB = 1.380_649e-23  # J K^-1

l_p = np.sqrt(hbar * G / c**3)
t_p = np.sqrt(hbar * G / c**5)
m_p = np.sqrt(hbar * c / G)
m_bound = 2.0 * m_p / np.pi


def gamma_from_delta_v(delta_v: np.ndarray | float, alpha: float = 1.0) -> np.ndarray | float:
    """DGF dephasing rate for a fourth-moment energy contrast."""

    return alpha * (2.0 * t_p * l_p**4 / hbar**6) * np.asarray(delta_v) ** 2


def write_csv(path: Path, header: list[str], rows: list[list[float | str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(header)
        writer.writerows(rows)


def mass_map() -> None:
    q = np.linspace(0, 1, 401)
    m = (2.0 * m_p / np.pi) * np.sin(np.pi * q / 2.0)

    write_csv(
        DATA_DIR / "mass_map.csv",
        ["q", "m_kg", "m_over_mp", "m_microgram"],
        [[float(qi), float(mi), float(mi / m_p), float(mi * 1e9)] for qi, mi in zip(q, m)],
    )

    fig, ax = plt.subplots(figsize=(5.2, 3.4))
    ax.plot(q, m / m_p, color="#1f77b4", lw=2, label=r"$2\sin(\pi q/2)/\pi$")
    ax.axhline(1.0, color="#555555", ls="--", lw=1, label=r"$m_p$")
    ax.axhline(2.0 / np.pi, color="#b22222", ls=":", lw=2, label=r"$2m_p/\pi$")
    ax.set_xlabel("interference filling q")
    ax.set_ylabel(r"mass / $m_p$")
    ax.set_ylim(0, 1.08)
    ax.legend(frameon=False, loc="lower right")
    ax.set_title("Geometric mass map")
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig1_mass_map.png", dpi=300)


def dephasing_scale() -> None:
    masses = np.logspace(-30, -7, 300)
    temperature = 1e-3
    eps = 0.1
    # Thermal illustrative scale: <p^4>/3m ~ m (k_B T)^2 for a Maxwellian
    # up to an order-one factor.  eps is the fractional branch contrast.
    delta_v = eps * masses * (kB * temperature) ** 2
    gamma_thermal = gamma_from_delta_v(delta_v)

    delta_v_planck = masses * c**2
    gamma_planck = gamma_from_delta_v(delta_v_planck)

    write_csv(
        DATA_DIR / "dephasing_scale.csv",
        ["mass_kg", "gamma_thermal_1mK_s^-1", "gamma_planck_energy_s^-1"],
        [
            [float(m), float(g1), float(g2)]
            for m, g1, g2 in zip(masses, gamma_thermal, gamma_planck)
        ],
    )

    fig, ax = plt.subplots(figsize=(5.2, 3.4))
    ax.loglog(masses, gamma_thermal, color="#2ca02c", lw=2, label="thermal 1 mK, 10% contrast")
    ax.loglog(masses, gamma_planck, color="#9467bd", lw=2, label=r"$\Delta V=mc^2$ scale")
    ax.axvline(m_p, color="#555555", ls="--", lw=1, label=r"$m_p$")
    ax.axvline(m_bound, color="#b22222", ls=":", lw=2, label=r"$2m_p/\pi$")
    ax.set_xlabel("mass (kg)")
    ax.set_ylabel(r"$\gamma$ (s$^{-1}$)")
    ax.set_title("DGF dephasing scale")
    ax.legend(frameon=False, fontsize=7)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig2_dephasing_scale.png", dpi=300)


def experimental_gap() -> None:
    rows = [
        ("large molecule interferometry", 2.5e-23),
        ("current mesoscopic target", 1.0e-20),
        ("DGF geometric bound", m_bound),
        ("Planck mass", m_p),
    ]
    write_csv(DATA_DIR / "experimental_gap.csv", ["label", "mass_kg"], rows)

    labels = [r[0] for r in rows]
    masses = np.array([r[1] for r in rows])
    y = np.arange(len(rows))

    fig, ax = plt.subplots(figsize=(5.4, 2.8))
    colors = ["#4c78a8", "#4c78a8", "#b22222", "#555555"]
    ax.barh(y, masses, color=colors)
    ax.set_xscale("log")
    ax.set_yticks(y, labels)
    ax.set_xlabel("mass scale (kg)")
    ax.set_title("Mass scale gap for superposition tests")
    ax.invert_yaxis()
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig3_experimental_gap.png", dpi=300)


def cosmic_decoherence_order() -> None:
    q = np.linspace(0, 1, 401)
    mass = (2.0 / np.pi) * np.sin(np.pi * q / 2.0)
    overflow = q
    accessible = 1.0 - q
    inaccessible_area = overflow**2
    classicality = 1.0 - np.exp(-8.0 * inaccessible_area)

    write_csv(
        DATA_DIR / "cosmic_decoherence_order.csv",
        ["q_overflow", "mass_over_mp", "accessible_fraction", "inaccessible_area_proxy", "classicality_proxy"],
        [
            [float(qi), float(mi), float(ai_frac), float(ai), float(ci)]
            for qi, mi, ai_frac, ai, ci in zip(q, mass, accessible, inaccessible_area, classicality)
        ],
    )

    fig, ax1 = plt.subplots(figsize=(5.2, 3.4))
    ax1.plot(q, mass, color="#1f77b4", lw=2, label=r"$m(q)/m_p$")
    ax1.plot(q, accessible, color="#b22222", lw=2, label=r"accessible coherence $1-q$")
    ax1.set_xlabel("overflow filling q")
    ax1.set_ylabel("normalized scale")
    ax1.set_ylim(0, 1.05)
    ax2 = ax1.twinx()
    ax2.plot(q, classicality, color="#2ca02c", lw=2, ls="--", label="classicality proxy")
    ax2.set_ylabel("decohered classicality proxy")
    ax2.set_ylim(0, 1.05)
    lines = ax1.get_lines() + ax2.get_lines()
    labels = [line.get_label() for line in lines]
    ax1.legend(lines, labels, frameon=False, fontsize=8, loc="center right")
    ax1.set_title("DGF macrocosmic decoherence order")
    fig.tight_layout()
    fig.savefig(FIG_DIR / "fig4_cosmic_decoherence_order.png", dpi=300)


def summary_table() -> None:
    systems = [
        ("electron_alpha_c", 9.109_383_7139e-31, 9.109_383_7139e-31 * (c / 137.036) ** 2),
        ("proton_nuclear", 1.672_621_92595e-27, 10e6 * 1.602_176_634e-19),
        ("1pg_1mK_10pct", 1.0e-15, 0.1 * 1.0e-15 * (kB * 1.0e-3) ** 2),
        ("Planck_energy_scale", m_p, m_p * c**2),
    ]
    rows = []
    for name, mass, delta_v in systems:
        gamma = float(gamma_from_delta_v(delta_v))
        tau = np.inf if gamma == 0 else 1.0 / gamma
        rows.append([name, mass, delta_v, gamma, tau])
    write_csv(DATA_DIR / "dgf_estimates.csv", ["system", "mass_kg", "deltaV_J", "gamma_s^-1", "tau_s"], rows)


if __name__ == "__main__":
    mass_map()
    dephasing_scale()
    experimental_gap()
    cosmic_decoherence_order()
    summary_table()
    print(f"Wrote figures to {FIG_DIR}")
    print(f"Wrote data to {DATA_DIR}")

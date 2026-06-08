#!/usr/bin/env python3
"""
ssd_engine.py
=============
Reproduces Fig. 1 of the main text: the steady-state ergotropy phase diagram
of the Scovil--Schulz-DuBois (SSD) three-level quantum engine, and verifies
the closed-form expression Eq. (Ess) against a numerical Lindblad
steady-state diagonalization over the full 405-point parameter scan.

Physics (units hbar = k_B = 1, omega_13 = 1):
  Three levels |1>,|2>,|3> with energies E1=0, E2=omega_12, E3=omega_13.
  omega_23 = omega_13 - omega_12.
  Hot bath  H couples |1> <-> |3|  (rate gamma_H, Bose factor n_H at omega_13).
  Cold bath C couples |1> <-> |2|  (rate gamma_C, Bose factor n_C at omega_12).

  Dimensionless drives:  u = omega_12 / T_C ,  v = omega_13 / T_H.
  Closed-form steady-state ergotropy (main text Eq. Ess):
        E_ss = omega_23 * (e^{u-v} - 1) / (e^u + 1 + e^{u-v}).
  Engine/refrigerator threshold (main text Eq. threshold):
        T_H / T_C > omega_13 / omega_12.

The numerical branch builds the SSD Lindblad generator with the four jump
operators (SM Eq. S20-S21) and solves L[rho_ss] = 0 directly, then computes
the ergotropy by the standard passive-state subtraction.

Outputs:
  figures/Fig1_SSD_phase_diagram.png
  data/ssd_405_scan.csv         (one row per scanned parameter point)
  data/ssd_summary.json         (headline numbers used in the paper/caption)

Author: Zhongchang Huang
"""

import os
import json
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# QuTiP is optional and imported lazily inside ergotropy_lindblad(); importing it
# at module load is slow on some platforms and is not needed by callers that only
# use the closed-form / direct-Liouvillian helpers.

HERE = os.path.dirname(os.path.abspath(__file__))
FIGDIR = os.path.join(HERE, "..", "figures")
DATADIR = os.path.join(HERE, "..", "data")
os.makedirs(FIGDIR, exist_ok=True)
os.makedirs(DATADIR, exist_ok=True)


# ---------------------------------------------------------------------------
# Analytical closed form
# ---------------------------------------------------------------------------
def ergotropy_closed_form(omega13, omega23, TH, TC):
    """Closed-form steady-state ergotropy, main text Eq. (Ess)."""
    omega12 = omega13 - omega23
    u = omega12 / TC
    v = omega13 / TH
    num = np.exp(u - v) - 1.0
    den = np.exp(u) + 1.0 + np.exp(u - v)
    return omega23 * num / den


# ---------------------------------------------------------------------------
# Numerical Lindblad steady state
# ---------------------------------------------------------------------------
def ergotropy_value(rho, H):
    """E = Tr[rho H] - sum_k r_k^down * eps_k^up  (passive-state subtraction)."""
    r = np.sort(np.real(np.linalg.eigvalsh(rho)))[::-1]      # descending
    eps = np.sort(np.real(np.linalg.eigvalsh(H)))            # ascending
    return float(np.real(np.trace(rho @ H)) - np.sum(r * eps))


def ergotropy_lindblad(omega13, omega23, TH, TC, gammaH, gammaC):
    """
    Numerical SSD steady state via the secular Lindblad generator.
    Jump operators (SM Eqs. S20-S21):
        L_H^- = sqrt(gammaH (nH+1)) |1><3| ,  L_H^+ = sqrt(gammaH nH) |3><1|
        L_C^- = sqrt(gammaC (nC+1)) |1><2| ,  L_C^+ = sqrt(gammaC nC) |2><1|
    Returns (E_ss, rho_ss as 3x3 ndarray).
    """
    omega12 = omega13 - omega23
    # Bose occupation factors at the respective transition frequencies
    nH = 1.0 / np.expm1(omega13 / TH)
    nC = 1.0 / np.expm1(omega12 / TC)

    # Energy basis |1>,|2>,|3>  ->  indices 0,1,2
    H = np.diag([0.0, omega12, omega13]).astype(complex)

    def proj(a, b):                      # |a><b|, 1-indexed levels
        M = np.zeros((3, 3), dtype=complex)
        M[a - 1, b - 1] = 1.0
        return M

    LHm = np.sqrt(gammaH * (nH + 1.0)) * proj(1, 3)
    LHp = np.sqrt(gammaH * nH) * proj(3, 1)
    LCm = np.sqrt(gammaC * (nC + 1.0)) * proj(1, 2)
    LCp = np.sqrt(gammaC * nC) * proj(2, 1)
    Ls = [LHm, LHp, LCm, LCp]

    # Direct Liouvillian null-space solve (no external dependencies).
    d = 3
    I = np.eye(d, dtype=complex)
    Liou = -1j * (np.kron(H, I) - np.kron(I, H.T))
    for L in Ls:
        Ld = L.conj().T
        Liou += (np.kron(L, L.conj())
                 - 0.5 * np.kron(Ld @ L, I)
                 - 0.5 * np.kron(I, (Ld @ L).T))
    w, V = np.linalg.eig(Liou)
    rho_ss = V[:, np.argmin(np.abs(w))].reshape(d, d)
    rho_ss = rho_ss / np.trace(rho_ss)
    rho_ss = 0.5 * (rho_ss + rho_ss.conj().T)

    return ergotropy_value(rho_ss, H), rho_ss


# ---------------------------------------------------------------------------
# 405-point scan.
#
# Grid (9 x 9 x 5 = 405), matching the documented parameter scan:
#   T_H/T_C  in {1.5, 2, 3, 4, 5, 7, 10, 15, 20}      (9 values)
#   w23/w13  in {0.1, 0.2, ..., 0.9}                  (9 values)
#   gH/gC    in {0.1, 0.3, 1, 3, 10}                  (5 values)
# Fixed: omega13 = 1, gamma_C = 0.01.
#
# Physical ergotropy is non-negative; the closed form Eq. (Ess) returns a
# negative value below the engine/refrigerator threshold, where the true
# steady-state ergotropy is identically zero (refrigerator regime). The
# analytic-vs-numeric comparison is therefore made on max(E, 0), which is the
# physical quantity both branches must agree on.
# ---------------------------------------------------------------------------
def run_scan():
    TH_TC = np.array([1.5, 2.0, 3.0, 4.0, 5.0, 7.0, 10.0, 15.0, 20.0])  # 9
    w23_w13 = np.round(np.arange(0.1, 0.91, 0.1), 1)                    # 9
    gH_gC = np.array([0.1, 0.3, 1.0, 3.0, 10.0])                        # 5
    omega13 = 1.0
    gammaC = 0.01

    rows = []
    max_reldev = 0.0
    for r_w in w23_w13:
        omega23 = r_w * omega13
        for r_T in TH_TC:
            TC = 1.0
            TH = r_T * TC
            for r_g in gH_gC:
                gammaH = r_g * gammaC
                E_ana = ergotropy_closed_form(omega13, omega23, TH, TC)
                E_num, _ = ergotropy_lindblad(omega13, omega23, TH, TC,
                                              gammaH, gammaC)
                E_ana_phys = max(E_ana, 0.0)        # physical ergotropy >= 0
                scale = max(abs(E_ana_phys), abs(E_num), 1e-9)
                reldev = abs(E_ana_phys - E_num) / scale
                max_reldev = max(max_reldev, reldev)
                rows.append(dict(TH_TC=r_T, w23_w13=r_w, gH_gC=r_g,
                                 omega12=omega13 - omega23, omega23=omega23,
                                 E_analytic=E_ana, E_analytic_phys=E_ana_phys,
                                 E_numeric=E_num, rel_dev=reldev))
    return rows, float(max_reldev)


def main():
    rows, max_reldev = run_scan()
    n = len(rows)
    n_pos = sum(1 for r in rows if r["E_analytic"] > 1e-9)
    frac_pos = n_pos / n

    # --- write per-point CSV
    csv_path = os.path.join(DATADIR, "ssd_405_scan.csv")
    with open(csv_path, "w") as f:
        f.write("TH_TC,w23_w13,gH_gC,omega12,omega23,E_analytic,"
                "E_analytic_phys,E_numeric,rel_dev\n")
        for r in rows:
            f.write("{TH_TC:.6g},{w23_w13:.6g},{gH_gC:.6g},{omega12:.6g},"
                    "{omega23:.6g},{E_analytic:.8e},{E_analytic_phys:.8e},"
                    "{E_numeric:.8e},{rel_dev:.3e}\n".format(**r))

    # --- summary numbers used in the paper/caption
    summary = dict(
        n_points=n,
        grid="9 (T_H/T_C) x 9 (w23/w13) x 5 (gH/gC) = 405",
        fraction_positive_ergotropy=frac_pos,
        max_relative_deviation_analytic_vs_numeric=max_reldev,
        agreement_within_2pct=bool(max_reldev < 0.02),
    )
    with open(os.path.join(DATADIR, "ssd_summary.json"), "w") as f:
        json.dump(summary, f, indent=2)

    print("=" * 64)
    print("SSD 405-point scan")
    print("=" * 64)
    print(f"  points scanned                : {n}")
    print(f"  positive-ergotropy fraction   : {frac_pos*100:.1f}%")
    print(f"  max |E_ana - E_num| / |E|     : {max_reldev*100:.3f}%")
    print(f"  analytic vs numeric < 2%      : {max_reldev < 0.02}")

    # --- Fig. 1: phase diagram E_ss/omega13 over (T_H/T_C, w23/w13)
    #     averaged is unnecessary (gamma-independent in secular limit); use the
    #     gamma_H/gamma_C = 1 slice for the heat map and overlay the threshold.
    TH_TC = np.array([1.5, 2.0, 3.0, 4.0, 5.0, 7.0, 10.0, 15.0, 20.0])
    w23_w13 = np.round(np.arange(0.1, 0.91, 0.1), 1)
    Z = np.zeros((len(w23_w13), len(TH_TC)))
    for i, rw in enumerate(w23_w13):
        for j, rT in enumerate(TH_TC):
            Z[i, j] = max(ergotropy_closed_form(1.0, rw, rT, 1.0), 0.0)  # /omega13

    fig, ax = plt.subplots(figsize=(5.4, 4.0))
    im = ax.pcolormesh(TH_TC, w23_w13, Z, cmap="inferno", shading="auto")
    cbar = fig.colorbar(im, ax=ax)
    cbar.set_label(r"$\mathcal{E}_{ss}/\hbar\omega_{13}$", fontsize=12)

    # analytical engine/refrigerator boundary:  T_H/T_C = omega13/omega12 = 1/(1-r)
    rr = np.linspace(0.1, 0.9, 200)
    boundary = 1.0 / (1.0 - rr)
    m = boundary <= 20.0
    ax.plot(boundary[m], rr[m], "w--", lw=2.0,
            label=r"$T_H/T_C=\omega_{13}/\omega_{12}$")

    ax.set_xlabel(r"$T_H/T_C$", fontsize=12)
    ax.set_ylabel(r"$\omega_{23}/\omega_{13}$", fontsize=12)
    ax.set_title("SSD steady-state ergotropy phase diagram", fontsize=12)
    ax.legend(loc="lower right", fontsize=9, framealpha=0.9)
    ax.text(0.03, 0.95,
            f"{frac_pos*100:.0f}% positive\nanalytic = Lindblad\n(dev < {max(max_reldev,1e-9)*100:.0e})",
            transform=ax.transAxes, va="top", fontsize=8, color="white",
            bbox=dict(boxstyle="round", fc="black", alpha=0.55))
    fig.tight_layout()
    out = os.path.join(FIGDIR, "Fig1_SSD_phase_diagram.png")
    fig.savefig(out, dpi=300)
    fig.savefig(out.replace(".png", ".pdf"))
    print(f"  wrote {out}")
    print(f"  wrote {csv_path}")


if __name__ == "__main__":
    main()

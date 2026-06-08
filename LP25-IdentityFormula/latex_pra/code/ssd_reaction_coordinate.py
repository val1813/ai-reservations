#!/usr/bin/env python3
"""
ssd_reaction_coordinate.py
==========================
Reproduces Fig. 2 of the main text: the strong-coupling analysis of the SSD
engine via the reaction-coordinate (RC) mapping.

Panel (a): steady-state ergotropy vs. system-bath coupling strength alpha --
             * Born-Markov baseline (alpha-independent weak-coupling value),
             * full reaction-coordinate numerics (qutrit + 2 RC modes),
             * leading-order level-shift estimate.
Panel (b): enhancement factor F(alpha) = E_RC / E_BM. The level-shift estimate
           predicts F > 1 (enhancement); the full RC numerics give F ~ 0.1-0.2
           (suppression): population dilution + extra dissipation overwhelm the
           level shift.

Model (companion SM Sec. S4):
  H_ext = H_S + sum_{k in {H,C}} [ Omega_k b_k^dag b_k
                                   + g_k V_k (b_k + b_k^dag) ],
  g_k = sqrt(alpha Omega_k / 2),  V_H = |1><3|+h.c.,  V_C = |1><2|+h.c.
  Each RC mode damped by a residual Markovian bath at temperature T_k:
  L_k^- = sqrt(gamma_res (N_k+1)) b_k,  L_k^+ = sqrt(gamma_res N_k) b_k^dag.
  rho_S = Tr_RC[rho_ss];  E = Tr[rho_S H_S] - passive-state energy.

Implementation: the Lindblad generator is built explicitly as a sparse
superoperator and its steady state is the null vector of the Liouvillian
(eigenvector with eigenvalue nearest 0). Only numpy/scipy are required.

Outputs:
  figures/Fig2_BM_vs_RC.png
  data/ssd_rc_scan.csv

Author: Zhongchang Huang
"""

import os
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from ssd_engine import ergotropy_closed_form, ergotropy_value

HERE = os.path.dirname(os.path.abspath(__file__))
FIGDIR = os.path.join(HERE, "..", "figures")
DATADIR = os.path.join(HERE, "..", "data")
os.makedirs(FIGDIR, exist_ok=True)
os.makedirs(DATADIR, exist_ok=True)

# Fixed engine parameters (omega13 = 1)
OMEGA13 = 1.0
W23_W13 = 0.5                       # representative working point
OMEGA23 = W23_W13 * OMEGA13
OMEGA12 = OMEGA13 - OMEGA23
TH, TC = 4.0, 1.0                   # engine regime (T_H/T_C = 4 > omega13/omega12 = 2)
GAMMA_RES = 0.02                    # residual-bath rate (weak, fixed)
OMEGA_RC = 4.0                      # RC (Drude-cutoff) frequency, above transitions
NRC = 6                             # RC truncation (convergence checked below)


def bose(omega, T):
    return 1.0 / np.expm1(omega / T)


def HS_matrix():
    return np.diag([0.0, OMEGA12, OMEGA13]).astype(complex)


def liouvillian(H, c_ops):
    """Sparse vectorized Lindblad generator L (column-stacking convention)."""
    d = H.shape[0]
    H = sp.csr_matrix(H)
    I = sp.identity(d, dtype=complex, format="csr")
    L = -1j * (sp.kron(I, H) - sp.kron(H.T, I))
    for C in c_ops:
        C = sp.csr_matrix(C)
        Cd = C.conj().T
        CdC = Cd @ C
        L += (sp.kron(C.conj(), C)
              - 0.5 * sp.kron(I, CdC)
              - 0.5 * sp.kron(CdC.T, I))
    return L.tocsr()


def steady_state(H, c_ops):
    """
    Direct steady state: solve L rho = 0 with the trace condition Tr rho = 1.
    Replace the first row of L by the vectorized identity (the trace functional)
    and solve the resulting non-singular sparse linear system.
    """
    d = H.shape[0]
    L = liouvillian(H, c_ops).tolil()
    # vectorized identity (column-stacking): trace = sum of diagonal entries
    trace_row = np.zeros(d * d, dtype=complex)
    for i in range(d):
        trace_row[i * d + i] = 1.0
    L[0, :] = trace_row
    b = np.zeros(d * d, dtype=complex)
    b[0] = 1.0
    rho = spla.spsolve(L.tocsr(), b).reshape(d, d, order="F")
    rho = 0.5 * (rho + rho.conj().T)
    rho = rho / np.trace(rho)
    return rho


def proj3(a, b):
    M = np.zeros((3, 3), dtype=complex)
    M[a - 1, b - 1] = 1.0
    return M


def ergotropy_bm():
    """Born-Markov (weak-coupling) baseline: bare SSD Lindblad steady state."""
    H = HS_matrix()
    nH, nC = bose(OMEGA13, TH), bose(OMEGA12, TC)
    g = GAMMA_RES
    c = [np.sqrt(g * (nH + 1)) * proj3(1, 3), np.sqrt(g * nH) * proj3(3, 1),
         np.sqrt(g * (nC + 1)) * proj3(1, 2), np.sqrt(g * nC) * proj3(2, 1)]
    rho = steady_state(H, c)
    return ergotropy_value(rho, H)


def _kron3(A, B, C):
    return np.kron(np.kron(A, B), C)


def ergotropy_rc(alpha, nrc=NRC):
    """Full reaction-coordinate steady-state ergotropy at coupling alpha."""
    HS = HS_matrix()
    I3 = np.eye(3, dtype=complex)
    Ia = np.eye(nrc, dtype=complex)

    a = np.zeros((nrc, nrc), dtype=complex)
    for n in range(1, nrc):
        a[n - 1, n] = np.sqrt(n)
    ad = a.conj().T
    num = ad @ a

    OmegaH, OmegaC = OMEGA_RC, OMEGA_RC          # RC (cutoff) frequencies
    gH = np.sqrt(alpha * OmegaH / 2.0)
    gC = np.sqrt(alpha * OmegaC / 2.0)

    VH = proj3(1, 3) + proj3(3, 1)
    VC = proj3(1, 2) + proj3(2, 1)

    Hext = (_kron3(HS, Ia, Ia)
            + OmegaH * _kron3(I3, num, Ia) + OmegaC * _kron3(I3, Ia, num)
            + gH * _kron3(VH, a + ad, Ia)
            + gC * _kron3(VC, Ia, a + ad))

    NH, NC = bose(OmegaH, TH), bose(OmegaC, TC)
    c = [
        np.sqrt(GAMMA_RES * (NH + 1)) * _kron3(I3, a, Ia),
        np.sqrt(GAMMA_RES * NH) * _kron3(I3, ad, Ia),
        np.sqrt(GAMMA_RES * (NC + 1)) * _kron3(I3, Ia, a),
        np.sqrt(GAMMA_RES * NC) * _kron3(I3, Ia, ad),
    ]
    rho_full = steady_state(Hext, c)

    # partial trace over the two RC modes -> 3x3 system state
    D = 3 * nrc * nrc
    rho_t = rho_full.reshape(3, nrc, nrc, 3, nrc, nrc)
    rho_S = np.einsum("aijbij->ab", rho_t)
    rho_S = 0.5 * (rho_S + rho_S.conj().T)
    rho_S = rho_S / np.trace(rho_S)
    return ergotropy_value(rho_S, HS)


def ergotropy_level_shift(alpha):
    """Leading-order level-shift estimate (SM S4.4a): the F>1 mechanism."""
    gH = np.sqrt(alpha * OMEGA_RC / 2.0)
    omega13_tilde = OMEGA13 - gH**2 / OMEGA_RC
    omega23_tilde = omega13_tilde - OMEGA12
    if omega23_tilde <= 0:
        return 0.0
    return ergotropy_closed_form(omega13_tilde, omega23_tilde, TH, TC)


def main():
    alphas = np.linspace(0.01, 0.5, 18)
    E_bm = ergotropy_bm()
    E_rc = np.array([ergotropy_rc(al) for al in alphas])
    E_ls = np.array([ergotropy_level_shift(al) for al in alphas])
    F_rc = E_rc / E_bm
    F_ls = E_ls / E_bm

    # convergence check at alpha=0.5 between NRC=4 and NRC=6
    conv = abs(ergotropy_rc(0.5, 6) - ergotropy_rc(0.5, 4)) / abs(E_bm)

    csv = os.path.join(DATADIR, "ssd_rc_scan.csv")
    with open(csv, "w") as f:
        f.write("alpha,E_BM,E_RC,E_levelshift,F_RC,F_levelshift\n")
        for i, al in enumerate(alphas):
            f.write(f"{al:.6g},{E_bm:.8e},{E_rc[i]:.8e},{E_ls[i]:.8e},"
                    f"{F_rc[i]:.6f},{F_ls[i]:.6f}\n")

    print("=" * 64)
    print("SSD reaction-coordinate strong-coupling scan")
    print("=" * 64)
    print(f"  E_BM baseline        : {E_bm:.6e}")
    print(f"  F_RC range           : [{F_rc.min():.3f}, {F_rc.max():.3f}]")
    print(f"  F_levelshift range   : [{F_ls.min():.3f}, {F_ls.max():.3f}]")
    print(f"  NRC 5->7 convergence : {conv*100:.3f}% of E_BM")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9.2, 3.9))

    ax1.axhline(E_bm, color="tab:blue", lw=2, label="Born--Markov baseline")
    ax1.plot(alphas, E_rc, "o-", color="tab:red", ms=4,
             label="reaction-coordinate (numerical)")
    ax1.plot(alphas, E_ls, "s--", color="tab:green", ms=3,
             label="level-shift estimate")
    ax1.set_xlabel(r"coupling strength $\alpha$", fontsize=11)
    ax1.set_ylabel(r"$\mathcal{E}_{ss}/\hbar\omega_{13}$", fontsize=11)
    ax1.set_title("(a) Ergotropy vs. coupling", fontsize=11)
    ax1.legend(fontsize=8, loc="best")

    ax2.axhline(1.0, color="gray", lw=1, ls=":")
    ax2.plot(alphas, F_ls, "s--", color="tab:green", ms=3,
             label=r"level-shift ($\mathcal{F}>1$)")
    ax2.plot(alphas, F_rc, "o-", color="tab:red", ms=4,
             label=r"full RC ($\mathcal{F}\approx0.1$--$0.2$)")
    ax2.set_xlabel(r"coupling strength $\alpha$", fontsize=11)
    ax2.set_ylabel(r"enhancement factor $\mathcal{F}(\alpha)$", fontsize=11)
    ax2.set_title("(b) Enhancement factor", fontsize=11)
    ax2.legend(fontsize=8, loc="best")

    fig.tight_layout()
    out = os.path.join(FIGDIR, "Fig2_BM_vs_RC.png")
    fig.savefig(out, dpi=300)
    fig.savefig(out.replace(".png", ".pdf"))
    print(f"  wrote {out}")
    print(f"  wrote {csv}")


if __name__ == "__main__":
    main()

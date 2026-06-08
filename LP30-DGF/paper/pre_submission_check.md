# Pre-Submission Check: Archive-Decompression Revision

Date: 2026-06-05

## What Changed

The theory now separates:

- \(q=N_{\rm accessible}/N_{\rm total}\): flowing, accessible coherence.
- \(A=1-q\): archived, locked information.

This fixes the contradiction:

- Decoherence means \(q\to0\), \(A\to1\).
- Mass follows \(A\), not \(q\).
- Ordinary decoherence does not imply rest-mass decrease.

## Added Structure

1. Microscopic cell-access definition of \(q\).
2. Fokker-Planck archival drift closed by total entropy:
   \(\mu(q_S)=-\Gamma\partial_{A_S}S_{\rm tot}\).
3. Receiver-capacity gradient as the source of direction, with sender cost separated from receiver record multiplicity.
4. Information-geometric endpoint plus maximum-entropy archive coordinate:
   \(\theta(A)=\pi A+O(N^{-1})\).
5. Euler residual mass \(m(A)=2m_p\sin(\pi A/2)/\pi\), now explicitly limited to a single DGF archival branch.
6. Composite mass branch decomposition:
   \(M_S=\sum_b m_b(A_b)+(E_{\rm bind}+E_{\rm field})/c^2\), with \(m(A_{\rm comp})\neq M_S\).
7. Receiver spectral density \(J_{\rm recv}(\omega)\) with photon/graviton examples and the filtered Markov limit \(D_\beta^{\rm eff}\).
8. Archive-decompression conjecture \(q\to0\to q\to1\) at Planck critical density.

## Files Updated

- `dgf_paper_draft.md`
- `dgf_supplemental.md`
- `dgf_prl.tex`
- `cover_letter_prl.md`
- `scripts/generate_dgf_figures.py`
- `figures/fig4_cosmic_decoherence_order.png`
- `data/cosmic_decoherence_order.csv`
- `D:\桌面\dgf_hypothesis_structure.svg`

## Remaining Proof Burdens

1. Define measurable surrogate for \(a_c\).
2. Derive \(S_{\rm recv}(A)\) beyond the minimal photon/graviton sketches.
3. Compute realistic \(J_{\rm recv}(\omega)\), cutoff functions \(f(\omega/\omega_c)\), and filters \(F_\tau(\omega)\) for proposed experiments.
4. Define the branch partition threshold \(\epsilon\) operationally.
5. Derive Planck critical decompression condition \(\rho_A\sim\rho_p\).
6. Add recent experimental references and BibTeX.

## Inspector Fixes Added After DeepSeek Review

- Fixed angle derivation: Bures/FS no longer claimed to be linear; it only fixes the endpoint diameter.
- Fixed drift derivation: drift now follows \(\partial_A S_{\rm tot}>0\), not an unexplained switch from sender to receiver entropy.
- Fixed receiver kernel: added \(\chi_{ab}(t)\) spectral integral and \(D_\beta^{\rm eff}\) filtered Markov limit.
- Fixed mass endpoint: \(2m_p/\pi\) is a single-branch closure endpoint, not a total composite mass cap.

## Malicious Reviewer Fixes Added

- Added operational \(q\) definition from coarse-grained density-matrix visibility \(a_{c,\ell}\).
- Added Kramers-Moyal derivation from \(W_+/W_-=\exp(\Delta S_{\rm tot}/k_B)\).
- Added finite-sector maximum-entropy coordinate theorem for \(\theta_j=\pi j/(N-1)\).
- Added coherence graph \(G_{ij}=e^{-\chi_{ij}}\) and fixed closure threshold \(\epsilon_\ast=e^{-1}\).
- Added spatial-path imprint \(\Delta\Phi_{\rm recv}[x_a,x_b]\) so spatial cats with equal momentum moments still decohere.
- Added Planck-local matching condition \(\Lambda^2D_\beta^{\rm eff}/\hbar^2=t_pl_p^4/\hbar^6\).
- Added archive density \(\rho_A=V^{-1}\sum_bA_bI_p\) and reset energy conservation.
- Replaced vague proof-burden ending with three concrete predictions.

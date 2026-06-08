# Pre-Submission Check: Four-Hard-Gap Repair

Date: 2026-06-05  
Target journal: Physical Review Letters  
Strategy: **strong claim retained; four logical gaps repaired by definitions and dynamics**

## 1. Hard Gap 1: Direction of Information Flow

Problem:

- Previous Axiom 4 gave only zero-mean fluctuation.
- White noise has no arrow of time and cannot explain one-way overflow.

Repair:

- Added Fokker-Planck equation:
  \[
  \partial_tP=-\partial_q(vP)+\partial_q^2(DP)
  \]
- Added entropy-gradient drift:
  \[
  v(q)=\Gamma(q)\partial_qS_{\rm recv}(q)>0
  \]
- Planck noise now supplies diffusion \(D(q)\), not direction.

Files:

- `dgf_paper_draft.md`, Sections III and IX
- `dgf_supplemental.md`, S3-S4

## 2. Hard Gap 2: \(q\) and Mass Circularity

Problem:

- Previous \(q\) could be read as a mass reparameterization.

Repair:

- Defined \(q\) microscopically:
  \[
  q_S=1-\frac{1}{N_S}\sum_{c\in\mathcal C_S}a_c
  \]
- \(a_c\) is local branch-recombination visibility/access weight.
- Mass now follows from \(q\); \(q\) is not inferred from mass.

Files:

- `dgf_paper_draft.md`, Section II
- `dgf_supplemental.md`, S1-S2

## 3. Hard Gap 3: Projection Angle

Problem:

- Previous \(\theta(q)\) relied on Wick-rotation analogy.

Repair:

- Added two-sector information state:
  \[
  |\chi\rangle=\sqrt{1-q}|L\rangle+\sqrt q|O\rangle
  \]
- \(\theta(q)=\pi q\) now follows from normalized arc measure of inaccessible spatial interference on the information half-circle.

Files:

- `dgf_paper_draft.md`, Section IV
- `dgf_supplemental.md`, S5

## 4. Hard Gap 4: Receiver Missing from Kernel

Problem:

- Previous \(p^4/3m\) kernel did not contain low-mass receiver degrees of freedom.
- \(m\to0\) receiver interpretation looked divergent.

Repair:

- Added receiver-mode coupling:
  \[
  H_{\rm int}=\Lambda(q)V_S\otimes\sum_\lambda g_\lambda(b_\lambda+b_\lambda^\dagger)
  \]
- Receiver modes enter through spectral density \(J_{\rm recv}(\omega)\).
- \(V_S=p^4/3m_S\) belongs to the emitting system, not to the receiver.
- Local Markovian limit reduces to the GUP kernel.

Files:

- `dgf_paper_draft.md`, Section VI
- `dgf_supplemental.md`, S7-S8

## 5. Current Outputs

Generated:

- `dgf_paper_draft.md`
- `dgf_supplemental.md`
- `dgf_prl.tex`
- `dgf_prl.pdf`
- `cover_letter_prl.md`
- `figures/fig1_mass_map.png`
- `figures/fig2_dephasing_scale.png`
- `figures/fig3_experimental_gap.png`
- `figures/fig4_cosmic_decoherence_order.png`
- `data/cosmic_decoherence_order.csv`

## 8. Post-Audit Fixes (2026-06-05, Session 2 — GPT + 对话3 Integration)

After comprehensive 4-agent adversarial audit, the following fixes were applied:

### Fatal fixes (theory self-consistency):
1. **Mass definition unified**: Distinguish $m_{\rm Euler}(q)$ (Euler residual, varies with q) from $m_{\rm rest}$ (rest mass from total information, constant). Resolves 3-file contradiction (paper §IX vs supp S10.3 vs derivations). Files: paper §V, §IX; supp S10.3; LaTeX.
2. **Second law claim recast**: Removed false claim that $\partial_q S_{\rm total}>0$ for all q. Replaced with information-theoretic flow: drift set by receiver multiplicity gradient, not thermodynamic entropy. Files: supp S3.3; paper §III; LaTeX.
3. **Boundary condition fixed**: Acknowledged reflecting boundaries are effective for $0<q<1$; $q=1$ is absorbing-emitting (archive-decompress). Files: supp S3.3; paper §III; LaTeX.
4. **Composite rule vs per-branch clarified**: Multiplicative rule applies within coherent subsystems; decohered branches' rest masses add linearly. Files: paper §II.

### Severe fixes (mathematical errors):
5. **$\theta=\pi q$ derivation corrected**: Removed incorrect arc-length doubling. Replaced with trace-distance normalization $\theta=(\pi/2)\|\rho-\rho_0\|_1=\pi q$ (exact, no $N\to\infty$ needed). Files: supp S5.2-S5.3.
6. **Photon $J_{\rm recv}$ dimensions fixed**: Added $\hbar$ factor, used standard dipole notation $|\mathbf{d}|^2/(6\pi^2\epsilon_0\hbar c^3)$. Files: supp S7.2.
7. **Graviton $J_{\rm recv}$ scaling fixed**: Changed $\omega^3\to\omega^5$ for quadrupole coupling. Files: supp S7.3.
8. **$D_{\rm eff}$ vs $J_{\rm recv}$ clarified**: $D_{\rm eff}=t_pl_p^4/\hbar^4$ is dimensional-analysis parameter, not Markovian limit of $J_{\rm recv}$. Files: supp S7.4; paper §VI; LaTeX.
9. **Spontaneous emission analogy downgraded**: Marked as heuristic (density of states vs log-derivative are different mathematical objects). Files: supp S3.3; paper §III; LaTeX.

### Files updated this session:
- `dgf_paper_draft.md` — §§II, III, V, VI, IX
- `dgf_supplemental.md` — §§S3.3, S5.2-S5.3, S6.1, S7.2-S7.5, S10.3
- `dgf_prl.tex` — synchronized all changes, compiles clean (4 pages)
- `dgf_derivations.md` — working notes (not synced, contains pre-fix material)
- `pre_submission_check.md` — this section
- `cover_letter_prl.md` — minor update

### Remaining known limitations:
1. $D_{\rm eff}$ is phenomenological; a full UV completion would compute it from $J_{\rm recv}$ explicitly.
2. $v(q)\propto 1/q$ diverges at $q=0$; regularization needed for quantum limit.
3. $m_{\max}=14\mu\text{g}$ is far above current experimental coherent-mass reach; direct falsification awaits technology.
4. No operational protocol for independently measuring $a_c$ (cell access weights).
5. The archive-decompress conjecture (S11) remains speculative.

1. Give a concrete experimental protocol for measuring \(a_c\) or an experimentally coarse-grained surrogate.
2. Derive \(S_{\rm recv}(q)\) for specific receiver sectors, e.g. photons, phonons, gravitons.
3. Justify the information half-circle beyond the two-sector minimal model.
4. Compute \(J_{\rm recv}(\omega)\) for realistic environments instead of using only the local Markovian limit.
5. Add recent experimental references and verified BibTeX.

## 7. Compile Status

To be recompiled after this report:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error dgf_prl.tex
pdflatex -interaction=nonstopmode -halt-on-error dgf_prl.tex
```

Directory:

`D:\Claude\ai-reservations\LP30-DGF\paper`

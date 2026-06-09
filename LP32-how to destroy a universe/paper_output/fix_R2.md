# R2 Fix Report

## New MAJOR Fixes

### NEW-M1 ($C_F$ normalization): FIXED
- Added justification: $C_F$ is initial-condition property, bound evaluable BEFORE dynamics
- Framed as feature: model-independent, avoids gate-sequence details
- $N_F \leq C_F$ → $\mathcal{R}$ is conservative lower bound on $N_{\rm back}/N_F$

### NEW-M2 ($N_{\rm back}$ measurement): FIXED
- Added §III.E "Measuring $N_{\rm back}$" with three strategies:
  (a) Mid-circuit measurement with post-selection
  (b) Ancilla-based weak measurement
  (c) Logical counting (simulation)
- Strategy (a) is immediately realizable on superconducting hardware

### NEW-M3 (expectation vs deterministic): FIXED
- Proof rewritten: two interpretations clearly separated
  - Deterministic: $N_{\rm back} \leq n_0$ (per-run, conditional on measured $n_0$)
  - Probabilistic: $\langle N_{\rm back}\rangle \leq N_S q_S$ (ensemble, using $q_S$)
- Hoeffding bound referenced for finite-$N_S$ tail

### M1-STILL (collision model computation): FIXED
- Monte Carlo simulation: $N_S=N_E=3$, all-to-all, $k_{\rm max}=30$, 2000 trials
- Numerical results: $\mathcal{R}$ approaches bound to 96-99% without violating
- Figure 2 added: (a) $N_{\rm back}(k)$ vs bound, (b) $\mathcal{R}/(q_S/q_E)$ normalization

### NEW-MINOR Fixes
- MINOR-1 (T1 concurrent): SM now notes sequential treatment is conservative
- MINOR-2 (pointer basis): Main text now acknowledges prior $H_{\rm int}$ characterization needed
- MINOR-3 (placeholders): All placeholder text removed; actual figures present

## Files Modified
- paper_output/final_paper/main.tex (C_F justification + N_back measurement + proof clarification + collision results + Figure 2)
- paper_output/final_paper/figures/fig2_collision.pdf (new)
- paper_output/figures/gen_fig2_collision.py (Monte Carlo script)

## R2→R3 Status
FATAL: 0 (cumulative)
MAJOR: All addressed → R3 should focus on residual narrative quality + edge cases

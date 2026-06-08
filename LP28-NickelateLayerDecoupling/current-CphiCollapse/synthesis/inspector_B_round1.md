# INSPECTOR Report: B Round 1

Project: LP28-NickelateLayerDecoupling / LP28-CphiCollapse  
Agent: B  
Round: 1  
Inspector stance: independent check of B output only; A output not inspected.

## Verdict

WARNING: INSPECTOR warning, not full pass.

B Round 1 is directionally useful and mostly clean on output leakage: it correctly attacks `C_phi` as an input-side latent variable and explicitly forbids use of `Tc`, zero resistance, Meissner response, critical current, gap opening, and other superconducting outputs. However, the formal collapse claim is overstrong. The sigma-algebra / conditional mutual information argument does not yet prove `C_phi` is baseline-measurable, and the Kubo reduction is currently a plausible physical heuristic rather than a no-go theorem.

No fatal dimensional error was found, but the main transport formula is schematic and should be labeled proportional / model-dependent, not used as a dimensionally complete equality.

## Mechanical Check

`validation/` directory not present in `current-CphiCollapse`; `validate.py` unavailable. Manual Q1-Q5 inspection performed.

## Q1 Dimensions

Formula checked:

`sigma_c(0) ~ e^2 sum_k t_perp_eff(k)^2 A(k,0)^2 tau_k`

Status: WARNING - schematic only.

Issue: as written, the expression omits conventional normalization factors and constants such as volume / lattice factors and powers of `hbar`; the dimension of `A(k,0)` also depends on convention. This is acceptable as a scaling relation, but not as a dimensionally complete Kubo formula.

Required next-round fix: rewrite as `sigma_c(0) proportional to ...` or provide the full Kubo expression with units/conventions.

Information-theoretic expressions:

`I(C_phi; Z | B)=0` is dimensionless and syntactically valid.

## Q2 Direction / Limits

Direction is internally consistent:

- Increasing baseline completeness should reduce any residual independent `C_phi`.
- Matching `W_D,c`, `gamma_c`, oxygen/disorder, strain/interface, pressure history, and `dz2`/self-doping should make `Delta C_phi | Delta B` vanish under B's hypothesis.
- Apparent reversals are predicted to disappear after adding missing sample-quality variables.

No sign reversal or numerator/denominator inversion was found.

Limit checks:

- In the complete-baseline limit, B predicts collapse.
- In the missing-confounder limit, B predicts apparent residuals.
- In the output-forbidden limit, B treats phase language as interpretation of normal-state channels.

These directions are coherent.

## Q3 Circularity / Output Leakage

Output leakage: PASS - mostly clean.

B explicitly excludes superconducting outputs in the falsifier and controls. This is a strength.

Circularity risk: WARNING - present.

The statement "`C_phi = f(X_pre)`, `X_pre = g(B, eta)`, therefore collapse" is not enough. If `eta` contains reproducible non-baseline structure, then `C_phi` need not be `B`-measurable. True `B`-measurability requires `C_phi = h(B)` up to measurement noise, or requires assumptions that `eta` is independent noise irrelevant to `Z`.

Required next-round fix: explicitly classify `eta` as either measurement noise, hidden confounder to be added into `B`, or a possible independent residual. The no-go only holds after this classification.

## Q4 Order-of-Magnitude / Claim Scale

No extreme numerical magnitude claims were made. No 10^N order mismatch detected.

Weakness: B provides qualitative confidence values and qualitative predictions, but no numeric landing estimate, no sample-size condition, no error tolerance, and no minimal detectable residual bound.

## Q5 Algebra / No-Go Logic

Main algebraic gap:

B defines collapse as `C_phi` being `B`-measurable, but the provided construction gives:

`X_pre = g(B, eta)`  
`C_phi = f(X_pre)`

This implies `C_phi = f(g(B, eta))`, not necessarily `C_phi = h(B)`.

Therefore:

`I(C_phi; Z | B)=0`

does not follow unless one additionally assumes:

1. `eta` is pure measurement noise independent of `Z` conditional on `B`; or
2. any structured component of `eta` is itself a missing baseline and must be absorbed into `B`; or
3. the admissible class of `C_phi` estimators is restricted to functions invariant to `eta`.

Without one of these assumptions, the theorem is only an empirical identifiability warning, not a mathematical collapse theorem.

Kubo / Golden-rule collapse:

The claim that normal-state probes reduce to `t_perp`, spectral weights, and lifetimes is physically plausible at scaling level, but overclaimed as a universal no-go. A real Kubo expression can include k-dependence, matrix elements, self-energy structure, vertex corrections, multiband coherence factors, inhomogeneity, and probe-specific windows. B may still argue these belong in `B`, but must state that as a closure assumption rather than derive it from the schematic formula alone.

## Q6 Claim Inflation

Overclaimed:

- "Every lab-feasible pre-output `C_phi` is built from observables already used to diagnose interlayer coherence or sample quality."
- "There is no independent phase-bus object left after `t_perp`, `A`, `tau`, `dz2`/self-doping, and disorder are fixed."
- "`I(C_phi; Z | B)=0` for any later readiness target `Z`."

Safer version:

B has a strong empirical-collapse hypothesis: under current nickelate sample counts and confounded synthesis/pressure conditions, no independent `C_phi` residual is identifiable unless a baseline-matched intervention produces a reproducible pre-output rank reversal.

## Q6.4 Alternative Explanations

B itself is an alternative-explanation attack. It identifies simpler alternatives: oxygen disorder, topotactic defects, dephasing, strain/interface state, pressure history, and `dz2`/self-doping. Pass for this role.

## Q6.5 Landing Strength

WARNING: Landing is too weak.

B gives a falsifier design in words but no concrete landing target:

- no specified material pair or pressure series;
- no numerical matching tolerances;
- no measurement error model;
- no required residual threshold for `C_phi`;
- no minimal experiment/data table that could decide B against A.

This does not invalidate the round, but it prevents the result from being a settled no-go.

## Bottom Line

B Round 1 should continue, but PI should not treat it as a proven collapse theorem. It is currently a strong parsimonious-identifiability argument plus a useful falsifier template. Round 2 must separate:

1. mathematical collapse under explicit closure assumptions;
2. empirical non-identifiability under realistic nickelate datasets;
3. experimental falsifier design.

--- Feed To Next Round ---

Blocking fixes:

None.

Warning-level fixes:

1. Sigma-algebra gap: `X_pre=g(B,eta)` and `C_phi=f(X_pre)` do not imply `C_phi` is `B`-measurable. Round 2 must either prove `C_phi=h(B)`, classify `eta`, or downgrade to empirical non-identifiability.
2. Conditional mutual information overclaim: `I(C_phi;Z|B)=0` needs extra assumptions about `eta`, hidden confounders, and the target `Z`. State these assumptions explicitly.
3. Kubo collapse overclaim: the formula is schematic. Use proportional language or provide a full Kubo expression; account for matrix elements, vertex/self-energy effects, multiband terms, and probe windows.
4. Landing weakness: add one concrete falsifier/confirmation design with a named material class, baseline vector, matching tolerances, error bars, and a residual threshold.
5. Claim scope: replace universal "every lab-feasible `C_phi` collapses" with "under the stated normal-state linear-response closure and current nickelate sampling constraints, independent `C_phi` is not identifiable."

---

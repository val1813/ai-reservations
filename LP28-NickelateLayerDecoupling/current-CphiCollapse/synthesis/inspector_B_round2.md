# INSPECTOR Report: B Round 2

Project: LP28-NickelateLayerDecoupling / LP28-CphiCollapse  
Agent: B  
Round: 2  
Inspector stance: independent check of B Round 2 only; A output not inspected.

## Verdict

WARNING: INSPECTOR warning, not blocking.

B Round 2 repairs the main Round 1 overclaim by explicitly downgrading universal no-go language to a conditional kernel-closure result plus empirical non-identifiability. The eta decomposition is logically cleaner, output leakage is mostly controlled, and the landing design now has concrete sample counts, tolerances, error model, and pass/fail thresholds.

Remaining risk: the formal `B_plus` closure is close to tautological because `B_plus` includes `M_even/odd`, `Sigma_even/odd`, and `Gamma_vertex_even/odd`, i.e. the same probe-kernel structure that generates `chi_even`, `chi_odd`, and therefore `P_oe`. This is acceptable only as an explicit closure assumption, not as an experimentally decisive no-go. Round 3 must define a non-tautological, experimentally measured `B_min` and separate it from the formal omniscient `B_plus`.

## Mechanical Check

`validation/` directory is not present in `current-CphiCollapse`; `validate.py` unavailable. Manual Q1-Q5 inspection performed.

## Q1 Dimensions

Formulae checked:

`eta = U_miss + epsilon_meas + R_oe`

Status: PASS if `eta` is dimensionless or normalized in the same units as `P_oe`. B should state the normalization explicitly. All three additive terms must live in the same eta/P_oe residual scale.

`P_oe = (chi_odd - chi_even) / (chi_odd + chi_even)`

Status: PASS. Dimensionless ratio if `chi_odd` and `chi_even` are the same susceptibility component measured in the same convention. Requires nonzero denominator and a denominator floor.

`chi_alpha(q,omega) = sum_k |M_alpha(k,q)|^2 [f(E_k)-f(E_{k+q})] / [omega + E_k - E_{k+q} + i Gamma_alpha(k,q,omega)] + vertex/self-energy corrections`

Status: WARNING - explicitly schematic only. As written, `omega` is used in an energy denominator without showing `hbar`, the units of `M_alpha`, the k-sum normalization, and susceptibility prefactors are unspecified. B labels it schematic and not a dimensionally complete conductivity/susceptibility formula, which is acceptable for qualitative closure logic.

`I(C_phi;Z_pre|B_plus)=0`

Status: PASS dimensionally. Mutual information is dimensionless.

## Q2 Direction / Limits

Direction is internally consistent:

- Complete kernel closure plus conditionally independent measurement noise implies `C_phi=h(B_plus,epsilon_meas)` and no independent conditional information about a pre-output `Z_pre`.
- Missing oxygen/strain/orbital/dephasing/pressure structure can generate apparent `P_oe` residuals.
- A sign-stable residual after matched `B_plus` baselines falsifies B's practical collapse.
- If `chi_odd + chi_even -> 0`, `P_oe` becomes ill-conditioned; B correctly flags exclusion or regularization.

No sign reversal, numerator/denominator inversion, or direction mismatch found.

## Q3 Circularity / Output Leakage

Output leakage: PASS with one caveat.

B explicitly excludes `Tc`, zero resistance, Meissner response, critical current, gap opening, and superconducting outputs from `Z_pre`, selection, ranking, fitting, and stopping. This is clean.

Caveat: `Z_pre` remains underspecified. If a "readiness label" is assigned using hidden or historical superconducting outcomes, output leakage re-enters. Round 3 must define allowed `Z_pre` labels operationally and forbid labels backfilled from later superconducting outcomes.

Circularity: WARNING.

`B_plus` includes the kernel terms that generate the target contrast itself. In the formal closure, `chi_alpha=K_alpha(B_plus)` and `P_oe=H(B_plus)` are true because `B_plus` contains `M_even/odd`, `Sigma_even/odd`, and `Gamma_vertex_even/odd`. That is not a discovery unless those quantities are measured independently before `P_oe` extraction and are not fitted using the same odd/even contrast.

Required next-round fix: split:

1. `B_formal`: full response-kernel state, allowed only for the conditional theorem.
2. `B_min`: experimentally accessible pre-registered baseline measured independently of `P_oe`, used for the empirical nickelate test.

## Q4 Order-of-Magnitude / Scale

B adds concrete landing thresholds:

- 12 specimens, 6 matched pairs across two batches.
- Pair pass: `|Delta r_pair| <= 2 sigma_res` in at least 5/6 pairs.
- B falsification: same-sign `|Delta r_pair| >= 3 sigma_res` in at least 4/6 pairs, pooled residual shift `>= 0.10`, and cross-validated partial `R2 >= 0.10` with 95 percent bootstrap CI excluding 0.

Status: WARNING but improved.

The thresholds are usable as a pilot decision rule, but `n=12` is thin for a hierarchical errors-in-variables model with many baseline dimensions. The claimed bootstrap CI and between-batch random effect will be fragile unless `B_min` is low-dimensional or calibrated using external/replicate data.

## Q5 Algebra / No-Go Logic

Round 1's invalid implication `C_phi=f(g(B,eta)) => C_phi=h(B)` is mostly fixed. Round 2 now states:

`eta = U_miss + epsilon_meas + R_oe`

and conditions the zero mutual-information result on:

- `U_miss` being added into `B_plus`;
- `epsilon_meas` being conditionally independent of `Z_pre`;
- `R_oe` being absent or failing the residual test;
- `Z_pre` being pre-output and not used to construct `C_phi`.

This is algebraically coherent as a conditional theorem.

No-go logic status: WARNING, not theorem-grade for experiment.

The closure is acceptable as "if the full normal-state kernel state is known, `P_oe` is not independent of that state." It is not acceptable as "nickelate experiments have already annihilated eta" unless the practical `B_min` is measured with enough accuracy and used out-of-sample.

## Q6 Claim Inflation

Round 2 substantially reduces claim inflation:

- It explicitly says universal no-go cannot be honestly proven.
- It downgrades to empirical non-identifiability under present nickelate constraints.
- It states that a sign-stable residual after matching falsifies B.

Remaining inflated/fragile phrasing:

- "Under expanded normal-state kernel closure, `P_oe` is baseline-generated rather than independent" is true but nearly definitional with the current `B_plus`.
- "Any `C_phi=f(P_oe,other input probes)` is `B_plus`-measurable" is only valid if all other probes are also generated by the same closed baseline and no unmodeled residual is used in constructing `C_phi`.

Safer wording: formal closure shows non-independence relative to an omniscient kernel baseline; the empirical claim is only that a realistic measured `B_min` may explain `P_oe` within error.

## Q6.3 Claim Shrinkage

PASS. B shrinks Round 1's universal collapse/no-go into:

1. conditional formal closure under normal-state response assumptions;
2. empirical non-identifiability under current nickelate constraints;
3. matched-pair residual test as falsifier.

This shrinkage should be reflected in the North Star scoring; it is a fidelity improvement but a scope downgrade.

## Q6.4 Alternative Explanations

PASS. B explicitly centers simpler alternatives: missing oxygen/apical structure, layer asymmetry, strain, dz2/RE5d/self-doping, pressure path, dephasing/disorder, and probe matrix-element calibration. These are concrete enough to enter a checkpoint register.

## Q6.5 Landing Design

PASS with warnings.

Strengths:

- Named material class: La3Ni2O7-delta / related bilayer nickelates.
- No output variables in selection/ranking/fitting/stopping.
- Concrete baseline vector and matching tolerances.
- Hierarchical error model and residual thresholds.
- Negative controls included.

Warnings:

1. No denominator floor is specified for `chi_odd + chi_even` or normalized `P_oe`; Round 3 must add it.
2. `E[P_oe|B_plus]` is high-dimensional relative to 12 specimens; this invites overfitting and post-hoc absorption of the target.
3. The pass/fail rules leave a gray zone, e.g. 3/6 same-sign residuals or disagreement between pair statistic and partial `R2`. Round 3 should define "inconclusive/repeat" handling.
4. The accepted probe list is still flexible; Round 3 should pre-register exact probe windows and extraction rules.

## Bottom Line

B Round 2 can proceed. It is no longer claiming a universal no-go, and its conditional mutual-information logic is coherent under explicit assumptions. The main issue to feed forward is tautology control: do not let `B_plus` include fitted versions of the target-generating odd/even kernel and then call the residual collapse empirical.

--- Feed To Next Round ---

Blocking fixes:

None.

Warning-level fixes:

1. Tautological `B_plus`: split `B_formal` from measured `B_min`. `B_formal` may contain full kernel closure; `B_min` must be independently measured, pre-registered, and not fitted from the same `P_oe` contrast.
2. Kubo closure: keep it explicitly conditional and schematic. Do not present it as a dimensionally complete susceptibility theorem unless units, prefactors, k-normalization, and probe conventions are supplied.
3. Denominator control: specify a numerical denominator floor or exclusion rule for `chi_odd + chi_even` before computing `P_oe`.
4. Landing thresholds: define gray-zone outcomes and require cross-fitting/external calibration for `E[P_oe|B_min]` because 12 specimens cannot support a high-dimensional `B_plus` regression.
5. Output leakage guard: operationally define allowed `Z_pre` readiness labels and forbid labels derived from later or historical superconducting outcomes.
6. Eta scale: state whether eta is dimensionless, normalized to `P_oe`, or measured in another residual scale; ensure `U_miss`, `epsilon_meas`, and `R_oe` share that scale.

---

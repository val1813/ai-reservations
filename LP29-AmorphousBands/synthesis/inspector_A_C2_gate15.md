# INSPECTOR Report: A C2 Gate 1.5 Deepening Supplement

Input:
- `D:\Claude\ai-reservations\LP29-AmorphousBands\current\A\C2_deepening_supplement_gate15.json`

Protocol:
- `D:\Claude\ai-reservations\ai\INSPECTOR.md`

Mechanical validation:
- No `validation/` directory was found under `D:\Claude\ai-reservations\LP29-AmorphousBands`, so `validate.py` is unavailable.
- This inspection uses manual Q1-Q6 checks.

## Verdict

INSPECTOR result: pass with one boundary warning.

- Blockers: 0
- Warnings: 1

The Gate 1.5 supplement is acceptable as an A-side mechanical-field/deepening summary. It contains the required `deepening_1_layer_1`, `deepening_1_layer_2`, `deepening_2_layer_1`, and `deepening_2_layer_2` fields. It does not claim same-sample material validation, does not claim graph residual power has been verified, and keeps Jankousky/Furubayashi/Srivastava material validation blocked.

## Required Gate 1.5 Field Check

Pass.

The object explicitly contains:

- `deepening_1_layer_1`: OI baseline absorption risk.
- `deepening_1_layer_2`: same-sample residual protocol.
- `deepening_2_layer_1`: forbidden controls and leakage boundary.
- `deepening_2_layer_2`: fixed-pair/fixed-density OI rule and blocked validation.

These are aligned with A Round 1-3:

- Round 1 established the baseline-first position and graph-residual-only opening.
- Round 2 corrected notation, schema, coefficient units, and same-sample protocol.
- Round 3 filled Srivastava baseline rows, made forbidden-control rules executable, and preserved Jankousky/Furubayashi blocked provenance.

No required Gate 1.5 layer is missing.

## A-Side Scope Check

Pass with warning.

The scientific content is an organization of existing A-side conclusions:

- `OI_baseline_absorption_risk` restates A's baseline-first claim.
- `same_sample_residual_protocol` restates A's residual-only admissibility condition.
- `forbidden_controls` restates A Round 3 leakage rules.
- `fixed_density_fixed_pair_OI_rule` restates A Round 3 fixed-pair/fixed-density safeguard.
- `blocked_validation` restates A Round 3 blocked-provenance status.

Warning: the supplement lists `synthesis/inspector_A_C2_round3.md` and `synthesis/reviewer_C2_round3.md` as source files, and includes `current_warning_from_inspector` plus `reviewer_decision`. These are external boundary/status annotations rather than A's own conclusions. This is not a scientific blocker because they are used only as restrictive guardrails, not as positive evidence or new physical claims. For a strict "A-only conclusion summary" artifact, move these into a separate `external_gate_constraints` section.

## Q1. Dimension / Formula Check

Pass.

Checked formulas:

- `OI_norm = sum(N_ab*S_ab)/volume`
  - `N_ab`: pair count.
  - `S_ab`: dimensionless orbital overlap integral/proxy.
  - `volume`: volume.
  - Result: inverse volume, consistent with the Srivastava Table II normalized-by-volume baseline usage from A Round 3.

- `OI_pair_mean = OI_raw_sum/N_pair`
  - `OI_raw_sum`: dimensionless pair-overlap sum.
  - `N_pair`: pair count.
  - Result: dimensionless mean overlap.

- `r_y_s = y_s - f_y(OI_norm_s, controls_s)`
  - Residual has the same unit as target `y_s`, assuming the baseline model predicts the same target.

- `r_y_s = alpha_0 + alpha_1*lambda2_resid_s + alpha_2*spectral_radius_resid_s + alpha_3*attack_resid_s + error_s`
  - Coefficients absorb the residual-label units; no dimensional inconsistency is introduced.

No invalid dimensional arguments to `exp`, `sin`, `log`, or similar functions are asserted in this Gate 1.5 supplement.

## Q2. Direction / Limit Check

Pass.

The stated directions are self-consistent:

- At fixed pair sum, increasing volume lowers volume-normalized `OI_norm`.
- At fixed declared `N_pair`, `OI_pair_mean = OI_raw_sum/N_pair` is the proper normalization, so raw-sum changes cannot be interpreted as density effects.
- When `N_pair` changes with volume, composition, or cutoff, `pair_density` must be controlled or matched before graph metrics can support any independent residual-power claim.
- Graph quantities are admissible only after OI plus mandatory controls and overlap/degree/weight/size-preserving residualization.

No reversed ratio, sign flip, or direction mismatch was found.

## Q3. Circularity / Leakage Check

Pass.

The supplement does not use baseline rows, synthetic rows, blocked rows, or residual protocols as proof that graph metrics work. It repeatedly marks:

- `same_sample_validation_done: false`
- `graph_residual_verified: false`
- `material_validation_status: blocked`
- `current_status: not met`

It also explicitly forbids:

- claiming graph residual power has been verified,
- claiming same-sample material validation is complete,
- using Srivastava Table II rows as evidence that graph metrics win,
- treating synthetic or blocked rows as physical validation.

No circular self-proof was found.

## Q4 / Q5. Numerical, Algebraic, and Source Check

Pass.

This supplement contains no new numerical calculation beyond restating A Round 3 formula boundaries and blocked source-family statuses. The cited source-family statuses match A Round 3 and the reviewer boundary:

- Srivastava: four reported Table II/Fig. 4 baseline rows only; graph metrics and external residuals blocked.
- Jankousky: blocked pending exact structure ID, same-sample `OI_norm`, graph metrics, external labels, and train/test residual split.
- Furubayashi: blocked pending real digitization and same-sample structure or accepted structural proxy.

Algebraic consistency:

- The Round 2 notation correction is preserved: spectral-radius residual is named `spectral_radius_resid_s`, not `rho_resid_s`.
- `attack_resid_s` is consistent with the Round 3 targeted-damage residual concept.
- Fixed-pair and fixed-density rules do not contradict each other; they apply under different pair-count conditions.

No quantity-level mismatch greater than order-of-magnitude tolerance is present because no new quantitative estimate is made.

## Same-Sample Validation Boundary

Pass.

No same-sample validation overreach was found. The supplement states the acceptance condition but does not claim it has been met:

- held-out residual improvement is required,
- stable signs are required,
- exact same-sample provenance is required,
- `same_sample_validation_done` remains false,
- `graph_residual_verified` remains false.

The blocked-validation section correctly says no row currently contains Srivastava-style `OI_norm`, executable controls, real graph spectral features, and an independent held-out residual label in the same auditable sample.

## Q6. Comprehensive Judgment

Pass with one warning. The supplement can be used as the Gate 1.5 A-side C2 deepening summary, provided downstream PI treats it as a restrictive summary/protocol boundary and not as material validation.

The one warning is administrative/scope-related rather than scientific: external INSPECTOR/REVIEWER constraints are included in the artifact. This is acceptable for gate hygiene, but if the artifact is meant to be purely A-authored, those constraints should be separated from A conclusions.

--- Feed Forward To Next Round ---

Blocking fixes:

None.

Warning-level fixes:

1. If strict A-only provenance is required, move `current_warning_from_inspector` and `reviewer_decision` into an `external_gate_constraints` section so the A conclusions remain cleanly separated from gate/reviewer annotations.

---

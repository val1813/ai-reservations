# INSPECTOR Report: A C2T Round 4

Role: INSPECTOR  
Object: `current/A/C2T_round4.json`  
Date: 2026-06-04

Reviewed inputs only:
- `current/A/C2T_round4.json`
- `current/C2T/artifacts/C2T_A_witness_requirements_round4.csv`
- `synthesis/reviewer_C2T_round3.md`
- `synthesis/inspector_A_C2T_round3.md`

Boundary: this inspection did not read any B output. Mechanical `validate.py` / `quantum.py` was not run because no `validation/validate.py` or `validation/quantum.py` exists under the project path. Q1-Q6.5 were checked manually against the supplied A-side Round 4 object and witness-requirements CSV.

## Verdict

PASS AS A-SIDE WITNESS-REQUIREMENT DEFINITION; NOT MATERIAL VALIDATION.

A Round 4 responds to the REVIEWER Round 3 fatal A-side point: the prior blocker labels lacked an executable witness layer. Round 4 defines the minimum A-side Srivastava/OI witness fields and mode-specific pass/block predicates needed for a future executor to evaluate `BLOCK/WARN/PASS` from payload fields rather than prose labels.

The artifact also preserves the required scientific boundary:
- `material_validation_allowed=false`
- `material_validation_performed=false`
- `Srivastava_baseline_status=not_reproduced`
- `current_candidate_decision=BLOCK`
- no graph-vs-OI, same-sample closure, Srivastava reproduction, or material-validation success is claimed.

## REVIEWER Fatal-Point Response

PASS for the A-side portion.

The REVIEWER fatal error was: Round 3 had blocker-status CSV labels but no executable witness payload schema, so `BLOCK/WARN/PASS` was not a reproducible audit decision.

A Round 4 does not deliver the full multi-side executor requested by REVIEWER, but it does deliver the A-side OI/Srivastava component it claims to deliver. The CSV defines concrete witness fields, the gate each field feeds, deterministic pass conditions, deterministic block conditions, and current-candidate missing/partial status.

The A-side response is sufficient for this narrower scope:
- exact source identity: `source_row_id`
- structure mapping: `structure_id`
- mode declaration: `OI_comparison_mode`
- raw and normalized OI witnesses: `OI_raw_sum`, `OI_norm`
- normalization provenance: `OI_normalization_formula_id`
- pair-selection provenance: `pair_cutoff_A`
- fixed-density support: `pair_density`
- fixed-pair support: `OI_pair_mean`, `N_pair`, `N_pair_provenance_id`

Residual scope limit: this is not the full C2T executor package requested by REVIEWER (`schema`, examples, expected results, command/script contract). It is acceptable only as A-side Round 4 contribution, not as North-Star closure.

## OI/Srivastava Witness Requirements

PASS.

The witness requirements are explicit enough to block the earlier ambiguity:
- Srivastava reproduction requires same-row/source linkage plus `OI_raw_sum`, `OI_norm`, `OI_normalization_formula_id`, and `pair_cutoff_A`.
- `OI_norm` alone is marked reported context only and not reproduced.
- `fixed_density` is blocked unless `pair_density` is present and tied to the same source row, structure, pair cutoff/rule, raw sum, and normalized OI provenance.
- `fixed_pair` is blocked unless `OI_pair_mean`, positive integer `N_pair`, and `N_pair_provenance_id` are present and tied to the same counted-pair denominator.
- `OI_comparison_mode=no_claim` is allowed only as context and cannot pass material validation.

This directly answers the A-side part of the REVIEWER demand for exact row-level witnesses for OI/Srivastava gates.

## Q1. Dimensional Check

PASS for contract-level equations.

The two equations are dimensionally coherent at schema level:
- `OI_norm == OI_raw_sum / cell_volume_m3`: raw overlap units divided by volume gives volume-normalized overlap units.
- `OI_pair_mean == OI_raw_sum / N_pair`: `N_pair` is dimensionless, so the result has overlap units per counted pair.

No exponential, logarithmic, trigonometric, or hyperbolic arguments appear.

## Q2. Sign / Direction Check

PASS.

Round 4 makes gate-direction claims only. Missing or provenance-inconsistent witnesses force `BLOCK`; complete same-source/same-structure witnesses are required before a Srivastava/OI row can be promoted. That direction matches the REVIEWER fatal point and the current candidate statuses in the CSV.

No physical directionality, material-performance direction, or graph-beats-OI direction is asserted.

## Q3. Circular Argument Check

PASS.

Round 4 does not validate the A-side gates by reusing their output as evidence of material success. It explicitly says current candidates remain `BLOCK` because the actual source-to-structure mapping, raw overlap sums, exact normalization provenance, pair selection, and complete same-sample row evidence remain missing or partial.

The current artifact is a requirement table, not a populated validation result.

## Q4. Order-of-Magnitude / Scope Check

PASS / NOT APPLICABLE.

No numerical material-property magnitude or graph-effect magnitude is claimed. The only quantitative formulas are consistency gates for future witness payloads. The current statuses are missing/partial/context-only, so no numerical validation follows.

## Q5. Algebraic / Limit Check

PASS.

Key limiting cases behave correctly:
- Missing `OI_raw_sum` blocks Srivastava reproduction, fixed-density, and fixed-pair modes.
- Reported `OI_norm` without raw-sum derivation remains context only and not reproduced.
- Missing `OI_normalization_formula_id` blocks Srivastava reproduction.
- Missing `pair_cutoff_A` or equivalent pair-selection rule blocks OI raw-sum reproducibility.
- Missing `N_pair_provenance_id` blocks fixed-pair mode even if a numeric denominator appears.
- `no_claim` cannot be upgraded into material validation.

These gates prevent the exact overclaiming path identified by the REVIEWER.

## Q5d. Source / Provenance Level

PASS WITH SCOPE LIMIT.

Round 4 defines source/provenance requirements but does not claim they are populated. Current statuses remain:
- `source_row_id`: required missing for current candidates
- `structure_id`: required missing or partial
- `OI_raw_sum`: required missing
- `OI_norm`: partial reported context only, not reproduced
- `OI_normalization_formula_id`: required missing
- `pair_cutoff_A`: required missing
- `pair_density`: required missing
- fixed-pair fields: conditionally required and not populated

This is correct for a witness-requirement artifact. It would become a blocker only if presented as populated Srivastava reproduction.

## Q6. Integrated Judgment

PASS for the stated A-side Round 4 goal.

A Round 4 defines OI/Srivastava witness requirements and deterministic gate predicates. It answers the A-side part of the REVIEWER fatal point without claiming the full C2T executor is complete.

No blocking mathematical, provenance-loop, or claim-scope error was found inside the stated A-side scope.

## Q6.3 Claim Shrinkage

No problematic shrinkage.

Relative to A Round 3, Round 4 narrows from row-level audit contract language to A-side OI/Srivastava witness requirements. This is explicit and aligned with the REVIEWER fatal point. It does not hide a failed validation as success; it states that current candidates remain `BLOCK`.

## Q6.4 Alternative Explanation Check

PASS.

The simpler alternative explanation is that existing Srivastava/OI entries are reported context candidates lacking reproducible raw-sum, normalization, pair-selection, and source-structure witnesses. Round 4 accepts that explanation by keeping `Srivastava_baseline_status=not_reproduced` and `material_validation_performed=false`.

## Q6.5 Landing Calculation Check

PASS.

Round 4 does not claim a no-prior-art blank without landing. Its landing object is concrete: `C2T_A_witness_requirements_round4.csv` with field-level pass/block requirements and current-candidate statuses. This is sufficient as an A-side half-product, not sufficient as final material validation or C2T closure.

## Focus Checks Requested By PI

1. Did A respond to the REVIEWER fatal point's A-side portion?

Yes. It defines the A-side witness fields and predicates needed to make Srivastava/OI blocker decisions reproducible at payload level.

2. Did A define OI/Srivastava witness requirements?

Yes. The CSV specifies source identity, structure mapping, OI mode, raw sum, normalized OI, normalization formula provenance, pair cutoff/rule, pair density, and fixed-pair denominator witnesses with pass/block conditions.

3. Does A still avoid claiming Srivastava reproduction?

Yes. It states `Srivastava_baseline_status=not_reproduced`, and the CSV marks reported `OI_norm` as context only unless raw-sum and normalization witnesses are supplied.

4. Does A still avoid material validation?

Yes. It states no material validation is allowed or performed, and current candidates remain `BLOCK`.

## Residual Warnings

1. Do not treat this A-side witness requirements file as the full REVIEWER-requested executor. It lacks populated witness rows, examples, expected executor results, and a runnable command/script contract.

2. Future work must keep `OI_comparison_mode` declared before target-label inspection; otherwise the gate can become label-adaptive.

3. Future populated payloads must derive `material_validation_allowed` from all C2T gates, not from the A-side OI/Srivastava gates alone.

## Feed To Next Round

--- Feed to next round ---

Must fix, blocking level:

None for the A-side witness-requirement definition stage.

Recommended fix, warning level:

1. Carry `C2T_A_witness_requirements_round4.csv` into the future executor as A-side predicates, but do not cite it as Srivastava reproduction.
2. Keep all current Srivastava/OI candidates `BLOCK` until `source_row_id`, `structure_id`, `OI_raw_sum`, `OI_norm`, `OI_normalization_formula_id`, `pair_cutoff_A`, and mode-specific denominator/density witnesses are populated and provenance-linked.
3. If implementing the full REVIEWER exit route, add populated witness examples, deterministic expected results, and a runnable validation command; A Round 4 alone is not the full closure artifact.

---

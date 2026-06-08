# INSPECTOR Report: A C2T Round 2

Role: INSPECTOR
Object: `current/A/C2T_round2.json`
Date: 2026-06-04

Reviewed inputs:
- `current/A/C2T_round2.json`
- `synthesis/inspector_A_C2T_round1.md`
- `current/plan/C2T_joined_table_schema.csv`
- `current/plan/C2T_field_blockers.csv`

Boundary: this inspection did not read `current/B/C2T_round2.json` or any B output.

## Verdict

WARN

A Round 2 materially addresses the A Round 1 inspector warnings and keeps the correct claim boundary: no material validation, no graph-beats-baseline claim, no reproduced Srivastava `O_s` claim, and no fixed-density/fixed-pair OI conclusion. `material_validation_allowed` is not erroneously enabled; it is false in the artifact-level `claim_boundary`, false in the default current-row derivation, and only becomes true after all row-level gates pass.

The remaining issue is audit-template executability. The template is close to executable, but one newly introduced rule depends on fields that are not listed as required template fields, so an automated row-level audit would still need schema expansion before it can run deterministically.

## Blocking Items

None.

## Warnings

1. The fixed-density versus fixed-pair rule is not fully executable as written. `A_R2_RULE_ADD_002` requires `OI_comparison_mode in {fixed_density, fixed_pair, no_claim}` and refers to fixed `N_pair` provenance, but `OI_comparison_mode` and an explicit `N_pair` / `N_pair_provenance` field are not present in `audit_template_fields`. This creates a parser-level ambiguity: rows can be blocked by the rule, but the required inputs to evaluate the rule are not guaranteed by the template schema.

2. The `forbidden_control_audit` field remains a high-level JSON result rather than a normalized audit table contract. A Round 2 correctly requires pass/fail/not_applicable and split namespace semantics, but it does not specify required per-rule output columns such as `rule_id`, `target_type`, `namespace`, `columns_checked`, `result`, and `reason`. This is not circular leakage, but it limits mechanical audit reproducibility.

3. The template adds several Srivastava/OI-specific required fields beyond the active joined-table schema, including `structure_id`, `num_atoms_or_snapshot_size`, `cell_volume_m3`, `OI_raw_sum`, `OI_norm`, `OI_normalization_formula_id`, `pair_cutoff_A`, `pair_density`, and `OI_pair_mean`. That is acceptable for an A-side Srivastava audit template, but the schema delta should be declared as an explicit A-side extension before joined-table automation.

## Round 1 Warning Resolution

| Round 1 warning | Round 2 status | Inspector assessment |
|---|---:|---|
| `label_provenance_id` was over-marked as present | RESOLVED | Downgraded to `partial`; pass condition now requires DOI plus table/figure/SI/path and row or point id. |
| `synthetic_label_flag` and `material_validation_allowed` not explicit | RESOLVED | Both are required row-level template fields, with missing/true synthetic rows blocking validation. |
| `forbidden_namespace=oi;graph` not mechanically clean | MOSTLY RESOLVED | Split rules are provided. Remaining warning is only the normalized audit-output contract. |
| `B0_carrier_density` needed row-level independence status | RESOLVED | `B0_carrier_density_independence_status` enum is required and same-measurement inversion is forbidden. |
| Reported `OI_norm` must not become reproduced `O_s` | RESOLVED | A explicitly keeps existing Srivastava rows context-only until raw sum, exact normalization, and row-to-structure mapping exist. |

## Leakage Check

No active circular leakage was found in the Round 2 artifact.

A correctly blocks:
- synthetic or graph-generated labels from material validation;
- effective-mass label self-leakage through `m_eff_over_m0` or algebraic copies;
- Hall-mobility leakage through same-measurement `sigma/(n*e)` carrier-density inversion;
- graph-independent claims using OI, pair-density, or cell-volume variables without residualization/matching controls;
- Srivastava reproduction or graph-vs-OI claims from reported `OI_norm` alone.

Residual leakage risk is procedural rather than active: if `OI_comparison_mode` and fixed-`N_pair` provenance are not added to the required schema, the fixed-density/fixed-pair gate cannot be evaluated mechanically.

## Material Validation Flag

PASS.

A Round 2 does not erroneously open `material_validation_allowed`. The artifact-level boundary sets it to `false`; the default current Srivastava-row decision sets it to `false`; and the final derivation only permits `true` after all required provenance, structure, B0, G1, synthetic-label, and forbidden-control gates pass.

## Required Fix Before PASS

To upgrade this artifact from WARN to PASS, add the missing executable rule inputs to `audit_template_fields`:

- `OI_comparison_mode`, enum: `fixed_density`, `fixed_pair`, `no_claim`.
- `N_pair` or `fixed_pair_count`, required when `OI_comparison_mode=fixed_pair`.
- `N_pair_provenance_id`, required when `OI_comparison_mode=fixed_pair`.
- A normalized `forbidden_control_audit` output contract, preferably one row per rule evaluation with stable `rule_id`, `result`, and `reason`.

After those additions, the template would be executable as a row-level gate template, assuming the actual row data are populated.

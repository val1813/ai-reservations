# PI synthesis: LP29-C2T Round 1

Date: 2026-06-04

## Inputs

- A: `current/A/C2T_round1.json`
- B: `current/B/C2T_round1.json`
- INSPECTOR A: `synthesis/inspector_A_C2T_round1.md`
- INSPECTOR B: `synthesis/inspector_B_C2T_round1.md`
- Prior/data-source search: `synthesis/R1_prior_search_C2T.md`
- Data precondition files:
  - `current/plan/C2T_required_join_fields.md`
  - `current/plan/C2T_joined_table_schema.csv`
  - `current/plan/C2T_source_inventory.csv`
  - `current/plan/C2T_field_blockers.csv`

## A/B independence and framework difference

A and B were launched as independent agents.

A framework: Srivastava/OI baseline and candidate AOS literature extractability. It asks whether exact overlap normalization, row-to-structure mapping, and external labels can be recovered.

B framework: graph feature and external-label provenance closure. It asks whether `G1_lambda2_Lsym`, `G1_rho_A_budget_norm`, and `G1_attack_gap_lambda2` can be closed on the same sample without synthetic-to-material leakage.

The frameworks are different and complementary. Both outputs keep material validation blocked.

## Core Round 1 result

C2T Round 1 produced a blocker/extractability state, not a material validation table.

Current status:
- Srivastava rows provide baseline context, but exact executable `O_s` normalization and row-to-structure mapping remain incomplete.
- The three G1 graph features are well-defined as schema targets, but no provenance-complete same-sample material rows exist.
- External labels remain candidate-only unless they carry row-level `label_provenance_id`, units, method, source, independent controls, and same-sample crosswalk.
- Synthetic rows remain diagnostic only with `synthetic_label_flag=true` and `material_validation_allowed=false`.

## INSPECTOR warnings carried forward

1. A should downgrade Srivastava `label_provenance_id` from `present` to `candidate/partial` until DOI/table/SI/path plus row-level label source is locked.
2. Future A/B artifacts must include schema flags `synthetic_label_flag` and `material_validation_allowed` in field-status accounting, not only in claim boundaries.
3. The `oi;graph` forbidden-control rule must be split or assigned explicit parser semantics before mechanical audit.
4. Hall mobility / carrier density independence requires row-level audit.
5. B cited some files outside the B INSPECTOR review bundle; those references are accepted as project context but remain not re-audited by that inspector.
6. Same-sample closure remains untested. Schema presence is not evidence of validation.

## Prior search result

No direct prior was found for a same-sample provenance-complete graph-vs-Srivastava-overlap residual validation joined table in amorphous oxide transport. This removes no evidence blocker; it only means Round 1 found no immediate same-topic prior-art kill.

## Claim boundary

Allowed:
- C2T has a concrete required-field schema, candidate source inventory, and field blocker table.
- A/B Round 1 identifies the minimal blockers for a provenance-complete external joined table.

Forbidden:
- No material validation.
- No graph-beats-overlap baseline claim.
- No Srivastava reproduction claim.
- No use of synthetic rows as material evidence.

## Next step

Continue to Round 2 only if the goal is to attempt unblock planning. The first Round 2 task should be mechanical: build an executable row-level audit template that includes `synthetic_label_flag`, `material_validation_allowed`, split forbidden-control namespaces, and carrier-density independence status.


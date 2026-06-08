# INSPECTOR: C2T-S1 Jankousky single-row audit

Date: 2026-06-04

Role: LP29-C2T-S1 Jankousky single-row audit INSPECTOR

## Verdict

PASS

The negative blocker witness is adequately supported by the locally extracted PDF evidence and by the executor output. The row should remain `BLOCK`, and `material_validation_allowed=false` is correct.

## Files inspected

- `synthesis/PI_C2T_S1_jankousky_single_row_audit.md`
- `current/C2T/artifacts/C2T_jankousky_single_row_payload.jsonl`
- `current/C2T/artifacts/C2T_jankousky_single_row_result.csv`
- `current/C2T/scripts/C2T_executor.py`
- `current/C2T/artifacts/jankousky_pdf_text_extract.txt`

## Checks

### PDF evidence supports BLOCK

PASS.

The PDF extract provides article identity and DOI at lines 1-3 and publication date at line 58. It provides method-level evidence for the amorphous In2O3 ensemble: 1,500 random 40-atom structures, randomized lattice/atom generation, VASP/PBE relaxation, convergence thresholds, and ensemble-level structure-function justification at lines 606-658. It also states that QSGW was run on a selected 100-structure subset at lines 660-669.

This evidence is sufficient for a negative absence/blocker finding because it documents method-level generation and analysis, but does not expose a machine-reviewable same-sample joined row with stable raw coordinates, `structure_id`, `snapshot_id_or_window`, graph convention provenance, and external label provenance.

### material_validation_allowed

PASS.

The payload sets `material_validation_claimed=false`, and the executor contract permits material validation only when `row_decision=PASS` and all required gate blockers are cleared. The result CSV reports:

- `required_joined_fields_presence_status=BLOCK`
- `same_sample_crosswalk_status=BLOCK`
- `graph_convention_lock_status=BLOCK`
- `external_label_independence_status=BLOCK`
- `row_decision=BLOCK`
- `material_validation_allowed=false`

I reran the executor against the same payload to a temporary verification CSV; the output matched the inspected result exactly. There is no erroneous material-validation opening.

### Obvious fillable fields

PASS.

No obvious machine-reviewable joined-table fields should be filled from the local PDF alone. The text supports high-level method fields such as material family, ensemble size, cell size, relaxation method, and QSGW subset size, but those do not satisfy the C2T gates requiring same-sample row identity and graph/label provenance.

Keeping the following fields missing/null is appropriate:

- `structure_or_SI_source`
- `structure_id`
- `snapshot_id_or_window`
- `label_provenance_id`
- `graph_convention_provenance_id`
- `graph_cutoff_rule`
- `rho_budget_normalization_rule`
- `same_graph_identity_record`
- `external_label_payload`
- `graph_proxy_exclusion_evidence`

### Supplement/source-data retrieval

PASS, with required next action preserved.

The PDF explicitly says online content, source data, supplementary information, and data/code availability statements are available at the DOI page at lines 518-523. It further states that data supporting the study are available from the corresponding author upon reasonable request and that source data are provided with the paper at lines 798-801. Supplementary material is also referenced at lines 845-847.

Therefore, the PI next unblock action is correct: retrieve supplementary/source data from the DOI page and, if necessary, corresponding-author or repository data. The local PDF alone is not enough to unblock the row.

## Final conclusion

The audit result is internally consistent and machine-reproducible:

`C2T-AUDIT-0101`: `BLOCK`, `material_validation_allowed=false`.

No change to the payload/result is recommended before supplement/source-data retrieval.

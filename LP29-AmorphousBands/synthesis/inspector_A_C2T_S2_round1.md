# INSPECTOR: LP29-C2T-S2 A Round 1

Date: 2026-06-04

Input inspected:
- `current/A/C2T_S2_round1.json`
- `synthesis/gate_minus1_LP29-C2T-S2.md`
- `current/A/artifacts/C2_Srivastava_baseline_rows.csv`

B-side output was not read.

## Verdict

INSPECTOR PASS WITH CONTINUATION WARNING.

A correctly blocks `reproduced exact O_s` and keeps Srivastava values as `reported_context_only`. No blocking error was found in the requested checks.

Continuation warning: Round 2 must not upgrade Srivastava `OI_norm` to a residual-validation or reproduced exact `O_s` baseline unless it supplies a row-level witness payload: `OI_raw_sum`, executable normalization rule/formula id, pair rule/cutoff provenance, `structure_id`, atom count or same-structure mapping, and source-row linkage.

## Requested Checks

### 1. Reported context vs reproduced exact `O_s`

PASS.

A explicitly separates the two standards:
- JSON verdict is `BLOCK_REPRODUCED_EXACT_O_S_BASELINE`.
- Summary states Srivastava 2019 is valid only as literature context for reported orbital-overlap values and effective-mass correlation.
- Decision rule says to use Srivastava 2019 only as `reported_context_only` unless exact formula/procedure, raw overlap sum, normalization, pair selection, and structure mapping are supplied.
- `reproduction_fields_status.OI_norm.status` is `reported_context_only`.
- `reproduction_fields_status.overall_status` is `reported_context_available_exact_O_s_reproduction_blocked`.
- CSV rows have `join_level=reported_table_and_text`, `decisive_claim_allowed=false`, and blank `OI_raw_sum`, `structure_id`, and `num_atoms`.

No instance was found where A treats reported `OI_norm` values as reproduced exact `O_s`.

### 2. Wrong fallback PDF use

PASS.

A identifies the fallback PDF as wrong and excludes it:
- `additional_access_checks.download_with_fallback` says the returned fallback was `wrong_pdf_core_38590358_excluded`.
- `wrong_pdf_identification` identifies DOI `10.1038/srep13467`, not Srivastava DOI `10.1063/1.5096042`.
- `negative_support_against_reproduced_baseline` states the downloaded 2015 Scientific Reports article was rejected as Srivastava evidence.

No evidence was found that A used the wrong fallback PDF to support Srivastava reproduction.

### 3. No material validation

PASS.

A preserves the no-material-validation boundary:
- CSV provenance is `reported_from_Srivastava_TableII_and_text_Fig4_paragraph;not_graph_validation`.
- `external_residual`, `lambda2_resid`, `spectral_radius_resid`, and `attack_resid` fields are blank in all four rows.
- `blocked_fields` explicitly includes the residual fields.
- `decisive_claim_allowed=false` for every row.
- JSON frames the C2 artifact as context baseline rows and does not claim graph/material validation.

No material residual validation, graph validation, or decisive LP29 material claim is made from these rows.

## INSPECTOR Q-Checks

Q1 quantity/unit check: Not applicable. A Round 1 does not introduce equations requiring dimensional validation; it audits evidence status.

Q2 sign/direction check: PASS. The direction of the conclusion is conservative: reported context exists, exact reproduction is blocked.

Q3 circularity check: PASS. A does not validate exact `O_s` by restating reported `OI_norm`; it uses missing witness fields as the blocker.

Q4 order-of-magnitude check: Not applicable for a new quantitative claim. The reported values are context rows only and are not used for material validation.

Q5 algebra/numeric provenance check: PASS for the requested scope. Numeric `OI_norm` values are provenance-labeled as reported table/text context, while the missing raw-sum and normalization witness fields block reproduction.

Q6.3 claim shrinkage: No blocking shrinkage. The round narrows the gate from possible Srivastava baseline use to context-only use, which matches GATE -1 Proposition B rather than silently weakening a claimed reproduction.

Q6.4 alternative explanation: Warning only. A does not need to exclude a physics alternative in this audit round because its claim is an evidence-gating conclusion, not a new mechanism.

Q6.5 landing calculation: PASS for this task. A does not assert a no-prior-art blank or material validation claim requiring landing calculation; it blocks reproduction pending witness payload.

## Feed To Next Round

--- Feed to next round ---

Blocking fixes:
1. None for A Round 1 under the requested checks.

Warning-level carryovers:
1. Keep `OI_norm` as `reported_context_only`; do not relabel it as reproduced exact `O_s`.
2. Do not use `core_38590358.pdf` or DOI `10.1038/srep13467` as Srivastava 2019 evidence.
3. If Round 2 attempts Srivastava reproduction, require row-level witness fields: `structure_id`, `num_atoms`, `OI_raw_sum`, `OI_normalization_formula_id`, exact pair rule or `pair_cutoff_A` provenance, `N_pair`/pair provenance where applicable, and same-structure mapping.
4. Maintain `decisive_claim_allowed=false` until a material/residual validation artifact is actually produced.

---

# INSPECTOR: LP29-C2T-S2 A Round 2

Date: 2026-06-04

Input inspected:
- `current/A/C2T_S2_round2.json`
- `current/A/artifacts/S2_Srivastava_reproduction_blocker_table.csv`
- `synthesis/inspector_A_C2T_S2_round1.md`

B-side output was not read.

## Verdict

INSPECTOR PASS.

A Round 2 correctly implements the requested blocker-table discipline. It mechanically separates `reported_context_only` Srivastava values from a reproduced exact `O_s` baseline, keeps the wrong fallback PDF excluded, and preserves the no-material-validation boundary. No blocking error was found.

Continuation warning: this is still a blocker artifact, not a reproduction artifact. Any next step that relabels Srivastava `OI_norm` as reproduced exact `O_s` must first supply row-level witnesses: official row/page provenance, exact structure identity, atom count, pair rule and pair list, `N_pair`, executable orbital-overlap kernel, `OI_raw_sum`, executable normalization formula id, reproduced `OI_norm` check, and same-structure mapping.

## Requested Checks

### 1. Reported context vs reproduced exact `O_s`

PASS.

Round 2 keeps the distinction mechanical rather than rhetorical:
- JSON verdict remains `BLOCK_REPRODUCED_EXACT_O_S_BASELINE`.
- JSON summary says the four rows are usable only as reported context and lack `structure_id`, `num_atoms`, `OI_raw_sum`, executable `OI_normalization_formula_id`, pair-list provenance, `N_pair`, same-structure mapping, and residual fields.
- CSV field `OI_norm` has status `REPORTED_CONTEXT_ONLY` and says it must stay context-only unless raw sum, normalization, pair rule, and structure witness reproduce it.
- CSV fields `OI_raw_sum`, `OI_normalization_formula_id`, `N_pair`, `N_pair_provenance_id`, `pair_density`, and `same_structure_mapping` remain blocking or partial-blocking.
- CSV `overall_reproduction_status` is `BLOCK_REPRODUCED_EXACT_O_S_BASELINE`.

No instance was found where A treats reported `OI_norm` values as reproduced exact `O_s`.

### 2. Wrong fallback PDF use

PASS.

A keeps the wrong fallback PDF excluded:
- JSON `forbidden_use_now` explicitly says not to use `core_38590358.pdf` or DOI `10.1038/srep13467` as Srivastava evidence.
- JSON `resolved_previous_warnings.do_not_use_wrong_fallback_pdf` says the warning is resolved by excluding that PDF.
- CSV field `wrong_fallback_pdf` has status `EXCLUDED` and identifies `core_38590358.pdf` as Lee et al. 2015 DOI `10.1038/srep13467`, not Srivastava 2019.

No evidence was found that A uses the wrong fallback PDF to support Srivastava reproduction.

### 3. No material validation

PASS.

A keeps material validation frozen:
- JSON forbids graph-vs-overlap residual validation and forbids claiming graph metrics beat the orbital-overlap baseline.
- JSON `next_plan.immediate` says not to advance to material validation.
- CSV fields `external_residual`, `lambda2_resid`, `spectral_radius_resid`, and `attack_resid` are `BLOCK_MATERIAL_VALIDATION`.
- CSV `decisive_claim_allowed` is `PASS_AS_BLOCKER` with value `false for all four rows`.
- CSV provenance remains `reported_from_Srivastava_TableII_and_text_Fig4_paragraph;not_graph_validation`.

No material residual validation, graph validation, or decisive LP29 material claim is made from these rows.

## INSPECTOR Q-Checks

Q1 quantity/unit check: Not applicable. No new equation requiring dimensional validation is introduced; Round 2 is a provenance/blocker table.

Q2 sign/direction check: PASS. The conclusion direction is conservative: reported context exists, exact Srivastava `O_s` reproduction remains blocked.

Q3 circularity check: PASS. A does not validate exact `O_s` by restating reported `OI_norm`; it treats missing witness fields as blockers.

Q4 order-of-magnitude check: Not applicable for a new quantitative claim. Reported values are not used for material validation.

Q5 algebra/numeric provenance check: PASS for this scope. Numeric `OI_norm`, `cell_volume_m3`, and `m_eff_over_m0` are labeled context-only or partial-context; executable raw-sum and normalization witnesses remain absent and blocking.

Q6.3 claim shrinkage: PASS. Round 2 does not silently shrink a reproduction claim; it explicitly preserves the Round 1 context-only boundary and converts it into a blocker table.

Q6.4 alternative explanation: Warning only / not required for this audit. A's active claim is evidence gating, not a new physical mechanism; it also does not assert material validation.

Q6.5 landing calculation: PASS for this task. A does not assert a no-prior-art blank or material-validation claim requiring landing calculation. The artifact instead blocks reproduction until landing witnesses exist.

Mechanical validation note: no `validation/` directory exists under `LP29-AmorphousBands`, so no project validator was run; this report uses manual INSPECTOR checks.

## Feed To Next Round

--- Feed to next round ---

Blocking fixes:
1. None for A Round 2 under the requested checks.

Warning-level carryovers:
1. Keep Srivastava `OI_norm` as `REPORTED_CONTEXT_ONLY`; do not relabel it as reproduced exact `O_s`.
2. Keep `core_38590358.pdf` and DOI `10.1038/srep13467` excluded as Srivastava evidence.
3. Do not advance to material/residual validation while `structure_id`, `num_atoms`, `OI_raw_sum`, executable normalization, pair-list provenance, `N_pair`, and same-structure mapping remain missing.
4. Preserve `decisive_claim_allowed=false` until a proof-carrying exact witness payload and residual-validation artifact pass inspection.

---

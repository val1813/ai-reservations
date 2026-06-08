# INSPECTOR Report: B C2T-S2-R1-I1 Round 1

Input files:
- `current/B/C2T_S2_R1_I1_round1.json`
- `current/B/artifacts/I1_adversarial_test_matrix_round1.csv`

Scope: adversarial no-silent-upgrade test matrix for executable `O_s` baseline-admission validator. `Phase清单.md` was not modified.

## Verdict

INSPECTOR PASS with one non-blocking synchronization warning.

No blocking defect was found against the requested I1 Round 1 criteria. The matrix covers the required adversarial axes, preserves the current exact `O_s` BLOCK guard, avoids the forbidden overclaims, includes two-layer deepening entries, and the CSV schema/row count are adequate.

## Required Coverage Check

PASS: locator-only covered.
- JSON: `I1_LOCATOR_ONLY_TO_CONTEXT`
- CSV: `I1_LOCATOR_ONLY_TO_CONTEXT`
- Expected terminal: `BLOCK`

PASS: scalar-only covered.
- JSON: `I1_SCALAR_ONLY_TO_CONTEXT`
- CSV: `I1_SCALAR_ONLY_TO_CONTEXT`
- Expected terminal: `BLOCK`

PASS: context-only covered.
- JSON: `I1_CONTEXT_ONLY_TO_EXACT`
- CSV: `I1_CONTEXT_ONLY_TO_EXACT`
- Expected terminal: `CONDITIONAL_CONTEXT_PASS`, not exact

PASS: numeric-closeness covered.
- JSON: `I1_NUMERIC_CLOSENESS_CONTEXT_TO_EXACT`, `I1_PAIR_CARDINALITY_MISMATCH_NUMERIC_CLOSE`
- CSV: adds `I1_NUMERIC_CLOSENESS_REPLAY_NO_TOLERANCE`
- Expected terminals include `BLOCK` or `DIAGNOSED_MISMATCH`, never exact

PASS: executor-quality-only covered.
- JSON: `I1_EXECUTOR_QUALITY_ONLY_TO_EXACT`
- CSV: adds `I1_EXECUTOR_TRACE_UNBOUND_INPUTS`
- Expected terminal: `BLOCK`

PASS: full-exact positive control covered.
- JSON/CSV: `I1_FULL_EXACT_MATCH`
- Expected terminal: `ADMITTED_EXACT`
- This is correctly framed as a positive control requiring full F01-F22 plus predeclared comparison, not as current Srivastava reproduction.

PASS: mismatch covered.
- JSON: `I1_COMPLETE_FINAL_VALUE_MISMATCH`, `I1_STRUCTURE_MAPPING_MISMATCH_WITH_GOOD_TRACE`, `I1_PAIR_CARDINALITY_MISMATCH_NUMERIC_CLOSE`
- CSV: adds raw-sum and normalization mismatch rows
- Expected terminal: `DIAGNOSED_MISMATCH` only where proof-carrying replay/mismatch predicates are sufficient.

## Current Exact O_s BLOCK

PASS.

The current exact `O_s` block is explicitly preserved:
- JSON: `I1_CURRENT_SRIVASTAVA_EXACT_BLOCK`, expected `BLOCK`
- CSV: `I1_CURRENT_SRIVASTAVA_SUMMARY_BLOCK`, expected `BLOCK`
- CSV: `I1_CURRENT_SRIVASTAVA_CONTEXT_ONLY_NOT_EXACT`, expected `CONDITIONAL_CONTEXT_PASS`
- Rule: `NSU-09` states current Srivastava exact `O_s` remains BLOCK unless the full F01-F22 proof-carrying witness tuple is supplied and passes.

This satisfies the regression guard: current Srivastava-related evidence may be reported context when F01-F03 are complete, but it is not silently promoted to exact `O_s`.

## Forbidden Claims Check

PASS.

The JSON explicitly lists the forbidden claims:
- exact Srivastava `O_s` reproduced
- material validation
- graph-vs-overlap residual regression
- graph beats overlap
- exact `O_s` impossible in principle
- numeric closeness is sufficient for exact admission
- executor quality is sufficient for exact admission
- context-only evidence is exact `O_s` evidence

No active claim asserts exact `O_s` reproduction, material validation, graph regression, graph beats overlap, or impossibility. Claims C1-C3 are limited to adversarial matrix coverage and validator terminal-state discipline.

## Deepening Check

PASS.

`deepening_1` has at least two layers:
1. Structural abstraction: monotone proof-lattice with non-substitutable coordinates.
2. Operational consequence: add tempting irrelevant evidence and verify the first missing or failed required predicate still dominates status.

`deepening_2` has at least two layers:
1. Structural abstraction: typed state machine with forbidden coercions.
2. Operational consequence: expose `first_failed_predicate` and reject status computation by evidence count, confidence score, target intent, or numeric distance before constructor predicates pass.

## CSV Schema And Row Count

PASS.

CSV columns:
- `case_id`
- `payload_defect`
- `attempted_upgrade`
- `expected_status`
- `first_failed_predicate`
- `why_this_catches_overclaim`

CSV data rows: 17.

Status coverage:
- `BLOCK`
- `CONDITIONAL_CONTEXT_PASS`
- `CANDIDATE_EXACT_REPLAY`
- `ADMITTED_EXACT`
- `DIAGNOSED_MISMATCH`

The row count is sufficient for the requested axes and includes additional stress rows for tolerance, trace binding, raw-sum mismatch, and normalization mismatch.

## Non-Blocking Warning

WARNING: JSON/CSV case lists are not fully synchronized.

The JSON `adversarial_cases` array has 12 rows, while the CSV matrix has 17 rows. The CSV appears to be the richer executable test matrix and includes additional valid stress cases not mirrored in JSON:
- `I1_NUMERIC_CLOSENESS_REPLAY_NO_TOLERANCE`
- `I1_EXECUTOR_TRACE_UNBOUND_INPUTS`
- `I1_RAW_SUM_MISMATCH_WITH_NORMALIZATION_PASS`
- `I1_NORMALIZATION_CONSTANT_MISMATCH_WITH_GOOD_TRACE`
- split current Srivastava cases

This is not blocking for I1 Round 1 because the required coverage is present and the CSV row count/schema pass. Recommended next-round cleanup: either mirror all CSV cases into JSON or explicitly declare CSV as the authoritative matrix artifact.

## Mechanical Check

No `validate.py` formula/unit validation was run because this I1 artifact is a test-matrix design with no new algebraic formula claims requiring dimensional, limit, or numerical formula validation. The inspection was performed against the requested adversarial coverage and matrix integrity criteria.

--- 投喂下一轮 ---

必须修正（阻断级）:
- None.

建议修正（警告级）:
1. Synchronize JSON and CSV case inventories, or mark the CSV as the authoritative executable matrix artifact.

---

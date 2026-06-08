# REVIEWER final: LP29-C2T-S2-R1-I1-X1

Date: 2026-06-05

## Verdict

**Conditional close only as a weak fixture-level validator baseline; do not close as a full CLI regression firewall.**

X1 is bounded correctly: it does not claim exact Srivastava `O_s` reproduction, material validation, graph-vs-overlap residual regression, or graph beats overlap. The required guard outcomes are present in the observed run. However, the command-line `--expected` contract is not enforced, and the suite command exits `0` even when given an intentionally wrong expected CSV. That prevents X1 from being called a strong "regression firewall" at the CLI contract level.

## Evidence Checked

Read:

- `synthesis/PI_C2T_S2_R1_I1_X1_final.md`
- `synthesis/regression_results_C2T_S2_R1_I1_X1.md`
- `synthesis/gate4_C2T_S2_R1_I1_X1.md`
- `validation/validate.py`
- `tests/test_validate.py`

Executed:

```powershell
python -m pytest tests/test_validate.py
```

Observed: `4 passed`.

Executed:

```powershell
python validation/validate.py --suite current/B/fixtures/I1_authoritative_cases_round3.jsonl --expected current/B/artifacts/I1_regression_command_contract_round3.csv --emit-csv validation/results.csv --strict-no-silent-upgrade --no-legacy-partial-context-only
```

Observed status distribution:

- `BLOCK`: 8
- `CONDITIONAL_CONTEXT_PASS`: 2
- `CANDIDATE_EXACT_REPLAY`: 1
- `ADMITTED_EXACT`: 1
- `DIAGNOSED_MISMATCH`: 5

This matches the stated 17-case distribution.

## Boundary Audit

No overclaim found in the three synthesis files. The PI final explicitly limits the close to executed fixture-level validation and lists forbidden claims:

- no exact Srivastava `O_s` reproduced
- no material validation
- no graph-vs-overlap residual regression
- no graph beats overlap
- no exact-impossible-in-principle claim

Gate 4 repeats the same boundary: the validator does not recompute physical `O_s`, the fixtures are proof-contract fixtures rather than material rows, and graph-vs-overlap regression was not attempted. This is a valid scope contraction, not a scientific result.

## Guard Audit

`PARTIAL_CONTEXT_ONLY` guard: pass at function level. `validate.py` blocks raw legacy `target_mode == "PARTIAL_CONTEXT_ONLY"` before alias resolution and emits `BLOCK + DEPRECATED_PARTIAL_CONTEXT_ONLY + migration_required=true`. This covers the requested raw legacy case, including the dangerous case where F01-F03 predicates are true.

Current Srivastava guard: pass at fixture level. The 17-case suite includes:

- `I1_CURRENT_SRIVASTAVA_SUMMARY_BLOCK` -> `BLOCK`
- `I1_CURRENT_SRIVASTAVA_CONTEXT_ONLY_NOT_EXACT` -> `CONDITIONAL_CONTEXT_PASS`

This correctly admits only reported context and blocks exact admission.

17-case status distribution: pass. I reproduced the stated distribution from `validation/results.csv`.

## Fatal/Serious Attacks

1. The CLI `--expected` argument is accepted but ignored. In `validate.py`, `_run_suite()` only receives `suite_path` and `emit_csv`; it never reads or compares the expected CSV. In `main()`, `args.expected`, `args.strict_no_silent_upgrade`, and `args.no_legacy_partial_context_only` are parsed but not used in the suite path. I gave the suite command a deliberately wrong temporary expected CSV and it still exited `0`. This is not a real CLI regression firewall. [serious]

Authors must prove: `--expected` is loaded and every expected status / first-failed predicate mismatch makes the command exit nonzero.

2. The suite CLI test only checks row count and that emitted statuses belong to the allowed set. `tests/test_validate.py` does not assert the 17-case distribution, expected first-failed predicates, diagnostics, or the expected CSV comparison in the CLI suite path. A validator could silently swap multiple case outcomes while staying inside the allowed status enum and this test would still pass. [serious]

Authors must prove: the suite test fails on a single case-level status mismatch, a first-failed-predicate mismatch, and an unexpected `PARTIAL_CONTEXT_ONLY`.

3. The claimed "strict" flags are cosmetic in the current implementation. `--strict-no-silent-upgrade` and `--no-legacy-partial-context-only` do not alter behavior or enforce additional checks. The raw legacy guard works because the function hard-codes it, not because the strict CLI flags are active. [medium]

Authors must prove: either remove the flags from the claim or make them enforceable contract switches with negative tests.

4. `ADMITTED_EXACT` exists as a positive synthetic control. That is acceptable only inside fixtures, but it is rhetorically dangerous: readers may confuse the status name with exact Srivastava reproduction. The PI boundary prevents that overclaim, but the report should continue saying "positive exact control fixture", not "exact Srivastava case". [medium]

Authors must prove: documentation and result tables label `I1_FULL_EXACT_MATCH` as a control fixture, not a material/Srivastava row.

5. The validator is a predicate-state machine, not a schema or source-object validator. It trusts `witness.predicates` booleans; it does not verify row locators, source digests, pair sets, raw sums, normalization formulae, executor traces, or tolerance provenance. This is inside stated scope, but it means the firewall protects fixture transitions only, not evidence authenticity. [medium]

Authors must prove: any future claim beyond fixture-level admission uses separate proof-object validation before invoking these terminal statuses.

## Required Close Language

Allowed:

> X1 closes a fixture-level predicate-state validator with passing pytest regression and observed 17-case distribution.

Not allowed:

> X1 closes a full CLI expected-contract regression firewall.

Not allowed:

> X1 reproduces Srivastava exact `O_s`, validates material rows, runs graph-vs-overlap residual regression, or shows graph beats overlap.

## If I Must Pick One Fatal Error

The one fatal weakness is that `--expected` is not enforced: the suite command can be green against a wrong contract file. That is the exact failure mode a regression firewall is supposed to catch.

Author exit: implement expected-CSV comparison in the suite path, make mismatches exit nonzero, assert the 17 exact case outcomes and first-failed predicates in tests, and add a negative test using a deliberately wrong expected contract.

## Final Recommendation

**Do not close as stated if "fixture-level executed `O_s` baseline-admission regression firewall" implies a failing CLI contract comparator.** Close only under the narrower label:

> fixture-level predicate-state validator with executed pytest coverage and observed 17-case baseline-admission distribution; CLI expected-contract enforcement still missing.

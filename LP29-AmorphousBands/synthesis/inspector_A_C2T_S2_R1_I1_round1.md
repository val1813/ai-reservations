# INSPECTOR Report: A C2T-S2-R1-I1 Round 1

Project: LP29-AmorphousBands  
Input JSON: `current/A/C2T_S2_R1_I1_round1.json`  
Input CSV: `current/A/artifacts/I1_validator_implementation_plan_round1.csv`  
Inspector: independent INSPECTOR  

## Verdict

INSPECTOR PASS WITH WARNING.

This submission is an implementation plan, not an implemented validator. That is consistent with the JSON role and goal:

- `role`: independent implementation-plan designer
- `validator_goal`: Design, but do not implement, an executable baseline-admission validator for O_s witness bundles.

No claim is made that `validation/validate.py` already exists or that a runnable validator has already passed tests. The local project `validation/` directory is absent, so this inspection treats the artifact as a plan-only deliverable and does not run validator mechanics.

## Required Checks

### 1. Plan vs Implemented Validator

PASS.

The JSON and CSV describe future implementation steps targeting `validation/validate.py`, fixtures, tests, and README. They do not present themselves as an already implemented validator.

CSV evidence:

- `I1.1` starts with "Create pure module and CLI entry point"
- `I1.9` and `I1.10` start with "Create fixtures"
- `I1.11` starts with "Parametrize tests"
- `I1.12` starts with "Document emitted statuses"

This is correctly framed as a build plan.

### 2. PARTIAL_CONTEXT_ONLY Handling

PASS WITH WARNING.

The status model correctly removes `PARTIAL_CONTEXT_ONLY` from emitted terminal statuses and places it under `non_emitted_compatibility_statuses`.

The plan also includes:

- diagnostic code `DEPRECATED_PARTIAL_CONTEXT_ONLY`
- implementation step `I1.6` to remove it from emitted terminals
- README documentation for retired handling
- a partial-context decision replacing incomplete context with `BLOCK` and valid source-local context with `CONDITIONAL_CONTEXT_PASS`

Warning: there is a small semantic tension between two passages:

- `implementation_plan.I1.6` says a legacy `PARTIAL_CONTEXT_ONLY` target can map to `CONDITIONAL_CONTEXT_PASS` when F01-F03 pass.
- `partial_context_decision.compatibility_rule` says a legacy payload should emit `BLOCK` unless converted by the caller to `reported_context`.

Both reject `PARTIAL_CONTEXT_ONLY` as an emitted terminal, so this is not a blocking defect. The next implementation should choose one compatibility rule explicitly: either automatic legacy conversion when F01-F03 pass, or strict `BLOCK` until the caller rewrites target_mode to `reported_context`.

### 3. Forbidden Claims

PASS.

The JSON explicitly forbids the required overclaims:

- exact Srivastava O_s reproduced
- material validation
- graph-vs-overlap residual regression
- graph beats overlap
- exact O_s impossible in principle

It also forbids related silent-upgrade claims:

- `CONDITIONAL_CONTEXT_PASS` is exact O_s admission
- numeric closeness alone can promote reported_context to admitted_exact
- executor quality alone can replace digest-bearing trace and required proof objects

### 4. Exact O_s Admission Gates

PASS.

The plan requires F01-F22 before `DIAGNOSED_MISMATCH` or `ADMITTED_EXACT`, and it delays numeric comparison until after the full proof-carrying witness bundle is present. It also states current Srivastava exact O_s remains `BLOCK` until the full witness tuple is supplied.

This prevents source-local context, scalar availability, narrative provenance, numeric closeness, or executor quality from being treated as exact O_s reproduction.

### 5. Deepening Checks

PASS.

`deepening_1` has at least two layers:

1. Immediate consequence: retiring `PARTIAL_CONTEXT_ONLY` creates a two-step ladder, `BLOCK` then `CONDITIONAL_CONTEXT_PASS`.
2. Next consequence: regression tests must assert empty, scalar-only, DOI-only, and legacy partial-context targets remain blocked unless valid reported context exists.

`deepening_2` has at least two layers:

1. Immediate weak premise: not all predicates may be representable as local syntax/internal-consistency checks.
2. Mitigation layer: split adapters into syntax, internal consistency, and executable provenance predicates; missing executable evidence invalidates the field rather than granting a pass.

### 6. CSV Columns and Task Count

PASS.

CSV columns are present and fit an implementation plan:

- `task_id`
- `file_target`
- `implementation_step`
- `depends_on`
- `expected_result`
- `risk`

Task count: 12.

The task count is sufficient for the stated implementation surface: module/CLI, FieldSpec table, JSON pointer extraction, predicate adapters, mode resolution, deprecated status handling, transition guards, comparison logic, A fixtures, oracle fixtures, parametrized tests, and README.

## Mechanical Validation Status

`validation/validate.py` was not run because this round is plan-only and the project `validation/` directory is absent. This is acceptable for I1 Round 1 only if the assigned output was an implementation plan rather than an implemented validator.

If a later round claims implementation completion, INSPECTOR must require:

- runnable `validation/validate.py`
- fixture files under `validation/fixtures/`
- executable tests in `tests/test_validate.py`
- machine-readable outputs proving `PARTIAL_CONTEXT_ONLY` is never emitted
- regression cases for scalar-only, DOI-only, context-only, replay-ready-no-recompute, complete-match, complete-mismatch, narrative-provenance-only, executor-quality-only, and failed structure/pair/sum/normalization variants

## Blocking Issues

None.

## Warnings

1. Clarify legacy `PARTIAL_CONTEXT_ONLY` compatibility semantics before coding. The plan currently contains two acceptable but different behaviors: automatic conversion to `CONDITIONAL_CONTEXT_PASS` when F01-F03 pass, versus strict `BLOCK` unless the caller rewrites the target mode.

--- 投喂下一轮 ---

必须修正（阻断级）:

None.

建议修正（警告级）:

1. Clarify legacy `PARTIAL_CONTEXT_ONLY` handling: choose either automatic conversion to `CONDITIONAL_CONTEXT_PASS` when F01-F03 pass, or strict `BLOCK` unless target_mode is explicitly converted to `reported_context`.

---

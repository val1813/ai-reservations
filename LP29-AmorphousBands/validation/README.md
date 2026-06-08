# O_s baseline-admission regression firewall

This validator implements the LP29-C2T-S2-R1-I1-X1 execution target. It checks proof-carrying payloads against the frozen admission semantics from I1. It does not perform material validation and does not recompute `O_s`.

## API

```python
from validation.validate import validate_payload

result = validate_payload(payload)
```

Required payload keys:

- `payload_id`
- `target_mode`
- `witness`

Executable fixtures use `witness.predicates` for F01-F22 boolean evidence, plus optional `comparison`, `first_failed_predicate_hint`, and `replay_complete` fields.

## Terminal Statuses

Emitted statuses:

- `BLOCK`
- `CONDITIONAL_CONTEXT_PASS`
- `CANDIDATE_EXACT_REPLAY`
- `DIAGNOSED_MISMATCH`
- `ADMITTED_EXACT`

Retired non-emitted status:

- `PARTIAL_CONTEXT_ONLY`

Raw `target_mode == "PARTIAL_CONTEXT_ONLY"` always returns `BLOCK` with `DEPRECATED_PARTIAL_CONTEXT_ONLY` and `migration_required=true`. The validator never silently migrates legacy partial context to `CONDITIONAL_CONTEXT_PASS`; the caller must resubmit as `target_mode == "reported_context"`.

## CLI

Single case:

```powershell
python validation/validate.py --case current/B/fixtures/I1_authoritative_cases_round3.jsonl::I1_FULL_EXACT_MATCH --expect-status ADMITTED_EXACT --expect-first-failed NONE --strict-no-silent-upgrade --no-legacy-partial-context-only
```

Suite:

```powershell
python validation/validate.py --suite current/B/fixtures/I1_authoritative_cases_round3.jsonl --expected current/B/artifacts/I1_regression_command_contract_round3.csv --emit-csv validation/results.csv --strict-no-silent-upgrade --no-legacy-partial-context-only
```

Pytest:

```powershell
python -m pytest tests/test_validate.py
```

## Forbidden Claims

This validator does not establish exact Srivastava `O_s` reproduction, material validation, graph-vs-overlap residual regression, graph beats overlap, or exact-impossible-in-principle claims.

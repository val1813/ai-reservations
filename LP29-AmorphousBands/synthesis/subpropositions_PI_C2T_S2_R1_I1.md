# Subpropositions: LP29-C2T-S2-R1-I1

Date: 2026-06-05

## Extracted Subpropositions

| ID | Subproposition | Status | Next Test |
|----|----------------|--------|-----------|
| LP29-C2T-S2-R1-I1-X1 | An `O_s` baseline-admission firewall becomes real only when `validation/validate.py`, fixtures, expected outputs, tests, and CLI/API contract are implemented and the 17-case regression suite is actually run. | Highest priority next candidate | Implement and run the regression firewall. |
| LP29-C2T-S2-R1-I1-X2 | Legacy `PARTIAL_CONTEXT_ONLY` must be treated as a raw deprecated input sentinel that always returns `BLOCK + DEPRECATED_PARTIAL_CONTEXT_ONLY + migration_required=true`, even when F01-F03 could pass diagnostically. | Implementation-critical subcandidate | Dedicated legacy fixtures must fail any silent upgrade. |
| LP29-C2T-S2-R1-I1-X3 | Current Srivastava exact `O_s` cannot be admitted from summary/citation/context evidence; exact admission requires full F01-F22 plus matching predeclared comparison. | Guard subcandidate | Include current-Srivastava summary and context-only regression cases. |
| LP29-C2T-S2-R1-I1-X4 | CLI and import API must call the same validator core, otherwise batch evidence and library evidence can diverge. | Engineering subcandidate | Test `validate_payload` directly and add CLI smoke check. |

## Priority Rationale

`X1` contains the other three subpropositions as required acceptance conditions. Therefore `X1` should be registered as the next active north star, with `X2-X4` as implementation gates rather than separate competing topics unless `X1` fails.

## Forbidden Expansion

No subproposition permits material validation, exact Srivastava reproduction, graph-vs-overlap residual regression, graph beats overlap, or exact-impossible-in-principle claims.

# Re-escalation: LP29-C2T-S2-R1-I1

Date: 2026-06-05  
North star: LP29-C2T-S2-R1-I1 / executable O_s baseline-admission validator

## Killed or Narrowed Claim

Original stronger claim:

> An executable `O_s` baseline-admission validator has become a real executable gate.

Fatal narrowing:

> `validation/validate.py`, fixtures, expected outputs, tests, and actual regression logs do not yet exist. The current result is an implementation-ready specification, not an executed validator.

## Independent A Draft

A independently re-escalated the claim to an implementation-ready gate contract: I1 has frozen the admission semantics so future implementation cannot silently promote context, DOI, scalar closeness, provenance narrative, or legacy `PARTIAL_CONTEXT_ONLY` into exact admission. The valid product is a state-gate specification with one `validate_payload(payload: dict) -> dict` API, a shared CLI wrapper, fixed terminal statuses, fixtures/expected-results/tests/README requirements, strict `PARTIAL_CONTEXT_ONLY -> BLOCK + DEPRECATED_PARTIAL_CONTEXT_ONLY`, and current Srivastava exact `O_s` retained as `BLOCK`.

## Independent B Draft

B independently re-escalated the claim to an implementation-ready regression firewall specification: the 17 authoritative cases fix evidence-state transitions, terminal statuses, first-failed predicates, and no-silent-upgrade rules. The result can only claim batch/single-case command contract, expected statuses, first-failed predicates, strict no-silent-upgrade, and expected output schema; it cannot claim any fixture, validator, test, or regression command has actually run.

## PI Synthesis

Accepted re-escalated claim:

> LP29-C2T-S2-R1-I1 has produced an implementation-ready `O_s` baseline-admission regression firewall specification. It freezes what a future executable validator must emit for the current 17 evidence classes and prevents silent upgrade from context, citation, scalar closeness, executor narrative, or legacy partial-context input into exact admission. This is not yet an executable validator.

This is at least same-level as the narrowed original claim because the scientific risk in this branch is not only code absence; it is accidental admission semantics drift. The specification-level firewall is the necessary precursor to executable validation, but the next north star must be actual implementation and execution.

## Next North Star Registered

`LP29-C2T-S2-R1-I1-X1 / executed O_s baseline-admission regression firewall`

One-sentence task:

> Implement `validation/validate.py`, JSONL fixtures, expected-output comparison, tests, and README/CLI contract, then run the 17-case regression firewall and preserve current Srivastava exact `O_s = BLOCK`, explicit reported-context `CONDITIONAL_CONTEXT_PASS`, and legacy `PARTIAL_CONTEXT_ONLY -> BLOCK + DEPRECATED_PARTIAL_CONTEXT_ONLY`.

## Forbidden Claims

- validator implemented
- validator passed tests
- regression command executed
- exact Srivastava `O_s` reproduced
- material validation
- graph-vs-overlap residual regression
- graph beats overlap
- exact `O_s` impossible in principle
- context-only equals exact admission
- numeric closeness, DOI, or executor quality is sufficient for exact admission

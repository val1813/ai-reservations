# PI final synthesis: LP29-C2T-S2-R1-I1

Date: 2026-06-05

## Final Status

`LP29-C2T-S2-R1-I1` closes as:

> implementation-ready `O_s` baseline-admission regression firewall specification / validator not implemented / regression not run.

The three AB rounds, inspectors, N=3 reviewer, GATE 1.5, re-escalation, contradiction deepening, and subproposition extraction converge on one bounded result:

> I1 has fixed the state semantics that a future executable validator must preserve, especially no silent upgrade from context, citation, scalar closeness, executor narrative, or legacy `PARTIAL_CONTEXT_ONLY` into exact admission.

## Concrete Products

- A minimal implementation package contract: `current/A/artifacts/I1_minimal_implementation_package_round3.csv`
- B 17-row regression command contract: `current/B/artifacts/I1_regression_command_contract_round3.csv`
- N=3 reviewer acceptance as specification closeout: `synthesis/reviewer_C2T_S2_R1_I1_N3.md`
- Re-escalation: `synthesis/reescalation_PI_C2T_S2_R1_I1.md`
- Contradiction deepening: `synthesis/contradiction_deepening_PI_C2T_S2_R1_I1.md`
- Subpropositions: `synthesis/subpropositions_PI_C2T_S2_R1_I1.md`

## Allowed Claims

- A future validator has a frozen implementation-ready API/CLI/specification target.
- The expected terminal statuses are constrained to `BLOCK`, `CONDITIONAL_CONTEXT_PASS`, `CANDIDATE_EXACT_REPLAY`, `DIAGNOSED_MISMATCH`, and `ADMITTED_EXACT`.
- Legacy raw `PARTIAL_CONTEXT_ONLY` must return `BLOCK + DEPRECATED_PARTIAL_CONTEXT_ONLY + migration_required=true`.
- Current Srivastava exact `O_s` summary evidence remains `BLOCK`.
- Explicit reported-context evidence can reach only `CONDITIONAL_CONTEXT_PASS`, not exact admission.

## Forbidden Claims

- `validation/validate.py` exists.
- validator tests passed.
- regression command executed.
- exact Srivastava `O_s` reproduced.
- material validation.
- graph-vs-overlap residual regression.
- graph beats overlap.
- exact `O_s` impossible in principle.
- context-only, DOI, scalar closeness, executor quality, or provenance narrative is sufficient for exact admission.

## Deepest Contradiction

Evidence semantics cannot be both narrative-flexible and exact-admission-safe. Either `O_s` admission is a deterministic executable transition over proof-carrying evidence, or it remains a prose judgment that can silently upgrade weak evidence into exact admission.

## Next North Star

`LP29-C2T-S2-R1-I1-X1 / executed O_s baseline-admission regression firewall`

Required first action:

> Implement `validation/validate.py`, JSONL fixtures, expected output manifest, tests, and README/CLI contract, then run the 17-case regression firewall and record actual results.

No further prose round can substitute for this implementation step.

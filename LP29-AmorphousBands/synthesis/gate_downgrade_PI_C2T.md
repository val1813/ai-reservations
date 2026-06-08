# LP29-C2T GATE downgrade precondition

Date: 2026-06-04

## Question

Was the current north star refuted such that PI.md §2 condition B requires a forced rescue round before downgrade?

## Decision

No.

The original stronger form "existing sources can produce provenance-complete same-sample rows" was refuted, but C2T's active post-REVIEWER form is an infrastructure/admissibility artifact:

- witness payload schema exists
- gate predicates exist
- expected executor results exist
- A-side OI/Srivastava witness requirements exist
- current candidate rows remain `BLOCK`

REVIEWER Round 3 did not prove the witness-executor approach impossible; it demanded Round 4 infrastructure. Round 4 supplied that infrastructure, and INSPECTOR accepted it with only a corrected expected-result status.

## Result

Do not trigger forced rescue/downgrade.

Proceed to contradiction deepening.

Boundary:
- C2T survives only as witness-executor admissibility infrastructure.
- It does not survive as material validation or joined-table success.

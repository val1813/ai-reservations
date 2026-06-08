# PI synthesis: LP29-C2T Round 2

Date: 2026-06-04

## Inputs

- A: `current/A/C2T_round2.json`
- B: `current/B/C2T_round2.json`
- INSPECTOR A: `synthesis/inspector_A_C2T_round2.md`
- INSPECTOR B: `synthesis/inspector_B_C2T_round2.md`

## Round 2 result

Round 2 converted the Round 1 blocker state into a row-level audit-template design.

A contribution:
- Added OI/Srivastava-side audit fields.
- Downgraded Srivastava provenance where Round 1 was too strong.
- Kept `material_validation_allowed=false`.
- Proposed executable forbidden-rule changes, including namespace splitting for `oi;graph`.

B contribution:
- Added same-sample crosswalk tests.
- Added graph convention lock tests.
- Added forbidden-control row-audit logic for graph/external-label closure.
- Kept synthetic rows diagnostic-only and did not enable material validation.

## INSPECTOR result

Both inspectors returned `WARN`, with no blocking error.

Remaining warnings:
- A template references fixed-density/fixed-pair fields such as `OI_comparison_mode` and `N_pair` provenance, but these fields are not yet fully present in the required audit template.
- B template direction is correct, but the current CSV schema still lacks several execution fields needed for row-by-row mechanical audit.
- Circular leakage is currently blocked by claim boundaries, not eliminated by a passing joined row.

## Claim boundary

Allowed:
- C2T now has a proposed row-level audit-template design.
- The template can guide what data must be collected before validation.

Forbidden:
- No material validation.
- No graph-beats-overlap claim.
- No Srivastava reproduction claim.
- No claim that same-sample closure has been achieved.

## Stop/continue decision

N=2. Minimum exploration requirement is not met, and no hard stop was triggered. Continue to Round 3.

Round 3 should focus on the smallest executable artifact: a merged C2T row-audit template that adds the missing execution fields and makes every row return `PASS`, `WARN`, or `BLOCK` without interpretive handwaving.


# PI synthesis: LP29-C2T-S2 Round 1

Date: 2026-06-04

## Inputs

- A: `current/A/C2T_S2_round1.json`
- B: `current/B/C2T_S2_round1.json`
- INSPECTOR A: `synthesis/inspector_A_C2T_S2_round1.md`
- INSPECTOR B: `synthesis/inspector_B_C2T_S2_round1.md`
- R1 prior intercept: `synthesis/R1_prior_search_C2T_S2.md`

## A/B independence and framework difference

A was literature-first reproducibility audit.

B was proof-carrying execution / reproducible-build attestation.

The frameworks differ and converge on the same boundary.

## Round 1 result

Srivastava 2019 is a valid reported-context baseline, but not yet a reproduced exact `O_s` baseline.

Allowed:
- Use Srivastava 2019 as literature context for reported orbital-overlap/effective-mass relation.
- Use existing `C2_Srivastava_baseline_rows.csv` as reported context rows.

Forbidden:
- No reproduced exact `O_s`.
- No graph-vs-overlap residual validation.
- No material validation.

## Inspector warnings

- A warning: continue, but do not convert failure to retrieve AIP/SI automatically into "impossible to reproduce."
- B warning: do not escalate current blocked payload into "Srivastava `O_s` is impossible in principle."

## R1 prior intercept

No direct same-topic prior-art kill found. Related orbital-overlap literature exists, including Srivastava arXiv and Frontiers 2024 orbital-overlap/tight-binding work, but no public exact reproduction payload was found.

## Breakthrough check

This round is mainly correctness/infrastructure, not a theory breakthrough. It sharpens the difference between reported context and reproduced baseline.

## AHA check

No AHA trigger. The useful direction is operational: build a reproduction blocker table and attempt to recover SI/formula details.

## Next round context

Round 2 should build a row-level `S2_Srivastava_reproduction_blocker_table.csv` and, if possible, attempt a concrete arXiv/PDF/SI extraction path for formula/code/normalization witnesses. Keep all validation claims frozen.

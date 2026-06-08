# GATE -1: LP29-C2T-S2

Date: 2026-06-04

## Current north star

LP29-C2T-S2 / context baseline vs reproduced Srivastava exact `O_s` baseline.

## Proposition A

Srivastava 2019 reported `OI_norm` / effective-mass context is sufficient as the orbital-overlap baseline for LP29-C2T residual validation.

Independent support:
- Srivastava 2019 reports orbital-overlap values and effective-mass context.
- Existing C2 artifacts include `C2_Srivastava_baseline_rows.csv` with reported `OI_norm`.

## Proposition B

Reported context is not sufficient. A valid residual-validation baseline requires exact formula/code, raw overlap sum, normalization rule, pair cutoff, same-structure mapping, and machine-reviewable witness payload.

Independent support:
- C2T witness-executor gates mark Srivastava rows `BLOCK`.
- C2T A-side witness requirements require `OI_comparison_mode`, `OI_raw_sum`, `OI_norm`, `OI_normalization_formula_id`, `pair_cutoff_A`, `pair_density`, `N_pair`, `N_pair_provenance_id`, `structure_id`, and `source_row_id`.
- REVIEWER C2T rejected blocker labels without executable witnesses.

## Q-1 checks

Q-1.1: Does A have independent evidence?

YES. Reported `OI_norm` and effective-mass context exist in prior artifacts and Srivastava 2019 metadata.

Q-1.2: Does B have independent evidence?

YES. Existing C2T executor/witness artifacts and blocker rows show reported context cannot pass the reproduction gate.

Q-1.3: Are A and B mutually incompatible under the same standard?

YES. Under residual-validation baseline standards, reported context is either sufficient or not sufficient. It cannot both be enough and require additional exact reproduction witnesses.

## Verdict

GATE -1 passed.

Proceed to Round 1 A/B.

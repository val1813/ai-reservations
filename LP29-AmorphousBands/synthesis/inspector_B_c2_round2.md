# INSPECTOR Report: B C2 Round 2

Input: `D:\Claude\ai-reservations\LP29-AmorphousBands\current\B\C2_round2.json`

Read:
- `D:\Claude\ai-reservations\ai\INSPECTOR.md`
- `D:\Claude\ai-reservations\LP29-AmorphousBands\synthesis\inspector_B_C2_round1.md`
- `D:\Claude\ai-reservations\LP29-AmorphousBands\current\B\scripts\C2_residual_benchmark.py`
- `D:\Claude\ai-reservations\LP29-AmorphousBands\current\B\artifacts\C2_residual_benchmark_synthetic_rows.csv`
- `D:\Claude\ai-reservations\LP29-AmorphousBands\current\B\artifacts\C2_residual_benchmark_summary.csv`

Scope: protocol and artifact inspection only. No material claim is judged here.

## Mechanical Check

`C2_residual_benchmark.py` was re-run successfully. It regenerated the synthetic rows and summary CSVs and printed `synthetic_only_not_material_validation=True`.

Result: pass.

## Check 1. Graph Convention

Status: pass.

Confirmed from `C2_round2.json` and the script:

- `w_ij` is locked to a nonnegative, dimensionless overlap-capacity unit.
- `A_w[i,j] = A_w[j,i] = w_ij >= 0`, with `A_w[i,i] = 0`.
- Primary Laplacian is the symmetric normalized weighted Laplacian `L_sym`.
- `lambda_2` is defined only from `L_sym` and is dimensionless.
- `L_w = D - A` is only a secondary sensitivity check.
- `rho_A = spectral_radius(A_w / S_w)` is explicitly budget-normalized and dimensionless.
- The direction note for `rho_A` is fixed, with localization caveats already stated.

No convention drift found.

## Check 2. Residualization and Namespace Isolation

Status: pass.

The round-2 pseudocode does the important parts correctly:

- outer folds are split by family;
- baseline models are fit on train folds only;
- `B0_*` and `G1_*` namespaces are separated;
- residualized labels and residualized graph features are not mixed with baseline controls again on the RHS;
- no train+test joint refit is used for residualizers.

The script follows the same pattern for the synthetic benchmark.

## Check 3. Deepening Layers

Status: pass.

`deepening_1_main_isomorphism` and `deepening_2_source_extension` each contain two layers, and both are anchored in the declared framework:

- distributed network reliability / min-cut redundancy;
- error-correcting redundancy / expander-code threshold behavior.

That matches the required deepening structure.

## Check 4. Synthetic Benchmark Boundary

Status: pass.

The synthetic benchmark is explicitly fenced off from material validation:

- the JSON hard-gates synthetic rows out of material tables;
- the script header says it is synthetic-only;
- the CSV includes `synthetic_label_flag=True` and `material_validation_allowed=False`.

This stays within protocol validation and does not overclaim material evidence.

## Check 5. Summary CSV

Status: pass with a null-control note.

The summary matches the expected A-null / B-positive shape:

- `Y_A_null` rows stay near zero or negative in held-out residual R2.
- `Y_B_positive` shows strong positive held-out residual R2 for `G1_lambda2_Lsym` and a smaller positive signal for `G1_attack_gap_lambda2`.
- `G1_rho_A_budget_norm` is not planted in the synthetic B-positive label, so its negative R2 is acceptable as null-control behavior.

The negative `R2` for `rho_A` does not by itself indicate an implementation bug. It only says that this feature is not predictive under the planted synthetic target, which is consistent with the benchmark design.

## Verdict

**PASS with warnings.**

No blocker.

## Warnings

1. `G1_rho_A_budget_norm` is effectively a null control in this benchmark; keep that label explicit so later readers do not misread the negative `R2` as a pipeline failure.
2. Preserve the synthetic-only boundary in later rounds. This artifact validates plumbing and leakage control, not LP29 material physics.

--- 投喂下一步 ---
1. Keep `G1_rho_A_budget_norm` tagged as null-control in any benchmark summary.
2. Next round should build the same-sample external-label join table with provenance and batch/family blocking.

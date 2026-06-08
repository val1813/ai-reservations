# INSPECTOR Report: B C2 Round 3

Input:
- `D:\Claude\ai-reservations\LP29-AmorphousBands\current\B\C2_round3.json`
- `D:\Claude\ai-reservations\LP29-AmorphousBands\current\B\artifacts\C2_graph_feature_rows_synthetic_only.csv`
- `D:\Claude\ai-reservations\LP29-AmorphousBands\current\B\artifacts\C2_material_graph_rows_blocked.csv`

Scope: artifact/data-gate inspection for LP29-C2 Round 3. No literature priority or novelty review is performed here.

## Mechanical Check

No project `validation/` directory was found under `D:\Claude\ai-reservations\LP29-AmorphousBands`, so `validate.py` is not available. I performed the INSPECTOR checks manually against the JSON and CSV artifacts.

## Q1. Quantity / Dimension Check

Status: pass.

Round 3 contains no new dimensional physics formula requiring unit algebra. The graph quantities are explicitly dimensionless:

- `w_ij=max(0,OI_ij/OI_ref)`: dimensionless.
- `L_sym=I-D^{-1/2}A_wD^{-1/2}` and `lambda_2`: dimensionless.
- `rho_A=spectral_radius(A_w/S_w)`: dimensionless after budget normalization.
- `attack_gap_lambda2`: dimensionless difference of graph-damage diagnostics.
- `synthetic_label_flag=true -> material_validation_allowed=false`: boolean gate.

No unit mismatch found.

## Q2. Direction / Sign Check

Status: pass.

The round does not claim a positive material direction. Its only positive synthetic result is framed as a planted diagnostic: `Y_B_positive` shows held-out residual signal for `G1_lambda2_Lsym` and weaker signal for `G1_attack_gap_lambda2`, while `Y_A_null` stays near-zero/negative. The JSON states this is pipeline sanity only and not material physics.

No reversed material conclusion found.

## Q3. Circularity / Synthetic Boundary Check

Status: pass.

I checked all 288 rows in `C2_graph_feature_rows_synthetic_only.csv`.

- Total rows: 288.
- Unique synthetic samples: 144.
- Per-sample rule: exactly two rows per sample, one `Y_A_null_diagnostic` and one `Y_B_positive_diagnostic`.
- Hard-gate anomalies: 0.
- All rows have `synthetic_label_flag=true`.
- All rows have `synthetic_only_not_material_validation=true`.
- All rows have `material_validation_allowed=false`.
- All rows have `is_external_to_graph_proxy=false`.
- All rows have `forbidden_if_graph_generated=true`.
- All rows have `validation_use=software_sanity_only`.
- All rows use `material_id=synthetic_only_not_material` and `label_source_type=diagnostic_synthetic`.

This is synthetic-only/no-material-validation throughout. The synthetic benchmark is not being used as material evidence.

Note: the synthetic CSV does not contain a `graph_feature_ready` column. That is acceptable for this diagnostic table because its material gate is already hard false; `graph_feature_ready` is present and checked in the blocked material table below.

## Q4. Order-of-Magnitude / Benchmark Check

Status: pass with boundary note.

The source benchmark summary still has the expected shape:

- `Y_A_null`: held-out residual R2 values are `-0.070`, `0.013`, and `-0.040`, consistent with null-control behavior.
- `Y_B_positive`: `G1_lambda2_Lsym` has strong planted residual signal (`R2=0.856`, corr `0.927`); `G1_attack_gap_lambda2` is weaker positive (`R2=0.134`); `G1_rho_A_budget_norm` is negative and remains a null-control-like feature.
- The summary includes `synthetic_only_not_material_validation=True` on every row.

These numbers support pipeline sanity only. They do not establish an LP29 material mechanism.

## Q5. Blocked Material Rows

Status: pass.

I checked all 5 rows in `C2_material_graph_rows_blocked.csv`.

- Total blocked rows: 5.
- `graph_feature_ready=false`: 5/5.
- `material_validation_allowed=false`: 5/5.
- Rows with missing blocking reason/status/unblock condition: 0.

Blocked sources and sufficiency:

1. `Jankousky raw structures`: sufficiently blocked. Missing same-sample atomic coordinates, snapshot/window, species/cell, OI inputs, cutoff rule, family key, and audit path/DOI. Graph features cannot be computed from citation/name alone.
2. `Srivastava structures`: sufficiently blocked. Missing structure files matched to Table II/Fig4 rows, executable OI convention, cutoff rule, row-to-structure mapping, and `m_eff` provenance if used.
3. `Furubayashi transport labels`: sufficiently blocked. External labels alone cannot compute graph metrics; same-sample structure join, label value/unit/temperature provenance, independent carrier-density source, family blocking, and forbidden-control audit are missing.
4. `Jankousky plus Furubayashi join`: sufficiently blocked. A cross-source validation row needs a stable material crosswalk, sample comparability, structure-label matching, temperature/carrier-density compatibility, family blocking, and target-leakage audit.
5. `Srivastava plus Furubayashi join`: sufficiently blocked. Same-sample or justified matched `material_id`, executable fixed-density OI rule, `m_eff` provenance, independent label provenance, forbidden-control audit, and held-out family split feasibility are missing.

The blocked table does not smuggle any material validation row through the gate.

## Q6. Deepening / Claim Shrinkage / Alternative Explanation

Status: pass.

Deepening is adequate for this artifact stage:

- `deepening_1_main_isomorphism` has two layers: distributed network reliability and min-cut redundancy.
- `deepening_2_source_extension` has two layers: error-correcting redundancy and expander-code threshold behavior.
- Each layer is explicitly downgraded to a computable hypothesis or interpretation until real/semi-real joined rows exist.

Claim shrinkage relative to Round 2 is appropriate, not problematic: Round 3 narrows from protocol scaffold plus synthetic benchmark to schema-compatible synthetic diagnostic rows and an explicit material blocked table. It preserves the prior warning that synthetic results are not LP29 material evidence.

Alternative explanation is explicitly acknowledged: all `G1_*` metrics may be nonlinear reparameterizations of Srivastava-style orbital overlap unless they show held-out residual power on external labels after `B0_OI_norm` plus controls. Round 3 does not claim this has happened.

Landing check: pass. Round 3 identifies the landing gap and blocks it rather than inventing a validation result. No prior-empty material claim is advanced without a landing calculation.

## Verdict

PASS.

No blocker.

The 288 synthetic rows are all synthetic-only/no material validation. The 5 material candidate rows are all blocked with sufficient reasons. `material_validation_allowed` is false everywhere it appears. `graph_feature_ready` is false for all material blocked rows; the synthetic diagnostic CSV does not carry this column but is hard-gated out by `material_validation_allowed=false`. Round 3 does not treat the synthetic pipeline as material evidence, and the deepening section is adequate for the current non-material, provenance-unblock stage.

--- 投喂下一步 ---
必须修正（阻断级）:
1. 无。

建议修正（警告级）:
1. 下一轮若继续使用 synthetic diagnostic rows，建议给 synthetic CSV 增加显式 `graph_feature_ready=false` 列，避免和 material blocked 表的门禁字段不一致。
2. 下一步应只推进一个可审计真实或半真实 row family：先补 `material_id/structure_id/snapshot_id/family/label_provenance_id` 与 executable OI/graph rules，再允许外部标签进入 residual validation。
---

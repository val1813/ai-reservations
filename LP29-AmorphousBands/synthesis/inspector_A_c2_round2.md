# INSPECTOR Report: A C2 Round 2

Input: `D:\Claude\ai-reservations\LP29-AmorphousBands\current\A\C2_round2.json`
Artifact: `D:\Claude\ai-reservations\LP29-AmorphousBands\current\A\artifacts\C2_join_schema.csv`

Scope: protocol/schema consistency only. This report does not judge mechanism truth.

## Verdict

INSPECTOR result: pass with warnings.

- Blockers: 0
- Warnings: 3

## Check 1: residual-only / raw-label confusion

Pass.

Round 2 separates the baseline label from residual objects:
- `external_label` is distinct from `external_residual`
- `baseline_residual` is reserved for train-fold residualization
- `spectral_radius_resid_s` replaces the Round 1 `rho_resid_s` collision
- `residual_protocol_after_round2` explicitly states the baseline and graph-residual equations

The round also states that no material mechanism claim is being made here, which is the right scope.

## Check 2: forbidden-control list vs target-adjacent leakage

Mostly pass, with a warning.

The schema now blocks obvious leakage channels through `forbidden_when_target` on:
- `deposition_or_generation_method`
- `structure_file_path`
- `pair_cutoff_A`
- `graph_node_rule`
- `graph_edge_rule`
- `edge_weight_definition`
- `carrier_density_m3`
- `baseline_residual`
- `OI_norm` / `OI_raw_sum` when the target is the same OI quantity or transform

This is enough to prevent the main target-adjacent joins, but the rule text is still prose-heavy. Downstream execution will be safer if the next pass normalizes these forbidden conditions into a machine-checkable enum/list.

## Check 3: `C2_join_schema.csv` executability

Pass.

The header is sufficient: `name,type,unit,provenance,namespace,allowed_targets,forbidden_when_target`.
It carries the minimal metadata needed to audit join eligibility and provenance. The namespace split (`sample`, `provenance`, `controls`, `oi`, `graph`, `null`, `residual`, `label`) is usable as-is.

## Check 4: OI_norm fixed-pair vs fixed-density limit

Warning.

Round 2 improves this area by separating:
- `OI_norm`
- `OI_raw_sum`
- `OI_normalization_method`
- `pair_density`

and by stating that exact Srivastava normalization is still missing. But it still does not spell out the fixed-pair vs fixed-density asymptotics as an explicit executable rule. The limit is better guarded, not fully resolved.

## Check 5: same-sample validation status

Still unfinished.

`same_sample_table_rows` is only a schema row, and the row provenance says it is "not same-sample complete until structure/SI and computed O_s/graph residuals are attached". `residual_protocol_after_round2.current_status` also says the acceptance condition is not met.

## Blocking Issues

None.

## Warnings

1. Forbidden-control logic is good enough for the current schema, but the prose form should be normalized next.
2. OI fixed-pair vs fixed-density behavior is not yet written as a direct executable rule.
3. Same-sample validation remains incomplete by explicit declaration.

## Feed To Next Round

--- 投喂下一步 ---

建议下一轮直接补两件事：
1. 给 `OI_norm` / `OI_raw_sum` / `pair_density` 写出可执行的 fixed-pair vs fixed-density 判据。
2. 把至少一条 same-sample row 补成完整记录：`structure_id`, `O_s`, `lambda2_resid_s` or `spectral_radius_resid_s`, `external_label`, `external_residual`, `provenance`.

---

# LP23-R4 Round3 - B路修正版报告

日期：2026-06-03

## 0. 修正目标

本修正版只处理 INSPECTOR_B_R4_round3 指出的循环论证阻断。原报告把 `holdout_error ~= 1.4e-3` 写成 accepted columns 在 held-out channel 上仍有预测力的证据，这是错误的。

原因是脚本中的 `synthetic_residual(d0, specs)` 明确构造为：

```text
synthetic residual = gauge
  + 0.55*local_loop_stencil
  + 1.35*passive_tail_pr
  + deterministic_probe_noise
```

其中 `local_loop_stencil` 和 `passive_tail_pr` 正是 verify 后进入 closure 的 accepted columns。因此原 `holdout_error` 不是独立预测力证据；它只说明当 residual 已由同一组 accepted columns 合成时，最小二乘投影可以在未参与拟合的坐标上恢复该合成模型。

## 1. 选择的修正路径

本项目当前没有外部实验 residual、独立仿真器输出、独立物理响应 component，或任何不由 accepted columns 合成的 holdout residual/component。

因此本轮不声称完成非循环 test。采用要求中的 b) 路径：

```text
verdict = R4_TOOL_NOT_VALIDATED_BY_HOLDOUT
```

并硬停止以下工具主张：

```text
holdout_error is independent prediction-power evidence
holdout_error validates the physical witness checker
```

保留 `holdout_error` 仅作为脚本 smoke-test 诊断值，不再作为独立证据。

## 2. 脚本修正

已修改：

```text
D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\scripts\r4_physical_witness_pipeline.py
```

修正内容：

```text
holdout_independent = false
holdout_evidence_status = not_independent_synthetic_smoke_test_only
synthetic_residual_provenance = synthetic residual = gauge + 0.55*local_loop_stencil + 1.35*passive_tail_pr + deterministic_probe_noise
verdict = R4_TOOL_NOT_VALIDATED_BY_HOLDOUT
```

脚本仍执行 preregistry -> verify -> rank -> train projection -> holdout scoring，但最终判定不再把 holdout scoring 解释为独立验证。

## 3. 复跑输出

命令：

```powershell
python -m py_compile D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\scripts\r4_physical_witness_pipeline.py
python D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\scripts\r4_physical_witness_pipeline.py
```

关键输出：

```json
{
  "accepted_columns": [
    "local_loop_stencil",
    "passive_tail_pr"
  ],
  "blocked_claims": [
    "holdout_error is independent prediction-power evidence",
    "holdout_error validates the physical witness checker"
  ],
  "holdout_error": 0.0014384846096407084,
  "holdout_evidence_status": "not_independent_synthetic_smoke_test_only",
  "holdout_independent": false,
  "oracle_rejected": true,
  "rank": 6,
  "synthetic_residual_provenance": "synthetic residual = gauge + 0.55*local_loop_stencil + 1.35*passive_tail_pr + deterministic_probe_noise",
  "train_residual_norm": 0.0013957664881648368,
  "verdict": "R4_TOOL_NOT_VALIDATED_BY_HOLDOUT"
}
```

`py_compile` 通过。

## 4. 修正版判定

允许保留的结论：

```text
1. 脚本可复跑。
2. oracle_source_challenge 和 future_leak_challenge 被 witness checker 拒绝。
3. verify -> rank -> train projection -> holdout scoring 的程序顺序成立。
4. rank=6, train_residual_norm=0.0013957664881648368, holdout_error=0.0014384846096407084 是合成 smoke test 的数值输出。
```

必须撤回或降级的结论：

```text
1. 不再声称 holdout_error 证明 accepted columns 具有独立预测力。
2. 不再声称 holdout_error 验证 physical witness checker。
3. 不再声称 R4_TOOL_SURVIVES_TOY_PHYSICAL_PIPELINE。
```

最终判定：

```text
R4_TOOL_NOT_VALIDATED_BY_HOLDOUT
```

研究层含义：

```text
R4b 至多保留为 witness-checker 程序骨架和 smoke test；
不能把该 holdout 数值用作真实物理 obstruction、独立预测力或工具有效性证据。
下一步若要恢复工具主张，必须提供不由 accepted columns 合成的 residual/component，
并重新测试 accepted columns 是否仍有预测力。
```

--- INSPECTOR_CHECK_REVISED ---

[循环论证修正] 已承认原 `holdout_error` 不是独立预测力证据，因为 synthetic residual 由 verify 后 accepted 的 `local_loop_stencil` 与 `passive_tail_pr` 合成。

[证据等级修正] 修正版没有构造独立 holdout residual/component；因此不保留非循环 holdout 主张，直接降级为 `R4_TOOL_NOT_VALIDATED_BY_HOLDOUT`。

[脚本输出修正] 脚本现在显式输出 `holdout_independent=false`、`holdout_evidence_status=not_independent_synthetic_smoke_test_only`、`blocked_claims=[...]`，并把最终 `verdict` 设为 `R4_TOOL_NOT_VALIDATED_BY_HOLDOUT`。

[结论] 修正后不再把合成 holdout 当作独立证据。`holdout_error` 仅是 synthetic smoke-test 数值，不能支撑 physical witness checker 有效性或独立预测力。

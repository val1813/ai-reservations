# INSPECTOR_B_R4_round3_recheck

日期：2026-06-03

角色：LP23-R4 Round3 B 修正版 INSPECTOR 复查

范围：严格只检查 B 路修正版是否解决原 `INSPECTOR_B_R4_round3.md` 指出的循环论证阻断；不评价发表价值或先发覆盖；未读取 A 路输出。

输入：
- `current/B/R4_round3_revised.md`
- `scripts/r4_physical_witness_pipeline.py`
- 原阻断：`synthesis/INSPECTOR_B_R4_round3.md`

复跑命令：
```powershell
python -m py_compile D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\scripts\r4_physical_witness_pipeline.py
python D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\scripts\r4_physical_witness_pipeline.py
```

`py_compile` 通过。脚本复跑关键输出：

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

## Q1. 量纲校对

本次复查重点不是重新评价物理发表价值，而是确认修正版是否撤回原循环 holdout 主张。脚本仍为 toy/无量纲数值管线：

- `H(omega)=d+sum_j a_j/(omega+p_j)` 在脚本中作为无量纲 toy passive response；若作物理频率解释，则 `omega` 与 `p_j` 同量纲，`a_j` 为 `[H]*[frequency]`，`d` 为 `[H]`。修正版未把该式提升为外部 SI 物理公式。
- `C_W(P)=span(D0,{g_i})` 中 `D0` 与 accepted columns 都是长度 9 的边向量，列空间对象匹配。
- 训练投影与 holdout error 均使用同型 residual 和 sigma 归一化，输出为无量纲范数。
- 脚本未使用 `exp()`, `sin()`, `log()`, `sinh()` 等需要额外检查无量纲自变量的超越函数。

Q1 结论：未发现新增量纲阻断；与原阻断无关。

## Q2. 符号/方向校对

- passive-real/Stieltjes 样本仍要求 positive poles、nonnegative residues/direct，并检查样本非增。方向与 `H(omega)=d+sum_j a_j/(omega+p_j)` 的单调递减趋势一致。
- `oracle_source_challenge` 复跑仍被拒绝，失败原因为未预注册、oracle/residual-shaped source、future dependence。
- `future_leak_challenge` 复跑仍被拒绝，失败原因为 `future dependence e0 <- e1`。
- accepted columns 仍为 `local_loop_stencil` 与 `passive_tail_pr`，与脚本输出一致。

Q2 结论：未发现符号/方向阻断；与原阻断无关。

## Q3. 循环论证校对

原阻断点：旧 B 路报告把 `holdout_error ~= 1.4e-3` 当作 accepted columns 在 held-out channel 上仍有独立预测力、并验证 physical witness checker 的证据。但脚本中的 residual 明确由同一组 accepted columns 合成：

```text
synthetic residual = gauge + 0.55*local_loop_stencil + 1.35*passive_tail_pr + deterministic_probe_noise
```

修正版处理：

- `current/B/R4_round3_revised.md` 明确承认原 `holdout_error` 不是独立预测力证据。
- 修正版明确说明当前没有不由 accepted columns 合成的独立 holdout residual/component。
- 脚本显式输出 `holdout_independent=false`。
- 脚本显式输出 `holdout_evidence_status=not_independent_synthetic_smoke_test_only`。
- 脚本显式列出 blocked claims：
  - `holdout_error is independent prediction-power evidence`
  - `holdout_error validates the physical witness checker`
- 脚本最终 `verdict` 已降级为 `R4_TOOL_NOT_VALIDATED_BY_HOLDOUT`。

Q3 结论：原循环论证阻断已处理。修正版不再把 synthetic holdout 当作独立证据；`holdout_error` 仅保留为 synthetic smoke-test 诊断值。

## Q4. 量级鸿沟标记

复跑数值：

- `train_residual_norm = 0.0013957664881648368`
- `holdout_error = 0.0014384846096407084`
- 原阈值量级仍为 `5e-3`

这些数值均在 `10^-3` 量级，没有发现 `|N-M|>10` 的量级鸿沟。关键修正不依赖改变数值大小，而是改变证据等级和 verdict。

Q4 结论：未发现量级鸿沟阻断；数值只支持 smoke-test，不支持独立 holdout 证据。

## Q5. 代数验算

复跑与脚本一致：

- incidence matrix、accepted columns、closure rank 流程未改变。
- rank 复跑为 `6`。
- 训练投影仍在 `train_idx=[0..7]` 上拟合。
- holdout scoring 仍在 `holdout_idx=[8]` 上计算。
- `oracle_rejected=true`。
- `train_residual_norm` 与 `holdout_error` 数值与修正版报告一致。

关键代数来源级别：

- residual 来源为脚本 synthetic probe。
- synthetic probe 明确由 `gauge + accepted columns + deterministic_probe_noise` 合成。
- 因此代数验算只能支持脚本可复跑和 smoke-test 自洽，不能支持独立物理 witness 或独立预测力。

Q5 结论：代数与脚本复跑一致；修正版已正确降级数值来源含义。

## Q6. 综合判定

复查问题：

1. 是否复跑脚本：是，`py_compile` 与脚本运行均通过。
2. verdict 是否已降级为 `R4_TOOL_NOT_VALIDATED_BY_HOLDOUT`：是。
3. 是否仍把 synthetic holdout 当独立证据：否。修正版与脚本均明确 `holdout_independent=false`，并把 `holdout_error` 限定为 synthetic smoke-test diagnostic。
4. 是否仍声称 `holdout_error` 验证 physical witness checker：否。该主张已进入 `blocked_claims`。
5. 是否仍声称 `holdout_error` 是 independent prediction-power evidence：否。该主张已进入 `blocked_claims`。
6. 是否解决原循环阻断：是。

最终结论：

```text
✅ INSPECTOR通过
```

允许保留的结论：脚本可复跑；oracle/future-leak challenge 被拒绝；verify -> rank -> train projection -> holdout scoring 的程序顺序成立；`holdout_error` 是 synthetic smoke-test 数值。

不得恢复的结论：`holdout_error` 证明 accepted columns 有独立预测力；`holdout_error` 验证 physical witness checker；`R4_TOOL_SURVIVES_TOY_PHYSICAL_PIPELINE`。

# LP23-R4 Round3 / Final PI 综合

日期：2026-06-03

## 输入

- A 路修正版：`current/A/R4_round3_revised.md`
- B 路修正版：`current/B/R4_round3_revised.md`
- B 路脚本：`scripts/r4_physical_witness_pipeline.py`
- A/B 复查：`synthesis/INSPECTOR_A_R4_round3_recheck.md`、`synthesis/INSPECTOR_B_R4_round3_recheck.md`

## 校对状态

A 路原 Herglotz 量纲阻断已由参考频率 `omega_0` 无量纲化修复，复查通过。

B 路原 holdout 循环阻断已修正：脚本明确输出 `holdout_independent=false`、`holdout_evidence_status=not_independent_synthetic_smoke_test_only`、`verdict=R4_TOOL_NOT_VALIDATED_BY_HOLDOUT`。复查通过。

PI 复跑脚本，当前关键输出：

```text
rank=6
train_residual_norm=0.0013957664881648368
holdout_error=0.0014384846096407084
holdout_independent=false
verdict=R4_TOOL_NOT_VALIDATED_BY_HOLDOUT
```

## 最终判定

**R4 作为新物理/新数学北极星硬停止。**

原因：

1. 在最小 passive/causal linear response 域中，`W_origin/W_causality/W_passivity` 已由 Herglotz、positive-real、passive realization、Kramers-Kronig、passive approximation 等成熟理论覆盖。
2. `W_nonoracle` 只能由预注册、独立校准、blind split、holdout 等成熟实验/统计协议提供，不是新物理原则。
3. B 路可复跑 pipeline 没有给出独立 holdout；synthetic residual 由 accepted columns 合成，因此 holdout error 只能作为 smoke test，不能作为独立预测力证据。
4. 因此 R4 不能支持“protocol-closure obstruction 是新物理自由度发现原则”的声张。

**可降级保留的工具命题：**

LP23-R4t Certified residual-linter / physical witness-validator skeleton。其输出只能是：

```text
ABSORBED
FINITE_LIBRARY_OBSTRUCTION
NONORACLE_FAILED
ILL_POSED
NOT_VALIDATED_BY_HOLDOUT
```

不得输出 `NEW_PHYSICS` 或 `PHYSICAL_OBSTRUCTION_CONFIRMED`。

## AHA / Re-escalation 检查

R4 的推翻过程揭示的更深层矛盾是：

```text
物理合法性证书 != 来源独立性证书
```

这比 R4 更基础，但当前还不能形成新的物理北极星；它更像审稿/方法论规则：任何 residual discovery 必须同时证明 physical admissibility 和 non-oracle provenance。若缺少独立校准/预注册/holdout，所有 residual 类声张都应降级。

暂不注册新的基础物理北极星。注册工具候选 R4t 到项目队列，分数按方法论工具降级。

## 停止条件

N=3，A/B 双路径收敛到同一结论：新物理声张硬停止，工具声张降级。满足 SOP 收尾条件。

## 后续收尾

需要进入 REVIEWER/AUDITOR：检查 R4t 是否仍被现有 model checking / certified software / passive realization tools 覆盖，并把最终知识库合并到共享知识库。

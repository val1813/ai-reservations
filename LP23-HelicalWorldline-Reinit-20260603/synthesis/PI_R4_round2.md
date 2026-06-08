# LP23-R4 Round2 PI 综合

日期：2026-06-03

## 输入

- A 路：`current/A/R4_round2.md`
- B 路：`current/B/R4_round2.md`
- B 路脚本：`scripts/r4_witness_checker_toy.py`
- INSPECTOR：`synthesis/INSPECTOR_A_R4_round2.md`、`synthesis/INSPECTOR_B_R4_round2.md`

## 校对状态

两个 INSPECTOR 均通过。A 路警告：`G_W(P,r)` 只能作为被修正的中间式，后续必须采用 `G_W(P)` / `Verify_P^pre`，不能让 residual 参与候选列或 witness 生成。B 路警告：checker-filtered residual norm `0.8971489604` 与绕过 checker 的 `5.24e-16` 之间约 15 个数量级鸿沟，来自 oracle 准入开关；`oracle.values=residual.copy()` 是构造性 stress test。

## 本轮结论

A 路把先发风险压清：

- “携证书可机检”已被 proof-carrying code / typed assembly / proof-carrying authorization 覆盖。
- 单域 witness 已被 passivity/Herglotz realization、EFT operator basis/redundancy、causal/system identifiability 覆盖。
- R4a 唯一活口是跨域 physical witness checker，且必须强制 `W_origin` 与 `W_nonoracle`。

B 路把 Round1 手写 constrained columns 升级为 toy witness checker：

```text
legal_only:WITNESS_OBSTRUCTION             rank=6 residual_norm=0.8971489604
with_residual_oracle:WITNESS_OBSTRUCTION   rank=6 residual_norm=0.8971489604
algebraic_open_if_oracle_ignored_checks    rank=7 residual_norm=5.240587849e-16
```

oracle column 代数上能吸收 residual，但因 nonlocal support、future dependence、oracle source 被 checker 拒绝，因此未进入 closure。

## PI 判定

R4 未硬停止，但仍未达到物理结论。Round2 只证明了“toy checker 可以阻止 residual-shaped oracle column”，没有证明真实光学/响应/测量协议自然给出这些 checker。

当前活口更窄但仍可执行：

**R4b：physical witness checker。** 先不输入 residual，只从预注册协议生成合法列和 witness；再输入 residual 做投影；最后用 holdout / 独立校准通道检验补列是否有预测力。若 checker 规则是 PI/B 手写或事后调节，R4 判死。

## 停止条件

N=2，未硬停止。按 SOP 继续 Round3。Round3 是关键：若不能把 witness checker 的可信计算基物理化，R4 必须硬停止或 Re-escalation。

## Round3 指令

1. A 路：选择一个最小物理域，优先被动/因果线性响应或 EFT operator closure，判断是否能把 `W_origin/W_nonoracle` 变成成熟证书；若成熟框架已完全覆盖，给出硬停止判据。
2. B 路：把 `r4_witness_checker_toy.py` 升级为 `r4_physical_witness_pipeline.py`，流程必须是：`columns_pre.json`/内置预注册列生成 -> verify -> rank -> residual projection -> holdout check。不能从 residual 生成候选列。
3. PI 判据：若 Round3 仍只靠 toy 手写规则，则 R4 降级；若 pipeline 可复跑且 oracle 被拒绝、合法物理列保留非零 residual，同时有 holdout 预测，则保留为工具命题。

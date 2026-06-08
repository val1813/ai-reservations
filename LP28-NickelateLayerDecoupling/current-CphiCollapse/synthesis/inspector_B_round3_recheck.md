# INSPECTOR 复检报告：B Round 3 revised

复检对象：`current-CphiCollapse/B/round3_revised.json`

边界：仅复检 B Round 3 revised 是否解除上一轮 blocker；未读取 A 输出；不做 PI 综合。

## 总判定：PASS

上一 blocker 是否解除：已解除。

B Round 3 revised 对上一轮阻断点作了实质修复：`Delta_r_pair` 的主判据不再依赖后验 left/right、同号方向或结论有利排序，而是改为方向无关的 `abs(R_oe_left - R_oe_right)` 加预注册 permutation/hierarchical measurement-error-plus-U_miss null。signed residual / same-sign survival 只允许在 `P_oe` extraction 前由 `P_oe/R_oe`-blind 的 deterministic rule 或独立 `X_pre_not_in_B_min` 轴冻结；若未冻结，则明确不得解释 signed direction 或 same-sign patterns。

因此，上一轮 “same-sign Delta_r_pair 方向未预注册，且 same-sign abs(...) 数学不成立” 的 BLOCKER 已充分解除。当前没有新的 BLOCKER。

## 逐项复检

### 1. `Delta_r_pair` 是否不再依赖后验 left/right 或同号解释：PASS

修订稿将 primary test 写为 direction-free `abs(Delta_r_pair)`，并要求 paired permutation 或 hierarchical measurement-error null。`pairing_rule` 明确 pair 选择在 `P_oe` 计算前完成，left/right orientation 必须在 `P_oe` extraction 前按 registry/acquisition order 或独立 `X_pre_not_in_B_min` 冻结；否则 signed direction 不解释。

这足以防止上一轮指出的后验 left/right 排序和 residual-informed same-sign 解释。

### 2. 是否删除/修正 `same-sign abs(...)`：PASS

修订稿不再把 “same-sign abs(Delta_r_pair)” 作为判据。现有表述为：

- 主判据：unsigned `abs(Delta_r_pair)`；
- 可选 signed 判据：仅在预冻结、`P_oe/R_oe`-blind 方向轴存在时使用；
- 未预冻结方向时：只报告 unsigned magnitude 和 null-test p-values。

数学矛盾已修正。

### 3. `P_oe` 括号公式是否修正且量纲自洽：PASS，轻微说明

`INSPECTOR_CHECK` 中公式已修为：

`P_oe = (chi_odd - chi_even) / (sign(S) * max(abs(S), S_floor))`

`denominator_floor_rule` 也定义 effective denominator 为 `sign(S) * max(abs(S), S_floor)`，且 `chi_odd`、`chi_even` 被要求为同一 normal-state susceptibility component、同一预注册窗口。若 `S_floor` 与 `S` 同量纲，则 `P_oe` 与 `R_oe` 均为 dimensionless，量纲自洽。

轻微说明：`observable_definitions.P_oe.formula` 仍写作 `max_abs_floor(chi_odd + chi_even)` 的 shorthand，但后续 denominator rule 与 INSPECTOR_CHECK 已消除括号歧义，不构成 blocker。

### 4. qz/c-axis `B_min` proxy 是否防止同源污染：PASS

修订稿新增明确 leakage guard：qz/c-axis coherence proxy 必须独立采集，或由与 odd/even susceptibility decomposition 分离的预冻结低维 pipeline 产生；不得复用 target-generating susceptibility data、odd/even matrix-element fits、probe-calibration matrices、window tuning 或 residual-informed preprocessing。

同时 protocol failure 条款列明：若 `B_min qz/c-axis coherence proxy` 与 odd/even susceptibility extraction 共享 target-generating information，则协议失败。这已把上一轮 WARNING 提升为执行前硬约束。

### 5. `U_miss` 是否不能事后吸收 residual：PASS

修订稿要求 `U_miss` 来自 residual inspection 前的独立 metrology uncertainty、external covariance estimates 或预注册 sensitivity grid；`U_miss_max`、covariance assumptions、grid endpoints 必须在看到 `R_oe`、`Delta_r_pair` 或 pooled shifts 前冻结，且不得扩大。

超过 frozen `U_miss + epsilon_meas` envelope 的 residual 必须进入 survival 或 gray-zone，不得被事后重命名为 missing-baseline uncertainty。该修复充分。

### 6. batch/sample-quality/probe-calibration controls 是否足够作为执行前要求：PASS

修订稿加入：

- `batch_stratified_control`：within-batch 与 leave-one-batch-out，pilot 至少 2 批，preferred decision 至少 3 批；
- `sample_quality_repeatability_report`：same-batch technical repeat、denominator exclusions vs sample-quality metrics、disorder/dephasing correlations；
- `probe_calibration_blank_or_reference`：blank/reference standard 走 frozen `P_oe` pipeline，报告 calibration drift、matrix asymmetry、window artifacts。

`INSPECTOR_CHECK.assumptions` 也要求这些 controls 被报告；survival claim 还要求 residual 通过 batch 和 negative-control checks。作为执行前要求已经足够。

## 剩余提醒

WARNING：当前 PASS 是协议修复层面的 PASS，不等于经验 no-go 已成立。B revised 仍需真实执行预注册 `B_min` matched-pair residual-annihilation test，并通过 denominator、leakage、batch、sample-quality、probe-calibration 与 `U_miss` 冻结要求，才可产生 collapse/survival/gray-zone 的经验结论。

BLOCKER：无。


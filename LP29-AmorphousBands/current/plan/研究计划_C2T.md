# 研究计划: LP29-C2T

## 目标

构建 provenance-complete external joined table 的最小可执行版本，用于后续检验:

`external_label ~ Srivastava_overlap + B0_controls + G1_graph_features`

在表不存在前，LP29-C2 只保持 protocol artifact 状态。

## Round 1 目标

1. A 路线: 从 Srivastava 2019 与候选 AOS 文献出发，确定 overlap baseline、normalization、sample identity、transport/effective-mass label 的可抽取性。
2. B 路线: 从 graph feature 与 external-label provenance 出发，确定哪些字段能在同一样本闭合，哪些只能 blocked。
3. INSPECTOR 重点: 防止字段偷换、跨样本拼接、synthetic-to-material leakage、forbidden controls 泄漏。
4. 最小落地: 产出 C2T joined-table schema、source inventory、field blocker table。

## 最小字段

沿用 `knowledge_graph/LP29-AmorphousBands_C2_v1_20260604.json` 的 `required_join_fields`。

## 成功/失败判据

- 成功: 至少一组 same-sample rows 满足全部 required fields，并有 DOI/table/figure/SI provenance。
- 失败但有价值: 生成 blocked provenance table，明确每个候选来源缺失哪个字段以及如何补齐。
- 禁止: 用跨样本拼接或 synthetic rows 伪装 material validation。

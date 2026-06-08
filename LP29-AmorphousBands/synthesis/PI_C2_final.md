# PI 最终综合：LP29-C2

日期：2026-06-04

## 结论类型

有边界 / protocol-ready / empirical validation paused。

LP29-C2 没有被击毙，但不能作为材料机制结论推进。当前最诚实的结论是：

> graph spectral features 是否有独立物理内容，已经被压缩为一个可执行的 same-sample residual validation protocol；在 provenance-complete external joined table 出现前，暂停真实材料经验验证。

## 三轮产物

Round 1：

- A：`current/A/C2_round1.json`
- B：`current/B/c2_round1.json`
- PI：`synthesis/PI_c2_round1.md`
- INSPECTOR：A 0/5，B 0/6

Round 2：

- A：`current/A/C2_round2.json`
- B：`current/B/C2_round2.json`
- B artifacts：`C2_round2_synthetic_seed_level.csv`、`C2_round2_external_label_schema.csv`
- PI：`synthesis/PI_c2_round2.md`
- INSPECTOR：A 0/2，B 0/7

Round 3：

- A：`current/A/C2_round3.json`
- B：`current/B/C2_round3.json`
- B artifacts：
  - `current/B/artifacts/C2_round3_synthetic_seed_level.csv`
  - `current/B/artifacts/C2_round3_field_mapping_upgrade_schema.csv`
  - `current/B/artifacts/C2_round3_external_label_schema.csv`
- INSPECTOR：A 0/1，B 0/1

## 核心收敛

A 路线结论：

- Srivastava SI / exact normalization 未取得时，所有 Srivastava reproduction、绝对 overlap 比较、overlap-preserving null、graph-beats-baseline 结论冻结。
- Jankousky 是最接近的 external join 起点；Furubayashi、Jang 仍是候选，缺 per-sample numeric labels、structure/SI mapping 和 provenance-complete rows。
- A 不支持立即启动 empirical residual test。

B 路线结论：

- synthetic benchmark 已加防误用字段：`synthetic_label_flag=true`、`material_validation_allowed=false`。
- B0/G1 namespace 和 external-label schema 已升级。
- synthetic 只能验证软件/残差化/空模型管线，不是材料证据。
- 没有 provenance-complete external joined table 时，暂停 empirical material validation。

## 残留警告

1. External join 仍停留在 candidate-level provenance，不是 same-sample complete。
2. Round3 synthetic CSV 中 `family`、`N`、`edge_count` 还未直接改名为 `B0_batch_or_family`、`B0_finite_size`、`B0_edge_count`；下一次 artifact 应执行该映射。

## 北极星状态

LP29-C2 当前状态：完成三轮探索，结论为有边界。

不允许声称：

- graph spectra 已独立解释 a-In2O3 / AOS 真实输运；
- synthetic benchmark 支持材料机制；
- Srivastava overlap baseline 已被复现；
- graph metrics 已经 beat orbital-overlap baseline。

允许声称：

- 已建立一个可执行的 residual validation protocol；
- 已明确 empirical validation 的最小缺口；
- 已定义防泄漏/防误用 schema 与 synthetic sanity benchmark。

## 下一步

唯一有效下一步是收集或构建 provenance-complete external joined table，最小字段：

- `sample_id`
- `label_provenance_id`
- `structure_or_SI_source`
- `O_s` or exact overlap baseline
- `B0_onsite_variance`
- `B0_carrier_density`
- `B0_mobility_edge_margin`
- `B0_finite_size`
- `B0_batch_or_family`
- `G1_lambda2_Lsym`
- `G1_rho_A_budget_norm`
- `G1_attack_gap_lambda2`
- external Hall/Drude/Wannier/spectral label
- forbidden-control audit

在此表不存在前，LP29-C2 不进入收官发表态，只作为 protocol artifact 暂存。

## REVIEWER 结果

独立 REVIEWER：`synthesis/reviewer_C2_final.md`

建议：拒稿。

PI 处理：采纳其对“发表态/材料机制主张”的拒稿结论，但不击毙 protocol artifact。

理由：

- REVIEWER 未发现直接同题先发，也未提出引用虚构指控。
- 最致命问题是缺 provenance-complete external joined table；这与本 PI 综合的边界一致。
- Srivastava 2019 orbital-overlap baseline 是必须击败/复现的近邻基线；本项目已冻结所有 graph-beats-baseline 与 Srivastava reproduction 声称。

最终状态保持：有边界 / protocol-ready / empirical validation paused。不得投稿为材料物理发现；可作为内部协议里程碑保存。

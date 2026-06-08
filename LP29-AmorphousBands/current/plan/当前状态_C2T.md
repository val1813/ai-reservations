# 当前状态

## 贡献者

{"orcid":"anonymous","github":"anonymous","name":"匿名贡献者；GATE 7 再确认"}

## 启动记录

- 日期: 2026-06-04
- 当前北极星: LP29-C2T / provenance-complete external joined table construction
- 阶段: Phase 启动
- 轮次计数: N=0
- 性质: C2 的经验验证前置产物，不是新材料机制命题

## GATE -1

核心矛盾:

- A: 现有公开文献、本地 PDF/SI、已抽取 C2 artifacts 足以构造 provenance-complete same-sample joined rows。
- B: 现有来源仍不足，只能形成 blocked provenance table，不能进入 material validation。

判定: 通过。二者在同一 `required_join_fields` 标准下互斥。

## 已知硬边界

- 不得声称 graph spectra 已独立解释真实 AOS/a-In2O3 transport。
- 不得把 synthetic benchmark 当作材料证据。
- 不得声称 Srivastava orbital-overlap baseline 已复现。
- 不得在缺 provenance-complete rows 前执行 material validation。

## 下一步指令

读取 C2 knowledge graph 的 `required_join_fields`，建立 C2T joined-table schema 草案，并为每个字段标记 provenance requirement、候选来源与 blocker。

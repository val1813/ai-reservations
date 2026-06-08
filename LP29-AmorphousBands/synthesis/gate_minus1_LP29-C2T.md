# GATE -1: LP29-C2T 核心矛盾结构验证

日期: 2026-06-04

## 当前北极星

LP29-C2T / provenance-complete external joined table construction。

C2T 不是新材料机制命题，而是 C2 的经验验证前置产物：在同一样本行中连接 Srivastava-style overlap baseline、B0 controls、G1 graph features 与外部 Hall/Drude/Wannier/spectral label。

## 命题 A

现有公开文献、本地 PDF/SI、已抽取的 C2 artifacts 足以构造至少一批 provenance-complete same-sample joined rows，满足 knowledge graph 中的 `required_join_fields`，并可进入 residual validation。

独立证据支持:

- `synthesis/PI_C2_final.md` 已列出最小 required fields。
- `knowledge_graph/LP29-AmorphousBands_C2_v1_20260604.json` 已固化 required_join_fields。
- 现有候选来源包括 Srivastava 2019、Jankousky 2026、Furubayashi/Jang 候选数据与 C2 join schema。

## 命题 B

现有公开文献、本地 PDF/SI、已抽取的 C2 artifacts 仍不足以构造 provenance-complete same-sample joined rows；最多只能形成 blocked provenance table，不能进入 material validation。

独立证据支持:

- `current/B/artifacts/C2_material_graph_rows_blocked.csv` 已将材料行标记为 `graph_feature_ready=false` / `material_validation_allowed=false`。
- REVIEWER final 指出缺少 provenance-complete external joined table 是最致命缺口。
- Srivastava exact normalization/SI、同样本 structure-label mapping、外部标签 provenance 仍未闭合。

## Q-1 三问

Q-1.1: 命题 A 是否有独立实验/观测证据支持为真？

YES。存在可抽取字段的候选来源和已建 schema，说明表构造不是空想；至少有部分字段可由现有文献与 artifacts 支撑。

Q-1.2: 命题 B 是否有独立实验/观测证据支持为真？

YES。C2 Round 3 blocked table、REVIEWER final、PI final 均独立指向关键字段尚不完整。

Q-1.3: 命题 A 和命题 B 在逻辑上是否不能同时为真？

YES。在同一 required_fields 标准下，要么至少存在 provenance-complete rows 可进入 residual validation，要么不存在而只能生成 blocked provenance table。二者不能对同一字段标准和同一候选语料同时为真。

## 判定

GATE -1 通过。

C2T 的第一目标是机械地判定 A/B 哪个成立：先建立字段级 provenance schema 与候选来源表，再逐字段填充、阻断或降级。任何缺 provenance 的字段不得进入 material validation。

# PI 综合 C2 Round 2

## 汇合判断

Round 2 把 C2 从概念检验推进成可执行 protocol scaffold。

- A 线完成 `C2_join_schema.csv`，68 行，字段包含 `name,type,unit,provenance,namespace,allowed_targets,forbidden_when_target`。这修复了 Round 1 的 residual/raw-label 混淆，明确 same-sample validation 尚未完成。
- B 线完成 `C2_residual_benchmark.py` 与 synthetic artifacts，并把 `synthetic_only_not_material_validation=True` 写入输出。benchmark 显示 A-null 不产生稳定 graph residual，B-positive 中 `G1_lambda2_Lsym` 可被 pipeline 检出。

## INSPECTOR 状态

两边均 pass with warnings，无阻断。

警告:

1. A: forbidden-control 规则仍偏 prose-heavy，需转成可执行规则；`OI_norm` fixed-pair/fixed-density 极限仍需 executable rule。
2. B: 图约定、train-fold residualization、deepening 已修好；`rho_A` 在 synthetic summary 的负 R2 是 null-control 表现，不是实现故障。

## 当前最坚固结论

C2 现在有两个可复核 artifact:

- `current/A/artifacts/C2_join_schema.csv`
- `current/B/scripts/C2_residual_benchmark.py` + synthetic rows/summary

但真实材料验证仍为 0。下一步必须把 schema 填入 Srivastava/Jankousky 可核字段，至少形成 OI baseline 表和 blocked provenance，而不是继续增加 protocol 文本。

## 下一轮 ≤300字投喂

LP29-C2 Round 3: Round 2 已完成 join schema 与 synthetic residual pipeline；两者均非材料验证。最坚固结论是: 若 graph metrics 要胜出，必须在 `OI_norm + controls` 后对 external labels 有 held-out residual power；synthetic 只证明 pipeline 能区分 A-null/B-positive。Round 3 必须转向真实/半真实数据填表: Srivastava Table II/Fig4 -> OI/m_eff baseline，Jankousky/Furubayashi -> external labels 或明确 blocked provenance。修正 A: forbidden-control prose 转 executable rules；补 OI fixed-density rule。B: 不再扩写协议，优先读取/生成 schema-compatible rows。

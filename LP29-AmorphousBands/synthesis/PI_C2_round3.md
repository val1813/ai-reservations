# PI 综合 C2 Round 3

## 汇合判断

C2 到 Round 3 已完成最小 artifact 化，但仍没有材料验证。

- A 线: `C2_Srivastava_baseline_rows.csv` 填入 4 行 Srivastava baseline；`C2_forbidden_controls_rules.csv` 给出 18 条 forbidden-control 规则；blocked provenance 对 Jankousky/Furubayashi 诚实。
- B 线: `C2_graph_feature_rows_synthetic_only.csv` 288 行全为 synthetic-only；`C2_material_graph_rows_blocked.csv` 5 行全为 blocked，`graph_feature_ready=false`, `material_validation_allowed=false`。

## INSPECTOR 状态

- A Round 3: pass with warnings。4 行 baseline 自洽；rules CSV 可编译；警告是 `forbidden_namespace=oi;graph` 需拆分或执行器支持，且 deepening 机械字段名可能需补。
- B Round 3: pass。synthetic/material 边界守住，无越界。

## 当前结论

LP29-C2 现在只能声称:

> 已建立 OI baseline + graph residual protocol 的最小 artifact scaffold，并证明 synthetic pipeline 能识别 planted graph residual；真实材料行仍全部 blocked，尚无 graph residual power 证据。

## 致命卡点

1. Jankousky raw structures / same-sample QSGW-Wannier-spectral labels 未 joined。
2. Furubayashi external transport labels 尚未 digitized。
3. Srivastava OI baseline 与 LP29 graph features 还未在同一真实样品上同时计算。
4. A deepening 字段可能无法通过后续机械 GATE 1.5，需要补格式。

## 下一步

N=3，必须触发 REVIEWER。若 REVIEWER 不击毙，进入北极星收尾；GATE 1.5 前先补 A Round 3 explicit `deepening_1/deepening_2` 字段格式。

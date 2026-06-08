# PI 综合 Round 3

## 汇合判断

A/B 独立汇合到同一结论：DGF-N4 不能再表述为“已证明质量上界”；它只能表述为一个待检验的约束统计模型。

共同核心：

```text
M0: environment/null visibility model
M1: DGF constrained model with q in [0,1]
```

A 给出 likelihood 骨架；B 给出 q 独立性的投影/rank 判据。

## Round 3 后状态

N=3，达到最低探索轮数，但不能收官为“理论成立”。当前最多可收官为：

> DGF-N4 被重写为 constrained likelihood research program；13.85 microgram 是模型约束边界，不是已证明自然边界。核心桥接 `q_visibility=q_DGF_mass` 未成立。

## 已解决

- 原始“虚 q”错误已清除。
- `clip(V/V_ref)` 被禁止。
- LLR 符号在 A 路径固定：`LLR=2(logL_env-logL_DGF)`，正值支持 environment/null。
- `fold caustic` 被降级为 `fold-type critical endpoint`。

## 未解决阻断

1. M1 逐点 `q_i` 过拟合。
2. `q_visibility=q_DGF_mass` 桥接未成立。
3. B 的 `log(M_cal)` 量纲错误。
4. q 独立性仍为统计检验计划。
5. 最小 LLR 表不完整。

## 突破方向检查

本轮离突破更近，但也明显降级：

- 更近：已有可检验统计框架和数据重分析路线。
- 降级：DGF 的基础物理声张未成立；当前只是可拒绝模型。

声张保真度应继续保持 0.7，不再上调。

## AHA 检查

本轮 AHA：DGF-N4 最稳妥的形态不是“质量上界理论”，而是“约束统计模型 + 桥接假设审判”。

新候选：

> DGF-N4f: 用 Fadel/Bild 16 microgram 数据执行 M0/M1 likelihood 审判；若 M1 需要逐点 q_i 才拟合，则 DGF-N4 降级为经验模型。

## 下一步

按 SOP，Round 3 后必须启动 REVIEWER。REVIEWER 应重点攻击：

- 先发覆盖：GUP-Lindblad、visibility likelihood、microgram cat data 是否已有。
- 声张缩水：是否已从基础理论缩水成统计模型。
- 拒稿点：桥接假设、过拟合、无真实数据、模型不可识别。

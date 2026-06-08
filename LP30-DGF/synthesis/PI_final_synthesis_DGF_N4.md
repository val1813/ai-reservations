# PI 最终综合：DGF-N4 结案

## 汇合判断

结论类型：证伪-降级，转入 DGF-N5。

A 路线把 DGF-N4 写成 `M0_environment_null` vs `M1_DGF_constrained` 的 latent-q likelihood，并明确 `q_visibility=q_DGF_mass` 是 `single_order_parameter_bridge`。这使模型可计算，但也暴露出：若 `q_i` 逐点自由，M1 获得过拟合能力；若桥接不被独立证明，M1 只能是经验 visibility 模型。

B 路线从统计几何和可观测性出发，给出 rank/projection、`S_q`、`T_14_22`、fold-type critical endpoint 等判据。它与 A 互补地指出：只有当 `X_q` 在质量、环境、校准 nuisance 的正交补中稳定非零，`q` 才可能独立。但 B 路线仍缺预注册图/秩/正则强度与完整 bootstrap/null。

INSPECTOR 与 REVIEWER 独立汇合到同一断点：逐点 `q_i` 过拟合 + 未证明 `q_visibility=q_DGF_mass` 桥接。强制挽救轮降低了自由度并修复了部分量纲问题，但没有落地外部 `q_DGF_mass` observable，也没有闭合低秩/图模型的有效自由度和 penalty。

## 被杀死的声张

- “宏观世界本体残缺已被严格物理证明”：未通过 GATE -1。
- “13.85 microgram 是自然质量上界”：未证明，只能作为模型参考边界或待检验尺度。
- “DGF-N4 likelihood 支持 DGF 物理机制”：被逐点 `q_i` 与桥接问题打穿。
- “fold caustic”：降级为 fold-type critical endpoint，除非证明 Jacobian 退化或 density pile-up。

## 保留下来的结果

- `I=(m/m_p)^2` 只能作为低质量近似；全域变量必须独立定义。
- `m(q)=(2m_p/pi)sin(pi q/2)` 是一个可拒绝的 constrained statistical ansatz，而不是已证物理定律。
- 任何后续 DGF 机制声张必须通过跨表征、跨样本、预注册复杂度后的不变量检验。
- DGF-N5 成为当前北极星：跨表征不变量/不可辨识性原则。

## 新北极星任务边界

DGF-N5 Round 1 不能复活 DGF-N4 的强质量上界说法。它必须先回答：

1. 是否存在独立 `q_DGF_mass` observable；
2. 低秩/图模型在预注册后是否仍优于环境 null；
3. fold-type endpoint 是否跨 visibility、质量代理、环境通道或信息几何坐标保持；
4. Fadel/Bild 类数据是否在惩罚化 likelihood 和 out-of-sample 判据下仍支持受限 DGF。

## 终审 caveat

DGF-N4 降级结案不依赖“无先发”证明；先发状态仅为不完整检索未命中 exact `2m_p/pi` / `13.85 microgram` 声张。终审 REVIEWER 未提出“引用虚构”或明确先发冲突指控，因此本轮无需触发额外 WebSearch 验证；后续若 DGF-N5 进入发表级论证，必须重新做完整先发检索。

## 矩阵 tie-break

DGF-N5、DGF-N6、DGF-N8 重算后同为 3.75。按 SOP 深度优先与 Re-escalation 来源，DGF-N5 作为当前北极星；DGF-N6/DGF-N8 不丢弃，而是作为 DGF-N5 Round 1 的核心子攻击面。

## PI 判定

DGF-N4 研究窗口完成：不是证明成功，而是一次有用的证伪-降级。它把原始本体断言重划定为 DGF-N5 的可检验方法论命题。

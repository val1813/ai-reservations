# PI 综合 Round 1

## 汇合判断

A/B 互补，未形成互相推翻。

- A 路径: Anderson/Mott mobility-edge + Drude/Ioffe-Regel。数值复算显示 a-In2O3 参数低端 `k_F l≈1.36`，用 `ΔE≈0.25 eV` 交叉检验为 `0.86-3.46`，说明低端确实贴近 Ioffe-Regel/mobility-edge 边界；高 n 或高 μ 端在金属侧。
- B 路径: weighted In-s hopping graph / percolation。提出 graph threshold 可同步控制 spectral ridge、IPR、level statistics、Drude weight、Hall mobility。

## 当前最坚固结论

LP29 不是“非晶也有 Bloch band”的课题；那是范畴错误。当前可守声张是:

> mobility-edge/Ioffe-Regel 是必要第一判据，但在 `k_F l≈1` 的 a-In2O3 边界区，结构连通阈值可能提供比 `E_F-E_c` 更强的充分判据。

## 致命弱点

1. A 的落地阻断: A 找到 same-sample `k_F l` vs In-s connectivity graph 的空白，但没有给具体数据表/蓝图/落地产物。
2. B 的循环风险: 不能只用 proxy graph 同时生成解释变量和验证 observables。
3. 先发风险: mobility edge、s-like conduction band、a-ZTO band transport 都不是新东西。

## Round 2 摘要

A 必须补落地: 指定同一样品数据源、列名/figure、抽取 `n, μ_H, m*, l, E_F-E_c, activation/T-dependence` 的表格蓝图，并处理 Hall factor/Drude 假设。B 必须补量纲和参数定义，给真实或 toy 结构输入、cutoff、`beta/alpha` 无量纲声明，并避免 proxy graph 自证循环。共同目标: 设计 matched carrier density / matched `E_F-E_c` 的 A-vs-B 判据。

## AHA 检查

本轮有 AHA 候选: "mobility edge 是 In-s weighted graph 的谱投影，而非与网络阈值竞争的独立解释"。暂不注册为更高分北极星，作为 Round 2 的待检验整合假说。

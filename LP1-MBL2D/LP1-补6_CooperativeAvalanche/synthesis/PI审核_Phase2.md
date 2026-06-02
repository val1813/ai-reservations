# PI审核 Phase 2 — CooperativeAvalanche 边界修复

## A/B 对齐结果

Phase 2 没有改变 Phase 1 的主方向，但降低了声张强度。

可保留的主结论：

`Gamma_coop <= (sum_j Gamma_j) [1 + 6 exp(-d_min/zeta_eff)]`

对 badly approximable `beta`、可分离 2D AA 势、单区域亚临界、并且协同定义为“同时/并行参与”时，协同增强为 O(1)，不随 `k` 增长。

## 必须写入正文的边界

1. `zeta` 取值统一为 `zeta_eff`，正文不依赖 `zeta=1` 的乐观估计。
2. WPL 只允许作为最坏 `C<=7` 的边界处理，不能声称 WPL 不热化。
3. avoided crossing 角度降格为旁证。
4. k-core 只提供必要图论条件，不写成量子动力学严格等价。
5. 串行级联不由本题排除。
6. Liouville `beta` 不在本题适用范围内。

## 收官裁决

允许以“有边界”收官。

本题填补的是 LP1-S3 的特定缺口：多个亚临界区域是否能通过同时协同触发雪崩。答案是否定的，但不能推广为“所有多区域传播机制都被排除”。

## 对 LP1 的回填句

可加入综合推导：

> 多亚临界区域的同时协同不会破坏 badly approximable 准周期势的数论保护。ETH-FGR 展开给出一阶交叉项为零、协同至少二阶，几何近邻数有界导致增强因子 `C<=1+6 exp(-d_min/zeta_eff)`，即使在 WPL 最坏边界下也只是 O(1)。该结论不覆盖串行级联、Liouville `beta` 或相边界附近的 Griffiths 尾巴修正。

▶️ 下一步：回填 LP1 综合推导与共享知识库，登记补6为有边界收官。

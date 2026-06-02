# LP7-S1 任务书：Page-Geilker 半经典方程失败边界

生成时间：2026-06-01 20:42

## 所属长命题

LP7：量子力学-广义相对论冲突到统一公式。

## 子命题定位

LP7-S1 不负责证明“引力必须量子化”。本子命题只攻击一个更窄、更可验证的命题：

> Moller-Rosenfeld 型半经典源项方程 `G_{\mu\nu}[g] = 8πG <\hat T_{\mu\nu}>_\psi` 是否能同时兼容量子测量的单次结果、局域质量分布和实验读出的经典引力场？

## 驱动矛盾

命题 A（半经典期望值源项）：

量子物质可保持量子态，时空度规保持经典，并由量子应力能量张量期望值决定：

`G_{\mu\nu}[g] = 8πG <\psi|\hat T_{\mu\nu}|\psi>`

在 Newtonian 极限下，对质量叠加态可写成：

`∇²Φ(x) = 4πG <\psi|\hat ρ(x)|\psi>`

命题 B（单次测量质量分布）：

在一次实验运行中，量子测量给出一个确定分支；宏观质量实际位于该分支对应位置，经典引力读数跟随该分支，而不是跟随所有分支的 ensemble average。

不可同真条件：

若实验装置用随机量子事件选择宏观质量位置，并在同一次运行中读出引力场，则 `expectation-source` 版本预测平均质量分布的引力场；单次测量版本预测所选分支质量分布的引力场。两者在同一次运行的读数上不可同真。

## 文献锚点

| 编号 | 文献 | 用途 |
|---|---|---|
| S1-L1 | Page & Geilker, "Indirect Evidence for Quantum Gravity", PRL 47, 979 (1981), DOI: 10.1103/PhysRevLett.47.979 | 实验/思想实验锚点：半经典期望值源项与单次引力读数冲突 |
| S1-L2 | Kiefer, Padmanabhan & Singh, "A comparison between semiclassical gravity and semiclassical electrodynamics", CQG 8, L185 (1991), DOI: 10.1088/0264-9381/8/8/007 | 半经典引力与半经典电动力学对比，防止错误类比 |
| S1-L3 | Giulini & Kiefer, "Consistency of semiclassical gravity", CQG 12, 403 (1995), DOI: 10.1088/0264-9381/12/2/009 | 一致性边界 |
| S1-L4 | Hu & Matacz, "Back reaction in semiclassical gravity: The Einstein-Langevin equation", PRD 51, 1577 (1995), DOI: 10.1103/PhysRevD.51.1577 | 随机引力/Einstein-Langevin 逃逸路线 |
| S1-L5 | Kafri, Taylor & Milburn, "A classical channel model for gravitational decoherence", NJP 16, 065020 (2014), arXiv:1401.0946 | 经典通道引力不能生成纠缠，给 LP7-S2 连接点 |
| S1-L6 | Kafri, Milburn & Taylor, "Bounds on quantum communication via Newtonian gravity", NJP 17, 015006 (2015), DOI: 10.1088/1367-2630/17/1/015006 | 经典 Newtonian 通道的量子通信边界 |
| S1-L7 | Carney, Stamp & Taylor, "Tabletop experiments for quantum gravity: a user's manual", CQG 36, 034001 (2019), arXiv:1807.11494 | 实验路线综述 |
| S1-L8 | Oppenheim, "A Postquantum Theory of Classical Gravity?", PRX 13, 041040 (2023), DOI: 10.1103/PhysRevX.13.041040 | 重要反例：经典引力不一定等同于 naive expectation-source 方程 |
| S1-L9 | Oppenheim & Weller-Davies, "Covariant path integrals for quantum fields back-reacting on classical space-time", arXiv:2302.07283 | 混合量子-经典协变路径积分；声称经典场不能经由自身生成纠缠 |
| S1-L10 | Terno, "Structure and statistical properties of the semiclassical Einstein equations", arXiv:2412.18213 | 现代边界：把半经典方程解释为 expectation over realizations，可引向 stochastic gravity |

## 反例栏

| 反例 | 影响 |
|---|---|
| Page-Geilker 只排除 naive expectation-source 版本，不排除所有经典引力或所有半经典近似 | LP7-S1 结论必须写成“有边界”，不能写成“已证明引力必须量子化” |
| Einstein-Langevin / stochastic gravity 可把源项涨落纳入经典随机度规 | 需要判断它是否能重现实验单次分支，而不仅是 ensemble statistics |
| Kafri-Taylor-Milburn 经典通道模型保留经典介质但加入 decoherence | 这类模型可逃过 Page-Geilker 的 naive 批评，但预测不能生成纠缠，转入 LP7-S2 |
| Oppenheim postquantum classical gravity 提供一致的量子-经典混合候选 | LP7-S1 必须把“半经典期望值源项失败”和“所有经典引力失败”分开 |

## 最小模型

考虑质量 `M` 在左右两位置 `L/R` 的宏观配置，由量子随机事件选择：

`|\psi> = (|L> + |R>)/sqrt(2)`

naive 半经典 Newtonian 源项给出：

`ρ_sc(x) = 1/2 ρ_L(x) + 1/2 ρ_R(x)`

因此：

`Φ_sc = 1/2 Φ_L + 1/2 Φ_R`

单次分支读数给出：

`Φ_run = Φ_L` 或 `Φ_R`

可观测差异：

`ΔΦ_branch = Φ_run - Φ_sc = ±(Φ_L - Φ_R)/2`

LP7-S1 的最小验证就是判断 Page-Geilker 类型装置是否测量了 `Φ_run` 而不是 `Φ_sc`，以及现代逃逸路线如何改写上述三行。

## 本 Phase 任务

### P1：方程边界

写出 `G_{\mu\nu}=8πG<T_{\mu\nu}>` 与 Newtonian 极限 `∇²Φ=4πG<ρ>` 的适用条件，标注它作为有效近似时不应跨越的 measurement branch 边界。

### P2：Page-Geilker 逻辑复原

把 Page-Geilker 的实验逻辑抽象成三段：

1. 量子随机事件选择宏观质量配置。
2. naive 半经典源项预测 ensemble-average 引力场。
3. 实际读数跟随单一宏观配置。

输出必须区分：实验事实、理论解释、后续争议。

### P3：逃逸路线分类

至少列 4 类：

1. collapse 后源项：`<T>` 在测量后按分支更新。
2. stochastic gravity：经典度规带噪声，源项包含涨落。
3. classical-channel gravity：引力作为测量-反馈通道，伴随退相干。
4. postquantum classical gravity：更一般的完全正量子-经典混合动力学。

### P4：最小判据矩阵

定义 `J_PG[model]`：

| 模型 | 单次分支读数 | ensemble 平均 | 是否生成纠缠 | 是否保留经典度规 | 与 Page-Geilker 冲突 |
|---|---|---|---|---|---|

先填定性值，数值实验放后续。

### P5：结论类型

LP7-S1 允许的结论只有四类：

- 已解决：naive expectation-source 半经典方程被边界化，矛盾转入更一般混合理论。
- 有边界：某些经典/半经典模型失败，另一些仍存活。
- 证伪：Page-Geilker 不构成有效约束。
- 不可达：缺少关键实验或文献。

当前预期：**有边界**。

## 输出文件

- `current/A/LP7-S1_phase1.md`：正规推导。
- `current/B/LP7-S1_independent_check.md`：独立检查任务书或后续 B 推导。
- `current/plan/LP7-S1_integration.md`：PI 整合与 GATE 检查。

## 下一步

▶️ 下一步：执行 LP7-S1 的 A 正规推导，先完成 Page-Geilker 最小模型与逃逸路线分类。

# LP7-S2 任务书：BMV 局域纠缠见证边界

生成时间：2026-06-01

## 所属长命题

LP7：量子力学-广义相对论冲突到统一公式。

## 子命题定位

LP7-S2 不负责证明“引力必须量子化”。
它只处理更窄的命题：

> 在 BMV 类实验中，若两个量子探针通过局域引力媒介产生纠缠，那么这个媒介在什么假设下必须非经典？哪些“经典但非局域可层析”的模型仍可逃逸？

## 驱动矛盾

命题 A（局域经典媒介）：

引力可以保持经典，只要它作为局域媒介，把两个探针的相位相关性串起来；若再叠加适当退相干或测量反馈，则可避免把引力本身量子化。

命题 B（BMV 纠缠见证）：

若两个量子系统仅通过一个局域媒介相互作用，却产生可验证纠缠，则该媒介至少不能是“局域、可完全经典层析、并满足常规复制/分解规则”的对象。

不可同真条件：

若同时假设局域性、local tomography、无直接探针-探针耦合、以及标准纠缠见证，那么“经典媒介”与“纠缠生成”不能同时成立。

## 文献锚点

| 编号 | 文献 | 用途 |
|---|---|---|
| S2-L1 | Marletto & Vedral 2017 | BMV 逻辑主线 |
| S2-L2 | Marletto & Vedral 2025 RMP | 综述入口，实验可及性与判据总框架 |
| S2-L3 | Di Pietra et al. 2024/2025 | locality 假设边界 |
| S2-L4 | Vidal et al. 2025 | 反例：无 observable spacetime superpositions 也可生成纠缠 |
| S2-L5 | Weber & Vedral 2024 | 相对论参考系一致性 |

## 反例栏

| 反例 | 影响 |
|---|---|
| local tomography 失效 | BMV 不能直接推出“标准量子时空” |
| classical mediator + non-local-tomographic coupling | 可在不显式时空叠加的情况下生成纠缠 |
| frame dependence / accelerated frames | 需区分惯性系与加速系的推论强度 |
| 仅有纠缠而无 mediator tomography | 不能把所有非经典性都归到“引力量子化” |

## 最小模型

考虑两个量子探针 `A,B` 和一个中介 `M`。

如果 `M` 只允许局域耦合：

`H = H_A + H_B + H_M + H_{AM} + H_{MB}`

且 `M` 满足 local tomography，那么任何由 `M` 诱导的可验证纠缠都可视为“媒介非经典”的证据。

但若 `M` 不满足 local tomography，则即使 `M` 在经典基底上没有可观测叠加，也可能通过非局域可层析耦合生成纠缠。

## 本 Phase 任务

### P1：假设表

把 BMV 推论所需假设拆成：

1. 局域性
2. 无直接探针-探针耦合
3. local tomography
4. 经典/非经典媒介定义
5. 参考系一致性

### P2：最小判据矩阵

定义 `J_BMV[model]`：

| 模型 | local tomography | 可生成纠缠 | 是否可直接推出“量子时空” | 备注 |
|---|---|---|---|---|

先填定性值。

### P3：反例分类

至少列出三类逃逸：

1. non-local-tomographic classical mediator
2. partially quantum mediator / rebit-like hybrid
3. frame-dependent or accelerated-frame loophole

### P4：结论类型

LP7-S2 允许的结论只有四类：

- 已解决
- 有边界
- 证伪
- 不可达

当前预期：**有边界**。

## 输出文件

- `current/A/LP7-S2_phase1.md`
- `current/B/LP7-S2_independent_check.md`
- `current/plan/LP7-S2_integration.md`

## 下一步

▶️ 下一步：执行 LP7-S2 的 A 正规推导，先完成假设表和 `J_BMV` 判据矩阵。


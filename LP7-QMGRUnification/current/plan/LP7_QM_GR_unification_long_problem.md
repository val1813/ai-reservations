# LP7 长命题草案：量子力学-广义相对论冲突到统一公式

生成时间：2026-06-01 20:42:13

## 用户长命题

找到量子力学和广义相对论的一个矛盾，从而研究统一公式，能解释两个领域。

## SOP执行状态

- `D:\Claude\ai-reservations\AGENTS.md` 缺失，已按全局路由回退读取 `ai\CLAUDE.md` 与本项目 `README.md/current/plan` 状态文件。
- 现有 `IND_quantum-relativity-unification` 项目为已关闭项目，`current` 是 v13 半起步版本；本文件不覆盖 v13，而是登记新的上层长命题 LP7。
- 已使用 MCP 多源检索：arXiv、CrossRef、Semantic Scholar、OpenAlex。

## 多源检索摘要

### 主线 A：半经典/经典引力与量子测量的张力

核心文献：

| 编号 | 文献 | 检索来源 | 作用 |
|---|---|---|---|
| LP7-L1 | Page & Geilker, "Indirect Evidence for Quantum Gravity", PRL 47, 979 (1981), DOI: 10.1103/PhysRevLett.47.979 | CrossRef | 半经典引力 `G_{\mu\nu}=8πG <T_{\mu\nu}>` 与量子测量结果之间的实验性张力锚点 |
| LP7-L2 | Kent, "Simple Refutation of the Eppley-Hannah argument", CQG 35, 245008 (2018), arXiv:1807.08708 | arXiv/CrossRef | 说明旧的 Eppley-Hannah 必然量子化论证不能直接作为无条件矛盾 |
| LP7-L3 | Mattingly, "Why Eppley and Hannah's Experiment Isn't", PRD 73, 064025 (2006), arXiv:gr-qc/0601127 | arXiv | 反例栏：Eppley-Hannah 装置物理不可实现，不能作为强主线 |
| LP7-L4 | Marletto & Vedral, "Why we need to quantise everything, including gravity", npj Quantum Information 3, 29 (2017), DOI: 10.1038/s41534-017-0028-0 | CrossRef | 信息论版本：若局域介质能在两个量子系统间生成纠缠，则该介质必须非经典 |
| LP7-L5 | Marletto & Vedral, "Quantum-information methods for quantum gravity laboratory-based tests", RMP 97, 015006 (2025), DOI: 10.1103/RevModPhys.97.015006 | CrossRef | 2025 综述级入口，适合作为实验可及性和 BMV 路线总引用 |
| LP7-L6 | Di Pietra, Vedral, Marletto, "On the Role of Locality in the Bose-Marletto-Vedral Effect", arXiv:2411.01285 | arXiv | BMV 证据链的局域性假设边界 |
| LP7-L7 | Vidal et al., "BMV experiment without observable spacetime superpositions", arXiv:2506.21122 | arXiv | 反例栏：纠缠见证并不必然要求可观测时空叠加，需区分"非经典引力"与"量子时空" |

### 主线 B：黑洞信息悖论

核心文献：

| 编号 | 文献 | 检索来源 | 作用 |
|---|---|---|---|
| LP7-L8 | Ydri, "Hawking radiation, the information paradox, and black hole thermodynamics", IOP book chapter (2017/2025 editions) | CrossRef | 黑洞信息悖论综述入口 |
| LP7-L9 | Adami, "Paradox No More...", arXiv:2502.05642 | arXiv | 反例栏：有作者声称通过受激辐射修复经典信息损失，需审慎查重 |

### 主线 C：因果集/离散时空传播子统一接口

本项目 v7-v13 已有工作基础：传播子、d'Alembertian、detector response、判据矩阵 `J_ij[D,J]`。该路线不直接回答最上层冲突，但可作为“统一公式”的候选技术底座之一。

## 最小验证

### 验证目标

不尝试直接构造终极统一公式；先把“矛盾”压缩为可判别命题：

> 若引力场保持经典且只通过局域经典自由度与量子物质相互作用，它能否在不引入非经典自由度的情况下，同时满足量子测量一致性、局域性、无超光速信号、以及可生成/不可生成纠缠的实验判据？

### 判定

- Eppley-Hannah 型“必然量子化”不是稳固主矛盾，因为 Mattingly 2006 与 Kent 2018 给出强反驳。
- Page-Geilker 型半经典方程张力更适合做第一子命题：它直接攻击 `G_{\mu\nu}=8πG <T_{\mu\nu}>` 与测量后单一结果的兼容性。
- BMV/Marletto-Vedral 型纠缠见证更适合做第二子命题：它给出实验可及的判据，但必须把结论限定为“引力介质非经典”，不能未经证明上升为“时空几何必然有可观测叠加”。
- 黑洞信息悖论是更高能/强引力路线，适合作为平行长命题分支，不应与实验室 BMV 路线混写为同一最小验证。

## 驱动矛盾候选

### LP7-核心矛盾

命题 A（经典/半经典引力）：时空几何可保持经典，曲率由量子物质的期望值或局域经典变量决定。

命题 B（量子测量/纠缠）：量子物质存在单次测量结果与可验证纠缠；若引力能在局域相互作用下生成纠缠，介质不能是完全经典的信息载体。

不可同真条件：在明确的局域性、测量更新规则和可观测 detector response 假设下，若经典引力模型无法同时给出单次结果、无超光速信号和 BMV 纠缠相位，则 A 与 B 不可同真。

## 拆解为子命题

| 子命题 | 标题 | 目标 | 最小验证 | 状态 |
|---|---|---|---|---|
| LP7-S1 | Page-Geilker 半经典方程失败边界 | 判定 `G_{\mu\nu}=8πG <T_{\mu\nu}>` 在测量诱导质量分布中的失败是否构成严格矛盾 | 复现 Page-Geilker 逻辑；列出所有现代半经典逃逸路线 | 待认领 |
| LP7-S2 | BMV 局域纠缠见证 | 判定“局域引力介质生成纠缠 => 引力非经典”的假设集合和反例边界 | 用 Marletto-Vedral 2017/2025 与 2024/2025 反例文献建立假设表 | 进行中-LP7-S2_BMV_locality_boundary |
| LP7-S3 | 经典-量子混合动力学 no-go 边界 | 找出哪些 hybrid classical-quantum dynamics 真正矛盾，哪些只是模型受限 | 搜索 Hall-Reginatto、Kafri-Taylor-Milburn、Oppenheim 等混合理论；分类保正性、局域性、能量守恒 | 待认领 |
| LP7-S4 | 黑洞信息悖论作为强引力统一判据 | 判断信息守恒、半经典 Hawking 辐射和广义协变性是否能形成独立矛盾 | 建立 Page curve / island / stimulated emission 反例栏 | 待认领 |
| LP7-S5 | 统一公式候选的判据矩阵 | 不提出玄学公式，而定义候选统一公式必须满足的最小公理与可观测判据 | 以 detector response、纠缠见证、半经典极限、GR 极限构造 `J_unify` | 进行中-LP7-S5_unified_formula_criterion_matrix |
| LP7-S6 | 因果集传播子路线对接 | 评估现有 v7-v13 因果集 `J_ij[D,J]` 是否能作为 LP7-S5 的一个实现 | 把 v13 5传播子矩阵映射到 BMV/Page-Geilker 的 detector observable | 待认领 |

## 反例栏

| 反例/风险 | 来源 | 影响 |
|---|---|---|
| Eppley-Hannah 思想实验不可实现或论证失效 | Mattingly 2006; Kent 2018 | 不得把 Eppley-Hannah 作为主矛盾 |
| BMV 见证依赖局域性和介质假设 | Di Pietra et al. 2024 | LP7-S2 必须显式列假设，不得直接推出“量子时空” |
| 非局域层析/后量子玩具模型可生成纠缠 | Vidal et al. 2025 | “非经典”与“标准量子场”之间存在中间理论空间 |
| 黑洞信息悖论已有 island/Page curve 等大量候选解决方案 | 近年综述与 arXiv | LP7-S4 需做查重，避免重复造轮子 |

## 建议下一步

▶️ 下一步：若继续推进，转入 LP7-S6 因果集传播子路线对接。

# AHA记录 — MIPT-NoPostselect (LP8-S1)

> 触发条件见 ai/AHA.md / CLAUDE.md第三节。

（暂无 — v1初始化）

---

## AHA #1 — Phase1（触发条件2：B博士独立推出与A不同框架但同样成立的路径）

**触发：** PI.md 检查点C1 + CLAUDE.md第三节条件2。A博士（统计场论replica + stabilizer数值）与B博士（信息论信道容量 + 贝叶斯BBP/KS可检测阈值）用**零中间重叠**的两条路径，独立到达同一结论：1+1D无对称投影Clifford/Haar下 p_c^learn=p_c^purif=p_c^ent，且结构化情形分离。

**AHA内容：** 两条路径在"为什么重合"上给出**互为翻译但形式不同**的机制：
- A：退火型(learnability) 与 淬火型(纠缠) 的自由能率函数在 replica n→1 单不动点处共享非解析点（Jensen gap=0）。
- B：监测电路=随机量子纠错码，无对称→码的可恢复性谱在阈值处是"全有全无"台阶（信道各向同性）→保护单qubit(purification/learnability)与保护extensive信息(entanglement)同阈值。

两者都把"learnability=entanglement"的实质内容压到同一个物理点：**纯化相变=纠缠相变**（这一步是真正的非平凡内容；learnability=purification 在两条路径里都近乎同义反复）。

**AHA评级：** ~~🔥~~ → **降级为 ⚠️候选（BLINDSPOT 2026-06-02）**。BLINDSPOT扫描判定"双独立路径汇合"**虚高**：两路径承载新奇性的唯一节点都是 purification=entanglement，且都进口同一 Gullans-Huse 前提；"零重叠"只在平凡步(learnability=purification)与共引文献层成立；真正独立的部分(分离充要条件)反而**冲突**。故这不是合格的AHA汇合，而是共享输入造成的外观。保留为待激活候选：**若卡点BS-1(独立重证purification=ent)闭合，则AHA升级回🔥真实双路径**。

**跨LP连接（math_object重叠）：** "monitored-circuit-as-random-code"与"通道层(Lindbladian/退火) vs 轨迹层(postselected/淬火)二分"——与 LP-4 NHSE 的 Stinespring/Lindbladian-vs-postselected 统一母框架是同一数学结构。📌 记入未追问问题池：LP-4 的方向反转相变 是否对应 LP8 的退火-淬火劈裂？（跨长命题候选连接，收官时写入knowledge_graph）

**处理（CLAUDE.md AHA处理规则）：** AHA一致于当前北极星 → 下一Phase以"判据等价性(LP8S1-K1)"为核心目标。这正是命题A vs 命题B 裁决的关键。

## 📌 AHA追问队列
- 📌1：Jensen gap=0 ⟺ 信道各向同性？（=卡点LP8S1-K1，Phase2核心）
- 📌2：LP-4方向反转相变 ↔ LP8退火-淬火劈裂 是否同源？（跨LP，收官时判断真假）

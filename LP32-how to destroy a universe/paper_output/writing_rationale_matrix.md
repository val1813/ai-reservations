# Writing Rationale Matrix

> 为论文每个section/段落记录: 功能 + 服务motivation + 范文参考 + 证据 + 检查

---

## Abstract
**功能**: 一句话定位(field-level), 结果陈述, 方法精髓, 应用范围
**服务Motivation**: Q2(Novelty) — 清晰区分前人与我们
**证据**: 主定理 + 碰撞模型
**检查**: ≤250词, 含非平凡条件($q_S < q_E$)

---

## I. Introduction

### P1: Broad opening → specific landscape
**功能**: 从open quantum systems → NM backflow → 已有检测/表征/分类工具
**服务Motivation**: Q1(Relevance) — 让PRA读者理解这是领域核心问题
**范文参考**: 标准PRA intro结构 (broad→narrow→gap)
**证据**: BLP(2009) + RHP(2010) + MSV(2021) + Buscemi(2025)
**检查**: 引用顺序 BLP→RHP→MSV→Buscemi, 逻辑递进

### P2: Gap statement → our contribution
**功能**: MSV的局限(tomography) → 我们的差异(projective only) → 独立价值
**服务Motivation**: Q2(Novelty) — "前人做了什么, 我们做了什么不同的"
**证据**: MSV需要$\varrho_{SE}$重建 vs 我们只需$q_S$, $q_E$
**检查**: 不说是MSV的"补充", 先讲独立价值

### P3: Method preview
**功能**: 物理假设(einselection + finite capacity) → 结果($\mathcal{R} \leq q_S/q_E$) → 方法(counting)
**服务Motivation**: Q3(Trust) — 预告证明是组合计数
**证据**: 单句概括假设和结果
**检查**: 不提前展开model细节

---

## II. Model

### II.A: Einselection (先物理机制)
**功能**: 建立pointer basis的量子力学起源
**服务Motivation**: Q3(Trust) — 解释为什么binary basis是物理的而非假设的
**证据**: Zurek(2003) + Eq.(1)
**检查**: 不提前用"finite capacity"语言

### II.B: Binary capacity (推论)
**功能**: 从einselection推出finite capacity — 逻辑是"物理机制→推论"
**服务Motivation**: Q3(Trust) — 每个qubit≤1bit不是因为假设, 是因为einselection
**证据**: Pointer basis只有两个正交态
**检查**: 明确说"this is a consequence of einselection, not an additional postulate"

### II.C: Forward transfer
**功能**: 操作定义$L_{S\to E}$ + energy asymmetry justification
**服务Motivation**: Q3(Trust) — 为什么没有$|0\rangle\langle 1|$项
**证据**: Eq.(2) + $\Delta E \gg k_B T$论证 + Jaynes-Cummings (SM)
**检查**: 能量论证在主文, 完整推导在SM

---

## III. Bound on Capacity-Normalized Backflow

### III.A: Definitions
**功能**: 操作定义$q_S$, $q_E$, $C_F$, $N_{\rm back}$, $\mathcal{R}$
**服务Motivation**: Q4(Reuse) — 每个量有操作定义, 可复现
**证据**: Projective measurement定义 + capacity vs actual fraction讨论
**检查**: $\mathcal{R}$物理意义正面陈述(\mathcal{R}=1→饱和)

### III.B: Theorem and proof
**功能**: 核心定理 + 组合证明
**服务Motivation**: Q3(Trust) — 证明完整可追溯
**证据**: Pigeonhole principle + 单次toggle约束
**检查**: 整数count(floor/ceil) + ensemble average说明

### III.C: Domain and non-triviality
**功能**: 明确什么时候bound有用
**服务Motivation**: Q5(Meaning) — 诚实讨论边界
**证据**: $q_S < q_E$条件 + $N_S \ll N_E$极限
**检查**: $q_E=0$的undefined情况处理

### III.D: $T_1$ correction
**功能**: 处理$|1\rangle \to |0\rangle$ relaxation的修正
**服务Motivation**: Q5(Meaning) — 实验可实现性
**证据**: $\delta \sim \tau_{\rm prot}/T_1$参数化
**检查**: Correction是加性而非乘性

---

## IV. Relation to Prior Work
**功能**: 系统对比本bound与已有NM框架
**服务Motivation**: Q2(Novelty) — 位置在landscape中
**证据**: BLP/RHP/MSV/Buscemi逐一对比
**检查**: Buscemi说明是"orthogonal question"

---

## V. Illustration
**功能**: 具体数值例 + 图示 + 物理直觉
**服务Motivation**: Q4(Reuse) + Q1(Relevance)
**证据**: Table 1 (7行) + Figure 1 (bound curves)
**检查**: 图由Python生成, 数值与正文一致

---

## VI. Discussion
**功能**: 为什么classical counting约束quantum system + 局限 + 展望
**服务Motivation**: Q5(Meaning)
**证据**: Einselection的quantum origin + 三类violation解释 + 双向扩展
**检查**: 结尾不weak ("future work"具体化)

---

## VII. Conclusion
**功能**: 总结核心结果 + 物理意义
**服务Motivation**: Q1(Relevance) — 最后一句话连接information capacity→observable consequences
**检查**: ≤1段, 不复述discussion

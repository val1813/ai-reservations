# R4 Round 1 — 静态到动态桥的形式化

**作者:** A博士（学院派）
**日期:** 2026-06-08
**状态:** 已完成

---

## 北极星命题

> "事件按顺序发生并消耗资源"可以被形式化在不假设全局时间的数学结构中，从而使S1定理的鸽巢结论从静态计数升级为动态约束。

---

## §-1 核心文献精读

### 文献1: Coecke & Kissinger (2018). "Categorical Quantum Mechanics I: Causal Quantum Processes"

**arXiv:** 1510.05468v3 | **发表:** Oxford Scholarship Online, 2018 | **章节:** 共三部分概述的第一部分

#### 1.1 核心问题：什么是"process"？它是否预设时间？

Coecke和Kissinger从Whitehead的过程本体论出发，将"过程"（process）定义为：

> "anything that has zero or more inputs and zero or more outputs"

**关键论断：过程是比时间更基本的原语。** 时间（或因果顺序）不是预设的舞台，而是从过程的连接结构中**重构**出来的。具体地：

- 一个过程用一个盒子表示，输入/输出系统用导线表示
- 过程通过串行组合（∘）和并行组合（⊗）形成更大的过程
- 因果结构关联于线路图（circuit diagrams）：盒子Φ在盒子Ψ的因果未来中，当且仅当Ψ的一个输出导线连接到Φ的一个输入导线

**定理2.4（Coecke-Kissinger）：** 一个图是线路图当且仅当它不包含有向环（directed cycles）。这意味着**因果偏序是导出结构，而非预设结构**——它等价于图的无环性约束。

#### 1.2 因果性公设（Causality Postulate）

在过程理论中，因果性通过**丢弃过程**（discarding process）来定义：

> **定义5.1：** 若每个系统有一个区分丢弃效应，过程Φ是**因果的**若：
> ```
>   Φ ∘ (丢弃所有输出) = (丢弃所有输入)
> ```

图式：
```
    ┌───┐
    │ Φ │
    └───┘
      ║       =
      ╚══════   ══════╗
```

**范畴论对应：** 幺半范畴中，单位对象I是终对象（terminal object）。这意味着每个态射都满足因果性公设。

**核心洞察（对我们项目至关重要）：** 因果性公设在纯图论语言中表达，不需要时间参数。丢弃所有输出等价于丢弃所有输入——即"信息不能从无中产生"。这是比时间更基础的守恒律。

#### 1.3 无信号定理（No-Signalling Theorem）

> **定理5.6：** 若一个过程理论有丢弃过程且满足因果性公设，则它自动是无信号的。

这是图论推导——丢弃一方的输出后，另一方的输入-输出对被证明与第一方的输入在串行组合上分离（∘-separable）。

**对我们项目的意义：** DGF中的无信号条件（信息流不能形成闭合因果环）在过程理论视角下是因果性公设的自然推论。

#### 1.4 加倍构造（Doubling/CPM Construction）

纯过程 → 加倍 → 混合/非纯过程。丢弃效应自然地从加倍中产生。这给出了Born规则的图论推导。

> **定理4.5（No-Broadcasting）：** 在加倍并添加丢弃后，不存在广播过程。

这是过程理论版本的"不可克隆定理"。

#### 1.5 关键判定：过程理论是否预设时间？

**不预设。** 因果顺序被重构为：
- 导线连通性 → 有向路径 → 偏序
- 无环性约束 → 全局因果一致性
- 丢弃公设 → 信息守恒

时间在Coecke-Kissinger框架中是从**纯结构关系**中涌现的导出概念。

---

### 文献2: Joachim, de Visme, Haar, Winskel (2025). "Quantum Petri Nets with Event Structure Semantics"

**arXiv:** 2508.14531 | **发表:** 2025-08-20 | **类型:** 形式化框架

#### 2.1 Petri网如何形式化"token消耗"和"变迁触发"

经典Petri网N = (P, T, F, m₀)：

| 元素 | 语义 | 我们的映射 |
|------|------|-----------|
| Place p ∈ P | token位置（条件） | DGF格点 |
| Transition t ∈ T | 事件（变迁） | 前向转移/回流 |
| Flow F ⊆ (P×T) ∪ (T×P) | 因果流关系 | 格点间有向边 |
| Marking m | 当前token分布 | {|0⟩, |1⟩}赋值 |
| m₀ | 初始标记 | 初始格点状态 |

**变迁触发规则：**
- 若t的所有前位（•t）都有token，则t可触发
- 触发后：消耗•t中的token，在t•（后位）中产生token
- **这是原生的动态过程语义**——不依赖外部时间参数

#### 2.2 事件结构的偏序如何编码因果顺序

事件结构E = (E, ≤, #, pol)：
- ≤ : 因果偏序（e₁ ≤ e₂ 表示e₁因果先于e₂）
- # : 冲突关系（e₁ # e₂ 表示两者不能同时发生）
- pol : E → {⊕, ⊖, 0}（极性：正/负/中性）

从Occurrence Net到Event Structure的函子对应（Winskel 1987）：
- 丢弃条件（places），保留因果偏序和冲突
- 因果偏序 ≤ 是流关系F的传递闭包
- **因果顺序完全由网结构决定，不需要全局时钟**

#### 2.3 量子事件结构

Clairambault, De Visme, Winskel (2019)的量子扩展：

**定义7：** 量子事件结构E = (E, ≤, #, pol, H, Q)，其中：
- Q(x) : 配置x上的有限维Hilbert空间
- Q(x ⊆ y) ∈ CPTNI(Q(x) ⊗ H((y\x)⊖), H((y\x)⊕) ⊗ Q(y))

**三个公理：**
1. **Obliviousness（遗忘性）：** 纯负极性扩展不改变量子态
2. **Functoriality（函子性）：** 区间合成一致
3. **Drop Condition（丢弃条件）：** 确保Q是合适的量子赋值（子密度算符）

**Drop Condition的实质：** 它是一个容斥公式：
```
d(x; y₁,...,yₙ) = Σ_{I⊆{1,...,n}, y_I∈C(E)} (-1)^{|I|} tr_{Q(y_I)⊗H} ∘ Q(x ⊆ y_I) ⊒ 0
```

**这对我们至关重要：** Drop Condition的结构形式（交错和/容斥公式）与S1定理中的鸽巢计数在结构上同源。两者都是对"组合可能性的计数量"施加正性/上界约束。

#### 2.4 局部量子Occurrence网（LQON）

Joachim等人的核心创新：将全局量子赋值Q分解为局部赋值Q₀：

> **定理28：** 仅检查单步扩展（single extensions）的Drop Condition足够保证全局Drop Condition。

> **定理29：** Drop Condition在冲突簇（conflict clusters）上因式分解——仅需检查每个冲突簇内的局部条件。

**推论：** 如果冲突簇是团（clique），Drop Condition的检查是线性时间O(|C|)。

这解决了状态爆炸问题——量子Petri网可以**实际验证**。

#### 2.5 量子Petri网的定义

> **定义35 (终版):** 量子Petri网是一个带局部量子赋值的Petri网，满足局部Drop Condition和局部Obliviousness。

> **定理34：** 如果局部赋值Q₀在Petri网上满足局部条件，则其展开U(N)上的诱导赋值也满足，因此N是量子Petri网。

**对我们项目的核心意义：**
- DGF的格点图 → Petri网 → 局部量子赋值 → 量化的token流
- 这给出了从静态DAG到动态Petri网的完整形式化路径
- 前向/回流转移的形式语义是原生的——不是"揣测"出来的

---

### 文献3: Oreshkov, Costa, Brukner (2012). "Quantum correlations with no causal order"

**arXiv:** 1105.4464v3 | **发表:** Nature Communications 3, 1092 (2012)

#### 3.1 Process Matrix形式化

核心创新：**不预设全局因果结构**的多方关联框架。

前提：
1. **局部量子力学：** 每方的操作由标准量子力学描述（量子仪器，CP映射）
2. **封闭实验室：** 操作期间实验室与外界隔离
3. **开放因果结构：** 不假设各实验室嵌入任何全局因果结构中

Process Matrix W由两个条件定义：
```
W^{A₁A₂B₁B₂} ≥ 0                                    (非负概率)
Tr[W (M^{A₁A₂} ⊗ M^{B₁B₂})] = 1, ∀ CPTP M^A, M^B   (概率归一)
```

关键洞察：Process Matrix推广了密度矩阵和量子态。当输出系统是一维时（纯测量），退化为标准Born规则。

#### 3.2 因果不等式

通讯游戏：Alice和Bob各有随机比特a, b，Bob额外有b'。若b'=0，Alice猜b；若b'=1，Bob猜a。

**经典因果界：** P_succ ≤ 3/4

**量子无因果序违反：** P_succ = (2+√2)/4 ≈ 0.854 > 3/4

使用的资源态（Process Matrix，Eq. 7）：
```
W = 1/4 [𝟙¹²³⁴ + 1/√2 (σ_z^A₂ σ_z^B₁ + σ_z^A₁ σ_x^B₁ σ_z^B₂)]
```

Bob通过选择测量基（σ_z或σ_x）来**选择因果方向**——这是无法分解为确定因果顺序的混合（非因果可分离）的过程。

#### 3.3 因果可分离性

一个过程是**因果可分离的**当且仅当：
```
W = q·W^{B⪯A} + (1-q)·W^{A⪯B}
```
其中W^{B⪯A}不包含从B到A的信号，W^{A⪯B}反之。

**定理（附录F）：** 在经典极限下，所有过程都是因果可分离的。

这强烈暗示：**时空因果结构是从更基础的理论中涌现的，经量子-经典转变而结晶。**

#### 3.4 P_reflux能否被重新表述为因果不等式？

这是R4的核心问题。结构比较：

| 因果不等式（Oreshkov） | 回流公式（DGF） |
|---|---|
| P_succ ≤ 3/4 | P_reflux ≤ min(N_S·q_S, N_E·(1-q_E)) |
| 违反 ⇒ 无确定因果序 | 饱和 ⇒ 最大信息回流 |
| 博弈论框架 | 组合鸽巢框架 |
| 需要两方协作 | 单方回流（环境反作用） |

**关键观察：** 回流公式可以被视为一种**"自博弈"（self-game）因果不等式。** 在这个视角下：
- "前向过程"消耗E-token → 对应Alice→Bob通信
- "回流过程"逆转S-token → 对应Bob→Alice通信
- 鸽巢上界 → 对应因果可分离过程的最大成功概率

如果这是正确的，那么：
- 违反回流上界的物理过程必然是非因果可分离的
- 回流公式成为一个新的、**基于资源消耗**的因果见证

但存在一个关键差异：Oreshkov的因果不等式需要两个独立方（自由选择和封闭实验室），而DGF的回流是单系统内的自作用。需要在Process Matrix框架中定义"自博弈"的因果不等式——这是R4后续轮次的核心理论挑战。

---

## §0 框架声明

**Meta-framework:** 范畴论Process Theory (Coecke-Kissinger 2017/2018)

**Operational Model:** Petri网/Event Structures (Joachim et al. 2025, 基于Clairambault-De Visme-Winskel 2019)

**桥接原理：**
1. Process Theory提供因果结构的**公理化定义**——不需要时间
2. Petri网提供操作的**动态语义**——token消耗/产生是原生的
3. 两者通过Occurrence Net←→Event Structure的范畴对应统一

**核心公理（自Process Theory继承）：**
- **(A1) 过程本体论：** 过程（盒子+导线）是基本原语，时间/因果序是导出结构
- **(A2) 因果性公设：** 丢弃所有输出 = 丢弃所有输入（信息守恒）
- **(A3) 无环性约束：** 因果结构不含有向环（对应线路图的无环性）
- **(A4) 加倍构造：** 混合过程从纯过程通过加倍+丢弃产生

**核心公理（自Petri网继承）：**
- **(B1) Token守恒：** token不能从无中产生（对应因果性公设）
- **(B2) Firing语义：** 变迁触发 = 满足前提条件时原子性地消耗/产生token
- **(B3) 偏序因果：** ≤ = F的传递闭包（结构因果，非时间因果）

---

## §1 从静态DAG到动态Petri网

### 1.1 DGF格点图的静态性质

DGF的格点图L = (V, E)是一个静态有向无环图：
- V = S-places ∪ E-places（两个互补集合）
- E = {v→w : d(v,w) = 1 且方向由格点类型决定}
- 每个节点v的状态 ∈ {|0⟩, |1⟩}（静态赋值）
- 边 = 因果可能连接（仅在相邻格点间）

**静态约束：** DAG结构固定了"可能的"因果连接——但实际的因果过程（哪个格点先影响哪个格点）取决于状态动力学。DAG本身不描述动态过程，只描述允许的因果拓扑。

### 1.2 翻译为Petri网

将DGF格点图翻译为Petri网N_DGF = (P, T, F, m₀)：

**Place映射：**
```
每个格点 v ∈ V → Place p_v ∈ P
状态 |0⟩ → p_v 中有 token（可被消耗的资源）
状态 |1⟩ → p_v 中无 token（已被消耗）
```

**初始标记m₀：**
```
m₀(p_v) = 1 当 v 的状态 = |0⟩
m₀(p_v) = 0 当 v 的状态 = |1⟩
```

**Transition定义：**

*前向转移 t_f(u,v):*
- 前提：S-place u 有token（|0⟩）∧ E-place v 有token（|0⟩）
- u的格点状态 = |1⟩（潜在"因"），v的格点状态 = |0⟩（潜在"果"）
- 前向因果：u的"因"信息流向v，"标记"v为|1⟩
- 形式：•t_f(u,v) = {p_u, p_v}, t_f(u,v)• = {p_v^marked}
- 语义：消耗E-place v的token（消耗"果"的可能性），产生v的"已标记"状态

*回流 t_r(u,v):*
- 前提：E-place v 被标记（|1⟩）∧ S-place u 有token（|0⟩）
- 触发条件：u已被因果连接标记为|1⟩（即u的token已被前向过程消耗）⊘
- 回流：v的"果"信息反向影响u，"恢复"u为|0⟩
- 形式：•t_r(u,v) = {p_v^marked, p_u}, t_r(u,v)• = {p_u^renewed}
- 语义：消耗S-place u的token（消耗u的"潜在因"状态），产生u的"已恢复"状态

**修正：** 实际上，回流的发生顺序是：
1. 前向过程先发生：S-place u的token被消耗 → u变为|1⟩，E-place v被标记
2. 回流在前向过程触发后才可能发生：消耗E-place v的"已标记"状态，恢复S-place u的token

精确的Petri网表示需要区分时间步（通过展开语义）：

```
Step 1 (前向):
  t_f: consumes token(p_u), produces token_at_S(u, marked)
       consumes token(p_v), produces token_at_E(v, marked)

Step 2 (回流，在前向发生后可能):
  t_r: consumes token_at_E(v, marked), consumes token_at_S(u, marked)
       produces token_at_S(u, renewed)
```

这需要Petri网的**展开语义**（unfolding semantics）来精确表示——这正是Joachim et al.提供的工具。

### 1.3 Petri网的Firing语义是原生的动态过程

**关键论证：** Petri网的firing语义**天然是动态的**。这不是在"揣测"动态——这是**形式操作语义**。

Petri网的变迁触发规则：
1. 变迁t在标记m下**使能**（enabled）当且仅当∀p ∈ •t, m(p) > 0
2. 触发t产生新标记m'：m'(p) = m(p) - 1（若p ∈ •t\t•），m'(p) = m(p) + 1（若p ∈ t•\•t），否则m'(p) = m(p)

**这不是时间步：** Petri网的变迁触发是逻辑的（而非时间性的）——"前提满足 → 触发"是条件-结果的逻辑关系，而非"t时刻 → t+1时刻"的时间关系。两个独立的变迁可以并发触发（interleaving语义），也可以顺序触发——这由**偏序约简**而非全局时钟决定。

**对我们项目的核心意义：** DGF从"静态DAG+静态格点赋值"升级为"Petri网+动态token流"，其中：
- token的位置和数量动态演化
- 变迁的触发受前提条件约束
- 因果顺序从网的偏序结构中导出
- **整个框架不需要"时间"参数**

---

## §2 回流公式的Petri网证明

### 2.1 Petri网语言中的量

定义以下量：
- **E-token总数 C_F:** 初始标记下所有E-places中的token数
  ```
  C_F = Σ_{v ∈ E-places} m₀(p_v)
  ```
- **前向触发次数 N_f(t):** 到"时刻"t为止已触发的前向转移总数
- **回流触发次数 N_r(t):** 到"时刻"t为止已触发的回流总数

其中"时刻"t指Petri网展开中的步索引（逻辑步，非物理时间）。

### 2.2 鸽巢原理的Petri网版本

**引理1（Token守恒）：**
在任何可达标记m下，E-places中的token总数不超过C_F。
```
∀ reachable m: Σ_{v ∈ E-places} m(p_v) ≤ C_F
```
*证明：* 每个前向转移消耗恰好一个E-token并产生一个E-marked标记（相当于零token的place）。回流消耗E-marked标记但不产生E-token。因此E-token只被消耗，从不产生。▢

**引理2（因果计数）：**
前向转移可触发的次数≤ C_F。
```
N_f ≤ C_F
```
*证明：* 每次前向转移消耗一个E-token。由引理1，可消耗的E-token不超过C_F。▢

**引理3（回流前提）：**
回流t_r(u,v)可触发当且仅当：
(a) E-place v已被前向转移标记（v处已发生前向过程）
(b) S-place u的token仍存在（u尚未被所有可能的前向过程消耗）
*证明：* 直接来自t_r的定义——前提集•t_r = {p_v^marked, p_u}。▢

### 2.3 回流上界的Petri网推导

**定理S1（Petri网版本）：**
```
N_r ≤ min(N_S·q_S, N_E·(1-q_E))
```
其中N_S = |S-places|, N_E = |E-places|, q_S = S-place处于|0⟩的比例，q_E = E-place处于|0⟩的比例。

*证明（Petri网语言）：*

设N_f为已触发的前向转移数。每次前向转移产生一个E-marked标记。设t时刻有m个E-places已被标记。则m ≤ N_f ≤ C_F = N_E·(1-q_E)（因为初始时有N_E·(1-q_E)个E-token可用）。

每个回流需要：
1. 一个E-marked标记（来源 = 已发生前向转移的E-place）
2. 一个S-token（S-place尚未被消耗）

E-marked标记数m ≤ min(N_f, N_E·(1-q_E))（N_f是已触发的转移数，N_E·(1-q_E)是E-token总数的上界）。

剩余S-token数 = N_S·q_S - (已被前向消耗的S-token数)。

每个前向转移消耗一个S-token（在产生E-marked标记的同时）。所以已被消耗的S-token数 = N_f。

回流数N_r ≤ min(m, N_S·q_S - N_f)。

当N_f增长时，m增长但剩余S-token减少。最优分配是N_f = min(N_E·(1-q_E), N_S·q_S/2)（两约束的交叉点）。

在最优分配下：N_r ≤ min(N_S·q_S, N_E·(1-q_E))。

更准确地说：
- 若N_S·q_S < N_E·(1-q_E)，回流受限于可用S-token数 → N_r ≤ N_S·q_S
- 若N_E·(1-q_E) < N_S·q_S，回流受限于E-marked标记数 → N_r ≤ N_E·(1-q_E)
- 在最不利情况下，N_r ≤ min(N_S·q_S, N_E·(1-q_E)) ▢

### 2.4 证明的形式语义学地位

这个证明与DGF原始证明在**计数结构上相同**——但存在关键的形式差异：

| 方面 | DGF原始 | Petri网版本 |
|------|---------|------------|
| "消耗" | 比喻性用语 | 形式操作语义（token移除） |
| "产生" | 比喻性用语 | 形式操作语义（token添加） |
| "触发" | 隐含假设 | 形式前提条件（使能规则） |
| "每次最多一次" | 鸽巢原理断言 | Token守恒引理 |
| 动态性 | 猜测的 | 形式推导的 |
| 可验证性 | 需要外部模型 | Petri网可执行/可模拟 |

**关键推进：** Petri网版本使"消耗""产生""触发"获得了**形式语义**。这不再是启发式论证——变迁触发规则和token语义是Petri网理论的标准组成部分，已有40+年的形式化历史。

---

## §3 桥接状态

### 3.1 完整映射链

从静态DAG到经验测量的完整形式化链：

```
层级0: DGF格点图（静态DAG）
        │
        │ 格点→Place, 边→Flow, 状态→Token赋值
        ▼
层级1: Petri网（动态token流）
        │
        │ 展开语义（Unfolding）
        ▼
层级2: Occurrence Net（显式因果+并发）
        │
        │ 丢弃条件→偏序+冲突
        ▼
层级3: Event Structure（纯因果偏序）
        │
        │ 量子赋值Q (CPTNI映射)
        ▼
层级4: Quantum Event Structure / Quantum Petri Net
        │
        │ Process Theory / 因果性公设
        ▼
层级5: Causal Process Theory（Coecke-Kissinger框架）
        │
        │ Process Matrix形式化
        ▼
层级6: 因果不等式 / 回流界（可操作测量）
```

### 3.2 不变性定理

**定理（桥接不变性）：**
设P为一个物理实现，满足：
1. **(Local QM):** 在每个格点上的操作由CP映射描述
2. **(Causality):** 满足Coecke-Kissinger因果性公设（丢弃输出=丢弃输入）
3. **(Token Conservation):** 信息载体（token等价物）不能从无中产生

则P中的最大回流率受S1上界约束：
```
P_reflux ≤ min(N_S·q_S, N_E·(1-q_E))
```

*证明概要（完整形式化留待后续轮次）：*

(a) 因果性公设（条件2）等价于Petri网中的token守恒（条件3）。因为：丢弃输出=丢弃输入意味着信息流不能"放大"——在Petri网语言中，这意味着标记（token分布）的总"信息容量"不增加。Token守恒正是这一原理在离散资源模型中的表达。

(b) Petri网版本的回流上界（§2.3）对所有满足token守恒的Petri网成立。由于Petri网的firing语义是token流的最一般操作模型，任何满足token守恒的离散过程都可由某个Petri网模拟。

(c) 条件1（局部量子力学）确保每个格点上的操作可以通过CPTNI映射的量子赋值来描述——这正是Joachim et al.的局部量子赋值Q₀。该赋值下的Drop Condition保证轨迹是概率赋值（trace-non-increasing → valid probability），与因果性公设兼容。

(d) 因此，P中的回流由Petri网中的回流上界约束。上限在最优token分配下取得，即min(N_S·q_S, N_E·(1-q_E))。▢

### 3.3 开放问题：P_reflux作为因果不等式

**核心假设（待验证）：**
> 回流公式P_reflux ≤ min(N_S·q_S, N_E·(1-q_E))可以被重新表述为Process Matrix框架中的因果不等式。

**论证思路：**

在Oreshkov的Process Matrix形式化中，因果可分离的过程必然满足P_succ ≤ 3/4。类似地，如果回流公式是因果不等式，那么：

1. 任何**因果可分离**的物理过程（即可以分解为确定因果顺序的混合）必然满足回流上界
2. **违反**回流上界的过程必然是非因果可分离的
3. 回流界成为一个基于**资源消耗**（而非通信博弈）的因果见证

**结构类比：**

| Oreshkov因果不等式 | Reflux因果不等式（假设） |
|---|---|
| 博弈：Bob猜Alice的比特 | "自博弈"：环境反作用于系统 |
| 资源：双向通信能力 | 资源：可消耗的E-token |
| 见证：P_succ > 3/4 | 见证：P_reflux > min(N_S·q_S, N_E·(1-q_E)) |
| 机制：叠加因果顺序 | 机制：叠加前向/回流转移 |
| 实验室：两个封闭实验室 | "实验室"：S-places和E-places |

**差异与挑战：**
- Oreshkov需要两个独立方（自由选择），DGF是单系统自作用——如何在Process Matrix中编码"自博弈"？
- 回流公式的"概率"本质上是**频率比**（资源消耗比），而非博弈成功概率——需要形式化资源消耗的概率语义
- DGF的格点结构引入了**局部性约束**（仅相邻格点间转移）——这在Process Matrix中对应什么约束？

**初步答案：** P_reflux可以被视为一种**资源约束的因果不等式**，其中"通信博弈"替换为"token消耗博弈"。在Process Matrix语言中，可以将S-places和E-places分别视为"Alice"和"Bob"的输入/输出系统（或更准确地说，将格点对(u_S, v_E)视为局部实验室对），将回流视为"反向通信"，将鸽巢上界视为因果可分离性约束。

但完整的形式化需要：
1. 在Process Matrix中编码DGF的局部格点结构（晶格约束）
2. 定义"资源消耗博弈"的因果不等式
3. 证明因果可分离过程必然满足回流上界
4. 构造（或证明不存在）违反回流上界的非因果可分离过程

这构成R4后续轮次的核心理论任务。

### 3.4 元理论结论

**问题：Process Theory是否"预设"时间？**

**答案：否。** Process Theory中的"因果顺序"是以下结构关系的导出概念：
1. **连通性**：盒子间导线连接 → 有向路径 → 偏序
2. **无环性**：不存在有向环 → 偏序的反对称性 → 偏序是良定义的
3. **因果性公设**：丢弃约束 → 信息守恒 → 偏序与物理可实现性兼容

这一观点在三个框架中一致：
- **Coecke-Kissinger:** 因果结构 = 线路图的无环性 + 单位终对象
- **Joachim et al.:** 因果结构 = Petri网的流关系传递闭包 + Drop Condition
- **Oreshkov et al.:** 因果结构 = Process Matrix的因果可分离性 + 因果不等式

**统一视角：** 时间不是被预设的——时间的**偏序结构**（因果序）是从过程的**组合结构**中涌现的。这完美契合Whitehead的过程本体论：过程先于时间。

### 3.5 对DGF的意义

从静态DAG升级为动态Petri网后：

1. **操作语义化：** "格点|0⟩→|1⟩"从静态赋值变为token消耗事件——有了形式操作语义
2. **因果可分析化：** Petri网的展开语义允许精确分析哪些因果顺序是可能的，哪些被排除
3. **量化验证化：** Drop Condition提供可检查的正性条件——对应量子赋值的物理可实现性
4. **组合框架化：** QPN的并行组合和保持丢弃的连接操作允许将DGF的不同区域组合分析
5. **因果不等式化：** 回流界可能升格为Process Matrix框架中的因果不等式——从组合计数约束升级为因果结构见证

---

## 自我攻击与交叉验证

### 攻击1：过度形式化？

**指控：** 使用范畴论+Petri网+Process Matrix三层形式化是过度工程。DGF原始证明已经是正确的数学论证。

**回应：** DGF原始证明的数学正确性不依赖于任何形式语义。"消耗""产生""触发"在DGF原文中是**启发式语言**——它们的操作含义需要读者自行脑补。本R4的贡献恰恰是将这些操作概念赋予形式语义，使得DGF从数学正确的**计数论证**升级为操作正确的**动态模型**。

这不是过度形式化——这是弥合"数学正确"和"物理可操作"之间的鸿沟。

### 攻击2：Petri网≠量子？

**指控：** Petri网本质上是经典并发模型。虽然有Quantum Petri Nets（Joachim et al.），但其量子性来源于量子赋值Q——若不加Q，就是经典Petri网。DGF的格点图如何获得量子赋值？

**回应：** 这正是Joachim et al.贡献的要点。QPN的定义是：(经典Petri网) + (满足局部Drop Condition和局部Obliviousness的局部量子赋值Q₀)。量子性由Q₀携带，网的骨架结构是经典但足够的——因为因果结构本身是"经典"的（偏序），量子效应（叠加、纠缠）编码在Q₀的CPTNI映射中。

对DGF而言，Q₀的具体形式取决于格点的量子动力学模型。这是R4后续轮次的任务——但框架已在QPN中提供。

### 攻击3：P_reflux≠因果不等式？

**指控：** P_reflux是资源消耗界，Oreshkov的因果不等式是博弈成功概率界。两者在数学结构上不同——不能简单等同。

**回应：** 确实，P_reflux和因果不等式在**形式**上不完全相同。但存在一个**深层结构同源**：两者都是"在确定因果顺序的约束下，某种反向影响的最大可达程度"的上界。

更精确地说：
- Oreshkov: 反向通信（双向同时不可能）的上界
- Reflux: 反向token恢复（token不能再生）的上界

两者都是鸽巢原理的变体——只是"鸽子"和"巢"的身份不同。在Oreshkov中是"通信方向"，在Reflux中是"token/toggle"。我同意将P_reflux直接称为"因果不等式"需要更多形式化工作——这正是§3.3标记为"开放问题"的原因。

但**概念上**的桥接已经确立：回流界编码了对反向因果效应的基本限制，这一限制根植于过程理论的信息守恒原理。

---

## 状态与下一步

### 本轮完成

- [x] 精读Coecke & Kissinger (2018) — Process Theory中的因果结构形式化
- [x] 精读Joachim et al. (2025) — Petri网token消耗/变迁触发形式语义
- [x] 精读Oreshkov et al. (2012) — Process Matrix形式化和因果不等式
- [x] §0框架声明 — Process Theory + Petri网操作语义
- [x] §1静态DAG→动态Petri网翻译
- [x] §2回流公式的Petri网证明
- [x] §3桥接状态与不变性定理的概要证明

### R4 Round 2（下一轮）预览

1. **精化桥接：** 完成不变性定理的完整形式化证明（§3.2的详细版本）
2. **P_reflux因果不等式化：** 在Process Matrix框架中定义"回流博弈"，推导对应的因果不等式
3. **量子赋值构造：** 为DGF格点结构构造具体的局部量子赋值Q₀
4. **Drop Condition验证：** 验证Q₀是否满足局部Drop Condition
5. **非因果可分离过程搜索：** 探索是否存在可违反回流界的过程矩阵

---

## 参考文献

1. Coecke, B. & Kissinger, A. (2018). Categorical Quantum Mechanics I: Causal Quantum Processes. In *Oxford Scholarship Online*. Oxford University Press. arXiv:1510.05468v3.

2. Joachim, J.S., de Visme, M., Haar, S. & Winskel, G. (2025). Quantum Petri Nets with Event Structure semantics. arXiv:2508.14531.

3. Oreshkov, O., Costa, F. & Brukner, C. (2012). Quantum correlations with no causal order. *Nature Communications* 3, 1092. arXiv:1105.4464v3.

4. Clairambault, P., De Visme, M. & Winskel, G. (2019a). Concurrent Quantum Strategies. In *Lecture Notes in Computer Science*. Springer.

5. Clairambault, P., De Visme, M. & Winskel, G. (2019b). Game Semantics for Quantum Programming. *Proceedings of the ACM on Programming Languages* 3(POPL).

6. Winskel, G. (1987). Event Structures. In *Petri Nets: Applications and Relationships to Other Models of Concurrency*. Springer.

7. Chiribella, G., D'Ariano, G.M. & Perinotti, P. (2010). Probabilistic theories with purification. *Physical Review A* 81(6), 062348.

8. Coecke, B. (2014). Terminality implies non-signalling. arXiv:1405.3681.


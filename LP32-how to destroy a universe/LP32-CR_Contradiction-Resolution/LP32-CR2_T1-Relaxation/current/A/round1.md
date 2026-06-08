# CR2 Round 1 -- A博士（形式攻击）

**日期:** 2026-06-08
**角色:** A博士，学院派
**轮次:** Round 1 -- T1弛豫的微观机制分析与框架内重新解释

---

## §-1 文献搜索

### 组1: T1机制分类 -- 自发辐射 vs 环境辅助

**检索结果评估:**

Yen et al. (2025, Phys. Rev. Applied, arXiv:2405.10107v2) "Interferometric Purcell suppression of spontaneous emission in a superconducting qubit" -- 直接相关。该工作实验演示了通过干涉Purcell滤波将共振器介导的qubit衰减抑制2个数量级以上，带宽400MHz。关键结论：Purcell衰减率可以通过工程设计(λ/4分离+电容/电感耦合比调谐)精确控制。**这意味着T1部分依赖于环境结构，是环境辅助的。**

Sete, Gambetta & Korotkov (2014, Phys. Rev. B, arXiv:1401.5545v2) "Purcell effect with microwave drive: Suppression of qubit relaxation rate" -- 直接相关。证明了Purcell率随微波驱动强度增加而减小——非线形区域抑制更显著。**进一步支持T1对环境参数的依赖。**

Carroll et al. (2022, npj Quantum Information) "Dynamics of superconducting qubit relaxation times" -- 在10个transmon qubit中观测到T1时间在~9个月尺度上的时域涨落，归因于二能级系统(TLS)缺陷的光谱扩散。**T1不是固定常数——它随环境缺陷动力学涨落。**

Reed et al. (2010, Appl. Phys. Lett.) "Fast Reset and Suppressing Spontaneous Emission of a Superconducting Qubit" -- 通过flux偏置实现in situ控制qubit寿命超过50倍。**T1可通过外部参数主动调控。**

**组1结论:** 文献一致支持T1本质上是环境辅助过程。T1率依赖于：(a)电磁环境态密度（Purcell效应），(b)材料缺陷动力学（TLS），(c)外部可调参数（flux偏置、驱动强度）。**"纯自发"的T1——即qubit在零光子真空中的本征衰减——在实验上被Purcell滤波抑制后仅表现为残余本底。** 自由空间自发辐射率是理论上限，在实际器件中被环境和工程设计主导。

### 组2: 开放量子系统不可逆性

**Hatano & Ordonez (2019, Entropy)** "Time-Reversal Symmetry and Arrow of Time in Quantum Mechanics of Open Systems" -- 关键结果：具有可数无限多态的开系统中，薛定谔方程的本征态（共振态和反共振态）自发破缺时间反演对称性。共振态主导t>0的衰变；反共振态主导t<0的增长过程。**时间箭头不是假设——它从开系统的态空间结构涌现。** 这对DGF的意义：如果|1⟩→|0⟩的T1衰减通过无限维环境发生，时间反演对称性在动力学层面自动破缺——与DGF的"irreversible forward transfer"自洽。

**Axelsson (2026, arXiv:2604.07418v1)** "Born's Rule from Reversible Evolution and Irreversible Outcomes" -- 从"可逆线性演化+不可逆记录形成"的兼容性推导Born规则。核心区分：微观动力学可逆（时间对称），但记录形成后不同结果配置不可互易（操作不可逆）。**这给出了"不可逆性"的操作定义：不是微观动力学不可逆，而是记录形成后不同分支不再可互易。** DGF的"determination不可逆"应在此意义上理解——与T1自发辐射的"不可逆"共享同一个操作结构。

**Settimo & Piilo (2026, arXiv:2605.07797v1)** "Quantum jump unravelings for non-Markovian open system dynamics: a review" -- 综述了非马尔可夫量子跳变unraveling技术。关键发现：**非马尔可夫体系中，衰减率可暂时变负——对应反向跳变(reverse jump)**。这意味着jump operator的单一方向性(L=|1⟩⟨1|⊗|1⟩⟨0|)严格只在马尔可夫极限成立。当环境有记忆时，反向跳变是动力学必然。这对DGF提出直接挑战：**如果DGF的L只含|1⟩⟨0|_E而不含|0⟩⟨1|_E，它在非马尔可夫区域——即真实物理系统中——不完整。**

**Tsang (2025, Quantum)** "Quantum reversal: a general theory of coherent quantum absorbers" -- 提出Petz recovery map的量子反转条件。证明了"反转器"(reverser)可以相干地反转另一个系统对场的任何效应。**原则上，任何开放系统动力学都有对应的反转操作——只要你能获取所有被发射的场量子。** 这从原理层面说明不可逆性是practical而非fundamental的——同Axelsson的"操作不可逆"结论一致。

**组2结论:** 开放量子系统中的"不可逆性"是操作性的而非原理性的。微观动力学保持时间反演对称；不可逆性从两个来源涌现：(a)无限维环境的共振态自发破缺T对称（Hatano-Ordonez），(b)记录形成后不同分支的操作不可互易性（Axelsson）。对DGF而言，这意味着determination的"不可逆"需要在操作意义上精确定义——**它是对系统自身的局部动力学而言不可逆，而非对系统+环境整体的幺正演化而言不可逆。**

### DGF原文中关于jump operator适用范围的讨论

DGF框架PRL S1论文(prl_s1.tex)中写道：

> "A qubit, once determined (|1⟩), has a vanishing probability of returning to |0⟩ under the **system's own dynamics.** This is not a postulate but a consequence of quantum Darwinism. The determined state |1⟩ of a pointer qubit is redundantly recorded in N_red other environment qubits via the same H_SE interaction. The Kac recurrence time for the coordinated reversal of all N_red records scales as τ_Kac ~ 2^{N_red}. For N_red >~ 100, this exceeds 10^30 years."

关键限定词：**"under the system's own dynamics"**（在系统自身动力学下）。这已为T1留出了概念空间——T1不是"系统自身动力学"驱动的，而是**系统+环境联合动力学**驱动的。DGF论文没有声称系统在环境作用下不能衰减——它声称的是指针基determination在系统自身动力学下不可逆。

此外，PRD论文(two_rules_prd_final.tex)明确声明：

> "The interaction Hamiltonian is diagonal in the computational basis: H_SE = Σ g_ij σ_z^(i) ⊗ σ_z^(j). This is the generic form for decohering interactions and einselects the computational basis as the pointer basis."

σ_z ⊗ σ_z 相互作用只产生退相位(T2)，不产生弛豫(T1)。T1需要σ_x ⊗ σ_x或σ_y ⊗ σ_y项——即qubit-环境耦合中的非对角分量。**DGF框架的当前形式只覆盖了T2型退相干。** T1的问题本质上是：框架是否需要引入非对角系统-环境耦合项来描述能量弛豫？

---

## §0 框架声明

**开放量子系统理论** + **量子光学（自发辐射/Purcell效应）** + **Zurek量子达尔文主义**

本CR2的分析基于以下理论框架：

1. **量子轨迹/跳变unraveling:** 开放系统动力学的纯态实现。马尔可夫极限下的标准GKSL主方程对应Wiener过程（量子态扩散）或Poisson过程（量子跳变）。非马尔可夫推广（Settimo & Piilo 2026）允许多种unraveling方案。

2. **Purcell效应:** 环境修改电磁态密度→增强或抑制自发辐射率。Purcell因子F_P ∝ Q/V（品质因子/模体积）。在腔QED中，F_P可从~10^{-3}(抑制)到~10^3(增强)。

3. **量子达尔文主义:** 指针态通过与环境的多重冗余记录获得客观性。一旦|1⟩被N_red >> 1个环境qubit冗余编码，其Kac recurrence时间指数增长。

4. **自发辐射的Wigner-Weisskopf理论:** 原子+真空辐射场的联合演化。真空涨落触发退激发；退激发率由费米黄金规则给出：γ = 2π|⟨f|H_int|i⟩|² ρ(ω)。该理论同时包含"自发"和"环境态密度依赖"两个方面——将在§1中仔细分析。

---

## §1 T1的微观机制分析

### 1.1 自发辐射：真空涨落触发，但环境态密度决定

Wigner-Weisskopf (1930)理论给出的自由空间自发辐射率为：

$$γ_0 = \frac{ω_{01}^3 |d|^2}{3πε_0 \hbar c^3}$$

其中d是偶极矩阵元，ω_{01}=|1⟩→|0⟩跃迁频率。

**关键物理拆分:**

| 成分 | 来源 | 是否可调制 |
|------|------|----------|
| 真空涨落 | 电磁场的零点能⟨0|E²|0⟩≠0 | 不可消除（量子电动力学的基本事实） |
| 态密度ρ(ω) | 环境光子模的空间分布 | 可通过腔/Purcell滤波调制 |
| 耦合强度|d|² | qubit的偶极矩 | 可通过qubit设计调制 |
| 温度激发 | 热光子布居n_th(ω) | 可通过冷却控制 |

**这意味着T1不完全是"自发的":** 真空涨落是触发器（trigger），但衰减率的大小由环境的态密度和qubit-环境耦合共同决定。没有任何实验能测量"裸"自发辐射率γ_0而不经过环境——因为做实验本身就是将qubit放在某种环境中。

### 1.2 Purcell效应：环境作为T1率的设计工具

在电路QED中，qubit通过共振器耦合到传输线。Purcell衰减率为：

$$Γ_P = κ \left(\frac{g}{Δ}\right)^2 \left(\frac{ω_q}{ω_r}\right)^4$$

其中κ是共振器线宽，g是qubit-共振器耦合，Δ=ω_q-ω_r是失谐。

**Yen et al. (2025)的关键实验事实:**
- 干涉Purcell滤波将Purcell衰减抑制2个数量级以上（~400MHz带宽内）
- 在notch频率处测得的Purcell限寿命>16ms（对应抑制因子>2000）
- 残留T1~20μs归因于**本征qubit衰减**（材料缺陷+准粒子+辐射损耗）

**本征T1的下界问题:** 即使完全消除Purcell通道（κ→0，无限失谐Δ→∞），超导qubit的T1仍受限于：
- 二能级系统(TLS)缺陷 ~10-100μs
- 非平衡准粒子 ~100μs-1ms
- 介电损耗 ~100μs-1ms
- 辐射到自由空间 ~ms级

这些是"environment-assisted"的不同形式——不是真空涨落本身，而是材料中的实际自由度。**在原则上，如果排除所有环境自由度（真空涨落除外），自由空间自发辐射率γ_0确实给出T1的上限。** 但这是纯原理讨论——没有实验能达到这个极限。

### 1.3 纯自发成分：原理上的存在

在零温极限(T=0)下、无腔自由空间中，一个激发态原子必然通过自发辐射衰减——这是量子电动力学的基本结果。真空涨落的存在不依赖于环境温度或腔结构。

**但这与DGF矛盾吗？** 关键在于：

- **自发辐射的完整过程是:** |1⟩_S ⊗ |0⟩_photon → |0⟩_S ⊗ |1⟩_photon
- 系统失去一个|1⟩，环境（电磁场）获得一个光子|1⟩_photon
- **这不是单纯的determination逆转——这是系统+环境间的determination交换。**

在DGF语言中：
- 系统S的|1⟩→|0⟩：系统损失了一个"已确定"bit
- 环境E的|0⟩_photon→|1⟩_photon：环境获得了一个"已确定"bit（光子的存在是确定的）
- **净结果：总的determination数量在系统+环境联合体上守恒。**

---

## §2 T1在DGF框架中的重新解释

### 2.1 CR1的遗产：determination = 布居数翻转

CR1建立了DGF的determination的精确定义：

- **determination = |0⟩→|1⟩的布居数翻转**（q减小的过程）
- **de-determination = 不存在于DGF的jump operator中**
- **相位退相干(T2)≠ determination** ——回波是T2过程，不涉及布居数改变

这立即导向CR2的核心张力：

| | Determination (DGF) | T1弛豫 |
|---|---|---|
| 跃迁方向 | |0⟩ → |1⟩ | |1⟩ → |0⟩ |
| q的变化 | q减小 | **q增大** |
| 在L中存在？ | 存在(K_1 = |1⟩⟨1|⊗σ⁺_E) | **不存在** |
| 物理过程 | 信息编码到环境 | 能量弛豫到环境 |

**乍看这是一个直接的方向矛盾：DGF说|0⟩→|1⟩不可逆，T1偏偏是|1⟩→|0⟩。** 但我们需要在系统+环境联合态的层面上重新分析。

### 2.2 三种可能性的严格分析

#### 可能性A：T1 = 环境determination（推荐方向）

**核心命题:** T1不是|1⟩→|0⟩的单纯逆转，而是系统+环境联合演化中的determination交换。

**联合演化:**
```
|1⟩_S ⊗ |0⟩_E  ──T1──→  |0⟩_S ⊗ |1⟩_E
```

- 系统S: 损失一个|1⟩（q_S增加）
- 环境E: 获得一个|1⟩（q_E减小）
- 联合体S+E: q_{total} = (q_S·N_S + q_E·N_E)/(N_S+N_E) **严格守恒**（在N_S=N_E时）

**在DGF框架中的解释:**
- DGF的determination定义为|0⟩→|1⟩在**指针基**中的跃迁
- T1过程中：S的指针基经历了|1⟩→|0⟩（从信息论角度看，"已确定"bit被"取消确定"了）
- 但同时E的指针基经历了|0⟩→|1⟩（光子被产生，一个"已确定"bit在环境中被创建）
- **DGF的determination是对单个qubit定义的，但T1涉及的是两个qubit（S+E）的联合演化。**
- 在联合态空间：T1不是determination逆转——它是determination**从S转移到E**。

**数学形式:**
DGF的forward transfer(CNOT_S→E):
```
|1⟩_S|0⟩_E → |1⟩_S|1⟩_E    (S保持不变, E被determine)
```

T1的swap-like过程:
```
|1⟩_S|0⟩_E → |0⟩_S|1⟩_E    (S失去determination, E获得determination)
```

关键区别：在forward transfer中，S保持|1⟩（信息被复制）。在T1中，S失去|1⟩（能量被转移）。**DGF的jump operator L = |1⟩⟨1|⊗|1⟩⟨0|描述的是复制型信息转移；T1是交换型能量转移。** 它们是不同的物理过程。

**支持证据:**
1. Wigner-Weisskopf理论：自发辐射的完整描述必然涉及原子+辐射场的联合态演化。在联合态中，原子退激发=光子产生——总的激发数守恒（在闭系统近似下）。
2. 量子轨迹理论中的跳变算子：标准自发辐射的Lindblad跳变算子是L = √γ |0⟩⟨1|_S ——但这是在对环境求迹后得到的约化描述。在联合态层面，存在L_joint = √γ |0⟩⟨1|_S ⊗ a^†_k，明确包含光子的产生。
3. Purcell效应的可调性：T1率依赖于环境态密度的事实表明，T1本质上是系统+环境联合过程，不是系统自身性质。

**反驳:**
- DGF的q定义在**单qubit的指针基布居**上。如果T1后S的|0⟩布居增加了，那就是q_S增加了，这在DGF中是被禁止的（因为没有对应L项）。
- 回应：DGF的禁止是针对**系统自身动力学**（见§-1中DGF原文的限定词）。T1不是系统自身动力学——它需要环境的主动参与。

#### 可能性B：T1 = 逆转 + 新determination（抵消论）

**核心命题:** S释放能量=逆转（S的|1⟩→|0⟩逆转了之前的determination），E获得能量=新determination（E的|0⟩→|1⟩）。逆转和新增互相抵消，净determination数为零，但逆转确实发生了。

**困难:**
- 如果逆转"确实发生了"，DGF的"不可逆"就被违反了——即使净determination守恒。
- DGF的核心声张是**determination事件是不可逆的**——一旦一个qubit从|0⟩变为|1⟩，它不能由系统自身动力学变回去。可能性B的"逆转+抵消"虽然在联合态层面净效果为零，但在S的局部层面，|1⟩→|0⟩确实是逆转。
- **但在联合演化的框架下，局部逆转+环境新增是标准开放系统动力学的核心。** 如果DGF不允许局部逆转，它实际上在禁止所有类型的T1过程——而这与所有实验矛盾。

**我的判断:** 可能性B在数学上等价于可能性A（都是联合演化|1⟩_S|0⟩_E → |0⟩_S|1⟩_E），但在概念框架上对DGF更不利，因为它直接将T1定性为逆转。**可能性A更精确——它强调净效果不是"逆转"，而是"转移"。**

#### 可能性C：|0⟩/|1⟩与能量本征态不正交

**核心命题:** DGF的|0⟩（未确定）/ |1⟩（已确定）是**信息论标记**，不是能量本征态。T1发生在**能量基**上（|g⟩→|e⟩的逆过程|e⟩→|g⟩），而determination发生在**指针基**上——两个基可能不正交。

**关键论证:**
- 在超导transmon qubit中，|0⟩=|g⟩（基态），|1⟩=|e⟩（第一激发态）。因此指针基=能量基。在这种实现中，T1的|e⟩→|g⟩同时就是|1⟩→|0⟩的信息论逆转——可能性C失效。
- 但在更一般的qubit实现中，指针基可能不是能量基。例如，在decoherence-free subspace编码中，逻辑|0⟩和|1⟩是简并能量子空间的基矢——T1发生在物理qubit的能量基上，不直接影响逻辑qubit的指针基布居。
- **因此可能性C的有效性取决于物理实现。** 它不能作为DGF框架的通用解决方案。

**我的判断:** 可能性C在通用理论层面无效——DGF声称其|0⟩/|1⟩适用于任何指针基选择的qubit系统。在超导qubit（最广泛使用的量子计算平台之一）中，指针基=能量基，T1直接就是|1⟩→|0⟩。不能依赖实现细节来避开矛盾。

### 2.3 推荐方向：可能性A + 框架精确化

**推荐采纳可能性A**，但需要以下精确化：

#### S1: 区分"复制型determination"和"交换型determination"

| | 复制型 (DGF Forward Transfer) | 交换型 (T1 Relaxation) |
|---|---|---|
| 过程 | CNOT_S→E: |1⟩_S|0⟩_E → |1⟩_S|1⟩_E | SWAP-like: |1⟩_S|0⟩_E → |0⟩_S|1⟩_E |
| S的最终态 | 保持|1⟩ | 回到|0⟩ |
| E的最终态 | 变为|1⟩ | 变为|1⟩ |
| 系统determination | 不变 | **丢失** |
| 环境determination | 增加 | 增加 |
| 净determination | 增加 | **不变** |
| 能量 | 计算基操作，不涉及能量转移 | **能量转移** |
| DGF是否覆盖 | 已覆盖(L = |1⟩⟨1|⊗σ⁺_E) | **未覆盖** |

**核心洞察:** DGF的jump operator L = |1⟩⟨1|⊗|1⟩⟨0|只覆盖了复制型determination。T1是交换型——它需要一个新的/扩展的jump operator来描述。

#### S2: 扩展jump operator的提议

如果DGF框架要自洽地包含T1过程，jump operator需要扩展为：

$$L_{total} = L_{copy} \oplus L_{swap}$$

其中：
- L_copy = √κ |1⟩⟨1|_S ⊗ |1⟩⟨0|_E （现有的复制型forward transfer）
- L_swap = √γ(q_E) |0⟩⟨1|_S ⊗ |1⟩⟨0|_E （新增的交换型energy relaxation）

L_swap的物理含义：
- |0⟩⟨1|_S: S从|1⟩衰减到|0⟩（能量弛豫）
- |1⟩⟨0|_E: E从|0⟩跃迁到|1⟩（环境获得激发）
- 联合操作：S失去的determination被E获得——determination转移，非逆转。

**关键参数γ(q_E):** T1率应依赖于环境容量q_E——如果环境已饱和(q_E→0)，没有|0⟩_E态可供激发跃迁，T1应被抑制。这与Purcell效应的物理一致：Purcell滤波本质上就是在修改环境的有效态密度→修改q_E。

#### S3: q_E依赖的T1率——DGF的独特可检验预言

根据A2（容量有界），当环境接近饱和(q_E→0)时，环境没有剩余容量接收能量→T1应被抑制。相反，当环境完全空(q_E→1)时，T1不受限制。

$$γ(q_E) = γ_0 \cdot q_E$$

其中γ_0 = 自由空间自发辐射率（q_E=1极限）。

**这是DGF独有的、可检验的预言:** T1率应该与环境qubit的|0⟩布居q_E正相关。在超导qubit中，可以通过改变Purcell滤波的有效q_E来检验——滤波抑制了共振腔提供的"|0⟩_E态"，等效于降低了q_E，因此T1应延长。这已被实验观察（Yen et al. 2025），但尚未在DGF框架下被解释。

---

## 深挖

### 如果可能性A成立 → jump operator需要扩展吗？

**需要，但扩展是自然的：** 增加L_swap = √γ(q_E) |0⟩⟨1|_S ⊗ |1⟩⟨0|_E是框架的逻辑延伸，不改变其核心结构（容量约束+因果方向性）。扩展后的框架能同时描述：
1. 信息编码（复制型determination，L_copy）
2. 能量弛豫（交换型determination，L_swap）

两者共享同一个q_E依赖——这是DGF区别于标准开放量子系统理论的核心：**标准理论中T1率由环境谱密度J(ω)决定，DGF中T1率由环境信息容量q_E决定。** 这两个描述并不冲突——q_E可以通过J(ω)的积分表达。

### 如果可能性C成立 → DGF的|0⟩/|1⟩能等同于能量本征态吗？

可能性C实质上是说：DGF的|0⟩/|1⟩不应被理解为能量本征态。但在超导qubit的实验现实下，能量基就是指针基——这个区分在物理实现中不能被维持。

**诚实结论：** 在通用理论层面，|0⟩/|1⟩既不是纯信息论标记也不是纯能量本征态——它是**指针基**。指针基由系统-环境耦合的对称性决定(Zurek einselection)。在H_SE ∝ σ_z ⊗ σ_z的耦合下，指针基恰好是σ_z的本征态=能量基。在其他耦合形式下，指针基可能偏离能量基。**DGF不需要承诺|0⟩/|1⟩就是能量态——只需要承诺它们是系统-环境相互作用的指针基。**

---

## Round 1 初步结论

### CR2矛盾的性质判定

| 维度 | 判定 |
|------|------|
| 矛盾类型 | **表面现象矛盾，深层框架可调和** |
| 严重度 | 中等——需要扩展L但不改变核心公理 |
| 是否威胁A1/A2 | **否** |
| 框架修改范围 | jump operator扩展（添加L_swap），不修改q的动力学方程 |

### 核心论证链

1. **T1不是纯自发过程** ——它依赖于环境态密度(Purcell效应)和环境缺陷动力学(TLS)，在实验中可通过外部参数主动调节。Wigner-Weisskopf理论本身就包含环境态密度的依赖。

2. **T1 = |1⟩_S|0⟩_E → |0⟩_S|1⟩_E是系统+环境联合演化** ——不是单方面的|1⟩→|0⟩逆转，而是determination从系统转移到环境。净determination数量在联合体上守恒。

3. **DGF原文已为T1留出空间** ——"under the system's own dynamics"的限定词表明，DGF的不可逆性是对系统自身动力学成立，不排除环境参与的过程。

4. **建议扩展而非修改** ——jump operator扩展为L_total = L_copy ⊕ L_swap，添加交换型determination转移。这不改变框架的A1/A2公理、q的动力学方程、或静态引力势的推导。

### 类比CR1定位

| | CR1 (Quantum Revival) | CR2 (T1 Relaxation) |
|---|---|---|
| 现象 | 自旋回波中相干性恢复 | T1衰减（|1⟩→|0⟩） |
| 矛盾类型 | 表面矛盾 | 表面矛盾（需扩展但可调和） |
| 核心区分 | T1≠T2，determination=布居数翻转 | 复制型≠交换型，T1=转移非逆转 |
| 框架修改 | 仅措辞精确化 | 需添加L_swap（扩展非修改） |
| 可检验预言 | α-EXTRACT协议 | γ(q_E) = γ_0·q_E |

### 开放的下一轮问题

1. **γ(q_E) = γ_0·q_E 的精确函数形式是什么？** 线性是自然猜测，但需要从DGF的格点动力学推导。

2. **L_swap的完整数学形式？** 需要将√γ(q_E)嵌入到q的连续场描述中——γ本身应成为q的泛函而非常数。

3. **非马尔可夫反向跳变（Settimo & Piilo 2026）的挑战？** 如果环境有记忆，L_swap在非马尔可夫区域会产生反向过程|0⟩_S|1⟩_E → |1⟩_S|0⟩_E（重新激发）。这是否违反A1的因果方向性？

4. **T1与DGF的H定理的关系？** DGF证明的Lyapunov泛函是否在添加L_swap后仍然单调递减？

---

## 参考文献

[1] A. Yen et al., "Interferometric Purcell suppression of spontaneous emission in a superconducting qubit," Phys. Rev. Applied 23, 024068 (2025), arXiv:2405.10107v2.

[2] E. A. Sete, J. M. Gambetta, and A. N. Korotkov, "Purcell effect with microwave drive: Suppression of qubit relaxation rate," Phys. Rev. B 89, 104516 (2014), arXiv:1401.5545v2.

[3] M. Carroll et al., "Dynamics of superconducting qubit relaxation times," npj Quantum Information 8, 123 (2022).

[4] M. D. Reed et al., "Fast Reset and Suppressing Spontaneous Emission of a Superconducting Qubit," Appl. Phys. Lett. 96, 203110 (2010), arXiv:1003.0142v2.

[5] N. Hatano and G. Ordonez, "Time-Reversal Symmetry and Arrow of Time in Quantum Mechanics of Open Systems," Entropy 21, 380 (2019), arXiv:1903.05227v2.

[6] O. Axelsson, "Born's Rule from Reversible Evolution and Irreversible Outcomes," arXiv:2604.07418v1 (2026).

[7] F. Settimo and J. Piilo, "Quantum jump unravelings for non-Markovian open system dynamics: a review," arXiv:2605.07797v1 (2026).

[8] M. Tsang, "Quantum reversal: a general theory of coherent quantum absorbers," Quantum 9, 1650 (2025), arXiv:2402.02502v3.

[9] W. H. Zurek, "Decoherence, einselection, and the quantum origins of the classical," Rev. Mod. Phys. 75, 715 (2003).

[10] W. H. Zurek, "Quantum Darwinism," Nature Phys. 5, 181 (2009).

[11] H. Z. Huang, "Information-Capacity Bound on Non-Markovian Backflow" (PRL S1, 2026), 见 LP32/paper/prl_s1.tex.

[12] H. Z. Huang, "Two Rules to Build a Universe" (PRD, 2026), 见 LP32/paper/two_rules_prd_final.tex.

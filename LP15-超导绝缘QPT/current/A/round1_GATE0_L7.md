# LP-15 Round 1: GATE 0 文献搜索 + 先发风险评估 + 核心障碍分析 + L7 分解

**日期**: 2026-06-02
**角色**: A博士
**北极星命题**: LP-15 — 超导-绝缘体量子相变（SIT）的本质是什么？
**状态**: Round 1 草稿，待 B博士 审阅

---

## 1. GATE 0 文献搜索

### 1.1 核心综述

| 文献 | 年份 | 要点 |
|------|------|------|
| *Quantum Phase Transitions in Two-Dimensional Superconductors*, Rep. Prog. Phys. **87**, 014502 (2024) | 2024 | 全面综述2D超导体中的SIT/SMT，覆盖量子Griffiths奇异性、反常金属态、charge-2e量子振荡。DOI: 10.1088/1361-6633/ad14f3 |
| *Bose Metals, from Prediction to Realization*, Diamantini & Trugenberger, Materials **17**, 4924 (2024) | 2024 | Bose金属综述：论证反常金属是玻色拓扑绝缘体，无序非必需，已在有序Josephson结阵列中观测到 |

### 1.2 关键理论突破

| 文献 | 年份 | 要点 |
|------|------|------|
| Poboiko & Feigel'man, *Mean-field theory of first-order quantum superconductor-insulator transition*, SciPost Phys. **17**, 066 (2024) | 2024 | **一级相变理论**：长程Coulomb排斥使绝缘态成为Coulomb玻璃（有独立序参量），与超导态（XY序）之间因序参量不兼容导致一级相变。arXiv:2405.08571 |
| Yang & Chen, *Thermodynamic Theory of Disordered 2D Superconductors*, arXiv:2410.05216 (2024) | 2024 | 自洽热力学理论：长程Coulomb相互作用使2D超导序在Hohenberg-Mermin-Wagner-Coleman定理下存活，SIT由非均匀量子相位涨落解释 |

### 1.3 关键实验突破

| 文献 | 年份 | 要点 |
|------|------|------|
| Charpentier, Sacépé et al., *First-order quantum breakdown of superconductivity in an amorphous superconductor*, Nature Physics **21**, 104–109 (2025) | 2025.01 | **实验发现一级SIT**：a-InO薄膜微波谐振子测量，超流刚度在临界无序度处跳跃至零。Tc由超流刚度而非配对能隙决定——预示pseudogap机制。DOI: 10.1038/s41567-024-02713-8 |
| Yadav, Saravanan & Sahoo, *Emergence of quantum Griffiths singularity in disordered TiN thin films*, Communications Physics **7**, 215 (2024) | 2024 | TiN薄膜QGS同时出现在SMT和SIT中，发散动力学指数zv，磁阻等温线遵循IRFCP激活标度律 |
| Ienaga, Tamoto, Yoshimura, Ishigami & Okuma, *Broadened quantum critical ground state in a disordered superconducting thin film*, Nature Communications **15**, 1–7 (2024) | 2024 | Nernst效应测量：反常金属态被确认为SIT的**展宽量子临界态**而非独立相。量子临界点位于AM态内部。DOI: 10.1038/s41467-024-46628-7 |
| *Two-Step Superconductor-Insulator Transitions in Iron Chalcogenide Superconductors*, PRB **111**, L060506 (2025) | 2025.02 | Fe₂Te₁₋ₓSeₓ薄膜中观察到量子逾渗(zν≈2.28)和经典逾渗(zν≈1.35)的双步SIT |
| *Bosonic Phases across the SIT in Infinite-Layer Samarium Nickelate*, PRX **16**, 011029 (2026) | 2026.02 | Sm镍酸盐无限层薄膜中通过空间周期性网络图案观察到跨SIT的玻色相，磁阻振荡周期关联超导磁通量子 |

### 1.4 前沿发展

| 文献 | 年份 | 要点 |
|------|------|------|
| Cohen et al., *Pressure Induced Anomalous Metal in the Vicinity of the SIT*, arXiv:2504.04460 (2025) | 2025.04 | a-InO高压驱动：Bose绝缘体→超导体→金属相→常规绝缘体，重申2D金属存在 |
| Du et al., *Higgs Mode in Anomalous Metal of NbSe₂*, PRL **134**, 066002 (2025) | 2025 | 原子薄NbSe₂中Higgs模存活于反常金属态——表明Cooper对仍存在，但作者审慎未称Bose金属 |
| Das et al., *SIT in Weakly Monitored Josephson Junction Arrays*, PRB **112**, L180503 (2025) | 2025 | 弱连续监控驱动SIT——开辟"量子温度"和测量诱导相变新维度 |
| *Quantum criticality and tunable Griffiths phase in TTG*, arXiv:2507.10687 (2025) | 2025.07 | 扭转三层石墨烯中首次观测到磁场调谐的SIT Griffiths相，磁场倾斜可坍缩Griffiths区为单量子临界点 |
| Feigel'man, SFB Colloquium Regensburg (2024.05.28) | 2024 | 一级SIT的完整理论报告: [PDF](https://www.uni-regensburg.de/assets/physik/evers/SFB_Colloquium_Mikhail_Feigelman_28_05_2024.pdf) |
| Strunk, LPTMC Seminar Paris (2025.05.14) | 2025 | NbN薄膜BKT转变：强无序下相位涨落区覆盖85%平均场Tc，决定超流刚度的能量标度未知 |

---

## 2. 先发风险评估

### 2.1 该领域是否已被解决？

**回答：远未被解决，且2024-2025年处于范式震荡期。**

理由：

1. **一级-vs-连续之争重新燃起**：Carpentier/Sacépé (2025) 的一级SIT实验发现是颠覆性的，推翻了近40年来的"dirty boson标度假说"。Poboiko/Feigel'man (2024) 的一级相变理论将Coulomb相互作用提升为核心角色。但该理论尚未被同行广泛接受，且一级相变是否普遍适用（a-InO之外）完全未知。

2. **反常金属态性质未定**：虽有charge-2e量子振荡（2024）和Higgs模（2025）证据表明其玻色特性，但它是真正的热力学相、量子临界展宽区、还是有限温度赝象，三方争论中。

3. **量子Griffiths奇异性与一级SIT的关系未解**：TiN (2024) 和TTG (2025) 中的QGS/IRFCP行为与a-InO (2025) 中的一级跳跃能否共存于统一框架，目前毫无头绪。

4. **缺少统一相图**：材料从a-InO、a-MoGe、NbN、TiN、NbSe₂到镍酸盐，各有各的行为。没有理论能同时解释所有实验。

5. **Schmid-Bulgadaev问题虽已解决（2024-2025）**，但那是单个Josephson结的耗散相变，与二维无序超导薄膜的SIT本质上是不同问题。

### 2.2 是否有大型实验合作组垄断？

**回答：不存在垄断。这是典型的桌面凝聚态物理领域。**

主要研究组：

| 组别 | 位置 | 材料平台 | 角色 |
|------|------|----------|------|
| Sacépé / Néel Institute | Grenoble, France | a-InO薄膜 | **当前实验领军者**（2025 Nature Physics一级SIT） |
| Feigel'man / CENN + Ioffe | Ljubljana / Google Research | 理论 | **当前理论领军者**（2024 SciPost一级SIT理论） |
| Okuma / Tokyo Tech | Tokyo, Japan | a-MoₓGe₁₋ₓ薄膜 | Nernst效应探测SIT（2024 Nature Comms） |
| Kapitulnik / Stanford | California, USA | a-MoGe | 历史实验先驱（2000年hysteretic SIT） |
| Goldman / Minnesota | Minnesota, USA | 多种薄膜 | 历史实验先驱 |
| Strunk / Regensburg | Germany | NbN薄膜 | BKT/SIT交叉（2025 seminar） |
| Yadav & Sahoo | India | TiN薄膜 | QGS/SIT（2024 Comm Phys） |
| Cohen / Bar-Ilan | Israel | a-InO高压 | 高压反常金属（2025 arXiv） |
| Diamantini & Trugenberger | Italy/Switzerland | 理论 + JJ阵列 | Bose金属理论 |

这些是各自独立的中型大学研究组，相互之间存在合作但非垄断性大科学协作。**进入壁垒较低**：核心实验技术（微波谐振子测量超流刚度、低温输运）可在单个实验室完成，不需要同步辐射、中子源或大科学装置。

### 2.3 竞争态势

- **理论窗口期**：一级SIT理论（Poboiko/Feigel'man 2024）刚发表两年，尚未成为共识，存在大量尚未被占领的理论空间。
- **实验窗口期**：一级SIT仅在a-InO中被确认（2025），在其他材料体系（NbN, TiN, a-MoGe, 镍酸盐）中的行为完全未知。
- **综合窗口期**：一级相变、反常金属、QGS三者之间的关系是完全开放的问题——尚未有理论甚至提出要统一它们。

---

## 3. 核心障碍分析

### 3.1 为什么SIT的本质至今未定？

#### 障碍一：材料非普适性（Material Non-Universality）

SIT在不同材料体系中表现出质的差异：

| 材料 | 观察到的行为 | 难题 |
|------|------------|------|
| a-InO | 一级跳跃（超流刚度→0） | 是否因强Coulomb? |
| a-MoGe | 连续标度（zν≈2.3） | 为何不像a-InO一级？ |
| TiN | QGS + IRFCP | 与一级能否共存？ |
| NbN | BKT展宽（85% MF Tc） | 相位涨落主导，配对未破坏 |
| NbSe₂（晶体） | 反常金属 + Higgs模 | 有序vs无序的本质差异？ |
| Fe₂Te₁₋ₓSeₓ | 双步SIT（量子+经典逾渗） | 薄膜不均匀性的角色？ |

**核心问题**：我们不知道SIT是否存在普适类（universality class），还是多种不同物理机制在实验上被统称为"SIT"。

#### 障碍二：绝缘态的本质不明确

SIT的"绝缘体"一侧到底是什么，直接影响相变的性质：

- **Dirty boson模型的答案**：平凡局域化态——玻色子被无序势局域化，没有独立序参量。
- **Poboiko/Feigel'man的答案**：Coulomb玻璃——有Parisi型副本对称破缺序参量，是真正的有序态。
- **可能的第三种答案**：Bose绝缘体——与SIT不是同一个相变，可能是先配对再局域的两步过程。

目前没有实验能直接探测绝缘态的序参量。

#### 障碍三：反常金属态的干预

在SC→绝缘体的直接路径上，几乎所有实验都观测到反常金属（AM）/Bose金属态介入：
- 如果AM是真正的热力学相 → SIT不再是直接的SC-Insulator相变 → 论文的"北极星命题"可能需要重新表述。
- 如果AM是量子临界展宽（Okuma 2024） → SC和绝缘体之间的"过渡"本身就是量子临界区 → SIT仍是连续QPT。
- 如果AM是有限温度赝象 → T=0下SC和绝缘体之间是一级跳跃。

**三个可能性对应三种完全不同的SIT本质。**

#### 障碍四：预形成Cooper对（Pseudogap）使问题复杂化

Charpentier/Sacépé (2025) 的关键发现：
- T_c 由超流刚度Θ决定，而非配对能隙Δ
- 意味着在T_c以上（甚至在"绝缘"区），Cooper对已经预形成
- SIT的"绝缘"态可能仍含有玻色对——它是相位相干性的丧失，而非配对本身的破坏

这使得传统BCS框架下的SIT理论（Finkelstein, dirty boson）从根本上不适用——它们假设超导序参量振幅和相位同时消失。

#### 障碍五：多个微小能量标度的竞争

SIT发生在mK-1K温区，涉及的物理能量标度极小：
- Δ（配对能隙）～ 0.1-1 meV
- E_C（Coulomb能）～ 0.1 meV  
- E_J（Josephson耦合）～ 0.01-0.1 meV
- 无序宽度W ～ 1-10 meV

这些标度彼此接近，微小的材料差异即可改变物理。同时，测量精度要求极高——超流刚度变化<1%就可能是物理。

#### 障碍六：量子涨落与热涨落的纠缠

SIT本质上是T=0的量子相变。但在0.1 meV标度上（~1K），热涨落不可忽略。区分"真正的T=0量子临界行为"和"被热涨落模糊的经典相变"极度困难——需要对0.01-1K温区中的标度行为进行极其精确的分析。

---

## 4. L7 分解

### 4.1 精炼后的核心矛盾

**原始矛盾**：
- 命题A：SIT是真正的连续量子相变（T=0下的二阶相变）
- 命题B：SIT是有限温度下被热涨落模糊的"赝相变"

**精炼后的矛盾**（考虑2024-2025实验进展）：
- **命题A**：SIT是连续二阶量子相变，由单个量子临界点控制——dirty boson标度理论适用，无序破坏相位相干性但不改变绝缘态的平凡性质。
- **命题B**：SIT不是单一量子临界现象——它是预形成Cooper对的玻色系统中，超导态（XY序）与Coulomb玻璃绝缘态（ZZ自旋玻璃序）之间的一级相变，反常金属态是量子临界展宽区或中间玻色金属相。

### 4.2 L7 子命题分解

#### L1: 绝缘态的序参量 —— 平凡局域化还是Coulomb玻璃？

**问题**：SIT绝缘侧的基态是否有独立序参量？

- **H1 (Dirty Boson)**：绝缘态是平凡玻色局域化态。无独立序参量。从SC到绝缘体，只有相位相干性丧失→连续相变。
- **H2 (Coulomb Glass)**：绝缘态是Coulomb玻璃——由长程Coulomb排斥产生的Parisi型副本对称破缺态。与SC的XY序不兼容→一级相变。

**论证路径**：
- 理论：在Anderson赝自旋模型中精确处理Coulomb ZZ耦合，计算相图作为Δ和E_C的函数（推广Poboiko/Feigel'man 2024到非平均场）
- 实验预测：一级相变标志——超流刚度的有限最小值的材料参数依赖关系；Coulomb玻璃标志——绝缘侧的Efros-Shklovskii跳跃传导标度

**依赖关系**: 根节点，L3和L5依赖于L1的结论

---

#### L2: 反常金属态 —— 热力学相、临界展宽区、还是有限温度赝象？

**问题**：在所有SIT实验中出现在SC和绝缘体之间的反常金属态是什么？

- **H1 (临界展宽)**：AM是SIT量子临界点的展宽——T>0时量子临界的"量子扇"扩展到有限电阻区。支持证据：Okuma (2024) Nernst探测。
- **H2 (Bose金属相)**：AM是一个真正的热力学玻色金属相——Cooper对未凝聚但未局域化。支持证据：charge-2e量子振荡 (2024), Higgs模存活 (2025)。
- **H3 (有限温度赝象)**：T=0极限下AM消失，SC和绝缘体之间是一级跳跃。AM仅是T>0时一级跃迁被涨落平滑化的表观结果。

**论证路径**：
- 将T→0外推结果与理论预测对比：H1预测标度收敛到QCP；H2预测有限残余电导；H3预测跳跃
- 在多种材料中系统测量ρ(T→0, B)的极限行为

**依赖关系**: 依赖L1（如果绝缘态有独立序参量→有利于H3或H2）；为L5提供关键输入

---

#### L3: 相变阶数的材料依赖性 —— E_C/Δ 比值决定一切？

**问题**：一级SIT（a-InO）和连续SIT（可能a-MoGe, TiN）能否用同一框架理解？

- **H1 (普适一级)**：所有SIT本质上是一级的——之前观测到的连续行为是测量精度不足或热展宽的伪像。
- **H2 (材料依赖)**：SIT的阶由无量纲参数κ = E_C/Δ控制——κ ≫ 1 (强Coulomb) 一级；κ ≪ 1 (弱Coulomb) 连续。
- **H3 (混合场景)**：SIT在不同材料中确实是不同物理——强无序+强Coulomb (a-InO) vs 弱无序 (a-MoGe) vs 结晶 (NbSe₂) 属于不同普适类。

**论证路径**：
- 对多种材料（a-InO, a-MoGe, NbN, TiN, NbSe₂）进行微波谐振子超流刚度测量（重复Charpentier/Sacépé方法）
- 计算/估算各材料的E_C/Δ，与观测阶数对比
- 理论：构建统一的Landau-Ginzburg泛函，包含κ作为控制参数

**依赖关系**: 依赖L1（Coulomb玻璃序参量的存在性是H1/H2/H3抉择的前提）；为L5提供材料轴

---

#### L4: 预形成Cooper对 —— Pseudogap在SIT中的角色

**问题**：Charpentier/Sacépé (2025) 发现T_c由Θ而非Δ决定。这意味着Cooper对在Tc以上（甚至"绝缘"区）已预形成。这对SIT本质意味着什么？

- **H1 (相位唯象)**：SIT的"绝缘"侧实际是相位失相的玻色对系统。SIT仅是相位相干性的建立/丧失，与配对无关。支持Bose绝缘体→SC的图像。
- **H2 (两步相变)**：随着无序/磁场增加，先经历配对破坏（Δ→0，真正的超导-金属转变），再经历局域化转变——两个独立的量子相变。
- **H3 (伪能隙的费米弧解释)**：Pseudogap是费米学性质的——来自费米面重构而非玻色对。SIT仍是费米子标度理论描述。

**论证路径**：
- STM/ARPES直接测量"绝缘"侧的能隙——是超导能隙（玻色性质）还是Coulomb能隙（费米/无序性质）？
- 理论：构建显含预形成对的SIT有效理论，计算超流刚度和Tc的关系

**依赖关系**: 连接L1和L2——如果绝缘侧仍有Cooper对，则dirty boson框架需要修正；影响对反常态的解释

---

#### L5: 统一相图的构建 —— 能否将一级相变、反常金属、Griffiths奇异性放入同一张图？

**问题**：2024-2025的三条独立发展线——一级SIT (Sacépé), 反常金属Bose金属 (Diamantini/Cohen), QGS (Yadav/TTG)——能否被统一？

- **H1 (可统一)**：存在一个以E_C/Δ和W/Δ（无序强度/配对能隙）为轴的二维相图。一级相变发生在高E_C区，QGS发生在高无序区，AM是中间态。
- **H2 (不可统一)**：这三者是在不同物理条件下三个独立的、互不关联的现象集合，没有统一定义SIT的"本质"——"SIT"是一个伞式术语。

**论证路径**：
- 构建二维（或多维）相图，标注每个实验观测对应的参数区域
- 寻找跨越不同区域的通用标度形式或拓扑不变量
- 如果H1成立，应在相图中预测尚未被实验探索的过渡区域的行为

**依赖关系**: 综合L1-L4的结论——这是L7分解的"收敛点"，决定北极星命题能否以一个肯定句回答

---

#### L6: 量子Griffiths奇异性 —— 与一级相变相容还是互斥？

**问题**：TiN (2024) 和TTG (2025) 中QGS/IRFCP与a-InO (2025) 中一级跳跃是否描述了同一现象的不同侧面？

- **H1 (共存)**：QGS描述了"如何到达"一级相变点的路径——在接近临界点时，由于无序导致的稀有区域Griffiths效应，标度行为由IRFCP而非平均场描述。一级跳跃是终态（T=0），QGS是接近过程（T→0）。
- **H2 (互斥)**：QGS与一级相变互斥——IRFCP是无序驱动连续相变中稀有区域效应的数学结构。如果真实相变是一级的（有限跳跃），则IRFCP的稀有区域无穷级联不能出现。
- **H3 (无关)**：QGS是超导-金属转变（SMT）的特征，不是SIT的特征——TiN观测到的是两个不同的相变。

**论证路径**：
- 严格理论分析：在Coulomb玻璃+无序赝自旋模型中，稀有区域Griffiths效应是否被Coulomb长程作用抑制（H2）还是与一级跳跃共存（H1）？
- 实验：对同一样品（a-InO）进行磁阻标度分析——在观察到一级跳跃的同一体系中是否也存在QGS？

**依赖关系**: 依赖L1（如果是Coulomb玻璃→长程Coulomb可能抑制稀有区域效应→支持H2）和L3（材料依赖）

---

### 4.3 L7 依赖关系图

```
L1 (绝缘态序参量)
├──→ L3 (相变阶数材料依赖性)
│    └──→ L5 (统一相图) ←── L2 (反常金属态性质)
│         └──→ 北极星命题解答
├──→ L4 (预形成Cooper对/pseudogap)
│    └──→ L5
└──→ L6 (Griffiths奇异性与一级相容性)
     └──→ L5
```

### 4.4 执行优先级

按北极星优先级矩阵：

| 子命题 | 优先级 | 理由 |
|--------|--------|------|
| **L1** | ★★★★★ (最高) | **根源节点**：绝缘态的性质决定整个相变的阶。L3, L5, L6都依赖它。同时也是最容易通过理论分析打开的节点（推广Poboiko/Feigel'man模型） |
| **L4** | ★★★★ | **概念性杠杆**：预形成Cooper对的存在意味着"SIT"这个术语本身可能误导——相变可能仅是相位相干性丧失，而非超导电性丧失。重新定义问题的框架 |
| **L2** | ★★★★ | **观察量的解释瓶颈**：几乎所有SIT实验中AM态都出现。不解释它，就无法说理解了SIT |
| **L3** | ★★★ | 依赖L1的结论。如果L1确认Coulomb玻璃，则L3自动前进 |
| **L6** | ★★★ | 理论上有趣但可能不与一级相变在同一材料中共存 |
| **L5** | ★★ | 综合命题，依赖L1-L4的充分进度才能有意义地推进 |

---

## 5. 初步方法论建议

### 5.1 L1 优先推进路径

1. **精确理论计算**（可立即开始）：
   - 在Anderson赝自旋模型中，数值模拟N个局域轨道上的赝自旋系统（XY + ZZ耦合），计算超流刚度和Coulomb玻璃序参量
   - 目标：确认存在或否定Coulomb玻璃序参量在热力学极限下的稳定性
   - 技术路线：副本方法 + 腔体QED类比（超导谐振子可作为Coulomb玻璃的"探测器"）

2. **实验预测**（指导后续实验）：
   - 如果Coulomb玻璃正确 → 绝缘侧应出现Efros-Shklovskii lnσ ∝ T⁻¹/²跳跃传导 → 可在现有a-InO样品上直接验证
   - 如果dirty boson正确 → 绝缘侧应为Mott变程跳跃σ ∝ exp[-(T₀/T)ⁿ]，n取决于维度

### 5.2 可规避的陷阱

1. **不要混淆Schmid-Bulgadaev相变和SIT**：前者是零维单结问题，已基本解决；后者是二维多体问题，完全不同。
2. **不要假设"SIT"是一个东西**：L7的核心洞察可能是——"SIT"在不同材料、不同参数区间对应不同物理。承认这一点本身就是进展。
3. **不要低估Coulomb相互作用**：2024-2025的所有进展都指向Coulomb排斥是被忽视的关键因素。早期dirty boson模型正是因此失效。

---

## 6. GATE 0 结论

**GATE 0 通过条件**：
- [x] 核心矛盾已精炼（incorporating 2024-2025最新进展）
- [x] L7子命题已定义，依赖关系明确
- [x] 先发风险评估完成：领域未被解决，无垄断，有理论窗口期
- [x] 核心障碍已识别（6项）
- [x] 优先级已分配

**下一步**: 等待 B博士 审阅和修正。预计开始 L1 的理论分析。

---

*参考列表见第1节。完整bib可后续补充。*

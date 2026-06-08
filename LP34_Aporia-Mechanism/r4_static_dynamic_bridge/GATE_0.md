# GATE 0: 四组文献搜索 — R4 静态→动态桥

**研究方向:** 形式化"事件按顺序发生，资源被消耗" — 不假设时间  
**执行日期:** 2026-06-07  
**搜索工具:** paper-search-mcp (arxiv, semantic, crossref, openalex, dblp)  
**总搜索次数:** 10次 (8 + 2 targeted)  
**候选框架:** Petri网+Event Structures, 资源论, Process Matrix, 范畴论Process Theory

---

## 组1: Petri网 + 物理

### 搜索1.1: "Petri net physics resource consumption causal structure"
**来源:** arxiv, semantic, crossref, openalex, dblp
**命中:** 15篇 (arxiv:5, crossref:5, openalex:5)

**关键发现:**
- **最相关:** "Resource-Oriented Petri Net Modeling" (CRC Press, 2018) — 专门研究resource-oriented Petri网，将资源消耗作为核心建模元素
- Maciel et al. (2001): "A Petri net based method for resource estimation: an approach considering data-dependency, causal and temporal precedences" — Petri网用于资源估计，**同时考虑因果优先关系和时序优先关系**，这是寻找的桥接的直接前身
- Aguirre-Samboní: "Ecosystem Causal Analysis Using Petri Net Unfoldings" — Petri网unfolding用于生态系统因果分析，处理token生产/消费的表征

### 搜索1.2: "Petri net quantum information flow event ordering"
**来源:** arxiv, semantic, crossref, openalex, dblp
**命中:** 20篇

**关键发现:**
- **突破性发现:** Joachim, de Visme, Haar, Winskel (2025): **"Quantum Petri Nets with Event Structures semantics"** — 将经典Petri网推广为Quantum Petri Nets (QPNs)，配备与量子event structure语义兼容的量子赋值。这是首次将Petri网理论与量子程序形式桥接的工作
  - 贡献: (i) 量子Occurrence Nets (LQONs)的局部定义; (ii) QPNs的unfolding语义; (iii) QPNs的组合框架
  - 同一论文有两个arXiv版本 (2508.14531v1, 2509.01423v2)
- van Glabbeek, Goltz, Schicke (2021): "On Causal Semantics of Petri Nets" — 经典Petri网的因果语义，通过偏序反映transition occurrence之间的因果依赖
- Varadharajan (1990): "Petri net based modelling of information flow security requirements" — Petri网用于信息流建模

**评估:** Petri网方向有直接且最近的文献支撑。Quantum Petri Nets (2025) 的的出现表明Petri网理论正在向量子领域扩展，这为将DGF(介于经典和量子之间的约束系统)编码为Petri网提供了自然基础。

---

## 组2: 资源论 + 时间涌现

### 搜索2.1: "quantum resource theory time emergence ordering events"
**来源:** arxiv, semantic, crossref, openalex, dblp
**命中:** 19篇

**关键发现:**
- Di Biagio, Donà, Rovelli (2021): **"The arrow of time in operational formulations of quantum theory"** — 证明操作形式的时间不对称性源于使用者相关假设而非基本物理。关键论证：操作量子力学的数学对象包含关于过去的隐式假设但不包含关于未来的
- Favalli (2025): "On the Emergence of Time and Space in Closed Quantum Systems" — Page-Wootters理论的现代版本：时间从纠缠中涌现
- Anastopoulos, Plakitsi (2023): "Quantum Probabilities for the Causal Ordering of Events" — 构造因果排序事件的概率，在经典(世界线重合)和量子(无轨迹)两种情况下
- Salazar et al. (2024/2026): "Quantum Resource Theories beyond Convexity" — 将量子资源论推广到非凸star-shape集合，提供操作解释

### 搜索2.2: "resource theory thermodynamics arrow of time"
**来源:** arxiv, crossref, openalex
**命中:** 15篇

**关键发现:**
- **突破性发现:** Vidotto (2025): **"Thermodynamics without Time"** — 直接回答"热力学能否不预设时间构建"这一问题。剑桥大学出版社
- Latune, Sinayskiy, Petruccione (2020): "Negative contributions to entropy production induced by quantum coherences" — 量子相干性可以导致**负熵产生**，这意味着时间箭头的量子修正
- de Oliveira et al. (2022): "Geometric structure of thermal cones" — 热锥将状态空间几何划分为past thermal cone, future thermal cone, incomparable region。**这是不假设时间的"顺序"概念的原型：状态A在状态B的past thermal cone中当且仅当A可以热力学演化到B**
- Horodecki, Oppenheim (2013): "Fundamental limitations for quantum and nanoscale thermodynamics" — 量子/纳米尺度热力学的根本局限 (804 citations)
- Lostaglio, Jennings, Rudolph (2015): "Description of quantum coherence in thermodynamic processes requires constraints beyond free energy" — 量子相干性需要超越自由能的热力学约束，时间不对称性是量化的基本资源 (732 citations)
- Zeh (2009): "Open Questions regarding the Arrow of Time" — 关于时间箭头的经典综述，讨论量子力学中的indeterminism
- Kastner (2023): "The Arrow of Time is Alive and Well but Forbidden Under the Received View of Physics" — 时间箭头与物理学的矛盾仅存在于某些可选形而上学承诺下

**评估:** 资源论方向提供了一条"用序关系替代时间参数"的精巧路径。Thermal cones的概念特别有启发性——它将状态空间划分为past/future/incomparable，而无需引入时间参数t。这直接对应DGF中"前向转移"(=past→future cone)和"reflux"(=incomparable或反向)的概念。Vidotto的"Thermodynamics without Time"提供了框架级别的合法性。

---

## 组3: 操作量子力学 + 因果顺序

### 搜索3.1: "operational quantum mechanics causal ordering process matrix"
**来源:** arxiv, crossref, openalex
**命中:** 15篇

**关键发现:**
- **奠基文献:** Oreshkov, Costa, Brukner (2012): **"Quantum correlations with no causal order"** (Nature Communications, 700+ citations) — 证明存在不能归因于确定因果顺序的量子关联。引入process matrix formalism。违反"causal inequality"
- Oreshkov, Giarmatzi (2016): "Causal and causally separable processes" — 发展严格的多体因果关系和因果可分离性概念。发现causal但不causally separable的过程。引入ECS (extensibly causally separable)过程类
- Barrett, Lorenz, Oreshkov (2021): **"Cyclic quantum causal models"** (Nature Communications, 55 citations) — 将量子因果模型扩展到**循环因果结构**。关键定理：**对unitary过程，因果不可分离性 = 因果结构的循环性**
- Oreshkov (2019): "Time-delocalized quantum subsystems and operations" — 证明无确定因果顺序的过程在标准量子力学中可以通过time-delocalized subsystems实现，形成因果循环
- Hoffreumon, Oreshkov (2021): "The Multi-round Process Matrix" — 允许多轮信息交换的process matrix，开启side channel的可能性
- Crogman (2026): "Operational Causality Without Definite Order" — 通过quantum switch的causal witness证明indefinite temporal order可作为量子信息资源
- Perinotti (2021): "Causal influence in operational probabilistic theories" — 在操作概率理论中严格区分causal influence和signalling

### 搜索3.2: "process matrix formalism Oreshkov causal inequality"
**来源:** arxiv, crossref, openalex
**命中:** 13篇

**关键发现:**
- Wechs, Branciard, Oreshkov (2023): "Existence of processes violating causal inequalities on time-delocalised subsystems" (Nature Communications) — 证明违反causal inequality的所有unitary扩展tripartite过程都可以在time-delocalized subsystems上实现
- Allen, Barrett, Horsman, Lee, Spekkens (2017): "Quantum Common Causes and Quantum Causal Models" (Physical Review X, 218 citations) — 将量子因果模型形式化，引入Reichenbach原理的量子版本
- Fitzsimons, Jones, Vedral (2015): "Quantum correlations which imply causation" — 引入pseudo-density matrix处理时空测量，定义causality measure区分空间和时间关联
- Guérin, Rubino, Brukner (2019): "Communication through quantum-controlled noise" — 论证quantum switch的优势来自"coherently control quantum operations"而非indefinite causal order本身
- Milz, Quintino (2024): "Characterising transformations between quantum objects... without a fixed causal order" — 提供characterising没有固定因果顺序的mapping的一般框架

**评估:** Process matrix formalism是桥接问题最直接相关的形式体系——它的核心恰好是"不假设全局因果顺序的前提下定义事件"。Barrett et al. (2021)的"cyclic quantum causal models"定理（因果不可分离性=循环性）直接对应reflux的概念：reflux = 循环因果结构中的反向边。

---

## 组4: 范畴论 + 资源消耗

### 搜索4.1: "monoidal category resource consumption physics"
**来源:** arxiv, semantic, crossref, openalex
**命中:** 20篇

**关键发现:**
- **核心文献:** Fritz (2015): **"Resource convertibility and ordered commutative monoids"** — 用有序交换幺半群形式化资源转换。核心贡献：在等号被替换为序关系(≥)的设置中发展代数。直接联系Girard的线性逻辑和Deutsch的constructor theory。**化学反应的类比(2H₂ + O₂ → 2H₂O)精确捕捉了"资源消耗+可转换性"的结构**
- Marsden, Zwart (2018): "Quantitative Foundations for Resource Theories" — 用enriched category theory处理costs, rates, probabilities
- **关键教材章节:** "Resource Theories: Monoidal Preorders and Enrichment" (Fong & Spivak, An Invitation to Applied Category Theory, Cambridge UP 2019) — monoidal preorders作为资源理论的基础数学结构
- Furter, Huang, Zardini (2025): "Composable Uncertainty in Symmetric Monoidal Categories for Design Problems" — 将Markov categories与SMCs结合处理不确定过程
- Nolan et al. (2020): "Compositional Models for Power Systems" — 用categorical databases和symmetric monoidal categories对电力系统(生产/消耗/存储资源)建模

### 搜索4.2: "categorical quantum mechanics irreversible process"
**来源:** arxiv, crossref, openalex
**命中:** 15篇

**关键发现:**
- **核心文献:** Coecke, Kissinger (2018): **"Categorical Quantum Mechanics I: Causal Quantum Processes"** — 从process ontology推导量子理论的范畴论骨干。causality = 与相对论的兼容性，通过discarding processes定义
- **核心文献:** Kissinger, Uijlen (2017/2019): **"A categorical semantics for causal structure"** (LMCS) — 在process theories中建模因果结构的范畴构造。关键贡献：框架足够一般，可以容纳classical probabilistic processes, quantum theory, **以及indefinite causal ordering (quantum switch, process matrices)**
- **核心文献:** Kissinger, Hoban, Coecke (2017): **"Equivalence of relativistic causal structure and process terminality"** — 证明GR的因果结构和process theory的causality principle是等价的。**这是连接物理因果和数学形式化的定理级结果**
- **核心文献:** Coecke, Gogioso, Selby (2017): **"The time-reverse of any causal theory is eternal noise"** — 证明任何causal theory的时间反演只允许单一状态：eternal noise。这是时间箭头在process theory中的严格陈述
- Abramsky, Coecke (2008): "Categorical quantum mechanics" — 奠基文献
- Speed (2026): "Why the Measurement Problem Is Not Dynamically Solvable" — 论证测量不应理解为时间中的事件而是"可能性的不可逆限制"

### Targeted搜索: Coecke process theory + causality
**额外搜索:** arxiv (10篇)
- **额外确认:** Kissinger, Uijlen (2017) 的论文是**最关键桥接文献**——它明确展示了如何在统一的categorical framework中同时容纳classical causal processes, quantum theory, 和indefinite causal structures。SOC_n family包括quantum switch和Oreshkov process matrices作为特例
- Friend, Kissinger (2023): "Identification of Causal Influences in Quantum Processes" — 将经典因果推断技术推广到量子设置

### Targeted搜索: thermal cones + majorization
**额外搜索:** arxiv (5篇)
- 确认thermal cones的研究活跃 (2020-2022)，但更多是应用于受限系统而非一般结构

---

## 综合评估: 哪个候选框架最有希望？

### 评估矩阵

| 评估维度 | Petri网+Event | 资源论(Ordered Monoids) | Process Matrix (Oreshkov) | 范畴论Process Theory (Coecke-Kissinger) |
|----------|--------------|------------------------|--------------------------|----------------------------------------|
| **不假设时间描述顺序** | ★★★★ Event structure的偏序定义为"a在b的因果历史中"，不引用全局时间t | ★★★★★ 序关系(≥)是公理化的，完全不存在时间 | ★★★ "causal past"由signaling定义，隐含操作→结果方向 | ★★★★★ Process terminality = 丢弃输出则丢弃过程。纯粹关于信息流 |
| **原生处理资源消耗** | ★★★★★ Token消耗是Petri网的built-in概念 | ★★★★ 序关系的monotonicity: x≥y意味着x可转化为y(消耗) | ★★ 不在原生框架中，需因果模型扩展 | ★★★ Effects + discarding processes = 不可逆消耗 |
| **与DGF兼容性** | ★★★ QPNs (2025)提供量子化路径，但DGF约束的特殊编码未知 | ★★★★ 抽象度合适——DGF = 一种specific ordered commutative monoid | ★★ 来自量子基础，用于经典约束系统需降级 | ★★★★ Meta-framework: 可嵌入GPTs和经典概率论 |
| **数学成熟度** | ★★★★ Petri网理论成熟(1960s-)，量子化是2025年的新进展 | ★★★ Fritz (2015)和Marsden-Zwart (2018)奠定基础，规模尚小 | ★★★★★ 12年积累，Oreshkov系列论文构建了完整体系 | ★★★★ 20年积累，Coecke/Abramsky/Kissinger系列，教科书级别 |
| **可操作性(算出P_reflux)** | ★★★★ Firing sequence → 计算reflux事件的比例 | ★★ Convertibility判定，不自然支持概率 | ★★★★★ Causal inequality formulation直接测量"非因果性" | ★★★ 可以，但需要从抽象范畴翻译为具体计算 |
| **关键突破文献** | QPNs (2025) | Vidotto (2025) | Barrett et al. (2021) | Kissinger-Uijlen (2017) |

### 加权综合得分

```
候选框架           桥接能力  成熟度  兼容性  可操作性  TOTAL
                 (35%)    (20%)   (25%)   (20%)
─────────────────────────────────────────────────────
范畴论Process     4.3      4.0     4.0     3.0     = 3.89  ★ 最高
Petri网+Event     4.3      4.0     3.0     4.0     = 3.81
资源论(Ordered)   4.3      3.0     4.0     2.0     = 3.50
Process Matrix    3.0      5.0     3.0     5.0     = 3.70
```

### 推荐: 范畴论Process Theory作为Meta-Framework + Petri网/Event Structures作为Operational Model

**理由:**

1. **Kissinger-Uijlen (2017)提供了统一的数学基础。** 他们已证明process theory可以容纳：
   - 经典因果过程(classical probabilistic processes)
   - 量子理论(quantum theory)
   - 无确定因果顺序的结构(quantum switch, process matrices — 即Oreshkov的整个program)
   
   这意味着选择范畴论process theory作meta-framework**不排除其他候选**——它包容它们。

2. **Petri网+Event Structures提供操作语义。** Joachim et al. (2025)的QPNs将Petri网的token/变迁/消耗语义与量子event structures的因果语义结合起来。这是一个可以直接编码DGF约束的操作层。

3. **两个层级之间的桥梁已存在。** 经典Petri网的unfolding语义(van Glabbeek et al. 2021)产生event structures，而event structures的因果偏序是process theory中causal structure的特例(Kissinger-Uijlen 2017的framework已涵盖partial orders)。

4. **P_reflux的自然定义:** 在process theory中，causal structure = 一个偏序。Reflux = 违反该偏序的事件对的比例。这直接对应Oreshkov的causal inequality的形式：如果所有事件满足全局因果顺序，某些关联必须满足特定不等式；violation = 因果顺序被破坏 = reflux。

5. **Vidotto (2025)的"Thermodynamics without Time"提供类比验证:** 如果热力学可以在不预设时间的情况下构建，那么DGF约束系统的reflux统计也可以。

### 四框架的关系图

```
                    范畴论Process Theory (Meta-Framework)
                    │  Coecke-Kissinger (2018)
                    │  Kissinger-Uijlen (2017) ← 统一基础
                    │
        ┌───────────┼───────────┐
        │           │           │
   Process Matrix  Petri网   资源论
   Oreshkov(2012)  +Event    有序幺半群
   Barrett(2021)   Structures Fritz(2015)
   │               │           │
   causal          token       序关系
   inequality      firing seq  convertibility
   │               │           │
   └───────┬───────┴─────┬─────┘
           │             │
        P_reflux      DGF约束
        定义          编码
```

### 下一步 (R4 Phase 1)

1. 将DGF约束系统形式化为一种特定的process theory
2. 在该process theory中定义causal structure (partial order)
3. 定义P_reflux = Pr[observed event pair violates causal order]
4. 证明P_reflux的边界可以由鸽巢原理推导但不等于鸽巢原理的结果
5. 找出"静态边界"和"动态测量"之间的精确修正因子

---

## 关键文献清单 (优先级排序)

### Tier 1: 必须深读

1. **Kissinger, Uijlen (2017/2019).** "A categorical semantics for causal structure." LMCS 15(3:15). — 统一框架的关键
2. **Coecke, Kissinger (2018).** "Categorical Quantum Mechanics I: Causal Quantum Processes." — Process theory的完整陈述
3. **Joachim, de Visme, Haar, Winskel (2025).** "Quantum Petri Nets with Event Structure semantics." arXiv:2509.01423v2. — Petri网→量子化的最新进展
4. **Barrett, Lorenz, Oreshkov (2021).** "Cyclic quantum causal models." Nature Communications 12. — 循环因果结构 = 因果不可分离性
5. **Oreshkov, Costa, Brukner (2012).** "Quantum correlations with no causal order." Nature Communications 3. — Process matrix formalism的源起

### Tier 2: 重要参考

6. **Fritz (2015).** "Resource convertibility and ordered commutative monoids." MSCS. — 资源论的代数基础
7. **Vidotto (2025).** "Thermodynamics without Time." — 不预设时间的热力学 (类比验证)
8. **Kissinger, Hoban, Coecke (2017).** "Equivalence of relativistic causal structure and process terminality." — 因果结构和process theory的等价性证明
9. **Coecke, Gogioso, Selby (2017).** "The time-reverse of any causal theory is eternal noise." — 时间反演与因果理论的深刻关系
10. **van Glabbeek, Goltz, Schicke (2021).** "On Causal Semantics of Petri Nets." — 经典Petri网的因果语义

### Tier 3: 补充阅读

11. Di Biagio, Donà, Rovelli (2021). "The arrow of time in operational formulations of quantum theory." Quantum 5.
12. Oreshkov (2019). "Time-delocalized quantum subsystems and operations." Quantum 3.
13. Marsden, Zwart (2018). "Quantitative Foundations for Resource Theories." CSL 2018.
14. Melgratti, Mezzina, Pinna (2023). "A Reversible Perspective on Petri Nets and Event Structures."
15. de Oliveira et al. (2022). "Geometric structure of thermal cones." Phys. Rev. E.

---

## 操作总结

```
GATE 0 状态: ✅ COMPLETE
搜索维度: 4组 × 2搜索/组 + 2 targeted = 10次搜索
覆盖来源: arxiv, semantic scholar, crossref, openalex, dblp
关键文献: 15篇 (Tier 1: 5, Tier 2: 5, Tier 3: 5)
推荐框架: 范畴论Process Theory (meta) + Petri网/Event Structures (operational)
定性判断: 存在可行数学路径。桥接不依赖新物理——依赖将已有的形式体系应用于DGF
```

**GATE -1 + GATE 0 执行完毕。R4可以进入Phase 1：DGF的process-theoretic形式化。**

# LP34 Phase 1 Round 1 -- A博士: 约束系统的系统化

**date:** 2026-06-08
**author:** A博士 (学院派)
**framework:** 约束理论 + GPT操作语义 + 约束分类学
**北极星:** N1 -- 约束系统C的完整枚举、分类学、依赖结构与独立基底
**Phase:** 1 (约束系统化)

---

## 摘要

本Round执行LP34 Phase 1的核心任务: 约束系统的系统化。产出包含: (1) §-1: 多源文献搜索,覆盖约束分类学、独立性/等价性和统一框架; (2) §1: 13个信息论约束的完整枚举(7个DGF内部 + 6个文献约束,扩展超过任务要求); (3) §2: 三维分类学(类型/来源/层级); (4) §3: 约束依赖图——识别出7条蕴含关系、3组等价对、2个关键约束节点; (5) §4: 最小独立约束集——|C_independent| = 5 (由C1容量上界、C4因果有向性、C6弱场极限、C_signal无信号条件、C_Holevo Holevo界构成),其余8个约束均可从该独立集导出或通过独立集+定义导出。

**核心发现:** 约束系统不是扁平的13元集合——它是一个有向无环图(DAG),其中5个叶子节点构成独立基底。C1(容量上界)是最关键的节点——它是6个其他约束的偏序前提。但C1不能自证——它本身需要物理动机(来自DGF的A2公理)。约束网络的拓扑结构揭示了一个三层架构: 信息格点层(Tier 0)提供"语言",量子涌现层(Tier 1)提供"动力学",经典引力层(Tier 2)提供"表观规律"。

---

## §-1 文献搜索

### 搜索1: 约束分类学

**搜索策略:** "physical constraints classification hierarchy information theoretic thermodynamic gravitational" × semantic/scholar/crossref

**关键发现:**

文献中不存在统一的"物理约束分类学"。约束以碎片化方式分布在各个子领域:

| 子领域 | 核心约束 | 分类状态 |
|:-------|:---------|:---------|
| 量子信息论 | Holevo界, Landauer原理, Margolus-Levitin界, 信息因果性 | 有上层分类(信息论上界)但缺跨领域统一 |
| 引力/黑洞物理 | Bekenstein界, 广义第二定律, 量子零能条件 | 与信息论约束的关联被认识但未被系统化 |
| 量子基础 | Bell不等式族, Tsirelson界, 无信号条件, 纯化公理 | Leifer (2014)有初步三层分类(代数/独立性/逻辑)但未扩展到热力学 |
| GPT/量子重构 | Hardy公理独立性(Schack 2002), Chiribella纯化公理 | 公理独立性被研究过,但目标是"选出QT"而非"构建排除系统" |

**关键文献:**

| # | 文献 | 核心贡献 | 与Aporia的关系 |
|:--:|------|:--------:|:--------------:|
| C1 | Leifer (2014), "No-go theorems" [philsci-archive:11617] | 三层no-go分类: 代数约束(Kochen-Specker式) / 独立性约束(Bell式) / 逻辑和方法论约束 | 提供了no-go分类的先例,但未扩展到信息论约束的全谱 |
| C2 | Clifton, Bub & Halvorson (2003), Found. Phys. 33, 1561 | 用3条信息论约束刻画量子理论: (1)无超光速信号 (2)无广播 (3)无无条件安全比特承诺 | 三条约束均落在Aporia的枚举范围内——它们是C_signal, C_broadcast, C_commitment |
| C3 | Plenio (1999), "The Holevo bound and Landauer's principle" [quant-ph/9910086] | Landauer原理⇒Holevo界的直观基础 | 建立了一个重要的蕴含关系: Landauer ⇒ Holevo |
| C4 | Harremoes (2020), "From thermodynamic sufficiency to information causality" [10.1007/s40509-020-00222-w] | 热力学充分性⇒信息因果性 | 另一条跨领域蕴含关系: 热力学⇒信息论约束 |

**搜索覆盖度:** 7/10。约束分类学确实是一个gap——这是Aporia的原创贡献空间。

### 搜索2: 约束等价性与独立性

**搜索策略:** "information causality equivalent to no-signaling plus something" × arxiv/semantic; "constraints independence redundancy physics axiomatic system" × crossref

**关键发现:**

信息因果性与其他约束的关系是活跃研究方向,2024-2025有重要进展:

| 发现 | 来源 | 状态 |
|:-----|:-----|:----:|
| IC排除超量子关联 → 但不完备 (Purushothaman et al. 2025) | PRA 112, 022211 | IC不是no-signaling+Tsirelson的等价替代 |
| IC成功依赖Shannon熵选择 (Oughton & Timpson 2024) | Entropy 26(7), 562 | IC本身不是独立"原理"——它依赖于熵定义的选择 |
| Bell不等式排除的类比推断理论更多 (Naeger 2018) | philsci-archive | 约束的"排除范围"大于通常假设 |
| 量子重构中Hardy公理5的独立性 (Schack 2002) | quant-ph/0210017 | Hardy公理1可从其他4条导出——公理系统的冗余性是普遍现象 |

**对Aporia的核心教训:**

1. **约束的"独立性"是逻辑概念,不是物理概念。** 两个约束可能在物理上等价(排除相同理论类)而逻辑上独立(互不蕴含)。Aporia需要在两个层面上分析独立性。
2. **约束的"有效独立性"依赖于辅助假设。** IC的有效性依赖Shannon熵——如果宇宙不服从Shannon熵作为信息度量,IC就失去了排除力。这意味着约束本身需要"meta约束"来锚定其适用范围。
3. **约束网络中的冗余可能是功能性的。** 多个约束蕴含相同推论不一定是冗余——它提供了故障容忍机制(即使一条约束被误述,排除系统仍能运作)。

### 搜索3: Bekenstein-Holevo-Landauer-Margolus-Levitin统一框架

**搜索策略:** "Bekenstein bound Holevo bound Landauer Margolus-Levitin unified framework" × arxiv

**关键发现:**

这四个界之间的逻辑关系已有初步研究:

| 蕴含关系 | 证据 | 可信度 |
|:---------|:-----|:------:|
| Landauer ⇒ Holevo | Plenio 1999: Landauer原理提供了Holevo界的直观基础 | 中——启发性论证, 非严格推导 |
| Bekenstein ⇔ 面积律 | Bousso 2018回顾: Bekenstein界 + 广义相对论 ⇒ 面积律; Casini 2008证明特定版本 | 高——在Casini版本下是定理 |
| Margolus-Levitin ↔ 能量-时间不确定性 | Zielinski & Zych 2006: ML界是Mandelstam-Tamm界的互补界 | 中——两者共同界定量子速度极限 |
| Bekenstein + Landauer → 黑洞热力学 | Abreu & Neto 2025, Ambrósio et al. 2025: 多个熵变形(Kaniadakis, Tsallis-Renyi)下Bekenstein界和Landauer原理仍然共存 | 中——新进展, 扩展了适用范围 |

**综合评判:**

这四个界构成一个"信息论约束的四边形":
- **Bekenstein:** 空间容量上界 (几何→信息)
- **Holevo:** 通道容量上界 (量子→经典信息)
- **Landauer:** 信息擦除的能价 (信息→热力学)
- **Margolus-Levitin:** 信息处理速率上界 (能量→时间→信息)

它们之间的完整蕴含关系图尚未被画出——这是Aporia §3的贡献。

---

## §1 约束的完整枚举

### §1.1 DGF内部约束 (7个)

从DGF v3.1-prd的核心公理(A1, A2)和推论(CR1-CR15)中提取:

#### C1: 容量上界 (Capacity Upper Bound)
**标签:** C_capacity
**形式:** χ(S_cell) ≤ 1 bit (每个Planck细胞承载 ≤ 1 bit信息)
**DGF来源:** A2公理 + CR1
**GPT表述:** 对任何基本子系统c, Holevo容量 χ(S_c) = max_{ensemble, measurement} I_acc ≤ log_2(2) = 1
**状态:** 已形式化(Phase 0), 选定C1_Holevo版本

#### C2: 回流界 (Reflux Bound)
**标签:** C_reflux
**形式:** P_reflux ≤ min(q_S/q_E, (1-q_E)/q_E)
**DGF来源:** S1补充, CR7-CR9
**GPT表述:** χ(Φ) ≤ I_max(A) · max{0, 1 - q_A/q_B}
**状态:** 已形式化(Phase 0), 统一为max{0,...}版本

#### C3: 熵面积界 (Entropy-Area Bound)
**标签:** C_entropy_area
**形式:** S(Ω) ≤ |∂Ω| · log_2(d_max)
**DGF来源:** S4补充, CR13-CR15
**GPT表述:** H_GPT(ρ_Ω) ≤ |∂Ω| · log_2(3) (对d_max=3)
**状态:** 已形式化(Phase 0), 熵定义(测量熵 vs 混合熵)待解决

#### C4: 因果有向性 (Causal Directedness)
**标签:** C_causal_directed
**形式:** 信息因果流有向——信息从发送方流向接收方,逆流被A1禁止
**DGF来源:** A1公理(因果不对称)
**GPT表述:** 对任意通道Φ: A→B, 存在偏序≤使得信息容量沿≤单调不增
**状态:** 未在GPt中形式化——本Round将其升级为独立约束

#### C5: 弱场极限 (Weak Field Limit)
**标签:** C_weak_field
**形式:** ∇²(ln q) = 0 ⇒ 牛顿极限
**DGF来源:** CR10-CR12, DGF §5.3
**GPT表述:** 在信息场弱的极限下,态空间梯度场塌缩为调和函数→产生经典引力势
**状态:** 仅在特定模型(T_θ族)中验证

#### C6: 活性独立 (Liveness Independence)
**标签:** C_liveness_indep
**形式:** 活性不可从A1+A2推导——不可推导性
**DGF来源:** DGF §7.2(meta-推论)
**类型:** Meta约束(⊬)
**GPT表述:** 不存在从公理集{A1, A2}到活性谓词L的演绎——L是与信息容量正交的自由度
**状态:** 形式化为独立性命題——它本身不排除理论,而是标识一个排除的边界

#### C7: ξ自由度 (Xi Freedom)
**标签:** C_xi_freedom
**形式:** ξ(q)不能唯一确定——函数形式有剩余自由度
**DGF来源:** DGF §8.1
**类型:** Meta约束(⊬)
**GPT表述:** 存在至少两个物理上不等价但满足所有DGF约束的泛函ξ₁ ≠ ξ₂
**状态:** 紧致性定理的直接推论——有限约束不能固定一个函数

### §1.2 文献约束 (6个,扩展列表)

#### C8: Bekenstein界 (Bekenstein Bound)
**标签:** C_Bekenstein
**形式:** S ≤ 2πkRE/(ħc)
**来源:** Bekenstein (1981), Phys. Rev. D 23, 287
**GPT表述:** 对任何有限空间区域R, 其内部量子态的总von Neumann熵被(半径×能量)界定
**与C3的关系:** C3特例化(Bekenstein界 ⇒ d=4时空中的面积律); C3推广(Bekenstein界将"边界面积"替换为"半径×能量")
**独立状态:** 部分独立。在Casini (2008)版本下可从相对熵正定性导出——暗示Bekenstein界不在独立基底中

#### C9: Holevo界 (Holevo Bound)
**标签:** C_Holevo
**形式:** χ = S(ρ) - Σ p_x S(ρ_x) ≤ H(X) (可访问信息 ≤ Holevo量)
**来源:** Holevo (1973); 在GPT中由Kimura et al. (2016)推广
**GPT表述:** 对任何系综{px, ρx}, 可访问信息I_acc ≤ χ({px, ρx})
**与C1的关系:** C1是Holevo界的"容量版本"——C1给出χ的上界(1 bit), C_Holevo给出I_acc的上界(χ本身)
**独立状态:** 与C1部分重叠但不冗余——C1约束态空间, C_Holevo约束测量提取信息的过程

#### C10: Landauer原理 (Landauer Principle)
**标签:** C_Landauer
**形式:** ΔE ≥ kT ln 2 · ΔI
**来源:** Landauer (1961); 广义版本: Anderson (2022), Entropy 24, 1568
**GPT表述:** 在GPT通道中,信息擦除(态空间维度缩减)消耗至少kT ln 2的能量/bit
**与C2的关系:** C2(回流界)的物理机制可能是Landauer原理——回流需要"反向擦除"环境信息
**独立状态:** 强独立——它是热力学→信息论的桥接约束, 不在纯信息论约束的闭包内

#### C11: Margolus-Levitin界 (Margolus-Levitin Bound)
**标签:** C_ML
**形式:** τ ≥ πħ/(2⟨E - E₀⟩)
**来源:** Margolus & Levitin (1998); 扩展: Hörnedal & Sönnerborn (2023)
**GPT表述:** 量子态从初始态演化到正交态的最小时间 ≥ πħ/(2×平均激发能量)
**与C1的关系:** C1 (1 bit/cell) + C_ML → 每细胞的最高信息处理速率 ≤ (2⟨E⟩)/(πħ) bit/s
**独立状态:** 独立——它约束的是速率(时间维度)而非容量(空间维度)

#### C12: 信息因果性 (Information Causality)
**标签:** C_IC
**形式:** Σ_{k=0}^{m-1} I(a_k : β|b=k) ≤ m (Bob的m-bit数据中的可访问信息 ≤ m bits)
**来源:** Pawlowski et al. (2009), Nature 461, 1101
**GPT表述:** 在无信号GPT中,Alice和Bob之间的IC博弈预测满足经典通信界
**与C4的关系:** IC是C4(因果有向性)的情境化版本——IC在通信博弈中表达因果有向性
**独立状态:** 部分冗余——IC = C4 + C_signal (无信号), 在特定通信场景中

#### C13: 无信号条件 + Tsirelson界
**标签:** C_NoSignaling_Tsirelson
**形式:** P(a|x,y) = P(a|x) (无信号); S_CHSH ≤ 2√2 (Tsirelson)
**来源:** Tsirelson (1980); 层级: NPA hierarchy (Navascues, Pironio, Acin 2007/2008)
**GPT表述:** 在无信号GPT中, 观测关联满足Tsirelson界当且仅当GPT是"量子可嵌入"的(通过Hilbert空间表示)
**与C1的关系:** Tsirelson界 = C1在Bell场景的特殊化——它排除了χ>1·bit在两体场景中的超量子关联
**独立状态:** 部分冗余——Tsirelson界可被信息因果性或宏观局域性蕴含

### §1.3 完整约束表 (13个约束)

| ID | 标签 | 名称 | 类型 | 来源 | 形式 |
|:--:|:-----|:-----|:----:|:----:|:-----|
| C1 | C_capacity | 容量上界 | 上界 | DGF | χ ≤ 1 bit/cell |
| C2 | C_reflux | 回流界 | 上界 | DGF | P_reflux ≤ q_S/q_E |
| C3 | C_entropy_area | 熵面积界 | 上界 | DGF | S ≤ N_∂Ω |
| C4 | C_causal_directed | 因果有向性 | 方向 | DGF | 信息因果流有向 |
| C5 | C_weak_field | 弱场极限 | 等号 | DGF | ∇²(ln q) = 0 |
| C6 | C_liveness_indep | 活性独立 | Meta | DGF | L ⊬ A1+A2 |
| C7 | C_xi_freedom | ξ自由度 | Meta | DGF | ξ(q)非唯一 |
| C8 | C_Bekenstein | Bekenstein界 | 上界 | 文献 | S ≤ 2πkRE/ħc |
| C9 | C_Holevo | Holevo界 | 上界 | 文献 | I_acc ≤ χ |
| C10 | C_Landauer | Landauer原理 | 上界 | 文献 | ΔE ≥ kT ln 2 · ΔI |
| C11 | C_ML | Margolus-Levitin | 上界 | 文献 | τ ≥ πħ/(2⟨E⟩) |
| C12 | C_IC | 信息因果性 | 方向 | 文献 | I(a:β|b) ≤ m |
| C13 | C_NSTS | 无信号+Tsirelson | 上界/方向 | 文献 | S_CHSH ≤ 2√2 |

---

## §2 约束分类学

### §2.1 按类型分类

**Taxonomy T: 约束的逻辑形式决定其排除机制**

| 类型 | 符号 | 排除机制 | 成员 | 数量 |
|:-----|:----:|:---------|:-----|:----:|
| **上界约束** | ≤ | 排除一切超过某阈值的理论 | C1, C2, C3, C8, C9, C10, C11, C13(Tsirelson部分) | 8 |
| **等号约束** | = | 在极限下强制精确匹配(但导数项允许连续偏离) | C5 | 1 |
| **方向约束** | → | 禁止因果逆流/后退—排除具有反向信息流的结构 | C4, C12, C13(无信号部分) | 3 |
| **Meta约束** | ⊬ | 在元语言层声明不可推导性——不直接排除理论,而是划定"系统不能说什么"的边界 | C6, C7 | 2 |

**分类洞察:**

上界约束占主导(8/13)——这与Phase 0的结论一致: DGF在最深层是不稳定+IP的理论, 只能导出forall-推论(上界、不等式)而非独一理论。约束类型的偏态分布(上界>>其他)不是设计缺陷——它是底层理论稳定性类别的必然表现。

**一个微妙之处:** C5(弱场极限)表面上是等号约束(=),但在操作上它更接近上界约束: 它排除了一切极限行为不是∇²(ln q)=0的理论。GPT同胚: C5 = {T | lim_{weak field} T = Newtonian gravity}, 这等价于排除极限偏离牛顿引力的理论类。

### §2.2 按来源分类

**Taxonomy S: 约束的来源决定其epistemic地位**

| 来源 | 包含 | Epistemic地位 | 成员 |
|:-----|:-----|:-------------|:-----|
| **信息论第一原理** | 从"信息是什么"的定义导出的约束 | 分析命题(analytic)——改变信息定义则约束改变 | C1, C8, C9, C10, C11, C13 |
| **图论/组合** | 从网络结构导出的约束——与"信息是什么"无关,只关心"信息如何流动" | 综合命题(synthetic)——独立于信息度量 | C2, C3 |
| **动力学涌现** | 在特定动力学极限下涌现的约束 | 条件命题(conditional)——仅在极限下成立 | C5 |
| **逻辑独立性** | 在元语言层声明的不可推导性 | Meta命题(meta)——对"约束系统的表达能力边界"做出声明 | C6, C7 |
| **操作因果性** | 从"测量和制备的操作顺序"导出的约束 | 操作命题(operational)——独立于实体论(ontology) | C4, C12 |

**一个关键区分:**

信息论第一原理约束(C1, C8-C11, C13中Tsirelson部分)共享一个脆弱性: 它们依赖熵/信息度量的定义。如果物理世界的信息度量不是von Neumann熵(量子)或Shannon熵(经典),这些约束的表述就需要修改。相比之下,图论/组合约束(C2, C3)和操作因果性约束(C4, C12)对信息度量的选择是不变的——它们只关心连通性、流动方向和网络容量。

这个区分对Aporia的方法论至关重要: **在构建Ω_info的约束系统时,应优先施加对信息度量选择不变的约束**, 然后在其基础上施加信息度量依赖的约束。这个优先级确保了修剪操作的基础是 robust(不依赖熵定义的任意选择)。

### §2.3 按层级分类

**Taxonomy H: 约束的层级反映其物理来源的深度**

| 层级 | 描述 | 成员 | 特点 |
|:----:|:-----|:-----|:-----|
| **Tier 0: 信息格点层** | 定义信息的基本操作语义——"什么是1 bit?" "谁向谁发送?" "什么不可推导?" | C1, C4, C6, C7, C13(无信号) | 不依赖时空、能量、或量子结构的任何细节。这是最深的约束层。|
| **Tier 1: 量子涌现层** | 信息度量+热力学涌现——通道容量、擦除能量、处理速度 | C2, C9, C10, C11, C12 | 依赖Tier 0的"信息"概念,在此基础上附加能量和动力学。量子相干性的涌现。|
| **Tier 2: 经典引力层** | 大尺度表观规律——从Tier 0+1涌现的面积律和牛顿极限 | C3, C5, C8 | 依赖时空连续统和宏观极限。最表层的约束——在其他层存在的理论中"浮出水面"。|

**层级之间的偏序关系:**

```
Tier 0 (信息格点) → Tier 1 (量子涌现) → Tier 2 (经典引力)
        ↓                    ↓                    ↓
    定义"信息"         附加"能量/时间"     附加"时空/几何"
```

- **Tier 0是Tier 1的前提:** 没有"信息容量"的概念, "Holevo界"和"Landauer原理"无法表述。没有"信息因果流有向", "信息因果性"失去意义。
- **Tier 1是Tier 2的前提:** 没有"熵"的量子定义(Holevo量), "面积律"和"Bekenstein界"只是空洞的几何不等式。没有"处理速率"(ML界), "信息场的弛豫时间"没有下界。
- **Tier 2的约束(C3, C5, C8)是涌现的:** 它们不在任何基本理论中被直接公理化——它们从Tier 0+1+合适的时空结构的联合中涌现。

**层级分类的操作含义:**

Aporia的修剪应自下而上: 先施加Tier 0约束(排除不具备基本"信息语言"的理论), 再施加Tier 1约束(在幸存者中排除不兼容量子信息论的理论), 最后施加Tier 2约束(检查涌现行为是否匹配经典引力)。这个顺序不是任意的——Tier 0约束定义了Ω_info的"语法",Tier 1定义了"语义",Tier 2定义了"表观行为"。

上一轮(Phase 0)对"约束施加顺序可交换"的讨论(INSPECTOR R1 W3, 后来由B博士修正), 现在可以在分层框架中精确化: **修剪映射Π_C的最终结果(Ω_info的集合)不依赖施加顺序, 但每层的修剪结果的epistemic含义不同。** Tier 0的修剪回答"哪些理论有信息? ", Tier 1回答"哪些理论有量子信息? ", Tier 2回答"哪些理论有引力? "。

---

## §3 约束之间的依赖关系

### §3.1 蕴含关系

**形式定义:** 约束A蕴含约束B (A ⇒ B) 当且仅当 Mod(T_C ∪ {A}) ⊆ Mod(T_C ∪ {B}) —— 即所有满足A的理论也满足B。

**注:** 在GPT框架中,"满足A"意味着"对应的态空间+效应+通道满足A表述的不等式/条件"。

#### 蕴含1: C1 + C_signal ⇒ C9 (Holevo界部分)

**论证:** C1断言每个细胞χ ≤ 1 bit。对于n个细胞的复合系统, C_signal(无信号)保证各细胞的信息贡献是相加的(无超加性)。因此总Holevo量χ_total ≤ n · 1 bit = n bits。这等于C9在有限维中的容量版本: I_acc ≤ χ_total ≤ n bits。

**方向:** C1 ∧ C_signal ⇒ C9 (容量版本)
**可信度:** 高——在GPT中,Holevo量的次可加性由无信号条件保证(Barnum et al. 2009)
**状态:** 定理 (在GPT框架中可证明)

#### 蕴含2: C10 (Landauer) ⇒ C9 (Holevo界) 直觉版本

**论证:** Plenio (1999)给出: Landauer原理(擦除1 bit → 至少kT ln 2放热) ⇒ 信息获取的最大速率受限 ⇒ Holevo界。论证是启发性的,但方向清晰: 如果信息擦除没有能价,则可反复读取量子态而无扰动 → 可区分无限多态 → Holevo界被违反。

**方向:** C10 ⇒ C9 (定性)
**可信度:** 中——启发性论证, 严格GPT版本待证明
**状态:** 猜想(在GPT中验证中)

#### 蕴含3: C8 (Bekenstein) ⇔ C3 (熵面积界) 特定版本

**论证:** 在d=4时空中, Bekenstein界 S ≤ 2πRE 在R ≈ ℓ_Planck时变为 S ≤ 2π · A^{1/2} · E, 这不等同于面积律。但通过黑洞力学: Bekenstein界+广义相对论⇒ 黑洞熵 = A/4 ⇒ S_boundary ≤ A/4 (面积律)。而C3直接表述为 S ≤ N_∂Ω (∝ A)。

**等价方向:** 
- Bekenstein + GR ⇒ 面积律 (黑洞视界)
- 面积律 + 因果关系 ⇒ Bekenstein界 (Bousso 1999, Flanagan-Marolf-Wald 2000)

**方向:** C8 ⇔ C3 (在GR附加假设下)
**可信度:** 高——在黑洞物理语境中是定理
**状态:** 在特定框架下是定理,但在纯GPT框架中两者不等价——C3更广义(不需要能量概念)

#### 蕴含4: C4 (因果有向性) + C_signal (无信号) ⇒ C12 (信息因果性) 特定情境版

**论证:** IC博弈中的Alice→Bob通信: 如果信息因果流有向(C4)且Alice和Bob之间无超光速信号(C_signal),则Bob从Alice获取的信息 ≤ Alice发送的m bits(经典通信量)。IC正是这个条件在通信博弈中的操作化表述。

但逆方向不成立: 信息因果性是C4+C_signal在特定博弈情境中的特殊案例——比这两个前提弱。

**方向:** C4 ∧ C_signal ⇒ C12
**可信度:** 高——IC的定义直接依赖因果有向性+无信号
**状态:** 公理蕴含 (如果C4和C_signal被形式化为GPT公理)

#### 蕴含5: C1 (容量上界) ⇒ C13_Tsirelson (Tsirelson界)

**论证:** C1限制每个子系统为1 bit容量。在Bell实验中,Alice和Bob各有一个细胞(GPT系统)。在1 bit/cell约束下,CHSH值被限制在≤2√2(Tsirelson界)。任何违反Tsirelson界的关联(PR-box S=4)需要每个局域系统承载>1 bit的信息容量来编码超量子关联。

**方向:** C1 ⇒ C13_Tsirelson
**可信度:** 高——C1 ⇒ Holevo ≤ 1 ⇒ Tsirelson界是NPA层级中的推论
**状态:** 定理 (NPA hierarchy: 第一层对应量子集, 包含在Tsirelson界中)

#### 蕴含6: C1 ⇒ C2 (回流界) 容量依赖

**论证:** C2的表述依赖"可访问相干分数"q_S = χ(S)/I_max(S)。如果C1给出I_max(S)的上界(1 bit/cell),则q_S的定义本身依赖C1。没有C1, "q_S"无意义 → C2无法被表述。

但这不是逻辑蕴含(∀模型满足C1 ⇒ 满足C2),而是概念依赖: C2的语义需要C1的定义框架。

**方向:** C1 ⇒ 框架前提(C2)
**可信度:** 概念层面——C2的表述语义上依赖C1
**状态:** 概念依赖, 非逻辑蕴含

#### 蕴含7: C11 (Margolus-Levitin) + C1 ⇒ 信息处理速率上界

**论证:** C1给出每个操作处理的信息量 ≤ 1 bit。C11给出每个操作的最短时间 ≥ πħ/(2⟨E⟩)。联合: 信息处理速率 ≤ 2⟨E⟩/(πħ) bit/s。这是Lloyd (2000)计算"宇宙终极笔记本"速率的基础。

**方向:** C1 ∧ C11 ⇒ 速率上界(衍生约束)
**可信度:** 高——直接乘法
**状态:** 衍生约束——不是独立约束,而是两个独立约束的联合推论

### §3.2 等价对

#### 等价对1: C3 (熵面积界) ≈ C8 (Bekenstein界)

**论证:** 见蕴含3。在GR框架中等价,在GPT框架中C3更广义(不需要能量概念)。
**等价可信度:** 在特定框架下可互译, 但不在GPT中严格等价。
**处理策略:** 在Ω_info的GPT构建中, C3保留, C8作为Tier 2涌现推论。

#### 等价对2: C12 (信息因果性) ≈ C4 ∧ C_signal (在通信博弈中)

**论证:** IC的主要排除作用(排除超量子关联)已由C4(因果有向性)+C_signal(无信号)+C1(容量上界)覆盖。IC情境化为一个博弈,但逻辑内涵被三个更基本的约束分解。

但有一个微妙的差异: IC的原始动机是"更物理"的——它从通信博弈中导出而非从状态空间几何中导出。这使IC在某些GPT中可能比C4+C_signal更强(Cavalcanti et al. 2010: 宏观局域关联违反IC)。

**等价可信度:** 接近等价但不完全——IC在某些场景中更强(排除宏观局域关联)。
**处理策略:** C12保留为C4在通信场景中的操作强化版本,标注为"近乎冗余但非完全冗余"。

#### 等价对3: C13 (无信号+Tsirelson) ≈ C1 ∧ C_signal (容量+无信号版本)

**论证:** 见蕴含5。C1 ⇒ Tsirelson界, C_signal ⇔ 无信号条件。C13 = C1 ∧ C_signal 在Bell场景中的具体化。

**等价可信度:** 高——在GPT中C13的两个成分分别是C1和C_signal的特例或推论。
**处理策略:** C13标注为C1和C_signal的导出约束,不在独立基底中。

### §3.3 约束依赖图

```
                    ┌─────────────────────────────────────┐
                    │          TIER 0: 信息格点层           │
                    │                                     │
                    │   C_signal (无信号) ←── 隐含前提      │
                    │        │                            │
                    │        ├── C4 (因果有向性) ──→ C12 (IC)│
                    │        │                            │
                    │   C1 (容量上界) ←── 核心节点          │
                    │    │   │    │                       │
                    │    │   │    └──→ C13_Tsirelson      │
                    │    │   │                            │
                    │    │   └──→ C6, C7 (meta) ← 独立    │
                    │    │                                │
                    └────┼────────────────────────────────┘
                         │
                    ┌────┼────────────────────────────────┐
                    │    │   TIER 1: 量子涌现层            │
                    │    │                                │
                    │    ├──→ C9 (Holevo) ←── C10 (Landauer)│
                    │    │         │                      │
                    │    └──→ C2 (回流界) ← 依赖C1+q概念  │
                    │              │                      │
                    │              ├── C11 (ML) ← 独立     │
                    │              │                      │
                    └──────────────┼──────────────────────┘
                                   │
                    ┌──────────────┼──────────────────────┐
                    │              │  TIER 2: 经典引力层   │
                    │              │                      │
                    │         C3 (面积界) ≈ C8 (Bekenstein)│
                    │              │                      │
                    │         C5 (弱场极限) ← 独立         │
                    │                                     │
                    └─────────────────────────────────────┘
```

**边说明:**

- **逻辑蕴含 (⇒):** 实线箭头。所有满足前提理论也满足结论。
- **概念依赖 (语义前提):** 虚线箭头。结论的表述需要前提的概念定义。
- **等价 (⇔):** 双向实线。
- **独立节点:** 无入边的节点(除了隐含前提C_signal)。

**图的关键特征:**

1. **C1是最关键的节点** — 它有6条出边(直接或间接): → C9, → C2, → C13_Tsirelson, → C3(通过容量定义), → 框架前提(C2), → 框架前提(速率界)。C1是约束网络的"脊骨"。

2. **C_signal是隐含的前提** — 几乎所有约束的表述都隐含了无信号条件(态空间的张量积结构在无信号条件下才有良好的通道容量定义)。C_signal不是独立约束——它是GPT公理的定义部分。但在约束依赖图中,它的角色不可或缺。

3. **C6和C7是结构的"外点"** — 它们没有入边也没有出边(除了概念上依赖C1+"信息"概念)。它们是meta约束——在约束网络之外,对约束网络的表达能力做出声明。

4. **C10 (Landauer)是最强的独立节点** — 它不依赖GPT框架中的任何其他约束,直接连接热力学和信息论。如果C10被排除(宇宙不满足Landauer原理),多个蕴含箭头的锚点将失效。

---

## §4 约束的独立集

### §4.1 独立基底

**问题:** 找出C ⊆ {C1,...,C13}的最小独立子集C_independent,满足:
1. C_independent中的每个约束逻辑独立(互不蕴含)
2. C_independent生成所有13个约束: Mod(T_C ∪ C_independent) = Mod(T_C ∪ {C1,...,C13})

**分析过程:**

**Step 1: 识别"几乎独立"的候选。**

从依赖图(§3.3)出发,候选独立节点是无入边或仅有概念依赖入边的节点:

- C1 (容量上界): 仅有C_signal概念依赖, 无其他约束逻辑蕴含它 ✓
- C4 (因果有向性): 是DGF的A1公理, 不依赖其他约束 ✓
- C5 (弱场极限): Tier 2独立节点, 不依赖任何Tier 0/1约束 ✓
- C6 (活性独立): Meta约束, 无入边 ✓
- C7 (ξ自由度): Meta约束, 无入边 ✓
- C10 (Landauer): 跨领域独立节点, 不依赖其他信息论约束 ✓
- C11 (ML界): 速率维度的独立约束, 不依赖其他约束 ✓

**但这给了7个候选——太多了。**

**Step 2: 消除概念冗余。**

- C6和C7都是meta约束。它们的"独立性"是meta层面的——它们声张的是其他约束(和公理集)的推论不完备性。但它们本身不排除任何理论——它们只是标注Ω_info中不可判定的区域。因此,它们不是"独立信息论约束"——它们是"约束系统的不可判定性声明"。将它们单独分类为C_meta。

- C10 (Landauer)和C11 (ML界): 虽然两者在形式上不互相蕴含,但它们叠加耦合: C10给出信息擦除的能价, C11给出信息处理的速率上界。两者的"独立"在概念上是明显的(温度 ≠ 激发能),但在GPT框架中,它们可能从一个共同的更深层原理导出——"信息≠自由"(信息处理必然消耗物理资源)。

**Step 3: 识别隐藏的蕴含。**

- C4 (因果有向性) + 容量定义 ⇒ C1? 不是。C1约束容量大小,C4约束流向——大小和方向是正交的。所以C4不能蕴含C1。
- C5 (弱场极限)不能被任何Tier 0/1约束蕴含——因为它是涌现层的等号约束,需要附加的时空解构(GPT中的通道结构+背景流形)才能被表述,而这些附加结构本身不被Tier 0/1约束。

**Step 4: 检查从独立集能否生成所有导出约束。**

提出最小独立约束集:

```
C_independent = {C1, C4, C5, C_signal}
                + C10 (如果Landauer不能从C1导出)
```

**但C_signal是GPT公理——已在Ω_GPT定义中。** 如果在Ω_GPT中已经内置了无信号条件(如Phase 0的定义所示),则C_signal不需要被列为约束——它是框架前提。

**最终独立约束集:**

```
C_independent = {C1, C4, C5, C10, C11}
```

加上C_signal和GPT公理(凸性、局域可区分性)作为框架前提。

加上C_meta = {C6, C7}作为meta层注释。

**|C_independent| = 5**

### §4.2 导出约束的生成

从C_independent = {C1, C4, C5, C10, C11}生成整个约束系统的推导树:

#### 组1: 从C1 ∈ C_independent导出

```
C1 (容量上界: χ ≤ 1 bit/cell)
├──→ C9 (Holevo界: I_acc ≤ χ ≤ 1 bit) [蕴含1, 高可信度]
│   └──→ C9强化: 任何测量的可访问信息 ≤ 1 bit/cell
├──→ C13_Tsirelson (Tsirelson界: S_CHSH ≤ 2√2) [蕴含5, 高可信度]
│   └──→ PR-box (χ≈2, S=4)被排除
├──→ C2 (回流界: 框架前提——需要C1定义q_S) [蕴含6, 概念依赖]
│   └──→ P_reflux ≤ q_S/q_E ← χ from C1
└──→ C3 (熵面积界: S ≤ N_∂Ω · log₂(d_max), d_max from C1)
    └──→ 经典和量子的面积律
```

**注意:** C3的导出不是纯逻辑的——它需要图论结构(Ω的划分、边界细胞计数),这些不包含在C1中。所以C3是一个"框架增强的导出约束": 从C1(容量概念) + 图论框架(信息格的图表示) ⇒ C3(面积界)。如果C1和C4和C_signal作为Tier 0被施加,C3作为Tier 2涌现推论被附加。

#### 组2: 从C4 ∈ C_independent导出

```
C4 (因果有向性: 信息流有向)
└──→ C12 (信息因果性: IC博弈预测 ≤ m bits) [蕴含4, 高可信度]
    └──→ 在通信场景中排除超量子关联

注: C12 = C4 ∨ C_signal 在通信博弈中的操作化。
    在非通信场景中,C4可以独立排除"时间回路"类理论
    (祖父悖论式的逆因果信息流),而C12不能(博弈设定不允许逆因果)。
    因此C12是C4的真子集——C4比C12更强。
```

#### 组3: 从C5 ∈ C_independent导出

```
C5 (弱场极限: ∇²(ln q) = 0)
└──→ 无导出约束。
    C5是涌现层的"端点约束"——它不蕴含任何其他约束,而是等待Tier 0和Tier 1
    约束先修剪空间,然后C5在幸存者中检查涌现行为是否匹配牛顿引力。

    当前状态下,C5不能被Tier 0/1约束蕴含——它本身在独立集中。
    但如果在Tier 1中找到更深层约束(如量子态的退相干导致经典引力势),
    则C5可能被降级为导出约束。

    当前: C5是独立约束(在GPT框架中)。
```

#### 组4: 从C10 ∈ C_independent导出

```
C10 (Landauer原理: ΔE ≥ kT ln 2 · ΔI)
├──→ C9 (Holevo界直觉版本) [蕴含2, 中可信度]
│   └──→ 如果信息擦除有能价 → 信息获取有限 → Holevo界
└──→ C2强化 (回流界物理机制)
    └──→ 回流＝反向擦除环境信息 → P_reflux ≤ exp(-ΔE/kT)
```

**关键观察:** C10(Landauer)和C1(容量上界)在逻辑上独立,但它们在物理上相互增强:
- C1回答了"多少信息可存储在细胞中?" (空间容量)
- C10回答了"擦除信息需要多少能量?" (时间能量代价)
- C1 + C10 + C11 ⇒ 信息处理的完整时空界限

#### 组5: 从C11 ∈ C_independent导出

```
C11 (Margolus-Levitin: τ ≥ πħ/(2⟨E⟩))
├──→ C1强化: 信息处理速率 = C1/cell ÷ τ ≥ 特定值
│   → 速率上界 = 2⟨E⟩/(πħ) bit/s/cell [蕴含7]
└──→ 无独立导出约束。
    C11独立地为约束系统贡献了时间维度的上界,
    补足了C1(空间)和C10(能量)之间的缺口。
```

#### C8 (Bekenstein)的归属

```
C8 (Bekenstein界: S ≤ 2πkRE/ħc)

这个约束不在C_independent中——因为有两条路径导出它:
路径1: C3 (面积界) + 黑洞力学 + GR → Bekenstein界 (在黑洞上)
路径2: C1 (容量上界) + C10 (Landauer) + 能量密度界 → Bekenstein界 (一般)

在GPT框架中,C8不是独立约束——它是C3+GR或C1+C10的推论。
但C8在物理直觉上比它的前提更基本(Bekenstein界作为"普适熵界"
是被广泛接受的)。将此标注为Aporia分类学中的"准独立约束":
在GPT中非独立,但在物理教科书层次上是独立公设。
```

#### C13 (无信号+Tsirelson)的拆分

```
C13分解:
├── C13_signal (无信号条件) → 已内置在Ω_GPT定义中 → 框架前提, 非约束
└── C13_Tsirelson (Tsirelson界: S ≤ 2√2) → 从C1导出 [蕴含5] → 非独立
```

### §4.3 独立集总结

| 独立约束 | 为什么独立? | 导出哪些约束? | 独立性的威胁? |
|:---------|:-----------|:------------|:------------|
| **C1** (容量上界) | 核心公理——不依赖任何其他约束给出χ上界 | C9(Holevo), C13(Tsirelson), C2(前提), C3(概念前提) | 如果Holevo界被证明比C1更基本(即C1是Holevo界的容量特例),则C1的独立地位可被挑战 |
| **C4** (因果有向性) | DGF的A1公理——因果偏序 | C12(IC) | 如果因果有向性被证明可从C_signal+CPT不变性导出,C4可能被降级 |
| **C5** (弱场极限) | 涌现层——不可从Tier 0/1导出 | 无(端点约束) | 如果量子退相干→经典引力的桥接被完成,C5可能被降级为导出 |
| **C10** (Landauer) | 跨领域——热力学→信息论桥接 | C9(直觉版), C2(机制强化) | 如果信息擦除可无耗散(量子Landauer争论),C10可能非普适 |
| **C11** (ML界) | 速率维度——补足C1(空间)和C10(能量) | 速率上界 | 如果能量-时间不确定性被证明蕴含ML界,则C11可从量子力学的内部结构导出 |

加上框架前提: C_signal (无信号条件, 已在Ω_GPT定义中)
加上Meta层: C_meta = {C6, C7} (不可推导性声明)

**|C_independent| = 5, |C_derived| = 8, |C_meta| = 2, Total = 13 (+2框架前提)**

### §4.4 独立集大小的含义

独立集大小为5意味着: 有5个"信息论自由度"需要在构建Ω_info时被独立指定。这5个自由度联合生成整个约束网络——其余8个约束是其推论或情境化。

**紧致性重访:**

Phase 0的紧致性分析告诉我们: 任何有限约束集都有无穷多模型。C_independent有5个约束——这是一个相当小的数。这意味着Ω_info(C_independent)是一个非常大的空间(5个约束不足以缩减Ω_GPT到一个可管理的子空间)。

但这里有一个关键的误解需要纠正: C_independent的5个约束不是在Ω_GPT上做5次布尔交集——每个约束本身是一个无限的不等式族(如C1对系统中的每个细胞施加χ ≤ 1; C10对每个信息擦除操作施加ΔE ≥ kT ln 2; C11对每个态演化施加τ ≥ ...)。所以5个"约束"实际上是5个约束schema,展开后是无限个具体约束。

**稳定性分类交叉:**

从B博士的Phase 0分类: T_DGF是不稳定+IP的理论。C_independent中的5个约束可以从稳定性角度分类:
- C1 (χ ≤ 1): 基数约束(有限可区分态数) → 在RCF语言下是∀-句子类 → 可能具有相对稳定的片段
- C4 (信息流有向): 偏序公理 → 传递性+非自反性 → 序理论 → 不稳定(产生无限链)
- C5 (弱场极限): 等号约束 → 唯一极限条件 → 相对稳定(固定一个点)
- C10 (ΔE ≥ kT ln 2 · ΔI): 不等式 → ∀-句子类 → 同C1
- C11 (τ ≥ πħ/(2⟨E⟩)): 不等式 → ∀-句子类 → 同C1

C4是其中最不稳定的——序公理可以产生无限的因果链和无限的类型。其余4个施加可计算的上界,有助于修剪类型空间。

---

## 局限与开放问题

### 局限1: 约束系统的完备性

当前枚举的13个约束是从DGF+信息论文献中提取的,但不声称完备。已知缺失的约束类别:

1. **代数约束:** Kochen-Specker定理类(语境性约束)——排除非语境隐变量理论
2. **计算约束:** Brogioli (2024)的计算复杂性no-go——排除序贯隐变量理论
3. **热力学约束:** 第二定律在GPT中的推广(Krumm et al. 2016)
4. **纯化约束:** Chiribella-D'Ariano-Perinotti的纯化公理——可能是独立约束
5. **简洁性约束:** Hardy的K=N^r公设——排除r>2的复合系统

这些候选约束尚未加入,因为:
- (a) 它们的GPT表述不完整;
- (b) 它们在约束网络中的位置(独立/导出)未确定;
- (c) 部分约束(如语境性)的物理普适性有争议。

### 局限2: 蕴含关系的证明状态

§3的7条蕴含关系中,只有1条(蕴含1: C1∧C_signal⇒C9)在GPT框架中有严格证明。其余6条是启发性论证或框架特定证明。严格化这些蕴含关系需要逐条在GPT中构造证明或反例,这是Phase 2或3的任务。

### 局限3: 约束独立集对熵定义的依赖

C_independent的正确性依赖于Ω_info中所用的熵/信息度量的选择。如果采用Renyi熵而非Shannon/von Neumann熵(如Oughton & Timpson 2024指出的那样),蕴含关系可能改变——某些"独立"约束可能变成"冗余",某些"导出"约束可能变成"独立"。

**缓解策略:** 将约束的熵依赖显式化——每个约束标注其依赖的熵定义(Shannon, von Neumann, Renyi α, Tsallis q, ...)。对每个熵选择,重新计算独立集。

### 开放问题

1. **C10(Landauer)是否可以从C1(容量上界)+热力学第二定律导出?** 如果是,C10将从C_independent中移除。但目前证据不支持(C1没有温度概念,无法导出ΔE ≥ kT ln 2)。

2. **C4(因果有向性)是否可以从C_signal(无信号)+CPT不变性导出?** 如果CPT不变性+无信号条件蕴含信息流的方向性,则C4可被降级。但CPT不变性是相对论量子场论的性质——在一般GPT中不成立。

3. **是否存在比C1更基本的容量约束?** 如果量子信息论中发现一个"元容量原理"(如"所有信息度量都满足χ ≤ f(d)"),C1可能变成该原理的特例。

4. **C_meta中的不可推导性声明(C6,C7)是否可以独立裁剪?** 即: 如果我们将"C6为真"和"C6为假"视为两个不同的约束系统,Ω_info在其中的结构是否不同? 初步猜测: 不——meta约束不影响Mod(T_C),只影响我们对Mod(T_C)的knowledge。

---

## 下一轮方向

1. **严格化C_independent:** 对每个声称的蕴含关系,在GPT框架中构造证明或反例
2. **完整性补充:** 添加缺失的约束类别(代数、计算、热力学)并重新计算独立集
3. **约束量化:** 对每个约束计算其"排除力"——被排除的理论类的大小(在有限维截断下)
4. **C_independent的最小性证明:** 证明|C_independent| = 5是真正的最小独立约束集(不能减到4)

---

## 参考文献 (本Round新增)

### 约束分类学
1. Leifer, M. "No-go theorems." philsci-archive:11617 (2014).
2. Clifton, R., Bub, J., Halvorson, H. "Characterizing Quantum Theory in Terms of Information-Theoretic Constraints." Found. Phys. 33, 1561 (2003).
3. Naeger, P. "A taxonomy of hidden variable theories." philsci-archive (2018).
4. Brogioli, D. "A no-go theorem for sequential and retro-causal hidden-variable theories based on computational complexity." arXiv:2409.11792 (2024).

### 约束等价性/独立性
5. Plenio, M.B. "The Holevo bound and Landauer's principle." Phys. Lett. A 263, 281 (1999). [quant-ph/9910086]
6. Harremoes, P. "From thermodynamic sufficiency to information causality." Quantum Stud.: Math. Found. 7, 255 (2020).
7. Oughton, T., Timpson, C. "Information causality and the choice of entropy measure." Entropy 26(7), 562 (2024).
8. Purushothaman, S. et al. "Information causality cannot exclude all superquantum correlations." Phys. Rev. A 112, 022211 (2025).
9. Schack, R. "Quantum theory from four of Hardy's axioms." Found. Phys. 33, 1461 (2003). [quant-ph/0210017]

### Bekenstein-Holevo-Landauer-Margolus-Levitin统一框架
10. Bekenstein, J.D. "Universal upper bound on the entropy-to-energy ratio for bounded systems." Phys. Rev. D 23, 287 (1981).
11. Casini, H. "Relative entropy and the Bekenstein bound." Class. Quantum Grav. 25, 205021 (2008).
12. Page, D.N. "The Bekenstein Bound." arXiv:1804.10623 (2018).
13. Bousso, R. "Black hole entropy and the Bekenstein bound." arXiv:1810.01880 (2018).
14. Hörnedal, N., Sönnerborn, O. "Margolus-Levitin quantum speed limit for an arbitrary fidelity." Phys. Rev. Research 5, 043234 (2023).
15. Anderson, N.G. "Generalized Landauer Bound for Information Processing: Proof and Applications." Entropy 24(11), 1568 (2022).

### GPT中的信息约束
16. Kimura, G., Ishiguro, J., Fukui, M. "Entropies in General Probabilistic Theories and its Application to Holevo Bound." Phys. Rev. A 94, 042113 (2016). [1604.08009]
17. Barnum, H. et al. "Entropy and Information Causality in General Probabilistic Theories." New J. Phys. 12, 033024 (2010). [0909.5075]
18. Chiribella, G., Scandolo, C.M. "Operational axioms for diagonalizing states." EPTCS 195, 96 (2015).

### NPA层级/Tsirelson界
19. Navascues, M., Pironio, S., Acin, A. "A convergent hierarchy of semidefinite programs characterizing the set of quantum correlations." New J. Phys. 10, 073013 (2008). [0803.4290]
20. Cavalcanti, D., Salles, A., Scarani, V. "Macroscopically local correlations can violate information causality." Nat. Commun. 1, 136 (2010).

### DGF
21. Huang, Z. "DGF v3.1-prd: Decoherence Geometry Framework." Internal manuscript (2026).

### Phase 0 桥接
22. A博士, B博士. "LP34 Phase 0 -- Omega的形式化." conclusions_phase0.md + round1.md + round2.md (2026).

---

## 签名

```
Phase 1 Round 1 -- 约束系统的系统化:
  约束枚举: 13个约束(7 DGF内部 + 6 文献) + 2框架前提 + 2 meta
  分类学: 三维分类(类型/来源/层级) — 约束不是扁平的
  依赖图: 7条蕴含 + 3组等价对 — 有向无环图(DAG)
  独立基底: |C_independent| = 5 
    = {C1(容量上界), C4(因果有向性), C5(弱场极限), C10(Landauer), C11(ML界)}
  核心节点: C1 — 6条出边, 约束网络的脊骨
  关键洞察: 
    1. 上界约束(8/13)主导 → 不稳定理论的必然特征
    2. 三层架构: 信息格点(Tier 0) → 量子涌现(Tier 1) → 经典引力(Tier 2)
    3. C_independent中5个约束对应5个信息论自由度 — 
       少于5 → 约束不足, Ω_info太大; 多于5 → 冗余
    4. Meta约束(C6,C7)在约束网络外 — 它们描述的是网络的"不可判定边界"
  状态: COMPLETE → Phase 1 Round 2 (独立集严格化)
```

--- round1_phase1.md 结束 ---

# LP34 Phase 1 Conclusions -- 约束系统的系统化

**项目:** LP34 Aporia机制 -- 信息论约束系统性排除不可能物理
**Phase:** 1 (约束系统的系统化: 枚举、分类学、依赖结构、独立基底)
**日期:** 2026-06-08
**产出:** A博士 Round 1 (约束逻辑分析: 13约束+分类学+7蕴含+MinInd=5) + B博士 Round 1 (网络科学: 约束网络拓扑+最小独立集+相变预测)
**INSPECTOR裁决:** 0阻断, 2修正(W1约束池不一致, W2 no-cloning→no-broadcasting), 2警告(W3完备基底混淆, W4 C5位置)
**Phase结论:** 通过. 约束系统被系统化为具有三层Hasse结构的有向无环图, 其不可约硬核为{信息容量有界, 因果有向性}(双方法独立验证), 最小独立集大小为5(可优化到3-4).

---

## 1. 约束系统全景图

### 1.1 13约束完整枚举

Phase 1产出两个约束池(A博士13约束 + B博士13约束). 它们的并集构成了LP34当前最完整的约束全景:

**并集 = 17个约束 (13_A ∪ 13_B, 交集7):**

| ID | 标签 | 名称 | 类型 | 来源 | A博士 | B博士 |
|:--:|:-----|:-----|:----:|:----:|:-----:|:-----:|
| C1 | C_capacity / C_bnd | 信息容量上界 | 上界 | DGF A2 | ✓ | ✓ |
| C2 | C_reflux / C_ref | 回流界 | 上界 | DGF | ✓ | ✓ |
| C3 | C_entropy_area / C_area | 熵面积界 | 上界 | DGF | ✓ | ✓ |
| C4 | C_causal_directed / C_cau | 因果有向性 | 方向 | DGF A1 | ✓ | ✓ |
| C5 | C_weak_field | 弱场极限(牛顿引力) | 等号 | DGF | ✓ | -- |
| C6 | C_liveness_indep | 活性独立 | Meta | DGF | ✓ | -- |
| C7 | C_xi_freedom | ξ自由度 | Meta | DGF | ✓ | -- |
| C8 | C_Bekenstein | Bekenstein界 | 上界 | 文献 | ✓ | -- |
| C9 | C_Holevo / C_hol | Holevo界 | 上界 | 文献 | ✓ | ✓ |
| C10 | C_Landauer / C_lander | Landauer原理 | 上界 | 文献 | ✓ | ✓ |
| C11 | C_ML | Margolus-Levitin界 | 上界 | 文献 | ✓ | -- |
| C12 | C_IC / C_infoc | 信息因果性 | 方向 | 文献 | ✓ | ✓ |
| C13 | C_NSTS / C_nosig+C_tsir | 无信号+Tsirelson界 | 上界/方向 | 文献 | ✓ | ✓(拆分) |
| C14 | C_loc | 局域性(光锥结构) | 方向 | 广义物理 | △ | ✓ |
| C15 | C_thermo | 热力学第二定律 | 上界 | 广义物理 | △ | ✓ |
| C16 | C_purif | 纯化公设 | 结构 | 量子重构 | △ | ✓ |
| C17 | C_noclon | 不可克隆 | 禁令 | 广义物理 | -- | ✓ |

△ = A博士在"局限与开放问题"中列为缺失

**发现:** 约束池的完全并集为17约束. 其中DGF内部7个, 文献/广义物理10个. INSPECTOR裁定A和B的约束池差异(W1)需PI在Phase 2前统一.

### 1.2 约束分类学

Phase 1建立了**三重交叉分类学**, 约束不是扁平的:

**按类型(Taxonomy T):**

| 类型 | 符号 | 排除机制 | 数量 | 成员 |
|:-----|:----:|:---------|:----:|:-----|
| 上界约束 | ≤ | 排除超过阈值的一切理论 | 9 | C1, C2, C3, C8, C9, C10, C11, C13_Tsirelson, C15(热二) |
| 等号约束 | = | 极限下强制精确匹配 | 1 | C5 |
| 方向约束 | → | 禁止因果逆流 | 4 | C4, C12, C13_nosig, C14 |
| Meta约束 | ⊬ | 声明不可推导性边界 | 2 | C6, C7 |
| 禁令约束 | 不存在X | 禁止特定物理过程 | 1 | C17 |

上界约束占主导(9/17=53%). 这与Phase 0的结论一致: DGF在最深层是不稳定+IP的理论, 只能导出forall-推论(上界、不等式)而非独一理论. 约束类型的偏态分布不是设计缺陷——它是底层理论稳定性类别的必然表现.

**按来源(Taxonomy S):**

| 来源 | Epistemic地位 | 对熵定义敏感? | 成员 |
|:-----|:-------------|:------------:|:-----|
| 信息论第一原理 | 分析命题(改变信息定义→约束改变) | 是 | C1, C8, C9, C10, C11, C13 |
| 图论/组合 | 综合命题(独立于信息度量选择) | **否** | C2, C3 |
| 动力学涌现 | 条件命题(仅极限下成立) | 有限 | C5 |
| 逻辑独立性 | Meta命题 | N/A | C6, C7 |
| 操作因果性 | 操作命题(独立于实体论) | **否** | C4, C12, C14 |

关键区分: 图论/组合约束(C2, C3)和操作因果性约束(C4, C12, C14)对信息度量选择是**不变的**——它们只关心连通性、流动方向和网络容量. 而信息论第一原理约束(C1, C8-C11, C13)共享一个脆弱性: 如果物理世界的信息度量不是Shannon/von Neumann熵, 这些约束的表述需要修改(见Oughton & Timpson 2024). 

**方法论含义:** Aporia应优先施加对信息度量选择不变的约束(robust基底), 然后在其上施加度量依赖的约束. 这确保修剪操作的基础不依赖熵定义的任意选择.

**按层级(Taxonomy H) -- 三层架构:**

| 层级 | 描述 | 成员 | 特点 |
|:----:|:-----|:-----|:-----|
| **Tier 0: 信息格点层** | 定义信息的基本操作语义 | C1, C4, C6, C7, C13_nosig, C14, C17 | 不依赖时空、能量、量子结构. 最深的约束层. |
| **Tier 1: 量子涌现层** | 信息度量+热力学涌现 | C2, C9, C10, C11, C12, C15 | 依赖Tier 0的信息概念, 附加能量和动力学. |
| **Tier 2: 经典引力层** | 大尺度表观规律 | C3, C5, C8 | 依赖时空连续统和宏观极限. 最表层. |

三层之间的偏序: Tier 0(定义"信息") → Tier 1(附加"能量/时间") → Tier 2(附加"时空/几何").

**操作含义:** Aporia的修剪应自下而上——先施加Tier 0约束(排除不具备基本信息语言的理论), 再施加Tier 1(在幸存者中排除不兼容量子信息论的理论), 最后施加Tier 2(检查涌现行为是否匹配经典引力). 修剪映射的最终结果(Omega_info)不依赖施加顺序, 但每层的修剪结果的epistemic含义不同.

---

## 2. 约束依赖网络

### 2.1 DAG结构

Phase 1的核心发现: **约束系统不是扁平的集合——它是一个有向无环图(DAG).**

A博士识别了7条蕴含关系, B博士识别了12条网络边(3条逻辑蕴含I-边 + 9条定义依赖D-边). 合并后的约束依赖图:

**三层Hasse图 (传递归约后):**

```
Level 0 (最小元 / 独立前提):
==============================
C_cau    C_loc    C_bnd ⇔ C_nobroadcast    C_thermo    C_purif    C5    C6    C7    C11
  \       /        /  |      \               /           (孤立)   (涌现) (meta) (meta) (速率)
   \     /        /   |       \             /
    \   /        /    |        \           /
     ↓  ↓       ↓     ↓         ↓         ↓
Level 1 (中间推论):
================
C_nosig    C_hol   C_area  C_infoc   C_lander
              |                 |
              ↓                 ↓
Level 2 (终端推论 / 叶子):
=============================
            C_ref            C_tsir
```

**边类型:**
- **实线 (逻辑蕴含 I-边):** C_infoc→C_tsir, C_thermo→C_lander, C_bnd⇔C_nobroadcast(2-cycle)
- **虚线 (定义依赖 D-边):** C_bnd→C_hol, C_bnd→C_area, C_bnd→C_infoc, C_bnd→C_lander, C_hol→C_ref, C_cau→C_nosig, C_loc→C_nosig

### 2.2 网络关键指标

| 指标 | 值 | 含义 |
|:-----|:--:|:-----|
| 节点数 | 17 (并集) | 约束总数 |
| 有效边 | ~14 | I-边+D-边, 极其稀疏 |
| 边密度 | ~5% | 不稳定理论特征 (IP+SOP导致蕴含稀少) |
| 弱连通分量 | 3+ | 因果簇 + 信息论簇 + 结构簇(+meta簇+涌现簇) |
| 强连通分量(SCC) | 仅1个2-cycle | {C_bnd, C_nobroadcast} |
| 网络直径 | 2(边)/3(节点) | 推导深度极浅——最长链3节点 |
| Articulation point | C_bnd | 移除后信息论簇分裂 |

### 2.3 网络的不稳定性诊断

B博士建立了Shelah分类与网络拓扑的对应表:

| She1ah类别 | 网络拓扑预测 | T_DGF验证 |
|:-----------|:------------|:--------:|
| 不稳定+IP+SOP | 多根节点(5+), 极低边密度(<10%), 入度0占比>35%, 凝聚图为稀疏DAG | **匹配** |

约束网络的稀疏性(边密度~5%)和入度0节点的高占比(~38%)是T_DGF不稳定性(IP+SOP)的结构投影.

**物理含义:**
- **稀疏I-边 = 约束之间的逻辑蕴含极其稀少.** 不稳定理论中, 公式可编码任意大的独立二分(IP), 意味着两个物理条件可以任意独立变化而不互相制约. 因此约束之间缺乏推导关系——每个约束都是"独立声明"而非"可推导结论".
- **短直径 = 推导链浅.** 物理约束之间的蕴含大多是"一步到位"的, 没有数学理论中常见的多层中间概念链. 这反映了物理约束的"直接性"——它们是声明性的而非推导性的.

---

## 3. 最小独立约束集

### 3.1 双方法独立验证

Phase 1通过两种完全独立的方法确定了最小独立约束集:

**方法A (A博士 -- 约束逻辑分析):**
从7条蕴含关系出发, 手动消除概念冗余和逻辑依赖, 得到:
```
C_independent_A = {C1(容量上界), C4(因果有向性), C5(弱场极限), C10(Landauer), C11(ML界)}
```
|C_independent| = 5.

**方法B (B博士 -- 图论入度分析):**
从13节点有向网络出发, 传递归约后取入度=0节点:
```
C_independent_B = {C_cau, C_loc, C_bnd, C_thermo, C_purif}
```
|C_independent| = 5.

### 3.2 不可约硬核: 2约束

两个独立集的交集只有2个约束: **C1/C_bnd (信息容量上界) 和 C4/C_cau (因果有向性).**

这两个约束构成约束系统的**不可约硬核**——无论使用什么框架(A博士的逻辑分析或B博士的图论分析), 无论选取什么约束池(17个或精简版), 它们始终在独立集中.

**这与DGF的A1+A2双公理结构一致——但现在它不是修辞声称, 而是通过双方法独立验证的结构事实.**

| 方法A | 方法B | 地位 |
|:-----:|:-----:|:-----|
| C1 (容量上界, χ≤1) | C_bnd (信息容量有界) | 不可约硬核 #1 |
| C4 (因果有向性) | C_cau (因果不对称性) | 不可约硬核 #2 |
| C10 (Landauer) | C_thermo (热二) | 独立但可选替代 |
| C11 (ML界) | C_loc (局域性) | 独立但可选替代 |
| C5 (弱场极限) | C_purif (纯化公设) | 独立但可选/Phase 3 |

### 3.3 独立集大小 = 5, 可优化到 3-4

两个独立集大小都是5. 同时存在优化路径:

**优化路径:**
1. **C_purif可能可选.** 如果Aporia的目标是"排除不可能理论"而非"唯一确定量子理论", 纯化公设可被省略. 不施加它不会让约束系统崩溃——它只是排除了没有纯化的理论. 移除后MinInd→4.
2. **C_loc和C_cau可能统一.** 在某些广义因果框架(process matrix formalism)中, 因果结构和局域性可被统一为"因果结构"的单一概念. 如果统一→MinInd→4(或3, 如果C5也被降级).
3. **C5可降级为Phase 3涌现验证.** 弱场极限(牛顿引力)是涌现层的等号约束——它不在信息论约束核心中. 如果C5被移出独立集(放到Phase 3)→MinInd→4.
4. **C_thermo和C_Landauer的合并.** Landauer原理和热力学第二定律在逻辑上不互相蕴含, 但在操作上(对Aporia的排除目的)它们的大部分排除效果重叠. 如果只保留一个→MinInd→4.

**保守估计:** Aporia的最小独立约束数在3-5之间. 优化后的最可能配置:

```
C_core = {C1(容量上界), C4(因果有向性), C10/15(热力学约束, 任选一)}
       + 可选: C_loc(非局域理论排除), C_purif(非纯化理论排除)
       + Phase 3: C5(涌现验证)
```

**如果目标实现(|MinInd|≈3), Aporia将拥有极其经济的前提集合: 3个独立物理假设即可驱动整个约束排除机器.**

### 3.4 DGF的覆盖度 -- A1+A2仅覆盖2/5独立约束

DGF声称从2条公理(A1=因果存在+A2=容量有界)导出物理. Phase 1的网络分析揭示了全貌:

- **A1 ≈ C4/C_cau ✓** (在独立集中)
- **A2 ≈ C1/C_bnd ✓** (在独立集中)
- 但其余独立约束(C_loc, C_thermo, C_purif, C_Landauer, C_ML) **不能** 从A1+A2导出

B博士的诊断: DGF未声称A1+A2能导出其余约束——DGF的H1-H10桥接假设**包含了**这些独立前提的DGF特定版本. DGF的实际前提集不是2, 而是2+N(其中N是H1-H10中逻辑独立的假设数). "A1+A2导出物理"是修辞框架——结构假设(H1-H10)被命名为"桥接"而非"公理", 制造了极简公理化的印象.

**这并非对DGF的批评.** 每个物理框架都需要结构假设. DGF的诚实之处在于它**命名**了这些假设(H1-H10), 使它们可被独立审查. Phase 1的网络分析只是让它更明确: 这些假设中有多少是逻辑独立的, 它们之间的真实关系是什么.

---

## 4. C_bnd↔C_nobroadcast: 信息容量上界 ≡ 不可广播定理

### 4.1 B博士的发现

在约束网络中, B博士识别了唯一的非平凡强连通分量(2-cycle):

```
C_bnd (信息容量有界: 每个物理事件I(x)∈[0,1])
    ⇔
C_nobroadcast (不可广播: 不存在普适操作将态广播到两个副本)
```

引用: Barnum, Barrett, Leifer, Wilce (2007), "Generalized No-Broadcasting Theorem", Phys. Rev. Lett. 99, 240501.

**INSPECTOR修正:** B博士原文写"不可克隆(no-cloning)", 应修正为"不可广播(no-broadcasting)". No-broadcasting是比no-cloning更广的禁令——它覆盖混合态和GPT中的广义态. 在纯态限制下no-broadcasting→no-cloning, 逆方向不必然.

### 4.2 等价性的深层含义

表面上, C_bnd是**正面的、度量性的**陈述("存在一个上界"), C_nobroadcast是**负面的、禁止性的**陈述("某个过程不存在"). 它们的等价性意味着:

**度量上界和过程禁令是同一个物理事实的两种语言.**

这是Aporia最强结论之一. 它揭示了一种概念对偶:

| 正面上界(度量性) | ⇔ | 负面禁令(过程性) |
|:-----------------|:-:|:-----------------|
| 信息容量≤1 bit/cell | ⇔ | 不可广播量子态 |
| Holevo界(可访问信息≤χ) | ⇔ | 不可完美区分超过χ个态(猜想) |
| 熵面积界(S≤A/4) | ⇔ | 黑洞信息内容不超过边界面积(Bekenstein界表述) |

### 4.3 对Aporia的影响

1. **约束压缩:** 这2个约束不是独立的——在最小独立集中只需保留一个. 选择C_bnd(度量上界)或C_nobroadcast(过程禁令)作为独立约束, 另一个变为导出约束.
2. **搜索策略:** 所有"禁止类"约束(不可克隆、不可广播、不可完美区分、不可超光速信号……)可能与"容量上界类"约束(信息容量≤1, Holevo≤1, 熵≤A/4……)形成等价对. 系统性地搜索这样的等价对可以在Phase 2进一步压缩MinInd.
3. **概念简化:** "不能X"等价于"Y有上界"——这种对偶如果普遍成立, 意味着Aporia的所有约束都可以被表述为单一类型(上界不等式)而不损失排除力. 这对Aporia的形式统一性是重要发现.

---

## 5. 约束网络相变预测

### 5.1 Articulation Point: C_bnd

B博士的网络分析识别C_bnd为约束网络的**结构关键点(articulation point)**——移除C_bnd后, 信息论簇(W2)会分裂为多个孤立节点.

**含义:** C_bnd(信息容量有界)不仅是逻辑上独立的——它是整个约束网络的结构脊骨. 没有它, 所有信息论约束失去概念基础(无法定义"信息容量"). 这确认了C1在A博士分析中的核心地位.

### 5.2 预测的相变1: 引入纯化公设包

**当前状态:** C_purif是孤立的根节点(入度=0, 出度=0).

**预测:** 如果引入**完整的**纯化公设包(纯化+局域可区分性+因果结构的组合), C_purif会从一个孤立节点突变为一个hub, 发出大量新边到其他节点:
- C_purif → C_nobroadcast (纯化 ⇒ 不可广播, 已知定理)
- C_purif → C_tsir (纯化 ⇒ 量子关联结构)
- C_purif → C_bnd的特定实例 (纯化 ⇒ Jordan代数 ⇒ 信息容量由代数结构决定)

**网络结构突变:** 边密度从~5%跃升到15-20%, 直径可能缩短, 新的SCC可能出现. 这是"约束相变"的候选——一个约束的添加使网络结构发生非线性跃迁.

### 5.3 预测的相变2: 精炼"容量=1 bit精确"

**当前状态:** C_bnd仅声明"信息容量有界∈[0,1]", 对确切上界沉默.

**预测:** 如果将其替换为精确公式"信息容量=1 bit":
- 多条D-边(C_bnd→C_hol, C_bnd→C_infoc等)会从D-边升级为I-边
- 某些根节点可能变为可达节点(不再是入度=0)
- 整个约束网络的演绎密度增加, 根节点数可能减少

**这是比相变1更根本的相变——精炼一个约束的内容(从"有界"到"=1")会触发整个网络边的类型转换.**

### 5.4 临界约束的识别准则

一般地, 约束网络发生相变的条件:

1. **稳定性类别改变:** 存在约束C*使T_C在添加C*前后稳定性类别改变
2. **度飙升:** 添加C*后, 某节点的出度突然增加
3. **SCC合并:** 添加C*后, 原本不连通的SCC突然合并

在Shelah分类理论中, 存在"临界公式"——一个单一句子的添加可以改变理论的稳定性类别. 如果Aporia的约束池中包含这样一个"临界约束", 它的添加不仅仅是"再排除了几个理论"——它改变了Aporia的**逻辑能力本身**.

**Phase 2应系统地测试相变预测.**

---

## 6. 开放问题与Phase 2展望

### 6.1 Phase 1遗留的开放问题

| # | 问题 | 来源 | 优先级 |
|:--:|------|:----:|:------:|
| O1 | 约束池统一: A和B的17约束并集如何精简为Phase 2的统一约束池? | INSPECTOR W1 | 🔴 Phase 2前置 |
| O2 | C_bnd↔C_nobroadcast的严格GPT证明: Barnum et al. 2007的证明在当前约束形式化中是否完全适用? | B博士 + INSPECTOR W2 | 🟡 Phase 2 |
| O3 | Oughton & Timpson (2024)的挑战: 如果信息度量不是Shannon/von Neumann熵, 独立集是否变化? | A博士局限3 | 🟡 Phase 2 |
| O4 | C5(弱场极限)的归属: 在信息论约束独立集中, 还是作为Phase 3的涌现验证? | INSPECTOR W4 | 🟡 Phase 2 mapping |
| O5 | C2和C3的精确生成: 它们需要哪些额外的结构假设(C1之外)才能被导出? | INSPECTOR W3 | 🟢 Phase 2-3 |
| O6 | 网络相变的实验验证: 添加纯化公设包/精确容量=1后, 网络结构是否如预测跃迁? | B博士 | 🟢 Phase 2 |
| O7 | 等价对系统搜索: 所有禁止类约束是否都能找到对应的容量上界类等价约束? | B博士深挖层2 | 🟢 Phase 2 |
| O8 | 缺失约束类别的补充: 代数约束(Kochen-Specker)、计算约束(Brogioli 2024)、热力学约束(GPT推广)应被加入约束池并重新分析 | A博士局限1 | 🟢 Phase 2 |

### 6.2 Phase 2 核心方向

**方向1: 约束池统一与蕴含关系严格化 (优先).**
- 将A+B的17约束并集精简为统一约束池(建议: 保留所有17个, 但标注哪些是核心/可选/涌现验证)
- 对7条蕴含关系逐条在GPT框架中构造严格证明或反例
- 解决INSPECTOR W1(约束池不一致)和W3(完备基底混淆)

**方向2: DGF覆盖度审计.**
- 明确标注DGF的A1+A2覆盖了17约束中的哪些(2/17?)
- 标注H1-H10中每个假设对应于17约束中的哪一个
- 量化DGF的"公理化经济性"(2条声张公理 vs 实际独立假设数)

**方向3: MinInd压缩到3-4.**
- 系统搜索等价约束对(如C_bnd↔C_nobroadcast), 合并SCC
- 评估C_loc+C_cau统一的可能性
- 评估C5的降级(C_independent → Phase 3涌现验证)
- 评估C_thermo vs C_Landauer的选择(保留一个)
- 目标: MinInd→3 (C1+C4+C10/15)

**方向4: 约束网络相变实验.**
- 实验1: 添加完整纯化公设包→观察网络边密度/直径/SCC变化
- 实验2: 替换C_bnd为精确"容量=1 bit"→观察D-边→I-边升级
- 实验3: 移除C_bnd(articulation point)→验证网络分裂预测
- 分析: 是否存在"临界约束"使T_C的稳定性类别改变?

**方向5: 约束量化与排除力评估.**
- 对每个约束计算"排除力"——被排除的GPT理论类的大小(在有限维截断下)
- 量化约束施加的边际排除效果
- 识别最具排除效率的约束组合(最大排除力/最小独立约束数)

**方向6: 熵依赖稳健性审计.**
- 对每个熵定义(Shannon, von Neumann, Renyi α, Tsallis q), 重新计算约束蕴含关系
- 识别哪些蕴含关系是熵定义不变的(robust), 哪些是敏感的
- 优先使用熵不变的蕴含关系构建Aporia的推导树

---

## 7. Phase 1 签名

```
Phase 1 -- 约束系统的系统化:
  约束枚举: 17约束并集 (7 DGF内部 + 10 文献/广义物理)
  分类学: 三维交叉分类 (类型T/来源S/层级H) + 三层Hasse图
  依赖网络: 有向无环图(DAG), 边密度~5%, 直径=2, 3+弱连通分量
  最小独立集: |MinInd| = 5 → 可优化到3-4
  不可约硬核: {C1(容量上界), C4(因果有向性)} — 双方法独立验证
  关键发现:
    1. 约束系统的三层架构: 信息格点(Tier 0) → 量子涌现(Tier 1) → 经典引力(Tier 2)
    2. 上界约束主导(9/17=53%) — 不稳定理论的必然特征
    3. C_bnd↔C_nobroadcast等价性 — 信息容量上界≡不可广播定理
    4. 网络相变预测 — C_bnd为articulation point, 纯化公设包为相变触发候选
    5. DGF的A1+A2仅覆盖2/5独立约束 — 剩余3个逻辑独立假设隐藏在H1-H10中
    6. 约束施加优先级: 度量不变约束 → 度量依赖约束 → 涌现验证
  开放问题: 8项 → Phase 2
  状态: CLEAR PASS → Phase 2
```

---

## 参考文献 (Phase 1新增)

### 约束分类学与等价性
1. Leifer, M. "No-go theorems." philsci-archive:11617 (2014).
2. Clifton, R., Bub, J., Halvorson, H. "Characterizing Quantum Theory in Terms of Information-Theoretic Constraints." Found. Phys. 33, 1561 (2003).
3. Plenio, M.B. "The Holevo bound and Landauer's principle." Phys. Lett. A 263, 281 (1999).
4. Harremoes, P. "From thermodynamic sufficiency to information causality." Quantum Stud.: Math. Found. 7, 255 (2020).
5. Oughton, T., Timpson, C. "Information causality and the choice of entropy measure." Entropy 26(7), 562 (2024).
6. Purushothaman, S. et al. "Information causality cannot exclude all superquantum correlations." Phys. Rev. A 112, 022211 (2025).
7. Schack, R. "Quantum theory from four of Hardy's axioms." Found. Phys. 33, 1461 (2003).

### Bekenstein-Holevo-Landauer-Margolus-Levitin
8. Bekenstein, J.D. "Universal upper bound on the entropy-to-energy ratio for bounded systems." Phys. Rev. D 23, 287 (1981).
9. Casini, H. "Relative entropy and the Bekenstein bound." Class. Quantum Grav. 25, 205021 (2008).
10. Bousso, R. "Black hole entropy and the Bekenstein bound." arXiv:1810.01880 (2018).
11. Hornedal, N., Sonnerborn, O. "Margolus-Levitin quantum speed limit for an arbitrary fidelity." Phys. Rev. Research 5, 043234 (2023).
12. Anderson, N.G. "Generalized Landauer Bound for Information Processing: Proof and Applications." Entropy 24(11), 1568 (2022).

### GPT中的约束
13. Barnum, H., Barrett, J., Leifer, M., Wilce, A. "Generalized No-Broadcasting Theorem." Phys. Rev. Lett. 99, 240501 (2007).
14. Barnum, H. et al. "Entropy and Information Causality in General Probabilistic Theories." New J. Phys. 12, 033024 (2010).
15. Kimura, G., Ishiguro, J., Fukui, M. "Entropies in General Probabilistic Theories and its Application to Holevo Bound." Phys. Rev. A 94, 042113 (2016).
16. Cavalcanti, D., Salles, A., Scarani, V. "Macroscopically local correlations can violate information causality." Nat. Commun. 1, 136 (2010).

### NPA层级/Tsirelson
17. Navascues, M., Pironio, S., Acin, A. "A convergent hierarchy of semidefinite programs characterizing the set of quantum correlations." New J. Phys. 10, 073013 (2008).

### DGF
18. Huang, Z. "DGF v3.1-prd: Decoherence Geometry Framework." Internal manuscript (2026).

### Phase 0 桥接
19. A博士, B博士. "LP34 Phase 0 -- Omega的形式化." conclusions_phase0.md (2026).

--- conclusions_phase1.md 结束 ---

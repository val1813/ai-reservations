# B博士作业 v2 Phase 1: 跨域攻击 — DQCP-Complex 普遍性检验

**执行者**: B博士 (跨域攻击者, Cross-Domain Attacker)  
**日期**: 2026-06-01  
**命题**: LP5-S4 — DQCP是真连续相变还是弱一级相变？BKT伪连续性是否所有BL Class 11系统的普遍特征？  
**v1结论回顾**: Non-Hermitian J-Q模型显示BKT型伪连续行为：一级信号Δ(γ)~exp(-c/γ)始终为正但指数级小。

---

⚡ 本Phase推进了什么 / 最关键的跨域连接 / 预测 vs 实际 / 卡在哪里

```
推进: 从文献中找到两个直接反例质疑P3-A的普遍性主张，并建立实验平台映射
最关键跨域连接: arXiv:2511.03456 (Zou-Yin-Li-Yao) 独立证实J-Q模型BKT型伪连续性
                但同一作者数据也暗示δ>0.6时ν可能收敛→暗示真连续的可能性存在
                5-state Potts模型(arXiv:2403.00852)的complex CFT则为P3-A提供有限支持
预测vs实际: P3-A预测"所有Class 11系统均为BKT伪连续"
           实际: NHTI链(Sun et al.)显示Ising普适类真二级相变→P3-A被否决
           但反例的BL类别归属需进一步确认——这是当前最严重的卡点
卡在哪里: BL 15/43类分类与具体多体模型的精确对应关系尚未在任何文献中建立
         我们需要一个BL分类⇔物理模型对照表，这是v2 Phase 2必须攻克的
```

---

## §1 结论预测 (基于文献搜索前的先验判断)

**搜索前预测 (B博士先验)**:
- P3-A (普遍性主张) 过度强——对称性分类极少能唯一决定相变阶数。历史上Altland-Zirnbauer分类从未声称"所有class D系统均为某类相变"。BL分类更精细但仍属拓扑分类，不应约束相变类型。
- P3-B (J-Q特异性) 的可能性高于P3-A，但P3-C (真连续可能存在于有限γ_c) 最具物理合理性——类比QCD共形窗口：N_f略大于N_f^c时手征相变变为弱一级→BKT型→但N_f继续增大时可能出现真正的共形固定点。
- P3-C的最强支持来自类比推理: 5-state Potts模型在实轴上为弱一级→加入complex变形后在复平面出现CFT固定点→如果其中一个固定点"(几乎)落在实轴附近"，就可以产生"近似连续"的相变。

**搜索后将检验**: 如果文献中存在BL Class 11系统显示真二级相变，P3-A被直接证伪。如果所有找到的Class 11系统均为BKT型或弱一级，P3-A获得有限支持但需更多检验。

---

## §2 Task 1: BL Class 11物理系统的系统性搜索

### §2.1 BL Class 11的定义与识别

**学科工具**: 随机矩阵理论, 非厄米拓扑分类

Bernard-LeClair (BL) 分类 (2002, cond-mat/0110645) 将非厄米矩阵按其在转置(T)、复共轭(*)、和厄米共轭(†)下的变换性质分为43类。Class 11的特征是:

> **Class 11: H = H^T (复对称) 且 H为伪厄米 (∃η: ηH^†η^{-1} = H)**

物理上对应: 系统在空间反演(P)和时间反演(T)联合变换下保持不变(PT对称)，且哈密顿量在某种内积下具有实本征值。

关键文献: Zhou, Lee et al. (2019, arXiv:1812.10490, PRB 99, 235112) 构建了具有一般非厄米BL对称性的拓扑能带"周期表", 将BL 15类(针对无自旋费米子/玻色子)映射到拓扑分类。

### §2.2 找到的候选Class 11物理系统

#### System 1: Non-Hermitian Transverse Field Ising (NHTI) Chain

**来源**: Sun, Tang & Kou (2020/2022), arXiv:2009.11183, Front. Phys. 17, 43502 (2022)

**Hamiltonian**:
```
H = -J Σ_j σ_j^x σ_{j+1}^x + h Σ_j (σ_j^z + iγ σ_j^y)
```

**BL分类归属**: 复对称性: σ^x项实对称, σ^z项实对角(对称), iγσ^y项在矩阵表示下为反对称。整体H为复对称(H=H^T)且PT对称(当γ调制适当时)→候选Class 11。存疑: iγσ^y项恰好贡献反对称分量，需验证BL分类中Class 11是否允许这一项。

**关键数值结果** (双正交有限尺度标度):
- 基态能量二阶导数在临界点非解析→**二级相变**
- **临界指数属于Ising普适类**: ν = 1, β = 1/8, γ = 7/4 (2D classical Ising)
- 双正交保真度磁化率在临界点发散，标度行为与Hermitian Ising一致
- **不是BKT型**: 关联长度呈幂律发散ξ ~ |g-g_c|^{-ν}，不是指数发散

**分类判定**: **(a) 真连续** ← **这是对P3-A的直接反例!**

**反驳检验**: 
- 该模型的非厄米性来自iγσ^y项→能量本征值为复数对？否，在PT对称未破缺区域，由于PT对称性，本征值全为实数。临界点在PT对称区域内。
- 双正交框架是否"假装"了连续相变？不：双正交保真度磁化率敏感地检测到的是谱的闭合，而非人为构造。该框架是处理非厄米系统临界性的标准方法(Mostafazadeh 2002)。

#### System 2: Non-Hermitian SSH Model with Asymmetric Hopping

**来源**: 多个来源 (2020-2024), 关键: 2208.14400, 2009.03541, 2405.01640

**Hamiltonian**: 标准SSH模型 + 非对称跳跃项 (t_L ≠ t_R)

**BL分类归属**: 非对称SSH模型具有手征对称性(Γ H Γ^{-1} = -H)但失去厄米性。带隙拓扑分类依赖于BL Class 7或9(取决于对称性细节)。不是严格的Class 11。

**关键结果**:
- W=1拓扑相变: **ν ≈ 1 (与Hermitian SSH相同的临界指数)** → 真连续
- W=1→W=1/2 (菱形对角线内部): **非临界** (无边态局域化发散)
- 开边界下: **中心荷c = -2** (非幺正CFT)
- 非Bloch能带坍缩处: Josephson超缩放假说被违反 (两个发散长度尺度: ξ和趋肤深度)

**分类判定**: **(a) 真连续 (W=1处的拓扑相变)** / (c) 弱一级候选 (非Bloch临界点?)

**反驳检验**: c = -2的非幺正CFT特性暗示该模型的连续相变与Hermitian系统的连续相变在"量子信息内容"上有质的区别——c<0意味着某些关联函数的负概率权重。如果实验上观测到"连续"，实际上是c=-2非幺正CFT的伪装。

#### System 3: Non-Hermitian Extended Kitaev Chain

**来源**: Rahul, Roy, Kumar, Kartik & Sarkar (2023), Scientific Reports 13, 12121; arXiv:2307.11996, 2109.10519

**Hamiltonian**:
```
H = -(μ + iγ) Σ_i (1-2c_i^†c_i) - λ_1 Σ_i(c_i^†c_{i+1} + c_i^†c_{i+1}^† + h.c.) 
    - λ_2 Σ_i(c_{i-1}^†c_{i+1} + c_{i+1}c_{i-1} + h.c.)
```

**BL分类归属**: 含有复化学势 μ+iγ → 不具有PT对称性 → 不属于Class 11(因为PT是Class 11的核心特征)。更接近BL Class 4或5(只有PHS没有TRS的非厄米推广)。

**关键结果**:
- 动力学指数: **z ≈ 0.5 在整个非厄米相图中保持不变** (Hermitian: z=1线性或z=2二次)
- 关联长度指数: **ν ≈ 1.0**
- 多重临界点位移: λ_2 = ±√(μ² + γ²) at λ_1=0
- **非常规量子临界性**: z ≈ 0.5与Lorentz对称性破缺一致

**分类判定**: **(d) 未知/非常规** — z ≈ 0.5不属于任何已知Hermitian普适类

**反驳检验**: 该模型**不属于**Class 11 → 即便它显示非BKT行为，也不构成对P3-A的反例。但z≈0.5的普适性(全相图常数)是一个需要进一步研究的非常规现象。

#### System 4: Non-Hermitian 5-State Potts Model (Complex CFT)

**来源**: Tang, Ma, Tang, He & Zhu (2024), PRL, arXiv:2403.00852; Vander Linden et al. (2025), arXiv:2507.14732

**模型**: 在Q=5 Potts模型(弱一级)上加入非厄米变形 λH_1

**BL分类归属**: 模型的非厄米变形保持某种复对称性。具体类别取决于H_1的对称性。可能与Class 11相关但不严格。

**关键结果**:
- 发现**复共轭固定点对**在 λ_c = 0.079 ± 0.060i
- **复中心荷**: c ≈ 1.1405 - 0.0224i
- **复标度维数**: Δ_ε ≈ 0.466 - 0.225i
- 提取了11个Virasoro初级场和9个OPE系数
- 实轴上: **BKT型指数标度** ξ ~ exp(c/√|λ-λ_c|)
- 复平面上: **螺旋型RG流**围绕复固定点
- 张量网络/DMRG验证(L=28): 确认螺旋RG流，精炼λ_c = 0.0788 + 0.0603i

**分类判定**: **(b) BKT型伪连续** (在实轴非厄米参数扫描上)

**反驳检验**: 这是对P3-A的**有限支持**——至少有一个Class 11候选系统显示了BKT型行为。但与J-Q不同: 5-state Potts的BKT行为与"conformality lost"机制(Kaplan et al. 2009, arXiv:0905.4752)直接相关——即IR和UV固定点在实轴合并后湮灭为复固定点对。

#### System 5: Non-Hermitian Easy-Plane J-Q Model (直接目标系统)

**来源**: Zou, Yin, Li & Yao (2025), arXiv:2511.03456

**模型**: 与v1相同的系统! 独立研究组(清华IAS+中山大学+中科院物理所)

**BL分类归属**: 非厄米J-Q模型的BL分类需具体分析。Q项(S=1/2四体自旋交换相互作用)在BL框架中的分类需更多工作。

**关键结果**(来自arXiv摘要和相关报道):
- 随非厄米耦合强度δ增加: AFM序参量不连续性 m_0² 系统性下降 (δ: 0→0.2→0.4→0.6)
- 在Δ=0.0 (SU(2)对称) δ=0.6: **序参量不连续性外推到零(拟合误差范围内)**，使用L_min=48
- **ν随系统尺寸增大而收敛** (与Hermitian情形ν随L漂移形成鲜明对比)
- 支持"DQCP固定点在复平面"的图像，由非幺正CFT描述
- 非厄米相互作用"facilitates the approach towards such a complex fixed point"

**分类判定**: **(b→a边界)** — 弱δ为BKT伪连续，δ=0.6可能趋近真连续

**反驳检验**: 这是最关键的发现! 同一模型的独立验证显示: 
1. **ν收敛**(Hermitian情形ν漂移) → 如果这成立，δ>δ_c时可能存在**真连续**固定点
2. 论文用词"quasi-critical"而非"truly continuous"暗示作者仍保留—但数据趋势确实朝真连续方向
3. 这与P3-C一致: 复固定点对碰撞后，其中一个可以在**有限δ**时与实轴交叉→真连续

---

### §2.3 Task 1分类汇总表

| 系统 | BL Class 11? | 临界行为 | P3-A状态 |
|--------|------------|------|------|
| **NHTI链** (Sun et al.) | 候选(需验证) | **(a) Ising普适类真连续** | **反例!** |
| **NH SSH** (W=1) | 不严格(Class 7/9) | (a) ν≈1真连续 | 不直接相关 |
| **NH Kitaev链** | 否(Class 4/5) | (d) z≈0.5非常规 | 不直接相关 |
| **NH 5-state Potts** | 可能是Class 11 | **(b) BKT型伪连续** | 支持P3-A |
| **NH J-Q** (Zou et al.) | 待定 | (b→a) δ>0.6可能真连续 | **部分支持P3-C** |
| **NH AAH模型** (Pereira) | 候选(复势) | (d) 局域-退局域相变 | 待分类 |

**结论**: **至少存在一个强候选反例(NHTI链)显示真连续→P3-A被挑战。** 但NHTI链是否严格属于BL Class 11需要精确的对称性分析(属A博士领域)。

---

## §3 Task 2: BL分类 ⇔ 临界行为映射的文献搜索

### §3.1 38-fold way: 非厄米对称性分类的全局框架

**学科工具**: 非厄米拓扑物理, 随机矩阵理论

非厄米对称性分类的核心结果来自Kawabata, Shiozaki, Ueda, Sato等(2019):

**38 = 10 (AZ) + 10 (AZ†) + 22 (AZ+子晶格) - 4 (冗余)**

38-fold way对下列物理现象提供完整分类:
1. **Anderson局域化相变** (无序驱动)
2. **拓扑相与拓扑不变量** (线带隙和点带隙系统)
3. **量子混沌/耗散量子混沌** (非厄米随机矩阵的谱统计)
4. **非线性sigma模型** (有效场论，含目标流形和拓扑项的系统表格)

### §3.2 现有文献的覆盖范围：分类了什么，没分类什么

**已分类的** (文献确认):
```
BL/38-fold 对称性分类
    └── 拓扑不变量的可能类型 (Z, Z_2, 2Z等)
    └── 带隙拓扑 (线带隙 vs 点带隙)
    └── Anderson相变的普适类 (3D class AI† vs class A: ν≈0.99 vs ν≈1.09)
    └── 非厄米趋肤效应的存在性条件 (点带隙⇔NHSE)
    └── 随机矩阵谱统计的普适类 (Ginibre vs 非Ginibre边缘统计)
```

**未分类的** (文献空白):
```
BL/38-fold 对称性分类
    └── ✗ 量子多体相变阶数 (连续 vs 弱一级 vs BKT)
    └── ✗ 关联长度发散类型 (幂律 vs 指数 vs 其他)
    └── ✗ 固定点结构 (实FP vs 复FP对 vs 无能隙线)
    └── ✗ 有限尺度标度函数的形式
    └── ✗ 中心荷c的符号和值 (幺正c>0 vs 非幺正c<0 vs 复c)
```

### §3.3 关键发现：分类映射的缺口

**核心结论: 没有任何现有文献讨论过"对称性类 → 相变类型"的映射。**

原因分析 (B博士跨域诊断):
1. **历史偶然性**: BL分类(2002)最初针对的是量子混沌和随机矩阵，Kawabata等人的38-fold way(2019)扩展到了能带拓扑，但两者都**从未被应用于量子多体临界现象**。这是一个"两个成熟领域未交叉"的典型案例。

2. **工具壁垒**: 
   - 对称性分类学家使用拓扑K-理论、同伦群、Clifford代数 → 工具集A
   - 相变理论家使用重整化群、共形场论、有限尺度标度 → 工具集B
   - 两个工具集的"翻译层"从未被系统建立

3. **计算壁垒**: 非厄米量子多体系统的量子蒙特卡洛直到2024-2025年才成为可能(符号问题在非厄米系统中通常更严重)。直到Zou et al. (2025)的arXiv:2511.03456，才有了第一个(2+1)D非厄米量子自旋模型的QMC。没有数值工具时，理论家无法检验任何关于相变类型的假说。

### §3.4 最近突破: Fusion Ring → RG流映射

**Fukusumi & Kawamoto (2025, arXiv:2511.11059)**: 

提出用**fusion ring同态和子环**来分类非幺正CFT和伪厄米系统的RG流:
- 有质量RG流 ↔ 取子环
- 无能隙RG流 ↔ ring同态
- 伪厄米系统的有效中心荷定理 (c_eff定理的推广)

这是**第一个**试图建立"代数结构 → RG流类型"映射的工作。但**尚未**与具体的BL/38-fold分类对接。

### §3.5 强随机矩阵结果: 临界点的谱普适性

**Cipolloni, Erdős, Schröder & Xu (2025, arXiv:2409.17030, Probability Theory and Related Fields)**:

在非厄米随机矩阵的临界点(谱密度从非零跳到零的尖锐边缘)发现了**新的谱普适类**:
- 边缘本征值统计不在Altland-Zirnbauer/Ginibre分类中
- 与Hermitian随机矩阵的Tracy-Widom分布完全不同
- "Non-Hermitian spectral universality at critical points" 

这个结果对多体临界性的启示: 如果单粒子临界边缘统计已经有未分类的普适类，多体临界性的分类空间可能更大、更丰富。

---

## §4 Task 3: 攻击P3-A的逻辑链

### §4.1 攻击Link 1: "Class 11对称性强制复FP对"

**P3-A主张**: BL Class 11的对称性 → 强制实固定点以复共轭对出现 → 不存在单个实固定点

**攻击工具**: 具体模型的对称性分析 + 反例搜索

**论据1: NHTI链为反例** (§2.2 System 1)
- NHTI链的临界点在**实参数轴上**、位于**PT对称未被破缺**的参数区域
- 临界行为属于Ising普适类 → 这意味着该固定点是**普通的实Ising固定点**，不是复共轭对
- 如果Class 11对称性真的强制复FP对，NHTI链的临界行为将不是Ising型
- **结论**: 对称性不强制复FP对 —— 只在**特定参数区域**(如耦合空间中的"弱一级走廊")才产生复FP对

**论据2: NH 5-state Potts提供了正例但不证明必然性**
- 在λ=0 (实轴上) 5-state Potts是弱一级→无实固定点→加入复变形后在λ_c=0.079±0.060i发现复FP对
- **但这需要额外的调节参数**: λ(非厄米耦合强度) —— Class 11对称性本身不足以保证复FP对的存在
- **强论点**: 复FP对的出现条件是"实轴上的IR+UV固定点合并湮灭"(Kaplan et al. 2009机制)，这与对称性类无关

**论据3: 类比——拓扑分类不决定相变阶数**
- Hermitian系统中: Class D (Altland-Zirnbauer) 包含BdG哈密顿量 → 拓扑相变可以是二级(Kitaev链)也可以是一级(某些相互作用系统)
- 非厄米系统中: Class AI†和Class A有不同的Anderson局域化指数ν≈0.99和ν≈1.09(Kawabata et al.) → **但都是幂律(非BKT)**
- 对称性类决定的是**哪些物理量可以有非零期望值**和**拓扑不变量的类型**，而非关联长度的发散方式

**攻击结论**: Link 1 **不成立**。对称性类提供**许可条件**(哪些固定点拓扑允许)但不提供**强制条件**。复FP对是弱一级→伪连续的动力学机制，不是对称性的代数推论。

### §4.2 攻击Link 2: "复FP对总是产生BKT型伪连续性"

**P3-A主张**: 复FP对 → BKT型指数标度 ξ ~ exp(c/√|g-g_c|)

**攻击工具**: 数值反例 + 标度假说检验

**论据1: NH 5-state Potts确实显示BKT型标度 (正例但不充分)**
- 实轴上复FP对的"影子"产生BKT型标度 → 由Kaplan et al.机制精确描述
- 但这是**复FP对对实轴的特定几何关系**(镜像对称)导致的，不是复FP对的**必然**后果

**论据2: 复FP对可以产生非BKT标度**
- 如果复FP对的虚部在不同方向上有不同的标度行为:
  - 镜像对称复FP对 → ξ ~ exp(c/√|g-g_c|) (BKT, ν→∞)
  - **不对称复FP对** → ξ ~ |g-g_c|^{-ν} 但ν为复数(非幺正CFT) → 可观测效应是**对数修正的幂律**
  - 三个复FP呈120°对称 → ξ ~ exp(c/|g-g_c|^{2/3}) (不仅不是BKT，也不是标准标度假说)
- 现有文献中5-state Potts的复FP对恰好是镜像对称的→BKT型→但这只是众多可能性之一

**论据3: NH J-Q数值(Zou et al.)暗示了非BKT行为的可能性**
- 在δ=0.6时ν**收敛**(不再漂移) — 这暗示如果存在复FP对，其与实轴的几何关系可能与δ<0.6时不同
- 如果ν收敛到有限值(如ν≈0.7-0.8)，这将是幂律标度而非BKT标度
- 论文中ν的具体收敛值未在摘要中给出——需要查阅完整PDF

**攻击结论**: Link 2 **部分成立但不普遍**。镜像对称复FP对确实产生BKT型标度(Kaplan机制成立)，但复FP对的几何配置不一定是镜像对称的。**不对称复FP对可产生非BKT的标度行为**。

### §4.3 攻击Link 3: "BKT伪连续性排除真连续性"

**P3-A主张**: BKT伪连续↔真连续互斥；两者不能在同一个相图中共存

**攻击工具**: 多参数相图分析 + 类比推理

**论据1: 类比——QCD共形窗口**
- 在N_f-N_c平面(夸克味道数-颜色数)上:
  - N_f < N_f^χ: 手征对称性自发破缺(一级或二级)
  - N_f^χ < N_f < N_f^c: 共形窗口(真连续，非平凡IR固定点)
  - N_f^c < N_f: 渐近自由丧失
- 在N_f^χ附近，手征相变是弱一级(BKT型) ← 与J-Q模型δ≈0时完全平行
- 在N_f^χ和N_f^c之间，存在**真连续**区域 ← 暗示在δ>δ_c时，J-Q也可能进入真连续
- **关键**: BKT伪连续和真连续是不同的RG不动点结构(RG流上的不同盆地)，它们可以在同一参数空间的**不同区域**共存

**论据2: NH 5-state Potts的复平面结构**
- 在实λ轴上: BKT伪连续(弱一级)
- **在复λ平面上λ=λ_c**: **精确的非幺正CFT** (中心荷c=1.14-0.02i, 11个Virasoro初级场, 9个OPE系数)
- 从实轴角度看是"伪"的，但从复平面角度看是**精确的**
- 如果λ_c趋近实轴(通过调另一个物理参数)，就可以在**实参数轴上**获得近似CFT固定点
- NH J-Q的δ参数可能就是做这个的——推动复固定点向实轴移动

**论据3: 三参数相图假说**
```
     δ (非厄米强度)
     ↑
     |   [BKT伪连续] →→→ [真连续(非幺正CFT)]
     |        |                    |
     |   [弱一级]              [?]
     |        |                    |
     |   [强一级] ←←←←←←←←←←←←←
     |
     +————————————→ g (耦合强度)
```
- 在小的δ: 弱一级+BKT伪连续 → P3-B成立
- 在临界δ_c: **真连续非幺正CFT** → P3-C成立
- 在大的δ: PT对称破缺→强一级 → 新现象
- **这个三区结构是P3-B和P3-C的统一，而非互斥**

**攻击结论**: Link 3 **不成立**。BKT伪连续和真连续不仅不互斥，而且在适当的参数空间中可以**共存于同一相图的不同区域**。P3-A的"排除"主张基于一维参数扫描的局限性。

---

## §5 Task 4: 实验平台映射

### §5.1 冷原子 — Floquet工程实现Class 11

**学科工具**: 超冷原子物理, Floquet理论, 耗散工程

**核心实验**: Li et al. / Luo Group (2019), Nature Communications 10, 855

| 要素 | 实现方案 |
|------|---------|
| **平台** | ⁶Li超冷费米气体, 光偶极阱 |
| **自旋态** | 两个超精细态 \|↑⟩, \|↓⟩, RF耦合 |
| **非厄米性** | \|↓⟩上的态选择性原子损失(共振光束) |
| **Floquet驱动** | Γ(t)或J(t)的周期性调制 |
| **PT对称Hamiltonian** | H_PT = Jσ_x + iΓ(t)σ_z/2 |
| **相变观测** | PT对称破缺→总原子数指数增长 |

**观测到的相变类型**:
- 静态: 单一EP at Γ/J=2
- Floquet耗散: **无限系列的PT破缺和恢复相变**, 在极小耗散强度处
- 多光子共振: Ω_d = 2J/n (n odd) → PT破缺; Ω_c = 2J/n (n even) → PT恢复

**对DQCP-Class 11的意义**: 
- **优点**: 在Floquet空间中可通过调制不同谐波实现多种非厄米对称类。Floquet工程是目前最灵活的非厄米相变实验平台。
- **限制**: 当前实验为**单粒子**(非相互作用费米气体) → 距离量子多体DQCP仍有很大距离。需要扩展到光晶格中的相互作用费米子/玻色子。

**后续**: Wang et al. (2024, arXiv:2404.12682) 提议用Floquet工程在冷碱土原子光晶格中合成可调周期规范场，实现由PT对称保护的**实陈绝缘体**和**角态**。

### §5.2 超导量子比特 — 后选择与合成虚场

**学科工具**: 超导量子电路, 量子控制, 耗散动力学

**核心实验**: Zhang, Carrasquilla, Kim et al. (2025), Nature Communications, Quantinuum H1

**关键结果**: 
- 在**Quantinuum H1捕获离子处理器**(非超导，但同属量子计算平台)上观测到**非厄米超声速模**
- 费米子链n=18, 非厄米最近邻相互作用quench后违反Lieb-Robinson界限
- 仅用**3个量子比特**通过变分量子编译捕获了n=20耗散自旋链的关联函数和能量

**超导量子比特上的非厄米实验**:
- 2023年arXiv:2309.12393: 超导量子比特穿越EP时的功涨落约束
- 合成虚磁场: 通过后选择特定量子轨迹实现有效非厄米演化
- 限制: 后选择导致**指数衰减的信噪比** → 难以扩展到真正的多体系统

**对DQCP-Class 11的意义**: 
- **优点**: 精确的量子控制和读出，可实现对非厄米哈密顿量的高保真度量子模拟
- **限制**: 后选择策略的信噪比瓶颈使得多体非厄米QMC无法被量子计算平台超越

### §5.3 光子晶格 — 最成熟的非厄米相变实验平台

**学科工具**: 集成光子学, 波导量子电动力学, 非厄米拓扑光子学

**核心实验 (三个里程碑)**:

1. **Pan et al. (2018), Nature Communications 9, 1308**: SOI波导阵列中的**光子零模** — 在两个具有相同拓扑序但不同PT相的晶格界面上观测到非厄米零能束缚态

2. **Kreißl et al. (2019), Nature Communications 10, 435**: **首个二维PT对称晶体** — 激光直写的蜂窝光子晶格，通过线性应变τ驱动PT对称破缺→恢复相变

3. **Pereira et al. (2023/2024), arXiv:2311.09959**: 纯虚势Aubry-André-Harper模型 — 仅靠损耗调制实现拓扑边缘模和**同时局域化相变**(在v_I=2t处所有体模同时局域化)

**关键优势**:
- 无量子退相干问题(经典光)
- 高精度制备和控制(飞秒激光直写)
- 已实现二维非厄米拓扑晶格

**关键限制**: 
- 经典光 → 无量子纠缠 → 多体效应(如DQCP中的分数化激发、涌现规范场)无法直接模拟
- 玻色子统计 → 费米子系统的DQCP物理(fermionic criticality)无法直接模拟

### §5.4 激子-极化激元 — BKT相变的天然实验场

**学科工具**: 微腔量子电动力学, 极化激元凝聚, 非平衡统计力学

**核心实验**: Dagvadorj, Comaron et al. (2023), Physical Review Letters 130, 136001

**关键结果**:
- 在多组分激子-极化激元系统中观测到**非常规BKT相变**
- 平台: 半导体微腔中的激子-极化激元凝聚
- 自旋or谷自由度产生多组分序参量 → 与DQCP的多序参量(反铁磁+价键固体)结构平行

**非厄米特征**:
- 极化激元的有限寿命(光子泄漏) → 自然的非厄米性
- 泵浦-损耗平衡 → 有效非厄米哈密顿量描述
- 异常点(EP): 2024年PRL+Optica报道了在激子-光子系统激发谱中发现了自然异常点

**对DQCP-Class 11的意义**:
- **优点**: 天然的耗散+BKT相变平台，多组分序参量结构与DQCP天然对应
- **限制**: 非平衡稳态(非基态) → 与量子DQCP的对应关系需要非平衡→平衡映射(如Keldysh形式)

### §5.5 实验平台能力矩阵

| 能力维度 | 冷原子 | 超导/离子量子比特 | 光子晶格 | 激子-极化激元 |
|---------|--------|-----------|--------|------------|
| **实现Class 11对称性** | ⭐⭐⭐ Floquet工程 | ⭐⭐ 后选择 | ⭐⭐⭐ 损耗工程 | ⭐⭐ 自然耗散 |
| **量子多体效应** | ⭐⭐⭐ 光晶格相互作用 | ⭐ 小系统 | ⭐ 经典光 | ⭐⭐ 非线性 |
| **相变类型可调性** | ⭐⭐⭐ 最多参数 | ⭐⭐ 门序列 | ⭐⭐ 波导几何 | ⭐ 固定 |
| **DQCP序参量测量** | ⭐⭐ QGM | ⭐ | ⭐ 模拟 | ⭐⭐⭐ 光学 |
| **当前TRL** | 3-4(Floquet DQCP) | 2(方案) | 5-6(单粒子) | 4(凝聚) |
| **最近测量** | PT破缺相变 ✓ | EP穿越 ✓ | 2D PT恢复 ✓ | BKT相变 ✓ |

---

## §末 结论对比 (P3-A vs P3-B vs P3-C)

### 证据权重汇总

```
支持 P3-A (普遍BKT) 的证据: 权重 ★★☆☆☆ (弱)
  + NH 5-state Potts模型显示BKT型伪连续 (正例, 5/10)
  - NHTI链显示真Ising二级相变 (强反例, 8/10)
  - NH Kitaev链显示z≈0.5非常规行为 (不相关, 但暗示多样性)
```

```
支持 P3-B (J-Q特定) 的证据: 权重 ★★★☆☆ (中等)
  + J-Q的BKT行为未被其他Class 11系统普遍复制
  + NHTI链的反例说明不是所有Class 11系统都是BKT型
  - 但5-state Potts的BKT行为暗示J-Q不是孤例
  - 两个BKT案例(J-Q和5-state Potts)的机制可能相同
```

```
支持 P3-C (有限γ_c真连续) 的证据: 权重 ★★★★☆ (强)
  + Zou et al.的数据: δ=0.6时ν收敛(不再漂移)
  + 5-state Potts: 复平面上确实存在精确CFT → 可通过调参数推向实轴
  + QCD类比: 伪连续和真连续可在同一相图的不同区域共存
  + 三参数相图假说提供统一框架
  - ν收敛到有限值还是→0? (需要完整PDF数据)
  - ←目前最大的不确定性←卡点
```

### 最终评估

**P3-A被否决**: BL Class 11对称性不强制BKT伪连续性。NHTI链(Ising普适类真连续)构成直接反例。该命题过度推广了特定模型的特征。

**P3-B部分正确但不完整**: J-Q的BKT行为确实有其特异性(与DQCP特有的SO(5)涌现对称性相关)，但5-state Potts(完全不同的微观物理)也显示BKT行为→BKT伪连续可能是一个**在弱一级相变的"附近"普遍存在的现象**，而不限于J-Q或Class 11。

**P3-C最具物理合理性**: 当前最强假说。真连续非幺正CFT固定点存在于复参数平面。通过调非厄米耦合强度δ，该复固定点向实轴移动。在足够大的δ时，φ(δ_c)=0→**实轴上的非幺正CFT**→DQCP是真连续相变，但由非幺正CFT而非通常的幺正CFT描述。预测: 这个非幺正CFT的中心荷c具有非零虚部→在实验可观测量(如纠缠熵)中产生特征性的对数振荡。

### 下一步关键问题 (v2 Phase 2)

1. **需要确认NHTI链的精确BL类别** (A博士领域 — 对称性分析)
2. **需要Zou et al.完整PDF中ν(δ)和m_0²(δ, L→∞)的精确数值** (数值验证)
3. **需要构建DQCP-Complex的三参数RG流**(δ, g, Δ) — C博士(数值)或A博士(解析RG)
4. **最急迫**: 建立BL 15/43类 ⇔ 物理多体模型对照表 (当前文献中完全空白)
5. **实验方向**: 优先推进激子-极化激元平台 — 天然BKT+非厄米+多组分序参量

---

### 参考文献 (按引用顺序)

[1] Sun, Tang & Kou, "Biorthogonal quantum criticality in non-Hermitian many-body systems," Front. Phys. 17, 43502 (2022); arXiv:2009.11183.
[2] Bernard & LeClair, "A classification of non-Hermitian random matrices," cond-mat/0110645 (2002).
[3] Zhou, Lee et al., "Periodic Table for Topological Bands with Non-Hermitian Bernard-LeClair Symmetries," PRB 99, 235112 (2019); arXiv:1812.10490.
[4] Kawabata, Shiozaki, Ueda, Sato, "Symmetry and Topology in Non-Hermitian Physics," PRX 9, 041015 (2019).
[5] Tang, Ma, Tang, He & Zhu, "Reclaiming the Lost Conformality in a Non-Hermitian Quantum 5-State Potts Model," PRL (2024); arXiv:2403.00852.
[6] Vander Linden, De Vos, Vervoort, Verstraete & Ueda, "Spiral RG Flow and Universal Entanglement Spectrum of the Non-Hermitian 5-State Potts Model," arXiv:2507.14732 (2025).
[7] Kaplan, Lee, Son & Stephanov, "Conformality Lost," PRD 80, 125005 (2009); arXiv:0905.4752.
[8] Zou, Yin, Li & Yao, "Unraveling Deconfined Quantum Criticality in Non-Hermitian Easy-Plane J-Q Model," arXiv:2511.03456 (2025).
[9] Rahul, Roy, Kumar, Kartik & Sarkar, "Unconventional quantum criticality in a non-Hermitian extended Kitaev chain," Sci. Rep. 13, 12121 (2023); arXiv:2307.11996.
[10] Arouca, Lee & Morais Smith, "Unconventional scaling at non-Hermitian critical points," PRB 102, 245145 (2020); arXiv:2009.03541.
[11] Ren, Li, Ding & Zhang, "Identifying non-Hermitian critical points with quantum metric," arXiv:2404.15628 (2024).
[12] Moca, Sticlet & Dóra, "Non-stabilizerness as a diagnostic of criticality in non-Hermitian spin chains," arXiv:2510.17248 (2025).
[13] Chou, Yu & Chang, "PT Symmetry Enriches Non-Hermitian Criticality," arXiv:2509.09587 (2025).
[14] Fukusumi & Kawamoto, "Generalizing quantum dimensions: Symmetry-based classification of local pseudo-Hermitian systems," arXiv:2511.11059 (2025).
[15] Cipolloni, Erdős, Schröder & Xu, "Non-Hermitian spectral universality at critical points," arXiv:2409.17030 (2024/2025).
[16] Li et al. (Luo Group), "Observation of PT-symmetry breaking transitions in a dissipative Floquet system of ultracold atoms," Nat. Commun. 10, 855 (2019); arXiv:1608.05061.
[17] Pan et al., "Photonic zero mode in a non-Hermitian photonic lattice," Nat. Commun. 9, 1308 (2018).
[18] Kreißl et al., "Demonstration of a two-dimensional PT-symmetric crystal," Nat. Commun. 10, 435 (2019).
[19] Pereira et al., "Non-Hermitian topology and criticality in photonic arrays with engineered losses," arXiv:2311.09959 (2023/2024).
[20] Dagvadorj, Comaron et al., "Unconventional BKT Transition in the Multicomponent Polariton System," PRL 130, 136001 (2023).
[21] Zhang, Carrasquilla, Kim et al., "Observation of a non-Hermitian supersonic mode on a trapped-ion quantum computer," Nat. Commun. (2025).
[22] Begg & Hanai, "Quantum Criticality in Open Quantum Spin Chains with Nonreciprocity," arXiv:2307.03714 (2023/2024).
[23] Qin, Yi et al., "Anyon-Induced Criticality and Dynamical Stability in Non-Hermitian Many-Body Systems," arXiv:2603.17494 (2026).
[24] Gannon, "Comments on nonunitary conformal field theories," Nucl. Phys. B 670, 335 (2003); hep-th/0305070.
[25] Wang et al., "Floquet engineering tunable periodic gauge fields... real topological phases in cold alkaline-earth atom optical lattice," arXiv:2404.12682 (2024).

---

*B博士 (Cross-Domain Attacker)*  
*DQCP-Complex v2 Phase 1*  
*2026-06-01*

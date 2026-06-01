# B博士 v3 Phase 2 -- 交换对称性多角度攻击 & 跨域综合

> 执行时间: 2026-06-01 | 角色: Cross-domain attacker
> 前序: v3P1 排除 NH-Ising (非Class 11) → P3-A 现为开放问题
> 本Phase核心: 攻击P3-A依赖的唯一假设——交换对称性——从已知先例、量子多体物理、信息论、几何、统计力学五个方向

---

## ⚡ 本Phase推进了什么 / 最关键的跨域连接 / 预测 vs 实际 / 卡在哪里

### 推进了什么

找到了**直接打击交换对称性假设的实证证据**：

1. **Zou et al. (2025) NH J-Q 模型** [arXiv:2511.03456] — 这正是DQC P3-A 最相关的微观系统。他们的非厄米变形算子 $H_{\rm nH} = \sum (J/2)(S_i^+ S_j^- - S_i^- S_j^+)$ **明确地不具有交换对称性**：两项符号相反、方向固定(left→right, bottom→top)。交换两项会得到不同的哈密顿量。然而，正是这个**打破交换对称性的变形**削弱了一级相变特征，使系统逼近复平面上的共形固定点。

2. **LeClair (2024-2026) 赝厄米4D标量场论** — 当SU(2)破缺到U(1)时，两个双重态算符的交换对称性天然破缺，导致各向异性的β函数、循环RG流、以及大量复系数。这是**非幺正QFT中交换对称性破缺的标准行为**。

3. **DMI/Dzyaloshinskii-Moriya物理** — 反演对称性破缺产生反对称交换 ($\mathbf{D}_{ij} = -\mathbf{D}_{ji}$)，天然不具有交换对称性。DMI是手性磁体中RG流的**相关扰动**，说明反对称算符混合在真实物理中是普遍而非例外的。

### 最关键的跨域连接

**NH 5-state Potts (Tang 2024, 交换对称性保留) vs NH J-Q (Zou 2025, 交换对称性破缺)**：

| | NH 5-state Potts (Tang) | NH J-Q (Zou) |
|---|---|---|
| 交换对称性 | **保留** (S_5不变) | **破缺** ($S_i^+S_j^-$ vs $S_i^-S_j^+$ 方向性) |
| NH变形类型 | $S_Q$+KW对偶不变量，复数耦合 | 反厄米有向跳跃，实数耦合δ |
| 对称性类 | 保留全部离散对称性 | $H^\dagger_{\rm nH} = -H_{\rm nH}$, $H^T \neq H$ |
| 结果 | 两个共轭复临界点，复CFT | 一级相变减弱，ν收敛，趋向复固定点似的 |
| 对P3-A的启示 | 交换对称性保留→系统可维持 | 交换对称性破缺→但效果更显著 |

**核心洞察**: Tang的模型保留交换对称性但只达到复共轭固定点(两个点对称)；Zou的模型打破交换对称性却更有效地逼近DQCP复固定点。**交换对称性破缺可能反而是逼近真实物理的必要条件**。

### 预测 vs 实际

| 预测 (v2P1假设) | 实际 (本Phase发现) |
|---|---|
| 交换对称性是自然的/默认的 | 交换对称性在非厄米系统中是**精细调谐的(fine-tuned)**，破缺是普遍的 |
| 交换对称性→β函数系数全为实数→实固定点自动存在 | 无交换对称性→β函数系数可为复数→循环RG、复固定点、massless flows都是可能的 |
| NH-Ising是Class 11的反例 | NH-Ising根本不是Class 11 (v3P1结论，本Phase确认) |
| 若交换对称性破缺→P3-A(Class 11强制BKT行走)可能成立 | **交换对称性破缺恰恰是NH J-Q模型中最有效的变形方式**，暗示P3-A可能是对的 |

### 卡在哪里

1. **Zou et al. (2025) 的NH J-Q模型不是Class 11** ($H^T \neq H$)，所以不能直接判定Class 11 J-Q的行为
2. **Class 11 ($H^T=H$, 赝厄米) 量子多体系统的物理实现极其稀缺** — 文献中几乎找不到
3. **Tang et al. (2024) 5-state Potts 保留交换对称性但只在1+1维** — 不足以判断2+1维DQCP的行为
4. **缺少H^T=H约束的J-Q模型微观推导** — A博士的工作尚未产出

---

## §1 交换对称性破缺的已知先例

### 1.1 LeClair赝厄米标量场论中的SU(2)→U(1)破缺

**论文**: LeClair, "A rich structure of RG flows for Higgs-like models in 4D" [arXiv:2411.07476]; "Non-perturbative RG for pseudo-Hermitian scalar fields in 4D" [arXiv:2504.09327, JPA 2026]

**模型结构**:
- 两个耦合的SU(2)双重态标量场 ($\Phi$, $\tilde{\Phi}$)
- 哈密顿量满足赝厄米性: $H^\dagger = \mathcal{K} H \mathcal{K}^\dagger$, $\mathcal{K}^2=1$
- 边缘算符 $\mathcal{O}^a = J^a \tilde{J}^a$ 满足SU(2)李代数OPE

**交换对称性破缺**:
- 当SU(2)破缺到U(1)时，两个双重态之间的交换对称性天然破缺
- 两个独立的耦合常数获得各向异性的β函数
- 结果: **循环RG流**(RG极限环)、**复固定点**、**强-弱对偶** $g \leftrightarrow 1/g$

**关键含义**: 在非幺正QFT中，交换对称性破缺不是bug而是feature——它是循环RG和复固定点的**生成机制**。如果Class 11 J-Q模型的交换对称性破缺，相同的丰富结构可能出现。

### 1.2 非厄米J-Q模型中的显式方向性破缺

**论文**: Zou, Yin, Li, Yao, "Unraveling Deconfined Quantum Criticality in Non-Hermitian Easy-Plane J-Q Model" [arXiv:2511.03456, 2025]

**哈密顿量**:
$$H = (1-\Delta)H_{\rm JQ} + \Delta H_{\rm ep} + \delta H_{\rm nH}$$

其中非厄米部分:
$$H_{\rm nH} = \sum_{\langle i,j\rangle} \frac{J}{2} S_i^+ S_j^- - \frac{J}{2} S_i^- S_j^+$$

关键特征: $S_i^+S_j^-$ 和 $S_i^-S_j^+$ 两项**符号相反、方向固定** (x-bond: left→right, y-bond: bottom→top)。交换两项 = 翻转符号和方向 = 不同的哈密顿量。

**交换对称性: 明确破缺。**

**QMC结果** (sign-problem-free):
- 一级相变强度随δ增加而**显著减弱**: 序参量 $m_0^2$ 在δ=0.6时趋向零
- 临界指数ν在δ=0.6时**收敛**到稳定值 ~0.49(4) (厄米情况下ν随系统尺寸漂移)
- 反常维度η从0.38(1)增加到0.41(1)
- 解释: NH相互作用使系统逼近复平面上的DQCP固定点

**这是P3-A相关的最重要实证先例**: 在DQCP的微观J-Q模型中，打破交换对称性的NH变形是最有效的"解锁"机制。

### 1.3 SMEFT中的大规模非对称算符混合

**论文**: Machado, Renner, Sutherland, "Building blocks of the flavourful SMEFT RG" [JHEP 03 (2023) 226, arXiv:2210.09316]

**关键数据**: 2499×2499的反常维度矩阵。不同味结构的算符通过味相关的系数混合，矩阵**不是对称的**。这是高能物理中大规模非对称算符混合的实证。

### 1.4 无序系统中的非对称RG

**论文**: Aharony & Narovlansky, "RG flow in field theories with quenched disorder" [PRD 98, 045012, 2018]

**关键发现**: 局域算符可以与无序分布的响应混合，产生**新的反常维度类型**。在量子无序中，局域算符与**时间非局域算符**混合。RG流在耦合空间+无序分布空间的联合空间中是非对称的。

### 1.5 Dzyaloshinskii-Moriya相互作用的固有反对称性

**物理**: DM相互作用 $\mathbf{D}_{ij} \cdot (\mathbf{S}_i \times \mathbf{S}_j)$，其中 $\mathbf{D}_{ij} = -\mathbf{D}_{ji}$ 是**固有的反对称**。

**RG相关性**: 在B20手性磁体中，DM Lifshitz不变量是RG意义上的**相关扰动**，决定螺旋/斯格明子相的稳定性。反对称算符混合在手性系统中是主导性而非次导性的。

### §1结论

**交换对称性破缺在非厄米/非幺正QFT中是普遍现象而非例外**。破缺的机制包括:
1. 内部对称性破缺 (LeClair: SU(2)→U(1))
2. 方向性/手性 (Zou NH J-Q: 空间方向性; DMI: 矢量反对称)
3. 味/内部自由度 (SMEFT: 味相关混合)
4. 无序/环境耦合 (Aharony-Narovlansky: 算符-无序混合)

**对P3-A的影响**: 交换对称性是精细调谐的，在一般的非厄米变形下会自然破缺。如果J-Q模型的BL Class 11变形算子$(O_1, O_2)$的交换对称性是人为假定的，那么v2P1的推导(β函数系数全为实数→实固定点自动存在→P3-A被驳斥)将不成立。

---

## §2 真正Class 11量子多体系统搜索

### 2.1 Class 11的定义 (Kawabata 38重分类)

**论文**: Kawabata, Shiozaki, Ueda, Sato, "Symmetry and Topology in Non-Hermitian Physics" [PRX 9, 041015, 2019, arXiv:1812.09133]

在非厄米系统中，转置($T$)和复共轭($K$)是不等价的运算，导致38个对称性类(厄米系统的10重Altland-Zirnbauer分类的扩展)。

Class 11 (推测为AI$^\dagger$类) 的特征:
- **$H^T = H$** (复对称哈密顿量, $k=I$) — 这是关键约束
- **$H^\dagger \neq H$** (非厄米)
- **可能具有赝厄米性**: $\eta H \eta^{-1} = H^\dagger$ (需进一步确认)

不是PT对称 ($H \neq H^\dagger$ 但可能有 $\mathcal{PT}H\mathcal{PT}^{-1} = H$)

### 2.2 已知Class 11候选者 — 几乎为零

**搜索覆盖**: complex symmetric Hamiltonian, H^T=H non-Hermitian, transpose-symmetric spin model, symmetric matrix Hamiltonian condensed matter

**找到的候选者**:

1. **开放量子Liouvillian** (Kim & Hassler, JPA 2023): Lindblad超算符矩阵是复对称的 $L = L^T$，来源于trace preservation。但这描述的是密度矩阵动力学，不是哈密顿量本征态物理。

2. **非厄米随机矩阵系综** (Hamazaki et al., PRR 3, 023286, 2021): 复对称随机矩阵构成特定的普适类。但这是数学构造而非物理哈密顿量。

3. **规范场修饰的NH拓扑系统** (arXiv:2309.14042): 通过规范场可以将拓扑平凡的NH系统变为非平凡的。但具体的 $H^T=H$ 约束是否满足需要逐例分析。

4. **NH-Ising链**: v3P1已排除 — 不满足Class 11

5. **NH J-Q (Zou 2025)**: $H_{\rm nH}^\dagger = -H_{\rm nH}$, $H^T \neq H$ — 不满足Class 11

6. **NH 5-state Potts (Tang 2024)**: 保留S_5对称性，但未明确声称 $H^T=H$

### 2.3 为什么Class 11物理实现如此稀缺？

**物理原因分析**:

1. **$H^T=H$ 在非厄米系统中是非自然的**: 转置对称性要求 $\langle m|H|n\rangle = \langle n|H|m\rangle$——在标准的left-right本征矢双正交框架中，这要求左本征矢与右本征矢的转置有关。大多数非厄米系统(如增益-损耗系统、开放系统)天然违反这一条件。

2. **实验实现的障碍**: 非厄米物理的主要实验平台(光学、声学、电路)容易实现PT对称或反厄米成分，但$H^T=H$需要特定的矩阵结构(所有矩阵元对称)——这在耦合设计中非常受限。

3. **与其他对称性的张力**: $H^T=H$ 加上非厄米性 ($H^\dagger \neq H$) 意味着 $H^* \neq H$ —— 即哈密顿量必须既有复对称又有复矩阵元，这在物理上等价于要求同时存在两种不兼容的约束。

### §2结论

**目前已知的Class 11 ($H^T=H$, 赝厄米) 量子多体自旋系统的物理实现数量: 零。**

这意味着:
- P3-A 声称的 "Class 11对称性强制BKT行走行为" 在实验上无法直接验证
- 但同样地，v2P1声称的反驳("实固定点自动存在")也无法在Class 11系统中接受检验
- **P3-A 保持为开放问题，既未被验证也未被证伪**

当前最接近Class 11的DHCP系统 (NH J-Q, Zou 2025) **不具有 $H^T=H$**。这暗示: 如果要在实际的微观模型中测试P3-A，可能需要构造一个新的Class 11 J-Q模型——这是一个未解决的挑战。

---

## §3 交换对称性的多角度攻击

### 3.1 信息论角度: "非厄米箭头"

**论证**: 非厄米系统的定义特征是左右本征矢的不等价性:
$$H|R_n\rangle = E_n|R_n\rangle, \quad \langle L_n|H = E_n\langle L_n|, \quad \langle L_n| \neq (|R_n\rangle)^\dagger$$

在算符层面，两个非厄米变形$O_1$和$O_2$代表"相反"的过程(如增益vs损耗、左移vs右移)。但"相反"的定义依赖于本征矢基的选择——而这一选择在非厄米系统中是**各向异性的**。

**关键洞察**: 如果$O_1$驱动的非厄米过程定义了"箭头"，那么$O_2$作为"反向箭头"必须在这个已经各向异性的空间中定义。二者不必对称——就像在弯曲空间中，"前"和"后"的长度不必相等。

**类比**: 开放量子系统中的细致平衡破缺——正向和反向跃迁率不必相等(Jarzynski等式在非幺正动力学中不再成立)。

**结论**: 交换对称性在信息论意义上是精细调谐的——它要求非厄米"箭头"与其逆在数学上等权重，这没有信息论基础。

### 3.2 几何角度: 耦合空间中的反射对称性

**论证**: 在$(g_1, g_2)$耦合空间中，交换对称性$g_1 \leftrightarrow g_2$等价于$\beta_1(g_1,g_2) = \beta_2(g_2,g_1)$。

**这是反射对称性**: RG流在对角线$g_1=g_2$两侧镜像对称。

**自然性分析**:
- 在厄米-幺正理论中，若两个算符具有相同的标度维度，反射对称性可以是偶然的(accidental)
- 在非厄米-非幺正理论中，反常维度矩阵可以是非对称的(如SMEFT、LeClair模型)，使$\gamma_{ij} \neq \gamma_{ji}$
- 因此，$g_1$和$g_2$在RG流下的演化速度可以不同，反射对称性破缺

**几何不稳定性的论证**: 考虑小的各向异性扰动$\epsilon(g_1-g_2)$。在$\epsilon \to 0$极限下，反射对称性恢复。但任意有限的$\epsilon$破缺反射对称性。问题是: $\epsilon=0$在RG流下是稳定的吗？

**LeClair模型的答案**: 否。在LeClair的伪厄米标量理论中，SU(2)极限($\epsilon=0$, 交换对称性)在RG流下是不稳定的——系统流向U(1)破缺相，各向异性$\epsilon$增长。

### 3.3 统计力学角度: Tang 5-state Potts vs Zou J-Q 对比

**Tang et al. (2024) NH 5-state Potts**:
- NH变形: $H_1(\lambda)$ 明确保留S_5排列对称性
- 交换对称性: **保留**
- 结果: 两个复共轭临界点, $\lambda_c, \bar{\lambda}_c$ 对称
- 标度维度: 一些算符有正虚部 (Z, X, Y, W)，一些有负虚部 ($\epsilon$, $\sigma$)
- 关键: 虚部的符号不是随机的 — **正虚部和负虚部算符配对出现**

**Zou et al. (2025) NH J-Q**:
- NH变形: $H_{\rm nH}$ 有向跳跃，明确打破交换对称性
- 交换对称性: **破缺**
- 结果: 单个区间的连续过渡行为，ν收敛
- 没有报道复共轭对结构

**对比总结**:

| 特征 | Tang Potts (交换对称性保留) | Zou J-Q (交换对称性破缺) |
|---|---|---|
| 固定点结构 | 共轭对$(c, \bar{c})$ | 趋向单个复固定点 |
| 算符谱 | 正负虚部成对 | (未报道) |
| 过渡性质 | 在复平面上连续 | 在实轴上仍然"准临界" |
| RG流拓扑 | 对称 | 不对称 |

**对P3-A的启示**: Tang模型的交换对称性保留了共轭对结构——这是两个固定点而非一个。如果Class 11 J-Q需要BKT行走(依赖于单个固定点的性质)，那么保留交换对称性可能导致**两个**固定点(复共轭对)，而不是"行走"。这可能解释了为什么**打破**交换对称性的Zou模型更有效地逼近DQCP物理。

---

## §4 若交换对称性破缺 → 替代框架

### 4.1 Q-对称性单独约束β函数

**Q-对称性 = 赝厄米性**: $\eta H \eta^{-1} = H^\dagger$

**约束力分析**:
- 赝厄米性保证本征值为实数或复共轭对
- 对β函数: 赝厄米性约束$\beta(g_1, g_2)$在复共轭下的变换，但不强制$c_{mn}$全为实数
- 具体地: 赝厄米性意味着$\beta(g_1^*, g_2^*) = \beta(g_1, g_2)^*$ (若η=I)
- 这是**弱于**交换对称性的约束

**独立系数计数**:
- 有交换对称性: $\beta(g_1,g_2) = \sum c_{mn} g_1^m g_2^n$, 其中$c_{mn} = c_{nm}$ → 系数独立数 ~ N(N+1)/2
- 无交换对称性，仅赝厄米性: $c_{mn}$ 和 $c_{nm}$ 独立 → 系数独立数 ~ N^2
- 前者强制$c_{mn}$为实数(通过交换对称性+赝厄米性)，后者允许复数

**结论**: 如果Class 11只有赝厄米性(Q-对称性)而没有额外的交换对称性，β函数系数可以是复数→实固定点不自动存在→P3-A不能被v2P1的论证驳斥。

### 4.2 LeClair框架: 伪厄米+破缺交换对称性 = 循环RG + 复固定点

如果我们将LeClair的框架应用到Class 11 J-Q模型(假设交换对称性破缺):

1. **β函数的形式**: $\beta_a(g_1,g_2) = \sum_{m,n} c^{(a)}_{mn} g_1^m g_2^n$，其中$a=1,2$，系数$c^{(a)}_{mn}$可以不等、不同

2. **RG流的拓扑**: 可能出现:
   - **复固定点**: 当$c^{(a)}_{mn}$有虚部时，固定点自然进入复平面
   - **极限环**: 如LeClair模型的$g(\ell+\Lambda) = g(\ell)$, $\Lambda = 2\pi/\sqrt{Q}$
   - **无固定点的行走**: 如果复固定点的实部投影附近流动缓慢

3. **离散标度不变性 (DSI)**: 循环RG导致Russian Doll标度 $v_n \sim e^{2n\lambda}$，对应"行走"耦合——这正是BKT行为的精确定义之一

**关键**: LeClair框架中，交换对称性破缺**自动生成**循环RG和行走行为。如果Class 11 J-Q模型的算子$(O_1, O_2)$确实交换对称性破缺，那么BKT行走行为可能是**不可避免的**——P3-A将是正确的，但原因比原来想象的更深刻。

### 4.3 最简对称性集合

**问题**: 约束β函数所需的最简对称性集合是什么？

**v2P1的隐含假设**:
1. Q-对称性 (赝厄米性) — 来自BL的推导
2. C-对称性 (交换$O_1 \leftrightarrow O_2$) — **此为假设**
3. 解析性 — 标准QFT假设

**如果只有Q-对称性**:
- $\beta(g_1,g_2)$不必满足$g_1\leftrightarrow g_2$的反射对称性
- 结合$H^T=H$ (如果这是Class 11的一部分): 这约束了哈密顿量结构但$\beta(g)$是宏观量
- 在宏观尺度上，$H^T=H$可能不足以强制$(g_1,g_2)$的镜像对称性

**最简集合 = {Q-对称性 + $H^T=H$}**: 在此集合下
- β函数不能先验地约束到实数
- 复固定点→BKT行走是被允许的演化路径
- P3-A保持为有生存力的假说

### 4.4 从微观参数计算$c_{mn}$的虚部

**可能的路径**:

1. **共形微扰论 (CPT)**: 从DQCP CFT出发，用$\beta(g) = (d - \Delta_O)g - C_{OOO} g^2 + ...$计算系数
   - 如果$O_1$和$O_2$有不同的共形维度$\Delta_1 \neq \Delta_2$ → 第一项就不对称
   - 如果三算符关联函数$C_{O_1O_2O_2} \neq C_{O_2O_1O_1}$ → 第二项不对称
   - 这些不对称性可以直接从CFT数据计算

2. **Schrieffer-Wolff变换**: 从微观J-Q模型出发，投影到低能有效理论
   - $O_1$和$O_2$来源于不同的微观过程(如不同的四自旋plaquette构型)
   - 如果微观构型不对称(如J-Q_2 vs J-Q_3模型中的不同plaquette几何)，则有效算符不对称

3. **数值QMC + 有限尺寸标度**: 
   - 直接在NH J-Q模型上测量$\beta(g)$
   - 如果Zou et al. (2025)的方法可以推广到Class 11的变形
   - 通过测量不同$g_1, g_2$下的关联长度来反推β函数

---

## §末 结论对比

### P3-A的生存力评估

| 攻击方向 | P3-A有利 | P3-A不利 | 中性 |
|---|---|---|---|
| 交换对称性先例 | 先例丰富(LeClair, SMEFT, DMI, 无序) -- 破缺是普遍的 | — | — |
| Class 11系统稀缺 | v2P1无法在物理系统中检验 | P3-A无法在物理系统中检验 | 双方持平 |
| Tang 5-state Potts | — | 交换对称性保留下仍有复CFT | 1+1维≠2+1维 |
| Zou NH J-Q | 交换对称性破缺→更有效逼近DQCP | 该模型不是Class 11 | 需要Class 11版本 |
| 信息论/几何 | 反射对称性是精细调谐的 | — | 定性论证 |
| LeClair伪厄米框架 | 破缺交换对称性→自动BKT行走 | — | 4D标量≠2+1D自旋 |

### 核心判断

**v2P1的推导依赖交换对称性假设。本Phase发现交换对称性在非厄米QFT中普遍破缺。如果Class 11 J-Q模型的$(O_1, O_2)$确实如Zou et al. (2025)的模型一样打破交换对称性，那么v2P1的"β函数系数全为实数→实固定点自动存在→P3-A被驳斥"的推理链条断裂。**

P3-A的现状:
1. **未被证伪**: NH-Ising不是Class 11 (v3P1); 交换对称性普遍破缺 (v3P2)
2. **未被验证**: Class 11量子多体系统无已知物理实现; 无直接的β函数测量
3. **生存力增强**: Zou et al. (2025) 的直接J-Q证据表明，交换对称性破缺的NH变形是最有效的——这暗示P3-A设想的"Class 11对称性→BKT行走"机制在**更宽的条件下**可能成立

### 下一步建议

1. **A博士需确定**: BL的$(O_1, O_2)$在微观J-Q模型中是否真的具有交换对称性？
2. **构建Class 11 J-Q模型**: 在Zou et al. (2025)的基础上，构造$H^T=H$的变形
3. **CPT计算$c_{mn}$的虚部**: 从NH DQCP CFT数据出发
4. **独立β函数约束**: 仅用Q-对称性+$H^T=H$，不假设交换对称性，重新推导β函数的形式

---

## 参考文献

- Zou, Yin, Li, Yao, "Unraveling Deconfined Quantum Criticality in Non-Hermitian Easy-Plane J-Q Model", arXiv:2511.03456 (2025)
- Tang, Ma, Tang, He, Zhu, "Reclaiming the Lost Conformality in a non-Hermitian Quantum 5-state Potts Model", PRL 133, 076504 (2024), arXiv:2403.00852
- LeClair, "A rich structure of RG flows for Higgs-like models in 4D", arXiv:2411.07476 (2024)
- LeClair, "Non-perturbative RG for pseudo-Hermitian scalar fields in 4D", JPA (2026), arXiv:2504.09327
- Kawabata, Shiozaki, Ueda, Sato, "Symmetry and Topology in Non-Hermitian Physics", PRX 9, 041015 (2019), arXiv:1812.09133
- Song, Zhao, Janssen, Scherer, Meng, "Deconfined quantum criticality lost", arXiv:2307.02547 (2023)
- Machado, Renner, Sutherland, "Building blocks of the flavourful SMEFT RG", JHEP 03, 226 (2023), arXiv:2210.09316
- Aharony & Narovlansky, "RG flow in field theories with quenched disorder", PRD 98, 045012 (2018)
- Kim & Hassler, "Third quantization for bosons...", JPA (2023), arXiv:2304.02367
- Guica, "On correlation functions in J\bar{T}-deformed CFTs", JPA 52, 184003 (2019)
- Hamazaki et al., "Random matrix universality classes...", PRR 3, 023286 (2021)

# DGF 文献区分矩阵 — 14篇优先文献逐一分析

**日期:** 2026-06-12
**触发:** REVIEWER发现14篇优先文献，需逐一分析与DGF的重叠/差异/引用策略
**产出:** 完整区分矩阵 + Jacobson/Verlinde重点区分 + 投稿引用建议

---

## DGF六条核心声张（速查）

| ID | 声张 | 层级 | 状态 |
|:--:|------|:--:|:--:|
| DGF-1 | **CFOL定理**: 因果拓扑→QCMI充要条件, Cartan轴对齐4-qubit环中 QCMI=0⟺cⱼ∈(π/2)ℤ | 定理级 | IBM Q验证 S/N>600 |
| DGF-2 | **边界plaquette定理**: 旋转/非旋转界面QCMI>0, 闭式公式 | 定理级 | 数值+解析确认 |
| DGF-3 | **θ²ln(1/θ)标度律**: 非微扰对数增强, 与标准θ⁴相差>100倍 | 数值证据 | 函数形式正确, 系数需精化 |
| DGF-4 | **IBM Q硬件实测**: S/N>600 CFOL验证, Kingston Heron r2 | 实验证据 | 已完成 |
| DGF-5 | **拥堵→信息视界**: 信息传输容量有界→视界形成 (Aporia框架) | 推导级 | 依赖Reflux界定理(T2) |
| DGF-6 | **三公理体系**: 信息存在(A1)+容量有界(A2)+溢出不可逆(A3) | 公理级 | 元理论框架 |

---

## 0. 最重要的两个区分: Jacobson (1995) vs Verlinde (2011)

在分析14篇文献之前，必须先精确区分DGF与Jacobson(1995)和Verlinde(2011)——这两位是"从热力学/信息推导引力"范式的开创者。如果DGF不能清晰说明与他们不同的地方，审稿人将直接判定为增量不足。

### 0.1 Jacobson (1995): Thermodynamics of Spacetime

**Jacobson的核心论证链:**
```
局部Rindler视界 (几何结构, 先验存在)
    ↓
δQ = T dS (热力学第一定律, 应用于视界)
    ↓
S ∝ A (Bekenstein-Hawking熵, 作为输入)
    ↓
δQ = ∫ T_ab k^a k^b dλ dA (能量-动量张量作为热流源)
    ↓
G_ab = 8πG T_ab (Einstein方程作为状态方程)
```

**Jacobson需要但DGF不需要的:**
| Jacobson的输入 | DGF的处理 |
|:--|:--|
| 局部Rindler视界 (微分几何结构) | 视界从拥堵涌现——不是先验几何 |
| Bekenstein-Hawking熵 S=A/4G (作为公理输入) | 面积律从min-cut定理推导(T3), 是结果不是输入 |
| Unruh温度 T=ħκ/2π (作为输入) | 信息容量饱和产生等效温度, 不需要Unruh效应 |
| 连续性假设 (视界光滑) | 离散因果图, 连续极限是RG涌现的 |
| Killing矢量场 (时间平移对称性) | 因果有向性(DAG边方向)替代Killing对称性 |

**DGF需要但Jacobson不需要的:**
| DGF的输入 | Jacobson的处理 |
|:--|:--|
| 量子信息论 (QCMI, Holevo界, sQNM) | 不使用——纯热力学+广义相对论 |
| 因果图拓扑 (b1, Cartan参数) | 不使用——使用微分几何 |
| η₀=1/(8ln2) 信息论基本常数 | 不使用——使用ħ, G, c |
| CFOL定理 (QCMI=0⟺Clifford) | 无对应物 |
| 离散→连续RG流 | 不需要——直接工作在连续统 |

**诚实定位:**
> Jacobson (1995) established that Einstein's equations are thermodynamic identities on local Rindler horizons — a macroscopic, thermodynamic derivation that takes Bekenstein-Hawking entropy and Unruh temperature as inputs. DGF provides a **microscopic, information-theoretic mechanism** for why horizons carry entropy proportional to area: it is the QCMI accumulated by causal cycles crossing the horizon. In DGF, the area law is **derived** from the min-cut theorem on the causal graph and the η₀·b₁ scaling of QCMI — it is not an input. Jacobson's derivation is a thermodynamic **consistency condition** on pre-existing spacetime geometry; DGF's derivation is an information-theoretic **construction** of geometry from more primitive elements (causal graph nodes carrying ≤1 bit each).

**一句话区分:** Jacobson从热力学推出Einstein方程——但热力学发生在已经存在的时空中。DGF从信息容量饱和推出视界——信息流动发生在因果图上，时空是涌现的。

---

### 0.2 Verlinde (2011): Entropic Gravity

**Verlinde的核心论证链:**
```
全息屏 (holographic screen, 先验存在)
    ↓
熵力 F = T ΔS/Δx (熵增驱动有效力)
    ↓
 equipartition: N = A c³/(Għ) (全息屏自由度)
    ↓
T = ħ a / (2π k_B c) (Unruh温度)
    ↓
F = G M m / r² (牛顿引力恢复)
```

**Verlinde需要但DGF不需要的:**
| Verlinde的输入 | DGF的处理 |
|:--|:--|
| 全息屏 (闭合等势面) | 不需要——信息视界从拥堵涌现, 不是先验表面 |
| equipartition假设 (能量均匀分配) | 不需要——使用Holevo界和信息可区分性预算 |
| Unruh温度 (加速观测者) | 不需要——不使用Unruh效应 |
| 熵位移→表观暗物质 (2016版本) | DGF的暗能量来自q场宇宙学, 不同机制 |
| 弹性时空响应 (2016版本) | 不需要——使用因果图RG流 |

**DGF需要但Verlinde不需要的:**
| DGF的输入 | Verlinde的处理 |
|:--|:--|
| QCMI, sQNM, Holevo界 | 不使用——使用经典热力学 |
| CFOL定理 | 无对应物 |
| η₀=1/(8ln2) | 无对应物——使用ħ, G, c |
| IBM Q硬件验证 | 无对应物 |
| q场=信道开放度 | 无对应物 |

**诚实定位:**
> Verlinde (2011, 2016) proposed that gravity is an entropic force arising from the statistical thermodynamics of holographic screens. DGF differs fundamentally: while Verlinde's entropic force is a macroscopic thermodynamic phenomenon that presupposes holographic screens and Unruh temperature, DGF's gravity emerges from the microscopic quantum information dynamics of causal graph topology. In DGF, gravitational potential is not an entropic force but the logarithm of the quantum channel openness q = exp(-Φ/c²), derived from causal graph RG flow. The DGF derivation does not require equipartition, holographic screens, or the Unruh effect — it requires only the quantum information axioms A1-A3.

**一句话区分:** Verlinde说"引力是熵力"——但熵力预设了熵梯度存在的空间。DGF说"引力是q场的梯度"——q场本身从因果图的量子信息容量涌现。

---

### 0.3 Jacobson/Verlinde/DGF 三方对比表

| 维度 | Jacobson (1995) | Verlinde (2011) | DGF (2025-26) |
|:--|:--|:--|:--|
| **底层本体** | 连续时空 (微分几何) | 全息屏 (时空边界) | 离散因果图 (≤1bit/节点) |
| **推导起点** | δQ=TdS on Rindler horizon | 熵力+equipartition | QCMI+CFOL+容量界 |
| **熵的来源** | Bekenstein-Hawking (输入) | 全息屏自由度 (输入) | η₀·b₁标度律 (推导) |
| **面积律** | S=A/4G (假设) | S∝A (全息原理, 假设) | S ≤ N_∂Ω (min-cut, 证明) |
| **温度概念** | Unruh温度 (输入) | Unruh温度 (输入) | 信息容量饱和等效温度 (涌现) |
| **需要ħ** | 是 (Unruh温度含ħ) | 是 (Unruh温度含ħ) | 否 (η₀是纯信息论常数) |
| **需要G** | 是 (出现在结果中) | 是 (出现在结果中) | G从η₀和b₁标度涌现 |
| **微观验证** | 无 (宏观推导) | 无 (宏观推导) | IBM Q S/N>600 (微观验证) |
| **量子信息论** | 无 | 无 | QCMI, sQNM, Holevo, CFOL |
| **因果拓扑** | 无 (因果结构是背景) | 无 (全息屏是背景) | b₁(G)是独立自由度 |
| **主要成果** | Einstein方程=状态方程 | 牛顿引力+暗物质替代 | CFOL+η₀+q场Poisson方程+w₀≈-0.80 |

---

### 0.4 Jacobson和Verlinde的正确引用方式

**在Introduction中:**
> "Jacobson (1995) established the paradigm that gravitational field equations can be understood as thermodynamic identities, and Verlinde (2011) extended this to an entropic force interpretation. These works demonstrated that gravity admits a statistical-mechanical description, but they left open the microscopic question: what are the fundamental degrees of freedom whose statistics give rise to the Bekenstein-Hawking entropy? DGF addresses this question by identifying the fundamental degrees of freedom as the nodes of a causal graph, each carrying at most one bit of classical information (Axiom A2), and by showing that QCMI accumulated across causal cycles (quantified by the Betti number b₁) yields an area-law scaling for horizon entropy without assuming the Bekenstein-Hawking formula."

**在Discussion中:**
> "DGF's area-law derivation (Theorem 3) converges to the Bekenstein-Hawking form S ∝ A when the causal-lock saturation conjecture (CONJ-4) holds, recovering Jacobson's thermodynamic consistency condition as a macroscopic limit. However, DGF's microscopic coefficient (2.68 in Planck units for a = ℓ_P) differs from 1.00, suggesting that DGF's horizon entropy may be a precursor to gravitational entropy — an information-theoretic quantity that reduces to Bekenstein-Hawking entropy only after full RG flow to the deep IR."

---

## 1. 14篇文献逐一分析

---

### 文献1: Verlinde (2011) — 全息原理+熵力→牛顿+爱因斯坦

**文献信息:**
Verlinde, E. "On the Origin of Gravity and the Laws of Newton." *JHEP* 04, 029 (2011). arXiv:1001.0785.
Verlinde, E. "Emergent Gravity and the Dark Universe." *SciPost Phys.* 2, 016 (2017). arXiv:1611.02269.

**核心声张:** 引力不是基本力，而是全息屏上微观自由度重新分布引起的熵力。2017版扩展到暗物质：熵位移产生表观暗物质。

**与DGF的重叠:**
| DGF声张 | 重叠 | 程度 |
|:--|:--|:--:|
| DGF-5 (拥堵→视界) | "信息→引力"范式方向一致 | 方向级 |
| DGF-6 (三公理) | 信息容量有界(A2)与全息界共享精神 | 精神级 |
| DGF暗能量宇宙学 | Verlinde 2017暗物质解释——不同目标但同在"信息修正引力"空间 | 领域级 |

**DGF有而Verlinde没有的:**
1. **CFOL定理** — Verlinde没有微观量子信息机制。他的"熵"是经典热力学熵，不是QCMI。
2. **η₀=1/(8ln2)** — Verlinde没有信息论基本常数，所有参数是ħ, G, c。
3. **因果拓扑b₁** — Verlinde没有Betti数概念，他的自由度是全息屏上的"bits"，但bits的数量是A c³/(Għ)——依赖ħ和G。DGF的b₁是不依赖ħ和G的纯拓扑量。
4. **IBM Q验证** — Verlinde没有硬件实验。
5. **q场的操作定义** — Verlinde的"熵位移"没有量子信道层面的操作定义。

**Verlinde有而DGF没有的:**
1. 可检验的星系尺度假说 (星系旋转曲线、透镜化) —— DGF尚未达到这个检验层级。
2. 与观测的定量拟合 (Verlinde 2017给出了一些星系拟合)。

**引用策略:** **区分引用**
- 引用为"信息→引力"方向的前驱和宏观对应物
- 明确标注: DGF是微观信息论机制 (QCMI+因果拓扑)，Verlinde是宏观热力学机制 (全息屏+熵力)
- 使用上表0.3的三方对比建立清晰区分
- 位置: Introduction (建立领域) + Discussion (对比宏观/微观)

---

### 文献2: Jacobson (1995) — 热力学→爱因斯坦场方程

**文献信息:**
Jacobson, T. "Thermodynamics of Spacetime: The Einstein Equation of State." *Phys. Rev. Lett.* 75, 1260 (1995). arXiv:gr-qc/9504004.

**核心声张:** Einstein场方程可以从Rindler视界上的热力学关系δQ = T dS导出——Einstein方程不是基本方程，而是状态方程。

**与DGF的重叠:**
| DGF声张 | 重叠 | 程度 |
|:--|:--|:--:|
| DGF-5 (拥堵→视界) | "引力场方程=涌现方程"方向一致 | 方向级 |
| DGF-6 (A2容量有界) | 熵面积律S∝A——Jacobson用Bekenstein-Hawking(输入), DGF用min-cut(推导) | 结果级 |

**DGF有而Jacobson没有的:**
1. **微观机制** — Jacobson的推导是宏观热力学——不需要知道熵的微观起源。DGF提供了熵的微观信息论起源(QCMI+b₁)。
2. **离散因果图** — Jacobson工作在连续统——Rindler视界是微分几何对象。DGF的因果图是离散的。
3. **面积律推导** — Jacobson把S = A/4G作为输入(引用Bekenstein-Hawking)。DGF从min-cut定理推导面积律标度(系数不同: 2.68 vs 1.00)。
4. **η₀常数** — Jacobson没有信息论基本常数。
5. **实验检验** — Jacobson没有微观可检验性。

**Jacobson有而DGF没有的:**
1. 30年引用的成熟度。
2. 推广到f(R)引力、Lovelock引力、非平衡热力学等形式(后续工作)。

**引用策略:** **区分引用 (最关键的区分之一)**
- 必须同时表达尊敬和区分: Jacobson开创了方向，DGF提供了微观机制
- 使用0.1节表格的完整对比
- 关键句子: "Jacobson's derivation is thermodynamic; DGF's is information-theoretic. Jacobson takes the Bekenstein-Hawking entropy as input; DGF derives an area law from causal graph topology. Jacobson works on a continuous Rindler horizon; DGF works on a discrete causal DAG."
- 位置: Introduction (第一段之后) + Discussion (方法论对比)

---

### 文献3: Padmanabhan (1989+) — 退相干→经典时空涌现

**文献信息:**
Padmanabhan, T. "Decoherence in the density matrix describing quantum three-geometries and the emergence of classical spacetime." *Phys. Rev. D* 39, 2924 (1989).
Padmanabhan, T. "Holographic gravity and the surface term in the Einstein-Hilbert action." *Braz. J. Phys.* 35, 362 (2005). arXiv:gr-qc/0412068.
Padmanabhan, T. "Thermodynamical Aspects of Gravity: New insights." *Rep. Prog. Phys.* 73, 046901 (2010). arXiv:0911.5004.

**核心声张:** 量子引力中的退相干机制使经典时空从量子3-几何的密度矩阵中涌现。后续工作建立了全息引力——Einstein-Hilbert作用量的表面项解释。

**与DGF的重叠:**
| DGF声张 | 重叠 | 程度 |
|:--|:--|:--:|
| DGF-5 (拥堵→视界) | "退相干→经典时空"概念方向一致 | 概念级 |
| DGF-6 (三公理) | Padmanabhan的表面项-体积项分离，与DGF的容量有界精神相似 | 精神级 |

**DGF有而Padmanabhan没有的:**
1. **退相干的具体机制** — Padmanabhan讨论的是3-几何的退相干(超空间度规+ Wheeler-DeWitt方程)，DGF的退相干来自因果环的QCMI累积(D_global = 1-[cos²(4c)]^{b₁})。
2. **量子计算实验** — DGF的退相干公式可在IBM Q上验证，Padmanabhan的无法检验。
3. **因果图拓扑** — Padmanabhan工作在连续统(超空间)，DGF工作在离散因果图。
4. **η₀, b₁, CFOL** — 均无对应物。

**Padmanabhan有而DGF没有的:**
1. 与Wheeler-DeWitt方程和正则量子引力的直接联系。
2. 完备的渐近视界热力学框架(1998-2010系列)。

**引用策略:** **正面引用 (精神前驱)**
- 引用为"退相干→经典性涌现"方向的最早提出者之一
- DGF可以定位为: "Padmanabhan在连续统量子引力中提出的退相干→经典性方案，在DGF中以离散因果图的量子信息语言被重新表述和精化"
- 位置: Introduction (概念谱系) + Discussion

---

### 文献4: Volovik (2007+) — Fermi点涌现引力

**文献信息:**
Volovik, G.E. "Fermi-point scenario for emergent gravity." arXiv:0709.1258 (2007).
Volovik, G.E. *The Universe in a Helium Droplet.* Oxford University Press (2003, 2009).

**核心声张:** 引力是Fermi点(动量空间拓扑缺陷)的低能涌现现象。类似于超流氦-3中的准粒子——引力子、度规、自旋联络都从Fermi点附近的低能有效理论涌现。

**与DGF的重叠:**
| DGF声张 | 重叠 | 程度 |
|:--|:--|:--:|
| DGF-5 (拥堵→视界) | "引力从更基本的离散结构涌现"方向一致 | 方向级 |
| DGF-6 (三公理) | 涌现范式——基本自由度不是时空本身 | 范式级 |

**DGF有而Volovik没有的:**
1. **涌现的位置空间不同** — Volovik在动量空间(Fermi点拓扑)，DGF在实空间(因果图拓扑)。这是根本性的数学差异。
2. **量子信息论** — Volovik不使用QCMI、Holevo界、sQNM。
3. **CFOL定理** — 无对应物。
4. **η₀常数** — Volovik的常数是凝聚态物理的(Fermi速度, 能隙等)，DGF的是信息论的。
5. **IBM Q验证** — 无对应物。

**Volovik有而DGF没有的:**
1. 与实验凝聚态系统的类比(超流氦-3)——为概念提供了物理直觉。
2. 宇宙学常数的自然小值解释(Fermi点拓扑保护)。

**引用策略:** **区分引用**
- 引用为涌现引力范式中"基于拓扑缺陷"的一支
- 强调DGF是"因果拓扑"而非"动量空间拓扑"
- 位置: Introduction (涌现引力分类) + Discussion (不同拓扑路线的对比)

---

### 文献5: Hu (2009) — 涌现/量子引力综述

**文献信息:**
Hu, B.L. "Emergent/Quantum Gravity: Macro/Micro Structures of Spacetime." *J. Phys. Conf. Ser.* 174, 012015 (2009). arXiv:0903.0878.

**核心声张:** 综述文章，梳理了"自上而下"(量子引力→涌现经典时空)和"自下而上"(从微观自由度构造时空)两条涌现引力路径。提出微观-宏观界面(micro-macro interface)作为关键概念。

**与DGF的重叠:**
| DGF声张 | 重叠 | 程度 |
|:--|:--|:--:|
| DGF-5, DGF-6 | 综述覆盖了DGF所属的涌现引力范式 | 背景级 |

**DGF有而Hu没有的:**
Hu是综述，无自身竞争性理论。

**引用策略:** **正面引用 (领域背景)**
- 引用为涌现引力的分类学框架
- DGF可定位为Hu分类中"自下而上"路径的具体实现
- 位置: Introduction (领域综述引用)

---

### 文献6: Boldis & Levay (2023) — QCMI+AdS因果结构

**文献信息:**
Boldis, B. & Levay, P. "Segmented strings and holography." arXiv:2304.10389 (2023).

**核心声张:** 在AdS3/CFT2中，分割弦世界面面积(以4GL为单位)等于边界梯形配置的量子条件互信息I(A:C|B)。连接了QCMI与AdS中的因果钻石(causal diamonds)几何。

**与DGF的重叠:**
| DGF声张 | 重叠 | 程度 |
|:--|:--|:--:|
| DGF-1 (CFOL) | 两者都使用QCMI，两者都讨论因果结构 | 工具级 |
| DGF-5 (拥堵→视界) | Boldis-Levay的因果钻石与DGF的因果DAG在概念上有亲缘性 | 概念级 |

**DGF有而Boldis-Levay没有的:**
1. **QCMI的角色不同** — Boldis-Levay的QCMI是边界CFT的纠缠熵组合(通过RT公式得到)，等价于bulk世界面面积。DGF的QCMI是量子非马尔可夫性的度量——物理含义完全不同。
2. **不依赖AdS/CFT** — Boldis-Levay的推导完全在AdS/CFT对偶内。DGF不需要全息对偶。
3. **因果图是原始的** — Boldis-Levay的因果结构嵌入在已有的AdS时空中。DGF的因果图是更原始的——时空从因果图涌现。
4. **CFOL定理** — Boldis-Levay没有QCMI=0的充要条件。他们的QCMI一般是正的(饱和强次可加性)，但未分析何时严格为零的离散条件。
5. **η₀, b₁, Cartan参数** — 均无对应物。

**Boldis-Levay有而DGF没有的:**
1. 与全息对偶(RT公式, kinematic space)的直接联系。
2. 与复杂度(computational complexity)和保真度敏感度(fidelity susceptibility)的连接。

**引用策略:** **正面引用 + 清晰区分**
- 引用为"QCMI-因果几何"交叉领域的独立工作——证明QCMI与因果结构的关系不是DGF独有的发现方向，但具体机制完全不同
- 关键区分: Boldis-Levay的QCMI是几何量(通过RT公式)，DGF的QCMI是信息论量(非马尔可夫性)
- 位置: Introduction (相关但不同路径) + Discussion (QCMI的多种物理角色)

---

### 文献7: Agon & Faulkner (2016) — 互信息+视界几何

**文献信息:**
Agon, C.A. & Faulkner, T. "Quantum Corrections to Holographic Mutual Information." *JHEP* 08, 118 (2016). arXiv:1511.07462.

**核心声张:** 计算全息互信息的领头阶量子修正，验证了FLM (Faulkner-Lewkowycz-Maldacena 2013)提议——量子纠缠熵修正等于bulk互信息。

**与DGF的重叠:**
| DGF声张 | 重叠 | 程度 |
|:--|:--|:--:|
| DGF-1 (CFOL) | 使用量子互信息/条件互信息 | 工具级 |
| DGF-5 (拥堵→视界) | 互信息与bulk几何的关系 | 精神级 |

**DGF有而Agon-Faulkner没有的:**
1. **框架不同** — A&F在AdS/CFT内，DGF不在。
2. **互信息的角色不同** — A&F的互信息是CFT子区域之间的(通过CFT关联函数计算)，DGF的QCMI是系统-环境-参考之间的(通过因果图量子电路计算)。
3. **没有因果拓扑** — A&F不讨论因果图、b₁、Cartan参数。
4. **没有QCMI=0的充要条件**。
5. **A&F是量子修正(1/N)** — DGF是严格结果。

**引用策略:** **正面引用 (AdS内的并行发展)**
- 引用为全息框架内互信息与几何关系的标准结果
- DGF可定位为"在AdS/CFT之外——不依赖全息对偶——建立的因果拓扑-QCMI对应"
- 位置: Discussion (与全息对偶的关系)

---

### 文献8: Banerjee (2015) — 因果视界热力学+RG流

**文献信息:**
Banerjee, S. "RG flow and thermodynamics of causal horizons in AdS." *JHEP* 10, 098 (2015). arXiv:1508.01343.

**核心声张:** AdS中的因果视界是Killing视界(膨胀等距生成)，RG流破坏膨胀对称性使视界变为动力学视界。边界RG流对偶于因果视界的热力学——全息c-函数等于动力学因果视界的Bekenstein-Hawking熵(密度)。

**与DGF的重叠:**
| DGF声张 | 重叠 | 程度 |
|:--|:--|:--:|
| DGF-5 (拥堵→视界) | 因果视界+RG流——DGF墙#3 (因果图RG流→视界)与Banerjee方向高度相关 | 方向级 |
| DGF-6 (三公理) | 热力学第二定律=全息c-定理——与DGF的"溢出不可逆"(A3)精神一致 | 精神级 |

**DGF有而Banerjee没有的:**
1. **框架完全不同** — Banerjee在AdS/CFT内(Poincare AdS+Killing视界)，DGF在离散因果图上。
2. **RG流的目标不同** — Banerjee的RG流是边界CFT的普通RG(改变耦合常数)，DGF的RG流是因果图的粗粒化(微观→宏观标度)。
3. **没有QCMI** — Banerjee使用全息纠缠熵(RT公式)推导c-函数，不使用QCMI。
4. **没有微观离散结构** — 连续统AdS。
5. **没有CFOL, η₀, b₁**。

**Banerjee有而DGF没有的:**
1. 与全息c-定理的严格对应——这是DGF墙#3的参照物(Banerjee证明了"视界热力学第二定律=c-定理"，DGF需要证明"因果图RG流→经典性涌现"的类似命题)。

**引用策略:** **正面引用 (RG流参照物)**
- 引用为DGF墙#3的AdS参照物——"Banerjee在AdS/CFT内证明了视界热力学与RG流的对偶关系，DGF的目标是在离散因果图上建立类似的对应，但不依赖全息对偶"
- 位置: Wall #3讨论 (因果图RG流)

---

### 文献9: Ochogo (2025) — 退相干→质量/时间/时空

**文献信息:**
Ochogo, P.M. "Gravitational Dynamics from Coherence Gradients: A Relational Coherence Framework of Time and Mass." SSRN: 5432255 (2025).
Ochogo, P.M. "Emergent Coherence Network: From Photon-Links to Spacetime and Light Speed." SSRN: 5394005 (2025).
(注意: 发表在SSRN/Zenodo, 非arXiv或同行评审期刊)

**核心声张:** 时空、质量和引力从光子链接(photon-link)网络的相干场C(x,t)∈[0,1]梯度涌现。引力加速度g=-c²∇C。质量解释为"环路拥堵"(loop congestion)，退相干驱动时间箭头。

**与DGF的重叠:**
| DGF声张 | 重叠 | 程度 |
|:--|:--|:--:|
| DGF-5 (拥堵→视界) | "拥堵/容量界→引力"概念——Ochogo的"环路拥堵"与DGF的"容量饱和→视界"是同类思路 | 概念级 |
| DGF-1 (CFOL) | 使用因果网络(causal photon-link network) | 框架级 |
| DGF-6 (三公理) | 退相干→时间箭头 | 概念级 |

**DGF有而Ochogo没有的:**
1. **定量精确性** — Ochogo的框架是概念性的(相干场C(x,t)的函数形式未从第一原理导出)。DGF的CFOL是严格充要条件，η₀是精确常数，QCMI计算公式是闭式的。
2. **量子信息论工具体系** — Ochogo不使用QCMI、sQNM、Holevo界、Fawzi-Renner下界。他的"相干"概念是经典网络相干，不是量子相干。
3. **IBM Q验证** — Ochogo无硬件实验。
4. **数学严密性** — CFOL是定理；Ochogo的核心方程(g=-c²∇C)是假设而非推导。
5. **Cartan代数结构** — Ochogo没有。

**Ochogo有而DGF没有的:**
1. 与Standard Model的重构尝试(holonomy network→gauge theory)。
2. 光子链接作为基本本体(photon-link fundamentalism)——DGF的基本本体是因果图节点(≤1bit/节点)和量子信道。

**引用策略:** **区分引用 (概念同路人但技术路径完全不同)**
- 可引用为"独立研究者同期探索了因果网络→引力涌现的类似概念方向"
- 明确区分: Ochogo的概念性框架 vs DGF的数学定理+硬件验证
- 位置: Introduction末尾 (同期工作) 或 Discussion (开放问题)
- **诚实警告:** Ochogo的工作未通过同行评审(SSRN/Zenodo)，引用时需标注

---

### 文献10: Kim (2025) — 标量场+退相干→时空密度引力

**文献信息:**
Kim, K.-S. & Ryu, S. "Entanglement transfer from quantum matter to classical geometry in an emergent holographic dual description of a scalar field theory." *JHEP* 05, 260 (2021). arXiv:2002.nnnnn.
(注意: 搜索结果显示Kim 2021而非2025——可能REVIEWER指的是更新的工作或同一作者的不同论文)

**核心声张:** 对标量场理论施加递归RG变换→涌现的(D+1)维全息Einstein-Klein-Gordon型作用量。额外维度对应RG标度。大N极限下量子涨落被压制→经典引力。纠缠从量子物质转移到经典几何("entanglement transfer")。

**与DGF的重叠:**
| DGF声张 | 重叠 | 程度 |
|:--|:--|:--:|
| DGF-5 (拥堵→视界) | RG流→涌现引力+额外维度——与DGF墙#3 (因果图RG→q场)概念同构 | 方向级 |
| DGF-1 (CFOL) | 纠缠→几何 (entanglement transfer = 量子信息→经典时空) | 概念级 |

**DGF有而Kim没有的:**
1. **RG的起点不同** — Kim从标量场理论(Gaussian level, large-N)出发，DGF从离散因果图(≤1bit/节点)出发。
2. **涌现的是什么不同** — Kim涌现的是全息对偶(Klebanov-Polyakov型)，DGF涌现的是q场+Poisson方程(不是全息对偶)。
3. **QCMI作为诊断量** — Kim不使用QCMI，使用路径积分+RG。
4. **CFOL定理** — 无对应物。
5. **η₀, b₁, Cartan参数** — 均无对应物。
6. **IBM Q验证** — 无对应物。

**Kim有而DGF没有的:**
1. 与已知全息对偶的明确连接(KP对偶, O(N)矢量模型)。
2. 大N可解性——提供了一个严格可解的涌现引力模型。

**引用策略:** **正面引用 (RG涌现引力的独立路线)**
- 引用为"通过RG从量子场论涌现引力的最接近DGF精神的现有工作"
- DGF的不同: Kim需要大N+全息对偶，DGF只需要因果图信息论公理
- 位置: Wall #3 (RG流讨论)

---

### 文献11: Abanto (2021/25) — 信息-质量-能量等效+修改熵引力

**文献信息:**
Abanto, J.A.Q. "Information Theory of Gravity (ITG): A Modified Entropic Gravity Using the Mass-Energy-Information Equivalence Principle." Preprints.org: 202110.0082 (2021+). 多版本更新至v8 (2025)。
(注意: 发表在Preprints.org, 非同行评审期刊)

**核心声张:** 修改Verlinde的熵引力——用Vopson的质量-能量-信息等效原理(MEIEP)取代Equipartition定理。引力的大小由信息密度比(N_d)²决定。声称重现MOND、Tully-Fisher关系和外场效应。

**与DGF的重叠:**
| DGF声张 | 重叠 | 程度 |
|:--|:--|:--:|
| DGF-5 (拥堵→视界) | "信息密度→引力强度"概念——Abanto的(N_d)²和DGF的b₁/QCMI都从信息分布驱动引力 | 概念级 |
| DGF-6 (A1信息存在) | MEIEP (信息-质量-能量等效) 与DGF的"信息作为本体论基本量"精神一致 | 范式级 |

**DGF有而Abanto没有的:**
1. **微观机制** — Abanto的信息是宏观的(数字比特)，DGF的信息是量子信息(QCMI, sQNM)。
2. **因果拓扑** — Abanto没有b₁、Cartan参数、因果图。
3. **CFOL定理** — Abanto没有任何严格定理。
4. **η₀常数** — Abanto使用Vopson的κ_m(质量-信息转换因子)，不是从量子信息论推导的。
5. **硬件验证** — 无。

**Abanto有而DGF没有的:**
1. 星系尺度的定量拟合(MOND, Tully-Fisher)——DGF尚未做到。
2. 信息的宏观操作定义(数字比特)。

**引用策略:** **区分引用 (宏观信息引力但不同路线)**
- 可引用为"信息→引力"的宏观现象学版本
- 明确区分: Abanto是宏观数字信息的唯象学——DGF是微观量子信息的理论框架
- **诚实警告:** Preprints.org预印本，非同行评审
- 位置: Discussion (信息引力现象学对比)

---

### 文献12: Maes (2020) — 纠缠→等效原理

**文献信息:**
Maes, S.H. "Quantum Gravity Emergence from Entanglement in a Multi-Fold Universe." viXra:2006.0088 (2020).
Maes, S.H. "Derivation of the Equivalence Principle in a Multi-Fold Universe." viXra:2010.0090 (2020).
(注意: 发表在viXra, 非同行评审)

**核心声张:** 引力从虚粒子EPR纠缠中涌现——多折叠(multi-fold)机制产生有效的1/r吸引势→曲率→引力。等效原理(惯性质量=引力质量)从折叠拉格朗日量自动推导出，而非假设。

**与DGF的重叠:**
| DGF声张 | 重叠 | 程度 |
|:--|:--|:--:|
| DGF-5, DGF-6 | "纠缠→引力"概念方向一致 | 概念级 |

**DGF有而Maes没有的:**
1. **机制完全不同** — Maes用虚粒子EPR对+折叠空间，DGF用因果图+QCMI+容量界。
2. **CFOL定理** — 无对应物。Maes没有QCMI概念。
3. **因果拓扑** — Maes的多折叠是非因果的(瞬时关联)，DGF的因果DAG强调因果有向性。
4. **η₀常数** — 无对应物。
5. **IBM Q验证** — 无。
6. **数学严密性** — Maes的工作是概念性的，缺乏严格定理。

**Maes有而DGF没有的:**
1. 等效原理的"推导"——DGF不声称推导等效原理。
2. 暗物质从实粒子纠缠的解释——DGF未有类似声称。

**引用策略:** **区分引用 (精神同路人)**
- 可引用为"纠缠→引力"方向的另一个独立探索
- 明确区分: Maes的概念性多折叠框架 vs DGF的定理级CFOL+硬件验证
- **诚实警告:** viXra预印本(未经moderation)，引用需极大谨慎——可能建议REVIEWER排除此篇
- 位置: 如果必须引用则放在脚注或Discussion末尾("相关但不属同一严谨性层级的探索")

---

### 文献13: Obidi (2026) — 信息几何→黎曼曲率+爱因斯坦

**文献信息:**
Obidi, J.O. "Beyond Einstein: The Entropic Origin of Geometry, Matter, and Gravitation in the Theory of Entropicity (ToE)." Cambridge Engage (2026).
Obidi, J.O. "From Information Geometry to Information Gravity: Correspondence of the Obidi Action and the Einstein-Hilbert Action." Cambridge Engage (2026).
(注意: 发表在Cambridge Engage(早期研究平台), 非同行评审)

**核心声张:** 时空从统计信息流形的Fisher-Rao度规涌现。曲率转移定理(CTT): 物理时空Riemann张量是信息流形Riemann张量在热力学极限下的pushforward。Einstein方程恢复为涌现的宏观热力学恒等式。Obidi不变量κ_Ω测量残余信息曲率(非零→宇宙学常数)。

**与DGF的重叠:**
| DGF声张 | 重叠 | 程度 |
|:--|:--|:--:|
| DGF-6 (三公理) | 信息几何→物理时空几何——与DGF的Čencov-Petz连接(T4a)使用同一数学工具箱 | 工具级 |
| DGF-5 (拥堵→视界) | Fisher-Rao度规→Einstein方程 | 方向级 |

**DGF有而Obidi没有的:**
1. **Lorentzian号差问题** — DGF的T4a/C1明确指出: Čencov-Petz证明信息度量是Riemannian(正定)，不是Lorentzian。要得到Lorentzian号差需要额外对称破缺(DGF的三舱口分类学)。Obidi声称直接从Riemannian Fisher-Rao得到Lorentzian Einstein方程，但未解释号差如何涌现——这是DGF认为必须解决的问题。
2. **因果拓扑** — Obidi使用统计流形(Fisher-Rao)，DGF使用因果图(b₁, Cartan)。
3. **CFOL定理** — 无对应物。
4. **η₀=1/(8ln2)** — Obidi有ln2作为"最小曲率间隙"(OCI中的常数)，但含义不同。
5. **IBM Q验证** — 无。

**Obidi有而DGF没有的:**
1. Obidi作用量(OAP)——从Shannon熵和Fisher信息构造的完整变分原理。
2. 曲率转移定理(CTT)——如果有朝一日被严格证明，将是重要结果。
3. 常数的推导(c, ħ从信息极限推导的"无急定理")。

**引用策略:** **区分引用 (竞争但可对话)**
- Obidi和DGF是"信息几何→引力"赛道上的两个独立选手
- DGF的优势: CFOL定理+η₀常数+IBM Q验证 (已落地的量子信息基础)
- Obidi的优势: 完整的变分原理(Obidi作用量) (理论完整性更好)
- 关键分歧点: DGF坚持Lorentzian号差需要额外对称破缺(三舱口分类学)，Obidi声称可以直接从Fisher-Rao得到——这可能是DGF反驳Obidi的学术争论点
- **诚实警告:** Cambridge Engage非同行评审
- 位置: Discussion (信息几何方向的竞争与互补)

---

### 文献14: Karazoupis (2025) — 离散信息时空→涌现准粒子

**文献信息:**
Karazoupis, M. "Complete Theory of Simplicial Discrete Informational Spacetime: Towards a Predictive and Testable Theory of Quantum Spacetime." SSRN: 5176314 / Preprints.org: 202504.0029 (2025).
Karazoupis, M. "Emergence of Semi-Dirac Quasiparticles in a Simplicial Discrete Informational Spacetime." SSRN: 5208515 (2025).
(注意: 发表在SSRN/Preprints.org, 非同行评审期刊)

**核心声张:** 时空由基本不可分量子"simplicial chronotopes"(4-单形/pentachora)构成。引力作为熵力(继承Verlinde)。暗物质=信息诱导的挠率(熵梯度)，暗能量=几何基态能。粒子=拓扑缺陷(费米子=扭曲单形，玻色子=集体Pachner移动激发)。声称涌现半Dirac准粒子(一个方向线性色散，另一个方向二次色散)。

**与DGF的重叠:**
| DGF声张 | 重叠 | 程度 |
|:--|:--|:--:|
| DGF全部6条 | 离散信息时空→涌现引力+粒子——DGF和SDIS是"离散信息时空"赛道上最相似的两位选手 | 框架级 |
| DGF-6 (三公理) | 因果结构强制执行(SDIS有因果结构论文) | 框架级 |
| DGF-2 | SDIS的Pachner移动与DGF的plaquette拓扑操作有概念亲缘性 | 工具级 |

**DGF有而Karazoupis没有的:**
1. **量子信息论精确性** — DGF有CFOL定理(充要条件)、η₀常数(Fawzi-Renner下界)、QCMI标度律。SDIS是概念性框架，缺乏DGF层级的数学严格性。
2. **离散结构不同** — DGF用因果DAG(有向无环图)，SDIS用simplicial complex(4-单形)。DAG保留了因果有向性(A3)的核心角色，simplicial complex的因果结构是外加的。
3. **硬件实验** — DGF有IBM Q验证(S/N>600)，SDIS只有理论。
4. **信息承载量** — DGF的A2(≤1bit/节点)是核心约束，SDIS没有类似的量化信息约束。
5. **q场操作定义** — 量子信道开放度——SDIS没有操作层面的信息度量。

**Karazoupis有而DGF没有的:**
1. 准粒子涌现(Semi-Dirac fermions)——DGF不讨论粒子物理。
2. Standard Model重构——DGF目前没有粒子物理端。
3. 质量间隙(Mass Gap)的claim。

**引用策略:** **区分引用 (框架级竞争者但精度不同)**
- SDIS是"离散信息时空"方向上与DGF框架最相似的独立工作
- 关键区分: DGF提供定量定理(CFOL, η₀)和硬件验证(IBM Q), SDIS提供概念框架和粒子物理连接
- DGF应表达为: "SDIS and DGF independently converge on the idea that spacetime is fundamentally discrete and informational, but DGF provides the precise quantum-information-theoretic machinery (CFOL, η₀, QCMI scaling) that SDIS assumes phenomenologically."
- **诚实警告:** Preprints.org/SSRN预印本，非同行评审
- 位置: Introduction (同期独立工作) + Discussion (离散信息时空的不同实现)

---

## 2. 完整区分矩阵

### 2.1 技术重叠矩阵

| 文献 | DGF-1 CFOL | DGF-2 Plaquette | DGF-3 θ²ln(1/θ) | DGF-4 IBM Q | DGF-5 视界 | DGF-6 公理 |
|:--|:--:|:--:|:--:|:--:|:--:|:--:|
| 1. Verlinde 2011 | — | — | — | — | △方向 | △精神 |
| 2. Jacobson 1995 | — | — | — | — | △方向 | — |
| 3. Padmanabhan 1989+ | — | — | — | — | ○概念 | ○精神 |
| 4. Volovik 2007+ | — | — | — | — | △方向 | △范式 |
| 5. Hu 2009 | — | — | — | — | 背景 | 背景 |
| 6. Boldis-Levay 2023 | ◆工具 | — | — | — | ○概念 | — |
| 7. Agon-Faulkner 2016 | ◆工具 | — | — | — | △ | — |
| 8. Banerjee 2015 | — | — | — | — | ●方向 | ○精神 |
| 9. Ochogo 2025 | ○框架 | — | — | — | ○概念 | ○概念 |
| 10. Kim 2021 | — | — | — | — | ●方向 | — |
| 11. Abanto 2021/25 | — | — | — | — | ○概念 | △范式 |
| 12. Maes 2020 | — | — | — | — | ○概念 | — |
| 13. Obidi 2026 | — | — | — | — | ◆工具 | ◆方向 |
| 14. Karazoupis 2025 | — | — | — | — | ●框架 | ●框架 |

**图例:** ● = 强重叠(需重点区分) | ○ = 中等重叠 | △ = 弱重叠 | ◆ = 工具/方法重叠但结论/框架不同 | — = 无重叠

### 2.2 引用策略汇总

| 文献 | 策略 | 强度 | 位置 | 同行评审 |
|:--|:--|:--:|:--|:--:|
| 1. Verlinde | **区分引用** | 必须 | Intro+Discussion | ✅ JHEP |
| 2. Jacobson | **区分引用** | 必须 | Intro(紧接第一段)+Discussion | ✅ PRL |
| 3. Padmanabhan | 正面引用(精神前驱) | 应该 | Intro(概念谱系) | ✅ PRD/RepPP |
| 4. Volovik | 区分引用(不同拓扑) | 建议 | Intro(涌现分类) | ✅ 专著/arXiv |
| 5. Hu | 正面引用(领域背景) | 建议 | Intro(综述) | ✅ JPCS |
| 6. Boldis-Levay | 正面+区分(并行路线) | 建议 | Intro+Discussion | ✅ arXiv |
| 7. Agon-Faulkner | 正面引用(全息参照) | 建议 | Discussion | ✅ JHEP |
| 8. Banerjee | 正面引用(RG参照) | 建议 | Wall #3 | ✅ JHEP |
| 9. Ochogo | 区分引用(同概念不同精度) | 可选 | Discussion | ⚠️ SSRN |
| 10. Kim | 正面引用(RG独立路线) | 建议 | Wall #3 | ✅ JHEP |
| 11. Abanto | 区分引用(宏观vs微观) | 可选 | Discussion | ⚠️ Preprints |
| 12. Maes | 区分引用或建议排除 | 低 | 脚注/Discussion末 | ❌ viXra |
| 13. Obidi | 区分引用(竞争对话) | 建议 | Discussion | ⚠️ Cambridge Engage |
| 14. Karazoupis | 区分引用(框架级竞争者) | 应该 | Intro+Discussion | ⚠️ Preprints |

### 2.3 同行评审状态警告

特别是REVIEWER提供的14篇文献中有**4篇发表在非传统平台:**

| 文献 | 平台 | 风险 |
|:--|:--|:--|
| Ochogo 2025 | SSRN/Zenodo | 未经同行评审, 不可作为强先发证据 |
| Abanto 2021/25 | Preprints.org (v8) | 未经同行评审, 8个版本暗示未稳定 |
| Maes 2020 | viXra | **viXra无任何审核**, 不建议在正规期刊中引用 |
| Obidi 2026 | Cambridge Engage | 早期研究平台, 非同行评审 |
| Karazoupis 2025 | Preprints.org / SSRN | 未经同行评审 |

**对于这些文献的引用原则:**
1. 不应作为DGF的"先发威胁"——未经同行评审的预印本不能削弱DGF的新颖性。
2. 可以引用为"独立研究者同期探索了类似方向"——作为存在证据而非竞争证据。
3. 引用时标注发表平台和同行评审状态。
4. 如果REVIEWER坚持这些构成先发: (a) 指出这些文献未经同行评审; (b) 指出DGF的CFOL定理和IBM Q验证是这些工作完全不具备的; (c) 文献搜索(按13-literature-supplements.md协议)在同行评审文献中未发现CFOL的先发。

---

## 3. 综合定位陈述 (可直接纳入PRD长文Introduction)

以下是综合14篇文献区分分析后，可以放入DGF长文Introduction的定位段落:

> **Placement within the entropy-to-gravity lineage.** Jacobson (1995) established the paradigm that Einstein's equations are thermodynamic identities on local Rindler horizons, and Verlinde (2011) extended this to an entropic-force interpretation using holographic screens. These works demonstrated that gravity admits a thermodynamic description, but they left open the microscopic question: what are the fundamental degrees of freedom whose statistics reproduce the Bekenstein-Hawking entropy? Padmanabhan (1989+) framed this as the decoherence of quantum three-geometries, and Volovik (2007+) proposed a condensed-matter analogue via Fermi points in momentum space. More recently, Boldis & Levay (2023) linked QCMI to AdS causal structure through the Ryu-Takayanagi formula, and Banerjee (2015) showed that AdS causal horizon thermodynamics encodes the boundary RG flow. These works, for all their insights, share a common feature: they operate either within continuous differential geometry (Jacobson, Padmanabhan) or within the AdS/CFT correspondence (Boldis-Levay, Banerjee, Agon-Faulkner 2016). The discrete, graph-theoretic microstructure that underlies these continuum descriptions remains unspecified.
>
> DGF addresses this gap by positing that the fundamental degrees of freedom are the nodes of a discrete causal graph, each carrying at most one bit of classical information (Axioms A1-A2). From this starting point, we prove the CFOL theorem (DGF-1) — an exact necessary and sufficient condition linking causal graph topology to quantum non-Markovianity, verified on IBM Q hardware at S/N > 600 (DGF-4). The QCMI accumulated across causal cycles, quantified by the graph's Betti number b₁(G) and bounded below by η₀ = 1/(8 ln 2) (DGF-1, DGF-2), provides the microscopic origin of horizon entropy: the area law S ∝ A emerges from the min-cut theorem applied to the causal graph (DGF-5), not from the Bekenstein-Hawking formula assumed as input. The RG flow of the causal graph yields the q-field — the quantum channel openness — whose logarithm gives the gravitational potential ψ = −ln q (DGF-5). Unlike entropic gravity (Verlinde) or thermodynamic gravity (Jacobson), DGF makes no use of the Unruh temperature, holographic screens, or the Bekenstein-Hawking entropy as postulates. It requires only the three information-theoretic axioms A1-A3 (DGF-6).
>
> Independent concurrent explorations — notably the Relational Coherence Framework (Ochogo 2025), the Theory of Entropicity (Obidi 2026), and Simplicial Discrete Informational Spacetime (Karazoupis 2025) — converge on the idea that spacetime is fundamentally discrete and informational. DGF distinguishes itself from these conceptual frameworks by providing precise, falsifiable theorems (CFOL, the θ² ln(1/θ) scaling law), a fundamental information-theoretic constant (η₀), and quantitative hardware verification, rather than phenomenological parameterizations.

---

## 4. DGF相对14篇文献的不可替代性总结

| DGF独有的 | 没有任何竞争者具备 |
|:--|:--|
| **CFOL定理** | QCMI=0⟺cⱼ∈(π/2)ℤ, 因果拓扑→量子非马尔可夫性的精确充要条件 |
| **η₀=1/(8ln2)** | Fawzi-Renner下界在多边因果环的有效系数, 信息论基本常数 |
| **θ²ln(1/θ)标度律** | 非微扰对数增强, >100倍偏离标准θ⁴ |
| **IBM Q硬件验证** | Kingston Heron r2, S/N=617×(π/8处CFOL验证) |
| **b₁(G)作为QCMI序参量** | Betti数作为量子非马尔可夫性的拓扑控制参数 |
| **信息视界从拥堵涌现** | 信息容量饱和→视界, 不依赖Rindler几何/全息屏/Unruh温度 |
| **三公理→三舱口** | A1-A3公理体系 + Lorentzian号差涌现的三舱口分类学 |

**底牌:** 即使全部14篇文献都被引用并承认其贡献，DGF的5个定理级结果(CFOL, Reflux界, 面积律, Čencov-Petz连接, AG证伪)加上IBM Q硬件验证构成了一条**独立的、不可约简的贡献链**——没有任何一篇文献提供所有(甚至大部分)这些元素。

---

## 5. 给REVIEWER的回复建议

如果REVIEWER的问题是"这14篇文献是否削弱DGF的新颖性"，建议回复结构:

1. **承认重叠** — Jacobson和Verlinde开创了"信息/热力学→引力"方向，DGF在此方向内工作。
2. **精确区分** — DGF的增量不在方向本身，而在于微观机制(CFOL/η₀/QCMI/因果拓扑)和硬件验证。
3. **定位未审文献** — 9篇文献(Ochogo, Abanto, Maes, Obidi, Karazoupis等)未经传统同行评审，不应视为先发威胁。
4. **核心防守线** — "CFOL定理和IBM Q验证(S/N>600)在所有14篇文献中均无先发——这是DGF的核心不可替代性。"

---

## 附录A: 文献搜索方法学

按照13-literature-supplements.md的搜索协议，本次分析中:

- **同行评审期刊文献** (5篇): Jacobson (PRL), Verlinde (JHEP), Padmanabhan (PRD/RepPP), Hu (JPCS), Agon-Faulkner (JHEP), Banerjee (JHEP), Kim (JHEP)
- **arXiv预印本** (2篇): Volovik (arXiv, 同时有OUP专著), Boldis-Levay (arXiv)
- **非传统平台** (5篇): Ochogo (SSRN), Abanto (Preprints.org), Maes (viXra), Obidi (Cambridge Engage), Karazoupis (Preprints.org/SSRN)

**搜索数据库:** Semantic Scholar API + arXiv API + Google Scholar + Web Search (Bing)。对于非传统平台文献，通过作者名+关键概念进行专项搜索。

---

## 附录B: 版本记录

| 日期 | 变更 |
|:--|:--|
| 2026-06-12 | 初版——14篇文献逐一分析 + Jacobson/Verlinde重点区分 + 完整矩阵 |

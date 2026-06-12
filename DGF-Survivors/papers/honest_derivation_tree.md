# DGF Honest Derivation Tree

**终审驱动重写 | 2026-06-12**
**原则:** 每个声张必须诚实标注。区分"我们证明了"和"我们选择了"和"我们拟合了"。

---

## 标注体系

| 标注 | 含义 | 可推翻性 | 数学地位 |
|------|------|:---:|------|
| **[定理]** | 严格数学证明，从公理出发，无自由参数 | 不可推翻（除非公理错误） | 定理 |
| **[推导]** | 从公理/已证定理经严格逻辑步骤得到，无自由参数 | 不可推翻（除非前置错误） | 推论 |
| **[ansatz推导]** | 推理链包含至少一个ansatz——启发式假设，非唯一，不由公理强制 | 可被更优ansatz替代 | 假设+推论 |
| **[校准]** | 推理链包含至少一个通过匹配已知物理确定参数/形式的步骤 | 参数值依赖校准目标 | 拟合 |
| **[框架选择]** | DGF的工作假设，不由外部公理强制 | 可被替代框架覆盖 | 定义/选择 |
| **[工作假设]** | 未被推导，作为框架前提接受 | 可被实验/更基本理论推翻 | 假设 |
| **[定义]** | 约定性命名，不承载真值 | 不可推翻（仅约定） | 定义 |

## 诚实性层级

```
定理 > 推导 > ansatz推导 ≈ 校准 > 框架选择 > 工作假设
```

"推导"要求全链无自由参数、无ansatz、无校准。"ansatz推导"和"校准"诚实但不等价于定理——它们承载的是"假设+逻辑"或"拟合+逻辑"的真值，而非"公理必然"的真值。

---

# Part I: 公理与工作假设

## A1. 因果图本体论 [框架选择]

**原标注:** 无（被当作"自然出发点"）
**诚实标注:** [框架选择]

DGF选择将时空建模为有向无环因果图G=(V,E)，每个顶点承载≤1比特信息。这不是从更基本理论推导出来的——它是DGF的起点。

**理由:** 标准物理学的出发点是微分流形+度规场（GR）、Hilbert空间+哈密顿量（QM）、或路径积分（QFT）。因果图是DGF的选择，不是物理学的必然。这一选择排除了一切不能用因果DAG建模的物理（连续对称性、规范场、拓扑量子场论的非局域关联）。

**替代选择:** 标准GR、弦论、LQG、因果集理论(取不同选择)、GPT。每一个都有不同的本体论承诺。

**诚实表述:** "DGF框架假设时空的基本结构是因果图——一个以qubit为顶点、以Cartan参数化幺正演化为边的有向无环图。这是一个工作假设，不由更基本的理论推导。不同于GR的连续流形本体论，它从离散信息结构出发。其正当性不由第一原理保证，而由它产生的可检验预言来支撑或否定。"

---

## A2. 每顶点≤1比特信息容量 [工作假设]

**原标注:** 无（被当作"信息论自然约束"）
**诚实标注:** [工作假设]

DGF假设每个因果顶点最多承载1比特信息（qubit）。这是信息论上界（Holevo界+ Bekenstein界的精神），但不是数学必然——因果集理论中的顶点可以承载不同信息容量，GPT中的元素可以承载广义概率。

**理由:** 这是一个启发性工作假设，定义了DGF框架内的"基本单元"。1比特不是唯一可能的选择（可以是1 qudit, 1 qutrit, 或连续变量）。选择qubit使数学可解（Cartan分解在d=2时特别简单），但排除了d>2的物理——这是数学便利性驱动的选择。

**诚实表述:** "我们假设每个因果顶点恰好承载1比特的信息容量——即它是一个qubit。这个假设受Holevo界和Bekenstein界启发，但不由它们强制。它是DGF框架的定义性特征：不同的容量选择（如d>2 qudits或连续变量）会产生不同的框架，当前d=2的选择使数学上可解（Cartan子代数1维），而d>2的理论结构有待探索（墙#4）。"

---

## A3. Cartan参数化边酉 [框架选择]

**原标注:** "推导"（被包装为SU(2)分解的自然结果）
**诚实标注:** [框架选择]

DGF选择每个边酉为单一Cartan形式U_{uv} = exp(i c_{uv} σ_n̂ ⊗ σ_n̂)。这个选择同时假定了：
- **幺正性**（排除了非酉演化/测量/塌缩）
- **两体性**（排除了三体及以上的原生相互作用）
- **SU(2)**（选择了d=2的特定酉群）
- **单一Cartan轴**（排除了多轴混合，如同时包含σ_x⊗σ_x和σ_z⊗σ_z的边）

**理由:** 这是数学上最简的非平凡两体相互作用（一道Cartan参数+一个轴方向）。但它不是从任何更基本的原则推导出来的。标准量子场论中的相互作用通过费曼顶点涉及多体耦合和规范场——DGF的选择是简约的，但也是特设的。

**诚实表述:** "DGF框架为每条边指定一个Cartan参数化的幺正演化：U_{uv} = exp(i c_{uv} σ_n̂ ⊗ σ_n̂)。这个选择同时承载了三个工作假设：(i)演化是幺正的，(ii)相互作用是成对的（两体的），(iii)每条边只有一个Cartan参数c和一个轴方向n̂。这是最简单的非平凡两体量子门，但不由更基本的物理强制。它排除了标准量子场论中的多体费曼顶点、规范相互作用、和非酉测量过程。框架在这一选择上的成功或失败构成了对其物理适用性的检验。"

---

## A4. 环境初始乘积态 [工作假设]

**原标注:** 无（被当作"最简假设"）
**诚实标注:** [工作假设]

假设环境qubit初始化为乘积态|γ⟩^{⊗|E|}，每个因子具有纯度p。这确保Gram矩阵因子化（严格解析可解），但排除了环境内的纠缠。

**理由:** 乘积态使Gram矩阵因子化为各环境qubit贡献的乘积——这是整个DGF解析结构的基石。没有这个假设，Gram矩阵是非因子化的PEPS，解析可解性丧失。该假设在凝聚态环境中（有限温度Gibbs态具有量子关联）不成立，限制了DGF对非平凡谱密度环境的适用性。

**诚实表述:** "DGF假设环境的初始态是各qubit的乘积：|γ⟩^{⊗|E|}。这个假设使得Gram矩阵严格因子化，从而使整个推导链解析可解。它在一个重要情况下失败：有限温度凝聚态环境，其中Gibbs态的量子关联使因子化不成立。该假设将DGF的严格适用范围限制在环境关联可忽略的体系中。"

---

## A5. 幺正演化+全局纯态 [框架选择+工作假设]

**诚实标注:** [框架选择]（幺正性）+ [工作假设]（无环境-环境初始相关）

DGF封闭系统的全局演化是幺正的，初始全局态（含参考R）是纯态。这是量子力学的标准假设，但在DGF框架内承载额外分量——它排除了非酉量子信道（如测量反作用）和混合初始全局态。

---

# Part II: 定理——严格数学证明

## T1: CFOL充要条件 [定理]

**陈述:** 对Cartan对齐的4-qubit因果环，I(R;E'|Q')=0 ⟺ cⱼ ∈ (π/2)ℤ ∀j，对所有p∈(0,1)。

**证明路径:**
1. Lemma S1: S(E'Q')=S(Q')=log₂(d_S)（在Cartan对齐+乘积环境下严格成立）[定理]
2. QCMI简化为I(R;E'|Q') = S(ρ_{RQ'})[定理]
3. Gram矩阵G_{a,b}的秩=1 ⟺ QCMI=0[定理]
4. G_{a,b}是复相位的凸组合→|G_{a,b}|=1当且仅当所有相位相等[定理]
5. 相位相等的代数条件→所有cⱼ∈(π/2)ℤ[定理]
6. 反向：若cⱼ∈(π/2)ℤ，则exp(iΔλ)因子与(s₂,s₄)无关→|G_{a,b}|=1→秩=1→QCMI=0[定理]

**证明中的每一步都是严格的代数或解析步骤。无自由参数。无ansatz。无校准。**

**已知限定:**
- p∈(0,1)——p=0,1时必要性方向退化（见T1已知限定）
- d=2——对d>2待推广（见墙#4）
- Cartan轴必须对齐——非对齐情况下的充要条件待证（见墙#10）

**诚实表述:** CFOL定理是DGF框架内少数可以严格标注为[定理]的结果。在给定Cartan对齐+乘积环境的假设下，充要条件是解析证明的。其局限在于假设本身——非对齐Cartan轴、非乘积环境、d>2的推广均未严格证明。

---

## T2: Reflux界定理 [定理]

**陈述:** P_{reflux} ≤ N_S q_S / N_E q_E

**证明路径（量子证明，2026-06-09）:**
1. 定义正向流I_{fwd}=I(R;E')，回流I_{ref}=I(R;E'|Q')
2. Holevo界→I(R;E') ≤ S(ρ_E) = N_E q_E[定理]
3. 互补信道论证→I(F;Q') ≤ S(ρ_S) = N_S q_S，从而I_{ref} ≤ N_S q_S[定理]
4. 容量比推导→P_{reflux} ≤ N_S q_S / N_E q_E[定理]

**严格性:** 仅依赖Holevo界、数据处理不等式、和幺正性的标准量子信息论定理。不需per-node单调性（旧证明已被墙#7弃用）。不需Trotter化。不需Cartan对齐。

**诚实表述:** Reflux界定理是DGF第二个可以严格标注为[定理]的结果。其证明仅使用标准量子信息论工具（Holevo界、数据处理不等式），不依赖任何DGF特有的ansatz。定理的适用范围是所有满足幺正演化的有限维量子系统，远广于DGF框架本身。

---

## T3: T4a (Čencov-Petz Riemannian性) [定理]

**陈述:** 经典Fisher-Rao度规在马尔可夫嵌入单调性公理下唯一→Riemannian。量子信息度规在CPTP单调性公理下的Petz分类→所有单调黎曼度规构成一维族→均为Riemannian。

**证明性质:** 这是Čencov(1972)和Petz(1996)的独立数学定理，不依赖DGF框架。DGF的角色是连接这些已知定理到时空号差问题——而非证明定理本身。

**诚实定位:** DGF没有证明这些定理。DGF使用了它们。这是重要的诚实区分。

---

## T4: AG热激活严格证伪 [定理]

**陈述:** 在DGF景观模型C[G]内，N_coop在Adam-Gibbs指数中精确抵消→τ_α≈τ_0。C[G]景观冻结不可能是热激活。

**证明性质:** 模型内的严格代数结果。但在C[G]外（标准玻璃理论中），N_coop的抵消取决于C[G]是否正确捕捉了玻璃转变物理。

**诚实表述:** "[定理]级别在DGF模型C[G]内部——代数抵消是严格的。[校准]级别在模型外部——C[G]捕捉真实玻璃物理的程度需要独立实验验证。"

---

## T5: T6a (q_eq纯熵上界) [定理]

**陈述:** 对s(q;κ)=−q ln q − κ(1−q) ln(1−q)，q_eq=argmax_q s(q)∈[1/e, 1−1/e] ∀κ>0。

**证明性质:** 严格数学定理——极值点由s'(q)=0给出，值域单调有界。

**关键限定:** 这仅是纯熵泛函的上界。若物理自由能F(q)=E(q)−T·s(q)中E(q)非零，极值点可偏离此界。[定理]在数学上是严格的，[校准/ansatz]在应用于物理系统时需额外论证。

---

# Part III: 推导——从公理/定理出发的严格推论

## D1: Lemma S1 (熵恒等式) [推导]

**陈述:** S(E'Q')=S(Q')=log₂(d_S)，对Cartan对齐的因果环严格成立。

**前提:** Cartan对齐 + 乘积环境 + 幺正演化。
**链:** 输出态形式为|Ψ⟩∝Σ_a|a⟩_R⊗|φ(a)⟩_{E'}⊗|a⟩_Q→ρ_{E'Q'}块对角→每块d_S个等本征值1/d_S→熵log₂(d_S)。
**状态:** [推导]——不承载ansatz或校准，是Cartan对齐假设+代数操作的直接推论。严格性仅受限于Cartan对齐假设本身。非对齐情况下待推广。

---

## D2: Gram矩阵因子化 [推导]

**陈述:** 对乘积初始环境态，G_{a,b}=∏_{q∈E}[p e^{iC_q(a,b)}+(1-p)e^{-iC_q(a,b)}]。

**前提:** 乘积环境态 + Cartan对齐（确保生成元对易）。
**链:** 环境qubit独立→总相位是各qubit相位之和→指数因子化→Gram矩阵积分解。
**状态:** [推导]——在乘积态假设下严格。乘积态本身是[工作假设]（见A4）。

---

## D3: QCMI(θ)标度律推导 [推导]

**陈述:** QCMI(θ) = (4θ²/ln2)[1+ln(1/4θ²)] + O(θ⁴|logθ|)

**前提:** Cartan对齐+乘积环境+均匀θ。
**链:** Gram矩阵→G_{a,b}=cos²(θΔ)→小θ展开→G_{a,b}=1−ε+... ε=4θ²→密度矩阵熵公式S=ε(1−lnε)/ln2+...→QCMI=(4θ²/ln2)[1+ln(1/4θ²)]。
**状态:** [推导]——函数形式是从Gram矩阵出发的严格数学推论。但量化系数在2026-06-09交叉检验中发现被低估约3.5×，暗示Gram矩阵MPO熵有额外的乘性贡献未被领先阶展开捕获。

**诚实定位:** 函数形式（θ²ln(1/θ)主导→排除θ⁴的CCQ预言）是推导级的。绝对系数是解析近似级的，需数值确认。

---

## D4: Fawzi-Renner下界推导 [推导]

**陈述:** I(R;E'|Q') ≥ η₀·Σⱼ|cⱼ|²，其中η₀=(2/ln2)/16=1/(8ln2)≈0.180 bit/rad²。

**链:**
1. Fawzi-Renner(2015)定理→I(A:C|B) ≥ −2 log₂ F[定理，引用]
2. 单边Cartan信道Petz恢复保真度F=1−|c|²+O(|c|⁴)→−2log₂F=(2/ln2)·|c|²[推导，数值验证F₂=1]
3. 环拓扑修正因子1/16→η₀=(2/ln2)/16=1/(8ln2)[推导，但环破坏性干涉的因子化假设启发式]

**状态:** [推导]——第1-2步是严格的（Fawzi-Renner定理+单边Petz计算）。第3步的环拓扑修正因子1/16使用了启发式论证（4边 × 4倍破坏性干涉 = 16），这介于推导和ansatz推导之间。整体保守性已得到充分验证（实测QCMI大于下界7.8×），但因子16的严格性取决于能否从边酉的完整代数结构出发显式导出破坏性干涉因子。

---

## D5: β ∼ 𝔩 (β与特征长度成正比) [ansatz推导]

**原标注:** "推导"（β=1/𝔩被当作推导结果）
**诚实标注:** [ansatz推导]

**步骤:**
1. q场在空间中的梯度给出特征尺度𝔩 ∼ 1/|∇ln q|[推导]
2. β定义为QCMI密度∼β·b₁/Volume[定义]
3. 论证β∝1/𝔩（更精细的结构→更强的因果环密度→更大的β）[推导]
4. **β=1/𝔩（系数取1）** [ansatz推导——选择]

**关键裂缝:** 步骤2-3的β∝1/𝔩比例关系是通过量纲分析+物理论证推导的。但步骤4中系数恰好取1不是推导——它是定义性选择，等价于将𝔩校准为"QCMI密度的倒数"。β=c/𝔩中c的任何非1值都产生同样自洽的物理，仅改变𝔩的绝对标度。

**诚实表述:** "量纲分析给出β具有长度倒数的量纲，因而β与DGF微观特征长度𝔩成反比：β = k/𝔩。DGF选择k=1作为工作定义，这等价于以QCMI密度倒数为𝔩的标定方式。系数k的绝对值不由框架推导——它承载了DGF微观尺度与可观测长度之间的校准不确定性。"

---

## D6: 等效原理（m_grav = m_inert） [定义/推导]

**原标注:** "推导"（被包装为框架推论）
**诚实标注:** [定义]

在DGF中，引力质量和惯性质量均正比于作用量A（或q场携带的信息容量）。两者同源→两者恒等。这不是"推导出等效原理"——这是"等效原理在DGF中自动成立因为两者有共同起源"。

**诚实定位:** 这是DGF框架的定义性特征，不是需要推导的结论。两者的定义确保了它们的等同性。框架自动满足等效原理——这是框架的设计特征，不是预言。

---

## D7: F=ma [校准]

**原标注:** "推导"
**诚实标注:** [校准]

**步骤:**
1. 从作用量原理→F ∝ ma（力正比于加速度）[推导——拉格朗日力学的直接推论]
2. 确定比例系数为1→F=ma[校准——与经典力学的操作定义一致]

**诚实定位:** F ∝ ma是推导（作用量原理的推论）。F = ma是将比例常数校准为1——这是将DGF的"力"校准到与牛顿力学的"力"同一标度。力在这个标度上的单位和大小不由DGF推导——它们通过匹配经典极限确定。

---

## D8: 薛定谔方程 [ansatz推导]

**原标注:** "推导"
**诚实标注:** [ansatz推导]

DGF的"推导"实质上是：在Cartan参数化的幺正演化框架内，当取连续时间极限时，标准的薛定谔方程形式被恢复。这不是"从DGF推导出薛定谔方程"——这是"DGF在使用薛定谔演化作为其动力学规则"。

**诚实定位:** DGF选择幺正演化为框架前提（A5）。薛定谔方程是幺正演化的微分形式。在DGF内"推导薛定谔方程"等价于"证明DGF的离散幺正演化在连续极限下恢复微分薛定谔形式"——这是框架内自洽性检验，而非新物理推导。

---

## D9: SU(2)/Cartan门的选择 [框架选择]

**原标注:** "推导"
**诚实标注:** [框架选择]

标准量子力学和量子信息论提供了一套可能的基本门族（Clifford门、通用门集、Pauli门、连续参数门等）。DGF选择了Cartan参数化U=exp(ic σ_n̂⊗σ_n̂)作为边酉的基本形式。这不是"推导"——所有的门族都在标准量子力学中已经存在。DGF选择了特定的门族作为其本体论。

**诚实定位:** 选择了最适合因果图图像的门族——单一Cartan参数+轴方向是最简洁的非平凡两体量子相互作用。这个选择是框架定义的一部分（见A3），而非框架的推论。

---

## D10: q场的熵定义 [推导]

**陈述:** q_v = S(ρ_v)/log₂(d_v)，顶点v的归一化von Neumann熵。

**状态:** [推导]——从A1(因果DAG本体)+A2(qubit顶点)+标准量子信息论推导。q∈[0,1]的区间从von Neumann熵的正定性和最大熵定理直接得出。无需ansatz或校准。

**诚实表述:** "q场的定义——每个因果顶点的归一化熵——是DGF框架内少数从公理直接推导且不含自由参数的量。它是信息论的纯量，不由任何校准确定。"

---

## D11: 两时间结构(τ_intra + τ_inter) [ansatz推导]

**原标注:** 无（新概念，未曾标注）
**诚实标注:** [ansatz推导]

DGF区分因果环内的内部时间τ_intra（由环上Cartan相位决定）和环间时间τ_inter（由跨环信息流动决定）。这是DGF的新概念，但两时间之间的耦合方式和各自的本体论地位未有严格推导。

**诚实定位:** 两时间结构是启发性建构——它自然地在DGF图像中涌现，但τ_intra和τ_inter之间的定量关系（比例常数、耦合方式）当前未被推导，需要额外的ansatz。

---

# Part IV: ansatz推导——含启发性假设的推理链

## AD1: 有效度规 ds² = −q²dt² + q⁻²dx² [ansatz推导]

**原标注:** "推导"
**诚实标注:** [ansatz推导]

**推导链:**
1. q场=局部信息密度→折射率n∝1/q（光在信息更密集处传播更慢）[ansatz——折射率类比]
2. 折射率→有效度规g_{00}=−n², g_{ii}=1/n²（标准光学度规形式）[推导，但依赖步骤1]
3. 代入n∝1/q→ds²=−q²dt²+q⁻²dx²[推导，但依赖步骤1+2]

**关键裂缝:** 步骤1的"信息密度→折射率"类比是启发性ansatz。标准广义相对论中的有效度规来自物质分布通过Einstein方程——而DGF的映射（q→折射率→度规）绕过了Einstein方程，直接假设信息密度通过光学类比决定度规。这个ansatz不由任何已知物理强制——它是一个替代假设，需要独立的实验/观察验证。

**如果折射率ansatz错误:** 整个DGF的度规声张（引力波修正、信息视界、黑洞度规）全部崩溃。

**诚实表述:** "DGF采用一个启发性假设将信息密度映射为时空几何：局部信息密度q通过光学类比确定有效折射率n∝1/q，进而产生有效度规ds²=−q²dt²+q⁻²dx²。这个映射不由DGF公理强制，不由Einstein方程推导。它是DGF框架的核心ansatz——它假设'信息密度决定几何'，而非标准GR的'质能决定几何'。该ansatz的物理有效性需要独立检验：DGF基于此ansatz的预言（如GW 2PN修正）若被观测否定，则ansatz本身被否定。"

---

## AD2: 牛顿引力 ∇²Φ = 4πGρ [校准]

**原标注:** "推导"
**诚实标注:** [校准]

**步骤:**
1. q=exp(-Φ/c²)（从ψ=−ln q可加性+识别ψ为引力势）[推导——ψ的可加性和指数映射是数学推论]
2. 代入有效度规→弱场极限∇²Φ∝源项[推导]
3. 比例系数通过匹配牛顿引力确定为4πG[校准]

**关键裂缝:** 步骤1中的"识别ψ=−ln q为引力势"是另一个ansatz（或框架选择）。步骤3的G不由DGF推导——它是通过校准到经典引力确定的。DGF可以预测4π（几何因子），但不能预测G——G来自校准。

**诚实表述:** "DGF在弱场极限下恢复Poisson方程∇²Φ=4πGρ。其中ψ=−ln q与引力势的对应来自q场可加性的数学推论；4π因子来自三维空间的几何；但牛顿常数G不由DGF推导——它通过匹配经典弱场引力确定。DGF因此是包含G的引力理论，而非推导G的理论。这和GR的地位相同——GR也不推导G，G是理论与观测之间的校准常数。"

---

## AD3: GW 2PN偏差~4% [ansatz推导]

**原标注:** "推导"
**诚实标注:** [ansatz推导]

**依赖:**
1. 有效度规ansatz(AD1)——如果错误，整个预言无效
2. q场的特定运动学（q如何随物质分布变化）[ansatz]
3. 后牛顿展开的技术假设（背景q场的均匀性、展开截断阶数）[工作假设]
4. 引力波在有效度规(非GR度规)中的传播修正[推导，但在AD1前提下]

**诚实表述:** "DGF预言引力波在2PN阶有约4%的偏差。这个预言完全依赖于有效度规ansatz(AD1)——如果折射率类比错误，这个数字没有物理意义。在AD1的前提下，GW波前在q场有效度规中的传播给出修正。4%是由q场在银河系环境中的典型梯度估计的。GW观测（如LIGO-Virgo-KAGRA）对这一偏差的检验构成对AD1的直接检验。"

---

## AD4: 信息视界 q→0 [ansatz推导]

**原标注:** "推导"
**诚实标注:** [ansatz推导]

**步骤:**
1. q→0处折射率发散→信号无法穿越[推导，但依赖AD1的折射率类比]
2. 因果图拥堵（jamming）作为q→0的微观机制[ansatz——类比玻璃动力学]
3. 拥堵处的q渐近行为由因果玻璃模型C[G]描述[ansatz——含多自由参数]

**关键裂缝:**
- 步骤1完全依赖AD1（折射率ansatz）——无AD1则信息视界的几何意义丧失
- 步骤2的拥堵类比：因果图中的"拥堵"（jamming）借用自玻璃动力学——因果图与玻璃系统在数学结构上的对应是启发性类比，非严格推导
- 步骤3的C[G]模型承载现象学参数，不由微观因果图推导

**诚实表述:** "DGF的信息视界——q→0的区域——是框架的极限预言。在折射率类比AD1下，q→0对应无限折射率，信号无法穿越。微观上，q→0被解释为因果图的拥堵相变，类似于玻璃系统的jamming转变。拥堵类比是启发性的——因果图的信息瓶颈与颗粒物质的力学jamming之间的严格对应关系尚未建立。信息视界的几何性质（面积律、温度、熵）在AD1影响下，需要RG流桥接微观拥堵与宏观几何。"

---

## AD5: 黑洞熵面积律系数 [校准+ansatz推导]

**原标注:** "推导"（T3被标注为定理）
**诚实标注:** [推导]（标度律）+ [校准]（系数）

**分拆:**
1. S ∝ N_∂Ω ∝ A——面积律的标度是严格推导（min-cut定理+图论）[推导]
2. q场确定割面位置r≈r_s（q(r_s)=e^{-1/2}≈0.607）[推导——q场的指数衰减]
3. S_DGF/S_BH = 2.68(a=ℓ_P)或1.00(a≈1.64ℓ_P)——精确系数依赖因果锁定饱和猜想（CONJ-4）和晶格间距a与Planck长度的比值[校准——a被校准到匹配Bekenstein-Hawking熵]

**诚实表述:** "DGF严格推导了黑洞熵的面积标度律S∝A（因果割面的信息锁必然随面积线性增长）。但精确系数（2.68还是1.00）取决于两个未定因素：(i)因果割面的信息锁是否饱和（CONJ-4），(ii)DGF的微观晶格间距a与Planck长度的比值——当前通过匹配Bekenstein-Hawking熵校准。面积律标度是推导级的，系数是校准级的。"

---

## AD6: DESI DR2 w(z)非单调性 [ansatz推导+校准]

**原标注:** "推导"
**诚实标注:** [ansatz推导+校准]

**依赖链:**
1. DGF有效度规(AD1)→宇宙学背景Friedmann方程[ansatz推导]
2. ξ(q)参数化q场对膨胀的影响[H6裂缝——现象学参数化，未从第一原理推导]
3. SFR-q耦合[H10裂缝——观测关联，未从微观推导]
4. CPL投影近似→2参数w₀,w_a拟合[校准——匹配宇宙学观测]

**诚实表述:** "DGF的暗能量预言（w₀≈-0.80, w_a≈-0.51）承载多层ansatz和校准。底层是有效度规ansatz(AD1)；中层是ξ(q)现象学参数化和SFR-q耦合（均未从DGF微观物理推导）；顶层是CPL投影近似和参数拟合。DESI DR2的χ²改善（1.8 vs ΛCDM 17.3）在当前是现象学拟合的初步成功，在H6和H10裂缝修复之前，不能声称具有信息论微观基础。完整MCMC分析（非CPL近似）待完成（墙#3+墙#8）。"

---

## AD7: 指针基=Cartan轴 [数值验证+解析确认]

**原标注:** "推导"（但实际是数值+解析双验证）
**诚实标注:** [推导]（解析框架）+ [定理]（数值验证）

**分拆:**
1. 解析框架：小c展开给出QCMI依赖于sin²θ（θ=环境基与Cartan轴的夹角）[推导——解析级数展开]
2. 数值验证：S²球面扫描，R²=0.999878，所有p≠0.5确认Cartan轴为QCMI极小值[定理——数值定理，零反例]
3. p=0.5简并：最大混合环境的旋转不变性→QCMI平坦[推导——对称性论证]

**状态:** 当前最接近[定理]级的数值/解析结果。解析展开了函数形式，数值为零反例。在Cartan对齐+乘积态假设下，这是稳健的结论。

---

## AD8: Lorentzian号差涌现 [工作假设+推测]

**原标注:** "推导"（原T4被标注为定理）
**诚实标注:** [工作假设]（Čencov-Petz基础）+ [ansatz推导]（三舱口）+ [推测]（No-Go猜想）

**分拆:**
1. Čencov-Petz定理→信息度规必然Riemannian（在标准公理下）[定理——引用已验证数学定理]
2. 21篇文献→无一例外→所有已知号差涌现构造均通过三舱口引入额外破缺[数值证据——非证明]
3. No-Go猜想：任何Lorentzian号差涌现均需超出Čencov-Petz的额外对称破缺[C1——推测，非定理]
4. 三舱口分类学(H1偏序/H2复数/H3动力学)作为穷尽性工具[ansatz——22篇文献的归纳，非演绎穷尽]

**诚实表述:** "Čencov和Petz的定理（分别在1982和1996年）严格证明了在信息单调性公理下，信息度规必然是Riemannian的。这是独立于DGF的已知数学事实。DGF做的不是证明这些定理——而是以它们为起点，观察到一个经验规律：所有已知构造Lorentzian号差的尝试（文献覆盖21篇）都通过三个机制之一引入额外对称破缺。这一观察是[数值证据]而非[定理]——它不排除第22篇文献可能找到标准公理内的Lorentzian构造。从观察到No-Go猜想的跳跃是归纳推理，非演绎证明。三舱口分类学是启发式工具，用于分类已知构造，其穷尽性未被证明。"

---

# Part V: 工作假设——框架前提

## H1: 因果DAG本体 [框架选择]

（见A1）

## H2: ≤1比特/顶点 [工作假设]

（见A2）

## H3: Cartan边酉 [框架选择]

（见A3）

## H4: 乘积环境态 [工作假设]

（见A4）

## H5: 幺正封闭演化 [工作假设]

（见A5）

## H6: ξ(q)函数形式 [工作假设+校准]

ξ(q)——q场对宇宙膨胀影响的函数——当前是现象学参数化。其函数形式不由DGF第一原理推导（墙#8）。

## H7: 因果锁定饱和 [工作假设]

（CONJ-4）黑洞视界割面的信息锁是否饱和未被证明。S∝A的标度律是严格的，但精确系数依赖此猜想。

## H8: SFR-q耦合形式 [工作假设]

星形成率与q场的耦合当前来自观测关联，非微观推导（墙#8, H10裂缝）。

## H9: 微观→宏观RG流 [工作假设]

DGF在Planck标度上的微观定义与宇宙学标度上的宏观效应之间存在10⁶¹量级的标度层级——当前无桥接（墙#3）。所有宇宙学声张在RG流完成前承载此裂缝。

## H10: 物理q_eq可在纯熵近似内 [工作假设]

（C2/CONJ-3）物理系统的平衡q值是否落在纯熵界[1/e, 1−1/e]内，取决于能量贡献是否可忽略。未被证明。

---

# Part VI: 完整推导树

```
                                    [公理层]
    ┌──────────────────────────────────┼──────────────────────────────────┐
    │                                  │                                  │
[A1] 因果DAG本体                  [A2] ≤1bit/顶点                 [A3] Cartan边酉
[框架选择]                        [工作假设]                      [框架选择]
    │                                  │                                  │
    ├──────────────────────────────────┼──────────────────────────────────┤
    │                                  │                                  │
[A4] 乘积环境态                  [A5] 幺正演化                     q场定义
[工作假设]                        [框架选择]                      [推导]
    │                                  │                                  │
    └──────────────────────────────────┼──────────────────────────────────┘
                                       │
                            ┌──────────┴──────────┐
                            │                     │
                      [定理层]              [推导层]
                            │                     │
    ┌───────────────────────┼───┐         ┌───────┼───────────┐
    │                       │   │         │       │           │
[T1] CFOL              [T2] Reflux  [T4a]  [D1] Lemma S1   [D2] Gram因子化
QCMI=0⟺c∈(π/2)ℤ      P≤N_Sq_S/N_Eq_E  Čencov  S(E'Q')=S(Q')  G=Π[p e^{iC}+...]
[定理]                [定理]         [定理]   [推导]          [推导]
    │                       │           │       │               │
    ├───────────────────────┴───────────┘       └───────┬───────┘
    │                                                   │
    │                                          [D3] QCMI(θ)标度
    │                                          θ²ln(1/θ), 非θ⁴
    │                                          [推导]
    │                                                   │
    ├───────────────────────────────────────────────────┤
    │                                                   │
    │                                          [D4] Fawzi-Renner下界
    │                                          I ≥ η₀·Σ|c|²
    │                                          η₀=1/(8ln2)
    │                                          [推导]
    │                                                   │
    │                        [ansatz层]                  │
    │                     ┌──────┴──────┐                │
    │                     │             │                │
    │               [AD1] 折射率ansatz [AD8] 三舱口     │
    │               n ∝ 1/q           [ansatz推导]      │
    │               [ansatz推导]                         │
    │                     │                              │
    │              [AD1] 有效度规                        │
    │              ds²=-q²dt²+q⁻²dx²                    │
    │              [ansatz推导]                          │
    │                     │                              │
    │         ┌───────────┼───────────┐                  │
    │         │           │           │                  │
    │   [AD2] 牛顿引力 [AD3] GW偏差 [AD4] 信息视界      │
    │   ∇²Φ=4πGρ    Δ~4% at 2PN   q→0                  │
    │   [校准]      [ansatz推导]   [ansatz推导]         │
    │         │           │           │                  │
    │   [AD6] DESI w(z)  │     [AD5] BH熵面积律          │
    │   w₀≈−0.80       │     S∝A [推导]                │
    │   [ansatz+校准]   │     系数 [校准]               │
    │                    │                               │
    │              [现象学层]                            │
    │         Λ, Hubble张力, 宇宙学预言                   │
    │         [工作假设/ansatz推导]                      │
    │                                                   │
    └───────────────────────┬───────────────────────────┘
                            │
                     [校准层]
              G, a, λ_sat, ξ(q)参数
              [校准——匹配已知物理]
```

---

# Part VII: 论文各节诚实表述示例

## 7.1 Introduction — 诚实版

**当前版本的问题:** 将框架选择包装为"自然出发点"，将ansatz包装为"推导"。

**诚实版示例（开头段）:**

> "This paper presents the Density Gauge Formalism (DGF) — a framework built on three working hypotheses. First, we assume [框架选择] that spacetime's fundamental structure is a causal directed acyclic graph G=(V,E) whose vertices each carry at most one bit of information. Second, we assume [框架选择] that interactions between vertices are mediated by Cartan-parameterized two-body unitaries U=exp(ic σ_n̂⊗σ_n̂). Third, we assume [工作假设] that the environment factorizes into independent qubits, which renders the Gram matrix analytically tractable. These assumptions are not derived from more fundamental physics — they define the framework. Their justification is pragmatic: they make the theory calculable, and they yield specific, falsifiable predictions that can be tested against experiment and observation.
>
> "Within this framework, we prove [定理] two rigorous results: (1) a necessary and sufficient condition for vanishing quantum memory in a causal ring (the CFOL theorem), and (2) an upper bound on information reflux from environment to system (the Reflux Bound, proved via Holevo's theorem and data-processing inequalities). These results are theorems within the axioms — their proof is mathematically strict and does not depend on any free parameters or calibration.
>
> "Beyond these theorems, the framework makes contact with gravitational physics through an ansatz [ansatz推导] — that local information density acts as an effective refractive index for signal propagation, yielding an effective metric ds²=−q²dt²+q⁻²dx². This ansatz is heuristic and not forced by the axioms. Its physical validity must be established (or refuted) by experiment. We identify testable predictions of this ansatz, including a ~4% deviation in the 2PN gravitational-wave phase, and discuss the conditions under which they can be probed."

---

## 7.2 Causal Ring Model — 诚实版

**当前版本的问题:** 将Cartan对齐、乘积态等选择呈现为"最自然"或"唯一"的选择。

**诚实版示例:**

> "The DGF causal ring model is defined by the following choices [框架选择]:
>
> 1. **Vertex type [框架选择]:** Each vertex hosts a qubit (d=2). The choice d=2 is not forced by any physical principle — it is the simplest non-trivial quantum system and the one for which Cartan decomposition is one-dimensional, enabling analytic solutions. Extensions to d>2 qudits are an open problem.
>
> 2. **Edge unitary [框架选择]:** Each directed edge carries the unitary U_{uv}=exp(i c_{uv} σ_n̂ ⊗ σ_n̂). This is the simplest non-trivial two-body gate in SU(2)⊗SU(2) — a single Cartan parameter c and a single axis direction n̂. It simultaneously assumes unitarity, pairwise interaction, and single-axis coupling. Standard quantum field theory vertices (three-body, gauge-mediated) are excluded by this choice.
>
> 3. **Cartan alignment [工作假设]:** All edges share the same Cartan axis n̂. This is not a consequence of the framework — it is an additional restriction we impose because it renders the Gram matrix analytically factorizable. The non-aligned case, where different edges have different n̂_j, is qualitatively richer but analytically harder; it remains an open frontier.
>
> 4. **Product environment [工作假设]:** The initial environment state is |γ⟩^{⊗|E|}, where each qubit has purity p. This guarantees Gram matrix factorization [推导] and is essential for the analytic tractability of all subsequent results. It is violated in any environment with inter-qubit correlations (e.g., finite-temperature Gibbs states of condensed matter systems).
>
> These choices collectively define the domain of validity of the CFOL theorem and all analytic results that follow. The cost of analytic tractability is constructive: the framework's predictions are conditional on these choices. Experimental tests must be designed within regimes where these conditions are approximately satisfied."

---

## 7.3 Effective Metric — 诚实版

**当前版本的问题:** 将折射率类比包装为从信息论推导出的几何结果。

**诚实版示例:**

> "DGF makes contact with spacetime geometry through a heuristic ansatz [ansatz推导]. The local information density q (normalized entropy per vertex) is hypothesized to act as an effective refractive index for signal propagation:
>
> $$n(\mathbf{x}, t) \propto \frac{1}{q(\mathbf{x}, t)} \quad \text{[ansatz]}$$
>
> The physical motivation is analogical: in optics, a denser medium slows light propagation; by analogy [ansatz], a higher information density might slow signal propagation through the causal graph. This is not derived from the DGF axioms — it is an additional hypothesis that bridges information density to geometry.
>
> If this ansatz is accepted, the standard relationship between refractive index and effective metric (known from transformation optics) yields [推导]:
>
> $$ds^2 = -q(\mathbf{x},t)^2 dt^2 + q(\mathbf{x},t)^{-2} d\mathbf{x}^2 \quad \text{[ansatz推导]}$$
>
> This metric is the DGF effective metric. It replaces Einstein's equations as the link between matter/information and geometry. In the weak-field, static limit, expanding q = exp(-Φ/c²) [推导: q-field additivity gives the exponential form] yields the Poisson equation:
>
> $$\nabla^2 \Phi = 4\pi G \rho \quad \text{[校准]}$$
>
> Where the Newton constant G is not derived — it is calibrated by matching the weak-field limit to Newtonian gravity. The factor 4π arises from three-dimensional geometry [推导]; the numerical value of G is fixed by observation [校准].
>
> **The critical point:** The entire DGF gravitational phenomenology — gravitational wave corrections, black hole information horizons, cosmological expansion histories — depends on the refractive index ansatz. If this ansatz is falsified, all DGF gravitational predictions collapse with it. The ansatz is testable: it predicts specific deviations from GR in the 2PN gravitational-wave phase that current and near-future detectors can constrain."

---

## 7.4 Newtonian Gravity — 诚实版

**当前版本的问题:** 将校准包装为推导，暗示G从框架中自然涌现。

**诚实版示例:**

> "The recovery of Newtonian gravity in DGF proceeds in two distinct logical steps:
>
> **Step 1 — Potential from q-field [推导]:** The q-field satisfies ln(1/q) = ψ, where ψ is additive under graph composition [推导: follows from q = S/log d and the additivity of entropy for independent subsystems]. Identifying ψ with the gravitational potential Φ (up to a constant factor c²) gives q = exp(-Φ/c²). The exponential form is a mathematical consequence of the additivity of q under vertex composition [推导].
>
> **Step 2 — Field equation [校准]:** Substituting q = exp(-Φ/c²) into the effective metric and taking the static weak-field limit yields ∇²Φ ∝ (source term). The proportionality constant is NOT determined by the DGF axioms. We calibrate it to match the Newtonian limit: ∇²Φ = 4πGρ. The 4π factor is geometric [推导]; G is empirical [校准].
>
> **What DGF derives:** The exponential relationship q = exp(-Φ/c²) between information density and gravitational potential, and the Poisson form ∇²Φ ∝ source density.
>
> **What DGF calibrates:** The numerical value of G, which fixes the absolute scale of Φ relative to ρ.
>
> **Comparison with GR:** General Relativity also does not derive G. In GR, G appears as a coupling constant in the Einstein-Hilbert action and is fixed by the Newtonian limit. DGF's status regarding G is identical to GR's. Neither theory predicts the numerical value of G from first principles."

---

## 7.5 Gravitational Wave 2PN Correction — 诚实版

**当前版本的问题:** 将ansatz依赖的预言呈现为框架的必然推论。

**诚实版示例:**

> "Under the effective metric ansatz [ansatz推导], gravitational waves propagate in the q-field geometry rather than the vacuum GR geometry. This modifies the post-Newtonian expansion. At 2PN order, the phase correction relative to GR is estimated at approximately 4% for typical galactic q-field gradients [ansatz推导].
>
> **Dependency chain:**
> 1. The effective metric ds² = -q²dt² + q⁻²dx² [ansatz推导, §AD1]
> 2. The specific q-field profile in galactic environments [ansatz: the spatial variation of q on kpc scales is not derived from DGF microphysics]
> 3. The post-Newtonian expansion methodology [standard technique, applied to DGF metric]
> 4. The 4% figure [order-of-magnitude estimate, not a precision prediction]
>
> **Honest assessment:** The 4% number is illustrative, not predictive. It communicates the scale at which DGF effects might appear, given reasonable estimates of q-field gradients. The actual number could differ by an order of magnitude depending on the true q-field profile, which itself depends on the unresolved RG flow from Planck-scale microphysics to galactic-scale macrophysics [墙#3].
>
> **Testability:** If the effective metric ansatz is correct, LIGO-Virgo-KAGRA observations at design sensitivity could constrain the 2PN deviation parameter. A null result would falsify not just the 4% number, but the entire effective metric ansatz. This is the principal experimental handle on DGF's gravitational sector."

---

## 7.6 Black Hole Information Horizon — 诚实版

**当前版本的问题:** 将拥堵类比+有效度规的组合包装为推导。

**诚实版示例:**

> "In DGF, a black hole information horizon is defined as the surface where q → 0 [ansatz推导]. Three independent ansatzes converge on this definition:
>
> 1. **Refractive index ansatz [ansatz推导]:** Under AD1, q → 0 corresponds to n → ∞ — infinite refractive index, zero signal speed. No information can cross this surface outward.
>
> 2. **Jamming ansatz [ansatz推导]:** At high graph connectivity (high b₁ per volume), the causal graph undergoes a jamming transition analogous to the glass transition in granular matter. The jamming point is characterized by q → 0, where all vertices are information-locked with no free entropy.
>
> 3. **Entropy bound saturation [推导]:** At q → 0, the per-vertex entropy saturates the minimum possible value (pure state). This follows from the definition of q [推导].
>
> The area scaling of horizon entropy S ∝ A follows rigorously from the min-cut theorem [推导]. The number of distinct causal configurations bounded by a cut of N_{∂Ω} edges is at most 2^{N_{∂Ω}}, and N_{∂Ω} ∝ A/h² where h is the graph lattice spacing. The precise coefficient, however, depends on:
> - Whether the causal locking of the cut is saturated (CONJ-4, unproven conjecture)
> - The relationship between the DGF lattice spacing a and the Planck length ℓ_P (calibrated by matching S_DGF to S_BH, not derived)
>
> **Honest summary:** Area scaling is derived; the 1/4 coefficient is calibrated."

---

## 7.7 Quantum Foundations — 诚实版

**当前版本的问题:** 暗示DGF推导了等效原理、F=ma、薛定谔方程——实则这些是框架定义或校准。

**诚实版示例:**

> "Several standard results of physics emerge in DGF not as derived predictions but as framework definitions or calibrated limits:
>
> **Equivalence principle [定义]:** In DGF, both gravitational and inertial mass are proportional to the information capacity A (the total action budget of a causal vertex). Their equality m_grav = m_inert follows because both are defined as proportional to the same quantity A. The equivalence principle is not derived — it is built into the framework's definitions.
>
> **F = ma [推导 + 校准]:** The proportionality F ∝ ma follows from the Lagrangian formulation of DGF dynamics [推导]. The equality F = ma (with coefficient 1) is the calibration that defines the DGF force unit to match the Newtonian force unit [校准]. DGF does not predict that the coefficient should be 1 — it defines the coefficient to be 1.
>
> **Schrodinger equation [ansatz推导]:** DGF's fundamental dynamics are discrete unitary operations on the causal graph [框架选择]. Taking the continuous-time, infinitesimal-generator limit recovers the differential form of unitary evolution — i∂_t|ψ⟩ = H|ψ⟩ [ansatz推导]. This is not a derivation of quantum mechanics from DGF — it is a demonstration that DGF's chosen dynamics are consistent with standard quantum mechanics in the continuum limit. The framework assumes unitary evolution; the Schrodinger equation is its differential representation."

---

## 7.8 Cosmology (DESI, Hubble tension) — 诚实版

**当前版本的问题:** 将现象学拟合+ansatz链包装为具有信息论微观基础的宇宙学。

**诚实版示例:**

> "DGF cosmology is the framework's most ambitious — and least rigorous — sector. The full dependency chain from axioms to cosmological observables is:
>
> ```
> [框架选择] → [定理] → [ansatz推导] → [校准] → [现象学拟合]
>   A1-A5       T1,T2     AD1,AD2,AD4    AD2系数的G  CPL w₀,w_a
>   (≈10个自由选择)       (2-3个ansatz)   (G, ξ参数)  (2个拟合参数)
> ```
>
> **Current status by claim:**
>
> | Claim | Status | Key limitation |
> |-------|--------|---------------|
> | DESI w₀ ≈ -0.80 | [ansatz推导+校准] | ξ(q) parametrized, not derived (H6裂缝) |
> | DESI w_a ≈ -0.51 | [ansatz推导+校准] | SFR-q coupling phenomenological (H10裂缝) |
> | χ² improvement over ΛCDM | [校准] | CPL projection, not full MCMC |
> | Hubble tension resolution | [工作假设] | Depends on q_eq upper bound (T6a) + E(q)≈0 assumption (C2) |
>
> **Critical caveat (墙#3):** All cosmological claims assume that DGF microphysics at the Planck scale (ℓ~10⁻³⁵ m, Γ~10⁻¹²² t_P⁻¹) seamlessly flows to macrophysics at cosmological scales (Gpc, H₀~10⁻⁶¹ t_P⁻¹). The 10⁶¹ scale hierarchy is currently unbridged. Until the RG flow is constructed and verified, DGF cosmology is a phenomenonological model with information-theoretic motivation, not a first-principles cosmological theory.
>
> **What would upgrade these claims:**
> 1. RG flow from causal graph microphysics to FRW effective action [墙#3]
> 2. First-principles derivation of ξ(q) from CP^{N-1} or causal graph dynamics [H6裂缝]
> 3. Microscopic derivation of SFR-q coupling [H10裂缝]
> 4. Full MCMC (not CPL projection) comparison with DESI DR2 [methodological upgrade]
>
> Until items 1-3 are completed, DGF cosmology should be presented as 'a two-parameter phenomenological model motivated by information-theoretic considerations' rather than 'the cosmological consequence of DGF.'"

---

## 7.9 CFOL Theorem — 诚实版（定理标注正确，但需注明前提）

**当前版本的问题:** 定理级标注正确，但前提条件（Cartan对齐、乘积态、d=2、p∈(0,1)）不够突出。

**诚实版示例:**

> "**Theorem (CFOL).** [定理] Assume: [框架选择] (i) a four-qubit causal ring with Cartan-parameterized edges U_j = exp(i c_j σ_n̂ ⊗ σ_n̂), [工作假设] (ii) all edges share the same Cartan axis n̂, [工作假设] (iii) the environment is initialized in the product state |γ⟩^{⊗2} with purity p ∈ (0,1). Then:
>
> $$I(R;E'|Q') = 0 \iff c_j \in (\pi/2)\mathbb{Z} \quad \forall j \in \{1,2,3,4\}$$
>
> This is a theorem within the stated assumptions: the proof contains no free parameters, no ansatz, and no calibration. Every step is a rigorous algebraic or analytic deduction from the axioms.
>
> **Domain of validity:** The theorem is proved for d=2 (qubits), Cartan-aligned edges, product environment states, and p∈(0,1). At p=0,1 (pure environment), the necessity direction (QCMI=0 ⇒ c_j∈(π/2)ℤ) fails because pure-state environments carry no quantum uncertainty and produce zero QCMI for any c_j. For d>2, the condition generalizes to a discrete subgroup of the (d-1)-dimensional Cartan torus, but the explicit proof remains to be completed. For non-aligned Cartan axes, the Gram matrix factorization that underpins the proof is no longer exact, and the condition may be qualitatively different."

---

# Part VIII: 标注总结表

| # | 声张 | 原标注 | 诚实标注 | 关键裂缝 |
|---|------|--------|---------|---------|
| 1 | CFOL充要条件 | 推导 | **[定理]** | Cartan对齐+乘积态+d=2假设 |
| 2 | Reflux界 | 推导 | **[定理]** | 无（纯量子信息论） |
| 3 | Lemma S1 (熵恒等式) | 推导 | **[推导]** | Cartan对齐假设 |
| 4 | Gram矩阵因子化 | 推导 | **[推导]** | 乘积态假设 |
| 5 | QCMI(θ)标度律 θ²ln(1/θ) | 推导 | **[推导]** | 函数形式正确，绝对系数被低估~3.5× |
| 6 | Fawzi-Renner下界 η₀=1/(8ln2) | 推导 | **[推导]** | 环拓扑修正因子启发式 |
| 7 | 指针基=Cartan轴 | 推导 | **[推导+验证]** | 解析+数值双确认 |
| 8 | AG热激活证伪 | 推导 | **[定理]**（模型内） | C[G]模型的物理适用性待独立验证 |
| 9 | q_eq纯熵上界 | 推导 | **[定理]**（数学内） | 物理系统E(q)是否可忽略 |
| 10 | **有效度规 ds²=-q²dt²+q⁻²dx²** | **推导** | **[ansatz推导]** | **折射率类比n∝1/q不由公理强制** |
| 11 | **牛顿引力 ∇²Φ=4πGρ** | **推导** | **[校准]** | **G通过匹配经典引力确定** |
| 12 | **GW 2PN偏差~4%** | **推导** | **[ansatz推导]** | **完全依赖有效度规ansatz+RG流** |
| 13 | **等效原理 m_grav=m_inert** | **推导** | **[定义]** | **两者均正比于A，定义了等同性** |
| 14 | **F=ma** | **推导** | **[推导+校准]** | **F∝ma推导，等式系数1校准** |
| 15 | **薛定谔方程** | **推导** | **[ansatz推导]** | **连续极限下恢复，非独立推导** |
| 16 | **SU(2)/Cartan门** | **推导** | **[框架选择]** | **选择而非推论** |
| 17 | **信息视界 q→0** | **推导** | **[ansatz推导]** | **折射率类比+拥堵类比** |
| 18 | **β=1/𝔩** | **推导** | **[ansatz推导]** | **β∝𝔩推导，系数1是选择** |
| 19 | 黑洞熵面积律 S∝A | 推导 | **[推导]**（标度） | 严格min-cut |
| 20 | 黑洞熵 S_DGF/S_BH=系数 | 推导 | **[校准]** | 依赖饱和猜想+lattice spacing |
| 21 | DESI w(z)非单调性 | 推导 | **[ansatz+校准]** | ξ(q)现象学+H6/H10裂缝 |
| 22 | Lorentzian号差涌现 | 推导 | **[推测]** | Čencov-Petz仅证Riemannian唯一性 |
| 23 | 因果DAG本体 | 无 | **[框架选择]** | 排除连续流形本体 |
| 24 | ≤1比特/顶点 | 无 | **[工作假设]** | d=2选择非必然 |
| 25 | Cartan边酉 | 无 | **[框架选择]** | 排除了三体/规范相互作用 |
| 26 | 乘积环境态 | 无 | **[工作假设]** | 凝聚态环境中不成立 |
| 27 | 两时间结构 | 无 | **[ansatz推导]** | τ_intra/τ_inter耦合待定量化 |

---

# Part IX: 诚实性热力图

按声张类型和层级可视化DGF的诚实性全景：

```
声张层                    [定理] [推导] [ansatz推导] [校准] [框架选择/工作假设]
═══════════════════════════════════════════════════════════════════════════════
CFOL充要条件                ████
Reflux界                   ████
Lemma S1                            ████
Gram因子化                           ████
QCMI标度律                          ████
FR下界 η₀                            ████
指针基                               ████
AG证伪                    ████
q_eq上界                  ████
───────────────────────────────────────────────────────────────────────────
有效度规                                       ████
牛顿引力                                                 ████
GW 2PN修正                                     ████
等效原理(定义)                                                     ████
F=ma                                                    ████
薛定谔方程                                     ████
SU(2)门                                                        ████
信息视界                                        ████
β=1/𝔩                                           ████
BH熵标度                             ████
BH熵系数                                                 ████
DESI w(z)                                      ████       ████
Lorentzian号差                                 ████
═══════════════════════════════════════════════════════════════════════════
底层本体论                                                          ████
  (DAG+qubit+Cartan+乘积态)
```

**关键观察:**
- DGF的定理层（T1, T2）是真实的定理，但其适用范围被框架假设严格限定
- 所有与引力/宇宙学的接触点至少承载一个ansatz或校准
- 没有任何宇宙学预言达到[推导]级——它们都在[ansatz推导]或[校准]层
- 框架选择层的5个工作假设（A1-A5）承载了整个推导大厦

---

# Part X: 方法论教训

## X.1 诚实标注为什么重要

1. **区分"我们证明的"和"我们选择的":** 将框架选择标注为[推导]会制造虚假的必然性——暗示"任何理性的人从信息论出发都必然得到DGF"，而事实上不同的框架选择会产生不同的理论。

2. **区分"理论预言"和"校准输出":** 将校准标注为[推导]会制造虚假的预言——G不由DGF推导，由匹配经典引力确定。将它包装为"预言"是不诚实的。

3. **保护可检验性:** 将ansatz标注为[推导]会使理论不可证伪——因为ansatz的失败会被解释为推导错误而非框架错误。诚实的ansatz标注确保：若预言被证伪，ansatz被否定。

## X.2 DGF论文的诚实叙事弧

```
[框架选择] → [定理] → [ansatz推导] → [实验/观测检验]
 "我们选择      在这些选择     在此ansatz下     这些预言
  这些假设"     下我们证明      我们预言         可被检验"
                了这些定理      了这些效应
```

**关键点:** ansatz推导的结果如果被实验否定，可能意味着ansatz错误而非框架错误。但如果所有的ansatz推导都被否定而定理层存活，框架可能仍保有价值——定理层（CFOL, Reflux界）可独立于宇宙学/引力而存在。

## X.3 对审稿人的诚实声明

> "DGF is a framework built on explicit working hypotheses [框架选择, 工作假设]. Within these hypotheses, certain results are mathematically rigorous [定理, 推导]. The framework's contact with gravitational physics involves an additional heuristic ansatz — that local information density acts as an effective refractive index [ansatz推导] — which is testable but not derivable from the axioms. Newton's constant G enters through calibration to the weak-field limit, not through derivation [校准]. We present the framework with these distinctions clearly marked, so that its successes and failures can be correctly attributed."

---

# 附录: 终审发现的系统性包装模式

终审发现的9个系统性包装错误呈现一致模式：**将"选择/ansatz/校准"包装为"推导"**。这不是个别疏忽，而是系统性偏向——框架倾向于将其建构呈现为必然推论。

| 模式 | 频次 | 例 |
|------|:---:|-----|
| ansatz→derivation | 5 | 有效度规, GW, 信息视界, 薛定谔, β=1/𝔩 |
| calibration→derivation | 2 | 牛顿引力, F=ma |
| definition→derivation | 1 | 等效原理 |
| framework choice→derivation | 1 | SU(2)/Cartan |

**修正策略:** 本文档的诚实标注体系应作为DGF所有后续论文的强制预审步骤。

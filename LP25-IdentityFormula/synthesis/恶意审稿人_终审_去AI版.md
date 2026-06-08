# 恶意审稿人终审：去AI重构版

**审稿对象**: `投稿包/main_humanized.tex` + `投稿包/Supplemental_Material.tex`
**审稿角色**: PRD终审恶意审稿人（最后一次拒稿机会，不得手软）
**审稿日期**: 2026-06-03
**背景**: 论文经历4轮自审+3轮AB修正，上一轮编辑给Major Revision（5项必须修正）。作者声称全部解决。本审稿验证这些声称。

---

## 总评（Bottom Line）

**推荐：拒稿 (REJECT)**

这稿子比上次好。但不等于它够格进PRD。作者做了大量修补工作——Supplemental Material从完全不存在变成了存在；Theorem 2的split-complex/dual排除加上了；实验时间估计从"不存在"变成了"有数字"；退相干理论的引用加上了。问题在于：这些修补是**量的累积**而非**质的跃迁**。核心逻辑问题（Theorem 2的论证预设i、诊断表的逻辑不一致、方差定义模糊）依然留在终稿里——不是措辞降级可以解决的。

下面逐武器攻击。每一项都标注严重性。最后给出拒稿理由。

---

## 武器1: 数学严格性

### A1. Theorem 2仍是变相循环 —— **致命**

**攻击目标**: Section III, lines 56-73

论文现在诚实地承认了（line 72）"The Heisenberg equation contains i, and our derivation of Eqs. (2) used i in the separation step." 但这句话是一颗炸弹——它承认了论证的起点含i。然后论文声称"the claim is more specific: once the real canonical conjugate structure of Eq. (2) is recognized, the necessity of complex numbers for describing the resulting diagonalized dynamics follows..." 

问题：如果你从含i的方程出发，分离实虚部得到两个实方程，然后发现这两个实方程的演化矩阵有纯虚特征值——你"发现"的复数结构来自哪里？来自你在第一步分离掉的i。这不是"发现了复数的必然性"——这是"展示了i在实数表示中会重新出现"。这是恒真命题。

类比：你可以从`e^{iωt}`出发，分离`cos(ωt)`和`sin(ωt)`，建立两个实微分方程`dx/dt = -ωy, dy/dt = ωx`，说它们的演化矩阵`[[0,-ω],[ω,0]]`不能在对实数域上对角化——因此"复数是被逼出来的"。这是对的，但也是什么都没说——因为你的起点`e^{iωt}`已经预设了复数。

论文试图通过引入split-complex和dual numbers的排除来增加新颖性。但如果起点就没有i（即如果你从纯实数动力学出发），你得到的演化矩阵的特征值不会是±iω——它们会是某种实数特征值，不需要复数来对角化。

**结论**: 这不是措辞问题——这是逻辑结构问题。论证从含i的起点出发，声称"逼出了"i。这是循环。论文的诚实承认（"Heisenberg equation contains i"）反而让这个循环更加显眼。

**如果我是编辑**: 我会说"要么你从纯实数假设出发（比如实数Hilbert空间+辛结构）证明i的必要性；要么你诚实地说你展示的是'含i的理论在实数表示中需要i来对角化'——后者是平凡的，不够PRD。Stueckelberg (1960)从实数辛结构推导i的路径已经做了这件事。"

---

### A2. |Z|² = (C^R)² + (C^I)²这个模方的选择 —— **严重**

**攻击目标**: Theorem 2 proof, lines 66-69

论证中排除split-complex和dual numbers的关键是：它们不守恒|Z|² = (C^R)² + (C^I)²。但论文从来没有证明**为什么**这个特定的欧几里得模方是"正确的"模方——而不是Minkowski型(C^R)² - (C^I)²或其他二次型。

问题可以用两句话堵上：|⟨c†c⟩|² ≤ 1来自费米子代数的谱有界性，这个有界性要求二次型是正定的，因此排除(C^R)² - (C^I)²（它可以是负的或无界的）。但**论文里没有这两句话**。论证跳过了这一步，隐含地假定欧几里得模方是正确的——而欧几里得模方正是复数模方的定义。所以你用"必须守恒复数模方"来"证明复数必须被使用"——这是循环的另一面。

Reviewer 6 (S4) 已经指出了这个缝隙并要求"增加一行模方-费米子代数的连接"。论文没有加。

---

### A3. ΔC^R = ΔÂ/2 "exact for Gaussian states" —— **严重（定义性混淆）**

**攻击目标**: Section IV, line 95

论文写道:"ΔC^R = ΔÂ/2, ΔC^I = ΔB̂/2, exact for Gaussian states where Wick's theorem holds; the non-Gaussian correction is treated in the Supplemental Material [SM]."

审稿人4已经指出：如果ΔC^R被定义为算符Ĉ^R ≡ (ĉ†_n ĉ_m + h.c.)/2的量子涨落，那么ΔC^R = ΔÂ/2对所有态是**精确恒等式**——不需要Wick定理，不需要Gaussian假设。这是一个因子的缩放：Δ(cX) = |c|ΔX对任何Hermitian算符X和实常数c成立。

如果ΔC^R的含义是别的什么（比如C^R作为随机变量的统计方差），那它就不是算子涨落，需要完全不同的定义——论文没有给出。

**论文的"Gaussian假设"是对推导而言完全不必要的**——不等式的推导只需要Robertson关系+对易子，这两步都不需要Gaussian性。"Gaussian假设"只在你需要从实验数据计算ΔC^R时才会出现——因为计算⟨(Ĉ^R)²⟩涉及四费米子期望值，Wick定理允许用二点关联函数表达四点关联函数。

这是定义层面的混淆，且**没有被修正**。Response Letter声称"Clarified ΔC^R definition; corrected role of Assumption A3"——但在`main_humanized.tex`中，line 95仍然写着"exact for Gaussian states"。修正在哪里？

---

### A4. "Purely imaginary"只对非对角元成立 —— **中等**

**攻击目标**: Section II, line 45

"[h, C^R] is real antisymmetric; multiplied by i, this gives a Hermitian matrix whose off-diagonal elements are purely imaginary."

这句话是对的：反对称矩阵的对角元是零，乘以i后对应对角元为零（实数）。所以"purely imaginary"确实只对非对角元成立。论文明确写了"off-diagonal elements"，因此技术上是精确的。

问题在别处：这种"实虚分离"依赖于h和C^R都是实矩阵的假设。在一般的单粒子基下（含自旋轨道耦合、磁场等），h不是实矩阵。论文承认了这一点（"for complex h, see SM"）但没有强调这个限制——对大多数读者来说，"purely real"这种措辞的含混性容易造成误解。

严重性较低，因为它最终可以被精确化。但论文没有在正文中给出精确化的条件。

---

## 武器2: 实验可行性

### B1. Table I诊断逻辑与System 3正文不一致 —— **致命**

**攻击目标**: Table I vs. Section V System 3

这是本轮审稿发现的最严重问题。Table I第四行:

| Violation pattern | Failing | Physical origin | Candidate system |
|---|---|---|---|
| $C_J(\omega,\omega') \neq 0$, $\omega \neq \omega'$ | (A2)+(A3) | $\mathcal{J}=0$ constraint | BEC analogue BH |

Table I将C_J ≠ 0归类为一种**违反**——即不等式不成立，因为(A2)或(A3)失败，"物理起源"是J=0约束。

但Section V System 3（line 132-139）的论述方向完全相反：C_J ≠ 0是J=0（信息守恒）的**信号**，不是违反。J=0意味着全局纯态 → 辐射非对角 → C_J ≠ 0。这不是任何假设的"违反"——恰恰相反，它展示的是**信息被守恒了**。

SM S10节清楚地写明："C_J(ω,ω') ≠ 0 ⇒ ¬(A2) ∨ ¬(A3)"的逻辑是：因为J=0约束在全局层面修改了(A2)（辐射子系统本身的幺正演化不够——全局纯态约束修改了辐射的约化动力学），并且打破了(A3)（辐射的约化态由于与内部的纠缠而非Gaussian）。

**但这是完全不同的逻辑**：J=0不是"让不等式失败的机制"——J=0是一个**额外的物理原则**，它预测了标准半经典计算（即没有J=0的计算）会得出C_J = 0，而包含J=0的计算会得出C_J ≠ 0。C_J ≠ 0的观测确认的是J=0（信息守恒），而非否定(A2)+(A3)。在标准半经典图像中（无J=0），(A2)和(A3)对辐射子系统是成立的——辐射是热态，C_J = 0——不等式成立。在有J=0的图像中，C_J ≠ 0不意味着任何假设被"违反"——它意味着你需要扩展(A2)+(A3)的适用范围以包含全局纯态约束。

**Table I需要完全重写，或者System 3的行需要完全重新解释。** 目前两者在逻辑上是互斥的。

---

### B2. 81-setting tomography: 线性反演不保证正定性 —— **严重**

**攻击目标**: Section V System 2, line 130

论文现在说:"With linear inversion tomography, the density matrix element error scales as σ ≈ √(d/N_total) for d = 15 parameters, requiring N_total ≈ 1.5 × 10^7 total shots."

线性反演tomography的问题是：它在重构的密度矩阵中不强制正半定性。对于接近边界的态（如高纯度NESS），线性反演经常产生非物理的密度矩阵（负特征值）。实际的量子态层析使用最大似然估计（MLE）或贝叶斯方法，这些需要迭代优化，远比简单的矩阵逆运算慢。

论文没有提到这一限制。Hradil (1997, Phys. Rev. A 55, R1561) 以及 Banaszek et al. (2013, Nature Photonics 7, 870) 是标准引用。4量子比特、256个参数的MLE需要数值优化——每次迭代O(256³)的矩阵运算——实际运行时间远超过"7秒纯测量时间"。

**此外**，Response Letter声称用3^4 = 81个设置替代4^4 = 256个。这个声称是对的——信息完备的Pauli测量只需要X/Y/Z三个基（而不是包含I的四个）。但3^N个设置只能通过线性反演重构（因为测量不是tomographically complete in the strict sense——3^N < 4^N-1 when N=4: 81 < 255）。**线性反演的密度矩阵有81个自由度，但一个4量子比特密度矩阵有255个实自由度**。信息是不完备的。除非你施加额外的约束（如低秩、Gaussian性等），否则重构的态不是唯一的。

论文既声称使用线性反演（81个设置），又声称精度σ ≈ √(d/N_total) with d=15。d=15是4量子比特密度矩阵的实自由度...等等。对于4量子比特：4^4 = 16维密度矩阵，实自由度 = 16² - 1 = 255。d=15怎么来的？15是16-1维密度矩阵的参数个数如果密度矩阵是实数且迹为1...这是不可理喻的。

**我怀疑d=15来自某种降维假设**（比如只考虑关联矩阵而非完整密度矩阵）。论文需要明确这个数字的来源。

---

### B3. BEC实验可行性: 乐观情景是330小时, 不是2.8小时 —— **严重**

**攻击目标**: Section V System 3, line 138

主文本说:"In an optimistic scenario... the integration time for 3σ detection is approximately 2.8 hours."

看Supplemental Material Table S?? (BEC_3sigma): 悲观情景330小时，乐观情景2.8小时，增强情景10分钟。悲观和乐观之间的差距是两个数量级（因素120）。

"乐观"在这里是什么意思？SM说的是: R_CJ中心值8.8×10^-4时需330小时；R_CJ被推到5×10^-3时需2.8小时；T_H被提升到20 nK时需10分钟。这(R_CJ = 5×10^-3)是怎么来的？SM Table S1给出的总系统学范围是[0.15, 6.0]，即R_CJ = [0.01%, 0.5%]。5×10^-3 = 0.5%是系统学范围的**上界**。但上界是"所有系统学误差都往同一个方向偏"的极端假设——这在统计上不应该被称为"乐观"，而应被称为"最好可能情形但概率极低"。

更诚实的方式：报告中心值（330小时）和90%置信区间上界（~20-30小时？），并明确"2.8小时"只是如果每个系统学源都取最佳值时的情形。

**我注意到主文本没有提到330小时这个数字。** 这虽然不是虚假陈述（因为明确写了"optimistic scenario"），但隐瞒了核心估计——这是**选择性报告**。

---

### B4. QPC交叉噪声到C^R/C^I的映射 —— **中等**

**攻击目标**: Section V System 1, lines 126-127

"the in-phase component giving C^R and the quadrature component—accessible through small magnetic field modulation of the Aharonov-Bohm phase—giving C^I."

SM S6节给出了具体的关系式（Eqs. S12-correlation, CR_extract, CI_extract）。但主文本的这句话是一个结论性陈述——没有给读者任何关于"how"的信息。PRD Letter的读者会问：磁场调制如何隔离出C^I？QPC交叉噪声S_{12}(ω)测的是⟨I_1(t)I_2(0)⟩ ~ |t|²⟨c†_1 c_2⟩ + c.c. = 2|t|²C^R。这里只有C^R。AB相位调制如何引入C^I？需要非平凡的推导。

具体关系在SM中，这是可以接受的。但主文本至少应该引用SM的具体章节并给出一个简化的关系式。

---

## 武器3: 叙事与先发

### C1. Goyal 2009区分已做，但"surprise"不足 —— **中等**

**攻击目标**: Section I, line 28

论文现在区分了三条路径：Goyal 2009（对称性→复数）、de Oliveira 2023（正则变换→复数）、Renou 2021（操作测试→复数vs实数QM）。论文声称自己的路径是：动力学+幺正性（从正则共轭矩阵的不可对角化→唯一选择C）。

这个区分的措辞是诚实的，引用的位置（Introduction末尾）也是合适的。问题不在于区分是否成立——而在于即使成立，这个增量是否足以支持PRD的novelty标准。

在量子基础领域，复数的必要性已经被多角度论证过（Goyal的对称性路径、Stueckelberg的辛结构路径、de Oliveira的正则变换路径）。论文加了一条动力学路径——技术上有增量，但概念上没有新结论。"C是唯一最小的动力学充分代数"这个结论，与"量子力学需要复数"这个17年前已知的结论，在概念层面是相同的。

**如果审稿人咬住这一点**（Surprise不足），论文需要展示动力学路径产生了独特的、其他路径不能产生的物理后果。论文试图用预言A和B来做这件事——但这些预言不依赖"i是被逼出来的"声称（预言A只需要费米子代数+Robertson，预言B只需要J=0+BdG）。"复数必然性"和"实验预言"之间的叙事连接是论文最强的卖点，但也是最容易被攻击的软肋。

---

### C2. "Phase-discard gap"的残影 —— **中等**

**攻击目标**: Section I, lines 22-24

论文区分了P1（phase-discard problem）和P2（outcome-uniqueness problem），并说"This Letter addresses (P1)."

审稿人3之前批评了(P1)不是量子基础文献中公认的独立"gap"。论文现在加了一句与退相干理论的对话："Decoherence explains why superpositions become effectively classical... What we add here is a different kind of question. Not how coherence disappears from the system—that much is understood. But where it goes."

"Where it goes"这个问题的答案是什么？退相干理论的答案是：相位信息流入环境。论文提出的替代答案是：可以被J守恒律追踪。但J在BEC以外的系统中没有操作性定义（见D1）。如果J不能被独立测量，"where it goes"就不是一个可操作性的问题——它是一个修辞框架。

论文的Discussion段（line 148）诚实地承认了"we have not solved the measurement problem in its outcome-uniqueness sense"——但"we have solved P1"的隐含声称（通过"this Letter addresses P1"）仍然存在于Introduction中。要么P1是一个真实的问题（需要解决），要么它是被构造出来的（不需要解决）。论文在两个立场之间摇摆。

---

## 武器4: 一致性

### D1. [重复] Table I vs. System 3不一致 —— 见B1

这是本轮审稿最严重的单一问题。不再重复。

---

### D2. 85,639态验证: "随机采样"与"参数扫描"的矛盾 —— **中等**

**攻击目标**: Section II, line 54; Section IV, line 120

论文说"randomly sampled states across L = 2,4,6,8 (ground states and boundary-driven NESS, with parameters J∈[0.1,5.0], α∈[0.5,3.0])"。

"randomly sampled"暗示从态空间均匀采样。"with parameters J∈[0.1,5.0], α∈[0.5,3.0]"暗示从参数空间采样然后解出对应的态。前者是态空间随机覆盖，后者是参数扫描。两者不是同一回事。

对于L=8费米子链，关联矩阵的实自由度约为64维。参数扫描（2-6个参数）产生的是64维空间中的一个极低维度的子流形。说"85,639个随机采样的态"在技术上不准确——它们是"85,639个通过参数扫描生成的态"。

论文现在已经诚实地将验证定位为"consistency check"而非"null hypothesis test"（line 54: "This verification is not a discovery—it is a consistency check that confirms the algebra is correct."）。这是好的修正。但"randomly sampled"的描述仍然不准确。

---

### D3. Response Letter vs. main_humanized.tex 内容鸿沟 —— **严重**

**攻击目标**: 整体一致性

Response Letter声称做出了约15项修改（见Response Letter Section F），包括:
- "Added Section VI.A (What We Do Not Claim)" 
- "Added Section VI.B (Relation to Decoherence Theory)" 含三级分析
- "Added extended Gleason discussion"
- "Added explicit non-circularity statement in Introduction"

但在`main_humanized.tex`中:
- "What We Do Not Claim"被缩减为Discussion段中的3句话（line 148）
- 退相干理论对话被缩减为Introduction中的2句话（line 24-25）+"its disappearance is forced by a quantitative constraint"（line 24）
- Gleason被缩减为line 148的一个括号提及："Gleason proved uniqueness in 1957"
- 没有"explicit non-circularity statement"

**这不是说论文错了**——而是说Response Letter中声称的修改幅度和实际稿子中的修改幅度之间存在显著差距。如果编辑对比Response Letter和实际稿子，会发现很多"已添加"的内容其实只是被缩成了一句话。

这是否构成致命问题取决于：Response Letter是给编辑看的（编辑可能不会逐句比对），还是给审稿人看的（审稿人会比对）。如果是后者，审稿人会认为作者在Response Letter中夸大了自己的修改程度。

---

## 武器5: 未回应的先前批评

### E1. J^μ_G在BEC中仍无操作性定义 —— **致命（对System 3的可检验性）**

**攻击目标**: Section V System 3, line 134

审稿人5（量子引力）的核心批评是: J^μ_G在BEC类比黑洞中没有独立操作性定义。没有这个定义，J=0在BEC语境中要么退化为dS_vN/dτ = 0（标准QM幺正性的重述），要么是一个不能独立检验的等式（你用未知量定义未知量）。

论文现在说（line 134）:"The J=0 constraint—the requirement that the global quantum state remain pure, enforcing information conservation—generically produces entanglement between radiation modes at different frequencies." 

这翻转了物理方向（C_J ≠ 0现在意味着信息守恒而非信息丢失），但没有解决操作性定义的问题。J仍然被引用为C_J ≠ 0的理论来源，但J本身在BEC中不能被独立测量。

SM S4.4节试图补上定义链：J=0 → 全局纯态 → Schmidt分解 → 辐射约化态非对角 → C_J ≠ 0。但第一步（J=0 → 全局纯态）依赖于"J=0"这个等式的物理有效性——而J的每个分项（dS_vN/dτ, ∇_μ J^μ_G）在BEC中没有独立操作性定义。J^μ_G仍然是从Jacobson (1995)借来的概念，而Jacobson的框架是为时空几何设计的——在声学类比几何中，J^μ_G的物理对应物没有建立。

**Barcelo, Liberati, Visser (2011)**（论文引用的类比引力综述）明确说类比系统只模拟运动学（波方程、色散关系），不模拟动力学（Einstein方程）。Jacobson的J^μ_G是动力学的（它与Einstein张量成正比——这是Jacobson的推导核心）。在只有运动学的类比系统中，J^μ_G的定义基础不存在。

**如果我不能独立测量J^μ_G**，那"J=0"就不是一个可检验的方程——它是用未知量确认未知量。C_J ≠ 0是一个凝聚态物理的独立发现（BdG非对角关联），但声称它"检验了J=0"是没有独立操作性基础的过度声称。

---

### E2. Wick breakdown vs. "新物理"的诊断混淆 —— **严重（未被修正）**

**攻击目标**: Table I, line 111 ("Violation only at strong driving → (A3) Wick breakdown")

审稿人4（数学物理）和审稿人2（凝聚态实验）都指出：Table I中的"A3 Wick breakdown"诊断可能不是"新物理"——Wick定理在强驱动下失效是标准量子力学内部的现象。如果正确计算了四阶cumulant修正（η_R），使用完整公式（而非Gaussian近似），不等式应该仍然成立。表观违反来自使用了近似方差公式——不来自基本物理假设的失效。

Response Letter Section C.2声称修正了这个问题：
> "Type A3 violation (apparent): using the Gaussian formula when κ ≠ 0 leads to an apparent violation. Measuring the full four-point function removes this apparent violation. This is not 'new physics' but a quantitative map of Wick breakdown."

但在`main_humanized.tex`的Table I中，我看到的仍然是原始的分类："Violation only at strong driving → (A3) Wick breakdown." 没有任何措辞区分"apparent violation from Gaussian approximation"和"genuine violation from modified (anti)commutation"。

这个修正**没有出现在正文中**。如果审稿人只看投稿稿不看Response Letter（这通常是审稿流程），他们会看到同样的老问题。

---

### E3. 与退相干理论的对话仍然只是引用+一句话 —— **严重（未被完全解决）**

**攻击目标**: Introduction, lines 24-25

审稿人3（量子基础）的核心批评是论文没有与退相干理论（Zurek's einselection, quantum Darwinism）进行实质性对话。论文现在在Introduction中加入了两句话（line 24-25）和Discussion段的若干内容，引用了Zurek 2003, 2009和Joos-Zeh 1985。

但"对话"不是引用。"对话"应该包含：
1. Zurek的einselection如何产生优先基并在此基下消除密度矩阵的非对角元（这正好是C^I衰减的机制）
2. 论文的不等式如何在这种情况下仍能成立（开放系统的扩展）
3. 量子达尔文主义如何解释信息冗余编码（这与论文的"信息追踪"有概念重叠）

Response Letter Section E.3确实给出了一段扩展讨论（三个层次的分析），但**这段文字不在`main_humanized.tex`中**。主文本的Introduction只有两句话，Discussion段没有专门的退相干讨论子节。

对于一个声称"quantifies the phase-discard structure"的论文，与退相干理论的实质性对话是必要成分，而非可选添加项。

---

### E4. 完整的误差分析只在SM中 —— **可接受但需标记**

这是武器2审稿人2（凝聚态实验）最核心的批评：完整的误差分析缺失。SM S6-S9节现在提供了详细的统计和系统误差分析。这解决了审稿人2的Finding 4。

但主文本中，三个实验系统的误差描述仍然极其简短。对于声称"可实验证伪"的论文，至少应该在主文本的每个实验系统中给出关键误差数字（目标信号量级、主要系统误差源、预期达到的σ阈值）。目前这三个数字在正文中没有出现——全在SM中。

PRD允许关键推导放在SM中，但通常要求核心结果（包括误差估计）可以在主文本中独立评估。

---

## 综合判断

### 最致命的五个问题（排序）

1. **【致命】Table I诊断逻辑与System 3正文不一致**: C_J≠0在Table I中是"违反"（(A2)+(A3)失败），在正文中是"信号"（J=0成立，信息守恒）。这两个方向是互斥的。这是本轮审稿发现的**新问题**——之前的审稿可能没有注意到这个矛盾，因为之前的Table I版本不同。

2. **【致命】Theorem 2的变相循环**: 论文承认了起点含i但仍然声称"逼出了"i。这不是措辞问题——这是逻辑结构问题。更加诚实的位置是："我们展示了在含i的量子力学中，关联矩阵实虚部动力学只能在C上对角化——这说明自然选择C（而非split-complex或dual numbers）是动力学结构的结果。"这个措辞与当前声称的距离是质的不同。

3. **【致命】Response Letter声称的修改幅度 vs. 实际稿子的内容鸿沟**: Response Letter声称的"Section VI.A (What We Do Not Claim)", "Section VI.B (Relation to Decoherence Theory)", "Extended Gleason discussion"等都不在`main_humanized.tex`中（或只被缩成一句话）。如果编辑对比两个文档，会发现显著的不一致。这是诚信问题。

4. **【严重】A3 Gaussian假设的角色混淆**: 论文仍说ΔC^R = ΔÂ/2 "exact for Gaussian states"——但这是一个对所有态都成立的算子恒等式。Gaussian假设对不等式的**推导**是不必要的——它只在实际计算方差数值时需要。这个混淆被审稿人4明确标记为需要修正，Response Letter声称已修正，但正文中没有修正。

5. **【严重】J^μ_G在BEC中无操作性定义**: 审稿人5将此标记为"致命"。论文没有提供J^μ_G在BEC类比系统中的独立操作性定义。由于J^μ_G是从Jacobson的时空几何框架中借用的概念，而BEC类比系统只模拟时空几何的运动学而非动力学（Barcelo et al. 2011的明确结论），J^μ_G在BEC中的定义本质上是未被建立的。没有独立操作性定义，J=0在BEC中不能作为可检验的物理假设——它只能作为启发式概念框架。

### 拒稿理由（如果你只能拒一次）

我会这样写：

> This manuscript has been through substantial revision and the authors have made genuine progress on several fronts. The Supplemental Material now contains a detailed BdG derivation and error analysis that partially address earlier experimental feasibility concerns. The inclusion of split-complex and dual number exclusion in Theorem 2 is a meaningful improvement.
>
> However, I recommend rejection for a single, decisive reason that cannot be addressed through further revision: **the paper's diagnostic logic is internally inconsistent.** Table I classifies $C_J(\omega,\omega') \neq 0$ as a "violation" caused by failure of assumptions (A2)+(A3), with physical origin attributed to the $\mathcal{J}=0$ constraint. Yet Section V, System 3 argues that $C_J \neq 0$ is a *signal* of $\mathcal{J}=0$---i.e., of information conservation, not its violation. These two claims are logically incompatible: $C_J \neq 0$ cannot simultaneously be evidence that assumptions (A2)+(A3) have failed AND that the $\mathcal{J}=0$ information-conservation principle holds. The authors must decide which diagnostic logic they mean and rewrite either Table I or Section V System 3 accordingly. This is not a cosmetic issue---it goes to the core of what the inequality is supposed to falsify and how each experimental system connects to the theoretical framework.
>
> Additionally, the central Theorem 2 argument---that complex numbers are "forced" by canonical conjugate dynamics---continues to presuppose the complex unit $i$ in its starting point (the Heisenberg equation). The paper's own acknowledgment of this fact (line 72) undermines rather than reinforces the claim. What remains is a demonstration that, *given* a dynamics already containing $i$, the real representation of that dynamics requires $\mathbb{C}$ for diagonalization---a statement that is mathematically correct but conceptually circular.
>
> I encourage the authors to resubmit after resolving the Table I/System 3 inconsistency and after either (a) providing a non-circular foundation for Theorem 2, or (b) significantly downgrading the claim from "complex numbers are forced" to "we identify the algebraic mechanism through which complex structure manifests in correlation dynamics." The Supplemental Material represents a substantial amount of good physics that deserves to see the light of day, but the manuscript in its current form is not internally coherent.

### 对作者的诚实建议

停止向这篇论文追加修补。问题的根源不在于缺少更多推导或更多引用——而在于**核心叙事骨架是反的**：

1. Theorem 2声称从实数方程"逼出"了i——但实数方程来自含i的Heisenberg方程的实虚部分离。骨架断了。
2. Table I说C_J≠0是违反的证据——但正文说C_J≠0是信息守恒的信号。骨架断了。
3. 不等式声称是量子力学的"必要条件"——但"必要条件"只是"推导结果"换了个名字。逻辑对但没分量。

好的科学在骨架层面是简单的。不等式ΔC^R·ΔC^I ≥ ¼|Δn|——这个结果本身就是一篇好论文的骨架。它不需要被包装成"我们在测试量子力学本身是否会崩溃"。它可以只是：我们发现了一个slick的不等式，它把不确定性关系的下界从常数变成了可观测量，这里是三个可以测它的实验系统。一篇诚实的6页PRD Letter——不需要Theorem 2（去掉），不需要J=0（留在SM作为动机），只需要不等式+实验靶点+诚实的误差分析。

当前的稿子把这个好的核心塞进了一个过于ambitious的外壳里。外壳在多个地方裂开了。我的建议不是修补裂缝——而是换一个更小的、更结实的外壳。

---

*恶意审稿人签署 | 2026-06-03*
*审稿依据: PRD五武器（数学严格性、实验可行性、叙事先发、一致性、未回应批评）*
*最终判定: REJECT* 
*核心拒稿理由: Table I与System 3诊断逻辑互斥 + Theorem 2变相循环 + Response Letter与正文修改幅度不一致*

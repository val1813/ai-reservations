# S2 B博士攻击：量子→经典过渡 = 欧拉恒等式的驻相条件

> 类型：B（异端派，攻击者）
> 日期：2026-06-03
> 父课题：LP25-S2
> 攻击对象：S2声称——量子→经典过渡 = e^(iS/ħ) = cos(S/ħ) + i sin(S/ħ) 在路径空间上的驻相条件

---

## 攻击总结

| # | 攻击维度 | 严重性 | 是否致命 | 理由 |
|---|---------|--------|---------|------|
| 1 | 这是标准驻相法，不是新框架 | 致命 | **是** | 驻相法自19世纪就是标准分析工具；Feynman & Hibbs (1965) 已在教科书中用完全相同的 cos+sin 分解解释经典极限 |
| 2 | 标准驻相法已经包含所有物理 | 致命 | **是** | WKB(1926)、驻相近似、loop expansion——所有这些都在1970年代前完成。欧拉分解没有增加任何这些工具不能给出的结果 |
| 3 | 先发文献搜索 | 致命 | **是** | 无人在文献中明确声称"量子→经典过渡 = 欧拉恒等式的驻相条件"，但这恰恰因为它是Feynman教科书的标准讲授内容——不是"新框架"，而是"过了专利期的标准叙述" |
| 4 | 焦散点预言是否真正新颖 | 高 | 否（可修正） | Maslov指数(1965)、Berry相位(1984)、catastrophe theory(Thom 1975, Berry & Upstill 1980)已完整处理δ²S=0的情况。欧拉框架需证明它给出这些已知框架不能给出的东西——目前没有 |
| 5 | "统一"框架统一了什么 | 致命 | **是** | 标准方法(WKB+驻相+loop expansion)已经是统一的了。把 e^(iS/ħ) 重写为 cos+sin 没有改变任何数学内容。像Maxwell统一电磁学那样产生新预言才算统一 |
| 6 | cos/sin振荡抵消是启发式图像，不是严格数学 | 高 | 否（可修正） | 对路径积分(无穷维)，严格驻相定理需要Malliavin calculus和无穷维振荡积分理论(Albeverio et al. 1977+)。欧拉分解没有解决这些严格的数学困难 |
| 7 | 可检验性——无独立可检验预言 | 致命 | **是** | 声称的独有修正(焦散点等)未被证明是标准方法不能给出的。S2北极星要求的"至少一个欧拉框架独有的可检验修正"未提供 |
| 8 | 身份的triviality——恒等式不能解释物理 | 致命 | **是** | e^(iθ)=cos θ+i sin θ 是数学恒等式——永远成立。用它"解释"量子→经典过渡犯了用恒等式解释物理的范畴错误。解释力来自驻相定理(分析学)，不是来自欧拉恒等式(三角学) |
| 9 | 退相干/consistent histories的欧拉叙述是隐喻不是推导 | 高 | 否 | S2第6步声称退相干=虚部被环境吸收→只剩cos θ。这是隐喻，没有给出任何退相干理论的数学推导 |
| 10 | 6个"最小数学对象"中，θ=S/ħ是唯一非平凡对象 | 致命 | **是** | e^(iθ)、cos θ、i sin θ、|e^(iθ)|²、i——5个都是欧拉恒等式的标准构件。θ=S/ħ是非平凡赋值，但它来自量子力学本身，不是来自欧拉框架 |

---

## 致命攻击详情

### 致命攻击1：这是Feynman教科书的标准叙述，不是新框架

**证据**：Feynman & Hibbs, *Quantum Mechanics and Path Integrals* (1965, McGraw-Hill)，第2章，约第28-29页：

> "Now if we move the path by a small amount dx, small on the classical scale, the change in S (the action), is likewise small on the classical scale, but not when measured in the tiny unit of reduced Planck's constant h. These small changes in path will, generally, make enormous changes in phase, and **our cosine or sine will oscillate exceedingly rapidly** between plus and minus values. The total contribution will then add to zero."

**分析**：Feynman在1965年已经用完全相同的 e^(iS/ħ) = cos(S/ħ) + i sin(S/ħ) 分解来解释经典极限。S2声称的"欧拉框架"就是Feynman的标准讲授内容。这不是新框架——这是Feynman路径积分教科书第二章的标准叙述。

**S2的北极星写道**："没有人用欧拉恒等式将它们统一为一个几何框架"——这句话是**事实错误**。Feynman本人（以及此后每一本路径积分教科书）都是用欧拉分解来统一解释的。Scholarpedia的"Path Integral"词条（Zinn-Justin, 2009）明确陈述：

> "When ħ is regarded as a small real-valued parameter which is allowed to converge to 0, the integrand e^(iS/ħ) behaves as a strongly oscillatory function and, according to a heuristic extrapolation of the stationary phase method to the path integral case, the main contribution to the integral should come from those paths which make stationary the phase functional S."

**结论**：S2声称的"没有人用欧拉恒等式将它们统一"是一个事实陈述错误。Feynman在1965年就这么做了。每一本路径积分教科书都这么做。这等价于声称"没有人用牛顿第二定律解释加速度"。

**严重性**：如果核心声称的优先性主张基于一个事实错误（"没有人做过"），则整个框架的"新意"是从未存在的真空里创造出来的。

---

### 致命攻击2：标准驻相法已经包含所有物理

**驻相法的历史**：驻相法（method of stationary phase）可追溯到Stokes (1856)和Kelvin (1887)。R. Wong *Asymptotic Approximations of Integrals* (Academic Press, 1989, 2001新版) 给出了完整的严格处理。

**路径积分ħ→0极限的历史**：
- Feynman & Hibbs (1965)：启发式驻相解释（含欧拉分解）
- Albeverio & Høegh-Krohn (1977)：无穷维振荡积分的严格驻相定理 — *Inventiones mathematicae* 40, 59-106
- Schulman *Techniques and Applications of Path Integration* (1981, Dover 2005)
- Kleinert *Path Integrals in Quantum Mechanics, Statistics, Polymer Physics, and Financial Markets* (1990, 2009第5版)
- Mazzucchi *Mathematical Feynman Path Integrals and Their Applications* (World Scientific, 2009)

**S2声称的新贡献**：
1. "路径积分 = 复平面单位向量的求和"——这是标准路径积分的定义
2. "ħ→0时cos和sin振荡抵消所有δS≠0的贡献"——这是Feynman 1965年的叙述
3. "仅δS=0处邻近向量的cos和sin对齐→经典路径存活"——驻相条件的几何解释，标准
4. "经典方程 = 对齐条件 δS=0"——欧拉-拉格朗日方程，标准
5. "量子修正 = i sin(S/ħ)在δS≠0处的系统性非振荡贡献"——这个表述有微妙的错误：量子修正（ħ≠0）来自整个 e^(iS/ħ) 围绕鞍点的展开，不是单独来自 i sin 部分。cos 部分也有非振荡贡献。标准展开是 e^(iS/ħ) 的整体 Gaussian 近似，不能分解为"cos贡献经典+sin贡献量子修正"——这种分解只在实部/虚部投影下成立，但没有独立的数学内容。

**结论**：S2声称的全部5个"新贡献"都是标准教材内容。S2没有给出任何这些已知工具不能给出的结果。

---

### 致命攻击3：先发文献搜索——"新框架"主张的真空不存在

**搜索1**："Euler formula stationary phase classical limit quantum"——返回Feynman & Hibbs (1965)的标准引用，无人声称"新框架"。

**搜索2**："cos + i sin classical limit"——同样指向Feynman标准叙述。

**搜索3**："Euler identity quantum classical transition"——返回矩阵推广论文(arXiv:math/0703448, Argentini 2007)，该论文将欧拉恒等式推广到Pauli矩阵，但不声称量子-经典框架。

**搜索4**："欧拉恒等式 量子经典过渡 驻相法"——中文搜索返回**零结果**。确认在中文文献中无人做过此声称。

**搜索5**：Zenodo预印本 "Reimagining the Imaginary" (2025) ——一个纯数学预印本，关于"相位提升"和"手性锁"，不涉及量子-经典过渡、路径积分或WKB。

**搜索6**："Euler identity quantum classical bridge framework" 在arXiv——零结果。

**判断**：确实没有人在文献中明确声称"量子→经典过渡 = 欧拉恒等式的驻相条件"。但这**不意味着它是新框架**——恰恰相反，这意味着它太标准了，以至于没有人会把它当作"新框架"来声称。Feynman已经在标准教科书中给出了完全相同的解释。把标准教科书内容包装成"新框架"是一种**优先性声称的新型错误**：不是发明了新东西，而是把标准叙述重新宣告为新发现。

**类比**：这等同于宣称发现了"牛顿第二定律其实是F=ma"——然后因为没有人明确说过"其实"而声称这是新框架。

---

### 致命攻击5："统一"框架统一了什么？没有新统一

**什么是真正的统一**：
- Maxwell统一电磁学→产生光速预言、电磁波的存在 → 可检验新预言
- 电弱统一(Weinberg-Salam)→产生W/Z玻色子质量关系 → 可检验新预言
- Dirac方程统一QM和狭义相对论→预言反物质 → 可检验新预言

**S2统一了什么**：把 e^(iS/ħ) 重写为 cos+sin，然后说"cos=经典，sin=量子"。这不是统一——这是**重标记**。WKB、驻相法、loop expansion在使用 e^(iS/ħ) 时不需要把它分解为 cos+sin——它们直接用复指数工作，因为复指数的代数性质比三角函数的代数性质更简洁。欧拉分解没有任何计算优势。

**标准方法的统一性**：WKB+驻相+loop expansion已经是统一的了——它们都是鞍点近似的不同形式。在复分析中，鞍点法（steepest descent）是驻相法的推广——它们统一在复平面的等高线变形框架下，远比实数轴的cos/sin分解更强大。把cos/sin分解说成"统一"是一种**概念倒退**：复数框架本身就是统一的（一个复指数统一了实部和虚部），再分解回实部和虚部是**拆散统一而非建立统一**。

---

### 致命攻击7：可检验性——无独立可检验预言

**S2北极星要求的独有可检验预言**（原文）：

> "3. 至少一个欧拉框架独有的可检验修正（焦散点？Maslov指数？）"

**现状**：S2北极星文档中没有提供任何这样的预言。焦散点处δ²S=0导致标准驻相法失效——这已经被以下框架完整处理：

- **Maslov指数**（Maslov 1965, Arnold 1967）：处理Lagrangian子流形投影的奇点，给出连接公式的全局相位修正
- **Berry相位**（Berry 1984）：参数空间中的几何相位，与焦散结构相交
- **Catastrophe theory**（Thom 1975, Berry & Upstill 1980 "Catastrophe optics: morphologies of caustics and their diffraction patterns", *Progress in Optics* 18, 257-346）：对光学焦散进行完全分类（fold, cusp, swallowtail, elliptic/hyperbolic umbilic），每一类有标准衍射积分（Airy, Pearcey等）
- **Kravtsov & Orlov** *Caustics, Catastrophes and Wave Fields* (Springer, 1999)：完整的专著，700+页

**欧拉框架声称的焦散点独特贡献**："cos和sin的贡献分离，导致可观测的干涉图样修正"

**评估**：cos和sin的贡献分离等价于实部和虚部分离。标准焦散衍射积分已经在做完全相同的计算——它们直接计算复振幅的衍射积分，实部和虚部自然地包含在内。欧拉框架的"贡献分离"没有给出新的可计算量。

**负荷性要求**：如果S2声称有独特的焦散点预言，它必须：(a) 给出新的解析公式，(b) 证明该公式与标准Maslov-catastrophe结果不同，(c) 证明差异在可测量量级。目前这三件事一件都没有做。

---

### 致命攻击8：身份的triviality——恒等式不能解释物理

**核心逻辑缺陷**：

e^(iθ) = cos θ + i sin θ 是一个**数学恒等式**——它对任意θ都精确成立，无论是在量子力学中、在电路分析中、在信号处理中还是在数论中。因为它是恒等式，所以**它不能解释为什么某个物理现象发生而不发生**。

**S2的逻辑结构**是：
1. 量子力学使用 e^(iS/ħ)（真）
2. e^(iS/ħ) = cos(S/ħ) + i sin(S/ħ)（真——恒等式）
3. 经典极限下 cos 和 sin 对 δS≠0 振荡抵消（真——但这是驻相定理的推论，不是欧拉恒等式的推论）
4. 因此"量子→经典过渡 = 欧拉恒等式的驻相条件"（**不成立**——第3步的成立是因为驻相定理，不是因为欧拉恒等式）

**关键区分**：
- 解释力来自**驻相定理**（分析学）：证明当频率参数→∞时，振荡积分的主要贡献来自相位函数的临界点
- 解释力**不来自**欧拉恒等式（三角学）：恒等式只是把复指数翻译成三角函数——这是翻译，不是解释

**范畴错误**：把恒等式的翻译功能（把 e^(iθ) 翻译成 cos+sin）当作物理解释功能（解释为什么经典物理浮现）。这相当于说"英文→中文翻译解释了莎士比亚为何伟大"——翻译没有增加任何新的理解。

**更强的表述**：如果欧拉恒等式真的提供了物理解释，那么任何使用 e^(iθ) 的物理理论都应该有相应的"欧拉解释"。但电路分析中的阻抗 Z = |Z|e^(iφ) 也可以写成 |Z|(cos φ + i sin φ)——我们从来不声称"交流电路的本质 = 欧拉恒等式"。因为恒等式不解释任何东西。

---

### 致命攻击10：6个"最小数学对象"中5个是欧拉恒等式的标准构件

**S2声称的6个最小数学对象**：
1. e^(iθ) = 量子态
2. cos θ = 经典可观测量
3. i sin θ = 量子相干
4. |e^(iθ)|² = Born规则+幺正性
5. θ = S/ħ = 相位=作用量/ħ
6. i = 量子力学的数学签名

**分析**：对象1-4和6是欧拉恒等式和复数的标准属性——它们在任何使用 e^(iθ) 的上下文中都成立。对象5（θ = S/ħ）是唯一的非平凡物理赋值，但它来自量子力学的路径积分公式（Feynman 1948），不是来自欧拉框架。

**问题**：S2声称这些对象构成了一个新的"统一框架"。但在标准量子力学中：
- 对象1：波函数/传播子 = e^(iS/ħ) ——标准
- 对象2：可观测量 = 波函数的模方/实部投影 ——标准
- 对象3：相干项 = 非对角元中的Im部分 ——标准
- 对象4：|e^(iS/ħ)|² = 1 = 幺正性 ——标准
- 对象5：S/ħ = 相位 ——标准
- 对象6：i 出现在Schrödinger方程中 ——标准

**S2没有定义任何新对象**。它只是把6个已知对象重命名为"欧拉分解构件"，然后声称这是新框架。这相当于把"汽车=引擎+轮子+方向盘+刹车+油箱+车架"说成是"汽车的新统一框架"——它既不是新的（这些部件本来就在那里），也不统一（它是在分解而不是统一）。

---

## 高严重性攻击详情

### 攻击4：焦散点预言——标准框架的已知内容

**问题**：S2声称"焦散点(δ²S=0)处欧拉框架给出标准驻相法不能给出的修正"

**标准框架已经给出的**：

1. **Maslov指数**（1965）：当路径穿越焦散时，WKB波函数的相位跳变π/2。Maslov指数给出全局一致的连接条件，不需要欧拉分解。

2. **Catastrophe diffraction integrals**（Berry & Upstill 1980）：每类焦散（fold, cusp, swallowtail等）有对应的标准衍射积分，给出了焦散附近的全波动光学解。这些解自然地包含了cos和sin的贡献分离——因为它们直接计算复振幅。

3. **均匀渐近近似**（uniform asymptotic approximation）：与标准驻相法不同，均匀近似在焦散附近给出处处适用的表达式，平滑地连接焦散两侧的振荡区和衰减区。Chester, Friedman & Ursell (1957) 发明了此方法，Berry (1966) 推广。

**欧拉框架需要证明的**：cos/sin分解在这些标准结果之上给出了什么新的预言？如果只是把标准衍射积分重写为cos+sin形式——这不是新预言，这是重写。

**具体挑战**：取fold caustic的标准Airy函数解：
```
Ai(-z) ~ π^{-1/2} z^{-1/4} sin(2/3 z^{3/2} + π/4)
```
这个 sin 来自 Airy 函数的渐近展开——它已经是"sin形式"了。欧拉框架是否需要引入"Airy函数 = cos/sin的某种重新组合"？如果是，这个新组合是否给出了与标准Airy解不同的数值结果？

**答复状态**：未提供。

---

### 攻击6：cos/sin振荡抵消——启发式图像，不是严格数学

**问题**：S2的推导使用了一个启发式论证：ħ→0时cos(S/ħ)和sin(S/ħ)剧烈振荡→积分为零。这是一个物理图像，不是严格数学。

**严格处理需要什么**：

1. **有限维**：Riemann-Lebesgue引理证明 ∫ f(x)e^(iλx)dx → 0 (λ→∞) 对 f∈L¹ 成立。但这要求相位函数是线性的。对非线性相位，需要驻相定理——它证明主要贡献来自临界点，非临界区域贡献为 O(λ^{-N})（通过分部积分获得任意阶衰减）。

2. **无穷维（路径积分）**：Riemann-Lebesgue引理和经典驻相定理都不适用于无穷维空间。路径空间没有平移不变的Lebesgue测度（Cameron 1960定理：没有 σ-可加测度能使Feynman路径积分成为Lebesgue积分）。

3. **Albeverio & Høegh-Krohn (1977)** 通过Parseval型等式定义了无穷维振荡积分——不是作为对测度的积分，而是作为有限维逼近的极限。

4. **Malliavin & Taniguchi (1997)** 通过复数化Wiener空间和无穷维Cauchy公式给出了更强大的工具。

**S2的论证水平**：S2使用的是Feynman (1965) 的启发式论证水平——对于物理教科书来说完全合适，但对于声称"严格数学"的框架来说不够。S2没有使用Malliavin calculus、没有讨论Wiener空间的复数化、没有处理非退化条件（δ²S非零时驻相法有效，δ²S接近零时需要单独处理）。

**这在物理上不是大问题**——Feynman的启发式论证在物理上是正确的。但是S2把"欧拉框架"当作比标准驻相法更严格的替代方案——而实际上它在严格性上没有任何进展，停留在和Feynman 1965完全相同的启发式水平。

---

### 攻击9：退相干的欧拉叙述——隐喻，不是推导

**S2第6步声称**："退相干选择指针态的过程 = 环境将不同指针态的 i sin θ（虚部、相干）扩散到无数自由度中。剩下的 cos θ（实部、概率）构成经典概率分布。"

**问题**：

1. **这不是退相干理论的推导**：标准退相干理论（Zurek 1981, 2003; Joos & Zeh 1985; Schlosshauer 2007）使用约化密度矩阵、环境影响泛函、Lindblad主方程。密度矩阵的非对角元衰减率由环境影响泛函的绝对值决定——它衰减的是 ρ_{ij} 的整体幅度，不只是 Im(ρ_{ij})。cos/sin的分解在标准退相干理论中不提供额外的计算工具。

2. **"cos θ 存活"说得不精确**：退相干后存活的是约化密度矩阵的对角元 ρ_{ii}（经典概率分布），不是 cos θ。在指针基下，ρ_{ii} = |c_i|² = (Re[c_i])² + (Im[c_i])²。cos 和 sin 都贡献给了经典概率——不是说 sin 被丢弃而 cos 存活。

3. **consistent histories不需要欧拉分解**：Griffiths (1984), Gell-Mann & Hartle (1990) 的consistent histories框架使用退相干泛函的实部条件（中川-石川条件），可以直接用复振幅工作，不需要分解为cos+sin。

**结论**：S2的退相干叙述是一个有启发性的**隐喻**——"虚部被环境吸收"——但不能替代退相干理论的严格数学推导。把它说成"欧拉框架的预测"是过度宣告。

---

## 存活的内核

在最诚实的评估下，S2中存在以下可能的非平凡内容：

### 1. 强调虚部(i sin θ)的角色作为量子相干的符号化标记

虽然 e^(iS/ħ) 的实部和虚部在标准框架中同样存在，但明确地把 i sin θ 标记为"量子相干的签名"、cos θ 标记为"经典概率的来源"——这种**符号化分类**可能有教学法价值，即使它在严格物理上没有增加新内容。

**局限**：这不是数学框架，是**叙事框架**。叙事框架有教学价值，但不应被宣告为物理发现。

### 2. 焦散点处cos/sin贡献分离

如果S2能将焦散点的标准衍射积分重新表述为cos和sin贡献的加权组合，并证明这种分解揭示了新的物理（例如：焦散两侧cos和sin的相位跳变不对称，导致可观测的偏振/干涉不对称性）——那么这可能是一个真正的贡献。

**局限**：这需要做出来，而不是声称"可能"。当前S2北极星中这一步完全是推测性的。

### 3. LP25大北极星语境中的系统性角色

在LP25的五个子命题中，S2作为WKB/驻相/ħ→0极限的组件有明确的逻辑位置。即使S2本身没有新物理内容，它作为LP25框架的一个**逻辑环节**（S1→S2→S3→S4→S5）扮演结构角色。

**局限**：逻辑环节不需要被宣告为独立发现。一个链条中的一环，如果这环本身就是标准材料，那么链条的价值来自整体的新连接，而不是单环的被重新发现。

---

## 最终判决

- [x] **彻底证伪** / [ ] 部分证伪 / [ ] 基本存活 / [ ] 完全存活

**判决理由**：

S2声称的核心主张（"量子→经典过渡 = 欧拉恒等式的驻相条件"）有五个构成要素：

| 构成要素 | 判决 |
|---------|------|
| 1. e^(iS/ħ) = cos + i sin 的分解 | 是欧拉恒等式，1748年已知 —— 不是新东西 |
| 2. 驻相条件(δS=0)选出经典路径 | 是驻相法，19世纪已知；Feynman(1965)在教科书中用相同的cos/sin叙述解释 |
| 3. 焦散点(δ²S=0)的独特修正 | 未提供具体公式；已知框架(Maslov+catastrophe)已完整处理 |
| 4. "统一几何-分析学基础" | 尚未建立任何标准框架中没有的统一 |
| 5. 独立可检验预言 | 未提供 |

**五个要素中，零个是新东西**。两个要素是18-19世纪的数学恒等式/定理，一个要素是Feynman(1965)的标准教科书叙述，两个要素尚未构建。

**核心理由（一句话）**：S2把Feynman 1965年教科书第二章的标准叙述重新宣告为"新框架"——这犯了优先性声称的新型错误：误把普遍已知的标准材料当作新发现。

---

## 修正建议

### 如果S2希望存活，必须满足以下最低条件：

1. **公开承认Feynman & Hibbs (1965) 的优先性**：Feynman在1965年已经用完全相同的cos+sin分解解释经典极限。任何关于此"框架"的讨论必须以此为出发点，且不能声称"没有人做过"。

2. **给出至少一个具体的、可检验的独有预言**：
   - 选一个具体系统（例如：一维双阱在焦散附近）
   - 用欧拉框架计算一个可观测量的预言值
   - 证明该预言与标准Maslov-catastrophe方法的结果在量级上不同
   - 给出实验检验的可行性评估

3. **放弃"新框架"的宣告，改为"重新强调"**：
   - S2可以合理地声称：虽然驻相法/欧拉分解是标准材料，但在教学和概念组织上对虚部角色的系统强调是新的
   - 这种"重新强调"的学术贡献要小得多，但它至少是诚实的

4. **修正"欧拉恒等式解释物理"的范畴错误**：
   - 明确区分：解释力来自驻相定理（分析学），不是来自欧拉恒等式（三角学）
   - 欧拉恒等式的作用是翻译（复指数↔三角函数），不是解释

5. **删除或严格限定退相干的欧拉叙述**：
   - 退相干不是"虚部被环境吸收"——这是隐喻
   - 如果要求此叙述有数学内容，必须给出从Lindblad方程到cos/sin分解的具体推导
   - 否则应将其标注为"启发式图像，非严格推导"

### 如果S2接受以上修正，它可以作为以下身份存活：

- **教学法创新**：以欧拉分解为中心重新组织驻相法/WKB/路径积分的教学叙述
- **LP25链条的逻辑环节**：不做独立声称，仅作为S1→S3之间的标准材料衔接
- **启发式框架**：明确标注为概念组织工具而非物理解释框架

在这些身份下，S2的学术诚实度是完整的，贡献（虽小）是真实的。

---

## 参考先发文献

1. Feynman, R.P. & Hibbs, A.R. *Quantum Mechanics and Path Integrals*. McGraw-Hill, 1965. Ch.2, pp.28-29. (经Dover 2010版确认)
2. Albeverio, S. & Høegh-Krohn, R. "Oscillatory integrals and the method of stationary phase in infinitely many dimensions." *Inventiones mathematicae* 40, 59-106 (1977).
3. Malliavin, P. & Taniguchi, S. "Analytic Functions, Cauchy Formula, and Stationary Phase on a Real Abstract Wiener Space." *J. Funct. Anal.* 143, 470-528 (1997).
4. Wong, R. *Asymptotic Approximations of Integrals*. Academic Press, 1989; SIAM, 2001.
5. Berry, M.V. & Upstill, C. "Catastrophe optics: morphologies of caustics and their diffraction patterns." *Progress in Optics* 18, 257-346 (1980).
6. Kravtsov, Yu.A. & Orlov, Yu.I. *Caustics, Catastrophes and Wave Fields*. Springer, 1999.
7. Schulman, L.S. *Techniques and Applications of Path Integration*. Wiley, 1981; Dover, 2005.
8. Kleinert, H. *Path Integrals in Quantum Mechanics, Statistics, Polymer Physics, and Financial Markets*. 5th ed., World Scientific, 2009.
9. Mazzucchi, S. *Mathematical Feynman Path Integrals and Their Applications*. World Scientific, 2009.
10. Zurek, W.H. "Decoherence, einselection, and the quantum origins of the classical." *Rev. Mod. Phys.* 75, 715 (2003).
11. Schlosshauer, M. *Decoherence and the Quantum-to-Classical Transition*. Springer, 2007.
12. Scholarpedia "Path Integral" entry (Zinn-Justin, 2009). http://www.scholarpedia.org/article/Path_integral
13. Argentini, G. "A matrix generalization of Euler identity e^(ix) = cos x + i sin x." arXiv:math/0703448 (2007).

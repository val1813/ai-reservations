# B博士 v4 Phase 1 作业: 近复不动点 β 函数计算方法——无交换对称性假设

**日期**: 2026-06-01
**角色**: 方法论搜索 + 跨域连接
**v3 输入**: {Q, C} = 0 反交换对称性; P3-A 完全重开; η 纯虚数

---

## ⚡ 本Phase推进了什么

本Phase建立了计算 β_I(x,0) 的已知方法论矩阵，识别了五个可直接借用的计算框架，并找到了两个关键的跨域桥梁：
1. **Faedo et al. (2021)** 的 β 函数广义形式精确覆盖 {Q, C}=0 可贡献的所有拓扑——该 β 函数的多cFP对结构与v3反交换约束的预测一致
2. **Jepsen-Klebanov-Popov (2021)** 的 "spooky fixed points" 提供了 Jacobian 复数本征值场景的最近似先例

**最关键的跨域连接**: v3 的反交换关系 {Q,C}=0 在 QFT 中没有直接先例——这是我们搜索的核心结论，意味着 DQCP-Complex 正在进入未被探索过的理论空间。但**方法学上**，GRZ、Faedo、LeClair 的框架都已经准备好适应这种对称性结构。

**预测 vs 实际**: 预测 GRZ 为主要方法来源 ✅；实际发现 Faedo et al. (2021) 多cFP碰撞框架更适合 v3 的需求。预测 LeClair 伪厄米 RG 有直接 β 函数方法 ✅；实际确认存在 3-loop + all-orders 猜想。预测 Kawabata 38 重路包含 {Q,C}=0 的处理 ❌；实际 38 重路是 AZ 类扩展，处理的是单粒子哈密顿量的对称性分类，而非 QFT 算子代数。

---

## §1 β 函数计算方法综述

### 1.1 GRZ (2018) 范式: 共形微扰论 + 复解析延拓

**参考**: Gorbenko, Rychkov, Zan, "Walking, weak first-order transitions, and complex CFTs," JHEP 10 (2018) 108 [arXiv:1807.11512]; companion paper SciPost Phys. 5 (2018) 050 [arXiv:1808.04380]

**核心方法**:
1. **诊断 β 函数结构**: 对 walking 耦合 λ (全局对称性单态):
   \[
   \beta(\lambda) = \frac{d\lambda}{dt} = -y - \lambda^2 + O(\lambda^3)
   \]
   其中 y 是小参数，高阶项有 O(1) 系数。

2. **二区域结构**:
   - y < 0: 两个实不动点 λ_± = ±√|y|，算符维度 Δ_± = d ∓ 2√|y| + O(y²)
   - y > 0: 无实不动点，"walking"耦合在 λ ∼ 0 附近滞留

3. **Walking 时间**: Δt ∼ ∫ dλ/β(λ) ∼ π/√y，产生指数层级 exp(π/√y)

4. **复不动点延拓**: 不动点位于 λ_* = ±i√y，维度有虚部 Δ = d ∓ 2i√y + O(y²)。**Walking判据是真小量是 |Im Δ| 而非 y 本身。**

5. **共形微扰论框架**: 以复不动点的共形CFT为参考，用其OPE系数计算walking物理观测量。

**对我们的可用性**: GRZ 的单耦合范式可直接接受 {Q,C}=0 贡献的 β_I(x,0) 作为 y 参数的虚部。需要推广到多耦合情况。

### 1.2 Faedo-Hoyos-Mateos-Subils (2021): 多cFP对碰撞的通用β函数

**参考**: Faedo, Hoyos, Mateos, Subils, "Multiple mass hierarchies from complex fixed point collisions," JHEP 10 (2021) 246 [arXiv:2106.01802]

**核心方法**——这是目前最直接可用的框架:

**单一 FPA β 函数** (不动点湮灭):
\[
\beta(g) = -\epsilon^2 - (g-g^*)^2 + O((g-g^*)^3)
\]
层级: log(μ_UV/μ_IR) ≃ π/ϵ = 2π/|Im Δ|

**双 FPA β 函数** (两个 cFP 对接近碰撞):
\[
\beta(g) = -[(g-g^* + \delta)^2 + \epsilon^2][(g-g^* - \delta)^2 + \epsilon^2]
\]
不动点位于 g = g^* ± δ ± iϵ

**三种区域** (以 δ/ϵ = |Im Δ/Re(d-Δ)| 为控制参数):

| 区域 | 条件 | 层级 scaling | 物理 |
|------|------|-------------|------|
| Case A | δ ≫ ϵ | 2π/|Im Δ| | 各对独立贡献，层级相加 |
| Case B | δ ∼ ϵ | π/[2(δ²ϵ+ϵ³)] | O(1/ϵ³) 增强 |
| Case C | δ ≪ ϵ | π/(2ϵ³) | 最大增强，算子变为确界 |

**关键对我们**: 若 {Q,C}=0 产生两个cFP对（来自Q和C各自贡献的复共轭对），则这个β函数是精确的数学模型。附录A已推广到任意数量cFP对。

**层级计算通用方法** (所有框架共用):
\[
\log\frac{\mu_{\text{UV}}}{\mu_{\text{IR}}} = \int_{g_{\text{IR}}}^{g_{\text{UV}}} \frac{dg}{\beta(g)} \simeq 2\pi i \sum \text{Res}\left(\frac{1}{\beta(z)}, z_k\right)
\]
主导贡献来自上半平面最接近实轴的极点。

### 1.3 Benini-Iossa-Serone (2020): 弱耦合4D实现

**参考**: Benini, Iossa, Serone, "Conformality Loss, Walking, and 4D Complex Conformal Field Theories at Weak Coupling," PRL 124, 051602 (2020)

**方法**: 构造UV完备的4D规范理论，通过双重迹算子耦合跨越边缘性来控制walking。关键创新是参数化控制弱耦合——使得复CFT的整个框架在微扰论层面可解。不假设任何对称性结构，因此不会预设交换对称性。

### 1.4 Gukov (2017): 动力系统方法

**参考**: Gukov, "RG Flows and Bifurcations," Nucl. Phys. B 919, 583 (2017) [arXiv:1608.06638]

**方法**: 将RG流视为耦合空间中的动力系统，应用 Conley 指数、Morse 理论和分岔分析。不动点合并/湮灭机制在数学上被归类为鞍结分岔。提供了拓扑约束规则来限制可能的RG流结构。

**对我们**: 若 Q 和 C 各自贡献一对复共轭不动点，Gukov 的分岔理论可以分类它们碰撞导致的可能流形拓扑。

### 1.5 方法比较矩阵

| 方法 | 输入 | 输出 | 对称性假设 | 对 {Q,C}=0 的适应性 |
|------|------|------|-----------|-------------------|
| GRZ 单耦合 | OPE数据 | β(λ), walking时间 | 全局对称单态 | 需推广到多耦合 |
| Faedo 多cFP | β 函数乘积形式 | 层级分析 | 无 | **最优** |
| LeClair OPE-RG | 算子代数 | 全阶β函数 | SU(2)代数结构 | 需替换SU(2)→{Q,C}代数 |
| Benini 弱耦合 | 双重迹算子 | walking/一阶相变 | 无 | 中等 |
| FRG (Wetterich) | 有效作用量 | 非微扰流 | 无 | 高(数值) |

---

## §2 反交换对称性约束的先例

### 2.1 核心发现: {Sym1, Sym2} = 0 在 QFT RG 中无直接先例

这是一个**重要的负结果**。我们的搜索未找到任何 QFT 论文明确研究两个对称性算子的反交换关系对 β 函数的约束。

### 2.2 最近的类比: 超对称性非重整化定理

**类比逻辑**: 在 SUSY QFT 中，超对称代数包含 {Q, Q̅} = P_μ 的反交换关系。该结构导致:
- **超势无非微扰修正**: 超势 W(Φ) 在任何阶都不重整化
- **Wilsonian β 函数单圈精确**: Shifman-Vainshtein 定理证明全纯 Wilsonian β 函数在单圈后截断
- **NSVZ β 函数**: 高阶修正仅通过反常维度进入

**关键对我们**: 如果 {Q,C} = 0 可以用类似 SUSY 代数的超代数框架理解，那么反交换关系可能产生类似的"非重整化定理"式的约束——约束 β_I(x,0) 的某些贡献必须为零。

**实现路径**: 
1. 将 Q 和 C 视为分次李代数(超代数)的奇生成元
2. {Q,C} = 0 意味着这是超代数的一个约束条件
3. β 函数的某些项可能因超代数选择规则而消失

**参考**: 
- Shifman & Vainshtein, Nucl. Phys. B 277, 456 (1986)
- Seiberg, Phys. Lett. B 318, 469 (1993)
- Rosten, JHEP 2010 (ERG框架证明)

### 2.3 BRST 反交换对称性与 RG 流

**参考**: Igarashi, Itoh, Morris, "BRST in the Exact Renormalization Group," PTEP 2019, 103B01 [arXiv:1904.08231]

BRST 算子 s 是反交换的 (s² = 0)，且量子主方程与 Wilsonian RG 流兼容。修改的 Slavnov-Taylor 恒等式约束 β 函数和反常维度。这提供了一个概念模板: 反交换对称性如何通过 Ward 恒等式约束 RG 流。

**对我们**: BRST 是单个反交换算子 (幂零)，而 {Q,C} = 0 是两个不同算子。但技术机制——通过推广的 Slavnov-Taylor 恒等式传导约束到 β 函数——是直接可推广的。

### 2.4 非交换对称性的 RG 约束 (一般框架)

虽然反交换对称性无直接先例，但**非交换**(不对易)连续对称性约束 RG 流的一般框架是已知的:
- 李代数对称性 G: β 函数必须与 G 的伴随作用兼容
- 非阿贝尔全局对称性: β 函数在对称群作用下协变
- 反常匹配条件: 't Hooft 反常必须沿 RG 流守恒

对 {Q,C} = 0 的自然推广: 将 Q 和 C 视为分次代数 (超代数) 的生成元，β 函数必须在该代数的伴随作用下协变。

---

## §3 {Q,C}=0 在 BL 分类中的处理

### 3.1 Bernard-LeClair 分类 (2001-2002)

**参考**: 
- Bernard & LeClair, "A Classification of Non-Hermitian Random Matrices," cond-mat/0110649
- Bernard & LeClair, "A classification of 2D random Dirac fermions," J. Phys. A 35, 2555 (2002)

**分类结构**: 
- 四个离散对合对称性: C (电荷共轭), P (宇称), Q, K (实性条件)
- 交换/反交换符号选择产生不等价的对称群
- 无实性条件: 10 个 AZ 类
- 有实性条件: 38 个总类

**关键对我们**: BL 分类中 C 和 P 的交换 vs 反交换产生不同的对称类。这与 {Q,C} = 0 概念上是同源的——它确认了对称性算子的交换关系确实改变物理分类。

**但 BL 分类的局限**: 它处理的是**自由费米子哈密顿量的对称性分类**（单粒子层面），而非相互作用 QFT 的算子代数。因此，BL 分类本身不包含 β 函数的约束信息。

### 3.2 Kawabata 38重路 (2019)

**参考**: Kawabata, Shiozaki, Ueda, Sato, "Symmetry and Topology in Non-Hermitian Physics," PRX 9, 041015 (2019) [arXiv:1812.09133]

**扩展内容**:
- 10 个 AZ 类 → 38 个类
- 关键创新: 非厄米系统中手征对称性 ≠ 子晶格对称性
- AZ† 类: AZ 的厄米共轭对应，仅在非厄米系统中存在

**对我们**: Kawabata 框架中的 Q 和 C 对应的是**时间反演**和**粒子-空穴对称性**的矩阵表示，其交换/反交换关系影响拓扑分类。这与 v3 的 Q (某种"电荷"或对称性算子) 和 C (可能对应"共轭"或"荷共轭") 是不同对象——但它们共享相同的代数结构: 离散对合算子的 (反) 交换关系区分物理类别。

**关键洞察**: 如果 Kawabata 的 38 重路能进一步扩展到包含更一般的算子代数（而非仅是单粒子对称性），那么 {Q,C} = 0 可能定义一个新的拓扑类。

### 3.3 结论: BL 分类和 Kawabata 分类都没有直接处理 {Q,C}=0 的场论含义

- BL 和 Kawabata 分类处理的是**分类学**（哪些对称类型存在），而非**动力学**（这些对称类型如何约束 RG 流）
- {Q,C} = 0 在 BL/Kawabata 的语境中对应的是反交换符号选择——这在分类学层面已经被考虑
- **但将这种反交换关系翻译为 β 函数的约束方程——这一步在现有文献中完全没有**

---

## §4 替代计算框架

### 4.1 泛函重整化群 (FRG/Wetterich)

**参考**: 
- Wetterich, Phys. Lett. B 301, 90 (1993)
- Bender & Sarkar, J. Phys. A 51, 225202 (2018) [arXiv:1801.08106]
- Ai, Alexandre & Sarkar, PRD 107, 025007 (2023)

**Wetterich 方程**:
\[
k\partial_k \Gamma_k = \frac{1}{2} \text{STr}\left[k\partial_k R_k (\Gamma_k^{(1,1)} + R_k)^{-1}\right]
\]

**对非厄米系统的适用性**: 
1. Bender-Sarkar (2018) 已将 LPA (local potential approximation) 应用于 PT 对称标量理论
2. 对 PT 对称 i g φ³ 理论: 有效势非奇异，基态稳定
3. PT 对称 -g φ⁴ 理论在 4D 中表现出渐近自由
4. Ai-Alexandre-Sarkar (2023) 证明 φ²(i φ)^ε 理论仅在 ε 为整数时可重整化

**对我们**: FRG 是非微扰方法，不需要假设交换对称性。可以直接将 {Q,C} = 0 引入有效作用量的对称性约束，然后数值解 Wetterich 方程得到 β_I(x,0)。

### 4.2 Jepsen-Klebanov-Popov (2021): Spooky Fixed Points

**参考**: Jepsen, Klebanov, Popov, "RG Limit Cycles and Unconventional Fixed Points in Perturbative QFT," PRD 103, 046015 (2021) [arXiv:2010.15133]

**关键发现——与 v3 的高概念类比**:
- **"Spooky" 不动点**: 耦合常数实值，但 Jacobian ∂βⁱ/∂gʲ 有**复数本征值**
- **Hopf 分岔**: 当这些复数本征值跨越虚轴时，产生 RG 极限环
- **关键阈值**: N_crit ≈ 4.475
- **计算到四圈**

**对我们**: "Spooky" 不动点是 β_I(x,0) ≠ 0 的已知最近似先例——实耦合上的复数本征值意味着虚部在 RG 流中起物理作用。JKP 的 Jacobian 分析技术在概念上可以直接应用于我们的情况，只需将 Jacobian 的虚部归因于 {Q,C} = 0 而不是 sextic 相互作用。

### 4.3 非幺正 CFT 的共形 Bootstrap

**参考**: 
- Gliozzi, "More constraining conformal bootstrap," PRL 111, 161602 (2013) [arXiv:1307.3111]
- Afkhami-Jeddi, "Conformal Bootstrap Deformations," arXiv:2111.01799

**方法**:
1. **Gliozzi 行列式法**: 不需要幺正性(positivity)，通过截断融合规则的 determinant/minor 条件直接求解
2. **Afkhami-Jeddi 变形法**: 从已知解（如2D Ising）连续变形到非幺正解（如 Yang-Lee 模型, c = -22/5, Δ_φ = -2/5）

**对我们**: 如果 {Q,C}=0 迫使 η 为纯虚数（v3 结论），则共形 Bootstrap 可以验证该复共形数据是否 self-consistent。这提供了一个**非微扰交叉检验**。

### 4.4 ε 展开 (绕复不动点)

**核心方法**: Sp(N) 模型在 d = 6-ε 中在复数耦合处展示不动点，但算子维度是**实数**。这暗示: 复数耦合不必然意味着复数物理量。

**对我们**: 若 v3 得出 β_I(x,0) ≠ 0（实轴上有虚部），这意味着与 Sp(N) 情况不同——DQCP 的物理观测量可能有虚部。这可以作为区分 DQCP 与已知非幺正 CFT 的诊断性特征。

### 4.5 晶格 MCRG (Monte Carlo Renormalization Group)

**当前状态**: 非厄米哈密顿量的晶格 MCRG 是新兴领域，没有成熟的通用框架。但 SU(2) 规范理论的梯度流 β 函数计算（Bennett et al. 2024, arXiv:2410.19484）提供了技术模板：
1. Wilson 流 → 定义跑动耦合 g²_GF(t)
2. β(t) = t d/dt g²_GF(t)
3. 无限体积极限 + 连续极限外推

**对我们**: 如果 DQCP 的格点实现包含 {Q,C}=0 约束（通过选取特定的非厄米格点哈密顿量），则梯度流方法可以直接数值测量 β_I。

---

## §5 LeClair (2024-2025) 伪厄米RG的详细分析

### 5.1 OPE 驱动的 β 函数

**参考**: LeClair, "A rich structure of renormalization group flows for Higgs-like models in 4 dimensions," arXiv:2411.07476; follow-up arXiv:2504.09327

**核心洞察**: LeClair 绕过了传统费曼图计算，直接从 OPE 推导 RG 流:

**第一步**: 构建有特定 OPE 结构的边缘算子 O^A:
\[
O^A(x) O^B(0) \sim \frac{1}{4\pi^4|x|^4} \sum_C C^{AB}_C O^C(0)
\]

**第二步**: 使用伪厄米流 J^a ≡ Φ†ᵏ τ^a Φ，其关键传播子:
\[
\langle Φ†ᵏ_i(x) Φ_j(y) \rangle = \frac{\delta_{ij}}{4\pi^2|x-y|^2}
\]

**第三步**: 流-流 OPE 因伪厄米性产生额外负号:
\[
J^a(x) J^b(y) = -\frac{\kappa}{16\pi^4|x-y|^4} \text{Tr}(\tau^a\tau^b) - \frac{if^{abc}}{4\pi^2|x-y|^2} J^c(y) + ...
\]

**第四步**: Master β 函数公式 (第二阶):
\[
\beta_{g_A} = \frac{dg_A}{d\ell} = -\sum_{B,C} C^{BC}_A g_B g_C
\]

其中 ℓ = log a，C^{BC}_A 直接来自 OPE 融合系数。

### 5.2 显式 β 函数系统

**SU(2) 实现** (f^{abc} = 2ε^{abc}, C^{12}_3 = C^{21}_3 = ... = -1):
\[
\boxed{\beta_{g_1} = g_2 g_3, \quad \beta_{g_2} = g_1 g_3, \quad \beta_{g_3} = g_1 g_2}
\]

RG 不变量: Q₁ = g₂² - g₃², Q₂ = g₃² - g₁², Q₃ = g₁² - g₂² (仅两个独立)

**U(1) 破缺**: 设 g₁ = g₂:
\[
\boxed{\beta_{g_1} = g_1 g_3, \quad \beta_{g_3} = g_1^2, \quad Q = g_1^2 - g_3^2 = \text{常数}}
\]

**循环RG解** (Q > 0):
\[
g_3(\ell) = \sqrt{Q} \tan\left(\sqrt{Q}(\ell - \widehat{\ell}_0)\right), \quad \lambda = \frac{\pi}{\sqrt{Q}}
\]

λ 是 RG 不变的周期。

### 5.3 对我们框架的适应性

LeClair 方法是**唯一一个不依赖费曼图、完全基于算子代数的 β 函数计算方法**。如果我们能:
1. 写出 {Q,C} = 0 代数下 Q 和 C 的 OPE
2. 推导出 C^{BC}_A 融合系数
3. 直接读取 β_{g_A}

则可以得到 β_I(x,0) —— **不需要路径积分，不需要微扰展开，不需要费曼图**。

**与 A 博士的协作**: A 博士可以从共形微扰论演绎推导 β 函数，而我们可以用 LeClair 的 OPE 代数方法提供**独立交叉检验**——两种方法必须在代数约束的阶重合。

---

## §末 对 A 博士计算的建议

### 建议一: 采用 Faedo 多 cFP 对 β 函数作为出发模板

理由: 若 {Q,C}=0，v3 已有 η 纯虚数。这意味着 β 函数在实轴上无零点但有两个接近的复共轭对（来自 Q 和 C 各自贡献）。Faedo 的 β = -[(g-g*+δ)²+ϵ²][(g-g*-δ)²+ϵ²] 是最精确的数学模型。

具体操作: 识别 (δ, ϵ) 与 ({Q,C}=0 的参数) 的映射关系。

### 建议二: 用 LeClair OPE 代数方法做交叉检验

理由: 两种完全不同的计算框架（共形微扰论 vs. OPE 代数）若给出相同的 β_I(x,0) 结构，则结论可靠度大增。

### 建议三: 检查 "spooky fixed point" 判据

JKP 的 Jacobian 复数本征值分析提供了一个有效诊断工具: 如果我们的 β 函数 Jacobian 在过渡点有复本征值跨越虚轴，则系统可能进入**极限环**而非 walking——这是与 P3-A 预测的 BKT walking 不同的物理。

### 建议四: 搜索反交换对称性对 Ward 恒等式的修正

这是本 Phase 发现的最有前景的理论方向:
1. {Q,C} = 0 在量子层面意味着什么 Ward 恒等式?
2. 该 Ward 恒等式如何约束 β 函数?
3. 推广 Slavnov-Taylor 技术（类似 BRST 但用两个反交换算子）

### 建议五: 优先级排序

| 优先级 | 任务 | 预期产出 | 风险 |
|--------|------|---------|------|
| P0 | Faedo β 函数代入 {Q,C}=0 代数 | β_I(x,0) 的显式依赖 | 低 |
| P0 | LeClair OPE 交叉检验 | 独立的 β_I 表达式 | 中 (需要写出 OPE) |
| P1 | {Q,C}=0 Ward 恒等式 | β_I 的对称性约束 | 高 (无先例) |
| P2 | JKP spooky 判据检验 | 极限环 vs Walking 判别 | 低 |
| P3 | FRG 数值验证 | 非微扰确认 | 中 (计算成本) |

### 关键文献清单 (按方法分类)

**β函数计算方法**:
- Gorbenko, Rychkov, Zan, arXiv:1807.11512 (GRZ 2018 — 复CFT范式)
- Gorbenko, Zan, arXiv:1808.04380 (Potts模型应用)
- Faedo, Hoyos, Mateos, Subils, arXiv:2106.01802 (多cFP对 — **最直接可用**)
- Benini, Iossa, Serone, PRL 124, 051602 (2020) (弱耦合4D实现)
- Gukov, arXiv:1608.06638 (RG分岔动力系统)
- Kaplan, Lee, Son, Stephanov, arXiv:0905.4752 (Conformality Lost — 鞍结分岔)

**伪厄米RG / OPE方法**:
- LeClair, arXiv:2411.07476 (2024 — OPE驱动的β函数)
- LeClair, arXiv:2504.09327 (2025 — 3-loop + all-orders猜想)

**非幺正CFT**:
- Jepsen, Klebanov, Popov, arXiv:2010.15133 (Spooky fixed points)
- Gliozzi, arXiv:1307.3111 (非幺正Bootstrap)
- Afkhami-Jeddi, arXiv:2111.01799 (Bootstrap变形法)

**对称性分类**:
- Bernard & LeClair, cond-mat/0110649 (BL分类)
- Kawabata, Shiozaki, Ueda, Sato, arXiv:1812.09133 (38重路)

**FRG/非厄米系统**:
- Bender & Sarkar, arXiv:1801.08106 (PT对称FRG)
- Ai, Alexandre & Sarkar, PRD 107, 025007 (2023) (Wilsonian FRG)

**SUSY类比 (反交换约束)**:
- Shifman & Vainshtein, Nucl. Phys. B 277, 456 (1986)
- Igarashi, Itoh, Morris, arXiv:1904.08231 (BRST + ERG)

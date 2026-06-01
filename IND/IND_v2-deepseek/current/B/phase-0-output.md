## B作业 v10 Phase 0 — ε-Bogoliubov 正则化关闭 C[v8-3]

---

### 【PI审核入口】

⚡ **本Phase推进了什么**：以测度论 + 凸分析 + 显式不定积分三路证明 ε-Bogoliubov 正则化族 σ^ε(u) 在 ε→0+ 时 L¹-强收敛到 σ⁰(u)，且积分极限 = 2ln2 路径无关。

⚡ **最关键的跨域连接**：将 v9-K1 的 dS_q/du = 2 sin(2u) ln cot u 重新解读为**二元熵的全变差结构**——∫|dS/du|du = TV(S) = 2(S_max − S_endpoint)，把"积分极限"问题化归为"熵函数边界值收敛"问题。这一观察使 DCT 的繁复估计被一行绝对收敛公式取代。

⚡ **预测 vs 实际**：
- 预测：R0 强收敛，因 sin(2u) 一阶零点 + ln cot u 对数发散仅形成 u·ln u 型可积奇点；ε 正则化不改变收敛阶。
- 实际：R0 成立。**且得到精确闭式**：N_I^{(S),ε} = 2ln2 − 2H(ε/2)，其中 H(x)=−x lnx−(1−x)ln(1−x)。这强于预测——不仅极限存在，**全程可解析、收敛速率严格为 O(ε ln ε)、路径完全无关**。

⚡ **卡在哪里（如果有）**：无卡点。所有积分闭式可算，DCT 主项可显式构造。

⚡ **对A上次质检的回应摘要**：本Phase为 v10 起步首次推导，无A上次正规推导作业可质检。

---

### §1 结论预测（推导开始前）

**预测命题（P-B0）**：在 toy 2-bit Bogoliubov 模型下，R0 成立。

**理由（直觉级）**：
1. ρ_B 退化谱处发散是**对数型**（|ln ρ_B| ~ |ln u|），sin(2u) 提供一阶零点，乘积 u·|ln u| → 0 可积。
2. ε-正则化在 2D 子空间是**仿射映射**（凸组合），保持秩≤2，仅把 0 特征值提升到 ε/2。
3. 由 DCT，只需找到 ε-无关的 L¹ 控制函数；q^ε ≥ ε/2 + (1−ε)q ≥ (1−ε)q 在 q>0 区域给出 |ln q^ε| ≤ |ln q| + O(1)。

**预测最易被证伪的环节**：路径依赖。若 ε(u) ∝ u^a，a < 2 时 p^ε 在 u=0 附近被 ε(u) 主导，ln p^ε 系数从 2 变为 a，**点态极限不再等于 σ⁰**。但若理解 ε(u) → 0 为 ε(u)/g(u) → 0 的均匀化（c→0），DCT 仍适用。这条裁决是 R0 vs R1 的关键。

---

### §2 Setup 与 v9-K1 一致性核验

**记号**：q(u) = cos²u, p(u) = sin²u, u ∈ [0, π/2]。则
- ρ_B(u) = q(u)|0⟩⟨0| + p(u)|1⟩⟨1|，二元谱 {q, p}。
- 边界点：u=0 时 ρ_B = |0⟩⟨0|（纯态，秩1）；u=π/2 时 ρ_B = |1⟩⟨1|；u=π/4 时 ρ_B = I/2（最大混合）。
- 二元熵 S_q(u) = −q ln q − p ln p ∈ [0, ln2]，S_q(π/4) = ln2，S_q(0)=S_q(π/2)=0。

**v9-K1 (A1) 复核**：
$$\frac{dS_q}{du} = -\frac{dq}{du}(\ln q + 1) - \frac{dp}{du}(\ln p + 1) = -\frac{dq}{du}\ln q - \frac{dp}{du}\ln p$$
（最后一步用 dq/du + dp/du = 0，因 q+p=1。）

代入 dq/du = −sin(2u), dp/du = sin(2u)：
$$\frac{dS_q}{du} = \sin(2u)\ln q - \sin(2u)\ln p = \sin(2u)\ln\frac{\cos^2 u}{\sin^2 u} = 2\sin(2u)\ln\cot u$$
✓ A1 验证通过，作为前提使用。

**关键观察**：dS_q/du 在 u ∈ (0, π/4) 上为正，(π/4, π/2) 上为负，且在 u=π/4 处过零。因此
$$N_I^{(S)} := \int_0^{\pi/2}|dS_q/du|du = 2\int_0^{\pi/4}\frac{dS_q}{du}du = 2[S_q(\pi/4) - S_q(0)] = 2\ln 2$$
**这恰是熵函数的全变差 TV(S_q)，几何上 = 2(峰值 − 端点值)**。这一身份将贯穿全证。

---

### §3 ε-正则化族的代数性质

**A2 给出**：q^ε(u) = (1−ε)cos²u + ε/2，p^ε(u) = (1−ε)sin²u + ε/2。

**性质 P1（保概率）**：q^ε + p^ε = (1−ε) + ε = 1 ✓

**性质 P2（保单调）**：dq^ε/du = −(1−ε)sin(2u)，dp^ε/du = +(1−ε)sin(2u)。导数符号不变，仅缩放 (1−ε) 倍。

**性质 P3（一致下界）**：
$$\min(q^\varepsilon, p^\varepsilon) \geq \varepsilon/2 \quad \forall u \in [0,\pi/2], \forall \varepsilon \in (0,1]$$
此外 q^ε ≥ (1−ε)cos²u 与 q^ε ≥ ε/2 同时成立，故
$$q^\varepsilon \geq \max((1-\varepsilon)\cos^2 u, \varepsilon/2)$$

**性质 P4（正则化熵 S^ε）**：
$$S^\varepsilon(u) = -q^\varepsilon\ln q^\varepsilon - p^\varepsilon\ln p^\varepsilon$$

边界值（关键！）：
$$S^\varepsilon(0) = S^\varepsilon(\pi/2) = -(1-\varepsilon/2)\ln(1-\varepsilon/2) - (\varepsilon/2)\ln(\varepsilon/2) = H(\varepsilon/2)$$
其中 H(x) := −x ln x − (1−x)ln(1−x) 为二元 Shannon 熵。

中点值不变：S^ε(π/4) = −2·(1/2)·ln(1/2) = ln 2，因 q^ε(π/4) = p^ε(π/4) = 1/2 与 ε 无关。

**性质 P5（dS^ε/du 显式）**：
$$\frac{dS^\varepsilon}{du} = (1-\varepsilon)\sin(2u)\ln\frac{q^\varepsilon}{p^\varepsilon}$$

定义被积式
$$\sigma^\varepsilon(u) := \left|\frac{dS^\varepsilon}{du}\right| = (1-\varepsilon)\sin(2u)\left|\ln\frac{q^\varepsilon(u)}{p^\varepsilon(u)}\right|$$

ε=0 极限：σ⁰(u) = sin(2u)|ln(q/p)| = 2sin(2u)|ln cot u|，与 v9-K1 一致。

---

### §4 R0 强收敛证明（DCT 路径）

**目标**：证明 lim_{ε→0+} ∫₀^{π/2} σ^ε(u) du = ∫₀^{π/2} σ⁰(u) du = 2ln2。

#### §4.1 点态收敛

对任意 u ∈ (0, π/2)，q(u) > 0 且 p(u) > 0。当 ε → 0+：
- q^ε(u) → q(u)
- p^ε(u) → p(u)
- ln(q^ε/p^ε) → ln(q/p)（因 ln 在 (0,1] 上连续）
- (1−ε)sin(2u) → sin(2u)

故 σ^ε(u) → σ⁰(u) 点态于 (0, π/2)。  
*学科工具*：实分析—连续函数复合的极限交换。  
*反驳检验*：u=0 与 u=π/2 处 σ⁰ 未定义（0·∞ 形式），但这两点为零测集，DCT 不要求点态收敛于零测集外。

#### §4.2 一致 L¹ 控制函数

**断言**：存在 g ∈ L¹(0, π/2)，使得 |σ^ε(u)| ≤ g(u) 对所有 ε ∈ (0, 1/2] 与 u ∈ (0, π/2) 成立。具体可取
$$g(u) = \sin(2u)\cdot(4\ln 2 + 2|\ln\sin u| + 2|\ln\cos u|)$$

**证明**：由 P3，q^ε ≥ max((1−ε)cos²u, ε/2)。分两情形：

*情形 A*（cos²u ≥ 1/2，即 u ∈ [0, π/4]）：q^ε ≥ (1−ε)/2 ≥ 1/4（因 ε ≤ 1/2）。又 q^ε ≤ 1。故
$$|\ln q^\varepsilon| \leq \ln 4 = 2\ln 2$$

*情形 B*（cos²u < 1/2，即 u ∈ (π/4, π/2)）：q^ε ≥ (1−ε)cos²u ≥ cos²u/2。故
$$|\ln q^\varepsilon| \leq |\ln(\cos^2 u/2)| = 2|\ln\cos u| + \ln 2$$

合并两情形（取上界）：|ln q^ε| ≤ 2ln2 + 2|ln cos u|。  
对称地：|ln p^ε| ≤ 2ln2 + 2|ln sin u|。

代入：
$$|\sigma^\varepsilon(u)| \leq (1-\varepsilon)\sin(2u)(|\ln q^\varepsilon| + |\ln p^\varepsilon|) \leq \sin(2u)(4\ln 2 + 2|\ln\cos u| + 2|\ln\sin u|) = g(u)$$
✓

**g 的可积性**：
- ∫₀^{π/2} sin(2u) du = 1
- ∫₀^{π/2} sin(2u)|ln sin u|du：令 s = sin u, ds = cos u du, sin(2u)du = 2sin u cos u du = 2s ds，
  = 2∫₀¹ s|ln s|ds = 2 · 1/4 = 1/2
- 对称地 ∫₀^{π/2} sin(2u)|ln cos u|du = 1/2

故 ∫g du = 4ln2 + 2(1/2) + 2(1/2) = 4ln2 + 2 < ∞ ✓

*学科工具*：测度论 DCT 控制函数构造；分段估计（凸组合的经典技巧）。  
*反驳检验*：边界 u→0 处 g(u) ~ 2u · 2|ln u| = 4u|ln u| → 0，可积。情形 B 的 ε≤1/2 限制是为了 1−ε ≥ 1/2，对充分小 ε 自动成立。

#### §4.3 DCT 应用

由 §4.1 + §4.2，Lebesgue 控制收敛定理直接给出：
$$\lim_{\varepsilon \to 0^+}\int_0^{\pi/2}\sigma^\varepsilon(u)\,du = \int_0^{\pi/2}\sigma^0(u)\,du = 2\ln 2$$

---

### §5 显式闭式（DCT 之外的独立验证 + 收敛速率）

**目的**：不靠 DCT，直接算出 ∫σ^ε，作为交叉验证。

**变量替换**：x = q^ε(u) = (1−ε)cos²u + ε/2。则
$$dx = -(1-\varepsilon)\sin(2u)\,du \quad \Longleftrightarrow \quad (1-\varepsilon)\sin(2u)\,du = -dx$$

边界：u=0 ↦ x = 1−ε/2；u=π/2 ↦ x = ε/2。又 p^ε = 1−x。

代入：
$$\int_0^{\pi/2}\sigma^\varepsilon\,du = \int_{1-\varepsilon/2}^{\varepsilon/2}\left|\ln\frac{x}{1-x}\right|\cdot(-dx) = \int_{\varepsilon/2}^{1-\varepsilon/2}\left|\ln\frac{x}{1-x}\right|dx$$

被积式关于 x = 1/2 对称，故
$$= 2\int_{1/2}^{1-\varepsilon/2}\ln\frac{x}{1-x}dx$$

**不定积分**（凸分析关键身份）：
$$\int\ln\frac{x}{1-x}dx = x\ln x + (1-x)\ln(1-x) + C = -H(x) + C$$

*验证*：d/dx [x ln x + (1−x)ln(1−x)] = ln x + 1 − ln(1−x) − 1 = ln(x/(1−x)) ✓

故
$$\int_{1/2}^{1-\varepsilon/2}\ln\frac{x}{1-x}dx = [-H(x)]_{1/2}^{1-\varepsilon/2} = -H(1-\varepsilon/2) + H(1/2) = \ln 2 - H(\varepsilon/2)$$

（用 H(1−x)=H(x)，H(1/2)=ln2。）

**最终闭式**：
$$\boxed{N_I^{(S),\varepsilon} := \int_0^{\pi/2}\sigma^\varepsilon\,du = 2\ln 2 - 2H(\varepsilon/2)}$$

**几何意义验证**：N_I^{(S),ε} = 2[S^ε(π/4) − S^ε(0)] = 2·全变差(S^ε)/2 = 全变差(S^ε)。这是熵曲线 u ↦ S^ε(u) 的"驼峰高度"两倍，恰为全变差。✓

**ε→0 极限**：H(ε/2) → 0，故 lim = 2ln2 ✓ 与 §4 DCT 结论一致。

**收敛速率**：H(ε/2) = −(ε/2)ln(ε/2) − (1−ε/2)ln(1−ε/2)
- 主导项：−(ε/2)ln(ε/2) = (ε/2)ln(2/ε) ~ (ε/2)|ln ε|（当 ε → 0+）
- 次导项：−(1−ε/2)ln(1−ε/2) ≈ ε/2 + O(ε²)

故
$$N_I^{(S),\varepsilon} = 2\ln 2 - \varepsilon\ln(2/\varepsilon) - \varepsilon + O(\varepsilon^2) = 2\ln 2 + \varepsilon\ln\varepsilon - \varepsilon(1+\ln 2) + O(\varepsilon^2)$$

**收敛速率严格为 O(ε ln ε)，主导系数为 +1**（即 ε ln ε，注意 ε ln ε < 0 当 ε ∈ (0,1)，所以 N_I^{(S),ε} < 2ln2 单调地从下方逼近）。

*学科工具*：信息论—二元熵函数 H 的解析延拓；凸分析—对偶函数 ∫ ln(x/(1−x))dx = −H(x)。  
*反驳检验*：对称性 x ↦ 1−x 使被积式 |ln(x/(1−x))| 不变，因子 2 来自此对称性。如果 q^ε ≠ p^ε 对称（如非对称 Bogoliubov），则需分别处理两个边界。

---

### §6 路径独立性（裁决 R1 是否需要）

**问题**：若 ε 不是常数而是 ε(u) = c·f(u)（c → 0+，f 有界正函数），N_I^{(S),ε} 极限是否仍 = 2ln2？

**答**：是。给出严格论证。

**§6.1 一般 ε(u) 下的控制函数**

定义路径相关族 σ^{ε(·)}(u) := (1−ε(u))sin(2u)|ln(q^{ε(u)}(u)/p^{ε(u)}(u))|。

**断言**：若 ε(u) ∈ (0, 1/2] 对所有 u 成立，则 |σ^{ε(·)}(u)| ≤ g(u)（同 §4.2 的 g）。

**证明**：§4.2 中所有估计**逐点**仅依赖于 ε(u) ≤ 1/2，不要求 ε 为常数。因此 g 是路径-无关的控制函数。✓

**§6.2 路径相关点态收敛**

若 ε(u) → 0 a.e.（如 c → 0 且 f 有界），则 q^{ε(u)}(u) → q(u) 与 p^{ε(u)}(u) → p(u) a.e.，故 σ^{ε(·)} → σ⁰ a.e.。

**§6.3 路径独立的 DCT**

由 §6.1 + §6.2 + DCT：
$$\lim_{c \to 0^+}\int_0^{\pi/2}\sigma^{c\cdot f(\cdot)}(u)\,du = 2\ln 2$$
对任意有界正函数 f 成立。

**§6.4 关于"ε ∝ u^a 与 a 不同导致路径相关 O(ε ln ε) 残差"**

PI 任务书提示的"路径相关残差"现象，**在严格 ε → 0 意义下不发生**。原因：

*精细分析*：考虑 ε(u) = c·u^a（c 固定但小，a > 0）。在 u → 0 附近：
- p^{ε(u)}(u) ≈ (1 − c·u^a)·u² + (c/2)·u^a
- 若 u² ≫ c·u^a（即 u^{2−a} ≫ c）：p^{ε(u)} ~ u²，|ln p^{ε(u)}| ~ 2|ln u|（与 ε=0 同形）
- 若 u² ≪ c·u^a（即 u^{2−a} ≪ c）：p^{ε(u)} ~ (c/2)·u^a，|ln p^{ε(u)}| ~ |ln(c/2)| + a|ln u|

两区域分界点：u_* ~ c^{1/(2−a)}（当 a < 2）。"边界层"宽度 ~ u_*。

在边界层内，被积式偏离 σ⁰ 的局部贡献 ~ ∫₀^{u_*} 2u·a|ln u|du ~ u_*²·|ln u_*| → 0 当 c → 0 ∀a < 2。

故**残差是边界层效应，c → 0 时所有 a 路径都给出同一极限 2ln2**。"路径相关"现象只出现在**c 固定**的有限正则化中，不属于 ε → 0 的本征行为。

**裁决**：R1 不被支持，R0 是严格答案。

*学科工具*：奇异摄动—边界层分析；测度论—路径独立 DCT。  
*反驳检验*：若 c 不→0（即正则化不撤），则路径确实相关——但这不是 ε → 0 极限问题。

---

### §7 关键引理 K-B0（命名 + 完整陈述）

**引理 K-B0（ε-Bogoliubov DCT 闭合）**

设 N=2 双模 toy 模型 Bogoliubov 谱 {q(u), p(u)} = {cos²u, sin²u}, u ∈ [0, π/2]。定义 ε-正则化：
$$q^\varepsilon(u) := (1-\varepsilon)\cos^2 u + \varepsilon/2, \quad p^\varepsilon(u) := 1 - q^\varepsilon(u)$$
被积式：
$$\sigma^\varepsilon(u) := (1-\varepsilon)\sin(2u)\left|\ln(q^\varepsilon(u)/p^\varepsilon(u))\right|$$

则：
- **(K-B0.i) 点态收敛**：σ^ε(u) → σ⁰(u) := 2sin(2u)|ln cot u|，∀u ∈ (0, π/2)。
- **(K-B0.ii) 一致 L¹ 控制**：g(u) := sin(2u)(4ln2 + 2|ln sin u| + 2|ln cos u|) ∈ L¹(0, π/2)，且 |σ^ε| ≤ g 对 ε ∈ (0, 1/2] 与 u ∈ (0, π/2) 成立。
- **(K-B0.iii) 强收敛**：lim_{ε→0+} ∫₀^{π/2} σ^ε du = ∫₀^{π/2} σ⁰ du = 2ln2。
- **(K-B0.iv) 显式闭式**：∫₀^{π/2} σ^ε du = 2ln2 − 2H(ε/2) = 2ln2 + ε ln ε − ε(1+ln2) + O(ε²)，收敛速率严格为 O(ε ln ε)。
- **(K-B0.v) 路径独立**：对任何可测族 ε_n: [0, π/2] → (0, 1/2] 满足 ε_n(u) → 0 a.e.，
$$\lim_{n\to\infty}\int_0^{\pi/2}(1-\varepsilon_n)\sin(2u)|\ln(q^{\varepsilon_n}/p^{\varepsilon_n})|\,du = 2\ln 2$$

**几何重述**：N_I^{(S),ε} = TV(S^ε) = 2[S^ε(π/4) − S^ε(0)] = 2[ln2 − H(ε/2)]，"熵曲线全变差 = 2 × 驼峰高度"。

**v9-K1 的严格化**：v9-K1 在 ε=0 极限点态成立（A1 给定）；K-B0 给出**积分意义下**的 ε→0 闭合，使得 N_I^{(S)} = 2ln2 不依赖正则化方案。

---

### §末 结论对比与裁决

**裁决**：R0（强收敛）成立。
- distributional 强收敛 = pointwise a.e.（K-B0.i）+ L¹ 控制（K-B0.ii）✓
- ρ_B 退化谱 ln 奇异性被 sin(2u) 一阶零点压回有限：σ⁰(u) ~ 4u|ln u| 在 u=0 附近，可积 ✓
- ∫ 良定义且 = 2ln2 ✓

**预测 vs 实际**：
- 预测 R0 → 实际 R0 ✓ **一致**
- 预测"易被路径依赖证伪" → 实际路径完全独立（§6 严格证明）：**比预测更强**
- 预测仅极限存在 → 实际得到精确闭式 N_I^{(S),ε} = 2ln2 − 2H(ε/2)：**比预测更强**

**对 v8-3 关切的回应**：v8-3 担忧 ε-正则化方案依赖性可能破坏 N_I^{(S)} = 2ln2。K-B0 显示：
- 在严格 ε → 0 意义下，结果 2ln2 是**绝对的、方案无关的、路径无关的**。
- 任何 O(ε ln ε) 残差都是有限正则化的伪迹，撤除正则化后消失。
- v9-K1 的精确性在 K-B0 加持下严格化。

**对 PI 的关键贡献**：
1. K-B0 把"奇异谱处熵积分"问题化归为"二元熵函数边界值"，可作为 v10 后续 Phase 的基础工具。
2. 闭式 2ln2 − 2H(ε/2) 给出**一切有限 ε 校正的精确表达式**，未来 Phase 若需保留 O(ε) 修正可直接使用。
3. 路径独立性证明排除 R1，简化 v10 后续推导（无需考虑正则化路径选择问题）。

---

### §A A 上次作业质检报告

本Phase为 v10 起步首次推导，无A上次正规推导作业可质检。

---

**完。**

# INSPECTOR Report: Wall 1 Round 1 -- Independent Audit

**审查员:** INSPECTOR (独立)
**审查日期:** 2026-06-09
**审查对象:**
- `attack/wall1_lower_bound/round1_A_formal.md` (A博士 形式攻击)
- `attack/wall1_lower_bound/round1_B_crossdomain.md` (B博士 跨域攻击)
**审查标准:** 比AB博士更严格，不因课题组内部而放水

---

## 0. 执行摘要

本轮攻击产出质量较高，核心分析框架基本正确。但发现 **2 个 BLOCK 级问题**（必须修正才能进入下一轮）、**7 个 WARNING 级问题**（技术上对但有重要caveat）、**5 个过度声张**。最严重的问题是 B博士将"典型值"混淆为"普适下界"，以及 A博士的"fully explained"声张与自身数据矛盾。

**总体评级: CONDITIONAL PASS** -- 修正 BLOCK 项后可进入 Round 2。

---

## 1. 声张一致性检查

### 1.1 恒等式一致性: PASS (经审查确认)

A博士: QCMI = 2log₂d_Q - I(R;Q'), d_Q = d², 对d=2给出 4 - I(R;Q')
B博士: QCMI = S(J(N)/d), d = dim(H_Q)

**表面矛盾:** A博士有 `J(N)/d²` (§2.2), B博士有 `J(N)/d` (§1.1).

**审查裁决:** 这是记号差异，非实质矛盾。A博士的 `d_Q = d²` 是系统 Q (两个 d 维节点) 的维度。B博士的 `d` 直接取系统维度 (在 2-qubit 系统中为 4)。将 B博士的 d 替换为 A博士的 d_Q 后，两人的恒等式完全等价: QCMI = S(J(N)/d_Q) = S(ρ_RQ')。两条推导路径均被独立验证为正确（审查员自行推导确认）。

**裁定:** PASS -- 二人声张一致，记号差异不影响实质。

### 1.2 CNOT QCMI: PASS (一致)

A博士: QCMI_CNOT = h₂(1) = 1.0 bit (引用了 η_quantitative.md §7.1)
B博士: QCMI_CNOT = 1.0 bit (来自 θ=π/4 对齐轴公式)

**裁定:** PASS -- 数值一致且数学上可互推。

### 1.3 η 改进幅度的分歧: WARNING

A博士: η₀≈0.180 → η_improved≈0.270 (improvement factor 1.5x, universal)
B博士: "物理下界至少 ~0.5-1.5 bits" (factor 3-8x, configuration-dependent)

**分析:** 这不是矛盾，而是针对不同问题的不同答案。A博士回答的是"universal (|c|-independent) prefactor 能改进多少"，B博士回答的是"对典型实验参数，实际 QCMI 是多少"。但 B博士的表述容易让人误以为是 universal result。

**裁定:** WARNING -- 两数表面矛盾但实质讨论不同量。然而 B博士的 executive summary 未充分区分 "typical value" vs "universal lower bound"，见 BLOCK-1。

### 1.4 恒等式"绕过 Fawzi-Renner"的声张一致性: PASS

两人均声称恒等式 QCMI = S(J(N)/d) 或等价形式绕过了 Fawzi-Renner 框架。此声张正确：恒等式直接给出 QCMI = S(ρ_RQ')，从 Kraus 算子构造 Choi 态再对角化即可得 QCMI，无需经过 Fawzi-Renner 的五层推导链。

**裁定:** PASS -- 声张正确且互相印证。

---

## 2. 数学正确性抽查

### 2.1 QCMI = S(J(N)/d) 恒等式: PASS

**审查员独立推导:**

给定:
- 初始态 |Φ⁺⟩_{RQ} maximally entangled, ρ_R = I/d
- N unital: N(I/d) = I/d
- ρ_RQ' = (I⊗N)(|Φ⁺⟩⟨Φ⁺|)

I(R;Q') = S(R) + S(Q') - S(RQ') = log₂d + log₂d - S(ρ_RQ') = 2log₂d - S(ρ_RQ')

由纯化论证 (B博士 附录A):
I(R;E'|Q') = S(RQ') - S(Q') - S(RQ'E') + S(Q'E')

在 U_{QE} 酉演化下，总态 |Ψ'⟩_{RQ'E'F} 保持纯性。RF 未被 U 触碰，故 S(RF) = S(R) + S(F) = log₂d + S(F)。由互补性 S(RE'F) = S(Q') = log₂d (因 N unital), S(RQ'E') = S(F)。

代入: I(R;E'|Q') = S(RQ') - log₂d - S(F) + (log₂d + S(F)) = S(RQ') = S(ρ_RQ') = S(J(N)/d). ∎

**裁定:** PASS -- 恒等式严格成立，对 unital 信道无误。

**注:** B博士将此标记为"定理 B1"暗示新颖性，但实际上这是量子信息论中 complementary channel 熵关系的标准推论（例如 Wilde 2017, §11.9 或 Hayden et al. 2008 的互补性讨论）。标记为"定理"技术上不算错（它确实是一个定理），但若暗示为本工作的新发现则有误导。见过度声张-2。

### 2.2 QCMI(θ=π/2, p=0.5) = 1.5 bits: PASS (验证正确)

**审查员独立验算:**

4 个 Kraus 算子在 θ=π/2, p=0.5 时:
- K_{00} = 0.5·diag(1,1,1,1) → 向量化为 0.5|I⟩⟩
- K_{11} = 0.5·diag(1,1,1,1) → 向量化为 0.5|I⟩⟩
- K_{01} = 0.5·diag(1,-1,1,-1)
- K_{10} = 0.5·diag(1,-1,-1,1)

K_{01} 与 K_{10} 在 Hilbert-Schmidt 内积下互相正交，且均与 |I⟩⟩ 正交。K_{00} 和 K_{11} 平行（方向 |I⟩⟩/2），合并权重为 4(p²+q²) = 4(0.25+0.25) = 2。

Choi 态 J(N) 的非零特征值: {2, 1, 1} (来自三个正交方向，每个权重归一化后)。J(N)/4 特征值: {1/2, 1/4, 1/4}。和=1. ✓

S = -(0.5 log₂ 0.5 + 0.25 log₂ 0.25 + 0.25 log₂ 0.25) = 0.5 + 0.5 + 0.5 = 1.5 bits. ✓

**裁定:** PASS -- B博士的计算严格正确。这是本轮最强产出之一。

### 2.3 Log-factor 推导: PASS (数学上正确但有范围限制)

A博士的小|c|展开推导:
- ρ_RQ' 在 c=0 时是纯态 (rank 1)
- 对小 |c|，主导特征值 λ₀ = 1 - α|c|² + O(|c|⁴)
- 次级特征值 λᵢ = βᵢ|c|² + O(|c|⁴)
- S ≈ -Σ βᵢ|c|² log₂(βᵢ|c|²) + O(|c|²) = κ|c|² log₂(1/|c|²) + O(|c|²)

这是标准微扰理论应用于密度矩阵熵。在 |c| → 0 极限下严格。

**裁定:** PASS -- 数学结构正确。但需注意:
- 仅在 |c| ≪ 1 时严格（微扰展开的收敛半径未确定）
- κ 系数的数值依赖于 Gram 矩阵的详细结构（A博士估计 ~2.3 for CNOT, 但未严格计算）
- 对于实验相关的 |c| ~ 0.8，微扰展开可能已发散

### 2.4 η 改进到 ~0.27 bits: WARNING

A博士的论证:
1. 二阶 Taylor bound: -log₂x ≥ (1-x)/ln2 + (1-x)²/(2ln2)
2. 适用于 x ∈ [0.5, 1] 即 F² ∈ [0.5, 1]
3. 对 F² = 0.5: improvement 25%; 对 F² = 0.3: improvement 35%
4. 结合 Layer 1→2 的 O(Δ_K²) correction → cumulative ~50%
5. η_improved ≈ 1.5/(8ln2) ≈ 0.270

**问题:**
- "cumulative ~50%" 是粗糙估计，各层改进并非简单乘法叠加
- F² 在实验中的实际范围未经验证（F² = 0.3-0.5 来自"估计"而非计算）
- 二阶 Taylor bound 在 x < 0.5 时不成立（二阶项可能为负），而 F² 可能低于 0.5
- η = 0.270 的声张精度给人精确计算的错觉，实为 back-of-envelope

**裁定:** WARNING -- 论证方向正确，但 0.270 这个数字的精度远高于论证本身的精度。建议标注为"order-of-magnitude estimate (~0.25-0.30)"。

---

## 3. Gap 检测

### BLOCK-1: B博士的"物理下界"概念混淆了典型值与普适最小值 [BLOCK]

**位置:** B博士 executive summary 和 §2.5

**声张:** "因果环的物理下界...至少为 ~0.5 bits (p=0.5)" 和 "物理下界...至少为 ~0.5-1.0 bits"

**问题:**
1. B博士自己承认 |c| → 0 时 QCMI → 0（§1.3, §1.5）。这意味着对任意固定的 p，存在合法的门配置使 QCMI 任意接近 0
2. "物理下界"一词暗示对所有物理上可能的门配置成立的最小值
3. 但 B博士实际上在讨论 (a) θ=π/2 特定配置的值 (1.5 bits), (b) Haar 期望值 (~2.25 bits), (c) Haar 下尾 (~1.0 bits)
4. 这些都不是"对所有配置成立的通用最小值" -- 它们分别是特定配置值、平均值、和统计分位数

**什么是真正的"物理下界":** 如果拒绝 |c|=0 的零测集，"物理下界"取决于 |c| 的下确界。如果存在物理机制强制 |c| ≥ ε > 0（例如 gate fidelity 的下限），则物理下界为 f(ε) > 0。但 B博士**没有**论证任何这样的 |c| 下界的存在性。

**后果:** 审稿人会直接指出这个混淆。声称"物理下界至少 0.5 bits"而同时承认 |c|→0 时 QCMI→0，是自相矛盾的。

**修正要求:** 必须明确区分:
- **普适下界** (对所有门配置成立): 0 (因为 |c|→0 极限)
- **典型值** (对 Haar 随机门): ~2.25 bits
- **有限|c|下的条件界** (给定 |c|² ≥ ε): f(ε) > 0
- 将"物理下界"的措辞改为"典型实验条件下的期望/保守估计"

### BLOCK-2: A博士的 "fully explained" 声张与后续分析矛盾 [BLOCK]

**位置:** A博士 §1.6

**声张:** "The observed gap of 4-18x...is fully accounted for by the cumulative conservatism...No additional 'mystery gap' exists."

**矛盾:** 同一文档的 §6.2 明确写道:
- "Total from lower bound: ≈ 0.53 bits"
- "Experimental QCMI: 2.0-3.2 bits"
- "UNACCOUNTED: ≈ 1.5-2.7 bits"

如果还有 1.5-2.7 bits "UNACCOUNTED"，那么 gap 就不是 "fully explained"。A博士在 §1.6 说的是 gap 的"来源"（哪些层导致了保守性）已被识别，而非 gap 的量值已被桥接。但措辞 "fully explained" 和 "No additional mystery gap" 强烈暗示 gap 已被量化分解，而实际并非如此。

**修正要求:**
- §1.6 改为: "The 4-18x gap can be qualitatively attributed to the five-layer chain's conservatism, but quantitative bridging remains incomplete: ~1.5-2.7 bits of QCMI for typical configurations are not captured by any term in our analysis (see §6.2)"
- 删除 "No additional mystery gap exists"

### GAP-1: Buscemi vs 乘积态环境的数量差异未分析 [WARNING]

**位置:** B博士 §1.2 (末尾注)

B博士计算得到 p=0.7, θ=π/2 时理论 QCMI = 1.357 bits，但实验 Rxx(π/2) 值 = 1.000 bits。差异 36%。

B博士的归因:"差异可能来自 Buscemi 混合态环境 vs 乘积环境的数值差异。"

**问题:**
- 36% 是一个显著差异 —— 约 0.357 bits
- 没有分析这个差异是否在 Buscemi 框架下可被理论解释
- 如果理论（乘积态）和实验（Buscemi）差异这么大，那么 B博士的整个对齐轴理论框架与实验数据的可比性存疑

**裁定:** WARNING -- 这个 gap 需要严肃处理。不能在论文中呈现精确理论值 1.357 而对实验值 1.000 只用一句 "可能来自框架差异" 带过。

### GAP-2: 对齐轴单调性无证明 [WARNING]

**位置:** B博士 §1.4

**声张:** "对齐轴的 QCMI 是非对齐轴 QCMI 的下界"

**证据:** 启发式论证（非对齐引入额外 Kraus 算子非对角元 → 特征值分布更分散 → 熵更大）

B博士在 SA-2 中诚实承认这需要严格证明，并建议标注为 "强数值证据支持" 而非 "定理证明"。但 §1.4 的攻击策略将此作为操作方法陈述（"利用操作单调性: QCMI(N) ≥ QCMI(N_aligned)"），使用了"单调性"这一暗示定理级别的术语。

**裁定:** WARNING -- 此声张在该攻击框架中是核心依赖项（未证明的单调性支撑了整个对齐轴下界策略），不能仅靠启发式论证。Round 2 必须提供证明或数值证据。

### GAP-3: |c|⁴ bonus 的符号区分不完整 [WARNING]

A博士 §6.1 和 commutativity_theorem.md Theorem (IV) 给出 bonus = -α Σ|c|⁴ + β Σ|c|⁴ sin²θ。但对 α 的定量确定依赖实验数据反推（"α_eff ≈ 10.5"），且 α 的非负性依赖 Kraus 算子的次可乘性论证（commutativity_theorem.md SA-4 承认这是"定理中最弱的部分"）。

**裁定:** WARNING -- bonus 定号规则在概念上是正确的，但 α 的非负性严格证明未完成，且 α 的数值依赖实验而非理论。这在投稿中会被审稿人质疑。

### GAP-4: Log-factor κ 系数未严格计算 [WARNING]

A博士估计 κ ≈ 2.3（§3.4），来自 CNOT 数据反推。§3.2 的 Gram 矩阵分析给出了 κ 的结构形式（κ = p(1-p)/(2ln2) × number of active Pauli sectors），但未给出严格的解析值。

**裁定:** WARNING -- κ 是 log-factor improvement 的核心参数。当前只有估计，没有严格计算。P0 (数值 Choi 对角化) 应优先执行。

---

## 4. 过度声张清单

### 过度声张-1: A博士 §1.6 "No additional mystery gap exists" [过度]

**严重性:** BLOCK
**详情:** 见 BLOCK-2。与 §6.2 自己报告的 ~1.5-2.7 bits unaccounted 矛盾。
**修正:** 移除或大幅弱化此声张。

### 过度声张-2: B博士将已知恒等式标记为"定理 B1" [轻微过度]

**严重性:** WARNING
**详情:** QCMI = S(J(N)/d) 是标准 complementary channel 关系，非本工作的新发现。标记为"定理"暗示新颖性。建议改为"引理 (标准结果)"或"恒等式 (已知)"。
**修正:** 引用标准来源 (如 Wilde 2017) 并标注为"known identity"而非"定理 B1"。

### 过度声张-3: B博士 "物理下界至少 ~0.5-1.0 bits" [过度]

**严重性:** BLOCK
**详情:** 见 BLOCK-1。将统计量或特定配置值混淆为普适下界。
**修正:** 明确区分 universal bound (0), conditional bound f(|c|), typical value (~2.25).

### 过度声张-4: A博士 "η 最多改进到 ~0.27 bits" 的精确性 [过度]

**严重性:** WARNING
**详情:** 见 §2.4 分析。数字精度远高于论证精度。
**修正:** 标注为 order-of-magnitude estimate, 给出范围而非单点值。

### 过度声张-5: A博士表格 §5.4 中 "η₀ is a valid universal lower bound -- TRUE" 的证据 [轻微过度]

**严重性:** 信息性
**详情:** 表格中该行的证据列为 "All experimental data satisfy QCMI ≥ η₀·Σ|c|²"。但由于 η₀ 是推导出来的下界，实验数据自动满足（它们来自同一个理论框架的计算）。这不是"independent verification"，只是"consistency check"。措辞应更精确。
**修正:** 证据改为 "Derived analytically; all numerical evaluations consistent."

---

## 5. 审稿人视角

### 5.1 审稿人会直接攻击的点 (高影响力)

1. **"物理下界"的措辞 (见 BLOCK-1):** 审稿人会指出 self-contradiction: 如果 |c|=0 是合法极限 (QCMI=0)，那么不存在正的普适物理下界。"物理下界"可能是 "conditional lower bound given a physically motivated prior on |c|" 但 A博士和 B博士都未建立这样的 prior。

2. **"Fully explained" vs 1.5-2.7 bits unaccounted (见 BLOCK-2):** 审稿人会标注这个内部矛盾并要求解释。

3. **d=2 only 的推广问题:** 所有精确计算 (B博士的 ZZ(θ) 解、A博士的 Pauli 扇区分析) 都依赖 d=2 的特殊性质 (Pauli 基的完备性、Cartan 子代数的 SO(3) 结构)。审稿人会问: 这对 d > 2 意味着什么? 是否有理由相信结果定性保留?

4. **Log-factor claim 无数值验证:** 审稿人会要求至少对一个具体配置 (如 θ=0.1 的小角度 ZZ ring) 做数值对角化来验证 O(|c|² log(1/|c|²)) 标度。

5. **Buscemi vs 乘积态差异 36%:** 审稿人会问为什么理论和实验差这么多，并要求在 Buscemi 框架下重做理论计算。

### 5.2 可辩护的改进 (中等影响力)

1. **五层保守性审计:** 方法学透明、定量。审稿人可能质疑具体数字 (如 "1.5-3x from Layer 0→1") 但不会否定方法论本身。

2. **QCMI = S(J(N)/d) 恒等式:** 正确且提供清晰的计算路线。审稿人会认可这个简化。

3. **ZZ(θ) 精确解:** 提供了一个可检验的 benchmark，增强论文可信度。审稿人会要求补充数值对角化交叉验证 (B博士已提出此建议)。

4. **|c|² log(1/|c|²) 标度:** 如果配合数值验证，这是对 Fawzi-Renner 线性界的实质性改进。审稿人会认可其在小 |c| 极限下的严格性。

### 5.3 会被审稿人轻易推翻的 (低防御力)

1. **对齐轴单调性作为定理使用:** 如果审稿人要求严格证明而你只能提供启发式论证，这个声张会崩溃。B博士的 SA-2 诚实标注了这一点——必须尊重这个标注，不能在实际使用中当作定理。

2. **"η ≤ 0.27 无法进一步改进":** A博士的论证假设 bound 必须具有 η·Σ|c|² 的形式且 η 必须 |c|-independent。如果接受 |c|-dependent prefactor (如 log-factor 形式)，这个限制就不适用。审稿人会质疑为什么坚持 |c|-independent 形式。

3. **"QCMI/Σ|c|² → 0 in aligned limit" 作为 universal feature:** 这对 aligned 配置是正确的，但对非对齐配置（sin²θ > 0），QCMI/Σ|c|² 的渐近行为可能不同。审稿人会要求区分 "aligned" 和 "misaligned" 的渐近行为。

---

## 6. 对 PI 的建议

### 6.1 Round 2 准入条件

**必须修正 (BLOCK 项):**
1. B博士修正"物理下界"措辞，严格区分 universal bound / conditional bound / typical value
2. A博士修复 "fully explained" 与 "1.5-2.7 unaccounted" 的矛盾表述
3. 两人就 Buscemi vs 乘积态差异给出分析或声明范围限制

**建议修正 (WARNING 项):**
4. B博士将对齐轴单调性从操作声张降级为待验证假设
5. A博士将 η≈0.270 标注为量级估计
6. B博士将"定理 B1"改为"已知恒等式"并引用来源
7. A博士执行 P0 (数值 Choi 对角化) 以验证 log-factor

### 6.2 论文策略建议

1. **重新定位 η₀ 的角色:** 与其声称 η₀ = 0.180 是一个 tight physical result，不如将其定位为 "worst-case floor of a |c|-dependent bound function"。论文的核心结果应该是: QCMI ≥ f(|c|, p, sin²θ) 其中 f 在小 |c| 时给出 log-factor improvement，在典型参数下给出 ~1-2 bits。η₀ 只是 f(|c|_max, p=0.5) 的极限值。

2. **建立 |c|-条件界:** 与其讨论"物理下界"（语义模糊），不如建立 "给定 |c|² ≥ ε 条件下的下界"。这需要: (a) 论证实验中 ε 有一个物理下限（如 gate fidelity 限制）, (b) 计算 f(ε)。这比"物理下界"在审稿人面前更有防御力。

3. **数值验证优先级:** P0 (Choi 对角化) 应该在 Round 2 被标记为最高优先级。它是验证所有声张 (log-factor, 对齐轴下界, 精确解 vs 数值) 的关键基础设施。

### 6.3 分工建议

- **A博士 Round 2:** 执行 P0 (数值 Choi 对角化)，完成 κ 的解析计算，修正 "fully explained" 表述
- **B博士 Round 2:** 提供对齐轴单调性的数值证据 (1000+ configurations)，将"定理 B1"降级为已知恒等式，分析 Buscemi vs 乘积态差异
- **INSPECTOR Round 2 审查点:** (a) 数值 Choi 对角化结果 vs 解析预测, (b) 对齐轴单调性的数值证据, (c) Buscemi gap 分析

---

## 7. 逐项裁决汇总

### PASS 项 (声张正确且被交叉验证)

| # | 项目 | 何人 | 状态 |
|:--:|------|:--:|:--:|
| P1 | QCMI = S(J(N)/d) 恒等式 (两人等价形式) | A+B | PASS |
| P2 | QCMI(θ=π/2, p=0.5) = 1.5 bits | B | PASS (审查员独立验算) |
| P3 | QCMI(CNOT, p=0.5) = 1.0 bit | A+B | PASS |
| P4 | 五层保守性审计方法论 | A | PASS |
| P5 | Log-factor 小|c|推导 (数学结构) | A | PASS (微扰论标准应用) |
| P6 | CFOL 基础: QCMI=0 ⇔ |c|=0 | A+B | PASS (继受此前审查) |
| P7 | d=2 范围限定 (两人均明确) | A+B | PASS |
| P8 | A博士自攻击 §7 | A | PASS (诚实识别弱点) |
| P9 | B博士自攻击 §SA-1 到 SA-4 | B | PASS (诚实识别弱点) |

### WARNING 项 (技术上正确但有重要 caveat)

| # | 项目 | 何人 | 严重性 |
|:--:|------|:--:|:--:|
| W1 | η≈0.270 的精确性远高于论证精度 | A | 中 |
| W2 | 对齐轴单调性用作操作声张但未证明 | B | 高 |
| W3 | Buscemi vs 乘积态 36% 差异未分析 | B | 高 |
| W4 | |c|⁴ bonus α 系数依赖实验反推 | A | 中 |
| W5 | Log-factor κ 系数无严格解析值 | A | 中 |
| W6 | 两人均未提供 log-factor 的数值验证 | A+B | 中 |
| W7 | "定理 B1"标记暗示新颖性 (实为标准结果) | B | 低 |

### BLOCK 项 (错误或致命 gap)

| # | 项目 | 何人 | 严重性 |
|:--:|------|:--:|:--:|
| B1 | "物理下界 ~0.5-1.0 bits" 混淆典型值与普适最小值 | B | 致命 |
| B2 | "Fully explained" 与 "1.5-2.7 bits unaccounted" 矛盾 | A | 致命 |

---

## 8. 对两文件的逐段审查注记

### A博士 round1_A_formal.md

| 段落 | 声张 | 审查意见 |
|------|------|---------|
| Executive Summary | gap fully accounted for | BLOCK -- 见 BLOCK-2 |
| §1.2 Layer 0→1 | gap factor table | PASS -- 定量正确，线性 bound vs 对数真值 |
| §1.3 Layer 1→2 | 1.5-2x conservatism | WARNING -- 数字粗糙但合理 |
| §1.4 Layer 2→3 | γ_min vs γ_avg factor 1.67x | PASS -- 分析正确 |
| §1.6 cumulative | "No additional mystery gap" | BLOCK -- 见 BLOCK-2 |
| §2.1 exact identity | QCMI = 4 - I(R;Q') (d=2) | PASS -- 正确且与 B博士一致 |
| §2.3 log-factor | O(|c|² log 1/|c|²) | PASS -- 数学结构正确 |
| §2.4 comparison | ratio table | PASS -- 明确标有 κ 因子 |
| §3.4 calibration | κ ≈ 2.3 from CNOT | WARNING -- 仅估计，未严格计算 |
| §4.3 | η improved to ~0.27 | WARNING -- 见 §2.4 分析 |
| §5.2 saturating seq | δ=ε² scaling | PASS -- 正确说明 ratio → 0 |
| §5.4 table | η₀ is NOT asymptotically tight | PASS -- 与 §5.2 分析一致 |
| §6.2 bottom-up | QCMI ≈ 0.5-0.8 from single-Pauli | WARNING -- 与实验 2.0-3.2 矛盾，暗示分析不完整 |
| §7 SA-1 | perturbative convergence concern | PASS -- 诚实 |
| §7 SA-4 | |c|⁴ bonus太小 | PASS -- 诚实且提出具体改进措施 |

### B博士 round1_B_crossdomain.md

| 段落 | 声张 | 审查意见 |
|------|------|---------|
| Executive Summary | "物理下界...至少为 ~0.5 bits" | BLOCK -- 见 BLOCK-1 |
| Executive Summary | "η₀ = 0.180 比...大 8.3x" | WARNING -- 这是特例比较，非普适 |
| §1.1 "定理 B1" | QCMI = S(J(N)/d) | WARNING -- 声张正确但标记为"定理"过度 |
| §1.2 精确解 | QCMI(θ=π/2, p=0.5) = 1.5 | PASS -- 审查员独立验算正确 |
| §1.3 一般 θ 公式 | λ₁, λ₂, λ₃ 表达式 | PASS -- 结构合理（函数形式有物理意义）|
| §1.4 非对齐轴扩展 | 对齐 = 最小 QCMI | WARNING -- 启发式论证，非证明 |
| §2.3 Haar 期望 | E[QCMI] ≈ 2.15 | PASS -- 量级估计，与实验 2.25 一致 |
| §2.4 下分位数 | 1% quantile ≫ 0.180 | PASS -- 定性正确，Haar 尾的零测度性质 |
| §2.5 物理相关性裁决 | η₀ 物理上不相关 | WARNING -- 措辞过度（见 BLOCK-1 分析）|
| §3 图论/干涉 | ‖ΔU‖_F 到 QCMI | PASS -- 与 commutativity_theorem 一致 |
| §4 量子估量学 | Fisher/Cramér-Rao 下界 | WARNING -- 推导不完整（"需要更精确的不等式"）|
| §综合表 | 四视角汇聚 | PASS -- 有用但需标注各视角的不同性质 |
| §SA-1 | unital 验证 | PASS -- 验证正确 |
| §SA-2 | 对齐轴单调性承认 | PASS -- 诚实标注为"建议数值证据支撑" |
| §SA-3 | Choi 熵 vs Fawzi-Renner 标度 | PASS -- 正确分析 |
| §SA-4 | p→0.5 行为 | PASS -- 与物理直觉一致 |
| 附录A | QCMI = S(J(N)/d) 证明 | PASS -- 完整且正确 |

---

## 9. 后续审查计划

Round 2 INSPECTOR 重点:
1. P0 (Choi 对角化) 结果验证 —— 与解析预测对比
2. 对齐轴单调性数值证据 (1000+ configurations)
3. BLOCK-1 和 BLOCK-2 的修正是否充分
4. Buscemi gap 分析
5. κ 系数的解析确定（若完成）

---

*INSPECTOR Wall 1 Round 1 审查完成。条件性通过 —— 修正两个 BLOCK 项后可进入 Round 2。Round 1 的核心正贡献: (1) QCMI = S(ρ_RQ') 恒等式确认, (2) ZZ(θ) 精确解, (3) Log-factor 识别, (4) 五层保守性定量分解。核心风险: (1) "物理下界"语义模糊, (2) 定量 gap 未桥接, (3) 对齐轴单调性未证明。*

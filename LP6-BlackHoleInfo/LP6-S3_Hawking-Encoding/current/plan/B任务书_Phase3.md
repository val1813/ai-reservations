# B 博士任务书 — Phase 3

**课题：** Hawking-Encoding v1
**Phase：** 3（路径 B — Canonical Type III₁ 独立论证 + Microcanonical 压力测试）
**日期：** 2026-06-01
**价值分类：** [核心] + [防守] — 关闭 CP-009 critical + 加固 Phase 1 no-go

---

## 攻击目标

**主攻**：在 canonical Type III₁ ensemble（SYK/JT 标准 TFD 设置，固定 β）中，建立 **不依赖 GKRR completeness** 的 M.B no-go 独立论证。

**副攻**：在 microcanonical Type II∞ 构架（"最有利 GKRR completeness" 的设置）中，检验 Phase 1 K1.10 no-go 是否仍成立。

你的 Phase 2 发现 GKRR completeness 在 canonical Type III₁ 中不成立（因为 P₀ ∉ algebra）。Phase 3 的任务是：**即使 GKRR completeness 不成立，M.B no-go 是否仍能从其他论证中推出？**

---

## 背景（你的 Phase 2 产出 + PI 裁决）

你在 Phase 2 的核心发现：
1. Type III₁ 不含有限投影 → P₀ ∈ 𝒜_ε 在 canonical ensemble 中不成立
2. GKRR completeness 仅在 microcanonical Type II∞ (crossed product) 中可能成立
3. Phase 1 四处论证需要修正（§4.2/§6.1/§6.3/§5）
4. Subfactor index 可能是独立于 GKRR completeness 的 M.B no-go 论证基础

**PI 裁决**：GKRR completeness = setup-dependent。Canonical Type III₁ 中不是 theorem。战略转向路径 B：寻找不依赖 GKRR completeness 的 M.B no-go。

---

## 具体推导任务

### 步骤 1：Type III₁ 中 M.B 的直接论证（canonical ensemble，不依赖 GKRR）

**核心问题**：在 canonical Type III₁ 中（不含 P₀），是否仍能证明 A_island ⊆ A_bdy 或 A_island 的算符可被 A_bdy 的算符逼近？

**候选论证路径**：

**(a) Tomita-Takesaki modular flow 路径**：
- Type III₁ algebra 𝒜 在态 ω 上的 modular flow σ_t^ω 是代数自同构
- Modular Hamiltonian = −log Δ_ω（Δ_ω 是 modular operator）
- 在 Type III₁ 中，modular flow 的 generator 不在 algebra 中（outer automorphism）
- **问题**：island 算符的时间演化是否可由 boundary modular flow 实现？
- 如果 island 算符的时间导数 ∈ A_bdy（通过 boundary Hamiltonian H ∈ A_bdy），则 island 算符在 WOT 中可被 A_bdy 逼近——即使没有 P₀！

**(b) Relative modular operator 路径**：
- 对任意态 ω₁, ω₀，relative modular operator Δ_{ω₁|ω₀} 定义了 algebra 之间的映射
- 如果 Δ_{ω₁|ω₀}（ω₁ 含 infallen qubit, ω₀ = TFD）可被 A_bdy 中的算符逼近 → island 态信息在 boundary 中
- 这给出了 M.B 的 modular 判据：M.B 非平凡 ⟺ Δ_{ω₁|ω₀} ∉ A_bdy''

**(c) Type III₁ centralizer 路径**：
- 在 Type III₁ 中，centralizer 𝒜_ω = {A ∈ 𝒜 : σ_t^ω(A) = A ∀t} 是 Type II₁ algebra
- Centralizer 包含 "modular-invariant" 算符
- 如果 island 算符（在 infallen qubit 附近）不属于 centralizer → 它们有非平凡的 modular flow → 可能不在 A_bdy 中
- 这给出 M.B 的 centralizer 判据：M.B 非平凡 ⟺ island operators ⊄ 𝒜_bdy centralizer

### 步骤 2：跨域论证 — Type III₁ 的 Connes-Takesaki 结构

**(a) Flow of weights**：
- Type III₁ 的 Connes-Takesaki flow of weights 给出代数在 spectrum 上的分解
- Type III₁ ⟺ flow of weights = ℝ 上的 ergodic action
- 这意味着 Type III₁ algebra 可以被写为 (Type II∞) ⋊_θ ℝ（crossed product by modular flow）
- **物理意义**：canonical Type III₁ 已经"内含"了所有 Type II∞ information（through decomposition）→ boundary algebra 可能已经 "足够大"

**(b) 如果 Type III₁ 已经"足够大"**：
- 那么即使 GKRR completeness 在这个 algebra 中不成立（没有 P₀）
- A_island 算符可能仍可以通过 modular theory 被 A_bdy 在物理上充分逼近
- 判据：对任意 island state |ψ_I⟩，存在 boundary operator sequence 使得所有物理观测量的期望值被逼近到任意精度

### 步骤 3：Subfactor index 的反面攻击

A 博士在正面攻 [𝒜_full : 𝒜_bdy] > 1。你的任务是同时考虑反面对手：

**(a) 如果 [𝒜_full : 𝒜_bdy] = 1 在 Type III₁ 中成立？**
- 这意味着 𝒜_bdy = 𝒜_full 在 canonical ensemble 中
- 但这与 "Type III₁ ≠ B(ℋ)" 是否矛盾？
- B(ℋ) 是 Type I factor（full matrix algebra 的 von Neumann closure）
- Type III₁ ≠ Type I → 𝒜_bdy ≠ B(ℋ)（作为 von Neumann algebras）
- **但是**：𝒜_full 真的等于 B(ℋ) 吗？在引力理论中，约束（Hamiltonian + diffeomorphism）可能使 𝒜_full 小于 B(ℋ)

**(b) 如果 𝒜_full ≠ B(ℋ)（引力约束）**：
- 则 [𝒜_full : 𝒜_bdy] 应理解为 Type III₁ subfactor 在更大 Type III algebra 中的 index
- 这需要 Kosaki-Longo 的 Type III index 理论
- Type III index 的可能性：可以是任意实数 ≥ 1（包括 ∞）
- **关键物理问题**：diffeomorphism constraint 是否将 𝒜_full 从 B(ℋ) 压缩到了某个 Type III algebra？

### 步骤 4：副攻 — Microcanonical Type II∞ 压力测试

**设置**：Microcanonical ensemble（窄能量窗口 ΔE），CPW crossed product → Type II∞。这是 GKRR completeness **最可能**成立的设置（P₀ ∈ algebra via crossed product）。

**检验**：在这个 "最有利 GKRR" 的设置中，Phase 1 K1.10 no-go（ε(N) ~ e^{-cN} 逼近）是否仍成立？

**(a) Type II∞ 中的 ε(N) bound**：
- Type II∞ 有 trace（finite trace projection）→ HKLL reconstruction 可以用 trace-norm 误差量化
- ε(N) ~ e^{-cN} 在 Type II∞ 中是否保持？
- CPW 的 Type II∞ 构造给了一个 explicit trace → 可用 trace-norm 替代 operator norm

**(b) Type II∞ 中的 EW reconstruction**：
- Entanglement wedge reconstruction 在 Type II∞ 构架下的误差 bound
- 如果误差仍是指数小的 → K1.10 在 microcanonical 中仍成立 → no-go 在 ensemble 选择下 robust

### 步骤 5：跨域连接 — QFT split property 与 Type III₁ completeness

**你 Phase 2 §3.1 的发现**：在某些 conformal nets 中 split property fails → boundary algebra 沿径向不 factorize。

**Phase 3 升级**：
- 如果 split property fails 在 SYK/JT boundary CFT 中 → 𝒜_bdy 的 commutant 结构可能是非平凡的
- 非平凡 commutant ⟺ (𝒜_bdy)' ≠ ℂ·𝟙 ⟺ 𝒜_bdy ≠ B(ℋ) → [B(ℋ) : 𝒜_bdy] > 1
- 这给出了 subfactor index > 1 的独立论证——不依赖 GKRR completeness！

---

## 必须回答的问题

1. 在 canonical Type III₁ 中（不含 P₀），是否存在不依赖 GKRR completeness 的 M.B no-go 论证？如果有，核心工具是什么（modular flow / centralizer / relative modular operator / split property）？
2. Type III₁ 的 Connes-Takesaki flow of weights 是否意味着 boundary algebra 已经是"足够大"的（即使不含 P₀）？
3. 如果 A 博士证明 [𝒜_full : 𝒜_bdy] > 1 → M.B no-go 自动成立。但如果 [𝒜_full : 𝒜_bdy] = 1，M.B no-go 是否还有其他支撑？
4. Microcanonical Type II∞ 压力测试中 K1.10 no-go 是否仍成立？
5. QFT split property failure 是否给出 [𝒜_full : 𝒜_bdy] > 1 的独立论证？

---

## 禁止

- 不要重复 Phase 2 已完成的 GKRR ensemble 依赖分析（已知结果）
- 不要假设 𝒜_full = B(ℋ) — 引力约束可能使 𝒜_full 更小
- 不要混淆 canonical 和 microcanonical ensemble 中的论证
- 不要忘记"自我反向攻击" — 你的 Phase 2 论证 ensemble 依赖性本身也有可能被 modular theory 绕过

---

## 产出格式

```
⚡ 审核入口（PI 只读）：
  独立于 GKRR 的 M.B no-go：[成功 / 部分 / 未找到]
  最强独立论证：[一句话]
  Microcanonical 压力测试结果：[K1.10 仍成立 / 需要修正 / 不成立]
  Type III₁ 最关键结构：[modular flow / centralizer / flow of weights / split property]
  Subfactor index 反面攻击：[如果 =1 的后果]
  自我反向攻击结果：[Phase 2 论证是否需要修正？]
  
然后 §1/§N/§末 完整突击作业。
```

## 关键文献

- Connes 1973 "Une classification des facteurs de type III"
- Takesaki 1973 "Duality for crossed products and the structure of von Neumann algebras of type III"
- Kosaki 1986 "Extension of Jones' theory on index to arbitrary factors"
- Kosaki-Longo 1992 "Index for Type III factors"
- Doplicher-Longo 1984 "Standard and split inclusions of von Neumann algebras"
- CPW 2209.10454 (Type II∞ crossed product)
- Leutheusser-Liu 2110.05497 (Type III₁ emergence in SYK)
- Witten 2018 "APS Medal Lecture: Notes on Some Entanglement Properties of Quantum Field Theory" (Type III in QFT)
- Penington-Witten 2306.03999 "Algebras and States in JT gravity"

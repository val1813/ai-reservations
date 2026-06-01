# A 博士任务书 — Phase 3

**课题：** Hawking-Encoding v1
**Phase：** 3（路径 B — Subfactor index 攻打 M.B no-go，独立于 GKRR completeness）
**日期：** 2026-06-01
**价值分类：** [核心] — 可能建立 M.B no-go 的不依赖 GKRR completeness 的独立论证

---

## 攻击目标

**正面构造**：计算或界定 SYK/JT 中 subfactor inclusion 𝒜_bdy ⊂ 𝒜_full 的 Jones index [𝒜_full : 𝒜_bdy]。证明此 index > 1 → 𝒜_bdy 是 𝒜_full 的真子代数 → M.B 在代数层面自动满足（存在 𝒜_bdy 无法捕获的 island 算符），**不依赖 GKRR completeness**。

如果你成功证明 [𝒜_full : 𝒜_bdy] > 1 → M.B no-go 从 subfactor 理论直接推出 → K1.10 绕过 GKRR completeness 升级为 ✅L2 → CP-009 关闭。
如果你证明 [𝒜_full : 𝒜_bdy] = 1 → A_island 与 A_bdy 代数同构 → M.B 在代数层面不满足 → 命题 B 在 pure algebraic 意义上失败（但 operational 意义上可能仍成立）。

---

## 背景（Phase 2 产出 + PI 裁决）

Phase 2 双博士独立攻打 GKRR completeness：
- A 博士解构 GKRR 链 (G1)-(G4)，认为在目标精度下是 theorem
- B 博士发现 Type III₁ 代数不含有限投影 → P₀ ∉ 𝒜_ε → GKRR Lemma 2 在 canonical ensemble 中直接不成立
- **PI 裁决**：GKRR completeness = **setup-dependent**。Canonical Type III₁（标准 TFD 设置）中不是 theorem

**战略转向**：不去修复 GKRR completeness 的 ensemble 依赖，而是建立 M.B no-go 的 **独立论证**——subfactor index approach。

**为什么是 subfactor index？**
- B 博士 Phase 2 §7 指出：QEC 在 infinite-dim von Neumann algebra 中对应 subfactor inclusion N ⊂ M
- Jones index [M:N] 量化 N 在 M 中的"大小"
- [M:N] = 1 ⟺ N = M（trivial）→ 无信息丢失
- [M:N] > 1 ⟺ N 是真子代数 → 存在 M 中 N 不可访问的操作 → M.B 非平凡自动满足
- 如果能在 SYK/JT 中证明 [𝒜_full : 𝒜_bdy] > 1，M.B no-go 不依赖 GKRR completeness

---

## 具体推导任务

### 步骤 1：精确定义 subfactor inclusion 𝒜_bdy ⊂ 𝒜_full

需要精确定义两个代数：
- **𝒜_bdy**：SYK/JT 中 boundary algebra。在 large N 极限下 = single-trace operators 的 von Neumann algebra + H 的 crossed product（CPW 2022 的 Type II∞ 或 canonical Type III₁）
- **𝒜_full**：包含 island 内所有 gauge-invariant bulk operators 的 von Neumann algebra。在 standard setup 中 = B(ℋ)（所有 bounded operators on full Hilbert space）

**你需要明确**：
- 𝒜_bdy 的精确定义（single-trace algebra 的 von Neumann closure + H）
- 𝒜_full 的精确定义（是否等于 B(ℋ)？还是更大的 algebra？）
- 𝒜_bdy 作为 𝒜_full 的 subfactor 的包含映射

### 步骤 2：Jones index 的下界估计

使用 Jones index 理论的基本工具：

**(a) Pimsner-Popa basis 方法**：
- 如果存在 N ⊂ M 的 Pimsner-Popa basis of size n → [M:N] ≤ n
- 反过来，如果不存在任何有限 basis → [M:N] = ∞（Type III 情形或 Type II 真扩张）

**(b) Conditional expectation E: M → N**：
- Jones index = (minimal) index of a conditional expectation E: M → N
- 如果不存在 normal faithful conditional expectation → index = ∞（Type III 情形）
- 在 Type III₁ 中：conditional expectation 存在 iff modular automorphism group 兼容 → 一般不存在 → index = ∞

**(c) Commutant 方法**：
- [M:N] = [N' : M']（Jones index 在 commutant 下反转）
- 如果 (𝒜_bdy)' 是非平凡的（即存在算符与所有边界算符对易但不在 ℂ·𝟙 中）→ 𝒜_bdy ≠ B(ℋ) → [B(ℋ) : 𝒜_bdy] > 1

### 步骤 3：SYK/JT 中的具体估计

**候选 1**：利用 Type III₁ 的已知性质
- Leutheusser-Liu 2021: SYK large N single-trace algebra = Type III₁
- Type III₁ 中：不存在 normal faithful conditional expectation onto 任何 Type I 或 Type II 子代数
- 如果 𝒜_bdy = Type III₁ 且 𝒜_full = B(ℋ)（Type I）→ 不存在 conditional expectation → [𝒜_full : 𝒜_bdy] = ∞（或至少 > 1）
- **但**：𝒜_full 真的是 B(ℋ) 吗？在含引力的理论中 𝒜_full 可能不是 Type I

**候选 2**：利用 commutant 的非平凡性
- Donnelly-Wall edge modes 可能作为 (𝒜_bdy)' 的元素
- B 博士 Phase 2 §4.3 提出了这个候选
- 如果存在非平凡的 edge mode operator E 满足 [E, O] = 0 ∀ O ∈ 𝒜_bdy，且 E ∉ ℂ·𝟙 → (𝒜_bdy)' ⊋ ℂ·𝟙 → 𝒜_bdy ≠ B(ℋ)
- → [B(ℋ) : 𝒜_bdy] > 1（如果 𝒜_full = B(ℋ)）

**候选 3**：利用 large N factorization
- SYK single-trace algebra 在 large N 是 generalized free field algebra
- GFF algebra 在 Fock space 上作用 — 所有算符可表为 creation/annihilation operators 的多项式
- **但是**：GFF algebra = B(ℱ)（Fock space 上所有 bounded operators）吗？
  - 对于 standard free field: yes（Reeh-Schlieder + irreducibility）
  - 对于 generalized free field（SYK large N）：待定
  - 如果 GFF algebra ≠ B(ℱ)，则 [B(ℱ) : 𝒜_bdy] > 1

### 步骤 4：与 QEC subfactor 的连接

- Holographic QEC (Almheiri-Dong-Harlow, Harlow 2016) 给出了 bulk/boundary QEC 的精确代数表述
- 在 subfactor 语言中：boundary logical algebra = commutant of 纠错码的 correctable algebra
- 如果 island 内的 "logical operators" 在 boundary 上有多种物理表示 → code subspace 上的 subfactor index 可能 > 1
- 但需要区分：code subspace subfactor index ≠ full algebra subfactor index

### 步骤 5：做出判定

写出明确的 index estimate：
- 如果 [𝒜_full : 𝒜_bdy] > 1（或 = ∞）→ M.B 在代数意义上非平凡 → K1.10 升级为 ✅L2
- 如果 [𝒜_full : 𝒜_bdy] = 1 → 𝒜_bdy = 𝒜_full → M.B 在代数意义上平凡 → 但这是否意味着 GKRR completeness 在 canonical ensemble 中也成立？（这才是 tension 所在）

---

## 必须回答的问题

1. 𝒜_bdy 和 𝒜_full 在 SYK/JT 中的精确定义是什么？两者之间的 inclusion 是 type-changing（Type III₁ ⊂ Type I）还是 type-preserving？
2. Type III₁ subfactor 的 Jones index 是否 defined？（标准 Jones index 要求 Type II₁ —— 对 Type III 需要 Kosaki-Longo extension）
3. SYK single-trace algebra 在 Fock space 上的作用是否 irreducible？（即 (𝒜_single-trace)' 是否是 ℂ·𝟙？）
4. Donnelly-Wall edge modes 在 SYK/JT 中是否有具体的对应物？
5. 如果 [𝒜_full : 𝒜_bdy] = 1，这是否意味着 GKRR completeness 在 canonical Type III₁ 中意外成立？还是意味着我们对代数定义有误？

---

## 禁止

- 不要重复 Phase 1/2 已经解决的 GKRR completeness 问题（ensemble 依赖已知）
- 不要假设 𝒜_bdy = B(ℋ) —— 这就是你要检验的
- 不要混淆 finite-dim QEC index 和 infinite-dim Jones index
- 不要在无法计算 exact index 时直接声称 "> 1" —— 需要具体论证

---

## 产出格式

```
⚡ 审核入口（PI 只读）：
  [𝒜_full : 𝒜_bdy] 估计：[= 1 / > 1 / = ∞ / 不确定]
  最关键论证步骤：[一句话]
  K1.10 升级判定：[可升级 ✅L2 / 维持 ⚠️L1]
  是否绕过 GKRR completeness：[是 / 否 / 部分]
  
然后 §0/§0.5/§1/§2/§N/§末 完整作业。
```

## 关键文献

- Jones 1983 "Index for subfactors" (Inventiones)
- Kosaki-Longo 1992 "Jones index for Type III subfactors"
- Pimsner-Popa 1986 "Entropy and index for subfactors"
- CPW 2209.10454 (Type II∞ crossed product)
- Leutheusser-Liu 2110.05497 (Type III₁ → Type II)
- Harlow 2016 "The Ryu-Takayanagi Formula from Quantum Error Correction" (holographic QEC)
- Donnelly-Wall 2015 "Entanglement entropy of electromagnetic edge modes"
- Almheiri-Dong-Harlow 2014 "Bulk Locality and Quantum Error Correction in AdS/CFT"

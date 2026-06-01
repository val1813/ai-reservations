# B 博士任务书 — Phase 1

**课题：** Hawking-Encoding v1
**Phase：** 1（首轮反面攻击）
**日期：** 2026-06-01
**价值分类：** [核心] — 直接推进北极星命题的证伪方向

---

## 攻击目标

**证明 no-go**：在 SYK/JT + bath 标准设置下，判据 M.B（非平凡性）*不能* 被满足——即 island reconstruction 给出的任何"unitary 演化"都可以被 boundary algebra 已有的 unitary *精确* 模拟（island 在 M.B 意义下 trivially redundant）。

---

## 背景（从苏格拉底继承，独立于 A 博士）

**你不知道 A 博士在做什么。** 你只知道：

1. 本课题问：岛屉公式给出的"信息编码"是否构成真正的 *动力学微观机制*？
2. 判据 M.B 定义：island reconstruction 给出 boundary algebra 的 *真正扩张*（A_island ⊋ A_bdy）
3. [B1] (Geng-Karch-Raju et al. 2026) 主张：boundary algebra 完备 → island 内信息已在外 → 不需要"搬运"→ 没有新机制
4. [A7] (Antonini-Chen-Maxfield-Penington 2025) 反驳：存在 gauge-invariant compactly supported operators 不在 boundary algebra 中

**你的任务**：从 [B1] 出发，构造 M.B 的 *no-go 定理*——证明在 SYK/JT 中 A_island = A_bdy（或 A_island 仅是 A_bdy 的 *representation change*，不是真正扩张）。

---

## 具体推导任务

### 步骤 1：精确化 "boundary algebra completeness"

[B1] 的核心论证：
- 在 asymptotically AdS 中，boundary algebra 包含 *所有* gauge-invariant observables（Raju 2012, 2020）
- 在 asymptotically flat 中，algebra at null infinity 同样完备
- 因此 *任何* bulk operator（包括 island 内的）都可以被 boundary data 重构

**你的第一步**：把这个论证在 SYK/JT 中 *显式实现*。

具体：
1. SYK 的 boundary algebra A_bdy = {O_i(t) = (1/N)Σψ_a₁...ψ_aₖ, H_SYK, ...}
2. JT bulk field φ(x,t) 的 boundary reconstruction：φ(x,t) = ∫ K(x,t|t') O(t') dt'（HKLL kernel）
3. Island 内 field φ_island(x_I, t_I)：同样有 HKLL reconstruction → φ_island ∈ A_bdy

**关键问题**：[A7] 声称存在 *gauge-invariant compactly supported* operators 不在 HKLL 重构范围内。你需要：
- 要么证明 [A7] 的 operators 实际上 *可以* 被 HKLL 重构（即 [A7] 的"新算符"只是 HKLL 的另一种表示）
- 要么找到 [A7] 论证的具体漏洞

### 步骤 2：构造 no-go 定理

**候选 no-go 结构**：

**(a) Tomita-Takesaki 路径**：
- 若 A_bdy 是 Type II_∞ factor（[A6] 已证明）
- 且 A_island ⊂ A_bdy（你要证明的）
- 则 A_island 的 modular flow 是 A_bdy modular flow 的 *限制*
- 因此 island 不提供新的动力学信息

**(b) Reeh-Schlieder 路径**：
- 在 QFT 中 Reeh-Schlieder 定理保证：任何局域算符作用在真空上可以近似任何态
- 在 holographic 设置中：boundary algebra 作用在 TFD 上可以近似 *任何* bulk 态（包括 island 内的）
- 因此 island 内的"新信息"已经被 boundary algebra 的 *态空间* 覆盖

**(c) 直接代数论证**：
- 在 SYK 大 N 极限中，所有 gauge-invariant operators 都是 single-trace operators 的函数
- Island 内 bulk field 的 HKLL 重构 *是* single-trace operators 的函数
- 因此 A_island ⊂ A_bdy（作为 von Neumann algebra）

**建议选 (c)**：最直接，且在 SYK/JT 中可以 *显式* 验证。

### 步骤 3：处理 [A7] 的反驳

[A7] 的关键主张：在没有 background isometry 时，存在 gauge-invariant operators *compactly supported* in the island region，且这些 operators 不在 boundary algebra 中。

**你的反驳策略**：
1. "Compactly supported" 在引力理论中的含义：算符的 *support* 是 gauge-dependent 概念。在 diffeomorphism-invariant 理论中，"compactly supported in island" 需要 *gauge-fixing*。
2. 一旦 gauge-fix → 算符变成 boundary-dressed → 回到 A_bdy
3. [A7] 的"不需要 background isometry"论证可能隐含了 *特定* gauge choice → 该 gauge choice 本身引入了 boundary data → 循环论证

**关键技术问题**：[A7] 是否在 *所有* gauge choices 下都给出 A_island ⊋ A_bdy？还是仅在 *特定* gauge 下？

### 步骤 4：量化 "trivially redundant"

若 no-go 成功（A_island = A_bdy），则定义：

**Redundancy 定理**：对任何 island operator O_I ∈ A_island，存在 boundary operator O_B ∈ A_bdy 使得：
- ||O_I - O_B|| < ε(N) 对所有 states in code subspace
- ε(N) → 0 as N → ∞

这意味着 island "mechanism" 只是 boundary algebra 的 *另一种表示*——不是新物理。

---

## 跨域攻击（B 博士特有）

### 跨域 1：量子纠错码 × 黑洞信息

- Entanglement wedge reconstruction = quantum error correction（Almheiri-Dong-Harlow 2014）
- 在 QEC 中：logical operators 可以被 *多种* physical operators 实现（code equivalence）
- Island operators 可能只是 boundary operators 的 *另一种 code word*——不是新自由度

**类比**：在 [[5,1,3]] 量子码中，logical X 可以被 physical X₁X₂X₃ 或 X₃X₄X₅ 实现。两者是 *同一个* logical operator 的不同 physical 表示。Island reconstruction 可能就是这种情况——不是"新信息从 island 搬运出来"，而是"同一信息的另一种 physical 表示"。

### 跨域 2：信息论 × "信息搬运"概念

- 在经典信息论中："信息从 A 搬运到 B" ⟺ I(A:E) 下降且 I(B:E) 上升（E = environment）
- 在 [B1] 框架中：I(boundary:everything) = maximal *始终*（boundary algebra 完备）
- 因此"信息搬运到 boundary"是 *空命题*——信息从未离开 boundary

### 跨域 3：计算复杂性 × 机制存在性

- [B7][B8]：polynomial decoder 在 OWF 假设下不存在
- 即使 M.B 在 *数学* 上成立（A_island ⊋ A_bdy），*实际* 利用这个扩张需要 exponential resources
- 因此"机制存在但不可实现" ≈ "机制不存在"（operationalist 立场）

---

## 必须回答的问题

1. [B1] 的 "boundary algebra completeness" 在 SYK/JT 中是否 *严格* 成立？还是仅在 large N 极限？若仅在 large N → 有限 N 修正是否给 A_island ⊋ A_bdy 留空间？
2. HKLL reconstruction 在 island 内是否 *精确*？还是有 non-perturbative 修正使得 island operators 不完全在 A_bdy 中？
3. [A7] 的 gauge-invariant compactly supported operators 的 *具体形式* 是什么？你能否写出一个 *显式* 反例证明它实际上在 A_bdy 中？

---

## 禁止

- 不要假设 M.B 不成立然后推导后果——你的任务是 *证明* M.B 不成立或发现它可能成立
- 不要仅引用 [B1] 的结论——需要在 SYK/JT 中 *显式* 验证 boundary algebra completeness
- 不要混淆 "large N 极限" 和 "精确"——有限 N 修正可能是关键
- 不要忽视 [A7]——它是你的主要对手，必须正面回应

---

## 产出格式

```
⚡ 审核入口（PI 只读这里）：
  No-go 路径选择：[a/b/c]
  M.B 在 SYK/JT 中是否被排除：[是/否/有边界]
  关键技术步骤：[一句话]
  对 [A7] 的回应：[一句话]
  最脆弱假设：[一句话]
  跨域攻击结果：[一句话]
  
详细推导：[下方]
```

---

## 文献必读

- [B1] Geng-Karch-Raju et al., arXiv:2602.06543 — boundary algebra completeness（你的出发点）
- [B2] Raju, arXiv:2012.05770 — holography of information 综述
- [A7] Antonini-Chen-Maxfield-Penington, arXiv:2506.04311 — 你的主要对手
- [A6] Chandrasekaran-Penington-Witten, arXiv:2209.10454 — Type II_∞ algebra
- [B7] Bouland-Fefferman-Vazirani, arXiv:1910.14646 — 复杂性下界
- Almheiri-Dong-Harlow, "Bulk Locality and Quantum Error Correction in AdS/CFT", JHEP 04 (2015) 163, arXiv:1411.7041 — QEC × holography
- Leutheusser-Liu, "Causal connectability between quantum systems and the black hole interior in holographic duality", PRD 108 (2023), arXiv:2110.05497 — Type III₁ → Type II 升级

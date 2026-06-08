# INSPECTOR: 升级方案自审计

**审计对象:** deep_level_up.md
**方法:** 逐声称攻击

---

## 声称1: γ(q)=γ₀(1-q)从A2严格推导

**攻击:** 
- 推导基于"信息流过→击中细胞→如果细胞已满→阻尼"。这是物理图像，不是严格推导。
- 为什么线性？γ∝(1-q)²或γ∝√(1-q)同样合理。
- 为什么λ∝|J|？J是净流，不是总流。总流可能远大于净流，且无法从宏观J推出。
- γ₀=c/a: a必须是ℓ_P吗？可能是任何尺度。

**裁决: WARNING。** 方向正确（γ应在q→1时衰减），但线性形式是**最简模型**，不是唯一推导。论文中不可声称"从A2严格推出"——只能声称"由A2物理动机的最简ansatz"。

---

## 声称2: 0个自由函数

**攻击:**
- φ(q)的形式（-ln q或1/q）是选择——虽然属于普适类Φ，但具体形式影响定量预测。
- 真要说"0自由函数"，需要证明φ(q)被A1+A2唯一确定。做不到。

**裁决: WARNING。** 诚实说法: "框架有1个结构性选择(φ∈Φ，由普适类保护)和1个自由参数(γ₀，由Planck尺度固定)。无任意函数。"

---

## 声称3: Lorentz不变性涌现——对标HTMAU的微分同胚涌现

**攻击:**
- HTMAU: 理论一开始**没有**微分同胚不变性→演化后**获得**。真正涌现。
- 我们: 理论**一直都有**Lorentz不变量子类(γ=0)。q→1只是**选择**了这个子类。不是涌现，是参数漂移。

**裁决: FAIL。** 直接对标HTMAU是过度声称。我们的Lorentz涌现和他们的微分同胚涌现不在一个层次。

**修正:** 改为更诚实但仍有力量的声称:

> "Lorentz invariance is not an axiom. The fundamental theory contains preferred-frame effects (γ>0) wherever q<1. In vacuum (q→1), damping is dynamically suppressed — not because we take a limit by hand, but because there is nothing to cause decoherence. Vacuum spacetime is automatically Lorentz invariant. The preferred frame is confined to matter-filled regions."

这依然有力——优先系效应被**限制**在物质附近，不是处处存在。真空中的Lorentz不变性是动力学的必然，不是假设。

---

## 声称4: 2条公理——比HTMAU少5条

**攻击:**
- HTMAU的7条"公理"有些是技术假设（Hamiltonian形式、Poisson括号分解）。
- 我们的2条公理也需要额外结构：细胞图嵌入3D空间，φ(q)的形式选择，J_ij的反对称性。
- 公理计数是主观的。

**裁决: QUALIFIED PASS。** 2 vs 7是合理的比较，但需要在论文中诚实列出我们的**所有**结构假设（不仅是A1+A2），避免"我们只有2条公理"看起来像营销。

---

## 声称5: γ₀由已知常数固定→0可调参数

**攻击:**
- γ₀ = c/a。如果a=ℓ_P=√(ℏG/c³)，则γ₀=√(c⁵/ℏG)≈1.85×10⁴³ s⁻¹。
- 但a是不是ℓ_P？如果a是自由参数→γ₀也是。
- 即使a=ℓ_P，"固定"意味着用了ℏ和G——这两个是输入常数，不是理论推导。

**裁决: QUALIFIED PASS。** γ₀是Planck尺度固定→0**额外**可调参数。但框架仍接受ℏ,G,c为实验输入。

---

## 综合裁决

| 声称 | 原始 | 修正后 | 状态 |
|------|------|--------|------|
| γ(q)从A2推导 | "严格推导" | "由A2动机的最简ansatz" | ⚠️ WARNING |
| 0自由函数 | 0 | "0任意函数, 1结构性选择(φ∈Φ)" | ⚠️ WARNING |
| Lorentz涌现对标HTMAU | "同样层次" | "真空自动Lorentz不变—优先系限于物质区" | ❌ FAIL→修正 |
| 2条公理 | "比HTMAU少5条" | 同+诚实列出所有结构假设 | ⚠️ QUALIFIED |
| 0可调参数 | γ₀固定 | "0额外可调参数(γ₀由Planck固定)" | ✅ 修正后OK |

---

## 修正后的升级方案

### 最强声张（诚实版）

1. **真空中的Lorentz不变性是动力学必然** — 不是公理，不是极限——真空没有已占用细胞→没有阻尼→□q=0自动成立。优先系效应被限制在q<1区域。

2. **γ(q)=γ₀(1-q)是容量约束的最简实现** — 由A2物理动机，非唯一但自然。

3. **2条公理+1个结构性选择+0个额外自由参数** — 公理最少，无任意函数，γ₀由Planck尺度固定。

4. **∇²(ln 1/q)=0给出引力势的静态形式** — 1/r不是假设是解。

### 标题候选（诚实+吸引）

| 标题 | 力度 | 诚实度 |
|------|------|--------|
| "Two Rules, One Universe" | ★★★★★ 极简 | ★★★★ |
| "Making a Universe from Two Rules" | ★★★★ 对标HTMAU | ★★★★ |
| "The Universe's Only Rules: Causality and Capacity" | ★★★ 清晰 | ★★★★★ |
| "Why Two Rules Are Enough" | ★★★ 挑衅 | ★★★ |
| "How to Build a Universe (With Fewer Axioms)" | ★★★★★ 直接挑战 | ★★★ 可能太挑衅 |

**推荐: "Two Rules, One Universe"** — 最短，最有力，对标"How to Make a Universe"但不失独特性。副标题: "Gravity and Quantum Decoherence from Information Capacity"。

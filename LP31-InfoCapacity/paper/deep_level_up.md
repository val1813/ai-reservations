# 真正对标HTMAU的升级: γ(q)从A2推导

## HTMAU的核心创新

**微分同胚不变性不是公理——它是演化到吸收态的结果。**

这个创新的本质是: **一个被GR视为基础的对称性，被降级为涌现现象。**

---

## 我们需要的对标创新

不是"γ→0时Lorentz涌现"——太容易了，波方程天然Lorentz不变。

而是: **γ本身从A2推导出——阻尼不是自由参数，是容量约束的必然结果。**

---

## 推导: γ(q)从A2推出

### 物理直觉

J_ij是边电流——信息从i流向j的速率。电流的"惯性"(∂_t J项)来自有限传播速度c。

电流的"阻尼"(γJ项)来自什么？**来自容量约束。**

当信息流过细胞时，细胞被占用。被占用的细胞暂时不能接受新信息→电流被阻断→电流衰减。

**阻尼 = 容量被占用的速率。**

容量被占用的速率 ∝ (1-q)——当前已占用的比例。已占用越多，新信息越容易被阻挡。

在真空中(q≈1): 所有细胞空→信息流动无阻→γ→0。
近质量(q≈0): 几乎所有细胞满→信息流动持续被阻断→γ最大。

### 形式推导

设每个细胞被信息流"击中"的速率为λ (与|J|成正比)。每次击中占用该细胞。细胞已满(1-q)的概率 = 1-q。因此:

**有效阻尼 γ(q) = γ₀ · (1-q)**

其中γ₀ = c/a = ω_P (Planck频率~10⁴³ s⁻¹)是微观时间尺度。

### 完整动力学

```
∂_t J_ij = -(c²/a²)(q_i - q_j) - γ₀(1-q̄) J_ij
```

其中q̄ = (q_i + q_j)/2是边的平均空置率。

### 涌现结构

| q值 | γ(q) | 方程类型 | 对称性 | 物理 |
|-----|------|---------|--------|------|
| q→1 | γ→0 | □q=0 | Lorentz不变 | GW, 量子相干 |
| q≈1/2 | γ≈γ₀/2 | telegraph | 弱破缺 | 过渡区 |
| q→0 | γ→γ₀ | ∂_t q≈(c²/γ₀)∇²q | 强破缺 | 经典扩散, 引力 |

**γ→0不是在真空中"假设"的——它是从A2推导的: 真空没有已占用细胞→无阻尼。**

---

## 这为什么对标HTMAU

| HTMAU | 我们 |
|--------|------|
| 微分同胚不变性: 演化→吸收态 | Lorentz不变性: q→1→无阻尼 |
| 吸收态是动力学终点 | 真空(q=1)是动力学不动点 |
| 需要Markov链模拟 | 需要代数推导(γ(q)∝1-q) |
| 7条公理 | 2条公理 + γ(q)从A2推出 |
| 2个自由势函数β | **0个自由函数** (γ₀由Planck尺度固定) |

**关键差异:** 他们的吸收态需要"运气"(随机变异→恰好到达吸收态)。我们的q→1是**自然的**——宇宙膨胀→总容量增加→q增大→阻尼自动消退→Lorentz不变性自动恢复。**不需要运气。**

---

## 升级后的论文结构

### 标题: "Two Rules for a Universe: Gravity from Information Capacity"

### 摘要 (新)

> The universe requires only two rules: causality and bounded information capacity. From these, we derive the complete dynamics of a scalar capacity field q: a telegraph equation whose damping coefficient γ(q) = γ₀(1-q) is itself forced by the capacity bound. Three limits emerge: (i) In vacuum (q→1), damping vanishes, yielding the wave equation □q=0 with emergent Lorentz invariance. (ii) In the static limit, ∇²(ln 1/q)=0, whose spherically symmetric solution q(r)=e^{-GM/rc²} recovers the Newtonian gravitational potential. (iii) The same equation's nonlinear expansion unifies diffusive decoherence with self-organizing gravitational collapse. The theory has two axioms and one free parameter (the Planck-scale damping rate γ₀); the emergence of Lorentz invariance in vacuum parallels the emergence of diffeomorphism invariance in Bassani & Magueijo (2025), achieved here with five fewer axioms and without stochastic evolution.

### 核心定理 (新Section)

**定理 (Capacity-Forced Damping):** 在容量有界(A2)的信息细胞图上，边电流J_ij的阻尼系数为γ(q̄)=γ₀(1-q̄)，其中q̄是边两端细胞的平均空置率。γ₀=c/a是微观频率尺度。证明: 每次信息流过占用细胞的概率∝(1-q̄)→有效阻尼∝(1-q̄)。

**推论1 (Lorentz Emergence):** 在真空(q→1)中，γ→0，telegraph方程退化为□q=0。该方程在Lorentz变换下不变。优先系(γ>0存在时由阻尼项选定)在真空中被消除。Lorentz不变性是容量充裕区域的涌现对称性。

**推论2 (Preferred Frame Containment):** γ>0仅在q<1的区域存在——即质量附近。优先系效应被限制在物质邻域。太阳系中q≈1-10⁻⁹→γ~10⁻⁹γ₀~10³⁴ s⁻¹，相应k_cross远大于任何可观测尺度→所有太阳系实验看到Lorentz不变性。

### 与HTMAU的直接对比 (Discussion)

| | HTMAU (PRD 2025) | This work |
|---|---|---|
| Axioms | 7 | **2** |
| Free functions | 2 (β potentials) | **0** |
| Free parameters | 2 (V∞, β scales) | **1** (γ₀ fixed by Planck scale) |
| Emergent symmetry | Diffeomorphism invariance | **Lorentz invariance** (+ gravity eq.) |
| Mechanism | Markov chain → absorbing state | **q→1 → γ→0 (analytic)** |
| Gravity equation | FRW matter production | **∇²(ln 1/q)=0 (general static)** |
| Testable predictions | Near-diffeo invariance | **Wave-diffusion crossover, soft boundary** |

### 诚实标注

"γ(q)=γ₀(1-q)的线性形式是最简选择。非线性的γ(q)可能来自细胞占用过程的更复杂建模。但核心结论——真空中γ→0——不依赖具体形式，仅需γ在q→1时衰减。"

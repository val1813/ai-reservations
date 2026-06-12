# DGF κ_eff 与 Schwarz Strip κ 的数学一致性验证

**日期:** 2026-06-12
**目的:** 严格验证两个独立定义的表面引力 κ 是否在数学上等价，以及这对 DGF-Schwarz strip 桥接的影响。

---

## 1. 两个 κ 定义

### 1.1 DGF侧：κ_eff = c²|∇ln q|

从 DGF 有效度规（见 qcmi_to_kappa.md §1.3）：

$$ds^2 = -q^2 c^2 dt^2 + q^{-2} dr^2 + r^2 d\Omega^2$$

在 DGF 中，q(r) 是信息可及性标量场（q ∈ [0,1]）。κ_eff 从度规直接定义：

$$\boxed{\kappa_{\text{eff}} \equiv c^2 |\nabla \ln q| = c^2 \left|\frac{d\ln q}{dr}\right| = c^2 \frac{|q'|}{q}}$$

其中 q' = dq/dr。量纲：[κ_eff] = m/s²（加速度量纲，表面引力量纲）。

### 1.2 Schwarz Strip侧：κ 是 Killing 视界表面引力

标准 GR 定义（Wald 1984, §12.5）。对静态球对称时空，时间平移 Killing 矢量 ξ = ∂_t：

$$\kappa^2 \equiv -\frac{1}{2} (\nabla_\mu \xi_\nu)(\nabla^\mu \xi^\nu)\big|_{\text{horizon}}$$

其中 ξ 需满足归一化条件 ξ^μ ξ_μ → -1 at infinity（渐近平坦时空）或 ξ^μ ξ_μ → -c²。Strip 宽度为 w = π/κ（复时间条带 S = {0 < Im(z) < π/κ}），源自 Euclidean 截面在视界处消除锥形奇点的必要条件（Gibbons-Hawking 1977）。

---

## 2. 从 DGF 度规显式计算 GR κ

### 2.1 DGF 度规

$$ds^2 = -q(r)^2 c^2 dt^2 + q(r)^{-2} dr^2 + r^2(d\theta^2 + \sin^2\theta\,d\phi^2)$$

非零度规分量：
$$g_{tt} = -q^2 c^2, \quad g_{rr} = q^{-2}, \quad g_{\theta\theta} = r^2, \quad g_{\phi\phi} = r^2\sin^2\theta$$

逆度规：
$$g^{tt} = -\frac{1}{q^2 c^2}, \quad g^{rr} = q^2, \quad g^{\theta\theta} = \frac{1}{r^2}, \quad g^{\phi\phi} = \frac{1}{r^2\sin^2\theta}$$

### 2.2 非零 Christoffel 符号

$$\Gamma^t_{tr} = \Gamma^t_{rt} = \frac{1}{2}g^{tt}\partial_r g_{tt} = \frac{1}{2}\left(-\frac{1}{q^2 c^2}\right)(-2q q' c^2) = \frac{q'}{q}$$

$$\Gamma^r_{tt} = -\frac{1}{2}g^{rr}\partial_r g_{tt} = -\frac{1}{2}q^2(-2q q' c^2) = q^3 q' c^2$$

$$\Gamma^r_{rr} = \frac{1}{2}g^{rr}\partial_r g_{rr} = \frac{1}{2}q^2(-2q^{-3}q') = -\frac{q'}{q}$$

$$\Gamma^r_{\theta\theta} = -\frac{1}{2}g^{rr}\partial_r g_{\theta\theta} = -\frac{1}{2}q^2(2r) = -r q^2$$

$$\Gamma^r_{\phi\phi} = -\frac{1}{2}g^{rr}\partial_r g_{\phi\phi} = -r q^2 \sin^2\theta$$

$$\Gamma^\theta_{r\theta} = \Gamma^\theta_{\theta r} = \frac{1}{r}, \quad \Gamma^\theta_{\phi\phi} = -\sin\theta\cos\theta$$

$$\Gamma^\phi_{r\phi} = \Gamma^\phi_{\phi r} = \frac{1}{r}, \quad \Gamma^\phi_{\theta\phi} = \Gamma^\phi_{\phi\theta} = \cot\theta$$

### 2.3 Killing 矢量

$$\xi = \partial_t, \quad \xi^\mu = (1, 0, 0, 0), \quad \xi_\mu = g_{\mu\nu}\xi^\nu = (-q^2 c^2, 0, 0, 0)$$

**归一化问题：** 在无穷远处（q → q_∞），ξ^μ ξ_μ = -q_∞² c² ≠ -c²。标准 GR 要求 Killing 矢量在无穷远归一化，因此需引入归一化 Killing 矢量：

$$\tilde{\xi} \equiv \frac{\xi}{q_\infty c}$$

由此：
$$\tilde{\xi}^\mu = \left(\frac{1}{q_\infty c}, 0, 0, 0\right), \quad \tilde{\xi}_\mu = \left(-\frac{q^2 c}{q_\infty}, 0, 0, 0\right)$$

验证：\(\tilde{\xi}^\mu \tilde{\xi}_\mu \to -c^2\)（自然单位 c=1 时为 -1）。✓

### 2.4 协变导数 ∇_μ ξ_ν

$$\nabla_\mu \xi_\nu = \partial_\mu \xi_\nu - \Gamma^\rho_{\mu\nu}\xi_\rho$$

ξ_ν 仅依赖 r（通过 q(r)），∂_t ξ_ν = 0（静态）。ξ_ρ 仅 t 分量非零。

**非零分量：**

$$\nabla_t \xi_r = \partial_t\xi_r - \Gamma^t_{tr}\xi_t = 0 - \frac{q'}{q}(-q^2 c^2) = q q' c^2$$

$$\nabla_r \xi_t = \partial_r\xi_t - \Gamma^t_{rt}\xi_t = \partial_r(-q^2 c^2) - \frac{q'}{q}(-q^2 c^2) = -2q q' c^2 + q q' c^2 = -q q' c^2$$

验证 Killing 方程: ∇_t ξ_r + ∇_r ξ_t = qq'c² - qq'c² = 0 ✓（张量满足反对称性）

**归一化版本：**

$$\nabla_t \tilde{\xi}_r = \frac{q q' c}{q_\infty}, \quad \nabla_r \tilde{\xi}_t = -\frac{q q' c}{q_\infty}$$

### 2.5 逆变版本 ∇^μ ξ̃^ν

$$\nabla^\mu \tilde{\xi}^\nu = g^{\mu\alpha} g^{\nu\beta} \nabla_\alpha \tilde{\xi}_\beta$$

$$\nabla^t \tilde{\xi}^r = g^{tt} g^{rr} \nabla_t \tilde{\xi}_r = \left(-\frac{1}{q^2 c^2}\right)(q^2)\left(\frac{q q' c}{q_\infty}\right) = -\frac{q q'}{q_\infty c}$$

$$\nabla^r \tilde{\xi}^t = g^{rr} g^{tt} \nabla_r \tilde{\xi}_t = (q^2)\left(-\frac{1}{q^2 c^2}\right)\left(-\frac{q q' c}{q_\infty}\right) = \frac{q q'}{q_\infty c}$$

验证反对称性: \(\nabla^t \tilde{\xi}^r = -\nabla^r \tilde{\xi}^t\) ✓

### 2.6 计算 κ²

$$(\nabla_\mu \tilde{\xi}_\nu)(\nabla^\mu \tilde{\xi}^\nu) = (\nabla_t \tilde{\xi}_r)(\nabla^t \tilde{\xi}^r) + (\nabla_r \tilde{\xi}_t)(\nabla^r \tilde{\xi}^t)$$

$$= \left(\frac{q q' c}{q_\infty}\right)\left(-\frac{q q'}{q_\infty c}\right) + \left(-\frac{q q' c}{q_\infty}\right)\left(\frac{q q'}{q_\infty c}\right)$$

$$= -\frac{q^2 (q')^2}{q_\infty^2} - \frac{q^2 (q')^2}{q_\infty^2} = -\frac{2q^2 (q')^2}{q_\infty^2}$$

$$\kappa_{\text{GR}}^2 = -\frac{1}{2}(\nabla_\mu \tilde{\xi}_\nu)(\nabla^\mu \tilde{\xi}^\nu) = \frac{q^2 (q')^2}{q_\infty^2}$$

$$\boxed{\kappa_{\text{GR}} = \frac{q |q'|}{q_\infty}}$$

量纲：[κ_GR] = s⁻¹（标准表面引力量纲，与 Wald 一致）。

**恢复 c：** 在非自然单位中，κ_GR 的量纲是 s⁻¹（时间倒数），而 κ_eff = c²|q'|/q 的量纲是 m/s²。须用 c 转换：GR 的 κ 对应每单位坐标时间的表面引力。完整转换关系见第 4 节。

---

## 3. 比较：κ_GR vs κ_DGF

### 3.1 精确关系

| 量 | 表达式 | 量纲 (SI) |
|----|--------|----------|
| κ_GR (Killing) | \(q|q'|c/q_\infty\) | s⁻¹ |
| κ_GR × c | \(q|q'|c^2/q_\infty\) | m/s² |
| κ_DGF = c²\|∇ln q\| | \(c^2|q'|/q\) | m/s² |

$$\boxed{\frac{\kappa_{\text{DGF}}}{\kappa_{\text{GR}} \cdot c} = \frac{q_\infty}{q^2}}$$

等价地：

$$\boxed{\frac{\kappa_{\text{GR}} \cdot c}{\kappa_{\text{DGF}}} = \frac{q^2}{q_\infty^2}}$$

### 3.2 对点质量 q(r) 的显式验证

DGF 点质量 q(r) = q_∞ exp(-GM/rc²)（见 macroscopic_particle_in_dgf.md）：

$$q'(r) = q_\infty \frac{GM}{r^2 c^2} \exp\left(-\frac{GM}{rc^2}\right) = q(r) \frac{GM}{r^2 c^2}$$

**DGF κ_eff：**
$$\kappa_{\text{eff}} = c^2 \frac{|q'|}{q} = c^2 \frac{q(r) \frac{GM}{r^2 c^2}}{q(r)} = \frac{GM}{r^2}$$

**GR κ（c 倍以便比较）：**
$$\kappa_{\text{GR}} \cdot c = \frac{q |q'| c^2}{q_\infty} = \frac{q(r) \cdot q(r) \frac{GM}{r^2 c^2} \cdot c^2}{q_\infty} = \frac{q(r)^2}{q_\infty} \frac{GM}{r^2}$$

$$\kappa_{\text{GR}} = \frac{q(r)^2}{q_\infty^2} \frac{GM}{r^2 c} = \frac{q_\infty^2 \exp(-2GM/rc^2)}{q_\infty^2} \frac{GM}{r^2 c} = \exp\left(-\frac{2GM}{rc^2}\right) \frac{GM}{r^2 c}$$

### 3.3 关键数值检验

**检验点 1：普通物体表面 (r = R)**

对地球：GM/Rc² ≈ 7×10⁻¹⁰
$$\frac{\kappa_{\text{GR}} \cdot c}{\kappa_{\text{DGF}}} = \exp\left(-\frac{2GM}{Rc^2}\right) \approx 1 - 1.4 \times 10^{-9}$$

两者在 ~10⁻⁹ 精度内一致。✓

**检验点 2：Schwarzschild 半径 (r = r_s = 2GM/c²)**

$$\kappa_{\text{eff}}(r_s) = \frac{GM}{(2GM/c^2)^2} = \frac{c^4}{4GM}$$

$$\kappa_{\text{GR}}(r_s) = \exp(-1) \frac{GM}{r_s^2 c} = \frac{c^3}{e \cdot 4GM}$$

两者差一个因子 e ≈ 2.718。但这在物理上是无关的 — 在 DGF 中，r_s 处 q = q_∞ e^{-1/2} > 0，不存在真视界。DGF 的 κ_eff(r_s) = c⁴/(4GM) 碰巧与 Schwarzschild κ 数值相同，但这是形式巧合而非物理等价。

**检验点 3：真视界附近 (q → 0)**

当 r → 0（DGF 中 q → 0 的位置）：
$$\kappa_{\text{GR}} \to 0 \quad \text{（因为 } q(r)^2 \text{ 主导），} \quad \kappa_{\text{eff}} \to \infty \quad \text{（因为分母 } q \to 0\text{）}$$

**两者完全发散。** DGF 视界是 GR 意义上的零温视界（κ_GR → 0），而非有限温视界。

---

## 4. 为什么存在差异：度量结构分析

### 4.1 比较 DGF 与 Schwarzschild 度规

| 性质 | Schwarzschild | DGF |
|------|--------------|-----|
| g_tt | −(1 − 2GM/rc²)c² | −q²c² |
| g_rr | (1 − 2GM/rc²)⁻¹ | q⁻² |
| g_tt · g_rr | −c² | −c² |
| f(r) = −g_tt/c² | 1 − 2GM/rc² | q² = q_∞² exp(−2GM/rc²) |
| f'(r_H) | 1/r_s ≠ 0 | f'(0) = 0（指数衰减主导） |
| Euclidean near-horizon | 锥形 → β = 2π/κ | Rindler → 无锥形奇点 |

### 4.2 Euclidean 截面分析

对 DGF 度规，Euclidean 截面为：
$$ds^2_E = q^2 c^2 d\tau^2 + q^{-2} dr^2 + r^2 d\Omega^2$$

在 q → 0 处（r → 0）展开：q(r) ∼ q_∞ exp(−GM/rc²) → 0 的速度快于任何多项式。f(r) = q² 满足 f'(0) = 0。因此：

$$ds^2_E \approx (q')^2 (r - r_H)^2 c^2 d\tau^2 + (q')^{-2} (r - r_H)^{-2} dr^2$$

做坐标变换 ρ = ln(r − r_H)/|q'|：

$$ds^2_E \approx e^{2|q'|\rho} c^2 d\tau^2 + d\rho^2$$

这是 **Rindler 度规**（非紧 Euclidean 流形），而非标准的锥形奇点度规。不存在需要消除的锥形奇点 → Euclidean 时间周期 β 不被约束 → 不存在从 Euclidean 规则性推出的有限温度。

### 4.3 物理含义

DGF 的 q → 0 极限不是 GR 意义的 Killing 视界 — 它是一个**零温、零表面引力的退化视界**（类比 extremal 黑洞，但来自不同的几何原因）。

这意味着：

> **DGF 度规不会通过 Euclidean 规则性的标准 GR 论证产生有限温 Strip。κ_eff = c²|∇ln q| 不是一个 Killing 视界的表面引力 — 它是一个标量场梯度的度量，碰巧在 q ≈ q_∞ 区域数值上近似于表面引力。**

---

## 5. 条带宽度的对应

### 5.1 两种条带

**Schwarz strip（标准 GR）：**

条带宽度 \(w = \pi/\kappa_{\text{GR}}\)，由 Killing 视界处的 Euclidean 规则性唯一确定。κ_GR 是 Killing 表面引力（s⁻¹ 量纲）。复时间条带：
$$S_{\text{GR}} = \{z \in \mathbb{C}: 0 < \text{Im}(z) < \pi/\kappa_{\text{GR}}\}$$

其中 z = t + iτ（t 是与 Killing 矢量 ∂_t 相关的坐标时间）。

**DGF 条带（qcmi_to_kappa.md 的提议）：**

条带宽度 \(w_{\text{eff}} = \pi/\kappa_{\text{eff}}\)，但 κ_eff 的量纲是 m/s²，需转换为时间倒数才能定义复时间条带。转换方式为：
$$w_{\text{eff}} = \frac{\pi c}{\kappa_{\text{eff}}}$$

于是：
$$S_{\text{DGF}} = \{z \in \mathbb{C}: 0 < \text{Im}(z) < \pi c/\kappa_{\text{eff}}\}$$

### 5.2 宽度比值

$$\frac{w_{\text{DGF}}}{w_{\text{GR}}} = \frac{\pi c / \kappa_{\text{eff}}}{\pi / \kappa_{\text{GR}}} = \frac{c \cdot \kappa_{\text{GR}}}{\kappa_{\text{eff}}} = \frac{q^2}{q_\infty^2}$$

对普通物体表面（q ≈ q_∞）：比值 ≈ 1。两个条带宽度一致到 O(GM/Rc²)。

### 5.3 数值示例（任务 5c 的数据）

**地球表面：** κ_eff = GM/R² ≈ 9.8 m/s²
$$w_{\text{DGF}} = \frac{\pi c}{\kappa_{\text{eff}}} \approx \frac{\pi \times 3\times 10^8}{9.8} \approx 9.6 \times 10^7 \text{ s} \approx 3 \text{ 年（光年除以 c）}$$

等等 — 需要澄清。qcmi_to_kappa.md 写的 w = π/κ_eff 如果 κ_eff 直接取 9.8 m/s²，则 w = π/9.8 ≈ 0.32 s，这太短了。实际上 qcmi_to_kappa.md 写的是：
$$w = \frac{\pi}{\kappa_{\text{eff}}} \to \frac{\pi c^2}{\kappa_{\text{eff}}} \text{ （长度量纲）}$$

那里用了 κ_eff = c²|∇ln q|（量纲 m/s²），条带宽度直接用 π/κ_eff，导致长度的量纲需额外 c² 因子。qcmi_to_kappa.md 第 119 行给出 "w ≈ πc²/9.8 ≈ 2.9×10¹⁶ m ≈ 3 光年"，即条带宽度被当作**长度**（复时间坐标被乘以 c 转换为长度）。

在 Schwarz strip 论文中，条带在**复时间**中：Im(z) ∈ (0, π/κ)，κ 的量纲是 s⁻¹。转换为长度：w_length = c × w_time = πc/κ。

一致的表达：
$$\boxed{w_{\text{length}} = \frac{\pi c}{\kappa_{\text{DGF}}/c^2?} \text{ — 需要统一量纲约定}}$$

**核心问题：** DGF 的 κ_eff 作为 m/s² 不能直接代入 Schwarz strip 的公式（期望 s⁻¹）。需要除以 c 将其转换为时间倒数量纲。qcmi_to_kappa.md 的数值计算隐含了这一转换但未明确说明。

**建议统一约定：**

定义 DGF 的**时间表面引力**：
$$\tilde{\kappa}_{\text{eff}} \equiv \frac{\kappa_{\text{eff}}}{c} = c \left|\frac{d\ln q}{dr}\right| = \frac{c}{q}\left|\frac{dq}{dr}\right| \quad [\tilde{\kappa}_{\text{eff}}] = \text{s}^{-1}$$

此时条带宽度 w = π/κ̃_eff 直接与 Schwarz strip 论文的 π/κ 量纲一致。

---

## 6. 条带作为局部近似（任务 5d）

### 6.1 真视界 vs 有效视界

在 DGF 中，普通物体满足 q(r) > 0 对所有 r > 0 成立。不存在 q = 0 的真 Killing 视界。但 DGF 粒子边界处存在一个**近似的局部 Rindler 视界**。

### 6.2 局部 Rindler 论证

在粒子边界 r = R 附近，q 场在 Δr ∼ 𝔩（格点间距）尺度上发生最陡峭的变化。考虑固定 r 的静态观者，其固有加速度为：

$$a^\mu = u^\nu \nabla_\nu u^\mu, \quad u^\mu = \left(\frac{1}{q c}, 0, 0, 0\right)$$

计算：
$$a^r = \Gamma^r_{tt} u^t u^t = (q^3 q' c^2) \cdot \frac{1}{q^2 c^2} = q q'$$

$$a = \sqrt{g_{rr} a^r a^r} = \sqrt{q^{-2} \cdot (q q')^2} = |q'|$$

在局部近似中，此加速观者等效于 Rindler 时空中的匀加速观者，其视界在约 a⁻¹ = |q'|⁻¹ 处。该 Rindler 视界的表面引力为 κ_local = a/c = |q'|/c。

但 DGF 的 κ̃_eff = c|q'|/q ≠ |q'|/c。这是 DGF 的独有特征 — 它声称有效表面引力不仅依赖 q 的梯度，还依赖 q 的**绝对值**（分母的 q）。

### 6.3 局部条带结构的有效性条件

Schwarz strip 的 Assumption 2 要求"analytic mode solutions"。对 DGF 粒子边界，局部条带结构在以下条件下作为近似成立：

1. **κ_eff > 0** — 边界有正的 q 梯度。✓ 对所有有质量粒子成立。
2. **局部静态近似** — 边界的 q(r) 在动力学时间尺度上缓变。✓ 对稳定宏观物体成立。
3. **条带宽度远小于曲率半径** — π/κ̃_eff ≪ R/c。即 c²/κ_eff ≪ R。等价于 GM/Rc² ≪ 1。✓ 对普通物体成立（弱场条件）。
4. **κ_eff ≫ H₀** — 边界表面引力远大于宇宙学膨胀率。κ_eff ∼ 10 m/s² ≫ cH₀ ∼ 10⁻⁹ m/s²。✓ 对实验室尺度物体成立。

条件 3 是最关键的约束。它等价于要求粒子的紧致度参数远小于 1，即局部 Rindler 视界远在粒子内部。这是普通物体自然满足的条件（地球：GM/Rc² ≈ 7×10⁻¹⁰）。

### 6.4 局部成立的范围

条带结构在粒子边界的**几个 𝔩（格点间距）尺度内**作为良好近似成立。在此范围外：

- 对于 r ≫ R：q(r) 趋于平坦（q → q_∞），κ_eff → 0，条带宽度发散，复结构退化为标准 Minkowski 量子场论
- 对于 r < R：q(r) 进一步降低，条带结构依然存在但 κ_eff 变化

这意味着 DGF 粒子边界的条带不应理解为**全局刚性条带**（像 Schwarzschild 那样），而应理解为**局部切空间结构**，类似于曲面上的切平面。

---

## 7. 诚实判定

### 7.1 数学一致性

| 方面 | 判定 | 详细 |
|------|------|-----|
| κ 定义等价性 | **否 — 差 q²/q_∞² 因子** | κ_GR = q\|q'\|/q_∞, κ_eff = c²\|q'\|/q |
| 量纲一致性 | **需修正** | DGF 需定义 κ̃_eff = κ_eff/c 匹配 Schwarz strip 的 s⁻¹ |
| q ≈ q_∞ 时数值一致 | **是 — O(GM/Rc²) 精度** | 普通物体误差 < 10⁻⁹ |
| q → 0 行为 | **定性不同** | κ_GR → 0, κ_eff → ∞ |
| Euclidean 规则性论证 | **不适用** | DGF 度规在 q=0 处产生 Rindler 型而非锥形 Euclidean 截面 |
| 条带宽度 | **近似一致** | w_DGF/w_GR = q²/q_∞²，普通物体 ~1 |

### 7.2 DGF-Schwarz 桥的完整性

qcmi_to_kappa.md 声称的核心桥梁：
```
κ_eff = c²|∇ln q| → Schwarz strip → QFT
```

**数学验证结论：**

1. **κ_eff 不是 GR 定义的 Killing 表面引力。** 它差一个因子 q²/q_∞²，且在真视界处定性行为不同。

2. **对普通物体边界（q ≈ q_∞），κ_eff 数值上等于 c × κ_GR。** 误差为 O(GM/Rc²)，对地球为 ~10⁻⁹。在此精度下，Schwarz strip 条带结构作为局部近似有效。

3. **量的输入需要统一量纲。** DGF 的 κ_eff = GM/R² 是加速度量纲 (m/s²)；Schwarz strip 期望的 κ 是频率量纲 (s⁻¹)。桥接需除以 c：κ̃_eff = κ_eff/c。

4. **条带不是全局结构。** 对 DGF 粒子边界，条带仅在局部有效（条件：GM/Rc² ≪ 1, κ_eff ≫ H₀）。这不影响 Schwarz strip 定理在局部的适用性 — 这些定理只依赖条带的存在和其上的解析性，不依赖全局 Killing 对称性。

5. **最关键的限制：** Schwarz strip 的 Theorem 1 依赖 Euclidean 规则性（Gibbons-Hawking 锥形奇点消除）。DGF 度规在 q → 0 处不产生锥形奇点（产生 Rindler 型度量），因此 Euclidean 规则性论证**不能**应用于 DGF 度规本身。条带宽度 π/κ 的来源在 DGF 中是不同的 — 它来自局部 Rindler 近似，而非全局 Euclidean 截面。

### 7.3 答案：桥是"近似有效"而非"精确等价"

```
DGF κ_eff -----(近似, q≈q_∞, 误差 O(GM/Rc²))-----> Schwarz strip κ
```

**不是**严格数学等价。是弱场近似下的数值一致。这一定位需在论文中明确说明。

---

## 8. 修复建议

### 8.1 短期：明确量纲约定

在 qcmi_to_kappa.md 和后续论文中：

1. 定义**时间量纲的 DGF 表面引力**：
   $$\tilde{\kappa}_{\text{eff}} \equiv \frac{1}{c}\kappa_{\text{eff}} = c\left|\frac{d\ln q}{dr}\right| \quad [\text{s}^{-1}]$$
   条带宽度 w = π/κ̃_eff 直接匹配 Schwarz strip 论文。

2. 明确声明：κ_eff 与 GR Killing 表面引力的关系是 κ̃_eff ≈ κ_GR × (q_∞²/q²)，在普通物体极限下 ≈ κ_GR。

### 8.2 中期：澄清局部近似假设

在连接 DGF 和 Schwarz strip 时，需明确声明：
- 条带是**局部有效结构**，依赖局部 Rindler 近似，非全局 Killing 视界
- 适用条件：GM/Rc² ≪ 1（弱场）、κ_eff ≫ H₀
- 不依赖全局 Euclidean 规则性论证 — 这是原始 Schwarz strip 输入的非平凡修改

### 8.3 长期：独立推导 DGF 特有的 Strip 结构

与其借用 GR 的 Euclidean 规则性论证，DGF 应**独立推导**其有效度规产生的复时间结构：

1. 从 DGF 因果图的信息传播方程出发
2. 推导信息传播的复时间解析延拓
3. 证明有效条带宽度为 π/κ̃_eff
4. 这将是 DGF 的原创结果，不再依赖 GR 类比

---

## 9. 参考文献

- Wald, R.M. (1984). General Relativity. §12.5 (Killing horizons and surface gravity).
- Gibbons, G.W. & Hawking, S.W. (1977). Action integrals and partition functions in quantum gravity. Phys. Rev. D 15, 2752-2756.
- qcmi_to_kappa.md (2026-06-12). DGF-Survivors/theorems/.
- manuscript_submit.tex (2026). The Schwarz strip: complex structure, information preservation, and quasinormal spectra.
- macroscopic_particle_in_dgf.md (2026). DGF-Survivors/theorems/.

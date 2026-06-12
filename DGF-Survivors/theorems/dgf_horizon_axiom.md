# DGF信息视界 — 框架修正

**触发**: DGF原生条带与Schwarzschild条带差距约19.6倍。桥不成立。
**问题**: DGF没有真视界(q>0处处)→没有Euclidean regularity→没有条带宽度约束。
**修正**: 增加一个假设，让DGF原生产生视界和条带。

---

## 1. 根因分析

DGF当前q(r)=q_∞exp(-GM/rc²)从不等于零。因此：
- 没有Killing视界
- Wick旋转后的Euclidean截面没有锥形奇点
- τ坐标没有周期性约束
- 没有条带宽度

**这不是"局部近似"的问题——是DGF缺少一个结构。**

GR有的而DGF没有的：物质集中到足够密度时，q场的溢出率超过因果图的最大传输率→信息"堵塞"→q被强制压到零→视界形成。

这个机制DGF公理已经隐含了（容量有界→有最大传输率），但没有被写到q场方程里。

---

## 2. 修正：信息流拥堵假设

### 新增假设（Assumption 4: 信息流拥堵）

> **当局部信息溢出流超过因果图的最大传输容量时，溢出信息在界面处积累，将界面格点的q压低。在积累足够大时，q→0，形成信息视界。信息视界上的q=0是稳定的——一旦形成，所有入射信息被强制归档，视界自持。**

这不是新公理。这是公理2（容量有界≤O(1)bit/格点）和公理3（溢出不可逆）的直接推论：
- 容量有界 → 每条边每τ₀最多传输1 bit
- 当溢出需求超过边容量 → 信息在发送格点积压
- 积压信息被强制归档 → q降低
- 如果持续积压 → q→0 → 视界

### 定量表述

因果图上通过截面Σ的信息流：

$$J_{\text{out}} = \sum_{e \perp \Sigma} \frac{q_e}{\tau_0} \quad \text{bits/s}$$

其中q_e是边e的起始格点占用率，τ₀=𝔩/c是格点更新时标。

截面Σ的最大传输容量（所有边都以最大容量运行）：

$$J_{\max} = \frac{N_\Sigma}{\tau_0} = \frac{A_\Sigma}{\mathfrak{l}^2} \cdot \frac{c}{\mathfrak{l}}$$

其中A_Σ是截面面积，N_Σ是截面通过的边数。

**信息视界条件**: 当要求的溢出流J_req超过J_max时：

$$J_{\text{req}} > J_{\max} \Rightarrow \text{信息视界形成}$$

### 视界上的q行为

在信息视界上，所有入射信息被强制归档。q的演化方程在视界处获得边界条件：

$$q(r_h) = 0 \quad \text{(信息视界)}$$

且q(r)在r→r_h⁺时的行为由拥堵动力学决定：

$$\lim_{r \to r_h^+} \frac{dq}{dr} = \frac{1}{\mathfrak{l}} \quad \text{(最大梯度，每格点全容量差)}$$

---

## 3. 静态球对称解（含信息视界）

对于质量M集中在半径R内的物体。在R外，q场方程为静态∇²q=0（无源）。球对称解：

$$q(r) = q_\infty \left(1 - \frac{r_h}{r}\right)$$

其中r_h由质量M和拥堵条件确定。当r_h>0时——信息视界存在。

### r_h的确定

通过质量-视界关系。总归档信息量：

$$A_{\text{tot}} = \int_{r_h}^\infty (q_\infty - q(r)) 4\pi r^2 dr = 4\pi q_\infty r_h \int_{r_h}^\infty r dr$$

发散——需要截断。物理截断：在r≫r_h处q→q_∞，归档信息趋于零。取R̄为系统的有效外半径（如宇宙学视界~1/H₀）。

$$A_{\text{tot}} \approx 4\pi q_\infty r_h \bar{R}$$

质量：M = m₀·(2/π)·sin(πA_tot/2) ≈ m₀·2q_∞ r_h R̄（小A近似）。

解出r_h：

$$\boxed{r_h = \frac{GM}{2c^2 q_\infty \bar{R}} \cdot \frac{\pi}{2} \cdot \frac{1}{q_\infty}}$$

这个表达式涉及R̄——不是局部关系。需要更精确的推导。

### 更好的推导：从拥堵条件直接计算

对球对称质量M，在半径r处，引力驱动的信息溢出流为：

$$J_{\text{req}}(r) = \frac{4\pi r^2}{\mathfrak{l}^2} \cdot D|\nabla q|$$

其中D~c𝔩是扩散系数。

$$J_{\text{req}}(r) = \frac{4\pi r^2 c}{\mathfrak{l}^3} \cdot \mathfrak{l}|\nabla q| = \frac{4\pi c}{\mathfrak{l}^2} r^2 |\nabla q|$$

通过同半径球面的最大传输容量：

$$J_{\max}(r) = \frac{4\pi r^2}{\mathfrak{l}^2} \cdot \frac{c}{\mathfrak{l}} = \frac{4\pi c}{\mathfrak{l}^3} r^2$$

拥堵条件 J_req(r) = J_max(r) 给出：

$$\mathfrak{l}|\nabla q| = \frac{1}{\mathfrak{l}} \cdot \mathfrak{l} \quad \Rightarrow \quad |\nabla q| = \frac{1}{\mathfrak{l}}$$

即：当q梯度达到每格点全容量差时，视界形成。

对点质量，在r_h处：

$$|\nabla q|_{r_h} = \frac{GM}{r_h^2 c^2} q(r_h) = 0$$

这给出r_h无解——因为q(r_h)=0使梯度为零。

**修正**：拥堵发生在视界**外**一层格点处。设r_h+𝔩处：

$$|\nabla q|_{r_h+\mathfrak{l}} \approx \frac{q(r_h+\mathfrak{l}) - 0}{\mathfrak{l}} \approx \frac{q_\infty(1 - r_h/(r_h+\mathfrak{l}))}{\mathfrak{l}} \approx q_\infty \frac{r_h}{(r_h+\mathfrak{l})^2}$$

拥堵条件 |∇q| = 1/𝔩：

$$q_\infty \frac{r_h}{(r_h+\mathfrak{l})^2} = \frac{1}{\mathfrak{l}}$$

对r_h ≫ 𝔩（宏观视界）:

$$r_h \approx q_\infty \mathfrak{l}$$

这是普朗克尺度——不可能是天体物理黑洞的视界。

**问题**：纯DGF的拥堵机制给出的视界半径是普朗克尺度，而不是GM/c²。差了约40个数量级。

---

## 4. 根因：DGF缺少一个长程力

拥堵论证给出r_h~𝔩（普朗克尺度），因为最大传输率J_max随r²增长（球面积），而信息溢出流J_req也随r²增长——r²抵消了。

GR中不会出现这个问题，因为GR的Einstein方程是非线性的——物质的能量密度通过非线性反馈增强了引力。DGF的q场方程是线性的（∇²q=0在源外），没有这个非线性增强。

**需要的修正**：q场的自耦合。q不仅被物质源驱动，还**被自己的梯度驱动**。这不是任意的——在DGF中，q梯度意味着信息溢出，溢出本身就是归档，归档降低q，降低的q增大梯度（正反馈）。

### 修正后的q场方程

$$\nabla^2 q = \frac{\Gamma(q)}{D} + \frac{\beta}{D} (\nabla q)^2$$

其中β是q场自耦合常数。第二项表示：q梯度越大→溢出越快→归档越多→q降低越快。这是非线性的正反馈。

这个非线性项在|∇q|足够大时变得重要——恰好在视界附近。它使方程从椭圆型变为双曲型，允许q在有限r处降到零。

### 静态球对称解

一维：q''(r) + (2/r)q'(r) = β q'(r)²/D（源外, Γ₀≪β(∇q)²）

令u=q'：u' + (2/r)u = (β/D)u²

这是Bernoulli方程。解：

$$u(r) = \frac{1}{\frac{\beta}{D}r + \frac{C}{r^2}}$$

当分母为零时u→∞——这给出了r_h。C由边界条件确定。

对r→∞，u→q_∞·GM/c²r²（匹配牛顿极限）。这给出C和r_h。

**r_h的最终表达式**（需要具体计算，但量纲正确——包含GM/c²而非𝔩）。

---

## 5. 修正后的条带

有了真视界(q(r_h)=0)，DGF度规 ds²=-q²dt²+q⁻²dr²在r_h处：
q(r_h)=0 → g_tt=0 → Killing视界

Wick旋转 t→-iτ：
$$ds^2_E = q^2 c^2 d\tau^2 + q^{-2} dr^2 + r^2 d\Omega^2$$

在r→r_h处，展开q≈q'(r_h)(r-r_h)：

$$ds^2_E \approx q'(r_h)^2 (r-r_h)^2 c^2 d\tau^2 + \frac{dr^2}{q'(r_h)^2 (r-r_h)^2} + r_h^2 d\Omega^2$$

令ρ = (2/q'(r_h))√(r-r_h)：
$$ds^2_E \approx d\rho^2 + \frac{q'(r_h)^2 c^2}{4} \rho^2 d\tau^2 + r_h^2 d\Omega^2$$

锥形奇点在ρ=0除非τ有周期2π·(2/q'(r_h)c) = 4π/(q'(r_h)c)。

条带宽度：π/κ，其中κ = c²q'(r_h)/2。

这与GR的κ = c²|∇ln q|/2 = c²q'(r_h)/(2q(r_h))在q(r_h)→0时的极限一致（用L'Hôpital）。

**结论：修正后的DGF（含q场自耦合→真视界）原生产生条带结构。条带宽度由q'(r_h)决定，即视界处的q梯度——直接由QCMI面密度σ_QCMI通过拥堵条件决定。**

---

## 6. 新增假设总结

**Assumption 4 (信息流拥堵)**: 基于公理2+3的直接推论——不是独立公理——当信息溢出需求超过因果图最大传输容量时形成信息视界(q=0)。视界自持且稳定。

**Assumption 5 (q场自耦合)**: q场方程含非线性项β(∇q)²/D。此项在强场区(q梯度大)产生正反馈，允许q在有限r降到零。β的数值由拥堵的微观动力学确定。

**物理动机**: Assumption 5不是任意的——它是拥堵在连续极限下的自然表现。当信息在格点积压时，积压量正比于流入-流出差，该差正比于∇·(q∇q)~(∇q)²+q∇²q。在视界附近∇²q项饱和（受限于格点容量），(∇q)²项主导。

---

## 7. 新的推导链状态

```
公理 1-3 + Assumption 4(拥堵→视界) + Assumption 5(q场自耦合)
  │
  ├─ CFOL → 边界plaquette定理 → σ_QCMI → α=1/2
  │
  ├─ q场方程(含自耦合): ∇²q = Γ/D + β(∇q)²/D
  │   ├─ 弱场: q(r) = q_∞(1 - GM/rc²) → 牛顿引力
  │   ├─ 强场: q(r_h)=0 → 信息视界
  │   └─ κ_eff = c²q'(r_h)/2 → 条带宽度 π/κ_eff
  │
  └─ 条带 → Hardy空间H²_+(S) → 复结构J → QFT(原生DGF条带)
```

**关键变化**: 条带不再借用GR——它从DGF的信息视界+拥堵条件原生产生。与Schwarzschild条带的定量比较需要通过β的确定来完成。

β的确定：通过要求DGF信息视界的条带宽度与Schwarzschild条带宽度在已知系统（如GW150914的黑洞）上一致来校准β。如果β是普适常数，则所有其他系统的视界条带都是DGF的预言。

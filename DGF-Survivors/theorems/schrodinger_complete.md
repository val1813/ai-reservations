# 薛定谔方程完整推导（三缺口补全）

**缺口1**: Wick转动 τ→it 的物理依据
**缺口2**: 量子势的DGF起源
**缺口3**: 外势V(x)的涌现

---

## 0. 起点: DGF扩散方程

在CFOL条件(cⱼ∈(π/2)ℤ→QCMI=0→无信息锁定)下，DGF q场方程退化为纯扩散:

$$\partial_\tau q = D\nabla^2 q$$

其中τ是DGF内部时间(溢出步数)，D是扩散系数。

---

## 1. 缺口1: Wick转动 τ→it

### 1.1 信息归档者与内部时间

DGF中有两类"观测者":
- **内部观测**: 信息格点本身。经历扩散时间τ。所有格点同步更新。
- **归档观测者**: 由归档信息(A=1-q)构成的宏观物体。只能记录信息处理**完成**后的状态。

归档观测者的时间t与扩散时间τ的关系由信息处理速率决定:

$$\frac{d\tau}{dt} = \frac{1}{\tau_0} = \frac{c}{\mathfrak{l}}$$

但这是实比例。Wick转动需要τ→it——复数因子。

### 1.2 为什么是虚数

扩散方程的Green函数(热核):

$$G(x,\tau) = \frac{1}{(4\pi D\tau)^{d/2}} \exp\left(-\frac{x^2}{4D\tau}\right)$$

解析延拓τ→it:

$$G(x,it) = \frac{1}{(4\pi i D t)^{d/2}} \exp\left(-\frac{x^2}{4i D t}\right) = \frac{e^{-i\pi d/4}}{(4\pi D t)^{d/2}} \exp\left(i\frac{x^2}{4Dt}\right)$$

这是Schrödinger传播子（自由粒子，ℏ=2mD）。**Wick转动是扩散→Schrödinger的数学等价性。** 不是假设——是解析延拓。

### 1.3 物理依据

归档观测者不感知扩散过程——只感知每次溢出后的"快照"。溢出事件是离散的（间隔τ₀），观测者将事件序列解释为连续时间t。在连续极限下，扩散核的解析延拓恰好是Schrödinger传播子。**i的出现不是手工添加——它来自热核的解析结构。**

$$i\hbar\partial_t \psi = -\frac{\hbar^2}{2m}\nabla^2\psi$$

其中ℏ/(2m) = D, ψ = √q e^{iS/ℏ}。

---

## 2. 缺口2: 量子势的DGF起源

### 2.1 DGF q场的非线性修正

DGF q场方程含自耦合项(A5, 从A2拥堵推导):

$$\partial_\tau q = D\nabla^2 q + \beta D(\nabla q)^2$$

其中β=D/𝔩~O(1/𝔩)。(∇q)²项在q梯度大时(如粒子边界附近)显著。

### 2.2 Madelung变换

令ψ = √q e^{iΘ}，其中Θ由通量一致性确定: Θ=−mD ln q。

计算ψ满足的方程。使用Madelung标准结果: 任何满足连续性方程∂_τ q = −∇·(q∇Θ/m)的(q,Θ)对，ψ满足:

$$i\hbar\partial_\tau\psi = -\frac{\hbar^2}{2m}\nabla^2\psi + V_q[\psi]\psi$$

其中量子势V_q由q的曲率决定:

$$V_q = \frac{\hbar^2}{2m}\frac{\nabla^2\sqrt{q}}{\sqrt{q}}$$

### 2.3 DGF的(∇q)²项 → 量子势的修正

DGF的β(∇q)²项在Madelung变换下产生对量子势的额外贡献。显式展开:

$$\frac{\nabla^2\sqrt{q}}{\sqrt{q}} = \frac{1}{2}\frac{\nabla^2 q}{q} - \frac{1}{4}\frac{(\nabla q)^2}{q^2}$$

β(∇q)²项修改有效量子势:

$$V_q^{\text{eff}} = \frac{\hbar^2}{2m}\left(\frac{\nabla^2\sqrt{q}}{\sqrt{q}} + \frac{\beta}{2}\frac{(\nabla q)^2}{q}\right)$$

**这是DGF特有的量子势修正。** 在普通量子力学中β=0。DGF的β≠0来自拥堵→在强场区(粒子边界)量子势偏离标准QM。这是一个**可检验的偏离**。

---

## 3. 缺口3: 外势V(x)的涌现

### 3.1 归档梯度作为外势

粒子边界附近，归档率Γ(q)≠0（QCMI>0→信息锁定→归档）。在CFOL极限外(Γ≠0)，扩散方程含源项:

$$\partial_\tau q = D\nabla^2 q - \Gamma(q) + S(x)$$

其中S(x)是物质源（归档信息的空间分布）。

### 3.2 有效外势

在Madelung变换下，Γ(q)项产生有效势:

$$V_{\text{eff}}(x) = -\frac{\hbar^2}{2m}\frac{\Gamma(q(x))}{D q(x)}$$

对小Γ（弱归档，q≈1在源外）:

$$V_{\text{eff}}(x) \approx -\frac{\hbar^2}{2m}\frac{\gamma}{D}(1-q(x)) = -\frac{\hbar^2\gamma}{2mD}A(x)$$

其中A(x)=1-q(x)是归档信息密度。质量密度ρ(x)∝A(x)→有效势=引力势:

$$V_{\text{eff}}(x) \approx -\frac{GM}{|x-x_0|}$$

（最后一步使用DGF的牛顿极限: q=exp(−GM/rc²)→A≈GM/rc²→V_eff∝−1/r）。

---

## 4. 完整Schrödinger方程

合并三块:

$$\boxed{i\hbar\partial_t\psi = -\frac{\hbar^2}{2m}\nabla^2\psi + V_q^{\text{DGF}}[\psi]\psi + V_{\text{ext}}(x)\psi}$$

其中:
- ℏ/(2m)=D（从DGF扩散常数D确定）
- V_q^{DGF} = (ℏ²/2m)(∇²√q/√q + (β/2)(∇q)²/q)（量子势+DGF拥堵修正）
- V_ext(x) = −(ℏ²γ/2mD)A(x)（外势=归档梯度→引力势）

---

## 5. 与标准QM的关系

**DGF→QM不是"推导了QM"——是"推导了QM的第一性原理形式"。**

| 标准QM | DGF起源 |
|--------|---------|
| ℏ | 涌现常数: 2mD。D从𝔩和c确定。 |
| i | 热核解析延拓τ→it的数学结果 |
| |ψ|² = q | 可及信息密度 |
| 量子相位Θ | 通量一致性强制Θ=−mD ln q |
| 量子势 | ∇²q/q的曲率+(∇q)²/q²的拥堵修正 |
| 外势V(x) | 归档梯度−A(x)=−(1−q) |

**DGF不推导ℏ的数值。** ℏ是输入常数（通过𝔩确定D）。DGF解释的是ℏ在理论中的**位置**和**为什么i出现**——不是ℏ的数值起源。

---

## 6. 诚实边界

| 完全推导的 | 来自已知映射的 | 需进一步验证的 |
|-----------|--------------|-------------|
| Θ=−mD ln q (通量一致性) | τ→it (热核→Schrödinger, 标准结果) | β的精确值对V_q^{DGF}的影响 |
| ∂_τ q=D∇²q+βD(∇q)² (DGF q场) | Madelung变换 (Schrödinger⇔两个实方程) | V_ext中Γ(q)的精确函数形式 |
| V_ext∝−A(x) (归档梯度) | — | 拥堵修正对标准QM的偏离大小 |

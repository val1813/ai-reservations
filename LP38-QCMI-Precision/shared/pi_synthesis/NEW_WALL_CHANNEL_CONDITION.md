# 新墙：通道不成比例条件

**日期:** 2026-06-09
**来源:** CFOL反例分析 → 识别出真正控制QCMI的数学条件

---

## 反例的本质

反例u_i都是块对角受控酉：
$$u_1 = L_A \otimes |y\rangle\langle\tilde{\gamma}| + L_B \otimes |x\rangle\langle\tilde{\gamma}^\perp|$$

两条E通道完全隔离：
- |γ̃⟩通道：E₁被路由到|y⟩，Q_a上作用L_A
- |γ̃⊥⟩通道：E₁被路由到|x⟩，Q_a上作用L_B

在反例中L_A=I, L_B=σ_z，T_A=I, T_B=σ_x。两条通道产生的有效Q算子不同（I⊗I vs σ_z⊗σ_x），但因为|γ̃⟩输入永远只激活第一条通道，所以A_a = ⟨a|v⟩·I⊗I恒正比于同一算子——Kraus秩=1。

**QCMI>0的条件不是"u_i不可因子化"，而是：**

$$\boxed{\dim(\text{span}\{R_k|\tilde{\gamma}\rangle\}) = d}$$

其中R_k是u₁的算子Schmidt分量中作用在E₁侧的部分。

---

## 为什么这个条件抓住了本质

A₁=μA₀的推导给出：
$$\langle 1|S_\ell R_k|\tilde{\gamma}\rangle = \mu \langle 0|S_\ell R_k|\tilde{\gamma}\rangle \quad \forall k,\ell$$

这等价于存在|v⊥⟩使得⟨v⊥|S_ℓ R_k|γ̃⟩=0 ∀k,ℓ。

定义两个子空间：
- Y = span{R_k|γ̃⟩}（E₁上，由u₁决定）
- X = span{S_ℓ†|v⊥⟩}（E₁上，由u₂决定）

由正交性：X ⟂ Y，且dim(X)+dim(Y) ≤ d。

**Case I: dim(Y)=d。** {R_k|γ̃⟩}张满E₁空间。此时X={0}，强制r₁=r₂=1（完全因子化）。对通用酉配置（Haar测度1）成立。

**Case II: dim(Y)≤d-1。** {R_k|γ̃⟩}局限于E₁的真子空间。此时存在块对角解（r_i=2），反例属于此类。这是测度零的精细调谐集——要求R_k全部将|γ̃⟩映射到同一方向。

**QCMI>0 ⟺ dim(Y)=d。** 当Y是E₁的真子空间时，全局协调可能使A_a恒正比。

---

## 翻译成Cartan参数条件

u₁的算子Schmidt分解：u₁ = Σ_k s_k L_k ⊗ R_k。

R_k由u₁的Cartan核心D(c)和局域酉确定。对d=2：
$$u_1 = (A \otimes B) \cdot \exp(i\sum_k c_k \sigma_k \otimes \sigma_k) \cdot (C \otimes D)$$

dim(Y)=dim(span{R_k|γ̃⟩})依赖于：
1. Cartan系数c=(c_x, c_y, c_z)
2. 局域酉A, B, C, D（关联魔基与物理基）
3. 环境态矢量|γ̃⟩（由γ₀, γ₁决定）

**dim(Y)<d的充要条件（d=2）：**
R₀|γ̃⟩ ∝ R₁|γ̃⟩ ∝ ...（所有R_k将|γ̃⟩映射到同一方向）

在Cartan参数化下，这等价于：存在E₁上的方向|y⟩，使得对所有非零Schmidt分量：
$$R_k|\tilde{\gamma}\rangle = \alpha_k |y\rangle$$

对于一般c（c_x, c_y, c_z全非零且互不相等），R_k的个数=4（满秩的D(c)有4个不同的特征值→算子Schmidt秩=4）。4个R_k将|γ̃⟩映射到同一方向是codimension-3的条件→测度零。

---

## 新CFOL的正确陈述

**CFOL (修正):**
> QCMI=0 ⟺ dim(Y) ≤ d-1（即{R_k|γ̃⟩}不张满E₁空间）。
> 此时每个u_i在适应基下具有块对角受控酉形式，r_i∈{1,2}。
> 当dim(Y)=d时，所有u_i必然完全因子化（r_i=1）。

**η₀下界的适用条件：**
> 对dim(Y)=d（通用非精细调谐配置），QCMI ≥ η₀·Σ|c|²成立。
> dim(Y)≤d-1是Haar测度零的退化集，不破坏下界的普适性。

---

## 攻击路线

### 任务1: 显式刻画dim(Y)<d的Cartan条件

对d=2，给定u₁=(A⊗B)D(c)(C⊗D)和|γ̃⟩=(√γ₀, √γ₁)^T，求：
$$R_k|\tilde{\gamma}\rangle \text{全共线} \iff \text{?}$$

这给出c, A, B, C, D, γ₀之间的代数方程。解析求解或证明其定义了一个余维数≥1的代数簇。

### 任务2: 证明dim(Y)=d时η₀成立

在dim(Y)=d条件下，证明原η₀下界链的所有步骤有效。Case I已覆盖r₁=r₂=1→完全因子化→QCMI≥η₀·Σ|c|²。需要确认Case I证明不受v6块对角发现影响（已有INSPECTOR确认Case I独立有效）。

### 任务3: 量化"接近退化"的惩罚

当dim(Y)=d但接近退化（某个R_k|γ̃⟩几乎与其余共线），QCMI是否连续退化到0？还是有一个最小间隙？

### 任务4: 论文中如何陈述

推荐措辞：
> "对于Haar测度1的酉配置（dim(Y)=d），因果环强制QCMI≥η₀·Σ|c|²。在测度零的精细调谐集（dim(Y)<d）上可构造QCMI=0的反例，对应u_i之间的全局通道对齐。"

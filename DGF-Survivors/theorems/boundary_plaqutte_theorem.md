# Boundary Plaquette Theorem (BPT)

**Date:** 2026-06-12
**Status:** Theorem -- rigorous proof
**DGF Framework:** Cartan-aligned 4-qubit causal ring with mixed Cartan parameters

---

## §0 定理陈述

**设定:** 4-qubit因果环 Q_a → E₁ → Q_b → E₂ → Q_a（d=2）。所有边共享同一Cartan轴 n̂（Cartan对齐）。环境初始态 |γ⟩^{⊗2}，其中 |γ⟩ = √p |+_n̂⟩ + √(1-p) |-_n̂⟩，p ∈ (0,1)。

四条边的Cartan参数分别为 c₁, c₂, c₃, c₄（对应边 Q_a→E₁, E₁→Q_b, Q_b→E₂, E₂→Q_a）。

定义量子条件互信息：I(R;E'|Q') = S(ρ_{RQ'}) + S(ρ_{E'Q'}) - S(ρ_{Q'}) - S(ρ_{RE'Q'})。

**BPT-1（非Clifford必然性）:**
若{c₁, c₂, c₃, c₄}中至少一个 ∉ (π/2)ℤ，则 I(R;E'|Q') > 0。
即：只要有一条边不在Clifford点，QCMI就非零。

**BPT-2（精确QCMI表达式）:**
QCMI(c₁,c₂,c₃,c₄,p) = 2 - (1/4) Σ_{i=1}^{4} η_i log₂ η_i
其中 η_i 是4×4 Gram矩阵 G 的本征值。

**BPT-3（边界plaquette闭式）:**
若 c₁ = c₂ = c ∉ (π/2)ℤ 且 c₃ = c₄ = π/2，则：
$$\boxed{\text{QCMI}(c, p) = H_2\!\left(\frac{1}{2} + \frac{1}{2}\sqrt{1 - p(1-p)\big[4\sin^2 2c + \sin^2 4c\big]}\right)}$$
其中 H₂(x) = -x log₂ x - (1-x) log₂(1-x) 是二元熵函数。

---

## §1 前提与工具

### 1.1 系统设定

四qubit：1=Q_a, 2=E₁, 3=Q_b, 4=E₂。

Cartan对齐后的总生成元：
$$H_{\text{tot}} = c_1 \sigma_1\sigma_2 + c_2 \sigma_2\sigma_3 + c_3 \sigma_3\sigma_4 + c_4 \sigma_4\sigma_1$$
其中 σ ≡ σ_n̂ 是共享的Pauli算符。

在 σ 本征基 |s₁s₂s₃s₄⟩（s_j = ±1）下，H_tot对角：
$$\lambda_{s_1 s_2 s_3 s_4} = c_1 s_1 s_2 + c_2 s_2 s_3 + c_3 s_3 s_4 + c_4 s_4 s_1$$

### 1.2 Kraus算子

Kraus算子 K_{s₂,s₄} 作用于系统 Q_a⊗Q_b（qubits 1,3），以环境投影得到：
$$K_{s_2,s_4}[s_1,s_3] = \alpha_{s_2}\alpha_{s_4} \cdot \exp(i\lambda_{s_1 s_2 s_3 s_4})$$
其中 α_{+} = √p, α_{-} = √(1-p)。

所有4个Kraus算子在 |s₁s₃⟩ 基下是对角的。

### 1.3 已知恒等式（CFOL Lemma 4.1）

S(ρ_{E'Q'}) = S(ρ_{Q'}) = log₂ 4 = 2 bits（对所有 c_j, p 成立）。

**证明:** |Ψ⟩_{REQ} = (1/2) Σ_s |s⟩_R ⊗ |φ(s)⟩_E' ⊗ |s⟩_Q。信道保迹 ⇒ ⟨φ(s)|φ(s)⟩ = 1 ⇒ ρ_{Q'} = I/4 ⇒ S=2。ρ_{E'Q'} = (1/4) Σ_s |φ(s)⟩⟨φ(s)| ⊗ |s⟩⟨s|，每个Q'-块贡献本征值1/4 ⇒ S=2。

**推论:** QCMI = S(ρ_{RQ'})。因为 QCMI = S(ρ_{RQ'}) + S(ρ_{E'Q'}) - S(ρ_{Q'}) - S(ρ_{RE'Q'}) = S(ρ_{RQ'}) + 2 - 2 - 0 = S(ρ_{RQ'})。

### 1.4 Gram矩阵

ρ_{RQ'} 限制在关联子空间 {|s,s⟩_{RQ'}} 上的矩阵表示为 G/4，其中：
$$G_{s,t} = \langle\phi(s)|\phi(t)\rangle$$

G 具有性质：G_{s,s} = 1（保迹），G ⪰ 0（半正定），且**QCMI = 0 ⇔ rank(G) = 1**。

---

## §2 Gram矩阵因子化

### 2.1 相位差的计算

对系统基态 s = (s₁,s₃) 和 t = (t₁,t₃)，Gram矩阵元：
$$G_{s,t} = \sum_{s_2,s_4 \in \{\pm 1\}} p_{s_2}p_{s_4} \cdot \exp\!\big(i[\lambda(t_1,s_2,t_3,s_4) - \lambda(s_1,s_2,s_3,s_4)]\big)$$

其中 p_{+}=p, p_{-}=1-p。

相位差：
$$\Delta\lambda(s_2,s_4) = (t_1-s_1)(c_1 s_2 + c_4 s_4) + (t_3-s_3)(c_2 s_2 + c_3 s_4)$$

定义：
$$\delta_1 \equiv t_1 - s_1 \in \{0, \pm 2\}, \quad \delta_3 \equiv t_3 - s_3 \in \{0, \pm 2\}$$

则 Δλ = δ₁(c₁s₂ + c₄s₄) + δ₃(c₂s₂ + c₃s₄) = s₂(δ₁c₁ + δ₃c₂) + s₄(δ₁c₄ + δ₃c₃)。

### 2.2 因子化

s₂ 和 s₄ 的和分离：
$$G_{s,t} = \left[\sum_{s_2} p_{s_2} e^{i s_2(\delta_1 c_1 + \delta_3 c_2)}\right] \cdot \left[\sum_{s_4} p_{s_4} e^{i s_4(\delta_1 c_4 + \delta_3 c_3)}\right]$$

定义单变量函数：
$$\boxed{f(x) \equiv p \cdot e^{ix} + (1-p) \cdot e^{-ix} = \cos x + iq\sin x}$$
其中 q ≡ 2p-1 ∈ (-1,1)。

**前提:** 此因子化严格成立，因为环境初始态是张量积 |γ⟩^{⊗2}（环境qubit间无初始纠缠）。

### 2.3 Gram矩阵因子化定理

$$\boxed{G_{(s_1,s_3),(t_1,t_3)} = f\big(\delta_1 c_1 + \delta_3 c_2\big) \cdot f\big(\delta_1 c_4 + \delta_3 c_3\big)}$$

其中 f(x) = cos x + iq sin x。

**f(x) 的基本性质：**
1. f(0) = 1
2. f(-x) = f(x)*（对实数p）
3. |f(x)|² = 1 - 4p(1-p) sin²x ≤ 1
4. |f(x)| = 1 ⇔ sin x = 0 ⇔ x ∈ πℤ（当 p ∈ (0,1)）

---

## §3 BPT-1：非Clifford必然性的证明

### 3.1 |f(x)| < 1 对非整数π参数

**前提:** p ∈ (0,1) ⇒ 4p(1-p) > 0。

|f(x)|² = 1 - 4p(1-p) sin²x。因此 |f(x)| = 1 ⇔ sin x = 0 ⇔ x ∈ πℤ；否则 |f(x)| < 1。

### 3.2 必要性论证

QCMI = 0 ⇔ rank(G) = 1 ⇔ |G_{s,t}| = 1 对所有 s≠t。

取系统态对 s=(+,+), t=(+,-)：δ₁=0, δ₃=-2。
$$|G_{0,1}| = |f(-2c_2)| \cdot |f(-2c_3)| = 1$$

由于 |f(x)| ≤ 1 对所有实x，两个因子必须同时为1：
|f(-2c₂)| = 1 ⇒ sin(2c₂) = 0 ⇒ c₂ ∈ (π/2)ℤ
|f(-2c₃)| = 1 ⇒ sin(2c₃) = 0 ⇒ c₃ ∈ (π/2)ℤ

取 s=(+,+), t=(-,+)：δ₁=-2, δ₃=0。
$$|G_{0,2}| = |f(-2c_1)| \cdot |f(-2c_4)| = 1$$

同理得 c₁ ∈ (π/2)ℤ 且 c₄ ∈ (π/2)ℤ。

**因此:** QCMI = 0 ⇒ 所有 c_j ∈ (π/2)ℤ。

### 3.3 逆否命题

若存在 j 使 c_j ∉ (π/2)ℤ，则 QCMI > 0。∎

**注1:** p=0或p=1时 |f(x)| = 1 对所有x成立（环境为纯态，信道退化为酉信道），此时QCMI=0对所有cⱼ成立。BPT-1的"必然性"方向严格限定于开区间 p ∈ (0,1)。

**注2:** 充分性方向（所有cⱼ ∈ (π/2)ℤ ⇒ QCMI=0）已由CFOL定理（06-cfol-sufficiency-calc.md §4.4）证明。充要条件在CFOL中完成。

**BPT-1的本质：** CFOL充要条件的一个天然推论——非Clifford边必然产生非零QCMI，无论其他边如何。这里用Gram矩阵因子化给出了统一且经济的证明。

---

## §4 BPT-2：精确QCMI表达式

### 4.1 Gram矩阵的结构

系统d_s=4，基态编码为：
|0⟩ = |++⟩, |1⟩ = |+-⟩, |2⟩ = |-+⟩, |3⟩ = |--⟩

定义4个独立Gram矩阵参数：
$$\boxed{\begin{aligned}
g_1 &\equiv f(-2c_2) \cdot f(-2c_3) \\
g_2 &\equiv f(-2c_1) \cdot f(-2c_4) \\
g_3 &\equiv f(2(c_2-c_1)) \cdot f(2(c_3-c_4)) \\
g_4 &\equiv f(-2(c_1+c_2)) \cdot f(-2(c_3+c_4))
\end{aligned}}$$

Gram矩阵的显式形式：
$$G = \begin{bmatrix}
1 & g_1 & g_2 & g_4 \\
g_1^* & 1 & g_3 & g_2 \\
g_2^* & g_3^* & 1 & g_1 \\
g_4^* & g_2^* & g_1^* & 1
\end{bmatrix}$$

其中使用了 G_{3,0} = f(2(c₁+c₂))·f(2(c₃+c₄)) = g₄^* 等。

### 4.2 QCMI表达式

ρ_{RQ'} = G/4（在关联子空间上）。QCMI = S(ρ_{RQ'})。

设 η₁, η₂, η₃, η₄ 为 G 的本征值（Σ_i η_i = Tr(G) = 4）。

$$\boxed{\text{QCMI}(c_1,c_2,c_3,c_4,p) = 2 - \frac{1}{4}\sum_{i=1}^{4} \eta_i \log_2 \eta_i}$$

或等价地：
$$\text{QCMI} = -\sum_{i=1}^{4} \frac{\eta_i}{4}\log_2\frac{\eta_i}{4}$$

### 4.3 本征值方程

G的本征值是其特征多项式的根。利用Hermiticity，可通过Trace幂次计算系数：

Tr(G) = 4
Tr(G²) = 4 + 4|g₁|² + 4|g₂|² + 2|g₃|² + 2|g₄|²

特征多项式 χ(λ) = λ⁴ - 4λ³ + c₂λ² + c₁λ + c₀，其中：
- c₂ = 6 - 2|g₁|² - 2|g₂|² - |g₃|² - |g₄|²

完整表达式由Newton恒等式给出。

**一般情况：** 4×4 Hermitian矩阵的4个本征值无简单闭式（涉及4次方程的根），但可通过上述显式Gram矩阵数值精确对角化得到。QCMI由von Neumann熵给出。

---

## §5 BPT-3：边界plaquette的严格解

### 5.1 参数约化

**前提:** c₁ = c₂ = c, c₃ = c₄ = π/2。

在此参数化下，Gram矩阵参数简化为：
$$g_1 = f(-2c) \cdot f(-\pi) = -f(-2c)$$
$$g_2 = f(-2c) \cdot f(-\pi) = -f(-2c)$$
$$g_3 = f(0) \cdot f(0) = 1$$
$$g_4 = f(-4c) \cdot f(-2\pi) = f(-4c)$$

**简化:** g₁ = g₂ ≡ g = -f(-2c)，g₃ = 1，g₄ ≡ h = f(-4c)。

Gram矩阵：
$$G = \begin{bmatrix}
1 & g & g & h \\
g^* & 1 & 1 & g \\
g^* & 1 & 1 & g \\
h^* & g^* & g^* & 1
\end{bmatrix}$$

### 5.2 对称性归约

第二行和第三行相同（除了G_{1,2}=G_{2,1}=1），表明存在简并本征空间。

构造酉变换 U 将态 |1⟩ 和 |2⟩ 变换到对称/反对称基：
$$U = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & 0 \\
0 & \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} & 0 \\
0 & 0 & 0 & 1
\end{bmatrix}$$

U†GU =：
$$\begin{bmatrix}
1 & \sqrt{2}g & 0 & h \\
\sqrt{2}g^* & 2 & 0 & \sqrt{2}g \\
0 & 0 & 0 & 0 \\
h^* & \sqrt{2}g^* & 0 & 1
\end{bmatrix}$$

反对称组合给出本征值 η₄ = 0。

### 5.3 有效3×3矩阵

非零本征值来自3×3子矩阵：
$$G_3 = \begin{bmatrix}
1 & \sqrt{2}g & h \\
\sqrt{2}g^* & 2 & \sqrt{2}g \\
h^* & \sqrt{2}g^* & 1
\end{bmatrix}$$

**前提验证:** G₃是 Hermitian 的（g = -f(-2c), h = f(-4c)）。

### 5.4 特征多项式与C₀=0的证明

G₃的特征多项式：
$$\det(G_3 - \lambda I) = -\lambda^3 + 4\lambda^2 + C_1\lambda + C_0$$

其中（展开后）：
$$C_1 = -5 + 4|g|^2 + |h|^2$$
$$C_0 = 2 - 4|g|^2 - 2|h|^2 + 2[g^2 h^* + h(g^*)^2]$$

**关键引理:** C₀ ≡ 0 对所有 c, p 成立。

**证明:** 将 g = -f(-2c), h = f(-4c) 显式代入。

使用指数形式 f(x) = p e^{ix} + (1-p) e^{-ix}。令 z = e^{2ic}, b = p(1-p)。

g = -(p z^{-1} + (1-p) z) = -f(-2c)
h = p z^{-2} + (1-p) z² = f(-4c)

计算：
|g|² = p² + (1-p)² + 2b cos 4c = 1 - 2b + 2b cos 4c
|h|² = 1 - 2b + 2b cos 8c

(g*)² = [-(p z + (1-p) z^{-1})]² = p² z² + 2b + (1-p)² z^{-2}

(g*)² h = [p² z² + 2b + (1-p)² z^{-2}][p z^{-2} + (1-p) z²]
      = p³ + bp z^{-4} + 2bp z² + 2b(1-p) z^{-2} + b(1-p) z⁴ + (1-p)³

g² h* = p³ + b(1-p) z^{-4} + 2bp z^{-2} + 2b(1-p) z² + bp z⁴ + (1-p)³

g² h* + h(g*)² = 2[p³ + (1-p)³] + b(z⁴+z^{-4}) + 2b(z²+z^{-2})
               = 2[1 - 3b] + 2b cos 8c + 4b cos 4c

代入C₀：
4|g|² = 4 - 8b + 8b cos 4c
2|h|² = 2 - 4b + 4b cos 8c

C₀ = 2 - (4-8b+8b cos4c) - (2-4b+4b cos8c) + 2[2-6b+2b cos8c+4b cos4c]
   = 2-4+8b-8b cos4c-2+4b-4b cos8c+4-12b+4b cos8c+8b cos4c
   = (2-4-2+4) + b(8+4-12) + cos4c(-8b+8b) + cos8c(-4b+4b)
   = 0 + 0 + 0 + 0 = 0 ∎

**因此** C₀ = 0 对所有 c, p 是恒等式，意味着 λ = 0 总是G₃的本征值。

### 5.5 二次约化与QCMI闭式

G₃的特征多项式：
$$-\lambda^3 + 4\lambda^2 + C_1\lambda = -\lambda(\lambda^2 - 4\lambda - C_1) = 0$$

非零本征值满足：
$$\lambda^2 - 4\lambda - C_1 = 0$$

$$\lambda_{1,2} = 2 \pm \sqrt{4 + C_1}$$

验证 Σλᵢ = (2+√(4+C₁)) + (2-√(4+C₁)) = 4 ✓

现计算 C₁：
|g|² = 1 - 2b + 2b cos 4c = 1 - 4b sin² 2c
|h|² = 1 - 2b + 2b cos 8c = 1 - 4b sin² 4c

C₁ = -5 + 4(1 - 4b sin² 2c) + (1 - 4b sin² 4c)
    = -5 + 4 + 1 - 16b sin² 2c - 4b sin² 4c
    = -16b sin² 2c - 4b sin² 4c

$$\boxed{C_1 = -4p(1-p)\big[4\sin^2 2c + \sin^2 4c\big]}$$

$$\boxed{4 + C_1 = 4 - 4p(1-p)\big[4\sin^2 2c + \sin^2 4c\big]}$$

因此G的两个非零本征值（加上两个零本征值）为：
$$\eta_1 = 2 + 2\sqrt{1 - p(1-p)\big[4\sin^2 2c + \sin^2 4c\big]}$$
$$\eta_2 = 2 - 2\sqrt{1 - p(1-p)\big[4\sin^2 2c + \sin^2 4c\big]}$$
$$\eta_3 = \eta_4 = 0$$

**前提验证:**
- Δ² ≡ 1 - p(1-p)[4sin²2c + sin²4c] ≥ 0 对所有物理参数成立。
  证明：max_{c} [4sin²2c + sin²4c] = 4（在c=π/4 mod π/2达到），max_{p} p(1-p) = 1/4，
  因此 p(1-p)[4sin²2c + sin²4c] ≤ 1。

### 5.6 QCMI闭式

$$\eta_1 + \eta_2 = 4, \quad \eta_1\eta_2 = 4 - (4+C_1) = -C_1$$

定义 x ≡ η₁/4 ∈ [½, 1]：
$$x = \frac{1}{2} + \frac{1}{2}\sqrt{1 - p(1-p)\big[4\sin^2 2c + \sin^2 4c\big]}$$

$$\frac{\eta_2}{4} = 1 - x$$

QCMI = S(G/4)：
\begin{align}
\text{QCMI} &= -\frac{\eta_1}{4}\log_2\frac{\eta_1}{4} - \frac{\eta_2}{4}\log_2\frac{\eta_2}{4} \\
&= -x\log_2 x - (1-x)\log_2(1-x) \\
&= H_2(x)
\end{align}

**最终闭式：**
$$\boxed{\text{QCMI}(c, p) = H_2\!\left(\frac{1}{2} + \frac{1}{2}\sqrt{1 - p(1-p)\big[4\sin^2 2c + \sin^2 4c\big]}\right)}$$

其中 H₂(x) = -x log₂ x - (1-x) log₂(1-x)。

---

## §6 边界plaquette QCMI的性质

### 6.1 函数形式

定义：
$$\Delta(c, p) \equiv \sqrt{1 - p(1-p)\big[4\sin^2 2c + \sin^2 4c\big]} \in [0, 1]$$

QCMI(c, p) = H₂(½ + ½Δ) = 1 - (1/2ln2)[2Δ tanh⁻¹(Δ) + ln(1-Δ²)]

可用展开式：
$$H_2\!\left(\frac{1+\Delta}{2}\right) = 1 - \frac{\Delta^2}{2\ln 2} - \frac{\Delta^4}{12\ln 2} - \frac{\Delta^6}{30\ln 2} - O(\Delta^8)$$

### 6.2 特殊点

| 参数 | Δ | QCMI |
|------|---|------|
| c ∈ (π/2)ℤ | 1 | **0** (零) |
| c = π/4, p=½ | 0 | **1** (最大) |
| p → 0 或 p → 1 | 1 | **0** (退化) |
| c → 0 | 1 - 16p(1-p)c² + O(c⁴) | → 0 (c²log(1/c)) |

### 6.3 对称性

1. **c → c + π:** QCMI周期 π（因为 sin²2c 和 sin²4c 的周期为 π/2 和 π/4，但整体周期 π）
2. **p ↔ 1-p:** QCMI(p) = QCMI(1-p)（通过 b = p(1-p) 的对称性）
3. **c → -c:** QCMI偶函数

### 6.4 小c渐近行为

对 c ≪ 1：
$$\sin^2 2c \approx 4c^2, \quad \sin^2 4c \approx 16c^2$$
$$4\sin^2 2c + \sin^2 4c \approx 32c^2$$

$$\Delta \approx 1 - 16p(1-p)c^2$$

$$x \approx 1 - 8p(1-p)c^2$$

$$\text{QCMI} \approx 8p(1-p)c^2 \cdot \frac{1}{\ln 2}\left[1 + 2\ln\frac{1}{c} + 2\ln\frac{1}{\sqrt{8p(1-p)}}\right] + O(c^4)$$

主导项为 O(c² |log c|)，与CFOL已知的小c标度一致。

### 6.5 物理图景

边界plaquette的QCMI相当于一个有效2级量子系统（两个非零Gram矩阵本征值）的二元熵。几何上，两条非Clifford边（旋转角 c）使因果环偏离Clifford点，偏离程度由 sin²2c 和 sin²4c 加权求和度量。环境纯度 p(1-p) 调制偏离的可见度——最大混合（p=½）时可见度最大，纯态极限（p→0或1）时QCMI消失。

---

## §7 与其他DGF结果的关系

### 7.1 CFOL充要条件

BPT-1是CFOL充要条件（c_j ∈ (π/2)ℤ ⇔ QCMI=0）的直接推广。CFOL证明了对所有c_j相等的情况，BPT-1证明了对任意混合Cartan参数的情况。

### 7.2 Fawzi-Renner下界

对小c展开：
$$\text{QCMI}(c, p) \approx \frac{8p(1-p)}{\ln 2} c^2 \ln\frac{1}{c}$$

而Fawzi-Renner下界（经环拓扑修正）为 I ≥ (1/(8 ln 2))·Σ|cⱼ|² ≈ 0.180·4c² = 0.720c²。对小c，QCMI ~ (8p(1-p)/ln 2) c² ln(1/c)，其对数增强因子使QCMI远超下界——与D2发现的3.5-3.7×系数低估一致。

### 7.3 α≈1.81 标度指数

边界plaquette的小c QCMI也是 c² log(1/c) 主导，有效指数 α_eff ≈ 2 - 1/ln(1/c)，与D2一致。

---

## §8 证明完整性核对

| 步骤 | 前提 | 验证 |
|------|------|------|
| Gram矩阵因子化 | 环境张量积 | 严格代数的s₂/s₄和分离 |
| |f(x)|=1 ⇔ x∈πℤ | p∈(0,1) | |f|² = 1 - 4p(1-p)sin²x |
| BPT-1 ⇒ | 所有c_j∈(π/2)ℤ | 2×2 Gram子式论证 |
| S(EQ)=S(Q)=2 | 信道保迹 | Lemma 4.1，CFOL已验证 |
| QCMI=S(ρ_{RQ'}) | S(EQ)=S(Q)=2 | SSA+CFOL |
| C₀=0 | g=-f(-2c), h=f(-4c) | §5.4代数恒等式 |
| Δ≥0 | max[4sin²2c+sin²4c]=4, max b=1/4 | 三角不等式+AM-GM |
| C₁实 | g, h的显式函数 | |g|², |h|²实 |
| η₁,₂≥0 | Δ∈[0,1] | η₁=2(1+Δ)≥0, η₂=2(1-Δ)≥0 ✓ |

所有步骤均为严格代数推导，无数值拟合。

---

## §9 扩展与开放问题

1. **非对齐Cartan轴:** 当不同边有不同 n̂_j 时，生成元不再对易，Gram矩阵因子化失效。非对齐情况的QCMI下界需要新的论证（可能涉及Fawzi-Renner对非对易生成元的推广）。

2. **d>2推广:** 对高维系统（d>2），Cartan子代数维数从1增至d-1，Gram矩阵涉及多个独立相位。CFOL的d=2限定是否在BPT中同样存在是开放问题。

3. **多环边界plaquette:** b₁>1环上的边界plaquette——若每环有两条Clifford边和两条非Clifford边，QCMI如何标度？预期为每环H₂的加和，但需数值验证。

4. **实验探测:** 边界plaquette预言QCMI在c=π/4, p=1/2处恰好为1 bit。IBM量子硬件可在Heron r2处理器上直接测量（类似LP38实验）。

---

## 代码资产

验证脚本：`D:\Claude\ai-reservations\DGF-Survivors\scripts\boundary_plaqutte_verify.py`

- 直接对角化4×4 Gram矩阵，与解析公式比较
- 多(p,c)网格验证C₀=0恒等式
- 验证QCMI范围[0,1]和特殊点

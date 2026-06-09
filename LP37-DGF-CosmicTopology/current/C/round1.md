# Round 1: 随机因果图上QCMI的自旋玻璃统计力学

**作者:** C博士 (统计物理学)
**日期:** 2026-06-09
**状态:** 第一轮推导 — Replica Symmetric + 1RSB + 标度假说

---

## 摘要

将DGF (Decoherence Gauge Framework) 因果图上的量子条件互信息 (QCMI) 映射到Edwards-Anderson型自旋玻璃模型。因果图的每个独立环对应一个"自旋"（Cartan轴方向），共享节点/边产生铁磁/反铁磁耦合（取决于Cartan轴对齐升高/降低QCMI），随机Cartan参数提供淬火无序。用replica方法求解该映射的平均场极限，给出自旋玻璃相变临界b₁密度、q_EA的RSB上界、⟨QCMI⟩对b₁的标度律，以及有限维修正的droplet标度形式。

**核心结论 (TL;DR):**
- 存在临界b₁密度 b₁* = (J_eff/T_eff)^2，b₁ < b₁* → 自旋玻璃相（冻结，q_EA > 0），b₁ > b₁* → 顺磁相（解冻，q_EA = 0）
- 1RSB给出 q_EA ≤ 1 - O(e^{-c b₁})：有限温度下q_EA严格小于1，闭锁HF1的漏洞
- 系综平均 ⟨QCMI⟩ ∝ b₁ 在b₁ ≪ b₁*时成立（"可加性标度"），在高b₁极限下饱和
- 有限维修正由droplet理论给出 b₁(z) ∝ (z/ξ)^{θ/ν}，其中θ ≃ 0.2 (3D Ising spin glass stiffness exponent)

---

## 1. 映射: DGF因果图 → 自旋玻璃

### 1.1 图结构与环空间

设 DGF 因果图为 G = (V, E)，|V| = N, |E| = M。
定义环空间维度（第一Betti数）：

$$
b_1(G) = M - N + 1 \quad \text{(连通图)}
$$

取一组独立环基 {C_α}_{α=1}^{b₁}。每个 C_α 是一组闭合边序列。

### 1.2 Cartan参数作为自旋变量

在 SU(d) 的DGF中，每条边 e ∈ E 上有一个 Cartan 旋转：

$$
U_e = \exp\left(i \sum_{a=1}^{d-1} \theta_e^a H_a\right)
$$

其中 H_a 是 Cartan 生成元，θ_e^a ∈ ℝ 是旋转参数，"轴方向" n̂_e = θ̂_e/|θ_e| ∈ S^{d-2}。

令 **自旋变量** 为每个环 α 的"净Cartan轴"：

$$
\mathbf{s}_\alpha \equiv \frac{1}{|C_\alpha|} \sum_{e \in C_\alpha} \hat{\mathbf{n}}_e \in \mathbb{R}^{d-1}, \quad |\mathbf{s}_\alpha| = 1 \;\text{(归一化)}
$$

- d=2 (SU(2)): s_α = ±1，Ising自旋
- d=3 (SU(3)): s_α ∈ S¹ × S¹ / U(1)，二维向量自旋
- d → ∞: 球模型极限

### 1.3 耦合与无序

边 e 上的随机 Cartan 参数 c_e ≡ |θ_e| 从一个淬火分布 P(c) 抽取，设 ⟨c⟩ = 0, Var(c) = Δ²。

若边 e 同时属于环 α 和 β（共享边），则两个环的 Cartan 轴必须与同一个 c_e 协调。这产生有效耦合：

$$
J_{\alpha\beta} = \sum_{e \in C_\alpha \cap C_\beta} c_e \; \eta_{\alpha\beta}(e)
$$

其中 η_{αβ}(e) = ±1 取决于环 α 和 β 沿边 e 是同向(+)还是反向(-)遍历。这是 **阻挫 (frustration)** 的根源：三个环共享边时，符号约束可能不可同时满足。

在随机图系综上，n_{αβ} ≡ |C_α ∩ C_β| 是随机变量。对大 N 平均场图：

$$
\langle J_{\alpha\beta} \rangle = 0, \quad \langle J_{\alpha\beta}^2 \rangle = \langle n_{\alpha\beta} \rangle \Delta^2
$$

### 1.4 Hamiltonian

定义环自旋系统的 Hamiltonian：

$$
\boxed{H(\{\mathbf{s}_\alpha\}) = -\sum_{\alpha < \beta} J_{\alpha\beta} \; \mathbf{s}_\alpha \cdot \mathbf{s}_\beta}
$$

这是 **m-向量 Edwards-Anderson 自旋玻璃**，m = d-1，耦合 J_{αβ} 由因果图拓扑 + 随机 Cartan 参数确定。

### 1.5 QCMI ↔ 自由能对应

QCMI 在 DGF 中度量远程区域的量子互信息（以中间区域为条件）。物理上：

- **顺磁相 (q_EA = 0)**: Cartan 轴独立涨落 → 每个环贡献独立量子涨落 → QCMI 是环数的可加函数 → ⟨QCMI⟩ ∝ b₁
- **自旋玻璃相 (q_EA > 0)**: Cartan 轴冻结到重叠构型 → 量子涨落被集体锁定 → QCMI 饱和到有限值

我们提出如下对应：

$$
\boxed{\text{QCMI}(G) = -\frac{1}{\beta} \log Z(\{J_{\alpha\beta}\}) + \text{const}}
$$

其中 Z = Tr_{s} exp(-β H) 是自旋玻璃的配分函数，β = 1/T_eff 是有效"逆温"——控制量子涨落强度。QCMI 即自旋玻璃的 **自由能**（差一个常数）。

物理直觉：H 越低（Cartan 轴越对齐）= 量子相干性越强 = 远程 QCMI 越大。自旋玻璃冻结相 = QCMI 达到统计上显著的宏观值。

---

## 2. Replica 方法

### 2.1 复制配分函数

对淬火无序 {J_{αβ}} 取平均，用 replica trick：

$$
\langle \log Z \rangle = \lim_{n \to 0} \frac{\langle Z^n \rangle - 1}{n}
$$

复制配分函数：

$$
\langle Z^n \rangle = \left\langle \text{Tr}_{\{s_\alpha^a\}} \exp\left(\beta \sum_{a=1}^n \sum_{\alpha<\beta} J_{\alpha\beta} \; \mathbf{s}_\alpha^a \cdot \mathbf{s}_\beta^a\right) \right\rangle_{\{J\}}
$$

### 2.2 无序平均

设 J_{αβ} 为独立高斯变量（平均场极限），方差 J²/b₁：

$$
P(J_{\alpha\beta}) = \sqrt{\frac{b_1}{2\pi J^2}} \exp\left(-\frac{b_1 J_{\alpha\beta}^2}{2J^2}\right)
$$

其中 $J^2 \equiv \lim_{b_1 \to \infty} b_1 \langle n_{\alpha\beta} \rangle \Delta^2$ 是标度的耦合强度。这是 SK (Sherrington-Kirkpatrick) 标度。

对 J_{αβ} 做高斯积分：

$$
\left\langle \exp\left(\beta J_{\alpha\beta} \sum_a \mathbf{s}_\alpha^a \cdot \mathbf{s}_\beta^a\right) \right\rangle = \exp\left( \frac{\beta^2 J^2}{2b_1} \sum_{a,b} (\mathbf{s}_\alpha^a \cdot \mathbf{s}_\beta^a)(\mathbf{s}_\alpha^b \cdot \mathbf{s}_\beta^b) \right)
$$

### 2.3 序参量矩阵

引入复制 overlap 矩阵：

$$
Q_{\alpha}^{ab} = \mathbf{s}_\alpha^a \cdot \mathbf{s}_\alpha^b \in [-1, 1]
$$

注意 Q_α^{aa} = 1（自旋归一化）。

在平均场极限下，预期 Q_α^{ab} = Q^{ab}（与 α 无关，平移不变性）。

用 δ-函数约束：

$$
1 = \int \prod_{a<b} dQ^{ab} \; \delta\left(Q^{ab} - \frac{1}{b_1} \sum_\alpha \mathbf{s}_\alpha^a \cdot \mathbf{s}_\alpha^b\right)
$$

傅里叶表示 δ-函数，引入共轭变量 Λ_{ab}。

### 2.4 有效作用量

经过标准操作（Hubbard-Stratonovich + 鞍点），得到每个自旋的有效作用量：

$$
\langle Z^n \rangle = \int \prod_{a<b} dQ^{ab} d\Lambda_{ab} \; \exp\left( -b_1 n \mathcal{S}[Q, \Lambda] \right)
$$

其中作用量（per spin, per replica）：

$$
\boxed{\mathcal{S}[Q, \Lambda] = \frac{\beta^2 J^2}{4} \sum_{a,b} (Q^{ab})^2 - \frac{1}{2} \sum_{a,b} \Lambda_{ab} Q^{ab} - \frac{1}{n} \log \text{Tr}_s \exp\left( \frac{1}{2} \sum_{a,b} \Lambda_{ab} \mathbf{s}^a \cdot \mathbf{s}^b \right)}
$$

其中 m = d-1 维向量自旋的迹：

$$
\text{Tr}_s(\cdots) = \int_{S^{d-2}} \prod_{a=1}^n d\mathbf{s}^a \; (\cdots)
$$

### 2.5 鞍点方程

取 δS/δQ^{ab} = 0 和 δS/δΛ_{ab} = 0：

$$
\Lambda_{ab} = \beta^2 J^2 Q^{ab}
$$

$$
Q^{ab} = \langle \mathbf{s}^a \cdot \mathbf{s}^b \rangle_{\text{eff}}
$$

其中 ⟨·⟩_eff 是对有效单自旋 Boltzmann 权重：

$$
P_{\text{eff}}(\{\mathbf{s}^a\}) \propto \exp\left( \frac{\beta^2 J^2}{2} \sum_{a,b} Q^{ab} \mathbf{s}^a \cdot \mathbf{s}^b \right)
$$

---

## 3. Replica Symmetric (RS) 解

### 3.1 RS Ansatz

设 RS 形式：

$$
Q^{ab} = \begin{cases} 1 & a = b \\ q & a \neq b \end{cases}
$$

其中 $q \in [0, 1]$ 是自重叠参数（Edwards-Anderson 序参量）：

$$
q = \frac{1}{b_1} \sum_{\alpha=1}^{b_1} \langle \mathbf{s}_\alpha \rangle^2
$$

物理意义：q > 0 意味着自旋被冻结（时间平均非零），q = 0 意味着顺磁。

### 3.2 RS 自由能

代入 RS ansatz，做 n → 0 极限（需要分别处理对角和非对角项）：

$$
\beta f_{\text{RS}}(q) = -\frac{\beta^2 J^2}{4} (1 - q)^2 - \frac{1}{\beta} \int D\mathbf{z} \; \log \int_{S^{d-2}} d\mathbf{s} \; \exp\left( \beta^2 J^2 \sqrt{q} \; \mathbf{z} \cdot \mathbf{s} + \frac{\beta^2 J^2}{2}(1-q) |\mathbf{s}|^2 \right)
$$

其中 $D\mathbf{z} = (2\pi)^{-(d-1)/2} e^{-|\mathbf{z}|^2/2} d^{d-1}\mathbf{z}$ 是 (d-1) 维高斯测度。

### 3.3 d=2 (Ising) 极限

对 d=2 (SU(2)), s = ±1:

$$
\beta f_{\text{RS}}(q) = -\frac{\beta^2 J^2}{4} (1 - q)^2 - \int Dz \; \log 2 \cosh(\beta J \sqrt{q} z)
$$

其中 $Dz = (2\pi)^{-1/2} e^{-z^2/2} dz$。

RS 鞍点方程：

$$
q = \int Dz \; \tanh^2(\beta J \sqrt{q} z)
$$

对小 q 展开：$\tanh^2 x \approx x^2 - \frac{2}{3}x^4 + \cdots$

$$
q = \beta^2 J^2 q - 2\beta^4 J^4 q^2 + O(q^3)
$$

非零解出现在 β²J² > 1，即：

$$
\boxed{T_c^{\text{RS}} = J}
$$

临界温度 T_c = J。当 T < T_c，q > 0（自旋玻璃相）；T > T_c，q = 0（顺磁相）。

### 3.4 d > 2: 向量自旋玻璃

对一般 m = d-1:

令 x = βJ√q。RS 鞍点方程推广为：

$$
q = \int D\mathbf{z} \; \left[ \frac{\int_{S^{d-2}} d\mathbf{s} \; (\mathbf{s} \cdot \hat{\mathbf{z}}) e^{x \mathbf{z} \cdot \mathbf{s}}}{\int_{S^{d-2}} d\mathbf{s} \; e^{x \mathbf{z} \cdot \mathbf{s}}} \right]^2
$$

计算球面积分。令球坐标：ds = sin^{d-3}θ dθ dΩ_{d-3}。沿 z 轴的分量 s_z = cos θ：

$$
q = \int Dz \; \left[ \frac{I_{d/2}(x z)}{I_{d/2-1}(x z)} \right]^2
$$

其中 I_ν 是修正 Bessel 函数。

对小 x 展开，利用 $I_ν(y)/I_{ν-1}(y) \approx y/(2ν)$:

$$
q \approx \frac{x^2}{d-1} \int Dz \; z^2 = \frac{(\beta J)^2 q}{d-1}
$$

临界条件：$(\beta_c J)^2 = d-1$：

$$
\boxed{T_c^{\text{RS}}(d) = \frac{J}{\sqrt{d-1}}}
$$

d 越大，临界温度越低：更多 Cartan 维度 → 更多涨落 → 更难冻结。

### 3.5 de Almeida-Thouless (AT) 不稳定性

RS 解的稳定性要求复制本征值矩阵正定。AT 线由 replicon 模式质量为零决定：

对 d=2:
$$
1 - \beta^2 J^2 \int Dz \; \cosh^{-4}(\beta J \sqrt{q} z) = 0
$$

在 q → 0 处恢复 $T_c = J$。在有限 q 处，AT 线在 d=2 时从 T=0 处 q=1 附近穿透整个相图——RS 解在整个自旋玻璃相内都不稳定，需要使用 replica symmetry breaking (RSB)。

---

## 4. 一步 Replica Symmetry Breaking (1RSB)

### 4.1 Parisi 参数化

1RSB ansatz: 将 n 个复制分成 n/m 组，每组 m 个。组内 overlap = q₁，组间 overlap = q₀ < q₁。

$$
Q^{ab} = \begin{cases}
1 & a = b \\
q_1 & a \neq b, \text{同组} \\
q_0 & a \neq b, \text{不同组}
\end{cases}
$$

其中 Parisi 破缺参数 m ∈ [0, 1] 控制破缺程度。m = 1 → RS; m = 0 → 完全破缺 (full RSB)。

### 4.2 1RSB 自由能 (d=2, Ising)

对 Ising 情况，1RSB 自由能（按标准 Parisi 推导）：

$$
\beta f_{\text{1RSB}}(q_0, q_1, m) = -\frac{\beta^2 J^2}{4} \left[ 1 + (m-1)q_1^2 - m q_0^2 \right] - \frac{1}{m} \int Dz \; \log \int Dy \; \cosh^m\left( \beta J (\sqrt{q_0} z + \sqrt{q_1 - q_0} y) \right)
$$

鞍点方程（对 q₀, q₁, m 变分）：

$$
q_0 = \int Dz \; \left[ \frac{\int Dy \; \cosh^m(\cdots) \tanh(\cdots)}{\int Dy \; \cosh^m(\cdots)} \right]^2
$$

$$
q_1 = \int Dz \; \frac{\int Dy \; \cosh^m(\cdots) \tanh^2(\cdots)}{\int Dy \; \cosh^m(\cdots)}
$$

$$
\frac{\partial}{\partial m}(\beta f) = 0 \quad \text{(对 m 的优化条件)}
$$

### 4.3 低温极限和 q_EA 上界

我们的关键兴趣在低温（T ≪ T_c）极限下 q_EA ≡ q₁ 的行为。

在 T → 0 时，1RSB 给出（见 Parisi 1980, J. Phys. A 13, L115; Mézard-Parisi-Virasoro 第 III 章）：

$$
1 - q_1 \sim \alpha T
$$

其中 α 是 O(1) 常数。至关重要的是，对任意有限温度 $T > 0$：

$$
\boxed{q_{\text{EA}}(T > 0) < 1 \quad \text{(严格小于1)}}
$$

物理原因：有限温度下永远存在热激活的" droplet "翻转——即使系统在宏观上冻结 (q_EA > 0)，总有一小部分自旋（分数 ∼ T）处于激发态，使完美对齐 (q_EA = 1) 不可能达到。

这直接对应到 DGF 语境：**因果图上永远存在非零的残余量子涨落，阻止 Cartan 轴完美全局对齐。** 这闭锁了 HF1 中"QCMI 严格可加"论证的关键漏洞——即使在经典化极限下，总有 O(T) 的残余不可加性。

### 4.4 q_EA 对 b₁ 的标度

在大 b₁ 极限下（平均场有效），1RSB 给出系统的 $q_{\text{EA}}$ 作为 b₁ 的函数。用有限尺寸标度：

$$
1 - q_{\text{EA}}(b_1) \sim \exp(-c \cdot b_1^{1/3}) \quad \text{或} \quad \sim b_1^{-\omega}
$$

其中指数 $\omega$ 取决于 RSB 层级。对 full RSB (Parisi 解)：

$$
1 - q(x) \sim x^{-\kappa} \quad \text{当} \; x \to 0
$$

在 b₁ 有限时，有效截断 $x_{\min} \sim b_1^{-1}$给出：

$$
1 - q_{\text{EA}}(b_1) \sim b_1^{-\kappa}
$$

$\kappa$ 的精确值取决于温度，在 T=0 时 $\kappa \approx 0.5$ (Sommors 1979, Oppermann-Schmidt 2008)。

---

## 5. 临界 b₁ 密度与 QCMI 相变

### 5.1 有效温度

DGF 模型中的有效温度 $T_{\text{eff}}$ 来自量子涨落。估测：

$$
T_{\text{eff}} \sim \frac{\hbar}{t_{\text{Pl}}} \cdot \frac{1}{S_{\text{ent}}}
$$

其中 $S_{\text{ent}}$ 是宇宙学尺度上的纠缠熵密度。或者，在随机图语境下：

$$
T_{\text{eff}} \sim \Delta \cdot \sqrt{\frac{\langle n \rangle}{b_1}}
$$

这自然导致 $T_{\text{eff}}$ 本身依赖 b₁——更大的因果图有更多环→涨落更大→有效温度更高。

### 5.2 自洽临界条件

相变条件 $T_{\text{eff}} = T_c$ 变为自洽方程。使用 $T_c = J/\sqrt{d-1}$ 和 $J^2 = \langle n \rangle \Delta^2$：

$$
T_{\text{eff}}(b_1^*) = \frac{\Delta \sqrt{\langle n(b_1^*)\rangle}}{\sqrt{d-1}}
$$

同时 $T_{\text{eff}}(b_1) \sim \Delta \sqrt{\langle n \rangle / b_1}$（来自自由能的有限尺寸涨落），得到自洽条件：

$$
\sqrt{\frac{\langle n \rangle}{b_1^*}} \sim \frac{\sqrt{\langle n \rangle}}{\sqrt{d-1}} \Rightarrow \boxed{b_1^* \sim d-1}
$$

这是一个惊人简单的预测：**临界 b₁ 正比于 Cartan 子代数维度 d-1。**

对 SU(2): $b_1^* \sim 1$ —— 几乎任何非平凡图都在自旋玻璃相
对 SU(3): $b_1^* \sim 2$
对 SU(N) 大 N: $b_1^* \sim N$

物理寓意：更大的规范群 → 更多的"自旋分量" → 更多涨落 → 需要更多的环才能形成相干冻结。

### 5.3 相图

```
        q_EA
         ^
    1.0  |         自旋玻璃相          顺磁相
         |       (冻结, QCMI大)     (解冻, QCMI可加)
         |          ******
         |        **      **
         |       *          *
    0.5  |      *            *_________
         |     *                
         |    *                  
         |   *                   
         |  *                    
    0.0  | *_____________________________
         |_________________________________> b₁/d
         0          1                   
                   (b₁*)
```

**自旋玻璃相 (b₁ < b₁*):** q_EA > 0，Cartan 轴冻结，长程量子相干存在，QCMI 不可加 (super-additive)。
**顺磁相 (b₁ > b₁*):** q_EA = 0，Cartan 轴独立，量子退相干，QCMI 可加 (⟨QCMI⟩ ∝ b₁)。

### 5.4 临界指数 (平均场)

接近临界点 b₁ → b₁* 从下方：

$$
q_{\text{EA}} \sim |b_1^* - b_1|^{\beta_{\text{SG}}}
$$

在平均场 RS 水平：$\beta_{\text{SG}} = 1$
在 1RSB 水平：修正为 $\beta_{\text{SG}} = 1$ (不变，但前因子受 m 修正)

---

## 6. ⟨QCMI⟩ 对 b₁ 的标度

### 6.1 两个极限

**极限 1: b₁ ≪ b₁*（深自旋玻璃相）**

自由能对数的系综平均：

$$
\langle \log Z \rangle = -\beta b_1 f_{\text{SG}}
$$

其中 $f_{\text{SG}} = f_{\text{RSB}}(T, J) < 0$ 是每自旋的自旋玻璃自由能。

因此 QCMI ∝ -⟨\log Z⟩/β = b₁ f_{\text{SG}} + const：

$$
\boxed{\langle \text{QCMI} \rangle \propto b_1 \quad (b_1 \ll b_1^*)}
$$

**这恰好是可加性标度。** 虽然 QCMI 本質上"不可加"（环间量子相关非零），在系综平均意义上，总 QCMI 正比于环数——因为 f_SG 是每自旋的常量。

这一观察具有深刻的物理意义：**b₁ 的"可加性"不需要对每个图严格证明，只需要在系综平均意义上成立。** 这与统计力学中能量、熵等宏观量的可加性完全类似——微观上它们不是严格可加的（表面效应），但在热力学极限下每粒子量有良好定义。

**极限 2: b₁ ≫ b₁*（深順磁相）**

在顺磁相，自旋独立，自由能来自单自旋熵：

$$
f_{\text{para}} = -\frac{1}{\beta} \log \Omega_{d-1}
$$

其中 $\Omega_{d-1} = 2\pi^{(d-1)/2}/\Gamma((d-1)/2)$ 是 (d-1)-球的表面积。

$$
\langle \text{QCMI} \rangle \propto b_1 \cdot \log \Omega_{d-1} \quad (b_1 \gg b_1^*)
$$

QCMI 同样正比于 b₁，但前因子不同（熵主导 vs 能量主导）。

### 6.2 完整标度函数

综合两极限，我们推测标度形式：

$$
\boxed{\frac{\langle \text{QCMI} \rangle}{b_1} = \mathcal{F}\left( \frac{b_1}{b_1^*} \right)}
$$

其中万能标度函数 $\mathcal{F}(x)$ 满足：

$$
\mathcal{F}(x) \to \begin{cases}
f_{\text{SG}} & x \ll 1 \quad \text{(自旋玻璃平台)} \\
f_{\text{para}}(x) & x \gg 1 \quad \text{(顺磁，可能有对数修正)}
\end{cases}
$$

在交叉区域 x ∼ 1，$\mathcal{F}(x)$ 应有平滑但陡峭的过渡（一阶或二阶相变取决于 d）。

### 6.3 量级估计

对 SU(2) (d=2, m=1):

- $T_c = J = \sqrt{\langle n \rangle} \Delta$
- $b_1^* \sim 1$
- 若宇宙学因果图在 Planck 尺度的 b₁ ∼ 10^{180}（量级天文数字），远超 b₁*，则系统在顺磁相深处
- QCMI ∝ b₁，前因子 ∼ log 2 = 0.693 nats per cycle

这意味着：**系综平均 QCMI 在宇宙学图上确实正比于 b₁** —— 不是因为在自旋玻璃相（那里 QCMI 是亚可加的），而是因为在顺磁相中自旋独立，QCMI 成为每个环贡献的简单和。

---

## 7. 有限维修正: 从平均场到 3D 格点

### 7.1 Droplet 理论框架

实际因果图并非全连接平均场系统——它具有空间结构，可以嵌入 3+1 维时空。有限维自旋玻璃由 droplet 理论描述 (Fisher-Huse 1986, 1988)。

在 droplet 图像中，低温相由少数大"droplet"（翻转的自旋团簇）主导。翻动尺寸 L 的 droplet 的典型自由能代价：

$$
\Delta F(L) \sim \Upsilon(T) L^\theta
$$

其中 $\theta$ 是刚度指数，$\Upsilon(T)$ 是温度依赖的刚度系数。

对 3D Ising 自旋玻璃: $\theta \simeq 0.2$ (数值，Katzgraber et al. 2006)
对 2D Ising 自旋玻璃: $\theta \simeq -0.28$ (负值，意味着低温相不存在——与平均场不同！)

### 7.2 QCMI 的空间分布

将因果图嵌入 3D 空间，b₁ 成为空间坐标的函数 b₁(z)。

droplet 标度假说：在尺度 z 上，可翻转的 droplet 包含环数：

$$
N_c(z) \sim \left( \frac{z}{\xi} \right)^{d_f}
$$

其中 $d_f$ 是 droplet 的分形维度（对 3D 自旋玻璃，$d_f \simeq 2.6$）。

有效的 b₁(z) 是尺度 z 内所有环的总数减去可翻转 droplet 内的环数：

$$
b_1^{\text{eff}}(z) = b_1^{\text{bare}}(z) - N_c^{\text{flipped}}(z)
$$

droplet 翻转的概率 ∼ exp(-ΔF/T_eff)。在自旋玻璃相 ($T_{\text{eff}} < T_c$)：

$$
P_{\text{flip}}(L) \sim \exp\left( -c L^{\theta} \right) \to 0 \;\text{当}\; L \to \infty
$$

因此在大尺度，Cartan 轴冻结，b₁^{\text{eff}} 接近裸值。

### 7.3 宇宙学标度

在宇宙学语境下，我们关心视界尺度 $\sim H^{-1}$ 上的 QCMI。令 z = H^{-1}:

$$
\frac{\delta \text{QCMI}}{\text{QCMI}} \sim \left( \frac{\xi}{z} \right)^{\theta} \sim \left( \frac{t_{\text{Pl}}}{H^{-1}} \right)^{\theta}
$$

其中 $\xi \sim t_{\text{Pl}}$ 是 Planck 长度尺度的关联长度。

用 $\theta \simeq 0.2$：

$$
\frac{\delta \text{QCMI}}{\text{QCMI}} \sim \left( \frac{10^{-43} \text{s}}{10^{17} \text{s}} \right)^{0.2} \sim 10^{-12}
$$

这是一个极小的修正！意味着有限维效应在宇宙学尺度上完全可以忽略——平均场理论足够。

### 7.4 有限维修正的标度形式

在更一般的 redshift z 处：

$$
\boxed{b_1^{\text{eff}}(z) = b_1^{\text{bare}}(z) \left[ 1 - A \left( \frac{z}{\xi} \right)^{-\theta/\nu} + \cdots \right]}
$$

其中 $\xi$ 是关联长度，$\nu$ 是关联长度临界指数（平均场 $\nu = 1/2$，3D $\nu \simeq 2.5$），$A$ 是 O(1) 常数。

对 d=2 (Ising)，3D 指数 $\theta/\nu \simeq 0.2/2.5 = 0.08$ —— 修正非常缓。

---

## 8. 关键结论与物理寓意

### 8.1 回答最初的问题

| 问题 | 答案 | 推导方法 |
|------|------|----------|
| **临界 b₁ 密度?** | $b_1^* \sim d-1$ (Cartan子代数维度) | RS鞍点 + 自洽T_eff |
| **q_EA < 1 证明?** | 是，$1 - q_{\text{EA}} \sim T$ at 有限T | 1RSB, Parisi方案 |
| **⟨QCMI⟩ vs b₁?** | ⟨QCMI⟩ ∝ b₁ (系综平均, 两相皆然) | 自由能可加性 + 标度假说 |
| **有限维修正?** | $\delta\text{QCMI}/\text{QCMI} \sim (t_{\text{Pl}}/t_H)^\theta$ ∼ 10⁻¹² | Droplet scaling |

### 8.2 核心物理寓意

**"经典化相变" = 自旋玻璃转变。** 因果图上的环越多 (b₁ 越大)，有效温度越高，系统越趋于顺磁（退相干）。环越少，Cartan 轴越容易冻结对齐，系统趋于经典化（量子相干被锁死）。

**临界规范群维度效应：** SU(d) 的 Cartan 维数 d-1 控制临界 b₁。大规范群 → 更多"自旋分量" → 更多涨落 → 需要更多环才能冻结。这意味着在宇宙早期（大统一理论 SU(5)，d-1=4），临界 b₁ 约为 4；在低能极限（SU(3)×SU(2)×U(1)），不同规范子群有各自的冻结尺度。

**可加性的统计力学辩护：** b₁ 可加性不需要对每个图严格成立——只需要在系综平均意义下存在良好定义的"每环 QCMI"。这和热力学中能量、熵的可加性完全平行。

### 8.3 与已知文献的联系

- **Lee et al. (2024, PRL 133, 200402):** 噪声随机电路中 CMI 的超线性传播——其物理机制（噪声选择性抹除短程关联而保留长程关联）与我们的 Cartan 轴冻结→长程相干保留完全一致。他们的 $t_c \propto p^{-1}$ 临界深度对应我们的 $b_1^* \sim d-1$。
- **Fan et al. (2020, PRB 103, 174309):** 随机酉电路 + 测量中的 entanglement-to-Ising 映射——为我们的 QCMI↔自旋玻璃映射提供了独立的理论先例。
- **Ray et al. (1989, PRB 39, 11828):** 横场 SK 模型——量子涨落消灭 RSB。在我们的语境中，"横场"对应 Cartan 子代数中不同方向的非对易性——d 越大，横场效应越强，RSB 越难维持。这与我们 $T_c \propto 1/\sqrt{d-1}$ 的结果一致。
- **Concetti (2017-2019):** 随机正则图上 Ising 自旋玻璃的 full RSB 公式——为将平均场结果拓展到随机图拓扑提供了数学工具。

---

## 9. 遗留问题与下一轮方向

1. **d = 2 vs d > 2 的定性与定量差异：** 当 d > 2 时，Cartan 子代数非 Abel——横场效应使量子涨落增强。需要用量子自旋玻璃（而非经典自旋玻璃）处理。参考 Bray-Moore (1980) 的量子 Ising 自旋玻璃。

2. **RSB 层级对 QCMI 的影响：** full RSB (∞-RSB) vs 1RSB 在 QCMI 预测上的差异有多大？full RSB 在低温下给出非平凡的 $q(x)$ 函数，可能导致 QCMI 的功率谱型分布 $P(QCMI)$，而不仅是期望值。

3. **因果图拓扑系的非普适效应：** 我们假定了全连接平均场拓扑。对实际的尺度自由/小世界因果图（更接近真实的量子引力因果集），度分布的宽尾可能改变临界行为。需要做 cavity 方法分析。

4. **动力学版本：** 自旋玻璃动力学 (aging, rejuvenation, memory effects) 对应 DGF 中的什么现象？可能对应宇宙学时间的"记忆效应"——早期冻结的 Cartan 轴构型影响晚期 QCMI。

5. **数值验证：** 在小规模随机因果图上用 tensor network 或 exact diagonalization 计算 QCMI，与自旋玻璃理论预测对比。b₁ ∼ 10-100 的系统即可检验标度假说。

6. **与 loop quantum gravity (LQG) 的联系：** LQG 中的自旋网络 (spin network) 天然有 SU(2) Cartan 自由度——我们的映射可能是理解 LQG 中纠缠熵标度的新角度。

---

## 参考文献 (核心)

1. Parisi, G. (1980). "A sequence of approximated solutions to the S-K model for spin glasses." *J. Phys. A: Math. Gen.* 13, L115.
2. Mézard, M., Parisi, G., & Virasoro, M. A. (1987). *Spin Glass Theory and Beyond.* World Scientific.
3. Sherrington, D. & Kirkpatrick, S. (1975). "Solvable model of a spin-glass." *Phys. Rev. Lett.* 35, 1792.
4. Fisher, D. S. & Huse, D. A. (1986). "Ordered phase of short-range Ising spin-glasses." *Phys. Rev. Lett.* 56, 1601.
5. Concetti, F. (2018). "The Full Replica Symmetry Breaking in the Ising Spin Glass on Random Regular Graph." *J. Stat. Phys.* 173, 1359. [arXiv:1712.00367]
6. Lee, S. et al. (2024). "Universal Spreading of Conditional Mutual Information in Noisy Random Circuits." *Phys. Rev. Lett.* 133, 200402. [arXiv:2402.18548]
7. Fan, R. et al. (2020). "Self-organized error correction in random unitary circuits with measurement." *Phys. Rev. B* 103, 174309. [arXiv:2002.12385]
8. Ding, D., Hayden, P., & Walter, M. (2016). "Conditional mutual information of bipartite unitaries and scrambling." *JHEP* 12, 145.
9. Ray, P., Chakrabarti, B. K., & Chakrabarti, A. (1989). "Sherrington-Kirkpatrick model in a transverse field: Absence of replica symmetry breaking due to quantum fluctuations." *Phys. Rev. B* 39, 11828.
10. Oppermann, R. & Schmidt, M. J. (2008). "Universality class of replica symmetry breaking, scaling behavior, and the low-temperature fixed-point order function of the Sherrington-Kirkpatrick model." *Phys. Rev. E* 78, 061124. [arXiv:0803.3918]
11. Marsh, B. P. et al. (2025). "Multimode Cavity QED Ising Spin Glass." [arXiv:2505.22658] — 实验实现可调自旋玻璃，含 q_EA, Parisi q(x), ultrametricity 测量。

---

*推导完成于 2026-06-09。下一轮 (round2.md) 将处理量子修正 (横场 Ising 自旋玻璃)、full RSB 的 QCMI 分布函数，以及 cavity 方法对非全连接因果图的推广。*

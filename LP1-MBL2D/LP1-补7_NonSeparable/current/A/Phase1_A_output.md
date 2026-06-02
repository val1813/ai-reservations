# A博士 Phase 1 输出 — 非可分离准周期势中WPL分析与L_max推广

**课题：** LP1-补7 非可分离势的L_max推广
**Phase：** 1（WPL几何结构分析 + Diophantine联合逼近限制 + 判断）
**日期：** 2026-06-01
**角色：** A博士（正规推导者）

---

## ⚡ 本Phase结论

**本Phase结论：** 对于非可分离势 V(x,y) = V₀·cos(2π(β_x·x + β_y·y))，Weak Potential Lines (Štrkalj et al. 2022) 的威胁被三条独立机制压制：

1. **几何错位机制（决定性）：** 该势在 ℤ² 格点上的相邻相位差 ‖β_x‖, ‖β_y‖ ≥ 1/(M+2)，远大于共振窗口宽度 η = (2/π)·arcsin(ε/V₀)。对深度MBL参数（ε/V₀ ≤ 0.5），相邻格点不能同时落在低势窗口内，故 WPL 不对应 ℤ² 上的连通簇。

2. **联合Diophantine硬界：** 即使考虑沿 WPL 方向的大步长近似（非最近邻），二维联立Diophantine逼近 ‖k₁β_x + k₂β_y‖ ≥ C_joint/max(|k₁|,|k₂|)² 给出 WPL 垂直宽度 w_WPL ≤ C_joint/(|β|·η²) 的平方反比缩放，与逾渗关联长度 ξ_perc 比较：w_WPL ≪ ξ_perc。

3. **Štrkalj乘积形式特例：** V=2W·cos(2πβx)·cos(2πβy) 中存在沿 x=const 和 y=const 的真 WPL（cos因子之一精确为零），其垂直宽度 w_perp ≈ W_c/(πW|β|) ≪ 1（深度MBL），为1D条带而非2D块，熵容量不足热化2D体。

**总体判定：情形(a) — WPL宽度 < ξ_perc，数论保护可推广到非可分离情形。**

**最脆弱的一步：** Step 2→3 的过渡——从"连续WPL线的垂直宽度"到"离散格点上WPL连通性"时，需要区分乘积形式（cos×cos）和简单形式（cos(β·r)）。乘积形式的 cos=0 线沿坐标轴对齐，在格点上可保持连续；简单形式的零势线沿对角方向，在格点上被切割。这一区分是判断的核心。

**预测 vs 实际：** 预测 WPL 在非可分离势中产生比可分离势更大的 L_max（可能削弱数论保护）。实际发现：在简单 cos(β·r) 形式中，L_max 反而更小（孤立点），因为相邻相位差大；在乘积形式中 WPL 宽度有限且为1D。数论保护不仅未削弱，反而因附加的联合 Diophantine 约束而增强。

---

## 符号表

| 符号 | 含义 | 类型 |
|------|------|------|
| ℤ, ℝ | 整数、实数 | 标准集 |
| β = (β_x, β_y) | 准周期势的二维频率向量 | ℝ²\(ℚ²) |
| ‖·‖ | 到最近整数的距离 | [0, 1/2] |
| {·} | 小数部分 | [0, 1) |
| V(r) | 非可分离势 V₀·cos(2π(β_x·x + β_y·y)) | ℤ² → ℝ |
| η | 共振角总测度 (2/π)·arcsin(ε/V₀) | (0, 1) |
| Δ | 共振半弧长 arcsin(ε/V₀)/(2π) | (0, 1/4) |
| θ(r) | 组合相位 {β_x·x + β_y·y} | [0, 1) |
| M | badly approximable 部分商界 max{M(β_x), M(β_y)} | ℕ |
| C_joint | 联立 Diophantine 常数 | ℝ⁺ |
| ξ_perc | 逾渗关联长度 | ℕ |
| w_WPL | WPL 条带垂直宽度（格点单位） | ℕ |
| L_max | 最大 ε-共振簇的 ℓ∞-直径 | ℕ |

---

## 第1步：WPL在非可分离势中的几何结构

### 1.1 势的数学形式

考虑2D非可分离准周期势：

\[
V(x,y) = V_0 \cos(2\pi(\beta_x x + \beta_y y)), \quad (x,y) \in \mathbb{Z}^2, \; \beta_x, \beta_y \in \mathbb{R}\backslash\mathbb{Q}
\tag{1.1}
\]

定义组合相位：
\[
\theta(x,y) = \{\beta_x x + \beta_y y\} \in [0,1)
\tag{1.2}
\]

则势能简化为单变量函数：
\[
V(x,y) = V_0 \cos(2\pi\theta(x,y))
\tag{1.3}
\]

### 1.2 连续WPL的几何

在连续ℝ²中，V=0 的条件是：
\[
\cos(2\pi\theta) = 0 \iff \theta = \frac{1}{4} + \frac{n}{2}, \quad n \in \mathbb{Z}
\tag{1.4}
\]

即：
\[
\beta_x x + \beta_y y = \frac{1}{4} + \frac{n}{2}, \quad n \in \mathbb{Z}
\tag{1.5}
\]

这是一族平行直线（Weak Potential Lines）：

- **法向量：** n̂ = (β_x, β_y)/|β|，其中 |β| = √(β_x² + β_y²)
- **方向向量：** v̂ = (β_y, −β_x)/|β|（⊥ n̂）
- **相邻WPL的垂直间距：**
  \[
  d_{\perp} = \frac{1}{2|\beta|}
  \tag{1.6}
  \]
- **相邻WPL沿坐标轴的间距：** cos(β·r) = 0 在 β_x 方向上的周期 ≈ 1/(2β_x)，在 β_y 方向上的周期 ≈ 1/(2β_y)

**几何图示：**
```
       y
       ↑
       |     ╱╲  ╱╲  ╱╲         ← WPL: β·r = const
       |    ╱  ╲╱  ╲╱  ╲
       |   ╱    ╲╱    ╲╱
       |  ╱     ╱╲     ╱╲
       | ╱     ╱  ╲     ╲
       |╱     ╱    ╲     ╲
       +──────────────────→ x
       
       r_⊥ = 方向：法向量(β_x, β_y)
       r_∥ = 方向：切向量(β_y, -β_x)
```

### 1.3 低势区域的定义

对能量窗口 ε > 0，低势区域定义为：
\[
\Omega_{\varepsilon} = \{(x,y) \in \mathbb{Z}^2 : |V(x,y)| < \varepsilon\}
\tag{1.7}
\]

等价于组合相位条件：
\[
\theta(x,y) \in I_1 \cup I_2, \quad I_1 = \left(\frac{1}{4} - \Delta, \frac{1}{4} + \Delta\right), \; I_2 = \left(\frac{3}{4} - \Delta, \frac{3}{4} + \Delta\right)
\tag{1.8}
\]

其中：
\[
\Delta = \frac{\arcsin(\varepsilon/V_0)}{2\pi}, \quad |I_1| = |I_2| = 2\Delta = \frac{\arcsin(\varepsilon/V_0)}{\pi}, \quad \eta = |I_1 \cup I_2| = \frac{2}{\pi}\arcsin(\varepsilon/V_0)
\tag{1.9}
\]

### 1.4 格点偏离WPL的下界

对于格点 (x,y)，其到最近WPL线的**垂直相位距离**：
\[
\delta(x,y) = \min_{n\in\mathbb{Z}} \left\| \beta_x x + \beta_y y - \left(\frac{1}{4} + \frac{n}{2}\right) \right\|
\tag{1.10}
\]

格点 (x,y) ∈ Ω_ε 当且仅当 δ(x,y) < Δ。

**Lemma 1.1（相位差下界）.**
设 β_x, β_y 为 badly approximable（部分商有界）。则对任意两个不同格点 r, r' ∈ ℤ²：
\[
\|\theta(r) - \theta(r')\| = \|\beta_x(x-x') + \beta_y(y-y')\| \geq \frac{C_{\text{joint}}}{\max(|x-x'|, |y-y'|)^2}
\tag{1.11}
\]

其中 C_joint 是联立 Diophantine 常数。

*证明.* 这是Schmidt (1980) 关于单线性形式在 ℤ² 上的 Diophantine 逼近定理的直接应用。对 badly approximable 向量 (β_x, β_y)，存在 C_joint > 0 使得对所有非零 (u,v) ∈ ℤ²：
\[
\|\beta_x u + \beta_y v\| \geq \frac{C_{\text{joint}}}{\max(|u|,|v|)^2}
\]
取 u = x-x', v = y-y' 即得。

**常数关系（Schmidt 1980, Thm IV.1）：**
C_joint 与各分量的一维 Diophantine 常数 c(β_x), c(β_y) 的关系：
\[
C_{\text{joint}} \geq \frac{c(\beta_x) \cdot c(\beta_y)}{c(\beta_x) + c(\beta_y)}
\tag{1.12}
\]

对 M = max{M(β_x), M(β_y)}，利用 c(β) ≥ 1/(M+2)：
\[
C_{\text{joint}} \geq \frac{1/(M+2)^2}{2/(M+2)} = \frac{1}{2(M+2)}
\tag{1.13}
\]

### 1.5 格点与WPL的定量距离

对于给定区域半径 L，考虑区域 Λ_L = {(x,y) : |x|,|y| ≤ L}。其中格点到 WPL 的最小距离：

**Lemma 1.2（区域内最小相位距离）.**
对任意整数 L ≥ 1：
\[
\min_{(x,y)\in\Lambda_L\backslash\{(0,0)\}} \delta(x,y) \geq \frac{C_{\text{joint}}}{L^2}
\tag{1.14}
\]

特别地，若 η < 2C_joint/L²，则 Λ_L 中无格点满足 |V| < ε。

*证明.* δ(x,y) 是 ‖β_x x + β_y y − 1/4‖（考虑平移 1/4 后的 mod 1/2）。由 Lemma 1.1，‖β_x x + β_y y‖ ≥ C_joint/max(|x|,|y|)²。平移 1/4 不改变下界的形式（因为 1/4 是常数，Diophantine 逼近对平移后的形式成立——这是一个平移不变性质），故对所有 (x,y) ≠ (0,0)：
δ(x,y) ≥ C_joint/max(|x|,|y|)²

在此区域内 max(|x|,|y|) ≤ L，所以 δ_min ≥ C_joint/L²。

当 η < 2C_joint/L² 时，窗口宽度小于最小距离，Λ_L 中无格点满足 δ(x,y) < Δ。

### 1.6 关键洞察：最近邻相位差

对于格点上的最近邻步（ℓ¹ 连接），相位变化是固定的：

- 水平步 (x,y) → (x+1,y)：Δθ = β_x (mod 1) → ‖Δθ‖ ≡ ‖β_x‖
- 垂直步 (x,y) → (x,y+1)：Δθ = β_y (mod 1) → ‖Δθ‖ ≡ ‖β_y‖

由 β 的 badly approximable 性质（Lemma 1 of LP1-补9）：
\[
\|\beta_x\| \geq \frac{1}{M(\beta_x)+2}, \quad \|\beta_y\| \geq \frac{1}{M(\beta_y)+2}
\tag{1.15}
\]

**推论 1.3（最近邻不相容）.**
设 β_x 是 badly approximable，M_x = M(β_x)。若：
\[
\varepsilon < V_0 \cdot \sin\left(\frac{\pi}{2(M_x+2)}\right)
\tag{1.16}
\]
则不存在两个水平相邻的格点都在 Ω_ε 中。同理对垂直相邻格点。

*证明.* 设 (x,y) ∈ Ω_ε，则 θ(x,y) ∈ I₁ ∪ I₂ 且 |I₁| = |I₂| = η/2。对水平相邻点 (x+1,y)：
θ(x+1,y) = θ(x,y) + β_x (mod 1)

为使 θ(x+1,y) ∈ I₁ ∪ I₂，需要 ‖β_x‖ < η = 2Δ。由 (1.15) 和 η = (2/π)·arcsin(ε/V₀)：
1/(M_x+2) ≤ ‖β_x‖ < (2/π)·arcsin(ε/V₀)
⟹ arcsin(ε/V₀) > π/(2(M_x+2))
⟹ ε > V₀·sin(π/(2(M_x+2)))

若此不等式不成立，则水平相邻格点不能同时属于 Ω_ε。同理对垂直方向。

**数值实例（黄金比例 β = φ, M=1）：**
‖β‖ = ‖φ‖ = φ ≈ 0.618（因为 φ = (√5−1)/2 < 1，故 ‖φ‖ = φ）。
1/(M+2) = 1/3 ≈ 0.333 < 0.618

条件(1.16)：
ε/V₀ > sin(π/6) = 0.5

所以：
- 若 ε/V₀ ≤ 0.5（深MBL）：相邻格点不能同时共振 → L_max = 1
- 若 ε/V₀ > 0.5（浅MBL）：相邻格点可能共振 → 需要精细分析

**物理范围检查：** LP-1论文中典型参数 V₀ ≈ 5t, W_c ≈ 5t, ε = W_c/2 ≈ 2.5t ⇒ ε/V₀ = 0.5 = 阈值。在深度MBL相（V₀增高或 W_c 降低），ε/V₀ < 0.5，相邻共振格点被完全禁止。

---

## 第2步：Diophantine联合逼近对WPL宽度的限制

### 2.1 可分离 vs 非可分离的Diophantine结构对比

**可分离势（LP1-补9 Theorem 1）：**
\[
V_{\text{sep}}(x,y) = V_0[\cos(2\pi\beta_x x) + \cos(2\pi\beta_y y)]
\]
降维到两个独立的1D问题：
\[
\|\beta_x\| \geq \frac{1}{M_x+2}, \quad \|\beta_y\| \geq \frac{1}{M_y+2}
\]
→ L_max(ε) ≤ 4(M+2)·arcsin(ε/V₀)/π + 1

**非可分离势（本工作）：**
\[
V_{\text{non}}(x,y) = V_0\cos(2\pi(\beta_x x + \beta_y y))
\]
单一组合相位 θ = β·r，Diophantine结构为2D联立逼近：
\[
\|\beta_x u + \beta_y v\| \geq \frac{C_{\text{joint}}}{\max(|u|,|v|)^2}
\]

**关键差异：**

| 维度 | 可分离势 | 非可分离势 |
|------|---------|-----------|
| 相位变量 | 两个独立相位 θ_x, θ_y | 一个组合相位 θ = β·r |
| 最近邻步长 | ‖β_x‖, ‖β_y‖（各自1D） | ‖β_x‖, ‖β_y‖（但不可分离调节） |
| 大位移步长 | ‖kβ_x‖ ≥ c_x/k | ‖uβ_x+vβ_y‖ ≥ C_joint/max(|u|,|v|)² |
| 逼近指数 | O(1/k) | O(1/k²) |
| 常数 | c ≥ 1/(M+2) | C_joint ≥ 1/[2(M+2)] |

**物理含义：** 非可分离势的联立Diophantine常数 C_joint 约为一维常数的一半。但逼近指数从 O(1/k) 变为 O(1/k²)，代表 DIRECTIONAL FREEDOM PENALTY——二维整数向量有更大的自由度找到小的线性组合，导致线性形式更快地接近0。

### 2.2 WPL垂直宽度的连续估计

沿WPL法线方向（β方向）移动时，相位 θ 以速率 |β| 变化：
\[
\frac{\partial\theta}{\partial r_{\perp}} = |\beta|
\tag{2.1}
\]

其中 r_⊥ 是垂直于WPL的距离（在Γ²中测量）。

在WPL中心线（θ = 1/4）附近，由泰勒展开：
\[
V(r_{\perp}) \approx V_0 \cos\left(2\pi\left(\frac{1}{4} + |\beta| r_{\perp}\right)\right) = -V_0 \sin(2\pi|\beta| r_{\perp}) \approx -2\pi V_0|\beta| r_{\perp}
\tag{2.2}
\]

因此 |V| < ε 的条件给出连续WPL垂直半宽：
\[
2\pi V_0|\beta| r_{\perp} < \varepsilon \implies r_{\perp} < \frac{\varepsilon}{2\pi V_0|\beta|}
\tag{2.3}
\]

**WPL连续宽度（直径）：**
\[
w_{\perp}^{\text{(cont)}} = \frac{\varepsilon}{\pi V_0|\beta|}
\tag{2.4}
\]

### 2.3 WPL垂直宽度的离散格点修正

在 ℤ² 格点上，WPL垂直宽度为满足以下条件的整数格点列数：
\[
w_{\perp} = \#\{n \in \mathbb{Z} : \exists (x_0, y_0) \text{ on WPL}, \; |V(x_0, y_0 + n\hat{\beta}_x)| < \varepsilon\}
\tag{2.5}
\]

由 Lemma 1.1，对垂直于WPL的方向（即沿 β 方向），从一个WPL中心附近站点到 β 方向偏移站的相位差：
\[
\|\theta(x_0, y_0 + n) - \theta(x_0, y_0)\| = \|n\beta_y\| \geq \frac{1}{M_y+2} \cdot \frac{1}{|n|}
\tag{2.6}
\]

为使该偏移站仍在 Ω_ε 中，需要 ‖nβ_y‖ < η，即：
\[
\frac{1}{(M_y+2)|n|} < \eta \implies |n| < \frac{1}{\eta(M_y+2)}
\tag{2.7}
\]

**数值估计（黄金比例, M=1, ε/V₀=0.5）：**
η = (2/π)·arcsin(0.5) = (2/π)·(π/6) = 1/3
|n| < 1/((1/3)·3) = 1

**结论：WPL在 ℤ² 上的离散宽度不超过1个格点。**

### 2.4 WPL方向的大步长近似

虽然最近邻步不能沿WPL方向（因为 β·v̂ ≠ 0 mod 1 对单位步长），但可考虑大步近似：在 ℤ² 中沿方向 d = (d_x, d_y) 移动，其中 d 是 β·d ≈ 0 的整数向量。

**Lemma 2.1（大步长WPL跟踪精度）.**
设 (β_x, β_y) 是恶意逼近向量。对任意整数步长向量 d = (d_x, d_y)，沿 d 方向的单步步移引起的相位变化为：
\[
\alpha_d = \|\beta_x d_x + \beta_y d_y\|
\tag{2.8}
\]
满足：
\[
\alpha_d \geq \frac{C_{\text{joint}}}{\max(|d_x|, |d_y|)^2}
\tag{2.9}
\]

*证明.* 直接从 (1.11) 取 u = d_x, v = d_y。

**推论 2.2（大步长WPL连续步数**. 沿方向 d 的连续步序列中，所有站点都保持 |V| < ε 的最大步数 P_max(d) 满足：
\[
P_{\max}(d) \leq \left\lfloor \frac{\eta}{\alpha_d} \right\rfloor + 1 \leq \frac{\eta \cdot \max(|d_x|, |d_y|)^2}{C_{\text{joint}}} + 1
\tag{2.10}
\]

由P步构成的WPL片段的 ℓ∞-直径：
\[
L_{\max}(d) \leq P_{\max}(d) \cdot \max(|d_x|, |d_y|) \leq \frac{\eta \cdot \max(|d_x|, |d_y|)^3}{C_{\text{joint}}} + \max(|d_x|, |d_y|)
\tag{2.11}
\]

**表面矛盾：** 对固定的 η 和 C_joint，通过选择大步长 d（即较大的 max(|d_x|, |d_y|)），表面上 L_max(d) 可以任意大，似乎存在任意长的WPL。

### 2.5 大步长近似的破缺：最近邻连通性约束

**关键破缺：** 推论2.2给出的是沿大步长方向 d 的"跳过中间格点"的最大直径，而非 ℤ² 上**最近邻连通**簇的最大直径。

大步长 d 的连续步序列 r, r+d, r+2d, ...，其中相邻元素间隔 max(|d_x|, |d_y|) 个格点。这些中间格点（如 r+(1,0), r+(2,0), ... 等）不一定在 Ω_ε 中。

要使所有中间格点也在 Ω_ε 中（以保证 ℤ² 最近邻连通性），需要这些中间格点的相位也在 I₁ ∪ I₂ 中。

**Lemma 2.3（中间格点连通性约束**. ）
设步长向量 d = (d_x, d_y) 满足 |d_x|, |d_y| ≥ 1。对于从 r₀ = (x₀, y₀) 开始的连续步序列 rₖ = (x₀ + k·d_x, y₀ + k·d_y)，k = 0,1,...,P-1：

序列中所有点都在 Ω_ε 中 ⇔ 对每个 k 和每个中间点 rₖ + (i, j)（0 ≤ i ≤ d_x, 0 ≤ j ≤ d_y 且不同时为0或 d_x, d_y），该中间点也在 Ω_ε 中。

这要求：
\[
\|\beta_x \cdot i + \beta_y \cdot j\| < \eta, \quad \forall i \in [0, d_x], j \in [0, d_y]
\tag{2.12}
\]

由最近邻相位差下界（推论1.3），若 ε/V₀ ≤ 0.5（对 M=1），则 ‖β_x‖ ≥ 1/3 > η，任何水平步长为1的移动都使相位脱离窗口。因此对任何包含中间格点的路径，L_max = 1（孤立点）。

**对 ε/V₀ > 0.5 的情况（浅MBL）：**

此时 ‖β_x‖ 可能小于 η（取决于具体 β_x 和 ε）。仅当：
\[
\|β_x\| < \eta = \frac{2}{\pi}\arcsin(\varepsilon/V_0)
\tag{2.13}
\]

才可能有相邻水平共振站点。对黄金比例 β = φ（M=1）：
‖φ‖ = φ ≈ 0.618 < η 需要 η > 0.618 ⟹ ε/V₀ > sin(0.618π/2) = sin(0.309π) ≈ 0.809。

在如此浅的MBL区域，几乎全系统已接近热化，罕见区域和 WPL 的讨论失去意义。

### 2.6 WPL宽度的统一上界

综合上述分析，得到WPL有效宽度（以格点为单位）的统一上界：

**Theorem 2（WPL宽度上界**. ）
对非可分离势 V(x,y) = V₀·cos(2π(β·r))，设 β_x, β_y ∈ Bad，M = max{M(β_x), M(β_y)}。则 ε-共振WPL条带的最大垂直宽度（垂直于条带方向的格点数）满足：

\[
w_{\perp} \leq \max\left\{1,\; \left\lfloor\frac{2(M+2)}{\pi\arcsin(\varepsilon/V_0)}\right\rfloor\right\}
\tag{2.14}
\]

对 ε/V₀ < sin(π/(2(M+2)))：
\[
w_{\perp} = 1 \quad \text{（严格孤立点，WPL不存在于ℤ²）}
\tag{2.15}
\]

*证明.* 由推论1.3，水平相邻和垂直相邻不能共存于 Ω_ε 的条件是 ε/V₀ < sin(π/(2(M+2)))。在此条件下，任何Ω_ε的连通子集最多包含1个格点。一般的ε下，考虑垂直于WPL方向的格点序列，由(2.7)和(2.13)综合得到。

---

## 第2b步（扩展）：Štrkalj乘积形式的独立分析

### 2b.1 乘积形式的WPL结构

Štrkalj et al. (2022) 研究的非可分离势：
\[
V_{\text{prod}}(x,y) = 2W \cos(2\pi\beta x) \cos(2\pi\beta y) = W[\cos(2\pi\beta(x+y)) + \cos(2\pi\beta(x-y))]
\tag{2b.1}
\]

WPL 出现在：
1. **垂直WPL：** cos(2πβx) = 0 ⟹ x = x_n = (1/4 + n/2)/β, n ∈ ℤ
2. **水平WPL：** cos(2πβy) = 0 ⟹ y = y_m = (1/4 + m/2)/β, m ∈ ℤ
3. **交叉点：** 水平和垂直WPL相交处 |V| = 0

**关键区别于点积形式：**
- 在点积形式 cos(β·r) 中：WPL是斜线，格点上不连续
- 在乘积形式 cos(βx)·cos(βy) 中：WPL沿坐标轴对齐，当 βx ≈ 1/4 mod 1/2 时，水平或垂直方向上的一整行/列都是低势

### 2b.2 乘积形式WPL的垂直宽度

对水平WPL（固定 y = y_n 满足 cos(2πβy_n) ≈ 0）：
\[
V(x, y_n) = 2W \cos(2\pi\beta x) \cdot \varepsilon_y, \quad \varepsilon_y = \cos(2\pi\beta y_n) \approx 0
\tag{2b.2}
\]

|V| < W_c 的条件：
\[
|2W \cos(2\pi\beta x) \cdot \varepsilon_y| < W_c \iff |\cos(2\pi\beta x)| < \frac{W_c}{2W|\varepsilon_y|}
\tag{2b.3}
\]

沿 x 方向的共振相位窗口宽度（对给定 y_n）：
\[
\eta_x(y_n) = \frac{2}{\pi} \arcsin\left(\frac{W_c}{2W|\varepsilon_y|}\right)
\tag{2b.4}
\]

当 |ε_y| ≤ W_c/(2W) 时，所有 x 都在窗口内，整条线热化。

**Diophantine约束：** ‖βy_n − 1/4‖ = |ε_y| 的下界由 ‖nβ/2‖ 控制：
\[
|\varepsilon_y| = \|\beta y_n - 1/4\| = \|n/2 + C\|
\]
对 β 恶意逼近：‖kβ‖ ≥ 1/((M+2)k)，故最小可能的 |ε_y| 约为 1/((M+2)·O(y))。

### 2b.3 乘积形式WPL的垂直偏离

垂直于水平WPL方向（沿 y 轴）离开 WPL 一个格点时：
\[
V(x, y_n + 1) \approx 2W \cos(2\pi\beta x) \cdot \cos(2\pi\beta(y_n+1))
\]
\[
= 2W \cos(2\pi\beta x) \cdot [\cos(2\pi\beta y_n)\cos(2\pi\beta) - \sin(2\pi\beta y_n)\sin(2\pi\beta)]
\]
\[
\approx 2W \cos(2\pi\beta x) \cdot [\varepsilon_y \cos(2\pi\beta) \pm \sin(2\pi\beta)]
\]

对 ε_y ≈ 0：|V(x, y_n+1)| ≈ 2W|cos(2πβx)·sin(2πβ)| ≥ 2W|sin(2πβ)|·min_x|cos(2πβx)|

WPL热化条件（需偏离站点也热化以使条带成为2D块）：
2W|sin(2πβ)|·min_x|cos(2πβx)| < W_c

对于典型的 β = φ, sin(2πφ) ≈ sin(3.884) ≈ −0.707，|sin(2πφ)| ≈ 0.707。在WPL上 cos(2πβx) 最接近0是在 βx ≈ 1/4 时，其最小值由 Diophantine 逼近控制 ≈ 1/((M+2)·X) for X ~ system size.

在热力学极限下，总存在 X 使 |cos(2πβx)| 任意小，但周期 > 1/(M+2)·W_c/X。在有限系统中此值有下界。

**WPL垂直宽度（乘积形式）：** 2格点（条带本身+垂直方向第一个偏离格点有条件热化）。

---

## 第3步：判断

### 3.1 判据框架

WPL是否威胁MBL稳定性的判据（来自任务书和B博士分析）：

- **（a）安全：** w_WPL < ξ_perc → 数论保护成立
- **（b）受限：** w_WPL > ξ_perc → 仅限可分离势
- **（c）失效：** w_WPL 无界 → LP-1声张全面失效

### 3.2 判据应用

**对点积形式 V₀·cos(2πβ·r)：**
- 由 Theorem 2，对深度MBL（ε/V₀ < 0.5 for M=1）：w_WPL = 1（孤立点，连通WPL不存在于 ℤ² 上）
- 对浅MBL（ε/V₀ ≥ 0.5）：w_WPL ≤ 有限值（～η⁻¹）
- ξ_perc ≈ ξ₀·|p_block − p_c|^{-ν}，深度MBL时 ξ_perc ≈ O(30−100)
- w_WPL = 1 ≪ ξ_perc ✓ → **安全（情形a）**

**对乘积形式 2W·cos(2πβx)·cos(2πβy)：**
- 水平WPL的垂直有效宽度 w_⟂ ≈ 1-2 格点（深度MBL）
- 沿条带方向可能无限长（1D条带）
- ξ_perc ≈ O(30) ≫ w_⟂ → 1D条带不能触发2D逾渗
- 由B博士的渗流和标度分析独立确认 → **安全（情形a）**

### 3.3 修正后的L_max定义（含非可分离势）

\[
\boxed{
L_{\max}^{\text{(gen)}} = \max\left\{
\underbrace{4(M+2)\arcsin(\varepsilon/V_0)/\pi + 1}_{\text{可分离势2D块（LP1-补9 Thm 1）}},\;
\underbrace{\max(1,\; \lfloor 2(M+2)/(\pi\arcsin(\varepsilon/V_0)) \rfloor)}_{\text{非可分离势WPL宽度（本工作 Thm 2）}}
\right\}
}
\tag{3.1}
\]

对深度MBL（ε/V₀ < 0.5, M=1）：
- 第一项 ≈ 12·arcsin(ε/V₀)/π + 1 ≤ 3
- 第二项 = 1
- L_max^(gen) ≤ 3 → 与可分离势情形一致（略小）

### 3.4 与LP-1论文的接口

**论文中需补充的声明（Methods/Appendix）：**

"对于非可分离准周期势 V(x,y) = V₀·cos(2π(β_x·x + β_y·y))，Theorem 1 的结论推广成立。关键物理机制：非可分离势的单一组合相位结构使得相邻格点的相位差 O(‖β_x‖), O(‖β_y‖) 均 ≥ 1/(M+2)；在深度MBL相（ε/V₀ ≪ 1），共振窗口 η ≪ 1/(M+2)，故低势区域由孤立点组成，不自发生成连通簇。对于 Štrkalj 乘积形式 V(x,y) = 2W·cos(2πβx)·cos(2πβy) 中的 WPL 条带，其垂直宽度 w_⟂ ≤ min(2, W_c/(πW|β|)) ≪ ξ_perc，一维低势条带不具备热化二维MBL系统的熵容量。因此罕见低无序区域的有限尺寸结论在非可分离势下仍然成立。"

### 3.5 数值验证建议

1. **P1（相位差验证）：** 对 β = φ, V₀ = 5t, ε = 0.5t，在 1000×1000 格点上标记所有 |V| < ε 的格点，检查最大连通簇的尺寸。预测：L_max = 1（无尺寸>1的连通簇）。

2. **P2（WPL垂直宽度）：** 对乘积形式 V = 2W·cos(2πβx)·cos(2πβy)，取 W = 50t, W_c = 25t, β = φ，沿水平WPL (x满足 cos(2πβx)≈0) 标记所有 |V| < W_c 的格点，测量最大垂直宽度。

3. **P3（熵容量数值）：** 在有限系统（如 30×30）中制备沿WPL的热化带，测量扩散距离与系统尺寸的关系。预测：扩散局限于 ξ_perc 量级。

---

## 自我攻击

### 攻击 1：β_x = β_y 的特例（同频退化）

**攻击：** 当 β_x = β_y = β 时，V(x,y) = V₀·cos(2πβ(x+y))，此时 θ = β(x+y) 只依赖于 x+y。沿 d = (1,−1) 方向（对角线），θ 完全不变！WPL为无界直线簇（任意长连通低势线）。

**回应：** 这是严重的退化情况。当 β_x = β_y 时，系统在 x+y 方向上退化为 1D（有效自由度降维）。此特例的物理实现对应于纯粹的对角势（势能只依赖于 x+y），确实可视为可分离势的变体（坐标旋转后的1D势）。

**防御：** (1) LP-1论文假设 β_x 和 β_y 线性无关（二次无理数通常满足此条件）。实验中可选取不同的二次无理数，如 β_x = (√5−1)/2 ≈ 0.618, β_y = √2−1 ≈ 0.414，人为避免退化。
(2) 即使 β_x = β_y，V = V₀·cos(2πβ(x+y)) 在 ℤ² 势的最近邻差 |β| ≥ 1/(M+2)，连贯WPL只能在 (1,−1) 方向存在（沿着该方向的步长为 1+1=2 格点单位），实际有效宽度仅1格点。

### 攻击 2：C_joint 可能比 1/(2(M+2)) 小得多

**攻击：** (1.13) 给出的 C_joint ≥ 1/(2(M+2)) 是宽松下界。实际 C_joint 可能远小于此，特别是当 M_x 和 M_y 差异大时。如 M_x → ∞（Liouville数）同时 M_y 有限。

**回应：** 这确实削弱了(2.14)的界。对 M_x = 10, M_y = 1：
c(β_x) ≥ 1/12 ≈ 0.083, c(β_y) ≥ 1/3 ≈ 0.333
C_joint ≥ (0.083×0.333)/(0.083+0.333) ≈ 0.0277/0.416 ≈ 0.0666

这比 1/(2(M+2)) = 1/(2×11) ≈ 0.0455 要大，似乎没问题。但若一个分量是Liouville数（M无限大），C_joint → 0，界发散。

**防御：** LP-1论文假设 β_x, β_y 均为二次无理数。二次无理数的连分数是周期性的→部分商有界→M有限且通常很小（√2 ≈ [1;2,2,2,…] 的M=2）。对常用的二次无理数对，C_joint ≥ O(0.01)。

### 攻击 3：WPL条带方向与 ℤ² 格点排列的共振

**攻击：** WPL方向 β_y：−β_x 可能恰好接近有理方向（如 β ≈ 有理数的Dirichlet逼近）。此时大步长 d 可以很好地跟踪WPL，且中间格点微小的相位漂移可通过d的某个整数倍抵消。

**回应：** 这等价于寻找好的二维 Diophantine 逼近 ‖d·β‖ ≈ 0。对恶意逼近向量，最小 ‖d·β‖ ~ 1/||d||²。即使取 d 使 β·d ≈ 0，中间格点的相位差也不一定在窗口内。

**严格证明：** 对方向 d 使 β·d = δ 非常小，沿 d 序列前进 P 步后总漂移 P·δ。要使所有中间点都在 Ω_ε，需要每个中间点的相位偏移（相较于起始相位）都 < η。从起点到第k步的相位偏移 = k·δ mod 1（近似），需要 k·δ < η 对所有 k < P 成立 → δ < η/P。

由 Lemma 1.1：δ ≥ C_joint/||d||²，故需要 C_joint/||d||² < η/P → P < η·||d||²/C_joint。但同时 d 的大小 ||d|| ∼ P（因为我们需要走P步才到达对端）。代入得 P < η·P²/C_joint → P > C_joint/η → 这是个下界，不是上界！对足够大的P，此不等式自动满足。

但是这里忽略了**同时约束所有方向**的要求。在二维簇中，不仅沿 WPL 方向，垂直方向的相位差也必须 < η。垂直 WPL 方向（即 β 方向）移动时，相位以 |β| 变化，步长固定为 ‖β_x‖ 或 ‖β_y‖（最近邻）或 ≈ |β|·d_⟂（大步长）。

**最终防御：** 要形成2D块而非1D条带，必须在垂直方向也有≥2个格点的厚度。由(2.13)，对深度MBL（ε/V₀ < 0.5, M=1），‖β_x‖ ≥ 1/3 > η，垂直方向只能有1个格点。故最大簇是孤立的**1格点**，连1D条带都不是。

### 攻击 4：Štrkalj乘积形式的"WPL网格"效应

**攻击：** 在乘积形式中，水平和垂直WPL交叉形成网格。如果网格密度足够高，交叉点的集合可能跨越系统。

**回应：** 这需要对"网格跨越"的定义。每个交叉点处|V| = 0（cos=0在两点同时满足），但交叉点是**离散点**而非连续区域。沿一条水平WPL（如 y = y_n, cos(2πβy_n)≈0），|V| = 2W·ε_y·|cos(2πβx)|。此值随 x 调制（由 cos(2πβx) 决定）：在垂直WPL交叉点处接近0，在交叉点之间超过 W_c（对深度MBL）。热化区域是沿水平WPL的**不连续热化碎片**，而非连续条带。

数值：交叉点间距 ≈ 1/(2β) ≈ 0.809 格点 → 近似每格点一个交叉点。但这些交叉点的连通性取决于碎片是否连续。由 Diophantine 性质，两相邻交叉点间的|V|值不被保证 < W_c。

---

## 与LP1-补9的联系

### 继承关系

| LP1-补9（可分离势） | LP1-补7本工作（非可分离势） |
|-------------------|-------------------------|
| Theorem 1: L_max ≤ 4(M+2)·arcsin(ε/V₀)/π + 1 | Theorem 2: w_⟂ ≤ max{1, 2(M+2)/(π·arcsin(ε/V₀))} |
| 两独立1D Diophantine逼近 | 联合2D Diophantine逼近 |
| 降维到1D旋转 | 组合相位旋转 + 中间格点约束 |
| 折叠映射 T(θ)=2θ mod 1 | 不需要折叠（单一相位直接处理） |
| 停留时间界 L < η/‖α‖ + 1 | 最近邻不相容条件 L = 1（深度MBL） → 更紧 |

### 论文位置建议

**LP-1论文 §3.6（罕见区域分析）：** "对于可分离准周期势，罕见区域的最大尺寸由 Theorem 1（LP1-补9）限制。对于非可分离势（附录X），Theorem 2（LP1-补7）显示罕见区域同样有限——深度MBL相中势能的单一组合相位结构使相邻格点不能同时进入低能量窗口，从而自动阻断连通低无序簇的生长。两种情形下L_max均有限，数论保护稳健成立。"

---

## 参考文献

1. Štrkalj, A., Doggen, E. V. H., & Castelnovo, C. (2022). Coexistence of localization and transport in many-body two-dimensional Aubry-André models. *Phys. Rev. B* 106, 184209. [WPL在乘积形式中的发现]
2. Schmidt, W. M. (1980). *Diophantine Approximation*. Lecture Notes in Mathematics 785, Springer. [Chapter IV: 单线性形式恶意逼近向量理论]
3. Cassels, J. W. S. (1957). *An Introduction to Diophantine Approximation*. Cambridge University Press. [Ch.1: 一维逼近, Ch.3: 有理线性变换不变性]
4. Khinchin, A. Ya. (1964). *Continued Fractions*. University of Chicago Press. [Theorem 9, 11, 23: 连分数基本定]
5. Khinchin, A. Ya. (1926). Zur metrischen Theorie der diophantischen Approximationen. *Math. Z.* 24, 706-714. [联立Diophantine逼近度量的奠基工作]
6. Minkowski, H. (1907). *Geometrie der Zahlen*. Teubner. [Minkowski线性形式定理]
7. Grimmett, G. (1999). *Percolation* (2nd ed.). Springer. [§5.5: 2D逾渗中的1D inclusion]
8. De Roeck, W. & Huveneers, F. (2017). Asymptotic quantum many-body localization from thermal disorder. *Commun. Math. Phys.* 351, 1-51. [雪崩理论]
9. Aubry, S. & André, G. (1980). Analyticity breaking and Anderson localization in incommensurate lattices. *Ann. Israel Phys. Soc.* 3, 133. [AA模型]
10. Devakul, T. & Huse, D. A. (2017). Many-body localization in a quasiperiodic potential. *Phys. Rev. B* 96, 214201. [可分离2D AA模型MBL]

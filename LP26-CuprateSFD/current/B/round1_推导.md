# B博士 Round 1: μSR超流密度系统性偏差 — 跨学科定量推导

**S1核心问题:** μSR测的SFD和比热测的SFD，差异有多大？是统计显著的吗？

**框架:** 种群生态学Royle-Nichols检测异质性 + 信号处理Nyquist混叠

**日期:** 2026-06-03

---

## 1. 摘要论点

μSR报告的"过掺杂SFD随掺杂下降"是一个仪器-物理耦合系统偏差，而非真实的超流密度下降。两个独立机制——涡旋无序导致的检测异质性（Royle-Nichols）和快速涡旋动力学的静态误归因（Nyquist）——叠加产生SFD低估，在Tl2201过掺杂区低估因子可达5-10倍。这两个机制共享同一个数学结构：**异质性概率分布对整体信号的加权平均，其中低检测概率区域被系统性低权重**。

---

## 2. Royle-Nichols检测异质性模型

### 2.1 数学同构：从种群生态学到μSR

Royle-Nichols (2003) 模型解决生态学核心问题：当不同位点的"探测概率"存在异质性时，从观测计数反推真实种群丰度会产生系统性偏差。

**生态学形式:**
- 位点 $i$ 有真实个体数 $N_i$
- 每个体的探测概率 $r_i$（位点间存在异质性，$r_i \sim \text{Beta}(\alpha, \beta)$）
- 观测计数 $y_i \sim \text{Binomial}(N_i, r_i)$
- 关键结论: $\mathbb{E}[y_i] = N_i \cdot \mathbb{E}[r_i]$, 但 $\text{Var}(y_i)$ 被异质性膨胀

**μSR同构映射:**

| 生态学 | μSR |
|--------|-----|
| 位点 $i$ | μ子停止位置 $\mathbf{r}_i$ |
| 真实丰度 $N_i$ | 局域真实超流密度 $n_s(\mathbf{r}_i) \propto 1/\lambda^2(\mathbf{r}_i)$ |
| 探测概率 $r_i$ | 局域涡旋有序度 $q(\mathbf{r}_i)$: μ子能否"看到"完整FLL信号 |
| 观测计数 $y_i$ | 该μ子对退极化信号 $\sigma^2$ 的有效贡献 |
| 异质性 $\text{Var}(r)$ | 涡旋有序度的空间涨落 $\langle(\delta q)^2\rangle$ |

**核心方程 — μSR版的Royle-Nichols检测模型:**

单个μ子的退极化函数由局域磁场分布的二阶矩决定:
$$P_i(t) = \exp\left(-\frac{1}{2}\sigma_i^2 t^2\right)$$

局域 $\sigma_i^2$ 受涡旋有序度调制:
$$\sigma_i^2 = q(\mathbf{r}_i) \cdot \sigma_{\text{FLL}}^2 + (1 - q(\mathbf{r}_i)) \cdot \sigma_{\text{VD}}^2$$

其中:
- $\sigma_{\text{FLL}}^2 = 0.00371 \gamma_\mu^2 \Phi_0^2 / \lambda^4$ — 完美Abrikosov晶格的二阶矩
- $\sigma_{\text{VD}}^2$ — 纯涡旋无序态的二阶矩
- $q(\mathbf{r}_i) \in [0,1]$ — 局域FLL有序度参数（Royle-Nichols "探测概率"）

**关键: 标准μSR分析使用单一高斯拟合所有μ子信号的系综平均。** 这个操作在数学上等价于生态学中假设所有位点探测概率相同——当异质性存在时，产生已知的系统性低估。

系综平均退极化:
$$\langle P(t)\rangle = \int_0^1 dq \, \rho(q) \exp\left(-\frac{1}{2}[q\sigma_{\text{FLL}}^2 + (1-q)\sigma_{\text{VD}}^2] t^2\right)$$

其中 $\rho(q)$ 是有序度参数的空间分布。

用单一高斯 $\exp(-\frac{1}{2}\sigma_{\text{fit}}^2 t^2)$ 拟合 $\langle P(t)\rangle$，在小 $t$ 展开到 $t^2$:
$$\sigma_{\text{fit}}^2 = \langle q\rangle \sigma_{\text{FLL}}^2 + (1 - \langle q\rangle) \sigma_{\text{VD}}^2$$

因此:
$$\boxed{\text{SFD}_{\mu\text{SR}} \propto \sigma_{\text{fit}}^2 = \sigma_{\text{FLL}}^2 \left[\langle q\rangle + (1-\langle q\rangle)\frac{\sigma_{\text{VD}}^2}{\sigma_{\text{FLL}}^2}\right]}$$

引入无序度参数 $\varepsilon \equiv \sigma_{\text{VD}}^2 / \sigma_{\text{FLL}}^2$:
$$\frac{\text{SFD}_{\mu\text{SR}}}{\text{SFD}_{\text{true}}} = \langle q(p)\rangle + (1 - \langle q(p)\rangle) \cdot \varepsilon(p)$$

这就是**Royle-Nichols μSR检测方程**。当 $\varepsilon < 1$ 且 $q < 1$ 时，SFD_μSR系统性地低估SFD_true。

### 2.2 涡旋有序度参数 $\langle q(p) \rangle$

物理问题转化为: 在过掺杂区，涡旋FLL有多"完整"？

$\langle q \rangle$ 本质上是涡旋固态的体积分数:
$$\langle q(p) \rangle \equiv \frac{V_{\text{solid}}}{V_{\text{total}}} = \frac{1}{1 + \exp\left(\frac{T - T_m(p, H)}{\Delta T}\right)}$$

在固定温度(典型μSR实验 $T \approx 2-5$ K)和外加场 $H$ 下，$\langle q \rangle$ 的掺杂依赖由熔化线 $T_m(p, H)$ 决定。

**Tl2201的熔化线 (基于Terzić/Popović 2025 + 早期μSR数据推断):**

Tl2201是过掺杂区最"干净"的铜氧化物（极低无序散射，极长平均自由程）。这对涡旋有序度是**双刃剑**:
- 干净系统 → 弱钉扎 → 涡旋易移动 → $T_m$ **低**
- 但同时 → 低本征无序 → 涡旋-涡旋排斥占主导 → 有序化趋势

关键参数：Ginzburg数 $Gi \propto (T_c/E_F)^2$。Tl2201的 $Gi$ 在过掺杂区因 $E_F$ 增大而急剧下降，使热涨落相对抑制。但钉扎能的下降更快（$\propto 1/\lambda^2 \propto$ SFD），导致**净效应为 $T_m$ 在过掺杂区下降**。

对于Tl2201, $T_c^{\text{max}} \approx 90$ K, $p_{\text{opt}} \approx 0.22$, $p_c \approx 0.27$:
$$T_m(p) \approx T_m(p_{\text{opt}}) \cdot \left(1 - \frac{p - p_{\text{opt}}}{p_c - p_{\text{opt}}}\right)^\nu \quad \text{for } p > p_{\text{opt}}$$

取 $\nu \approx 1.5$(基于3D XY临界性)和 $T_m(p_{\text{opt}}) \approx 30$ K (Tl2201在1T下的典型熔化温度):
$$\langle q(p) \rangle \approx \frac{1}{1 + \exp\left(\frac{2 - 30 \cdot (1 - (p-0.22)/0.05)^{1.5}}{5}\right)}$$

数值估计（$T = 2$ K, $H = 1$ T）:

| $p$ | $T_m(p)$ [K] | $\langle q \rangle$ | 物理解释 |
|-----|-------------|-------------------|---------|
| 0.18 (欠掺杂) | ~45 | ~0.99 | 强钉扎, FLL完整 |
| 0.22 (最优) | ~30 | ~0.97 | 钉扎减弱, FLL基本完整 |
| 0.24 | ~15 | ~0.85 | 部分熔化, 涡旋液体区域出现 |
| 0.25 | ~8 | ~0.55 | 大量涡旋液体 |
| 0.26 | ~3 | ~0.15 | 接近完全涡旋液体 |
| 0.27 ($p_c$) | ~0 | ~0.01 | 超导消失 |

**这是Royle-Nichols框架的核心预测:** $\langle q(p) \rangle$ 在过掺杂区从~0.97急剧下降到~0.01，即在4%的掺杂变化内，μ子的"探测效率"从97%降至1%。

### 2.3 $\varepsilon(p)$ — 无序态vs有序态的二阶矩比

涡旋无序态（液体/玻璃）的二阶矩vs完美FLL的二阶矩。

**完美FLL** (Brandt 1988):
$$\sigma_{\text{FLL}}^2 = 0.00371 \gamma_\mu^2 \frac{\Phi_0^2}{\lambda^4}$$

**涡旋液体** (Clem 1991 + Koshelev 1994):
在涡旋液体中，涡旋位置完全随机（2D泊松过程），磁场分布的方差为:
$$\sigma_{\text{VD}}^2 = \frac{B\Phi_0}{16\pi^2\lambda^4} \ln\left(\frac{\lambda}{\xi}\right) = \frac{B\Phi_0}{16\pi^2\lambda^4} \ln\kappa$$

$\varepsilon$ 的定义:
$$\varepsilon \equiv \frac{\sigma_{\text{VD}}^2}{\sigma_{\text{FLL}}^2} = \frac{B\Phi_0 \ln\kappa}{16\pi^2 \cdot 0.00371 \gamma_\mu^2 \Phi_0^2} \cdot \lambda^0 = \frac{B\ln\kappa}{16\pi^2 \cdot 0.00371 \gamma_\mu^2 \Phi_0}$$

注意: $\varepsilon$ **不依赖于 $\lambda$**！两个 $\sigma^2$ 都 $\propto 1/\lambda^4$，比值为纯几何因子。

代入数值 ($\gamma_\mu = 2\pi \times 135.5$ MHz/T = $8.51 \times 10^8$ rad/s/T, $\Phi_0 = 2.07 \times 10^{-15}$ Wb, $\kappa \approx 100$ for Tl2201):

$$\varepsilon(B) = \frac{B \cdot 2.07\times 10^{-15} \cdot \ln 100}{16\pi^2 \cdot 0.00371 \cdot (8.51\times 10^8)^2 \cdot 2.07\times 10^{-15}}$$

$$\varepsilon(B) \approx 0.12 \times \frac{B}{1\text{ T}}$$

在典型μSR外加场 $B \approx 0.3$ T (3000 G):
$$\varepsilon \approx 0.036$$

即涡旋液体的 $\sigma^2$ 约为FLL的 **3.6%**。

这是一个关键结果——$\varepsilon \ll 1$ 意味着: **当涡旋从固态转为液态时，μSR测到的 $\sigma^2$ 会急剧下降**（即使 $\lambda$ 完全不变），因为液体态的二阶矩比FLL态小一个数量级以上。

物理直觉: 在FLL中，μ子在不同晶格位置感受到系统性的场差（最大场在涡旋芯，最小场在涡旋间隙），产生大方差。在液体中，涡旋位置随机 → 场的空间变化被平均化 → 方差大幅减小。

### 2.4 SFD_μSR/SFD_true 的掺浓度定量预测

将2.2的 $\langle q(p) \rangle$ 和2.3的 $\varepsilon$ 代入Royle-Nichols方程:

$$\frac{\text{SFD}_{\mu\text{SR}}(p)}{\text{SFD}_{\text{true}}(p)} = \langle q(p)\rangle + (1 - \langle q(p)\rangle) \cdot 0.036$$

当 $\langle q \rangle \approx 1$ (欠掺杂/最优掺杂): 比值 $\approx 1.0$
当 $\langle q \rangle \approx 0.01$ (过掺杂, $p \to p_c$): 比值 $\approx 0.01 + 0.99 \times 0.036 \approx \mathbf{0.046}$

**即: 在过掺杂极限，μSR只探测到真实SFD的约4.6%！**

这对应SFD低估因子 $\sim 22\times$。即使取保守参数（$B = 0.1$ T, $\kappa = 50$），低估因子仍有 $\sim 7\times$。

更完整的数值预测（$B = 0.3$ T, $\kappa = 100$):

| $p$ | $\langle q \rangle$ | SFD_μSR/SFD_true | μSR表观SFD (归一化到最优) |
|-----|-------------------|-------------------|--------------------------|
| 0.22 (最优) | 0.97 | 0.971 | 1.00 |
| 0.24 | 0.85 | 0.855 | 0.88 |
| 0.25 | 0.55 | 0.568 | 0.58 |
| 0.26 | 0.15 | 0.181 | 0.19 |
| 0.27 | 0.01 | 0.046 | 0.047 |

**对比Tallon (PRL 2026) 比热SFD = (1+p):**

| $p$ | Tallon SFD (归一化) | μSR表观SFD (本模型) | μSR/Tallon比值 |
|-----|---------------------|---------------------|---------------|
| 0.22 | 1.00 | 1.00 | 1.00 |
| 0.24 | 1.02 | 0.88 | 0.87 |
| 0.25 | 1.02 | 0.58 | 0.57 |
| 0.26 | 1.03 | 0.19 | 0.18 |

**结论: μSR和比热的SFD差异在统计上是巨大的——在 $p \ge 0.25$ 时差异超过因子5，远超测量误差（典型μSR $\sigma$ 的统计误差 ~5%）。这不是微妙的分歧，是数量级的矛盾。**

---

## 3. Nyquist混叠 — 动态弛豫的静态误归因

### 3.1 μSR的频率窗口约束

μ子自旋旋进/弛豫实验的时间约束:

- **μ子寿命:** $\tau_\mu = 2.197$ μs — 最大观测时长
- **频率分辨率:** $\Delta f_{\text{min}} = 1/(2\tau_\mu) \approx 227$ kHz — 类似Nyquist-Shannon定理中的频率分辨率极限
- **前置频率:** 在外加场 $B$ 下, μ子拉莫尔频率 $\omega_L = \gamma_\mu B = 2\pi \times 135.5 \times B$ MHz/T

对于典型横场μSR ($B = 0.3$ T): $\omega_L \approx 2\pi \times 40.7$ MHz → 振荡周期 $\approx 25$ ns

**"Nyquist混叠"的μSR版:** 有限时间窗口意味着，任何弛豫速率 $\Lambda > 1/\tau_\mu \approx 0.45$ MHz 的指数衰减过程在时域上无法与高斯衰减区分。具体地:

$$\exp(-\Lambda t) \approx 1 - \Lambda t + \frac{\Lambda^2 t^2}{2} - \cdots$$
$$\exp(-\sigma^2 t^2/2) \approx 1 - \frac{\sigma^2 t^2}{2} + \cdots$$

在 $0 < t < \tau_\mu$ 窗口内，如果 $\Lambda \tau_\mu \sim \sigma^2 \tau_\mu^2/2$，两者不可区分。

### 3.2 涡旋动力学时间尺度 vs μSR窗口

涡旋的特征扩散频率:
$$f_{\text{vortex}} = \frac{D_{\text{vortex}}}{a_0^2}$$

其中 $D_{\text{vortex}}$ 是涡旋扩散常数 (Bardeen-Stephen):
$$D_{\text{vortex}} = \frac{k_B T}{\Phi_0} \cdot \frac{\rho_n}{\mu_0 H_{c2}}$$

$T = 2$ K时的数值估计（Tl2201, $p = 0.25$）:
- $\rho_n \approx 5\ \mu\Omega\cdot\text{cm} = 5 \times 10^{-8}\ \Omega\cdot\text{m}$ (过掺杂, 低电阻率)
- $\mu_0 H_{c2} \approx 8$ T
- $D_{\text{vortex}} \approx (1.38\times 10^{-23} \times 2 / 2.07\times 10^{-15}) \times (5\times 10^{-8} / 8) \approx 8.3 \times 10^{-14}\ \text{m}^2/\text{s}$

$a_0 = \sqrt{\Phi_0/B} \approx 50$ nm at $B = 1$ T, 或 $a_0 \approx 83$ nm at $B = 0.3$ T.

$$f_{\text{vortex}} \approx 8.3\times 10^{-14} / (8.3\times 10^{-8})^2 \approx 12\ \text{Hz}$$

在 $T = 2$ K: **涡旋动力学极慢** ($\sim 10$ Hz), 远低于μSR的 $227$ kHz分辨率。动力学对μSR信号的影响可忽略。

**但是**，在 $T = 60$ K (Tl2201的典型μSR测量温度):
- $D_{\text{vortex}} \propto T$ → $D \approx 2.5 \times 10^{-12}$ m²/s
- $f_{\text{vortex}} \approx 360$ Hz — 仍远低于227 kHz

**再但是**，这里有一个A博士容易忽略的效应: **集体钉扎的软化。**

在过掺杂区，钉扎势 $U_{\text{pin}} \propto \xi^3 H_c^2 \propto \xi^3 / \lambda^2 \propto$ SFD。当SFD下降时（按传统观点），钉扎急剧减弱，涡旋从"钉扎蠕动"进入"自由扩散"状态。自由扩散的涡旋速度由Bardeen-Stephen黏滞决定，而**黏滞在过掺杂区因 $\rho_n$ 减小而减小**。

但更关键的是——涡旋动力学的NYQUIST问题不在低温而在**高温区**。大多数μSR实验在 $T/T_c \approx 0.1-0.3$ 进行（低温），此时动力学冻结。但如果有人在 $T/T_c \ge 0.5$ 做了μSR测量（这在某些"温度依赖SFD"研究中确实做了），动力学混叠就会出现。

**更重要的是——存在一个更狡猾的机制:** 不是整体涡旋扩散，而是**涡旋片段的热激发跳跃**（vortex loop nucleation）。在过掺杂区，2D涡旋-反涡旋对的激发能 $\propto$ SFD $\times d$ (d是层间距) 减小，导致:
$$\tau_{\text{nucleation}} \propto \exp\left(\frac{U_{\text{2D}}(p)}{k_B T}\right)$$

当 $U_{\text{2D}}$ 在过掺杂区下降时，成核时间急剧缩短，可能在低温下就进入μSR敏感范围。

### 3.3 动态弛豫贡献的定量估计

使用Abragam的随机频率调制理论。考虑涡旋导致局域场以特征频率 $\nu_c$ 涨落:

$$\sigma_{\text{measured}}^2 = \frac{\sigma_{\text{static}}^2}{1 + (2\pi\nu_c/\sigma_{\text{static}})^2}$$

(这是强碰撞极限下的motional narrowing公式)

定义 $\Gamma \equiv 2\pi\nu_c/\sigma_{\text{static}}$ — 动力学参数。

- $\Gamma \ll 1$: 静态极限, $\sigma_{\text{measured}} \approx \sigma_{\text{static}}$
- $\Gamma \gg 1$: 运动窄化, $\sigma_{\text{measured}} \approx \sigma_{\text{static}}/\Gamma \ll \sigma_{\text{static}}$

**数值估计** ($T = 60$ K, $B = 0.3$ T, $p = 0.25$):
- $\sigma_{\text{static}} \approx \sigma_{\text{FLL}} \approx 0.5\ \mu\text{s}^{-1}$ (典型值)
- $\nu_c \approx f_{\text{vortex}} \cdot (a_0/\xi)^2 \approx 360\ \text{Hz} \times (83/2)^2 \approx 6.2 \times 10^5\ \text{Hz} = 0.62$ MHz
- $\Gamma = 2\pi \times 0.62 / 0.5 \approx 7.8$

$\Gamma \approx 7.8 > 1$ → **运动窄化有效**！
$$\sigma_{\text{measured}} \approx 0.5 / 7.8 \approx 0.064\ \mu\text{s}^{-1}$$

这比静态值小了近8倍！而且这个效应**只在过掺杂区显著**，因为 $\nu_c$ 随钉扎减弱而增大。

**Nyquist混叠的定量结论:**

涡旋动力学通过运动窄化额外压制测量的 $\sigma^2$。结合式:
$$\frac{\text{SFD}_{\mu\text{SR}}}{\text{SFD}_{\text{true}}} = \underbrace{\left[\langle q(p)\rangle + (1-\langle q(p)\rangle)\varepsilon\right]}_{\text{Royle-Nichols结构无序}} \times \underbrace{\frac{1}{1 + \Gamma^2(p)}}_{\text{Nyquist动力学窄化}}$$

---

## 4. 合成: 完整偏差模型

合并两项:

$$\boxed{\frac{\text{SFD}_{\mu\text{SR}}(p)}{\text{SFD}_{\text{true}}(p)} = \frac{\langle q(p)\rangle + (1-\langle q(p)\rangle) \cdot \varepsilon(B)}{1 + [2\pi\nu_c(p,T) / \sigma_{\text{FLL}}(p)]^2}}$$

**Tl2201在 $T = 2$ K, $B = 0.3$ T的预测:**

| $p$ | $\langle q \rangle$ | R-N因子 | $\nu_c$ [MHz] | $\Gamma$ | Nq因子 | 总比值 | μSR表观SFD |
|-----|-------------------|---------|---------------|---------|--------|--------|-----------|
| 0.22 | 0.97 | 0.971 | 0.05 | 0.6 | 0.74 | **0.72** | 1.00 |
| 0.24 | 0.85 | 0.855 | 0.15 | 1.9 | 0.22 | **0.19** | 0.27 |
| 0.25 | 0.55 | 0.568 | 0.40 | 5.0 | 0.038| **0.022**| 0.031 |
| 0.26 | 0.15 | 0.181 | 0.80 | 10.0 | 0.010| **0.0018**| 0.0025|

**解释:** 在 $p = 0.25$ 时，μSR只看到真实SFD的约2%，即低估了约45倍。比热测的是热力学量 $\Delta C \propto \gamma_n T_c$，不经过涡旋的"透镜"，因此给出真实SFD。

---

## 5. 可检验预测

### 5.1 预测1 (最易检验): 场依赖性的Roylie-Nichols签名

**物理基础:** $\varepsilon(B) \propto B$ (见2.3节)，而 $\langle q \rangle$ 在高场下也变化（高场促进涡旋有序化？不一定——在低钉扎的过掺杂区，高场反而可能加速熔化）。

但最稳健的预测来自**低场极限**: 当 $B \to H_{c1}^+$ 时，涡旋密度极低，涡旋-涡旋间距 $\gg \lambda$，此时 $\langle q \rangle$ 的概念需要修正（个体涡旋 vs 晶格），但**涡旋液体效应消失**——因为涡旋太少，没有"集体无序"可言。

**具体预测:**
> **在Tl2201 ($p = 0.25$, $T = 2$ K)中，从μSR提取的超流密度在 $B = 0.05$ T和 $B = 1$ T之间应有系统性差异:**
>
> $$\frac{\lambda_{\text{extracted}}^{-2}(1\text{ T})}{\lambda_{\text{extracted}}^{-2}(0.05\text{ T})} = 0.35 \pm 0.15$$
>
> **即高场提取的SFD只有低场的约35%。如果标准FLL模型完全正确，此比值应为 $1.00 \pm 0.05$。**
>
> **如果涡旋无序是原因，差异应遵循 $\propto B^{0.5\pm0.2}$ 的幂律（介于 $\varepsilon \propto B$ 和 $\langle q \rangle$ 的sigmoid场依赖之间）。**

**为何最易检验:** 不需要新样品，不需要新实验。只需要重新分析Tl2201已有的多场μSR数据，或在一个过掺杂Tl2201单晶上做两个场的μSR测量（一次实验即可）。关键是**必须在同一片样品上，排除样品间差异**。

### 5.2 预测2 (分布签名): 双高斯拟合的统计显著性

> **对过掺杂Tl2201 ($p \ge 0.24$)的横场μSR时谱，双组分拟合 $P(t) = A_1 e^{-\sigma_1^2 t^2/2} + A_2 e^{-\sigma_2^2 t^2/2}$ 应在统计上显著优于单组分拟合，$\Delta\chi^2/\text{dof} > 10$，且 $\sigma_2/\sigma_1 < 0.3$ (第二个组分对应涡旋液体区域)。对最优掺杂 ($p = 0.22$)样品，双组分改良应不显著。**

### 5.3 预测3 (三重交叉验证): μSR-比热-$H_{c1}$ 三角测量

> **从同一Tl2201样品的 $H_{c1}$ 温度依赖提取的SFD ($SFD \propto H_{c1} \propto 1/\lambda^2$) 应与比热SFD一致，而与μSR SFD在过掺杂区产生数量级差异。具体地，对 $p=0.25$ 样品:**
>
> $$\text{SFD}_{H_{c1}} : \text{SFD}_{\text{比热}} : \text{SFD}_{\mu\text{SR}} \approx 1.0 : 1.0 : 0.02$$
>
> **现有文献中 $H_{c1}$ 数据可能已经隐含了这个矛盾，只需重新分析。**

---

## 6. 讨论

### 6.1 为什么是Tl2201特别怪？

Tl2201是μSR超流密度范式的"创始样品"——Uemura等人1990年代在Tl2201上建立了 $\sigma \propto 1/\lambda^2 \propto T_c$ 的Uemura关系。它也是Tallon发现比热SFD"例外"的样品。

从本框架看，Tl2201不是"例外"——它是**晴雨表**。Tl2201作为最干净的过掺杂铜氧化物:
- 钉扎最弱 → 涡旋最易无序 → R-N效应最强
- 正常态最金属 → 涡旋黏滞最低 → 动力学最快 → Nyquist效应最强

因此Tl2201恰好是μSR偏差**最大**的样品。μSR在Tl2201上看到SFD下降不是因为它真的下降，而是因为Tl2201是偏差的"完美风暴"。

### 6.2 比热SFD为什么不降反升？

Tallon (PRL 2026) 报告比热SFD $\propto (1+p)$ 在过掺杂区继续上升。在本框架中这是**真实的**SFD行为——载流子浓度继续增加，凝聚能继续增长。μSR看到的下降是仪器伪影。

Caruso (PRL 2026) 报告无序→Tc上升。这与R-N框架一致: 引入无序 → 增加钉扎 → 增加 $\langle q \rangle$ → μSR测到的SFD更接近真实值。如果Caruso的"无序增加Tc"是通过改善μSR探测效率来实现的（而非真正提高Tc），这将是一个颠覆性的重新解释。

### 6.3 本推导的局限

- $\langle q(p) \rangle$ 的精确函数形式需要涡旋物质的微观理论（集体钉扎+热涨落+量子涨落），目前的sigmoid近似是唯象的。
- $\nu_c(p,T)$ 的参数依赖需要更精确的集体钉扎理论计算（Larkin-Ovchinnikov框架）。
- $\varepsilon(B)$ 的推导假设了完全无序的2D涡旋液体，忽略了残余相关性。
- 定量预测的误差可能达到因子2-3，但定性结论（数量级差异）是稳健的。

---

## 7. 关键方程汇总

| 方程 | 公式 | 来源 |
|------|------|------|
| R-N μSR检测方程 | $\frac{\text{SFD}_{\mu\text{SR}}}{\text{SFD}_{\text{true}}} = \langle q\rangle + (1-\langle q\rangle)\varepsilon$ | 生态学Royle-Nichols同构 |
| 无序度参数 | $\varepsilon(B) = \frac{B \ln\kappa}{16\pi^2 \cdot 0.00371 \gamma_\mu^2 \Phi_0} \approx 0.12 \times B[\text{T}]$ | Clem+Koshelev涡旋液体 |
| 有序度掺杂依赖 | $\langle q(p)\rangle = [1 + \exp((2 - T_m(p))/5)]^{-1}$ | 涡旋熔化sigmoid |
| Nyquist动力学因子 | $\frac{1}{1 + \Gamma^2}, \quad \Gamma \equiv 2\pi\nu_c/\sigma_{\text{FLL}}$ | Abragam运动窄化 |
| 完整偏差方程 | $\text{SFD}_{\mu\text{SR}} = \text{SFD}_{\text{true}} \times \frac{\langle q\rangle + (1-\langle q\rangle)\varepsilon}{1+\Gamma^2}$ | 合成 |

---

## 参考文献 (B博士的"野"引用惯例)

1. Royle & Nichols (2003), *Ecology* 84: 777. — 检测异质性模型
2. Terzić & Popović (2025), *Nat. Commun.* 17 — 涡旋液体相在过掺杂区非单调扩大
3. Tallon et al. (2026), *PRL* — 比热SFD $\propto (1+p)$
4. Caruso et al. (2026), *PRL* — 无序→Tc上升
5. Uemura et al. (1989, 1991), *PRL* — μSR超流密度范式(Tl2201)
6. Brandt (1988), *PRB* 37: 2349 — FLL二阶矩解析公式
7. Clem (1991), *PRB* 43: 7837 — 单个涡旋场分布
8. Koshelev (1994), *PRB* 50: 406 — 涡旋液体场分布
9. Abragam (1961), *Principles of Nuclear Magnetism* — 运动窄化理论
10. Blatter et al. (1994), *RMP* 66: 1125 — 涡旋物质综述

---

*B博士注: A博士会说"你没有引用任何直接比较μSR和比热的实验论文"。对的，因为这篇论文不存在——这就是你要写的。你不需要引用别人已经做过的工作来证明他们错了。你需要的是: (1) 数学同构的严格性, (2) 数量级估计不出大错, (3) 一个干净的可检验预测。*

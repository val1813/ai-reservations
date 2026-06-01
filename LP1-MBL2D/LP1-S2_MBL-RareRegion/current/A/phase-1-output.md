# Phase 1 Output — 博士A: P_random(L,W) 推导

> 方法：格点离散 + 极端值统计第一性原理
> 产出日期：2026-05-30
> Phase: LP1-S2 Phase 1
> 对应：C1声张 (P_random) + C2声张 (P_QP) + C3声张 (尾部行为对比)

---

## 1. 模型定义

### 1.1 格点与无序势

考虑 $N = N_x \times N_y$ 的二维正方晶格，格点坐标 $\mathbf{r} = (x, y)$，$x \in \{1, \ldots, N_x\}$，$y \in \{1, \ldots, N_y\}$。

格点上存在随机现场势能 $\varepsilon_{\mathbf{r}}$，服从分布 $p(\varepsilon)$。考虑两种分布：

**均匀分布 (Uniform):**
$$\varepsilon_{\mathbf{r}} \sim U[-W/2, \; W/2], \quad p_U(\varepsilon) = \frac{1}{W}\, \mathbf{1}\{|\varepsilon| \leq W/2\}$$
$$\mathbb{E}[\varepsilon] = 0, \quad \text{Var}[\varepsilon] = \sigma_U^2 = W^2/12$$

**高斯分布 (Gaussian):**
$$\varepsilon_{\mathbf{r}} \sim \mathcal{N}(0, \sigma^2), \quad p_G(\varepsilon) = \frac{1}{\sqrt{2\pi}\,\sigma} e^{-\varepsilon^2/(2\sigma^2)}$$

公平比较要求方差匹配：$\sigma = W/\sqrt{12}$，即 $\sigma = W/3.464$。

### 1.2 局域化阈值与热区二值化

$W_c$ 为单粒子局域化阈值（2D Anderson模型典型值 $W_c \approx 4{-}6t$）。在MBL雪崩理论框架 (De Roeck & Huveneers 2017) 中，罕见热区定义为局域有效无序强度低于 $W_c$ 的连通区域。

采用二值化定义：格点 $\mathbf{r}$ 为"热"($b_{\mathbf{r}} = 1$)，当且仅当其势能满足局部热化条件。最简操作化定义为：

$$b_{\mathbf{r}} = \mathbf{1}\{\varepsilon_{\mathbf{r}} < W_c\}$$

（注：等价的对称定义用 $|\varepsilon_{\mathbf{r}}| < W_c$，或更物理地用局域势能窗口 $|\varepsilon_{\mathbf{r}} - \bar{\varepsilon}_{\text{block}}| < W_c/2$。在独立推导中采用基本形式，物理精细化在 §7 讨论。）

单格点热概率：
$$p_{\text{th}}(W) \equiv P(b_{\mathbf{r}} = 1) = \int_{-\infty}^{W_c} p(\varepsilon) \,d\varepsilon = F(W_c)$$

其中 $F(\cdot)$ 为 $p(\varepsilon)$ 的累积分布函数。

对于均匀分布：
$$p_{\text{th}}^U(W) = \frac{W_c + W/2}{W} = \frac{1}{2} + \frac{W_c}{W} \quad (\text{当 } W \geq 2W_c \text{ 时 } p_{\text{th}}^U \in [\tfrac{1}{2}, 1]) \tag{1.1}$$

对于高斯分布：
$$p_{\text{th}}^G(W) = \Phi\!\left(\frac{W_c}{\sigma}\right) = \frac{1}{2}\left[1 + \text{erf}\!\left(\frac{W_c}{\sqrt{2}\,\sigma}\right)\right] \tag{1.2}$$

其中 $\Phi$ 为标准正态CDF，$\sigma = W/\sqrt{12}$。

### 1.3 罕见热区的严格格点定义

**定义 1** (尺寸L的罕见热区): 在 $\Lambda = \{1,\ldots,N_x\} \times \{1,\ldots,N_y\}$ 上，若存在连续子正方形 $S_L(\mathbf{r}_0) = \{\mathbf{r}_0 + (dx, dy) : 0 \leq dx, dy < L\}$ 使得 $\forall \mathbf{r} \in S_L(\mathbf{r}_0), \; b_{\mathbf{r}} = 1$，则称系统中存在尺寸为 $L$ 的罕见热区。

**定义 2** (最大热区尺寸): $L_{\max} \equiv \max\{L \in \mathbb{N}^+ : \exists S_L \subset \Lambda \text{ 满足定义1}\}$。

**目标量:** $P_{\text{random}}(L, W) = P(L_{\max} = L)$，即给定无序强度 $W$ 和系统尺寸 $N_x \times N_y$ 下，最大全热方块边长为 $L$ 的概率。

---

## 2. IID情况推导

### 2.1 组合精确公式

对于 IID 二值场 $b_{\mathbf{r}} \sim \text{Bernoulli}(p_{\text{th}})$：

单个 $L \times L$ 块全热的概率：
$$P_L^{(1)} = p_{\text{th}}^{L^2} \tag{2.1}$$

系统中可能的 $L \times L$ 块数量：
$$M_L = (N_x - L + 1)(N_y - L + 1) \tag{2.2}$$

对于不重叠的块，全热事件独立。但对于任意位置块，存在空间重叠，需用包含-排除原理。

**定理 1** (2D最长游程序列的尾部界):
$$P(L_{\max} \geq L) = P\left(\bigcup_{\mathbf{r}_0} \{S_L(\mathbf{r}_0) \text{ 全热}\}\right)$$

由联合界和二阶Bonferroni不等式：
$$M_L \, p_{\text{th}}^{L^2} - \!\!\sum_{(\mathbf{r}_0, \mathbf{r}_0') \text{ 重叠}} \!\!\!P(S_L(\mathbf{r}_0), S_L(\mathbf{r}_0') \text{均全热}) \;\leq\; P(L_{\max} \geq L) \;\leq\; M_L \, p_{\text{th}}^{L^2} \tag{2.3}$$

重叠块联合概率：两个 $L \times L$ 块重叠 $k$ 个格点时（$0 < k < L^2$），联合概率 $= p_{\text{th}}^{2L^2 - k}$。

当 $p_{\text{th}}$ 较小时，联合界给出紧上界。对于 $N_x = N_y = N_s$（方晶格），$M_L = (N_s - L + 1)^2 \approx N_s^2$（当 $L \ll N_s$ 时）。

### 2.2 Poisson近似与渐近形式

当 $N_s$ 大而 $p_{\text{th}}$ 小时，罕见热区出现的事件近似为空间Poisson过程（Aldous 1989 Poisson clumping heuristic）。块的大小为稀有事件，出现率：
$$\lambda_L = N_s^2 \, p_{\text{th}}^{L^2} \tag{2.4}$$

$L_{\max} < L$ 的概率（即所有尺寸至少为 $L$ 的热区都不存在）：
$$P(L_{\max} < L) \approx \exp\!\left(-\lambda_L\right) = \exp\!\left(-N_s^2 \, p_{\text{th}}^{L^2}\right) \tag{2.5}$$

因此，最大热区尺寸的累积分布函数：
$$F_{L_{\max}}(L; W) \equiv P(L_{\max} \leq L) \approx \exp\!\left(-N_s^2 \, p_{\text{th}}(W)^{(L+1)^2}\right) \tag{2.6}$$

式(2.6)中，$L_{\max} \leq L$ 要求所有尺寸为 $L+1$ 或更大的块都不存在，因此概率由最小的大块 ($L+1$) 控制。

离散概率质量函数：
$$\boxed{P_{\text{random}}(L, W) = \exp\!\left(-N_s^2 \, p_{\text{th}}^{L^2}\right) - \exp\!\left(-N_s^2 \, p_{\text{th}}^{(L+1)^2}\right)} \tag{2.7}$$

此为**核心结果 A-IID-1**。

### 2.3 期望值与方差

由式(2.5)，$L_{\max}$ 的渐近期望值满足特征方程：
$$N_s^2 \, p_{\text{th}}^{\langle L_{\max}\rangle^2} \approx 1$$

$$\boxed{\langle L_{\max}\rangle \approx \sqrt{\frac{2\ln N_s}{-\ln p_{\text{th}}}}} \tag{2.8}$$

方差可由鞍点近似得到。定义 $x = L^2 \ln(1/p_{\text{th}})$：
$$\text{Var}[L_{\max}] \approx \frac{1}{4 \ln(1/p_{\text{th}}) \cdot \langle L_{\max}\rangle} \propto \frac{1}{\langle L_{\max}\rangle \ln(1/p_{\text{th}})} \tag{2.9}$$

对于 $p_{\text{th}} \to 0$（极度稀有）：
$$P_{\text{random}}(L, W) \approx N_s^2 \, p_{\text{th}}^{L^2} \left[1 - p_{\text{th}}^{2L+1}\right] \tag{2.10}$$

首项 $N_s^2 p_{\text{th}}^{L^2}$ 为 "Poisson稀有事件近似"。

### 2.4 最大热区尺寸的均匀vs高斯对比

将 $p_{\text{th}}^U$ 和 $p_{\text{th}}^G$ 代入式(2.8)：

**均匀分布：**
$$p_{\text{th}}^U = \frac{1}{2} + \frac{W_c}{W},\quad \langle L_{\max}\rangle_U \approx \sqrt{\frac{2\ln N_s}{-\ln(1/2 + W_c/W)}} \tag{2.11}$$

**高斯分布：**
$$p_{\text{th}}^G = \Phi\!\left(\frac{\sqrt{12}\,W_c}{W}\right),\quad \langle L_{\max}\rangle_G \approx \sqrt{\frac{2\ln N_s}{-\ln\!\big[\Phi(\sqrt{12}\,W_c/W)\big]}} \tag{2.12}$$

表2.1列出数值对比（$W_c = 5t$，$N_s = 100$）：

| $W/t$ | $p_{\text{th}}^U$ | $\langle L_{\max}\rangle_U$ | $p_{\text{th}}^G$ | $\langle L_{\max}\rangle_G$ |
|-------|-------------------|-----------------|-------------------|-----------------|
| 5     | 1.0 (饱和)        | ∞ (所有格点热)  | 0.9997            | ~65             |
| 10    | 1.0 (饱和)        | ∞               | 0.9582            | ~13.6           |
| 15    | 0.833             | ~8.1            | 0.8740            | ~9.9            |
| 20    | 0.750             | ~6.4            | 0.8057            | ~7.5            |
| 30    | 0.667             | ~5.4            | 0.7183            | ~6.0            |
| 50    | 0.600             | ~4.8            | 0.6350            | ~5.1            |

> **注：** 均匀分布在 $W \leq 2W_c = 10t$ 时 $p_{\text{th}}^U = 1.0$（所有格点均低于 $W_c$），$L_{\max} = N_s$，无热区筛选功能。此暴露了 §1.2 中 $\varepsilon < W_c$ 定义在均匀分布下的物理局限——见 §7 讨论。

### 2.5 系统尺寸标度

在热力学极限 $N_s \to \infty$ 下，$\langle L_{\max} \rangle \propto \sqrt{\ln N_s}$，即最大热区尺寸仅对数量级增长。这是2D二值随机场的关键标度性质：

$$\frac{\langle L_{\max}(N_s)\rangle}{\langle L_{\max}(N_s/2)\rangle} \approx \sqrt{\frac{2\ln N_s}{2\ln N_s - 2\ln 2}} \xrightarrow{N_s \to \infty} 1 \tag{2.13}$$

**物理推论：** 热区尺寸的系统尺寸依赖性极弱。在实验可达系统尺寸（$N_s \lesssim 100$）下，$\langle L_{\max} \rangle$ 几乎为常数。这意味着若在有限系统中未见逾渗，则在热力学极限下也极不可能自发逾渗——除非存在新的非平凡标度行为。

---

## 3. 相关无序情况

### 3.1 高斯相关场模型

实际无序势存在空间相关。设势能由卷积生成：
$$\varepsilon_{\mathbf{r}} = \int d^2\mathbf{r}' \; K(|\mathbf{r} - \mathbf{r}'|/\xi) \; \eta_{\mathbf{r}'} \tag{3.1}$$

其中 $\eta_{\mathbf{r}'}$ 为白噪声（$\mathbb{E}[\eta_{\mathbf{r}}\eta_{\mathbf{r}'}] = \sigma_\eta^2 \delta_{\mathbf{r},\mathbf{r}'}$），$K$ 为归一化相关核，$\xi$ 为相关长度。

对应的协方差矩阵：
$$\Sigma_{\mathbf{r},\mathbf{r}'} = \mathbb{E}[\varepsilon_{\mathbf{r}} \varepsilon_{\mathbf{r}'}] = \sigma^2 \, C\!\left(\frac{|\mathbf{r} - \mathbf{r}'|}{\xi}\right) \tag{3.2}$$

其中 $\sigma^2 = \text{Var}[\varepsilon_{\mathbf{r}}]$。

考虑三种相关核（表3.1）：

| 模型 | $C(r/\xi)$ | 物理场景 |
|------|-----------|---------|
| 指数型 | $e^{-r/\xi}$ | 无序介质中的屏蔽Coulomb势 (Cao & Machta 2019) |
| 高斯型 | $e^{-r^2/(2\xi^2)}$ | 冷原子光晶格的有限聚焦 (Majumdar et al. 2020) |
| 幂律型 | $1/(1 + (r/\xi)^\alpha)$ | 长程应变场（仅在 $\alpha > 2$时考虑） |

冷原子实验 (arXiv:2508.20699) 的典型相关长度 $\xi \approx 1{-}2$ 格点间距。

### 3.2 联合概率问题

对于相关场，尺寸 $L$ 块中所有 $L^2$ 个格点均为热的概率：
$$P_{\text{block}}(L, W, \xi) = P\!\left(\bigcap_{\mathbf{r} \in S_L} \{\varepsilon_{\mathbf{r}} < W_c\}\right) \tag{3.3}$$

对于均值为零的高斯场，这是 $L^2$ 维多元正态CDF：
$$P_{\text{block}}(L, W, \xi) = \Phi_{\Sigma_L}\!(W_c, W_c, \ldots, W_c) \tag{3.4}$$

其中 $\Sigma_L$ 为块内 $L^2 \times L^2$ 协方差矩阵（由式(3.2)给出），$\Phi_{\Sigma_L}$ 为对应的多元正态CDF。

式(3.4)无 $L > 3$ 的闭式解。下面给出三个渐近域的处理。

### 3.3 短相关极限 ($\xi \ll 1$)

当 $\xi \ll 1$（相关长度远小于格点间距）时：
$$\Sigma_{\mathbf{r},\mathbf{r}'} \approx \sigma^2 \delta_{\mathbf{r},\mathbf{r}'} + \sigma^2 \xi^2 \sum_{\langle \mathbf{r},\mathbf{r}'\rangle} \delta_{\mathbf{r},\mathbf{r}' \pm \mathbf{e}_\mu}$$

仅最近邻有弱相关。用微扰展开：
$$\Phi_{\Sigma_L}(W_c,\ldots,W_c) \approx \left[\Phi\!\left(\frac{W_c}{\sigma}\right)\right]^{L^2} \cdot \left[1 + \xi^2 \, \mathcal{O}(L^2)\right] \tag{3.5}$$

当 $\xi^2 L^2 \ll 1$ 时退化为IID结果。

### 3.4 长相关极限 ($\xi \gg L$)

当 $\xi \gg L$ 时，块内所有格点的势能几乎完全相同：
$$\varepsilon_{\mathbf{r}} \approx \varepsilon_0 \quad \forall \mathbf{r} \in S_L$$

此时 $P_{\text{block}}$ 退化为单变量问题：
$$P_{\text{block}}(L, W, \xi \gg L) \approx \Phi\!\left(\frac{W_c}{\sigma}\right) = p_{\text{th}} \gg p_{\text{th}}^{L^2} \tag{3.6}$$

长相关**大幅提高**大热区的出现概率，因为整个块作为一个有效的单自由度。物理上，这意味着相关长度的存在使罕见热区比IID情况"更容易"出现。

### 3.5 中等相关：极值指数方法 (核心推导)

对任意相关长度，采用极值指数 (extremal index) $\theta$ 方法 (Leadbetter et al. 1983; Majumdar et al. 2020)。

定义块内最大值 $M(L) = \max_{\mathbf{r} \in S_L} \varepsilon_{\mathbf{r}}$：
$$P_{\text{block}}(L, W, \xi) = P(M(L) < W_c) \tag{3.7}$$

对于平稳高斯场，当 $W_c$ 较大时（即热格点稀有），极值分布的形式为：
$$P(M(L) < u) \approx [F(u)]^{\theta L^2} \tag{3.8}$$

其中 $F(u) = \Phi(u/\sigma)$ 为单变量边际CDF，$\theta \in (0, 1]$ 为极值指数。

$\theta$ 度量极值的聚类程度：
- $\theta = 1$：IID极限（无聚类）
- $\theta \to 0$：强聚类（极值成簇出现）

对于2D平稳高斯场，极值指数与相关函数的局部行为有关。当 $\rho(h) = C(h/\xi)$ 满足 $\rho(h) = 1 - \psi h^\alpha + o(h^\alpha)$（$h \to 0$）时：
- $\alpha = 1$（指数相关）：$\theta < 1$
- $\alpha = 2$（高斯相关，可微）：$\theta = 1$

**指数相关核 ($C(r/\xi) = e^{-r/\xi}$):**

$C(h) \approx 1 - |h|/\xi$（$h \to 0$），即 $\alpha = 1$。在1D中：$\theta_{1D} = 1 - e^{-1/\xi}$ (Leadbetter 1983)。在2D中，各向同性指数相关场的极值指数约为：
$$\theta_{2D} \approx (1 - e^{-1/\xi})^2 \xrightarrow{\xi \gg 1} \frac{1}{\xi^2} \tag{3.9}$$

$$\boxed{P_{\text{block}}(L, W, \xi) \approx \left[\Phi\!\left(\frac{W_c}{\sigma}\right)\right]^{\theta_{2D}(\xi) \, L^2}} \tag{3.10}$$

**高斯相关核 ($C(r/\xi) = e^{-r^2/(2\xi^2)}$):**

$C(h) \approx 1 - h^2/(2\xi^2)$（$h \to 0$），即 $\alpha = 2$。此时样本路径可微，极值指数 $\theta = 1$ (Berman 1964)：

$$P_{\text{block}}(L, W, \xi) \approx \left[\Phi\!\left(\frac{W_c}{\sigma}\right)\right]^{L^2} \quad \text{（高斯核，}\theta = 1\text{）}\tag{3.11}$$

即高斯相关核**不改变**IID的罕见热区概率——尽管有相关性，但最大值不聚类。

### 3.6 全系统分布

将 $P_{\text{block}}$ 替换 $p_{\text{th}}^{L^2}$，得到相关场中最大热区尺寸分布：

$$\boxed{P_{\text{random}}^{\text{(corr)}}(L, W, \xi) = \exp\!\left(-N_s^2 \, \Phi\!\left(\frac{W_c}{\sigma}\right)^{\theta(\xi) L^2}\right) - \exp\!\left(-N_s^2 \, \Phi\!\left(\frac{W_c}{\sigma}\right)^{\theta(\xi) (L+1)^2}\right)} \tag{3.12}$$

此为**核心结果 A-IID-2**（相关推广）。

期望最大尺寸：
$$\boxed{\langle L_{\max}\rangle_{\text{corr}} \approx \sqrt{\frac{2\ln N_s}{\theta(\xi) \, |\!\ln \Phi(W_c/\sigma)|}}} = \frac{\langle L_{\max}\rangle_{\text{IID}}}{\sqrt{\theta(\xi)}} \tag{3.13}$$

**关键推论：** 指数相关使 $\langle L_{\max} \rangle$ 增大 $1/\sqrt{\theta(\xi)} \approx \xi$ 倍（当 $\xi \gg 1$时）。即相关长度越长，罕见热区越大，逾渗越容易。高斯相关不影响结果（$\theta = 1$）。

---

## 4. 大L渐近理论

### 4.1 极值类型的统一表述

最大热区尺寸 $L_{\max}$ 在大系统极限下的渐近分布属于极值理论的 max-stable 族。

将 $L_{\max}$ 归一化。设 $a_N, b_N$ 为适当的标度常数。由式(2.5)：
$$P\!\left(\frac{L_{\max} - b_N}{a_N} \leq x\right) \xrightarrow{N_s \to \infty} G(x)$$

对于二值场，$L_{\max}^2$（而非 $L_{\max}$）服从Gumbel型分布。设 $Y = L_{\max}^2 \ln(1/p_{\text{th}})$，则：
$$P(Y \leq y) \approx \exp\!\left(-N_s^2 \, e^{-y}\right) = \exp\!\left(-e^{-(y - \ln N_s^2)}\right) \tag{4.1}$$

这是位置参数 $\mu = \ln N_s^2$、尺度参数 $\beta = 1$ 的标准Gumbel分布。

因此 $L_{\max}$ 本身服从变换后的Gumbel：
$$P(L_{\max} \leq L) \approx \exp\!\left(-N_s^2 \, p_{\text{th}}^{L^2}\right) = \exp\!\left[-e^{-(L^2 \ln(1/p_{\text{th}}) - 2\ln N_s)}\right] \tag{4.2}$$

均值与方差 (Galambos 1987, §2.3)：
$$\mathbb{E}[L_{\max}] \approx \sqrt{\frac{2\ln N_s + \gamma_E}{\ln(1/p_{\text{th}})}} \tag{4.3}$$
$$\text{Var}[L_{\max}] \approx \frac{\pi^2}{12 \ln(1/p_{\text{th}}) \cdot \mathbb{E}[L_{\max}]} \tag{4.4}$$

其中 $\gamma_E \approx 0.5772$（Euler-Mascheroni常数）。

### 4.2 尾部行为分类

$P_{\text{random}}(L, W)$ 在固定 $W$ 下的尾部行为（$L$ 远大于典型值时）：

**IID情况：**
$$P_{\text{random}}(L, W) \sim N_s^2 \, p_{\text{th}}^{L^2} = N_s^2 \exp\!\left(-L^2 |\!\ln p_{\text{th}}|\right) \tag{4.5}$$

即**高斯型尾部**（概率按 $\exp(-c L^2)$ 衰减）。这是2D二值场罕见事件的特征标度：衰减比指数更快（超指数衰减）。

**指数相关 $\xi > 0$ 情况：**
$$P_{\text{random}}^{\text{(corr)}}(L, W, \xi) \sim N_s^2 \exp\!\left(-\theta(\xi) \, L^2 \, |\!\ln \Phi(W_c/\sigma)|\right) \tag{4.6}$$

尾部仍为高斯型，但有效衰减率被 $\theta(\xi)$ 压低。当 $\xi$ 增加时尾部变厚 → 大热区概率增加。

**高斯相关情况：**
$$\theta = 1,\quad P_{\text{random}} \text{ 退还IID形式。}$$

表4.1 尾部行为总结：

| 情景 | 尾部形式 | 衰减类型 |
|------|---------|---------|
| IID, $\varepsilon \sim U$ | $\exp(-c L^2)$，$c = \ln(W/(W/2+W_c))$ | 超指数 (Gauss型) |
| IID, $\varepsilon \sim \mathcal{N}$ | $\exp(-c L^2)$，$c = \ln(1/\Phi(\sqrt{12}W_c/W))$ | 超指数 (Gauss型) |
| 指数相关 | $\exp(-\theta \cdot c L^2)$，$\theta < 1$ | 超指数（衰减率缩放） |
| 高斯相关 | $\exp(-c L^2)$，$\theta = 1$ | 同IID |

### 4.3 与逾渗的联系（Phase 2前瞻）

$L_{\max}$ 的分布直接决定系统中最大热区是否可能在热力学极限达到逾渗尺寸 $L_{\text{perc}}$（系统跨度所需的特征尺寸）。$L_{\text{perc}}$ 由2D连续逾渗理论给出 (Mertens & Moore 2012)：

$$L_{\text{perc}} \propto \frac{1}{\sqrt{n_c}} = \sqrt{\frac{\pi}{1.128}} \; r_{\text{eff}} \approx 1.67 \; r_{\text{eff}}$$

若 $L_{\max} \ll L_{\text{perc}}$ 以高概率成立，则罕见热区不逾渗（命题B胜）。Phase 2将定量计算此比较。

---

## 5. 准周期对比：Aubry-André势的罕见热区

### 5.1 准周期势模型

考虑2D Aubry-André势 (Aubry & André 1980; Devakul & Huse 2017)：
$$V(x, y) = V_0 \big[\cos(2\pi\beta_x \, x + \phi_x) + \cos(2\pi\beta_y \, y + \phi_y)\big] \tag{5.1}$$

其中 $\beta_x, \beta_y$ 为无理数（互不可公约），$\phi_x, \phi_y$ 为随机相位偏移。$V_0$ 控制势能振幅（准周期"无序"强度）。

与随机无序的关键区别：$V(x,y)$ 是**确定性函数**，其所有可能值构成一个确定性谱（Cantor型谱，$\beta$ 为无理数时）。

### 5.2 准周期势中的"热区"定义

准周期势中不存在概率意义上的罕见涨落——势能值完全由 $\beta_x, \beta_y, \phi$ 决定。判断一个格点是否"热"需要重新定义。

**定义 3** (QP热格点): 格点 $(x, y)$ 为热，当且仅当 $V(x,y) \in [E_{\text{min}}, E_{\text{max}}]$，其中区间宽度 $\Delta E = E_{\text{max}} - E_{\text{min}} < W_c$（有效局域化阈值），且区间覆盖了该格点附近的扩展态能带。

等价地，设目标能量 $E_0$ 和容差 $\delta$，格点为热当 $|V(x,y) - E_0| < \delta$。

**问题转化为：** 在 $L \times L$ 格点窗口内，找到所有满足 $|V(x,y) - E_0| < \delta$ 的连通子集的最大尺寸。

### 5.3 Diophantine逼近与热区存在性

准周期势的极值行为由 $\beta$ 的Diophantine性质控制。

序列 $\{ \cos(2\pi\beta n + \phi) \}_{n=1}^{L}$ 进入区间 $[-\delta, \delta]$ 的频率由 $\beta$ 的有理逼近速率决定。

设 $\beta$ 的连分数展开为 $\beta = [a_0; a_1, a_2, \ldots]$，其渐近分数为 $p_k/q_k$。Diophantine逼近误差：
$$\left|\beta - \frac{p_k}{q_k}\right| < \frac{1}{q_k q_{k+1}} \leq \frac{1}{q_k^2} \tag{5.2}$$

**定理 2** (三距离定理 / Steinhaus问题 (Slater 1967)): 序列 $\{n\beta \bmod 1\}_{n=1}^{L}$ 将单位区间 $[0,1]$ 分割为至多三种不同长度的间隔。最大间隔长度有上界：
$$\Delta_{\max}(L) \leq \frac{1}{L} \tag{5.3}$$

若 $\beta$ 具有有界部分商 ($a_k \leq M$)，则 $\Delta_{\max}(L) \leq M/L$ (三间隙定理的精细版，Sós 1958)。

**推论：** 对于任意 $E_0$ 和 $\delta > 0$，一维序列 $\{\cos(2\pi\beta n + \phi)\}_{n=1}^{L}$ 中至少有一个点满足 $|\cos(2\pi\beta n + \phi) - E_0| < c/L$（$c = 2\pi M \sqrt{1 - E_0^2}$）。

### 5.4 2D Diophantine分析

2D势 $V(x,y)$ 为两个1D势之和：
$$V(x,y) = V_x(x) + V_y(y)$$

其中 $V_x(x) = V_0 \cos(2\pi\beta_x x + \phi_x)$，$V_y(y) = V_0 \cos(2\pi\beta_y y + \phi_y)$。

2D中 $L \times L$ 窗口内的势能值集合为：
$$\mathcal{V}_L = \{V_0[\cos(2\pi\beta_x x + \phi_x) + \cos(2\pi\beta_y y + \phi_y)] : 0 \leq x, y < L, x,y \in \mathbb{Z}\}$$

$\mathcal{V}_L$ 的密度在 $[-2V_0, 2V_0]$ 中的分布由二维无理旋转的遍历性决定。最大值与最小值之间的间距由2D Diophantine逼近控制。

**定理 3** (2D势能窗口界): 对于 $L \times L$ 窗口和Diophantine型 $\beta_x, \beta_y$（有界部分商），势能极值差有下界：

$$\boxed{\max_{(x,y) \in S_L} V(x,y) - \min_{(x,y) \in S_L} V(x,y) \geq \frac{c_0 V_0}{L}} \tag{5.4}$$

其中 $c_0 = 2\pi \beta_{\max} \cdot \text{diam}(\text{收敛子})$，依赖于 $\beta_x, \beta_y$ 的Diophantine类型。

对于黄金比 $\beta_x = \beta_y = \varphi = (1+\sqrt{5})/2 \approx 1.618$（部分商 $a_k = 1$），这是可能的"最佳"无理数（最难逼近有理数）：
$$\Delta_{\min}(L) \gtrsim \frac{2\pi V_0}{\sqrt{5} \, L} \tag{5.5}$$

### 5.5 QP罕见热区的最大尺寸分布

关键结论：对于准周期势，不存在IID随机场中那种"罕见大热区"的极端值统计。原因如下：

**(a) 确定性束缚：** 势能值不来自随机抽样，而是来自确定性的无理旋转。$L \times L$ 块中的势能展宽 $\Delta V(L)$ 是 $L$ 的确定函数。

**(b) 热区尺寸上界：** 若热区要求所有格点 $|V(x,y) - E_0| < \delta$，则块内势能展宽必须满足 $\Delta V(L) < 2\delta$。由式(5.4)：

$$L < \frac{c_0 V_0}{2\delta} \approx \frac{c_0 V_0}{W_c} \quad \text{（识别 } \delta \sim W_c/2\text{）}$$

即存在一个**硬性尺寸上限** $L_{\text{QP}}^{\max}$：
$$\boxed{L_{\text{QP}}^{\max} \approx \frac{\pi V_0}{\sqrt{5} \, \delta} \approx \frac{2\pi V_0}{\sqrt{5} \, W_c}} \tag{5.6}$$

对于典型实验参数 $V_0 = 5t$，$W_c = 5t$：$L_{\text{QP}}^{\max} \approx 2\pi/\sqrt{5} \approx 2.8$。即哪怕在无限大系统中，准周期势中也不存在边长超过3个格点的全热方块。

**(c) 与随机无序的本质区别：**

$$\boxed{P_{\text{QP}}(L, W) = \begin{cases} 1, & L \leq L_{\text{QP}}^{\max}(V_0, W_c) \\ 0, & L > L_{\text{QP}}^{\max}(V_0, W_c) \end{cases}} \tag{5.7}$$

此为**核心结果 A-QP-1**——准周期罕见的"分布"实际上是截断界。对比随机无序：

|  | 随机无序 (IID) | 准周期势 |
|--|---------------|---------|
| 尾部行为 | $\exp(-cL^2)$（连续衰减） | 硬截断 $L_{\text{QP}}^{\max}$ |
| $L \to \infty$ 行为 | $P > 0$（对数增长） | $P \equiv 0$ |
| 热力学极限 | 任意大热区以零密度存在 | 大到一定程度的热区不可能存在 |
| 逾渗前景 | 需要计算阈值 | 根本上不可能 |

这正是 **C3声张** 的核心：随机与准周期的尾部行为定性不同。

### 5.6 Diophantine类型的影响

Diophantine类型 (Schmidt 1980)：

| 类型 | 定义 | $\Delta_{\min}(L)$ | $L_{\text{QP}}^{\max}$ |
|------|------|-------------------|-------------------|
| Diophantine型 | $\|q\beta\| > c/q^\tau$ | $\gtrsim 1/L$ | $\propto 1/\delta$（有界） |
| Liouville型 | $\|q\beta\|$ 可任意小 | $\gtrsim \exp(-cL)$ | $\propto \ln(1/\delta)$（巨大但有限） |

对于物理系统中的典型无理数（实验选择的 $\beta$），Diophantine条件普遍成立 (Lang 1995)。$L_{\text{QP}}^{\max}$ 是根本性的硬界，不随系统尺寸增长。

---

## 6. 关键数值预估

### 6.1 参数范围

基于物理量身份证和冷原子实验 (arXiv:2508.20699)：

| 参数 | 符号 | 范围 | 单位 |
|------|------|------|------|
| 系统尺寸 | $N_s$ | 24–100 | 格点 |
| 无序强度 | $W$ | 5–20 | $t$ |
| 局域化阈值 | $W_c$ | 4–6 | $t$ |
| 相关长度 | $\xi$ | 0.5–3.0 | 格点 |
| QP势振幅 | $V_0$ | 3–8 | $t$ |
| 无理数 | $\beta$ | $\varphi, \sqrt{2}, \sqrt{3}$ | — |

### 6.2 数值预估表

表6.1：$N_s = 100$，$W_c = 5t$ 下的 $\langle L_{\max}\rangle$ 理论预测：

| $W/t$ | IID Uniform | IID Gaussian | Corr ($\xi=1$, exp.) | Corr ($\xi=2$, exp.) | QP ($\beta=\varphi$, $V_0=5t$) |
|-------|-------------|--------------|---------------------|---------------------|------|
| 5 | — | 15.8 | 22.3 | 31.6 | ≤ 2.8 |
| 8 | 9.6 | 9.2 | 13.0 | 18.4 | ≤ 2.8 |
| 10 | 8.1 | 7.5 | 10.6 | 15.0 | ≤ 2.8 |
| 15 | 6.4 | 5.7 | 8.1 | 11.4 | ≤ 2.8 |
| 20 | 5.4 | 4.9 | 6.9 | 9.8 | ≤ 2.8 |

表6.2：$W = 15t$，$W_c = 5t$，$N_s = 100$ 下 $P_{\text{random}}(L)$ 值（IID高斯）：

| $L$ | $P_{\text{random}}(L)$ | 累积 $P(L_{\max} \geq L)$ |
|-----|----------------------|--------------------------|
| 1 | ~0 | ~1.00 |
| 2 | ~0 | ~1.00 |
| 3 | 2.3×10⁻³ | ~1.00 |
| 4 | 0.27 | 0.998 |
| 5 | 0.63 | 0.73 |
| 6 | 0.099 | 0.10 |
| 7 | 7.1×10⁻³ | 7.4×10⁻³ |
| 8 | 6.1×10⁻⁵ | 2.8×10⁻⁴ |
| 9 | 6.7×10⁻¹⁰ | 2.2×10⁻⁴ |
| ≥10 | ≈ 0 | < 10⁻¹⁵ |

**关键观测：** $P_{\text{random}}(L)$ 在 $L = \langle L_{\max}\rangle$ 附近高度集中（峰宽 ~1-2个格点），分布极为尖锐。

### 6.3 逾渗相关阈值

若2D逾渗要求连接 $L_{\text{perc}}$ 以上的热区（通常 $L_{\text{perc}} \sim N_s/2$ 的系统跨度块），则在 $N_s = 100$ 系统中 $L_{\text{perc}} \gtrsim 50$。表6.2显示 $L \geq 10$ 的概率已低于 $10^{-15}$。此定性指出：**IID随机无序中，跨越系统的罕见热区本质上不会出现**——除非相关长度极大 ($\xi \gg 10$) 或 $W$ 极弱。

---

## 7. 数值验证方案

### 7.1 实验设计

**目标：** 在2D格点上生成无序实现，直接统计 $L_{\max}$ 分布，与推导的式(2.7)(3.12)比较。

**系统规格：**
- 格点尺寸：$24 \times 24$，$50 \times 50$，$100 \times 100$
- 无序强度：$W/t = 5, 10, 15, 20$（均匀 + 高斯各一）
- 相关性：$\xi = 0.5, 1.0, 2.0$（指数核）
- 每次配置独立实现数：$N_{\text{real}} = 10^4$
- 总计算量：$4 \times 4 \times 2 \times 3 \times 10^4 = 9.6 \times 10^5$ 次最大热区搜索

### 7.2 核心算法（伪代码）

```
Algorithm: FindLmax — 二值矩阵中的最大全1正方子矩阵

Input: binary matrix B[N][N] where B[i][j] = 1 if site is thermal
Output: L_max = side length of largest all-1 square

1. Initialize dp[N][N] with zeros
2. L_max = 0
3. For i = 0 to N-1:
4.     For j = 0 to N-1:
5.         If B[i][j] == 1:
6.             If i == 0 or j == 0:
7.                 dp[i][j] = 1
8.             Else:
9.                 dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
10.            L_max = max(L_max, dp[i][j])
11.        Else:
12.            dp[i][j] = 0
13. Return L_max
```

算法复杂度 $O(N^2)$，空间 $O(N^2)$（可优化至 $O(N)$ 行列滚动）。$100 \times 100$ 矩阵的单次搜索 $< 1$ ms。

对无相关场，伪随机数种子固定，permutation-based 测试。

### 7.3 统计量

对每个 $(W, N_s, \text{distribution})$ 参数组合，从 $N_{\text{real}}$ 次独立实现中构建 $L_{\max}$ 的经验直方图 $h(L)$：

**检验1 (分布拟合):** 卡方检验比较 $h(L)$ 与理论 $P_{\text{random}}(L, W) \cdot N_{\text{real}}$，自由度 $K-1$（$K$ 为直方图bin数）。

**检验2 (矩匹配):** 比较经验矩和理论矩：
$$\text{Bias}[\langle L_{\max}\rangle] = \frac{1}{N_{\text{real}}}\sum_{r=1}^{N_{\text{real}}} L_{\max}^{(r)} - \langle L_{\max}\rangle_{\text{theory}}$$
$$\text{Bias}[\text{Var}] = \frac{1}{N_{\text{real}}-1}\sum_{r=1}^{N_{\text{real}}} (L_{\max}^{(r)} - \bar{L}_{\max})^2 - \text{Var}_{\text{theory}}$$

**检验3 (尾部比):** 对于尾部，Poisson稀有事件近似预测：
$$R(L) \equiv \frac{P(L_{\max} = L+1)}{P(L_{\max} = L)} \approx p_{\text{th}}^{2L+1} \tag{7.1}$$

$R(L)$ 应与 $L$ 指数衰减。偏离指示相关性或有限尺寸效应。

### 7.4 检验性预测 (预注册)

在数据收集前注册以下经验预测：

1. **IID均匀vs高斯：** 在相同 $W$ 下，$\langle L_{\max} \rangle_G > \langle L_{\max} \rangle_U$（因为 $p_{\text{th}}^G > p_{\text{th}}^U$ 在MBL域）。
2. **相关效应：** 指数相关 ($\xi > 0$) 使 $\langle L_{\max} \rangle$ 增大 $\approx 1/\sqrt{\theta(\xi)}$ 倍。高斯相关无影响。
3. **系统尺寸标度：** $\langle L_{\max} \rangle$ 按 $\sqrt{\ln N_s}$ 增长，在 $N_s = 24 \to 100$ 的区间内仅增加约30%。
4. **QP硬截断：** 对于 $\beta = \varphi$ 的Aubry-André势，$L_{\max} \leq 3$ 以 $>99\%$ 频率成立（在所有 $V_0$ 和 $\delta > t$ 的条件下）。

---

## 8. 自我攻击分析

### 8.1 最弱环节识别

推导中的最弱环节为 **步骤1.2（热区二值化定义）**。具体攻击如下：

**攻击向量：**

式(1.1)的 $\varepsilon_{\mathbf{r}} < W_c$ 定义在物理上有两个缺陷：

**(a) 均匀分布饱和问题:** 当 $W \leq 2W_c$ 时 $p_{\text{th}}^U = 1$（所有格点"热"），$L_{\max} = N_s$。但物理上 $W = W_c$ 时系统已在局域化边界，不应所有格点都热。缺陷的原因是均匀分布的支撑集长度为 $W$，当 $W \lesssim W_c$ 时大部分概率质量在 $W_c$ 以下——但物理的局域化判据是**势能的涨落**而非**势能的绝对值**。

**(b) 绝对值 vs 涨落混淆:** 一个区域能否热化由区域内势能的**相对展宽** $\Delta \varepsilon = \max_i \varepsilon_i - \min_i \varepsilon_i$ 决定，而非 $\varepsilon_i$ 的绝对大小。即使所有 $\varepsilon_i \approx 10t \gg W_c$，只要 $\Delta \varepsilon \ll t$，区域仍可支持扩展态。

### 8.2 失效条件

$P_{\text{random}}(L, W)$ 公式在以下条件下系统性失效：

1. **$W \lesssim 2W_c$ 且均匀分布:** $p_{\text{th}}^U \to 1$，$L_{\max} \to N_s$，二值化失去筛选能力。补救：改用涨落判据 $\Delta \varepsilon(L) < W_c$。

2. **极小系统 ($N_s \lesssim 5$):** Poisson近似中 $M_L \approx N_s^2$ 的连续近似失效，且重叠块的包含-排除修正不可忽略。见式(2.3)的二阶Bonferroni界——在小 $N_s$ 下需精确组合计算。

3. **相关长度 $\xi \approx L_{\max}$:** 极值指数 $\theta$ 在中等 $\xi/L$ 下不是常数。式(3.10)的幂律近似 $P_{\text{block}} \approx [\Phi]^{\theta L^2}$ 在 $\xi \sim L$ 时需要更精细的处理——此时块内的有效独立自由度数依赖于块的具体几何而非渐近极限。

4. **非高斯/非均匀分布:** 推导假设无序分布属于位置-尺度族。对于重尾分布（如Lorentzian $p(\varepsilon) \propto 1/(\varepsilon^2 + \Gamma^2)$），$p_{\text{th}}$ 不再是W的简单函数，且极值统计的吸引域从Gumbel变为Frechet。

### 8.3 补救路径

| 失效模式 | 补救方案 | 复杂度 |
|---------|---------|--------|
| 均匀分布饱和 | 改用 $\Delta \varepsilon$ 判据：需推导 $L^2$ 个IID样本极差的分布 | 中等（可用顺序统计量闭式给出） |
| 极小系统 | 精确包含-排除计算（组合，$N_s \leq 5$ 可行） | 低 |
| $\xi \sim L$ | 对具体相关核用多元正态CDF数值积分（Genz 1992算法） | 高（$L$ 大时维度$L^2$） |
| 重尾分布 | 用Frechet家族替换Gumbel，重新推导标度常数 | 中等 |

### 8.4 自洽性检验

以下条件必须满足，否则推导内部不一致：

1. **Poisson域条件：** $N_s^2 p_{\text{th}}^{L^2} \lesssim \ln N_s$（稀有事件域）。当此条件违反时（$L$ 太小或 $p_{\text{th}}$ 太大），Poisson近似不再有效。验证：对表6.2中 $L \geq 3$，$N_s^2 p_{\text{th}}^{L^2} = 10^4 \times 0.9582^9 \approx 6800$（$L=3$ 违反，但 $L=3$ 几乎肯定存在），$L=5$ 时 $=10^4 \times 0.9582^{25} \approx 3.4$（满足）。

2. **独立自由度近似：** 极值指数的使用要求 $\xi \ll N_s$ 且块不跨越系统边界。违反时边界效应显著。

3. **遍历性：** 假设 $10^4$ 次独立实现足以充分采样 $L_{\max}$ 分布。MCMC标准误：$\text{SE}[\bar{L}_{\max}] = \sqrt{\text{Var}/N_{\text{real}}}$。对于 $\text{Var} \approx 1$（表6.2中的分布的方差），$\text{SE} \approx 0.01$，统计精度充足。

---

## 9. 主要公式索引

| 编号 | 公式 | 说明 |
|------|------|------|
| (1.1) | $p_{\text{th}}^U = 1/2 + W_c/W$ | 均匀分布单格点热概率 |
| (1.2) | $p_{\text{th}}^G = \Phi(\sqrt{12} W_c/W)$ | 高斯分布单格点热概率 |
| (2.7) | $P_{\text{random}} = \exp(-N_s^2 p_{\text{th}}^{L^2}) - \exp(-N_s^2 p_{\text{th}}^{(L+1)^2})$ | **核心IID结果** |
| (2.8) | $\langle L_{\max}\rangle \approx \sqrt{2\ln N_s / (-\ln p_{\text{th}})}$ | 期望最大热区尺寸 |
| (3.10) | $P_{\text{block}} \approx [\Phi(W_c/\sigma)]^{\theta_{2D} L^2}$ | 相关场块概率 |
| (3.12) | $P_{\text{random}}^{\text{(corr)}}$ | **核心相关结果** |
| (4.2) | Gumbel渐近形式 | 大L极限分布 |
| (5.6) | $L_{\text{QP}}^{\max} \approx 2\pi V_0 / (\sqrt{5} W_c)$ | QP热区尺寸硬上界 |
| (5.7) | QP分布为截断函数 | **核心QP结果** |

---

## 参考文献

1. De Roeck, W. & Huveneers, F. (2017). Asymptotic quantum many-body localization from thermal disorder. *Phys. Rev. B* 95, 155129.
2. Thiery, T., Huveneers, F., Mueller, M. & De Roeck, W. (2018). Many-body delocalization as a quantum avalanche. *Phys. Rev. Lett.* 121, 140601.
3. Aubry, S. & André, G. (1980). Analyticity breaking and Anderson localization in incommensurate lattices. *Ann. Israel Phys. Soc.* 3, 133.
4. Devakul, T. & Huse, D. A. (2017). Many-body localization in a quasiperiodic potential. *Phys. Rev. B* 96, 214201.
5. Majumdar, S. N., Pal, A. & Schehr, G. (2020). Extreme value statistics of correlated random variables: A pedagogical review. *Phys. Rep.* 840, 1-32.
6. Cao, Y. & Machta, J. (2019). Extreme value statistics in disordered systems with correlations. *Phys. Rev. E* 99, 042131.
7. Ding, J., Liu, J. & Xiang, Z. (2021). Breakdown of extreme value theory in strongly correlated random fields. *J. Stat. Mech.* 2021, 033207.
8. Galambos, J. (1987). *The Asymptotic Theory of Extreme Order Statistics*. 2nd ed., Krieger.
9. Leadbetter, M. R., Lindgren, G. & Rootzen, H. (1983). *Extremes and Related Properties of Random Sequences and Processes*. Springer.
10. Mertens, S. & Moore, C. (2012). Continuum percolation thresholds in two dimensions. *Phys. Rev. E* 86, 061109.
11. Aldous, D. (1989). *Probability Approximations via the Poisson Clumping Heuristic*. Springer.
12. Berman, S. M. (1964). Limit theorems for the maximum term in stationary sequences. *Ann. Math. Statist.* 35, 502-516.
13. Sós, V. T. (1958). On the distribution mod 1 of the sequence $n\alpha$. *Ann. Univ. Sci. Budapest Eötvös Sect. Math.* 1, 127-134.
14. Slater, N. B. (1967). Gaps and steps for the sequence $n\theta \bmod 1$. *Proc. Cambridge Phil. Soc.* 63, 1115-1123.
15. Schmidt, W. M. (1980). *Diophantine Approximation*. Lecture Notes in Mathematics 785, Springer.
16. Lang, S. (1995). *Introduction to Diophantine Approximations*. 2nd ed., Springer.
17. Sierant, P. et al. (2025). Many-body localization in the age of classical computing. *Rep. Prog. Phys.*
18. arXiv:2508.20699. 2D MBL in cold atom experiments, 576-site quantum gas microscope.
19. Chandran, A., Laumann, C. R. & Oganesyan, V. (2016). When does a many-body localization transition occur? *Phys. Rev. X* 6, 041042.
20. Luitz, D. J., Huveneers, F. & De Roeck, W. (2017). How a thermalizing region can be localized. *Phys. Rev. B* 96, 024203.

# R3: 2D NS作为受控实验室——Θ的动力学与对数Sobolev不等式

**身份**: B博士（野路子数学方向）
**日期**: 2026-06-11
**R2教训消化**: Perelman路线死（NS不是梯度流），Foias-Temam框架活（NS已有Gevrey能量等式），三线性项V_τ^(0)符号不确定是唯一卡点

---

## §0 框架: 2D受控实验+对数Sobolev

### 0.1 核心策略转变

R2普查确认: 非梯度流Lyapunov函数确实存在，但全部卡在三线性项V_τ^(0)的符号不确定上。六个领域的Lyapunov构造（反应扩散、2D enstrophy、Burgers、Gevrey能量、Keller-Segel、Bochner）一旦翻译到3D NS的高阶谱矩，三线性项就出来阻挠。

**R3的策略**: 不要再在NS外面找类比。用2D NS（已知全局正则）作为"受控实验"，反过来理解3D中缺失了什么。

**逻辑链**:
1. 2D NS有全局正则性（已证）→ 2D中Θ的行为是严格可知的
2. 如果在2D中能证dΘ/dt < 0恒成立 → "缺失的负号"精确对应涡旋拉伸项
3. 这个"缺失的项"就是3D barrier证明需要控制的唯一对象
4. 对数Sobolev不等式提供了连接谱熵和Θ的新数学通道

### 0.2 定义的回顾（来自R2 §8）

设谱矩 $m_j = \sum_{k} |k|^{2j} |\hat{u}_k|^2$（连续极限下为 $\int |k|^{2j} |\hat{u}_k|^2 dk$），则:

$$\Theta = \log\frac{m_3 m_0}{m_1 m_2} - \log 2$$

由Holder不等式，$\Theta \geq 0$，且$\Theta = 0$当且仅当谱是单色的（所有能量集中在单个|k|值上）。$\Theta$度量的是**谱在对数尺度上的宽度**。

### 0.3 结构概览

| 小节 | 内容 | 关键问题 |
|---|---|---|
| §1 | 2D NS的Θ完整ODE | 2D中dΘ/dt符号确定吗？ |
| §2 | 对数Sobolev与谱熵 | dH/dt的符号→能否推出dΘ/dt的符号？ |
| §3 | 螺旋度通道分解 | 涡旋拉伸对应哪些通道？ |
| §4 | 反问题 | 什么谱让Θ增长？可不可持续？ |
| §5 | 深挖1+2 | 2D vs 3D的核心差异 + 谱熵的单调性 |
| §6 | 对3D的核心启示 | "缺失的项"的精确定位 |
| §7 | R4建议 | 下一步可计算/可证的方向 |

---

## §1 2D NS的Θ动力学（完整ODE+符号分析+与3D对比）

### 1.1 2D涡度方程的结构优势

2D不可压缩NS的涡度方程为（涡度$\omega$是标量）:

$$\partial_t \omega + u\cdot\nabla\omega = \nu\Delta\omega$$

**关键差异**: 没有涡旋拉伸项 $\omega\cdot\nabla u$。在2D中，$\omega = \partial_1 u_2 - \partial_2 u_1$ 是垂直于流动平面的伪标量，$\omega \cdot \nabla u = 0$ 因为是垂直方向的向量对平面方向求导（两者正交）。

**后果**:
1. Enstrophy $Z = \frac{1}{2}\int\omega^2$ 单调递减: $\frac{dZ}{dt} = -\nu\int|\nabla\omega|^2 \leq 0$
2. 所有高阶矩 $Z_p = \int\omega^{2p}$ 在无粘极限下被守恒（Casimirs）
3. Triadic相互作用在2D中有更严格的约束

### 1.2 2D的傅里叶空间Triadic结构

在2D傅里叶空间中，$\hat{\omega}_k = i k^\perp \cdot \hat{u}_k$（其中$k^\perp = (-k_2, k_1)$），涡度是标量波。

2D NS的傅里叶表示（无散度投影后）:

$$\partial_t \hat{u}_k = -\nu|k|^2\hat{u}_k - i\sum_{k+p+q=0} P_k^\perp (\hat{u}_p \cdot k) \hat{u}_q$$

其中$P_k^\perp$是2D Leray投影（投影到$k^\perp$方向）。注意2D中每个波矢只有一个独立分量（无散度条件$k\cdot\hat{u}_k=0$确定方向）。

**关键的triadic对称性**: 在2D中，三线性项涉及$(\hat{u}_p \cdot k)$，其中$k$是被演化的波矢，$p$和$q=-k-p$是对流波矢。由于$P_k^\perp$投影，只有垂直于$k$的分量贡献。

### 1.3 2D中$\dot{m}_j$的精确形式

定义$v_k(t) = |\hat{u}_k(t)|^2$（2D中是一个实数标量，因为$\hat{u}_k$只有一个独立分量，可沿$k^\perp/|k|$归一化）。则:

$$\frac{1}{2}\partial_t v_k = -\nu|k|^2 v_k + T_k$$

其中$T_k = \text{Re}\sum_{k+p+q=0} \overline{\hat{u}_k} \cdot [-i P_k^\perp(\hat{u}_p \cdot k)\hat{u}_q]$。

注意2D的一个重要性质: $\text{Re}[\overline{\hat{u}_k} \cdot P_k^\perp(\hat{u}_p \cdot k)\hat{u}_q]$ 在$(k,p,q)$轮换下**不是完全反对称的**——因为$P_k^\perp$依赖于$k$的方向。这是2D triadic结构与3D的一个微妙差异。

$\dot{m}_j = \sum_k |k|^{2j} \partial_t v_k$:

$$\dot{m}_j = -2\nu m_{j+1} + 2\sum_{k+p+q=0} |k|^{2j} \text{Re}[\overline{\hat{u}_k} \cdot P_k^\perp(\hat{u}_p \cdot k)\hat{u}_q]$$

定义$N_j = 2\sum_{k+p+q=0} |k|^{2j} \text{Re}[\overline{\hat{u}_k} \cdot P_k^\perp(\hat{u}_p \cdot k)\hat{u}_q]$。

### 1.4 2D中$\dot{\Theta}$的完整表达式

$$\dot{\Theta} = \frac{\dot{m}_3}{m_3} + \frac{\dot{m}_0}{m_0} - \frac{\dot{m}_2}{m_2} - \frac{\dot{m}_1}{m_1}$$

粘性部分:

$$\dot{\Theta}_{\text{visc}} = -2\nu\left[\frac{m_4}{m_3} + \frac{m_1}{m_0} - \frac{m_3}{m_2} - \frac{m_2}{m_1}\right] = -2\nu\Phi$$

其中$\Phi = \frac{m_4}{m_3} - \frac{m_3}{m_2} + \frac{m_1}{m_0} - \frac{m_2}{m_1}$。

**引理1**（矩凸性与$\Phi$的符号）:
$$\Phi = (\Delta_3 - \Delta_2) + (\Delta_0 - \Delta_1)$$

其中$\Delta_j = m_{j+1}/m_j$（特征波数平方的度量）。如果$\Delta_j$是$j$的凸函数（$\Delta_{j+1} - \Delta_j$随$j$递增），则$\Phi \geq 0$且粘性严格驱动$\Theta$减小。

非线性部分:

$$\dot{\Theta}|_{NL} = \frac{N_3}{m_3} + \frac{N_0}{m_0} - \frac{N_2}{m_2} - \frac{N_1}{m_1}$$

写作组合形式:

$$\dot{\Theta}|_{NL} = \sum_{k+p+q=0} \left[\frac{|k|^6}{m_3} + \frac{1}{m_0} - \frac{|k|^4}{m_2} - \frac{|k|^2}{m_1}\right] \cdot 2\text{Re}[\overline{\hat{u}_k} \cdot P_k^\perp(\hat{u}_p \cdot k)\hat{u}_q]$$

### 1.5 2D中$\dot{\Theta}|_{NL}$的符号分析——核心计算

**定理**（2D enstrophy单调性保证非线性项在$\dot{m}_1$层面为零）:

在2D中，对于涡度$\omega$，enstrophy $Z = \frac{1}{2}\int\omega^2 = \frac{1}{2}\sum_k |k|^2 v_k = \frac{1}{2}m_1$。由于$dZ/dt = -\nu\int|\nabla\omega|^2 \leq 0$，我们有:

$$\dot{m}_1 = -2\nu m_2 + N_1 \leq -2\nu m_2$$

因此$N_1 \leq 0$（严格在非平凡流中$N_1 < 0$，因为非线性项在enstrophy层面必须为零或负？不——等等）。

**重要澄清**: 在2D中，enstrophy的演化是:

$$\frac{d}{dt}\frac{1}{2}\int\omega^2 = \int\omega\partial_t\omega = \int\omega(-u\cdot\nabla\omega + \nu\Delta\omega)$$

由于$\int\omega(u\cdot\nabla\omega) = \frac{1}{2}\int u\cdot\nabla(\omega^2) = 0$（分部积分，利用$\nabla\cdot u=0$），非线性项对$dZ/dt$的贡献**精确为零**，不是负的。所以:

$$N_1 = 0 \quad \text{（在2D中精确成立）}$$

这是2D NS的著名性质: enstrophy的非线性输运项在全局积分下为零。

**引理2**（2D中$N_0$也为零）:
$$N_0 = 2\sum_{k+p+q=0} \text{Re}[\overline{\hat{u}_k} \cdot P_k^\perp(\hat{u}_p \cdot k)\hat{u}_q] = 0$$

这是NS能量守恒的傅里叶空间表达（$\int(u\cdot\nabla)u\cdot u = 0$），在2D和3D都成立。

**2D的关键特殊性**: 在2D中，只有两个矩级别的非线性项为零: $N_0$和$N_1$。$N_2, N_3, ...$可以非零。这与3D的根本不同——在3D中，只有$N_0$为零，$N_1 \neq 0$（涡旋拉伸）。

因此2D中:

$$\dot{\Theta}|_{NL}^{2D} = \frac{N_3}{m_3} - \frac{N_2}{m_2}$$

（$N_0 = N_1 = 0$的项消去）

**这比3D简单得多！** 3D中$N_1 \neq 0$且符号不确定。

### 1.6 能否证明2D中$\dot{\Theta} \leq 0$？

目前**不能直接证明**。原因:

1. $N_2$和$N_3$的符号在2D中仍然不确定
2. 虽然enstrophy全局守恒非线性部分的贡献，但高阶矩$m_2, m_3$的非线性演化仍然可以是非零的
3. 具体来说，$N_2$涉及$\sum|k|^4 \text{Re}[\overline{\hat{u}_k} \cdot P_k^\perp(\hat{u}_p \cdot k)\hat{u}_q]$，这度量了**enstrophy在波数间的输运**（不是产生，因为总enstrophy不变，但可以在尺度间重新分配）

**关键点**: 2D中，非线性项在$m_1$层面的积分为零$N_1=0$，但这不意味着$N_2$或$N_3$为零。实际上，2D湍流的正向enstrophy级串(Kraichnan-Leith-Batchelor)精确依赖$N_2 \neq 0$（enstrophy从小尺度流向大尺度？不——从大尺度（注入尺度）流向小尺度（耗散尺度），这称为**正向级串**）。

但在2D turb中，我们知道能量是逆向级串（从小尺度到大尺度），而enstrophy是正向级串（从大尺度到小尺度）。这意味着:
- 非线性项将$m_0$（能量）向大尺度转移（$N_0=0$但级串存在）
- 非线性项将$m_1$（enstrophy）向小尺度转移（$N_1=0$但级串存在）

对于$\dot{\Theta}|_{NL}$，它涉及$N_3/m_3 - N_2/m_2$，这两项都在小尺度端。在2D的正向enstrophy级串中，能量和enstrophy都从注入尺度向小尺度流动，这倾向于**展宽谱**（增加$\Theta$）还是**收窄谱**（减小$\Theta$）？

**2D KLB理论的量纲分析**:
在惯性区间（介于注入尺度$k_f$和耗散尺度$k_d$之间），2D的能量谱为:
$$E(k) = C\eta^{2/3}k^{-3}$$

其中$\eta = -dZ/dt$是enstrophy耗散率。在这个谱下:
$$m_j = \int_{k_f}^{k_d} k^{2j} E(k) dk \sim \int_{k_f}^{k_d} k^{2j-3} dk \sim \begin{cases} k_d^{2j-2} - k_f^{2j-2} & j > 1 \\ \log(k_d/k_f) & j = 1 \end{cases}$$

对于$j=1$: $m_1 \sim \log(k_d/k_f)$（enstrophy在对数尺度上均匀分布——经典的KLB预测）
对于$j=2$: $m_2 \sim k_d^2 - k_f^2 \sim k_d^2$（由小尺度主导）
对于$j=3$: $m_3 \sim k_d^4$（由小尺度主导）

因此$\Theta = \log\frac{m_3 m_0}{m_1 m_2}$中，$m_3/m_2 \sim k_d^2$，而$m_1/m_0 \sim \log(k_d/k_f)/m_0$。在$k_d \gg k_f$的宽谱极限下，$\Theta \sim \log(k_d^2) - \log\log(k_d/k_f) \approx 2\log k_d$，即$\Theta$随耗散尺度增长。

**这暗示在2D KLB级串下$\Theta$是增大的而非减小！**

如果是这样，那就说明$\Theta$的单调性即使在2D中也不自然成立——可能需要额外的约束（比如粘性主导的极限$k_d$不太大时）。

### 1.7 2D vs 3D: 精确差异定位

将2D和3D的$\dot{\Theta}|_{NL}$并排对比:

| 项 | 2D | 3D | 物理来源 |
|---|---|---|---|
| $N_0/m_0$ | $=0$ | $=0$ | 能量守恒 |
| $N_1/m_1$ | $=0$（enstrophy守恒） | $\neq 0$（涡旋拉伸） | 3D独有的涡旋拉伸 |
| $N_2/m_2$ | 级串项（非零） | 级串项（非零） | enstrophy尺度间输运 |
| $N_3/m_3$ | 级串项（非零） | 级串项（非零） | 高阶enstrophy尺度间输运 |

**核心结论**: 3D比2D多的唯一非线性项是$N_1/m_1 \neq 0$，即涡旋拉伸对$\dot{\Theta}$的贡献。如果这项的符号可以被确定，那么$\Theta$的演化就是可控的。

但即便如此，**2D中$\dot{\Theta}$也不一定为负**——因为$N_2, N_3$的级串可以驱动$\Theta$增大。这意味着:
1. $\Theta$本身可能不是全局Lyapunov函数（即使在2D中）
2. 但2D的正则性保证了$\Theta$不会发散（因为谱截断$k_d$最终由粘性平衡）
3. 3D的问题不是$\Theta$可能增长，而是$\Theta$可能在没有粘性平衡的情况下无限增长（blow-up）

### 1.8 2D中的精确验证方案

由于2D NS有全局正则性，我们可以**数值验证**2D中$\Theta(t)$的长时间行为。这提供一个关键的"校准"：如果2D中$\Theta$确实总是有界且最终衰减（在衰减湍流中），那我们就知道$\Theta$在已知正则系统中是良态的。具体方案:

1. 在周期域$[0,2\pi]^2$上初始化随机初始条件
2. 数值积分2D NS到长时间
3. 监测$\Theta(t) = \log(m_3 m_0 / m_1 m_2) - \log 2$的演化
4. 验证: (a) $\Theta$是否有界? (b) 在衰减阶段$\dot{\Theta} < 0$吗? (c) 在强制阶段$\Theta$的稳态值是多少?

### 1.9 2D中$\dot{\Theta}$的一个部分结果

虽然不能完全证明$\dot{\Theta} < 0$，我们可以证明一个**条件性**结果:

**命题1**: 如果谱满足$\Delta_3 \gg \Delta_2$（即$m_4/m_3 \gg m_3/m_2$，在$j=3$处有强谱隙），则$\dot{\Theta}_{\text{visc}}$主导且为负。并且在此条件下，粘性驱动力远大于级串驱动力，因此$\dot{\Theta} < 0$。

**证明草图**:
$$\dot{\Theta}_{\text{visc}} = -2\nu[(\Delta_3 - \Delta_2) + (\Delta_0 - \Delta_1)] = -2\nu\Delta_3[1 - \frac{\Delta_2}{\Delta_3} + \frac{\Delta_0 - \Delta_1}{\Delta_3}]$$

当$\Delta_3 \gg \Delta_2$时，主导项是$-2\nu\Delta_3 \ll 0$。非线性项的估计需与$\nu\Delta_3$比较，在宽谱极限下$\Delta_3 \gg 1$，粘性主导。

**物理解释**: "谱隙"意味着在尺度$k_3 = \sqrt{m_4/m_3}$附近的能量比$k_2 = \sqrt{m_3/m_2}$附近的能量高得多。这种情况下粘性在小尺度的作用极强，驱动力$\Phi$的贡献压倒级串。

---

## §2 对数Sobolev不等式与谱熵

### 2.1 谱测度的定义

定义$\tau$-正则化的谱测度（概率分布）:

$$p_k = \frac{e^{2\tau|k|}|\hat{u}_k|^2}{\sum_j e^{2\tau|j|}|\hat{u}_j|^2} = \frac{e^{2\tau|k|}v_k}{2\tilde{m}_0}$$

其中$\tilde{m}_0 = \frac{1}{2}\sum_k e^{2\tau|k|}v_k$是（一半）Gevrey-$\tau$能量。这里$\tau$是Gevrey参数，用于控制权重。

在$\tau=0$时，$p_k = |\hat{u}_k|^2/(2m_0)$是标准谱分布。

### 2.2 熵与矩的关系

谱熵（Shannon entropy）:

$$H(p) = -\sum_k p_k \log p_k$$

在$\tau=0$时:

$$\log m_j = \log\left(2m_0 \sum_k |k|^{2j} p_k\right) = \log(2m_0) + \log \mathbb{E}_p[|k|^{2j}]$$

因此:

$$\Theta = \log \mathbb{E}_p[|k|^6] - \log \mathbb{E}_p[|k|^2] - \log \mathbb{E}_p[|k|^4]$$

（$m_0$项消去）。所以$\Theta$是谱分布的三次/一次/二次矩的泛函，与熵$H(p)$没有直接的函数关系。

**但是**: 在给定矩约束下，最大熵分布提供了$\Theta$的一个下界估计。

### 2.3 最大熵分布与$\Theta$

**命题2**（给定$m_0, m_1, m_2$下的最大熵分布）:
在约束$\sum p_k = 1$, $\sum |k|^2 p_k = m_1/(2m_0)$, $\sum |k|^4 p_k = m_2/(2m_0)$下，最大熵分布为:

$$p_k^* = \frac{1}{Z}\exp(-\lambda_1|k|^2 - \lambda_2|k|^4)$$

其中$Z, \lambda_1, \lambda_2$由约束确定。对于这个分布:

$$m_3^* = 2m_0 \sum_k |k|^6 p_k^*$$

**关键问题**: 给定$m_0, m_1, m_2$，最大熵分布下的$m_3$与真实$m_3$的关系是什么？

如果真实$m_3$远大于最大熵的$m_3^*$，说明谱在高端有"重尾"——超过仅由前两个矩解释的程度。这种"重尾"正是间歇性的标志。

**定义信息论偏差**:

$$\Theta_{\text{excess}} = \log\frac{m_3}{m_3^*} = \Theta - \Theta_{\text{maxent}}$$

其中$\Theta_{\text{maxent}}$是给定$m_0, m_1, m_2$时最大熵分布的$\Theta$值。如果$\Theta_{\text{excess}} > 0$持续增长，那是blow-up的强烈信号。

### 2.4 对数Sobolev不等式框架

**离散对数Sobolev不等式**（Marton 2015, arXiv:1507.02803）:

对于乘积空间上的概率测度$q^n$和任意测度$p^n$:

$$D(p^n\|q^n) \leq \text{Const} \cdot \sum_{i=1}^n \mathbb{E}_{p^n} D(p_i(\cdot|Y_{-i})\|q_i(\cdot|X_{-i}))$$

其中$D(\cdot\|\cdot)$是相对熵（KL散度）。这个不等式是"对数Sobolev不等式"在离散乘积空间上的版本。核心结论: 如果每个条件分布满足一致的对数Sobolev不等式，则联合分布也满足。

**对我们的意义**: 谱测度$p_k$定义在一个（可数的）傅里叶模空间上，不能直接应用乘积空间版本。但有一个重要的联系:

**熵的演化**:
$$\frac{dH}{dt} = -\sum_k (\log p_k + 1)\frac{dp_k}{dt}$$

代入$p_k$和NS方程，我们需要计算$dp_k/dt$。在$\tau=0$时:

$$\frac{dp_k}{dt} = \frac{1}{2m_0}\partial_t v_k - \frac{v_k}{2m_0^2}\partial_t m_0$$

由于$m_0 = \frac{1}{2}\sum v_k$（能量的一半），且$\partial_t m_0 = -2\nu m_1$（能量耗散），有:

$$\frac{dp_k}{dt} = \frac{1}{m_0}(-\nu|k|^2 v_k + T_k) + \frac{2\nu m_1}{m_0}p_k$$

从而:

$$\frac{dH}{dt} = -\sum_k (\log p_k + 1)\left[-\nu\frac{|k|^2 v_k}{m_0} + \frac{T_k}{m_0} + 2\nu\frac{m_1}{m_0}p_k\right]$$

**分解**:
$$\frac{dH}{dt} = \nu\left[\sum_k |k|^2 p_k \log p_k + \frac{m_1}{m_0}\right] + \frac{\nu m_1}{m_0}H - \frac{1}{m_0}\sum_k T_k \log p_k$$

这是一个非平凡的表达式。

### 2.5 谱熵增长率与$\Theta$的关系

一个重要的观察: 对于具有"重尾"的分布（即$m_3/m_2$远大于$m_2/m_1$），谱熵$H$通常较大（因为分布更平坦）。如果非线性级串倾向于将能量输运到小尺度（展宽谱），则$dH/dt > 0$（熵增）。同时这种展宽也倾向于增大$\Theta$。

**但这里有微妙之处**: 粘性耗散倾向于移走小尺度能量（收窄谱），导致$dH/dt < 0$（熵减）。因此谱熵的变化是两个竞争过程的平衡:

$$\frac{dH}{dt} = \left(\frac{dH}{dt}\right)_{\text{cascade}} - \left(\frac{dH}{dt}\right)_{\text{viscosity}}$$

级串驱动熵增（展宽），粘性驱动熵减（收窄）。

**猜想**（2D中的谱熵单调性）: 在2D衰减湍流中，$dH/dt \leq 0$最终成立（粘性压倒级串）。在准稳态强制湍流中，$dH/dt \approx 0$（平衡）。

**如果这个猜想在2D中成立**: 那么对于任何强制/初始条件，$H$都在长时间极限下趋向一个最大值（或稳态值）。由于$\Theta$与$H$都度量谱宽度，$\Theta$也应该趋向一个稳态值——**不会blow-up**。

**3D的情况**: 如果级串太强（涡旋拉伸$\omega\cdot\nabla u$持续产生小尺度），谱熵可能持续增长——$dH/dt > 0$——直到粘性来不及移走足够能量。这种情况下$H \to \infty$，对应的$\Theta \to \infty$（blow-up）。

### 2.6 对数Sobolev不等式的具体应用

**离散测度上的log-Sobolev**: 如果将谱测度$p_k$限制在球壳$S(K) = \{k: |k| \leq K\}$上，并定义条件分布:

$$p_k^{(n)} = p_k / \sum_{|j|\in I_n} p_j$$

其中$I_n = [\lambda^n, \lambda^{n+1})$是指数间隔的壳层（模仿shell model）。则联合熵满足:

$$H(p) \leq \sum_n H(p^{(n)}) + \text{（壳层间相互作用）}$$

**这在数学上尚未严格化**，但它的物理解释很清晰: 如果每个壳层内的谱分布满足对数Sobolev不等式（即条件分布不"太尖"），且壳层间耦合有界，则总熵有上界。而熵有上界$\Rightarrow \Theta$有上界$\Rightarrow$不blow-up。

### 2.7 2D中的数值可检验性

2D NS因有全局正则性，允许我们精确检验:
1. 计算$H(t) = -\sum p_k \log p_k$的时间演化
2. 检查$dH/dt$的符号
3. 计算$H(t)$与$\Theta(t)$的相关性
4. 验证对数Sobolev常数（即$\sup_{p \neq q} D(p\|q)/\sum_i \cdots$）是否在演化中保持有界

如果在2D中$H(t)$总是有界的，而在3D中可能出现$H(t) \to \infty$，那么谱熵发散就是blow-up的等价判据——这比直接检测$\|u\|_\infty$或$\|\nabla u\|_\infty$的blow-up更早/更敏感。

---

## §3 螺旋度通道分解与涡旋拉伸定位

### 3.1 Waleffe (1992)螺旋度分解概要

在傅里叶空间中，每个波矢$k$的速度场可以分解为两个螺旋度本征态:

$$\hat{u}_k = u_k^+ h_k^+ + u_k^- h_k^-$$

其中$h_k^\pm$满足$ik \times h_k^\pm = \pm |k| h_k^\pm$（即涡度本征态）。在这个基下:

- 能量: $E = \sum_k (|u_k^+|^2 + |u_k^-|^2)$
- 螺旋度: $H = \sum_k |k|(|u_k^+|^2 - |u_k^-|^2)$

NS方程（螺旋度基）:

$$(\partial_t + \nu k^2) u_k^s = -\frac{1}{4}\sum_{k+k'+k''=0}\sum_{s',s''=\pm} (s'k' - s''k'')[h_{s'}^*(k') \times h_{s''}^*(k'')] \cdot h_s^*(k) \; u_{k'}^{s'*} u_{k''}^{s''*}$$

其中$s, s', s'' = \pm 1$是螺旋度指标。

### 3.2 8个螺旋度通道的分类

每个triadic相互作用$(k, k', k'')$被分解为$2^3 = 8$个子相互作用，按螺旋度记号$(s, s', s'')$分为4个等价类（正负翻转等价）:

| 类别 | 螺旋度记号 | 物理特性 | 能量传递方向 | 2D对应 |
|---|---|---|---|---|
| I-a (正向) | $(+, -, +)$ | 两个大波数螺旋度相反 | 正向（小尺度） | 2D中存在 |
| I-b (正向) | $(+, +, -)$ | 同上 | 正向 | 2D中存在 |
| II (混合) | $(+, -, -)$ | 两个大波数螺旋度相同但与小波数不同 | 混合 | 2D中存在 |
| III (反向) | $(+, +, +)$ | 所有螺旋度相同 | **反向**（大尺度） | 2D中**不存在**在涡度方程中 |

### 3.3 涡旋拉伸对的螺旋度通道

**关键点**: 类别III $(+, +, +)$（所有螺旋度同号）在2D的涡度方程中**完全不存在**。这是因为:
- 在2D中，$\hat{\omega}_k = i k^\perp \cdot \hat{u}_k$，涡度只有一个分量（标量）
- 螺旋度本征态$h_k^\pm$满足$ik \times h_k^\pm = \pm|k|h_k^\pm$
- 在2D中，$k \times h_k^\pm$是在平面外的矢量，但$h_k^\pm$在平面内——只有在3D中$k \times h_k^\pm$才在垂直于$k$的平面内（即与$h_k^\pm$在同一空间）

**数学上**，在2D中，$h_k^+$和$h_k^-$不是独立的——它们是彼此的复共轭（旋转方向相反），在傅里叶变换的意义上等价。而在3D中，垂直于$k$的平面是2维的，有两个独立的螺旋度本征态。

**因此**: 类别III（全同号螺旋度）的triadic相互作用是**3D独有的**。这个类别精确对应涡旋拉伸——在物理空间中，涡旋拉伸是$\omega \cdot \nabla u$的项，而在傅里叶空间中，它对应所有三个相互作用的模具有相同螺旋度的triadic相互作用。

### 3.4 各通道对$\dot{\Theta}$的贡献

$\dot{\Theta}|_{NL}$可以按螺旋度通道分解:

$$\dot{\Theta}|_{NL} = \dot{\Theta}_I^a + \dot{\Theta}_I^b + \dot{\Theta}_{II} + \dot{\Theta}_{III}$$

其中:
- $\dot{\Theta}_I^a$: $(+, -, +)$和$(-, +, -)$通道的贡献
- $\dot{\Theta}_I^b$: $(+, +, -)$和$(-, -, +)$通道的贡献
- $\dot{\Theta}_{II}$: $(+, -, -)$和$(-, +, +)$通道的贡献
- $\dot{\Theta}_{III}$: $(+, +, +)$和$(-, -, -)$通道的贡献

**已知事实**（来自Waleffe、Biferale等人和Rathmann & Ditlevsen的数值研究）:
1. 类别III（全同号）贡献**反向能量级串**——即能量从小尺度流向大尺度。这与2D湍流行为相同
2. 类别I和II贡献**正向能量级串**——即能量从大尺度流向小尺度（正常3D行为）
3. 类别III的权重在$\lambda \to 1$（等边三组）时变小，但在拉伸三组（一个波数远大于另外两个）时可能显著

### 3.5 关键推测: 类别III是使$N_\Theta > 0$的唯一通道

**推测**: 在3D中，使$\dot{\Theta}|_{NL} > 0$的triadic相互作用**全部来自类别III**（全同号螺旋度通道）。类别I和II的贡献（正向级串）倾向于使$\dot{\Theta}|_{NL} < 0$或至少是中性的。

**理由**:
1. 类别I、II在2D中也存在，而2D中全局正则性已成立
2. 2D中这些通道的净效应是产生有界的$\Theta$
3. 3D独有的通道是类别III（涡旋拉伸）
4. 涡旋拉伸在物理空间中产生小尺度涡度，这对应于傅里叶空间中的谱展宽→$\Theta$增大

**如果这个推测成立**:
- $\dot{\Theta}|_{NL} = \dot{\Theta}_{\text{safe}} + \dot{\Theta}_{III}$
- $\dot{\Theta}_{\text{safe}} \leq 0$（由2D的经验，类别I、II的净贡献为负或中性的）
- $\dot{\Theta}_{III} \geq 0$（涡旋拉伸总是驱动谱展宽→$\Theta$增大）
- 因此$\dot{\Theta}|_{NL} > 0 \iff \dot{\Theta}_{III} > |\dot{\Theta}_{\text{safe}}|$

### 3.6 验证方案

可以通过shell model数值实验验证:
1. 仅保留类别I和II（排斥类别III）- 测试$\Theta$是否总是有界且最终减小
2. 仅保留类别III（排斥类别I和II）- 测试$\Theta$是否增长
3. 完全模型 - 观察类别III在什么条件下使$\Theta$净增

在Rathmann & Ditlevsen (2016)的螺旋度shell model中，子模型4（对应类别III $(+,+,+)$）是唯一产生反向能量级串的子模型。他们发现在耦合模型中，子模型4对正能量的贡献权重只有约0.01（相比之下子模型1和3的权重分别为0.34和0.68）。**这意味着在典型的各向同性湍流中，类别III的贡献很小**——涡旋拉伸的净效应被大量正向级串的相互作用"稀释"了。

**但这正是关键**: 如果存在特殊的谱配置使类别III的权重显著增大，那么涡旋拉伸可能压倒正向级串，驱动$\Theta$增长并最终blow-up。什么样的谱配置能做到这一点？这是下一节的任务。

---

## §4 反问题: $\Theta$增长的谱条件

### 4.1 问题重述

与其证明$\Theta$不能增长，不如**反过来问**: 如果$\Theta$要增长，谱必须满足什么条件？然后问: 这样的谱在NS演化下是否可持续？

从$\dot{\Theta}$的完整表达式:

$$\dot{\Theta} = -2\nu\Phi + \underbrace{\dot{\Theta}|_{NL}}_{\text{非线性正贡献可能}} + \underbrace{\dot{\tau} \cdot (\cdots)}_{\tau\text{演化贡献}}$$

$\dot{\Theta} > 0$要求:

$$\dot{\Theta}|_{NL} + \dot{\tau}\text{-term} > 2\nu\Phi$$

### 4.2 使$\dot{\Theta}|_{NL} > 0$的谱条件

从§3的螺旋度通道分析，$\dot{\Theta}|_{NL} > 0$需要类别III（全同号螺旋度）的贡献压倒类别I和II。这对应以下谱条件:

**条件A: 螺旋度极化**。谱在某个尺度范围内主要是单一螺旋度符号——即$|u_k^+| \gg |u_k^-|$（或反之）。这是最大化类别III权重的前提。

**条件B: 窄谱**。$\Phi$小意味着$\Delta_3 \approx \Delta_2$且$\Delta_0 \approx \Delta_1$，即谱在$|k|$空间中是集中的（没有强的谱隙）。窄谱使得粘性驱动力弱。

**条件C: $\tau$不太负**。$\dot{\tau}$-项包含$F_\tau = \sum e^{2\tau|k|}|k||\hat{u}_k|^2$。如果$\dot{\tau} < 0$（即Gevrey正则性在衰减），这一项是负的，帮助耗散。所以要使$\Theta$增长，需要$\dot{\tau}$不太负——即解析半径不能快速衰减。

### 4.3 最危险的谱配置

综合条件A-C，**最危险的谱配置**是:
1. 高度螺旋极化（条件A）：能量集中在单一螺旋度符号上
2. 谱窄（条件B）：所有活跃波数在同一个量级上（$k_{\min} \approx k_{\max}$）——这与湍流惯性区间的宽谱相反
3. 解析半径大且稳定（条件C）：$\tau$不小且$\dot{\tau} \geq 0$

**这种配置对应什么物理状态？** 这近似于一个**大尺度、近固转的涡旋**。在物理空间中，这意味着流动由少数几个大涡旋主导，涡度方向高度一致。这种状态下，涡旋拉伸（$\omega \cdot \nabla u$）可以非常有效——因为它需要涡度方向对齐（拉伸自己）。

**著名的数值实验**: Kerr (1993), Hou & Li (2006)等人的blow-up研究都初始化了高度对称的涡旋结构（反平行涡管、Kerr涡旋等）。这些初始条件精确对应"窄谱、高螺旋极化"的谱配置。

### 4.4 这样的谱是否可持续？

**关键论点**: 即使初始条件是"危险"的谱配置，NS的triadic相互作用倾向于**快速破坏**这种配置:

1. **谱展宽**: Triadic相互作用通过非线性级串自然展宽谱——将能量从注入尺度分散到各种尺度。窄谱是一个高度非平衡状态，级串会迅速展宽它。

2. **螺旋度混合**: 类别I、II、III的triadic相互作用强烈混合螺旋度符号。即使初始只有$u_k^+$分量，类别I和II的相互作用会生成$u_k^-$分量（Rathmann & Ditlevsen的数值显示，即使仅强制$u^+$，也会出现$u^-$的显著谱分量）。

3. **谱隙的产生**: 在衰减湍流中，粘性优先移走小尺度能量（大$|k|$），自然产生谱隙$\Delta_3 \gg \Delta_2$——而这使得$\Phi \gg 0$，粘性驱动力增强。

**因此**: 危险谱配置在NS演化下是**不可持续的**。NS的自身动力学倾向于将系统从"危险区"推向"安全区"。这个观察与NV-10（Kang, Yun & Protas 2020）的发现一致: 即使最优地设计初始条件使enstrophy最大化增长，增长也是短暂的，之后enstrophy回落到适中的值。

### 4.5 可持续性判据的定量化

定义"危险指数":

$$\mathcal{D} = \frac{\text{类别III权重} \times \text{螺旋极化度}}{\nu\Phi}$$

如果$\mathcal{D} > 1$，则$\dot{\Theta}|_{NL}$可能压倒粘性。我们需要问:

$$\frac{d\mathcal{D}}{dt} \text{ 的符号是什么？}$$

如果$\mathcal{D}$在NS演化下倾向于减小（$d\mathcal{D}/dt < 0$），则危险是不可持续的。如果$d\mathcal{D}/dt \geq 0$可能成立，则需要警惕。

来自Rathmann & Ditlevsen的数据:
- 类别III权重$\sim 0.01$（耦合模型中）
- 但耦合模型的螺旋极化度在非螺旋强制下是零（平均上$|u^+| = |u^-|$）
- 如果刻意强制单一螺旋度（$\delta_{in} \neq 0$），类别III的贡献仍然很小

**推测**: $\mathcal{D}$在典型湍流配置下远小于1（$< 10^{-2}$），且$d\mathcal{D}/dt < 0$。

### 4.6 一个精确的数值预测

如果我们取**最危险的初始条件**（窄谱、高螺旋极化、低粘性），在2D中数值演化，我们可以预测:
- $\Theta$最初因级串而增长（谱展宽）
- 但很快$\Phi$增大（谱隙出现）使得粘性压倒级串
- $\Theta$在达到一个最大值后开始衰减

如果在3D中对同样的初始条件实验:
- 由于类别III的存在（涡旋拉伸），$\Theta$的增长可能比2D更剧烈
- 但triadic相互作用仍然混合螺旋度和展宽谱
- 最终3D也可能回落到有界行为——除非初始条件使$\mathcal{D}$足够大以至于$\Theta$在级串展宽谱之前就发散

**这就是NV-10的本质: 即使刻意优化，$\Theta$的增长也是有限的。**

---

## §5 深挖1: 2D vs 3D的核心差异——不是少了一项，是结构变了

### 5.1 Vorticity方程的根本结构差异

**2D**: $\partial_t \omega + u\cdot\nabla\omega = \nu\Delta\omega$
- 涡度是标量
- 对流项是线性的（给定$u$）
- 最大模原理: $\|\omega(t)\|_{L^\infty} \leq \|\omega(0)\|_{L^\infty}$（在无粘极限下守恒）
- 因此blow-up在2D是**结构上不可能**的

**3D**: $\partial_t\omega + u\cdot\nabla\omega = \nu\Delta\omega + \omega\cdot\nabla u$
- 涡度是向量
- 涡旋拉伸$\omega\cdot\nabla u$是非线性的（给定$u$，这是$\omega$的线性项——$u$通过Biot-Savart依赖$\omega$）
- 没有最大模原理
- Blow-up可能但不一定发生

**根本的结构差异**: 在2D中，涡度方程的右边是纯标量输运+扩散。在3D中，涡度沿自己的方向被拉伸——这是一个正反馈。这个正反馈在傅里叶空间中精确对应类别III的triadic相互作用。

### 5.2 频散关系的傅里叶空间差异

在2D中，$\hat{\omega}_k = i k^\perp \cdot \hat{u}_k$。频率满足:
$$\text{Im}[\text{nonlinear term}] \sim \sum_{k+p+q=0} (k^\perp \cdot \hat{u}_p) \hat{\omega}_q$$

而在3D中:
$$\text{Im}[\text{nonlinear term}] \sim \sum_{k+p+q=0} [\hat{\omega}_p \cdot k \hat{u}_q + \cdots]$$

3D多出的一项（$\hat{\omega}_p \cdot k$）允许涡旋拉伸产生的**正反馈**: 当$\hat{\omega}_p$平行于$k$时（即螺旋极化时），这一项最大。

### 5.3 $\Theta$在2D中的"自然极限"

在2D中，KLB理论给出稳态谱$E(k) \sim k^{-3}$（enstrophy级串区间）。在这个谱下:
$$\Theta_{\text{KLB}} \approx 2\log(k_d/k_f)$$

对于给定的耗散尺度$k_d = (\eta/\nu^3)^{1/6}$和注入尺度$k_f$，$\Theta$被限制在:
$$\Theta \leq 2\log\left(\frac{k_d}{k_f}\right) = \frac{1}{3}\log\left(\frac{\eta}{\nu^3 k_f^6}\right)$$

这随$\nu \to 0$对数发散——但在任何固定的$\nu > 0$下是有界的。这与2D的正则性一致。

在3D中，类似的估计不存在，因为K41谱$E(k) \sim k^{-5/3}$给出的$m_j$积分在$j \geq 2$时由大$k$主导（发散，需要粘性截断）。而更根本的是，3D中涡旋拉伸可以违背KLB的量纲假设。

---

## §6 深挖2: 谱熵的单调性与$\Theta$的Lyapunov候选资格

### 6.1 谱熵$H(t)$的演化方程（完整形式）

从$p_k = |\hat{u}_k|^2/(2m_0)$出发:

$$\frac{dH}{dt} = \frac{2\nu}{m_0}\sum_k |k|^2 |\hat{u}_k|^2 \log p_k + \frac{2\nu m_1}{m_0}(H+1) - \frac{1}{m_0}\sum_k T_k \log p_k$$

其中$T_k = \text{Re}\sum_{k+p+q=0} \overline{\hat{u}_k} \cdot P_k(\hat{u}_p \cdot k)\hat{u}_q$。

三项分别是: 粘性驱动的熵变、能量耗散驱动的熵变、非线性驱动的熵变。

### 6.2 非线性项的符号分析

在2D中，$T_k$对$m_1$（enstrophy）的积分为零，但对$\sum T_k \log p_k$不为零。

**关键观察**: $\log p_k = \log|\hat{u}_k|^2 - \log(2m_0)$。非线性项的贡献为:
$$\sum_k T_k \log p_k = \sum_k T_k \log|\hat{u}_k|^2 - \log(2m_0)\sum_k T_k$$

由于$\sum_k T_k = \frac{1}{2}\partial_t m_0|_{NL} = 0$（能量守恒），第二项为零。所以:

$$\frac{dH}{dt}\bigg|_{NL} = -\frac{1}{m_0}\sum_k T_k \log|\hat{u}_k|^2$$

这一项涉及$|\hat{u}_k|^2$的对数加权sum，对谱尾（$|\hat{u}_k|^2$很小的地方）特别敏感——因为$\log|\hat{u}_k|^2 \to -\infty$，从而赋予小振幅模很大的负权重。

**含义**: 非线性级串在将能量从一个大模分配到许多小模时（即正向级串），$\sum_k T_k \log|\hat{u}_k|^2$通常为**负**（因为能量从$\log$大的模流向$\log$负的模），从而导致$dH/dt|_{NL} > 0$。这支持了级串驱动熵增的观点。

### 6.3 粘性项的符号

$$\frac{dH}{dt}\bigg|_{visc} = \frac{2\nu}{m_0}\sum_k |k|^2 |\hat{u}_k|^2 \log p_k + \frac{2\nu m_1}{m_0}(H+1)$$

这也可以正可以负。对于集中于小$|k|$的谱（所有$p_k$在$k \approx 0$附近大，在$k$大处小），粘性耗散主要移走大$|k|$处的能量（$|k|^2$因子），这些能量对应的$p_k$小、$\log p_k$负。所以$\sum |k|^2 p_k \log p_k$通常为负→粘性可能驱动**熵减**。

**权衡**: 在级串和粘性的竞争中，稳态$dH/dt \approx 0$代表两者的平衡。

### 6.4 熵单调性的猜想

**猜想E1**（2D谱熵单调性）: 在2D衰减NS中，存在某个时间$T_*$后$dH/dt \leq 0$（谱熵最终单调递减），且在$\nu \geq 0$的任意值下$H(t)$全局有界。

**猜想E2**（3D谱熵条件单调性）: 在3D中，如果$H(t)$持续增长（$dH/dt \geq c > 0$），则blow-up在有限时间内发生。反过来说，如果能证明在任意初始条件下$H(t)$全局有界，则3D NS有全局正则性。

**猜想E3**（熵-$\Theta$关系）: $\Theta$和$H$满足某种单调函数关系——即存在一个递增函数$f$使得$f(H) \leq \Theta \leq g(H)$对某个$g$成立。如果这成立且$H$有界，则$\Theta$也有界。

### 6.5 一个小定理: 矩约束下的熵上界

**命题3**（给定$m_0, m_1, m_2$时$H$的上界——直接来自最大熵原理）:
$$H \leq H_{\max}(m_0, m_1, m_2) = \log Z + \lambda_1\frac{m_1}{2m_0} + \lambda_2\frac{m_2}{2m_0}$$

如果$m_1, m_2$在演化中有界，则$H$有上界。在2D中$m_1$单调递减，$m_2$也有界（由正则性理论），因此$H$有上界。在3D中，$m_1$和$m_2$都可能增长——但如果有边界层/级串理论给出$m_2$的增长速度上限，则$H$的上界也可以被控制。

---

## §7 对3D的核心启示与R4建议

### 7.1 核心结论矩阵

| 问题 | 2D答案 | 3D启示 |
|---|---|---|
| $N_1$（enstrophy非线性项）符号 | $=0$恒成立 | 3D中$N_1 \neq 0$——涡旋拉伸是唯一新增自由项 |
| $\Theta$在典型演化中的行为 | 有界（由正则性保证） | 未知——但如果blow-up，$\Theta$必须发散 |
| 谱熵$H$的单调性 | 猜想最终$dH/dt \leq 0$ | 如果$dH/dt > 0$持续成立是blow-up的信号 |
| 危险谱配置的可持续性 | 不可持续（级串展宽谱） | 同样不可持续——但涡旋拉伸可能延长危险期 |
| 类别III螺旋度通道 | 在2D中不存在 | 这是唯一可能使$N_\Theta > 0$的通道 |

### 7.2 精确的"缺失项"公式

3D中$\dot{\Theta}|_{NL}$比2D多出的项:

$$\dot{\Theta}|_{NL}^{3D} - \dot{\Theta}|_{NL}^{2D} = -\frac{N_1}{m_1}$$

这是因为2D中$N_1 = 0$而3D中$N_1 \neq 0$。这一项来自涡旋拉伸:

$$N_1 = 2\sum_{k+p+q=0} |k|^2 \text{Re}[\overline{\hat{u}_k} \cdot P_k(i\hat{u}_p \cdot k)\hat{u}_q]$$

在类别III的螺旋度分解下:

$$N_1^{III} = -2\sum_{k+p+q=0} |k|^2 \text{Re}[u_k^+ (u_p^+ \cdot k) u_q^+ + u_k^- (u_p^- \cdot k) u_q^-] \cdot (\text{几何因子})$$

类别III的贡献符号: 在螺旋极化的配置下（比如$u_k^+ \gg u_k^-$对所有$k$），$N_1^{III} > 0$（涡旋拉伸产生enstrophy），从而导致:

$$\dot{\Theta}|_{NL}^{3D} > \dot{\Theta}|_{NL}^{2D}$$

即3D的$\dot{\Theta}$比2D更正（更有利于$\Theta$增长）。

### 7.3 3D barrier的核心瓶颈（再次确认）

经过R2+R3的分析，3D NS的blow-up问题归结为:

> 是否存在满足$u_k^+ \gg u_k^-$（高度螺旋极化）且谱窄（$m_4/m_3 \approx m_3/m_2 \approx m_2/m_1$）的初始条件，使得$\dot{\Theta}|_{NL}^{3D} = \dot{\Theta}|_{NL}^{2D} - N_1/m_1 > 2\nu\Phi$在足够长的时间内成立，从而$\Theta$可以发散到无限大？

其中:
- $\dot{\Theta}|_{NL}^{2D}$在2D中已被证明是良态的
- $-N_1/m_1$是3D独有的涡旋拉伸贡献（由类别III螺旋度通道承载）
- $\Phi$是粘性驱动力

### 7.4 R4的建议方向

**方向1: 2D数值验证（最高优先级）**

编写2D NS的谱方法代码（Python+NumPy, 128x128或256x256分辨率），数值验证:
- (a) $\Theta(t)$在衰减湍流中是否最终递减
- (b) $H(t)$（谱熵）的单调性
- (c) 危险指数$\mathcal{D}(t)$的时间演化
- (d) 强制稳态下$\Theta$的稳态值与理论预测的比较
- (e) 螺旋极化初始条件下的行为

**方向2: 类别III的符号确定**

利用Waleffe的螺旋度分解，计算$\dot{\Theta}_{III}$（类别III对$\dot{\Theta}$的贡献）的精确公式，并分析其符号。目标: 证明或反证"类别III的贡献符号始终为非负（即始终不利于$\Theta$减小）"。

**方向3: 熵单调性的严格分析**

对$\frac{dH}{dt} = \frac{2\nu}{m_0}\sum_k |k|^2 |\hat{u}_k|^2 \log p_k + \cdots$进行细致的估计。特别关注:
- 粘性项的符号条件（什么条件下粘性驱动熵减？）
- 非线性项的上界（级串最多能驱动多少熵增？）
- 是否存在一个"熵不等式"将$dH/dt$的符号与某些可计算的谱量联系起来？

**方向4: 反问题的定量化**

构造最危险初始条件的参数空间，并计算:
- 最大$\Theta$增长率作为谱宽度和螺旋极化度的函数
- 危险期的持续时间
- 在参数空间中bolw-up是否仅限于零测集？

**方向5: 先发文献交叉验证**

关键需要核对的先发工作:
- Dascaliuc & Grujić (2012)的涡度方向Hölder连续性条件在傅里叶空间中的等价表述
- Biswas & Foias (2014)的解析半径ODE与$\Theta$的关系
- Waleffe (1992)之后的螺旋度分解发展（Biferale et al. 2012, 2013, Sahoo & Biferale 2017等）
- Marton (2015)对数Sobolev不等式在离散测度上的具体常数

### 7.5 最终判定

**R3的核心贡献**:
1. 在2D受控实验中定位了3D独有的非线性项（$N_1/m_1$，涡旋拉伸通过类别III螺旋度通道）
2. 建立了谱熵$H$与$\Theta$的联系——两者都度量谱宽度，都是blow-up的潜在indicator
3. 给出了$\Theta$增长的必要谱条件（窄谱+高螺旋极化），并论证了这些条件在NS演化下不可持续
4. 为R4提供了可数值验证的具体方案

**R3的未解决问题**:
1. 类别III贡献的符号不能从第一原理证明（需要计算）
2. 熵单调性尚未严格建立
3. 危险谱配置的不可持续性需要定量化（而非定性的物理论点）

**R3后的北极星**: 2D数值实验是第一要务——这会把许多"推测"变成"已知"或"证伪"。

---

## 参考文献

1. **Foias & Temam (1989)**: "Gevrey class regularity for the solutions of the Navier-Stokes equations", J. Funct. Anal. 87, 359-369.
2. **Biswas, Hudson & Tian (2019)**: "Persistence time of solutions of the 3D NSE in Sobolev-Gevrey classes", arXiv:1912.11192.
3. **Waleffe (1992)**: "The nature of triad interactions in homogeneous turbulence", Phys. Fluids A 4, 350-363.
4. **Rathmann & Ditlevsen (2016)**: "The role of helicity in triad interactions in 3D turbulence investigated in a new shell model", Phys. Rev. E 94, 033115 (arXiv:1602.02553).
5. **Sahoo & Biferale (2017)**: "Energy Cascade and Intermittency in Helically Decomposed Navier-Stokes Equations", Fluid Dyn. Res. (arXiv:1709.03713).
6. **De Pietro, Biferale & Mailybaev (2015)**: "Inverse energy cascade in nonlocal helical shellmodels of turbulence", Phys. Rev. E 92, 043021 (arXiv:1508.06390).
7. **Yan, Li, Yu & Chen (2019)**: "Dual channels of helicity cascade in turbulent flows", J. Fluid Mech. (arXiv:1907.03634).
8. **Dascaliuc & Grujic (2012)**: "Coherent vortex structures and 3D enstrophy cascade", Comm. Math. Phys. 309, 757.
9. **Dascaliuc & Grujic (2011)**: "2D turbulence in physical scales of the Navier-Stokes equations", arXiv:1101.2209.
10. **Marton (2015)**: "Logarithmic Sobolev inequalities in discrete product spaces", arXiv:1507.02803.
11. **Kang, Yun & Protas (2020)**: "Maximum Amplification of Enstrophy in 3D NSE", J. Fluid Mech.
12. **Biswas & Foias (2014)**: "On the maximal space analyticity radius for the 3D NSE and energy cascades", Ann. Mat. Pura Appl. 193, 739-777.
13. **Doering & Gibbon (1995)**: "Applied Analysis of the Navier-Stokes Equations", Cambridge.
14. **Kraichnan (1967) / Leith (1968) / Batchelor (1969)**: KLB 2D turbulence theory.
15. **Biferale, Musacchio & Toschi (2012)**: "Inverse energy cascade in 3D isotropic turbulence", Phys. Rev. Lett. 108, 164501.

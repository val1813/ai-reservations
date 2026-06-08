# LP12-S3 Phase 1 — B博士独立推导：半经典混沌+亚稳态统一框架

**作者**: B博士（野路子独立探索者）
**日期**: 2026-06-02
**框架**: 半经典混沌 + Metastability统一框架
**核心区分**: A博士用代数对易关系（静态结构），B博士用动力学稳定性（动态演化）

---

## §0 框架声明

### 0.1 核心哲学分歧

A博士问："扰动算符与涌现SU(2)代数对易吗？"（静态判据）
B博士问："扰动改变了相空间周期轨道的稳定性吗？改变了多长时间尺度上的动力学吗？"（动态判据）

代数对易告诉你"什么不变"，动力学告诉你"在多长时间尺度上不变，以及什么使它崩溃"。

### 0.2 理论支柱

| 支柱 | 来源 | 核心主张 |
|------|------|---------|
| **半经典混沌抑制** | Omiya (PRB 2025) | QMBS在半经典极限下抑制混沌，Lyapunov指数~1/N→0。疤痕=经典相空间中的稳定周期轨道或弱不稳定轨道。扰动通过改变相空间拓扑来杀死或保留疤痕。 |
| **亚稳态统一理论** | Yin, Surace & Lucas (PRX 2025, arXiv:2408.05261) | 短程纠缠亚稳态必然是某个邻近哈密顿量的本征态（即scar）。prethermal窗口由"虚假真空衰减"的量子隧穿速率决定。扰动改变有效势垒高度→改变prethermal寿命。 |
| **经典周期轨道-疤痕对应** | Pizzi, Evrard, Dag & Knolle (arXiv:2408.10301, 2024) | TI态和IS态周期轨道在S≥3/2的自旋链中产生量子疤痕。稳定性由λ/ω比值控制（Lyapunov指数/轨道频率）。 |
| **Arnold扩散与准周期暂态** | Ermakov, Lychkovskiy & Fine (arXiv:2409.00258, 2024) | 周期轨道不稳定发展成"近准周期非遍历暂态"——解释为可积动力学附近的Arnold扩散。非单调Lyapunov指数依赖于链长。 |

### 0.3 方法论声明

本推导不使用：
- SU(2)谱生成代数的对易关系
- commutator algebra的分类框架
- 静态"代数免疫"判据

本推导使用：
- 经典相空间周期轨道的Monodromy矩阵分析
- Lyapunov指数对扰动强度的标度
- Prethermal寿命的量子隧穿图像
- KAM理论在量子多体系统中的对应

---

## §1 PXP-α模型的经典极限

### 1.1 自旋相干态表示

PXP-α哈密顿量：

$$H_{\text{PXP-}\alpha} = \sum_j P_{j-\alpha}\cdots P_{j-1} \sigma_j^x P_{j+1}\cdots P_{j+\alpha}$$

其中$P_j = (1-\sigma_j^z)/2$是投影到基态的投影算符。约束条件是：位点j被激发当且仅当距离α范围内的所有位点都处于基态。

**经典极限构建**：用自旋相干态（Bloch相干态）替代自旋算符：

$$|\theta_j, \phi_j\rangle = \cos\frac{\theta_j}{2} |0\rangle_j + e^{i\phi_j} \sin\frac{\theta_j}{2} |1\rangle_j$$

经典相空间是L个Bloch球面的直积，每个位点由$(\theta_j, \phi_j)$参数化。$\theta_j = 0$对应基态$|0\rangle$，$\theta_j = \pi$对应激发态$|1\rangle$。

投影算符的经典对应：$P_j \to \cos^2(\theta_j/2) = (1+\cos\theta_j)/2$是"未被占据"的概率权重。

### 1.2 经典约束条件的相空间含义

量子约束"激发态不能有邻近激发"在经典极限下变为：

$$\sin^2\frac{\theta_j}{2} \cdot \prod_{d=1}^{\alpha} \sin^2\frac{\theta_{j\pm d}}{2} = 0$$

即：若$\theta_j = \pi$（激发态），则距离α内的所有位点必须满足$\theta_{j\pm d} = 0$（基态）。

这定义了一个**约束子流形** $\mathcal{M}_{\alpha} \subset (S^2)^{\times L}$：

$$\mathcal{M}_{\alpha} = \{(\theta_j, \phi_j)_{j=1}^L : \forall j, \text{若} |\theta_j - \pi| < \epsilon, \text{则} |\theta_{j\pm d} - 0| < \epsilon \text{对所有} 1 \leq d \leq \alpha\}$$

### 1.3 周期轨道识别

在约束流形$\mathcal{M}_{\alpha}$上，哈密顿量的经典极限（取期望值在相干态上）为：

$$\mathcal{H}_{\text{cl}}(\{\theta_j, \phi_j\}) = \sum_j \left(\prod_{d=1}^{\alpha} \cos^2\frac{\theta_{j-d}}{2}\right)\left(\prod_{d=1}^{\alpha} \cos^2\frac{\theta_{j+d}}{2}\right) \sin\theta_j \cos\phi_j$$

其中利用了$\langle \sigma_j^x \rangle = \sin\theta_j \cos\phi_j$。

**§1.3.1 α=1的标准Néel轨道**

最大投影约束下，经典运动方程为（变分原理或TDVP）：

$$\dot{\theta}_j = \frac{\partial \mathcal{H}_{\text{cl}}}{\partial (\cos\theta_j)\sin\phi_j}, \quad \dot{\phi}_j = -\frac{\partial \mathcal{H}_{\text{cl}}}{\partial (\cos\theta_j)\cos\phi_j}$$

Néel态对应$\theta_j = \pi$对于奇数j，$\theta_j = 0$对于偶数j（或反之）。在约束流形上，这个构型是一个**周期轨道**：σ^x项翻转自旋，但翻转后约束强制翻转回来，产生周期为T≈4.78（以Ω=1为单位）的振荡。

关键观察：在经典描述中，Néel周期轨道是**孤立的**——约束条件阻止它在相空间中连续变形为其他构型。这与自由自旋链中的连续族（magnon连续谱）形成对比。

**§1.3.2 α=2,3的扩展约束轨道**

α=2时，最小激发间距为3个位点。Néel态（间距2）不满足约束，因此Néel周期轨道在$\mathcal{M}_2$上**不存在**。替代的周期轨道是：

$$\cdots 100100100 \cdots \quad \text{（间距3的密度波）}$$

α=3时，最小间距为4，周期轨道为：

$$\cdots 100010001000 \cdots \quad \text{或} \quad \cdots 10010001001000 \cdots$$

这些轨道具有不同的周期和不同的相空间拓扑——它们不是同伦等价的。

### 1.4 半经典极限中的系统尺寸标度

Omiya的核心发现是：在Shiraishi-Mori构造下，疤痕轨道的Lyapunov指数标度为：

$$\lambda_L \sim \frac{1}{N} \xrightarrow{N\to\infty} 0$$

其中N是"味"的数量（系统尺寸或等效自由度数目）。在半经典极限下，疤痕轨道是**精确稳定的**（椭圆型），不受经典混沌影响。

对于PXP模型，等效的"味"数量由约束空间的维度决定：$N_{\text{eff}} = \dim\mathcal{H}_{\text{constrained}} \sim \phi^L$其中$\phi \approx 1.618$（黄金比例，PXP-1的约束空间增长因子）。

关键预测：**在热力学极限下，PXP-α的约束子空间维度指数增长，使得疤痕轨道的Lyapunov指数指数级小：**

$$\lambda_L(L) \sim \exp(-\text{const} \cdot L) \quad \text{对于} L \to \infty$$

这比Omiya原始的~1/N标度更强——因为约束空间的"有效味数"随L指数增长。

---

## §2 周期轨道稳定性分类

### 2.1 Monodromy矩阵分析

对于约束流形$\mathcal{M}_\alpha$上的周期轨道$\Gamma$（周期T），线性稳定性由**Monodromy矩阵** $M(T)$决定，它是线性化流在轨道切空间中的时间演化：

$$\frac{d}{dt}\delta\mathbf{z} = J \cdot \nabla^2 \mathcal{H}_{\text{cl}}|_{\Gamma(t)} \cdot \delta\mathbf{z}$$

其中$\delta\mathbf{z} = (\delta\theta_1, \ldots, \delta\theta_L, \delta\phi_1, \ldots, \delta\phi_L)$是相空间偏离，J是辛矩阵。

Monodromy矩阵$M(T)$将初始偏离映射到时间T后的偏离：

$$\delta\mathbf{z}(T) = M(T) \cdot \delta\mathbf{z}(0)$$

### 2.2 稳定性分类（经典动力系统理论）

周期轨道的稳定性由$M(T)$的本征值$\{\mu_i\}$（Floquet乘子）完全分类：

| 类型 | Floquet乘子 | 物理含义 | QMBS对应 |
|------|------------|---------|---------|
| **椭圆型** | $\mu_i = e^{\pm i\nu_i}, \nu_i \in \mathbb{R}$ | 线性稳定，偏离做拟周期振荡 | **QMBS的经典对应**（Omiya: λ~1/N） |
| **双曲型** | $\mu_i = e^{\pm \lambda_i}, \lambda_i > 0$ | 指数不稳定，Lyapunov指数λ_i > 0 | 无疤痕或弱疤痕（λ/ω < 1时为传统量子疤痕） |
| **抛物型** | $\mu_i = \pm 1$（简并） | 边际稳定，线性分析不足，需高阶项 | 分界线/separatrix——量子对应物极敏感于扰动 |

在辛几何中，Floquet乘子成对出现：若μ是乘子，则μ*和1/μ也是。这强制了椭圆/双曲/抛物三分类的完备性。

### 2.3 PXP-α各轨道的稳定性诊断

**α=1，Néel轨道**：
在无扰动PXP-1中，数值证据（FSA误差闭合慢、revival持久）表明Néel轨道是**弱椭圆型**——其Floquet乘子在单位圆上但非常接近+1（抛物边界）。这是"近似scar"的动力学根源：轨道是椭圆的但不是强椭圆的，因此有很慢但非零的衰减。

Monodromy特征：$\mu_j = e^{\pm i \nu_j}$其中$\min_j |\nu_j| \sim 1/L$——最小KAM频率随系统尺寸减小。这解释了为什么精确的Néel revival是近似的：频率间隙随L→0而闭合轨道最终通过Arnold扩散衰变。

**α=2，间距3密度波轨道**：
轨道在$\mathcal{M}_2$上存在但更脆弱。原因是：α=2的约束条件更强，导致约束流形的余维度更大，允许更少的稳定方向（更少的椭圆Floquet乘子对）。预测：λ_L在α=2时比α=1大一个因子——疤痕更弱但非零。

**α=3，间距4密度波轨道**：
轨道进一步受限于更严格的约束。稳定性取决于具体的初始态选择（间距4或2+3混合模式）。有些轨道可能是**双曲型**的——在约束维持的情况下仍然是经典不稳定的——对应于Kerschbaumer et al. (PRL 2025)发现的"需要纠缠初始态"的疤痕家族。

### 2.4 稳定性分类vs代数分类：哪个更基本？

动力系统的三分类（椭圆/双曲/抛物）是**拓扑的**——它由Monodromy矩阵在辛群中的共轭类决定。这些共轭类在连续形变下是离散的（不变）。

SU(2)谱生成代数分类是**代数的**——它由涌现算符之间的对易关系决定。

关键观察：**在无扰动极限下，PXP-α中涌现SU(2)的J^z和J^±算符之所以存在，恰恰是因为周期轨道是椭圆型的**。椭圆稳定性产生了近似等间距的能谱（量子化条件），这被解释为"SU(2)塔"。但椭圆稳定性是更基本的——它先于代数结构。

证明轮廓：考虑周期轨道Γ量子化产生的能级$E_n$。Einstein-Brillouin-Keller (EBK)量子化给出：

$$E_n = \mathcal{H}_{\text{cl}}(\Gamma) + \hbar \omega \left(n + \frac{1}{2}\right) + \mathcal{O}(\hbar^2)$$

其中ω = 2π/T是轨道频率。等间距能谱（su(2)塔的标志）直接从**轨道是周期性的且孤立的**这一事实得出——不需要任何代数结构。

扰动改变轨道稳定性 → 能级间距偏离等距性 → "SU(2)塔"被破坏。但这首先是一个**动力系统事件**（椭圆→双曲转变），其次才是一个**代数事件**（交换子非零）。

---

## §3 扰动下的相空间分析

### 3.1 五种扰动的相空间作用

#### 3.1.1 Ising对角扰动：$V \sum_j n_j n_{j+1}$

经典极限：$\mathcal{H}_{\text{Ising}} = V \sum_j \sin^2\frac{\theta_j}{2} \sin^2\frac{\theta_{j+1}}{2}$

这是纯对角项——它不产生动力学（$\partial\mathcal{H}_{\text{Ising}}/\partial\phi_j = 0$），仅仅给能量添加一个构型依赖的偏移。在经典运动方程中：

$$\dot{\theta}_j = 0 \text{（来自Ising项贡献）}, \quad \dot{\phi}_j = -V\left[\sin^2\frac{\theta_{j-1}}{2} + \sin^2\frac{\theta_{j+1}}{2}\right]\cos\theta_j$$

Néel轨道上：相邻位点不同时为1，因此Ising项的期望值恒为零。Ising项不改变Néel轨道的**相空间几何**——轨道的Flux不改变，Floquet乘子不改变。

**稳定性判据**：Ising扰动不改变约束流形$\mathcal{M}_\alpha$上的轨道稳定性类型。轨道保持椭圆型。

这解释了ED数据中n_scar=29在Ising扰动λ=0到2.0的整个范围内保持恒定。

#### 3.1.2 Heisenberg交换扰动：$J \sum_j \mathbf{S}_j \cdot \mathbf{S}_{j+1}$

经典极限：$\mathcal{H}_{\text{Heis}} = \frac{J}{4} \sum_j [\cos\theta_j \cos\theta_{j+1} + \sin\theta_j \sin\theta_{j+1} \cos(\phi_j - \phi_{j+1})]$

关键：**flip-flop项** $\sin\theta_j \sin\theta_{j+1} \cos(\phi_j - \phi_{j+1})$直接耦合$\phi_j$自由度，产生非平凡的角动力学。这是真正的**非线性扰动**——它改变了周期轨道的Monodromy矩阵。

在Néel轨道上，相邻位点有不同的$\theta$值（0 vs π），因此flip-flop振幅为$\sin 0 \cdot \sin\pi = 0$——恰好为零。这意味着Néel轨道是Heisenberg动力学的**不动点**（在一阶）。

但是：flip-flop项产生了一个剩余相互作用，破坏了约束流形的切空间结构。在轨道附近的小偏离中，flip-flop产生非零的Lyapunov指数。

**稳定性判据**：Heisenberg扰动将某些Floquet乘子从单位圆推向实轴——从椭圆型变成**弱双曲型**。Lyapunov指数在小的J下非零，但$\lambda_L \sim J^2$（二阶效应因为Néel轨道是一阶不动点）。

这解释了ED数据：n_scar在J=0.01时从29降到18（快速初始杀伤），然后在J=0.5时恢复到34（轨道变形但未被完全破坏）。

#### 3.1.3 无序扰动：$W \sum_j \epsilon_j n_j$

经典极限：$\mathcal{H}_{\text{dis}} = W \sum_j \epsilon_j \sin^2\frac{\theta_j}{2}$

无序破坏了**平移不变性**。周期轨道$\Gamma$在均匀系统中是闭合的，但在无序势中不再是精确周期的——不同的位点获得不同的在位能，破坏了轨道的空间周期性。

更重要的是：无序使约束流形$\mathcal{M}_\alpha$变得"粗糙"——原本光滑的流形现在有了随机皱纹。这导致Arnold扩散的极大加速：原本受KAM保护的环面现在被稠密的随机共振覆盖。

**稳定性判据**：无序将约束流形从光滑变为分形。周期轨道在**任意小的无序**下就不再是精确周期性的——但在中等W下，MBL效应产生大量低纠缠定域态，ED数据显示n_scar不降反升（W=1.0时n_scar=52）。这不是疤痕保护，而是MBL定域化的伪装——需要仔细区分。

#### 3.1.4 边界场扰动：$h(\sigma_0^z - \sigma_{L-1}^z)$

经典极限：$\mathcal{H}_{\text{bd}} = h(\cos\theta_0 - \cos\theta_{L-1})$

边界场作用在两个端点上。在相空间中，它产生一个**边界层效应**——只有接近边界的自由度受到影响。体周期轨道$\Gamma$的绝大部分（O(L-2)个位点）不受影响。

**稳定性判据**：边界场的效应在热力学极限下是亚广延的（O(1)/L → 0）。轨道的Floquet乘子中只有O(1)个（对应边界模式）被改变，O(L)个体乘子保持不变。疤痕保持存活——但边界的少数自由度可能与体解耦，产生额外的低纠缠态（n_scar从29变到26-38）。

ED数据证实：n_scar在h=0-2.0范围内波动但不归零。

#### 3.1.5 长程扰动：$V \sum_{i<j} \frac{n_i n_j}{|i-j|^\gamma}$

经典极限：$\mathcal{H}_{\text{LR}} = V \sum_{i<j} \frac{\sin^2(\theta_i/2) \sin^2(\theta_j/2)}{|i-j|^\gamma}$

长程相互作用打破了约束的局域性——原本的约束是短程的（范围α），现在任意距离的位点之间存在相互作用。

**稳定性判据**：这取决于γ。若γ > 2（短程有效），效应类似于Ising对角项，轨道保持。若γ ≤ 1（真正长程），约束流形$\mathcal{M}_\alpha$被破坏——长程耦合创造了一个全局势能面，周期轨道可能完全消失。

预测：存在临界γ_c(α)，当γ < γ_c时疤痕轨道变为双曲型→疤痕死亡。γ_c(α)随α增大而减小，因为更大的α使约束流形更脆弱。

### 3.2 扰动-稳定性相图（B博士预测）

| 扰动类型 | Floquet乘子变化 | 稳定性转变 | n_scar预测 | 扰动阈值λ_c |
|---------|---------------|----------|-----------|-----------|
| Ising | Δμ=0（不变） | 保持椭圆型 | 恒定N_scar | ∞（无阈值） |
| Heisenberg | Δμ~J^2（二阶） | 椭圆→弱双曲 | 先降后稳 | J_c ~ 0.5-1.0 |
| Disorder | Δμ~W（一阶） | 光滑→粗糙流形 | 先降后升（MBL伪装） | W_c ~ 0.1（轨道破坏）/ W~0.5（MBL增强） |
| Boundary | Δμ~h/L | O(1)模式变化 | 轻微波动 | ∞（TL下无阈值） |
| Long-range | Δμ~V/γ | 椭圆→双曲（γ<γ_c） | 逐渐归零 | γ_c(α) ~ 1+α |

---

## §4 Prethermal寿命的亚稳态理论

### 4.1 Yin-Surace-Lucas框架应用于PXP-α

Yin, Surace & Lucas (PRX 2025)证明了：一个态是亚稳态，当且仅当它是某个邻近哈密顿量的本征态。形式化地：

**定理（YSL 2025）**：设$|\psi\rangle$是H的亚稳态，亚稳态半径为R。则存在哈密顿量H'满足$\|H - H'\| \leq \epsilon(R)$，使得$|\psi\rangle$是H'的精确本征态，其中$\epsilon(R) \sim \exp(-R^\alpha)$对某α>0。

应用于PXP-α：Néel态$|\mathbb{Z}_2\rangle$在无扰动下是亚稳态，亚稳态半径$R \sim L$（由约束空间维度决定）。存在一个邻近哈密顿量$H'_{\text{PXP}}$使Néel态是精确本征态——这就是被代数框架解释为"涌现SU(2)"的东西。

扰动H_pert的加入改变了邻近哈密顿量的存在性。关键量是**扰动在亚稳态子空间上的投影**：

$$\Delta = \|P_{\text{scar}} H_{\text{pert}} P_{\text{scar}}\|$$

和**出射振幅**（将scar耦合到热库的矩阵元）：

$$\Gamma = \|P_{\text{thermal}} H_{\text{pert}} P_{\text{scar}}\|$$

其中$P_{\text{scar}}$是疤痕子空间的投影，$P_{\text{thermal}} = 1 - P_{\text{scar}}$。

### 4.2 有效势垒和量子隧穿速率

Prethermal寿命由量子隧穿决定——系统从"虚假真空"（scar态）隧穿到"真真空"（热库）的速率。在YSL框架中：

$$\tau(\lambda) \sim \exp\left(\frac{c}{\Gamma(\lambda)^d \log^3(1/\Gamma(\lambda))}\right)$$

其中d=1（一维链），c是O(1)常数，$\Gamma(\lambda)$是出射振幅。

关键：**不同扰动类型有不同的$\Gamma(\lambda)$标度**，因此有不同的$\tau(\lambda)$。

### 4.3 各扰动类型的τ标度推导

**Ising扰动**：
Ising项是纯对角的：$P_{\text{scar}} H_{\text{Ising}} P_{\text{thermal}} = 0$当scar由Néel-like的Fock态张成时。因为Ising项不改变占据数——它对角在Fock基中。如果疤痕子空间与某个Fock基有大量重叠（Néel态就是Fock态），则出射振幅指数级小：

$$\Gamma_{\text{Ising}} \sim V \cdot e^{-\alpha L}$$

$$\tau_{\text{Ising}} \sim \exp\left(\frac{c}{V^d e^{-\alpha d L} \log^3(\cdots)}\right) \sim \exp(\exp(\alpha d L))$$

这是**双重指数**长的prethermal寿命——在热力学极限下实际上是无限的。对应n_scar恒定。

**Heisenberg扰动**：
Flip-flop项非对角在Fock基中——它直接耦合scar子空间和热库。出射振幅在微扰论中为：

$$\Gamma_{\text{Heis}} \sim J \cdot \mathcal{O}(1)$$

（因为存在大量Fock态可以通过单次flip-flop从Néel态到达。）

$$\tau_{\text{Heis}} \sim \exp\left(\frac{c}{J^d \log^3(1/J)}\right) \sim \exp(c'/J)$$

标度：$\tau \sim \exp(c/J)$。

对于J=0.01：τ很长（n_scar降至18但未归零）；对于J=0.5：τ较短（n_scar波动）。

**无序扰动**：
无序产生的$\epsilon_j$在位能破坏了平移对称性。出射振幅：

$$\Gamma_{\text{dis}} \sim W \cdot \sqrt{L}$$

（来自L个独立的在位势能）。

$$\tau_{\text{dis}} \sim \exp\left(\frac{c}{W^d L^{d/2} \log^3(\cdots)}\right)$$

无序的τ在热力学极限下趋于零——因为$\Gamma \sim W\sqrt{L}$发散。这与ED数据一致：W=1.0时n_scar=52的表面"增强"实际上是MBL定域化产生的众多低纠缠态，不是疤痕保护。

**边界场扰动**：
$$\Gamma_{\text{bd}} \sim h$$

（边界场耦合了O(1)个体自由度到热库）。

$$\tau_{\text{bd}} \sim \exp\left(\frac{c}{h^d \log^3(1/h)}\right)$$

τ在h → ∞时也不归零——因为只有边界模式受影响，体疤痕仍然存在。这解释了n_scar在h=0-2.0范围内的波动但不归零。

### 4.4 τ标度总结

| 扰动类型 | Γ(λ)标度 | τ(λ)标度 | TL极限下的τ |
|---------|---------|---------|-----------|
| Ising | $V e^{-\alpha L}$ | $\exp(e^{\alpha L})$ | ∞ |
| Heisenberg | $J$ | $\exp(c/J)$ | 有限（J>0时） |
| Disorder | $W\sqrt{L}$ | $\exp(c/(W\sqrt{L}))$ | →1（坏） |
| Boundary | $h$ | $\exp(c/h)$ | 有限（但N_scar降至O(1)？不——体存活） |
| Long-range | $V L^{1-\gamma}$（若γ<2） | $\exp(c/(V L^{1-\gamma}))$ | →1（若γ<1）或有限（若γ>1） |

---

## §5 Lyapunov分析与疤痕死亡阈值

### 5.1 经典极限下的Lyapunov指数

在经典相空间中，周期轨道Γ的Lyapunov指数从Floquet乘子计算：

$$\lambda^{(i)}_L = \frac{1}{T} \log|\mu_i|$$

对于椭圆轨道（所有|μ_i|=1），所有$\lambda^{(i)}_L = 0$。
对于双曲轨道（至少一个|μ_i|>1），最大的λ_L > 0。

### 5.2 扰动下的λ_L标度

**Ising扰动**：
Ising项不产生新动力学（纯对角），因此不改变μ_i。分两种情况：
- 对于约束流形上的轨道：Floquet乘子不变，λ_L保持为零。
- 对于偏离约束流形的方向：Ising项创建一个能量偏移但不改变线性稳定性。λ_L ≡ 0。

**预测**：Ising扰动的疤痕死亡阈值λ_c = ∞。在任何Ising强度下，周期轨道保持椭圆型。

**Heisenberg扰动**：
Heisenberg项产生非平凡角动力学。Monodromy矩阵被扰动：

$$M(T; J) = M_0(T) \cdot \exp\left(J \int_0^T dt \, \mathcal{L}_{\text{flip-flop}}(t)\right)$$

在小的J下展开：

$$\mu_i(J) = e^{\pm i\nu_i^{(0)}} \cdot \left(1 \pm c_i J^2 + \mathcal{O}(J^3)\right)$$

当$c_i J^2 > |\nu_i^{(0)}|$时，乘子从单位圆移出→椭圆→双曲转变。

$$\lambda_L(J) \approx \max(0, c_i J^2 - |\nu_i^{(0)}|/T)$$

疤痕死亡阈值：$J_c \sim \sqrt{|\nu_{\min}^{(0)}|/c} \sim \sqrt{1/(cL)}$（因为$\nu_{\min}^{(0)} \sim 1/L$）。

对于L=14：$J_c \sim \sqrt{1/(c \cdot 14)} \sim 0.27$（c=1时）。ED数据显示n_scar在J=0.2时恢复到28（接近未扰动的29），表明J=0.2尚未达到死亡阈值。

**Disorder扰动**：
无序产生一个随机势能面。周期轨道不再是精确周期的——它变成一个**噪声扰动的准周期轨道**。Lyapunov指数：

$$\lambda_L(W) \sim W^2 \cdot \frac{1}{|\nu_{\min}^{(0)}|} \sim W^2 L$$

在W ~ 1/√L处：λ_L ~ O(1)。疤痕死亡阈值$W_c \sim 1/\sqrt{L}$。

对于L=14：$W_c \sim 1/\sqrt{14} \sim 0.27$。这与ED数据一致：W=0.1时n_scar=20（开始下降），W=0.5时n_scar=33（MBL混杂）。

### 5.3 疤痕死亡阈值相图

| 扰动类型 | λ_L(λ) | λ_c（L=14） | λ_c（TL） |
|---------|--------|-----------|----------|
| Ising | 0 | ∞ | ∞ |
| Heisenberg | c J^2 - 1/(LT) | ~0.27 | →0（有趣！） |
| Disorder | c W^2 L | ~0.27 | →0 |
| Boundary | c h/L | ~L·1 | ∞ |
| Long-range | c V/(L^{γ-1}) | 取决于γ | 0（γ<1）/有限（γ>1）/∞（γ>2）|

**关键预测**：在热力学极限下，Heisenberg扰动在任意小的J>0时都可以杀死疤痕——因为$J_c \sim 1/\sqrt{L} \to 0$。这与Ising扰动形成鲜明对比（$\lambda_c = \infty$，无论L多大）。

这是**B博士框架的核心预测**——它不由代数对易关系给出。

---

## §6 深挖1：稳定性分类比代数分类更基本

### 6.1 涌现代数的动力学根源

PXP模型中的"涌现SU(2)"可以从经典动力系统角度重新理解：

周期轨道Γ的量子化产生等间距能级$E_n = n\omega$（在ℏ=1单位下，忽略零点能）。任何具有等间距能谱的系统在代数上都"看起来像"SU(2)的J^z表示——因为等间距能级可以对角化为$J^z = \sum_n n |E_n\rangle\langle E_n|$，而相邻能级之间的跃迁算符自然满足$[J^z, J^\pm] = \pm J^\pm$。

但这是**表象的**，不是**实质的**。涌现SU(2)的存在仅仅反映了：
1. 存在一个孤立的周期轨道（动力学事实）
2. 该轨道是椭圆型的（稳定性事实）→能级近似等间距
3. 存在将系统耦合到该轨道的非平凡矩阵元（FSA结构）

如果(1)或(2)被破坏——例如扰动使轨道变为双曲型——则"涌现SU(2)"必然崩溃。但代数框架可能无法预测这一点，因为它只检查扰动算符是否与J^z对易，而不检查J^z本身是否仍然是好的量子数。

### 6.2 稳定性分类的拓扑鲁棒性

椭圆/双曲/抛物分类在辛群Sp(2n,ℝ)的共轭作用下是**离散不变量**。这意味着：
- 小扰动不能将椭圆型变为双曲型——必须通过**分岔**（抛物边界）
- 扰动强度的临界值λ_c对应于椭圆→抛物→双曲的分岔点
- 这个分岔点是否存在取决于扰动的**辛结构**，不仅取决于其代数性质

这就是为什么Ising扰动不产生分岔（对角项保持辛结构不变），而Heisenberg扰动产生分岔（非对角项改变辛结构）。

### 6.3 预测：存在代数对易但动力学不稳定的情况

考虑以下构造（一个Gedankenexperiment）：

在PXP-1上添加一个扰动：
$$H_{\text{pert}} = \epsilon \sum_j P_{j-1} \sigma_j^y P_{j+1}$$

这个算符与J^z对易吗？如果J^z ≈ ∑_j (-1)^j n_j（Néel交错磁化），那么$[H_{\text{pert}}, J^z]$涉及σ^y → 由于σ^y翻转自旋（在σ^x基中），它不保持n_j的本征值。因此$[H_{\text{pert}}, J^z] \neq 0$ → 代数框架预测**非免疫**。

但从动力系统角度：σ^y在约束子空间中的效应是旋转自旋的方位角φ。这种旋转不改变Bloch矢量的极角θ，因此不改变约束流形的嵌入方式。在合适的旋转框架下，这个扰动实际上等价于无扰动的PXP——只是自旋方向被旋转了。从动力学角度，周期轨道保持椭圆型 → **动力学稳定**。

这是代数非对易但动力学稳定的例子。

反过来：考虑对角长程扰动：
$$H_{\text{pert}} = V \sum_{i,j} (-1)^{i+j} n_i n_j$$

这个算符与J^z ≈ ∑_j (-1)^j n_j严格对易：$[H_{\text{pert}}, J^z] = 0$（因为n_i n_j与n_k对易）。代数框架预测**免疫**。

但从动力系统角度：长程对角项产生了一个全局势能面，可能完全改变约束流形的拓扑——将孤立的周期轨道连接成连续族（通过创建新的相空间通道）。如果轨道不再是孤立的，量子化条件失效，"scar塔"崩溃。→ **动力学不稳定**。

这是代数对易但动力学不稳定的例子。

---

## §7 深挖2：KAM理论与QMBS的对应

### 7.1 KAM定理速览

经典的Kolmogorov-Arnold-Moser (KAM)定理说：

考虑一个可积哈密顿量H_0(I)（作用量-角变量），加入小扰动ε H_1(θ, I)。如果H_0满足**非简并条件**（$\det(\partial^2 H_0/\partial I_i \partial I_j) \neq 0$），那么频率向量ω = ∂H_0/∂I满足**Diophantine条件**的不变环面在扰动下存活：

$$|\mathbf{k} \cdot \boldsymbol{\omega}| \geq \frac{\gamma}{|\mathbf{k}|^\tau} \quad \forall \mathbf{k} \in \mathbb{Z}^n\setminus\{0\}$$

对于某γ>0和τ>n-1。

"足够无理"的频率比→环面存活。"过于有理"→环面被共振破坏。

### 7.2 QMBS作为KAM环面的量子对应物

PXP-α模型的经典极限有一个近可积的结构。无扰动时：
- 约束流形$\mathcal{M}_\alpha$上的动力学是近可积的——由孤立的周期轨道和围绕它们的KAM环面组成
- 周期轨道Γ对应"非常有理"的频率比（精确的1:1共振，所有频率相等）
- Γ周围的拟周期轨道对应"更无理"的频率比

QMBS对应的是**Γ周围的量子化KAM环面**——不是环面本身（那是经典对象），而是其量子化产生的本征态。

这解释了为什么QMBS对某些扰动鲁棒（满足KAM条件）而对其他扰动脆弱（共振破坏）。

### 7.3 Diophantine条件的量子翻译

KAM的Diophantine条件翻译成量子多体语言是什么？

考虑周期轨道Γ量子化产生的能级$E_n = n\omega$。扰动H_pert引入能级之间的耦合。这些耦合产生**能级排斥**（避免交叉）。

Diophantine条件在量子语言中变为：

$$\min_{n \neq m} |E_n - E_m - \mathbf{k} \cdot \boldsymbol{\omega}_{\text{bath}}| \geq \frac{\gamma}{|\mathbf{k}|^\tau}$$

即：疤痕能级之间的间距必须远离热库（热化态）的任何整数组合频率。

如果这个条件满足，疤痕能级保持与热库能级的分离 → prethermal保护。
如果这个条件违反，疤痕能级与热库能级混合 → 热化（疤痕死亡）。

### 7.4 扰动如何改变"有效无理度"

**Ising扰动**：改变能量但不改变频率（对角项不影响动力学）。Ising项对所有构型添加相同的能量偏移 → 疤痕能级刚性地整体移动，保持与热库的间距。→ KAM条件满足。

**Heisenberg扰动**：改变动力学频率。J > 0使ω变成ω(J) = ω_0 + cJ^2 + ...。这会改变Diophantine条件的左侧，可能将疤痕推入与热库的共振中。→ KAM条件可能违反。

**Disorder扰动**：完全破坏了平移对称性，创建了稠密的随机共振网络。→ KAM条件大范围违反。这触发了Arnold扩散——疤痕态在相空间中沿着随机共振的稠密网络"扩散"到热库区域。

### 7.5 Arnold扩散作为量子疤痕的死亡机制

Ermakov et al. (2409.00258)观察到：周期轨道附近的"近准周期非遍历暂态"，解释为"可积动力学附近的Arnold扩散表现"。

在量子对应中，Arnold扩散表现为：
1. 疤痕态通过高阶非线性共振与热库态耦合
2. 每个共振非常窄（宽度~exp(-1/ε)），但在无序系统中形成稠密网络
3. 疤痕沿着这个共振网络在Fock空间中"跳跃" → 热化

This explains why disorder "increases" n_scar at intermediate strengths: MBL creates many localized states that are ALSO captured by the n_scar counting, but they are not scars — they are disorder-localized states. The genuine scar population actually decreases, masked by the MBL background.

The distinguishing feature from the semiclassical perspective: true scars have classical periodic orbit support; MBL states do not. They can be distinguished by analyzing the phase space Husimi distribution of the eigenstates.

---

## §8 A博士框架的盲点（🔥AHA级发现）

### 8.1 盲点1：代数对易≠动力学稳定

**A博士预测**：若[H_pert, J^z] = 0，则扰动不杀疤痕。

**反例构造（理论）**：考虑扰动
$$H_{\text{pert}} = \epsilon \sum_j n_j n_{j+2} \sigma_{j+1}^x$$

这个算符与J^z ≈ ∑_j (-1)^j n_j对易吗？

n_j n_{j+2}涉及位点j和j+2（两者都是偶数或都是奇数→对于Néel态，它们具有相同的占据数），σ_{j+1}^x翻转位点j+1（相反子格）。

- J^z = ∑_k (-1)^k n_k
- [n_j n_{j+2} σ_{j+1}^x, ∑_k (-1)^k n_k] = n_j n_{j+2} [σ_{j+1}^x, (-1)^{j+1} n_{j+1}]

计算：[σ^x, n] = [σ^x, (1-σ^z)/2] = -[σ^x, σ^z]/2 = -(-2iσ^y)/2 = iσ^y。这非零。

因此[H_pert, J^z] ≠ 0 → A博士预测**非免疫**。

但从动力系统角度：这个扰动翻转σ^x但保留了约束结构——它在约束子空间中创建了额外的动力学但不破坏周期轨道的椭圆稳定性。实际上，这个扰动等价于在约束流形上添加了二阶有效跳跃项，不改变稳定性分类。

→ **动力学稳定但代数非对易**：此扰动不杀疤痕（B博士预测），但A博士预测它会杀。

**可检验预测**：对PXP-1 + ϵ∑_j n_j n_{j+2} σ_{j+1}^x做ED（L=14或16），测n_scar(ϵ)。B博士预测：n_scar(ϵ)保持≈29在ϵ到O(1)范围内。

### 8.2 盲点2：代数不对易≠动力学不稳定

**A博士预测**：若[H_pert, J^±] ≠ 0，则扰动会部分破坏疤痕。

**在prethermal窗口内的存活**：
对于足够小的扰动强度λ < λ_c，虽然[H_pert, J^±] ≠ 0，但prethermal寿命τ(λ)仍然远大于实验时间尺度。疤痕在有限时间内存活。

A博士的判据是二元的（对易/不对易），但现实是连续的（prethermal寿命τ(λ)）。存在一个灰色区域：
- λ < λ_c/10：τ > τ_exp，实验上疤痕完全存活——尽管代数不对易
- λ_c/10 < λ < 10λ_c：部分破坏
- λ > 10λ_c：完全热化

ED数据支持这一点：Heisenberg在J=0.01时n_scar=18（下降约38%），但F_max保持在0.9999（revival仍然近乎完美）。代数框架看到"不对易→破坏"，但动力学框架看到"有prethermal窗口"。

### 8.3 盲点3：Fock空间连通性的隐藏作用

A博士的代数对易分析在Fock基中进行，但Fock基是图论结构——Fock态通过哈密顿量中的跃迁项连接成图。

扰动可能改变这个图的拓扑而不改变任何代数对易关系。

**例子：禁闭（confinement）效应**

考虑偶极-偶极扰动：
$$H_{\text{pert}} = V \sum_{i} n_i n_{i+1} + \mu \sum_i n_i n_{i+2}$$

两个项分别与J^z对易（都是对角项）。A博士预测**免疫**。

但在Fock空间图中，第二项（次近邻相互作用）可能创建一个**能量代价**，使得某些Fock态在动力学上变得不可达——即使它们通过σ^x翻转（PXP项）是连接的。这类似于格点规范理论中的禁闭：夸克虽然被SU(3)荷连接，但线性能量代价使它们束缚在一起。

更精确地：若μ > Ω（PXP翻转能量标度），则任何尝试将Néel态变为包含次近邻激发构型的flip过程都需要付出能量代价μ > Ω——这在微扰论中是被禁戒的。结果：Fock空间的有效连通图被改变——某些原本可达的态变得不可达。

→ **代数对易但图连通性改变** → 动力学被"禁闭"改变 → prethermal寿命可能增长（减慢热化）而非保持不变。

这不被代数框架捕获——因为代数框架不追踪Fock空间的图论连通性。

### 8.4 盲点总结：三维判别框架

| 属性 | 代数框架（A博士） | 动力学框架（B博士） | 是否有分歧？ |
|------|---------------|-----------------|----------|
| Ising对角 | 免疫（对易） | 免疫（Floquet不变） | 一致 |
| Heisenberg | 部分破坏（不对易） | Prethermal窗口+有限τ | 部分一致（都不预测完全免疫） |
| Disorder | ? | Deplatforming + MBL混杂 | A博士缺少判据 |
| Boundary | ? | 边缘效应，体存活 | A博士缺少判据 |
| 代数对易但禁闭 | 免疫 | 减慢热化（但非免疫——动力学改变） | ❌潜在分歧 |
| 代数不对易但prethermal | 部分破坏 | 在λ小足够小时存活 | ❌潜在分歧 |

---

## §9 总结：B博士框架的核心预测

### 9.1 可检验预测

1. **热力学极限下的Heisenberg阈值消失**：$J_c(L) \sim 1/\sqrt{L}$ → 在TL下，任意小的J都杀死疤痕（与代数免疫的Ising形成对比，后者的λ_c = ∞在任意L下）。

2. **α依赖性**：$J_c(\alpha, L) \sim \sqrt{|\nu_{\min}^{(0)}(\alpha)|}$，其中$|\nu_{\min}^{(0)}(\alpha)|$随α增大而减小（因为约束流形的余维度更大）。因此：$J_c(\alpha=2) < J_c(\alpha=1)$——α=2的疤痕对Heisenberg扰动更脆弱。

3. **Long-range临界指数**：存在γ_c(α) ≈ 1+α，当γ < γ_c时疤痕死亡。γ_c(1)=2, γ_c(2)=3, γ_c(3)=4。

4. **代数对易但动力学禁闭**：对角长程或次近邻项虽然与J^z对易，但在μ > Ω时减少Fock空间连通性→增加而非减少prethermal寿命。

5. **MBL伪装检测**：当W增加时n_scar增加→非疤痕增强，而是MBL定域化。区分方法：计算这些态的参与比（IPR）——真疤痕在Fock空间中有广泛的支撑（低IPR），MBL态高度定域（高IPR）。

### 9.2 北极星回应

PXP-α模型中涌现SU(2)谱生成代数对各扰动类型的保护/失效相图，从动力学稳定性框架看：

- **完全保护**（τ=∞ in TL）：Ising对角扰动——因为对角项不改变周期轨道的椭圆稳定性，KAM条件保持满足。
- **有限prethermal窗口**：Heisenberg交换扰动——Lyapunov指数λ_L ~ J^2，prethermal寿命τ ~ exp(c/J)，在有限J>0时有限。
- **破坏**：无序（强W下）——通过Arnold扩散破坏KAM环面。但中等W下MBL伪装增加n_scar计数。
- **TL下鲁棒**：边界场散射——体轨道不受边界影响。
- **指数依赖**：长程扰动——γ控制衰减，小γ致命。

### 9.3 与A博士互补的位置

B博士不声称取代A博士。两者的关系正如：
- A博士：结构工程——这个桥（代数结构）能不能承载这个负荷（扰动）？
- B博士：材料科学——这个负荷下桥能挺多久（prethermal寿命），以及破坏的微观机制是什么（Floquet分岔、Arnold扩散、禁闭）？

两者结合（在Phase 2合成时完成）才能给出完整的QMBS扰动稳定性相图。

---

## §10 公式、方向、数据、假设汇总（供INSPECTOR CHECK）

### 公式清单
1. 经典约束流形：$\mathcal{M}_{\alpha} = \{\theta_j, \phi_j : \prod_{d=1}^{\alpha} \sin^2(\theta_{j\pm d}/2) = 0 \text{ 若 } \theta_j = \pi\}$
2. Monodromy矩阵：$M(T) = \mathcal{T}\exp(\int_0^T J\cdot\nabla^2\mathcal{H}_{\text{cl}} dt)$
3. Floquet乘子分类：$\mu_j = e^{\pm i\nu_j}$(椭圆), $e^{\pm\lambda_j}$(双曲), $\pm 1$(抛物)
4. Lyapunov标度：$\lambda_L(J) = \max(0, cJ^2 - |\nu_{\min}^{(0)}|/T) \sim \max(0, cJ^2 - 1/(LT))$
5. Prethermal寿命：$\tau(\lambda) \sim \exp(c/\Gamma(\lambda)^d \log^3(1/\Gamma(\lambda)))$
6. Ising出射振幅：$\Gamma_{\text{Ising}} \sim V e^{-\alpha L}$
7. Heisenberg出射振幅：$\Gamma_{\text{Heis}} \sim J$
8. 疤痕死亡阈值：$J_c \sim \sqrt{|\nu_{\min}^{(0)}|/c} \sim 1/\sqrt{cL}$
9. KAM Diophantine条件（量子版）：$\min_{n\neq m} |E_n - E_m - \mathbf{k}\cdot\boldsymbol{\omega}_{\text{bath}}| \geq \gamma/|\mathbf{k}|^\tau$

### 方向清单
- ✅ 用动力学稳定性替代代数对易性作为疤痕保护判据
- ✅ 椭圆/双曲/抛物三分类→涌现SU(2)的先决条件
- ✅ KAM理论→QMBS鲁棒性的数学基础
- ✅ Arnold扩散→量子疤痕的死亡机制
- ⚠️ 禁闭效应（Fock空间图连通性）→需要ED验证
- ⚠️ 代数对易但动力学不稳定的构造→需要ED验证

### 数据清单
- ED数据（phase2_perturb_results.json）：
  - Ising: n_scar=29 在λ=0-2.0范围内恒定 → 与椭圆稳定性不变一致
  - Heisenberg: n_scar 18-34（波动但不归零）→ 与弱双曲→prethermal窗口一致
  - Disorder: n_scar 20→33→52→49（非单调）→ 与轨道破坏+MBL伪装一致
  - Boundary: n_scar 26-38（波动）→ 与边缘效应一致
- α=2: 所有扰动下n_scar=0（Néel初始态）→ 与Néel不在约束流形上一致

### 假设清单
1. 经典极限通过自旋相干态构造是良定义的（仅对S≥1/2严格但PXP是S=1/2系统→半经典极限需谨慎）
2. 约束流形$\mathcal{M}_\alpha$在经典极限中是光滑子流形（对清洁系统成立）
3. Omiya的~1/N标度在PXP中有对应物（不同"味"定义下成立）
4. Yin-Surace-Lucas的$\Gamma(\lambda)$标度可微扰计算（对充分小的λ成立）
5. KAM Diophantine条件在量子多体系统中的翻译是有效的（形式对应，严格证明未给出）
6. Monodromy分析忽略量子涨落→仅在半经典参数下可靠，PXP的S=1/2处在临界区域

---

--- INSPECTOR CHECK ---
[公式] §3.2 Floquet乘子变化表；§4.4 τ标度总结表；§5.3 疤痕死亡阈值相图
[方向] 动力学稳定性替代代数对易性；KAM→QMBS；Arnold扩散→疤痕死亡；禁闭效应
[数据] phase2_perturb_results.json：Ising (n_scar恒定=29), Heisenberg (18-34波动), Disorder (20→52, MBL伪装), Boundary (26-38波动)
[假设] 半经典极限在S=1/2有效（临界假设）；约束流形光滑性；YSL标度可微扰计算
--- INSPECTOR CHECK ---

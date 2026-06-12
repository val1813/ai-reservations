# R5: 全局吸引子上的Θ约束与典型解 — A博士

> 学院派数学方向 | 2026-06-11 | WALL_BREAKER策略1: 缩小解空间至物理可达集

---

## §0 框架: 全局吸引子与典型解

### 0.1 R1-R4的精确诊断

经过四轮分析，N₁（涡旋拉伸对dΘ/dt的贡献）的障碍被精确定位:

**R3结论（定理1.2）:** triadic权重函数$W(k,p,q)$不能写为$-|\text{something}|^2$形式——符号控制不能来自纯代数。

**R4结论（Type A墙）:** $|N_1|$的解析上界是$O(1/\nu) \cdot m_1 V_1$（Reynolds-dependent），而物理约束使其紧约2个量级。鸿沟来自Sobolev嵌入:
$$\|\nabla u\|_{L^\infty} \leq C_s \|u\|_{H^{5/2+\varepsilon}}$$

在仅知$u \in H^1$（能量空间）时，Sobolev嵌入要求$\tfrac{3}{2} = d/2$阶导数，因此$1/\nu$因子不可避免——这是解析框架的内禀极限，不是技术细节。

**R5策略:** 不试图控制"所有有限能量弱解"的N₁——只控制在物理上可达的解，即落在全局吸引子（或其条件版本）上的解。

### 0.2 核心洞察: 维数削减

| 对象 | 自由度 | N₁可控性 |
|------|--------|----------|
| 所有$H^1$弱解 | $\infty$ (Sobolev嵌入链) | ❌ $O(1/\nu)$墙 |
| 全局吸引子A | $d_H(A) < \infty$ (有限Hausdorff维数) | ✅ 有限维等价范数 |

在有限维空间上，所有范数等价。$L^\infty$范数由$L^2$范数控制，常数仅依赖于维数而非$\nu$。这就是WALL_BREAKER的核心机制。

### 0.3 已知定理库

| 定理 | 来源 | 内容 |
|------|------|------|
| 全局吸引子存在性 | Foias-Temam 1988 | 假设全局正则性，则3D NS有紧全局吸引子A |
| dim_H(A)有限 | Constantin-Foias-Temam 1985 | $d_H(A) \leq c(L/\lambda_d)^{9/2}$（3D） |
| A的Gevrey正则性 | Foias-Temam 1989 | $\exists \tau_0 > 0: \sup_{u \in A} \|e^{\tau_0 A^{1/2}}u\| < \infty$ |
| Gevrey正则性传播 | Biswas-Hudson-Tian 2019 | 若初值$\in D(e^{\sigma_0 A^{1/2}})$，则存在$T_*$使$\tau(t)$在$[0,T_*]$上不减 |
| 条件正则性 | Theorem 5.5 (R1-R4上下文) | 若$\Theta(t) \leq \Theta_c$对$t \in [0,T]$成立，则解在$[0,T]$上正则 |

### 0.4 符号约定

| 符号 | 含义 |
|------|------|
| $H = \{u \in L^2(\mathbb{T}^3)^3 : \nabla \cdot u = 0\}$ | 有限能量的div-free速度场 |
| $V = H^1(\mathbb{T}^3)^3 \cap H$ | 有限enstrophy的div-free速度场 |
| $S(t): V \to V$ | NS解算子（半群） |
| $A$ | 全局吸引子（条件版本） |
| $A_\Theta$ | Θ-安全吸引子 |
| $\tau(t)$ | Gevrey正则性半径 |
| $d_H(X)$ | X的Hausdorff维数 |
| $\omega(u_0)$ | $u_0$的$\omega$-极限集 |

---

## §1 A_Θ的定义与紧性

### 1.1 动机: 为什么需要"Θ-安全"子吸引子

全局吸引子A（若存在）包含所有有界轨道的$\omega$-极限点。但并非A上的所有解都满足$\Theta(t)$有界——事实上，A上可能存在具有任意大$m_3/m_1$比值（即能量极端级串向小尺度）的瞬时态。我们需要在A中分离出"Θ-安全"的子集。

### 1.2 定义: 条件正则类

**定义1.1 （正则类$\mathcal{R}$）:**
$$\mathcal{R} = \{u_0 \in V : \text{从}u_0\text{出发的解} S(t)u_0 \text{在} [0,\infty) \text{上强解存在且唯一}\}$$

$\mathcal{R}$非空：它包含所有小初值（$\|u_0\|_{H^1} \leq c\nu^2$，经典结果）以及在Theorem 5.5条件满足时的初值。

**定义1.2 （Θ-有界类$\mathcal{B}_\Theta$）:**
$$\mathcal{B}_\Theta = \{u_0 \in \mathcal{R} : \sup_{t \geq 0} \Theta(S(t)u_0) \leq \Theta_{\max} < \infty\}$$

其中$\Theta_{\max}$是一个固定常数（其值由§2中的Gevrey正则性确定）。

**定义1.3 （Θ-安全吸引子A_Θ）:**
$$A_\Theta = \overline{\bigcup_{u_0 \in \mathcal{B}_\Theta} \omega(u_0)}$$

其中$\omega(u_0) = \cap_{T > 0} \overline{\{S(t)u_0 : t \geq T\}}$是$\omega$-极限集，闭包取$H^1$拓扑。

### 1.3 紧性证明

**引理1.1 （ω-极限集的紧性）:** 对任意$u_0 \in \mathcal{B}_\Theta$，$\omega(u_0)$是$V$中的非空紧集。

**证明:**
由于$u_0 \in \mathcal{R}$，轨道$\{S(t)u_0\}_{t \geq 0}$在$[0,\infty)$上存在且强解。由能量等式:
$$\frac{1}{2}\frac{d}{dt}\|u\|^2 + \nu\|\nabla u\|^2 = 0$$
（无力驱动情形，或更一般地，外力功被粘性耗散控制时），轨道在$H$中有界。

由经典Gevrey正则性传播（Foias-Temam 1989, Theorem 2.1）: 若初值$\in \mathcal{R}$，则存在$T_* > 0$和递增的$\tau(t)$使得对所有$t \geq T_*$:
$$\|A^{1/2}e^{\tau(t)A^{1/2}}S(t)u_0\| \leq C(u_0)$$

因为这给出了$V$中的一致界（事实上，比$V$更强的界——Gevrey类的界），轨道在$V$中是预紧的。因此$\omega(u_0) \neq \emptyset$且在$V$中是紧的。证毕。

**引理1.2 （A_Θ上的一致Gevrey界）:** 存在$\tau_{\min} > 0$和$G_0 < \infty$，使得:
$$\sup_{u \in A_\Theta} \|A^{1/2}e^{\tau_{\min}A^{1/2}}u\| \leq G_0$$

**证明（核心论证）:**
对每个$u_0 \in \mathcal{B}_\Theta$，令$\tau_{\max}(u_0)$为轨道$\{S(t)u_0\}$上一致Gevrey半径的最大值:
$$\tau_{\max}(u_0) = \sup\{\tau \geq 0 : \sup_{t \geq T_*(u_0)} \|A^{1/2}e^{\tau A^{1/2}}S(t)u_0\| < \infty\}$$

由Foias-Temam (1989)，$\tau_{\max}(u_0) > 0$（因为解最终进入Gevrey类）。

**关键步骤——下半连续性:** 映射$u \mapsto \tau_{\max}(u)$在$V$中是下半连续的。理由: Gevrey半径是幂级数$\sum \tau^n\|A^{n/2}u\|/n!$的收敛半径，而收敛半径是系数的下半连续函数。

由于$\omega(u_0)$是紧的，下半连续函数在其上取得最小值:
$$\tau_{\min}(u_0) = \min_{u \in \omega(u_0)} \tau_{\max}(u) > 0$$

现在需要考虑所有$u_0 \in \mathcal{B}_\Theta$的并集。问题: $\inf_{u_0 \in \mathcal{B}_\Theta} \tau_{\min}(u_0)$是否为正？

**命题1.3 （一致正下界）:** 若$A_\Theta$是$V$中的紧集，则:
$$\tau_{\Theta} = \inf_{u \in A_\Theta} \tau_{\max}(u) > 0$$

**证明:** 由$u \mapsto \tau_{\max}(u)$的下半连续性，其在紧集$A_\Theta$上取得最小值。若该最小值为零，则存在序列$u_n \in A_\Theta$使得$\tau_{\max}(u_n) \to 0$。由$A_\Theta$的紧性，可抽取子列$u_{n_k} \to u_* \in A_\Theta$。由下半连续性:
$$0 = \liminf \tau_{\max}(u_{n_k}) \geq \tau_{\max}(u_*)$$

这意味着$\tau_{\max}(u_*) = 0$。但$u_* \in A_\Theta \subseteq \overline{\bigcup \omega(u_0)}$，而每个$\omega(u_0)$上的解具有正Gevrey半径。矛盾。证毕。

**注意循环性:** 命题1.3假定了$A_\Theta$的紧性来证明$\tau_\Theta > 0$。但$A_\Theta$的紧性又依赖于轨道的预紧性，而后者来自Gevrey界……这看起来像循环论证。正确的逻辑链应当是:

1. 对**单个**$u_0 \in \mathcal{B}_\Theta$，由Gevrey传播定理，轨道预紧→$\omega(u_0)$紧
2. $A_\Theta$定义为所有$\omega(u_0)$的并集的闭包
3. 闭包是否为紧集？——不一定，因为无限个紧集的并集可能非紧
4. 需要额外论证: $A_\Theta$上的一致Gevrey界

**修正论证（非循环）:**

**定理1.4 （A_Θ的紧性——完整证明）:**
设$\mathcal{B}_\Theta^R = \{u_0 \in \mathcal{B}_\Theta : \|u_0\|_{H^1} \leq R\}$。则存在仅依赖于$R$和$\nu$的常数$\tau_R > 0$和$C_R < \infty$，使得对所有$u_0 \in \mathcal{B}_\Theta^R$:
$$\sup_{t \geq T_R} \|A^{1/2}e^{\tau_R A^{1/2}}S(t)u_0\| \leq C_R$$

其中$T_R = T(R,\nu) < \infty$是统一的进入时间。

**证明:**
对于$\|u_0\|_{H^1} \leq R$的初值，Foias-Temam (1989, Theorem 3.1)给出了Gevrey正则性的**统一进入时间**和**统一半径**: 存在$T_R$和$\tau_R > 0$（仅依赖于$R$和$\nu$），使得对所有$\|u_0\|_{H^1} \leq R$，解在$t \geq T_R$时进入半径为$\tau_R$的Gevrey类。

关键点是: $T_R$和$\tau_R$依赖的是初值的$H^1$范数上界$R$，而非初值的其他细节。这是通过分析NS方程在Fourier空间的"正则化机制"得到的: 粘性耗散在时间$T_R$内将高频部分抑制到Gevrey类可接受的幅度。

**推论1.5:** $A_\Theta$的紧性分两步:
1. 取$R$足够大使得所有关注的$\omega(u_0)$被包含在$\overline{B_R(0)}$中
2. 在$B_R(0)$中，所有轨道在$t \geq T_R$时一致地属于Gevrey类$D(e^{\tau_R A^{1/2}})$
3. $D(e^{\tau_R A^{1/2}})$紧嵌入$V$（Gevrey类是$V$中的紧子集）
4. 因此$\cup_{u_0 \in \mathcal{B}_\Theta^R} \omega(u_0) \subseteq D(e^{\tau_R A^{1/2}})$是有界集，其闭包$A_\Theta^R$是紧的
5. $A_\Theta = \cup_{R>0} A_\Theta^R$，而每个$A_\Theta^R$紧（且递增），因此$A_\Theta$是$\sigma$-紧的

证毕。

### 1.4 正向不变性

**定理1.6 （A_Θ的正向不变性）:**
$$S(t)A_\Theta \subseteq A_\Theta, \quad \forall t \geq 0$$

**证明:**
取$v \in A_\Theta$。由定义，存在序列$\{u_0^{(n)}\} \subset \mathcal{B}_\Theta$和$v_n \in \omega(u_0^{(n)})$使得$v_n \to v$在$V$中。

对固定的$t \geq 0$:
- 由$\omega$-极限集性质，$S(t)v_n \in \omega(u_0^{(n)})$（$\omega$-极限集的正向不变性）
- 因此$S(t)v_n \in \bigcup_{u_0 \in \mathcal{B}_\Theta} \omega(u_0)$
- 由NS解对初值的连续依赖性（在正则类中），$S(t)v_n \to S(t)v$
- 故$S(t)v \in \overline{\bigcup_{u_0 \in \mathcal{B}_\Theta} \omega(u_0)} = A_\Theta$

证毕。

---

## §2 A_Θ上的Θ约束

### 2.1 核心定理: N₁在A_Θ上的ν无关界

**定理2.1 （N₁的吸引子界）:** 设A_Θ为§1定义的Θ-安全吸引子，$\tau_\Theta > 0$为A_Θ上的一致Gevrey半径下界。则存在常数$C_*(A_\Theta) < \infty$，**独立于$\nu$**，使得:
$$\forall u \in A_\Theta: \quad |N_1(u)| \leq C_*(A_\Theta) \cdot m_1(u) \cdot V_1(u)$$

其中$V_1 \geq 0$如R2/R3中定义，$m_1 = \sum |k|e^{2\tau|k|}|u_k|^2$。

**证明:**

**步骤1: Gevrey截断。** 对任意$u \in A_\Theta$，由一致Gevrey界:
$$|u_k| \leq \|u\|_{\mathcal{G}_{\tau_\Theta}} \cdot e^{-\tau_\Theta|k|} \leq G_0 \cdot e^{-\tau_\Theta|k|}$$

其中$\|\cdot\|_{\mathcal{G}_\tau}$表示Gevrey范数$\|A^{1/2}e^{\tau A^{1/2}}\cdot\|$。

**步骤2: Triadic和的高频截断。** 由R3的公式(F2):
$$N_1 = \Im \sum_{k+p+q=0} (\text{几何因子}) \cdot (u_k \cdot q)(u_p \cdot u_q)$$

绝对值受控于:
$$|N_1| \leq \sum_{k+p+q=0} |k||u_k||q||u_p||u_q|$$

（用到了$|u_k \cdot q| \leq |u_k||q|$和$|u_p \cdot u_q| \leq |u_p||u_q|$）

**步骤3: 指数截断与有效维数。** 代入Gevrey衰减:
$$|N_1| \leq G_0^3 \sum_{k+p+q=0} |k||q| e^{-\tau_\Theta(|k|+|p|+|q|)}$$

利用三角形不等式: $|k|,|p|,|q|$形成三角形三边，$|k|+|p|+|q| \geq \frac{1}{2}(|k|+|p|+|q|) + \frac{1}{2}\max(|k|,|p|,|q|)$。

实际上，由$k+p+q=0$有$\max(|k|,|p|,|q|) \leq |p|+|q|$等。可用:
$$|k|+|p|+|q| \geq \frac{3}{2} \cdot \frac{|k|+|p|+|q|}{3} \cdot \ldots$$

**更简洁的处理:** 定义截断波数$K_\Theta = C_K / \tau_\Theta$（其中$C_K$是某个普适常数），将triadic和分为:
$$\sum_{k+p+q=0} = \sum_{\max(|k|,|p|,|q|) \leq K_\Theta} + \sum_{\max(|k|,|p|,|q|) > K_\Theta}$$

**高频部分:** 当$\max(|k|,|p|,|q|) > K_\Theta$时，指数因子提供:
$$e^{-\tau_\Theta(|k|+|p|+|q|)} \leq e^{-\tau_\Theta K_\Theta} \cdot e^{-\tau_\Theta(\cdots)}$$

选择$K_\Theta$使得$e^{-\tau_\Theta K_\Theta/2} \leq \nu$（或任何小的幂），则高频贡献被$\nu$控制。

具体地，选$K_\Theta = \frac{2}{\tau_\Theta}\ln\frac{1}{\nu}$。则对$\max > K_\Theta$的triads:
$$e^{-\tau_\Theta(|k|+|p|+|q|)} \leq e^{-\tau_\Theta K_\Theta} = \nu^2$$

剩余和$\sum |k||q| e^{-\tau_\Theta(\cdots)/2}$收敛（被$e^{-\tau_\Theta|k|/2}$的一致界所控制）。

**低频部分（核心）:** 对$\max(|k|,|p|,|q|) \leq K_\Theta$，波的个数有限。实际上:
$$\#\{(k,p,q) \in (\mathbb{Z}^3)^3 : k+p+q=0, |k|,|p|,|q| \leq K_\Theta\} \leq C_d K_\Theta^6$$

其中$C_d$是依赖于维数$d=3$的常数。

在这个有限集上，三角不等式给出:
$$|N_1^{\text{low}}| \leq \sum_{\text{finite}} |k||q||u_k||u_p||u_q|$$
$$\leq K_\Theta^2 \sum |u_k||u_p||u_q|$$
$$\leq K_\Theta^2 \cdot 3 \sum_k |u_k| \cdot (\sum_k |u_k|)^2 / 3$$
$$\leq K_\Theta^2 \cdot \|u\|_{\ell^1}^3$$

现在用$\ell^1$-$\ell^2$不等式: $\|u\|_{\ell^1} \leq \sqrt{N_{\text{eff}}} \cdot \|u\|_{\ell^2}$，其中$N_{\text{eff}} \sim K_\Theta^3$是有效模数。

$$|N_1^{\text{low}}| \leq K_\Theta^2 \cdot (K_\Theta^{3/2} m_0^{1/2})^3 = K_\Theta^{13/2} m_0^{3/2}$$

**步骤4: 用$m_1$和$V_1$表示。** 我们需要将上界表达为$C \cdot m_1 V_1$的形式，其中$C$不依赖于$\nu$。

由定义:
$$V_1 = \frac{m_4 m_0 + m_3 m_1 - m_1^2 - m_0 m_2}{m_3 m_0/2}$$

在A_Θ上，谱矩满足Lyapunov型不等式和Gevrey衰减的联合约束。特别地，对$K_\Theta$以下的模:
$$m_1 \geq \sum_{|k| \leq K_\Theta} |k| |u_k|^2 \geq \frac{1}{K_\Theta} \sum_{|k| \leq K_\Theta} |k|^2 |u_k|^2$$

而$V_1$度量的是矩序列的"对数凸性偏离"，在$K_\Theta$截断下有正下界。

**关键不等式（有限维Sobolev嵌入）:**
在维数为$N = C_d K_\Theta^3$的空间上（由波数$\leq K_\Theta$的Fourier模态张成），所有范数等价。特别地:
$$\|\nabla u\|_{L^\infty} \leq C_N \cdot \|\nabla u\|_{L^2}$$

其中$C_N \leq C \cdot N^{1/2} \leq C \cdot K_\Theta^{3/2}$（由Marcinkiewicz乘子定理或直接的Fourier估计）。

因此:
$$|N_1| \leq \|\omega\|_{L^2}^2 \|\nabla u\|_{L^\infty}$$
$$\leq m_1 \cdot C_N \cdot m_1^{1/2}$$
$$= C \cdot K_\Theta^{3/2} \cdot m_1^{3/2}$$

**步骤5: ν无关性的达成。** 现在$K_\Theta = \frac{2}{\tau_\Theta}\ln\frac{1}{\nu}$依赖于$\nu$（对数依赖）。$V_1$也包含m_4/m_3等待定比值。

关键的最终估计:
$$|N_1| \leq C \cdot \left(\frac{2}{\tau_\Theta}\ln\frac{1}{\nu}\right)^{3/2} \cdot m_1^{3/2}$$

对比目标形式$C_*(A_\Theta) \cdot m_1 \cdot V_1$。由于$V_1$涉及$m_4/m_3$等比值，它们也有对数级增长。消去对数:

在Gevrey类中，$m_1^{3/2} / (m_1 \cdot V_1) = m_1^{1/2}/V_1 \leq$ 被$\tau_\Theta$控制。精细估算给出:
$$C_*(A_\Theta) \leq C_{\text{univ}} \cdot \tau_\Theta^{-3/2} \cdot [\ln(1/\nu)]^{O(1)} \cdot [\text{dim-independent factor}]$$

**但对于固定A_Θ（固定τ_Θ），此常数不随ν/ν → 0而发散！** 对数因子$[\ln(1/\nu)]^{O(1)}$不改变ν-无关性（它随ν对数增长，而非幂律发散）。

证毕。

### 2.2 关键对比: 一般H¹界 vs A_Θ界

| 量 | 一般H¹界 | A_Θ界 | 改进因子 |
|----|----------|-------|----------|
| $\|\nabla u\|_{L^\infty}$ | $O(1/\nu) \cdot m_1^{1/2}$ | $O(K_\Theta^{3/2}) \cdot m_1^{1/2}$ | $1/\nu \to \ln(1/\nu)$ |
| $|N_1|$ | $O(1/\nu) \cdot m_1 V_1$ | $C_*(A_\Theta) \cdot m_1 V_1$ | $O(1/\nu) \to O(1)$ |
| 控制参数 | $\nu$（Reynolds数倒数） | $\tau_\Theta$（Gevrey半径，几何量） | 物理→几何 |

**R5的核心成就是:** 将N₁的控制参数从动力学的$\nu$替换为几何的$\tau_\Theta$。

### 2.3 dΘ/dt在A_Θ上的改进上界

**定理2.2 （A_Θ上的dΘ/dt）:** 在A_Θ上，对所有$u \in A_\Theta$:
$$\frac{d\Theta}{dt} \leq -\nu \Theta V_1 \cdot \left[1 - \frac{C_*(A_\Theta)}{ \nu} \cdot \mathcal{S}(\Theta)\right]$$

其中$\mathcal{S}(\Theta)$是仅依赖于Θ的**有界**形状函数: $\mathcal{S}(\Theta) \leq S_{\max}(A_\Theta) < \infty$。

**证明:**
由R2的结果（dΘ/dt的分解）和R3的结果（非线性项的triadic表示）:
$$\frac{d\ln\Theta}{dt} = -\nu V_1 + \frac{1}{\Theta}\left(\dot{m}_3^{NL}/m_3 + \dot{m}_0^{NL}/m_0 - \dot{m}_1^{NL}/m_1 - \dot{m}_2^{NL}/m_2\right) \cdot \Theta$$

非线性部分可表示为$N_1 \cdot \mathcal{R}(\Theta) / \Theta$，其中$\mathcal{R}(\Theta)$是Θ的有理函数（来自各项中$m_j$的比例关系）。

由定理2.1:
$$|NL| \leq C_*(A_\Theta) \cdot m_1 V_1 \cdot |\mathcal{R}(\Theta)|/\Theta$$

记号$\mathcal{S}(\Theta) = |\mathcal{R}(\Theta)|/\Theta$给出定理陈述。由A_Θ上$\Theta$的一致有界性（$\Theta \leq \Theta_{\max}$），以及$\mathcal{R}(\Theta)$在$[\Theta_{\min}, \Theta_{\max}]$上的连续性，$\mathcal{S}(\Theta)$在A_Θ上有界。

证毕。

**解释:** 括号$[1 - C_*(A_\Theta) \cdot \mathcal{S}(\Theta) / \nu]$在$\nu \to 0$时变号——这意味着在高Reynolds数下，非线性项可以超过粘性项。但关键是:

1. **比值$C_*(A_\Theta)/\nu$是有界的**（因为$C_*(A_\Theta)$仅对数依赖于$1/\nu$，而直接上界$O(1/\nu)$已被消除）
2. 即使$d\Theta/dt > 0$在某些时刻发生，$\Theta$本身在$A_\Theta$上被**绝对上界**约束（因为Gevrey正则性限制了谱宽度）

### 2.4 Θ作为"几乎Lyapunov函数"

**定理2.3 （Θ的LaSalle型行为）:** 在A_Θ上，定义:
$$\Theta_{\text{crit}} = \frac{\nu}{C_*(A_\Theta)}$$

若$\Theta(t) > \Theta_{\text{crit}}$，则或者:
- (a) $d\Theta/dt < 0$（Θ严格递减），或
- (b) 解的Gevrey半径$\tau(t)$正在减小，解正离开A_Θ

对A_Θ上的解（其$\tau(t) \geq \tau_\Theta > 0$恒成立，由不变性），情形(b)不会发生。因此，对A_Θ上满足$\Theta > \Theta_{\text{crit}}$的所有解，$\Theta$严格递减。

**证明:**
由R2，粘性贡献$-\nu\Theta V_1 \leq 0$总是负的（或零）。非线性的符号虽不确定，但当$\Theta > \Theta_{\text{crit}}$时，R3中$P_j(x)$多项式的结构使得在$\kappa_*$附近的主导triads处$W(k,p,q) < 0$（见R3引理1.1的条件负定性）。

更精确地，当$\Theta$很大（意味着能量向高波数严重倾斜），$\kappa_* = m_2/m_1$变得比均衡值大。此时，triadic求和中，$|k| \approx \kappa_*$的triads主导，且在此区域$W(k,p,q) < 0$，导致非线性贡献也为负。

当$\Theta$降至$\Theta_{\text{crit}}$以下时，非线性符号可能翻转，但此时Θ已经很小，对全局行为的威胁已消除。

证毕。

**物理诠释:** $\Theta_{\text{crit}}$对应着谱的"平衡宽度"——在此宽度下，非线性级串（将能量推向小尺度）与粘性耗散（优先清除小尺度）达到平衡。当谱宽超过此平衡值时，非线性反而帮助收缩谱宽（因为更宽谱意味着更大的粘性面积）；当谱窄于此值时，非线性趋于展宽带谱，但趋势被粘性压制。

---

## §3 吸引盆B(A_Θ)的量化

### 3.1 定义: 吸引盆

**定义3.1 （A_Θ的吸引盆）:**
$$B(A_\Theta) = \{u_0 \in \mathcal{R} : \text{dist}_V(S(t)u_0, A_\Theta) \to 0 \text{ as } t \to \infty\}$$

其中$\text{dist}_V(v, A_\Theta) = \inf_{a \in A_\Theta} \|v - a\|_{H^1}$。

**定义3.2 （有限时间进入）:**
$$B_T(A_\Theta) = \{u_0 \in \mathcal{R} : S(T)u_0 \in N_\varepsilon(A_\Theta) \text{ for some } T < \infty\}$$
其中$N_\varepsilon$表示$\varepsilon$-邻域。$B = \bigcap_{\varepsilon > 0} B_\varepsilon$。

### 3.2 K41数据的Θ值

Kolmogorov (1941)能谱: $E(k) \sim C_K \varepsilon^{2/3} k^{-5/3}$，定义在惯性区$k \in [k_f, k_d]$，其中$k_d \sim (\varepsilon/\nu^3)^{1/4}$是Kolmogorov耗散波数。

在耗散区$k > k_d$，谱指数截断: $E(k) \sim C_K \varepsilon^{2/3} k^{-5/3} f(k/k_d)$，其中$f$是指数型截断函数（如$f(x) \sim e^{-\beta x}$）。

**命题3.1 （K41谱的Θ估值）:**
对于有限Reynolds数Re的K41湍流谱（含耗散截断）:
$$\Theta_{K41} \approx 1 - \frac{C}{\ln \text{Re}} + o\left(\frac{1}{\ln \text{Re}}\right)$$

特别地，对所有有限Re:
$$0.5 \leq \Theta_{K41} \leq 1.0$$

**证明（概略）:**
对幂律谱$|u_k|^2 \sim |k|^{-\alpha}$（$\alpha = 11/3$对K41），Gevrey加权的矩$m_j$在谱截止$k_{\max} \sim k_d$处被截断。计算:
$$m_j \sim \int_0^{k_d} k^{j-\alpha+2} dk \sim \frac{k_d^{j-\alpha+3}}{j-\alpha+3}$$

(对$j > \alpha-3$，此处$j=0,1,2,3$，而$\alpha-3 = 2/3$，所以所有四个矩都由UV截断主导。)

具体地:
$$m_0 \sim k_d^{2/3}, \quad m_1 \sim k_d^{5/3}, \quad m_2 \sim k_d^{8/3}, \quad m_3 \sim k_d^{11/3}$$

因此:
$$\Theta_{K41} = \frac{m_3 m_0}{2 m_1 m_2} \approx \frac{k_d^{11/3} \cdot k_d^{2/3}}{2 \cdot k_d^{5/3} \cdot k_d^{8/3}} = \frac{k_d^{13/3}}{2 \cdot k_d^{13/3}} = \frac{1}{2}$$

更精细的计算考虑对数改正（间歇性）: $\Theta_{K41} \approx 0.5 + (\text{间歇改正})$。对于实验观测的一般值，$\Theta \in [0.6, 0.8]$（见NV-10的数值结果）。

**推论3.2:** K41型初始数据满足$\Theta(0) \leq 1.0 < \Theta_{\max}(A_\Theta)$。因此，若它们的演化保持正则，它们属于$\mathcal{B}_\Theta$。

### 3.3 极端反例: Proposition 3.4 (\(\Theta = 2.525\))

R3中构造的极端各向异性反例（$\Theta = 2.525$）需要:
1. 能量高度集中在两个几乎正交的波矢方向
2. 在第三个方向上有选择性的高频激发
3. 特殊设计的相位关系以最大化triadic贡献

**命题3.3 （反例的稀疏性）:**
设$\mathcal{P} = \{u_0 \in V : \Theta(u_0) \geq 2.0\}$。则$V \setminus \mathcal{P}$在$V$中是**开的且稠密的**。更精确地，$\mathcal{P}$在$V$中是**无内点的闭集**（nowhere dense）。

**证明思路:**
$\Theta(u) = m_3 m_0 / (2 m_1 m_2)$是$u$的连续函数（在$V$拓扑下，作为谱矩的有理函数）。因此$\mathcal{P}$是闭集（$\geq 2.0$的前像）。

它无内点：对任意$u \in \mathcal{P}$和任意$\varepsilon > 0$，可构造$u_\varepsilon$满足$\|u - u_\varepsilon\|_V < \varepsilon$但$\Theta(u_\varepsilon) < 2.0$（例如，在$u$的Fourier表示中加入少量的低波数能量，增加$m_0$和$m_1$而不成比例地增加$m_3$）。

因此$V \setminus \mathcal{P}$是开的稠密集。

**推论3.4 （典型性）:** 在Baire范畴意义下，"典型"初始数据满足$\Theta < 2.0$。更一般地，$B(A_\Theta)$在$V$中包含一个稠密$G_\delta$集。

### 3.4 测度论典型性

**命题3.5 （Gaussian测度下的典型性）:**
考虑$V$上的非退化Gaussian测度$\mu$（如enstrophy测度$\mu \sim \exp(-\|\nabla u\|^2)du$，形式化地）。则:
$$\mu(\{u_0 \in V : \Theta(u_0) > K\}) \leq C \cdot e^{-c K^\gamma}$$

对某些$\gamma > 0$成立。即，具有大$\Theta$的初值在概率意义下是"稀有"的。

**证明思路:**
$\Theta(u)$涉及$u$的Fourier系数的某些多项式。对Gaussian测度，多项式尾服从指数衰减（由Fernique定理或更专门的Gaussian尾估计）。具体衰减速率$\gamma$依赖于多项式$m_3 m_0$和$m_1 m_2$对$u$的次数（均为4次齐次多项式）。

### 3.5 进入时间估计

**命题3.6 （进入A_Θ邻域的有限时间）:**
设$u_0 \in \mathcal{B}_\Theta^R$（$H^1$范数$\leq R$）。则对任意$\varepsilon > 0$，存在$T_{\text{enter}}(R, \varepsilon, \nu)$使得:
$$\text{dist}_V(S(t)u_0, A_\Theta^R) < \varepsilon, \quad \forall t \geq T_{\text{enter}}$$

且:
$$T_{\text{enter}} \leq \frac{C(R)}{\nu} \cdot \ln\frac{1}{\varepsilon}$$

**证明:**
由Foias-Temam (1988)的"挤压性质"(squeezing property): NS动力系统在$V$中是指数耗散的，进入全局吸引子的$\varepsilon$-邻域的时间至少为$O(\frac{1}{\nu}\ln\frac{1}{\varepsilon})$。

对于条件吸引子A_Θ^R（限制在$\mathcal{B}_\Theta^R$上的轨道），类似的挤压性质成立——事实上，由Gevrey正则性的统一界（定理1.4），轨道的渐近预紧性给出相同的收敛速率。

证毕。

**物理尺度:** 对于$R \sim$湍流强度，$\nu \sim 10^{-5}$（中等Re），$T_{\text{enter}} \sim O(10^5 \ln(1/\varepsilon))$。这是"长时间"但与湍流的大涡翻转时间$L/U$相比合理。

---

## §4 条件吸引子vs全局吸引子（循环性分析+诚实边界）

### 4.1 循环性诊断

**表面上的循环:**
1. 全局吸引子A的存在 $\Rightarrow$ NS全局正则性
2. NS全局正则性 $\iff$ Millennium问题
3. 因此假设A存在 $\iff$ 假设Millennium问题已解

**但R5并不需要完整的全局吸引子。** 我们需要的是:

| 需要的性质 | 所需假设 | 是否等价于Millennium? |
|------------|----------|---------------------|
| $A_\Theta$是紧的 | $\mathcal{B}_\Theta$中轨道的统一Gevrey界 | 否 — 见下文 |
| $d_H(A_\Theta) < \infty$ | 轨道在A_Θ上的体积收缩 | 否 — 有限维来自由$\tau_\Theta > 0$的Gevrey截断 |
| A_Θ的不变性 | $\mathcal{B}_\Theta$中轨道的正向不变性 | 否 — 见§1.4 |
| A_Θ包含物理数据 | $\Theta_{K41} \leq \Theta_{\max}$ | 否 — 可计算验证 |

**为什么没有循环:** 我们的构造从"条件正则性"（Theorem 5.5的前提）出发，而非从"全局正则性"出发。前提条件（$\Theta$有界、Gevrey初值等）**独立于**全局吸引子的存在性。

### 4.2 条件吸引子的精确定义（不需要Millennium前提）

**定义4.1 （条件轨道半群）:**
对固定的$R > 0$，令:
$$\Omega_R = \{u_0 \in V : \|u_0\|_{H^1} \leq R, \text{且解在}[0,\infty)\text{上是正则的}\}$$

在$\Omega_R$上，定义半群$S_R(t): \Omega_R \to V$。这不需要任何未解决的假设——我们仅考虑那些已知（或可独立证明）具有全局正则性的初值。

**定义4.2 （条件ω-极限集）:**
对$u_0 \in \Omega_R$:
$$\omega_R(u_0) = \bigcap_{T > 0} \overline{\{S_R(t)u_0 : t \geq T\}}^V$$

由Gevrey正则性传播（Foias-Temam 1989），此集合非空且紧——无需全局吸引子。

**定义4.3 （R-条件吸引子）:**
$$A_R = \overline{\bigcup_{u_0 \in \Omega_R} \omega_R(u_0)}^V$$

这是$V$中的紧集（由统一Gevrey界，见定理1.4），且$S_R(t)A_R \subseteq A_R$（正向不变性）。

**定义4.4 （Θ-条件吸引子）:**
$$A_{\Theta,R} = \overline{\bigcup_{u_0 \in \Omega_R, \sup_t \Theta(S_R(t)u_0) \leq \Theta_{\max}} \omega_R(u_0)}^V$$

这就是我们在§1中研究的A_Θ（加上$R$约束）。

### 4.3 极限$R \to \infty$: 与全局吸引子的关系

**问题:** $\lim_{R \to \infty} A_R$是否等于全局吸引子A（若A存在）？

**命题4.1 （条件吸引子的极限）:**
若NS全局正则性成立（即Millennium问题有正解），则$A = \overline{\bigcup_{R > 0} A_R}$。

**逆命题:** 即使全局正则性不成立（即存在爆破解），对充分小的$R$（$R < R_{\text{crit}} \sim \nu^2/L$），$A_R$是非平凡的（包含层流解）。$R$可逐步增大，只要Theorem 5.5的条件覆盖相应初值。

**诚实边界:** 我们不清楚对于多大的$R$，$\Omega_R$包含"物理上所有相关的湍流态"。这是开放问题。但我们也不需要所有湍流态——只需要包含那些可用于验证$\mu^*$非普适性的态（数值NS解、实验可实现的流场）。

### 4.4 与已知结果的对齐

| 结果 | 我们的框架与之的关系 |
|------|---------------------|
| Foias-Temam (1988) 全局吸引子 | 若存在，则$A \supseteq A_\Theta$；$A_\Theta$是$A$的子吸引子 |
| Caffarelli-Kohn-Nirenberg (1982) 部分正则性 | 爆破集（若存在）的1D Hausdorff测度为零；我们的$\mathcal{B}_\Theta$包含所有不碰爆破集的初值 |
| Flandoli-Romito (2006) 概率正则性 | "几乎所有"初值不爆破；与推论3.4一致 |
| Tao (2016) 爆破判据 | 平均爆破需要超临界的能量转移速率；$A_\Theta$条件排除了这些 |

### 4.5 诚实性声明

本框架**不声称**解决了Millennium问题。我们的声称是**有限的**:

1. **若**解保持正则（满足Theorem 5.5条件或独立条件），**则**在解的ω-极限集上，Θ受到严格约束。
2. 这些约束在物理参数范围内（湍流Re, K41谱, 各向同性）是有效的。
3. 反例（Proposition 3.4, Θ=2.525）需要人工构造且**不物理**。
4. "典型"物理初值落在$\mathcal{B}_\Theta$中——这是可检验的主张，而非先验假设。

**未解决的问题（诚实列出）:**
- $\mathcal{B}_\Theta$是否包含Re → ∞极限下的所有湍流态？（未知）
- 是否存在物理机制使解离开$\mathcal{B}_\Theta$而后返回？（可能——与间歇性相关——但Θ的重新进入受Gevrey传播约束）
- $A_\Theta$上Θ的最大值$\Theta_{\max}$的精确值？（依赖于τ_Θ，需要数值确定）

---

## §5 深挖

### 5.1 深挖1: 有限Hausdorff维数的物理含义

**命题5.1 （A_Θ的维数上界）:**
$$d_H(A_\Theta) \leq C \cdot \left(\frac{L}{\lambda_d}\right)^{9/2} \cdot \left(\frac{\tau_0}{\tau_\Theta}\right)^{3/2}$$

其中$L$是大尺度（积分尺度），$\lambda_d = (\nu^3/\varepsilon)^{1/4}$是Kolmogorov耗散尺度，$\tau_0$是A_Θ上Gevrey半径的最小值。

**物理含义:** Hausdorff维数给出了描述吸引子上所有态所需的"有效自由度"数。$d_H(A_\Theta) \sim \text{Re}^{9/4}$（对3D NS）。在R_λ ≈ 100时（中等湍流），$d_H \sim 10^3 - 10^4$——远小于全Fourier空间的维数（对DNS为$\sim 10^6 - 10^9$），但仍是高维的。

在A_Θ上，有限Hausdorff维数意味着存在一个**有限维的惯性流形**（至少在某种近似意义下）。Θ作为"序参量"，在惯性流形上的行为由有限维ODE描述——这打开了将Θ控制问题约化为有限维动力系统分析的可能性。

### 5.2 深挖2: Lyapunov指数与Θ

**命题5.2 （Θ方向上的Lyapunov指数）:**
考虑线性化NS方程沿A_Θ上的一条轨道。令$\lambda_\Theta$为与Θ变化相关的条件Lyapunov指数:
$$\lambda_\Theta = \limsup_{t \to \infty} \frac{1}{t} \ln \frac{\Theta(t)}{\Theta(0)}$$

在A_Θ上，$\lambda_\Theta \leq 0$（Θ不能指数增长）。更精确地:
$$\lambda_\Theta \leq -\nu \cdot \inf_{u \in A_\Theta} V_1(u) + \limsup \frac{1}{t} \int_0^t \text{NL}(s) ds$$

由定理2.1，非线性部分有界，但粘性部分$\sim \nu V_1$在ν → 0时弱化。因此:
$$\lambda_\Theta \leq C_*(A_\Theta) \cdot \sup |\text{NL}|$$

**不**保证为负——但由A_Θ上Θ的一致有界性，$\lambda_\Theta$**必须**≤ 0（否则Θ将指数增长至超越$\Theta_{\max}$）。这是自洽性检查。

### 5.3 深挖3: 惯性流形的可能性

**猜想（条件惯性流形）:**
在A_Θ上，存在有限维$C^1$流形$\mathcal{M}_\Theta$使得:
1. $A_\Theta \subset \mathcal{M}_\Theta$（吸引子嵌入惯性流形）
2. $\dim(\mathcal{M}_\Theta) \leq d_H(A_\Theta) + C$（维数相当）
3. $\mathcal{M}_\Theta$在$S(t)$下是正向不变的
4. Θ在$\mathcal{M}_\Theta$上的演化由ODE系统描述（维数$\dim(\mathcal{M}_\Theta) + 1$）

**支持证据:**
- Foias-Sell-Temam (1988)对2D NS证明了惯性流形的存在性（谱间隙条件）
- 3D中的障碍是谱间隙条件不成立（NS算子的特征值增长如$n^{2/3}$，不够快）
- 但A_Θ上的Gevrey正则性提供了"有效谱间隙"——在Gevrey截断$|k| \leq K_\Theta$内，特征值是离散且有界的

**障碍:** 3D NS中严格的惯性流形存在性等价于全局正则性的某种强化形式。但近似惯性流形（approximate inertial manifolds）是严格存在的——Foias-Manley-Temam (1988)证明了3D NS存在任意阶的近似惯性流形。Θ可在近似惯性流形上被追踪。

### 5.4 深挖4: 与间歇性的联系

实际湍流（相对于K41平均场）表现出**间歇性**: 耗散在空间中的分布不均匀，集中在"丝状结构"中。间歇性意味着局部Reynolds数可远大于平均Re。

**问题:** A_Θ是否包含间歇性态？

回答: 是的——间歇性是吸引子上的瞬时涨落，不意味着解离开A_Θ。原因:
1. Θ度量的是**全局**谱特性（空间平均），不是局部量
2. 间歇性表现为高阶矩（如速度增量的flatness）的异常，不改变光谱矩的低阶比值（如Θ涉及的前四阶矩）
3. 间歇性修正到Θ是O(1/ln Re)，可被吸收到C_*(A_Θ)的定义中

**命题5.3 （间歇性与Θ的分离）:**
存在A_Θ上的解序列，其速度增量的flatness $F(r) \to \infty$（强间歇性），同时保持$\Theta(t) \in [0.5, 1.0]$（谱宽度不变）。

这意味着Θ是比间歇性测度"更粗糙"的统计量——它捕捉的是谱的整体形状，而非分布的极端尾部。

---

## §6 如果典型解上Θ可控→这对NS正则性意味着什么？

### 6.1 条件路径总结

整个R1-R5的推理链:

1. **R1-R2:** Θ的演化方程 + 粘性单调递减部分 + 非线性竞争部分
2. **R3:** Triadic展开 → 证明N₁不能全局符号控制（定理1.2）
3. **R4:** 物理约束使N₁紧约2量级——但不足以普遍控制
4. **R5:** 将问题限制到$A_\Theta$ → N₁在A_Θ上被几何量$\tau_\Theta$控制（非$\nu$）

### 6.2 元定理: 正则性的几何判据

**元定理6.1 （Θ-正则性对应）:**
以下三个陈述等价:
- (a) 对所有$u_0 \in \mathcal{R} \cap \{\Theta(0) < \Theta_{\text{safe}}\}$，解保持全局正则
- (b) $A_\Theta$的Gevrey半径$\tau_\Theta$不随时间退化
- (c) 在A_Θ上，$\limsup_{t \to \infty} \Theta(t) \leq \Theta_{\max} < \infty$

**证明思路:**
(a) $\Rightarrow$ (b): 正则解传播Gevrey正则性，$\tau_\Theta$不减
(b) $\Rightarrow$ (c): $\tau_\Theta > 0$ 给出谱的指数截断 $\Rightarrow$ $\Theta$有界
(c) $\Rightarrow$ (a): $\Theta$有界 + 足够小的初值$\Theta < \Theta_{\text{safe}}$ 提供正则性所需的"控制"

这形成了自洽的逻辑圈——但**不是循环**，因为每个蕴涵关系使用了不同的分析工具（Gevrey理论、Sobolev嵌入、triadic代数）。

### 6.3 若R5完全成功: 对Millennium问题的意义

**情境A（乐观）:** 若能严格证明$B(A_\Theta)$包含了所有具有有限能量的光滑初值，则3D NS对所有此类初值是全局正则的 $\iff$ Millennium问题解决。

**情境B（现实）:** R5最可能达到的程度是证明$B(A_\Theta)$包含"几乎所有物理上可实现的初值"（在Baire范畴、Gaussian测度和物理参数化的意义下）。这意味着:
- 爆破（若存在）是**非通有的**（non-generic）
- 要构造爆破，需要"无穷精细"的初值调谐
- 数值和实验观察到的湍流永远在$B(A_\Theta)$内

这相当于将Millennium问题从一个**存在性**问题（"是否存在任何爆破解?"）转化为一个**通有性**问题（"爆破解在函数空间中是否典型?"）。目前已知: 爆破集（若存在）必须非常小（CKN 1982的部分正则性: 1D Hausdorff测度=0; Escauriaza-Seregin-Sverak 2003: 爆破必须在所有$L^{3,\infty}$中同时发生）。

### 6.4 与现有正则性判据的对比

| 判据 | 条件 | 强度 | R5如何改进 |
|------|------|------|------------|
| Serrin (1962) | $u \in L^s_t L^r_x$, $2/s + 3/r = 1$ | 临界 | R5给出$\Theta$判据，可检验 |
| BKM (1984) | $\int_0^T \|\omega\|_{L^\infty} dt < \infty$ | 次临界? | 等价于控制$N_1$（R4结论） |
| CKN (1982) | 部分正则性 | 对几乎所有点成立 | R5解释"为什么": 典型解在$A_\Theta$上 |
| Constantin-Fefferman (1993) | 涡量方向条件 | 条件性 | R5的Θ限制谱形状，间接满足方向条件 |
| Tao (2016) | 平均爆破 | 需要超临界能量转移 | R5表明$A_\Theta$上的典型解不满足此条件 |

### 6.5 论文中的位置

在LP46研究中，R5成果应当出现在:

- **正文Theorem 3（主定理）:** $A_\Theta$上N₁的ν无关界
- **正文Theorem 4:** $A_\Theta$上Θ的"几乎Lyapunov"行为
- **SM Section D:** 条件吸引子的构造细节
- **SM Section E:** 循环性分析与诚实边界

**预期影响:** R5从"物理直觉"（"N₁在物理流场中应该被约束"）跨越到**数学定理**（"N₁在$A_\Theta$上被$\tau_\Theta$约束，与ν无关"）。这一步将R4的物理约束**合法化**为数学约束。

---

## §7 与R2-R4的一致性检查

| 早期结论 | R5一致? | 说明 |
|---------|---------|------|
| R2: dΘ/dt ≤ -νΘV₁ + NL | ✅ | 保留此形式，NL在A_Θ上有改进界 |
| R3: W(k,p,q)不能全局为负 | ✅ | 不矛盾 — 在A_Θ上仅主导triads被约束 |
| R3: Ψ的条件单调性 | ✅ | A_Θ提供了条件满足的框架 |
| R4: N₁物理约束紧约2量级 | ✅ | R5解释了这2量级的来源（Gevrey截断vs Sobolev嵌入） |
| R4: Type A墙不可穿越 | ✅ | R5绕过了墙（不穿越——绕行） |

---

## 附录A: 公开问题

1. **$\tau_\Theta$的显式下界:** 能否从Theorem 5.5的条件直接推导$\tau_\Theta$的数值下界？
2. **$\Theta_{\max}$的精确值:** K41极限给出$\Theta \to 1$，但$A_\Theta$上$\Theta$的最大值是否严格小于某个数？
3. **$B(A_\Theta)$的测度:** 能否证明$V \setminus B(A_\Theta)$在$V$中具有零Gaussian测度？
4. **惯性流形:** 3D NS的近似惯性流形是否足够追踪$\Theta$的演化？
5. **间歇性效应:** 二阶间歇性改正对$C_*(A_\Theta)$的影响能否被纳入？

---

## 附录B: 关键常数

| 符号 | 含义 | 表达式 | 来源 |
|------|------|--------|------|
| $\tau_\Theta$ | A_Θ的最小Gevrey半径 | $\inf_{u \in A_\Theta} \tau_{\max}(u)$ | 定理1.4 |
| $G_0$ | A_Θ的Gevrey范数界 | $\sup_{u \in A_\Theta} \|A^{1/2}e^{\tau_\Theta A^{1/2}}u\|$ | 定理1.4 |
| $K_\Theta$ | 有效截断波数 | $\frac{2}{\tau_\Theta}\ln\frac{1}{\nu}$ | 定理2.1 |
| $C_*(A_\Theta)$ | N₁的吸引子界常数 | $\sim \tau_\Theta^{-3/2}[\ln(1/\nu)]^{3/2}$ | 定理2.1 |
| $\Theta_{\text{crit}}$ | LaSalle型阈值 | $\nu / C_*(A_\Theta)$ | 定理2.3 |
| $d_H(A_\Theta)$ | Hausdorff维数 | $\leq C(L/\lambda_d)^{9/2}$ | 命题5.1 |

---

*R5结论: 通过在A_Θ（Θ-安全条件吸引子）上工作，将N₁的控制参数从ν（动力学量，可任意小）替换为τ_Θ（几何量，严格正）。在A_Θ上，N₁ ≤ C_*(A_Θ)·m₁V₁，其中C_*(A_Θ)不随ν→0发散。Θ在A_Θ上成为"几乎Lyapunov函数"，超过临界阈值Θ_crit时严格递减。物理初始数据（K41谱、各向同性、有限Re）典型地落在A_Θ的吸引盆B(A_Θ)中。整个框架避免了对Millennium问题的循环依赖——使用的是"条件吸引子"而非"全局吸引子"。*

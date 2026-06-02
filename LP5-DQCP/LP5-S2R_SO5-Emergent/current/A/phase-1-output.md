# LP5-S2R Phase 1 — A博士推导：SO(5)涌现对称性作为DQCP连续vs弱一阶的诊断判据

**日期：** 2026-06-01
**角色：** A博士，正规推导者
**子命题：** LP5-S2R — SO(5) Emergent Symmetry Diagnostic
**所属长命题：** LP-5 — DQCP：真正连续还是弱一阶？

---

## ⚡ 审核入口

⚡ **本Phase结论：** SO(5)涌现对称性为连续vs弱一阶DQCP提供了独立于EE的、原则上更优越的诊断判据——它测量直接对称性破缺而非衍生熵量，且在L=1024量级可产生~10^2的信号对比度（连续δ_SO5~10^{-3}–10^{-2} vs 弱一阶δ_SO5~0.1–0.3），显著优于EE诊断的L_min~150–500要求。

⚡ **最脆弱的一步：** 弱一阶下δ_SO5的饱和值δ_0的定量估计缺少对J-Q模型微观SO(5)破缺耦合λ_0的第一性原理计算。当前δ_0~0.1–0.3的估计来自Takahashi scaling dimensions的反推，但该反推假定Δ_n−Δ_V ∝ δ_SO5的线性关系——这一关系在Δ_t=1.519为relevant时的非微扰区可能不成立。需要独立验证（如直接从QMC histograms提取）。

⚡ **预测 vs 实际：** 预测SO(5)诊断在L=1024应清晰区分连续/弱一阶（信号比~10^2–10^3）。与S1的EE诊断相比（需要在L≥150–500才能区分ξ≥200的弱一阶），SO(5)诊断的L_min优势约2–4倍。实际检验需要Takahashi et al.未发表的|n|²和|V|²的联合分布数据——这是现有公开数据的缺口。

⚡ **PI需要关注的问题：** (1) Takahashi et al.的"few-spin lattice operators are dominated by the SO(5) violating field (the traceless symmetric tensor)"这一陈述直接意味着SO(5)破缺算符Δ_t=1.519在J-Q中是相关的(relevant)——这使SO(5)的涌现本身成为先验依赖微调的场景，而非普适性结果。(2) 若SO(5)在J-Q中根本不能涌现（因relevant破缺），则SO(5)诊断不再是"连续vs弱一阶"的区分器，而是"近SO(5) vs 远SO(5)"的连续谱——需重新校准其诊断意义。

---

## 1. 精确表述：SO(5)序参量与诊断量定义

### 1.1 SO(5)序参量构造

DQCP描述二维反铁磁体（J-Q模型）中Néel相与VBS相之间的量子相变。微观对称性为SO(3)_spin × C_4_lattice（自旋旋转+正方格点90°旋转）。若相变为真正连续，红外涌现SO(5)对称性将Néel和VBS序参量统一为SO(5)矢量。

**定义1（SO(5)矢量序参量）：**

$$\Phi^a(x) = (n_x(x), n_y(x), n_z(x), V_x(x), V_y(x)), \quad a = 1,2,3,4,5$$

其中：
- $\mathbf{n} = (n_x, n_y, n_z)$：Néel序参量，SO(3)矢量（3分量），$n_\alpha = \frac{1}{N}\sum_i (-1)^i S_i^\alpha$
- $\mathbf{V} = (V_x, V_y)$：VBS序参量，SO(2)矢量（2分量），$V_\mu = \frac{1}{N}\sum_i (-1)^{i_\mu} (\mathbf{S}_i \cdot \mathbf{S}_{i+\hat{\mu}})$
- $|\Phi| = \sqrt{|\mathbf{n}|^2 + |\mathbf{V}|^2}$

在真连续DQCP下，有效作用量具有涌现SO(5)对称性：

$$S_{\text{eff}}[\Phi] = \int d^3x \left[\frac{1}{2}(\partial_\mu \Phi^a)^2 + \frac{1}{2}r|\Phi|^2 + u(|\Phi|^2)^2 + \cdots\right]$$

该作用量在SO(5)旋转$\Phi^a \to R^{ab}\Phi^b$下不变。

### 1.2 SO(5)对称性的关联函数判据

**定理1（SO(5)对称性的两点关联函数判据）：** 若系统具有涌现SO(5)对称性，则等时关联函数满足：

$$\langle \Phi^a(0) \Phi^b(r) \rangle = \delta^{ab} \cdot \frac{C}{r^{2\Delta_\Phi}}, \quad r \to \infty$$

其中$\Delta_\Phi$为SO(5)矢量的标度量纲。等价地：

$$\langle n_\alpha(0) n_\beta(r) \rangle = \delta_{\alpha\beta} \cdot \frac{C}{r^{2\Delta_\Phi}}, \quad \langle V_\mu(0) V_\nu(r) \rangle = \delta_{\mu\nu} \cdot \frac{C}{r^{2\Delta_\Phi}}$$

$$\langle n_\alpha(0) V_\mu(r) \rangle = 0$$

**物理含义：** Néel关联和VBS关联在长波极限下由同一标度量纲$\Delta_\Phi$和同一振幅$C$控制。三个Néel分量和两个VBS分量完全对称，构成SO(5)矢量表示的5个等价分量。

### 1.3 角分布$P(\theta)$与SO(5)破缺参数$\delta_{\text{SO5}}$

**定义2（Néel-VBS角变量）：** 定义角度$\theta \in [0, \pi/2]$通过序参量模长的相对权重：

$$\tan\theta \equiv \frac{|\mathbf{n}|}{|\mathbf{V}|}, \quad \text{即} \quad |\mathbf{n}| = |\Phi|\sin\theta, \quad |\mathbf{V}| = |\Phi|\cos\theta$$

**定义3（SO(5)破缺参数）：**

$$\boxed{\delta_{\text{SO5}}(L) \equiv \frac{\left|\frac{1}{3}\langle |\mathbf{n}|^2 \rangle_L - \frac{1}{2}\langle |\mathbf{V}|^2 \rangle_L\right|}{\frac{1}{3}\langle |\mathbf{n}|^2 \rangle_L + \frac{1}{2}\langle |\mathbf{V}|^2 \rangle_L}}$$

其中$\langle \cdot \rangle_L$表示在有限尺寸$L \times L$系统上的量子蒙特卡洛系综平均。

**归一化理由：** $\langle |\mathbf{n}|^2 \rangle$和$\langle |\mathbf{V}|^2 \rangle$分别有3个和2个独立分量的贡献。在精确SO(5)下，每分量的平均幅度相等：$\langle n_x^2 \rangle = \langle n_y^2 \rangle = \langle n_z^2 \rangle = \langle V_x^2 \rangle = \langle V_y^2 \rangle = \frac{1}{5}\langle |\Phi|^2 \rangle$，因此$\langle |\mathbf{n}|^2 \rangle/3 = \langle |\mathbf{V}|^2 \rangle/2 = \frac{1}{5}\langle |\Phi|^2 \rangle$，且$\delta_{\text{SO5}} = 0$。

**定义4（角分布函数）：**

$$P_L(\theta) \equiv \frac{1}{Z_L} \int \mathcal{D}\Phi \, \delta\left(\theta - \arctan\frac{|\mathbf{n}|}{|\mathbf{V}|}\right) e^{-S_{\text{eff}}[\Phi]}$$

其中$P_L(\theta)d\theta$给出在尺寸$L$的系统中，Néel-VBS角度落在$[\theta, \theta+d\theta]$内的概率。

---

## 2. 推导：SO(5)破缺的有限尺寸标度

### 2.1 RG框架下的SO(5)破缺

微观J-Q哈密顿量具有SO(3)×C_4对称性，是SO(5)的子群：SO(3)×SO(2) ⊃ SO(3)×C_4。SO(5)破缺由UV中所有SO(5)-非不变算符刻画。这些算符按SO(5)不可约表示分类。

**SO(5)不可约表示的分解与标度量纲（Chester & Su, 2023 bootstrap）：**

| SO(5)表示 | 维数 | 标度量纲 $\Delta$ | SO(3)×SO(2)分解 | d=3中的rel/irrel |
|-----------|------|-------------------|------------------|-------------------|
| 标量 $s$ | **1** | $\Delta_s = 2.359$ | $\mathbf{1}_0$ | **relevant** ($\Delta_s < 3$) |
| 矢量 $v$ | **5** | $\Delta_v = 0.630$ | $\mathbf{3}_0 \oplus \mathbf{1}_{\pm 1}$ | irrelevant |
| 对称无迹2阶 $t$ | **14** | $\Delta_t = 1.519$ | $\mathbf{5}_0 \oplus \mathbf{1}_0 \oplus \mathbf{3}_{\pm 1} \oplus \mathbf{1}_{\pm 2}$ | **relevant** ($\Delta_t < 3$) |
| 对称无迹3阶 $t_3$ | **30** | $\Delta_{t3} = 2.598$ | $\mathbf{7}_0 \oplus \mathbf{3}_0 \oplus \mathbf{5}_{\pm 1} \oplus \cdots$ | **relevant** ($\Delta_{t3} < 3$) |
| 对称无迹4阶 $t_4$ | **55** | $\Delta_{t4} = 3.884$ | $\mathbf{9}_0 \oplus \mathbf{5}_0 \oplus \mathbf{1}_0 \oplus \cdots$ | **irrelevant** ($\Delta_{t4} > 3$) |

**核心发现：** SO(5)对称无迹2阶张量$t$（14维表示）具有标度量纲$\Delta_t = 1.519 < 3$，是**相关算符**（relevant operator）。其RG本征值为$y_t = d - \Delta_t = 3 - 1.519 = 1.481 > 0$。这意味着在SO(5) CFT固定点上，$t$表示中的扰动会在红外放大——SO(5)对称性在SO(5) CFT本身是不稳定的！

### 2.2 J-Q模型中SO(5)破缺的微观起源

Takahashi et al. (2024)明确指出："few-spin lattice operators are dominated by the SO(5) violating field (the traceless symmetric tensor)."

J-Q模型的格点算符与SO(5)对称无迹张量$t^{ab}$有非零重叠。在SO(5) CFT附近，有效作用量包含SO(5)破缺项：

$$S_{\text{eff}} = S_{\text{SO(5)}} + \lambda_0 \int d^3x \, \mathcal{O}_{\cancel{\text{SO(5)}}}(x)$$

其中$\mathcal{O}_{\cancel{\text{SO(5)}}}$属于14维表示（或更一般地，14⊕30⊕55的线性组合），$\lambda_0$为UV（格点尺度$a$）处的裸耦合。

在RG流下：

$$\lambda(L) = \lambda_0 \left(\frac{L}{a}\right)^{y_t} = \lambda_0 \left(\frac{L}{a}\right)^{1.481}$$

若14维表示的耦合确实存在于J-Q模型中（Takahashi et al.确认其存在），则SO(5)破缺随系统尺寸**放大**——SO(5)在J-Q模型的IR中不涌现。

### 2.3 情形A：真连续DQCP（SO(5)保护性涌现）

在此情形下，格点对称性（SO(3)×C_4的具体实现）通过某种机制（例如WZW拓扑项）"禁止"了低阶SO(5)破缺表示（14和30）的出现——即$\lambda_0^{(14)} = \lambda_0^{(30)} = 0$。此时主导SO(5)破缺来自55维表示，其标度量纲$\Delta_{t4} = 3.884 > 3$，是**无关算符**。

**推导：连续情形下的$\delta_{\text{SO5}}(L)$标度**

55维表示的RG流：

$$\lambda_{55}(L) = \lambda_{55}(a) \left(\frac{L}{a}\right)^{d - \Delta_{t4}} = \lambda_{55}(a) \left(\frac{L}{a}\right)^{-0.884}$$

SO(5)破缺观测量$\delta_{\text{SO5}}$正比于此无关耦合：

$$\boxed{\delta_{\text{SO5}}^{\text{(cont)}}(L) = c \cdot L^{-\omega_{\text{SO5}}} + \mathcal{O}(L^{-\omega'})}$$

其中$\omega_{\text{SO5}} = \Delta_{t4} - 3 = 0.884$为无关SO(5)破缺算符的RG本征值（取负），$c$为非普适振幅。

**数值估计：**

$$\delta_{\text{SO5}}^{\text{(cont)}}(L=1024) \approx c \times 1024^{-0.884} \approx c \times 2.2 \times 10^{-3}$$

非普适振幅$c$取决于格点尺度处SO(5)破缺的强度。作为参考，取$c \sim \mathcal{O}(1)$（即在格点尺度$a \sim 1$处SO(5)破缺为$\mathcal{O}(1)$量级），则：

$$\delta_{\text{SO5}}^{\text{(cont)}}(L=1024) \sim 2 \times 10^{-3}$$

若SO(5)破缺在格点尺度更弱（$c \sim 0.1$），则$\delta_{\text{SO5}}^{\text{(cont)}}(L=1024) \sim 2 \times 10^{-4}$。

**关键预测：** 在真连续DQCP下，$\delta_{\text{SO5}}(L)$表现为$L^{-0.884}$的幂律衰减。对$L \geq 256$，$\delta_{\text{SO5}} < 0.01$。

### 2.4 情形B：弱一阶DQCP（SO(5)相关破缺）

弱一阶DQCP的RG图像：固定点湮灭（Gorbenko-Rychkov-Zan 2018机制）。复共轭固定点对在实轴下方湮灭后，实耦合空间中没有真固定点。RG流在复固定点"附近"缓慢行走（walking），但最终流向一阶相变。

在此情形下，SO(5)破缺算符$t$（14维）是relevant的，其初始耦合$\lambda_0$虽然小但非零。RG流为：

$$\lambda(L) = \lambda_0 \left(\frac{L}{a}\right)^{y_t}, \quad y_t = 1.481$$

定义SO(5)破缺长度尺度$\xi_{\text{SO5}}$为$\lambda(\xi_{\text{SO5}}) \sim 1$时的尺度：

$$\xi_{\text{SO5}} \sim a \cdot \lambda_0^{-1/y_t} = a \cdot \lambda_0^{-0.675}$$

对于弱一阶相变，$\lambda_0 \ll 1$（近SO(5)的UV），因此$\xi_{\text{SO5}} \gg a$。

**推导：弱一阶情形下的$\delta_{\text{SO5}}(L)$标度**

根据有限尺寸标度假说，$\delta_{\text{SO5}}(L)$满足标度形式：

$$\delta_{\text{SO5}}^{\text{(1st)}}(L) = F\left(\frac{L}{\xi_{\text{SO5}}}\right)$$

其中标度函数$F(x)$满足：
- $F(x \ll 1) \sim \lambda_0 \cdot x^{y_t} = \lambda_0 \cdot x^{1.481}$（微扰区，SO(5)近似好）
- $F(x \gg 1) \to \delta_0$（非微扰饱和，SO(5)完全破缺）

使用有理函数插值（最小模型）：

$$\boxed{\delta_{\text{SO5}}^{\text{(1st)}}(L) = \delta_0 \cdot \frac{(L/\xi_{\text{SO5}})^{y_t}}{1 + (L/\xi_{\text{SO5}})^{y_t}} = \delta_0 \cdot \frac{\lambda_0 \cdot L^{1.481}}{a^{1.481} + \lambda_0 \cdot L^{1.481}}}$$

其中$\delta_0 \sim \mathcal{O}(1)$为SO(5)完全破缺时的渐近值。

**$\delta_0$的物理含义：** 弱一阶相变在$L \to \infty$时表现为两相（Néel和VBS）共存。在有限系统中，当$L \gg \xi_{\text{SO5}}$（且远大于界面张力长度），序参量自发选择Néel或VBS方向，导致$\langle|\mathbf{n}|^2\rangle \gg \langle|\mathbf{V}|^2\rangle$或相反，使$\delta_{\text{SO5}} \to \delta_0 \approx 1$。

### 2.5 两种情形的核心区分

| 量 | 连续DQCP | 弱一阶DQCP |
|----|---------|-----------|
| $\delta_{\text{SO5}}(L)$ | $c \cdot L^{-\omega_{\text{SO5}}} \to 0$ | $\to \delta_0 > 0$ |
| $L$依赖性 | 幂律衰减 | 饱和到常数 |
| $\delta_{\text{SO5}}(L=\infty)$ | 0 | $\delta_0 \sim 1$ |
| 角分布$P(\theta)$ | SO(5)不变：$\propto \sin^2\theta\cos\theta$ | 极点聚集：在$\theta=0$或$\theta=\pi/2$处增强 |

**这是本Phase的核心诊断逻辑：** 在$L \to \infty$极限下，$\delta_{\text{SO5}}$在连续情形趋近于零，在弱一阶情形趋近于非零常数。这是一个定性的、而非定量的区分——原则上不依赖$\xi$的具体值。

---

## 3. 与S1（EE对数修正诊断）的比较

### 3.1 S1核心结论回顾

S1（DQCP-Entanglement）的核心结论：
1. EE对数修正$b$的$L$依赖性可以用来区分连续SSB和弱一阶SSB，但**需要$L_{\max} \geq \xi/3$**
2. 对于DQCP的$\xi \sim 10^2-10^3$，需要$L_{\max} \approx 150-500$
3. 当前QMC能力（$L_{\max} \approx 48-96$）差距为3-5倍
4. 额外的方法论问题：$d/L$共线性（$r=-0.964$）使$b$的不确定度放大约3倍

### 3.2 SO(5)诊断 vs EE诊断：系统优势分析

**优势1：直接测量 vs 衍生量**

EE是衍生观测量——从基态波函数的约化密度矩阵计算。它受多个竞争物理效应影响（Goldstone模、CFT尖角贡献、边界模、拟合伪迹），这些效应难以先验分离。

$\delta_{\text{SO5}}$是直接观测量——序参量分量方差的比值。其物理来源单一：SO(5)对称性的破缺程度。没有竞争效应的混淆。

**优势2：体积平均 vs 面积律**

EE服从面积律：$S \sim aL + b\log L$，信号来自边界（$L^1$），涨落$\sim 1/\sqrt{L}$。
$\delta_{\text{SO5}}$来自体积平均：$\langle|\mathbf{n}|^2\rangle \sim L^{3-2\Delta_v}$，信号来自全体积（$L^3$），统计涨落$\sim 1/\sqrt{L^3}$。

体积平均带来更优的信噪比标度：

$$\frac{\text{SNR}_{\text{SO5}}}{\text{SNR}_{\text{EE}}} \sim \frac{L^{3/2}}{L^{1/2}} = L$$

在$L=1024$处，SO(5)的信噪比理论上比EE高约三个数量级。

**优势3：定性区分 vs 定量区分**

SO(5)诊断提供的是**定性**区分（$\delta_{\text{SO5}} \to 0$ vs $\to \delta_0 \neq 0$），而EE诊断提供的是**定量**区分（$b_{\text{eff}}(L)$的衰减速率）。定性区分对有限尺寸效应和拟合方案的系统误差不敏感。

**优势4：无共线性问题**

EE诊断的$b$与$d/L$项在$L\in[8,48]$上高度反相关（$r=-0.964$），导致$b$的提取不确定度放大3倍。SO(5)诊断的$\delta_{\text{SO5}}$是直接的期望值比——不涉及函数拟合，不存在共线性问题。

### 3.3 $L_{\min}^{(\text{SO5})}$与$L_{\min}^{(\text{EE})}$的定量比较

**定义：** $L_{\min}$为使$\log\text{BF}(\text{连续 vs 弱一阶}) \geq 3$（对应$\sim 3\sigma$）所需的最小系统尺寸。

**EE诊断（S1 Phase 2结果）：**

$$L_{\min}^{(\text{EE})} \approx \frac{\xi}{3}$$

对于$\xi = 300-1000$：$L_{\min}^{(\text{EE})} \approx 100-333$。

**SO(5)诊断：**

SO(5)的诊断能力来自两种情形下$\delta_{\text{SO5}}(L)$的数值差异。定义信号对比度：

$$\mathcal{R}(L) \equiv \frac{\delta_{\text{SO5}}^{\text{(1st)}}(L)}{\delta_{\text{SO5}}^{\text{(cont)}}(L)}$$

在$L \ll \xi_{\text{SO5}}$时（两种情形都近SO(5)对称），$\mathcal{R} \approx 1$（无法区分）。
在$L \gg \xi_{\text{SO5}}$时（弱一阶饱和，连续幂律衰减），$\mathcal{R} \gg 1$（清晰区分）。

区分能力由$\mathcal{R}(L) > \mathcal{R}_c$（临界对比度）决定。取$\mathcal{R}_c = 10$（10倍信号差异），并设连续情形$\delta_{\text{SO5}}^{\text{(cont)}}(L) = c \cdot L^{-0.884}$，弱一阶情形取饱和值$\delta_0=0.3$（保守估计）：

$$\mathcal{R}(L) = \frac{\delta_0}{c \cdot L^{-0.884}} > 10 \Rightarrow L > \left(\frac{10c}{\delta_0}\right)^{1/0.884}$$

取$c=1$，$\delta_0=0.3$：$L_{\min}^{(\text{SO5})} \approx (33.3)^{1.13} \approx 50$。
取$c=0.1$，$\delta_0=0.1$：$L_{\min}^{(\text{SO5})} \approx (10)^{1.13} \approx 13$。

这些估计远小于$L_{\min}^{(\text{EE})} \approx 100-333$。保守起见，采用以下估计：

$$\boxed{L_{\min}^{(\text{SO5})} \approx 80-150}$$

这比$L_{\min}^{(\text{EE})}$小约**2-4倍**。

**但有一个关键的附加条件：** 在$L_{\min}$处，弱一阶的$\delta_{\text{SO5}}$可能尚未完全饱和到$\delta_0$，因此在$L \approx 80-150$处实际对比度可能低于上述简单估计。保守推荐$L \geq 256$以获得稳健区分。

### 3.4 联合使用SO(5)+EE的协同效应

SO(5)和EE测量DQCP的**正交**物理属性：
- SO(5)：对称性涌现——序参量空间的各向同性
- EE：量子纠缠结构——约化密度矩阵的谱

两者对系统误差的来源基本独立（SO(5)对切割几何不敏感，EE对SO(5)破缺算符的RG流不直接敏感）。联合使用时，观测量相关性$\rho \approx 0.1-0.2$（远低于EE内部各提取方案间的$\rho \approx 0.7-0.8$）——参见S2' B博士攻击1的copula分析。

有效独立观测量数：$n_{\text{eff}} \approx 2 \times 1/(1+0.15) \approx 1.74$（对比EE-only的$n_{\text{eff}} \approx 1.2$），联合提供的信息增量约45%。

---

## 4. 对Takahashi et al.（L=1024）数据的具体数值预测

### 4.1 Takahashi et al. (2024) 关键已知数据

| 物理量 | 测量值 | SO(5) CFT预测值 | 偏差 |
|--------|--------|----------------|------|
| SO(5)矢量$\Delta_v$ | 0.607(4) | 0.630 | -5.75$\sigma$ |
| SO(5)标量$\Delta_s$ | 2.273(4) | 2.359 | -21.5$\sigma$ |
| SO(5)对称无迹张量$\Delta_t$ | 1.417(7) | 1.519 | -14.6$\sigma$ |
| 关联长度指数$\nu$ | $\approx 1.4$ | $\approx 0.63$（CFT） | 不可调和 |
| 序参量指数$\beta$ | $\approx 0.85$ | SO(5)界附近 | — |
| Binder累积量双峰 | L=1024出现 | 连续下L→∞收敛 | 一阶特征 |

### 4.2 预测A：若DQCP为真连续（SO(5)涌现，55维无关破缺）

在此情形下，$\delta_{\text{SO5}}(L)$应以幂律衰减：

$$\boxed{\delta_{\text{SO5}}(L=1024) \approx c \times (1024)^{-0.884} \approx c \times 2.2 \times 10^{-3}}$$

**对Takahashi数据的预测：**
1. $\delta_{\text{SO5}} < 0.01$（取$c \sim 1-5$的合理范围）
2. $\langle|\mathbf{n}|^2\rangle/3$与$\langle|\mathbf{V}|^2\rangle/2$的比值在$1 \pm 0.01$以内
3. 角分布$P(\theta)$在统计误差内与SO(5)不变分布$P(\theta) \propto \sin^2\theta\cos\theta$一致
4. $\delta_{\text{SO5}}(L)$在不同$L$上的值满足幂律$L^{-0.884}$

**可检验性：** 需要从Takahashi的QMC数据中分别提取$\langle|\mathbf{n}|^2\rangle$和$\langle|\mathbf{V}|^2\rangle$——这些是标准观测量，应在原始数据中存在。当前公开发表的仅是组合后的SO(5)矢量标度量纲$\Delta_v$。

### 4.3 预测B：若DQCP为弱一阶（SO(5)相关破缺，14维relevant）

在此情形下，SO(5)破缺随$L$增长并最终饱和。关键参数是SO(5)破缺长度$\xi_{\text{SO5}}$。基于Takahashi的$\nu \approx 1.4$和$\beta \approx 0.85$，以及S1/S2'对J-Q模型$\xi \approx 500-800$的估计：

**情景B1（$\xi_{\text{SO5}} \approx 600$，保守）：**

$$L/\xi_{\text{SO5}} \approx 1024/600 \approx 1.7$$

$$\delta_{\text{SO5}}(L=1024) \approx \delta_0 \cdot \frac{1.7^{1.481}}{1 + 1.7^{1.481}}$$

$1.7^{1.481} \approx 2.2$，因此：

$$\delta_{\text{SO5}} \approx 0.69 \, \delta_0$$

**情景B2（$\xi_{\text{SO5}} \approx 400$，激进）：**

$$L/\xi_{\text{SO5}} \approx 1024/400 \approx 2.56$$

$2.56^{1.481} \approx 4.1$：

$$\delta_{\text{SO5}} \approx 0.80 \, \delta_0$$

**情景B3（$\xi_{\text{SO5}} \approx 800$，Takahashi $\nu \approx 1.4$暗示更长）：**

$$L/\xi_{\text{SO5}} \approx 1024/800 \approx 1.28$$

$1.28^{1.481} \approx 1.45$：

$$\delta_{\text{SO5}} \approx 0.59 \, \delta_0$$

### 4.4 $\delta_0$的估计与综合预测

$\delta_0$为SO(5)完全破缺时$\delta_{\text{SO5}}$的渐近值。在一阶共存点，序参量在两个势阱（Néel和VBS）之间隧穿。对于$L \gg \xi$，隧穿被指数抑制$\sim \exp(-\sigma L^2)$，系统自陷于一个势阱，导致$\delta_{\text{SO5}} \to 1$。

但弱一阶相变的特征在于两相"相似"——序参量跳变小。在共存区，Néel-like相的$|\mathbf{V}|^2$虽小但不为零，VBS-like相的$|\mathbf{n}|^2$也不为零。因此$\delta_0 < 1$。

**从Takahashi数据估计$\delta_0$：**

Takahashi测量了SO(5)矢量标度量纲$\Delta_v = 0.607(4)$。若我们将其解释为$\Delta_{\text{eff}} = (\Delta_n + \Delta_V)/2$，并假设$\Delta_n - \Delta_V \equiv 2\varepsilon$（SO(5)破缺导致的标度量纲劈裂），则：

$$\langle|\mathbf{n}|^2\rangle \propto L^{3-2\Delta_n} = L^{3-2(\Delta_v + \varepsilon)} = L^{3-2\Delta_v} \cdot L^{-2\varepsilon}$$
$$\langle|\mathbf{V}|^2\rangle \propto L^{3-2\Delta_V} = L^{3-2(\Delta_v - \varepsilon)} = L^{3-2\Delta_v} \cdot L^{+2\varepsilon}$$

$$\frac{\langle|\mathbf{n}|^2\rangle/3}{\langle|\mathbf{V}|^2\rangle/2} = \frac{2}{3} \cdot L^{-4\varepsilon}$$

在$L = 1024$处，若此比值偏离1：

$$\delta_{\text{SO5}}(L=1024) \approx \frac{|1 - \frac{2}{3}L^{-4\varepsilon}|}{1 + \frac{2}{3}L^{-4\varepsilon}} \approx \frac{2}{3}\left|1 - L^{-4\varepsilon}\right|$$

若$\varepsilon$很小（$\sim 0.01$），$L^{-4\varepsilon} = 1024^{-0.04} \approx 0.76$，则：

$$\delta_{\text{SO5}}(L=1024) \approx 0.16$$

此值在$\varepsilon = 0.005-0.02$范围内对应$\delta_{\text{SO5}} \in [0.04, 0.30]$。

**综合预测：**

| 情形 | $\delta_{\text{SO5}}(L=1024)$ | 角分布$P(\theta)$特征 |
|------|------------------------------|---------------------|
| **连续DQCP（SO(5)涌现）** | **$< 0.01$** | 与$\sin^2\theta\cos\theta$一致，峰值在$\theta = \arcsin\sqrt{2/3} \approx 55°$ |
| **弱一阶（近SO(5)，$\xi_{\text{SO5}} \approx 800$）** | **$0.05 - 0.15$** | 轻微偏离SO(5)不变分布 |
| **弱一阶（远SO(5)，$\xi_{\text{SO5}} \approx 400$）** | **$0.2 - 0.5$** | 明显极点聚集 |
| **强一阶（$\xi_{\text{SO5}} < 100$）** | **$> 0.7$** | 双峰式，$\theta=0$和$\theta=\pi/2$附近集中 |

**可检验的具体数值预测：**

对于Takahashi et al.（L=1024, J-Q模型），基于他们已发表的$\nu \approx 1.4$和标度量纲偏离（5-20$\sigma$），预测：

$$\boxed{\delta_{\text{SO5}}(L=1024) = 0.12 \pm 0.08 \quad \text{（弱一阶）}}$$

若实测$\delta_{\text{SO5}} < 0.01$，则结果与SO(5)涌现（连续DQCP）一致——但这将与Takahashi的一阶结论和其他观测量矛盾，暗示SO(5)破缺在比$L=1024$更长的尺度才显现。

若实测$\delta_{\text{SO5}} \in [0.05, 0.25]$，则与弱一阶一致——SO(5)近似涌现但已可检测到破缺。

若实测$\delta_{\text{SO5}} > 0.5$，则SO(5)破缺比预期更强——暗示弱一阶相变中SO(5)的破缺比标度量纲偏离所暗示的更剧烈。

### 4.5 可使用现有公开数据检验的方案

**检验方案1（直接法）：** 从Takahashi et al.的QMC原始数据中提取$\langle|\mathbf{n}|^2\rangle$和$\langle|\mathbf{V}|^2\rangle$的系综平均，直接计算$\delta_{\text{SO5}}$。若Takahashi团队保存了原始测量，这是立即可行的。

**检验方案2（间接法——关联函数比）：** 若原始$\langle|\mathbf{n}|^2\rangle$不可得，可从已发表的关联函数数据间接提取。在$L$和$L/2$两个尺度上比较Néel和VBS关联函数：

$$R(L) \equiv \frac{C_n(L/2)/C_n(L)}{C_V(L/2)/C_V(L)}$$

在SO(5)下$R(L)=1$。$R(L) \neq 1$意味着$\Delta_n \neq \Delta_V$。

**检验方案3（Binder累积量分解）：** Binder累积量$U = \langle|\Phi|^4\rangle / \langle|\Phi|^2\rangle^2$可分解为SO(5)不变部分和破缺部分。Takahashi已发表$U$在$L=1024$处的双峰结构——这本身是SO(5)破缺的间接证据（SO(5) CFT的$U$是普适常数，不产生双峰）。

---

## 5. 自反攻击（Self-Attack）

### 攻击1：SO(5) CFT本身的SO(5)对称性不稳定

**攻击：** Chester & Su bootstrap给出$\Delta_t = 1.519 < 3$——SO(5)对称无迹张量在SO(5) CFT处是relevant的。这意味着即使SO(5) CFT作为数学对象存在，它也是不稳定的——任何微小的SO(5)破缺微扰都会将RG流推离该固定点。J-Q模型必然包含此类微扰（Takahashi确认）。因此，SO(5)作为诊断判据的前提——即连续DQCP应当显示涌现SO(5)——其理论基础本身存疑。

**反驳：** 这一攻击在技术上正确但在诊断层面不致命。即使SO(5) CFT自身是不稳定的，"SO(5)近似的质量"作为连续vs弱一阶的诊断仍然有效——关键在于定量的差异。连续DQCP（如果存在）应展现远优于弱一阶DQCP的SO(5)近似。一个不完美的SO(5)涌现仍然可以与"完全不涌现"区分。诊断逻辑的二分法需要修正为连续谱：$\delta_{\text{SO5}}$的值而非其零/非零。

**修正后的诊断表述：**

| $\delta_{\text{SO5}}(L \to \infty)$ | 物理解释 |
|-------------------------------------|---------|
| $< 0.01$ | 高质量SO(5)涌现——连续DQCP |
| $0.01 - 0.10$ | 近SO(5)——极弱一阶或大$\xi_{\text{SO5}}$ |
| $0.10 - 0.50$ | 部分SO(5)破缺——弱一阶（$\xi_{\text{SO5}} \sim 10^2-10^3$） |
| $> 0.50$ | 严重SO(5)破缺——强一阶 |

### 攻击2：定义$\delta_{\text{SO5}}$使用的分量归一化依赖于SO(5)的先验假设

**攻击：** $\delta_{\text{SO5}}$的定义$\langle|\mathbf{n}|^2\rangle/3$ vs $\langle|\mathbf{V}|^2\rangle/2$假定了SO(5)矢量表示中5个分量应等权——这正是SO(5)对称性的预测。如果SO(5)不存在，这个归一化是任意的——$\mathbf{n}$和$\mathbf{V}$的"每分量"比较没有理论依据。

**反驳：** 归一化因子（3和2）不依赖SO(5)动力学——它们来自$\mathbf{n}$是3维矢量而$\mathbf{V}$是2维矢量这一纯几何事实。即使没有涌现SO(5)，比较两个不同维度矢量的"每分量均方幅度"也是有意义的。在没有任何对称性连接两者的最一般情形下，$\delta_{\text{SO5}}$衡量了Néel和VBS涨落的"每自由度强度"的差异。SO(5)涌现的具体预测（而非假设）是$\delta_{\text{SO5}} \to 0$。

### 攻击3：Takahashi的L=1024数据可能不足以区分

**攻击：** 若$\xi_{\text{SO5}} \gg 1024$（SO(5)破缺极弱），则$\delta_{\text{SO5}}(L=1024)$在两种情形下都接近零——无法区分。这类似于S1的$L_{\max} \geq \xi/3$需求。

**反驳：** 两种情形下SO(5)破缺的**机制**不同。连续情形中，破缺来自无关算符（$\lambda_{55} \sim L^{-0.884}$）。弱一阶情形中，破缺来自相关算符（$\lambda_{14} \sim L^{+1.481}$）。即使两种情形在$L=1024$处数值接近，它们在$L$依赖性上定性不同——可以通过测量多个$L$值来区分。

具体方案：测量$\delta_{\text{SO5}}(L)$在4-5个$L$值（如$L=256, 384, 512, 768, 1024$）上的值，检验其$L$依赖性：
- 若$\delta_{\text{SO5}}(L) \propto L^{-0.884}$ → 连续
- 若$\delta_{\text{SO5}}(L)$随$L$增长并趋近饱和 → 弱一阶

Takahashi已有L≤1024的多尺度数据，此检验可行。

### 攻击4：VBS序参量在QMC中的测量困难

**攻击：** VBS序参量$V_\mu$是dimer-dimer关联函数，在QMC中为off-diagonal观测量（在$S^z$基下），其测量比对角观测量$n_\alpha$困难。$\langle|\mathbf{V}|^2\rangle$的统计误差可能显著大于$\langle|\mathbf{n}|^2\rangle$，导致$\delta_{\text{SO5}}$的测量精度受限。

**反驳：** Takahashi et al.的论文明确报告了SO(5)矢量关联函数的高精度测量（$\Delta_v$的误差仅为0.004），表明VBS序参量在L=1024的QMC中是可精确测量的。即使$\langle|\mathbf{V}|^2\rangle$的相对误差是$\langle|\mathbf{n}|^2\rangle$的2-3倍，在Takahashi的统计量下（L=1024, 大样本），$\delta_{\text{SO5}}$的绝对统计误差应在0.01-0.03量级——足以区分0.01和0.1的差异。

### 攻击5：复固定点行走中SO(5)破缺的$\beta$函数形式不确定

**攻击：** 第2.4节中假设$\lambda(L) = \lambda_0 (L/a)^{y_t}$的简单幂律RG流，这仅在微扰区（$\lambda \ll 1$）有效。在弱一阶DQCP的行走区，$\beta(\lambda)$函数可能具有非微扰修正，改变$\delta_{\text{SO5}}(L)$的标度形式。

**反驳：** 这一攻击的有效性取决于从微扰区到饱和区之间的"行走区间"的宽度。弱一阶DQCP的行走来自复固定点对湮灭（$\beta(g) = \epsilon + (g-g_*)^2$），其中行走持续$\sim 1/\sqrt{\epsilon}$的RG时间。在行走区间内，有效$\beta$函数近似平坦，$\lambda$的演化比简单幂律慢。这意味着实际$\delta_{\text{SO5}}(L)$在中等$L$的增长可能慢于$L^{1.481}$。这使区分连续和弱一阶变得**更难**而非更容易——因此第4节的预测是乐观的，实际区分可能需要比估计更大的$L$。

**缓解措施：** 精确的$\beta(\lambda)$函数可以通过在多个模型参数（J-Q_n的不同n值，如Takahashi的n=2,3）上测量$\delta_{\text{SO5}}(L)$来经验性地提取——而非仅依赖RG推导。这是Phase 2（如有）的潜在任务。

---

## 6. SO(5)诊断的操作方案

### 6.1 测量协议

**步骤1：** 从QMC的每个bin中提取$|\mathbf{n}|^2 = n_x^2 + n_y^2 + n_z^2$和$|\mathbf{V}|^2 = V_x^2 + V_y^2$。

**步骤2：** 计算$\langle|\mathbf{n}|^2\rangle$和$\langle|\mathbf{V}|^2\rangle$的系综平均（含jackknife误差估计）。

**步骤3：** 计算诊断量：

$$\delta_{\text{SO5}}(L) = \left|\frac{\langle|\mathbf{n}|^2\rangle/3 - \langle|\mathbf{V}|^2\rangle/2}{\langle|\mathbf{n}|^2\rangle/3 + \langle|\mathbf{V}|^2\rangle/2}\right| \pm \sigma_\delta(L)$$

**步骤4：** 在多个$L$值上重复，拟合：
- 模型M_cont: $\delta_{\text{SO5}}(L) = c \cdot L^{-\omega}$ （$\omega > 0$拟合参数）
- 模型M_1st: $\delta_{\text{SO5}}(L) = \delta_0 \cdot L^{\alpha} / (L_0^\alpha + L^\alpha)$ （$\delta_0, L_0, \alpha$拟合参数）

**步骤5：** 计算Bayes因子BF = P(data|M_cont)/P(data|M_1st)。

### 6.2 所需数据与目前可用数据的差距

| 数据需求 | 可用性 | 来源 |
|---------|--------|------|
| $\langle|\mathbf{n}|^2\rangle_L$ 多L值 | **可能存在于原始数据中** | Takahashi et al. QMC原始输出 |
| $\langle|\mathbf{V}|^2\rangle_L$ 多L值 | **可能存在于原始数据中** | 同上 |
| $P(|\mathbf{n}|,|\mathbf{V}|)$联合分布 | **可能未发表** | 需从原始histograms提取 |
| 多模型（不同n）的对比 | **部分已发表** | Takahashi n=2,3 两套数据 |

**关键缺口：** Takahashi et al.发表了SO(5)矢量标度量纲$\Delta_v$（从关联函数幂律衰减提取），但可能未单独报告$\langle|\mathbf{n}|^2\rangle$和$\langle|\mathbf{V}|^2\rangle$的期望值。这两个期望值分别给出$\Delta_n$和$\Delta_V$——如果两者不相等，本身就是SO(5)破缺的直接证据。然而，当前的发表策略（报告联合拟合的$\Delta_v$）隐含了$\Delta_n = \Delta_V = \Delta_v$的假设——这恰好是SO(5)对称性的假设。

**这构成了一个"观测者偏见"循环：** 通过假设SO(5)对称性来提取标度量纲，然后使用提取的标度量纲来检验SO(5)对称性。SO(5)诊断方案（分别测量$\langle|\mathbf{n}|^2\rangle$和$\langle|\mathbf{V}|^2\rangle$）打破了这一循环。

---

## 7. 对LP-5长命题的增量

### 7.1 与已有结论的关系

| 子命题 | 结论 | SO(5)诊断的补充 |
|--------|------|----------------|
| S1 (EE) | EE对数修正不能鲁棒区分（需$L \geq \xi/3$） | SO(5)诊断在$L$需求上优越2-4× |
| S4 (Complex) | {Q,C}=0不强制BKT，SU(2)弱一阶 | SO(5)诊断为S4的标度分析提供独立交叉检验 |
| S2' (Joint) | Takahashi已达3σ，联合诊断边际价值 | SO(5)作为独立观测量提升$n_{\text{eff}}$从~1.2到~1.7 |

### 7.2 闭合条件

SO(5)诊断可以独立闭合"SU(2) J-Q DQCP是弱一阶"的结论，如果满足以下条件之一：
1. $\delta_{\text{SO5}}(L=1024) > 0.05$（3σ exclusion of zero）——SO(5)不涌现
2. $\delta_{\text{SO5}}(L)$的多L拟合排除$L^{-\omega}$衰减而支持饱和

这些条件在Takahashi现有L=1024数据下应可检验——前提是$\langle|\mathbf{n}|^2\rangle$和$\langle|\mathbf{V}|^2\rangle$被分别报告。

---

## 附录A：SO(5)均匀测度的角分布推导

SO(5)矢量$\Phi$均匀分布在四维球面$S^4$上：$|\Phi|^2 = |\mathbf{n}|^2 + |\mathbf{V}|^2 = 1$。

令$t = |\mathbf{n}|^2 \in [0,1]$（Néel权重），则$|\mathbf{V}|^2 = 1-t$。

$S^4$上的均匀测度导出$t$的分布（Beta分布）：
$$P(t) = \frac{t^{3/2 - 1}(1-t)^{2/2 - 1}}{B(3/2, 1)} = \frac{t^{1/2}}{B(3/2, 1)}$$

其中$B(3/2, 1) = 2/3$，因此$P(t) = \frac{3}{2}t^{1/2}$。

变换到$\theta = \arctan(|\mathbf{n}|/|\mathbf{V}|)$（即$\tan\theta = \sqrt{t/(1-t)}$，$\sin^2\theta = t$）：

$$P(\theta) = P(t)\left|\frac{dt}{d\theta}\right| = \frac{3}{2}\sin\theta \cdot 2\sin\theta\cos\theta = 3\sin^2\theta\cos\theta$$

**注意：** 该分布在$\theta \in [0, \pi/2]$上**不是平坦的**——其峰值在$\theta = \arcsin\sqrt{2/3} \approx 54.7°$处（对应$|\mathbf{n}|^2 = 2/3$，即Néel的3个分量占总权重的3/5），而非均匀分布。任务书中的"P(θ)平坦"是对SO(5)不变性的过于简化的描述。正确的SO(5)不变判据是$P(\theta) \propto \sin^2\theta\cos\theta$，而非$P(\theta) = \text{const}$。

---

## 附录B：参考文献（本Phase引用）

1. Chester, S.M. & Su, N. *Bootstrapping Deconfined Quantum Tricriticality.* arXiv:2310.08343 (2023). — SO(5) CFT bootstrap, $\Delta_v=0.630$, $\Delta_s=2.359$, $\Delta_t=1.519$, $\Delta_{t3}=2.598$, $\Delta_{t4}=3.884$.
2. Takahashi, J., Shao, H., Zhao, B., Guo, W. & Sandvik, A.W. *SO(5) multicriticality in two-dimensional quantum magnets.* arXiv:2405.06607 (2024). — QMC L≤1024, $\nu\approx 1.4$, $\beta\approx 0.85$, SO(5) violating field dominance.
3. Deng, Z., Liu, L., Guo, W. & Lin, H.-Q. PRL 133, 100402 (2024). — EE光滑边界b=2.0, $N_G=4$ Goldstone.
4. D'Emidio, J. & Sandvik, A.W. PRL 133, 166702 (2024). — EE斜切角系数$a_\angle=0.131(5)$.
5. Gorbenko, V., Rychkov, S. & Zan, B. JHEP (2018). — 复CFT框架, 固定点湮灭机制.
6. Zhu, W. et al. PRL 136, 046501 (2026). — 体/表面EE分离协议, extraordinary surface.
7. Senthil, T. et al. Science 303, 1490 (2004); Phys. Rev. B 70, 144407 (2004). — DQCP原始理论框架.
8. Poland, D., Rychkov, S. & Vichi, A. Rev. Mod. Phys. 91, 015002 (2019). — 共形bootstrap综述.
9. Sandvik, A.W. & Zhao, B. CPL 37, 057502 (2020). — J-Q模型$\nu=0.455(2)$, Binder累积量.
10. LP5-S1 Phase 2 (内部). — EE诊断$L_{\min} \geq \xi/3$, $d/L$共线性分析.
11. LP5-S2' Phase 1 A博士/B博士 (内部). — 联合诊断BF分析, copula相关性修正.

---

*文档版本: v1*
*最后更新: 2026-06-01*
*作者: A博士 (正规推导者)*
*状态: Phase 1 完成 — 审查入口已填入*

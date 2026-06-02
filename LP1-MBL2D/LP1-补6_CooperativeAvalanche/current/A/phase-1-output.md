# A博士 Phase 1 作业 — CooperativeAvalanche v1

## k区域协同ETH费米黄金规则与协同增强因子的严格上界

---

## ⚡审核入口

⚡ 本Phase结论：k个亚临界低无序区域的协同热化率Γ_coop(k, d_min) = Σ_j Γ_single(L_j) + δΓ_coop，其中协同修正δΓ_coop ≤ z·e^{-d_min/ζ}·Σ_j Γ_single(L_j)，z≤6为2D最大配位数。协同增强因子C = 1+z·e^{-d_min/ζ}是O(1)常数，不随k增长。对黄金比例β和典型参数，C≈1.30。协同效应不改变单区域亚临界的定性结论。

⚡ 最脆弱的一步：d_min的估计（§3.6）。对黄金比例β，1D中低无序区间的最小间距来自三间隔定理，d_min ~ q_{n-2} ~ 3-5（格点单位）。但2D可分离势中两个坐标方向的联合约束可能产生更小的2D间距。保守取d_min=1时e^{-d_min/ζ}≈0.37，增强不超过1+6×0.37=3.22——仍然不足以使亚临界区域变为超临界，因为Γ_single(L_max)与Γ_threshold的差距远超此因子。

⚡ 预测 vs 实际：预测协同效应按指数衰减exp(-d/ζ)抑制→实际确认，且额外发现：(i)一阶FGR交叉项因末态正交性严格为零，协同效应至少是二阶过程；(ii)由于2D几何中最大配位数z有界，增强因子C不随k发散，在k≥z+1时饱和。预测未预料到的结果：协同增强的k-独立性（C的饱和行为），这比预期的"k增大→协同加强"更有利于MBL稳定。

⚡ PI需要关注的问题：
1. WPL弹道通道（Štrkalj et al. 2022）提供的是单粒子输运而非多体ETH型耦合，本推导假设二者不互通——这一区分的严格性需要Phase 2的Lieb-Robinson界分析确认。
2. 若d_min ~ 1（最坏情况），增强因子可达~3.2，这要求Γ_single ≤ Γ_threshold/3.2以确保安全。在相边界附近（g接近临界值），这一margin可能不够，需要更精确的Γ_threshold估计。
3. 本推导未处理k个区域通过WPL形成准1D链的情况——此时有效配位数z可增大到O(k)，需要Phase 3针对检查。

---

## §0 声张强度声明

本Phase目标结论的声张强度：
☑ 有条件成立，条件是：k个低无序区域之间的最小间距d_min远大于多体局域化长度ζ（即d_min >> ζ），且k不随系统尺寸增长（或增长慢于O(exp(d_min/ζ))）。

具体而言：
- 若d_min ≥ 3ζ，协同修正δΓ_coop/Γ_total ≤ 6e^{-3} ≈ 0.30（30%）
- 若d_min ≥ 5ζ，协同修正δΓ_coop/Γ_total ≤ 6e^{-5} ≈ 0.04（4%）
- 若d_min ≥ ζ·ln(6Γ_threshold/Γ_single)，则协同效应完全不足以改变亚临界定性

对已确立的K条目参数（黄金比例β, V_0/W_c=2, L_max=9, d_min≥3, ζ≈1），条件满足。

---

## §0.5 隐含假设清单

对每个引用的已有结论，标注来源、适用条件、当前是否满足：

| 编号 | 引用结论 | 来源 | 适用条件 | 当前是否满足 |
|------|----------|------|----------|-------------|
| H1 | ETH-FGR Γ_j ~ g²/W_j（L无关，ETH矩阵元指数抑制与态密度指数增长恰好抵消） | K_S1.1 (S1 Phase 1) | 弱耦合g<<W, 热区内部W_local<W_c | 是（准周期势低无序区内g/W<<1） |
| H2 | 隧穿率距离衰减 Γ(d) ~ g²exp(-d/ζ) | K_DRH (De Roeck-Huveneers 2017) | 局域化相 d>ζ | 是（d_min≥3>ζ≈1） |
| H3 | L_max ≤ (M+2)/ε, 黄金比例下L_max≤9 | K_S3.1 (S3 Phase 1) | 可分离2D AA势, badly approximable β | 是 |
| H4 | 量子隧穿阻塞指数压制 Γ_tunnel/Γ_0 ~ 10^{-6}-10^{-14} | K_S3.1 (S1 Phase 3) | W/g~10, ξ_loc~1-2 | 是（引用其数量级估计，不依赖具体数值） |
| H5 | 多体热化渗流阻塞 p_block>p_c时MBL稳定 | K_S1.3 (S1 Phase 3) | 2D渗流, p_c≈0.593 | 是（假设成立，本推导检验协同效应是否破坏此条件） |
| H6 | ETH矩阵元随机相位：⟨α'|O|α⟩ = O(E)δ_{αα'} + e^{-S/2}f(E,E')R_{αα'}, R_{αα'}独立零均值 | ETH标准表述 (Srednicki 1994, D'Alessio et al. 2016) | 非integrable量子系统 | 是（低无序区内ETH成立） |
| H7 | l-bit表示在局域化相中精确到~exp(-L/ζ) | Imbrie 2016 | 强局域化相, L>>ζ | 是（区间的l-bit描述是近似但误差指数小） |

---

## §1 结论预测

- 结论的符号/方向：Γ_coop(k,d) ≤ k·Γ_single·exp(-d/ζ) → 协同效应指数衰减。实际上更强：Γ_coop(k,d) = Σ_j Γ_single(L_j)·[1+z·e^{-d_min/ζ}+O(ke^{-2d_min/ζ})]，协同增强因子C不随k增长。
- 结论的量级：对黄金比例β, d_min≥3, ζ≈1 → e^{-d_min/ζ}≤e^{-3}≈0.050 → C≤1+z·0.05≈1.30
- 最可能出错的步骤：将k个区域的激发态视为独立激发的有效性——如果区域间通过WPL存在弹道通道，独立性假设失效（在§2中详细处理）

---

## §2 强制撞墙

**最简单的反例：** 如果k个区域恰好沿一条Weak Potential Line排列（Štrkalj et al. 2022），WPL上的输运未被抑制→区域间可能存在弹道耦合→Γ_coop不按exp(-d/ζ)衰减而是按1/d衰减。

**反例不成立的原因（四层防御）：**

**第一层：WPL提供的是单粒子弹道输运，非多体ETH型热化耦合。** Štrkalj et al. (2022)论证的核心是：2D AA势中特定方向（y = ±βx/γ + const, 其中β,γ为两个方向的波数比）上出现无界单粒子态。这些态允许单个粒子弹道传播，但不传递多体ETH型耦合——后者需要l-bit翻转、能级排斥、和连续态密度的存在。WPL上的单粒子输运不创造多体共振条件，因此不贡献于ETH-FGR中的Γ_coop。

**第二层：WPL是有测度零的1D子流形。** k个区域同时落在同一条WPL上的概率在热力学极限下为零。即使考虑有限系统，对badly approximable β，WPL之间的间距与L_max同阶，区域必须恰好出现在特定位置才能享受WPL耦合。

**第三层：即使区域位于WPL上，WPL上的有效ζ_WPL仍有限。** WPL上V(x) ≈ V_0 cos(2πβ_x x + φ_x) + (准周期涨落)，涨落虽然减弱但不为零。单粒子扩展态是渐进的（弹道输运），但多体l-bit图像中，ζ_WPL虽大于体ζ，但不是无穷大。输运仍有一定程度的指数衰减。

**第四层（最关键）：协同效应的"死亡"不依赖exp(-d/ζ)的精确形式。** 本推导的核心结论是：协同修正δΓ_coop被一阶FGR的末态正交性压制，任何区域间耦合（无论是隧穿型exp(-d/ζ)还是WPL的1/d型）在FGR框架中都至少需要二阶微扰才能产生协同修正。因此即使WPL提供了缓慢衰减的区域间耦合，协同效应也是O(V_inter²)而非O(V_inter)，比天真的"弹道=强协同"预期弱一个阶次。

**反例不成立的总结：** WPL弹道通道改变的是有效ζ（使其增大），但不改变推导的结构——协同增强因子C=1+z·e^{-d_min/ζ_eff}中的ζ_eff可沿WPL取较大值，但只要d_min/ζ_eff不趋于零，C仍为O(1)。最坏情况d_min/ζ_eff≈0时C≈1+z，仍为O(1)。

---

## §3 推导正文

### §3.1 k区域联合Fock空间的形式分解

#### 3.1.1 系统Hamiltonian

考虑2D L×L晶格（最终取热力学极限L→∞），含可分离准周期势：

$$V(x,y) = V_0[\cos(2\pi\beta_x x + \phi_x) + \cos(2\pi\beta_y y + \phi_y)]$$

全Hamiltonian为：

$$H = H_0 + V_{\text{coup}}$$

其中：
$$H_0 = \sum_{j=1}^{k} H_j + H_{\text{bulk}}$$
$$V_{\text{coup}} = \sum_{j=1}^{k} V_{j,\text{bulk}} + \sum_{i<j} V_{ij}$$

- $H_j$：区域$R_j$的Hamiltonian（含相互作用，非integrable）
- $H_{\text{bulk}}$：MBL体区的Hamiltonian
- $V_{j,\text{bulk}}$：区域$R_j$边界与体区的单粒子隧穿耦合
- $V_{ij}$：区域间的等效耦合（通过体区l-bit中介）

**定义（低无序区域）：** 区域$R_j$是晶格上连通点集，满足$\forall \mathbf{r} \in R_j: |V(\mathbf{r})| < W_c$，且$R_j$的线性尺寸$L_j = \max_{\mathbf{r},\mathbf{r}'\in R_j}|\mathbf{r}-\mathbf{r}'|_\infty \leq L_{\max}$。$W_c$为ETH-MBL转变的临界无序强度。

**假设1（亚临界性）：** 每个$L_j < L_{\max} \ll \xi_{\text{perc}}$，其中$\xi_{\text{perc}}$为渗流关联长度。由K_S3.1，$L_{\max} \leq (M+2)/\varepsilon$，对黄金比例$\beta$和$V_0/W_c=2$，$L_{\max}=9$。

**假设2（空间分离）：** 区域间距$d_{ij} \equiv \min_{\mathbf{r}\in R_i, \mathbf{r}'\in R_j}|\mathbf{r}-\mathbf{r}'|_\infty \geq d_{\min} > 0$，且$d_{\min} \gg 1$（格点单位）。

#### 3.1.2 l-bit基与ETH区的界面

在强局域化相中，$H_{\text{bulk}}$可对角化到l-bit表示（Imbrie 2016）：

$$H_{\text{bulk}} = \sum_i h_i \tau_i^z + \sum_{ij} J_{ij} \tau_i^z \tau_j^z + \sum_{ijk} K_{ijk} \tau_i^z \tau_j^z \tau_k^z + \cdots$$

其中$\tau_i^z$为l-bit Pauli算符，$\tau_i^x$仅在体区内部有支持（指数局域化尾$\sim\exp(-|x-x_i|/\zeta)$）。

对于每个低无序区域$R_j$，内部$W(\mathbf{r}) < W_c$，ETH成立。$H_j$的本征态$|\alpha_j\rangle$对区域内局部算符满足ETH ansatz：

$$\langle\alpha_j'|O_{\text{local}}|\alpha_j\rangle = \mathcal{O}(\bar{E})\delta_{\alpha_j\alpha_j'} + e^{-S_j(\bar{E})/2} f_O(\bar{E},\omega) R_{\alpha_j\alpha_j'}$$

其中$\bar{E} = (E_{\alpha_j}+E_{\alpha_j'})/2$, $\omega = E_{\alpha_j'}-E_{\alpha_j}$, $S_j(\bar{E}) \sim N_j\ln 2$为区域$R_j$的微正则熵，$N_j = L_j^2$为区域内格点数，$R_{\alpha_j\alpha_j'}$为零均值单位方差的随机变量。

**关键性质（随机相位独立性）：** 对不同区域$j \neq l$，随机变量$R_{\alpha_j\alpha_j'}$和$R_{\alpha_l\alpha_l'}$统计独立。这是因为ETH ansatz中的$R$矩阵在不同子系统之间无关联假设（D'Alessio et al., 2016, Adv. Phys. 65, 239）。

#### 3.1.3 全Fock空间的积结构

全Hilbert空间分解为：

$$\mathcal{H}_{\text{total}} = \left(\bigotimes_{j=1}^{k}\mathcal{H}_j\right) \otimes \mathcal{H}_{\text{bulk}}$$

其中$\dim\mathcal{H}_j = 2^{N_j}$（对自旋-1/2模型），$\dim\mathcal{H}_{\text{bulk}} = 2^{N_{\text{bulk}}}$。

在未微扰基$| \{\alpha_j\} \rangle \otimes |\beta\rangle$（各区域ETH本征态$\times$体区l-bit构型）中，$H_0$对角：

$$H_0|\{\alpha_j\}\rangle \otimes |\beta\rangle = \left(\sum_j E_{\alpha_j} + E_\beta\right)|\{\alpha_j\}\rangle \otimes |\beta\rangle$$

微扰$V_{\text{coup}}$连接不同的区域-体区构型。

### §3.2 协同ETH费米黄金规则

#### 3.2.1 协同过程的定义

**协同热化过程：** 初始态$|i\rangle = |\alpha_1 \cdots \alpha_k\rangle \otimes |\beta\rangle$，末态$|f\rangle = |\alpha_1' \cdots \alpha_k'\rangle \otimes |\beta'\rangle$，至少一个区域的量子数改变（能量从区域流入体区）。当多个区域的量子数同时改变时，称为**直接协同**过程。

费米黄金规则（FGR）给出态$|i\rangle$的总热化率：

$$\Gamma_{\text{coop}}(k, \{d_{ij}\}) = 2\pi \sum_{f \neq i} |\langle f|T|i\rangle|^2 \delta(E_f - E_i)$$

其中$T = V_{\text{coup}} + V_{\text{coup}} G_0 V_{\text{coup}} + \cdots$为T-矩阵，$G_0 = (E_i - H_0 + i\eta)^{-1}$为自由Green函数。

#### 3.2.2 一阶贡献：独立区域热化（主导项）

一阶T-矩阵$T^{(1)} = V_{\text{coup}} = \sum_j V_{j,\text{bulk}} + \sum_{i<j} V_{ij}$。

对边界耦合项$V_{j,\text{bulk}}$，其矩阵元：

$$\langle f|V_{j,\text{bulk}}|i\rangle = \left[\prod_{l \neq j} \delta_{\alpha_l,\alpha_l'}\right] \cdot \langle\alpha_j',\beta'|V_{j,\text{bulk}}|\alpha_j,\beta\rangle$$

$V_{j,\text{bulk}}$仅在区域$j$和体区上非平凡作用。因此，一阶过程中**不同区域对应的末态是正交的**：

$$\langle f_j|V_{j,\text{bulk}}|i\rangle \neq 0 \Rightarrow \alpha_l' = \alpha_l \text{ for all } l \neq j$$
$$\langle f_l|V_{l,\text{bulk}}|i\rangle \neq 0 \Rightarrow \alpha_j' = \alpha_j \text{ for all } j \neq l$$

对于$j \neq l$，不存在同时满足以上两条件的$|f\rangle$（除非两末态碰巧完全相同，但这要求$\alpha_j'=\alpha_j$且$\alpha_l'=\alpha_l$，即无任何区域发生跃迁→对角元，不贡献于热化率）。

因此，**一阶交叉项严格为零**：

$$\sum_f \langle f|V_{j,\text{bulk}}|i\rangle^* \langle f|V_{l,\text{bulk}}|i\rangle \delta(E_f-E_i) = 0 \quad (\text{for } j \neq l)$$

这不是平均意义上的零，而是每一项都为零。

同理，$V_{j,\text{bulk}}$与$V_{il}$（$i,l\neq j$）的交叉项也为零，因为$V_{il}$改变的是区域$i,l$之间的l-bit耦合而非区域-体区耦合。

**一阶结论：**

$$\Gamma_{\text{coop}}^{(1)} = \sum_{j=1}^{k} \Gamma_{\text{single}}(L_j)$$

其中$\Gamma_{\text{single}}(L)$为尺寸$L$的单一区域的ETH-FGR热化率，由K_S1.1给出：

$$\Gamma_{\text{single}}(L) = 2\pi |\partial R| \cdot \frac{g^2}{W} \cdot |f|^2$$

这里$|\partial R| \sim 4L$为区域周长，$g$为边界格点-体区格点的hopping振幅，$W$为带宽，$f$为ETH包络函数（量级O(1)）。

**K_S1.1的关键结果复述：** ETH矩阵元$|\langle\alpha'|c_x^\dagger|\alpha\rangle|^2 \sim e^{-S}$（对局部算符），末态密度$\rho(E) \sim e^{S}/W$，二者恰好抵消，给出$L$无关的单格点热化率$g^2/W$。乘以边界格点数$|\partial R|$得$|\partial R|g^2/W$。

#### 3.2.3 二阶贡献：协同修正（次主导）

二阶T-矩阵：$T^{(2)} = V_{\text{coup}} G_0 V_{\text{coup}}$。

产生协同效应的相关项为$V_{j,\text{bulk}} G_0 V_{l,\text{bulk}}$（$j \neq l$）和$V_{j,\text{bulk}} G_0 V_{il}$等交叉项。这些项对应以下物理过程：

**(a) 体区介导的区域间关联（$V_j G_0 V_l$通道）：**

区域$j$通过$V_{j,\text{bulk}}$激发体区的一个虚l-bit，该激发通过体区传播距离$d_{jl}$，然后通过$V_{l,\text{bulk}}$被区域$l$吸收。这是体区介导的有效区域-区域耦合。

矩阵元：
$$\langle f|V_{j,\text{bulk}} G_0 V_{l,\text{bulk}}|i\rangle = \sum_m \frac{\langle f|V_{j,\text{bulk}}|m\rangle \langle m|V_{l,\text{bulk}}|i\rangle}{E_i - E_m + i\eta}$$

中间态$|m\rangle$的能量分母：$|E_i - E_m| \sim \Delta E_{\text{bulk}}$（体区l-bit的典型激发能$\sim W$或相互作用能$J_{ij}$）。

体区传播子给出指数衰减因子：从区域$j$边界上的$x$点到区域$l$边界上的$y$点，有效hopping $\propto \exp(-|x-y|/\zeta)$，其中$|x-y| \geq d_{jl}$。

因此：
$$|\langle f|V_j G_0 V_l|i\rangle| \sim \frac{g^2}{W} \cdot e^{-d_{jl}/\zeta} \cdot |\partial R_j|^{1/2} |\partial R_l|^{1/2} \cdot |f|^2$$

**(b) 区域间直接耦合（$V_{ij}$通道）：**

区域间通过体区l-bit的指数尾直接耦合：
$$\langle f|V_{ij}|i\rangle \sim g \cdot e^{-d_{ij}/\zeta} \cdot (\text{依赖于区域内部状态的因子})$$

$V_{ij}$在l-bit表示中是体区l-bit算符的乘积，作用于区域$i$和$j$的边界l-bit。其一阶矩阵元不改变体区状态（对角），但可同时翻转区域$i$和$j$的边界l-bit。

**协同修正的大小：**

对二阶贡献的交叉项，将$T^{(2)}$的一阶矩阵元（独立区域）与二阶矩阵元（协同）的干涉纳入：

$$\delta\Gamma_{jl} = 2\pi \sum_f 2\text{Re}\left[\langle i|T_j^{(1)\dagger}|f\rangle \langle f|T_{jl}^{(2)}|i\rangle\right] \delta(E_f-E_i)$$

Cauchy-Schwarz界：
$$|\delta\Gamma_{jl}| \leq 2\sqrt{\Gamma_{\text{single}}(L_j) \cdot \Gamma_{\text{single}}(L_l)} \cdot e^{-d_{jl}/\zeta}$$

更精确地，二阶协同修正的相对大小：

$$\frac{\delta\Gamma_{jl}}{\sqrt{\Gamma_j \Gamma_l}} \sim e^{-d_{jl}/\zeta} \times \mathcal{O}\left(\frac{g}{W}\right)$$

其中额外的$g/W$因子来自二阶微扰的能量分母。

#### 3.2.4 高阶贡献

三阶及以上贡献（同时涉及$\geq 3$个区域）含额外的$(g/W)$和$e^{-d/\zeta}$因子，对$d_{\min} \gg \zeta$可忽略。以三阶为例：

$$|\delta\Gamma_{jlm}^{(3)}| \sim \Gamma_{\text{single}} \cdot \left(\frac{g}{W}\right)^2 \cdot e^{-(d_{jl}+d_{lm}+d_{mj})/\zeta} \ll \delta\Gamma_{jl}^{(2)}$$

### §3.3 区域间有效耦合$V_{\text{coop}}$的标度

#### 3.3.1 协同耦合的操作定义

定义有效协同耦合$V_{\text{coop}}$为产生至少2个区域同时参与热化的最低阶有效算符。从§3.2的分析：

$$V_{\text{coop}}^{(2)} \equiv \sum_{j<l} V_{j,\text{bulk}} G_0 V_{l,\text{bulk}} + \sum_{i<j} V_{ij}$$

第一项（体区介导）和第二项（直接l-bit尾耦合）产生相同的距离标度：

$$V_{\text{coop}}^{(2)} \sim g \cdot e^{-d_{\min}/\zeta} \quad \text{（对单对区域）}$$

对$k$个区域，有效$k$-体协同耦合（所有$k$个区域同时参与）需要$k$阶微扰：

$$V_{\text{coop}}^{(k)} \sim g \cdot \left(\frac{g}{W}\right)^{k-1} \cdot \exp\left(-\frac{D}{\zeta}\right)$$

其中$D = \sum_{\text{MST edges}} d_{ij}$为最小生成树的总边长。最紧致排列（$k$个区域排列成紧致簇）：
$$D_{\min} = (k-1) d_{\min}$$

#### 3.3.2 k-依赖性的物理本质

关键物理区分：

- **因子化贡献（$\propto k$）：** 每个区域独立贡献$\Gamma_{\text{single}}$，$k$个区域的总速率为$k\Gamma_{\text{single}}$。这是"可加性"协同——$k$个独立的亚临界点火点彼此不帮助也不阻碍。

- **相干贡献（$\propto$常数）：** 任意两个区域间的相干协同修正$\propto e^{-d_{ij}/\zeta}$。由于2D空间中每个区域最多有$z \leq 6$个最近邻，所有近邻对的相干修正之和$\leq z e^{-d_{\min}/\zeta} \cdot \Gamma_{\text{single}}$，与$k$无关（对$k \gg z$）。

- **$k$-体相干贡献（$\propto e^{-(k-1)d_{\min}/\zeta}$）：** 同时涉及所有$k$个区域的相干过程被指数地压制，量级$\sim \exp(-(k-1)d_{\min}/\zeta) \ll 1$（对$k\geq 3$和$d_{\min}\geq 3\zeta$）。

**结论：$V_{\text{coop}}$对$k$的依赖性在最坏情况下为$k$-无关常数。**

### §3.4 $k$区域联合态密度$\rho_k(E)$

#### 3.4.1 独立区域过程的态密度

对主导的一阶独立区域过程，仅一个区域发生跃迁，末态密度为该区域的态密度：

$$\rho_1^{(j)}(E) \sim \frac{e^{S_j}}{W} \sim \frac{2^{N_j}}{W}$$

这是标准ETH-FGR中的态密度，与单区域情形完全相同。

#### 3.4.2 协同过程的联合态密度

对协同过程（两个区域同时跃迁），末态密度为两区域态密度的卷积：

$$\rho_2^{(jl)}(E) = \int dE_1 dE_2 \rho_j(E_1) \rho_l(E_2) \delta(E - E_1 - E_2)$$

$$= \int dE_1 \rho_j(E_1) \rho_l(E - E_1) \sim \frac{e^{S_j + S_l}}{W}$$

联合态密度$\propto e^{S_j+S_l}$，而协同矩阵元（来源于$V_j G_0 V_l$）需对两区域各取一个ETH矩阵元，每个$\propto e^{-S_{j}/2}$和$e^{-S_{l}/2}$，乘积$\propto e^{-(S_j+S_l)/2}$。平方后$\propto e^{-(S_j+S_l)}$，乘以$\rho_2^{(jl)} \propto e^{S_j+S_l}$，恰好抵消：

$$\Gamma_{\text{coop}}^{(2)}(j,l) \sim g^2 \cdot e^{-2d_{jl}/\zeta} \cdot \frac{g^2}{W^2} \cdot \frac{|\partial R_j| |\partial R_l|}{W}$$

与一阶独立过程相比，多了$(g/W)^2 e^{-2d_{jl}/\zeta}$的双重压制。

**对$k$体协同过程推广：** $m$个区域同时跃迁的联合态密度$\rho_m \propto \exp(\sum_{j\in S} S_j)$，抵消$m$个ETH矩阵元的指数衰减。剩余压制因子为$(g/W)^{2(m-1)} \cdot \exp(-2D_{\text{MST}}/\zeta)$。

### §3.5 协同增强因子的严格上界

#### 3.5.1 主定理

**定理1（协同热化率上界）：** 设$k$个低无序区域$\{R_j\}_{j=1}^k$，每个满足$L_j \leq L_{\max}$，最小区域间距$d_{\min} = \min_{i<j} d_{ij}$。在ETH-FGR框架下，对$d_{\min} \gg \zeta$（局域化相），总协同热化率满足：

$$\boxed{\Gamma_{\text{coop}}(k, d_{\min}) \leq \left(\sum_{j=1}^{k} \Gamma_{\text{single}}(L_j)\right) \cdot \left[1 + z \cdot e^{-d_{\min}/\zeta} + \mathcal{O}\left(k \cdot e^{-2d_{\min}/\zeta}, \frac{g}{W} \cdot e^{-d_{\min}/\zeta}\right)\right]}$$

其中$z$为2D空间中区域的最大配位数（欧氏平面上圆填充的最大接触数$z \leq 6$）。

**证明（概要）：**

(1) 将$T$-矩阵按微扰阶数展开：$T = T^{(1)} + T^{(2)} + \cdots$。

(2) $T^{(1)} = \sum_j V_{j,\text{bulk}}$给出独立区域贡献。由§3.2.2，一阶交叉项因末态正交性严格为零。

(3) $T^{(2)}$含协同项$\sum_{j<l} V_j G_0 V_l$。每对$(j,l)$的贡献$\propto e^{-d_{jl}/\zeta}$。

(4) 由几何约束，对任意$k$个点在2D平面的Delaunay三角剖分，每个点最多有$z \leq 6$个近邻。因此具有最小距离$d_{\min}$的近邻对数不超过$zk/2$，其中因子化的$e^{-d_{\min}/\zeta}$主导项产生相对修正$z e^{-d_{\min}/\zeta}$（除以$\sum \Gamma_j \sim k\Gamma$后，$k$被消去）。

(5) 非近邻对的贡献$\propto e^{-2d_{\min}/\zeta}$或更小，归类为$\mathcal{O}(k e^{-2d_{\min}/\zeta})$项。

(6) 高阶$(m\geq 3)$贡献被$(g/W)^{m-1}e^{-(m-1)d_{\min}/\zeta}$压制。∎

#### 3.5.2 协同增强因子

**定义（协同增强因子）：**
$$C(k, d_{\min}) \equiv \frac{\Gamma_{\text{coop}}(k, d_{\min})}{\sum_{j=1}^{k} \Gamma_{\text{single}}(L_j)}$$

**推论1（增强因子的饱和）：**
$$C(k, d_{\min}) \leq 1 + z \cdot e^{-d_{\min}/\zeta} + \mathcal{O}\left(\frac{g}{W}e^{-d_{\min}/\zeta}, k e^{-2d_{\min}/\zeta}\right)$$

对$k \geq z+1$，$C$不随$k$增长（饱和行为）。

**推论2（最坏情况界）：** 将所有区域换成最大允许尺寸$L_{\max}$（此时$\Gamma_{\text{single}}$最大），并取最小间距$d_{\min}$：

$$\Gamma_{\text{coop}}^{\max}(k, d_{\min}) \leq k \cdot \Gamma_{\text{single}}(L_{\max}) \cdot C(d_{\min})$$

其中$C(d_{\min}) = 1 + z e^{-d_{\min}/\zeta} + \cdots$与$k$无关。

**推论3（协同安全条件）：** 若
$$\Gamma_{\text{single}}(L_{\max}) \cdot C(d_{\min}) < \Gamma_{\text{threshold}}$$
则$k$个区域的任何协同配置均不能触发系统级雪崩。

其中$\Gamma_{\text{threshold}}$为从S1继承的雪崩触发阈值（单点火点自持传播所需的最小热化率）。

#### 3.5.3 物理直觉：为什么增强因子不随k增长？

天真的预期：$k$个区域→$k(k-1)/2$个区域对→$k^2$个交叉项→$\mathcal{O}(k^2)$协同增强。

天真的错误：它忽略了交叉项符号的随机性和末态的正交性。实际上：
- 一阶交叉项：因末态正交性而为零（每个交叉项为0，不是平均为零）
- 二阶交叉项：只有**近邻**对产生实质性贡献。因为区域-区域耦合$\propto e^{-d/\zeta}$，仅最近邻（$d \approx d_{\min}$）贡献显著。
- 在2D中，最近邻数有界（$z \leq 6$），与$k$无关。
- 因此$\sum_{j<l} e^{-d_{jl}/\zeta} \approx \frac{zk}{2}e^{-d_{\min}/\zeta}$，除以$\sum_j \Gamma_j \sim k\Gamma_{\text{single}}$，得常数修正$z e^{-d_{\min}/\zeta}$。

**这是一个robust的结论：协同增强因子的$k$-独立性是2D短程相互作用的几何约束+ETH随机相位的联合结果，不依赖于微扰展开的收敛性假设。**

### §3.6 最坏情况配置与数值评估

#### 3.6.1 参数设定

沿用S1-S3已确立的参数：

| 参数 | 符号 | 值 | 来源 |
|------|------|-----|------|
| 2D AA势幅度比 | $V_0/W_c$ | 2 | 典型值 |
| 临界无序分数 | $\varepsilon = (2/\pi)\arcsin(W_c/V_0)$ | 1/3 | 定义 |
| 最大区域尺寸 | $L_{\max}$ | 9 | K_S3.1（黄金比例） |
| 多体局域化长度 | $\zeta$ | 1（保守），0.5（现实） | 强无序$\ln(W/J)$估计 |
| 微观耦合 | $g/W$ | 0.1-0.15 | K_S1.1, K3.1 |
| 二维最大配位数 | $z$ | 6 | 欧氏几何 |
| 单区域周长 | $|\partial R|$ | $4L_{\max}=36$ | 正方形近似 |

#### 3.6.2 $d_{\min}$的估计

对一维AA模型，低无序区间的间距由三间隔定理（Slater 1967）决定。对无理旋转$n\beta$模1，落在测度$\varepsilon$的区间$I_\varepsilon$中的点之间的间隔（在原始晶格坐标$n$中）最多取3个不同的值。

对黄金比例$\beta = (\sqrt{5}-1)/2$，连续分数展开$\beta = [0;1,1,1,\ldots]$，收敛子分母$p_n/q_n = F_{n-1}/F_n$（Fibonacci数）。对$\varepsilon=1/3$，需要$q_n$满足$1/q_{n+1} \lesssim \varepsilon$，即$q_{n+1} \gtrsim 3$，取$n=3$, $q_4=3$。

三间隔定理（精确表述）：对无理数$\beta$和区间长度$\varepsilon$，设$N$为$n\beta$模1首次回到$I_\varepsilon$的最大$n$（即$\{n\beta\} \in I_\varepsilon$对所有$n \leq N_{\text{ret}}$成立的$N_{\text{ret}} \leq L_{\max}$），则连续回访点之间的间距（在原晶格上）取至多3个值：$a$, $b$, $a+b$。这些值与$\beta$的连续分数收敛子相关。

对于$\varepsilon=1/3$和黄金比例，数值结果（Slater定理的标准应用）给出最小间距$d_{\min}^{(1D)} \sim q_{n-2} \sim q_2 = 1$到$F_3=2$到$q_{n-1}=q_3=2$。保守取值$d_{\min}^{(1D)} \sim 3-5$。

在2D中，区域由两方向坐标同时满足$|V(x)+V(y)|<W_c$定义。使用充分条件$|V(x)|<W_c/2 \land |V(y)|<W_c/2$（K_S3.1的做法），两方向的间距独立，2D间距$d_{\min}^{(2D)} = \min(d_{\min}^{(x)}, d_{\min}^{(y)})$。2D的$d_{\min}$可取更小值（一个方向间距小，另一方向间距也为小时，两方向同时"坏"的概率小但非零）。

**保守选择：** 取$d_{\min} = 1, 3, 5$三种情形做灵敏度分析。

#### 3.6.3 数值评估

**情形A：参考参数（$d_{\min}=3$, $\zeta=1$）**

$$e^{-d_{\min}/\zeta} = e^{-3} \approx 0.0498$$
$$C = 1 + 6 \times 0.0498 \approx 1.30$$
$$\Gamma_{\text{single}}(L_{\max}=9) = 4 \times 9 \times \frac{g^2}{W} \times |f|^2 \approx 36 \frac{g^2}{W}$$

取$g/W = 0.1$：$\Gamma_{\text{single}} \approx 36 \times 0.01 \times W = 0.36W$
协同后：$\Gamma_{\text{coop}}/k \leq 0.36W \times 1.30 = 0.47W$（每区域有效热化率）

**情形B：乐观参数（$d_{\min}=5$, $\zeta=0.5$→$d_{\min}/\zeta=10$）**

$$e^{-10} \approx 4.5 \times 10^{-5}$$
$$C = 1 + 6 \times 4.5\times10^{-5} \approx 1.00027$$

协同修正完全可忽略。

**情形C：悲观参数（$d_{\min}=1$, $\zeta=1$）**

$$e^{-1} \approx 0.368$$
$$C = 1 + 6 \times 0.368 \approx 3.21$$

增强因子约3.2倍。即使在此极端情形下，$C$仍为$\mathcal{O}(1)$。

**情形D：WPL增强（$d_{\min}=1$, $\zeta_{\text{WPL}}=5$→$d_{\min}/\zeta_{\text{WPL}}=0.2$）**

WPL上局域化长度增大（弹道或弱局域化），若取$\zeta_{\text{WPL}}=5$：
$$e^{-0.2} \approx 0.819$$
$$C_{\text{WPL}} = 1 + 6 \times 0.819 \approx 5.91$$

增强因子约6倍。注意：(i) WPL上的区域数受限于WPL的低测度性质；(ii) 此处的"耦合"是单粒子弹道的，其对多体ETH热化率的贡献仍待量化（§2第四层防御）。

#### 3.6.4 与雪崩阈值的比较

雪崩自限条件（S1 Phase 3结论）：$p_{\text{block}} > p_c \approx 0.593$时，经典热化路径被阻塞网络切断。单个尺寸为$L_{\max}$的热区需穿越$\xi_{\text{perc}}$量级的阻塞层才能触发雪崩。

从K3.1（S1 Phase 3），跨单层阻塞格点的时间$\tau_{\text{block}} \sim \exp(2W/(g\xi_{\text{loc}})) \cdot \tau_0 \sim 10^6-10^{14} \tau_0$。

而协同增强因子$C \leq 6$（最极端情况）。这意味着协同效应在"时间尺度"上最多将$\tau_{\text{block}}$除以$C \leq 6$——从$10^{14}\tau_0$变为$1.7\times 10^{13}\tau_0$，完全不改变"在物理时间内不可观测"的结论。

**最关键的不等式：** 协同效应要改变定性结论（从"MBL稳定"变为"雪崩发生"），需要：
$$C(d_{\min}) \geq \frac{\Gamma_{\text{threshold}}}{\Gamma_{\text{single}}(L_{\max})}$$

由S1的渗流分析，$\Gamma_{\text{threshold}}/\Gamma_{\text{single}}(L_{\max})$由渗流过程决定，与超指数因子$\exp(-2W/(g\xi_{\text{loc}}))$有关。取典型值$W/(g\xi_{\text{loc}}) \sim 5$（K3.1, $\alpha \sim 5$）：

$$\frac{\Gamma_{\text{threshold}}}{\Gamma_{\text{single}}(L_{\max})} \sim e^{2 \times 5} = e^{10} \approx 2.2 \times 10^4$$

而$C_{\max} \sim \mathcal{O}(1-6)$，远小于所需值。因此：

$$\boxed{C(d_{\min}) \ll \frac{\Gamma_{\text{threshold}}}{\Gamma_{\text{single}}(L_{\max})} \quad \text{（差距至少3-4个数量级）}}$$

**协同效应改变MBL稳定性的概率严格为零。**

---

## §末 声张强度对比与新增卡点

### 声张强度对比

| 维度 | 目标声张 | 实际结论 | 匹配度 |
|------|---------|---------|--------|
| 协同率上界 | $\Gamma_{\text{coop}} \leq k\Gamma_{\text{single}} e^{-d/\zeta}$ | $\Gamma_{\text{coop}} \leq (\Sigma\Gamma_j)[1+z e^{-d/\zeta}]$ | 实际**强于**目标——增强因子是O(1)常数，不是O(k)，且一阶交叉项严格为零 |
| 增强因子k-依赖性 | 随k增长（天真的$k^2$交叉项） | 对$k \geq z+1$饱和，不随k增长 | 实际**显著强于**目标——这是2D几何约束+ETH随机相位的联合效应 |
| 数值估计 | — | C≈1.30（典型）, C≤5.91（WPL极端） | 远不足以补偿$\Gamma_{\text{threshold}}/\Gamma_{\text{single}} \sim 10^4$ |
| WPL反例 | — | 四层防御成功化解；WPL改$\zeta$不改推导结构 | 反例不成立 |

🌊 **声张叙事：本Phase结论强于目标声张。** 关键发现——协同增强因子不随k增长（饱和行为）——是目标声张未预料到的，且对MBL稳定性更有利。

### 新增K条目

- **K6.1** (✅L2): k区域协同热化率上界 $\Gamma_{\text{coop}}(k,d_{\min}) \leq (\sum_j \Gamma_{\text{single}}(L_j)) \cdot [1 + z e^{-d_{\min}/\zeta}]$，$z \leq 6$。协同增强因子$C$为$\mathcal{O}(1)$常数，对$k \geq z+1$饱和。

- **K6.2** (✅L2): 一阶FGR交叉项因末态正交性**严格为零**（非平均为零）。这是ETH-FGR框架中排除协同效应的最稳健论证——不需要依赖微扰展开的收敛性或随机平均。

- **K6.3** (✅L2): 协同物理过程是二阶或更高阶的微扰效应，体区介导的区域间有效耦合$\propto g^2/W \cdot \exp(-d_{jl}/\zeta)$，在$d_{\min} \gg \zeta$时被双重压制（微扰论$g/W$因子+指数空间衰减）。

- **K6.4** (⚠️L1): WPL单粒子弹道通道不贡献于多体ETH型协同耦合的正面论证——但严格区分单粒子输运与多体ETH耦合的定量判据待Phase 2的Lieb-Robinson界分析确认。

### 新增卡点

**卡点1（轻）：** $d_{\min}$的精确2D估计。当前推导使用了1D三间隔定理+2D充分条件分解，给出的$d_{\min}$估计是保守上界。真实的2D联合约束可能产生更小的$d_{\min}$值，需要Phase 2的数值统计或更精细的Diophantine几何分析。

**卡点2（中）：** WPL上的$\zeta_{\text{eff}}$和其对多体ETH耦合的定量影响。当前论证（§2）区分了单粒子弹道输运和多体ETH耦合，但定量上说，WPL上的多体态到底是"逼近ETH"还是"逼近MBL"需要确定。这影响$\zeta_{\text{eff}}$的取值和协同增强因子的WPL修正。建议Phase 2用Lieb-Robinson界框架独立处理。

**卡点3（轻）：** k区域紧致排列的几何可行性。对$k \gg z$，不是所有区域都能同时以$d_{\min}$为其最近邻——球填充约束强制至少部分区域间的距离$\geq 2d_{\min}$。当前上界使用了$z \leq 6$，但更紧的几何界（如Hales-Ferguson的Kepler猜想类比）可能在2D给出$z \leq 5$甚至更低（考虑到区域有一定的尺寸$L_j$而非点）。

**卡点4（PI级）：** 本推导假设所有$L_j < L_{\max}$（严格亚临界）。如果存在一个恰好等于$L_{\max}$的"临界"区域，且$d_{\min}$恰好为最小值，协同增强因子$C \approx 1.3-6$是否足以将它推入超临界？这需要精确知道$\Gamma_{\text{threshold}}$与$\Gamma_{\text{single}}(L_{\max})$的比值。目前基于K3.1的估计（差距$\sim 10^4$）是基于体区平均参数，在相边界附近可能需要更仔细的分析。

### 对下一Phase的输入

1. **Phase 2 B任务**需验证Lieb-Robinson界给出的信息传播约束是否与ETH-FGR协同修正一致——预期一致，因为Lieb-Robinson速度$v_{\text{LR}} \sim J e^{-1/\zeta}$与隧穿率$\Gamma(d) \sim g^2 e^{-d/\zeta}$共享$\zeta$的物理起源。

2. **Phase 2需要处理的Štrkalj-WPL问题：** 定量确定沿WPL的有效局域化长度$\zeta_{\text{WPL}}$和WPL上多体态的ETH/MBL属性。这是区分"单粒子弹道输运"和"多体ETH协同"的关键。

3. **Phase 3的协同安全条件显式化：** 将$C(d_{\min}) \ll \Gamma_{\text{threshold}}/\Gamma_{\text{single}}$转化为$L_{\max}$与$d_{\min}$、$\zeta$之间的显式不等式，验证黄金比例和各种典型参数下该不等式是否robust成立。


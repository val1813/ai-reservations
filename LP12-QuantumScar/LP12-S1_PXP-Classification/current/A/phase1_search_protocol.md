# Phase 1 穷举搜索协议 — PXP-α QMBS 完整分类

**作者：** A博士（形式攻击者）
**日期：** 2026-06-02
**对应课题：** LP12-S1_PXP-Classification (v1)
**基于文献：** Kerschbaumer et al., PRL 134, 160401 (2025); Commutant Algebras (Caltech, arXiv:2209.03377, 2024); GZ Scar (arXiv:2507.14895, 2025); TL Scars (arXiv:2403.14755, 2024); SPT Scars (arXiv:2512.11216, 2025)

---

## 0. 与 Kerschbaumer (2025) 的精确差异化声明

本协议立意与 Kerschbaumer et al. (PRL 134, 160401) 的 **核心差异** 如下：

| 维度 | Kerschbaumer et al. (2025) | 本协议 (LP12-S1 Phase 1) |
|------|---------------------------|--------------------------|
| **目标** | 发现PXP-α(α=1,2,3)中的多个QMBS家族及其涌现SU(2)代数 | **穷举**PXP-α中全部QMBS家族，检测任何超出SU(2)框架的代数结构 |
| **初始态选择** | 以特定W态构造驱动动力学回复 | 系统性扫描整个Fock基+product态+MPS随机态空间，避免初始态选择偏差 |
| **方法** | 从特定初态出发的动力学回复分析 | 全谱ED→纠缠熵预筛选→代数结构逆向工程的无偏搜索 |
| **尽度声明** | 未声称穷举性 | **明确声称穷举性**（在L≤16、PBC、给定参数域内的严格意义下） |
| **代数框架** | 仅涌现SU(2)代数 | SU(2) + 广义SGA + Temperley-Lieb + 可积边界态 + 未预期新代数 |
| **分类学** | 各家族独立报告 | 统一分类树：每个家族映射到代数结构类别和表示参数 |

**剩余差异化空白摘要：** 即使Kerschbaumer已经发现了所有PXP-α中的SU(2)疤痕家族，本协议将通过系统性全谱搜索验证其完备性，并专门搜索非SU(2)代数疤痕（广义SGA、TL等）。若未发现非SU(2)疤痕，则命题A（SU(2)普适分类）获得支持；若发现，则命题B（非SU(2)疤痕存在）获得证实——这一二分判定是Kerschbaumer未执行的关键步骤。

---

## 1. 子任务1：操作性疤痕判据定义

### 1.1 判据分层体系

四个判据按递进关系排列为**三级过滤**：

```
Level 1（粗筛）: 纠缠熵离群值 ──────────────────────────────→ 候选集 C1
Level 2（精筛）: 谱等距性 + Fidelity revival ──────────────→ 候选集 C2
Level 3（终筛）: 代数结构逆向工程 ──────────────────────────→ 代数分类
```

每个判据给出明确的数学定义和阈值。所有判据的实证可靠性针对 L=12/14/16 的ED可及范围有特别评估。

### 1.2 判据A：纠缠熵离群值判据（Level 1 — 粗筛）

#### 1.2.1 定义

对 PXP-α 模型的完整Hamiltonian H_α,Ω,Δ 做全谱精确对角化（ED），得到全部本征态集合 {|ψ_i⟩, E_i}。

对每个本征态 |ψ_i⟩，计算**半链von Neumann纠缠熵**：

```
S_i = -Tr(ρ_A log ρ_A),   ρ_A = Tr_B(|ψ_i⟩⟨ψ_i|)
```

其中 A = {1, 2, ..., L/2}, B = {L/2+1, ..., L}（左侧半链 vs 右侧半链）。

辅助使用 **Renyi-2纠缠熵** 做交叉验证（对L=12/14/16，Renyi-2对有限尺寸效应更敏感，但可作为稳定性检查）：

```
S_i^{(2)} = -log Tr(ρ_A^2)
```

#### 1.2.2 本底模型

对每个能量 E，建立ETH预期熵：

**(a) 移动窗口法**（主方法）：
以 E_i 为中心构建能量窗口 [E_i - δE, E_i + δE]，窗口宽度 δE 自适应选择以使窗口内包含至少 N_min 个非疤痕本征态：

```
N_min = max(10, ⌊0.05 × D_Hilbert⌋)
```

其中 D_Hilbert 是约束后Hilbert空间维度。在该窗口内计算：
- 熵均值 μ_S(E_i) = (1/N_win) Σ_{j∈win} S_j
- 熵标准差 σ_S(E_i)

**(b) 热熵密度插值法**（辅助方法）：
在全能谱范围内，用微正则系综计算热熵密度 s_th(e)（e = E/L 为能量密度）：

```
S_th(E) = s_th(e) × (L/2)  （半链热熵 = 熵密度 × 子系统体积）
```

其中 s_th(e) 通过计算满足约束的微正则态的Page熵获得：

对于约束系统，精确Page熵公式为：
```
S_Page = ln d_A - d_A/(2d_B)    （当 d_A ≤ d_B）
```
其中 d_A = dim(H_A) 是子系统满足约束的Hilbert空间维度。
但此处子系统与整体的约束耦合，不能简单用Page公式的独立维度。因此更可靠的方法是直接取窗口中所有本征态熵的平均值作为ETH预期。

#### 1.2.3 离群值阈值

一个本征态 |ψ_i⟩ 被标记为疤痕候选（进入C1）需同时满足：

**(a) σ阈值**（统计学显著性）：
```
S_i < μ_S(E_i) - n_σ · σ_S(E_i),    n_σ = 3.0
```

**(b) 相对阈值**（绝对偏离）：
```
S_i / S_th(E_i) < r_cut,    r_cut = 0.6
```
即熵不超过热期望的60%。

**(c) 稳定性条件**（消除边缘效应）：
排除谱两端各 5% 的本征态（基态附近和最高激发态附近），因为在这些区域ETH的适用性存疑，且边界态的纠缠较小可能被误判为疤痕。

#### 1.2.4 多分区交叉验证

为避免半链切分位置的人为性，对 L=12/14/16 分别尝试三种切分：
- A:B = L/2 : L/2 （对称二分）
- A:B = ⌊L/3⌋ : L-⌊L/3⌋ （1/3-2/3）
- A:B = ⌊L/4⌋ : L-⌊L/4⌋ （1/4-3/4）

仅当在至少两种切分下满足离群条件时，该态才进入C1。

#### 1.2.5 L≤16可靠性评估

**可靠性：高**（3/5星）
- 纠缠熵离群检测在约束自旋模型中已验证有效（Turner et al. 2018, Kerschbaumer 2025）
- 但L=12时仅377个态（α=1 PBC），统计样本小→σ_S(E)估计有显著不确定性
- L=16时2584个态，统计量改善但仍有限
- **缓解方案：** 合并(Ω,Δ)参数网格上的所有ED数据共分析，而非单一点分析

### 1.3 判据B：谱等距性判据（Level 2 — 精筛）

#### 1.3.1 定义

对候选集 C1 中的态，进行能量值聚类分析。若一组本征态 {|ψ_k⟩: k=0,...,K-1} 满足近似等距谱条件，则称它们构成一个 **候选疤痕塔**。

设该组态的能量为 {E_0 < E_1 < ... < E_{K-1}}，定义能级间距序列：

```
ΔE_k = E_{k+1} - E_k,   k = 0, 1, ..., K-2
```

#### 1.3.2 等距质量因子

定义**谱等距性质量因子**：

```
Q_equi = mean(ΔE_k) / std(ΔE_k)
```

物理意义：Q_equi 是信号（等距间距均值）与噪声（间距波动）之比。

**阈值：**
- Q_equi > 5：强等距信号，确认为疤痕塔候选
- 3 < Q_equi ≤ 5：弱等距信号，需辅助判据确认
- Q_equi ≤ 3：不认定为疤痕塔

#### 1.3.3 谱密度傅里叶分析法（辅助）

计算全能谱的能级关联函数：

```
R(ω) = |Σ_i δ(E - E_i) · w(E_i)| 的傅里叶变换功率谱
```

其中 w(E_i) 是能量窗口权重函数（如高斯包络）。等距塔会在 ω = ω_tower 处产生尖锐峰。此方法能检测出肉眼难以发现的稀疏等距序列。

阈值：在功率谱中检测显著高于本底（> 3σ_noise）的峰值，并检查该峰值对应的态是否在C1中。

#### 1.3.4 工程约束

- 疤痕塔至少需要 K ≥ 3 个态才能定义等距性（K=2无法区分等距vs偶然简并）
- 当K极小（如K=3）时，放宽Q_equi阈值至3
- 对于孤立疤痕态（单态，不属于任何塔），不等距判据不适用，直接保留到代数结构判据

#### 1.3.5 L≤16可靠性评估

**可靠性：中高**（4/5星）
- 等距性在有限尺寸下受边界效应影响较弱，因为它是全局谱特征
- 但低能级（特别是基态附近）的能级可能因对称性简并显得"看似等距"
- **缓解方案：** 检查等距序列是否具有明确的角动量量子数k的二次型E_k ∝ k(2j+1-k)特征

### 1.4 判据C：Fidelity Revival判据（Level 2 — 精筛辅助）

#### 1.4.1 定义

对每个候选初始态 |ψ_0⟩（来自搜索空间中的初始态，见子任务2），计算动力学回复：

```
F(t) = |⟨ψ_0| e^{-iHt} |ψ_0⟩|^2
```

在 L≤16 下，F(t) 可通过完整谱分解精确计算：

```
F(t) = |Σ_n |c_n|^2 e^{-iE_n t}|^2,   c_n = ⟨ψ_0|E_n⟩
```

#### 1.4.2 回复质量度量

**(a) 最大回复因子**：
```
R_max = [max_{t > t_min} F(t)] / F_∞
```
其中 F_∞ = Σ_n |c_n|^4 是无限时间平均（对角线系综），t_min = 2π/Ω 避免t=0的平凡回复。

**(b) 回复高度阈值**：
```
R_max > 5     （回复比热期望高5倍）
```
且绝对回复高度：
```
max_{t > t_min} F(t) > 0.3
```

**(c) 回复周期性**：
若回复随时间近似周期性的（多个等间距回复峰），进一步支持疤痕塔解释。

#### 1.4.3 初始态依赖性

- 对 C2 中的每个候选疤痕塔，计算其塔中所有态的相干叠加 |ψ_scar⟩ = Σ_k α_k |ψ_k⟩
- 构造使回复最大化的 α_k 组合
- 若存在显著的回复（R_max > 5），且初始态不是特定精细调谐的，则该塔具有动力学相关性

#### 1.4.4 L≤16可靠性评估

**可靠性：中**（3/5星）
- 小系统的回复容易被有限尺寸伪影增强（准周期行为不足以证明QMBS）
- 但结合谱等距性可以过滤大部分假阳性
- 对于 L=12 的最小系统，回复F(t)的模态丰富性受限，需谨慎解读

### 1.5 判据D：代数结构判据（Level 3 — 终筛与分类）

#### 1.5.1 一般化谱生成代数（SGA）定义

如果存在一组Hermitian算子 {H_0, H_+, H_-} 作用在疤痕子空间上，满足：

```
[H_0, H_±] = ±ω H_±
[H_+, H_-] = 2ω H_0 + 小修正
```

则称该疤痕子空间具有**近似谱生成代数**（SGA）结构。

对于SU(2)情形，ω = 1（无量纲化）且对易关系严格满足 su(2) Lie代数：

```
[H_0, H_±] = ±H_±
[H_+, H_-] = 2H_0
```

疤痕态构成自旋j表示：H_0|m⟩ = (j-m)|m⟩, H_±|m⟩ ∝ |m±1⟩。

#### 1.5.2 数值提取梯子算子方法

**核心思想：** 从候选疤痕塔 {|ψ_k⟩} 出发，逆向工程寻找局部算子 L, L† 使得它们在 scars subspace 上的投影表现为梯子算子。

**算法步骤：**

**(a) 梯子算子Ansatz：**
在有限的局部算子基 {O_p} 上展开候选梯子算子：

```
L = Σ_{p=1}^{M} c_p O_p
```

选取O_p的候选集为：
- 所有单位子/双体算子：{X_i, Y_i, Z_i, n_i, X_iX_j, ...} 限制在PXP约束允许的范围内
- 所有相邻弦算子：{σ_i^+ Z_{i+1}...Z_{j-1} σ_j^-}（弦算子，长度为2的整数）
- MPS表示的低秩算子（MPO，bond dimension ≤ 4）
- 总候选数 M ≤ 100（取决于L和α），可完整枚举

**(b) 目标函数：**
最小化算符与梯子对易关系偏差：

```
L[ {c_p} ] = || [H, L] - ω_L L ||^2_F
```

其中 ||·||_F 是Frobenius范数在约束Hilbert空间上的归一化，ω_L 是自由参数。

约束条件：||L||_F = 1（归一化），L 不包含全局常数项。

**(c) 优化策略：**
这是一个非凸二次优化问题。采用交替最小化：
1. 固定 {c_p}，优化 ω_L = Tr(H L L†) / Tr(L L†) （Rayleigh商）
2. 固定 ω_L，优化 {c_p}：这是一个广义特征值问题，直接对角化 M × M 矩阵：
   - 定义矩阵 A_{pq} = Tr( [H, O_p] [H, O_q]^† )
   - 定义矩阵 B_{pq} = Tr( O_p O_q^† )
   - 定义矩阵 C_{pq} = Tr( H O_p O_q^† + O_p O_q^† H )
   - 优化问题变为：(A - ω_L C + ω_L^2 B) c = λ c，取最小λ对应的特征向量

**(d) 梯子验证：**
对找到的L，显式验证梯子作用：
```
⟨ψ_{k+1}| L |ψ_k⟩ 和 ⟨ψ_{k-1}| L^† |ψ_k⟩
```
应非零且与SU(2)预期值一致：⟨ψ_{k+1}| L |ψ_k⟩ = √[(j-k)(j+k+1)]。

**(e) SU(2)代数验证：**
将H投影到疤痕子空间并检查：
```
P_scar H P_scar = constant + ω H_0
```
其中 P_scar = Σ_k |ψ_k⟩⟨ψ_k|。验证 H_0 在疤痕子空间的对角化形式。

#### 1.5.3 广义SGA检测

当标准SU(2)代数不满足时（误差超过阈值 ϵ_th = 0.1），进行以下广义代数测试：

**(a) 广义SGA测试：**
放松对易关系，测试是否存在非SU(2)但闭合的梯度算子代数。检测条件：
```
|| [H_0, H_±] ∓ ω_± H_± || < ϵ_th
|| [H_+, H_-] - 2ω_0 H_0 - c I || < ϵ_th
```
其中 ω_± 和 ω_0 不必相同。

**(b) Temperley-Lieb代数测试：**
若疤痕态数目K较小（K ≤ 4），测试Temperley-Lieb生成元结构。检测条件：存在一组算子 {U_i} 使得：
```
U_i^2 = δ U_i
U_i U_{i±1} U_i = U_i
U_i U_j = U_j U_i  (|i-j| > 1)
```
在疤痕子空间上的投影近似满足这些关系。

**(c) SPT疤痕子空间测试：**
若疤痕态具有明显的对称性保护拓扑（SPT）序特征（如简并的纠缠谱），则标记为SPT疤痕候选（对应Matsui et al. 2025框架）。

#### 1.5.4 代数匹配终止条件

判定流程图：
```
找到的代数近似满足SU(2)? → 是 → 标记为 SU(2)-SGA, 记录 j值
    ↓否
满足广义SGA? → 是 → 标记为广义SGA, 记录 ω_+, ω_-, ω_0
    ↓否
满足Temperley-Lieb? → 是 → 标记为 TL-Scar, 记录 δ 值
    ↓否
满足SPT特征? → 是 → 标记为 SPT-Scar
    ↓否
→ 标记为"未归类疤痕"，需要独立深入分析
```

#### 1.5.5 L≤16可靠性评估

**可靠性：中高**（4/5星）
- 代数结构检测在L=14/16时已可获得有意义的收敛结果
- 主要限制：局部算子基的完整性（M=100可能不足以捕获长程关联的代数结构）
- cross-check: 增加 M 观察误差是否显著下降

### 1.6 判据可靠性汇总

| 判据 | L=12 | L=14 | L=16 | 综合评级 |
|------|------|------|------|---------|
| A: 纠缠熵离群值 | ★★★ | ★★★ | ★★★★ | 高 |
| B: 谱等距性 | ★★★★ | ★★★★ | ★★★★★ | 中高 |
| C: Fidelity Revival | ★★★ | ★★★ | ★★★★ | 中 |
| D: 代数结构 | ★★★ | ★★★★ | ★★★★ | 中高 |

**特别说明：** L≤16的固有限制意味着判据的可靠性无法通过增大系统尺寸来验证。因此Phase 2的数值结果必须辅以： (a) L=8/10的完整验证（全同参数下检查小系统趋势一致性）(b) 与Kerschbaumer 2025结果交叉比对（作为外部验证标准）。

---

## 2. 子任务2：完整搜索空间定义

### 2.1 模型哈密顿量

#### 2.1.1 PXP-α一般形式

```
H_α(Ω, Δ) = Σ_{i=1}^{L} P_i^{(α)} (Ω X_i + Δ n_i) P_i^{(α)}
```

其中：
- X_i = σ_i^x + σ_i^x† (Rabi耦合)
- n_i = (1 + σ_i^z)/2 = |1⟩⟨1|_i (占据数)
- P_i^{(α)} = Π_{j: 1 ≤ |i-j| ≤ α} (1 - n_j)   [封锁范围内无激发]
- α = 1, 2, 3 分别为最近邻/次近邻/第三近邻封锁

#### 2.1.2 等价记号（与Kerschbaumer 2025对接）

Kerschbaumer使用的形式是：
```
H_α = Σ_j P_{j-α}...P_{j-1} σ_j^x P_{j+1}...P_{j+α}
```
即仅保留Ω项（Δ=0）且用 σ^x 而非 X_i。在我们的约定中，X_i = σ_i^x（实矩阵），两者等价。

我们增加Δ n_i项（detuning），这是实验上的标准参数（Rydberg激光失谐）。

### 2.2 边界条件和系统尺寸

| 参数 | 值 |
|------|-----|
| 边界条件 | 周期边界条件（PBC） |
| 系统尺寸 L | 12, 14, 16 |
| 更多尺寸检查 | 8, 10（验证大小趋势一致性） |

PBC的选择理由：
- 消除边界效应，使纠缠熵切分更干净
- 与Kerschbaumer 2025的PBC设置一致
- 但PBC下Hilbert空间维度略小（周期性约束减少部分态）

OBC辅助：对关键发现，额外做OBC L=12,14,16验证，确保发现的疤痕非PBC伪影。

### 2.3 约束Hilbert空间维度

#### 2.3.1 精确维度计算

PXP-α约束：每个激发位点i周围α个邻居必须为空（|0⟩）。

**(a) OBC维度 — 递推关系：**

对于 α=1（Fibonacci）：dim_α=1(L) = F_{L+2}
- 递推：d_L = d_{L-1} + d_{L-2}
- 基：d_0 = 1, d_1 = 2

对于 α=2（广义Fibonacci）：dim_α=2(L) 满足 d_L = d_{L-1} + d_{L-3}
- 基：d_0 = 1, d_1 = 2, d_2 = 3

对于 α=3：d_L = d_{L-1} + d_{L-4}
- 基：d_0 = 1, d_1 = 2, d_2 = 3, d_3 = 4

**(b) PBC维度：**

PBC下需要额外考虑周期性边界跨越封锁区的约束。精确维度需通过转移矩阵法计算。对于 α=1，PBC维度 = F_{L-1} + F_{L+1}。

#### 2.3.2 各参数下的维度明细表

| α | L | OBC维度 | PBC维度 | 完整2^L空间 | 压缩因子 |
|---|---|---------|---------|------------|---------|
| 1 | 12 | F_14 = 377 | F_11+F_13 = 322 | 4096 | ~12.7x |
| 1 | 14 | F_16 = 987 | F_13+F_15 = 843 | 16384 | ~19.4x |
| 1 | 16 | F_18 = 2584 | F_15+F_17 = 2207 | 65536 | ~29.7x |
| 2 | 12 | 129 | ~112* | 4096 | ~36.6x |
| 2 | 14 | 277 | ~248* | 16384 | ~66.1x |
| 2 | 16 | 595 | ~544* | 65536 | ~120.5x |
| 3 | 12 | 69 | ~62* | 4096 | ~66.1x |
| 3 | 14 | 131 | ~120* | 16384 | ~136.5x |
| 3 | 16 | 250 | ~232* | 65536 | ~282.5x |

*PBC维度带 * 号为估计值（来自递推在L ≤ 2α+2时的边界修正），精确值需通过转移矩阵精确计算。

**最大矩阵维度：** α=1, L=16, PBC: ~2207维。全谱ED可直接计算（无需求助于Lanczos），获取全部本征态和本征矢。

### 2.4 初始态空间（用于动力学回复检查）

初始态分为四个层次：

#### 2.4.1 层次A：所有Fock基态（约束空间完全基）

约束Hilbert空间的所有计算基矢 |s_1 s_2 ... s_L⟩（s_i ∈ {0,1}，满足PXP-α约束）。

**数量：** 等于各D_Hilbert（见上表）。
**目的：** 洗脱初始态选择偏差。每个基矢都是潜在的疤痕初始态。

#### 2.4.2 层次B：所有product态（满足PXP约束的直积态）

与层次A相同（在约束下Fock基=product态），但额外包括：
- 少数不满足约束但"近乎满足"的初始态（如果实验上容易准备的话，不考虑）--- 忽略
- 注意：在PXP-α约束下，product态必须满足约束条件

#### 2.4.3 层次C：W态类型（Kerschbaumer 2025）

Kerschbaumer引入的弱纠缠初始态族：

```
|W_M⟩ = ⊗_{k=1}^{M} [ |0⟩_⊗A ⊗ |W⟩_B ]
```

其中：
- M × (A+B) = L（系统尺寸被均匀分割为M个单元）
- |W⟩_B = (1/√B)( |10...0⟩ + |01...0⟩ + ... + |0...01⟩ )  长度为B的W态
- |0⟩_⊗A = A个连续的|0⟩

对于α=1, A=B=1：|W_M⟩ = (|01⟩ + |10⟩)^⊗(L/2) / 2^{L/4}（但需检查是否满足约束）
对于α=2, A=2, B=2：|W_{L/4}⟩
对于α=3, A=3, B=3：|W_{L/6}⟩

更一般地，探索A ∈ {α, α+1}, B ∈ {α, α+1}的组合。

#### 2.4.4 层次D：随机MPS态

从均匀分布随机采样的MPS态，bond dimension χ ∈ {2, 3, 4}。

生成方法：对每个虚拟指标维度χ，随机取张量A^{[i]}_{α_i, β_i}的每个元素为均匀独立同分布U[-1,1]后归一化。

采样数量：每个χ采样 N_MPS = min(1000, 10 × D_Hilbert) 个随机MPS态（受限于计算资源）。

**初始态总数估算（α=1, L=16）：**
- 层次A+B: 2207
- 层次C: ~100（不同A,B组合及平移）
- 层次D: min(1000, 22070) = 1000
- 总计: ~3307个初始态
- 每个初始态做ED谱分解F(t)计算：可在数十分钟内完成（2207×2207矩阵对角化一次，然后对每个初态只需做向量内积）

### 2.5 参数空间

#### 2.5.1 原始参数

| 参数 | 符号 | 范围 | 说明 |
|------|------|------|------|
| Rabi频率 | Ω | 1 （固定能量单位） | 仅设定能量尺度，不失一般性 |
| Detuning | Δ | [-10Ω, 10Ω] | 物理相关范围 |
| 封锁范围 | α | {1, 2, 3} | 已确认Kerschbaumer研究范围 |

Ω固定为1的理由：对于H_α(Ω,Δ)，整体能量单位可自由选取。将Ω固定后，Δ成为唯一自由参数。Hamiltonian可写为：

```
H_α(Δ) = Σ_i P_i^{(α)} (X_i + Δ n_i) P_i^{(α)}
```

#### 2.5.2 离散扫描网格

| Δ/Ω区间 | 网格步长 | 网格点数 | 备注 |
|----------|---------|---------|------|
| [-1, 1] | 0.1 | 21 | 共振区精细扫描 |
| [-5, -1) ∪ (1, 5] | 0.5 | 16 | 中距非共振区 |
| [-10, -5) ∪ (5, 10] | 1.0 | 10 | 远共振区粗扫 |
| Δ/Ω → ±∞ (Ising极限) | — | 2 (Δ=±10⁴) | 极限点检查 |

**总网格点数：** 21 + 16 + 10 + 2 = **49 个 Δ 点** × 3 个 α = **147 套 ED 计算**

对应 L=12,14,16 各三套 → 3 × 147 = 441 次完整全谱ED。

#### 2.5.3 特殊关注参数点

| 参数点 | (α, Δ/Ω) | 预期发现 |
|--------|----------|---------|
| 标准PXP共振点 | (1, 0) | 经典QMBS塔（Turner 2018） |
| Kerschbaumer A点 | (2, 0) | α=2 SU(2)塔 |
| Kerschbaumer B点 | (3, 0) | α=3 SU(2)塔 |
| 非共振检查点 | (1, 1.5) | Δ引入后疤痕性变化 |
| 强失谐极限 | (1, 100) | Ising极限，0阶疤痕塔显现 |
| 广义SGA预测点 | (1, -2.5) | 可能非SU(2)代数结构区域 |
| TL代数检查点 | (2, 0) | TL疤痕是否存在？ |

### 2.6 对称性约化

为了减少计算负担并简化分类，利用对称性将Hilbert空间分块：

| 对称性 | 操作 | 块数 | 备注 |
|--------|------|------|------|
| 平移不变性 | T: |i⟩ → |i+1⟩ | L | PBC下可Bloch分解 |
| 空间反演 | P: |i⟩ → |L-i+1⟩ | 2 | 结合平移使用 |
| 粒子-空穴 | C: n_i → 1-n_i | 2 | 仅在Δ=0时有效 |
| 时间反演 | T: i → -i | 实哈密顿量自动实 | — |

ED在最大对称性约化块中进行，每个块维度应不超过 ~500（L=16时）。这对于完全对角化是可行的。

---

## 3. 子任务3：搜索算法 + 分类树设计

### 3.1 算法总流程图

```
 ┌──────────────────────────────────────────────────────────┐
 │               Phase 2 ED 数值穷举搜索                      │
 └──────────────────────────────────────────────────────────┘
                              │
                              ▼
            ┌──────────────────────────────────┐
            │  Step 0: 预计算                  │
            │  ──────────────────               │
            │  - 构建约束Hilbert空间基矢集合     │
            │  - 构建对称约化分块                │
            │  - 每个(α,Δ)点全谱ED              │
            └──────────────────────────────────┘
                              │
                              ▼
            ┌──────────────────────────────────┐
            │  Step 1: 纠缠熵筛选 → C1          │
            │  ──────────────────               │
            │  对全部本征态:                     │
            │  1. 计算 S_i (von Neumann)        │
            │  2. 能量窗口统计 → μ_S(E), σ_S(E) │
            │  3. 离群检测 → 候选集 C1          │
            │  4. 多分区交叉验证                 │
            └──────────────────────────────────┘
                              │
                              ▼
            ┌──────────────────────────────────┐
            │  Step 2: 谱等距性 + 回复 → C2    │
            │  ──────────────────               │
            │  对C1聚类:                        │
            │  1. 能量聚类 → 候选塔 {T_k}       │
            │  2. 计算Q_equi → 筛选塔           │
            │  3. 层次A初始态F(t) → 回复检测     │
            │  4. 更新C2 = 保留态               │
            └──────────────────────────────────┘
                              │
                              ▼
       ┌──────────────────────────────────────────┐
       │  Step 3: 代数结构表征                     │
       │  ──────────────────                       │
       │  对C2中每个塔:                            │
       │  1. 梯子算子优化 → 求L, L†                │
       │  2. 代数类型判定（分类树）                  │
       │  3. 未归类态单独分析                       │
       └──────────────────────────────────────────┘
                              │
                              ▼
       ┌──────────────────────────────────────────┐
       │  Step 4: 穷举性检查                       │
       │  ──────────────────                       │
       │  1. 回溯检查C1/C2间隙                    │
       │  2. 检查整个Ω-Δ-α参数空间覆盖              │
       │  3. 异常态再分析                           │
       │  4. 最终声明穷举性（或报告后选区域）         │
       └──────────────────────────────────────────┘
```

### 3.2 Step 0：预计算（基线准备）

**输入：** (α, Δ/Ω) 参数网格点
**输出：** 全部本征值 {E_i} 和本征矢 {|ψ_i⟩}，以及各对称性扇区标记

```
for each α in {1, 2, 3}:
    for each Δ in scan_grid:
        // 基矢生成
        basis_α,L = generate_constrained_basis(L, α, boundary="PBC")
        
        // Hamiltonian构建
        H = build_Hamiltonian(basis_α,L, Ω=1, Δ)
        
        // 对称性约化（仅报告维度，无需实际分块）
        blocks = decompose_by_symmetry(H, translations, parity)
        
        // 全谱ED
        for each block in blocks:
            {E_i, |ψ_i⟩} = full_diagonalize(block)
        
        // 存储结果
        save_eigensystem({E_i, |ψ_i⟩}, symmetry_quantum_numbers)
```

**计算复杂度估算（最坏情况 α=1, L=16, PBC, D=2207）：**
- 构建H: O(D^2 × L) ~ 2207^2 × 16 ≈ 7.8×10^7 操作
- 全谱ED: O(D^3) ~ 2207^3 ≈ 1.07×10^10 操作
- 对称约化后最坏块维度 ~500: O(500^3) = 1.25×10^8 操作 × ~10个块 ≈ 1.25×10^9
- 每个参数点: 约数分钟（现代工作站）
- 全部147点 × 3尺寸: 约 147 × 3 × 3min ≈ 22小时

### 3.3 Step 1：纠缠熵离群筛选 → 候选集 C1

#### 伪代码：

```
Algorithm: Entanglement_Outlier_Detection

Input: 全部本征态 {|ψ_i⟩, E_i} for given (α, L, Δ)
Output: 候选集 C1 = {i: |ψ_i⟩ is scar candidate}

Parameters:
    n_σ = 3.0         // sigma threshold
    r_cut = 0.6       // relative entropy threshold
    α_partitions = {0.5, 0.33, 0.25}  // partition ratios

Procedure:
    C1 = empty set
    
    for each partition_ratio in α_partitions:
        define A = first N = floor(partition_ratio × L) sites
        B = remaining sites
        
        for each i:
            ρ_A = partial_trace(|ψ_i⟩⟨ψ_i|, A, B)
            S_i[ratio] = -Tr(ρ_A log ρ_A)
        
        // Energy windows
        E_min = min(E_i), E_max = max(E_i)
        N_win = max(10, 0.05 × D_Hilbert)
        window_width = (E_max - E_min) / (D_Hilbert / N_win)
        
        for each energy window W centered at E:
            states_in_W = {i: E_i ∈ [E - window_width/2, E + window_width/2]}
            μ_S = mean({S_j[ratio]: j ∈ states_in_W})
            σ_S = std({S_j[ratio]: j ∈ states_in_W})
            
            for each i in states_in_W:
                if S_i[ratio] < μ_S - n_σ × σ_S:
                    mark_as_outlier(i, ratio)
    
    // Cross-partition validation
    for each i:
        count = number of ratios where i is outlier
        if count >= 2:
            // Check relative threshold
            E_i_frac = (E_i - E_min) / (E_max - E_min)
            if E_i_frac > 0.05 and E_i_frac < 0.95:
                C1 = C1 ∪ {i}
    
    // Remove trivial scar candidates (ground state band)
    C1 = C1 \ detect_ground_state_band()
    
    return C1
```

#### C1预期规模估算：
- 对于 α=1, L=12, D=322: 谱中通常有 ~1-3个疤痕塔，每个塔 3-5 个态 → C1约 3-15 个态（~1-5%）
- 对于 α=2/3，由于约束更强，疤痕态占比可能略高
- C1 应远小于总谱尺寸，确保后续步骤可计算

### 3.4 Step 2：谱等距性 + Fidelity Revival → 候选集 C2

#### 3.4.1 能量聚类子算法

```
Algorithm: Energy_Clustering

Input: C1 = {i_1, i_2, ..., i_M} with energies {E_{i_1}, ..., E_{i_M}}
Output: 塔集合 {T_k}，每个塔是本征态索引的有序序列

Procedure:
    // 1. 排序
    sorted_indices = sort(C1 by E_i ascending)
    
    // 2. 聚类：按能量间隙切割
    gaps = [E_{next} - E_{current} for consecutive pairs]
    mean_gap = mean(gaps)
    std_gap = std(gaps)
    cut_threshold = mean_gap - 0.5 × std_gap  // 较平均间隙小的归为同一塔
    // 实际上，塔内间隙应显著小于塔间间隙
    
    // 3. 层次聚类（更稳健）
    clusters = single_linkage_clustering({E_i}, 
                                         distance_threshold = max(mean_gap/2, 3*min_gap))
    
    // 4. 筛选有效塔：K ≥ 3
    towers = {cluster: |cluster| >= 3}
    
    return towers
```

#### 3.4.2 谱等距性子算法

```
Algorithm: Spectral_Equidistance_Check

Input: 塔 T = {E_0, E_1, ..., E_{K-1}}  (sorted)
Output: Q_equi 和通过/不通过判定

Procedure:
    if K < 3:
        return (0, FAIL)   // 无法评估等距性
    
    ΔE = [E_{k+1} - E_k for k = 0 to K-2]
    mean_ΔE = mean(ΔE)
    std_ΔE = std(ΔE)
    
    if std_ΔE < 1e-10:
        return (∞, PASS)   // 完全等距
    
    Q_equi = mean_ΔE / std_ΔE
    
    // 辅助：等距偏差百分比
    deviation_pct = max_k |ΔE_k - mean_ΔE| / mean_ΔE × 100%
    
    if Q_equi >= 5 and deviation_pct <= 20%:
        return (Q_equi, PASS)
    elif Q_equi >= 3 and K >= 4:
        return (Q_equi, PASS_WEAK)
    else:
        return (Q_equi, FAIL)
```

#### 3.4.3 Fidelity Revival子算法

```
Algorithm: Fidelity_Revival_Check

Input: Hamiltonian H, 初始态集初始态集 {|ψ_0⟩} (层次A-D), 时间范围 [0, T_max]
Output: 每个初始态的回复质量 R_max 和回复峰位置

Procedure:
    T_max = 10 × (2π/Ω)  // 10个Rabi振荡周期
    N_t = 2000            // 时间步数
    
    // 预先计算谱分解（仅一次）
    {E_n, |E_n⟩} = full_diagonalize(H)
    
    for each |ψ_0⟩ in initial_states:
        c_n = ⟨E_n|ψ_0⟩
        
        for t in linspace(0, T_max, N_t):
            F(t) = |Σ_n |c_n|^2 e^{-iE_n t}|^2
        
        F_∞ = Σ_n |c_n|^4
        t_min = 2π/Ω
        
        F_peaks = find_peaks(F(t) for t > t_min)
        if F_peaks is not empty:
            R_max = max(F_peaks) / F_∞
            max_revival = max(F_peaks)
        else:
            R_max = 0
            max_revival = 0
        
        if R_max > 5 and max_revival > 0.3:
            mark_as_reviving(|ψ_0⟩, R_max, peak_times)
```

#### 3.4.4 C2构造

```
C2 = {|ψ_i⟩ ∈ C1: |ψ_i⟩ ∈ some tower T with Q_equi(T) ≥ 3}
      ∪ {|ψ_i⟩ ∈ C1: |ψ_i⟩ is orthogonal component of reviving initial state}
```

#### 3.4.5 特殊处理：孤立疤痕态

对满足以下条件的孤立态（不属于任何塔，K=1）：
1. 纠缠熵显著低于ETH预测（S_i / S_th < 0.3）
2. 从某些初始态（如W态）出发的F(t)具有长时段的高保真度
3. 代数检测中显示非平凡的局部关联结构

这些孤立态不通过Step 2的塔筛选，但直接进入Step 3的代数分析。

### 3.5 Step 3：代数结构表征与分类树

#### 3.5.1 梯子算子优化子算法

```
Algorithm: Ladder_Operator_Optimization

Input: 候选疤痕塔 T = {|ψ_0⟩, ..., |ψ_{K-1}⟩} with energies {E_k}
       局部算子基 {O_p: p=1,...,M}
Output: 最优梯子算子 L，代数类型标签

Parameters:
    ϵ_algebra = 0.1    // 代数拟合容差

Procedure:
    // 1. 构建投影到疤痕子空间的 Hamiltonian
    P = Σ_k |ψ_k⟩⟨ψ_k|
    H_scar = P H P
    
    // 2. 检查 H_scar 是否近似具有谐振子或SU(2)谱
    E_diag = diag(H_scar)  // 应该恢复 {E_k}
    
    // 3. 能量梯子算子优化
    for each O_p:
        ω_p = Tr(H O_p O_p^†) / Tr(O_p O_p^†)   // Rayleigh商
        ϵ_p = || [H, O_p] - ω_p O_p || / ||O_p||
        store (ϵ_p, ω_p)
    
    // 4. 选取最优初始猜测
    best_single = argmin_p ϵ_p
    L_0 = O_{best_single}
    
    // 5. 联合优化（多算子组合）
    // 构建矩阵 A, B, C (见 1.5.2(c))
    solve_generalized_eigenvalue(A - ω C + ω^2 B) c = λ c
    L_opt = Σ_p c_p O_p  （取最小本征值λ对应的c）
    
    if λ < ϵ_algebra^2:
        // 成功找到梯子算子
        verify_ladder_action(L_opt, T)
    else:
        // 尝试更大M的算子基
        expand_operator_basis()
        retry()
    
    // 6. 代数类型判定 → 分类树路由
    algebra_type = classify_algebra(L_opt, H, T)
    
    return L_opt, algebra_type
```

#### 3.5.2 分类树路由算法

```
Algorithm: Classify_Algebra

Input: L, H, T = {|ψ_k⟩}
Output: 代数类型标签 + 参数

Procedure:
    // 0. 从 L 构造 H_0 = [L, L†] (归一化后)
    //    验证 [H, L] ≈ -ω L
    
    N = L†L - LL†  (或 L†L + LL† 的适当组合)
    
    // 1. 测试 SU(2) 代数
    error_su2 = 0
    error_su2 += || [H, L] + ω L ||^2     // 梯子对易
    error_su2 += || [H, L†] - ω L† ||^2
    error_su2 += || [L, L†] - 2N ||^2     // Cartan对易
    error_su2 += || [N, L] + L ||^2        // 权值对易
    error_su2 = sqrt(error_su2 / 4)
    
    if error_su2 < ϵ_algebra (=0.1):
        // 检查spin j值
        j_estimate = (K - 1) / 2
        tower_length_match = (2*j_estimate + 1 ≈ K)
        return SU2(j=j_estimate, ω=ω)
    
    // 2. 测试广义SGA
    //    放松SU(2)结构，检测任意二阶闭合代数
    //    寻找 H_0, H_+, H_- 封闭子代数
    error_gsga = test_generalized_SGA(H, L, T)
    if error_gsga < ϵ_algebra:
        ω_+, ω_-, ω_0 = extract_gsga_params()
        return GENERALIZED_SGA(ω_+, ω_-, ω_0)
    
    // 3. 测试 Temperley-Lieb
    error_tl = test_TL_algebra(T, L_opt, H)
    if error_tl < ϵ_algebra:
        δ = extract_TL_delta()
        return TEMPERLEY_LIEB(δ=δ)
    
    // 4. 测试 SPT scar
    if has_SPT_signature(T):
        return SPT_PROTECTED
    
    // 5. 未归类
    return UNCLASSIFIED(need_deep_analysis=True)
```

#### 3.5.3 未归类疤痕的深度分析

对标记为 UNCLASSIFIED 的态执行：

```
Protocol: Deep_Analysis_Unclassified

1. 检查是否是已知对称性保护的态（如平移不变性导致的简并）
2. 计算rung纠缠谱（entanglement spectrum）→ 寻找拓扑特征
3. 计算互信息 I(A:B) 的范数 → 寻找长程关联
4. 构建超胞 Hamiltonian（L=2×原始尺寸）→ 检查是否是折叠BZ效应
5. 检查与已知可积模型的关联
6. 如果以上全部未归类 → 声明"新代数结构候选"
```

### 3.6 Step 4：穷举性检查

#### 3.6.1 回溯检查

```
Algorithm: Exhaustiveness_Check

目的：验证C1/C2没有遗漏，且参数空间已被充分覆盖

1. **低门槛回溯：** 将n_σ降至2.0重新运行Step 1
   → 新态若进入C1'但不在C2，检查它们是否是"假性疤痕"（即纠缠熵稍低但无代数结构）
   → 若存在有意义的态被遗漏，标记为"边缘疤痕"，记录在附录中

2. **高门槛对偶检查：** 将Q_equi阈值从5降至3重新运行Step 2
   → 发现更多候选塔，检查这些弱等距塔是否具有代数结构
   → 若存在有代数结构的弱等距塔，则原阈值过于严格

3. **参数插值检查：** 在网格点之间的中点做插值ED
   → 若(α,Δ)点上的疤痕结构在相邻点间连续变化，则网格分辨率充足
   → 若发现突变（某些疤痕在相邻网格点间消失），在间隙处加密扫描

4. **交叉验证：** 用Kerschbaumer 2025报告的所有已知QMBS家族
   → 检查协议是否能自动恢复所有已知疤痕
   → 已知家族的恢复率 = 穷举搜索灵敏度
```

#### 3.6.2 已知家族的恢复验证

| Kerschbaumer家族 | α | 预期位置 | 协议应能恢复？ | 验证条件 |
|-----------------|---|---------|--------------|---------|
| 标准PXP疤痕塔 | 1 | 谱中部~0.5Ω | 是 | C1自动捕获，Q_equi > 10 |
| α=2族A | 2 | 依赖于W态 | 是 | 层次C初态→回复→C2 |
| α=2族B | 2 | 次要家族 | 是（如果存在） | C1+Q_equi | 
| α=3族A | 3 | 依赖于W态 | 是 | 层次C初态→回复→C2 |

#### 3.6.3 最终穷举声明格式

穷举性声明将按以下模板报告：

```
穷举性声明 — (α=?, L=?, Δ=?)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
已搜索参数空间：{参数描述}
总Hilbert空间维度：D = ?
纠缠熵筛选阈值：n_σ = 3.0, r_cut = 0.6
谱等距筛选阈值：Q_equi ≥ 3
初始态测试数量：N_init = ?
代数拟合容差：ϵ = 0.1

发现的疤痕塔：{K_tower}个
  - SU(2)-SGA: {N_SU2}个（j值: ...）
  - 广义SGA: {N_GSGA}个
  - TL: {N_TL}个
  - SPT: {N_SPT}个
  - 未归类: {N_UN}个
  - 总计: {N_SU2 + N_GSGA + N_TL + N_SPT + N_UN}

回溯验证：
  - 降低n_σ至2.0新增: {M_new}个候选, 其中有意义: {M_sig}个
  - Kerschbaumer已知家族恢复率: {recovery_rate}%
  
穷举性声明：[PASS/FAIL_WITH_GAPS]
  - 通过条件：回溯检查无有意义遗漏 + Kerschbaumer恢复率100%
  - 有条件通过：回溯检查有少量边缘疤痕，但不影响总体分类
  - 不通过：存在系统性的遗漏
```

### 3.7 分类树终态节点定义

```
分类树 — PXP-α QMBS 完整分类
========================================

Level 0: 全体本征态 (D_Hilbert 个)
  │
  ├── Level 1a: ETH热态 (典型本征态，高纠缠熵)
  │
  └── Level 1b: C2疤痕候选 (纠缠熵离群值 + 谱结构)
        │
        ├── Node A: SU(2)-SGA 疤痕
        │     ├── A1: 标准PXP塔 (j=L/2, Δ=0, α=1)
        │     ├── A2: α=2 SU(2)族A (j=?，来自Kerschbaumer)
        │     ├── A3: α=2 SU(2)族B
        │     ├── A4: α=3 SU(2)族A
        │     └── A5: 新发现的SU(2)家族 (如有)
        │
        ├── Node B: 广义SGA 疤痕
        │     ├── B1: GZ型广义SGA (非等距梯子)
        │     └── B2: RSGA型 (交错等距塔)
        │
        ├── Node C: Temperley-Lieb 疤痕
        │     └── C1: TL-QMBS (如存在)
        │
        ├── Node D: SPT 疤痕
        │     └── D1: SPT保护疤痕子空间
        │
        ├── Node E: 可积边界态疤痕塔
        │     └── E1: 边界态塔 (如存在)
        │
        └── Node F: 未归类疤痕 (需深入分析)
              ├── F1: 可能的新代数
              ├── F2: 有限尺寸伪影
              └── F3: 其他（对称性保护简并等）
```

**节点定义约定：**
- 每个节点关联一组具体的 (α, Δ/Ω, L) 参数
- 每个节点记录代数结构的具体参数 (j, ω, etc.)
- 每个节点标注重现初始态的 properties（保真度回复最小值/最大值）

---

## 4. 预期发现

### 4.1 已被Kerschbaumer (2025)报告的家族（应被自动恢复）

| 家族 | α | 预期 代数类型 | 协议中的发现路径 |
|------|----|-------------|----------------|
| 标准PXP疤痕塔 | 1 | SU(2), j=L/2 | Step 1: 纠缠熵离群; Step 2: Q_equi >> 5; Step 3: 自动匹配SU(2) |
| α=2 弱纠缠W态家族 | 2 | SU(2) | 层次C初始态 → Step 2回复 → Step 3梯子算子 |
| α=3 弱纠缠W态家族 | 3 | SU(2) | 层次C初始态 → Step 2回复 → Step 3梯子算子 |

**可验证假设：** Kerschbaumer的α=2和α=3的W态家族将全部在层次C的初始态回复检测中出现。如果检测不到，则要么W态参数选择不当，要么这些家族的回复质量弱于预期。

### 4.2 潜在非SU(2)疤痕候选特征

根据GZ Scar (Bhowmick & Ho 2025)和Temperley-Lieb疤痕 (Wang et al. 2024)的启示，非SU(2)疤痕在PXP-α中的可能表现：

**(a) 广义SGA疤痕（GZ型）：**
- 特征：能级等距但梯子算子的对易关系偏离SU(2)
- 在PXP-α中可能出现的区域：α=2或3的参数空间
- 识别方法：Step 3中SU(2)测试失败但广义SGA测试通过

**(b) Temperley-Lieb型疤痕：**
- 特征：少量态（K=2-4）组成"闭合"代数，与TL生成元关联
- 在PXP-α中可能出现的条件：α≥2时封锁约束增强，投影算子P_i的集合可能生成TL代数
- 识别方法：TL代数检测（3.5.2步）

**(c) SPT疤痕子空间：**
- 特征：特定动量扇区中的一组保护态，纠缠谱具有拓扑特征
- 在PXP-α中的可能性：大α下系统更接近多个解耦的子链，SPT相更可能出现
- 识别方法：纠缠谱分析

**(d) 零能疤痕（Zero-mode scar）：**
- 特征：在Δ特定取值下出现的孤立零能态
- 识别方法：Level 1的孤立态处理

### 4.3 穷举性假说

穷举搜索的结果将导向三种可能结果之一：

| 结果 | 含义 | 对驱动矛盾的影响 |
|------|------|----------------|
| **全部疤痕 ∈ SU(2)** | PXP-α的所有疤痕态都可归入SU(2)SGA表示 | 支持命题A（SU(2)普适），否定命题B |
| **部分疤痕 ∉ SU(2)** | 存在非SU(2)代数结构的疤痕 | 支持命题B（非SU(2)存在），否定命题A的普适性 |
| **完全新代数** | 发现当前代数框架无法归类的代数结构 | 超越命题A/B二分，导致新型疤痕机制的发现 |

**无偏见预测：** 在有限尺寸下（L≤16），很可能所有发现的疤痕都是SU(2)类型（因为PXP-α的约束结构天然有利于su(2)字称投影），但大型α（特别是α=3）可能有非SU(2)的小型塔。

### 4.4 协议预期灵敏度

| 判据灵敏度 | 真正的 SU(2)疤痕 | 真正的非SU(2)疤痕 | 假阳性（非疤痕） |
|-----------|----------------|-----------------|----------------|
| 纠缠熵离群值 | 100% (已知) | 预计 >95% | 低能基态带可能被误判 |
| 谱等距性 | 100% (等距塔) | >90% | 对称性简并可能误判 |
| Fidelity revival | 100% (适当初态) | 未知（取决于初态） | 准周期有限尺寸效应 |
| 代数结构 | 100% | >80% | 代数拟合可能在随机低纠缠态上也收敛 |

**最可能遗漏：** 非SU(2)疤痕的梯子算子可能具有较长的空间范围，在有限的局部算子基（M≤100）中无法完整表示。

---

## 5. 穷举性论证的局限性声明

### 5.1 固有局限

本协议的穷举性声明伴随以下固有局限性：

| 局限性 | 影响 | 缓解措施 |
|--------|------|---------|
| **L≤16限制：** 热力学极限下的效应可能在小系统上不可见 | 非SU(2)疤痕可能在L→∞时才显现 | Phase 2后将关键发现外推到L=20-24（用稀疏矩阵Lanczos法），检测尺寸趋势 |
| **初始态空间的离散采样：** 层次D的随机MPS态是MPS流形上的有限样本 | 可能遗漏最适初始态 | 用MPS随机样本的回复覆盖度作为统计保证 |
| **参数网格离散化：** Δ/Ω在49个点采样 | 可能遗漏精细调谐的疤痕点 | 特殊关注点 + 回溯插值检查 |
| **局部算子基的有限性：** M≤100的算子基 | 长程梯子算子可能被遗漏 | 逐步增加M值至M=500做收敛性测试 |
| **代数拟合容差ϵ=0.1：** 阈值选择的人为性 | 边缘代数结构可能被误分类 | 在0.05-0.2范围测试ϵ的敏感性 |
| **纠缠熵离群的统计局限性：** L=12时D仅有322 | σ_S(E)的统计估计噪声大 | 多(α,Δ)点联合分析，增加有效统计量 |

### 5.2 声明形式

最终的穷举声明将采用以下限定形式：

> **声明：** 在系统尺寸 L ≤ 16、周期边界条件、参数空间 Δ/Ω ∈ [-10, 10] 离散化扫描下，PXP-α模型（α=1,2,3）的全部QMBS家族已被本协议检出并代数分类。该声明不排除以下可能性：(a) L>16时出现新的疤痕家族 (b) 极窄参数窗口（宽度 < 网格分辨率）中存在未扫描的疤痕 (c) 超出局部算子基M=100的长程代数结构 (d) 热力学极限下某些疤痕的消失。

### 5.3 强度阶梯（在SOP GATE 7的知识图谱备份中应体现）

```
穷举性强度：▶▶▶▶▶▶▶▶◁◁ (80%)
损失主要来自：(1) L=12小系统统计噪声 (2) M=100算子基截断 (3) Δ网格分辨率
```

---

## 附录A：参考实现的伪代码框架

### A.1 约束基生成器

```python
def generate_constrained_basis(L, alpha, boundary='PBC'):
    """
    生成满足PXP-alpha约束的所有计算基矢。
    
    参数:
        L: int — 系统尺寸
        alpha: int — 封锁范围 (1,2,3)
        boundary: str — 'PBC' 或 'OBC'
    
    返回:
        basis: List[int] — 每个int的二进制表示为一个基矢
    """
    from itertools import product
    
    def is_valid(state_tuple):
        """检查给定的二进制tuple是否满足PXP-alpha约束"""
        L = len(state_tuple)
        for i in range(L):
            if state_tuple[i] == 1:
                # 检查所有在封锁范围内的邻居
                for j in range(1, alpha + 1):
                    left = (i - j) % L if boundary == 'PBC' else i - j
                    right = (i + j) % L if boundary == 'PBC' else i + j
                    if boundary == 'PBC':
                        if state_tuple[left] == 1 or state_tuple[right] == 1:
                            return False
                    else:
                        if left >= 0 and state_tuple[left] == 1:
                            return False
                        if right < L and state_tuple[right] == 1:
                            return False
        return True
    
    # 对全2^L空间枚举 + 过滤（L≤16可行）
    basis = []
    for state_int in range(2**L):
        state_tuple = tuple((state_int >> k) & 1 for k in range(L))
        if is_valid(state_tuple):
            basis.append(state_int)
    
    return basis
```

### A.2 Hamiltonian构建器

```python
import numpy as np
from scipy.sparse import lil_matrix, csr_matrix

def build_hamiltonian(basis, L, Omega=1.0, Delta=0.0):
    """
    构建PXP-alpha模型的稀疏Hamiltonian矩阵。
    
    参数:
        basis: List[int] — 约束基
        L: int — 系统尺寸
        Omega: float — Rabi频率
        Delta: float — Detuning
    
    返回:
        H: csr_matrix — 稀疏Hamiltonian
    """
    D = len(basis)
    H = lil_matrix((D, D), dtype=np.complex128)
    
    # 基矢到索引的映射
    state_to_idx = {state: idx for idx, state in enumerate(basis)}
    
    for idx, state_int in enumerate(basis):
        state = [(state_int >> k) & 1 for k in range(L)]
        
        # detuning项: Δ Σ n_i (被P_i保护在内)
        for i in range(L):
            if state[i] == 1:
                H[idx, idx] += Delta  # n_i|1⟩ = 1|1⟩
        
        # Rabi项: Ω Σ P_i X_i P_i
        for i in range(L):
            # P_i = (1-n_{i-1})(1-n_{i+1}) 对所有封锁邻居的乘积
            # ...检查所有α邻居都是0
            block_free = True
            for d in range(1, alpha+1):
                left = (i - d) % L
                right = (i + d) % L
                if state[left] == 1 or state[right] == 1:
                    block_free = False
                    break
            
            if not block_free:
                continue
            
            # X_i作用: 翻转 site i
            new_state = state.copy()
            new_state[i] = 1 - new_state[i]
            new_state_int = sum(new_state[k] << k for k in range(L))
            
            if new_state_int in state_to_idx:
                jdx = state_to_idx[new_state_int]
                H[idx, jdx] += Omega
    
    return H.tocsr()
```

### A.3 纠缠熵计算器

```python
def entanglement_entropy(state_vector, basis, L, partition_size):
    """
    计算一个本征态的von Neumann纠缠熵。
    
    参数:
        state_vector: np.ndarray — 本征态向量（在约束基空间中）
        basis: List[int] — 约束基
        L: int — 系统尺寸
        partition_size: int — A子系统包含的位数
    
    返回:
        S: float — von Neumann熵
    """
    D = len(basis)
    n_A_states = 2**partition_size
    n_B_states = 2**(L - partition_size)
    
    # 构造Schmidt分解
    rho_A = np.zeros((n_A_states, n_A_states), dtype=np.complex128)
    
    for idx, amp in enumerate(state_vector):
        state_int = basis[idx]
        # 分离A和B部分
        A_part = state_int & ((1 << partition_size) - 1)
        B_part = state_int >> partition_size
        
        for jdx, amp2 in enumerate(state_vector):
            state_int2 = basis[jdx]
            A_part2 = state_int2 & ((1 << partition_size) - 1)
            B_part2 = state_int2 >> partition_size
            
            if A_part == A_part2:
                # 只有当B部分相同时的贡献
                # （这里做了简化，实际需要完整的partial trace）
                pass
    
    # 注：实际实现需要对Hilbert空间约束做修正
    # 在约束系统中，A和B的Hilbert空间不是独立的2^{L/2}
    # 需要构建A子系统的约束约化密度矩阵
    
    # ...（完整实现略）
    
    return S
```

### A.4 梯子算子优化器

```python
def optimize_ladder_operator(H, scar_states, local_operators, omega_init=None):
    """
    优化梯子算子 L = Σ c_p O_p 满足 [H, L] ≈ -ω L
    
    参数:
        H: sparse matrix — Hamiltonian
        scar_states: List[ndarray] — 疤痕塔中的本征态
        local_operators: List[sparse matrix] — 局部算子基
        omega_init: float or None — 初始猜测
    
    返回:
        c_opt: ndarray — 最优系数
        omega_opt: float — 最优梯子频率
        error: float — 拟合误差
    """
    M = len(local_operators)
    D = H.shape[0]
    
    # 构建 Frobenius范数相关的矩阵
    # A_{pq} = Tr([H,O_p] [H,O_q]^†)
    # B_{pq} = Tr(O_p O_q^†)
    # C_{pq} = Tr(H O_p O_q^† + O_p O_q^† H)
    
    A = np.zeros((M, M), dtype=np.complex128)
    B = np.zeros((M, M), dtype=np.complex128)
    C = np.zeros((M, M), dtype=np.complex128)
    
    for p in range(M):
        Op = local_operators[p]
        H_Op = H @ Op - Op @ H  # [H, O_p]
        
        for q in range(M):
            Oq = local_operators[q]
            H_Oq = H @ Oq - Oq @ H  # [H, O_q]
            
            A[p,q] = np.trace(H_Op @ H_Oq.conj().T)
            B[p,q] = np.trace(Op @ Oq.conj().T)
            C[p,q] = np.trace(H @ Op @ Oq.conj().T + Op @ Oq.conj().T @ H)
    
    # 迭代优化
    if omega_init is None:
        omega = 1.0  # 单位能量尺度
    else:
        omega = omega_init
    
    for iteration in range(100):
        # 构造广义本征值问题
        M_mat = A - omega * C + omega**2 * B
        
        # 添加归一化约束
        eigenvalues, eigenvectors = eigh(M_mat, B)
        
        # 取最小本征值
        min_idx = np.argmin(np.abs(eigenvalues))
        c = eigenvectors[:, min_idx]
        error = np.abs(eigenvalues[min_idx])
        
        # 更新omega
        c_norm = c.conj().T @ B @ c
        L = sum(c[p] * local_operators[p] for p in range(M))
        omega_new = np.trace(H @ L @ L.conj().T) / np.trace(L @ L.conj().T)
        
        if np.abs(omega - omega_new) < 1e-6:
            omega = omega_new
            break
        
        omega = omega_new
    
    return c, omega, error
```

---

## 附录B：参数空间扫描进度表（Phase 2使用）

| (α, Δ/Ω) | L=12 | L=14 | L=16 | 备注 |
|-----------|------|------|------|------|
| (1, -10) | □ | □ | □ | |
| (1, -9) | □ | □ | □ | |
| ... | □ | □ | □ | |
| (1, 0) | □ | □ | □ | 标准PXP点，基准 |
| ... | □ | □ | □ | |
| (1, 10) | □ | □ | □ | |
| (2, -5) | □ | □ | □ | |
| ... | □ | □ | □ | |
| (3, -10) | □ | □ | □ | |
| ... | □ | □ | □ | 直到 (3, 10) |

总计：147 × 3 = 441 套ED计算。每套生成一个C1/C2/代数分类的摘要报告。

---

## 附录C：与B博士并行工作的接口

B博士将独立从交换子代数框架推导可能的代数结构。本协议与B博士的接口：

1. **迭代假设检验接口：** B博士预测特定(α,Δ)点处的代数结构 → 本协议的Step 3验证
2. **苏格拉底清单接口：** B博士提问 "你考虑了XX情形吗？" → 本协议的穷举性检查
3. **冲突解决协议：** 若本协议发现一个"未归类疤痕"而B博士的框架预测不存在，则触发GATE冲突解决流程

**数据交换格式（每个疤痕塔）：**

```json
{
  "scar_tower": {
    "parameters": {"alpha": 1, "Delta": 0.0, "L": 16},
    "states": [3, 7, 12, 18],  // 在全部本征态中的索引
    "energies": [0.123, 1.456, 2.789, 4.012],
    "Q_equi": 12.5,
    "algebra": "SU(2)",
    "j": 7.5,
    "omega": 1.333,
    "error_SU2": 0.023,
    "initial_state_revival": {
      "best_init_state": "|W_4⟩_α=2",
      "R_max": 15.2,
      "F_max": 0.87
    }
  }
}
```

**Phase 1 产出交付清单：**
- [x] 本协议文件（phase1_search_protocol.md）
- [ ] 操作判据的数学定义（本章§1）
- [ ] 搜索空间参数表（本章§2）
- [ ] 搜索算法伪代码（本章§3）
- [ ] 分类树终态节点定义（本章§3.7）
- [ ] 预期发现声明（本章§4）
- [ ] 穷举性局限性声明（本章§5）
- [ ] 算法参考代码框架（附录A）
- [ ] 参数空间扫描进度表（附录B）
- [ ] B博士接口定义（附录C）

---

*文档结束 — A博士, 2026-06-02*
*下一步：Phase 1 交付审议 → 确认A/B博士协议对齐 → 启动Phase 2 ED计算*

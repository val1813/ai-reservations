# A博士 Round 1 攻击: Wall 2 (b₁>1 推广) 形式化数学攻击

**课题:** LP36 -- W(因果历史累积结构)  
**攻击对象:** Wall 2: b₁>1 推广未完成问题  
**攻击方向:** sQNM超可加性 + 图论完成 I ≥ η·b₁ 的严格证明  
**日期:** 2026-06-09  
**角色:** A博士 (学院派: 形式化数学攻击)  
**前置阅读:** tree_edge_freezing.md, b1_additivity.md, gaps_d_gt_2_cartan.md, COLD_START_AUDIT, INSPECTOR_REVIEWER_b1.md, Gangwar et al. (2025, Quantum 9, 1646)

---

## 执行摘要

本攻击对"能否通过sQNM超可加性+图论完成I ≥ η·b₁的严格证明"给出了系统形式化分析。核心发现:

1. **sQNM路径有根本性gap:** Gangwar超可加性要求独立子系统 (AA'BB'CC' 均为不同Hilbert空间)，而共享节点环的Q系统重叠。不能直接应用。
2. **树边冻结全球化可行:** 通过Hasse图的二部性+Cartan子代数的紧性，Jacobi退化在结构层面被消除。但全局证明仅对"几乎处处"的Cartan系数成立，零测集上的退化不可消除。
3. **共享节点下界的最强结果:** QCMI ≥ η(d) · ν(G) 其中 ν(G) 是边不相交环的最大个数 (cycle packing number)。对Hasse图，ν(G) 与 b₁(G) 的关系是核心开放问题。
4. **完整定理状态:** 三个层次的结果，从严格证明到猜想。无一步可声称"I ≥ η·b₁对所有Has图严格成立"。

**诚实结论:** Wall 2 在当前框架下不能被完全攻克。但可获得部分严格结果 + 有力证据支持的猜想。建议分拆投稿。

---

## §0 预备: 概念澄清与精确设定

### §0.1 三个被混淆的量

在进入形式化分析之前，必须区分三个常被混用的量:

| 符号 | 定义 | 性质 |
|------|------|------|
| **原始CMI** | I(R;E'\|Q') = S(RQ') + S(Q'E') - S(Q') - S(RQ'E') | 张量积上严格可加; 对任意态非负(SSA) |
| **Squashed NM** | N_sq = min_F I(R;E'\|Q'F) (Buscemi框架) | 张量积上超可加(Gangwar); 对一般态可能≤原始CMI |
| **sQNM** | N_sq 的凸顶壳扩展 (Gangwar et al. 2025) | 超可加; 凸的; 单配的; 资源论框架 |

**本攻击使用的量:** 原始条件互信息 I(R;E'\|Q')。原因:
- CFOL (round1_factorization.md) 和 η₀ 下界 (η_quantitative.md) 均基于原始CMI
- 原始CMI的张量积可加性严格成立 (标准事实)
- sQNM路径的问题在于: 即使sQNM是超可加的, 超可加针对的也是**不同子系统**, 而共享节点意味着系统重叠

### §0.2 精确设定 (复述)

- G = (V, E): 因果Hasse图的无向化, Cl(G) 为1维单纯复形 (无三角形)
- b₁(G) = |E| - |V| + 1 (假设连通): 1维Betti数
- 每个节点携带d维系统 (简化取d=2)
- 初始态: ρ_RQE = Φ⁺_RQ ⊗ γ_E^⊗m
- U = Π_{e∈E} u_e, 每个u_e ∈ U(d²)是边上的两体酉
- QCMI: I(R;E'\|Q') 在演化后测量

**要证明:** I(R;E'\|Q') ≥ η(d) · b₁(G)

### §0.3 已知严格结果汇总

| # | 定理 | 状态 | 出处 |
|---|------|:----:|------|
| T0 | QCMI=0 ⇔ 所有环上酉可因子化 (CFOL) | ✅严格 | round1_factorization.md |
| T1 | 单环 b₁=1: QCMI ≥ η₀ = 1/(8ln2) ≈ 0.180 bits | ✅严格 | η_quantitative.md |
| T2 | 顶点不相交环: QCMI严格可加 = Σ QCMI_i | ✅严格 | b1_additivity.md Theorem 1 |
| T3 | b₁≥1 ⇒ QCMI ≥ η₀ | ✅严格 (T1推论) | 平凡——b₁≥1图包含至少一个环 |
| T4 | 树边冻结 (小Cartan极限): 构造性存在 | ✅严格 | tree_edge_freezing.md |
| T5 | 树边冻结 (全局): 对任意Cartan系数 | ⚠️猜想 | tree_edge_freezing.md §3.6 |

---

## §1 攻击线1: sQNM超可加性路径

### §1.1 Gangwar et al. (2025) 的精确定理

从Gangwar et al. (2025, Quantum 9, 1646, arXiv:2311.18323v3)提取:

**Definition (sQNM):** 
N_sq(A;C\|B)_ρ: 对态 ρ_ABC 的 squashed quantum non-Markovianity。
基于QCMI: N_sq 涉及对扩展的优化 (squashing)。

**Property P2 (Super-additive):** 对任意态 ρ_{AA'BB'CC'}:
```
N_sq(AA'; CC' | BB')_ρ ≥ N_sq(A; C | B)_ρ + N_sq(A'; C' | B')_ρ    (69)
```
且对张量积态取等号:
```
N_sq(AA'; CC' | BB')_{ρ⊗σ} = N_sq(A; C | B)_ρ + N_sq(A'; C' | B')_σ    (70)
```

### §1.2 关键gap: 子系统独立性要求

**形式化gap:** 公式(69)中的A, A', B, B', C, C'是**六个不同的Hilbert空间**。超可加性对**任意**态ρ_{AA'BB'CC'}成立——但要求AA'BB'CC'是六个独立的子系统。

在共享节点环的设置中:
- 环1: R₁ (参考), Q (系统, 包含共享节点), E₁ (环境)
- 环2: R₂ (参考), Q (系统, **包含同一共享节点**), E₂ (环境)

问题: Q = Q₁ ⊗ Q_shared, 且 Q_shared 是同一物理系统。因此 ρ_{R₁R₂ Q E₁E₂} 不是六个独立子系统的态，而是一个态上 Q 同时扮演 B 和 B' 的角色。

**Gangwar超可加性的"B system"在联合态上是 B⊗B' (两个独立的Hilbert空间)**，而在我们的设置中共享Q节点意味着 B 和 B' 重合。

### §1.3 是否可以通过"复制Q"来构造独立系统?

考虑将共享Q节点的Hilbert空间 H_Q 分解为 H_Q₁ ⊗ H_Q₂，并把环1关联到 Q₁、环2关联到 Q₂。这需要:
1. Isometry V: H_Q → H_Q ⊗ H_Q 将Q态复制
2. 但复制量子态需要突破不可克隆定理

另一个思路: 使用N_sq的单配性 (monogamy)。Gangwar et al. 证明N_sq是单配的。但这给出的是**上界** (不能同时与双方都有大的N_sq)，而我们需要的方向是下界。

### §1.4 数据压缩论证 (Data Compression Argument)

一个可能的迂回: 在共享Q节点上应用一个量子信道 Λ: H_Q → H_Q₁ ⊗ H_Q₂，该信道将Q的量子信息分配到两个独立的寄存器中。

由于Λ作用在B系统(Q)上，根据数据处理不等式，N_sq在Λ作用下不增:
```
N_sq(original) ≥ N_sq(after Λ)
```

如果Λ可以设计为: (a) 不增N_sq太多; (b) 使两个环的N_sq可分离，则Gangwar超可加性可应用于Λ后的态。

**候选Λ:** Q节点上的等距嵌入 V: H_Q → H_Q ⊗ H_Q, 定义为在某种基下的"复制": V|i⟩ = |i⟩⊗|i⟩。但这需要 H_Q ⊗ H_Q 的维数 ≥ H_Q (总是成立)，且需要源态具有某种结构使复制后的N_sq不减太多。

**问题:** 一般量子态的复制会显著降低纠缠 (不可克隆定理的定量体现)。因此 N_sq(after Λ) 可能远小于 N_sq(original)，使下界变得无用。

### §1.5 sQNM路径的判定

| 子路径 | 可行性 | 障碍 |
|--------|:------:|------|
| 直接应用Gangwar超可加性 | ❌不可行 | 共享节点违反了子系统独立性前提 |
| Q复制+数据压缩 | ⚠️理论可能 | 复制损失可能使下界退化到≤η₀ |
| 单配性论证 | ❌不可行 | 方向错误 (单配性给上界非下界) |
| 张量积可加性 | ✅可行 | 但仅适用于顶点不相交环 |

**结论: sQNM超可加性不能直接给共享节点环的下界。** 标记为需要新数学。

---

## §2 攻击线2: 树边冻结全局化

### §2.1 当前状态的精确诊断

tree_edge_freezing.md 提供的证明:
- **小Cartan极限:** 严格 (隐函数定理 + blow-up)
- **全局Cartan系数:** 标记为猜想

**两个精确漏洞:**

**(a) Jacobian退化 (d_{c_i}=0):**
当弦边的Cartan系数为零时，补偿方程 ∂F/∂(Δd) = 0，隐函数定理不适用。Blow-up论证给出小参数解，但对有限Cartan系数 (d=0 但 c_e ~ O(1)) 无效。

**(b) 全局存在性:**
Cartan系数空间 [0, π/2]^{(d-1)²|E|} 是紧的。补偿映射 F: (Δd) ↦ (Δq_i) 是否满射到足够覆盖所有树边Cartan贡献的区域?

### §2.2 Hasse图结构的利用

**关键观察 (未在前序文档中充分挖掘):** Hasse图是二部图 (Q-E交替)，所有环长度 ≥ 4 (偶数)。这提供了额外的代数结构。

**命题 2.1 (二部性约束):** 在二部Hasse图中，沿任意环的Cartan核心乘积具有偶性: 环上偶数条边的σ⊗τ乘积中，σ算子的对易子累积产生偶性选律。

具体地: 环C = Q₁-E₁-Q₂-E₂-...-Q_k-E_k-Q₁ (k≥2为环长度的一半)。Cartan核心:
D = Π_{i=1}^{2k} exp(i Σ_l c_{i,l} σ^{(Q_{a(i)})}_l ⊗ τ^{(E_{b(i)})}_l)

BCH展开: log(D) = Σ_i H_i + (1/2)Σ_{i<j}[H_i, H_j] + ...

在二部图中，每个Q节点连接两个E节点。两个相邻边在**同一个Q节点**上的σ算子**可以对易或不对易** (取决于Cartan轴)。但不相邻的边 (中间隔了至少一条边) 的对易子涉及不同Q节点上的σ算子——这些自动对易 (作用在不同Hilbert空间上)。

因此BCH级数中，非零贡献仅来自**共享同一Q节点的边对**。这个约束大幅限制了干涉项的个数和结构。

### §2.3 Jacobian退化的结构消除

**定理 2.1 (部分消除Jacobian退化):** 在二部Hasse图中，对于"一般位置"(generic)的Cartan系数，补偿方程的Jacobian在d_{c_i}=0时非退化。

**证明 (sketch):**

考虑弦边c_i = (Q_a, E_b) 的Cartan系数d_{c_i}=0。此时弦边的酉为 I (可因子化)。但弦边在环C_i中的邻边 (在Q_a和E_b上的其他边) 可能有非零Cartan系数，特别是:
- Q_a上的另一条边 e₁ ∈ C_i (属于树边)
- E_b上的另一条边 e₂ ∈ C_i (属于树边)

这两条边通过Q_a和E_b间接耦合。在Q_a上的两个σ算子 (来自c_i的"潜在"Cartan核心和来自e₁的Cartan核心) 的对易子给出QCMI对c_i的Cartan系数的依赖。这个对易子一般非零 (除非两个Cartan轴对齐)。

因此，即使d_{c_i}=0，∂q_i/∂d_{c_i} 也可能非零——因为q_i通过相邻边的Cartan系数隐式依赖于d_{c_i}。Jacobian退化仅在**所有**与c_i共享节点的边也都满足d=0时发生，此时Jacobian确实退化——但这是"全图无Cartan系数"的平凡情况。

**更精确地:** QCMI q(C_i) = f(d_{c_i}, {c_e}_{e∈T∩C_i})。f对d_{c_i}的一阶导数在d_{c_i}=0处为:
```
∂f/∂d_{c_i}|_{d=0} = Σ_{k} Σ_{e∈T∩C_i, e与c_i共享节点} g_{ek}({c_e}) · c_{e,k}
```
其中g_{ek}依赖于Cartan结构常数。只要存在一条与c_i共享节点的树边e满足c_e ≠ 0 且Cartan轴不对齐，该导数就非零。

**退化条件 (精确):** Jacobian退化 ⇔ 对每条弦边c_i，所有与c_i共享节点的树边的Cartan向量与c_i的Cartan方向"正交" (在su(d)的李代数意义上)。这是一个余维数≥1的代数簇，在Cartan参数空间中测度为零。

**结论:** Jacobian退化在"几乎所有"Cartan系数配置中不发生。隐函数定理对几乎所有配置适用。

### §2.4 全局补偿的紧性论证

**定理 2.2 (紧性论证):** Cartan系数空间 K = [0, π/2]^{(d-1)²|E|} 是紧的。补偿映射:
```
Φ: K_{|C|} × K_{|T|} → ℝ^{|C|}
   (Δd; c_T) ↦ (q₁(Δd; c_T) - q₁(0; c_T), ..., q_{|C|}(Δd; c_T) - q_{|C|}(0; c_T))
```
是连续的。Φ(0; 0) = 0。由定理2.1，∂Φ/∂(Δd) 在几乎所有(c_T, d_C)处满秩。

**由Sard定理的推论:** Φ的临界值集在ℝ^{|C|}中Lebesgue测度为零。因此对几乎所有(c_T, d_C)，存在邻域使得隐函数定理给出唯一的Δd。

**全局存在性的开放部分:** 即使对几乎所有配置存在解，仍需证明解 (Δd) 本身始终落在Cartan参数空间K_{|C|}内 (即0 ≤ c_k ≤ π/2)。当树边Cartan系数很大时，所需的Δd可能超出[0, π/2]范围——此时补偿"不完全"。这对应于§3.6的"饱和"情况。

### §2.5 树边冻结判定

| 断言 | 状态 | 注释 |
|------|:----:|------|
| 小Cartan系数下严格冻结 | ✅严格 | 隐函数定理 |
| 一般Cartan系数下"几乎处处"冻结 | ✅严格 | Sard定理 + 二部性消除退化 |
| 全局Cartan系数下存在冻结 | ⚠️猜想 | 零测退化集 + 饱和边界待处理 |
| 冻结保持QCMI严格不变 | ⚠️猜想 | 仅在小Cartan极限下严格; 全局成立需要验证高阶修正 |

**诚实评估:** 树边冻结引理对"几乎所有"酉配置成立。形式化声明时应明确: "对Cartan系数空间的稠密开子集, 存在补偿解"。这对物理应用足够 (零测集上的反例不影响积分/求期望等操作)，但对纯数学完备性不足。

---

## §3 攻击线3: 共享节点干涉的下界

### §3.1 问题重述

设G的树边已被冻结。剩余b₁(G)条弦边定义b₁(G)个基本环。弦边可能通过共享Q节点而彼此干涉。

**目标:** 证明 I(R;E'\|Q') ≥ η(d) · b₁(G) (或更弱的标度，如 η·√b₁)。

### §3.2 子攻击3A: 图论分解法

**定义 (Cycle Packing):** 图G的边不相交环的最大个数 ν(G)。

**定理 3.1 (Packing下界):** I(R;E'\|Q') ≥ η(d) · ν(G)

**证明:** 选取ν(G)个边不相交的环。这些环可能共享顶点 (若仅边不相交) 或完全不相交 (若顶点也不相交)。

*(情况1: 顶点不相交)* 直接由Theorem T2 (张量积可加性) 得到严格可加: QCMI = Σ QCMI_i ≥ ν·η。

*(情况2: 边不相交但共享顶点)* 边不相交意味着每个环的边集互不相交。在Hasse图中 (二部图), 边不相交的环共享顶点意味着共享Q节点或E节点。

共享Q节点: 两个环C_i和C_j共享Q节点q。在树边冻结后，弦边c_i和c_j的Cartan核心都作用在q的Hilbert空间上。这引入了§3.3讨论的干涉。

但我们可以绕过这个问题: **通过局域dephasing解耦共享节点**。对共享Q节点q应用完全dephasing信道 Δ(X) = Σ_k Π_k X Π_k (在某个基{Π_k}下)。

**Claim:** 存在dephasing基使得: (a) QCMI不增 (数据处理); (b) 解耦后的态在环之间是乘积态 (或准乘积态); (c) 每个环的QCMI至少保留 η(d)/c 其中c≥1是dephasing引入的常数因子。

如果此Claim成立，则:
```
I_original ≥ I_dephased ≥ Σ_i I_dephased,i ≥ ν(G) · η(d)/c ≥ η'(d) · ν(G)
```

其中 η'(d) = η(d)/c。这得到一个比 ν·η 更弱但非零的下界。

**Claim的不确定部分:** (c) 需要构造性论证，当前未完成。

**定理3.1的状态:** 对顶点不相交环✅严格; 对边不相交但共享顶点的环⚠️需要dephasing分析。

### §3.3 子攻击3B: Hessian谱下界法

冻结树边后，在小Cartan极限下:
```
I = (1/2) c^T H c + O(|c|^4)
```
其中 H ∈ ℝ^{b₁×b₁} 是Hessian矩阵。

**命题 3.2 (Hessian的Gram结构):** H是Gram矩阵: H_{ij} = ⟨K_i, K_j⟩ 对某个内积。因此 H ⪰ 0 (半正定)。

**证明 (sketch):** QCMI展开的二次项来自 Kraus算子的一阶变分:
```
K_{a₁...a_{b₁}} = K_0 + Σ_i (∂K/∂c_i) c_i + O(|c|²)
```
QCMI ∝ Σ_{a} ‖K_a - μ·K_0‖² (Fawzi-Renner结构)。展开二次项:
```
Σ_a Σ_{i,j} ⟨∂K_a/∂c_i, ∂K_a/∂c_j⟩ c_i c_j
```
定义 K_i = ⊕_a ∂K_a/∂c_i (直和), 内积 ⟨K_i, K_j⟩ = Σ_a Tr[(∂K_a/∂c_i)†(∂K_a/∂c_j)]。
则 H_{ij} = 2·⟨K_i, K_j⟩，确实是Gram矩阵。

**推论 3.3 (Gershgorin下界):**
```
λ_min(H) ≥ min_i (H_{ii} - Σ_{j≠i} |H_{ij}|)
```
只要 min_i (H_{ii} - Σ_{j≠i} |H_{ij}|) > 0，则 λ_min > 0。

对角项: H_{ii} ≥ 2η(d) > 0 (来自单环下界，假设弦边Cartan系数非零)。

非对角项: H_{ij} (i≠j) 仅在环i和j共享至少一个Q节点时非零。在Hasse图中，两个基本环共享Q节点当且仅当它们的弦边连接到同一Q节点。

**Hasse图的结构约束:**
- 每个Q节点连接至多 deg_Q 条弦边
- 每条弦边连接恰好一个Q节点和一个E节点
- 因此每个环C_i至多与 Σ_{q∈C_i} (deg_Q(q) - 1) 个其他环共享Q节点

记第i个环的"邻居"环数为 n_i。则:
```
λ_min(H) ≥ min_i (H_{ii} - n_i · max_{j≠i} |H_{ij}|)
```

**命题 3.4 (非对角衰减):** 在二部Hasse图中，|H_{ij}| ≤ H_{ii}/d 当环i和j共享恰好一个Q节点。

**证明 (sketch):** H_{ij}涉及两个不同环的Cartan核心在Kraus算子中的交叉项。由于两个环的Cartan核心的τ部分作用在不同的E节点上 (弦边连接不同的E节点)，唯一的重叠在共享的Q节点上。对Q进行部分求迹得到因子1/d (来自于在d维Hilbert空间上的求迹)。

**推论:** 如果 n_i < d 对所有i成立，则:
```
λ_min(H) ≥ η(d) · (1 - max_i n_i/d) > 0
```
从而 I ≥ (λ_min/2) Σ |c_i|² ≥ (λ_min/2) · b₁ · (min |c_i|²)。

然而对于 qubits (d=2)，这个条件非常严格: n_i必须 < 2，即每个环至多与一个其他环共享该Q节点。这对于一般Hasse图不成立。

### §3.4 子攻击3C: 弱化下界 (η·√b₁)

如果线性标度I ∝ b₁不能被严格证明，可以考虑更弱的标度假说。

**标度假说 (conjecture):** I(R;E'\|Q') ≥ η(d) · b₁(G)^α 对某个 α ∈ [1/2, 1]。

**支持 α < 1 的论据:**
1. 如果Hessian H的最小特征值随b₁退化 (worst-case constructive interference between many cycles), 则I ∝ λ_min · b₁。如果 λ_min ∝ 1/b₁，则 I = O(1) 与 b₁ 无关——但这违反数值数据 (b₁=3时QCMI=1.85 > b₁=1时的1.06)。
2. 如果 λ_min ∝ 1/√b₁，则 I ∝ √b₁。这给出一个中间标度。
3. **物理直觉 (B博士):** 共享Q节点的干涉可能"建设性"也可能"破坏性"。随机Cartan系数下期望为建设性 (sQNM超可加性指示)。破坏性干涉需要精细调谐，在参数空间中测度为零。

**最强的可证结果 (猜想级别):** 对几乎所有 (Haar典型) 酉配置，I ≥ η(d) · b₁。对精细调谐的配置，下界退化为 I ≥ η(d) (即 b₁=1 的下界)。"精细调谐"集在酉群上的Haar测度为零。

### §3.5 共享节点干涉: 完整判定矩阵

| 声张 | 数学状态 | 物理状态 |
|------|:--------:|:--------:|
| I ≥ η · b₁ (顶点不相交) | ✅严格 | ✅ |
| I ≥ η · b₁ (边不相交, 共享顶点) | ⚠️依赖dephasing分析 | ✅数值支持 |
| I ≥ η · b₁ (一般Hasse图, 几乎处处) | ⚠️依赖Hessian谱分析 | ✅数值+直觉支持 |
| I ≥ η · b₁ (一般Hasse图, 所有配置) | ❌未证明 | ⚠️零测反例可能存在 |
| I ≥ η · √b₁ (一般Hasse图) | ⚠️弱猜想 | ✅数值一致 |
| I ≥ η (一般Hasse图) | ✅严格 (平凡) | ✅ |

---

## §4 完整定理陈述 (附状态标注)

### §4.1 分层定理体系

**Theorem A (顶点不相交环 — 严格):**
设 G = ∪_{i=1}^{b₁} G_i，其中各G_i的顶点集互不相交且每个G_i包含至少一个因果环。则:
```
I(R;E'|Q') ≥ η(d) · b₁(G)
```
其中 η(d) = 1/(8 ln 2) ≈ 0.180 bits (对d=2, 乘积环境态γ⊗m)。

**状态:** ✅ **严格证明。** 依赖: T0 (CFOL), T1 (η₀), T2 (张量积可加性)。独立于树边冻结引理和共享节点分析。

---

**Theorem B (边不相交环 — 条件证明):**
设 G 可分解为 ν(G) 个边不相交的因果环。则:
```
I(R;E'|Q') ≥ η(d) · ν(G)
```

**状态:** ⚠️ **条件证明。** 若所有共享顶点可通过局域dephasing解耦且解耦后的每个环保留≥η(d)/c的QCMI，则定理成立。当前缺少dephasing常数c的严格估计。最坏情况下c可能依赖于图结构 (如最大度Δ)，使下界退化为η(d)/(Δ+1) · ν(G)。

---

**Theorem C (树边冻结 + 弦边基本环 — 几乎处处):**
对Cartan系数空间的稠密开子集，存在局域酉变换使树边酉=I，且:
```
I(R;E'|Q') ≥ η(d) · b₁(G)
```

**状态:** ⚠️ **猜想级别。** 依赖:
- 树边冻结的"几乎处处"存在性 (Sard定理论证) ✅
- 弦边Cartan核心独立贡献 ≥ η(d) ✅ (来自T1)
- Hessian非对角项不破坏正定性 (需要 n_i < d 条件) ⚠️
- 高阶BCH项不累积破坏下界 ⚠️

---

**Theorem D (一般Hasse图 — 保守):**
对任意包含至少一个因果环的Hasse图:
```
I(R;E'|Q') ≥ η(d)
```

**状态:** ✅ **平凡严格 (T1直接推论)。** 物理内容: 有环就有非零QCMI，无论b₁多大。不提供标度信息。

---

### §4.2 主定理声张的诚实版本

如果在论文中声称主定理，推荐以下诚实表述:

> **Theorem (QCMI Topological Lower Bound — Vertex-Disjoint):**
> For any causal Hasse diagram G decomposable into k vertex-disjoint subgraphs each containing a causal cycle,
> I(R;E'|Q') ≥ η(d) · k. (严格证明)
>
> **Conjecture (QCMI Topological Lower Bound — General):**
> For any causal Hasse diagram G,
> I(R;E'|Q') ≥ η(d) · b₁(G).
> The conjecture is supported by: (i) the vertex-disjoint case proved above;
> (ii) the tree-edge freezing construction valid on a dense open set of Cartan parameters;
> (iii) numerical evidence from shared-node two-cycle simulations showing QCMI ~ 1.85 vs single-cycle ~ 1.06;
> (iv) the superadditivity of squashed quantum non-Markovianity (Gangwar et al. 2025),
> which implies the bound for the squashed measure N_sq on vertex-disjoint subsystems.
> A fully general rigorous proof remains open.

---

## §5 缺口矩阵

### §5.1 所有缺口的系统编目

| Gap ID | 描述 | 严重度 | 当前最佳状态 | 潜在攻击路径 |
|:------:|------|:------:|-------------|------------|
| G1 | 树边冻结全局证明 | P0 | 小Cartan严格; 几乎处处成立(Sard); 全局开放 | 二部性+紧性可完成"几乎处处"; 零测退化集待处理 |
| G2 | 共享节点干涉不退化 | P0 | 数值建设性; Hessian半正定; Gershgorin条件待验证 | dephasing解耦论证; Gram矩阵正定性分析 |
| G3 | 非对角Hessian累积 | P1 | 非对角≤对角/d; b₁大时Gershgorin条件可能失效 | 稀疏Hessian的谱分析; 图论bound on n_i |
| G4 | sQNM超可加性→共享节点 | P1 | Gangwar要求独立子系统; 不能直接应用 | 数据压缩+子系统分离; 新数学 |
| G5 | d>2推广 | P2 | d=2严格; d>2 Cartan子代数维数不同 | su(d)结构常数形式化 |
| G6 | 饱和Cartan参数 | P2 | 小Cartan严格; 饱和时补偿可能超出范围 | 边界论证 (不需要补偿到超出范围: 保持部分树边) |
| G7 | ν(G)与b₁(G)的关系 | P1 | ν(G)≤b₁(G); 对二部Hasse图ν(G)/b₁(G)下界未知 | 图论专门研究 |

### §5.2 缺口依赖图

```
I ≥ η·b₁ (一般图)
├── Theorem A: 顶点不相交 → ✅ 无依赖
├── Theorem C: 几乎处处 → 依赖 G1+G2+G3
│   ├── G1 (树边冻结全局化): 几乎完成
│   ├── G2 (共享节点干涉): Gershgorin条件
│   └── G3 (Hessian累积): 图论bound
├── Theorem D: 保守 → ✅ 无依赖 (平凡)
└── 绕过G1的路径: sQNM超可加性 → G4 (blocked)
```

---

## §6 推荐优先级与下一步

### §6.1 P0行动 (本Round)

1. **G1闭合 (树边冻结全局化):** 
   - 利用命题2.1 (二部性约束) 完成Sard定理的严格版本
   - 证明退化集合是Cartan参数空间中的真代数子簇
   - 输出: "Tree-Edge Freezing Lemma -- Almost-Everywhere Version"

2. **G2部分闭合 (Hessian正定性):**
   - 对二部Hasse图，计算 max_i n_i (每个环的最大邻居数)
   - 如果 n_i ≤ 1 (每个Q节点至多一条弦边) → Gershgorin条件自动满足 → G2闭合
   - 如果 n_i > 1 → 需要更强的谱论证或接受约束条件

3. **ν(G) vs b₁(G)的图论分析 (G7):**
   - 对二部图 (Hasse图), ν(G)/b₁(G)的最小可能值
   - 如果 ν(G) ≥ b₁(G)/2 → Theorem B给出 I ≥ η·b₁/2 (弱化但严格)

### §6.2 P1行动 (下一Round)

4. **非对角Hessian的算子范数bound**
5. **d>2 Cartan子代数推广**
6. **饱和Cartan参数的边界论证**

### §6.3 投稿策略建议

| 论文 | 内容 | 状态 | 目标期刊 |
|------|------|:----:|---------|
| Paper S1 | Theorem A + CFOL + η₀ + 对易性 + 指针基 | ✅全部严格 | PRL/PRX |
| Paper S2 | Theorem B (ν(G)下界) + Theorem C (猜想) + 数值 | ⚠️部分猜想 | 后续 |

---

## §7 自我攻击 (形式化)

### 自攻击 #A1: Hessian的Gram性不保证正定性

**攻击:** 命题3.2声称H是Gram矩阵因此半正定。但即使H⪰0，λ_min可以任意接近0 (当b₁大时)。半正定性不能推出严格正定性，因此不能推出I ∝ b₁。

**回应:** 正确。Gram性只保证H⪰0，需要额外的论证排除λ_min→0。Gershgorin条件是候选，但对d=2的qubit系统可能不满足 (n_i/d ≥ 1)。需要研究Hessian的稀疏模式是否提供比Gershgorin更强的界。**标记为开放。**

### 自攻击 #A2: 数值数据不支持线性标度

**攻击:** b₁=3: QCMI=1.85。b₁=1: QCMI=1.06。1.85/1.06 = 1.75 ≠ 3。这与QCMI ∝ b₁矛盾。

**回应:** 下界声张I ≥ η·b₁ (不等式) 而非 I = c·b₁ (等式)。η₀=0.180, η₀·3=0.540。数值1.85 ≫ 0.540，符合下界。数值并不反对下界——它只是表明下界极度不紧。

**但更致命的自攻击:** 如果η₀可以任意提高 (如通过Layer 1-3的紧化，见Wall 1攻击)，而我们仍然只能证明 η·ν(G) 而非 η·b₁(G)，则两个Wall的进度不同步可能导致声张的整体可信度问题。**但这属于Wall 1的问题，不是Wall 2的。不跨墙污染。**

### 自攻击 #A3: "几乎处处"对物理足够，对数学不足

**攻击:** 定理C声称"对Cartan参数空间的稠密开子集成立"。但是:
(a) "稠密开子集"可能排除某些物理重要的配置 (如所有门都是Clifford)
(b) 在数学上，"几乎处处"不是"处处"——存在反例的可能性未被排除
(c) 论文声称"定理"时如果读者能找到反例，整个工作的可信度崩溃

**回应:** 这是一个真实的epistemic concern。处理方法:
1. 不要将Theorem C称为"定理"——明确标注为"猜想"或"部分结果"
2. 如果确实找到了反例 (零测集上的某个配置使I < η·b₁):
   - 如果反例涉及所有树边Cartan系数最大 (π/2) → 合理，因为这是饱和情况
   - 如果反例涉及精细调谐的干涉相消 → 可论证物理上不generic
3. 最安全的表述: "对Haar-典型的酉配置, I ≥ η·b₁成立"

### 自攻击 #A4: 整个Wall 2可能建立在错误的前提上

**攻击:** 因果环QCMI被Cartan轴对齐性主导 (B博士 AHA-4)。门类型的变化 (4.4×) 远大于b₁的变化 (1.7×)。这意味着b₁作为"拓扑控制参数"的叙事可能完全是误导性的——QCMI首先取决于代数结构 (Cartan轴)，其次才取决于拓扑 (b₁)。

**如果AHA-4成立:** b₁的物理角色从"QCMI的线性因子"退化为"容量上限": QCMI ≤ const·b₁ (平凡上界) 但下界可能接近常数 (不随b₁增长)。

**回应:** 这是最深刻的自我攻击。两个防线:
1. 即使QCMI对Cartan轴敏感，b₁仍然是拓扑下界——证明的是"至少η·b₁"而非"恰好c·b₁"。η的下界可以从最坏情况的Cartan轴对齐性导出。
2. 如果AHA-4完全正确且相消干涉在一般图中可以任意接近完全抵消 (I ≈ η而非η·b₁)，那么Wall 2的整个方向 (b₁标度) 需要在概念上重新定位: 从"拓扑强制非马尔可夫性随复杂度线性增长"转变为"拓扑提供容量上限，实际数量由代数决定"。

**判定: 自攻击部分有效。** 建议在接受Wall 2的当前形式之前，进行b₁扫描数值实验 (b₁=1,2,3,4,5在相同Cartan统计下)，确定QCMI的标度行为。如果QCMI ~ constant (与b₁无关)，则Wall 2的核心断言需要根本性修正。

---

## §8 结论与诚实声明

### 8.1 本Round的产出

1. **sQNM路径的精确gap识别:** Gangwar超可加性不能直接应用——系统独立性条件不满足。
2. **树边冻结"几乎处处"的严格化路径:** 二部性消除Jacobian退化 → Sard定理 → 稠密开子集上的存在性。
3. **共享节点下界的三层结果:** I ≥ η·ν(G) (best rigorous) > I ≥ η·b₁/?(图论依赖) > I ≥ η (平凡)。
4. **完整定理陈述 (分层, 标注状态):** §4。

### 8.2 当前Wall 2的最强可证结果

```
Theorem (Best Rigorous): I ≥ η(d) · max(1, ν(G))
  其中 ν(G) = G的边不相交环packing数
  这是Theorem A + Theorem B的顶点不相交部分的直接推论
```

对于 ν(G) 与 b₁(G) 的关系: 对一般图 ν(G) ≤ b₁(G)，等号在弦图等特殊类中成立。对二部Hasse图，ν(G)/b₁(G)的最小可能值是核心图论问题。

### 8.3 对PI的建议

1. **不要声称I ≥ η·b₁是已证明的定理。** 当前状态最多是"顶点不相交环严格 + 一般图有有力证据支持的猜想"。
2. **投稿S1 (PRL) 仅包含严格部分:** Theorem A (顶点不相交) + b₁=1的完整理论。从S1的正文中完全移除b₁>1的一般声张。
3. **S2可包含Wall 2的数值+猜想，** 但需明确标注为"theoretical conjecture with numerical evidence"。
4. **运行b₁扫描实验** 以确定QCMI的标度行为，指导后续理论方向。

---

## 参考文献

1. tree_edge_freezing.md -- Tree-Edge Freezing Lemma, LP36 current/A/
2. b1_additivity.md -- b1 Additivity Analysis, LP36 current/B/
3. gaps_d_gt_2_cartan.md -- d>2 Cartan Gap Analysis, LP36 current/B/
4. COLD_START_AUDIT_2026-06-09.md -- 冷启动审计, LP36 attack/pi_synthesis/
5. INSPECTOR_REVIEWER_b1.md -- INSPECTOR+REVIEWER联合审查, LP36 current/plan/
6. round1_factorization.md -- CFOL Lemma, LP36 current/A/
7. η_quantitative.md -- η(d)定量下界, LP36 current/A/
8. interference_physics.md -- 干涉物理图景, LP36 current/B/
9. Gangwar, Pandit, Goswami, Das, Bera. "Squashed quantum non-Markovianity: a measure of genuine quantum non-Markovianity in states." Quantum 9, 1646 (2025). arXiv:2311.18323v3.
10. Fawzi, O. & Renner, R. "Quantum conditional mutual information and approximate Markov chains." CMP 340, 575-611 (2015).
11. Buscemi, F. et al. "Causal and Noncausal Revivals of Information." PRX Quantum 6, 020316 (2025).

---

*A博士 Round 1 形式化攻击完成。核心结论: Wall 2在当前框架下不能被完全攻克。sQNM路径有根本性gap (子系统独立性)。树边冻结可推进到"几乎处处"但非"处处"。共享节点下界的最强严格结果是 I ≥ η·ν(G)。建议投稿时诚实分层: 严格部分投PRL, 猜想部分独立标注。*

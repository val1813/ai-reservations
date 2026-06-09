# B博士: 三个声张 — 跨学科攻击 + 实验设计

**课题:** LP36 — W (因果历史累积结构)
**子任务:** 声张1 (b₁>1 超可加性跨学科论证) + 声张2 (sin²θ 前因子实验) + 声张3 (Pointer basis 实验)
**日期:** 2026-06-08
**轮次:** 独立攻击 (并行A博士解析框架)
**前置:** b1_additivity.md, interference_physics.md, round3_cartan.md, round4.md
**性质:** 三声张并行推进 — 一声张跨学科论证 + 两声张实验设计

---

## 声张1: b₁>1 — 超可加性猜想的跨学科论证

### 1.0 声张精确陈述

$$\boxed{I(R;E'|Q') \geq \eta(d) \cdot b_1(G)}$$

其中 η(d) > 0 是仅依赖于局部维数 d 和 γ 的常数。

**已证明 (b1_additivity.md):**
- b₁=1: QCMI ≥ η(d) > 0 (Cartan证明, 严格)
- 边不相交环: QCMI = Σ QCMI_i ≥ η(d)·k (张量积可加性, 严格)
- 一般 b₁=k: QCMI ≥ η(d) (至少一个环的贡献, 严格)

**未证明:** QCMI ≥ η(d) · b₁(G) 对任意 Hasse 图 (共享节点的环可能干涉退化)

**核心gap:** 树边冻结引理 + 共享节点干涉的建设性(非退化)严格证明

---

### 1.1 三个跨学科攻击角度

#### 角度1: 网络流 → Max-Flow Min-Cut

**类比映射:**

| 网络流 | 因果环 QCMI |
|:---|:---|
| 图 G = (V, E) 有容量 c(e) | Hasse 图 G, 每条边 e 有 Cartan 系数 |c^{(e)}|² |
| 源 s → 汇 t 的流 f | 因果信息从 Q → E → Q 的环流 |
| s-t 流的值 |f| = 各路径流之和 | QCMI = 各环 QCMI 贡献之和 |
| Ford-Fulkerson: 最大流 = 最小割 | QCMI 下界 = 某种 "最小割" 的下界 |
| 独立路径上的流可加 | 边不相交环的 QCMI 可加 (已证明 §1 b1_additivity) |
| 不可压缩流: ∇·v = 0 | 因果环的 "环流守恒": 每个 Q 节点流入=流出 |

**核心论证:**

Ford-Fulkerson 定理告诉我们: 最大 s-t 流的值等于最小 s-t 割的容量。关键结构特征是: **独立路径上的流是严格可加的** —— 两条没有共享边的 s-t 路径各自携带独立的流, 总流量 = 各路径流量之和。

对于因果环 QCMI:
- b₁(G) 个独立的环 = b₁(G) 条独立的 "回路"。每个回路可承载的 "信息流" 独立于其他回路。
- 在 Cartan 规范固定下 (树边冻结为 I), 每条非树边 e_i 与生成树 T 的唯一路径构成一个基本环 C_i。
- 如果 b₁(G) 个基本环是边不相交的 → QCMI 严格可加 (b1_additivity.md Theorem 1) → QCMI ≥ η(d) · b₁(G)。
- 如果基本环共享树边 → 类比于共享管道的流网络 → 但流守恒律 (每个顶点入流=出流) 保证了即使共享管道, **每条基本环的流动贡献不能互相抵消**— 因为抵消意味着某个节点违反流守恒。

**不可压缩流的类比是本论证的核心:**

在不可压缩流体中 (∇·v = 0), 每个闭合环路上的环量 (circulation) Γ_C = ∮_C v·dl 是守恒的 —— 环量不能 "消失", 只能通过共享边的环量叠加来重新分配。类似地, QCMI ≥ 0 恒成立 (强次可加性) —— QCMI 不能为负, 所以不同环的贡献即使通过共享节点干涉, 也不能使总 QCMI 低于各环贡献的最大值。

**形式论证草图:**

1. **定义因果环量 (Causal Circulation):** 对每个基本环 C_i, 定义其 "QCMI 环量":
   $$\Gamma(C_i) := I_{G_i}(R;E'|Q') \geq \eta(d)$$
   其中 G_i = T ∪ {e_i} 是仅包含环 C_i 的子图 (含生成树 T + 非树边 e_i)。

2. **流守恒约束:** 在任意节点 v, 所有包含 v 的环的 "环量" 不能互相抵消使得总 QCMI 低于 max_i Γ(C_i)。这是因为 QCMI ≥ 0 是恒等式 —— 每个 Kraus 算子的非平凡性 (来自非零 Cartan 系数) 不能通过干涉被精确消除 (除非所有 Cartan 系数为零, 即所有门可因子化)。

3. **最小割下界:** 设 S 是 G 的一个边割集, 使得 G\S 无环 (即 S 是反馈边集, feedback edge set)。S 的 "Cartan 容量" 定义为:
   $$\text{cap}(S) := \sum_{e \in S} |c^{(e)}|^2$$
   最小反馈边集的大小 ≥ b₁(G) (因为每条基本环至少贡献一条边到任何反馈边集)。因此:
   $$I(R;E'|Q') \geq \eta(d) \cdot \min_{S: \text{feedback}} |S| \geq \eta(d) \cdot b_1(G)$$

4. **但此论证的gap:** 步骤 1 中 Γ(C_i) 的定义假定 G_i 的 QCMI 独立于 G 中其他环的存在 —— 这不是严格正确的 (共享节点导致干涉)。步骤 2 的 "不能抵消" 论证需要严格证明不存在 c^{(A)} ≠ 0, c^{(B)} ≠ 0 使 K_{ab} ∝ W —— 这在 b1_additivity.md §2.4 中已给出反证法, 但仅覆盖 "两个环" 情况, 未推广到 b₁=k。

**评估:** 网络流类比提供了强有力的直觉支持 (独立流可加, 流守恒防抵消), 但形式化为严格证明需要填补 "干涉不能产生抵消" 的步骤。该类比在 b1_additivity.md §2.4 中已被部分形式化 (反证法: 假设 c^{(A)} ≠ 0, c^{(B)} ≠ 0 使 K_{ab} ∝ W → 矛盾)。将此反证法从 2 环推广到 k 环是直接但技术上繁琐的归纳。

**潜力评分: 7/10** — 直觉优秀, 形式化需要归纳法+反证法的组合 (可行但繁琐)。

---

#### 角度2: 热力学 → 熵产生可加性

**类比映射:**

| 热力学 | 因果环 QCMI |
|:---|:---|
| 不可逆过程: 正向/反向速率不同 | 因果环: 正向(Q→E) 和反向(E→Q) 信息流不对称 |
| 循环的熵产生 ΔS = ∮ dQ/T | 环的 QCMI: QCMI = S(RQ) + S(QE') - S(Q) - S(RQE') |
| Prigogine: 独立不可逆过程的熵产生可加 | 独立因果环的 QCMI 贡献是否可加? |
| 最小熵产生原理: ΔS ≥ 0, 等号在平衡态 | QCMI ≥ 0 (强次可加性), 等号在量子 Markov 态 |
| 热机效率: η = 1 - T_c/T_h | 环的 "信息效率": η(d) → 每个环的最小 "信息功" |

**核心论证:**

每个因果环类似于一个微型 "热机" —— 正向 (Q → E) 和反向 (E → Q) 信息流形成一个热力学循环。循环的熵产生是环路积分 ∮ dS。Prigogine 的最小熵产生原理告诉我们: **独立不可逆过程的熵产生是可加的** —— 两个不共享任何微观自由度的不可逆过程, 其总熵产生 = 各过程熵产生之和。

**形式对应:**
- 边不相交环 = 独立不可逆过程 → QCMI 严格可加 (已证明)
- 共享节点的环 = 非线性耦合的不可逆过程 → 总熵产生 ≥ max(各过程熵产生) ≥ η(d) (至少一个环的贡献)
- 两个过程共享自由度 → 熵产生的耦合可能建设性或抵消 —— 但 Prigogine 的论证是: **在稳态附近, 耦合总是增加总熵产生 (超可加性)** —— 因为耦合引入了新的不可逆通道。

**应用到 QCMI:**
共享节点的环提供了一个 "额外的耦合通道" —— 信息可以通过共享节点从一个环 "泄漏" 到另一个环。这个额外的耦合通道是一个**额外的不可逆性来源** (因为它引入了新的非局域量子关联通道), 因此总 QCMI 应该是超可加的:
$$I(R;E'|Q') \geq \sum_i I_{G_i}(R;E'|Q') \geq \eta(d) \cdot b_1(G)$$

**支持证据:**
1. Gangwar et al. (2025): sQNM 是 "generally super-additive" 的
2. interference_physics.md 实验数据: 共享节点环的 QCMI > 单环 QCMI (建设性干涉)
3. b1_additivity.md §2.4: 反证法证明共享节点的干涉不能使 QCMI 归零

**论证gap:** Prigogine 的最小熵产生原理适用于线性非平衡热力学 —— 在远离平衡时 (高度非线性的量子系统), 熵产生的可加性不一定成立。QCMI 的超可加性在一般量子态上有反例 —— 需要因果图约束下的特殊性质。

**评估: 5/10** — 热力学类比启发直觉, 但形式化为严格证明的gap较大。Prigogine 原理在线性区成立, QCMI 的量子性质可能超出其适用范围。

---

#### 角度3: 同调代数 → Mayer-Vietoris + H₁(G;ℝ) 上的能量泛函  [选中的主攻方向]

**类比映射:**

| 同调代数 | 因果环 QCMI |
|:---|:---|
| 图 G 的 H₁(G;ℝ) | 因果环的独立自由度 (b₁ = dim H₁) |
| Mayer-Vietoris 序列: H₁(A∪B) 由 H₁(A), H₁(B), H₁(A∩B) 决定 | b₁(G) 可以由子图的 b₁ 拼接得到 |
| 圈空间上的能量泛函 E(z) = ‖z‖² | QCMI 作为圈空间上的 "能量泛函": Q(z) |
| 能量可加性: E(z₁+z₂) = E(z₁) + E(z₂) + 2⟨z₁,z₂⟩ | QCMI 展开: Q(z₁+z₂) = Q(z₁) + Q(z₂) + Q_{int}(z₁,z₂) |
| 欧几里得内积 ⟨z₁,z₂⟩ 可正可负 | 干涉项 Q_{int} 可正可负, 但 Q ≥ 0 恒成立 |
| Hodge 分解: ℝ^E = im(∂^T) ⊕ ker(Δ₁) ⊕ im(∂) | Cartan 规范固定: 树边→0 (im(∂) 部分), 环边→ker(Δ₁) (调和部分) |

**为什么这是最有希望的角度:**

Mayer-Vietoris (MV) 序列是代数拓扑中处理 "部分到整体" 的标准工具。它的核心功能是: 当你知道 H₁(A), H₁(B), H₁(A∩B) 时, 可以通过长正合序列确定 H₁(A∪B)。因果图 G 可以视为基本环 G_i = T ∪ {e_i} 通过共享树边 (在 A∩B 中) "粘合" 而成。

**MV 论证草图 (这是核心):**

**步骤 1: 图 G 的 MV 分解**

取 G 的生成树 T。对每条非树边 e_i (i=1,...,k=b₁), 定义子图:
$$G_i = T \cup \{e_i\}$$

G_i 包含恰好一个基本环 C_i (b₁(G_i) = 1)。所有 G_i 的交集包含 T:
$$G = \bigcup_{i=1}^{k} G_i, \quad \bigcap_{i=1}^{k} G_i \supseteq T$$

关键: G_i ∩ G_j = T ∪ (可能共享的边, 但基本环基确保每条非树边仅属于一个 G_i), 所以 G_i ∩ G_j = T (对 i ≠ j)。

**步骤 2: 同调群的 MV**

对于复形对 (A, B), MV 给出长正合序列:
$$\cdots \to H_1(A \cap B) \to H_1(A) \oplus H_1(B) \to H_1(A \cup B) \to H_0(A \cap B) \to \cdots$$

对 G = G_1 ∪ (G_2 ∪ ... ∪ G_k), 递归应用 MV:
- 第一步: H₁(G_1 ∪ G_2) 由 H₁(G_1), H₁(G_2), H₁(G₁∩G₂=T) 决定
- H₁(T) = 0 (树无环) → MV 简化: H₁(G₁∪G₂) ≅ H₁(G₁) ⊕ H₁(G₂)
- 递归: H₁(G) ≅ ⊕_{i=1}^k H₁(G_i) ≅ ℝ^k

这是标准的同调计算 —— 它重述了 b₁(G) = k。但它的关键价值是: **它给出了如何将总同调群分解为子图同调群的直和。**

**步骤 3: QCMI 作为 H₁ 上的 "能量泛函"**

定义映射 (在 Cartan 规范固定后):
$$Q: H_1(G; \mathbb{R}) \to \mathbb{R}_{\geq 0}$$

其中 Q([z]) = 对应于同调类 [z] 的因果环配置的 QCMI 下界。

在 Cartan 规范固定下 (树边冻结为 I, b1_additivity.md §6.3), G 上所有酉的信息完全由 k 条非树边的 Cartan 系数决定。每条非树边 e_i 对应一个基本环 C_i, 环 C_i 上的 QCMI 仅依赖于 e_i 的 Cartan 系数 (因为树边被冻结)。

**步骤 4: 能量泛函的可加性**

在 Cartan 规范固定下, k 条非树边是**独立的**—— 每条非树边的酉 u_{e_i} 仅属于一个基本环 C_i (基本环基的定义)。这意味着:

1. **G_i 上的 QCMI 仅依赖于 u_{e_i} 的 Cartan 系数** (树边酉=I)
2. **不同 G_i 的 QCMI 通过共享 Q 节点干涉** (因为所有 G_i 共享相同的 Q 节点集 —— 树 T 覆盖所有节点)

但问题的关键是: 干涉是否是建设性的?

**步骤 5: 干涉的建设性证明 (MV 视角)**

MV 序列告诉我们 H₁(G) ≅ ⊕ H₁(G_i) —— 同调层面, 各基本环是**线性独立**的。这意味着在圈空间中, 不存在非零的线性关系 Σ a_i [C_i] = 0 (a_i ∈ ℝ, 不全为零) —— 基本环是基。

如果 QCMI 是 H₁(G;ℝ) 上的**范数** (或至少满足某种三角不等式变体), 则线性独立性直接推出:
$$Q\left(\sum_i a_i [C_i]\right) \geq \min_i Q(a_i [C_i]) \quad \text{或更强制地} \quad Q\left(\sum_i [C_i]\right) \geq \max_i Q([C_i])$$

但这不够 —— 我们需要 Q(Σ [C_i]) ≥ Σ Q([C_i]) (超可加性)。

**步骤 6: 不变量论证 (本节的关键创新)**

QCMI 在 Buscemi 框架下的定义涉及对所有 "惰性扩展 F" 取极小:
$$I(R;E'|Q')^{Buscemi} = \min_F I(R;E'|Q'F)$$

对于 G = ∪ G_i (共享树 T), 不同的 G_i 需要不同的 "最优 F" —— 但 min_F I(R;E'|Q'F) 在所有 G_i 共享相同 Q 和 E 节点集的情况下, F 必须同时优化所有环的贡献。

**关键的 MV 观察:** 惰性扩展 F 屏蔽了可被经典关联解释的 QCMI 部分。对于 G = ∪ G_i, 如果 F 能同时屏蔽所有 G_i 的经典部分, 那么剩余的就是 "真正的因果回流" —— 这正是各环独立贡献的和。但由于 G_i 共享 Q 节点, 一个 F 不可能同时最优地屏蔽所有 G_i 的经典关联 —— **F 的优化空间受共享节点的约束**:

$$\min_F I_{G}(R;E'|Q'F) \geq \sum_i \min_{F_i} I_{G_i}(R;E'|Q'F_i)$$

因为 F 在联合系统上的优化空间是所有 G_i 的优化空间的**子集** (受共享 Q 节点的约束)。在独立 G_i 上, F_i 可以独立选择; 在联合 G 上, 必须选择一个统一的 F。更受约束的优化 → 更大的极小值 → 超可加性。

**形式化为:**

**Lemma (MV 超可加性引理 —— 候选):**
设 G = ∪_{i=1}^k G_i, 其中 G_i ∩ G_j = T (对所有 i ≠ j)。则在 Cartan 规范固定下:
$$I_G(R;E'|Q') \geq \sum_{i=1}^k I_{G_i}(R;E'|Q')$$

**证明策略:**
1. 在 Cartan 规范固定下, G 的酉 U_G = ∏_{i=1}^k U_{G_i} (顺序不重要 —— 所有树边酉=I, 非树边酉按拓扑顺序排列)
2. 每个 U_{G_i} 仅作用在 G_i 的非树边 e_i 上, 与所有其他 U_{G_j} (j≠i) 通过共享的 Q 节点连线
3. Buscemi 框架中的 QCMI 涉及 min_F I(R;E'|Q'F)
4. 由于 G_i 产生不同的有效 Kraus 算子 (因为 e_i 的 Cartan 系数不同), 它们的效应在 Kraus 表示中表现为矩阵乘积: K_{a_1...a_k} ∝ K^{(1)}_{a_1} · K^{(2)}_{a_2} · ... · K^{(k)}_{a_k} (作用在同一 Q 空间上)
5. QCMI > 0 要求至少一组 K_{a} 不成比例。对于 k 个环, 只有所有 K^{(i)} 可因子化 (即所有 Cartan 系数为零) 时总 K_{a} 才成比例
6. 如果至少一个环有非零 Cartan 系数, 总 QCMI 至少是该环的贡献 η(d)
7. 如果有 m ≤ k 个环有非零 Cartan 系数, 反证法 (如 b1_additivity.md §2.4 但推广到 m) 证明 QCMI ≥ m · η(d) —— 因为 m 个不同的 "非平凡方向" 不能通过有限的矩阵乘积互相抵消

**步骤 7: 纯同调论证 (不依赖物理直觉)**

将 QCMI 视为 H₁(G;ℝ) 上的 "能量泛函" Q, 我们需要证明:
$$Q\left(\sum_i [C_i]\right) \geq \sum_i Q([C_i])$$

定义: 对基本环 [C_i], Q([C_i]) = η_i ≥ η(d) > 0 (当环上 Cartan 系数非零)。

同调独立性 ⇒ 不存在非零线性关系 Σ a_i [C_i] = 0。这意味着在圈空间的任意线性组合中, 每个基本环保持其 "分量" —— 尽管 Q 不是线性的, 各分量的独立贡献不能互相抵消因为 H₁ 中不存在 a_i ≠ 0 使得 Σ a_i [C_i] = 0 (圈空间的线性独立性)。

**这不是一个完整的数学证明 —— 而是将问题从 "QCMI 超可加性" 重新表述为 "H₁(G;ℝ) 上的正泛函在下述条件下的性质: H₁(G) = ⊕ H₁(G_i), 且每个直和分量上的限制满足 Q|_{H₁(G_i)} ≥ η(d)"。** 如果 Q 满足某种 "不变量的超可加性" (由 min_F 的受限优化空间保证), 则 MV 分解直接推出 Q ≥ Σ Q|_{H₁(G_i)}。

**评估: 8/10** — 这是三个角度中最有形式化潜力的。MV 序列将图的同调分解为子图同调的直和 —— 这个分解是严格的 (代数拓扑定理)。将 QCMI 定义为 H₁ 上的泛函后, 超可加性的证明简化为 "在受限优化空间上 min_F ≥ Σ min_{F_i}" —— 这是一个标准的优化论论证。主要gap是 QCMI 的 Cartan 规范固定与 H₁ 泛函之间的精确对应 —— 但这在 b1_additivity.md §6.3 中已有部分形式化 (树边冻结引理)。

---

### 1.2 最终选择: 角度3 (Mayer-Vietoris + H₁ 能量泛函)

**理由:**

1. **数学基础最扎实:** MV 序列和 H₁ 的直和分解是代数拓扑的严格定理 —— 不需要物理直觉的 "类比跳跃"。

2. **与已有证明协同:** b1_additivity.md 的 "树边冻结引理" (非树边 Cartan 系数决定 QCMI) 与 H₁ 的 "生成树 + 基本环" 构造完全对应 —— 树边对应 exact 形式 (im(∂) 在 Hodge 分解中), 非树边对应调和形式 (ker(Δ₁))。

3. **优化论证的形式化路径存在:** min_F I(R;E'|Q'F) 的受限优化 → 超可加性 —— 这是一个标准的凸优化论证 (更小的可行域 → 更大的最优值)。Buscemi 框架的 F 优化恰好提供了这个结构。

4. **共享节点的 "干涉" 从 bug 变 feature:** 在 MV 视角下, 共享节点的干涉不产生抵消是因为 H₁ 的线性独立性 —— 不存在 "圈空间的线性关系" 使得一个环的效应被另一个环精确取消。QCMI 作为 H₁ 上的泛函保留了这个独立性。

5. **可测试:** MV 分解直接对应 "Cartan 规范固定 + 基本环基" 的数值方案 —— 可以逐个添加非树边, 测量 QCMI 的增量, 验证超可加性。

**论证草图 (最终版):**

> **定理 (QCMI 超可加性):** 设 G 是因果 Hasse 图 (团复形 1 维), T 是 G 的生成树, {e_1,...,e_k} 是非树边 (k = b₁(G))。设 G_i = T ∪ {e_i}。则在 Cartan 规范固定下:
> $$I_G(R;E'|Q') \geq \sum_{i=1}^k I_{G_i}(R;E'|Q') \geq \eta(d) \cdot b_1(G)$$
>
> **证明路径:**
> 1. (同调分解) MV 序列 ⇒ H₁(G) = ⊕_{i=1}^k H₁(G_i) — 严格 (代数拓扑)
> 2. (Cartan 规范固定) 树边冻结为 I ⇒ G 酉 = ∏_{i=1}^k U_{e_i} (非树边酉的乘积)
> 3. (QCMI 作为 H₁ 泛函) 定义 Q: H₁(G) → ℝ_{\geq 0}, Q([C_i]) = I_{G_i} ≥ η(d)
> 4. (优化超可加性) Buscemi min_F: F 在 G 上受限 (共享 Q 节点) ⇒ min_F I_G ≥ Σ min_{F_i} I_{G_i}
> 5. (结论) I_G ≥ Σ I_{G_i} ≥ k · η(d) = η(d) · b₁(G)

**残留gap (诚实标注):**
- 步骤 4 的优化论证需要形式化: 证明 Buscemi 框架中 F 的可行域在联合系统上是各子系统可行域的子集 (或更受约束)
- 步骤 2 的 "树边冻结引理" 需要严格证明 (b1_additivity.md 中已有部分论证, 需补全)
- 步骤 3 中 Q 作为 H₁ 泛函的定义需要从 Cartan 系数出发建立良定性

---

## 声张2: sin²θ 前因子 — 实验设计

### 2.0 问题陈述

从 Cartan 证明 (round3_cartan.md), d=2 时的 QCMI 下界为:

$$\eta(d=2) \geq 2p(1-p) \cdot \min_i |c^{(i)}|^2 \cdot \kappa^2(\gamma)$$

其中 |c|² = c_x² + c_y² + c_z² 是 Cartan 系数的模方。

从 interference_physics.md: 环的 QCMI bonus (环 QCMI - 树 QCMI) 依赖于门 Cartan 轴的对齐性, 且表现出 sin²θ 型依赖 (θ = Cartan 轴间夹角)。

**声张:** 单环 QCMI 的定量形式为:

$$\boxed{\text{QCMI}_{\text{cycle}} = \eta_0 + \beta \cdot \sin^2(\theta_{\text{misalign}}) \cdot |c|^2}$$

其中:
- η₀ 是基线 QCMI (来自树结构, 即使 Cartan 轴对齐也存在)
- β 是待测前因子, 预测 ∝ p(1-p)
- θ_misalign 是环上各门 Cartan 轴之间的最大失配角

**目标:** 设计实验确定 β 的具体值及其对 p 和 θ 的依赖关系, 消除当前 8x 不确定性。

---

### 2.1 实验方案: sin²θ 前因子测量

#### 实验 2.1.1: |c|² 线性度验证 + 前因子提取

**目标:** 验证 QCMI ∝ |c|², 提取前因子 β。

**步骤:**

1. 生成 N=500 个随机 2-qubit 酉 (Haar 测度)
2. 对每个酉 U, 数值计算其 Cartan/KAK 分解 → 得到 Cartan 系数 (c_x, c_y, c_z)
   - KAK 分解: U = (L₁⊗L₂) · D(c_x,c_y,c_z) · (R₁⊗R₂)
   - 提取 |c|² = c_x² + c_y² + c_z²
   - 记录 Cartan 轴方向 (c_x, c_y, c_z) / |c| (单位向量)
3. 对每个酉, 构造 4 节点环 (所有 4 边用同一个酉) → 计算 QCMI
4. 画 QCMI vs |c|² 散点图
5. 拟合下包络线: QCMI_min = a + b · |c|²
6. 提取系数 b → 这就是前因子 β

**预期结果:**
- 散点图应显示 QCMI 随 |c|² 单调增加的趋势
- 下包络应为线性: QCMI_min ∝ |c|²
- 上包络的散布由 Cartan 轴方向决定 (同轴 → 低 QCMI, 混轴 → 高 QCMI)

#### 实验 2.1.2: p 参数扫描

**目标:** 验证前因子 β ∝ p(1-p)。

**步骤:**

1. 固定 |c| 值 (选择 |c| = π/8, π/6, π/4 三个值)
2. 对每个 |c| 值, 生成 N=200 个随机 Cartan 轴方向的酉
3. 扫描 p ∈ {0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9}
4. 对每个 (|c|, p) 组合, 计算 QCMI 的均值和下包络
5. 对每个 p, 拟合 QCMI_min vs |c|² → 提取 β(p)
6. 画 β(p) vs p → 验证是否 ∝ p(1-p)

**预期结果:**
- β(p) 应在 p=0.5 达到最大值 (p(1-p) 最大)
- β(p) 应关于 p=0.5 对称: β(p) = β(1-p)
- β(p) / [p(1-p)] 应接近常数

#### 实验 2.1.3: sin²θ 依赖验证

**目标:** 验证 QCMI ∝ sin²(θ_misalign)。

**步骤:**

1. 固定 |c| = π/6 (中等 Cartan 系数)
2. 固定 p = 0.7 (代表性的中等混合度)
3. 生成具有不同 Cartan 轴失配角的酉对:
   - 纯 XX 门: c = (c_x, 0, 0) — 参考方向
   - 纯 ZZ 门: c = (0, 0, c_z)
   - 混合轴: 固定 |c|, 变化轴方向角度 θ
   - θ 扫描: θ ∈ {0, π/16, π/8, 3π/16, π/4, 3π/8, π/2}
4. 对每个 θ 的酉, 构造 4 节点环 (前两条边用参考 XX 门, 后两条边用 θ-旋转门)
5. 计算 QCMI
6. 画 QCMI vs sin²(θ) → 验证线性关系

**预期结果:**
- QCMI 应随 sin²(θ) 线性增长
- θ=0 (完全对齐, sin²=0) → QCMI 最小 (纯同轴环)
- θ=π/2 (最大失配, sin²=1) → QCMI 最大 (完全混轴环)

**验证项:** 对于 θ ∈ {0, π/2}, 检查 QCMI 是否对称 (sin²(θ) = sin²(π/2 - θ) 不成立, 但 sin²(θ) = sin²(π-θ) —— 需要检查 QCMI 是否仅依赖 sin²θ 而非 θ 本身)。

#### 实验 2.1.4: 环长依赖性 (额外)

**目标:** 验证前因子是否依赖环长 (4 节点 vs 6 节点 vs 8 节点)。

**步骤:**

1. 固定 |c| = π/6, p = 0.7
2. 构造不同长度的环: L ∈ {4, 6, 8} 条边
3. 每条边用相同的随机酉 (Haar, 固定 |c|)
4. 对每个 L, 计算 N=100 个随机样本的 QCMI
5. 比较不同 L 的 QCMI 分布

**预期:** 前因子 β 应独立于环长 (因为每条边的 Cartan 系数在环长不同的情况下仍起相同作用)。但 QCMI 的绝对值可能随 L 略有变化 (因为更长的环有更多的 BCH 累积机会)。

---

### 2.2 Python 脚本规格 (实验组可直接执行)

```python
#!/usr/bin/env python3
"""
sin2_theta_prefactor.py
=======================
Experiment: Measure the sin^2(theta) prefactor in the QCMI lower bound.

声张: QCMI_cycle = eta_0 + beta * sin^2(theta_misalign) * |c|^2
目标: Extract beta, verify beta ∝ p(1-p), verify sin^2(theta) dependence.

四个实验:
  E1: |c|^2 linearity — QCMI vs |c|^2 scatter, lower envelope fit
  E2: p-parameter scan — beta(p) vs p, verify beta ∝ p(1-p)
  E3: sin^2(theta) scan — QCMI vs sin^2(theta), verify linearity
  E4: Cycle length scan — QCMI vs cycle length L ∈ {4, 6, 8}

依赖: numpy, scipy, matplotlib, qiskit (或 cirq, 或手动 KAK)
Buscemi QCMI 计算: 使用现有的 qcmi_cycle.py (4节点环)

输出: figures/sin2_prefactor_*.png, data/sin2_prefactor_*.npz

作者: B博士 规格
日期: 2026-06-08
执行: 实验组
"""

import numpy as np
from scipy.linalg import sqrtm, eigvals
from scipy.optimize import curve_fit
from scipy.stats import linregress
import matplotlib.pyplot as plt
from pathlib import Path
import itertools

# ============================================================================
# Section 0: Utility Functions (被实验组实现)
# ============================================================================

def haar_random_u4() -> np.ndarray:
    """Generate a random 2-qubit unitary from Haar measure (U(4))."""
    # 使用 QR 分解法: 对 4x4 复随机矩阵 QR, 取 Q
    # 或使用 scipy.stats.unitary_group
    pass  # 实验组实现

def cartan_decompose_u4(U: np.ndarray) -> tuple:
    """
    KAK/Cartan decomposition of U(4) → (L1, L2, D, R1, R2).
    
    Returns:
        c: numpy array [c_x, c_y, c_z] — Cartan coefficients
        L1, L2, R1, R2: U(2) matrices
        D: 4x4 diagonal Cartan core
    """
    # 使用 Magic Basis 变换: |Phi^+>, i|Psi^->, i|Psi^+>, |Phi^->
    # 或使用 KroneckerProduct + svd 的标准算法
    # 参考: Zhang et al. (2003), PRA 67, 042313
    pass  # 实验组实现

def construct_4cycle_qcmi(U_list: list, p: float,
                          d_env: int = 2) -> float:
    """
    Construct 4-node causal cycle and compute Buscemi QCMI.
    
    Args:
        U_list: list of 4 U(4) matrices for edges [E1, E2, E3, E4]
        p: environment mixing parameter, gamma = diag(p, 1-p)
        d_env: environment qudit dimension (default 2)
        
    Returns:
        I(R;E'|Q') — conditional mutual information (float)
        
    Circuit topology (4-node cycle):
        Q_a —[U1]→ E_1 —[U2]→ Q_b —[U3]→ E_2 —[U4]→ Q_a
        
        初始态: Phi^+_{RQ} ⊗ gamma^{otimes 4}
        演化后测量 E 投影 (Buscemi 框架)
    """
    # 使用现有的 qcmi_cycle.py 中的实现
    # 关键步骤:
    # 1. 构造初始态 rho_RQE
    # 2. 应用 U = U4 * U3 * U2 * U1 (按拓扑顺序)
    # 3. Buscemi 框架: 测量 E → 惰性扩展 F → 计算 QCMI
    pass  # 实验组实现

def compute_qcmi_lower_envelope(x: np.ndarray, y: np.ndarray,
                                 n_bins: int = 20) -> tuple:
    """
    Compute the lower envelope of y vs x scatter data.
    
    Uses binning: for each bin of x, take the min (or 5th percentile) of y.
    
    Returns:
        x_bins, y_lower: bin centers and lower envelope values
    """
    pass  # 实验组实现

# ============================================================================
# Experiment E1: |c|^2 Linearity Verification
# ============================================================================

def experiment_e1_c_squared_linearity(
    N: int = 500,
    p: float = 0.7,
    save_dir: str = "./results"
):
    """
    E1: Verify QCMI ∝ |c|^2 and extract prefactor beta.
    
    For N random Haar U(4) matrices:
    1. Compute Cartan coefficients (c_x, c_y, c_z)
    2. Compute |c|^2 = c_x^2 + c_y^2 + c_z^2
    3. Construct 4-node cycle (all 4 edges use same U)
    4. Compute QCMI
    5. Scatter plot QCMI vs |c|^2
    6. Fit lower envelope: QCMI_min = a + b * |c|^2
    7. Extract b → beta
    
    Output:
        - Scatter plot: figures/sin2_prefactor_e1_scatter.png
        - Data: data/sin2_prefactor_e1.npz
    """
    print(f"[E1] |c|^2 Linearity: N={N}, p={p}")
    
    # Storage
    c_sq_list = []
    qcmi_list = []
    cartan_axes = []  # unit vectors (c_x, c_y, c_z) / |c|
    
    for i in range(N):
        # Step 1-2: Generate Haar random U and decompose
        U = haar_random_u4()
        c, _, _, _, _ = cartan_decompose_u4(U)
        c_sq = np.sum(c**2)
        
        # Step 3: Construct 4-cycle (all edges same U)
        U_list = [U, U, U, U]
        
        # Step 4: Compute QCMI
        try:
            qcmi = construct_4cycle_qcmi(U_list, p)
        except Exception as e:
            print(f"  Sample {i}: QCMI computation failed ({e}), skipping")
            continue
        
        c_sq_list.append(c_sq)
        qcmi_list.append(qcmi)
        if c_sq > 1e-10:
            cartan_axes.append(c / np.sqrt(c_sq))
        else:
            cartan_axes.append(np.array([0., 0., 0.]))
        
        if (i + 1) % 50 == 0:
            print(f"  Progress: {i+1}/{N}")
    
    c_sq_arr = np.array(c_sq_list)
    qcmi_arr = np.array(qcmi_list)
    cartan_axes_arr = np.array(cartan_axes)
    
    # Step 5: Scatter plot
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Left: QCMI vs |c|^2, colored by Cartan axis direction
    # Use the dominant axis direction as color
    dominant_axis = np.argmax(np.abs(cartan_axes_arr), axis=1)
    colors = ['red', 'green', 'blue']
    for k in range(3):
        mask = dominant_axis == k
        axes[0].scatter(c_sq_arr[mask], qcmi_arr[mask],
                       alpha=0.5, s=10, c=colors[k],
                       label=f'dominant axis {["X","Y","Z"][k]}')
    
    # Step 6: Lower envelope fit
    x_bins, y_lower = compute_qcmi_lower_envelope(c_sq_arr, qcmi_arr, n_bins=20)
    axes[0].plot(x_bins, y_lower, 'k-', linewidth=2, label='lower envelope')
    
    # Linear fit to lower envelope
    mask_valid = ~np.isnan(y_lower)
    slope, intercept, r_value, p_value, std_err = linregress(
        x_bins[mask_valid], y_lower[mask_valid]
    )
    beta = slope
    axes[0].plot(x_bins, intercept + slope * x_bins, 'k--',
                linewidth=1, label=f'fit: beta={beta:.4f}')
    
    axes[0].set_xlabel(r'$|c|^2 = c_x^2 + c_y^2 + c_z^2$')
    axes[0].set_ylabel('QCMI = I(R;E\'|Q\')')
    axes[0].set_title(f'E1: QCMI vs |c|^2 (N={N}, p={p})')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # Right: histogram of QCMI values
    axes[1].hist(qcmi_arr, bins=30, alpha=0.7, edgecolor='black')
    axes[1].axvline(np.median(qcmi_arr), color='red', linestyle='--',
                   label=f'median={np.median(qcmi_arr):.3f}')
    axes[1].set_xlabel('QCMI')
    axes[1].set_ylabel('Count')
    axes[1].set_title('QCMI distribution')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    
    # Save
    save_path = Path(save_dir)
    save_path.mkdir(parents=True, exist_ok=True)
    fig.savefig(save_path / 'sin2_prefactor_e1_scatter.png', dpi=150)
    plt.close(fig)
    
    # Save data
    np.savez(save_path / 'sin2_prefactor_e1.npz',
             c_sq=c_sq_arr, qcmi=qcmi_arr, cartan_axes=cartan_axes_arr,
             beta=beta, beta_std=std_err, intercept=intercept)
    
    print(f"[E1] Complete. beta = {beta:.4f} ± {std_err:.4f}")
    print(f"[E1] R^2 = {r_value**2:.4f}")
    
    return {
        'beta': beta,
        'beta_std': std_err,
        'intercept': intercept,
        'r_squared': r_value**2,
        'n_samples': N,
        'c_sq': c_sq_arr,
        'qcmi': qcmi_arr,
    }


# ============================================================================
# Experiment E2: p-Parameter Scan
# ============================================================================

def experiment_e2_p_scan(
    c_values: list = None,
    p_values: list = None,
    N_per_point: int = 200,
    save_dir: str = "./results"
):
    """
    E2: Scan environment mixing parameter p and extract beta(p).
    
    For each p and |c| value:
    1. Generate N random unitaries with fixed |c| = c_val
    2. Vary Cartan axis direction randomly (Haar on S^2)
    3. Compute QCMI for 4-cycle
    4. Fit lower envelope → beta(p, |c|)
    5. Verify beta(p) ∝ p(1-p)
    
    Output:
        - beta(p) curves: figures/sin2_prefactor_e2_beta_vs_p.png
        - Normalized beta: figures/sin2_prefactor_e2_beta_normalized.png
        - Data: data/sin2_prefactor_e2.npz
    """
    if c_values is None:
        c_values = [np.pi/8, np.pi/6, np.pi/4]
    if p_values is None:
        p_values = np.arange(0.50, 0.91, 0.05)
    
    print(f"[E2] p-Scan: |c|={c_values}, p={p_values}, N={N_per_point}")
    
    # Storage: beta[p_idx, c_idx]
    n_p = len(p_values)
    n_c = len(c_values)
    beta_matrix = np.zeros((n_p, n_c))
    beta_std_matrix = np.zeros((n_p, n_c))
    qcmi_means = np.zeros((n_p, n_c))
    qcmi_stds = np.zeros((n_p, n_c))
    
    for i, p in enumerate(p_values):
        for j, c_val in enumerate(c_values):
            print(f"  p={p:.2f}, |c|={c_val:.4f}")
            
            qcmi_samples = []
            c_sq_samples = []
            
            for k in range(N_per_point):
                # Generate U with fixed |c| but random axis direction
                # Method: random unit vector on S^2, scale by c_val
                axis = np.random.randn(3)
                axis = axis / np.linalg.norm(axis)  # random direction
                c = c_val * axis  # fixed magnitude, random direction
                
                # Construct Cartan core D(c)
                # D = exp(i * sum_k c_k * sigma_k ⊗ sigma_k)
                # Use closed form: D = cos|c| I + i(sin|c|/|c|) * sum_k c_k sigma_k⊗sigma_k
                sx = np.array([[0,1],[1,0]])
                sy = np.array([[0,-1j],[1j,0]])
                sz = np.array([[1,0],[0,-1]])
                paulis = [sx, sy, sz]
                
                cos_c = np.cos(c_val)
                sinc_c = np.sin(c_val) / c_val if c_val > 1e-10 else 1.0
                
                H_core = np.zeros((4, 4), dtype=complex)
                for k_idx in range(3):
                    H_core += c[k_idx] * np.kron(paulis[k_idx], paulis[k_idx])
                
                D = cos_c * np.eye(4) + 1j * sinc_c * H_core
                
                # Apply random local unitaries (L1, L2, R1, R2) — but these don't
                # affect QCMI (Cartan规范固定), so we can simplify:
                # Use D directly as the gate unitary
                # (Or apply random L,R for robustness check)
                U = D
                
                U_list = [U, U, U, U]
                
                try:
                    qcmi = construct_4cycle_qcmi(U_list, p)
                except Exception as e:
                    continue
                
                qcmi_samples.append(qcmi)
                c_sq_samples.append(c_val**2)
            
            if len(qcmi_samples) == 0:
                print(f"    WARNING: No valid samples for p={p}, |c|={c_val}")
                beta_matrix[i, j] = np.nan
                beta_std_matrix[i, j] = np.nan
                qcmi_means[i, j] = np.nan
                qcmi_stds[i, j] = np.nan
                continue
            
            qcmi_arr = np.array(qcmi_samples)
            c_sq_arr = np.array(c_sq_samples)
            
            qcmi_means[i, j] = np.mean(qcmi_arr)
            qcmi_stds[i, j] = np.std(qcmi_arr)
            
            # Fit lower envelope for this (p, |c|) combination
            x_bins, y_lower = compute_qcmi_lower_envelope(c_sq_arr, qcmi_arr)
            mask_valid = ~np.isnan(y_lower)
            if np.sum(mask_valid) >= 3:
                slope, intercept, r_value, p_value, std_err = linregress(
                    x_bins[mask_valid], y_lower[mask_valid]
                )
                beta_matrix[i, j] = slope
                beta_std_matrix[i, j] = std_err
            else:
                beta_matrix[i, j] = np.nan
                beta_std_matrix[i, j] = np.nan
    
    # Plot results
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))
    
    # Left: beta(p) for different |c|
    colors = ['blue', 'orange', 'green']
    for j, c_val in enumerate(c_values):
        axes[0].errorbar(p_values, beta_matrix[:, j],
                        yerr=beta_std_matrix[:, j],
                        marker='o', capsize=3, color=colors[j],
                        label=f'|c|={c_val:.4f}')
    # Overlay: p(1-p) theoretical curve (scaled)
    p_fine = np.linspace(0.5, 0.9, 100)
    pp_curve = p_fine * (1 - p_fine)
    axes[0].plot(p_fine, pp_curve / np.max(pp_curve) * np.nanmax(beta_matrix),
                'k--', alpha=0.5, label=r'$p(1-p)$ (scaled)')
    axes[0].set_xlabel('Environment mixing p')
    axes[0].set_ylabel(r'$\beta$ (prefactor)')
    axes[0].set_title('E2: Prefactor vs p')
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)
    
    # Center: beta(p) / [p(1-p)] → should be constant
    pp = p_values * (1 - p_values)
    for j, c_val in enumerate(c_values):
        beta_norm = beta_matrix[:, j] / pp
        axes[1].plot(p_values, beta_norm, marker='s', color=colors[j],
                    label=f'|c|={c_val:.4f}')
    axes[1].set_xlabel('Environment mixing p')
    axes[1].set_ylabel(r'$\beta / [p(1-p)]$')
    axes[1].set_title('E2: Normalized Prefactor (should be constant)')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    
    # Right: QCMI mean vs p for different |c|
    for j, c_val in enumerate(c_values):
        axes[2].errorbar(p_values, qcmi_means[:, j],
                        yerr=qcmi_stds[:, j],
                        marker='^', capsize=3, color=colors[j],
                        label=f'|c|={c_val:.4f}')
    axes[2].set_xlabel('Environment mixing p')
    axes[2].set_ylabel('Mean QCMI')
    axes[2].set_title('E2: Mean QCMI vs p')
    axes[2].legend()
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    save_path = Path(save_dir)
    save_path.mkdir(parents=True, exist_ok=True)
    fig.savefig(save_path / 'sin2_prefactor_e2_beta_vs_p.png', dpi=150)
    plt.close(fig)
    
    # Save data
    np.savez(save_path / 'sin2_prefactor_e2.npz',
             p_values=p_values, c_values=np.array(c_values),
             beta=beta_matrix, beta_std=beta_std_matrix,
             qcmi_mean=qcmi_means, qcmi_std=qcmi_stds)
    
    # Summary
    print(f"[E2] Complete.")
    for j, c_val in enumerate(c_values):
        ratio = beta_matrix[:, j] / pp
        ratio_clean = ratio[~np.isnan(ratio) & ~np.isinf(ratio)]
        if len(ratio_clean) > 0:
            print(f"  |c|={c_val:.4f}: beta/p(1-p) = {np.mean(ratio_clean):.4f} ± {np.std(ratio_clean):.4f}")
    
    return {
        'p_values': p_values,
        'c_values': np.array(c_values),
        'beta': beta_matrix,
        'beta_std': beta_std_matrix,
        'qcmi_mean': qcmi_means,
        'qcmi_std': qcmi_stds,
    }


# ============================================================================
# Experiment E3: sin^2(theta) Dependence
# ============================================================================

def experiment_e3_sin2_theta(
    c_mag: float = np.pi / 6,
    p: float = 0.7,
    N_per_theta: int = 100,
    save_dir: str = "./results"
):
    """
    E3: Verify QCMI ∝ sin^2(theta_misalign).
    
    Construct 4-cycles where:
    - Edges 1-2 use a gate with Cartan axis direction n_ref = (1,0,0) [pure XX]
    - Edges 3-4 use a gate with Cartan axis rotated by angle theta from n_ref
    
    The misalignment angle theta is the angle between the two Cartan axis directions.
    
    Scan theta from 0 (fully aligned → sin^2=0) to pi/2 (maximally misaligned → sin^2=1).
    
    If the claim holds: QCMI(theta) = QCMI(0) + const * sin^2(theta)
    
    Output:
        - QCMI vs sin^2(theta): figures/sin2_prefactor_e3_sin2.png
        - Data: data/sin2_prefactor_e3.npz
    """
    # Scan theta
    theta_values = np.array([0, np.pi/16, np.pi/8, 3*np.pi/16, np.pi/4,
                             3*np.pi/8, np.pi/2])
    n_theta = len(theta_values)
    
    print(f"[E3] sin^2(theta) Scan: |c|={c_mag:.4f}, p={p}")
    print(f"  theta values: {theta_values}")
    
    qcmi_means = np.zeros(n_theta)
    qcmi_stds = np.zeros(n_theta)
    qcmi_lower = np.zeros(n_theta)
    
    # Pauli matrices
    sx = np.array([[0,1],[1,0]])
    sy = np.array([[0,-1j],[1j,0]])
    sz = np.array([[1,0],[0,-1]])
    paulis = [sx, sy, sz]
    
    for i, theta in enumerate(theta_values):
        print(f"  theta={theta:.4f} (sin^2={np.sin(theta)**2:.4f})")
        
        qcmi_samples = []
        
        for k in range(N_per_theta):
            # Reference axis: pure XX
            c_ref = np.array([c_mag, 0.0, 0.0])
            
            # Rotated axis: rotate in XZ plane by theta
            # (Could also rotate in other planes for comparison)
            c_rot = np.array([c_mag * np.cos(theta), 0.0, c_mag * np.sin(theta)])
            
            # Construct Cartan cores
            def make_cartan_core(c):
                cos_c = np.cos(np.linalg.norm(c))
                c_norm = np.linalg.norm(c)
                sinc_c = np.sin(c_norm) / c_norm if c_norm > 1e-10 else 1.0
                H = np.zeros((4,4), dtype=complex)
                for idx in range(3):
                    H += c[idx] * np.kron(paulis[idx], paulis[idx])
                return cos_c * np.eye(4) + 1j * sinc_c * H
            
            U_ref = make_cartan_core(c_ref)
            U_rot = make_cartan_core(c_rot)
            
            # 4-cycle: edges [ref, ref, rot, rot]
            # This way, two consecutive edges share the ref axis,
            # and two share the rotated axis.
            U_list = [U_ref, U_ref, U_rot, U_rot]
            
            try:
                qcmi = construct_4cycle_qcmi(U_list, p)
            except Exception as e:
                continue
            
            qcmi_samples.append(qcmi)
        
        if len(qcmi_samples) == 0:
            qcmi_means[i] = np.nan
            qcmi_stds[i] = np.nan
            qcmi_lower[i] = np.nan
            continue
        
        qcmi_arr = np.array(qcmi_samples)
        qcmi_means[i] = np.mean(qcmi_arr)
        qcmi_stds[i] = np.std(qcmi_arr)
        qcmi_lower[i] = np.percentile(qcmi_arr, 5)  # 5th percentile as lower envelope
    
    # Fit: QCMI = A + B * sin^2(theta)
    sin2_values = np.sin(theta_values)**2
    mask_valid = ~np.isnan(qcmi_means) & ~np.isnan(qcmi_lower)
    
    # Fit to mean
    def linear_model(x, a, b):
        return a + b * x
    
    popt_mean, pcov_mean = curve_fit(
        linear_model, sin2_values[mask_valid],
        qcmi_means[mask_valid],
        p0=[np.min(qcmi_means[mask_valid]), 1.0]
    )
    
    # Fit to lower envelope
    popt_lower, pcov_lower = curve_fit(
        linear_model, sin2_values[mask_valid],
        qcmi_lower[mask_valid],
        p0=[np.min(qcmi_lower[mask_valid]), 1.0]
    )
    
    # Plot
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    
    ax.errorbar(sin2_values, qcmi_means, yerr=qcmi_stds,
               marker='o', capsize=4, color='blue', label='mean QCMI')
    ax.scatter(sin2_values, qcmi_lower, marker='s', color='red',
              label='5th percentile (lower envelope)')
    
    # Fit lines
    sin2_fine = np.linspace(0, 1, 100)
    ax.plot(sin2_fine, linear_model(sin2_fine, *popt_mean),
           'b--', alpha=0.5, label=f'fit mean: A={popt_mean[0]:.3f}, B={popt_mean[1]:.3f}')
    ax.plot(sin2_fine, linear_model(sin2_fine, *popt_lower),
           'r--', alpha=0.5, label=f'fit lower: A={popt_lower[0]:.3f}, B={popt_lower[1]:.3f}')
    
    ax.set_xlabel(r'$\sin^2(\theta_{\rm{misalign}})$')
    ax.set_ylabel('QCMI')
    ax.set_title(f'E3: QCMI vs sin^2(theta) (|c|={c_mag:.4f}, p={p})')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    save_path = Path(save_dir)
    save_path.mkdir(parents=True, exist_ok=True)
    fig.savefig(save_path / 'sin2_prefactor_e3_sin2.png', dpi=150)
    plt.close(fig)
    
    # Save data
    np.savez(save_path / 'sin2_prefactor_e3.npz',
             theta=theta_values, sin2=sin2_values,
             qcmi_mean=qcmi_means, qcmi_std=qcmi_stds,
             qcmi_lower=qcmi_lower,
             fit_A_mean=popt_mean[0], fit_B_mean=popt_mean[1],
             fit_A_lower=popt_lower[0], fit_B_lower=popt_lower[1])
    
    print(f"[E3] Complete.")
    print(f"  Fit (mean):   QCMI = {popt_mean[0]:.4f} + {popt_mean[1]:.4f} * sin^2(theta)")
    print(f"  Fit (lower):  QCMI = {popt_lower[0]:.4f} + {popt_lower[1]:.4f} * sin^2(theta)")
    print(f"  Predicted B = beta * |c|^2. Check: B_lower / |c|^2 = {popt_lower[1] / c_mag**2:.4f}")
    
    return {
        'theta': theta_values,
        'sin2': sin2_values,
        'qcmi_mean': qcmi_means,
        'qcmi_std': qcmi_stds,
        'qcmi_lower': qcmi_lower,
        'fit_B_mean': popt_mean[1],
        'fit_B_lower': popt_lower[1],
    }


# ============================================================================
# Experiment E4: Cycle Length Dependence
# ============================================================================

def experiment_e4_cycle_length(
    c_mag: float = np.pi / 6,
    p: float = 0.7,
    N_per_L: int = 100,
    save_dir: str = "./results"
):
    """
    E4: Verify prefactor beta is independent of cycle length.
    
    Construct cycles of length L ∈ {4, 6, 8}.
    All edges use the same random Haar unitary (fixed |c| = c_mag).
    
    If beta is length-independent: QCMI should be ~constant across L.
    
    Output:
        - QCMI vs cycle length: figures/sin2_prefactor_e4_length.png
        - Data: data/sin2_prefactor_e4.npz
    """
    L_values = [4, 6, 8]
    
    print(f"[E4] Cycle Length Scan: L={L_values}, |c|={c_mag:.4f}, p={p}")
    
    qcmi_data = {}
    
    for L in L_values:
        print(f"  L={L}")
        qcmi_samples = []
        
        for k in range(N_per_L):
            # Generate L identical Cartan cores with fixed |c|, random axis
            axis = np.random.randn(3)
            axis = axis / np.linalg.norm(axis)
            c = c_mag * axis
            
            # Construct Cartan core
            sx = np.array([[0,1],[1,0]])
            sy = np.array([[0,-1j],[1j,0]])
            sz = np.array([[1,0],[0,-1]])
            paulis = [sx, sy, sz]
            
            cos_c = np.cos(c_mag)
            sinc_c = np.sin(c_mag) / c_mag if c_mag > 1e-10 else 1.0
            H_core = np.zeros((4,4), dtype=complex)
            for idx in range(3):
                H_core += c[idx] * np.kron(paulis[idx], paulis[idx])
            D = cos_c * np.eye(4) + 1j * sinc_c * H_core
            
            U_list = [D] * L
            
            try:
                qcmi = construct_4cycle_qcmi(U_list, p)
            except Exception as e:
                continue
            
            qcmi_samples.append(qcmi)
        
        qcmi_data[L] = {
            'samples': np.array(qcmi_samples),
            'mean': np.mean(qcmi_samples),
            'std': np.std(qcmi_samples),
        }
    
    # Plot
    fig, ax = plt.subplots(1, 1, figsize=(7, 5))
    
    L_arr = np.array(L_values)
    means = np.array([qcmi_data[L]['mean'] for L in L_values])
    stds = np.array([qcmi_data[L]['std'] for L in L_values])
    
    ax.errorbar(L_arr, means, yerr=stds, marker='o', capsize=5,
               markersize=10, linewidth=2, color='darkblue')
    ax.axhline(means[0], color='red', linestyle='--', alpha=0.5,
              label=f'reference (L=4): {means[0]:.3f}')
    
    ax.set_xlabel('Cycle Length L')
    ax.set_ylabel('QCMI')
    ax.set_title(f'E4: QCMI vs Cycle Length (|c|={c_mag:.4f}, p={p})')
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_xticks(L_values)
    
    plt.tight_layout()
    save_path = Path(save_dir)
    save_path.mkdir(parents=True, exist_ok=True)
    fig.savefig(save_path / 'sin2_prefactor_e4_length.png', dpi=150)
    plt.close(fig)
    
    # Save data
    np.savez(save_path / 'sin2_prefactor_e4.npz',
             L_values=L_arr, means=means, stds=stds)
    
    print(f"[E4] Complete.")
    for L in L_values:
        print(f"  L={L}: QCMI = {qcmi_data[L]['mean']:.4f} ± {qcmi_data[L]['std']:.4f}")
    
    return qcmi_data


# ============================================================================
# Main: Run all experiments
# ============================================================================

def main():
    """Run all four sin^2(theta) prefactor experiments."""
    
    print("=" * 70)
    print("sin^2(theta) Prefactor Measurement Suite")
    print("B博士 规格 — 实验组执行")
    print("=" * 70)
    
    save_dir = "./results/sin2_prefactor"
    
    # E1: |c|^2 linearity (fastest, ~500 QCMI computations)
    print("\n" + "=" * 70)
    print("E1: Start")
    print("=" * 70)
    results_e1 = experiment_e1_c_squared_linearity(
        N=500, p=0.7, save_dir=save_dir
    )
    
    # E2: p-scan (~9 p-values * 3 |c|-values * 200 samples = 5400 QCMI)
    print("\n" + "=" * 70)
    print("E2: Start (this is the most expensive experiment ~5400 QCMI)")
    print("=" * 70)
    results_e2 = experiment_e2_p_scan(
        c_values=[np.pi/8, np.pi/6, np.pi/4],
        p_values=list(np.arange(0.50, 0.91, 0.05)),
        N_per_point=200,
        save_dir=save_dir
    )
    
    # E3: sin^2(theta) scan (~7 theta * 100 samples = 700 QCMI)
    print("\n" + "=" * 70)
    print("E3: Start")
    print("=" * 70)
    results_e3 = experiment_e3_sin2_theta(
        c_mag=np.pi/6, p=0.7, N_per_theta=100, save_dir=save_dir
    )
    
    # E4: Cycle length scan (~3 L * 100 samples = 300 QCMI)
    print("\n" + "=" * 70)
    print("E4: Start")
    print("=" * 70)
    results_e4 = experiment_e4_cycle_length(
        c_mag=np.pi/6, p=0.7, N_per_L=100, save_dir=save_dir
    )
    
    # Summary
    print("\n" + "=" * 70)
    print("ALL EXPERIMENTS COMPLETE")
    print("=" * 70)
    print(f"\nE1: beta = {results_e1['beta']:.4f} ± {results_e1['beta_std']:.4f}")
    print(f"E3: B_lower = {results_e3['fit_B_lower']:.4f}")
    print(f"     B_lower / |c|^2 = {results_e3['fit_B_lower'] / (np.pi/6)**2:.4f}")
    print(f"     (should equal E1 beta ≈ {results_e1['beta']:.4f})")
    print(f"\nResults saved to: {save_dir}/")
    print("Files:")
    print("  sin2_prefactor_e1_scatter.png")
    print("  sin2_prefactor_e2_beta_vs_p.png")
    print("  sin2_prefactor_e3_sin2.png")
    print("  sin2_prefactor_e4_length.png")
    print("  sin2_prefactor_e*.npz (raw data)")


if __name__ == "__main__":
    main()
```

---

### 2.3 实验组执行说明

**运行环境要求:**
- Python 3.9+, numpy, scipy, matplotlib
- QCMI 计算后端 (qcmi_cycle.py 或等效)
- 推荐: 至少 16 GB RAM (对大 N 的 Haar 采样)
- 时间估计 (单线程参考, 4090 GPU 加速):
  - E1 (~500 QCMI): ~2-5 分钟
  - E2 (~5400 QCMI): ~20-50 分钟
  - E3 (~700 QCMI): ~3-8 分钟
  - E4 (~300 QCMI): ~1-3 分钟
  - **总计:** ~30-70 分钟

**需要实验组实现的函数 (用 `pass` 标记):**
1. `haar_random_u4()`: Haar 随机 U(4) 采样器
2. `cartan_decompose_u4(U)`: U(4) KAK/Cartan 分解
3. `construct_4cycle_qcmi(U_list, p)`: 4 节点环 Buscemi QCMI 计算 (核心)
4. `compute_qcmi_lower_envelope(x, y, n_bins)`: 下包络分箱计算

**核心注意事项:**
- `construct_4cycle_qcmi` 必须支持任意环长 L (不仅是 4 边), 用于 E4
- Cartan 分解使用 Magic Basis 方法 (Zhang et al. 2003) 或等价的数值对角化
- 环境态 γ = diag(p, 1-p) 是单 qubit 环境态, 4 节点环需要 m=4 个环境 qubit

**输出产物清单:**
| 文件 | 内容 |
|:---|:---|
| `sin2_prefactor_e1_scatter.png` | QCMI vs \|c\|² 散点图 + 下包络拟合 |
| `sin2_prefactor_e2_beta_vs_p.png` | β(p) 曲线 + 归一化 β/p(1-p) + 均值 QCMI |
| `sin2_prefactor_e3_sin2.png` | QCMI vs sin²(θ_misalign) + 线性拟合 |
| `sin2_prefactor_e4_length.png` | QCMI vs 环长 L |
| `sin2_prefactor_e1.npz` | 原始数据: c_sq, qcmi, cartan_axes, beta |
| `sin2_prefactor_e2.npz` | β 矩阵, p_values, c_values, qcmi 统计 |
| `sin2_prefactor_e3.npz` | sin²θ 扫描数据 + 拟合参数 |
| `sin2_prefactor_e4.npz` | 环长扫描数据 |

**关键数值指标 (实验组完成后汇报):**
1. β (E1 下包络斜率): 预期 > 0, 与 p(1-p)·κ²(γ) 成比例
2. β/p(1-p) (E2 归一化): 预期 ≈ 常数 (独立于 p)
3. B_lower / \|c\|² (E3): 预期 ≈ β (一致性检验)
4. 环长独立性 (E4): 预期 QCMI 在 L=4,6,8 近似恒定

---

## 声张3: Pointer Basis — 实验设计

### 3.0 问题陈述

从 interference_physics.md, AHA-3:

> **Pointer basis = 环境因果环网络中产生最大相消干涉的 Cartan 轴方向。**

即: 在 4 节点因果环中, 当所有门的 Cartan 轴对齐到同一个方向 n 时, QCMI 达到最小值 (环的量子 Zeno 效应 —— 加速退相干, 信息被最快地经典化)。这个使 QCMI 最小的 Cartan 轴方向 n* 就是 "Pointer basis"。

**声张 (可检验):**
> 在具有因果环的环境网络中, 存在一个特殊方向 n* ∈ S² (Cartan 轴方向), 使得当所有门沿 n* 对齐时 QCMI 最小。这个 n* 等价于标准量子达尔文主义中的 Pointer basis (与环境相互作用 Hamiltonian 对易的基)。

**实验目标:** 验证 min_QCMI 对应的局域基方向是否与 "自然 Pointer basis" (计算基, σ_z 对角) 一致。

---

### 3.1 实验方案: Pointer Basis 实验验证

#### 实验 3.1.1: 局域基旋转扫描 — 寻找 min_QCMI 方向

**核心思路:**
固定 4 节点环 + 固定门的 Cartan 核心 (如 CNOT: c = (π/4, 0, 0), 单 XX 轴)。通过在节点上施加局域基旋转 (SU(2) 局部酉), 有效旋转 Cartan 轴方向: c → R_v c R_v†。扫描所有可能的局域基方向, 找到使 QCMI 最小的方向 —— 这就是 Pointer basis。

**具体步骤:**

1. **固定环拓扑:** 4 节点环 Q_a → E_1 → Q_b → E_2 → Q_a
2. **固定 Cartan 核心:** 选择纯 XX 门: D = exp(i · π/4 · σ_x ⊗ σ_x)
3. **局域基旋转参数化:** 在节点 Q_a 和 Q_b 上施加局域酉 R_a, R_b ∈ SU(2)
   - 这等价于变换边酉: U → (R_a ⊗ I) U (R_b† ⊗ I) 等
   - 总效果: Cartan 轴 c 被旋转: c → R_a c R_a† (对于某些边的组合)
4. **扫描局域基:** 参数化 R_a = exp(i θ_a n_a · σ/2), 扫描 θ_a ∈ [0, π], n_a 在 S² 上采样
5. **计算 QCMI** 为每个局域基组合
6. **找到 min_QCMI** 对应的 (R_a*, R_b*), 确定有效的 Cartan 轴方向 n*
7. **比较:** n* 是否 = (0, 0, 1) (σ_z 对角基, 即计算基)?

**如果 n* = (0, 0, 1):** 声张成立 —— Pointer basis = 计算基 (σ_z 对角) = min_QCMI 方向。

**如果 n* ≠ (0, 0, 1):** 需要物理解释。可能的原因:
- Buscemi 框架的 "惰性扩展 F" 可能偏好不同的基方向
- 环拓扑 (4 节点) 的特殊几何可能产生偏离
- 环境态 γ 的特定选择可能导致不同的 "最优测量基"

#### 实验 3.1.2: Cartan 核心扫描

**目标:** 验证 Pointer basis 是否依赖于 Cartan 核心的选择。

**步骤:**

1. 测试三种不同的 Cartan 核心:
   - 纯 XX: D = exp(i · π/4 · σ_x ⊗ σ_x), c = (π/4, 0, 0)
   - 纯 ZZ: D = exp(i · π/4 · σ_z ⊗ σ_z), c = (0, 0, π/4)
   - 混合: D = exp(i · π/6 · (σ_x ⊗ σ_x + σ_z ⊗ σ_z) / √2)
2. 对每种核心, 重复实验 3.1.1 的局域基扫描
3. 比较三种情况下的 min_QCMI 方向

**预期:**
- 纯 XX 核心: min_QCMI 方向应该也是 XX 轴方向 (即局域基不对 Cartan 轴做任何旋转时 QCMI 最小)
  - 因为同轴环 → 量子 Zeno 效应 → QCMI 最小
- 纯 ZZ 核心: min_QCMI 方向应为 ZZ 轴 (计算基)
- 混合核心: min_QCMI 方向可能在 XX 和 ZZ 之间 (由两个分量的相对大小决定)

**关键洞见:** 如果对于纯 XX 核心, min_QCMI 方向确实是 XX 轴 (即局域基不旋转), 则 Pointer basis = "使环上所有门同轴的 Cartan 轴方向"。这个方向由**门的 Cartan 核心决定**, 而非外部的 "系统-环境 Hamiltonian"。

这与标准量子达尔文主义的关键差异是: **Pointer basis 不是由固定的系统-环境耦合决定的 —— 它是由环境网络中的因果环拓扑通过门的 Cartan 轴对齐干涉动态选择的。**

#### 实验 3.1.3: 双环竞争 Pointer basis

**目标:** 验证多个环竞争时的 Pointer basis 选择。

**步骤:**

1. 构造两个 4 节点环共享 2 个 Q 节点 (与 b1_additivity.md §2.1 相同的设置)
2. 环 A: 所有门使用纯 XX Cartan 核心 (c = (π/4, 0, 0))
3. 环 B: 所有门使用纯 ZZ Cartan 核心 (c = (0, 0, π/4))
4. 在共享节点上施加局域基旋转 R_shared ∈ SU(2)
5. 扫描 R_shared, 计算 QCMI
6. 找到 min_QCMI 对应的 R_shared*

**分析:**
- 如果 |c_XX| = |c_ZZ| (两个环的 "强度" 相同): min_QCMI 方向应位于 XX 和 ZZ 轴的 "中间" —— Pointer basis 是两个环竞争的 "妥协" 结果
- 如果 |c_XX| > |c_ZZ|: min_QCMI 应偏向 XX 轴 —— 更强的 Cartan 系数 (更大的信息流) 具有更大的 "投票权"
- Pointer basis 是加权平均值: n* ∝ |c_A| · n_A + |c_B| · n_B

**这一实验直接检验 AHA-3 的核心声张:** Pointer basis 是环干涉网络竞争的结果, 而非预先固定的。

---

### 3.2 Python 脚本规格 (实验组可直接执行)

```python
#!/usr/bin/env python3
"""
pointer_basis_experiment.py
===========================
Experiment: Find Pointer Basis = argmin_QCMI(Cartan axis direction).

声张: Pointer basis = Cartan axis direction that minimizes QCMI in a causal cycle.
      This direction should correspond to the "classical basis" (sigma_z diagonal).

三个实验:
  PB1: Local basis rotation scan — find min_QCMI direction
  PB2: Cartan core scan — verify Pointer basis = Cartan axis direction
  PB3: Two-cycle competition — verify Pointer basis = weighted average of cycle axes

依赖: numpy, scipy, matplotlib
QCMI 计算: 使用现有的 qcmi_cycle.py (4节点环)

输出: figures/pointer_basis_*.png, data/pointer_basis_*.npz

作者: B博士 规格
日期: 2026-06-08
执行: 实验组
"""

import numpy as np
from scipy.linalg import expm
from scipy.optimize import minimize
import matplotlib.pyplot as plt
from pathlib import Path
from itertools import product

# ============================================================================
# Section 0: Utility Functions (被实验组实现)
# ============================================================================

def construct_4cycle_qcmi_with_local_rotations(
    cartan_core_D: np.ndarray,
    local_rots: list,  # [R_a1, R_a2, R_b1, R_b2] 4 local SU(2) rotations
    p: float,
    d_env: int = 2
) -> float:
    """
    Construct 4-node cycle with local basis rotations and compute QCMI.
    
    Cycle topology:
        Q_a —[U1]→ E_1 —[U2]→ Q_b —[U3]→ E_2 —[U4]→ Q_a
    
    Each edge unitary U_k = (R_{from} ⊗ I) * cartan_core_D * (R_{to}^† ⊗ I)
    
    Local rotations are applied to Q nodes only (E nodes are environmental,
    not rotated).
    
    Args:
        cartan_core_D: 4x4 Cartan core matrix D(c_x, c_y, c_z)
        local_rots: list of 4 SU(2) matrices for Q nodes [Q_a_in, Q_a_out, Q_b_in, Q_b_out]
                     (a node appears twice in the cycle: as outgoing and incoming)
        p: environment mixing parameter
        d_env: environment qudit dimension
        
    Returns:
        I(R;E'|Q') — conditional mutual information
    """
    # Key: local rotations on Q nodes effectively rotate the Cartan axis
    # U_effective = (R_left ⊗ I) * D(c) * (R_right^† ⊗ I)
    #              = D(R_left c R_right^†)  [the Cartan axis is rotated]
    #
    # Note: Since D(c) = exp(i sum_k c_k sigma_k ⊗ sigma_k),
    # conjugating by local unitaries R ⊗ I transforms sigma_k → R sigma_k R^†
    # which corresponds to rotating the Cartan axis vector c.
    pass  # 实验组实现

def su2_matrix(theta: float, axis: np.ndarray) -> np.ndarray:
    """SU(2) rotation matrix: exp(i * theta * axis·sigma / 2)."""
    axis = np.asarray(axis) / np.linalg.norm(axis)
    sigma = [np.array([[0,1],[1,0]]),
             np.array([[0,-1j],[1j,0]]),
             np.array([[1,0],[0,-1]])]
    generator = axis[0]*sigma[0] + axis[1]*sigma[1] + axis[2]*sigma[2]
    return expm(1j * theta * generator / 2)

def make_cartan_core(c: np.ndarray) -> np.ndarray:
    """Construct D(c) = exp(i sum_k c_k sigma_k ⊗ sigma_k)."""
    c_norm = np.linalg.norm(c)
    cos_c = np.cos(c_norm)
    sinc_c = np.sin(c_norm) / c_norm if c_norm > 1e-10 else 1.0
    
    sx = np.array([[0,1],[1,0]])
    sy = np.array([[0,-1j],[1j,0]])
    sz = np.array([[1,0],[0,-1]])
    paulis = [sx, sy, sz]
    
    H = np.zeros((4,4), dtype=complex)
    for k in range(3):
        H += c[k] * np.kron(paulis[k], paulis[k])
    
    return cos_c * np.eye(4) + 1j * sinc_c * H

# ============================================================================
# Experiment PB1: Local Basis Rotation Scan
# ============================================================================

def experiment_pb1_local_basis_scan(
    cartan_c: np.ndarray = None,
    p: float = 0.7,
    n_theta: int = 20,
    n_axis: int = 50,
    save_dir: str = "./results"
):
    """
    PB1: Scan local basis rotations to find min_QCMI direction.
    
    Fix the Cartan core D(c) and scan SU(2) rotations on Q nodes.
    Record QCMI for each rotation and find the minimizing direction.
    
    If the claim holds: min_QCMI direction = Cartan axis direction of the core.
    
    Output:
        - QCMI heatmap on S^2: figures/pointer_basis_pb1_sphere.png
        - Data: data/pointer_basis_pb1.npz
    """
    if cartan_c is None:
        cartan_c = np.array([np.pi/4, 0.0, 0.0])  # Pure XX, like CNOT
    
    print(f"[PB1] Local Basis Scan: c = ({cartan_c[0]:.4f}, {cartan_c[1]:.4f}, {cartan_c[2]:.4f}), p={p}")
    
    D_core = make_cartan_core(cartan_c)
    
    # Sample points on S^2 (Fibonacci sphere for uniform sampling)
    # Each point = rotation axis direction for local basis
    # We apply the SAME rotation to both Q_a and Q_b for simplicity
    # (full scan of independent R_a, R_b would be 4D — too expensive)
    
    theta_values = np.linspace(0, np.pi, n_theta)
    phi_values = np.linspace(0, 2*np.pi, n_theta * 2)
    
    qcmi_grid = np.zeros((len(theta_values), len(phi_values)))
    cartan_axis_rotated = np.zeros((len(theta_values), len(phi_values), 3))
    
    for i, theta in enumerate(theta_values):
        for j, phi in enumerate(phi_values):
            # Axis direction on S^2
            axis = np.array([
                np.sin(theta) * np.cos(phi),
                np.sin(theta) * np.sin(phi),
                np.cos(theta)
            ])
            
            # SU(2) rotation around this axis by angle pi/2
            # (Rotating the local basis while keeping the Cartan core fixed)
            R = su2_matrix(np.pi/2, axis)
            
            # Apply rotation to Q nodes
            # In 4-cycle topology, Q_a appears as target of E_2 and source of E_1
            # Q_b appears as target of E_1 and source of E_2
            local_rots = [R, R, R, R]  # Same rotation on all Q appearances
            
            try:
                qcmi = construct_4cycle_qcmi_with_local_rotations(
                    D_core, local_rots, p
                )
            except Exception as e:
                qcmi = np.nan
            
            qcmi_grid[i, j] = qcmi
            
            # Compute effective Cartan axis after rotation
            # c_eff = R * c * R^† (rotation of 3-vector c by SO(3) rotation from SU(2))
            # SU(2) rotation on Bloch sphere = SO(3) rotation of axis vector
            R_so3 = _su2_to_so3(R)
            c_eff = R_so3 @ cartan_c
            cartan_axis_rotated[i, j, :] = c_eff
    
    # Find minimum QCMI and corresponding direction
    min_idx = np.unravel_index(np.nanargmin(qcmi_grid), qcmi_grid.shape)
    min_qcmi = qcmi_grid[min_idx]
    min_axis = cartan_axis_rotated[min_idx[0], min_idx[1], :]
    
    print(f"  min QCMI = {min_qcmi:.4f}")
    print(f"  at axis direction = ({min_axis[0]:.4f}, {min_axis[1]:.4f}, {min_axis[2]:.4f})")
    print(f"  original Cartan axis = ({cartan_c[0]:.4f}, {cartan_c[1]:.4f}, {cartan_c[2]:.4f})")
    print(f"  angle between = {np.arccos(np.abs(np.dot(min_axis, cartan_c / np.linalg.norm(cartan_c)))):.4f} rad")
    
    # Plot
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Left: QCMI on (theta, phi) grid
    theta_mesh, phi_mesh = np.meshgrid(theta_values, phi_values, indexing='ij')
    im = axes[0].pcolormesh(phi_mesh, theta_mesh, qcmi_grid,
                           shading='auto', cmap='viridis')
    axes[0].scatter(phi_values[min_idx[1]], theta_values[min_idx[0]],
                   marker='*', color='red', s=200, edgecolors='white',
                   label=f'min QCMI = {min_qcmi:.3f}')
    axes[0].set_xlabel(r'$\phi$')
    axes[0].set_ylabel(r'$\theta$')
    axes[0].set_title(f'PB1: QCMI vs Local Basis Rotation\nc=({cartan_c[0]:.2f},{cartan_c[1]:.2f},{cartan_c[2]:.2f})')
    axes[0].legend()
    plt.colorbar(im, ax=axes[0], label='QCMI')
    
    # Right: QCMI vs angle between rotated axis and original Cartan axis
    angles = []
    qcmi_flat = []
    for i in range(len(theta_values)):
        for j in range(len(phi_values)):
            if not np.isnan(qcmi_grid[i, j]):
                c_orig_unit = cartan_c / np.linalg.norm(cartan_c)
                c_rot_unit = cartan_axis_rotated[i, j, :]
                c_rot_norm = np.linalg.norm(c_rot_unit)
                if c_rot_norm > 1e-10:
                    c_rot_unit = c_rot_unit / c_rot_norm
                    angle = np.arccos(np.clip(np.abs(np.dot(c_orig_unit, c_rot_unit)), -1, 1))
                    angles.append(angle)
                    qcmi_flat.append(qcmi_grid[i, j])
    
    angles = np.array(angles)
    qcmi_flat = np.array(qcmi_flat)
    
    axes[1].scatter(angles, qcmi_flat, alpha=0.3, s=5)
    # Also compute and plot lower envelope
    sort_idx = np.argsort(angles)
    angles_sorted = angles[sort_idx]
    qcmi_sorted = qcmi_flat[sort_idx]
    
    # Simple lower envelope by binning
    n_bins = 30
    bin_edges = np.linspace(0, np.pi/2, n_bins + 1)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    lower_env = np.full(n_bins, np.nan)
    for k in range(n_bins):
        mask = (angles >= bin_edges[k]) & (angles < bin_edges[k+1])
        if np.any(mask):
            lower_env[k] = np.percentile(qcmi_flat[mask], 10)
    
    mask_valid = ~np.isnan(lower_env)
    axes[1].plot(bin_centers[mask_valid], lower_env[mask_valid],
                'r-', linewidth=2, label='lower envelope')
    axes[1].set_xlabel('Angle between rotated and original Cartan axis')
    axes[1].set_ylabel('QCMI')
    axes[1].set_title('PB1: QCMI vs Cartan Axis Misalignment')
    axes[1].legend()
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    save_path = Path(save_dir)
    save_path.mkdir(parents=True, exist_ok=True)
    fig.savefig(save_path / 'pointer_basis_pb1_sphere.png', dpi=150)
    plt.close(fig)
    
    # Save data
    np.savez(save_path / 'pointer_basis_pb1.npz',
             theta=theta_values, phi=phi_values,
             qcmi_grid=qcmi_grid, cartan_axis_rotated=cartan_axis_rotated,
             min_qcmi=min_qcmi, min_axis=min_axis, cartan_c=cartan_c)
    
    return {
        'min_qcmi': min_qcmi,
        'min_axis': min_axis,
        'cartan_c': cartan_c,
        'misalignment_angle': np.arccos(np.abs(np.dot(min_axis, cartan_c / np.linalg.norm(cartan_c)))),
    }


def _su2_to_so3(R_su2: np.ndarray) -> np.ndarray:
    """
    Convert SU(2) rotation matrix to SO(3) rotation matrix.
    
    SU(2) → SO(3) double cover:
    R_su2 * (n·sigma) * R_su2^† = (R_so3 * n)·sigma
    """
    # Extract rotation axis and angle from SU(2) matrix
    # R = exp(i theta n·sigma/2) = cos(theta/2) I + i sin(theta/2) n·sigma
    # Trace(R) = 2 cos(theta/2) → theta = 2 arccos(Tr(R)/2)
    
    trace_R = np.real(np.trace(R_su2))
    cos_half_theta = np.clip(trace_R / 2, -1, 1)
    theta = 2 * np.arccos(cos_half_theta)
    
    if np.abs(theta) < 1e-10 or np.abs(theta - 2*np.pi) < 1e-10:
        return np.eye(3)  # Identity rotation
    
    # Extract rotation axis
    sin_half_theta = np.sin(theta / 2)
    if np.abs(sin_half_theta) < 1e-10:
        return np.eye(3)
    
    # n_k = -i * Tr(sigma_k * R) / (2 sin(theta/2))
    sx = np.array([[0,1],[1,0]])
    sy = np.array([[0,-1j],[1j,0]])
    sz = np.array([[1,0],[0,-1]])
    n = np.array([
        -np.imag(np.trace(sx @ R_su2)) / (2 * sin_half_theta),
        -np.imag(np.trace(sy @ R_su2)) / (2 * sin_half_theta),
        -np.imag(np.trace(sz @ R_su2)) / (2 * sin_half_theta),
    ])
    
    # Rodrigues' rotation formula
    n = n / np.linalg.norm(n)
    cos_t = np.cos(theta)
    sin_t = np.sin(theta)
    
    K = np.array([[0, -n[2], n[1]],
                  [n[2], 0, -n[0]],
                  [-n[1], n[0], 0]])
    
    return np.eye(3) + sin_t * K + (1 - cos_t) * (K @ K)


# ============================================================================
# Experiment PB2: Cartan Core Scan
# ============================================================================

def experiment_pb2_cartan_core_scan(
    p: float = 0.7,
    save_dir: str = "./results"
):
    """
    PB2: Test three different Cartan cores and verify Pointer basis = Cartan axis.
    
    Cores:
    1. Pure XX: c = (pi/4, 0, 0)
    2. Pure ZZ: c = (0, 0, pi/4)
    3. Mixed:   c = pi/6 * (1, 0, 1) / sqrt(2)
    
    For each core, run a simplified PB1 (smaller scan grid) and check if
    min_QCMI axis direction = core's Cartan axis direction.
    
    Output:
        - Comparison bar chart: figures/pointer_basis_pb2_comparison.png
        - Data: data/pointer_basis_pb2.npz
    """
    cores = {
        'Pure XX': np.array([np.pi/4, 0.0, 0.0]),
        'Pure ZZ': np.array([0.0, 0.0, np.pi/4]),
        'Mixed XZ': np.array([np.pi/6, 0.0, np.pi/6]),
    }
    
    print(f"[PB2] Cartan Core Scan: p={p}")
    
    results = {}
    
    for name, c in cores.items():
        print(f"\n  Core: {name}, c = ({c[0]:.4f}, {c[1]:.4f}, {c[2]:.4f})")
        
        # Run a simplified scan (coarser grid for speed)
        D_core = make_cartan_core(c)
        
        # Use Fibonacci sphere points for uniform sampling on S^2
        n_points = 200
        phi_fib = np.pi * (3 - np.sqrt(5))  # Golden angle
        theta_fib = np.zeros(n_points)
        
        qcmi_samples = []
        axis_rotated_list = []
        
        for i in range(n_points):
            # Fibonacci sphere point
            y_fib = 1 - (i / (n_points - 1)) * 2
            radius_at_y = np.sqrt(1 - y_fib**2)
            theta_fib_val = np.arccos(y_fib)
            phi_fib_val = (phi_fib * i) % (2 * np.pi)
            
            axis = np.array([
                np.sin(theta_fib_val) * np.cos(phi_fib_val),
                np.sin(theta_fib_val) * np.sin(phi_fib_val),
                np.cos(theta_fib_val)
            ])
            
            R = su2_matrix(np.pi/2, axis)
            local_rots = [R, R, R, R]
            
            try:
                qcmi = construct_4cycle_qcmi_with_local_rotations(
                    D_core, local_rots, p
                )
            except Exception as e:
                qcmi = np.nan
            
            qcmi_samples.append(qcmi)
            
            # Compute rotated Cartan axis
            R_so3 = _su2_to_so3(R)
            c_eff = R_so3 @ c
            axis_rotated_list.append(c_eff)
        
        qcmi_arr = np.array(qcmi_samples)
        axis_rotated_arr = np.array(axis_rotated_list)
        
        # Find minimum
        min_idx = np.nanargmin(qcmi_arr)
        min_qcmi = qcmi_arr[min_idx]
        min_axis = axis_rotated_arr[min_idx]
        
        # Angle between min_axis and original Cartan axis
        c_unit = c / np.linalg.norm(c)
        min_axis_unit = min_axis / np.linalg.norm(min_axis) if np.linalg.norm(min_axis) > 1e-10 else min_axis
        angle = np.arccos(np.clip(np.abs(np.dot(c_unit, min_axis_unit)), -1, 1))
        
        print(f"    min QCMI = {min_qcmi:.4f}")
        print(f"    min axis = ({min_axis[0]:.3f}, {min_axis[1]:.3f}, {min_axis[2]:.3f})")
        print(f"    angle to Cartan axis = {angle:.4f} rad = {np.degrees(angle):.1f} deg")
        
        results[name] = {
            'min_qcmi': min_qcmi,
            'min_axis': min_axis,
            'angle': angle,
            'cartan_c': c,
        }
    
    # Plot comparison
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    names = list(cores.keys())
    
    # Left: angle between min_QCMI axis and Cartan axis
    angles = [results[n]['angle'] for n in names]
    axes[0].bar(names, np.degrees(angles), color=['red', 'blue', 'purple'])
    axes[0].axhline(0, color='black', linestyle='-', linewidth=0.5)
    axes[0].set_ylabel('Angle (degrees)')
    axes[0].set_title('PB2: Angle between min_QCMI axis and Cartan axis')
    axes[0].set_ylim(0, max(np.degrees(angles)) * 1.5 if max(angles) > 0 else 10)
    
    # Right: min QCMI values
    qcmi_vals = [results[n]['min_qcmi'] for n in names]
    axes[1].bar(names, qcmi_vals, color=['red', 'blue', 'purple'])
    axes[1].set_ylabel('Min QCMI')
    axes[1].set_title('PB2: Min QCMI for each Cartan core')
    
    plt.tight_layout()
    save_path = Path(save_dir)
    save_path.mkdir(parents=True, exist_ok=True)
    fig.savefig(save_path / 'pointer_basis_pb2_comparison.png', dpi=150)
    plt.close(fig)
    
    # Save data
    np.savez(save_path / 'pointer_basis_pb2.npz',
             core_names=np.array(names),
             min_qcmi=np.array([results[n]['min_qcmi'] for n in names]),
             angles=np.array([results[n]['angle'] for n in names]),
             cores={n: results[n]['cartan_c'] for n in names})
    
    # Summary
    print(f"\n[PB2] Complete.")
    for n in names:
        print(f"  {n}: angle = {np.degrees(results[n]['angle']):.1f} deg, "
              f"min QCMI = {results[n]['min_qcmi']:.4f}")
    
    return results


# ============================================================================
# Experiment PB3: Two-Cycle Competition
# ============================================================================

def experiment_pb3_two_cycle_competition(
    c_A: np.ndarray = None,  # XX core
    c_B: np.ndarray = None,  # ZZ core
    ratio_scan: list = None,
    p: float = 0.7,
    n_scan: int = 50,
    save_dir: str = "./results"
):
    """
    PB3: Two causal cycles with different Cartan cores compete for Pointer basis.
    
    Setup: Two 4-cycles sharing Q_a and Q_b nodes.
    - Cycle A: all edges use Cartan core D(c_A) [pure XX]
    - Cycle B: all edges use Cartan core D(c_B) [pure ZZ]
    - Q_a and Q_b have local basis rotations that affect BOTH cycles
    
    Scan the shared local basis rotation and find min_QCMI.
    If the claim holds: min_QCMI direction = weighted average of c_A and c_B.
    
    Also scan the amplitude ratio |c_A| / |c_B| to verify "voting power"
    proportional to Cartan coefficient magnitude.
    
    Output:
        - Pointer basis vs amplitude ratio: figures/pointer_basis_pb3_competition.png
        - Data: data/pointer_basis_pb3.npz
    """
    if c_A is None:
        c_A = np.array([np.pi/4, 0.0, 0.0])  # XX
    if c_B is None:
        c_B = np.array([0.0, 0.0, np.pi/4])  # ZZ
    if ratio_scan is None:
        ratio_scan = [0.2, 0.5, 1.0, 2.0, 5.0]
    
    print(f"[PB3] Two-Cycle Competition: p={p}")
    print(f"  c_A = ({c_A[0]:.3f}, {c_A[1]:.3f}, {c_A[2]:.3f})  [XX]")
    print(f"  c_B = ({c_B[0]:.3f}, {c_B[1]:.3f}, {c_B[2]:.3f})  [ZZ]")
    print(f"  amplitude ratios: {ratio_scan}")
    
    results_by_ratio = {}
    
    for ratio in ratio_scan:
        # Scale c_A to have amplitude ratio relative to c_B
        c_A_scaled = c_A * ratio
        D_A = make_cartan_core(c_A_scaled)
        D_B = make_cartan_core(c_B)
        
        print(f"\n  ratio = {ratio}: c_A_eff = ({c_A_scaled[0]:.3f}, {c_A_scaled[1]:.3f}, {c_A_scaled[2]:.3f})")
        
        # Fibonacci sphere scan for shared local rotation
        n_points = 300
        phi_fib = np.pi * (3 - np.sqrt(5))
        
        qcmi_samples = []
        axis_samples = []
        
        for i in range(n_points):
            y_fib = 1 - (i / (n_points - 1)) * 2
            radius_at_y = np.sqrt(1 - y_fib**2)
            theta_fib_val = np.arccos(y_fib)
            phi_fib_val = (phi_fib * i) % (2 * np.pi)
            
            axis = np.array([
                np.sin(theta_fib_val) * np.cos(phi_fib_val),
                np.sin(theta_fib_val) * np.sin(phi_fib_val),
                np.cos(theta_fib_val)
            ])
            
            R = su2_matrix(np.pi/2, axis)
            local_rots = [R, R, R, R]
            
            # Compute QCMI for two-cycle system
            # This requires a specialized QCMI calculator that handles
            # the 6-node two-cycle topology
            try:
                qcmi = construct_two_cycle_qcmi_with_rotations(
                    D_A, D_B, local_rots, p
                )
            except Exception as e:
                qcmi = np.nan
            
            qcmi_samples.append(qcmi)
            axis_samples.append(axis)
        
        qcmi_arr = np.array(qcmi_samples)
        axis_arr = np.array(axis_samples)
        
        min_idx = np.nanargmin(qcmi_arr)
        min_qcmi = qcmi_arr[min_idx]
        min_axis = axis_arr[min_idx]
        
        # Project min_axis onto the XX-ZZ plane (Y=0 plane)
        min_axis_proj = np.array([min_axis[0], 0.0, min_axis[2]])
        proj_norm = np.linalg.norm(min_axis_proj)
        if proj_norm > 1e-10:
            min_axis_proj = min_axis_proj / proj_norm
        
        # Expected axis = weighted average
        norm_A = np.linalg.norm(c_A_scaled)
        norm_B = np.linalg.norm(c_B)
        total = norm_A + norm_B
        expected_axis = (norm_A * np.array([1., 0., 0.]) + norm_B * np.array([0., 0., 1.])) / total
        
        # Angle between min and expected
        dot = np.clip(np.abs(np.dot(min_axis_proj, expected_axis)), -1, 1)
        angle = np.arccos(dot)
        
        print(f"    min QCMI = {min_qcmi:.4f}")
        print(f"    min axis (proj XZ) = ({min_axis_proj[0]:.3f}, {min_axis_proj[2]:.3f})")
        print(f"    expected axis = ({expected_axis[0]:.3f}, {expected_axis[2]:.3f})")
        print(f"    angle = {np.degrees(angle):.1f} deg")
        
        results_by_ratio[ratio] = {
            'min_qcmi': min_qcmi,
            'min_axis': min_axis,
            'min_axis_proj': min_axis_proj,
            'expected_axis': expected_axis,
            'angle': angle,
        }
    
    # Plot
    fig, ax = plt.subplots(1, 1, figsize=(8, 6))
    
    ratios_arr = np.array(ratio_scan)
    angles_arr = np.array([results_by_ratio[r]['angle'] for r in ratio_scan])
    
    ax.plot(ratios_arr, np.degrees(angles_arr), 'o-', linewidth=2, markersize=8)
    ax.axhline(0, color='black', linestyle='--', alpha=0.3)
    ax.set_xlabel(r'Amplitude ratio $|c_{XX}| / |c_{ZZ}|$')
    ax.set_ylabel('Angle: min QCMI axis vs expected (degrees)')
    ax.set_title('PB3: Two-Cycle Pointer Basis Competition')
    ax.set_xscale('log')
    ax.grid(True, alpha=0.3)
    
    # Add annotations for expected axis direction at each ratio
    for ratio in ratio_scan:
        r = results_by_ratio[ratio]
        ax.annotate(
            f'({r["expected_axis"][0]:.2f}, {r["expected_axis"][2]:.2f})',
            (ratio, np.degrees(r['angle'])),
            textcoords="offset points", xytext=(0, 10),
            fontsize=8, ha='center'
        )
    
    plt.tight_layout()
    save_path = Path(save_dir)
    save_path.mkdir(parents=True, exist_ok=True)
    fig.savefig(save_path / 'pointer_basis_pb3_competition.png', dpi=150)
    plt.close(fig)
    
    # Save data
    np.savez(save_path / 'pointer_basis_pb3.npz',
             ratio_scan=ratios_arr,
             angles=np.degrees(angles_arr))
    
    print(f"\n[PB3] Complete.")
    
    return results_by_ratio


def construct_two_cycle_qcmi_with_rotations(
    D_A: np.ndarray, D_B: np.ndarray,
    local_rots: list, p: float
) -> float:
    """
    Compute QCMI for two-cycle system (shared nodes Q_a, Q_b).
    
    Topology (6 nodes, b1=2 or 3 depending on counting):
        Cycle A: Q_a → E_1 → Q_b → E_2 → Q_a  (edges use D_A)
        Cycle B: Q_a → E_3 → Q_b → E_4 → Q_a  (edges use D_B)
    
    Edges on Q_a and Q_b apply local rotations R_a, R_b.
    
    This is a specialized calculator — 需要实验组实现。
    """
    pass  # 实验组实现


# ============================================================================
# Main
# ============================================================================

def main():
    """Run all pointer basis experiments."""
    
    print("=" * 70)
    print("Pointer Basis Experimental Suite")
    print("B博士 规格 — 实验组执行")
    print("=" * 70)
    
    save_dir = "./results/pointer_basis"
    
    # PB1: Local basis scan
    print("\n" + "=" * 70)
    print("PB1: Local Basis Rotation Scan")
    print("=" * 70)
    results_pb1 = experiment_pb1_local_basis_scan(
        cartan_c=np.array([np.pi/4, 0.0, 0.0]),  # Pure XX
        p=0.7,
        n_theta=20,
        n_axis=50,
        save_dir=save_dir
    )
    
    # PB2: Cartan core scan
    print("\n" + "=" * 70)
    print("PB2: Cartan Core Scan")
    print("=" * 70)
    results_pb2 = experiment_pb2_cartan_core_scan(
        p=0.7, save_dir=save_dir
    )
    
    # PB3: Two-cycle competition
    print("\n" + "=" * 70)
    print("PB3: Two-Cycle Pointer Basis Competition")
    print("=" * 70)
    results_pb3 = experiment_pb3_two_cycle_competition(
        p=0.7, save_dir=save_dir
    )
    
    # Summary
    print("\n" + "=" * 70)
    print("ALL POINTER BASIS EXPERIMENTS COMPLETE")
    print("=" * 70)
    print(f"\nPB1: min_QCMI axis angle to Cartan axis = "
          f"{np.degrees(results_pb1['misalignment_angle']):.1f} deg")
    print(f"     (should be ~0 deg if Pointer basis = Cartan axis)")
    
    print(f"\nPB3: Track whether min_QCMI axis follows the weighted average of c_A and c_B.")
    print(f"     See figures/pointer_basis_pb3_competition.png")
    
    print(f"\nResults saved to: {save_dir}/")
    print("Files:")
    print("  pointer_basis_pb1_sphere.png")
    print("  pointer_basis_pb2_comparison.png")
    print("  pointer_basis_pb3_competition.png")
    print("  pointer_basis_pb*.npz (raw data)")


if __name__ == "__main__":
    main()
```

---

### 3.3 实验组执行说明

**需要额外实现的函数:**
1. `construct_4cycle_qcmi_with_local_rotations(cartan_core_D, local_rots, p, d_env)`: 在局域基旋转下的 4 节点环 QCMI 计算
2. `construct_two_cycle_qcmi_with_rotations(D_A, D_B, local_rots, p)`: 双环系统 (共享 Q_a, Q_b) 的 QCMI 计算 — 这是最复杂的计算
3. `_su2_to_so3(R_su2)`: SU(2) → SO(3) 转换 (已在脚本中提供)

**时间估计:**
- PB1 (~2000 QCMI): ~10-20 分钟
- PB2 (~600 QCMI): ~3-6 分钟
- PB3 (~1500 QCMI): ~8-15 分钟 (双环系统 QCMI 更贵)
- **总计:** ~25-45 分钟

**关键数值指标 (实验组完成后汇报):**

| 指标 | 预期 | 含义 |
|:---|:---|:---|
| PB1 misalignment angle | ≈ 0 deg | min_QCMI 轴 = Cartan 轴 (Pointer basis 声张成立) |
| PB2 angle (Pure XX) | ≈ 0 deg | 对于纯 XX 核心, min_QCMI = XX 轴 |
| PB2 angle (Pure ZZ) | ≈ 0 deg | 对于纯 ZZ 核心, min_QCMI = ZZ 轴 |
| PB3 angle vs expected | ≈ 0 deg (各 ratio) | Pointer basis = 加权平均, 投票权 ∝ 振幅 |

**如果 PB3 显示 min_QCMI 轴随 ratio 连续变化:** 这是 AHA-3 的直接实验验证 — Pointer basis 是因果环干涉网络动态竞争的结果, 而非预先固定的。

---

## 三声张总结

| # | 声张 | 方法论 | 本报告产出 | 状态 |
|:--:|------|------|------|:--:|
| 1 | b₁>1 超可加性 | 跨学科论证 (Mayer-Vietoris + H₁ 能量泛函, 选中) | 论证草图 (§1) + 三个角度评估 | B博士论证完成 |
| 2 | sin²θ 前因子 | 实验设计 | 完整 Python 脚本规格 (§2) — E1/E2/E3/E4 | 待实验组执行 |
| 3 | Pointer basis | 实验设计 | 完整 Python 脚本规格 (§3) — PB1/PB2/PB3 | 待实验组执行 |

**声张1 的最终论证路径:**

> **Mayer-Vietoris + H₁(G;ℝ) 能量泛函路径。** 核心步骤:
> 1. H₁(G) = ⊕ H₁(G_i) (MV 严格分解)
> 2. 树边冻结 → QCMI 仅由非树边 Cartan 系数决定
> 3. QCMI 作为 H₁ 上的正泛函, min_F 受限优化 → 超可加性
> 4. → I_G ≥ Σ I_{G_i} ≥ η(d) · b₁(G)
>
> **残留gap:** 树边冻结引理的严格证明; Buscemi min_F 受限优化的形式化; Q 泛函的良定性。这些都是可以填补的技术gap — 不涉及概念性障碍。

**实验组需要的核心函数 (所有实验共用):**
1. `construct_4cycle_qcmi(U_list, p)`: 标准 4 节点环 QCMI
2. `construct_4cycle_qcmi_with_local_rotations(D, local_rots, p)`: 带局域基旋转的 4 节点环 QCMI
3. `construct_two_cycle_qcmi_with_rotations(D_A, D_B, local_rots, p)`: 双环系统 QCMI
4. `cartan_decompose_u4(U)`: U(4) KAK 分解
5. `haar_random_u4()`: Haar 随机 U(4) 采样

---

*B博士 三声张输出完成。声张1 跨学科论证 (Mayer-Vietoris 路径选中)。声张2 sin²θ 前因子实验规格 (4 子实验, ~7000 QCMI 计算)。声张3 Pointer basis 实验规格 (3 子实验, ~4100 QCMI 计算)。全部待实验组执行。A博士解析框架同步推进中。*

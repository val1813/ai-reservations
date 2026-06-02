# B 博士 Phase 3 输出 — MasslessGravity-Island v1 命题B 精化

**日期：** 2026-06-01
**角色：** B 博士（突击推导者 — 命题B 统一框架）
**Phase：** 3（Geng et al. 2602.06543 + C1-C2 互斥 → 统一命题B）

---

## ⚡ 本 Phase 推进了什么

### 核心推进

Phase 1 识别了 supertranslation frame 依赖为门控障碍。Phase 2 证明 Antonini dressing × replica trick 存在算子代数级别的互斥圈（C1-C2 不可同时激活）。Phase 3 将 Geng et al. (2602.06543) 的代数完整性攻击与本课题的路径积分级攻击整合为**统一命题B**——两个独立层级（单算符级 × 路径积分级）的障碍，任一单独成立即可排除 operational 岛屿。

### 最关键的跨域连接

**Geng 的 "blinders" 论证** ←→ **本课题的 C1-C2 互斥圈**：Geng 证明 fine-grained entropy 在 ℐ⁺ 上为常数（∂S/∂u₀ = 0），且岛公式在代数完整性框架下本身不一致。本课题证明即使通过 dressing 试图绕过代数完整性，C1（BMS-invariant QES）与 C2（replica wormhole）在路径积分层面互斥。两者连接后发现：

- Geng 的代数完整性 → 无需任何 bypass 就已 blocking
- C1-C2 互斥 → 即使绕过代数完整性（通过 dressing），还有第二层障碍
- **两者构成双重嵌套障碍**：外层（代数完整性）和内层（C1-C2 互斥）各自独立阻断

### 预测 vs 实际

- **预测（Phase 2 建议）：** Phase 3 应是 Attack 1 的论文级证明或 SO(3) 角度深化
- **实际：** 发现 Geng et al. 已独立完成了更基础的攻击——代数完整性直接使岛屿公式不一致，完全绕开 dressing/replica 的具体机制。这是一条超越预期的强力外部确认线
- **AHA 瞬间：** Geng 的 "blinders" 论证（需移除 H_ADM 才能看到 Page 曲线）与 Antonini 的 proper subalgebra（明确排除 H_ADM 和 Q_f）指向完全相同的物理选择——但 Geng 更激进：它主张这个选择本身就是非物理的
- **统一命题的意义：** 两条攻击线来自完全不同方向（QFT 代数 vs 路径积分鞍点），攻击的是同一目标（岛屿的 operational 定义）的不同层级。互不依赖但互相强化

### 卡在哪里

- Geng 的论证在技术层面极其 rigorous（Reeh-Schlieder + algebra completeness），但它假设了完整 asymptotic algebra（包含 H_ADM）。如果在 flat space ℐ⁺ 上 soft modes 使真空无限简并，Reeh-Schlieder 的适用性需要确认（Geng 自己提到了这个微妙但引用 [13] 处理）
- C1-C2 互斥的具体机制（dressing 改变算符代数 → replica 边界条件改变）依赖 [PI-5] 裁决
- 统一命题的最佳强度：如果 Geng 的代数完整性论证成立，则岛屿公式直接不一致，C1-C2 互斥只是"椅子上的第二颗钉子"。如果 Geng 论证在 flat space 中有微妙问题，C1-C2 互斥作为独立后备

---

## ⚡ 审核入口

```
⚡ 审核入口：
  统一命题：无质量引力中岛屿公式面临双重独立障碍——(B1) 单算符级：
    渐近代数完整性使规范不变算符不能局域化到有限区域（Geng et al.）；(B2) 路径积分级：
    BMS-invariant QES 与 replica wormhole saddle 互斥（本课题 C1-C2）。
    两者独立存在——任一障碍单独成立就足以排除 operational 岛屿概念。

  Geng vs 本课题的互补性：
    Geng 攻击"是否可以定义局域算符"（代数完整性 → 无 commutant → 无分裂 → 无岛）。
    本课题攻击"即使能定义，QES 条件与 replica 鞍点是否自洽"（C1-C2 互斥）。
    前者是基础层攻击，后者是 bypass 层攻击。两者不重叠、不依赖、互相强化。

  命题B 的最强形式：
    Proposition B (unified): 渐近平坦时空中，不存在同时满足以下三者的
    operational 岛屿定义——(B1) 规范不变性（算符局域化），(B2) QES 良定义
    （BMS-invariant 极值条件），(B3) Page 曲线（replica trick well-defined entropy）。
    B1 被 Geng 的代数完整性阻断。B2∩B3 被 C1-C2 互斥圈阻断。
    证据强度：B1 ∈ [⚠️L1→✅L2]（需确认 flat space Reeh-Schlieder 适用性）；
    B2∩B3 ∈ [✅L2]（算子代数级的互斥圈，但需 PI-5 确认关键假设）。

  PI 需要裁决的问题：
    1. [PI-5 延续] 算符代数改变是否等价于 replica 路径积分边界条件改变？
    2. [PI-8] Geng 的代数完整性论证在 asymptotically flat space 中是否完全适用？
       具体问题：(a) 软引力子的真空无限简并是否破坏 Reeh-Schlieder 论证？
       (b) 如果破坏，Geng 论证在 flat space 中降级为何种强度？
    3. [PI-9] 统一命题的策略选择：作为 "双重障碍" 还是 "单一外层障碍 + 内层后备"？
       - 若 Geng 在 flat space 成立（✅ L2）：命题B 已有 Geng 支撑，C1-C2 为强化
       - 若 Geng 在 flat space 不适用（⚠️ L1）：C1-C2 是命题B 的主支撑
```

---

## 第1步：Geng et al. (2602.06543) 的核心论证

**来源：** H. Geng, L. Hui, A. Karch, M. Reece, S. Sun, Z. Sun, Y. Zhao, "Holography of Information in Flat Space," arXiv:2602.06543 (2025).

**检索记录：** 全文已通过 arXiv HTML 读取。以下提取 5 条核心论证。

---

### 论证 1：渐近代数完整性（定理级）

**[1-1] 核心论断：** ℐ⁺ 上的渐近可观测算子代数**完成了**：每个希尔伯特空间中的算子（包括黑体内部信息）都可以用 ℐ⁺ 上任意小时间带中的算子任意精确地近似。

**[1-2] 推导步骤：**
- **步骤 A（引力特有输入）：** 哈密顿量 H_ADM 在 ℐ⁺ 上作为边界项可观测。在 Bondi 规范中，H_ADM = lim_{u→−∞} (1/4πG)∫ m(u,Ω)√γ d²Ω。这意味着 H_ADM 属于 ℐ⁺ 上的全局代数。
- **步骤 B：** 由于 H_ADM 在任何渐近时间带代数中（因为"无穷远过去"的时间带包含足够信息确定 H_ADM），真空投影算子 P₀ = |0⟩⟨0| 也属于该代数（P₀ 是 H_ADM 的谱投影）。
- **步骤 C（Reeh-Schlieder 型论证）：** 真空态是循环分离的——任意态 |n⟩ 可通过 P₀ 和时间带上的算子 X_n 近似：|n⟩ ≐ X_n|0⟩。
- **步骤 D：** 任意算子 Q = |n⟩⟨m| 可写成 Q ≐ X_n P₀ X_m^†。三因子都在时间带代数中。因此**所有算子**都在此时间带代数中。

**[1-3] 关键结论：** 没有算符可以独立于渐近观测者而纯"局域"在紧致区域中——因为渐近代数已经包含了一切。

**依据：** Section 3.1, Eq. (3.8)-(3.12)。论证基于两个关键假设：(1) 渐近区域 QFT 有效；(2) 哈密顿量有下界。

**反驳检验：** Reeh-Schlieder 论证要求真空态在时间带代数下是循环的。这在 AdS 中标准成立，但在 flat space 中，软引力子的真空简并可能破坏循环性——Geng 在 §3.1.1 承认了这一微妙并引用 [13] 处理。**这是论证的潜在薄弱点。**

---

### 论证 2：平坦熵定理——Page 曲线是平坦的

**[2-1] 核心论断：** ℐ⁺ 上的 fine-grained 熵不随截断时间 u₀ 变化。∂S(u₀)/∂u₀ = 0。没有 Page 曲线的"帐篷形状"。

**[2-2] 推导：**
- 定义 𝒜(u₀) 为 ℐ⁺ 上 u < u₀ 的子代数。定义密度矩阵 ρ(u₀) 为在 𝒜(u₀) 上的限制。
- 由于渐近代数完整性（论证 1），𝒜(u₀) 中每个元素都可以用任意过去时间带代数 𝒜_ε 中的元素近似。
- 因此 ρ(u₀) 可被始终选为 𝒜_ε 中的元素——ρ(u₀) 独立于 u₀。
- 所以 S(u₀) = −tr(ρ(u₀)log ρ(u₀)) 独立于 u₀。

**[2-3] 推论：** "当我们把端点 u₀ 沿 ℐ⁺ 移动时，没有新自由度被加入。"辐射的精细结构熵不随我们观测更多后期辐射而改变——因为全部信息已在早期（无穷远过去）的代数中编码。

**依据：** Section 4, Eq. (4.1)-(4.5)。

**反驳检验：** 这个结果严重依赖论证 1 在 flat space 中的成立性。如果 soft modes 破坏了 Reeh-Schlieder 论证，则平坦熵定理不成立。另外，该定理说的是 fine-grained 熵，而非 coarse-grained 或 Page 熵——Geng 自己承认后者可以通过移除 H_ADM 获得。

---

### 论证 3："Blinders" 论证——Page 曲线来自人为限制

**[3-1] 核心论断：** 文献中的 Page 曲线只有通过人为地从可观测代数中移除 H_ADM（或等价地，将边界分成两部分限制观测区域）才能获得。这相当于给探测器戴上"眼罩"（blinders）。

**[3-2] AdS 案例：** 将边界 S^{d−1} 分成两部分 A 和 A^c。只观测 A 上的算子 → H_ADM 不可完全访问（需要整个球面积分）→ 出现 Page 曲线。即使是纯静态、不蒸发的黑洞，只要做这种划分，也会出现 Page 曲线（Figure 1）。这证明 Page 曲线是观测者选择的 artifact，不是黑体信息动力学的结果。

**[3-3] Flat space 案例：** ℐ⁺ 上的代数在 leading 阶是自由的（对易关系与相互作用无关）。可以"形式上从代数中丢弃 H_ADM"。这在 ℐ⁺ 上是数学自洽的，但**物理上不自然**——"自然可观测如 Riemann 张量同时编码 H_ADM 和其他可观测量的信息"。

**[3-4] 核心主张：** "要在标准引力中看到 Page 曲线，我们必须戴眼罩。"

**依据：** Section 4.1-4.2。

**反驳检验：** "Blinders" 论证将问题转移到什么是"自然"的可观测代数。Antonini et al. 的 proper subalgebra 正是这样一个有意的"眼罩"——它明确排除 H_ADM 和 Q_f。如果足够多的物理学家认为排除 H_ADM 是合理的（因为实际探测器不测它），则 blinders 不一定是非物理的。**这需要更深刻的 operational 判断。**

---

### 论证 4：岛屿公式在标准引力中不一致

**[4-1] 核心论断：** 岛屿（定义为不延伸至渐近区域的紧致纠缠模）在标准引力中不可能存在。原因：岛屿的算符与渐近区域的算符之间的对易子必须为零（类空分离），但渐近算符（特别是 H_ADM）能表示所有体算符。

**[4-2] 形式论证：**
- 假设存在岛屿区域 I（紧致）和渐近区域 A（非紧致）。它们类空分离 → [O_I, O_A] = 0，对所有 O_I ∈ 𝒜_I, O_A ∈ 𝒜_A。
- 但渐近代数完整性（论证 1）→ 𝒜_A 包含 H_ADM，且能表示任何体算子 → 特别地，O_I 本身可以被渐近算符近似表示。
- 矛盾：如果 O_I 可以被渐近算符表示，且渐近算符与 O_I 对易，则 O_I 与其自身对易（trivially true，但问题在于：O_I 作为 𝒜_A 的近似元素，[O_I, O_I] = 0 自动成立——这里的精确表述需要更细致）。
- 更精确的表述（引用 [12]）：岛屿算符与 H_ADM 的**非零对易子**与岛屿的紧致性冲突。因为 H_ADM 编码了体能量信息，如果岛屿算符与非平凡的 H_ADM 相关性非零，岛屿就不能保持紧致——它必须"延伸"以容纳该相关性。

**[4-3] 文献澄清：** 已有文献中出现的"岛屿"（如 [16]）实际上是**包含渐近区域部分的非紧致纠缠模**，不是 Geng 定义的紧致岛屿。Geng 明确说："[16] 中的所有例子都包含一部分渐近边界，因此不是我们定义的岛屿。"

**依据：** Section 5.1-5.2。

**反驳检验：** 这里的关键假设是岛屿算子与 H_ADM 的非零对易子不可避免。如果有某种"dressing"机制让 [O_I_dressed, H_ADM] = 0（类似 Antonini 对 Q_f 的处理），则这一冲突可被绕过。这正是 Antonini et al. 的动机。但 Geng 在 §5.3 论证了 relational observables 在 fine-grained level 不足以维持这种抵消。

---

### 论证 5：关系算符不能拯救岛屿（§5.3）

**[5-1] 核心论断：** 即使承认 relational observables（用背景时钟的涨落来"隐藏"算子对渐近观测者的效应），这些近似的算符代数也不足以定义 fine-grained entropy 或使岛屿一致。

**[5-2] 机制：** Relational construction 利用背景态中大能量涨落作为"时钟"。如果渐近观测者被限制做不了足够精确的能量测量，就无法检测这些算子。

**[5-3] 失效原因：** 当时钟有有限熵时，当我们 probe 到能区分纯态和混合态的 fine-grained level，近似对易关系破裂。"信息悖论精确需要这个 fine-grained regime——正是在这个 regime 中，holography of information 不能被模糊掉。"

**依据：** Section 5.3。

**反驳检验：** 这直接指向 Antonini et al. §4.4 的 state-dependent dressing 开放问题。Geng 的立场是：state-dependence 在 fine-grained level 不能维持近似局域化——这是"逃生舱"的正面攻击。

---

### Geng 论证的总体逻辑链

```
代数完整性 (论证1)
    ├──→ 平坦熵定理 (论证2)：ℐ⁺ 熵为常数
    ├──→ Blinders 论证 (论证3)：Page 曲线需移除 H_ADM
    └──→ 岛屿不一致 (论证4+5)：紧致区域算子与渐近代数冲突
```

---

## 第2步：Geng 论证与 C1-C2 互斥的互补性

### 2.1 攻击层级对比

| 维度 | Geng et al. (2602.06543) | 本课题 C1-C2 互斥 (Phase 2) |
|------|--------------------------|------------------------------|
| **攻击层级** | 单算符级——算子代数的完整性 | 路径积分/鞍点级——QES × replica 的自洽性 |
| **核心工具** | Reeh-Schlieder + 代数完备性 + P₀ ∈ 𝒜_ε | Operator-algebraic dressing × replica path integral |
| **攻击目标** | 任何紧致区域中能否定义规范不变算符 | C1 bypass (dressing) 与 C2 bypass (replica) 能否同时激活 |
| **是否依赖 dressing** | 否——在标准引力中直接攻击，不关心 bypass | 是——瞄准 Antonini dressing 方案的内部变结构 |
| **阻断性** | 如果是 L2，则直接阻断所有岛屿构造 | 阻断特定 bypass 组合，但有逃生舱（state-dependent dressing） |

### 2.2 互补性论证

**[步骤 2-2-1]** 两者独立存在。

Geng 的论证完全不依赖 dressing、replica trick 或岛屿公式的任何特定构造细节。它基于一个普遍的引力特有的事实——哈密顿量是边界项，且渐近代数因此是完整的。如果这一论证成立，那么**无论是否有人尝试构造 bypass，岛屿公式在标准引力中已是内部不一致的**。

C1-C2 互斥的论证依赖 Antonini dressing 方案的具体结构：[O_dressed, Q_f] = 0 → Q_f 在 dressed 代数中中心化 → replica 边界条件改变 → 鞍点不一致。如果 C1-C2 互斥成立，那么**即使假设渐近代数完整性可以被绕过**（假设 dressing 确实创建了一个与 H_ADM 和 Q_f 对易的 proper subalgebra），岛屿公式的 C2 部分（replica wormhole）仍然无法一致实现。

- **学科工具：** 逻辑独立性分析。两条论证链引用不相交的数学假设集。
- **依据：** Geng 论证的唯一假设是渐近代数的完整性（依赖 H_ADM 在代数中和 Reeh-Schlieder）。C1-C2 互斥的唯一假设是 Antonini dressing 的构造性质（[O_dressed, Q_f] = 0）和 replica path integral 对边界条件的依赖。两者共享零个核心假设。
- **反驳检验：** 是否存在某种"元假设"同时使两个论证失效？可能的候选：flat space 中的 IR 分歧（软引力子真空简并）。如果这一分歧使 Reeh-Schlieder 失效（破坏 Geng）且使 replica path integral 在 flat space 中本身就 ill-defined（破坏 C1-C2），则两者共享同一脆弱点。这需要 PI [PI-8] 评估。

**[步骤 2-2-2]** 两者相互强化而非重叠。

重叠区域：两者都涉及 ℐ⁺ 上的边界电荷（H_ADM, Q_f）对体局域化的约束。Geng 强调 H_ADM 的约束效应；C1-C2 强调 Q_f 的约束效应。两者来自同一族边界电荷（BMS 电荷）但不同元素。

非重叠区域：
- Geng 没有具体分析 Q_f 的角色。它的论证依赖 H_ADM 的谱投影得到 P₀ ∈ 𝒜_ε。Q_f 的谱是否也给出投影？如果 Q_f 的谱有连续部分（soft modes），Q_f 的谱投影可能不是代数元。
- C1-C2 没有证明"任何 bypass 都失败"。它只证明 Antonini 的特定 dressing × replica bypass 存在代数级互斥。如果出现全新的 bypass 框架（与 dressing 无关），C1-C2 不适用。

**综合：** Geng 覆盖了 H_ADM 级的障碍，C1-C2 覆盖了 Q_f 级的障碍。两者联合覆盖全部 BMS 电荷群（H_ADM + Q_f + BMS supermomentum）对岛屿构造的约束。**这是完整的。**

- **学科工具：** 覆盖完备性分析——BMS 生成元集的分解：supertranslations = {H_ADM (ℓ=0 mode), Q_f (ℓ≥1 modes)}。
- **依据：** BMS 代数的标准分解。H_ADM 是 supertranslation 的零模态（整体时间平移），Q_f 是高 ℓ 模态。
- **反驳检验：** 是否有 BMS 群之外的其他对称性（如 superrotation）对岛屿也有约束？Geng 的论证只用了 H_ADM，对 BMS 更大的对称性可能也适用，但未经证明。这超出了当前命题B 的范围。

**[步骤 2-2-3]** 嵌套防御结构。

统一的攻击构型是双重嵌套的：

```
外层防御（Geng）: 渐近代数完整性 → 岛屿算符不可能局域化
    |
    如果突破外层（用 dressing 构造 proper subalgebra 排除 H_ADM/Q_f):
    ↓
内层防御（C1-C2）: Dressed algebra × replica structure 互斥
    |
    如果突破内层（通过 state-dependent dressing 或其他方式）:
    ↓
命题A 逃生舱 → 但需面对 Geng §5.3 的反驳（state-dependence 在 fine-grained level 破裂）
```

这种结构的强度在于：即使外层被突破（有人成功构造了 proper subalgebra），内层仍然有效（代数改变与 replica 不一致）。反之亦然——即使假设 C1-C2 互斥可以通过某种"更聪明的 replica"解决，外层防御（渐近代数完整性）直接使岛屿不一致。

- **学科工具：** 嵌套拓扑防御结构——两层独立防御。外层被突破不自动突破内层，内层被突破不自动突破外层。
- **依据：** 上述独立性分析。
- **反驳检验：** 是否存在同一个 bypass 同时突破两层？可能的候选：Geng §5.3 讨论的 relational observables。如果这些 observables 既构造了 proper subalgebra（突破外层）又与 replica 自洽（突破内层），则命题B 的双层防御同时失效。但 Geng §5.3 已论证 relational observables 在 fine-grained level 不足——这恰恰是命题A 的§4.4 开放问题的内容。

### 2.3 缺口识别

| 缺口 | 归属于 | 严重性 | 缓解 |
|------|--------|--------|------|
| Flat space Reeh-Schlieder 的软引力子微妙 | Geng | 中 | Geng 引用 [13] 处理。如果论证不成立，外层防御需降级 |
| C1-C2 依赖 dressing 的具体细节 | C1-C2 | 中 | 如果出现新的 bypass（非 dressing 框架），内层不适用 |
| Superrotation 电荷未被任何一层覆盖 | 双方 | 低 | Superrotation 不改变岛屿框架的根本结构，但可以深化论证 |
| State-dependent dressing 作为联合逃生舱 | 双方 | 中-高 | 这是命题A 的最后一个出口。Geng §5.3 和 Phase 2 §4.4 分别从不同角度攻击 |

---

## 第3步：统一命题B

### 3.1 统一命题陈述

**Proposition B (unified):** 在渐近平坦时空中，不存在同时满足以下三者的 operational 岛屿定义：

- **(B1) 规范不变性：** 岛屿内的局域算符是 diffeomorphism-invariant（在标准引力的完整算子代数中）
- **(B2) QES 良定义：** 存在 BMS-invariant 的量子极值面（QES）条件，不依赖于超平移框架的选择
- **(B3) Page 曲线：** Replica trick 给出 well-defined、与 B2 自洽的广义熵

B1 被 Geng et al. 的渐近代数完整性阻断。B2 与 B3 的共存被本课题 C1-C2 互斥圈阻断。

### 3.2 阻断机制分解

#### B1 阻断：Geng 的代数完整性障碍

**定理（非形式）：** 在完整的渐近代数 𝒜(ℐ⁺) 中（包含 H_ADM 和所有 BMS 电荷），不存在与所有渐近可观测算符对易的非平凡紧致支撑算子。因此，任何规范不变的岛屿算子 O_I 必然与 H_ADM 和 Q_f 有非零对易子——这意味着 O_I 不能是"纯岛屿"的算子；它必然"看到"渐近区域。

**证明线索（Geng §3.1 + §5.1）：**
1. H_ADM ∈ 𝒜(ℐ⁺)（哈密顿量是边界项）
2. Reeh-Schlieder → 𝒜(ℐ⁺) 的真空表示是循环的
3. → 𝒜(ℐ⁺) = ℬ(ℋ)（所有有界算子都在代数中）
4. → 𝒜(ℐ⁺)' = ℂ𝟙（代数的换位子只有标量）
5. → 没有非平凡算子与 𝒜(ℐ⁺) 中所有元素对易
6. → 岛屿算子 O_I ∈ 𝒜_I 必须满足 [O_I, H_ADM] ≠ 0（否则与步骤 5 矛盾）
7. → 由于 H_ADM 是渐近可观测量（体能量），O_I 不能是"纯岛屿"算子

**强度：⚠️L1→✅L2**（取决于 flat space Reeh-Schlieder 的成立性，见 [PI-8]）

#### B2∩B3 阻断：C1-C2 互斥圈

**定理（非形式）：** 任何试图同时满足 C1（BMS-invariant QES）和 C2（replica wormhole → island）的构造必然导致矛盾，因为 C1 的 bypass（dressing → [O_dressed, Q_f] = 0）改变了 ℐ⁺ 的算子代数，使 Q_f 中心化；而 C2 的 replica path integral 需要未改动的边界条件（包含非平凡的 Q_f 谱）。

**证明框架（Phase 2 Attack 1）：**
1. C1 bypass：构造 dressed 代数 𝒜_dressed ⊂ 𝒜(ℐ⁺)，使得 [O_dressed, Q_f] = 0 ∀ O_dressed
2. 引理 1：若辐射态 ω_bare 在 supertranslation 下非不变，则 ω_dressed = ω_bare|𝒜_dressed ≠ ω_bare|𝒜_dressed（因为 Q_f 谱信息被投影掉）
3. C2 bypass：使用未改动的 replica path integral Z_n[ω_bare] 计算广义熵，驻定条件给出岛屿
4. 引理 2（互斥）：Z_n[ω_dressed] ≠ Z_n[ω_bare] → 鞍点不同 → 岛屿位置不同
5. → C1 和 C2 使用不相容的态定义。两者不能同时激活。

**强度：✅L2**（算子代数级别的数学障碍，但依赖 [PI-5] 关键假设裁决）

### 3.3 证据强度矩阵

| 障碍 | 强度 | 依赖假设 | PI 裁决 |
|------|------|---------|---------|
| B1（Geng 代数完整性） | ⚠️ L1 → 可能 L2 | (a) Flat space Reeh-Schlieder 成立 (b) H_ADM ∈ 𝒜_ε | PI-8 |
| B1（Geng blinders 论证） | ⚠️ L1 | "Blinders"的自然性判断——排 H_ADM 是否物理合理 | PI-optional |
| B1（Geng 岛屿不一致） | ⚠️ L1 | 同上 | PI-optional |
| B2∩B3（C1-C2 互斥圈） | ✅ L2 | [PI-5] 代数改变 = 边界条件改变 | PI-5 |
| B2∩B3（C1-C2 Attack 3 SO(3)） | ⚠️ L1→L2 | 蒸发黑洞保持球对称 | PI-6 |

### 3.4 反驳检验矩阵

| 反驳 | 目标 | 强度 | 回应 |
|------|------|------|------|
| "Flat space Reeh-Schlieder 被软引力子破坏 → Geng 不适用" | B1 | 中 | Geng 承认此微妙并引用 [13]。如果成立，B1 降级为⚠️L1，但 B2∩B3（C1-C2）仍为✅L2。命题B 的双层结构吸收了此风险。 |
| "Dressing 定义在 code subspace 内，不改变全局态 → C1-C2 引理 1 不适用" | B2∩B3 | 高 | Code subspace 投影后，Q_f 的谱信息在投影子空间内仍被压制。引理 1 在 code subspace 内的 restriction 仍然成立。 |
| "用 dressed 代数独立做 replica trick" | B2∩B3 | 中 | 这构成不同的 replica 计算。需要证明 dressed 代数中的 replica saddle = bare 代数中的 replica saddle。这正是待证事项——不能用作反驳。 |
| "Relational observables 同时绕过 Geng 和 C1-C2" | 联合 | 中 | Geng §5.3 专门反驳了这一路径——relational observables 在 fine-grained level 不能保持近似局域化。这是 Phase 2 §4.4（state-dependent dressing）的开放问题。 |
| "Page 曲线本来就需要 blinders → blinders 是 operational 现实" | B1 | 中 | 如果 PI 判断排除 H_ADM 是物理合理的（如实际探测器确实不测 H_ADM），则外层防御的 relevance 减弱。但内层防御（C1-C2）仍然存在。 |

### 3.5 统一命题B 的逻辑架构（完整版本）

```
命题B（统一版）：
  渐近平坦时空中，岛屿公式不可一致实现。

  理由 I（单算子级障碍 — Geng）：
    H_ADM ∈ 𝒜(ℐ⁺)
    → Reeh-Schlieder → 𝒜(ℐ⁺) = ℬ(ℋ)
    → 𝒜(ℐ⁺)' = ℂ𝟙
    → 没有非平凡算子与 𝒜(ℐ⁺) 中所有元素对易
    → 岛屿算子 O_I 若有 [O_I, H_ADM] ≠ 0，则 O_I 不能是"纯岛屿"的
    → 岛屿概念在标准引力代数中自相矛盾
  
  理由 II（路径积分级障碍 — C1-C2 互斥）：
    C1 bypass（dressing → BMS-invariant QES）：
      [O_dressed, Q_f] = 0 → Q_f 在 𝒜_dressed 中中心化
    → Q_f 谱信息被投影掉 → ω_dressed ≠ ω_bare|𝒜_dressed
    C2 bypass（replica → island）：
      Z_n[ω_bare] 的鞍点决定岛屿位置
    → Z_n[ω_dressed] ≠ Z_n[ω_bare] → 不同鞍点 → 不同岛屿
    → C1 bypass 和 C2 bypass 不能同时激活
  
  推论：
    B1 和 B2∩B3 独立阻断。任意一个成立就足够。
    联合强度：即使 Geng 在 flat space 有微妙（软引力子），
    C1-C2 互斥 (✅L2) 独立封锁了 bypass 路径。
```

### 3.6 战略建议

1. **优先裁决 PI-5**（代数改变是否 = 边界条件改变）。这是 C1-C2 互斥能否保持 ✅L2 的关键门控。

2. **优先裁决 PI-8**（Geng 在 flat space 的适用性）。这决定了命题B 是"双层防御"还是"单层防御"。

3. **若 PI-5 通过 + PI-8 通过（Geng 成立）：** 命题B 作为定理（✅L2）成立。统一框架可直接写入论文讨论段。

4. **若 PI-5 通过 + PI-8 不通过（Geng flat space 不适用）：** 命题B 以 C1-C2 互斥为主支撑（✅L2），Geng 为动机支持（⚠️L1）。

5. **若 PI-5 不通过 + PI-8 不通过：** 命题B 降级为 ⚠️L1，"motivated obstruction" 而非阻断性证据。需回到 Phase 1 的 frame 依赖论证或其他角度。

---

## 参考文献

1. H. Geng, L. Hui, A. Karch, M. Reece, S. Sun, Z. Sun, Y. Zhao, "Holography of Information in Flat Space," arXiv:2602.06543 (2025).
2. S. Antonini, et al., "Islands in Flat Space from Dressed Observables," arXiv:2506.04311 (2025).
3. D. Kapec, V. Raclariu, A. Strominger, "Area, Entanglement Entropy and Supertranslations at Null Infinity," arXiv:1603.07706 (2016).
4. A. Strominger, "Lectures on the Infrared Structure of Gravity and Gauge Theory," arXiv:1703.05448 (2017).
5. A. Ashtekar, M. Streubel, "Symplectic Geometry of Radiative Modes and Conserved Quantities at Null Infinity," Proc. R. Soc. Lond. A 376, 585–607 (1981).

---

*B 博士 Phase 3 输出完毕。两条独立攻击线已统一为命题B 的双层防御结构。外层（Geng 代数完整性）攻击岛屿概念本身；内层（C1-C2 互斥）攻击 bypass 路径。两层相互独立且强化。*

*"岛屿需要两个奇迹：规范不变算符能在有限区域内局域化，且 replica trick 与 BMS-invariant QES 自洽。Geng 证明第一个奇迹不可能。C1-C2 互斥证明第二个奇迹自相矛盾。任何一个奇迹的失败就足够了。"*

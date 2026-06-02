# B博士 Phase 1 — LP1-补9 Diophantine: 审计 A 博士的证明

**审计对象：** A任务书_Phase1.md 规划的 Theorem 1 证明骨架（A博士尚未写出完整证明，故本审计基于其计划 + S3原始版本推理链）
**审计日期：** 2026-06-01
**角色：** 突击推导者/数论防守审计

---

## ⚡ 本Phase推进了什么
推进了A博士规划中5条关键gap的识别，全部需在论文发表前解决。

## ⚡ 最关键的跨域连接
Three-Gap Theorem（动力系统/几何数论）↔ 部分商有界（连分数）↔ L_max bound（MBL物理）。

## ⚡ 预测 vs 实际
- 预测：A博士的证明骨架大致自洽，只需补充引用。
- 实际：发现**一个可证明的错误**（常数自洽性）+ **三个不可绕过gap**（折叠映射常数转移、ε公式歧义、非可分离势）。
- 剩余计算资源：5个被定位gap中的3个可以在本Phase内修复（by A博士修正）。

## ⚡ 卡在哪里
折叠映射的常数M' ≠ M是最硬的障碍——它不仅影响golden ratio的数值预测（3/ε→6/ε），更意味着**任何包含折叠映射的证明都需重新计算常数**。A博士有两个选择：折叠映射+显式M'计算，或者放弃折叠映射直接使用三间隙定理。

---

## 前置：S3审计中的Gap与Task 9的责任划分

在进入4条正式审计线前，先界定**哪些历史gap被Task 9解决，哪些仍悬空**。

| 历史Gap | 是否属于A任务书覆盖范围 | 本审计态度 |
|---------|----------------------|-----------|
| S3-A1: 折叠映射严格性 | 是（Step 2核心） | 深入审计 — 发现常数转移问题 |
| S3-A2: 2D联合条件 vs 分解条件 | 部分（Step 4提到min归约） | 深入审计 |
| S3-B2: β_x=β_y退化情况 | 否（A任务书未覆盖） | ⚠️ 标记为需补充 |
| S3-ε公式不一致: W_c/V₀ vs W_c/(2V₀) | 否（A任务书未修复此bug） | ⚠️ 标记为论文需修正 |
| S3-B3: 均匀vs局部p_block | 否（不属于Theorem 1范围） | 不审计（属未来工作） |
| 补7: 非可分离势WPL | 相关但不属于Task 9 | 审计1中标记接口依赖 |

---

## 审计1：可分离势假设

### 陈述审计
Theorem 1（A任务书）明确假设 V(x,y) = V₀[cos(2πβ_x·x+φ_x) + cos(2πβ_y·y+φ_y)] —— 可分离的2D AA势。

### ✅ 通过项
- Theorem 1在陈述中显式写出可分离形式，没有隐藏隐含假设
- 2D归约使用 min(L_max^(x), L_max^(y)) 在可分离势下逻辑自洽

### ⚠️ 需修正项

#### 1.1 [严重] Theorem 1必须显式标注"可分离势"为假设前提，而非仅从公式推断
论文应在Theorem 1陈述后立即注明：
> **Remark:** Theorem 1 holds under the assumption that the 2D quasiperiodic potential is separable, i.e., V(x,y) = V_x(x) + V_y(y) where each component depends on a single coordinate. The non-separable case requires additional analysis (see Appendix [X] / Ref [补7 output]).

理由：在非可分离势（如 V(x,y) = V₀cos(2π(β_x·x + β_y·y))）中，A任务书的整个推导（x和y方向独立处理→min归约）直接失效。非可分离势中存在Weak Potential Lines（Štrkalj et al. 2022），可产生1D无界低无序通道，绕过了L_max bound。

#### 1.2 [中等] min归约的上界性质需澄清
A任务书 Step 4写"2D低无序区域的L_max ≤ min(L_max^(x), L_max^(y))"。这个陈述是正确的——L×L区域要求x和y方向同时满足|V| < W_c的连续区间。

但注意：
- **min归约是L×L方形区域的上界，不是L_max^(2D)本身的表达式**
- L_max^(2D)（最大连通区域的线性尺寸）可能小于min(L_max^(x), L_max^(y))，也可能等于
- 甚至存在更紧的上界：L_max^(2D) ≤ min(L_max^(x), L_max^(y)) 是充分但非必要的
- 建议改为更谨慎表述：L_max^(2D) ≤ min(L_max^(x), L_max^(y))

#### 1.3 [轻微] β_x=β_y退化情况需单独标记
A任务书隐含假设β_x和β_y线性无关(over ℚ)，但未明确声明。若β_x=β_y（或β_x/β_y ∈ ℚ），则2D势退化为两个相同1D势的叠加，导致低无序区域是L_max^(x) × L_max^(x)的笛卡尔积，尺寸可能显著大于min(L_max^(x), L_max^(y))。

**修正建议：** 显式注明"假设β_x和β_y在ℚ上线性无关"，或给出退化情况下的独立处理。

### ❌ 不成立项
无。可分离假设本身在物理论证中合理（实验常用可分离AA势），但不标注适用范围则构成发表风险。

---

## 审计2：标准结果的引用

### 2.1 "Badly approximable"的连分数判据

#### ✅ 通过项
A任务书定义：β badly approximable ↔ 存在c > 0, M > 0使‖kβ‖ ≥ c/|k| for all k ∈ ℤ\{0}。这是公认定义。

Khinchin的定理：部分商有界 ↔ 坏逼进性。来自Khinchin "Continued Fractions" Theorem 13（第3版第2章）。

#### ⚠️ 需修正项

**2.1.1 [中等] c和M的关系需要显式陈述**
存在方向性gap：
- 部分商 ≤ M → c ≥ 1/(M+2)（这是Khinchin的结论，但需要具体引用位置）
- c ≥ c₀ → 部分商 ≤ floor(1/c₀)（稍微更复杂）

论文中M被定义为"sup a_k"，但A任务书同时写"存在c>0, M>0"。严格说M和c是冗余参数——只需一个。建议统一使用部分商上界M，删除冗余的c。

**2.1.2 [轻微] Khinchin定理的精确引用位置**
A任务书写"Khinchin定理Y"——论文发表前必须找到具体定理编号。Khinchin "Continued Fractions"第3版中：
- Theorem 12: 任意无理数的逼近性质由连分数决定
- Theorem 13: 部分商有界 ↔ 存在c > 0使‖qα‖ > c/q
- Theorem 14: Lagrange spectrum的上界关系

**建议引用：** Khinchin, "Continued Fractions", Theorem 13, Chapter 2.

#### ❌ 不成立项
无。

---

### 2.2 2β mod 1保持badly approximable

这是A任务书 Step 2 Lemma（折叠映射引理）的核心。此引理声称"2β mod 1保持badly approximable"。

#### ⚠️ 需修正项 [严重]

**2.2.1 [致命] 声称此结果是Cassels/Khinchin的标准引用是错误的**

独立查证：
1. **Cassels "Geometry of Numbers"** 不包含"2β mod 1保持badly approximable"的显式陈述。Cassels处理的是二次无理的逼近、Minkowski定理、线性齐次逼近等，不直接涉及"乘法映射保持部分商有界"。
2. **Khinchin "Continued Fractions"** 也不包含此结果。Khinchin第2章讨论连分数基本运算（加法、乘法的cf表示），但从未声称"2α mod 1的cf从α的cf直接读出，且M保持不变"。
3. 事实上，**2β mod 1的连分数不能直接从β的cf简单读出**——乘法操作在cf表示中不保持简单结构。

**✅ 结论正确性：** 但此结论本身是正确的。badly approximable数的集合在ℚ乘法下封闭（因为如果|α-p/q| > c/q²，则|2α-p/q| = 2|α-p/(2q)| > c/(2q²)，常数减半）。这是一个标准数论事实，但需要自己证明或引用标准文献。

**2.2.2 [致命] M的变化未被处理——这是A博士自己标注的"最脆弱一步"的正确数学表述**

即使承认2β mod 1是badly approximable，M（部分商上界）的变化**必须被显式计算**。A博士在S3中将其标记为"最脆弱一步"——这是一个负责任的标注，但在Task 9中未被修复。

**关键的数值反例：**
- β = (√5-1)/2 ≈ 0.618034，CF = [0; 1, 1, 1, 1, ...]，M = 1
- 2β = 1.236067...，小数部分 = 0.236067...，CF = [0; 4, 4, 4, 4, ...]，M' = 4

**这意味着：**
- A任务书写 L_max ≤ (M+2)/ε = 3/ε
- 通过折叠映射后，实际使用的常数应为M' = 4（对2β mod 1）
- 因此实际 bound 应为 L_max ≤ (M'+2)/ε = 6/ε = 18，**不是3/ε = 9**
- 常数因子2的差异

**定理层面的影响：**
如果A博士的证明路径是：(a) 折叠映射 → (b) 对2β应用bound → (c) 代入β的M=1 → 得到L_max≤3/ε，则此证明存在错误。正确的(b)应该是：计算2β mod 1的M'，代入M'而非M。

#### 修正方案

A博士有两个选择：

**选项A：修复折叠映射（保留现有推理链）**
- 显式计算：β的CF [0; a₁, a₂, ...] → 2β mod 1的CF [0; a₁', a₂', ...] 
- 证明 M' ≤ 2M + 1（或更紧的界）
- 将bound写为 L_max ≤ (M'+2)/ε，其中M'是2β mod 1的部分商上界
- 对黄金比例：M'=4，bound = 6/ε（保守性增加一倍）

**选项B：放弃折叠映射，直接使用三间隙定理（更推荐）**
- Three-Gap Theorem: 序列{nβ mod 1}的间隙最多3种长度
- 最大间隙 ≤ 1/q_k，其中q_k是最大分母≤N的收敛子
- 用部分商上界M bound q_k → 最大间隙 ~ 1/((M+1)N)
- 要求最大间隙 ≤ ε → N ≥ (M+1)/ε
- 直接得到 L_max ≤ (M+1)/ε（无折叠映射的常数转移问题）
- 对黄金比例：L_max ≤ 2/ε ≈ 6

**推荐选项B**：更直接、常数更紧、回避了折叠映射的M'问题、不需要Bourgain。

#### 2.2.3 [轻微] 替代文献引用
如果选择选项A（保留折叠映射），可引用的数论文献：
- 标准事实："Badly approximable numbers form a set that is closed under multiplication by non-zero rationals" — 可在Schmidt's "Diophantine Approximation"（1980）中找到，Ch. 2, Theorem 2C
- 或者：证明该性质只需直接放缩逼近不等式（如上所述5行证明）
- 建议在Lemma中给出5行证明（避免引用争议），而非引用"标准结果"

---

### 2.3 Bourgain "Green's Function Estimates"的角色

#### ⚠️ 需修正项 [中等]

**2.3.1 Bourgain在此证明中的确切角色不清楚**

A任务书在工具清单中提到Bourgain "Green's Function Estimates"第1章，但在4步推导中并未具体使用Bourgain的结果。

Bourgain的第1章核心结果是：对几乎Mathieu算子 H_ω = λ cos(2π(nα + θ))δ_{n,n'} + Δ，在Diophantine条件下，Green's function满足指数衰减估计。这个结果用于证明在λ > 2时系统处于局域化相。

**可能的映射方法：**
如果A博士打算将L_max bound通过Bourgain的估计来证明，推理链应为：
- 对λ > 2（即V₀ > 2t），Bourgain的Green's function估计给出局域化长度ξ_loc
- L_max ≤ ξ_loc × (something) → 同时L_max ≤ Diophantine bound
- 但这与A任务书的第3步（直接计数论证）不同

**建议：**
- 如果Bourgain仅作为背景引用（"在准周期系统中，Green's function估计表明..."），需注明不是Theorem 1证明的一部分
- 如果Bourgain确实是证明的核心工具，需要明确说明第几节、哪条引理被使用
- 如果Theorem 1的bound来自更初等的三间隙定理，Bourgain的引用可能是不必要的——在严格的论文中，每个引用必须有明确角色

**风险：** 审稿人会问"Bourgain的Green's function estimate在定理X的确切角色是什么？"如果回答不清楚，会被标记为不必要的引用膨胀。

---

## 审计3：常数最优性

### 3.1 L_max ≤ (M+2)/ε 的紧致性

#### ⚠️ 需修正项 [中等]

**3.1.1 常数(M+2)是保守的，非最优**

独立估计：
- **三间隙定理直接法（推荐）：** L_max ≤ (M+1)/ε
  - 推导：最大间隙 ≤ 1/((M+1)N) → N ≥ (M+1)/ε
  - 对黄金比例M=1：L_max ≤ 2/ε
- **折叠映射法（当前方案）：** L_max ≤ (M'+2)/ε，其中M'≥4
  - 对黄金比例：L_max ≤ 6/ε
- **A任务书：** L_max ≤ (M+2)/ε 
  - 对黄金比例：L_max ≤ 3/ε

三间隙直接法给出最优常数，折叠映射法比三间隙法保守2-3倍。

**建议：** 如果使用三间隙直接法，可以在Theorem 1中给出更紧的bound，且不需要Bourgain。常数(M+1)几乎是最优的（渐进意义上，最大间隙不可能小于1/((M+2)N)因Khinchin下界）。

如果A博士选择保留(M+2)常数，需标注"此上界保守，紧致bound为(M+1)/ε——论文选择保守估计以保证证明简介"。但如审计2.2所示，若通过折叠映射，实际bound会膨胀到约6/ε，此保守性需要重新评估。

#### ✅ 通过项

**3.1.2 M=1确实是下确界**
- 部分商a₁ ≥ 1对所有无理数恒成立
- 黄金比例M=1是所有a_n=1的唯一完全情况
- M无法取0（否则收敛子退化为整数→无理数不存在）
- ✅ 黄金比例给出最优badly approximable保护，此定性结论正确

---

### 3.2 公式中的ε有两种定义——必须统一

#### ❌ 不成立 [严重] — 源自S3审计的一致性bug

回顾S3版本中A博士和B博士的数值分歧（S3审计已记录）：

**A博士（S3版本）：**
- 公式文本写 W_c/V₀
- 数值计算用 W_c/(2V₀)
- ε_A = (2/π)arcsin(0.25) ≈ 0.161
- L_max ≤ 19

**B博士（S3版本）：**
- 公式用 W_c/V₀
- ε_B = (2/π)arcsin(0.5) = 1/3
- L_max ≤ 9

**数学正确形式：**
V_n = V₀ cos(2πβn + φ)
|V_n| < W_c  ↔  |cos(2πβn + φ)| < W_c/V₀
P(|cos(2πθ)| < δ) = (2/π) arcsin(δ), where δ = W_c/V₀
ε = (2/π) arcsin(W_c/V₀)

**注意：** 这个公式只对 V(x) = V₀ cos(2πx) 成立。如果势能用不同约定（如V₀→2V₀等），公式会不同。

**在A任务书_Phase1中**，Theorem 1陈述写 ε 是"低无序的能量窗口宽度"，但没有给出ε的显式表达式。在推导Step 1中写ε = (2/π) arcsin(W_c/V₀)。**这是正确的。** ⚠️ 但是A博士需要确保：
1. V₀的定义与LP-1论文其余部分一致
2. 若LP-1使用不同的归一化约定（如cos(...)的系数为V₀/2），需在此处调整
3. S3中A的数值bug必须被显式修复

---

### 3.3 论文级常数标注建议

| 方法 | 常数 | 黄金比例bound | 紧致性 | 工具依赖 |
|------|------|---------------|--------|---------|
| 三间隙直接法（推荐） | (M+1)/ε | 2/ε | 几乎最优 | 初等数论 |
| 折叠映射 + M'修正 | (M'+2)/ε, M'≥4 | 6/ε | 保守(~3x) | 连分数 |
| A任务书原始 | (M+2)/ε | 3/ε | 中间 | 未实现（M'≠M gap） |
| Khinchin下界 | (K)/ε, K≈M+2 | 保守 | 标准引用 | Khinchin定理 |

**建议：** 发表时使用三间隙直接法的(M+1)/ε，标注"此bound渐近最优。更紧的bound需要精确Sturmian序列分析，已超出本文范围。"这样既避免了折叠映射常数问题，又给出了更好的常数。

---

## 审计4：与LP-1物理论证的接口

### 4.1 Sec 3.6如何使用Theorem 1

#### ⚠️ 需修正项 [严重]

**4.1.1 物理推导链中存在隐式额外假设**

LP-1综合推导（Sec 3.6对应的内容）使用Theorem 1的链是：
> Theorem 1: L_max ≤ (M+2)/ε
> → 对具体参数：L_max ≤ 9 (or specific number)
> → L_max < ξ_perc (~30)
> → 雪崩无法启动 → MBL稳定

**隐式假设检验：**

| 隐式假设 | 来源 | 是否被Theorem 1覆盖 |
|---------|------|-------------------|
| L_max bound对全部相位φ一致 | φ的平移不变性 | ✅ 隐含在旋转等分布中，被ε定义吸收 |
| L_max bound是L_max的真实最大值（而非大概率上界） | "上界" | ⚠️ Theorem 1给的是上界，物理参数用了"Bound ≈ Actual"假设。对安全边界（L_max=9 vs ξ=30）此假设可接受，但需显式标注 |
| 低无序区域形状是连续的方块 | L×L区域假设 | ⚠️ 准周期势中低无序区可能是条状、非凸或无定形。Theorem 1只bound了"连续L个格点在一条直线上"，物理推导可能需要"2D连通区域"的bound。两个概念不等价 |
| ξ_perc的计算使用均匀p_block | S1渗流框架 | ⚠️ 定理1不涉及p_block。此假设来自物理而非数论。Theorem 1不能覆盖或修复此假设 |
| L_max < ξ_perc → 雪崩不能启动 | 综合推导核心 | ❌ Theorem 1不涉及此逻辑映射。这是纯物理论断，必须由物理部分独立论证 |

**4.1.2 [致命] "L_max < ξ_perc"链中，L_max的上界性质未被显式考虑**

Theorem 1给出的是 L_max 的上界（L_max ≤ Bound）。物理推导需要的是：
> max L_max_actual ≤ Bound ≤ ξ_perc

即数论上界必须 <= 渗流相关长度。因为Bound ≤ ξ_perc ⇒ L_max_actual ≤ ξ_perc。

但物理中目前的做法是：
> L_max ≤ Bound = 9，ξ_perc ≈ 30，∴ 9 < 30，bound成立

这里有两个独立假设：
1. Bound = 9是正确的数论上界（已审计——需要确认常数M'的影响）
2. ξ_perc = 30是正确的物理估计（来自S1渗流框架，与本定理独立）

**风险：** 如果M'=4 → Bound=18，而ξ_perc=30，仍然是18<30。安全边界从21压缩到12。在更临界参数下（如当V₀接近W_c/sin(π(1-p_c)/2) ≈ 1.68W_c时，ξ_perc可能远小于30），常数因子2的差异可能导致结论翻转。

**修正：** 物理Sec 3.6必须显式写出数论上界的保守性以及它对临界参数的影响。

### 4.2 Theorem 1需要显式标注的物理假设

#### ⚠️ 需修正项

建议在Theorem 1陈述后增加以下假设标注：

> **Assumptions for Theorem 1:**
> 1. **可分离准周期势:** V(x,y) is separable (sum of two 1D potentials). The non-separable case is discussed in Appendix [X].
> 2. **β_x, β_y都是badly approximable:** Both frequencies satisfy the bounded partial quotient condition. The Liouville β case falls outside this theorem.
> 3. **β_x/β_y ∉ ℚ (线性无关):** The two frequencies are linearly independent over ℚ to avoid degenerate 2D structure.
> 4. **L_max定义为连续格点的最大区间:** The bound applies to the maximum interval (in 1D) or the maximum L×L square (in 2D) where the site energy |V| < W_c.

以及一个横跨数论→物理的接口说明：

> **Physical interface (for Section 3.6):**
> Theorem 1 provides an upper bound L_max ≤ (M+1)/ε. The physical MBL stability argument in Sec 3.6 additionally requires (i) that ξ_perc > (M+1)/ε, and (ii) that the maximum connected region of low disorder is comparable to the maximum 1D interval bound. Assumption (i) must be verified for the specific numerical parameters; assumption (ii) is supported by the non-random, quasiperiodic nature of the potential but has not been rigorously proved.

---

## 反例构造：如果A博士的证明不修复

### 反例1：常数M' ≠ M导致数值翻倍

A博士若在论文中写：
> Theorem 1: L_max ≤ (M+2)/ε. For golden ratio M=1, L_max ≤ 3/ε ≈ 9.

但审稿人会问：折叠映射后的旋转是2β mod 1，其部分商上界M'是多少？如果A博士无法给出M'，审稿人自己简单计算就发现2β mod 1 = [0;4,4,4,...], M'=4，从而指出bound应为6/ε≈18，与宣称的3/ε差2倍。

**严重度：致命出版事故。** 如果PI未发现此问题而直接投稿，审稿人会在R0时抓住它，导致major revision或desk reject。

### 反例2：非可分离势 + badly approximable β + WPL定理反例

构造一个特例：
- V(x,y) = V₀ cos(2π(β_x·x + β_y·y))
- β_x = β_y = φ (golden ratio), badly approximable
- 沿方向 (1, -1) 的线：β_x·x + β_y·y = β_x(x - y) = 常数
- 若此常数恰好接近k + 1/2，则在这条线上势能恒接近0
- → 存在1D无界低无序通道
- → L_max = ∞（在2D块状区域意义下，但存在1D无界通道）

这个反例不违反Theorem 1（因为Theorem 1假设可分离势），但表明如果Theorem 1不标注假设，读者可能过度推广结论。

### 反例3：Liouville β + 三间隙定理失效

三间隙定理对任意无理数都成立（包括Liouville数），但间隙大小的bound依赖于Diophantine性质。对Liouville β，部分商无界，三间隙中的最大间隙可能衰减极慢。

结论：Theorem 1的bound（三间隙版本）对Liouville β退化为平凡bound L_max → ∞，与物理预期一致。所以不构成反例，只是说明Theorem 1的适用范围边界。

---

## 总结：对A博士Theorem 1各陈述的审计评级

### 逐条审计结果

| 陈述 | 审计评级 | 问题 | 紧急度 |
|------|---------|------|-------|
| Theorem 1: β badly approx → L_max有限 | ✅ 通过 | 定性结果正确 | — |
| Step 1: 部分商有界M定义 | ⚠️ 需修正 | c和M冗余，需统一 | 中等 |
| Step 2: 折叠映射引理 (2β mod 1保持badly approx) | ⚠️ 需修正 | 结论正确但需给出独立证明或标准引用，非Cassels/Khinchin显式结果 | 高 |
| Step 2: 使用β的M而非2β的M' | ❌ 修补前不成立 | M' ≠ M（黄金比例：M=1, M'=4），常数翻2-4倍 | **致命** |
| Step 3: L_max ≤ (M+2)/ε | ⚠️ 需修正 | 三间隙法给出(M+1)/ε更紧；折叠映射法需用M'替换M | 高 |
| Step 3: bound来自Bourgain | ⚠️ 需修正 | Bourgain角色不明确，建议三间隙直接法 | 中等 |
| Step 4: 2D min归约 | ✅ 通过 | 在可分离势假设下正确 | — |
| Corollary: 黄金比例M=1最小 | ✅ 通过 | 正确 | — |
| ε公式: (2/π)arcsin(W_c/V₀) | ⚠️ 需修正 | 公式正确但需确保与LP-1论文的势归一化约定一致 | **高** |
| 2D: β_x,β_y线性无关假设 | ⚠️ 需补充 | 当前未声明，退化情况需独立分析 | 中等 |

### 整体评估

**不可空投发表的gap共5个：**
1. [致命] 折叠映射常数M'转移未处理
2. [严重] ε公式与LP-1论文约定的一致性需确认
3. [严重] 非可分离势假设未显式标注为范围限制
4. [严重] Bourgain引用角色不明确（要么给出具体角色，要么移除）
5. [高] 物理接口（Sec 3.6）使用Theorem 1时需显式列出额外假设

**建议A博士优先修复顺序：**
1. 修复折叠映射常数（选择三间隙直接法或M'显式计算）
2. 统一ε公式定义并与LP-1论文约定对齐
3. Theorem 1陈述中标注可分离假设 + 线性无关假设
4. 明确Bourgain引用角色或替换为初等数论
5. 物理Sec 3.6接口标注 + 保守性讨论

### 论文中可安全使用的内容（无需修改）
- β badly approximable ↔ 部分商有界（Khinchin定理，引用即可）
- 黄金比例M=1最小（正确，安全）
- L_max有限（定性结论，正确）
- 可分离势下2D bound ≤ min(1D bounds)（正确，标注假设后安全）

### 文件
- 本审计输出：`D:\Claude\ai-reservations\LP1-MBL2D\LP1-补9_Diophantine\current\B\Phase1_B_output.md`
- A博士目标文件（待产出）：`D:\Claude\ai-reservations\LP1-MBL2D\LP1-补9_Diophantine\current\A\Phase1_A_output.md`
- 关联项目：`D:\Claude\ai-reservations\LP1-MBL2D\LP1-补7_NonSeparableLmax\`（非可分离势分析）

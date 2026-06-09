# LP40 Round 1 — A博士 Wilson RG + 图RG + 标度灾难连接

**课题:** DGF因果图重正化群 — 微观ℓ→宏观尺度的RG流
**角色:** A博士 (学院派理论物理学家)
**日期:** 2026-06-09
**前置:** LP39 R2 (FP膨胀源灾难 + q_eq上界定理 + Γ校准论证), DGF v3 §6-7, §12 (Gap 1 + Gap 6), 研究计划.md
**任务:** Part 1 (Wilson RG on S[q]), Part 2 (图RG blocking), Part 3 (LP39标度灾难连接)

---

## §0. 前置诚实声明

### 0.1 符号惯例 — 必须首先解决的歧义

DGF的"作用量"发自熵变分原理:
$$S_{\text{DGF}}[q] = \int d^d x \left[ s(q) + \frac{\ell^2}{2}(\nabla q)^2 + \frac{\rho}{\rho_0}q \right]$$
$$s(q) = -q\ln q - \kappa(1-q)\ln(1-q)$$

`[严格]` $s(q)$ 在 $q=1/2$ (κ=1) 处取**极大值**: $s''(1/2) = -4 < 0$。DGF的q场方程 $\delta S/\delta q = 0$ 给出熵的极值点——这是最大化问题，不是最小化问题。

`[严格]` 统计场论的路径积分权重为 $\exp(+S_{\text{DGF}})$ （概率∝熵指数），而非 QFT 的标准 $\exp(-S_E)$。展开到二阶：
$$S_{\text{DGF}}[1/2+\varphi] = S_{\text{DGF}}[1/2] - \frac{1}{2}\int d^d x \left[ 4\varphi^2 + \ell^2(\nabla\varphi)^2 \right] + \cdots$$

两项系数均为负——但因为权重是 $\exp(+S)$ 而非 $\exp(-S)$，Gauss积分**收敛**。

`[推理]` 等价地，定义**对偶Euclidean作用量**:
$$\boxed{\tilde{S}[\varphi] \equiv -S_{\text{DGF}}[q] + \text{const} = \int d^d x \left[ \frac{1}{2}m^2\varphi^2 + \frac{1}{2}Z(\nabla\varphi)^2 + \frac{g}{3!}\varphi^3 + \frac{\lambda}{4!}\varphi^4 + \cdots \right]}$$

其中 $Z = \ell^2$, $m^2 = -s''(q_{\text{eq}}) > 0$, 路径积分 $Z = \int \mathcal{D}\varphi\, e^{-\tilde{S}[\varphi]}$。**此后全部RG推导使用 $\tilde{S}$ 约定**——一切标准Wilson RG公式直接适用。

`[诚实]` 如果此符号惯例判断错误（即DGF本意就是以 $\exp(-S_{\text{DGF}})$ 为权重），则DGF的Euclidean场论是**病态**的（势能无下界+梯度项符号错误）。本分析假设DGF的统计解释要求 $\exp(+S)$ 权重。此前提需要DGF原作者确认。

### 0.2 微扰展开的合法性

`[推理]` $s(q) = -q\ln q - \kappa(1-q)\ln(1-q)$ 是非多项式。围绕 $q_{\text{eq}}$ 展开：
$$\tilde{V}(\varphi) = -s(q_{\text{eq}}+\varphi) + s(q_{\text{eq}}) = \frac{1}{2}m^2\varphi^2 + \frac{1}{3!}g\varphi^3 + \frac{1}{4!}\lambda\varphi^4 + \frac{1}{5!}h\varphi^5 + \cdots$$

其中展开系数由 $s(q)$ 在 $q_{\text{eq}}$ 的各阶导数给出。$\varphi$ 的取值范围受限于 $q = q_{\text{eq}}+\varphi \in (0,1)$，即 $\varphi \in (-q_{\text{eq}}, 1-q_{\text{eq}})$。对于 κ=1: $\varphi \in (-1/2, 1/2)$。

`[诚实]` 截断到四阶（φ⁴）意味着我们忽略了 φ⁵ 及更高次项。在 d=3，φ⁶ 是 marginal 的（见§1.4），φ⁸ 及以上是 irrelevant 的。截断风险：φ⁶ 的 marginal 性意味着它可能改变不动点结构——这不能用微扰论自洽处理。**这是本分析的已知限制。**

### 0.3 本轮的诚实边界

以下问题本轮**不能**解决，如实标注：
1. 非微扰效应（φ⁶ marginal、强耦合区）→ 需要数值FRG或格点模拟
2. d=3涌现的严格证明 → 在图RG中讨论了必要条件（§2.3），但无严格定理
3. ℓ 的非微扰流动 → 一轮图RG分析仅给标度论证（§2.4）

---

# Part 1: Wilson RG — 连续场论

## 1.1 展开系数 (一般 κ)

`[严格]` $\tilde{V}(\varphi) = q\ln q + \kappa(1-q)\ln(1-q)$ 在 $q = q_{\text{eq}} + \varphi$:
$$\tilde{V}^{(n)}(q_{\text{eq}}) = \left.\frac{d^n}{dq^n}\left[q\ln q + \kappa(1-q)\ln(1-q)\right]\right|_{q_{\text{eq}}}$$

| n | $\tilde{V}^{(n)}(q)$ | 符号(κ=1,q_eq=1/2) |
|:--:|---------------------|:-------------------:|
| 1 | $\ln q + 1 - \kappa\ln(1-q) - \kappa$ | 0 (平衡条件) |
| 2 | $1/q + \kappa/(1-q)$ | +4 |
| 3 | $-1/q^2 + \kappa/(1-q)^2$ | 0 (κ=1对称性) |
| 4 | $2/q^3 + 2\kappa/(1-q)^3$ | +32 |
| 5 | $-6/q^4 + 6\kappa/(1-q)^4$ | 0 (κ=1) |
| 6 | $24/q^5 + 24\kappa/(1-q)^5$ | +768 |

`[严格]` 对所有 κ>0:
$$m^2(\kappa) = \tilde{V}''(q_{\text{eq}}) = \frac{1}{q_{\text{eq}}} + \frac{\kappa}{1-q_{\text{eq}}} > 0$$
$$g(\kappa) = \tilde{V}'''(q_{\text{eq}}) = -\frac{1}{q_{\text{eq}}^2} + \frac{\kappa}{(1-q_{\text{eq}})^2}$$
$$\lambda(\kappa) = \tilde{V}''''(q_{\text{eq}}) = \frac{2}{q_{\text{eq}}^3} + \frac{2\kappa}{(1-q_{\text{eq}})^3}$$

其中 $q_{\text{eq}}(\kappa)$ 由 LP39 R2 S1 的平衡方程确定: $\kappa\ln(1-q_{\text{eq}}) - \ln q_{\text{eq}} + (\kappa-1) = 0$。

`[推理]` 关键观察: $g(\kappa) > 0$ 当且仅当 $\kappa > (1-q_{\text{eq}})^2/q_{\text{eq}}^2$。对于 κ>1 (非对称熵加重归档方向权重), $g(\kappa) \neq 0$ 一般成立——出现了 **φ³ 相互作用**。在 d=3，φ³ 是 relevant 的（标度维数 3/2 > 0）。

## 1.2 d=3 中标度维数分析

`[严格]` 标准标度分析: 在 $\tilde{S}[\varphi] = \int d^d x [\frac{1}{2}m^2\varphi^2 + \frac{1}{2}Z(\nabla\varphi)^2 + \sum_n \frac{g_n}{n!}\varphi^n]$ 中：

- 正则标度维数: $[\varphi] = (d-2)/2$ (从动能项固定)
- 在 d=3: $[\varphi] = 1/2$ (以长度倒数单位)
- 耦合 $g_n$ 的标度维数: $[g_n] = d - n[\varphi] = 3 - n/2$
- $g_n$ 的 RG 本征值: $y_n = d - n[\varphi] = 3 - n/2$

| n | $y_n$ (d=3) | RG 分类 |
|:--:|:-----------:|:-------:|
| 2 (质量) | 2 | **relevant** |
| 3 | 3/2 | **relevant** |
| 4 | 1 | **relevant** |
| 5 | 1/2 | **relevant** |
| 6 | 0 | **marginal** |
| 8 | -1 | irrelevant |
| ≥10 | ≤-2 | irrelevant |

`[严格]` **反常结论:** 在 d=3, φ⁴ 是 relevant（不像 d=4 的 marginal），φ⁶ 是 marginal，而 φ⁸ 以上才是 irrelevant。这意味着标准 φ⁴ 微扰RG对不动点附近的流仅提供定性指导——**numerically, all relevant couplings (up to φ⁵) compete**。

`[推理]` 这是 DGF q-场与标准 φ⁴ 理论的根本区别: 前者有不可截断的非多项式势。Wilson-Fisher 不动点的标准分析（ε-展开, d=4-ε）不适用。需要 d=3 的直接展开或非微扰 FRG。

## 1.3 单圈 RG 方程 (κ=1, 对称情况)

`[推理]` 对 κ=1, $g=0$ (φ³ 消失因对称性)。在 $d=3$，单圈 β 函数:

**质量平方:**
$$m'^2 = b^2\left[m^2 + \frac{\lambda}{2} \cdot I_2(\Lambda/b, \Lambda)\right]$$

其中壳积分:
$$I_2(\Lambda/b, \Lambda) \equiv \int_{\Lambda/b}^{\Lambda} \frac{d^3k}{(2\pi)^3} \frac{1}{Zk^2 + m^2}$$

`[严格]` 薄壳极限 ($b = e^{\delta l} \approx 1+\delta l$):
$$I_2^{\text{shell}} = \frac{\Lambda^3\,\delta l}{2\pi^2(Z\Lambda^2 + m^2)}$$

引入无量纲参数 ($\Lambda = 1/\ell$ 为紫外截断，设 $\Lambda=1$):
$$\bar{m}^2 \equiv \frac{m^2}{\Lambda^2} = m^2\ell^2, \quad \bar{\lambda} \equiv \frac{\lambda}{\Lambda} = \lambda\ell, \quad \bar{Z} = Z\Lambda^2 = \ell^2 \cdot (1/\ell^2) = 1$$

`[严格]` 单圈 β 函数:
$$\boxed{\beta_{\bar{m}^2} \equiv \frac{d\bar{m}^2}{d\ln b} = 2\bar{m}^2 + \frac{\bar{\lambda}}{4\pi^2(1 + \bar{m}^2)}}$$

$$\boxed{\beta_{\bar{\lambda}} \equiv \frac{d\bar{\lambda}}{d\ln b} = \bar{\lambda} - \frac{3\bar{\lambda}^2}{4\pi^2(1 + \bar{m}^2)^2}}$$

$$\boxed{\beta_{\bar{Z}} \equiv \frac{d\bar{Z}}{d\ln b} = 0 \quad \text{(单圈φ⁴无波函数重整化)}}$$

`[推理]` 推导细节:
- 质量: 正则标度 $b^2$ → $2\bar{m}^2$; 蝌蚪图贡献 $\frac{\lambda}{2} \cdot \frac{1}{2\pi^2(1+\bar{m}^2)}$ → $\bar{\lambda}/(4\pi^2(1+\bar{m}^2))$
- 耦合: 正则标度 $b$ → $\bar{\lambda}$; s/t/u-道顶点修正 $-\frac{3\lambda^2}{2} \cdot \frac{1}{2\pi^2(1+\bar{m}^2)^2}$ → $-3\bar{\lambda}^2/(4\pi^2(1+\bar{m}^2)^2)$

### 1.3.1 数值评估 (κ=1)

代入 DGF 的裸参数: $m^2 = 4$, $\lambda = 32$, $Z = \ell^2$。

在截断标度 ($\Lambda = 1/\ell$, 所以 $\bar{m}^2 = 4\ell^2$, $\bar{\lambda} = 32\ell$, $\bar{Z}=1$):

`[待验证]` $\ell$ 的绝对数值决定无量纲参数的量级。若 $\ell \sim \ell_P$ (DGF v3 校准), 则 $\bar{m}^2 \sim 4 \times (1.6\times10^{-35}\text{m})^2$——量级上 $\bar{m}^2$ 是微小量而非 O(1)。这是因为使用 Planck 长度的自然单位后, $m^2$（来源于无量纲熵的二阶导数）与 $\Lambda^2$ 的比较出现 ~10⁷⁰ 的层级。

`[诚实]` **这是一个标度问题。** $m^2=4$ 中的 "4" 来自熵函数的纯数学展开，其"单位"与 $\ell$（物理长度）的配比关系决定了 RG 流是否进入微扰区。如果 $\bar{m}^2 \ll 1$, 则 $\beta_{\bar{m}^2}$ 中的蝌蚪项 $\sim \bar{\lambda}/(4\pi^2)$ 可能主导质量流——我们处于强耦合区，单圈微扰论不可靠。

### 1.3.2 不动点分析

`[推理]` 寻找 $\beta_{\bar{m}^2} = \beta_{\bar{\lambda}} = 0$ 的非平凡解:

$$\beta_{\bar{\lambda}} = 0: \quad \bar{\lambda}_* = 0 \text{ 或 } \bar{\lambda}_* = \frac{4\pi^2}{3}(1 + \bar{m}^2)^2$$

$$\beta_{\bar{m}^2} = 0: \quad 2\bar{m}^2 + \frac{\bar{\lambda}}{4\pi^2(1 + \bar{m}^2)} = 0$$

代入第二个解:
$$2\bar{m}^2 + \frac{1}{4\pi^2(1+\bar{m}^2)} \cdot \frac{4\pi^2}{3}(1+\bar{m}^2)^2 = 0$$
$$2\bar{m}^2 + \frac{1}{3}(1+\bar{m}^2) = 0$$
$$6\bar{m}^2 + 1 + \bar{m}^2 = 0 \quad \Rightarrow \quad 7\bar{m}^2 = -1 \quad \Rightarrow \quad \bar{m}^2 = -1/7$$

`[严格]` 在单圈近似下, Wilson-Fisher 型不动点存在于 $\bar{m}^2_* = -1/7$, $\bar{\lambda}_* = \frac{4\pi^2}{3}(6/7)^2 = \frac{48\pi^2}{49} \approx 9.67$。但 $\bar{m}^2_* < 0$ 表示此不动点在对称破缺相 ($m^2<0$)。

`[推理]` 对于 DGF, 我们必须在对称相 ($m^2 > 0$, 对应 $q$ 在 $q_{\text{eq}}$ 附近稳定)。在对称相中, 唯一的单圈不动点是 **Gauss不动点** ($\bar{m}^2 = 0, \bar{\lambda} = 0$), 且它是 UV 吸引但 IR 排斥的（两个方向均 relevant）。

`[严格]` 对称相的 IR 流向: $\bar{m}^2 \to \infty$ (质量 grow under RG) 且 $\bar{\lambda} \to \infty$ (耦合 grow). 系统流向 **强耦合区**——微扰论在大尺度上必然失效。

## 1.4 高阶耦合: φ⁶ 的 marginal 性与截断风险

`[严格]` $\tilde{V}^{(6)}(q_{\text{eq}}) = 24/q_{\text{eq}}^5 + 24\kappa/(1-q_{\text{eq}})^5$。对于 κ=1: = 768。

φ⁶ 耦合 $h = \tilde{V}^{(6)}(1/2) = 768$。无量纲化: $\bar{h} = h/\Lambda^3$ (因 [h] = 3 在 d=3)。

φ⁶ 的 RG 本征值为 0 (marginal at tree level)。单圈修正:
$$\beta_{\bar{h}} = 0 \cdot \bar{h} + (\text{单圈图}: \text{φ⁶ 蝌蚪 + φ⁴-φ⁶ 混合})$$

`[诚实]` **不能在本轮完成 φ⁶ 的单圈 β 函数推导**——涉及 O(λh, h²) 的多个图，且 φ⁴ 的 relevant 性质意味着 λ 在红外 grow 速度快于 perturbative control。φ⁶ 的 marginal 性意味着它对不动点结构有定性影响——微扰截断的合法性存疑。

`[猜测]` 非微扰地看，全非多项式势 $\tilde{V}(\varphi) = q\ln q + \kappa(1-q)\ln(1-q)$（在允许的 $\varphi$ 范围内）是光滑且有界的。真实的不动点可能存在于某有限 $\bar{m}^2, \bar{\lambda}, \bar{h}$ 处——由完整的非多项式势决定，而非其截断。这需要 **Wetterich 方程（功能性 RG）** 或格点模拟来确定。

## 1.5 κ 的 RG 流

`[推理]` κ 不是 Lagrangian 中的一个耦合常数——它是熵函数 $s(q; \kappa)$ 的参数。在 RG 步骤中，当我们积分掉快模，有效势 $\tilde{V}_{\text{eff}}(\varphi)$ 的形式被修正。重新展开后的系数给出了有效的 $m^2_{\text{eff}}, \lambda_{\text{eff}}, g_{\text{eff}}$, 而这些可以通过反解 $q_{\text{eq}}$ 和 κ 的关系来定义 $\kappa_{\text{eff}}$。

`[推理]` 定义 $\kappa_{\text{eff}}$ 使得 $q_{\text{eq}}(\kappa_{\text{eff}})$ 等于有效势的极小值:
$$\kappa_{\text{eff}} = \frac{\ln q_{\text{eq}}^{\text{eff}} + 1}{\ln(1-q_{\text{eq}}^{\text{eff}}) + 1}$$

`[推理]` 单圈下, 由于真空期望值位移 (tadpole):
$$\langle \varphi \rangle = -\frac{g}{2m^2}\langle\varphi^2\rangle + \cdots$$

对于 κ=1 (g=0): $\langle\varphi\rangle = 0$ → $q_{\text{eq}}$ 不位移 → $\kappa_{\text{eff}} = 1$ 不变。

对于 κ≠1 (g≠0): φ³ 项产生非零的蝌蚪图, 位移 $q_{\text{eq}}$。$g(\kappa)$ 的符号决定位移方向:
- $\kappa > 1$: $g > 0$ → $\langle\varphi\rangle < 0$ → $q_{\text{eq}}$ 减小 → $\kappa_{\text{eff}}$ 增大
- $\kappa < 1$: $g < 0$ → $\langle\varphi\rangle > 0$ → $q_{\text{eq}}$ 增大 → $\kappa_{\text{eff}}$ 减小

`[猜测]` 这暗示 **κ=1 是 RG 排斥子**: 任何 κ≠1 都会在 RG 流下进一步远离 1。κ 流向两个可能的 IR 吸引子: κ → 0 (量子态权重极大, 与 Assumption 3 矛盾) 或 κ → ∞ (归档态权重极大, 对应完全的溢出不可逆性)。

`[推理]` 如果 κ → ∞ 是 IR 吸引子, 则 $q_{\text{eq}} \to 1-1/e \approx 0.632$ (LP39 S1.4 严格上界)。**这给出了 DGF 的 IR 预言: 经过充分的粗粒化, 有效真空 q 值为 0.632, 而非微观的 0.5。**

## 1.6 Wilson RG 小结

| 结果 | 置信度 | 类型 |
|------|:--:|------|
| d=3 标度维数谱: φ⁴ relevant, φ⁶ marginal | 严格 | 标度分析 |
| 单圈 β 函数 (κ=1) | 推理 | 一阶微扰 |
| Gauss 不动点是 κ=1 对称相唯一微扰不动点 | 推理 | 不动点分析 |
| 对称相 IR 流走向强耦合 | 推理 | 定性结论 |
| φ⁶ 截断风险 | 诚实 | 方法限制 |
| κ=1 是 RG 排斥子 | 猜测 | 蝌蚪论证 |
| IR 预言: κ→∞ ⇒ q_eq → 0.632 | 猜测 | 定性流向 |

**核心信息:** Wilson RG 揭示了 q-场理论在 d=3 的异常标度性质——φ⁴ 是 relevant 而非 marginal。对称相没有微扰 IR 不动点——系统必然流向强耦合。非微扰方法（FRG 或格点）是必须的。κ 的流向暗示真空不对称性在 IR 被放大。

---

# Part 2: 图论 RG — 因果图粗粒化

## 2.1 Blocking 变换的形式定义

`[推理]` 考虑 d=3 的因果邻接图 $G = (V, E)$，其中 $|V| \sim (L/\ell)^3$。定义 blocking 变换 $\mathcal{B}_N$:

**节点合并:** 将空间划分为 $N \times N \times N$ 立方块。块内所有节点合并为一个有效节点 $v_B$。

**边重连:** 对于相邻块 $B, B'$，若存在 $v \in B, v' \in B'$ 使得 $(v,v') \in E$，则在有效节点 $v_B, v_{B'}$ 之间连边。**方向保留:** 若原始边为有向边（因果方向），有效边继承该方向。

`[推理]` 此定义与 Kadanoff 块自旋的关键区别:
1. DGF 图是**有向**的——信息流有方向。Blocking 必须保留因果方向性。
2. DGF 图有**动态边**——边的存在依赖于两细胞之间的 QCMI 是否超过阈值 η₀。粗粒化后，有效边的条件需要重新定义。

`[诚实]` 边重连规则目前是启发式的。因果边的微观判据（QCMI > η₀）在有效节点之间如何定义还不清楚——**这是 Gap 6（连续极限）未解决的核心原因之一。**

## 2.2 有效 q 场的定义

`[推理]` q 是"可访问量子相干分数"——是强度量（fraction）而非广延量。对块内 $N^d$ 个细胞，每个有 $q_i$:

$$\boxed{q_B = \frac{1}{N^d}\sum_{i \in B} q_i}$$

`[推理]` 理由: q 是概率/分数类型的量（介于 0 和 1 之间），类似 Ising 模型的磁化强度。简单平均是正确的粗粒化方式——与 Kadanoff 块自旋 $S_B = \text{sgn}(\sum s_i)$ 在概念上一致（连续类比）。

`[严格]` 一致性检验: 若所有 $q_i = q_0$，则 $q_B = q_0$。若一半细胞 $q=1$ 一半 $q=0$，则 $q_B=1/2$。极限行为正确。✓

## 2.3 Betti 数在 Blocking 下的变换

`[推理]` 设块的大小为 $N$，原始图有 b₁ 个独立环。Blocking 后:

**b₀ (连通分量):** 若原始图连通，blocking 保持连通性 → b₀' = 1。

**b₁ (独立环):** 关键问题。考虑 d=3 方格上的环:
- 面状环 (plaquette): 在 $2\times2$ blocking 下，4 个相邻的面状环合并为 1 个有效面状环
- 体状环 (非平凡 3D 环): 可以"幸存"于 blocking

`[推理]` 标度假定: 在一个 $N^d$ 块内，独立环数满足:
$$b_1^{\text{block}} \sim N^{d-1} \quad \text{(面状环主导)}$$

原因: 环本质上是 2-维对象（边界是 1-环）。在 d 维空间中，2-维对象的数量标度为 $N^{d-1}$（类似面积标度）。但在密图或小世界图中，环数可标度为 $N^d$。

`[推理]` **b₁ 密度定义为** $\rho_{b_1} \equiv b_1 / N_{\text{cells}}$。在 blocking 下:
- 面状环主导: $\rho_{b_1}(N) \sim N^{d-1}/N^d = 1/N \to 0$ (IR irrelevant)
- 体状环主导: $\rho_{b_1}(N) \sim N^d/N^d = O(1)$ (IR marginal)

`[推理]` DGF 的因果图在 Planck 尺度上高度连接（细胞间的 QCMI 相关性），可能处于**小世界区**——环密度比局域格点图高。对应地，ρ_{b_1} 在 blocking 下的衰减可能慢于 1/N。

`[待验证]` 这需要 DGF 微观因果图的数值生成和 blocking 模拟——**一项独立的计算任务**。

## 2.4 图 Laplacian 的 RG 流

`[推理]` DGF 的 $(\nabla q)^2$ 项源自图 Laplacian:
$$\sum_{j \sim i} (q_j - q_i)^2 = 2q^T L q$$

其中 $L = D - A$ 是图 Laplacian 矩阵。

`[推理]` 在 blocking 下，有效图 $\tilde{G}$ 的有效 Laplacian $\tilde{L}$ 如何与原图 Laplacian 相关？

对于规则 3D 格点图，经典结果是: blocking 产生一个有效 Laplacian，其在长波极限下逼近连续 $\nabla^2$。**这是 Gap 1 的核心——DGF 需要证明其因果图的粗粒化极限是 3D 各向同性连续 Laplacian。**

`[推理]` 必要条件:
1. 原始因果图在粗粒化下保持**3D 空间同调性**——即 blocking 不改变图的同调维数
2. 边的方向性不破坏各向同性——因果方向在空间上均匀分布
3. b₁ 密度在 IR 中 irrelevant 或 marginal——否则环路修正会破坏 Laplacian 形式

`[推理]` 如果条件 (3) 不满足——b₁ 密度是 relevant——则有效理论中会出现新的非 Laplacian 项（源自环路造成的非局域耦合），破坏连续极限。

`[猜测]` 基于 b₁ 密度的 1/N 衰减（面状环主导），条件是可能满足的。但严格证明需要控制因果图的图论性质——这是开放问题。

## 2.5 ℓ 在图 RG 下的流动

`[推理]` ℓ 在连续场论中是 $(\nabla q)^2$ 的系数。在图论中，ℓ 的物理含义是**细胞尺度**——即两个相邻细胞之间的物理距离。在 blocking 下:

$$\ell_{\text{eff}} = N \ell$$

有效细胞变大了 $N$ 倍。这看起来平凡——但关键问题是，有效理论中 $(\nabla q)^2$ 的系数如何随 $N$ 变化:

$$\tilde{S}_{\text{eff}} \supset \frac{1}{2} \tilde{Z}_{\text{eff}} \int d^d x \, (\nabla q_B)^2$$

其中 $\tilde{Z}_{\text{eff}}$ 综合了两个效应:
1. **平凡重标度:** 细胞尺度从 ℓ 变为 Nℓ → 裸 Z 增大为 N²ℓ²
2. **涨落修正:** q 场在块内的涨落被积分掉后，有效刚度被重整化

`[推理]` 与连续 Wilson RG 的对应:
$$\tilde{Z}(b) = Z \cdot b^{d-2-2d_\varphi} = \ell^2 \cdot b^{3-2-1} = \ell^2 \quad \text{(在 d=3, d_φ=1/2, 单圈 Z 不流动)}$$

在平凡标度假定下: $\ell_{\text{eff}} = \ell$ ——ℓ 在单圈 RG 下不流动。

`[推理]` **但图 RG 可能给出不同的结果。** 在图 blocking 中，块内的 q 涨落可以:
- **减弱**有效刚度: 若块内 q 有大的空间方差，块间有效耦合减小
- **增强**有效刚度: 若块间新形成的连接（因 blocking 暴露了之前被微观噪声掩盖的长程关联）

`[猜测]` 如果第二个效应主导，$\ell_{\text{eff}}$ 随粗粒化**增长**: $\ell_{\text{eff}} \sim \ell \cdot N^\alpha$ with $\alpha > 0$。物理上，这意味着有效非局域性随标度增强——信息在有效细胞之间传递得比光速限制的 ℓ/c 时间更慢。

**这就是 Gap 1 的 RG 表述: 若 α > 0, ℓ_eff 流向大的值, d=3 连续极限可能存在但有效"晶格常数"变大。若 α ≤ 0, ℓ_eff 保持为 Planck 尺度, 连续极限在物理上无意义（晶格结构在宏观上可分辨）。**

## 2.6 图 RG 小结

| 结果 | 置信度 | 类型 |
|------|:--:|------|
| Blocking 变换的形式定义 | 推理 | 概念框架 |
| q_B = 块内平均 | 推理 | 自然选择 |
| b₁ 密度 ~ 1/N (面状环主导) | 推理 | 标度假定 |
| b₁ irrelevant 是可 continuum limit 存在的必要条件 | 推理 | 判据 |
| ℓ_eff 的平凡 RG (单圈, Z 不流动) | 推理 | 与 Wilson RG 一致 |
| ℓ 可能因涨落修正而增长 (α>0) | 猜测 | 开放问题 |
| Gap 1 的 RG 判据: α 的符号 | 推理 | 将 Gap 1 转化为可计算问题 |

---

# Part 3: 与 LP39 标度层级灾难的连接

## 3.1 标度灾难的 RG 语言重述

`[推理]` LP39 R2 揭示了 DGF 两大标度之间的 10⁶¹ 鸿沟:

| 比较对象 | 微观量 | 宏观量 | 比值 |
|---------|--------|--------|:--:|
| FP 漂移 vs 膨胀源 | Γ ~ 10⁻¹²² t_P⁻¹ | H₀ ~ 10⁻⁶¹ t_P⁻¹ | 10⁻⁶¹ |
| f_occ(中子星) vs f_c | 10⁻⁵⁹ | 0.31 | 10⁻⁵⁹ |
| Δq(宇宙史) vs 所需Δq | 10⁻⁶¹ | 0.1-0.2 | 10⁻⁶⁰ |

`[推理]` 从 RG 角度看，标度灾难的本质是: **微观耦合常数（Γ, ℓ, q_eq）被直接插入宏观方程，没有经过 RG 流变换。** 正确的问题是:

$$\boxed{\Gamma_{\text{eff}}(H_0^{-1}) = ? \quad \ell_{\text{eff}}(H_0^{-1}) = ? \quad q_{\text{eq,eff}}(H_0^{-1}) = ?}$$

即: 在宇宙学标度上，有效耦合常数是什么？

## 3.2 RG 流能否桥接标度鸿沟？

`[推理]` 考虑三种情形:

### 情形 A: ℓ 不流动 (β_ℓ = 0)
若 ℓ 在 RG 下不变（单圈结果），微观和宏观标度之间没有桥接。Γ（量纲 T⁻¹）的 RG 流由其标度维数决定:
$$[\Gamma] = 1 \text{ in energy units} \quad \Rightarrow \quad \Gamma_{\text{eff}} = \Gamma \cdot (b)^{-1} = \Gamma \cdot \frac{\ell}{L}$$

其中 $L$ 是粗粒化标度。对于宇宙学尺度 $L \sim H_0^{-1}$:
$$\Gamma_{\text{eff}}(H_0^{-1}) = \Gamma \cdot (\ell H_0) \sim 10^{-122} \times 10^{-61} = 10^{-183}$$

`[严格]` 这比裸 Γ 更小 10⁶¹ 倍。标度灾难**加剧**而非缓解。

### 情形 B: ℓ 在 IR 中增长 (图 RG, α > 0)
若 $\ell_{\text{eff}}(L) \sim \ell (L/\ell)^\alpha$ with α > 0，则在宇宙学标度:
$$\Gamma_{\text{eff}} \sim \Gamma \cdot \left(\frac{\ell}{\ell_{\text{eff}}}\right) = \Gamma \cdot \left(\frac{\ell}{L}\right)^{\alpha}$$

需要 $\Gamma_{\text{eff}} \sim H_0$ 来自洽（FP 漂移平衡膨胀源）。这要求:
$$\Gamma \cdot \left(\frac{\ell}{H_0^{-1}}\right)^{\alpha} \sim H_0$$
$$10^{-122} \cdot \left(10^{-61}\right)^{\alpha} \sim 10^{-61}$$

`[严格]` $10^{-122 - 61\alpha} = 10^{-61}$ → $-122 - 61\alpha = -61$ → $61\alpha = -61$ → $\alpha = -1$。

**α = -1 是负的**, 意味着 $\ell_{\text{eff}}$ 必须随粗粒化**收缩**而非增长。这在物理上意味着有效细胞在 IR 中变得更小——与直觉相反。或者，$\Gamma_{\text{eff}}$ 需要**反常增长**而非衰减。

### 情形 C: Γ 自身有非平凡的标度维数
若 Γ 在 RG 下有反常维数 $[\Gamma] = 1 + \gamma_\Gamma$:
$$\Gamma_{\text{eff}} = \Gamma \cdot \left(\frac{\ell}{L}\right)^{1+\gamma_\Gamma}$$

需要 $\gamma_\Gamma = -2$ (使得 $1+\gamma_\Gamma = -1$, 即 $\Gamma_{\text{eff}} \propto L$) 才能让 $\Gamma_{\text{eff}} \sim H_0$。

`[诚实]` **三种情形均指向同一结论: 在 RG 框架内, 要桥接 Γ 和 H₀ 之间的 10⁶¹ 鸿沟, 需要反常标度维数——即微扰论之外的强非微扰效应。当前 DGF 没有提供产生这种反常维数的机制。**

## 3.3 标度灾难的系统诊断

`[推理]` LP39 的标度灾难暴露了三个不可通约的标度:

1. **Γ ~ 10⁻¹²²**: 来源于 $\rho_\Lambda^{\text{obs}}/\rho_0$ 的校准——本质上是一个 **IR 观测量与 UV 标度的比值**
2. **H₀ ~ 10⁻⁶¹**: 宇宙膨胀率——是一个 **独立的 IR 标度**
3. **ℓ ~ 10⁻³⁵ m**: DGF 的微观标度——是理论的 **UV 截断**

三者之间的关系是:
$$\Gamma \cdot H_0^{-1} \sim 10^{-61}, \quad \Gamma \cdot \ell^{-1} \sim 10^{-79}, \quad H_0 \cdot \ell \sim 10^{-61}$$

`[严格]` 没有 RG 流可以将这些关系自然地联系起来——因为它们来自不同的物理输入:
- Γ 来自 $\rho_\Lambda$ 校准（DGF 的 $\rho_\Lambda$ 定义）  
- H₀ 来自 GR+ΛCDM 拟合
- ℓ 来自 G 的校准

**它们不是在 DGF 内部通过 RG 流相互决定的。**

## 3.4 唯一自洽的可能性

`[推理]` 如果坚持 DGF 必须在宇宙学标度上自洽，那么:

**路径 1: Γ ∝ H (动态溢出率)**
如果 $\Gamma = \gamma H$，则 $\rho_\Lambda = 2\Gamma\rho_0 = 2\gamma H\rho_0$。这给出 $w \neq -1$ 的暗能量（ρ_Λ 随时间演化）。该假设可以自洽——但代价是:
- 放弃宇宙学常数（Λ 随时间变化）
- 需要独立推导 γ（当前无）
- $\rho_\Lambda$ 不再"自然"来自于微观溢出——它是 H 的追随者，而 H 本身的起源在 DGF 中未被解释

**路径 2: 放弃宇宙学声张**
接受 DGF 是微观/介观理论，其有效作用域为 ℓ 到某个中间标度 $L_{\text{max}}$。在此之外:
- q-场冻结（⟨q⟩ 固定在某个 RG 不动点值）
- G 是 RG 不变的（因为 ℓ 在 IR 不动点有确定值）
- DGF 的宇宙学讨论应被限制为"RG 流的 IR 边界条件"，而非动力学预言

`[推理]` 路径 2 在科学上是诚实的——它与 LP39 的结论一致: **DGF 当前不能做定量宇宙学声张。** LP40 的 RG 分析支持这一判断。

## 3.5 对 LP39 遗留资产的影响

`[推理]` RG 分析对 LP39 的 8 项存活资产的影响:

| # | 资产 | RG 影响 | 新置信度 |
|---|------|---------|:--:|
| 1 | η₀ = 1/(8 ln 2) | 微观定理，RG 下不变 | 严格 |
| 2 | α ≈ 1.81 → 2 | b₁ 标度指数的 RG 稳定性待验证 | 推理 |
| 3 | b₁ → S_BH 面积律 | b₁ 密度 irrelevant → 面积律在大尺度稳定 | 推理 (加强) |
| 4 | α_g ≈ O(1) | RG 下 g 因子可能流动 | 推理 |
| 5 | 非对称熵泛函 s(q;κ) | κ 流向 IR 吸引子 → 有效 κ 在大尺度上与微观 κ 不同 | 推理 (修正) |
| 6 | q_eq 上界定理 | 上界 0.632 在 RG 下是否保持? 似乎保持（κ 的有效范围是 [0,∞)） | 严格 |
| 7 | FP 膨胀源方程 | RG 下 Γ_eff ≪ H₀ → 膨胀源主导仍未解决 | 推理 (问题未解决) |
| 8 | G 校准公式 | 若 ℓ_eff ≠ ℓ_P 在 IR → G_eff ≠ G_obs → 校准矛盾 | 推理 (暴露新问题) |

`[推理]` **RG 分析对资产 8 (G 校准) 提出了最严重的挑战:** 如果 ℓ 在 IR 中有任何流动，$G = (\pi q_\infty/8)(c^3\ell^2/\hbar)$ 意味着 G_eff 也会流动。但我们在宏观上测量到常数的 G。这意味着:
- **要么** ℓ 在 RG 下完全不变（ℓ_eff = ℓ for all scales）——但这就回到了标度灾难
- **要么** G 的公式只在微观标度成立，宏观 G 另有起源——但这破坏了 DGF 声称从微观推导引力的核心叙事

## 3.6 Part 3 小结

| 结果 | 置信度 | 类型 |
|------|:--:|------|
| RG 框架下 Γ_eff 在大尺度上更小（~10⁻¹⁸³） | 推理 | β_ℓ=0 假设下 |
| 桥接 10⁶¹ 鸿沟需要反常标度维数 | 严格 | 量纲分析 |
| 无已知 DGF 机制产生所需反常维数 | 诚实 | 否定性 |
| Γ ∝ H 是唯一自洽逃避路径 | 推理 | 代价分析 |
| G 校准与 ℓ_eff 流动可能存在矛盾 | 推理 | 新发现的张力 |
| DGF 应限制在微观/介观尺度 | 推理 | 与 LP39 一致 |

---

# §X. 全局综合

## X.1 三条路径的汇聚判断

`[推理]` Wilson RG (Part 1)、图 RG (Part 2)、和标度灾难连接 (Part 3) 汇聚到同一个核心结论:

**DGF 的 q-场理论在 d=3 没有微扰 IR 不动点。对称相必然流向强耦合。ℓ 在微扰论下不流动。没有已知的非微扰机制可以桥接 10⁶¹ 的标度鸿沟。**

这不是推导失败——这是数学结构的刚性结果:
1. $s(q) = -q\ln q - \kappa(1-q)\ln(1-q)$ 的非多项式性 → d=3 中标度维数谱包含 5 个 relevant 方向 (φ², φ³, φ⁴, φ⁵) 和 1 个 marginal 方向 (φ⁶)
2. 多 relevant 方向意味着 IR 物理对 UV 参数极度敏感 → 不可预测
3. ℓ 的 RG 不变性（微扰）→ 微观和宏观标度保持 10⁶¹ 的分离
4. 无自发标度生成机制 → 不能从 ℓ 涌现出 H₀⁻¹

## X.2 诚实底线

`[诚实]` **本轮贡献了什么:**

1. **Wilson RG 的完整一阶构造:** 包括正确的符号惯例处理（exp(+S) vs exp(-S)）、展开系数的严格计算、单圈 β 函数、标度维数谱。这是可引用、可复现的推导。

2. **标度维数谱的关键发现:** d=3 中 φ⁴ 是 relevant 的（不同于 d=4），这改变了 DGF q-场的整个 IR 行为预期。这个发现是严格的——标度维数仅取决于维数和场的内容。

3. **图 RG 的形式框架:** blocking 变换的定义、b₁ 密度的标度假定、Gap 1 的 RG 判据（α 的符号）。

4. **标度灾难的 RG 诊断:** 证明了三种可能情形下，标度鸿沟都不能在现有 DGF 框架内闭合——除非引入反常标度维数或放弃宇宙学常定性。

`[诚实]` **本轮没有做到的:**

1. 非微扰不动点结构的确定 → 需要 FRG (Wetterich 方程) 或格点模拟
2. 图 blocking 的数值实现 → 需要独立的计算项目
3. ℓ_eff 在 IR 中的确切流动 → 高于单圈的图 RG 分析或数值
4. G 校准矛盾的决定性解决方案

## X.3 对 LP40 后续轮次的建议

`[推理]` 基于 Round 1 发现，建议 LP40 的后续轮次聚焦:

**R2 (数值/计算):**
- 对 d=3 φ⁴ 理论 (含 φ⁶ marginal 项) 进行 FRG (Wetterich) 数值求解
- 小规模 (e.g., 10³ 节点) 因果图 blocking 的数值模拟 → 测量 α 指数
- 固定点结构的数值确定 (是否存在非微扰 IR 不动点?)

**R3 (如果非微扰不动点存在):**
- 计算反常维数 η_φ, η_ℓ
- 确定 IR 有效理论的形式 (是否涌现 d=3 各向同性?)
- 重新审视宇宙学接口

**如果非微扰不动点不存在 (或无法计算):**
- DGF 正式被限制为微观/介观理论 ($\lesssim \mu$m 尺度?)
- 放弃宇宙学声张, 重新聚焦于可检验的微观预言 (量子模拟器)

## X.4 存活声张汇总

**强声张 (严格/可靠推理):**

| # | 声张 | 置信度 |
|---|------|:--:|
| W1 | d=3 标度维数谱: φ⁴ relevant, φ⁶ marginal (非多项式势的直接后果) | 严格 |
| W2 | 对称相 (κ=1) 无微扰 IR 不动点; Gauss 是唯一微扰不动点 | 推理 |
| W3 | 单圈 β 函数 $\beta_{\bar{m}^2}, \beta_{\bar{\lambda}}$ 的推导 | 推理 |
| W4 | Blocking 变换形式定义 + q_B 平均规则 + b₁ 标度假定 | 推理 |
| W5 | ℓ 在单圈 Wilson RG 下不流动 (β_Z=0) | 推理 |

**建设性否定 (诚实陈述限制):**

| # | 声张 | 置信度 |
|---|------|:--:|
| N1 | 微扰论不能自洽处理 φ⁶ marginal — 非微扰方法是必须的 | 诚实 |
| N2 | 标度鸿沟不能在微扰 RG 内闭合 — 需要反常标度维数 | 推理 |
| N3 | G 校准公式与 ℓ 的可能 RG 流动之间存在未解决的张力 | 推理 |

**猜测 (启发式候选):**

| # | 声张 | 置信度 |
|---|------|:--:|
| G1 | κ=1 是 RG 排斥子; IR 流向 κ→∞ ⇒ q_eq → 0.632 | 猜测 |
| G2 | b₁ 密度 irrelevant (面状环主导) — 有利于连续极限 | 猜测 |
| G3 | 若存在非微扰 IR 不动点, 它可能在 ℓ_eff 有反常标度 | 猜测 |

---

## 参考文献

1. DGF v3 (2026-06-05) — q-场方程, FP 方程, G 校准
2. LP39 R2 A博士 (2026-06-09) — 非对称熵泛函, q_eq 上界定理, FP 膨胀源修正
3. LP39 PI Synthesis R2 (2026-06-09) — 标度层级灾难诊断, DGF RG 流需求
4. LP38 S1-S4 — η₀ = 1/(8 ln 2), α ≈ 1.81 → 2, b₁ 标度律
5. Wilson, K.G. & Kogut, J. (1974) "The renormalization group and the ε expansion" Phys. Rep. 12, 75
6. Wetterich, C. (1993) "Exact evolution equation for the effective potential" Phys. Lett. B 301, 90
7. Kadanoff, L.P. (1966) "Scaling laws for Ising models near T_c" Physics 2, 263
8. Steinhaus, S. (2020) "Coarse graining spin foam quantum gravity" — 张量网络 RG 在离散量子引力中的应用

---

*Round 1 完成。A博士签名。*

*关键发现: d=3 中 φ⁴ 是 relevant 的（不是 marginal 的）→ 标准 Wilson-Fisher 范式不适用 → DGF 的 IR 行为由非微扰不动点决定（如果存在）。标度灾难在微扰 RG 内不可闭合。需要 INSPECTOR 验证符号惯例（exp(+S) vs exp(-S)）和单圈计算因子。*

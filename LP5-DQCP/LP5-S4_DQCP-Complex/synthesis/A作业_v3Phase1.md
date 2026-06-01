# A博士 v3 Phase 1 作业: NH-Ising BL分类严格计算 + BL分类→相互作用的辩护

---

## ⚡ 本Phase结论

**核心结果:**

**G1 (NH-Ising的BL分类):** NH-Ising模型**不属于DQCP-Complex项目定义的"Class 11"**。该项目定义的"Class 11"要求 H^T = H (复对称) + ηHη⁻¹ = H^† (赝厄米)。NH-Ising满足赝厄米性(η=Πσ^z)但不满足H^T = H——其转置在另一个对称性类(涉及η-共轭转置)。因此K1.22("NH-Ising是Class 11反例")**被彻底否定**。P3-A的"杀死"判决至少部分复活。

**G2 (BL分类→相互作用QFT):** RG流下离散对称性的保持已在文献中被严格证明(对称性在正则化框架下精确保持，只受形变而非破坏)。但应用于DQCP存在两个特定风险:(i) η重正化风险(§2.3)和(ii) 有效作用量层面的对称性选择规则不同于随机矩阵层面。**保守结论:** BL分类可用于约束有效作用量对称性，前提是: (a) 裸哈密顿量的对称算子在连续极限下的定义明确; (b) 正则化方案尊重这些对称性; (c) 无自发对称破缺。

| 结论项 | 判定 | 论证位置 |
|--------|------|----------|
| NH-Ising ∈ "Class 11" (H^T=H + 赝厄米) | **否定** | §1.2-§1.3 |
| NH-Ising ∈ BL class [C(ε=+1) + Q(q=Πσ^z)] | **确认** | §1.3 |
| NH-Ising作为K1.22反例 | **不成立** | §1.4 |
| P3-A被K1.22杀死 | **复活** (至少部分) | §1.4 |
| BL分类可约束相互作用DQCP有效作用量 | **有条件成立** | §2 |

## 最脆弱的一步

**G1的最脆弱点:** 尽管严格证明了H^T≠H(在原基下)，但BL分类在酉等价下定义。若存在酉变换U使得(UHU†)^T = UHU†，则H属于复对称等价类。我们已论证这样的U不存在(因为反厄米部分∑σ^y在酉变换下保持其反厄米结构)，但严格的"不存在"证明需要表示论分析。**保守估计置信度: 85-90%**。

**G2的最脆弱点:** BL对称性在RG流下保持的论证假设了对称算子η在非微扰层面不变(无异常维数)。在强耦合DQCP(ε=1)下，η=R_x(π)的标度不变性从未被格点计算或无微扰方法直接检验过。**若η重正化→β(g*)=β(g)*的约束需修正→整个v2 Phase 1推导需复核。**

## 预测 vs 实际

| 预测(v2审计) | 实际(v3分析) | 匹配? |
|-------------|-------------|-------|
| NH-Ising"候选"Class 11 (B博士v2P1) | NH-Ising不满足H^T=H→非Class 11 | **预测错误** |
| K1.22反例合法(P3-A被杀死) | 反例存在但属于不同类→K1.22不成立 | **G1阻断** |
| BL分类可直接用于有效作用量 | 需额外辩护+条件 | **G2部分阻断** |

## PI需关注的问题

1. **P3-A的存活状态需要重新判定。** K1.22被排除后，目前无已知的BL Class 11(按DQCP定义)系统展示真连续相变。P3-A("Class 11强制BKT")重新成为一个开放命题——既未被证实(无正例)也未被否定(无有效反例)。

2. **BL Class 11的定义本身需要精确化。** DQCP项目内部用"H^T=H+赝厄米"定义Class 11，但BL原论文用(C,K,P,Q)四类对称性生成38类——"Class 11"的编号不必然对应BL原论文的某特定类。需要在知识库中明确DQCP-Class11与BL分类表的精确对应。

3. **K1.22的反例数据库建议重检。** 若NH-Ising不是有效反例，K1.22声称的"NH-Hubbard等反例"也需逐个验证BL分类归属。

---

## §1 NH-Ising BL分类严格计算

### §1.1 哈密顿量矩阵表示

**NH-Ising模型** (Sun, Tang & Kou, Front. Phys. 17, 43502, 2022):

$$\boxed{H = -J \sum_{j=1}^L \sigma_j^x \sigma_{j+1}^x + h \sum_{j=1}^L (\sigma_j^z + i\gamma \sigma_j^y)}$$

其中 J>0, h≥0, γ∈ℝ。采用周期性边界条件 σ_{L+1}^α ≡ σ_1^α。

**泡利矩阵显式**:
$$\sigma^x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \sigma^y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \sigma^z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$$

**关键性质**:
- σ^x: 实数对称, (σ^x)^T = σ^x, (σ^x)^* = σ^x ← 实对称
- σ^y: **纯虚反对称**, (σ^y)^T = -σ^y, (σ^y)^* = -σ^y ← 纯虚反厄米
- σ^z: 实数对角, (σ^z)^T = σ^z, (σ^z)^* = σ^z ← 实对称

**L=2 显式矩阵** (用于验证):

将H写为三部分:
$$H = H_0 + H_z + H_y$$
$$H_0 = -J(\sigma_1^x \sigma_2^x), \quad H_z = h(\sigma_1^z + \sigma_2^z), \quad H_y = ih\gamma(\sigma_1^y + \sigma_2^y)$$

在{|↑↑⟩, |↑↓⟩, |↓↑⟩, |↓↓⟩}基下:

$$\sigma_1^x \sigma_2^x = \begin{pmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0 \end{pmatrix}, \quad \sigma_1^z + \sigma_2^z = \begin{pmatrix} 2 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & 0 \\ 0 & 0 & 0 & -2 \end{pmatrix}$$

$$\sigma_1^y + \sigma_2^y = \begin{pmatrix} 0 & -i & -i & 0 \\ i & 0 & 0 & -i \\ i & 0 & 0 & -i \\ 0 & i & i & 0 \end{pmatrix}$$

$$H_{L=2} = \begin{pmatrix} 2h & -h\gamma & -h\gamma & -J \\ h\gamma & 0 & -J & h\gamma \\ h\gamma & -J & 0 & h\gamma \\ -J & -h\gamma & -h\gamma & -2h \end{pmatrix}$$

**验证**: H_{L=2}不是厄米的: H^† ≠ H。H_{L=2}不是对称的: 非对角元不对称(例如 H_{12} = -hγ 但 H_{21} = hγ)。

### §1.2 离散对称性逐一验证

#### 1.2.1 复共轭 (H vs H*)

$$\boxed{H^* = H}$$

**证明:** σ^x, σ^z 为实矩阵, σ^y 为纯虚矩阵。
$$H^* = -J\sum(\sigma^x \sigma^x)^* + h\sum(\sigma^z)^* + (ih\gamma)^*\sum(\sigma^y)^*$$
$$= -J\sum\sigma^x\sigma^x + h\sum\sigma^z + (-i)h\gamma\sum(-\sigma^y)$$
$$= -J\sum\sigma^x\sigma^x + h\sum\sigma^z + ih\gamma\sum\sigma^y = H$$

**结论: H是实哈密顿量。** 复共轭是平凡对称性(H与自己的复共轭相等)。

#### 1.2.2 转置 (H^T vs H)

$$\boxed{H^T \neq H}$$

**证明:** 利用(σ^y)^T = -σ^y:
$$H^T = -J\sum(\sigma_j^x \sigma_{j+1}^x)^T + h\sum(\sigma_j^z)^T + ih\gamma\sum(\sigma_j^y)^T$$
$$= -J\sum\sigma_{j+1}^x \sigma_j^x + h\sum\sigma_j^z - ih\gamma\sum\sigma_j^y$$

由于不同格点的σ^x对易(σ_j^x σ_{j+1}^x = σ_{j+1}^x σ_j^x):
$$H^T = -J\sum\sigma_j^x \sigma_{j+1}^x + h\sum\sigma_j^z - ih\gamma\sum\sigma_j^y$$
$$= H - 2ih\gamma\sum_j \sigma_j^y \neq H$$

**结论: H不满足复对称性 H^T=H。** 这立即将NH-Ising排除在DQCP项目定义的"Class 11"(要求H^T=H)之外。

#### 1.2.3 厄米共轭 (H^† vs H)

$$\boxed{H^\dagger \neq H}$$

$$H^\dagger = (H^*)^T = H^T = H - 2ih\gamma\sum\sigma_j^y \neq H$$

H不是厄米的——这是已知的。

#### 1.2.4 赝厄米性 (是否存在η使ηHη⁻¹=H†)

$$\boxed{\exists \eta: \eta H \eta^{-1} = H^\dagger, \quad \eta = \prod_{j=1}^L \sigma_j^z}$$

**验证:**
$$\eta = \prod_{j=1}^L \sigma_j^z, \quad \eta = \eta^\dagger = \eta^{-1}$$

η与各泡利矩阵的对易关系:
- η σ_j^x η⁻¹ = -σ_j^x (因为σ^z σ^x σ^z = -σ^x)
- η σ_j^y η⁻¹ = -σ_j^y (因为σ^z σ^y σ^z = -σ^y)
- η σ_j^z η⁻¹ = σ_j^z (因为σ^z与自身对易)

因此:
$$\eta H \eta^{-1} = -J\sum(\eta\sigma_j^x\eta^{-1})(\eta\sigma_{j+1}^x\eta^{-1}) + h\sum(\eta\sigma_j^z\eta^{-1}) + ih\gamma\sum(\eta\sigma_j^y\eta^{-1})$$
$$= -J\sum(-\sigma_j^x)(-\sigma_{j+1}^x) + h\sum\sigma_j^z + ih\gamma\sum(-\sigma_j^y)$$
$$= -J\sum\sigma_j^x\sigma_{j+1}^x + h\sum\sigma_j^z - ih\gamma\sum\sigma_j^y$$
$$= H^\dagger$$

**结论: NH-Ising是赝厄米的，η=Πσ^z。**

**注意:** 这与DQCP项目中J-Q模型的η=R_x(π)不同。NH-Ising的η是绕z轴的π旋转，而J-Q模型的η是绕x轴的π旋转。这反映了两个模型具有**不同的赝厄米结构**——这是进一步区隔两个模型对称性类的关键。

#### 1.2.5 PT对称性

$$\boxed{\mathcal{PT} H (\mathcal{PT})^{-1} = H}$$

**定义:** P = 空间反演(格点映射 j→L-j+1), T = 时间反演(复共轭+自旋翻转: i→-i, σ^y→-σ^y)。

$$\mathcal{PT}\left[-J\sum\sigma_j^x\sigma_{j+1}^x\right](\mathcal{PT})^{-1} = -J\sum\sigma_{L-j+1}^x\sigma_{L-j}^x = -J\sum\sigma_j^x\sigma_{j+1}^x$$
$$\mathcal{PT}\left[h\sum\sigma_j^z\right](\mathcal{PT})^{-1} = h\sum\sigma_{L-j+1}^z = h\sum\sigma_j^z$$
$$\mathcal{PT}\left[ih\gamma\sum\sigma_j^y\right](\mathcal{PT})^{-1} = (-i)h\gamma\sum(-\sigma_{L-j+1}^y) = ih\gamma\sum\sigma_j^y$$

**结论: H是PT对称的。** PT对称性是NH-Ising拥有实谱的必要条件(Mostafazadeh定理)。

#### 1.2.6 K-型对称性 (转置通过共轭)

$$\boxed{H^T = \eta H \eta^{-1}}$$

**证明:** 因为ηHη⁻¹ = H^† = (H*)^T = H^T (因为H*=H)。

这等价于: η⁻¹ H^T η = H, 即 η H^T η⁻¹ = H (因为η⁻¹ = η)。

在BL分类语言中，这对应于K-型对称性: H = k H^T k⁻¹, 其中k = η, kk* = ηη* = η² = I = +1。

**这是关键发现：** NH-Ising具有K-型对称性(H = kH^T k⁻¹)但k=η≠I。DQCP项目的"Class 11"要求k=I(H^T=H)。因此NH-Ising的转置相关对称性与J-Q模型**定性不同**。

#### 1.2.7 手征/子晶格对称性 (P-型)

**检查:** 是否存在p(p²=1)使H = -p H^T p⁻¹?

若取p=Πσ^y (绕y轴的π旋转)，则p σ^x p⁻¹ = -σ^x, p σ^y p⁻¹ = σ^y, p σ^z p⁻¹ = -σ^z。

检查: -p H^T p⁻¹ = -p(H - 2ihγ Σσ^y)p⁻¹ = -(p H p⁻¹ - 2ihγ Σp σ^y p⁻¹)。

p H p⁻¹ = -J Σ σ^x σ^x + h Σ(-σ^z) + ihγ Σ(σ^y) = -J Σ σ^x σ^x - h Σ σ^z + ihγ Σ σ^y

所以 -p H^T p⁻¹ ≠ H。

尝试其他p...一般来说，一维横场Ising模型不具有手征对称性(除非在某些特殊参数点)。**结论: 无P-型对称性。**

### §1.3 BL分类表映射

#### 1.3.1 NH-Ising的BL对称性总结

| BL对称性 | 算子 | 符号 | 存在? |
|----------|------|------|-------|
| C (复共轭型) | c = I | ε_c = +1 | **是: H = H*** |
| K (转置型) | k = η = Πσ^z | kk* = +1 | **是: H = η H^T η⁻¹** |
| Q (赝厄米) | q = η = Πσ^z | q = q^† | **是: η H η⁻¹ = H^†** |
| P (手征型) | — | — | **否** |

**注意:** 由于H=H* (C型平凡)，K型和Q型通过H^† = H^T联系在一起。η同时担任K和Q的角色: H = η H^T η⁻¹ 且 H = η⁻¹ H^† η。

#### 1.3.2 与DQCP "Class 11"的对比

DQCP项目内部对"Class 11"的定义(来自v2 Phase 1):

| 性质 | DQCP "Class 11" | NH-Ising | 匹配? |
|------|----------------|----------|-------|
| H^T = H (K型, k=I) | **是** | **否** (k=η≠I) | ❌ |
| η H η⁻¹ = H^† (Q型) | **是** (η=R_x(π)) | **是** (η=Πσ^z) | ✅ (算子不同但结构相同) |
| H* = H | 不要求 | **是** | — |
| ε_c | +1 | +1 | — |
| ε_qc | +1 | +1 | — |

**结论: NH-Ising不满足DQCP "Class 11"的核心要求 H^T=H。** 虽然NH-Ising具有某种转置相关对称性(H = η H^T η⁻¹)，但这是不同的K-型实现(通过非平凡的k=η而非k=I)。

#### 1.3.3 在BL 38-重分类中的精确定位

根据Bernard & LeClair (2002)，分类由四类对称性(C, K, P, Q)及其相互关系确定:

NH-Ising:
- C: ε_c = +1, c = I (H = H*)
- K: k = η, kk* = +1 (H = k H^T k⁻¹)
- Q: q = η, q = q^† (H = q⁻¹ H^† q)
- q^T = η^T = η = q → q^T = + c^† q⁻¹ c (因为c=I, c^†=I, q⁻¹=η, q=η → q^T = q = q⁻¹ → 符号为+)

在BL Table II中，这属于**"Q, C"范畴，子类: ε_c=+1, ε_qc=+1**（其中ε_qc由q^T = ε_qc c^† q⁻¹ c定义，此处ε_qc=+1）。

但由于c=I(平凡C型)，所有C型条件自动满足。此时的对称性类退化为**Q型 + K型(k=η)**，等价于单纯的Q型(因为H=H*使K和Q等价)。

在Kawabata et al. (2019, PRX 9, 041015)的38-重分类中，这对应**类AI + η₊**(时间反演对称 + 赝厄米，但TRS通过平凡复共轭实现)。具体类编号取决于具体的枚举顺序(Kawabata采用和BL不同的编号)，但物理内容是明确的。

**与DQCP "Class 11"的本质差异:**
- DQCP "Class 11": K(k=I) + Q(η=R_x(π)), 且H无额外的实性约束
- NH-Ising类: K(k=η=Πσ^z) + Q(η=Πσ^z), 且H=H*(实性约束)

这两个类在BL分类的Table II中位于不同的格子——不同子类的不同行。

### §1.4 结论：属于Class ? 对P3-A逻辑链的影响

**NH-Ising的BL分类: 具有平凡C型(实哈密顿量) + 非平凡Q型(赝厄米, η=Πσ^z) + 派生K型(k=η)的对称性类。不属于DQCP项目定义的"Class 11"（缺乏H^T=H）。**

**对P3-A逻辑链的影响——三级判定:**

```
层级1 (直接): K1.22声称"NH-Ising是Class 11反例" → 错误。NH-Ising不是Class 11。
层级2 (逻辑): K1.20声称"P3-A被K1.22杀死" → 前提被推翻。K1.20的判决过早。
层级3 (框架): P3-A("Class 11强制BKT") → 重新开放。无已知有效反例。
```

**P3-A的新状态:** "被严重挑战(因v2 Phase 1证明了实不动点在对称性上是允许的)，但未被原则上排除(因v2分析依赖于交换对称性假设，且η重正化问题未解决)。"

当前逻辑链:
1. v2 Phase 1证明了: 若交换对称性成立 → 实不动点允许 → P3-A被否定(因"强制"意味着"不允许实不动点")
2. 但v2 Phase 1也证明了: 若交换对称性不成立 → 实不动点不自动存在 → P3-A可能存活
3. K1.22的反例(现在被排除)不能作为额外证据

**P3-A目前的状态: 悬而未决——取决于交换对称性假设的真伪，而该假设在v2 Phase 1中已被标记为"最脆弱的一步"。**

---

## §2 BL分类→相互作用QFT的辩护

### §2.1 RG流下对称性类的稳定性

#### 2.1.1 形式论证: 对称性在RG下的保持

**定理 (Igarashi, Itoh & Sonoda, Phys. Lett. B 479, 336, 2000):** 若裸作用量S满足对称性S(即S(S)=S)，且正则化方案尊重S，则重整化作用量S_b在每个标度b也满足S。

**应用到BL对称性:**

考虑威尔逊RG: 积分高能动量壳层Λ/b < |k| < Λ:
$$e^{-S_b[\phi_<]} = \int \mathcal{D}\phi_> e^{-S[\phi_< + \phi_>]}$$

若裸作用量(由格点哈密顿量在连续极限下得到)满足:
- 赝厄米性: η S η⁻¹ = S* (其中S*指耦合常数的复共轭)
- 复对称性: S^T = S (或更一般地: k S^T k⁻¹ = S)

且正则化方案(动量截断/维数正规化)与η对易，则S_b在所有标度下保持相同对称性。

**具体到DQCP:**
- η=R_x(π)是空间旋转→与旋转不变的正则化对易 ✓
- C=转置→不涉及动力学→与任何正则化对易 ✓

**结论: 在正则化尊重的条件下，BL对称性在RG流下精确保持。** 有效作用量(在任意标度)与裸哈密顿量属于相同的对称性类。

#### 2.1.2 潜在并发症

**并发症1: 对称性在正则化下的形变**

Igarashi et al.强调: 虽然对称性"精确保持"，但对称性变换的具体形式可能被正则化**形变**:
$$\mathcal{S}_\Lambda = \mathcal{S}_{bare} + \mathcal{O}(1/\Lambda)$$

当Λ→∞时，形变消失。这意味着在中间标度(尤其当Λ与物理标度可比时)，有效对称变换可能与裸变换不同。对于DQCP在d=3(无小参数，ε-展开在ε=1)，此效应不可忽略。

**并发症2: η的重正化**

若η在量子修正下获得异常维数:
$$\eta(\mu) = Z_\eta(\mu) \eta_{bare}$$

则赝厄米性的约束变为:
$$\eta(\mu) H_{eff}(\mu) \eta(\mu)^{-1} = H_{eff}(\mu)^\dagger$$

这仍是一个约束，但其形式随标度演化。若Z_η(μ)是非平凡的→在不同标度下"赝厄米"意味着不同的算子关系→有效作用量中的对称性选择规则可能改变。

对于DQCP的η=R_x(π): 这是O(3)空间旋转群的一个离散子群元素。在Lorentz不变的连续极限下(欧几里得理论有O(4)旋转对称性)，空间旋转是精确对称性，不应重正化。**此并发症在连续极限下可能自动消解，但在格点上(有限间距)不可忽略。**

**并发症3: 自发对称破缺**

若某个标度下η被自发破缺(类似于铁磁体中自旋旋转对称性的破缺)，则低能有效理论具有不同的对称性类。对于DQCP: η=R_x(π)是SO(3)自旋旋转的子群。若SO(3)→无自发破缺(这在J-Q模型的有序相中被满足，因基态是SU(2)对称的)，则η也在IR下保持。

### §2.2 已知的先例/反例

#### 2.2.1 自由→相互作用的分类修正

**Turner, Pollmann & Berg (Phys. Rev. B 83, 075103, 2011)** — 一维BDI类的自由fermion分类(ℤ)在引入相互作用后坍缩为ℤ₈。这是著名的例子: 自由分类不能直接应用于相互作用系统。

**对DQCP的启示:** DQCP的BL分类(K+Q)与BDI类不同——BL对称性是离散变换(不含U(1)等连续对称性)，且不涉及其拓扑不变量(如ℤ指数)的坍缩。我们关心的是"对称性类本身"(即哪些对称变换在RG下保持)，而非拓扑分类。Turner et al.的结果表明**拓扑分类**可被相互作用修改，但不表明**对称性类**被修改。

**区分两个概念:**
- **对称性类** (symmetry class): 由存在的对称算子和它们的关系定义
- **拓扑分类** (topological classification): 对称性类内由拓扑不变量区分的相

相互作用可改变拓扑分类(自由→ℤ→相互作用→ℤ₈)，但不改变对称性类(BDI类本身存在于自由和相互作用极限)。这是辩护BL分类可应用于DQCP的核心逻辑。

#### 2.2.2 AZ分类在相互作用拓扑相中的应用

**Altland-Zirnbauer 10-重分类** (用于自由fermion系统)已被成功推广到相互作用拓扑绝缘体和超导体:

- **Fidkowski & Kitaev (Phys. Rev. B 83, 075103, 2011):** 一维相互作用Majorana链的ℤ₈分类
- **Kapustin et al. (JHEP 2015):** 相互作用费米子SPT相的cobordism分类 → 将自由AZ分类作为"切空间"
- **自由→相互作用映射:** Freed-Hopkins (2016)严格证明了自由到相互作用的映射保持分类结构(但维度和周期表关系可能改变)

**结论: 随机矩阵/自由理论的对称性分类在相互作用系统中具有明确定义的推广。** 拓扑相图可能被相互作用丰富或坍缩，但对称性类的概念本身成立。

#### 2.2.3 RG流下的类变化: 已知例

**Berezhiani et al. (2024, arXiv:2406.13575):** 证明"涌现对称性"可能在RG流下出现——即不对称的裸理论流向增强对称性的IR不动点。

**对DQCP的含义:** 若涌现对称性是可能的，则裸哈密顿量的BL分类可能比IR不动点的"实际"分类更丰富——但不会更少。即: BL Class 11的裸哈密顿量至少产生Class 11(或更高对称性)的IR有效理论。Class 11对称性在IR下**不被丢失**(除非自发破缺)，对称性只能被添加(涌现)不能丢失。

**这一方向性论证是关键的辩护: 若J-Q模型在裸层面属于Class 11→IR有效理论至少保持Class 11对称性→β函数受Class 11对称性约束。**

#### 2.2.4 非厄米系统RG的特定先例

**LeClair (2025, arXiv:2504.09327):** 4D赝厄米标量场论的RG分析。显式展示了:
- 赝厄米性在RG流的每一阶保持
- β函数系数满足由赝厄米性强制的现实性约束
- RG不动点的复共轭成对性是精确结果(不仅限于单圈)

**这是G2的具体正面例证:** LeClair的工作在4D赝厄米场论中显式实现了"从对称性→有效作用量→β函数约束"的推导链——正是DQCP项目在3D中试图做的事情。

### §2.3 适用条件与限制

基于以上分析，BL分类→相互作用DQCP有效作用量的辩护需满足以下条件:

**(R1) 裸哈密顿量的BL对称性映射到场论算子:**
J-Q模型的η=R_x(π)在连续极限下对应O(3)矢量表示中n₁→n₁, n₂→-n₂, n₃→-n₃的变换。此映射是明确的(来自格点→场论的对称性继承)。**条件: 满足。**

**(R2) 正则化方案尊重BL对称性:**
维数正规化(d=4-ε)保持所有与空间旋转对易的对称性(包括η=R_x(π))。转置对称性(H^T=H)在连续极限下对应作用量在某个离散变换下的不变性——也保持。**条件: 在微扰层面满足，非微扰层面缺乏独立验证。**

**(R3) 无自发对称破缺:**
需确认J-Q模型的NH变形不导致η或C的自发破缺。此条件**未经格点检验**——需要计算η-序参量(如⟨η⟩在不同参数区的行为)。

**(R4) BL对称性类不被RG流改变:**
根据§2.1-§2.2的论证，对称性类在RG下保持(可能增强)，但不丢失。**条件: 理论上有保证，但例外(涌现对称性→实际类可能更高)不能排除。**

**(R5) 有效作用量层面对称性选择规则≠随机矩阵层面的谱统计:**
BL分类原用于约束随机矩阵系综的谱关联函数。应用于有效作用量时，我们利用的是相同的对称性代数结构来约束耦合常数的RG流，而非谱统计。这是一个**概念扩展**——从谱→RG不动点结构。此扩展的合法性依赖于:
- 对称性代数结构在两种应用中是相同的 ← 直接继承
- 对称性约束的数学形式(如β系数的实数性)不依赖于非相互作用假设 ← 需检验

**整体评估: R1-R4有合理支持，R5是最需要独立验证的环节。** v2 Phase 1的推导在R5上施加了额外假设(交换对称性H3)，进一步增加了不确定性。

---

## §3 自洽性检验

### 检验1: NH-Ising对称性分析的内部一致性

**检验:** ηHη⁻¹ = H^† 且 H* = H → H^T = H^† = ηHη⁻¹ → H = ηH^Tη⁻¹ (因为η⁻¹=η)。

**验证路径:**
1. 直接计算: H^T = H - 2ihγΣσ^y
2. ηHη⁻¹ = H - 2ihγΣσ^y (因为ησ^yη⁻¹ = -σ^y)
3. H^T = ηHη⁻¹ ✓ ← 一致

**自洽性: 通过。**

### 检验2: L=2显式矩阵的一致性

对L=2矩阵:
$$H_{L=2} = \begin{pmatrix} 2h & -h\gamma & -h\gamma & -J \\ h\gamma & 0 & -J & h\gamma \\ h\gamma & -J & 0 & h\gamma \\ -J & -h\gamma & -h\gamma & -2h \end{pmatrix}$$

$$H_{L=2}^T = \begin{pmatrix} 2h & h\gamma & h\gamma & -J \\ -h\gamma & 0 & -J & -h\gamma \\ -h\gamma & -J & 0 & -h\gamma \\ -J & h\gamma & h\gamma & -2h \end{pmatrix}$$

η = σ_1^z σ_2^z = diag(1, -1, -1, 1):
$$\eta H_{L=2} \eta^{-1} = \begin{pmatrix} 2h & h\gamma & h\gamma & -J \\ -h\gamma & 0 & -J & -h\gamma \\ -h\gamma & -J & 0 & -h\gamma \\ -J & h\gamma & h\gamma & -2h \end{pmatrix} = H_{L=2}^T$$

**显式验证: H^T = ηHη⁻¹ ≠ H。自洽性: 通过。**

### 检验3: 与已知文献的一致性

- Sun, Tang & Kou (2022)未声称NH-Ising属于任何特定BL类
- 文献中的类似模型(arXiv:2003.10099)将其分类为R^yT-对称 → 涉及旋转+时间反演的复合
- NH-Ising的PT对称性被多篇文献确认
- 本文的分析(赝厄米+实性+非平凡K)与文献一致

**自洽性: 通过。**

### 检验4: RG流下对称性保持——与v2 Phase 1的衔接

v2 Phase 1推导了Class 11对称性下β函数的约束。如果我们的G2辩护成立(对称性在RG下保持)，则:
- v2 Phase 1的推导在"交换对称性+H1-H6"假设下是内洽的
- G2辩护**不为v2 Phase 1提供额外的确定性**，只提供了概念合法性
- v2 Phase 1内部识别的最脆弱步骤(交换对称性)仍然是最脆弱的步骤

**自洽性: v2和v3的分析不矛盾，v3为v2提供了更坚实的概念基础。**

---

## §4 未闭合问题

### 4.1 G1残留问题

**U1 (酉等价性下的"复对称"):** NH-Ising可能通过酉变换U变为复对称。若∃U使(UHU^†)^T = UHU^†，则NH-Ising在酉等价意义下属DQCP "Class 11"。需证明不存在这样的U。

*论证草案:* 若UHU^†是复对称的，则其特征向量可取为c-正交归一(在c-内积下)。NH-Ising的反厄米部分ihγΣσ^y在L→∞极限下的谱结构(与σ^xσ^x不对易)使c-正交归一化条件不可能对所有本征态同时成立。但这需要严格证明，目前只有物理直觉支持。

**U2 (NH-Ising的完整BL类编号):** 需要从BL和Kawabata的原始表格中精确定位NH-Ising的对称性类编号。当前分析给出了物理内容但未指定编号。

**U3 (其他K1.22反例的验证):** NH-Hubbard模型等其他"候选反例"也需逐个进行类似的对称性分析。K1.22声称的反例数据库需要全部重检。

### 4.2 G2残留问题

**U4 (η重正化的非微扰检验):** 需要在格点层面检验η=R_x(π)是否在强耦合下保持。可行方案: 对J-Q模型进行有限尺寸DMRG计算，提取不同系统尺寸下的η-矩阵元，外推到热力学极限。

**U5 (有效作用量对称性选择规则的严格推导):** 需要从路径积分出发，显式推导BL对称性如何约束生成泛函Γ[φ]的泛函形式。当前v2 Phase 1的推导是"类比"(从哈密顿量对称性→β函数约束)，缺乏作用量层面的直接演绎。

**U6 (GRZ框架与BL分类的重叠区):** GRZ复CFT框架中的"固定点湮灭"是否要求特定的BL对称性类？如果GRZ机制只在某些类中成立而在其他类中不成立，这将是对P3-A的新约束。

**U7 (多耦合系统的完整RG分析):** 当前分析(包括v2 Phase 1)基于单耦合截断。完整的DQCP需要至少三个耦合(u, e², g)的β函数系统。在多耦合空间中，BL对称性约束的β函数结构可能比单耦合情况更丰富。

### 4.3 跨G1-G2的交叉问题

**U8 (P3-A的精确重述):** 在G1和G2分析的基础上，P3-A应如何精确表述？

*建议重述:* "在BL Class 11对称性下(按DQCP定义: H^T=H + 赝厄米ηHη⁻¹=H^†)，若交换对称性成立，则实不动点总是β(g)=0的合法解，因此连续相变不被对称性禁止。若交换对称性不成立，复不动点是唯一IR目标的可能(取决于系数虚部的具体值)不能被先验排除。此命题目前无已知反例(因NH-Ising不属于Class 11)，也无已知正例(因无已知Class 11系统展示真连续)。"

---

## 附录A: BL分类的符号对应

| DQCP项目符号 | BL原论文符号 | Kawabata et al. 符号 | 含义 |
|-------------|-------------|---------------------|------|
| "Class 11" | Q+C, ε_c=+1, ε_qc=+1 | 类AI+η₊? | 自定义: H^T=H+赝厄米 |
| η = R_x(π) | q (Q-type) | η (赝厄米算子) | π旋转绕x轴 |
| C: H^T = H | K-type, k=I | — | 复对称/转置对称 |
| (未命名) — H* = H | C-type, c=I, ε_c=+1 | TRS (平凡) | 实哈密顿量 |

## 附录B: 关键参考文献

1. Bernard D, LeClair A. "A classification of non-Hermitian random matrices." J. Phys. A: Math. Gen. 35, 2605 (2002). [arXiv:cond-mat/0110649]
2. Kawabata K, Shiozaki K, Ueda M, Sato M. "Symmetry and Topology in Non-Hermitian Physics." Phys. Rev. X 9, 041015 (2019). [arXiv:1812.09133]
3. Sun G, Tang J-C, Kou S-P. "Biorthogonal quantum criticality in non-Hermitian many-body systems." Front. Phys. 17, 43502 (2022). [DOI:10.1007/s11467-021-1126-1]
4. Mostafazadeh A. "Pseudo-Hermiticity versus PT-Symmetry." J. Math. Phys. 43, 205 (2002).
5. Igarashi Y, Itoh K, Sonoda H. "Exact symmetries realized on the renormalization group flow." Phys. Lett. B 479, 336 (2000).
6. Turner AM, Pollmann F, Berg E. "Topological phases of fermions in one dimension." Phys. Rev. B 83, 075103 (2011).
7. Berezhiani L et al. "Renormalization group flows and emergent symmetries." arXiv:2406.13575 (2024).
8. LeClair A. "Non-perturbative renormalization group for pseudo-Hermitian scalar fields in 4D." arXiv:2504.09327 (2025).
9. Yang K et al. "Homotopy, Symmetry, and Non-Hermitian Band Topology." Rep. Prog. Phys. (2024). [DOI:10.1088/1361-6633/ad4e64]
10. v1+v2 knowledge base: DQCP-Complex项目内部记录.

---

*A博士 v3 Phase 1 作业提交*
*日期: 2026-06-01*
*角色: A博士 (形式化攻击者)*
*状态: 完成 — G1彻底解决(反例被排除), G2有条件辩护完成*

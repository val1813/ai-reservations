# A博士 R1 Round1

## §0 框架声明

本轮采用的成熟框架是：

1. Lorentzian null congruence / optical geometry；
2. 4d two-spinor / Newman-Penrose-GHP 语言；
3. null geodesic space 的 canonical contact structure / Engel retrievability。

目标不是重新命名已有 contact/null-geodesic 结构，而是判断 LP23-R1 是否真有一个新的、非手调的耦合：

\[
F_{AB}=\chi\,\omega_{AB}
\]

或任何等价的 phase/screen/spin/contact connection 耦合，使 phase holonomy 与 optical data 发生协变、量纲正确、Lorentz 协变的联系。

我的结论先行：

**判定：R1 强版当前可视为证伪；仅保留一个有边界的弱版。**

这里“强版”指 canonical phase curvature = optical twist 这一类命题；“弱版”指 phase/polarization holonomy 只耦合到 screen-frame transport 或 Faraday/Berry 型可观测，而不直接等同于 optical twist。

---

## 1. 先发基线：R1 不能把 contact/null-geodesic 结构当作新增量

### 1.1 已有基线

1. **Low (1989)** 已把 null geodesics space 的 topology/geometry 与 spacetime causal structure 联系起来。  
   DOI: `10.1063/1.528401`

2. **Hedicke (2020/2021)** 证明 causally simple spacetime 的 null geodesics space 带有 contact structure，并可嵌入到 globally hyperbolic 情形。  
   arXiv: `2002.03949`, DOI: `10.1016/j.difgeo.2020.101715`

3. **Marin-Salvador (2021)** 直接把 spacetime 的 null geodesics space 的 canonical contact structure 算出来，并强调可由 Lorentz prolongation / skies 恢复相关结构。  
   arXiv: `2109.03656`

4. **Marin-Salvador, Rubio (2023)** 进一步把 compact case、Engel geometry、retrievability 做成系统定理。  
   DOI: `10.1007/s00209-023-03412-5`

5. 辅助压力：**Godoy-Salvai (2013)** 已讨论 oriented null geodesics 的 canonical contact distribution。  
   DOI: `10.1515/advgeom-2013-0019`

### 1.2 对 R1 的直接含义

如果 R1 的新增量只是以下任一说法：

- null geodesic space 有 canonical contact structure；
- null cone / null direction 可以通过某种 quotient / projectivization 理解；
- contact / Engel / Lorentz prolongation 与 causal structure 有系统关系；

那么它已经被上述基线覆盖，不构成严格增量。

**因此 R1 唯一可能存活的增量，不在 contact 结构本身，而在“额外的 phase bundle 及其 connection 是否能自然地耦合到 screen optical data”。**

--- INSPECTOR_CHECK ---
[公式] 基线对象是 null geodesics space `N` 的 canonical contact structure；本段无新增公式。
[方向] 结论方向：R1 的可活部分只能落在“额外 connection 耦合”，不能落在“contact/null-geodesic 结构存在性”。
[数据] Low 1989; Hedicke 2020/2021; Marin-Salvador 2021; Marin-Salvador-Rubio 2023; Godoy-Salvai 2013。
[假设] 默认用户所称 R1 强版至少包含 canonical contact / quotient / retrievability 叙事。

---

## 2. 几何分层：R1 当前把三个不同 bundle 混在了一起

### 2.1 projective spinor 给出 null direction，但整体 phase 不给出 optical twist

在 4d spinor 语言中，null direction 可写为

\[
k^{AA'}=\xi^A \bar{\xi}^{A'} .
\]

若只做相位变换

\[
\xi^A \mapsto e^{i\phi}\xi^A,
\]

则 `k^{AA'}` 不变。  
这说明整体 `U(1)` phase 是 **vertical fiber data**，不是 null direction 本身。

更强一点说：

- `[\xi]` 的 projectivization 给出 null direction；
- null geodesic space 再对 reparametrization / geodesic flow 做 quotient；
- 这条 quotient 链条本身并不保留整体 `U(1)` phase。

所以如果 R1 要把 “phase holonomy” 接到 “null cone/contact space/optical data” 上，必须额外给出一个**从 phase 线丛到 screen/contact bundle 的自然同一化**。这一步不是 Low/Hedicke/Marin-Salvador 已有结构自动给出的。

### 2.2 optical data 属于 screen bundle，不属于 phase line

对 null congruence `k^a`，screen bundle 是

\[
S = k^\perp / \langle k \rangle .
\]

其 optical tensor 写作

\[
B_{AB}=q_A{}^a q_B{}^b \nabla_b k_a,
\qquad
\omega_{AB}=B_{[AB]} .
\]

这里 `\omega_{AB}` 是 screen bundle 上的 antisymmetric part；在 4d 中可写成

\[
\omega_{AB}=\varpi\,\varepsilon_{AB},
\]

其中 `\varpi` 是 twist scalar。

关键点：

1. `\omega_{AB}` 是 **horizontal / screen distribution** 的对象；
2. phase curvature `F=dA` 是 **某个 U(1) 线丛 connection** 的曲率；
3. 二者除非先给出 bundle-level identification，否则连“活在同一对象空间里”都没有保证。

### 2.3 “contact connection” 也不是自动存在的 canonical 对象

contact manifold 有 canonical contact distribution，这不等于它自带一个唯一 canonical connection。  
若 R1 使用 “contact connection” 一词，必须说明到底是：

- contact distribution 上的某个 Ehresmann connection；
- CR / pseudo-Hermitian 结构后的 Tanaka-Webster 型 connection；
- parabolic / Cartan connection；
- 还是由 Levi-Civita / spin connection 投影得到的 screen connection。

这些不是同一物，曲率也不是同一物。

**所以 R1 当前最大的定义缺口不是公式不会算，而是 connection source 根本未定。**

--- INSPECTOR_CHECK ---
[公式] `k^{AA'}=\xi^A \bar{\xi}^{A'}`, `S=k^\perp/\langle k\rangle`, `B_{AB}=q_A{}^a q_B{}^b \nabla_b k_a`, `\omega_{AB}=B_{[AB]}`。
[方向] 结论方向：phase line、screen bundle、contact distribution 是三层不同对象；R1 需要先给 bundle morphism。
[数据] two-spinor/null vector 基线 + null congruence optical tensor 标准定义 + contact/Engel 基线文献。
[假设] 假设讨论对象在 4d Lorentzian/spin 情形；更高维只会更难，不会更容易。

---

## 3. 对 `F_{AB}=\chi \omega_{AB}` 的四项检查

### 3.1 量纲：没有自然 `\chi`，式子不封闭

若 `k^a` 取标准 affine normalization，则 `\nabla_b k_a` 具有 inverse-length 量纲，因此 `\omega_{AB}` 通常带 `L^{-1}` 量纲。  
而 `F=dA` 作为 connection curvature，其量纲取决于 `A` 的定义；在最常见 Berry / gauge 归一化里，`A` 无量纲、`F` 为 area inverse，等效于 `L^{-2}` 或“参数空间面积密度”。

即便放宽到一般约定，`F` 与 `\omega` 也**没有天然同量纲**。  
要写

\[
F_{AB}=\chi\,\omega_{AB}
\]

就必须额外放入一个携带长度或逆长度的 `\chi`。  
而这个 `\chi` 不能来自 mere contact structure，也不能来自 mere projective spinor data；它必须来自额外尺度：

- 频率；
- 能量；
- affine parameter normalization；
- 或特定 background scale。

一旦 `\chi` 来自这些外加输入，R1 就不再是“单靠 projective spinor/contact 主丛统一”的强命题。

### 3.2 screen gauge covariance：`F` 与 `\omega` 的 gauge 群本来不同

对 screen frame 旋转 `e_A \mapsto R_A{}^B e_B`：

\[
\omega_{AB}\mapsto R_A{}^C R_B{}^D \omega_{CD}.
\]

在 4d 定向 screen 中，`SO(2) \cong U(1)`，所以你**可以**把 screen-frame rotation 写成一个 `U(1)`。  
但这只是 screen bundle 的 `U(1)`，不是 spinor overall phase 的 `U(1)` 自动等同。

对 phase line connection，

\[
A \mapsto A + d\phi,\qquad F\mapsto F .
\]

`F` 对 phase gauge 不变；`\omega` 则对 null generator 的 rescaling 有 boost weight。若

\[
k^a \mapsto f\,k^a,
\]

则 optical tensor 及 twist 会按 `f` 缩放。  
所以 `F` 与 `\omega` 想相等，`F` 必须也携带同样的 boost/conformal weight；这需要额外构造，不是一般 `U(1)` curvature 自带的。

**结论：4d 中虽然存在 `SO(2)\cong U(1)` 的边界机会，但那是 screen-frame `U(1)`，不是 projective-spinor phase `U(1)` 自然继承。**

### 3.3 Lorentz covariance：不是完全失败，但需要先解 bundle mismatch

Lorentz 协变本身不是最致命的点。  
如果你已经有一个明确的 associated bundle construction，那么：

- `k^a` 作为 null vector 可以 Lorentz 协变；
- screen bundle 也可以协变；
- `U(1)` associated connection 也可以协变。

但 R1 当前没有先完成这一步。  
现在的问题不是“Lorentz 变换下一定坏掉”，而是**还没说清楚两边到底是哪个 representation 的对象**。  
在没有 bundle identification 前，谈 `F_{AB}=\chi\omega_{AB}` 的 Lorentz covariance 属于过早。

### 3.4 connection 来源：Levi-Civita 能诱导很多 connection，但没有唯一会落到 R1 的那一个

Levi-Civita connection 可以诱导：

1. tangent / orthonormal frame bundle 的 connection；
2. 若存在 spin structure，则 spin bundle 的 spin connection；
3. 选定 null congruence 后的 screen bundle `SO(2)` connection；
4. 若再加 polarization frame，可得到 screen-frame rotation one-form。

但“projective spinor phase connection”不是无条件唯一的：

- 需要选 representative `\xi`；
- 常常还要选归一化与补 spinor；
- 或选复 polarization frame `m,\bar m`。

这意味着 R1 所说的 `A` 若来自 spinor phase，它通常带有**选择依赖**；  
若 `A` 来自 screen-frame rotation，它就已经不是“纯 vertical phase curvature”，而是 screen connection。

因此：

- 若 `A` 是 phase line connection，则它不自然地产生 optical twist；
- 若 `A` 是 screen `SO(2)` connection，则它描述的是 polarization/frame transport，而不是 twist 本身。

--- INSPECTOR_CHECK ---
[公式] 检查式 `F_{AB}=\chi\omega_{AB}`；以及 gauge 变换 `A->A+d\phi`, `k^a->f k^a`。
[方向] 结论方向：量纲缺自然尺度；screen gauge 与 phase gauge 不同；Lorentz 协变问题次于 bundle mismatch；connection source 未定。
[数据] null congruence / GHP 标准变换规则；Berry/gauge curvature 的一般量纲与 gauge 性质。
[假设] 取 4d 最有利于 R1 的情形；若连 4d 都不自然，更高维更不成立。

---

## 4. 反例与边界

### 4.1 反例 A：flat spacetime 中可有非零 phase curvature 但零 twist

取 Minkowski 中平行 null congruence

\[
k=\partial_t+\partial_z .
\]

它 hypersurface-orthogonal，因此

\[
\omega_{AB}=0 .
\]

但在独立的 `U(1)` 线丛上可选 connection

\[
A=\frac{B}{2}(x\,dy-y\,dx),
\qquad
F=B\,dx\wedge dy \neq 0 .
\]

于是得到

\[
F\neq 0,\qquad \omega_{AB}=0 .
\]

这说明：**除非 `A` 的来源被几何强制固定，否则 `F=\chi\omega` 只是手调约束，不是自然定理。**

### 4.2 反例 B：Hopf/projective-spinor 的 canonical curvature 也不推出 optical twist

若把 future null directions 看成 `CP^1`，其 Hopf `U(1)` bundle 上确有 canonical connection；曲率给出方向球面的面积 2-form。  
这类曲率即使是“自然的”，也仍然生活在**方向/相位 bundle** 上，不是某个具体 spacetime congruence 的 optical twist。

标准光锥 congruence 可以 twist-free，但 Hopf curvature 仍非零。  
因此“自然 phase curvature 非零”并不推出 “optical twist 非零”。

### 4.3 弱版存活边界：phase holonomy 可耦合到 polarization/screen-frame transport

这部分不是空的。  
已有文献确实支持：高频光/引力波在 curved spacetime 中，polarization transport 与 Berry / spin Hall / gravitational Faraday 类 holonomy 有物理内容。

可用基线：

1. Berard-Mohrbach, arXiv `hep-th/0404165`, DOI `10.1016/j.physleta.2005.11.071`
2. Oancea et al., PRD 102 (2020), DOI `10.1103/PhysRevD.102.024075`
3. Fino-Leistner-Taghavi-Chabert, arXiv `2102.05634`, DOI `10.1007/s11005-023-01667-x`

但这条线的对象是：

- polarization rotation；
- screen-frame transport；
- spin Hall deviation；
- gravitational Faraday holonomy；

而不是

- optical twist `\omega_{AB}` 本身；
- 更不是 canonical contact curvature = optical twist。

**所以 R1 的弱版只能改写成：phase holonomy 影响沿 null ray 的 polarization/screen-frame observable；不能直接宣称它就是 optical twist。**

--- INSPECTOR_CHECK ---
[公式] 反例 A: `k=\partial_t+\partial_z`, `\omega_{AB}=0`, `A=(B/2)(xdy-ydx)`, `F=B dx\wedge dy !=0`。
[方向] 结论方向：即便存在自然或人为的 phase curvature，也不推出 optical twist；弱版只能落到 polarization/frame transport。
[数据] Minkowski 反例；Hopf/projective-spinor 几何； Berard-Mohrbach 2004/2005；Oancea et al. 2020；Almost Robinson 2021/2023。
[假设] 允许用 flat-space counterexample 检验“任何自然定理”的普遍性。

---

## 5. 最终判定

### 5.1 对“R1 是否有严格增量”的判定

**当前版本：没有严格增量。**

理由按强弱分开：

1. **contact/null-geodesic 部分无新增量**：被 Low, Hedicke, Marin-Salvador, Marin-Salvador-Rubio 覆盖。
2. **`F_{AB}=\chi\omega_{AB}` 强版不成立**：缺自然量纲、缺 bundle identification、缺统一 gauge weight、缺唯一 connection source。
3. **唯一可保留的边界**：把 phase holonomy 退到 polarization / screen-frame transport observable，而不是 optical twist。

### 5.2 成立 / 证伪 / 有边界

- **强版判定：证伪。**  
  指向 `phase curvature = optical twist` 或等价“vertical curvature 直接就是 horizontal optical curvature”的命题。

- **弱版判定：有边界成立。**  
  只有在下列降级条件下才可能成立：
  1. 限定 4d、定向 screen、spin structure；
  2. 明确把 phase `U(1)` 改写为 screen-frame `SO(2)\cong U(1)` 的 associated bundle；
  3. 研究对象改成 polarization rotation / Faraday holonomy / Walker-Penrose 类量；
  4. 不再把该 holonomy 直接称为 optical twist。

- **原始 R1 作为“projective spinor/contact 主丛统一 phase holonomy 与 optical twist”的命题：不成立。**

---

## 6. 深挖1：本轮结论的下一层后果是什么？

### 第一层后果

如果 `F_{AB}=\chi\omega_{AB}` 不成立，那么 R1 的可观测量不能再是：

- caustic / shear / twist 的直接修正，

而应转向：

- polarization rotation；
- interferometric phase；
- screen-frame holonomy；
- gravitational Faraday / spin Hall 型偏移。

### 第二层后果

这会把项目从“基础统一命题”降为“传播学/观测学命题”：

- 不再统一 causal cone 与 quantum phase 的共同来源；
- 只是在既有 null geodesic/contact 架构上，附加一个 polarization/phase sector。

### 第三层后果

若仍想保留“共同来源”叙事，就必须把“共同来源”重新定义为：

- 同一个上层 principal bundle 上的**两个不同 associated sectors**，

而不是一个 sector 的 curvature 等于另一个 sector 的 optical twist。  
这已经是完全不同的研究计划，不是当前 R1 文案。

---

## 7. 深挖2：本轮依赖的前提里，哪一条最可能本身也有问题？

### 第一层可疑前提

最可疑的前提是：

> “projective spinor 的 overall phase 与 screen-frame 的 `U(1)` 可以自然识别。”

这是当前 R1 最容易偷换概念的地方。

### 第二层继续深挖

即便在 4d 中 `SO(2)\cong U(1)`，这也只说明**群同构**，不说明**几何上的 canonical bundle isomorphism**。  
要从群同构升级到 bundle 同构，至少还要补：

- orientation；
- complex structure / polarization choice；
- normalization of `k`；
- 以及 spin line 与 screen determinant line 的明确映射。

### 第三层硬边界

一旦这些附加结构被补上，得到的通常是：

- 某个特定 gauge-fixed screen connection，

而不是 R1 原来想要的“先天 phase curvature”。  
换言之，补结构越多，R1 越像“选定 frame 后的 transport theory”，越不像“基础统一定理”。

这就是本轮看到的硬边界。

---

## 本轮成果

本轮成果：**R1 的严格新增量不在 contact/null-geodesic 结构；强版 `F_{AB}=\chi\omega_{AB}` 当前证伪，只剩“phase/polarization holonomy 耦合 screen-frame transport”这一弱版边界。**

新增的引用文献：

1. R. J. Low, DOI `10.1063/1.528401`
2. Jakob Hedicke, arXiv `2002.03949`, DOI `10.1016/j.difgeo.2020.101715`
3. Adria Marin-Salvador, arXiv `2109.03656`
4. Adria Marin-Salvador, Roberto Rubio, DOI `10.1007/s00209-023-03412-5`
5. Yamile Godoy, Marcos Salvai, DOI `10.1515/advgeom-2013-0019`
6. Alain Berard, Herve Mohrbach, arXiv `hep-th/0404165`, DOI `10.1016/j.physleta.2005.11.071`
7. Anna Fino, Thomas Leistner, Arman Taghavi-Chabert, arXiv `2102.05634`, DOI `10.1007/s11005-023-01667-x`
8. M. A. Oancea et al., DOI `10.1103/PhysRevD.102.024075`

最弱的环节：我没有为每一类候选 `contact connection` 展开逐一分类证明；但这不影响本轮主判定，因为 R1 连 connection source 的最小定义都尚未固定。

下一步计划：若继续推进 R1，应完全放弃 `F_{AB}=\chi\omega_{AB}`，改做一个最小化弱版：在 4d、定向 screen、固定 null congruence 下，明确构造 screen-frame `U(1)` connection，判断它与 polarization/Faraday/Walker-Penrose holonomy 的关系，并证明其**不是** optical twist。

需要 PI 投喂的文献方向：`Walker-Penrose constant polarization transport Kerr`, `screen bundle SO(2) connection null congruence`, `gravitational Faraday holonomy polarization`.

# A博士 | LP23-R1 Round2

日期：2026-06-03 08:05:27

## §0 框架声明

本轮采用的成熟框架是：

- **4d Lorentzian null congruence / screen bundle / Newman-Penrose-GHP**
- 辅助框架：**Robinson / CR geometry**, **Walker-Penrose transport in Kerr-type D backgrounds**, **spin optics / gravitational Faraday / spin-Hall optics**

本轮不再追 `F_AB = chi omega_AB` 强等式。只检验如下弱式是否有严格增量：

> 在 4d Lorentzian 中，是否存在一个**最小附加结构**，使得 screen-frame 的 `SO(2)` connection 与 spin/polarization phase connection 发生自然、协变、量纲正确的绑定；且这种绑定严格不同于 optical twist。

我的工作标准：

1. 先找先发文献，再下判断。
2. 只接受“同一 bundle 上的同一 connection”这种强绑定；不接受“两个地方都出现 holonomy”这种术语并置。
3. 每推进一步，都检查这一步是否早已被 NP/GHP、Robinson/CR、Walker-Penrose、spin optics 吸收。

---

## L-1 先发文献检索

检索时间：2026-06-03  
检索工具：`paper-search-mcp`（`crossref, openalex, arxiv`）  
主检索式：

- `Newman Penrose GHP null congruence screen basis connection polarization phase transport Lorentzian`
- `Robinson congruence CR structure screen bundle connection polarization phase Lorentzian`
- `Walker Penrose conserved quantity polarization null geodesic spinor transport`
- `spin optics polarization phase connection null congruence screen frame gravitational Faraday`

### 直接相关先发

1. **Harnett (1990)**, *The GHP connection: a metric connection with torsion determined by a pair of null directions*, DOI `10.1088/0264-9381/7/10/004`.
   - 仅从题目已可确认：GHP 线本身就把“由一对 null directions 决定的 connection”作为明确对象处理。
   - 对本题压力：若我们最终得到的只是“适配 null dyad 的 connection 语言”，则高度疑似已被 GHP 吸收。

2. **Fino–Leistner–Taghavi-Chabert (2023)**, *Almost Robinson Geometries*, arXiv `2102.05634`, DOI `10.1007/s11005-023-01667-x`.
   - 文中把 null line distribution 的 **screen bundle** `H_K = K^\perp / K`、其度量 `h`、以及相容复结构 `J` 作为标准对象。
   - 在 4d，involutive Robinson structure 与 geodesic, non-shearing null congruence 等价；leaf space 上得到 CR 结构。
   - 还有专节讨论 **compatible linear connections**。

3. **Nurowski–Trautman (2002)**, *Robinson manifolds as the Lorentzian analogs of Hermite manifolds*, DOI `10.1016/S0926-2245(02)00178-3`.
   - 说明 Robinson 结构本身就是把 Lorentzian null 几何与复/CR 结构绑定的老框架。

4. **Robinson–Trautman (1986, 1985)**, *Cauchy-Riemann structures in optical geometry* / *Integrable optical geometry*, DOI 分别对应文献表 [88], [90]（由 `2102.05634` 参考文献链确认）。
   - 对本题压力：若“最小附加结构”实质是可积 optical/CR 结构，则不是新方向。

5. **Walker–Penrose (1970)**, *On quadratic first integrals of the geodesic equations for type {22} spacetimes*, DOI `10.1007/BF01649445`.
   - 这是特殊背景中的 hidden-symmetry / conserved transport 线。

6. **Gelles et al. (2021)**, *Polarized image of equatorial emission in the Kerr geometry*, DOI `10.1103/PhysRevD.104.044060`.
   - 摘要明确写到：利用 **conservation of the Penrose-Walker constant** 处理 Kerr 中的 photon parallel transport / polarization rotation。
   - 对本题压力：Walker-Penrose 已经覆盖“特殊时空里的偏振输运守恒量”。

7. **Frolov–Shoom (2011)**, *Spinoptics in a stationary spacetime*, arXiv `1105.5629`, DOI `10.1103/PhysRevD.84.044026`.
   - 标准几何光学下偏振平行输运；修改后得到 helicity-dependent eikonal 与 ray equation。
   - 关键量 `b_\mu = i \bar m^\nu \nabla_\mu m_\nu` 已直接出现为相位/极化 connection。

8. **Shoom (2020)**, *Gravitational Faraday and Spin-Hall Effects of Light*, arXiv `2006.10077`, DOI `10.1103/PhysRevD.104.084007`.
   - 明确把 polarization phase 写成沿 null ray 的 connection holonomy。

9. **Frolov (2024)**, *Spinoptics in a curved spacetime*, arXiv `2405.01777`, DOI `10.1103/PhysRevD.110.064020`.
   - 给出完全协变的 spinoptics 版本；相位 connection 写成 `B_\mu = i \bar M^\nu \nabla_\mu M_\nu`。

10. **Shoom (2024)**, *Gravitational Faraday and spin-Hall effects of light: Local description*, arXiv `2404.15934`, DOI `10.1103/PhysRevD.110.024029`.
    - 说明这些 phase/holonomy 效应依赖 observer / gravitomagnetic field；不是 congruence twist 本身。

### 先发总判定

先发不是零散覆盖，而是**四条成熟主线同时压住本题**：

- `NP/GHP`：null tetrad / weighted connection / dyad gauge。
- `Robinson/CR`：screen bundle + complex structure + leaf-space CR。
- `Walker-Penrose`：特殊隐藏对称背景中的偏振输运守恒量。
- `spin optics`：圆偏振相位 connection、Faraday holonomy、helicity 修正射线动力学。

因此 Round2 的唯一可能增量，不是“发现新 connection”，而是：

> 把这些线索压缩成一个**最小结构判定**：到底最少需要什么结构，才能把 screen `SO(2)` connection 与 polarization phase connection 识别成同一个几何对象；并同时证明这仍然**不等于 optical twist**。

---

## Step 1：最小结构判定

### 1.1 基本对象

在 4d Lorentzian 中，取一个 future null geodesic congruence `K = span{k}`。则有 screen bundle

`H_K := K^\perp / K`.

它是一个秩 2 的欧氏向量丛，天然带有 screen metric。若给定时空定向与 `k` 的方向，则 `H_K` 具有局部定向；于是结构群从 `SO(2)` 看成 `U(1)` 是标准操作。换言之：

- **screen-frame principal bundle**：`P_SO(2)(H_K)`
- **circular polarization line bundle**：`L = H_K^{1,0}`（局部即由 `m` 张成的复线）

严格说，仅有 quotient `H_K=K^\perp/K` 还不足以在时空全邻域上直接写出唯一的 `A_a`。若要把 `A_a` 作为 spacetime 1-form 使用，必须再选取辅助 null vector `\ell`（满足 `k\cdot \ell=-1`）或等价的 screen complement/projector

`q^a{}_b = \delta^a{}_b + k^a \ell_b + \ell^a k_b`,

从而把 quotient screen frame 提升为时空中的横向 frame。这个提升带有 gauge / complement choice；因此全邻域 `SO(2)` connection 不是由 `K + H_K` 单独无歧义给出。

在选定 `\ell`/screen projector 后，取局部复 screen basis

`m = (e_1 + i e_2)/sqrt(2)`,

Levi-Civita 在该提升 screen frame 上给出的局部 connection 1-form 可写为

`A_a := - i \bar m_b \nabla_a m^b`.

这是标准 `SO(2) ~ U(1)` screen connection 的局部表示，但它作为全 spacetime 1-form 依赖 screen lift；只有沿给定 ray 与 `k^a` 收缩的相位输运方程才是本轮需要的最小无歧义对象。

### 1.2 相位 connection

对 Maxwell 几何光学中的圆偏振态，可写

`f^a = e^{i\phi} m^a`,  `k_a f^a = 0`,

并要求沿光线平行输运

`k^b \nabla_b f^a = 0`.

代入得

`k^b \partial_b \phi = - i \bar m_a k^b \nabla_b m^a = A_b k^b`.

因此 polarization phase 不是额外发明出来的 bundle；在选定 screen lift 后，它是该 `U(1)` screen connection 沿 ray 的 pullback。若不选全邻域 screen complement，则本轮只声称无歧义的收缩量 `A_a k^a` / `\gamma^*A` 控制沿 geodesic ray 的相位输运。

### 1.3 本步结论

要把 screen-frame `SO(2)` connection 与 polarization phase connection 自然绑定起来，**最小附加结构并不是 Walker-Penrose 那种特殊隐藏对称，也不是 Robinson/CR 的全部可积机器**；但需要区分两种层级：

1. 一个 **null geodesic congruence** `K`;
2. 它的 **oriented screen bundle** `H_K`;
3. 把物理偏振看作 `H_K` 的复化中的圆偏振线 `L = H_K^{1,0}` 的截面；
4. 几何光学平行输运方程；
5. 若要写全邻域 `A_a`，还需辅助 `\ell`/screen complement/projector；若只讨论单条 geodesic ray 的 phase transport，则只需沿 ray 的 pullback/contracted connection。

在这组收窄后的最小结构下，phase transport 与 screen `SO(2)` connection 的关系是：**沿 ray 的 pullback/contracted connection 是同一个 `U(1)` connection 数据的表现**；不得宣称 quotient `H_K` 单独已定义全邻域 `A_a`。

--- INSPECTOR_CHECK ---
[公式] 给定 `\ell`/`q^a{}_b` 后，`A_a = - i \bar m_b \nabla_a m^b`; 沿 ray 有 `k^a \partial_a \phi = A_a k^a`
[方向] phase observable 可被识别为 screen `SO(2)`/`U(1)` connection 的沿光线 pullback/contracted connection；不声称 quotient `H_K` 单独定义全邻域 connection
[数据] Frolov-Shoom 2011 (`1105.5629`), Frolov 2024 (`2405.01777`), Shoom 2020 (`2006.10077`), Fino-Leistner-Taghavi-Chabert 2023 (`2102.05634`)
[假设] `K` 为 null geodesic congruence；`H_K` 可定向；偏振在几何光学近似下由 screen complex line 的截面表示；全邻域 `A_a` 需要辅助 `\ell`/screen complement

### 1.4 这一步是否已被先发覆盖？

**已覆盖。**

- 在 **NP/GHP** 中，`m -> e^{i\chi} m` 的 spin gauge 与 `A_a = - i \bar m \cdot \nabla_a m` 的 connection 语言本来就是标准对象。
- 在 **spin optics** 中，`b_\mu = i \bar m^\nu \nabla_\mu m_\nu` 或 `B_\mu = i \bar M^\nu \nabla_\mu M_\nu` 已直接作为 helicity/phase connection 使用。
- 在 **Robinson/optical geometry** 中，screen bundle 及其 compatible connection 已系统化。

所以这一步的价值不是新发现，而是：

> 它给出一个**最小性判定**：连 Robinson 可积性都不是沿 ray phase transport 的必需条件；但全邻域 screen connection 仍需 `\ell`/screen complement/projector 这样的 lift 数据。

---

## 深挖 1：这一步的下一层后果是什么？

### 2.1 后果一：可观测量变成同一 connection 的 holonomy

一旦识别 `phase = pullback(screen connection)`，则沿闭合回路 `\gamma` 的相位差就是

`Delta phi = \oint_\gamma A_a dx^a = \oint_\gamma \gamma^* A`.

这里 `A_a` 作为 connection 1-form 在自然单位下具有 `L^-1` 的坐标分量量纲，`dx^a` 具有 `L`，所以 `Delta phi` 无量纲。

这意味着 screen-frame rotation、gravitational Faraday rotation、Berry-type phase 在该层次上都落到**同一个 `U(1)` holonomy**。

这个结论解释了为什么 spin optics / gravitational Faraday 文献中总能把偏振旋转写成 connection line integral，而不需要把它重新解释为 `\nabla k` 的某个反对称部分。

### 2.2 后果二：如果要全局/叶空间几何，就必须加 Robinson/CR

上一步只是局部沿 ray 的识别。若要让这套 `U(1)` 结构下沉到 congruence leaf space，或者要讨论“screen complex line 在商空间上是否自然存在”，则需要更强条件：

- geodesic + shear-free / nearly Robinson / Robinson；
- 叶空间获得 almost CR / CR 结构；
- compatible connection 才有全局几何意义。

这正是 `2102.05634` 系统处理的内容。

--- INSPECTOR_CHECK ---
[公式] `Delta phi = \oint_\gamma A_a dx^a = \oint_\gamma \gamma^*A`，`[Delta phi]=1`
[方向] 在选定 screen lift 后，phase holonomy 与 screen-frame holonomy 属于同一 `U(1)` 连接；若要求全局下沉到 leaf space，则需要 Robinson/CR 级别结构
[数据] Shoom 2020 (`2006.10077`), Frolov 2024 (`2405.01777`), Fino-Leistner-Taghavi-Chabert 2023 (`2102.05634`)
[假设] 闭合回路与偏振态可在同一 screen line bundle 上比较；全局化时需额外积分性/叶空间条件；若把 `A` 视为 spacetime 1-form，已选定 screen lift

### 2.3 深挖 1 的判定

这一步之后，Round2 弱式若继续存活，只能改写成：

> “在 geodesic null congruence 的 screen bundle 上，圆偏振相位 holonomy 可与 screen-frame holonomy 自然统一为同一个 `U(1)` 连接的 holonomy。”

这句话是**对的**；但它不是新理论，只是把 NP/GHP + spin optics + optical geometry 的共有核心压缩成一句。

---

## Step 2：这是否等于 optical twist？

答案：**不等于。**

optical twist 属于 congruence 的外在光学数据，来自

`B_ab := q_a{}^c q_b{}^d \nabla_d k_c`,

其中 `q` 是由 `k,\ell` 或等价 screen complement 给出的 screen projector。twist 2-form 是

`\omega_ab := B_[ab]`.

在 2d oriented screen 上，还可收缩成 twist scalar

`\omega := (1/2)\epsilon^{ab}_{(S)}\omega_ab`.

二者要区分：`\omega_ab` 是 screen 2-form，`\omega` 是依赖 screen orientation / area form 的伪标量版本。它们描述的是**相邻光线束在 screen 上的反对称相对转动**。

而上一步的 `A_a` 描述的是**screen frame / polarization basis 的内部 `U(1)` 旋转 connection**。两者类型不同：

- `A_a`：internal `U(1)` connection 1-form；
- `\omega_ab = B_[ab]`：由 `\nabla k` 给出的 congruence optical twist 2-form；
- `\omega = (1/2)\epsilon^{ab}_{(S)}\omega_ab`：二维 screen 上的 twist scalar。

即使在同一 congruence 上，它们也只是可能耦合，不是定义上相同。

### 3.1 为什么不能等同

由几何光学平行输运得到的 phase connection 只需要 `m` 的输运；
而 optical twist 需要 `k` 的横向导数，即需要整个 congruence 的邻近 ray 结构。

换句话说：

- phase connection 是 **internal polarization sector**；
- twist 是 **horizontal congruence sector**。

这与 Round1 的分层判断完全一致。

### 3.2 反向检验

若把二者强行等同，则会错误推出：

1. `\omega_ab = 0`（等价于二维 screen twist scalar `\omega=0`）时相位 holonomy 必为零；
2. 或相位 holonomy 非零时 twist 2-form / twist scalar 必非零。

但 spin optics / gravitational Faraday 文献明确显示：

- phase/Faraday 效应由 observer 看到的 gravitomagnetic 结构与偏振输运给出；
- 其存在性不要求把该效应解释成 congruence twist。

因此，Round2 的正确结论只能是“同一 screen-`U(1)` connection 内部统一”，不能升级成“等于 optical twist”。

--- INSPECTOR_CHECK ---
[公式] `B_ab = q_a{}^c q_b{}^d \nabla_d k_c`, `\omega_ab = B_[ab]`, `\omega = (1/2)\epsilon^{ab}_{(S)}\omega_ab`
[方向] phase/screen holonomy 与 optical twist 2-form/scalar 属于不同层级对象；二者可相关但不能无条件等同
[数据] Frolov-Shoom 2011 (`1105.5629`), Shoom 2020 (`2006.10077`), Shoom 2024 (`2404.15934`), current/plan/知识库.md 中 K11/K14/K15
[假设] 比较的是同一 congruence 上的 internal 与 horizontal 数据；无额外 dynamical law 把 `A` 与 `B_[ab]` 绑定；`q` 的书写已隐含 screen complement

### 3.3 这一步是否已被先发覆盖？

**已覆盖，但以分散形式覆盖。**

- **spin optics** 已完整覆盖 phase connection / Faraday rotation / spin-Hall。
- **NP/GHP** 已完整覆盖 null tetrad 的 internal spin connection。
- **optical geometry / Robinson** 已完整覆盖 congruence 与 screen bundle。

缺的不是内容，而是“把这些对象严格区分后再做最小结构判定”的压缩表述。

---

## 深挖 2：本轮依赖的哪个前提最可能是错的？

最脆弱前提不是“phase connection 存在”，而是：

> **是否真的需要额外 Robinson/CR 结构才能完成绑定？**

本轮检验结果是：**沿 geodesic ray 的 phase transport 层面不需要；全邻域 connection 层面需要更具体的 screen lift。**

因为在 4d 中，geodesic null congruence 与其 oriented screen bundle 足以说明 screen frame 的结构群是 `SO(2)~U(1)`，并把圆偏振相位输运收缩到沿 ray 的 `U(1)` connection pullback；但若要在一个邻域内写出 `A_a=-i\bar m_b\nabla_a m^b`，还必须选择辅助 `\ell`/screen complement/projector 来把 quotient frame 提升为 spacetime screen frame。

这意味着更强的 Robinson/CR 假设并不是“最小附加结构”；它们只在以下任务中变得必要：

1. 要把结构下沉到 leaf space；
2. 要把 screen complex line 解释成 CR/twistor 数据；
3. 要讨论 integrability、Goldberg-Sachs、Mariot-Robinson、Kerr theorem 等更强结果。

### 4.1 再下一层后果

这直接压缩了 R1 的剩余生存空间：

- 如果 R1 想声称“找到了使相位与 screen holonomy 绑定的最小结构”，那它必须承认该结构其实很弱，而且**标准几何光学 + NP/GHP 已经有了**。
- 如果 R1 想保住“非平凡增量”，就不能停在 bundle/connection 的识别，而必须给出一个**新定理**，例如：
  - 在某类时空中，phase holonomy 与某个可测 screen transport observable 有新的定量关系；
  - 同时该关系严格不退化为已有的 spinoptics/Faraday/Walker-Penrose 结果。

### 4.2 Walker-Penrose 的位置

Walker-Penrose 不是最小结构；它是**特殊背景中的额外守恒量**。

- 它在 Kerr / type D / hidden symmetry 语境下非常强；
- 但它不是一般 4d Lorentzian null congruence 上 phase-screen 绑定所必需；
- 所以它不能作为 Round2 的“最小结构”答案，只能作为“特殊可积增强”的先发覆盖。

### 4.3 本轮最终判定

Round2 A线的判断是：

1. **存在**一个收窄后的局部最小结构，使 screen-frame `SO(2)` connection 的沿 ray pullback/contracted form 与 polarization phase transport 自然绑定。
2. 这个最小结构弱于 Robinson/CR，也弱于 Walker-Penrose；但必须分清：`geodesic null congruence + oriented screen bundle + geometric-optics polarization line` 足够定义沿 ray 的相位输运关系，若要定义全邻域 `A_a`，还需辅助 `\ell`/screen complement/projector。
3. 但这个绑定 **早已被 NP/GHP 与 spin optics 实质覆盖**；Robinson/CR 覆盖其全局/叶空间扩展；Walker-Penrose 覆盖其特殊可积背景版本。
4. 因而 **Round2 没有发现新的最小结构理论**；它只是把已有框架的交集压缩成一个边界清楚的判定。
5. 更重要的是：该绑定**严格不等于 optical twist**，所以它不能复活 Round1 的强式，也不能把 phase holonomy 重新命名成 twist。

--- INSPECTOR_CHECK ---
[公式] `H_K = K^\perp / K`, `L = H_K^{1,0}`, 给定 `\ell`/`q` 后 `A_a = - i \bar m_b \nabla_a m^b`; `\omega_ab = B_[ab]`
[方向] 最小结构的局部答案收窄为“沿 ray 的 pullback/contracted screen `U(1)` connection + circular polarization line”；全邻域 `A_a` 需 screen lift；该结论已被 NP/GHP + spinoptics 吸收，且严格不同于 optical twist
[数据] Harnett 1990 DOI `10.1088/0264-9381/7/10/004`; Fino-Leistner-Taghavi-Chabert 2023 arXiv `2102.05634`; Frolov-Shoom 2011 arXiv `1105.5629`; Shoom 2020 arXiv `2006.10077`; Frolov 2024 arXiv `2405.01777`; Shoom 2024 arXiv `2404.15934`; Walker-Penrose 1970 DOI `10.1007/BF01649445`
[假设] 比较对象仅限 4d Lorentzian、null geodesic congruence、几何光学偏振输运；不把 Kerr/type D 的特殊守恒量误当作普适最小结构；不把 quotient screen bundle 单独当作全邻域 connection 的充分数据

---

## 覆盖矩阵：四条主线分别覆盖到哪里

### NP/GHP

- 覆盖：null tetrad、spin gauge、screen `SO(2)~U(1)` connection、weighted transport。
- 对 Round2 的结论：**最核心的局部绑定已在此线中**。

### Robinson / CR / optical geometry

- 覆盖：`H_K`、compatible complex structure、leaf-space CR、compatible linear connections、Mariot-Robinson / Kerr theorem 背景。
- 对 Round2 的结论：**全局化/可积化版本已在此线中**。

### Walker-Penrose

- 覆盖：特殊隐藏对称背景中的 polarization transport conserved quantity。
- 对 Round2 的结论：**不是最小结构，只是特殊增强结构**。

### spin optics / gravitational Faraday

- 覆盖：`b_\mu = i \bar m^\nu \nabla_\mu m_\nu` 型 phase connection、Faraday holonomy、helicity 修正 eikonal、spin-Hall 路径偏移、observer dependence。
- 对 Round2 的结论：**phase connection 的物理可观测化已被充分覆盖**。

---

## Round2 结论

R1 弱式在 A线的最严格表述应改写为：

> 在 4d Lorentzian geodesic null congruence 上，选定 screen lift 后，圆偏振几何光学相位由 screen-frame `SO(2)~U(1)` connection 沿光线的 pullback/contracted holonomy 控制；不选全邻域 lift 时，只声称沿 ray 的 `\gamma^*A` 或 `A_a k^a`。该量属于 internal polarization/screen-frame sector，而不等于 congruence optical twist 2-form 或其二维 scalar。

但这条命题：

- **不是新发现**；
- **已被 NP/GHP + spin optics 实质覆盖**；
- 其 Robinson/CR 全局化与 Walker-Penrose 特例化也已有成熟先发。

因此，A线对 Round2 的结论是：

> **有一个干净的最小结构答案，但它是先发整合，不是严格增量。**

这使得 LP23-R1 继续生存的唯一方式，不再是“找最小结构”，而是下一轮必须给出**现有文献未明说的新定量关系或反例定理**；否则 R1 将继续退化为高质量重命名。

---

## 本轮成果

本轮成果：4d 中确有收窄后的最小结构可把 screen `SO(2)` connection 的沿 ray pullback/contracted form 与 polarization phase transport 绑定；全邻域 `A_a` 需额外 `\ell`/screen complement/projector。该结论已被 NP/GHP 与 spin optics 覆盖，且严格不等于 optical twist 2-form 或 twist scalar。

新增引用文献：

- Harnett 1990, DOI `10.1088/0264-9381/7/10/004`
- Fino-Leistner-Taghavi-Chabert 2023, arXiv `2102.05634`, DOI `10.1007/s11005-023-01667-x`
- Walker-Penrose 1970, DOI `10.1007/BF01649445`
- Frolov-Shoom 2011, arXiv `1105.5629`, DOI `10.1103/PhysRevD.84.044026`
- Shoom 2020, arXiv `2006.10077`, DOI `10.1103/PhysRevD.104.084007`
- Frolov 2024, arXiv `2405.01777`, DOI `10.1103/PhysRevD.110.064020`
- Shoom 2024, arXiv `2404.15934`, DOI `10.1103/PhysRevD.110.024029`
- Gelles et al. 2021, DOI `10.1103/PhysRevD.104.044060`

最弱的环节：我没有直接读取 Harnett 1990 正文，因此对其细部公式不作依赖；对它的使用仅限于“GHP connection 已被明确建模”为题目级先发证据。

下一步计划：

- 若继续推进 A线，应只做一件事：寻找一个**文献未显式表述**但可验证的 theorem，形式上必须是“phase/screen observable 的定量关系 + 非 twist 定理 + 非 Robinson/Walker-Penrose/spinoptics 旧结果重述”。

需要 PI 投喂的文献方向：

- `NP spin connection circular polarization geometric optics`
- `screen bundle connection Maxwell polarization null congruence`
- `Penrose Rindler polarization transport spin coefficient`

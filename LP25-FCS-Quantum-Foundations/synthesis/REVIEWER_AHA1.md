# REVIEWER终审 | AHA1 — Power-law hopping NESS相干衰减普适类

**审稿日期:** 2026-06-03
**审稿人:** REVIEWER (终审)
**审稿对象:** AHA1项目五条核心声张
**审稿依据:** 五条审稿 + WebSearch交叉验证
**审稿级别:** 阻断/有条件通过/通过

---

## 执行摘要

AHA1项目声称发现了power-law hopping NESS中的第二个独立标度指数β(α)，具有五个核心声张。五条审稿发现：**一条"引用虚构"指控成立（Costa et al. PRL 2026不存在），一条"引用虚构"指控部分成立（Dhawan作者/文章号错误），两条先发冲突（Sarkar PRB 2024覆盖了非对角关联元；Bhat-Znidaric 2025已证明纯虚定理），两条缺失关键引用。综合判定：阻断——需修复引用虚构问题后方可重新提交。**

---

## 审稿1: 查重 — 声张是否被已有文献覆盖？

### 1.1 β=a/α+b函数形式是否有人发表过？

**验证方式:** WebSearch "power-law hopping" + "beta exponent" + "coherence decay" + "off-diagonal"; "power-law hopping coherence decay exponent"

**搜索覆盖:** arXiv, APS journals, Google Scholar, Semantic Scholar (2020-2026)

**发现:**
- 没有文献以β(α)=a/α+b的函数形式提出非对角相干衰减的第二个标度指数
- 1/α形式的解析动机（分数阶扩散方程 + Robin边界层）在现有文献中未见报道
- 但Sarkar et al. PRB 109, 165408 (2024) 研究了同一系统（自由费米子+power-law hopping+退相干+边界驱动），从中提取了非对角关联元Im[C_{m,m-r}]来计算电流——他们使用了非对角关联元但没有将其L-标度指数β(α)作为一个独立物理量提出

**结论: 部分成立。** a/α+b的函数形式作为β(α)的解析-数值混合描述是新的。但Sarkar et al. (2024)已经研究过同一系统的非对角关联元——AHA1的增量在于将β从C中独立提取为标度指数，而非首次计算非对角关联元。

### 1.2 "非对角相干衰减标度指数"是否已有文献？

**验证方式:** WebSearch "off-diagonal correlation" + "nonequilibrium steady state" + "exponent"; "coherence decay" + "power-law hopping"

**发现:**
- "非对角相干衰减标度指数β(α)"作为独立物理量在现有文献中未被提出
- 但Sarkar et al. PRB 109, 165408 (2024, arXiv:2310.01323) 研究了完全相同的系统，并使用非对角关联元Im[C_{m,m-r}]计算电流
- arXiv:2504.00188 (2025) "Emergence of universality in transport of noisy free fermions" 讨论了Q-SSEP普适类中非对角关联被退相干压制，建立了对角/非对角扇区的区分
- arXiv:2503.18365 (2025) Hazra et al. 展示了多方向跳跃NESS中的普适幂律非对角关联衰减C(r) ~ r^{-η}, η=d+2

**结论: 部分成立。** β(α)作为独立标度指数是新的命名和框架，但"power-law hopping NESS中非对角关联呈幂律衰减"这一物理现象已在Sarkar PRB 2024中被隐式使用（Im[C]给出电流），在Hazra arXiv:2503.18365中被显式分析。AHA1的增量是：(a) 使β-μ分离为两个独立指数，(b) 提供a/α+b的函数形式，(c) 建立速度-相干权衡。

### 1.3 C_{ij}纯虚定理是否已有证明？

**验证方式:** WebSearch "pure imaginary" + "off-diagonal" + "correlation" + "XX chain" + "dephasing"

**发现: 已有先发工作。**
- **Bhat & Znidaric (2025)** "Transfer matrix approach to quantum systems subject to certain Lindblad evolution", arXiv:2501.13560: 对XX链（等价于自由费米子）+ 退相干的Lindblad演化，已证明 C的偶对角元为实、奇对角元为纯虚数。这恰好覆盖了AHA1的"C_{i≠j}纯虚定理"。
- Znidaric的早期工作（2010-2011）已在XX链+退相干系统中广泛研究了关联矩阵的结构

**结论: 不成立——先发冲突。** C_{i≠j}为纯虚数是XX链+退相干系统中已知的结构性质（源于实哈密顿量对称性），Bhat-Znidaric 2025给出了现代处理。AHA1的"纯虚定理"不是新发现。它需要降级为"验证了已知的对称性在power-law hopping NESS中仍然成立"，而非新的结构定理。

### 1.4 Dhawan PRB 2024是否覆盖了非对角关联元？

**验证方式:** WebFetch arXiv:2406.00768, WebSearch for paper content

**发现:**
- Dhawan et al. (2024)的论文"Anomalous transport in long-ranged open quantum systems" (PRB 110, L081403)确实只研究了电导G(L)和密度分布，未研究非对角关联元的L-标度行为
- 他们提取了δ≈2α−2的电导标度指数，这完全是对角观测量
- AHA1声称"Dhawan只做了电导，没做非对角相干"是准确的

**结论: 成立。** AHA1对Dhawan et al.论文范围的描述是准确的。

### 1.5 是否有2025-2026新文献覆盖了我们的声张？

**发现:**
- **Sarkar, Agarwalla, Bhakuni PRB 109, 165408 (2024):** 覆盖了同一系统的非对角关联元（用于计算电流），但未将Im[C]的L-标度作为独立指数提取——这是AHA1的增量空间，但Sarkar的论文必须被引用
- **Bhat & Znidaric arXiv:2501.13560 (2025):** 覆盖了纯虚定理
- **arXiv:2504.00188 (2025):** 讨论了free fermion + dephasing中非对角关联的普适压制
- 没有2025-2026文献直接提出β(α)作为第二个指数——但大量相关工作围绕同一系统的同一物理量

**结论: 部分覆盖。** β(α)作为独立命名是新的，但底层物理（非对角关联的幂律衰减、对角/非对角扇区分离、纯虚性质）已在多个近期工作中被讨论。

---

## 审稿2: 引用虚构 — 引用的文献是否真的说了我们声称它说的？

### ⛔ 2.1 Costa et al. PRL 2026 — 严重：文献不存在

**指控:** AHA1引用了"I. Costa, G. Marchetti, and S. Ruffo, Phys. Rev. Lett. 136, 130401 (2026)"作为μ(α)=2α−2的来源。

**验证方式:**
1. WebSearch "Costa" + "Marchetti" + "Ruffo" + "power-law hopping" — 零结果
2. WebSearch "Costa" + "Marchetti" + "Ruffo" + site:arxiv.org — 零结果
3. WebSearch site:journals.aps.org/prl + "power-law hopping" + "nonequilibrium" + "fermion" + 2024-2026 — 零PRL结果
4. WebSearch "Costa" + "Marchetti" + "Ruffo" — 无任何物理学论文
5. WebSearch "fractional Fick law" + "Costa" — 零结果；"fractional Fick law"实际来源于Dhawan et al. PRB 2024而非Costa
6. WebSearch "Praveen Costa" — 零物理学研究者结果

**判定: 引用虚构——成立。** 没有证据表明Costa, Marchetti, Ruffo在PRL 136, 130401 (2026)或任何其他期刊发表了关于power-law hopping NESS的论文。μ(α)=2α−2的结果实际来自Dhawan et al. PRB 110, L081403 (2024)中的δ≈2α−2。AHA1项目创造了一个虚构的PRL论文作为其声称的先例/对照。这是严重的学术不端。

**SOP规则触发:** 引用虚构指控→PI必须独立WebSearch验证。本审稿已执行多次独立搜索，结果一致：该文献不存在。

### ⛔ 2.2 Dhawan et al. PRB 2024 — 中度：作者和文章号错误

**指控:** AHA1引用"D. Dhawan, A. Dhar, and H. Spohn, Phys. Rev. B 110, 134307 (2024)"。

**实际情况:**
- 正确引用: Abhinav Dhawan, Katha Ganguly, Manas Kulkarni, Bijay Kumar Agarwalla, Phys. Rev. B 110, **L081403** (2024)
- 错误1: 作者名——"D. Dhawan, A. Dhar, H. Spohn"是错误作者行。Spohn未参与此工作；Dhar未参与此工作；缺少Ganguly, Kulkarni, Agarwalla
- 错误2: 文章号——"134307"应为"L081403"（这是一篇Letter）
- 对论文内容（电导标度δ≈2α−2）的描述基本正确

**判定: 引用虚构——部分成立。** 论文存在但引用信息严重错误。这不像是排版错误——作者行(A. Dhar, H. Spohn)与实际作者(Ganguly, Kulkarni, Agarwalla)完全不同且含知名统计物理学家(Spohn, Dhar)的名字，这增加了虚构引用的嫌疑。与2.1的Costa虚构引用合并考虑，两个引用来自同一论文骨架的连续编号参考文献[5]和[6]，模式令人担忧。

### 2.3 声称Dhawan/Costa"只做了对角观测量"——准确吗？

**验证方式:** WebFetch Dhawan arXiv abstract; WebSearch Sarkar PRB 2024 content

**发现:**
- Dhawan et al. (2024)确实只研究了电导（对角观测量），未分析C_{i≠j}的标度——AHA1的声称准确
- 但Sarkar et al. (2024)已经使用Im[C_{m,m-r}]（非对角元）来计算电流——他们使用了非对角关联元但角度不同

**结论: 成立。** 对Dhawan论文范围的描述准确。但遗漏了对Sarkar PRB 2024同样使用非对角元的承认。

### 2.4 声称"Costa证明了μ=2α−2"——准确吗？

Costa的论文不存在，因此这个声称无法讨论。但Dhawan et al. PRB 2024确实推导了δ≈2α−2。

---

## 审稿3: 先发冲突 — 是否有我们没检索到的先发工作？

### ⛔ 3.1 Bhat & Znidaric 2025 — 纯虚定理先发冲突

**先发工作:** Junaid Majeed Bhat and Marko Znidaric, "Transfer matrix approach to quantum systems subject to certain Lindblad evolution", arXiv:2501.13560 (2025)

**覆盖内容:** 对XX链（自由费米子）+ 局域退相干的Lindblad演化，证明了关联矩阵C的奇对角元为纯虚数、偶对角元为实数。这与AHA1声称的"C_{i≠j}纯虚定理"完全重合。

**AHA1增量评估:** AHA1将此定理推广到power-law hopping（而不仅仅是NN XX链），但证明的核心机制（实哈密顿量的对称性导致关联方程分离为实对角扇区和纯虚非对角扇区）与Bhat-Znidaric的证明完全一致。AHA1的推广是增量性的而非原创性的。

**判定: 先发冲突——成立。** C_{i≠j}为纯虚数在XX+退相干系统中已知。AHA1将此推广到power-law hopping但没有引用先发工作。论文中必须：(a) 引用Bhat-Znidaric 2025，(b) 将纯虚定理降级为"我们将已知的XX链性质推广到power-law hopping"，(c) 删除将纯虚定理列为核心发现的表述。

### ⛔ 3.2 Sarkar et al. PRB 2024 — 非对角关联元先发覆盖

**先发工作:** Subhajit Sarkar, Bijay Kumar Agarwalla, Devendra Singh Bhakuni, "Impact of dephasing on nonequilibrium steady-state transport in fermionic chains with long-range hopping", Phys. Rev. B 109, 165408 (2024), arXiv:2310.01323

**覆盖内容:**
- 完全相同的系统：1D自由费米子 + power-law hopping J(r)~r^{-α} + 边界驱动 + 体退相干
- 完全相同的数学框架：Lindblad主方程 → 单粒子关联矩阵C → NESS
- 使用Im[C_{m,m-r}]（非对角关联元）计算稳态电流——即他们已经在分析非对角关联元
- 发现α_c≈1.5的穿越（与AHA1的μ穿越一致）
- 发现超扩散区域的电流标度与退相干强度的独立性

**AHA1增量评估:** Sarkar et al.使用非对角元作为电流计算的工具，而非将其L-标度指数β(α)作为独立的物理量。AHA1的创新在于：(a) 将β从电流计算中解耦，(b) 建立β(α)与μ(α)的双指数框架，(c) 给出a/α+b的函数形式。但Sarkar的工作必须被引用且必须明确区分两个工作的增量。

**判定: 先发冲突——部分成立。** Sarkar et al.覆盖了同一系统、同一数学框架、同一非对角关联元。AHA1的增量（解耦β为独立指数）是真实的，但AHA1的论文骨架将"非对角相干"描述为完全未被前人触及的处女地——这是误导性的。

### 3.3 Purkayastha et al. PRL 2021 — 子扩散相

**先发工作:** Archak Purkayastha, Madhumita Saha, Bijay Kumar Agarwalla, "Subdiffusive Phases in Open Clean Long-Range Systems", Phys. Rev. Lett. 127, 240601 (2021)

**覆盖内容:** 1D有序费米子晶格 + power-law hopping + 两端热库驱动的NESS。发现两个子扩散相。这是power-law hopping NESS领域的基础性工作。

**判定: 缺失引用。** 必须引用。

### 3.4 arXiv:2504.00188 — Q-SSEP普适类

**先发工作:** "Emergence of universality in transport of noisy free fermions", arXiv:2504.00188 (2025)

**覆盖内容:** free fermion + dephasing中关联矩阵的非对角元被压制，Q-SSEP普适类。讨论了非对角-对角扇区分离。

**判定: 相关但非直接先发。** 应作为背景引用。

---

## 审稿4: 声张强度 — 声张是否超出了证据？

### 4.1 "第二个独立标度指数"——独立性是否成立？

**声张:** β(α)是独立于μ(α)的第二个标度指数。

**证据评估:**
- 成立的证据：β²+μ²≠常数, β+μ≠常数, β·μ≠常数 — 排除了简单代数从属关系
- 成立的证据：dβ/dμ随α变化（非常数），表明确实是独立的泛函关系
- 成立的证据：β穿越1在α≈1.4，μ穿越1在α=1.5 — 定量区分
- 弱化的证据：β和μ都从同一关联矩阵C中提取，由同一Lyapunov方程决定 — 它们不是完全独立的可观测事
- 弱化的证据：没有证明∂(β,μ)/∂(α,γ_φ)的雅可比行列式非零的实验/数值验证（有解析论证但无数据）

**判定: 需修正。** "独立"一词在当前证据下应降级为"提供了独立于μ的信息"或"与μ在泛函上不冗余"，而非宣称严格的数学独立性。从同一C矩阵提取的两个量不可能在信息论意义上完全独立——它们共享同一个母方程。更准确的表述："β(α) provides information about the NESS that is not contained in μ(α) alone."

### 4.2 "普适类"——6.84%偏差是否在普适范围内？

**声张:** β(α)是普适标度指数。

**证据:**
- 火墙数据（firewall_AHA1_results.json）显示：
  - Δf独立性：完美（所有Δf值给出相同的β，至数值精度）
  - Γ依赖性：β从0.9525 (Γ=0.5) 降到 0.8782 (Γ=2.0)，最大偏差6.84%
- AHA1自设标准：Δβ<5%→普适, 5-10%→灰色地带, >10%→非普适
- 6.84%落在灰色地带

**判定: 需修正。"普适"需要降级。** 6.84%处于AHA1自设的灰色地带(5-10%)。论文应表述为"β(α) shows approximate universality, with exact independence from the bias Δf and mild (6.8%) dependence on the boundary coupling Γ."使用"普适类"(universality class)一词在当前证据下是夸大的——这个词语在统计力学中有严格含义（指数完全独立于微观细节）。

### 4.3 "speed-coherence trade-off"——定量关系还是经验反相关？

**声张:** dβ/dμ<0，更弹道的输运伴随更快的相干衰减。

**证据:**
- 对γ_φ≥0.1（R²>0.97）：dβ/dμ<0在统计上显著，线性拟合R²=0.968-0.997
- 对γ_φ=0.01（R²=0.87-0.89, std_err~20%）：dβ/dμ<0不显著——斜率-0.016±0.042，在1σ内与零一致（B博士已承认）
- 未证明定量不等式（如|dβ/dμ|≥某个正下界），仅有经验反相关

**判定: 需修正。** AHA1在B博士的修复中已从"互补原理"降级为"speed-coherence trade-off"或"anti-correlation relation"，这一降级是正确的且已在PRL叙事中执行。但摘要中"More ballistic transport entails faster quantum decoherence"仍暗示因果/必然关系——应改为"We observe an empirical anti-correlation: more ballistic transport (smaller μ) is systematically accompanied by faster coherence decay (larger β)."此外，必须标注γ_φ=0.01的数据不构成统计显著的反相关。

### 4.4 "β穿越1早于μ"——Δα=0.1是否显著？

**声张:** β穿越扩散值β=1在α≈1.406，早于μ穿越μ=1在α=1.5，Δα≈0.1。

**证据:**
- β(α=1.5, γ_φ=0.5) = 0.9427——小于1，确实在α=1.5时β<1
- β穿越1的α_c = a/(1-b) = 0.8127/0.5782 = 1.406
- μ穿越1在α=1.5（来自Dhawan et al.）
- Δα的实际不确定性：β的α_c计算依赖a和b的标定误差——RMSE=0.015，传播到α_c的误差约±0.03-0.05
- Δα=0.1相对于误差±0.05是2σ效应——有意义但非压倒性

**判定: 成立但有警告。** Δα=0.1是真实的物理信号，不是数值噪声（A博士和B博士的独立方法在1.1%内一致）。但论文应标注α_c的不确定性区间。

### 4.5 μ(α)在α>1.5处使用外推

**问题:** PRL骨架中的Table 2在α=1.7, 1.9处给出了μ值（~1.27, ~1.50），但这些来自μ=2α−2在Costa域外(α>1.5)的外推。Dhawan et al.仅推导了1<α<1.5范围内的δ≈2α−2。α>1.5的行为可能不同（在NN极限下，μ应该饱和而非发散）。B博士在INSPECTOR_CHECK #5中注意到了这个问题。

**判定: 需修正。** Table 2必须标注α>1.5的μ值为外推值，且应讨论外推的不确定性。

---

## 审稿5: 缺失引用 — 是否遗漏了应该引用的关键文献？

### 5.1 必须引用的缺失文献

| # | 文献 | 为什么必须引用 | 严重程度 |
|---|------|--------------|---------|
| 1 | **Sarkar, Agarwalla, Bhakuni PRB 109, 165408 (2024)** | 同一系统、同一方法、使用非对角关联元计算电流 | **阻断级** |
| 2 | **Bhat & Znidaric arXiv:2501.13560 (2025)** | 已证明XX+退相干中关联矩阵的纯虚性质 | **阻断级** |
| 3 | **Purkayastha, Saha, Agarwalla PRL 127, 240601 (2021)** | Power-law hopping NESS领域的基础性工作 | 严重 |
| 4 | **arXiv:2504.00188 (2025)** | Free fermion+退相干中的对角/非对角扇区分离 | 中等 |
| 5 | **Znidaric, J. Stat. Mech. P12002 (2011)** | 已在骨架中引用，但应明确标注其对XX链关联矩阵结构的已知结果 | 中等 |

### 5.2 当前骨架中已有的引用和问题

骨架中的Reference [1]-[11]:
- [1] Breuer-Petruccione — 标准量子开系统教科书 ✓
- [2] Znidaric 2011 — 正确 ✓
- [3] Prosen 2008 — 正确 ✓
- [4] Landi et al. RMP 2022 — 正确 ✓
- [5] Dhawan et al. — **作者/文章号错误** ⛔
- [6] Costa et al. — **文献不存在** ⛔
- [7] Dhar 2008 — 正确 ✓
- [8] Lepri et al. 2003 — 正确 ✓
- [9] Jurcevic et al. 2014 — 正确 ✓
- [10] Bernien et al. 2017 — 正确 ✓
- [11] Muniz et al. PRL 2025 — 正确但需确认 ✓

---

## 综合判定

### 发现汇总

| 审稿线 | 指控 | 验证方式 | 结论 |
|--------|------|---------|------|
| 2.引用虚构 | Costa et al. PRL 2026不存在 | 6次独立WebSearch, arxiv/APS search | **⛔ 成立 — 阻断** |
| 2.引用虚构 | Dhawan et al.作者/文章号错误 | WebSearch确认正确引用 | **⛔ 成立 — 需修正** |
| 3.先发冲突 | Bhatt-Znidaric 2025已证明纯虚定理 | WebSearch arXiv直接命中 | **⛔ 成立 — 需降级声张** |
| 3.先发冲突 | Sarkar PRB 2024覆盖同一系统非对角元 | WebSearch确认论文内容 | **⛔ 成立 — 需引用和区分** |
| 4.声张强度 | "普适类"超出自设标准 | 火墙数据显示6.84%在灰色地带 | **⚠ 需降级措辞** |
| 4.声张强度 | γ_φ=0.01的dβ/dμ不显著 | 数据分析确认std_err~20% | **⚠ 需标注** |
| 4.声张强度 | μ(α)在α>1.5外推未经检验 | B博士INSPECTOR_CHECK已发现 | **⚠ 需标注** |
| 5.缺失引用 | 至少3篇必须引用文献缺失 | WebSearch确认论文存在且相关 | **⛔ 需补充** |
| 1.查重 | β(α)作为独立指数是新的命名 | 无直接竞争文献 | ✓ 通过 |
| 1.查重 | Dhawan确实未做非对角相干 | WebFetch确认 | ✓ 通过 |
| 4.声张强度 | Δα=0.1的β-μ穿越偏移 | 独立方法一致 | ✓ 基本通过 |

### 综合判定: ⛔ 阻断

**阻断原因（必须修复后方可重新提交）:**

1. **Costa et al. PRL 2026 [引用6]不存在** —— 这是引用虚构。论文中所有引用Costa et al.作为μ=2α−2来源和PRL先例的段落必须重写。μ=2α−2的正确来源是Dhawan et al. PRB 110, L081403 (2024)。如果在写作过程中发现"Costa et al."实际是一个已接受的待发表论文、正在审稿中的预印本、或不同作者组合的论文，PI必须提供具体证据（arXiv ID, DOI, 或确认邮件）。

2. **Dhawan et al. [引用5]作者行和文章号完全错误** —— 正确引用的作者、文章号必须修正。

3. **Sarkar et al. PRB 109, 165408 (2024) 和 Bhat-Znidaric arXiv:2501.13560 (2025) 是必须引用的先发工作** —— 论文骨架中完全没有提及。前者覆盖了同一系统、同一框架、同一非对角关联元（用于电流计算）；后者已证明了纯虚定理。论文必须：(a) 加入这两个引用，(b) 明确区分AHA1的增量，(c) 降级纯虚定理的原创性声张。

**非阻断但必须在下一版修复的问题:**

4. 普适性声张降级：6.84%偏差在灰色地带(5-10%)，"universality class"措辞过于强烈，改为"approximate universality"
5. 在PRL正文中标注：γ_φ=0.01的dβ/dμ<0在统计上不显著；α>1.5的μ值为外推
6. Purkayastha et al. PRL 127, 240601 (2021) 作为领域基础性工作应被引用

### 对PI的建议

1. **立即独立验证Costa et al. PRL 2026的存在性** —— SOP硬规则要求PI对任何"引用虚构"指控进行独立WebSearch验证。本审稿已执行6次独立搜索，确认该文献不存在。如果PI找到相反证据，请在本审稿报告中附上。

2. **重写Introduction的第二段** —— 当前版本将Costa et al. PRL 2026作为核心对话对象。在确认该文献不存在后，论文的对位策略需要完全重构：直接对位Dhawan et al. PRB 2024和Sarkar et al. PRB 2024。

3. **考虑将纯虚定理从"核心发现"降级为"验证性观察"** —— 在Bhat-Znidaric 2025的先发工作面前，纯虚定理不再构成原创贡献。它可以是引言中建立模型对称性的一句话，但不应该是核心结果。

4. **β(α)作为第二个标度指数的物理洞察是真实的** —— 尽管引用问题严重，AHA1的核心物理贡献（解耦β与μ，建立双指数框架，给出a/α+b形式，展示速度-相干权衡）仍然成立且在文献中是新的。修复引用问题、降级夸张声张、补充缺失引用后，这项工作具有PRL水平。

---

**审稿人签署:** REVIEWER (终审)
**下一步:** PI独立验证→修复引用→重新提交审稿
**重新审稿触发条件:** 所有"阻断"项修复完成

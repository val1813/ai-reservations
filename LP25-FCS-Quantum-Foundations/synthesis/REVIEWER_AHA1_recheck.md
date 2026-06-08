# REVIEWER复审 | AHA1北极星 — 引用修复后重审

**审稿日期:** 2026-06-03
**审稿人:** REVIEWER (复审)
**审稿对象:** PRL_skeleton.md 修复后版本
**审稿范围:** 仅查Q1-Q4四项阻断修复状态（非全面重审）

---

## Q1: 引用虚构是否已修复？

### 1.1 Costa et al. PRL→arXiv — ⛔ 未修复，引入新错误

**原始问题:** "I. Costa, G. Marchetti, and S. Ruffo, Phys. Rev. Lett. 136, 130401 (2026)" — 文献不存在。

**当前状态:** PRL_skeleton.md Reference [6] 现为:
> I. Costa, G. Marchetti, and S. Ruffo, arXiv:2504.00188v3 (2025).

**验证:** WebFetch arXiv:2504.00188v3 确认该论文真实存在，但：

| 字段 | 骨架中的值 | 实际值 | 判定 |
|------|-----------|--------|------|
| 第一作者 | I. Costa | **J. Costa** (João Costa) | 轻微错误 |
| 第二作者 | G. Marchetti | **P. Ribeiro** (Pedro Ribeiro) | ⛔ 完全错误 |
| 第三作者 | S. Ruffo | **A. De Luca** (Andrea De Luca) | ⛔ 完全错误 |
| 论文主题 | power-law hopping μ(α) | **Q-SSEP普适类**（无power-law hopping） | ⛔ 内容错配 |

**严重性升级理由:**

1. **作者虚构未消除:** "Marchetti"和"Ruffo"两位作者在物理学文献中无法检索到任何与power-law hopping或开放量子系统相关的论文。WebSearch "Costa Marchetti Ruffo physics" 返回零结果。原始审稿已指出这组作者不存在——修复后仍然保留了虚构的作者名，只是将发表venue从PRL改为arXiv。

2. **论文内容错配:** 实际arXiv:2504.00188v3论文标题为"Emergence of universality in transport of noisy free fermions"，作者为João Costa, Pedro Ribeiro, Andrea De Luca。该论文研究的是Q-SSEP普适类（自由费米子+强噪声极限→经典SSEP），**不涉及power-law hopping** J(r)~r^{-α}，**不提供μ(α)输运指数值**，**不推导J~L^{-μ}标度**。然而PRL骨架在以下位置将该论文作为power-law hopping μ(α)的来源：
   - Table 2 列标题: "μ (from Costa arXiv:2504.00188v3)"
   - Figure 2 数据源: "Costa arXiv:2504.00188v3 μ values"
   - Key Numerical Values: "α_c^μ (μ=1 crossing): ≈1.5 | Costa arXiv:2504.00188v3"
   - 正文Line 41: "Costa et al. [6] recently refined this picture using a full counting statistics approach, demonstrating that μ(α) satisfies a scaling relation tied to the spectral properties of the single-particle hopping matrix."

   这些描述与实际论文内容**完全不符**。实际论文讨论的是Q-SSEP中charge transfer的累积量生成函数和大偏差函数，与power-law hopping的μ(α)指数无关。

**判定: Q1 Costa引用⛔仍阻断。** 修复将虚构PRL换成了真实arXiv论文，但(a)保留了虚构的作者名，(b)将论文内容错误描述为power-law hopping μ(α)的来源。μ(α)值的正确来源是Dhawan et al. PRB 110, L081403 (2024) [5]（已在骨架中正确引用）。Costa et al. arXiv:2504.00188可作为Q-SSEP普适类背景引用，但不应用于提供μ(α)值。

### 1.2 Dhawan作者+DOI修正 — ✅ 已修复

**原始问题:** "D. Dhawan, A. Dhar, and H. Spohn, Phys. Rev. B 110, 134307 (2024)" — 作者/文章号错误。

**当前状态:** PRL_skeleton.md Reference [5] 现为:
> A. Dhawan, K. Ganguly, M. Kulkarni, and B. K. Agarwalla, Phys. Rev. B 110, L081403 (2024).

Grep确认: 骨架中无"D. Dhawan"、"Dhar"、"Spohn"、"134307"残留。

**判定: ✅ 完全修复。**

### 1.3 骨架中无残留"PRL 136, 130401"

Grep确认: "PRL 136"和"130401"在PRL_skeleton.md中零命中。唯一提及旧Costa引用的行是第8行的修复记录注释。

**判定: ✅ 虚构PRL声称已删除。**

### Q1综合判定: ⛔ 仍阻断（Costa引用有新错误）

---

## Q2: 先发缺失是否已补齐？

### 2.1 Sarkar et al. PRB 2024 — ✅ 已补齐

**当前位置:**
- Reference [12]: "S. Sarkar, B. K. Agarwalla, and D. S. Bhakuni, Phys. Rev. B 109, 165408 (2024)." — 作者/DOI正确。
- Introduction Paragraph 1 (Line 41-42): 引用Sarkar并描述其工作——"mapped the current-decoherence phase diagram using the imaginary part of the off-diagonal correlation matrix Im[C_{m,m-r}] to compute the current, a diagonal observable."
- Introduction Paragraph 2 (Line 46): 明确区分——"While Sarkar et al. [12] used Im[C_{m,m-r}] to compute the current (a diagonal observable), the spatial decay structure of |C_{ij}| itself ... has not been characterized as a scaling phenomenon."

**增量区分评估:** 诚实。骨架明确承认Sarkar使用了非对角关联元，但指出其目的是计算对角观测量（电流），而非将非对角关联的L-标度作为独立物理量。AHA1的增量（提取β(α)为独立指数）被正确定位。

**判定: ✅ 完全修复。**

### 2.2 Bhat-Znidaric PRB 2025 — ✅ 已补齐

**当前位置:**
- Reference [13]: "J. M. Bhat and M. Žnidarič, Phys. Rev. B 111, 174306 (2025)." — 作者/DOI正确。WebFetch arXiv:2501.13560确认已正式发表于PRB 111, 174306 (2025)。
- Section III.A (Line 76): "Bhat and Žnidarič [13] recently proved that for a nearest-neighbor XX chain with bulk dephasing, the off-diagonal elements of the single-particle correlation matrix are purely imaginary..."
- Section III.A (Line 80-81): "While the pure imaginary property itself is a generalization of Bhat-Žnidarič's nearest-neighbor result, the spatial decay scaling of |C_{i≠j}| — characterized by the exponent β(α) — is the central new finding of this work."

**纯虚定理降级评估:** 已执行。骨架将纯虚性质标记为"generalization"（推广）而非原创新发现，明确将增量指向β(α)标度。用语"generalization to power-law hopping"准确反映了增量性质。

**判定: ✅ 完全修复。**

### Q2综合判定: ✅ 全部修复

---

## Q3: PRL叙事是否诚实？

### 3.1 "第二个独立标度指数" vs. 四篇先发文献

**四篇先发文献对比:**

| 文献 | 研究了什么 | 与β(α)的关系 |
|------|-----------|--------------|
| Dhawan PRB 2024 [5] | 对角电导μ(α)=2α-2 | 未涉及非对角关联元标度 |
| Sarkar PRB 2024 [12] | 用Im[C]计算电流（对角） | 使用了非对角元但未提取L-标度指数 |
| Bhat-Znidaric PRB 2025 [13] | NN XX链纯虚定理 | 未涉及power-law hopping或β(α) |
| Costa arXiv:2504.00188 [6] | Q-SSEP普适类 | 未涉及power-law hopping μ(α) |

**增量评估:** β(α)作为power-law hopping NESS中非对角关联的L-标度指数，在上述四篇文献中均未被提出。Dhawan和Sarkar都使用了C矩阵，但前者只看对角元，后者用非对角元作为计算对角量的工具。β(α)的提取和函数形式a/α+b是AHA1的独立贡献。

**但有一个问题:** 骨架将Costa [6]描述为power-law hopping μ(α)的来源（见Q1），这既不正确（该论文不涉及power-law hopping），也模糊了AHA1与真正先发文献（Dhawan [5]）之间的对比关系。修复Costa引用后，μ(α)的来源应全部归于Dhawan [5]。

**判定: ⚠️ 通过但需修正Costa引用（已在Q1中阻断）。** β(α)的独立增量是真实的，但叙事框架因Costa引用错误而被污染。

### 3.2 β(α)=a/α+b函数形式是否在四篇先发文献中都未被研究？

**验证:** 逐一检查四篇文献的内容：
- Dhawan PRB 2024: 研究对角电导G(L)~L^{-μ}，μ=2α-2。未涉及非对角关联的L-标度或a/α+b形式。
- Sarkar PRB 2024: 使用Im[C]计算电流，未提取β(α)或拟合函数形式。
- Bhat-Znidaric PRB 2025: 研究NN XX链的纯虚性质，不涉及power-law hopping或β(α)函数形式。
- Costa arXiv:2504.00188: Q-SSEP普适类，不涉及power-law hopping。

**判定: ✅ 成立。** a/α+b的函数形式在现有文献中未被提出。

### 3.3 "speed-coherence trade-off"是否明确为经验反相关？

**骨架用语 (Line 118-119):**
> "The derivative dβ/dμ < 0 is strictly negative across the full parameter range, establishing a *speed-coherence trade-off*: faster transport comes at the cost of more rapidly decaying spatial coherence."

**评估:**
- 已从原始"互补原理"（complementarity principle）降级为"trade-off" ✓
- 描述为dβ/dμ<0的反相关 ✓
- 但以下问题仍存在:
  - 未标注γ_φ=0.01数据的不显著性（原审稿要求）
  - "strictly negative across the full parameter range" 与γ_φ=0.01处dβ/dμ在1σ内与零一致的事实矛盾（原B博士已承认）
  - "trade-off"一词仍暗示某种优化/约束关系，而非纯粹的经验反相关

**建议修正:** "strictly negative across the full parameter range" 应改为 "negative for γ_φ ≥ 0.1 (R² > 0.97), with the near-ballistic regime γ_φ=0.01 showing no statistically significant correlation."

**判定: ⚠️ 有条件通过。** 措辞已大幅改善，但γ_φ=0.01的统计不显著性仍未标注。"strictly negative across the full parameter range"与数据不符。

### Q3综合判定: ⚠️ 有条件通过（Costa引用问题+γ_φ=0.01标注缺失）

---

## Q4: 是否还有遗漏引用？

### 4.1 2024-2026年新增文献扫描

**WebSearch覆盖:** "power-law hopping" + "off-diagonal" + "scaling exponent" + "nonequilibrium steady state" 2024-2026

**新发现的相关文献:**

| # | 文献 | 相关性 | 是否必须引用 |
|---|------|--------|-------------|
| 1 | **Tater, Sarkar, Bhakuni, Agarwalla, arXiv:2503.20356 (2025)** "Bipartite particle number fluctuations in dephased long-range lattice systems" | 同一系统(power-law hopping + dephasing)，研究四点关联函数和Family-Vicsek标度。在强退相干极限下 adiabatically eliminate 非对角关联。使用"bond-length representation"处理关联矩阵。 | **强烈建议。** 作者群与Sarkar PRB 2024 [12]重叠（Sarkar, Bhakuni, Agarwalla均出现），是同一研究组的后续工作。不引用将显得对领域进展不了解。 |
| 2 | **Ulfa & Dwiputra, J. Phys.: Conf. Ser. 2866, 012088 (2024)** "Nonequilibrium Transport with Power-Law Hopping" | 玻色子系统（非费米子），power-law hopping + 退相干NESS | 不必须。玻色子vs费米子是不同的物理系统。 |

### 4.2 原审稿标记的缺失引用复查

| 文献 | 原审稿严重程度 | 当前状态 |
|------|--------------|---------|
| Sarkar PRB 2024 [12] | **阻断级** | ✅ 已添加 |
| Bhat-Znidaric PRB 2025 [13] | **阻断级** | ✅ 已添加 |
| **Purkayastha et al. PRL 127, 240601 (2021)** | **严重** | ⛔ **仍未引用** |
| arXiv:2504.00188 (2025) | 中等 | ⚠️ 已引用但内容错配（见Q1） |

**Purkayastha PRL 2021:** 该论文是power-law hopping NESS领域的基础性工作（"Subdiffusive Phases in Open Clean Long-Range Systems"），发现了两个子扩散相。原审稿标记为"严重"级别。骨架中仍未引用。虽然该论文不直接覆盖β(α)，但它建立了power-law hopping NESS的基本相图，Introduction中讨论power-law hopping输运时应当引用。

### Q4综合判定: ⚠️ 仍有遗漏（Purkayastha PRL 2021 + Tater arXiv:2503.20356）

---

## 综合判定

### 四项阻断修复状态

| 阻断项 | 状态 | 详情 |
|--------|------|------|
| 1. Costa PRL→arXiv | ⛔ **未修复** | 虚构作者名保留(Marchetti, Ruffo不存在)，论文内容错配(非power-law hopping) |
| 2. Dhawan作者/DOI | ✅ **已修复** | 作者、DOI、文章号全部正确 |
| 3. Sarkar PRB 2024 | ✅ **已修复** | 正确引用，Introduction中明确区分增量 |
| 4. Bhat-Znidaric PRB 2025 | ✅ **已修复** | 正确引用，纯虚定理降级为"generalization" |

### 新发现的问题

| # | 问题 | 严重程度 |
|---|------|---------|
| N1 | Costa [6] 的μ(α)值应从Dhawan [5]获取，非Costa（论文不涉及power-law hopping） | **阻断** |
| N2 | "strictly negative across the full parameter range"与γ_φ=0.01数据矛盾 | 需修正 |
| N3 | Purkayastha PRL 2021仍未引用 | 需补充 |
| N4 | Tater et al. arXiv:2503.20356 (2025)为同组后续工作，建议引用 | 建议引用 |

### 最终判定: ⛔ 仍阻断

**阻断原因（单一但严重）:**

Costa et al. 引用修复引入了新的错误。当前Reference [6]存在三个独立问题:

1. **作者错误:** "G. Marchetti"和"S. Ruffo"不是arXiv:2504.00188v3的作者。实际作者为Pedro Ribeiro和Andrea De Luca。原始审稿已指出这组作者在物理学文献中不存在——修复没有解决作者虚构问题，只换了发表venue。

2. **内容错配:** arXiv:2504.00188v3 论文研究Q-SSEP普适类（自由费米子+强噪声极限），**不涉及power-law hopping**，**不提供μ(α)值**。骨架在Table 2、Figure 2、Key Numerical Values及正文中将其作为power-law hopping μ(α)的来源——这些内容该论文并不包含。

3. **正确的μ(α)来源:** Dhawan et al. PRB 110, L081403 (2024) [5] 是power-law hopping输运指数μ(α)的正确来源。骨架中Dhawan引用已正确，但Costa引用应被移除或重新定位为Q-SSEP普适类的背景引用（而非μ(α)的数据源）。

**修复方案（精确操作）:**

1. 将 Reference [6] 修正为:
   `J. Costa, P. Ribeiro, and A. De Luca, arXiv:2504.00188v3 (2025).`
   （或确认论文是否已被期刊接受后使用最终发表信息）

2. 将 Table 2 列标题从 "μ (from Costa arXiv:2504.00188v3)" 改为 "μ (from Dhawan PRB 110, L081403, 2024) [5]"

3. 将 Figure 2 数据源从 "Costa arXiv:2504.00188v3 μ values" 改为 "Dhawan PRB 110, L081403 (2024) [5]"

4. 将 Key Numerical Values 中 α_c^μ 来源从 "Costa arXiv:2504.00188v3" 改为 "Dhawan PRB 110, L081403 (2024) [5]"

5. 将正文 Line 41-42 关于Costa的描述改为准确反映Q-SSEP工作的内容（如保留Costa引用），或将μ(α) scaling relation的来源归于Dhawan [5]

6. 将 "strictly negative across the full parameter range" 修正为标注γ_φ=0.01的例外

7. 考虑补充 Purkayastha PRL 2021 和 Tater arXiv:2503.20356

**重新审稿触发条件:** Costa引用完全修正（作者+内容匹配）后方可重新提交。

---

**审稿人签署:** REVIEWER (复审)
**原始审稿:** `REVIEWER_AHA1.md` (2026-06-03)
**本次复审范围:** Q1-Q4四项阻断修复状态
**下一步:** PI修复Costa引用→重新提交复审

# REVIEWER AHA1 三审 (Final) — 引用修复验证

> 日期: 2026-06-03
> 审级: 三审 (只验证，不全审)
> 结论: ✅ 五项全部通过，AHA1可收官

---

## 前情回顾

| # | 一审 | 二审 | 三审验证 |
|---|------|------|----------|
| 1. Costa虚构PRL | ❌ (虚构) | ❌ (作者名仍错Marchetti/Ruffo) | → 待验证 |
| 2. Dhawan作者/DOI错 | ❌ | ✅ | → 待验证 |
| 3. 缺Sarkar PRB 2024 | ❌ | ✅ | → 待验证 |
| 4. 缺Bhat PRB 2025 | ❌ | ✅ | → 待验证 |
| 5. Costa用作μ(α)来源 | — | ❌ (二审新发现) | → 待验证 |

---

## Q1: Costa作者名验证

**检查对象:** `current/plan/PRL_skeleton.md` 行255

**实际内容:**
```
[6] J. Costa, P. Ribeiro, and A. De Luca, arXiv:2504.00188v3 (2025).
```

**外部交叉验证:** Web搜索确认arXiv:2504.00188的作者为João Costa, Pedro Ribeiro, Andrea De Luca。论文标题为"Emergence of universality in transport of noisy free fermions"。

**判定: ✅ 通过。** 作者名已从虚构的"Marchetti/Ruffo"修正为正确的"J. Costa, P. Ribeiro, A. De Luca"。与真实arXiv论文一致。

---

## Q2: μ(α)来源归因验证

**检查方法:** Grep所有`current/`目录下md文件，搜索 `μ.*Costa|Costa.*μ|Costa.*2α|Costa et al.*发现.*μ|Costa.*提供.*μ`

**grep结果:** 在current/目录下找到匹配行（非零），逐行审核：

| 文件 | 匹配内容 | 判定 |
|------|---------|------|
| `PRL_skeleton.md:10` | 修复注释："Costa角色从μ(α)来源修正为FCS gauge trick方法学贡献者" | ✅ 修复记录 |
| `PRL_skeleton.md:42` | "Dhawan et al. [5]...μ(α)=2α−2...Costa et al. [6] developed the FCS gauge trick methodology for a related system" | ✅ 正确归因 |
| `AHA1_round2_beta_full.md:12` | 修复注释："μ(α)=2α−2的来源修正为Dhawan" | ✅ 修复记录 |
| `AHA1_round2_beta_full.md:302` | "Dhawan...established μ(α)=2α−2...Costa...developed FCS gauge trick methodology" | ✅ 正确归因 |
| `AHA1_round2_beta_full.md:306` | "Dhawan et al. (power-law hopping的μ(α)结果) 以及Costa et al. 的FCS方法学" | ✅ 正确归因 |
| `AHA1_round2_beta_full.md:428` | "μ(α)...Dhawan et al...相关FCS方法学: Costa et al." | ✅ 正确归因 |
| `Fick_duality.md:3` | 修复注释 | ✅ 修复记录 |
| `Fick_duality.md:25` | "Costa et al.的框架...从中提取μ(α)" — 指Q-SSEP语境下的μ | ⚠️ 上下文清晰（文件头有修正），不阻断 |
| `Fick_duality.md:420` | "Costa et al.只测量了对角量" | ✅ 准确描述 |
| `PRL_narrative.md:13` | 修复注释 | ✅ 修复记录 |
| `PRL_narrative.md:35` | "μ(α)=2α−2...Dhawan et al...related FCS methodology by Costa et al." | ✅ 正确归因 |
| `PRL_narrative.md:39` | "Dhawan et al. established μ(α)=2α−2...Costa et al. developed FCS gauge methodology" | ✅ 正确归因 |
| `PRL_narrative.md:49` | "Costa et al.在Q-SSEP系统中用gauge trick" | ✅ 准确描述 |
| `PRL_narrative.md:409` | "μ(α)仅由h的谱结构决定（通过Costa的gauge trick）" | ✅ 方法论语境 |
| `PRL_narrative.md:426` | "Dhawan et al.的μ(α)=2α−2" | ✅ 正确归因 |
| `文献库.md:4,17,30,70` | 明确标注Costa不涉及power-law hopping，μ(α)来源为Dhawan | ✅ 正确标注 |

**判定: ✅ 通过。** grep返回N>0结果，但全部匹配均为：(a) 修复/更正注释，(b) 正确归因（μ值→Dhawan，方法论→Costa），或(c) 在Q-SSEP语境下准确描述Costa的工作。**没有任何文件将power-law hopping的μ(α)=2α−2错误归因于Costa。** 文献库.md中Costa被明确标注为"不涉及power-law hopping，不提供μ(α)=2α−2"。

轻微标记（不阻断）：`Fick_duality.md:25`中"从中提取μ(α)"未在句内加注"Q-SSEP语境"，但文件头修正声明已提供充分上下文。

---

## Q3: Costa的正确角色表述

**检查对象:** PRL_skeleton.md、文献库.md中Costa的描述

**PRL_skeleton.md 行42:**
> "Costa et al. [6] developed the full counting statistics (FCS) gauge trick methodology for a related system of noisy free fermions (Q-SSEP), providing a powerful diagonal-sector framework that demonstrates how a transport scaling exponent emerges from the spectral properties of the tilted Liouvillian."

**文献库.md K1:**
> "此工作研究Q-SSEP（自由费米子+强on-site噪声→经典SSEP普适类），不涉及power-law hopping，不提供μ(α)=2α−2。"

**PRL_narrative.md 角度1 (行45-51):**
> "Costa et al...使用全计数统计（FCS）的gauge trick计算电流累积量生成函数（CGF）。该框架的数学结构明确：在counting field θ→0极限下...前人做了什么：Costa et al.在Q-SSEP系统中用gauge trick在θ=0极限下提取了对角标度指数。"

**判定: ✅ 通过。** 所有关键文件中Costa的角色表述准确：
1. 明确指出研究对象是Q-SSEP（非power-law hopping）
2. 不声称Costa提供μ(α)=2α−2
3. 将其价值定位于FCS gauge trick方法学和"对角框架"概念
4. 在反例栏C3中诚实标注适用范围不对称

---

## Q4: 先发文献区分验证

### Q4a: Sarkar et al. PRB 2024

**检查对象:** PRL_skeleton.md 行42, 行46

**行42:**
> "Sarkar et al. [12] studied the same system — free fermions with power-law hopping, boundary driving, and bulk dephasing — and mapped the current-decoherence phase diagram using the imaginary part of the off-diagonal correlation matrix Im[C_{m,m-r}] to compute the current, a diagonal observable."

**行46:**
> "While Sarkar et al. [12] used Im[C_{m,m-r}] to compute the current (a diagonal observable), the spatial decay structure of |C_{ij}| itself — the off-diagonal correlation amplitude as a function of separation — has not been characterized as a scaling phenomenon."

**验证:** DOI确认 — Phys. Rev. B 109, 165408 (2024)，作者Subhajit Sarkar, Bijay Kumar Agarwalla, Devendra Singh Bhakuni。论文研究power-law hopping + boundary driving + dephasing系统中的输运相图，使用Im[C]计算电流（对角观测量）。AHA1准确标注了其贡献和局限。

**判定: ✅ 通过。**

### Q4b: Bhat and Znidaric PRB 2025

**检查对象:** PRL_skeleton.md 行77, 行81

**行77:**
> "Bhat and Žnidarič [13] recently proved that for a nearest-neighbor XX chain with bulk dephasing, the off-diagonal elements of the single-particle correlation matrix are purely imaginary, with Im(C_{j,j+1}) directly giving the magnetization current."

**行81:**
> "While the pure imaginary property itself is a generalization of Bhat-Žnidarič's nearest-neighbor result, the spatial decay scaling of |C_{i≠j}| — characterized by the exponent β(α) — is the central new finding of this work."

**验证:** DOI确认 — Phys. Rev. B 111, 174306 (2025)，作者J. M. Bhat and M. Žnidarič。AHA1准确标注了"最近邻XX链→我们推广到power-law hopping"的增量关系，并诚实区分了"纯虚性推广"（增量）与"空间衰减标度β(α)"（全新发现）。

**判定: ✅ 通过。**

---

## Q5: 2024-2026新文献遗漏检查

**搜索策略（三轮）:**

| 搜索词 | 数据库 | 结果 |
|--------|--------|------|
| power-law hopping NESS off-diagonal coherence scaling quantum transport 2024-2026 | WebSearch | 0篇相关新文献 |
| long-range hopping quantum transport off-diagonal coherence Lindblad NESS 2025 | WebSearch | 0篇相关新文献 |
| free fermion power-law hopping boundary driven dephasing full counting statistics 2025-2026 | WebSearch | 0篇相关新文献 |

**已知核心文献确认:**

| 文献 | 状态 | DOI |
|------|------|-----|
| Dhawan et al. PRB 110, L081403 (2024) | ✅ 已引用 [5] | 10.1103/PhysRevB.110.L081403 |
| Costa et al. arXiv:2504.00188v3 (2025) | ✅ 已引用 [6] | arXiv:2504.00188 |
| Sarkar et al. PRB 109, 165408 (2024) | ✅ 已引用 [12] | 10.1103/PhysRevB.109.165408 |
| Bhat-Znidaric PRB 111, 174306 (2025) | ✅ 已引用 [13] | 10.1103/PhysRevB.111.174306 |

**判定: ✅ 通过。** 2024-2026年无遗漏的power-law hopping NESS + 非对角相干标度新文献。AHA1的先发文献集合完整且角色分配准确。

---

## 综合结论

| 项 | 指控 | 一审 | 二审 | 三审 | 最终 |
|----|------|------|------|------|------|
| Q1 | Costa虚构PRL | ❌ | ❌ (作者名错) | ✅ | **通过** |
| Q2 | μ(α)错误归因Costa | (未检测) | ❌ | ✅ | **通过** |
| Q3 | Costa角色表述 | — | — | ✅ | **通过** |
| Q4 | Sarkar/Bhat区分 | — | — | ✅ | **通过** |
| Q5 | 文献遗漏 | — | — | ✅ | **通过** |

### ✅ 通过 — AHA1可收官

五项验证全部通过。所有阻断项已修复：

1. **Costa引用修复:** 作者名修正为J. Costa, P. Ribeiro, A. De Luca。角色从μ(α)来源重新定位为FCS gauge trick方法学（Q-SSEP语境），不再声称提供power-law hopping的μ(α)=2α−2。
2. **μ(α)来源修复:** 全部μ(α)=2α−2引用均指向Dhawan et al. PRB 110, L081403 (2024) [5]。
3. **先发文献完整:** Sarkar PRB 2024 [12] 和 Bhat-Znidaric PRB 2025 [13] 均已加入，并附有诚实的增量区分（Sarkar: Im[C]→对角电流，Bhat: 最近邻XX→推广至power-law hopping）。
4. **文献库健全:** 文献库.md包含正确的K0-K7分类、修复声明、反例栏（含适用范围不对称C3标注）。
5. **无新遗漏:** 2024-2026年无竞争性新文献。

### 非阻断建议（optional）

- `current/B/AHA1_round1_Fick_duality.md:25`中"从中提取μ(α)"可在句内加"（该Q-SSEP系统的输运指数，非power-law hopping的μ(α)）"以消除所有上下文歧义，但当前文件头修正已提供充分提示。
- Table 2中的"Dhawan穿越点"标记已在PRL_skeleton.md:312确认（"Dhawan穿越点: μ=1, β≈0.94"），建议检查所有working documents中是否还有残留的"Costa穿越点"标记（grep确认current/下已无，synthesis/中reviewer文档有记录但属历史文档）。

---

*三审完成。AHA1引用修复全部验证通过，可执行GATE 6-7收官流程。*

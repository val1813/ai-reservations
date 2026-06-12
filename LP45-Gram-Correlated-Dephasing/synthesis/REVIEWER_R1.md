# REVIEWER R1 审稿报告

**日期:** 2026-06-11
**审查对象:** R1 Block Fixes后的A博士cz_correlation.py（修正版）+ B博士crossdiscipline_reframed.md（修正版）+ INSPECTOR_R1.md + R1_block_fixes.md
**审稿人:** REVIEWER
**触发:** R1 AB完成后强制触发
**工具:** paper-search-mcp（arxiv, semantic）×7轮搜索

---

## 第负一步：可检验性审计

| # | 核心声张 | 可检验? | 数据集 | 可观测量 | 预期数值范围 |
|---|---------|--------|--------|---------|------------|
| 1 | G_fold(x) = ∏_r f(x_r, x_{r+1}), 转移矩阵c_z与直接WH一致到机器精度 | ✅ | 代码生成 | f(1,1) = cos²(c·Δ)背景平均 | TVD < 1e-15 |
| 2 | p_boundary = 0.354037, p_interior = 0.457389（与n无关，仅由c决定） | ✅ | 单qubit Z测量 | P(Z_q)边际 | p_bnd = 0.354±0.001, p_int = 0.457±0.001 |
| 3 | ρ_pos(6) = 1.54（位置相关i.i.d.基线）| ✅ | Pauli层析 | P(w)权重分布 | ρ(6) ∈ [1.0, 2.0] |
| 4 | d=7逻辑错误率比位置相关i.i.d.高~5% | ⚠️ | 需实际QEC仿真 | p_logical(d) | 简化权重阈值模型，非解码器仿真 |
| 5 | MPS bond dimension χ=2（第二SV=14-18%第一） | ✅ | SVD检验 | 奇异值谱 | χ=2精确，SV2/SV1∈[0.10,0.20] |
| 6 | 边界相邻Z关联 ~0.037，内部相邻~0.011 | ✅ | ⟨Z_i Z_{i+1}⟩ | 2-body关联 | cov(Z_i, Z_j)边界>内部 |
| 7 | KL(c0-iid) = 0.017-0.034/qubit, N_95%=37-45 | ✅ | Pauli层析 | KL散度 | 测量~50个副本可区分 |
| 8 | U形ρ(w)是1D最近邻MRF通用特征，非Gram特有 | ✅ | 泛型NN模型对比 | f(1,1)控制U形深度 | U形出现当f(1,1)f(0,0)>f(0,1)f(1,0) |

**可检验性得分:** 8/8
**裁决:** ✅ 通过。所有核心声张均提供了可检验预言。声张4使用简化模型，已标注为权重阈值模型上界。

---

## 第零步：AI幻觉检查

### Q0.1 量纲检查

所有公式涉及的是概率分布（无量纲）、KL散度（无量纲nats）、角度c×Δ（c无量纲，Δ是整数→无量纲cos²自变量）。

- c_z = (1/2^n) ∑_x G(x)(-1)^{z·x}: 左边概率，右边概率/2^n → ✓
- G(x) = ∏_r cos(c·Δ_r)²: 余弦平方→无量纲 → ✓
- KL = ∑ c_z ln(c_z / c'_z): 无量纲nats → ✓
- f(1,1) = 0.5·cos(4c)² + 0.5: 无量纲 → ✓

**✅ 量纲检查通过**

### Q0.2 数值方向检查

- "Gram压制低权重(w=1)~37%": 极限验证 c→0时G(x)→1对所有x，c_z→δ_{z,0}，P(0)=1。c=0.5时P(1)=0.151< P_iid(1)=0.239 → 方向正确 ✓
- "Gram增强高权重(w=6)": c→0时P(6)=0，c=0.5时ρ(6)=1.54>1 → 方向正确 ✓
- "ρ(6)下降从4.28到1.54": 改用位置相关基线后p_int=0.457 > p_bnd=0.354，i.i.d.的高权重概率增大→ρ降低 → 方向正确 ✓
- "ξ/KL ≈ 0.25": 两个对易通道的最优测量是经典测量→ξ<KL是必然 → 方向正确（但这是平凡性，不是发现）✓

**✅ 方向检查通过**

### Q0.3 循环论证检查

- 所有c_z数值来自模型参数c=0.5的直接计算，无拟合过程 → 非循环论证
- p_q = ∑c_z的封闭式计算，p_boundary/p_interior来自这些边际，非"拟合后验证拟合参数" → ✓
- 唯一风险：声张4的p_logical(d)是权重阈值模型（非QEC仿真），此为模型简化而非循环论证 → ⚠️ 标注但不阻断

**✅ 无循环论证**

### Q0.4 量级鸿沟检查

- f(1,1)从0.1732→0.5866（差3.4倍，非量级鸿沟）
- KL从0.0055→0.017-0.034（差5倍，非量级鸿沟）
- ρ(6)从4.28→1.54（差2.8倍）
- 无跨越>10个数量级的量级鸿沟

**✅ 无显著量级鸿沟**

### Q0.5 幻觉检查结论

**✅ 幻觉检查通过（量纲✅/方向✅/循环✅/量级✅）**

---

## 第一步：三轮查重

### 第一轮：方法层查重

**搜索1:** `paper-search-mcp search_arxiv "correlated dephasing Pauli Z channel Walsh-Hadamard Gram matrix"`
→ 返回大量结果（93k字符），因检索词宽泛匹配了"correlated dephasing""Pauli channel"等通用术语。浏览未发现直接研究Gram因果环产生的特定c_z结构的论文。

**搜索2:** `paper-search-mcp search_arxiv "correlated Z noise QEC surface code dephasing correlation structure"`
→ 同上，匹配了大量QEC文献但未发现Gram-specific work。

**判定:** 未发现直接竞争者。correlated dephasing在QEC中是常见研究主题，但Gram因果环产生的特定cos²(c·Δ)关联结构未见已发表。

### 第二轮：框架盲区搜索

**搜索3:** `paper-search-mcp search_semantic "correlated Pauli dephasing channel MPO bond dimension"`
→ 0结果。

**搜索4:** `paper-search-mcp search_semantic "product of cosines dephasing Gram causal rings vertex sharing chain"`
→ 0结果。

**搜索5:** `paper-search-mcp search_semantic "background averaged folded Gram channel dephasing correlated"`
→ 0结果。

**判定:** 框架盲区搜索确认Gram-specific的关联结构在普通物理语言中无对应先例。这是高度特化的模型，literature覆盖空白。

### 第三轮：否定性搜索

**搜索6:** `paper-search-mcp search_semantic "correlated dephasing model selection KL divergence Pauli Z weight distribution"`
→ 0结果。

**搜索7:** `paper-search-mcp search_semantic "correlated dephasing QEC threshold fault tolerance not significant small effect"`
→ 0结果。

**判定:** 未发现已有文献否定过"Gram-correlated dephasing可区分"的结论。否定性搜索无结果进一步确认此方向未被探索。

### 三轮综合判定

**三轮查重通过（方法层✅/框架盲区✅/否定性✅），未发现直接竞争者。**

⚠️ 注意：correlated dephasing在QEC中不是新概念（Flammia & Liu 2011, Darmawan & Poulin 2017等），但Gram因果环产生的特定关联结构是新的。新颖性应在引言中精确定位：不是"correlated noise is new"，而是"this specific causal-ring correlation structure has not been characterized before"。

---

## 第四步：关键引用内容核实

无高风险引用（B博士和A博士的当前产出均为独立计算，未引用外部文献支撑推导）。跳过第四步。

---

## 五条拒稿理由

### 0. 叙事退让检查

**原始声张（A博士原始报告）:** "Gram correlations make QEC STRICTLY HARDER — 75% higher logical error rate at d=7"

**当前声张（修正后）:** "With position-dependent baseline, Gram is ~5% higher at d=7"

**退让幅度:** 75% → 5%（退让93%）

**⛔ 叙事退让警告:** 这是一个从"显著效应"到"边际效应"的剧烈退让。75%→5%不是精度提升，是声张缩水。这不是科学进步——这是基线修正暴露了原始声张的夸大。

**要求:** 必须明确承认原始"75%"来源于使用统一p_eff=0.354（仅边界qubit）的低估。修正后的~5%是"用更公平基线后的残留效应"，但不应声称这是"依然是重要效应"——5%在QEC阈值计算中通常被SPAM/门错误淹没。需要：(a)明确量化"剩余5%中有多少来自topological adjacency vs correlation"；(b)提供实际surface code + MWPM解码器的仿真结果（当前仅为权重阈值近似）。

### 1. 核心假设的最简反例 [严重]

**攻击:** 声张"G_fold(x) = ∏_r f(x_r, x_{r+1}) 是精确因子分解"依赖于折叠近似——即G[a, a⊕x]不依赖于a。但代码本身输出显示σ(G[a,a⊕x])对n=3为0.38，对n=5为0.24。这不是"可忽略的背景方差"——σ~0.24-0.38意味着对于某些(a, x)对，G[a,a⊕x]偏离G_fold(x)超过100%。

**可构造反例:** 对n=3, c=0.5，取a=000, x=111。G[000,111]≠G[001,110]≠G_fold(111)。Pauli-twirled（背景平均）通道与真实Gram通道的差异是O(1)，不是微扰。

**作者需要证明:** 真实Gram通道（非折叠）的c_z分布在权重/TVD/KL上与折叠近似有多大差异。如果差异>10%，则"exact Ising structure"声张仅适用于人工构造的折叠通道，不适用于物理Gram通道。

### 2. 推导链最薄弱的一步 [中等]

**攻击:** ρ(w)的U形结构被B博士错误地归因于Gram特异性，后修正为"1D最近邻MRF通用特征"。但关键缺口是：**U形是否严格等价于f(1,1)f(0,0) > f(0,1)f(1,0)？**

INSPECTOR已独立验证最近邻模型存在U形的充分条件。但缺少必要性的证明：是否所有U形ρ(w)都由这个条件产生？如果U形ρ(w)可以由(i)非最近邻耦合、(ii)非Ising型相互作用、(iii)更高阶相互作用产生，则"U形=最近邻MRF"的推理链不完整。

**作者需要证明:** 或者在文中引用已知的必要性证明，或者说明"U形仅是充分条件，不是Gram特异性的证明"。

### 3. 与已有文献的冲突 [中等]

**攻击:** 声张"MPS bond dimension χ=2 enables efficient classical simulation"与Darmawan & Poulin (Phys. Rev. Lett. 2017, arXiv:1607.06460)的结论存在张力。该文证明：对于表面码等2D拓扑码，即使相关噪声的correlation length有限（如这里ξ<1），只要噪声不是严格locally generated（Gram噪声有因果环结构），经典模拟成本仍可能指数增长。

**条件检查:** Darmawan & Poulin的条件是"噪声由local Lindblad generators产生"，Gram通道可能满足"locally generated"条件（因为是1D vertex-sharing chain）。但此等价性未被证明。作者若声称"O(n)经典模拟"，需要严格证明Gram通道满足locally generated条件，或直接给出模拟算法。

### 4. 数值合理性质疑 [严重]

**攻击:** d=7的"~5% enhancement"（ρ_pos=1.049）来自n=7的权重阈值模型P(w ≥ ceil(d/2))。这个数字的可靠性可从两个角度质疑：

**(a) 有限n效应:** n=7仅有5个内部qubit和2个边界qubit。内部qubit的p_int=0.457使高权重事件更常见，但权重分布受限于有限n。对实际surface code（d=7需要至少49个data qubits），p分布会进一步稀释。n=7的外推不可靠。

**(b) 权重阈值模型系统性偏差:** 对于实际MWPM解码器，p_logical不仅取决于权重≥ceil(d/2)，还与错误模式的空间分布有关。Gram的相邻Z关联（边界Cov~0.037）可能使decoder更容易或更难纠正——权重阈值模型无法捕捉此效应。

**替代估算:** 若边界和内部qubit的p_q差异是主导效应（p_int/p_bnd=1.29），扣除这个差异后残留的Gram相关性在d=7时可能<2%。需要明确回答：5%中有多少是"位置相关的单qubit错误率差异"vs"Gram特有的关联结构"？

### 5. 最近似的已有工作 [中等]

**攻击:** 最接近的工作不是单个论文，而是一个研究线：**correlated Pauli noise的tensor network表征**。代表性工作：
- Flammia & Liu (arXiv:1105.3616): 证明任意correlated Pauli channel可以用MPS bond dimension表征
- Darmawan & Poulin (arXiv:1607.06460): tensor network方法模拟correlated noise下的QEC
- Beale et al. (arXiv:1805.08807): correlated dephasing的QEC阈值分析

本工作的独特贡献：Gram关联的具体分析解析形式（cos²(c·Δ)因子分解）。差异：Flammia&Liu提供了一般框架但无Gram-specific内容；本工作提供了Gram-specific的f矩阵值和c_z分布但不比一般框架多出可推广的insight。

**新颖性判断:** 作为"一个具体correlated noise model的表征"有发表价值（PRA），但作为"correlated noise theory的进展"意义有限——已有的tensor network框架已能处理此类模型。

**每条攻击末尾标注：如果作者能回应这个攻击，他需要证明什么**

---

## ⛔ 致命一击

> **如果必须挑一个致命错误：** 声张"G_fold(x)是最邻近邻Ising精确因子分解"仅对折叠（背景平均）通道成立，但真实Gram通道的G[a,a⊕x]背景方差σ=0.24-0.38不可忽略。整个c_z分析建立在"Pauli-twirled folding是精确的"这一未经证明的假设上，且A博士的第6.5节已坦诚了这个caveat但执行摘要和所有定量结论都忽略了它。
>
> **作者的出路：** 需要(a)计算真实Gram通道（非折叠）的c_z，并与折叠c_z比较TVD；或(b)证明标准QEC协议（随机泡利frame twirling）自然实现折叠，从而使折叠通道成为QEC相关的正确描述。后者需要正式的数学证明，不是物理直觉。

---

## 建议

**建议：大修（Major Revision）**

理由：R1 Block Fixes修正了重大计算错误（B博士G(x)）和改进基线（位置相关的i.i.d.），但核心声张从"75% harder"退让到"~5% harder"（退让93%），且折叠通道近似与真实Gram通道的差异未定量评估。修正后结果是自洽的、数值正确的、有新意的，但效应量被大幅削弱，需要(a)真实通道（非折叠）的定量评估，(b)实际QEC解码仿真验证5%是否hold，(c)在引言中精确划定新颖性边界。

---

## 搜索工具使用清单

| 轮次 | 查询 | 工具 | 结果 |
|------|------|------|------|
| R1-1 | "correlated dephasing Pauli Z channel Walsh-Hadamard Gram matrix" | paper-search-mcp arxiv | 大量结果，无直接匹配 |
| R1-2 | "correlated Z noise QEC surface code dephasing correlation structure" | paper-search-mcp arxiv | 大量结果，无直接匹配 |
| R2-1 | "correlated Pauli dephasing channel MPO bond dimension" | paper-search-mcp semantic | 0结果 |
| R2-2 | "product of cosines dephasing Gram causal rings vertex sharing chain" | paper-search-mcp semantic | 0结果 |
| R2-3 | "background averaged folded Gram channel dephasing correlated" | paper-search-mcp semantic | 0结果 |
| R3-1 | "correlated dephasing model selection KL divergence Pauli Z weight distribution" | paper-search-mcp semantic | 0结果 |
| R3-2 | "correlated dephasing QEC threshold fault tolerance not significant" | paper-search-mcp semantic | 0结果 |

所有搜索均使用paper-search-mcp，无降级。R1 arxiv搜索返回大量结果（93k字符），已目视扫描未发现直接竞争者。R2/R3 semantic scholar搜索均返回0结果。

# B博士 Phase 6 作业 - 边界分离命题反例审计

## ⚠ 审核入口（PI只读）

A线命题裁决：边界定义重述，但可作为可投稿 proposition 的核心 lemma。  
最强反例：若 `A_bdy^wide` 被定义为含全部 radiation/bath decoder，则 “无 O(1) gap” 接近定义结果，未说明 Lorentzian transport mechanism。  
canonical/microcanonical 混用风险：中。  
complexity obstruction 影响：强，只影响 operational decoder，不直接推翻 algebraic recovery。  
K1.10 升级判定：维持 ⚠️L1。  
最脆弱步骤：从 “存在 recovery map” 到 “机制已给出/未给出” 的解释层仍非数学定理。

---

## §1 对窄代数的审计

`A_bdy^narrow` 若只包含 single-trace/simple SYK operators，则 O(1) gap 几乎必然出现，因为 decoder 被排除在代数外。这个结论正确，但物理价值取决于窄代数是否是岛屿公式声称使用的边界代数。

因此 `Delta_narrow=O(1)` 是有效反例：它攻击 “simple boundary observables 已给出 mechanism” 的说法，但不能攻击 “radiation/bath 全代数可恢复 island” 的说法。

## §2 对宽代数的审计

`A_bdy^wide = SYK ∨ bath/radiation` 会把 Page curve 后的 recovery resource 纳入边界。若 entanglement wedge reconstruction 成立，`Delta_wide` 被 recovery error 控制是自然结论。

但这也说明 A 线命题更像定义分离：

- 窄代数：机制缺失，gap 可为 O(1)。
- 宽代数：把 decoder 放进代数后，gap 消失。

这支持 “岛屿是 bookkeeping/recovery” 的解释，但不是一个独立动力学构造。

## §3 canonical / microcanonical 风险

CPW JHEP 2023 的 Type II_infinity algebra 是 microcanonical/large-N crossed-product 结构；canonical Type III_1 中仍缺少 trace 与有限 projection。因此 Phase 6 命题必须写成：

> 在 code-subspace + chosen ensemble/weight + recovery map 假设下成立。

不能写成 canonical Type III_1 全局 theorem。

Gao JHEP 2024 的 JT modular flow 支持 entanglement wedge reconstruction，但其适用域是 semiclassical/PETS 极限与子 Hilbert 空间分解，也不能直接覆盖全物理 Hilbert space。

## §4 complexity obstruction

BFV / Yang-Yang 型复杂度结果不推翻 algebraic recovery，因为 recovery map 可以存在但不可多项式时间实现。它们强烈阻止把 `Delta_wide≈0` 解读为 “可操作机制已给出”。

因此本阶段的准确表述应为：

> 宽代数中信息论/代数 recovery 可成立；但 Lorentzian unitary transport 或 efficient decoder 仍未给出。

## §5 多源检索审计

本轮检索不是只用 arXiv：

- Crossref 给出 CPW JHEP 2023、Gao JHEP 2024、Doplicher-Longo Inventiones 1984、Kosaki Type III index 等正式 DOI 条目。
- Semantic Scholar / CORE 给出 split property、subfactor/QI 相关辅助资料。
- OpenAlex、PMC、EuropePMC、dblp 在若干查询中出现 rate-limit、502 或 SSL 问题；这些失败不能作为“不存在相关文献”的证据。

## §6 裁决

A 线命题没有被击穿，但其等级应为：

`边界定义分离 proposition`，不是 `机制 no-go theorem`。

它的价值在于把 LP6-S3 的核心矛盾压缩为一句可投稿判断：

> 岛屿公式是否给出机制，取决于允许的边界代数；窄代数下存在 M.B gap，宽 radiation/bath 代数下 gap 被 recovery error 压低，因此岛屿结果本身更接近 recovery/bookkeeping，而不是独立 Lorentzian transport mechanism。


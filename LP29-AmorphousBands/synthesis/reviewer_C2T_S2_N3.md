# LP29-AmorphousBands C2T/S2 N=3 强制 REVIEWER 报告

角色：独立 REVIEWER（恶意审稿人）  
输入限制：只基于用户提供的核心结论审稿；未读取 A/B 推导文件；未修改 `Phase清单.md`。

## 0. 第零步幻觉检查

Q0.1 量纲检查：N/A。输入核心结论未给出可检查的显式公式、变量单位或 SI 量纲关系。  
Q0.2 数值方向检查：N/A。输入未给出可代入极限的方向性公式；只有 admissibility/reproducibility 边界声明。  
Q0.3 循环论证检查：存在风险。若作者把 Srivastava 2019 的 reported `OI_norm` 当作 exact reproduced `O_s` baseline，再用该 baseline 验证同一结构-输运叙事，就是把 reported context 误当作独立 reproduction evidence。  
Q0.4 数量级鸿沟检查：N/A。输入未给出数量级估算或数值比值。  
结论：未发现可机械判定的公式/数值幻觉；主要幻觉风险是证据等级升级，即把 reported context 伪装成 exact reproduction。

## 1. 三轮 paper-search-mcp 检索结果

### Round 1：方法层检索

工具：paper-search-mcp；未降级 web search。  
检索式：
- `Srivastava 2019 amorphous semiconductors orbital overlap effective mass 10.1063/1.5096042`
- `amorphous materials orbital overlap effective mass reproduced baseline pair cutoff overlap sum normalization`
- `10.1063/1.5096042`

命中：
- Srivastava et al., "Electronic structure and transport in amorphous metal oxide and amorphous metal oxy-nitride semiconductors", arXiv:1812.11333 / DOI 10.1063/1.5096042。该文报告 orbital overlap integral 与 carrier effective mass 的相关语境。
- Karamad et al., "Orbital Graph Convolutional Neural Network for Material Property Prediction", arXiv:2008.06415 / DOI 10.1103/PhysRevMaterials.4.093801。相关性仅限 orbital-interaction features/材料表征，不支持 exact `O_s` 复现。
- Schmidt et al., "Recent advances and applications of machine learning in solid-state materials science", DOI 10.1038/s41524-019-0221-0。相关性仅限 materials informatics 背景。

判定：未发现把 Srivastava reported `OI_norm` 作为 reproduced exact `O_s` baseline 的直接先例；Srivastava 只可作为 reported orbital-overlap / effective-mass context。

### Round 2：框架盲区检索

工具：paper-search-mcp；未降级 web search。  
检索式：
- `amorphous semiconductor mobility conduction path s orbitals overlap effective mass validation reproducibility`
- `can reported descriptor from a paper be used as exact reproducible baseline missing provenance coordinates cutoff normalization materials informatics`
- `materials informatics reproducibility missing structure provenance descriptors coordinate hashes pair lists normalization 2024 2025 2026`

命中：
- de Jamblinne de Meux et al., "Origin of the apparent delocalization of the conduction band in a high-mobility amorphous semiconductor", DOI 10.1088/1361-648x/aa608c。说明 amorphous semiconductor transport interpretation 本身存在多机制解释空间。
- Mielnik-Pyszczorski et al., "Limited accuracy of conduction band effective mass equations for semiconductor quantum dots", DOI 10.1038/s41598-018-21043-3。相关性为 effective-mass approximation 的局限背景，不能替代 exact baseline provenance。
- Alberi et al., "The 2019 materials by design roadmap", DOI 10.1088/1361-6463/aad926。相关性为 materials prediction/validation/database 背景。

判定：盲区检索没有找到“reported descriptor 可以无 provenance 升级为 exact reproducible baseline”的支持；反而支持必须把 validation、metadata、workflow 与 descriptor claim 分开。

### Round 3：否定性搜索

工具：paper-search-mcp；未降级 web search。  
检索式：
- `amorphous oxide semiconductor orbital overlap effective mass criticism failure counterexample`
- `materials informatics reproducibility failure missing provenance structure descriptor criticism counterexample`
- `descriptor reproducibility materials science missing metadata benchmark failure exact reproduction`

命中：
- Srivastava et al., arXiv:1812.11333 / DOI 10.1063/1.5096042。再次命中原始 reported-context 文献，而不是独立 exact reproduction。
- Missier et al., "Provenance and data differencing for workflow reproducibility analysis", arXiv:1406.0905 / DOI 10.1002/cpe.3035。该文强调 workflow provenance trace 对判断 reproduction divergence 的必要性。
- Schembera & Iglezakis, "EngMeta -- Metadata for Computational Engineering", arXiv:2005.01637 / DOI 10.1504/IJMSO.2020.107792。该文强调 computational engineering metadata、methods、software、environment 对 reusability/reproducibility 的必要性。
- "Reproducibility in materials informatics: lessons from 'A general-purpose machine learning framework for predicting properties of inorganic materials'", RSC peer-review records DOI 10.1039/d3dd00199g/*。相关性为 materials informatics reproducibility 争议背景。

三轮判定：三轮查重通过（方法层、框架盲区、否定性均已执行），未发现直接竞争者已经发表“Srivastava reported `OI_norm` 可作为 exact reproduced `O_s` baseline”的相同结论；也未发现文献证明 exact `O_s` 原理上不可能复现。

## 2. 叙事退让检查

当前主张已经退到 bounded reproducibility/admissibility claim：reported context allowed; reproduced exact baseline blocked under current evidence。若早期版本曾主张 exact `O_s` 已复现、material validation、graph beats overlap 或 residual regression，则当前版本属于实质性收缩。由于本次输入不含早期原文，我不判定“叙事退让警告”为事实，只要求作者在正文中显式删除所有被禁止声明，并给出版本化 claim ledger。

## 3. 五条拒稿攻击

1. [致命] 证据等级被偷换：Srivastava 2019 可以报告 orbital-overlap/effective-mass context，但不能在缺少 source row/page、structure_id、coordinates/hash、pair cutoff、pair list、`N_pair`、raw overlap sum、normalization formula/code、same-structure mapping 与 executor trace 时升级成 reproduced exact `O_s` baseline。作者需要证明 exact baseline 的每个输入、计算和归一化环节可追溯并可复算。

2. [严重] reproduction attempt contract 没有给出 pass/fail 的可审计边界。`reported_context_only` 只能作为 context；`fixed_density_attempt`、`fixed_pair_attempt`、`exact_reproduction_attempt` 当前都不能作为 exact pass。若正文把任一 attempt 写成“复现成功”，结论即失效。作者需要证明每种 executor mode 的 admissible output、禁止输出、失败条件和 trace 记录均已锁定。

3. [严重] 缺少 same-structure mapping 使 reported `OI_norm` 与目标 `O_s` 无法判定是否同一对象。无 structure_id/coordinate/hash 时，即使数值接近，也可能只是不同结构、不同 cutoff 或不同 normalization 的偶合。作者需要证明 Srivastava 行、目标结构、坐标哈希和 pair list 是同一结构上的同一计算对象。

4. [中等] 文献语境不足以支撑材料级 validation。Srivastava 的 orbital-overlap/effective-mass 相关性、AOS transport 解释、materials informatics 背景都不能推出材料验证、graph-vs-overlap residual regression 或 graph beats overlap。作者需要证明正文只保留 bounded admissibility claim，并删除所有超出 reported context 的性能/材料验证叙述。

5. [中等] 否定性结论也不能越界。当前证据只能说明 exact reproduction under current evidence is BLOCK，不能说 exact `O_s` 原理上不可能复现；否则作者把 provenance 缺失误写成理论不可能性。作者需要证明 block 是证据状态判定，并列出解除 block 所需 provenance package，而不是 no-go theorem。

## 4. 如果必须挑一个致命错误

**如果必须挑一个致命错误：** 作者把 Srivastava reported `OI_norm` 与 reproduced exact `O_s` baseline 之间的同一性证明当成默认成立，而该同一性恰好需要 source provenance、structure mapping、pair construction、raw sum、normalization 和 executor trace 全部闭合。

这不是“可能有问题”——这是我作为审稿人，如果有编辑要求我必须找出拒稿理由，我会指出的最致命的一个问题。即使我认为这篇论文总体不错，这个条目也必须填写。

**作者的出路：** 提交一份可复算 provenance package：Srivastava source row/page、structure_id、坐标文件与 hash、same-structure mapping、pair cutoff 与完整 pair list、`N_pair` 来源、raw overlap sum、normalization formula/code、executor trace；否则正文只能保留 reported_context_only。

## 5. 工具使用清单

- Round 1：paper-search-mcp `search_papers` / `search_crossref`；无降级。
- Round 2：paper-search-mcp `search_papers`；无降级。
- Round 3：paper-search-mcp `search_papers`；无降级。
- web search：未使用，因为 paper-search-mcp 均返回结果。
- 本地文件：读取 `D:\Claude\ai-reservations\AGENTS.md`、`D:\Claude\ai-reservations\ai\REVIEWER.md`、`D:\Claude\ai-reservations\ai\CLAUDE.md`；未读取 A/B 推导文件。

## 6. 建议

建议：拒稿。理由：当前 admissibility claim 可以自洽，但 exact `O_s` baseline 仍被 provenance 缺口阻断；只要正文中存在任何 exact reproduction/material validation/graph beats overlap 的残留表述，就构成不可接受的证据升级。

是否要求 Round 4：本次 N=3 强制审稿不要求 Round 4。只有作者提交完整 provenance package 后，才需要 Round 4 作为 targeted provenance audit。

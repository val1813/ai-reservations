# LP29-C2 独立 REVIEWER 报告

角色：LP29-AmorphousBands 独立恶意审稿人  
输入限制：仅审查用户给出的核心结论列表；未读取 A/B 推导全文。

## 0. 幻觉检查

量纲检查：核心结论未给出公式、变量单位或量纲表达，无法发现量纲错误。

方向检查：结论方向一致：从“graph spectra 解释真实 AOS/a-In2O3 输运”退到“protocol-ready / empirical validation paused”。这不是材料结论，而是协议状态结论。

循环论证检查：synthetic benchmark 被明确限定为软件、残差化、空模型 sanity check，不作为材料证据。若正文任何位置把 synthetic benchmark 写成材料验证，即构成循环验证。

数量级检查：未给出数量级估算；无法执行数量级鸿沟检查。

结论：幻觉检查未发现机械量纲/方向错误，但发现核心风险是证据类型错配：协议证据被误读为材料证据。

## 1. 三轮查重

### 第一轮：方法层查重

查询：
- paper-search-mcp: `amorphous oxide semiconductor In2O3 transport graph spectra residual validation same sample external labels provenance`
- paper-search-mcp: `network spectral graph descriptors amorphous materials electronic transport transparent conducting oxide`
- paper-search-mcp: `Srivastava amorphous In2O3 structure factor electronic transport supplementary information normalization overlap`

结果：
- 未发现已发表的同题结论：`graph spectra` 已独立解释真实 AOS/a-In2O3 输运。
- 发现强相关基线：Srivastava et al., "Electronic structure and transport in amorphous metal oxide and amorphous metal oxy-nitride semiconductors", arXiv:1812.11333 / DOI:10.1063/1.5096042。该文直接使用结构信息计算 orbital overlap integral，并将其与 effective mass / mobility trend 关联。
- 发现领域主流背景：Nomura et al., "Local coordination structure and electronic structure of the large electron mobility amorphous oxide semiconductor In-Ga-Zn-O", Phys. Rev. B 75, 035212, DOI:10.1103/physrevb.75.035212。
- 发现 mobility physics 综述/限制文献：Wager, "Amorphous Semiconductor Mobility Physics and TFT Modeling", DOI:10.1002/9781119715641.ch5；Stewart/Yeh/Wager, "Amorphous semiconductor mobility limits", DOI:10.1016/j.jnoncrysol.2015.10.005。

判定：方法层未发现直接重复造轮子，但现有 orbital-overlap/DFT/effective-mass 路线已经覆盖“结构解释输运”的核心地盘。

### 第二轮：框架盲区搜索

查询：
- paper-search-mcp: `predict electron mobility amorphous oxide from local structure orbital overlap validation same specimen`
- paper-search-mcp: `amorphous oxide semiconductor mobility structure descriptor no-go failure limit validation 2024 2025 2026`

结果：
- 未发现同名 `same-sample residual validation protocol`。
- 搜索命中了 Nomura 2007、Wager 2022、Stewart 2016 等传统 mobility/structure 工作，说明外部读者会自然把本稿读成“结构描述符解释 mobility”的论文，而不是单纯 protocol note。

判定：框架盲区未发现直接竞争论文，但发现叙事误读风险极高。

### 第三轮：否定性搜索

查询：
- paper-search-mcp: `graph spectral features materials property prediction null model residualization criticism counterexample`
- paper-search-mcp: `amorphous oxide semiconductor mobility structure descriptor no-go failure limit validation 2024 2025 2026`

结果：
- 未发现明确反证 `graph spectra` 不可能用于 AOS 输运。
- 发现更致命的间接否定：真实 AOS mobility 受 carrier concentration、oxygen vacancy、process condition、gate/interface、tail states、scattering time 等变量影响。没有 same-sample joined table 时，任何 graph-spectra residual 结论都无法排除样本来源/工艺/标签混杂。

判定：三轮查重通过（方法层、框架盲区、否定性均执行），未发现直接竞争者；但发现足以拒稿的既有解释框架和混杂风险。

工具清单：三轮均使用 paper-search-mcp；未降级 web_search。

## 2. 叙事退让检查

叙事退让警告：若早期版本曾声称 `graph spectra independently explain real AOS/a-In2O3 transport`，当前版本退到 `bounded / protocol-ready / empirical validation paused`，这是从材料发现退到实验协议。

这不是科学进步本身，而是承认原实证主张尚未成立。当前可保留的贡献只剩：same-sample residual validation protocol、synthetic sanity benchmark、B0/G1 namespace、external-label provenance schema。不能再包装成 graph spectra 已经胜过 orbital-overlap 或 DFT mobility baseline。

## 3. 五条拒稿理由

1. 真实材料证据缺席：无 provenance-complete external joined table，不能验证 graph spectra 与输运标签的同样本关系。[致命]  
作者需证明：每个 graph 样本与每个输运标签同源、同处理、可追溯。

2. Synthetic benchmark 只能测代码，不能测材料：它验证残差化/空模型管线，不验证 AOS 物理。[致命]  
作者需证明：真实外部标签上同样出现非平凡残差信号。

3. Srivastava 复现冻结导致基线不可判定：无 SI/exact normalization，不能做绝对 overlap 比较。[严重]  
作者需证明：取得 exact normalization，完成 reproduction 与 overlap-preserving null。

4. 与既有 AOS mobility 机制未解耦：carrier concentration、vacancy、工艺和界面混杂未被 same-sample 控制。[严重]  
作者需证明：graph residual 在控制工艺/载流子/界面后仍显著。

5. 新颖性目前停在工程协议：B0/G1 namespace 和 provenance schema 是可用基础设施，不是 Nature Physics 级物理结论。[严重]  
作者需证明：该协议产出传统 orbital-overlap/DFT/mobility 模型之外的新可检验现象。

## 4. 与已有文献的冲突

核心冲突文献：Srivastava et al., arXiv:1812.11333, DOI:10.1063/1.5096042。

精确冲突：Srivastava 已把电子输运解释为金属 cation s-orbital overlap，并报告 total normalized orbital overlap integral 与 effective mass / mobility trend 的直接相关。LP29-C2 在未取得 Srivastava SI/exact normalization、未完成 reproduction、未构造 overlap-preserving null 前，不能声称 graph spectra 独立解释真实输运，更不能声称 graph-beats-baseline。

条件检查：该冲突完全覆盖 AOS/a-IGZO/a-ZnON 的结构-输运解释框架；对 a-In2O3 的覆盖可能不是逐样本同材料，但足以作为必须击败的近邻基线。

## 5. 最致命一击

如果必须挑一个致命错误：核心逻辑把“可执行的残差验证协议”放在了“真实 AOS/a-In2O3 输运解释”旁边，但没有 provenance-complete external joined table 来连接 graph、样本、标签和工艺。

这不是可能有问题；这是我作为审稿人若必须给出拒稿理由，会指出的最致命问题。没有这张 joined table，所有 graph-spectra residual、baseline comparison、null model 和 material interpretation 都只是待执行计划。

作者的出路：构建 provenance-complete external joined table；逐样本记录结构来源、图构造版本、B0/G1 namespace、输运标签、测量条件、工艺条件、文献/DOI/表号/图号 provenance；随后只在这张表上做 residualization、Srivastava reproduction、overlap-preserving null 和 graph-vs-baseline 比较。

## 6. 建议

建议：拒稿。

理由：当前稿件可以作为 protocol-ready 内部里程碑，但缺少同样本外部真实标签验证；在 Srivastava normalization 和 provenance-complete joined table 缺席时，材料物理主张必须冻结。

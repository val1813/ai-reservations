# LP28 Round 3 强制审查 - Nature Physics 匿名恶意审稿人

审稿输入限制：本报告只依据用户给出的五条核心结论列表与独立文献检索；未读取 PI/Inspector 的推导内容作为审稿依据。

## 第零步：AI 幻觉检查

### Q0.1 量纲检查

唯一显式公式：

`I_phi = E_z2*C_phi/(kBT + hbar Gamma_phi + E_floor)`

- `E_z2`：若定义为谱权重，必须为能量量纲或已归一化无量纲权重；当前结论只说“谱权重/结构/退相干变量”，未给单位。
- `C_phi`：若为结构/相干连通因子，应为无量纲。
- `kBT`：J。
- `hbar Gamma_phi`：J，前提是 `Gamma_phi` 为 s^-1。
- `E_floor`：J。
- 右侧量纲：若 `E_z2` 为 J，则 `I_phi` 无量纲；若 `E_z2` 为无量纲谱权重，则 `I_phi` 为 1/J，不能作为无量纲 predictor。

结论：未发现必然量纲错误，但存在定义缺口。作者必须明确定义 `E_z2`、`C_phi`、`Gamma_phi`、`E_floor` 的单位；否则公式可被直接判为不可复现。

### Q0.2 数值方向检查

代入极限：

- `E_z2 -> 0`，`I_phi -> 0`。若声称 dz2 谱权重恢复促进 phase-bus recovery，则方向一致。
- `Gamma_phi -> infinity`，`I_phi -> 0`。若退相干增强抑制 bulk phase output，则方向一致。
- `T -> infinity`，`I_phi -> 0`。若热涨落抑制相干，则方向一致。
- `E_floor -> 0` 时，低温低退相干极限可能导致指标发散，除非 `E_floor` 有物理下界。

结论：方向未见反号，但 `E_floor` 是人为防发散项；若没有独立测量或固定协议，predictor 可被后验调参。

### Q0.3 循环论证检查

当前结论明确说 `I_phi` 只使用输入侧谱权重/结构/退相干变量，bulk output 用 shielding/Meissner/vortex/THz/Josephson 独立验证。形式上避开了直接把输出量塞回 predictor 的循环。

警告：如果 `E_z2` 或 `C_phi` 在实践中由 superconducting response、Josephson/THz mode、或 pressure-SC phase boundary 反拟合得到，则循环论证重新出现。必须要求同一样品、同一压力轴上先验锁定 predictor。

### Q0.4 量级鸿沟检查

核心结论未给数值估计，不能执行量级鸿沟审查。缺失本身是问题：Nature Physics 级别的工程化 predictor 至少需要给出典型 `kBT`、`hbar Gamma_phi`、`E_floor`、`E_z2` 的 meV 标尺，以及 `I_phi` 阈值的误差带。

### 第零步结论

幻觉检查有条件通过：未发现机械量纲/方向反号；但 `E_z2` 单位、`E_floor` 物理来源、阈值标定和非循环测量顺序必须补齐。否则 predictor 不是物理量，只是记号。

## 三轮查重

### 第一轮：方法层查重

使用工具：paper-search-mcp。

检索式：

- `La4Ni3O10 Pr4Ni3O10 trilayer nickelate density wave dz2 pz hybridization layer decoupling pressure superconductivity`
- `La4Ni3O10 Pr4Ni3O10 2023 2024 2025 2026 superconductivity density wave interlayer coherence bilayer dz2 pz`

命中：

- Haoxiang Li et al., `Fermiology and electron dynamics of trilayer nickelate La4Ni3O10`, Nature Communications 2017, DOI `10.1038/s41467-017-00777-0`。已覆盖 La4Ni3O10 的 trilayer fermiology、额外 dz2 相关 band 与低温 gap。
- Jialin Chen et al., `Magnetically mediated cross-layer pairing in pressurized trilayer nickelate La4Ni3O10`, Science China Physics, Mechanics & Astronomy 2026, DOI `10.1007/s11433-025-2862-6`。已把 pressurized trilayer La4Ni3O10 与 cross-layer pairing 放在机制中心。

判定：方法层没有发现完全相同的 `phase-bus recovery protocol`，但 LP28 不能把 dz2、trilayer、pressure、cross-layer/interlayer superconductivity 作为新颖贡献。

### 第二轮：框架盲区查重

使用工具：paper-search-mcp。

检索式：

- `layer selective electronic decoupling density wave trilayer nickelate superconductivity pressure restore interlayer coherence`
- `pressure suppresses density wave restores superconductivity La4Ni3O10 trilayer nickelate bulk Meissner shielding Hall Drude disorder domains`

命中：

- Feiyang Liu et al., `Interlayer electronic coherence links magnetism and superconductivity in Ruddlesden-Popper nickelates`, arXiv `2605.18524`。其摘要直接把 interlayer electronic coherence 作为组织参数，并提出其与 maximum pressure-induced Tc 反相关/相关约束。
- Yidian Li et al., `Orbital-selective Mottness Driven by Geometric Frustration of Interorbital Hybridization in Pr4Ni3O10`, arXiv `2602.03658`。其摘要直接覆盖 Pr4Ni3O10 的 dz2 incoherence、interorbital hybridization frustration、density-wave transition 和 structural control parameter。
- Sonia Deswal et al., `Dynamics of electron-electron correlation and electron-phonon coupled phase progression in trilayer nickelate La4Ni3O10`, Applied Physics Letters 2025, DOI `10.1063/5.0288265`。Raman 证据给出 La4Ni3O10 中 density-wave 相关 gap 与 electron-phonon/electron-electron crossover。

判定：LP28 Round 3 的退让是必要的。先发文献已覆盖“组织参数”和“dz2/hybridization/DW baseline”的大部分地盘。剩余新颖性只剩工程化 protocol 与非循环 predictor，而不是物理图像本身。

### 第三轮：否定性搜索

使用工具：paper-search-mcp。

检索式：

- `trilayer nickelate phase bus recovery protocol density wave layer decoupling failure problem criticism`
- `La4Ni3O10 pressure superconductivity density wave disproof counterexample Hall Drude Meissner shielding vortex Josephson 2024 2025 2026`
- `Ruddlesden Popper nickelate interlayer coherence superconductivity criticism counterexample anisotropy pressure 2024 2025 2026`

命中：

- Mengzhu Shi et al., `Absence of superconductivity and density-wave transition in ambient-pressure tetragonal La4Ni3O10`, Nature Communications 2025, DOI `10.1038/s41467-025-57264-0`。
- Dan Zhao et al., `Pressure-enhanced spin-density-wave transition in double-layer nickelate La3Ni2O7-delta`, arXiv `2402.03952`。虽为 bilayer，且条件不完全适用，但指出 pressure 与 DW/SDW 的关系不必然是简单 suppression。

判定：未发现直接反证 `phase-bus recovery protocol` 的同题论文；但已存在条件性反例和近邻体系冲突，足以反对“DW suppression/recovery protocol 自动推出 bulk superconductivity”的强叙事。

三轮查重结论：三轮查重已执行（方法层、框架盲区、否定性）。未发现完全相同的已发表 protocol；发现直接竞争的组织参数文献和 dz2/hybridization 文献。LP28 的可发表新颖性只存在于可检验工程协议，而非背景机制。

## 高风险引用核实

输入核心结论未提供具体引用句、摘要级引用或印象引用。按 REVIEWER 流程，本步跳过；但报告中所有外部文献均来自 paper-search-mcp 检索结果。未使用 WebSearch。

## 叙事退让检查

发现退让：

原可能声张：`interlayer coherence / dz2-pz-dz2 hybridization / DW layer decoupling 构成 LP28 的原创概念`。

当前声张：`不声称概念首创；只保留 static DW-induced dz2 layer decoupling 可转化为工程化 phase-bus recovery protocol`。

判定：这是实质退让，但不必然是规避攻击；若 manuscript 明确把先发文献列为背景并把贡献限缩为可执行 protocol，则退让可接受。若正文仍用“first/principle discovery/new mechanism”包装，则构成叙事退让警告。

## 五条拒稿攻击

1. 最小反例：tetragonal La4Ni3O10 没有 ambient DW transition 也没有 superconductivity。若 DW 消失或 dz2 decoupling 缺失本身足以 recover phase bus，该相应至少应给出正向 bulk signature；Shi et al. 2025 直接破坏单因果链。作者必须证明 protocol 需要的不是“无 DW”，而是特定压力路径下的可测 `I_phi` 增大。[fatal if manuscript claims sufficiency; otherwise serious]

2. 最薄弱推导步：`static DW-induced dz2 layer decoupling` 到 `engineerable phase-bus recovery protocol` 之间没有动力学闭环。静态 ARPES/Raman/structural baseline 只能说明存在 decoupling，不说明压力能可逆、单调、同一样品地恢复跨层相位刚度。作者必须补同一样品压力轴上的输入-输出联测，而不是跨样品拼图。[serious]

3. 与已有文献冲突：Liu et al. arXiv:2605.18524 已把 interlayer coherence 与 RP nickelate superconductivity 组织起来；Li et al. arXiv:2602.03658 已把 Pr4Ni3O10 的 dz2 incoherence、hybridization frustration 和结构控制讲清。LP28 若只重述这些再加一个 `I_phi`，新颖性不足。作者必须逐句说明 protocol 比这些工作的可检验增量是什么。[serious]

4. 数值合理性质疑：`I_phi` 没有量级标定。以 100 K 为例，`kBT ~ 8.6 meV`；若 `hbar Gamma_phi` 也是 1-10 meV，`E_floor` 取值会显著控制阈值。没有预注册 `E_floor` 和 `E_z2` 的归一化，任何 phase boundary 都可被后验拟合。作者必须给出无输出量参与的阈值、误差传播和失败判据。[fatal if used as claimed predictor]

5. 最近相似工作压缩新颖性：Chen et al. 2026 已讨论 pressurized La4Ni3O10 的 cross-layer pairing；Deswal et al. 2025 已给 La4Ni3O10 DW 相关 Raman gap；Liu et al. 2026 已把 interlayer coherence 作为组织参数。LP28 剩下的“phase-bus”命名不能替代新实验。作者必须交付最小突破实验，而不是概念重命名。[serious]

## Fatal / 非 fatal 区分

Fatal：

- 若 LP28 把 `I_phi` 当成已经成立的 predictor，但没有同一样品压力轴、输入侧先验测量、bulk output 独立验证，则这是 fatal。原因不是“未验证”这么温和，而是 predictor 的科学地位不存在。
- 若 LP28 声称 `DW-induced dz2 decoupling -> pressure recovery -> bulk SC` 为充分因果链，Shi et al. 2025 的 tetragonal La4Ni3O10 是条件性致命反例。

非 fatal 但必须降格：

- 若 LP28 只声称“提出一个待验证 protocol/experimental program”，当前状态是未验证与工程化不足，不是直接科学错误。
- 若 LP28 明确承认先发已覆盖 interlayer coherence、dz2-pz-dz2 hybridization、Pr4Ni3O10 dz2 incoherence，则查重不构成重复造轮子；但 Nature Physics 主文贡献会显著不足。

## 如果必须挑一个致命错误

**如果必须挑一个致命错误：** `I_phi = E_z2*C_phi/(kBT + hbar Gamma_phi + E_floor)` 被当作非循环 predictor，但核心结论没有给出独立单位定义、阈值标定、先验测量顺序和同一样品 pressure-axis 验证。

这不是“可能有问题”——这是我作为审稿人如果必须给出拒稿理由时会指出的最致命问题。没有这些，`I_phi` 只是把希望看到的 superconducting output 改名为输入侧指标。

**作者的出路：** 在同一块 La4Ni3O10 样品上沿同一 pressure tuning axis 预注册测量 `E_z2`、`C_phi`、`Gamma_phi` 和固定 `E_floor`，再盲测 shielding/Meissner/vortex/THz/Josephson；同时控制 Hall、ab Drude、domain、oxygen/disorder，并给出至少一个 pressure 点的失败判据。

## 建议

建议拒稿，除非稿件被重写为“待验证实验协议/roadmap”并删除 predictor 已成立的语气。当前核心结论最多支持 ambient DW layer-decoupling baseline 与 pressure-SC 邻近性；还不支持工程化 phase-bus recovery protocol 已被验证。

## 搜索工具使用清单

- 第一轮方法层查重：paper-search-mcp `search_arxiv`、`search_papers`；arXiv 子源多次空结果，但跨源检索命中 CrossRef/Semantic/OpenAlex。
- 第二轮框架盲区查重：paper-search-mcp `search_papers`、`search_arxiv`；命中 Semantic/OpenAlex/CrossRef。
- 第三轮否定性查重：paper-search-mcp `search_papers`；命中 CrossRef/OpenAlex。
- 未降级 WebSearch；无 WebSearch 标注需求。

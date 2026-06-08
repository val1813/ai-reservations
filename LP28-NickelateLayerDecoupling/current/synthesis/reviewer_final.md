# LP28 终审 REVIEWER

审查范围：重点复核 `pi_final_synthesis.md` 是否越过 `reviewer_round3.md` 边界，并执行必要最小引用/查重检查。读取文件包括：

- `current/synthesis/pi_final_synthesis.md`
- `current/synthesis/reviewer_round3.md`
- `current/plan/卡点登记册.md`

## 终审结论

**终审通过：当前最终综合没有仍然保留 fatal 表述。**

理由：最终综合已经把 LP28 降格为“有突破潜力的待验证实验协议 / 技术路线”，明确写出“不是已验证机制”，并把 `I_phi` 作为 input-side predictor 的待验证协议，而不是已校准、已证明的超导预测器。它还明确禁止用 `shielding/Tc/zero resistance` 反推 `I_phi`，并要求 independent bulk output，因此没有触发 Round 3 的两个 fatal 边界：

1. 没有把 `I_phi` 写成已验证 predictor。
2. 没有声称 DW disappearance 或 zero resistance 单独足以推出 bulk SC。

## Round 3 边界复核

### R3-C1: `I_phi` 不能被写成已验证 predictor

当前表述：

- “`I_phi` 未验证。”
- “阈值表是工作协议，不是已校准常数。”
- “若要进入下一窗口，优先追 LP28-S1：`I_phi` 是否能独立于 bulk output 预注册。”

判定：**已守住边界。非 fatal。**

仍需边界建议：下一稿中 `Input-side predictor` 最好改为 `Input-side candidate index` 或 `pre-registered input-side index`，避免 “predictor” 一词被读成已验证预测器。

### R3-C2: DW 消失不是充分条件

当前表述：

- “用 DW disappearance 单独判成功” 被列为禁止。
- 成功判据要求 `I_phi` 先于或同步于 `B_bulk` 跨阈值，并且 bandwidth/Hall/domain/oxygen 不能单独解释。
- 失败判据包括 `I_phi` 明显提升但无 independent bulk output。

判定：**已守住边界。非 fatal。**

### R3-C3: 先发压缩新颖性

当前表述：

- “LP28 的理论增量不是 interlayer coherence 或 dz2 hybridization 的发现；这些已有先发。”
- 新颖性收窄为 static/dynamic 功能分离与 phase-bus recovery 的可实验协议。

判定：**已守住边界。非 fatal，但新颖性仍是窄贡献。**

边界建议：不能在标题、摘要或图示中使用 “new mechanism of nickelate superconductivity” 这类强语气；应写成 “testable ordering protocol” 或 “pre-registered input/output validation scheme”。

### R3-C4: 阈值标定仍半定量

当前表述：

- “阈值表是工作协议，不是已校准常数。”
- 下一步要求同一样品 pressure axis 上先验测 `E_z2`、`C_phi`、`Gamma_phi`、`E_floor`。

判定：**已守住边界。非 fatal。**

边界建议：最终综合仍保留公式

```text
I_phi = E_z2 * C_phi / (k_B*T + hbar*Gamma_phi + E_floor)
```

但没有在本文件内给出单位约定。若作为项目收官文档可以接受；若进入 manuscript 或 proposal，必须补一句：`E_z2` 为能量标尺或归一化谱权重时的不同量纲处理，以及 `C_phi` 无量纲、`Gamma_phi` 为 s^-1、`E_floor` 为预注册能量下限。

## 必要最小查重

### 第一轮：方法层查重

工具：paper-search-mcp。

检索式：

- `La4Ni3O10 Pr4Ni3O10 trilayer nickelate phase bus recovery protocol I_phi pressure superconductivity density wave dz2`

命中近邻：

- Haoxiang Li et al., `Fermiology and electron dynamics of trilayer nickelate La4Ni3O10`, Nature Communications 2017, DOI `10.1038/s41467-017-00777-0`
- Sonia Deswal et al., `Dynamics of electron-electron correlation and electron-phonon coupled phase progression in trilayer nickelate La4Ni3O10`, Applied Physics Letters 2025, DOI `10.1063/5.0288265`

判定：未发现同名或同构 `I_phi / phase-bus recovery protocol`；但 dz2、trilayer fermiology、DW/Raman gap 不是 LP28 新颖性来源。

### 第二轮：框架盲区查重

工具：paper-search-mcp；补充 arXiv 直接网页核验，因为 paper-search-mcp 对 `2605.18524` 返回空。

检索式：

- `trilayer nickelate input side predictor bulk output validation pressure axis Meissner shielding THz Josephson phase stiffness density wave`
- `Interlayer electronic coherence links magnetism and superconductivity in Ruddlesden Popper nickelates 2605.18524`
- `Orbital-selective Mottness Driven by Geometric Frustration of Interorbital Hybridization in Pr4Ni3O10 2602.03658`

命中近邻：

- Feiyang Liu et al., `Interlayer electronic coherence links magnetism and superconductivity in Ruddlesden-Popper nickelates`, arXiv `2605.18524`。paper-search-mcp 未命中，降级用 arXiv/WebSearch 核验存在性。
- Yidian Li et al., `Orbital-selective Mottness Driven by Geometric Frustration of Interorbital Hybridization in Pr4Ni3O10`, arXiv `2602.03658`
- Jialin Chen et al., `Magnetically Mediated Cross-Layer Pairing in Pressurized Trilayer Nickelate La4Ni3O10`, arXiv `2508.06802`, DOI `10.1007/s11433-025-2862-6`

判定：框架近邻很强，尤其 interlayer coherence、orbital-selective dz2 incoherence、cross-layer pairing 已压缩机制新颖性。最终综合已承认这一点，因此不构成 fatal。

### 第三轮：否定性/反例搜索

工具：paper-search-mcp；补充 arXiv/WebSearch 核验 `2604.16611`。

检索式：

- `La4Ni3O10 pressure superconductivity density wave counterexample absence superconductivity tetragonal no density wave`
- `Ultrafast Magneto-Pressure Spectroscopy Control Correlated Phases Trilayer Nickelate 2604.16611`

命中：

- Mengzhu Shi et al., `Absence of superconductivity and density-wave transition in ambient-pressure tetragonal La4Ni3O10`, Nature Communications 2025, DOI `10.1038/s41467-025-57264-0`
- Zhi Xiang Chong et al., `Ultrafast Magneto-Pressure Spectroscopy and Control of Correlated Phases in a Trilayer Nickelate`, arXiv `2604.16611`

判定：这些结果继续反对“无 DW / zero resistance / SC-like dynamics 自动等于 bulk SC”的强叙事。但最终综合已经要求 independent bulk output，并把 `I_phi` 提升但无 bulk output 列为失败，因此反例没有击穿当前降格版本。

三轮查重结论：**方法层、框架盲区、否定性三轮已执行。未发现直接重复的同题 protocol；发现多个强近邻与反例压力，均已被最终综合的边界声明吸收。**

## 高风险引用核实

`pi_final_synthesis.md` 未列具体文献引用、摘要级引用或印象引用，因此没有可逐条核实的高风险引用句。Round 3 中出现的关键近邻文献，本轮做了必要最小存在性核验：

- `10.1038/s41467-017-00777-0`：存在。
- `10.1063/5.0288265`：存在。
- `10.1038/s41467-025-57264-0`：存在。
- `arXiv:2602.03658`：存在。
- `arXiv:2508.06802` / `10.1007/s11433-025-2862-6`：存在。
- `arXiv:2605.18524`：paper-search-mcp 未命中，arXiv/WebSearch 命中；应在正式文档中人工复核版本号和作者列表。
- `arXiv:2604.16611`：paper-search-mcp/openalex 或 arXiv/WebSearch 命中；可作为边界加强文献。

## 最终边界建议

1. 把 `Input-side predictor` 改成 `pre-registered input-side index`，除非后续 LP28-S1 真正完成盲测预测。
2. 在任何对外文本中避免 “I_phi predicts superconductivity” 这句话；允许写 “I_phi is proposed as a pre-registered input-side ordering variable to be tested against independent bulk output.”
3. `B_bulk` 不应把 `zero resistance` 列为充分项；当前最终综合已正确排除，应保持。
4. `E_floor` 必须固定为先验协议参数或独立测量量，不能作为后验 fit knob。
5. 新颖性只应落在“同一样品 pressure-axis 的 input/output ordering protocol”，不要回撤到 interlayer coherence、dz2 hybridization 或 DW-SC 邻近性首创。

## 如果必须挑一个致命错误

**当前最终综合中没有必须导致 fatal 的表述。**

如果将来稿件把 `I_phi` 从“待验证、预注册输入侧指标”重新写成“已成立的 superconductivity predictor”，致命错误会立即恢复：该公式尚无单位闭合、阈值标定、同一样品 pressure-axis 盲测和 independent bulk output 验证。

## 终审决定

**通过，带边界建议。**

一句话理由：最终综合已经从机制结论退到可检验实验协议，并明确禁止循环反推与单一 bulk 判据，因此不再越过 Round 3 的 fatal 边界；但对外表述必须继续压低 “predictor / mechanism / discovery” 语气。

## 搜索工具使用清单

- 第一轮方法层查重：paper-search-mcp `search_papers`。
- 第二轮框架盲区查重：paper-search-mcp `search_papers`、`search_arxiv`；`arXiv:2605.18524` 因 paper-search-mcp 空结果，降级 WebSearch/arXiv 页面核验。
- 第三轮否定性搜索：paper-search-mcp `search_papers`；`arXiv:2604.16611` 补充 WebSearch/arXiv 页面核验。
- 未对最终综合做全文引用核验，因为最终综合没有具体引用句。

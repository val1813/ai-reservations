# REVIEWER_R4_final

角色：LP23-R4 收尾 REVIEWER 重跑实例  
项目：`D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603`  
输出时间：2026-06-03  
输入限制：仅使用本轮传入核心结论列表；未读取旧 LP23-螺旋世界线目录。

## 第零步：幻觉检查

### Q0.1 量纲检查

关键修正公式：

`zeta = z / omega0`，`tau = t / omega0`，`H_tilde(zeta)=H(omega0*zeta)`。

检查：

- `z` 与 `omega0` 同为频率量纲，故 `zeta` 无量纲。
- `t` 与 `omega0` 若均用于同一谱变量归一化，则 `tau` 无量纲。
- `H_tilde` 的自变量 `zeta` 无量纲，实际传入 `H` 的是 `omega0*zeta`，恢复频率量纲。
- 因此此前 `1+tau^2` 的量纲错误在该修正版中被消除。

结论：量纲检查通过，但仅限修正版。任何保留未归一化 `1+tau^2` 的表述均为量纲错误。

### Q0.2 数值方向检查

本轮输入没有新的方向性不等式声称，除工具输出：

- `rank=6`
- `train_residual_norm=0.0013957664881648368`
- `holdout_error=0.0014384846096407084`
- `holdout_independent=false`
- `verdict=R4_TOOL_NOT_VALIDATED_BY_HOLDOUT`

检查：`holdout_error` 与训练残差同量级，只能说明合成 smoke test 没有立即崩溃；由于 `holdout_independent=false`，方向上不能推出外部独立预测力。

结论：若将 `holdout_error` 解释为独立预测证据，则为方向错误。

### Q0.3 循环论证检查

数据来源被明确标注为合成 smoke test，不是外部实验。`holdout_independent=false` 明确排除独立 holdout。

结论：存在循环验证风险。该测试最多验证脚本路径、残差计算和接口行为，不能验证物理假设或非 oracle 原则。

### Q0.4 量级鸿沟检查

本轮无跨 10 个数量级以上的物理量级估算。训练残差与 holdout_error 均约 `1.4e-3`，无量级鸿沟可作为物理结论依据。

### Q0.5 第零步结论

幻觉检查结论：通过的是“硬停止/降级”解释，不通过的是“NEW_PHYSICS”解释。

警告：B 路脚本结果只能支持 `R4_TOOL_NOT_VALIDATED_BY_HOLDOUT`，不得转写为独立预测力证据。

## 三轮查重

### 第一轮：方法层查重

使用 paper-search-mcp 优先检索。

命中结果：

- Timothy H. Hughes, “A theory of passive linear systems with no assumptions”, arXiv:1611.06140。摘要给出一般线性系统被动性的充要条件，并扩展 positive-real lemma。
- Valerio Lucarini, “Response Theory for Equilibrium and Non-Equilibrium Statistical Mechanics: Causality and Generalized Kramers-Kronig relations”, arXiv:0710.0958。因果性直接导出 Kramers-Kronig 关系与自洽性基准。
- Yang Meng et al., “Fundamental constraints on broadband passive acoustic treatments in unidimensional scattering problems”, Proc. R. Soc. A 2022, DOI:10.1098/rspa.2022.0287。明确将 Herglotz 函数用于被动系统 sum rules 与约束。
- Lang Zhang, Francesco Monticone, Owen D. Miller, “All electromagnetic scattering bodies are matrix-valued oscillators”, Nature Communications 2023, DOI:10.1038/s41467-023-43221-2。将 causality/passivity 嵌入线性散射表示。

判定：`W_origin/W_causality/W_passivity` 在 passive/causal linear response 最小域内已被 Herglotz、positive-real、passive realization、Kramers-Kronig、passive approximation/sum-rule 文献覆盖。方法层查重未支持新物理。

### 第二轮：框架盲区搜索

普通语言改写检索：

- “what can be inferred from passive causal response”
- “independent holdout validation preregistration blind calibration”
- “synthetic data smoke test validation predictive power”

命中结果：

- Daniel Grünbaum et al., “Quantitative probing: Validating causal models using quantitative domain knowledge”, arXiv:2209.03013。将验证类比 train/test split，并强调验证策略的边界。
- Matthew Salganik et al., “Introduction to the Special Collection on the Fragile Families Challenge”, Socius 2019, DOI:10.1177/2378023119871580。以高质量 cohort 和挑战赛形式评估可预测性。
- Katie E. Lotterhos et al., “Simulation Tests of Methods in Evolution, Ecology, and Systematics”, Annual Review 2022, DOI:10.1146/annurev-ecolsys-102320-093722。区分 simulation-based method evaluation 与 validation，并讨论误用风险。

判定：`W_nonoracle` 的可执行内容是成熟实验/统计协议：预注册、独立校准、blind split、locked model、外部 holdout、泄漏控制。它不是新物理原则。

### 第三轮：否定性搜索

检索 “protocol closure obstruction nonoracle physics principle passive causal response”、 “model validation independent holdout synthetic smoke test not evidence predictive power”等。

结果：

- 未发现“LP23-R4 Protocol-Closure Obstruction”作为同名成熟定理或新物理命题的直接先发。
- 但其每个可检验子声称均被成熟数学、控制、响应理论或验证协议吸收。

三轮结论：三轮查重已执行（方法层、框架盲区、否定性）。未发现直接同名竞争者；但发现核心内容不具备新物理新数学独立贡献。

## 叙事退让检查

原始可疑声称：Protocol-Closure Obstruction 作为新物理/新数学北极星。  
当前可保留声称：R4t residual-linter / physical witness-validator skeleton。

判定：这是从原则性北极星退让为工程工具骨架。该退让不是科学进步，而是承认新物理声称不能成立。必须显式降级，且输出不得包含 `NEW_PHYSICS`。

## 五条拒稿理由

1. 核心假设已被成熟理论吸收。  
在 passive/causal linear response 最小域内，Herglotz、Kramers-Kronig、positive-real lemma/passive realization 已覆盖可检验约束。作者需证明存在超出这些框架的新定理或新可观测量。[致命]

2. `W_nonoracle` 不是物理原则。  
非 oracle 性只能通过预注册、独立校准、blind split、locked model、外部 holdout 等实验统计协议实现。作者需证明它导出新的物理限制，而非复述验证规范。[致命]

3. B 路工具未被独立 holdout 验证。  
脚本自身 verdict 为 `R4_TOOL_NOT_VALIDATED_BY_HOLDOUT`，且 `holdout_independent=false`。`holdout_error=0.0014384846096407084` 是合成 smoke test 结果，不能作为外部预测力证据。作者需提供真正独立数据和冻结模型验证。[致命]

4. 从硬停止到工具骨架的退让消除了北极星。  
若最终仅剩 residual-linter / witness-validator skeleton，则贡献类型变为工程审计辅助，而非新物理/新数学。作者需重写题目、摘要、claim 和验收标准。[严重]

5. 现有最近工作已提供更强、更具体的成熟框架。  
Hughes 2016/2017 给出被动线性系统充要条件，Lucarini 2007/2008 给出因果响应的 Kramers-Kronig 关系，Meng 2022 用 Herglotz 处理被动 sum rules，Zhang/Monticone/Miller 2023 将 causality/passivity 嵌入散射表示。作者需逐条说明 LP23-R4 相比这些结果的不可化约差异。[致命]

## 最终裁决

建议：拒稿 / 硬停止。

最终判定：

- `LP23-R4 Protocol-Closure Obstruction` 作为新物理/新数学北极星：硬停止。
- `W_origin/W_causality/W_passivity`：在最小域内被成熟理论覆盖。
- `W_nonoracle`：只能作为成熟实验/统计协议要求，不是新物理原则。
- B 路最终脚本：`R4_TOOL_NOT_VALIDATED_BY_HOLDOUT`，不得将合成 smoke test 解释为独立预测力。
- 可降级保留项：`R4t certified residual-linter / physical witness-validator skeleton`。

强制约束：任何后续 R4t 输出不得包含 `NEW_PHYSICS`。

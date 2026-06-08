# INSPECTOR 审查报告：B Round 3

审查对象：`current-CphiCollapse/B/round3.json`  
北极星：LP28-CphiCollapse  
角色边界：仅审查 B Round 3；未读取 A 输出；不替 PI 综合。

## 总判定：BLOCKER

B Round 3 的方向比前轮更收敛：它明确承认 B_plus/B_formal 只是形式闭包，不能当作经验 no-go；也把 B_min 定义为预注册、可测、无 superconducting output leakage 的经验基线。Kubo/response closure 没有继续过度声称为 universal theorem。

但当前 matched-pair residual-annihilation 判据仍有一个致命定义漏洞：`same-sign Delta_r_pair` 的符号没有预注册方向。若 left/right 顺序、pair orientation 或“同号”解释在看到 `P_oe`/`R_oe` 后才确定，就会把输出信息泄漏进 survival/collapse 判定。这个漏洞直接影响 B 的核心判定：它可能把真实 residual survival 消掉，也可能把噪声解释成稳定同号 residual。

## 致命问题

### BLOCKER 1：matched-pair residual survival 的符号方向未定义，存在输出泄漏风险

文件定义：

`Delta_r_pair_j = R_oe_left_j - R_oe_right_j`

并用“same-sign residual survival”“same-sign abs(Delta_r_pair)”作为 B 被 falsify 或 residual survival 的条件。

问题：

- `left/right` 没有给出预注册、与 `P_oe`/`R_oe` 无关的排序规则。
- 如果 pair 内两件样品本来是“near-identical B_min”，则 signed pair difference 的方向在物理上未定义，除非另有预注册的独立轴。
- “same-sign abs(Delta_r_pair)”在数学上自相矛盾：取绝对值后没有符号。
- 若后验按 residual 大小、C_phi 方向、或有利于某结论的顺序排列 pair，就构成输出泄漏。

必须修正：

1. 预注册 pair orientation，例如按完全不含 `P_oe` 的独立变量排序，且该变量必须不等价于 B_min 拟合目标；或
2. 放弃同号 pair 差，改用无方向的绝对 residual survival 判据，并另用层级模型/置换检验评估是否超过 measurement-error null；或
3. 若 A/B 需要“同号”，必须定义一个独立 residual predictor `X_pre_not_in_B_min`，符号由 `X_pre_not_in_B_min(left)-X_pre_not_in_B_min(right)` 决定，且冻结在 `P_oe` 提取前。

在此修正前，B Round 3 的 collapse/no-go 表不能作为可杀死/保留 `C_phi` 理论对象的有效实验判据。

## 警告

### WARNING 1：B_min 与 P_oe extraction 的分离基本成立，但 c-axis/qz 项仍需防同源污染

B_min 明确排除：

- `P_oe` 派生 odd/even contrast terms；
- 同一 susceptibility decomposition 中拟合出的 matrix elements；
- superconducting output variables；
- post-hoc feature selection。

这是合格的分离声明。

但 `ordinary_c_axis_coherence` 允许 `normal_state qz scattering width / qz_broadening_proxy`，而 `P_oe` 也来自 odd/even susceptibility 的预注册 q, omega, polarization, temperature window。若 qz proxy 与 odd/even decomposition 共用同一响应数据、同一矩阵元校正、或同一窗口调参，就可能从 B_min 侧重新引入 target-generating 信息。

必须传给 PI synthesis：B_min 的 c-axis/qz coherence 特征需要独立采集或至少使用冻结的、与 odd/even contrast extraction 分离的低维 proxy。否则 B_min 会向 B_plus 滑回去。

### WARNING 2：Kubo/response closure 已降级为条件示意，但 formal closure 仍不能进入经验结论措辞

B Round 3 写明：

- `B_plus` 是 full normal-state response-kernel state；
- collapse 是 tautological closure only；
- 不声称 measured B_min 等于 full kernel；
- 不声称 universal theorem。

这通过 INSPECTOR 对 universal theorem 的检查。

但允许结论中仍有“Conditional no-go under full normal-state kernel closure”。PI synthesis 应避免把这句话放在主结论位置。它只是一条形式条件句，不是北极星的经验成果。

### WARNING 3：denominator floor 主定义量纲自洽，但检查区公式有运算优先级错误

主定义：

`effective denominator = sign(S) * max(abs(S), S_floor)`  
`S_floor = max(5*sigma_S, 0.05*S_ref)`

若 `chi_odd` 与 `chi_even` 是同一 susceptibility component，且 `sigma_S`、`S_ref` 与 `S` 同量纲，则 `P_oe` 是 dimensionless，`R_oe` 也是 dimensionless。这部分量纲通过。

但 `INSPECTOR_CHECK.formulae` 写成：

`P_oe = (chi_odd - chi_even) / sign(S) * max(abs(S), S_floor)`

按通常运算优先级，这等于先除以 `sign(S)` 再乘以 `max(...)`，量纲变成 susceptibility squared，错误。应统一为：

`P_oe = (chi_odd - chi_even) / (sign(S) * max(abs(S), S_floor))`

这不是主协议的根本错误，但会误导后续机械校验，必须修正。

### WARNING 4：eta 分解需要防止把未解释 residual 重新命名为 U_miss

文件称：

`eta = U_miss + epsilon_meas + R_oe`

且 B 解释为 remaining eta 是 `U_miss` 加 measurement noise。

量纲上它们都在 normalized P_oe residual scale，可以通过。但 epistemically 有风险：如果 `U_miss` 没有独立估计或上界，B 可以把任何 residual survival 重命名为 missing baseline uncertainty。需要规定：

- `epsilon_meas` 来自 technical repeats；
- `U_miss` 来自独立 metrology uncertainty/covariance 或预注册 sensitivity analysis；
- `U_miss` 不能在看到 `R_oe` 后调大；
- 超出预注册 `U_miss + epsilon_meas` envelope 的 residual 必须进入 survival/gray-zone，而不能被 B 后验吸收。

### WARNING 5：negative controls 覆盖面较好，但“样品质量 vs 非 bilayer artifact”仍需硬判据

已有 controls：

- scrambled pair；
- single-layer/non-bilayer；
- high-disorder；
- probe-window。

这些能覆盖 pairing discriminating power、非 bilayer artifact、disorder/dephasing、probe-window systematic。

不足是样品质量控制仍主要通过 disorder/dephasing 间接处理。建议 PI synthesis 要求增加或明确：

- 同批次重复样品/technical repeat 的 `P_oe` repeatability；
- probe calibration blank 或 reference standard；
- denominator-ill-conditioned exclusion 与 sample-quality metrics 的相关性报告；
- batch-stratified negative control，防止 batch effect 被误判为 residual survival/collapse。

## 七项重点检查结论

1. B_plus/B_formal 与 B_min：大体分离成功；B_plus 被明确标为 tautological closure only。但 B_min 的 qz/c-axis coherence proxy 仍需防同源污染。
2. Kubo/response closure：未过度声称 universal theorem；通过，但 formal closure 不应被 PI synthesis 升格为经验 no-go。
3. denominator floor、eta normalization、R_oe：主定义量纲自洽；`INSPECTOR_CHECK` 中 P_oe 公式括号错误；eta 的 `U_miss` 需要独立上界。
4. matched-pair residual annihilation：BLOCKER。符号方向未预注册，“same-sign abs”不成立，存在输出泄漏风险。
5. negative controls：设计较完整，但样品质量、batch effect、probe calibration 需要更硬的判据。
6. gray-zone：正确标为 inconclusive/repeat；不得选择性解释。
7. 理论对象矛盾：已经接近真实矛盾，即“B_min 是否 out-of-sample annihilate R_oe”。但在 matched-pair 符号/泄漏问题修正前，还不能说形成了可杀死/保留 `C_phi` 的干净矛盾。

## 必须传给 PI synthesis 的结论

PASS：

- B Round 3 明确降级 B_plus：形式闭包不是经验 no-go。
- B_min 的预注册、排除 superconducting output、cross-fitting、negative controls、gray-zone 规则方向正确。
- Kubo closure 目前只是 conditional schematic，不是 universal theorem。

WARNING：

- c-axis/qz coherence proxy 可能与 `P_oe` extraction 同源，需独立化或冻结低维 proxy。
- `INSPECTOR_CHECK` 中 P_oe 公式括号错误，必须修正以免量纲校验失败。
- `U_miss` 必须独立估计，不能后验吸收 residual。
- negative controls 需加入 batch/sample-quality/probe-calibration 硬报告。

BLOCKER：

- matched-pair residual survival/collapse 判据的 signed residual direction 未预注册；“same-sign abs(Delta_r_pair)”数学上不成立，并可能造成输出泄漏。修正前，B Round 3 的 collapse/no-go table 不可作为最终杀死或保留 `C_phi` 的实验判据。

--- 投喂 PI synthesis ---

必须修正（阻断级）：

1. 预注册 `Delta_r_pair` 的方向，或改用无符号 paired residual/置换检验；不得在看到 `P_oe` 或 `R_oe` 后决定 left/right 或“同号”方向。
2. 删除或修正“same-sign abs(Delta_r_pair)”表述。若需要同号，必须由独立的 `X_pre_not_in_B_min` 决定符号方向，并在 `P_oe` extraction 前冻结。

建议修正（警告级）：

1. 修正 `INSPECTOR_CHECK` 公式为 `P_oe = (chi_odd - chi_even) / (sign(S) * max(abs(S), S_floor))`。
2. 明确 B_min 的 qz/c-axis coherence proxy 不与 odd/even susceptibility decomposition 共用 target-generating extraction。
3. 给 `U_miss` 独立上界，禁止后验调参吸收 residual。
4. negative controls 增加 batch/sample-quality/probe-calibration 报告。


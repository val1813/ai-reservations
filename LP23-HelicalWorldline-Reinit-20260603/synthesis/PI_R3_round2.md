# LP23-R3 Round2 PI 综合

日期：2026-06-03

## 输入

- A 路：`current/A/R3_round2.md`
- B 路：`current/B/R3_round2.md`
- B 路本地脚本：`scripts/r3_qnp_lint_toy.py`
- A 路 INSPECTOR：`synthesis/INSPECTOR_A_R3_round2.md`
- B 路 INSPECTOR：`synthesis/INSPECTOR_B_R3_round2.md`

## 独立性与校对

A 路声明未读取 `current/B`、`synthesis/INSPECTOR_B*` 和旧 LP23 目录；B 路声明未读取 `current/A`、`synthesis/INSPECTOR_A*` 和旧 LP23 目录。A 路框架为有限维链复形、逆问题 discrepancy、半参数 nuisance tangent、model checking；B 路框架为静态分析、proof-carrying code、纠错码 syndrome/logical 分离。框架独立。

两个 INSPECTOR 均通过。A 路警告集中在阈值、协方差可逆性/伪逆、合法扩张库预注册。B 路警告集中在 toy 内部构造不可外推、`1e-16` 数值零与 `0.798` 有限范数的量级鸿沟、adversarial expansion 是构造性补列压力测试。

PI 复跑 `scripts/r3_qnp_lint_toy.py`，输出与 B 路报告一致。

## 本轮核心结果

A 路给出 no-go：若存在预注册合法扩张 \(j\)，使 \(D_1^{(j)}D_0^{(j)}=0\)、\(r^{(j)}\in\ker D_1^{(j)}\)，且白化投影残差

\[
\epsilon_\perp^{(j)}
=\{I-A_j(A_j^\top A_j)^+A_j^\top\}z_j
\]

为零或低于阈值，则 residual 不能声称为新物理自由度或新 obstruction；它只是既有 nuisance projection、inverse-problem discrepancy、model discrepancy 或 model checking 语境中的可吸收残差。

B 路把该判据做成本地矩阵 toy。基准合同下存在 `PASS_OBSTRUCTION`，`residual_norm=0.7981011406`；但只要把该 quotient 方向本身作为一列合法 template/nuisance/history 扩张加入，残差范数分别降到 `4.19e-16`、`4.50e-16`、`3.37e-16`，标签退化为 `TEMPLATE_RESIDUAL`、`NUISANCE_DIAGNOSTIC`、`HISTORY_DIAGNOSTIC`。

## 判定

R3a 的可保留版本继续收缩：它不再是“新物理自由度原则”，也不再是一般的“residual cohomology 新方法”。它只剩：

**有限合同相对的负判据协议。** 只有在选择合同、合法扩张库、协方差白化、阈值和复形条件全部预注册后，QNP-Lint 才能机械地说某个 residual 被吸收、未定义、或在有限库内暂未吸收。

这比 R3 Phase 启动声张显著更窄，触发 Re-escalation。不能把当前状态包装成 PRL 级“半定理”；若无更大命题，R3 将在 Round3 或 Re-escalation 后硬停止/降级。

## 新命题检查

Round2 产生一个更深层候选，不是更窄工具本身：

**LP23-R4 合法扩张合同的物理边界 / Protocol-Closure Obstruction。**

命题草案：真正有价值的问题不在 residual 是否非零，而在“哪些 template/bridge/history/nuisance 扩张被物理协议允许”。若存在由因果性、局域性、能量条件、测量协议或介质响应限制出的闭合扩张类，使某个 residual 对所有闭合内扩张不可吸收，那么 obstruction 才可能有物理意义；若扩张合同任意开放，则任何 residual 都能被事后补列吸收。

该候选比 R3a 更接近基础矛盾：物理可允许扩张的边界 vs 事后模型补全自由度。需要 Re-escalation A/B 独立攻击后决定是否注册为下一北极星。

## 停止条件

N=2，未到最低 3 轮。未触发最终硬停止，因为 Round2 揭示了一个可能更大的问题：合法扩张合同本身的物理闭合性。但 R3 原本声张已经持续降级，必须立即 Re-escalation，不能直接进入普通 Round3 继续磨窄。

## 下一步

按 PI §3 触发 Re-escalation：把被杀死/收缩的声张列给 A/B，要求各自提出比 R3a 更大或同等大的声张，尤其围绕“合法扩张合同如何由物理原则闭合”。若 A/B 不能给出更大声张，R3 进入硬停止/降级；若给出 R4 级候选，注册到项目北极星矩阵并切换验证。

# INSPECTOR Report: B Round 2

审查对象：`current-CphiPacket/B/round2.json`

总判定：WARNING

机械检查：PASS。JSON 可解析，必需主字段存在。

## 逐项审查

1. 是否仍避免 universal no-go：PASS

B 明确写出 `scope_guard`，并在 `structural_impossibility_trigger` 中声明 Round 2 不能证明所有未来 campaign 的普遍结构不可能性，只能定义审计路线。因此它保留的是 packet-level / protocol-level nonidentifiability，不是 universal no-go。

2. quantified_falsifier 的 N=48/36 complete/4 batches/3 labs 是否合理：WARNING

这些阈值作为“decision-grade protocol threshold”是清楚的，也没有伪装成文献事实。但它们偏重、偏昂贵，尤其是 `probe_families_min=4`、3 labs、4 batches、4 pressure cells/runs 叠加后，可能把“可推翻路线”推向 near-future consortium 级别，而不是普通单组 campaign。

PI synthesis 应保留这些数值为 B 的强协议门槛，但不应把它们当成已经由功效分析推出的最小样本量。下一轮应要求 B 给出可执行性分层：hard minimum、target、pilot-only、以及哪些 probe family 是必需而非冗余。

3. nonidentifiability_boundary 是否具体且可审计：PASS

边界列出 shared_extraction、unsealed_output、batch/lab aliasing、montage rows、denominator instability、calibration contingency、small-N、missingness 等具体失败条件。大多数条件可由日志、raw store、分析脚本、holdout fold、censoring rate 和 covariance sensitivity 审计。

轻微风险：`batch_lab_aliasing` 中“strongly enough”仍略抽象，但后半句“leave-one-batch-out or leave-one-lab-out validation cannot be run”给出了可操作判据。

4. independence_audit 是否真正定义 P_oe/B_min firewall：PASS

它明确规定 P_oe 与 B_min 的 raw store 分离、分析团队或 locked scripts 分离、双向 forbidden-information list、共享 metadata 限制、hash-locked calibration/script、output blind custodian，以及 green/yellow/red row 分级。`B_min_independence_threshold` 也给出 primary residual test 的准入规则：>=80% green，zero red。

这是本轮最强的部分，应传给 PI 作为下一轮协议核心。

5. gray_zone 是否合理、能否指导下一轮：PASS

24-35 complete blinded rows 被定义为 pilot-only gray zone，允许估计 variance、censoring、calibration sensitivity、axis coupling、full-N feasibility，同时禁止 “R_oe survives/killed” 等结论。退出条件分别指向 valid packet 与 nonidentifiable，能直接指导下一轮。

轻微风险：`after two realistic acquisition batches` 中 “realistic” 需要 PI 下一轮要求具体化为时间、成功率、样品损失率或 beamtime/run budget。

6. claims 是否把协议阈值伪装成统计功效结论：WARNING

整体上没有严重伪装。关键 claim 已标记为 `decision_rule_not_literature_fact`、`decision_rule`、`B_round2_boundary`，并在 `main_residual_risk` 中承认 N=36/48 不是 empirically optimized power calculation。

但有一处需要压低语气：`Rows below 24 complete blinded specimens are non-identifiable for R_oe because crossfit cannot distinguish...` 这句话容易从协议判定滑向统计定理。更稳妥表述应是：“under this protocol, N<24 is non-decision-grade / treated as non-identifiable unless an independently justified design proves otherwise。”

7. 是否正确保留 near-future sealed campaign 的可推翻路线：PASS

B 保留了 `concede_PACKET_FEASIBLE_NEAR_FUTURE` 与 `concede_PACKET_FEASIBLE_NOW` 两条路线，并明确：sealed output labels、same-sample/sistered genealogy、P_oe/B_min independent acquisition、blind custody、pilot proof、leave-one-batch/lab-out validation 都可推翻 B 的当前保留立场。

## 必须传给 PI synthesis 的结论

PASS:
- B Round 2 不是 universal no-go；它保留 near-future sealed campaign 可推翻路线。
- P_oe/B_min firewall 定义充分，应该进入 PI synthesis 的协议核心。
- nonidentifiability boundary 和 gray zone 可审计、可用于下一轮。

WARNING:
- N=48 total、N=36 complete、4 batches、3 labs、4 pressure cells/runs、4 probe families 的组合是高门槛。可作为 decision-grade threshold，但不能写成统计功效结论或自然界最低要求。
- `N<24 non-identifiable` 应改写为协议准入失败/非 decision-grade，而不是绝对统计不可能。
- 下一轮应要求 B 把阈值拆成 hard minimum、target、pilot-only，并说明 4 probe families 中哪些是真正必要的独立信息源。

BLOCKER:
- 无。B Round 2 可进入 PI synthesis，但上述 WARNING 必须显式保留。

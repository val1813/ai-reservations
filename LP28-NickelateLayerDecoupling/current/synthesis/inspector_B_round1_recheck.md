# INSPECTOR 窄范围复核：LP28 B博士 Round 1

输入：`current/B/round1.json`  
复核范围：只验证 JSON 格式，并保留原报告警告项摘要；不重新做完整物理审查。

## 格式复核

结论：格式阻断撤销。

- `Get-Content -Raw -Encoding UTF8 | ConvertFrom-Json`：通过。
- Python `json.loads(..., encoding='utf-8')`：通过。
- 解析到的顶层标识：`project=LP28`，`round=1`，`agent=B`。

说明：若 PowerShell 使用默认 `Get-Content -Raw` 读取该文件，仍会因无 BOM UTF-8 在当前 Windows PowerShell 环境中的默认解码问题报错；这不是当前文件的 JSON 语法阻断。后续机器验证应显式按 UTF-8 读取。

## 原报告警告项摘要

- `t_perp_eff` 单位约定需固定：若为速率，`hbar*t_perp_eff` 量纲成立；若为 hopping energy，应去掉 `hbar`。
- P4 的 `epsilon_c` 应变符号未定义；必须声明 `epsilon_c > 0` 是否表示 c-axis compression，否则 `d(rho_c/rho_ab)/d epsilon_c < 0` 不可执行。
- `Lambda` 验证链条有循环论证风险：需要区分哪些量是输入代理，哪些量是独立外部验证。
- 替代解释仍需补强：压力直接带宽/载流子/晶格效应、散射各向异性或结构畴、共同第三变量。
- 落地仍偏半定量：P2-P4 需要压力范围、时间尺度、`Delta sigma_c/Delta sigma_ab` 下限、Meissner/shielding fraction 阈值、应变量级。

## 投喂下一轮

必须修正（阻断级）：

无。格式阻断已撤销。

建议修正（警告级）：

1. 后续解析 `round1.json` 时显式使用 UTF-8。
2. 保留并处理上述原 INSPECTOR 警告项。

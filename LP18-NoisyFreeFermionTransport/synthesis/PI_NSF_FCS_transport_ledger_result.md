# PI NSF-FCS-1 Transport Ledger Result

## 输入

- Script: `scripts/nsf_fcs_transport_ledger.py`
- Formal ledger: `current/plan/nsf_fcs_transport_ledger.csv`
- Bare sanity check: `current/plan/nsf_fcs_transport_ledger_bare_check.csv`
- Smoke ledger: `current/plan/nsf_fcs_transport_ledger_smoke.csv`

## 执行

正式命令：

`python scripts\nsf_fcs_transport_ledger.py --L 16,24,32,48,64 --alpha 0.5,1.0,1.5 --m-tail 4000 --out current\plan\nsf_fcs_transport_ledger.csv`

结果：

- rows = 15
- valid = 15
- invalid_bare = 0
- `python -m py_compile scripts\nsf_fcs_transport_ledger.py` 通过

bare sanity check：

`python scripts\nsf_fcs_transport_ledger.py --L 8,12 --alpha 1.0 --m-tail 1000 --observable bare_right_exchange --out current\plan\nsf_fcs_transport_ledger_bare_check.csv`

结果：2 行均被门控为 `INVALID_BARE_EXCHANGE_NOT_TRANSPORT`，`S_R=NA`，不进入科学 keep/kill。

## 数值摘要

| alpha | slope(log G_R) | slope(log lambda_T'') | slope(log S_T) | S_T range |
|---:|---:|---:|---:|---|
| 0.5 | -0.456319 | -0.456319 | 0.000000 | 2.000000140..2.000000200 |
| 1.0 | -0.920382 | -0.920382 | 0.000000 | 2.000000258..2.000000370 |
| 1.5 | -1.322418 | -1.322418 | -0.000000 | 2.000000274..2.000000601 |

## 判断

最小 two-terminal single-particle transport ledger **没有 falsify** transport-FCS 改写版 NSF-FCS-1。`lambda_T''` 与 `G_R` 在每个 alpha 上同斜率，`S_T=lambda_T''/G_R` 稳定在约 2。

这不是 many-particle theorem，也不是 analytic `D_R~Cap` lemma 的证明。它只完成 minimal falsifier 层面的 keep：transport 版本可以进入下一阶段；bare exchange 版本仍关闭。

## 下一步

下一步有两个等价优先方向：

1. analytic：证明或反驳 `D_R(L)~Cap(R,0)`，尤其检查 reservoir-edge energy 是否可能低于 total capacity 一个额外尺度。
2. numerical：把 ledger 从 single-particle open sector 扩展到 finite-density exclusion sector，检查 `S_T` 是否仍跨 reservoir realization 收敛。

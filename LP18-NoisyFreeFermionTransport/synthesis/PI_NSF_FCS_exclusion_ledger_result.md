# PI NSF-FCS-1 Finite-Density Exclusion Ledger Result

## 输入

- Script: `scripts/nsf_fcs_transport_ledger.py`
- Formal exclusion ledger: `current/plan/nsf_fcs_exclusion_ledger.csv`
- Smoke ledger: `current/plan/nsf_fcs_exclusion_ledger_smoke.csv`

## 执行

正式命令：

`python scripts\nsf_fcs_transport_ledger.py --sector exclusion --L 4,5,6,7,8 --alpha 0.5,1.0,1.5 --m-tail 2000 --out current\plan\nsf_fcs_exclusion_ledger.csv`

结果：

- rows = 15
- valid = 15
- invalid_bare = 0
- `python -m py_compile scripts\nsf_fcs_transport_ledger.py` 通过

## 数值摘要

| alpha | slope(log G_R) | slope(log lambda_T'') | slope(log S_T) | S_T range |
|---:|---:|---:|---:|---|
| 0.5 | 0.540272 | 0.540272 | 0.000000 | 1.999999949..1.999999957 |
| 1.0 | 0.108798 | 0.108798 | 0.000000 | 1.999999976..1.999999999 |
| 1.5 | -0.252065 | -0.252065 | -0.000000 | 1.999999974..2.000000054 |

## 判断

finite-density exclusion ledger **没有 falsify** transport-FCS 改写版 NSF-FCS-1。与 single-particle ledger 一样，`lambda_T''` 与 `G_R` 在每个 alpha 上同斜率，`S_T=lambda_T''/G_R` 稳定在约 2。

这个结果比 single-particle keep 更强：occupation-dependent exclusion rates 没有破坏 `lambda_T''~G_R`。但它仍是小系统数值证据，不是 thermodynamic-limit theorem。

## 下一步

当前最有价值的推进是 analytic 化：解释为什么 `S_T≈2` 精确稳定。候选机制是 equilibrium / local detailed balance 下的 Einstein relation 或 Green-Kubo fluctuation-dissipation identity。下一轮应证明在 two-terminal symmetric gauge 与 `rho0=1/2` 下，`lambda_T''(0)=2 G_R` 是否为有限体积恒等式；若是，则 NSF-FCS-1 的二阶 FCS 同标度问题在该规范下变成一条 FDT 恒等式，而真正有风险的将是非平衡密度、非对称 reservoir、或高阶 cumulants。

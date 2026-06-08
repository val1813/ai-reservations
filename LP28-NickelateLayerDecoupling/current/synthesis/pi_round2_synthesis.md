# PI Round 2 综合

## 汇合判断

Round 2 明确把 LP28 从“谁对谁错的判据”推进到“可工程化变量”：

> 可能的突破杠杆不是 interlayer coherence 这个概念本身，而是把 Ni dz2/apical-O/dz2 层间通道工程化为 phase bus：恢复 c-axis 相位传输，同时尽量保留有利的 pairing fluctuations。

A 的贡献是先发边界和数据缺口：`arXiv:2605.18524` 已先发 interlayer coherence 组织参数，`arXiv:2604.14701` 已先发 bilayer dz2-pz-dz2 hybridization enables SC。LP28 必须收窄到 trilayer La4Ni3O10/Pr4Ni3O10 的 static-DW layer decoupling 与 pressure/strain/pump recovery sequence。  
B 的贡献是工程化表述：`Q_phi` 作为 phase-bus predictor，但不能把 `f_shield` 这种结果变量放进 predictor。

## 核心修正

INSPECTOR 指出 A 的 `Q = (W_c/W_ab)*f_shield/(1+A_DW)` 有循环风险。必须拆成两类量：

**Predictor（输入/设计变量）**

```
I_phi = E_z2 * C_phi / (k_B*T + hbar*Gamma_phi + E_floor)
```

- `E_z2`: dz2/pz c-axis coherent spectral weight converted to an energy scale, or `E0 * W_z2` if measured as dimensionless normalized weight.
- `C_phi`: 0-1 phase-connectivity factor, separately estimated from domain fraction / kz dispersion / structural coherence.
- `Gamma_phi`: dephasing rate.
- `E_floor`: experimental resolution / residual disorder floor to avoid unphysical divergence.

**Outcome（外部验证）**

```
B_bulk = f_shield plus Meissner/vortex/THz phase-stiffness evidence
```

`I_phi` 用来预测，`B_bulk` 用来验证；不得把 `B_bulk` 塞回 `I_phi`。

## 突破潜力检查

本轮更接近真实突破，但还没有到“理论突破已成型”。如果成立，科技进步价值在于：

1. 给 RP 镍酸盐高温超导设计从“找 pairing glue”转向“双目标调控”：保留涨落胶水 + 恢复 dz2 phase bus。
2. 指导压力、单轴应变、氧化学计量、非平衡泵浦的具体优化指标。
3. 把 bulk SC 失败解释为 phase-quorum failure，而不是 pairing failure。

当前障碍：仍缺少阈值表和同一样品 tuning-axis 数据。下一轮必须把工程路线变成 go/no-go protocol。

## 下一轮上下文摘要（≤300字）

Round 2 收敛：LP28 的突破杠杆是 Ni dz2/apical-O/dz2 interlayer phase bus，而非“interlayer coherence 概念首创”。先发已覆盖 interlayer coherence 与 bilayer dz2 hybridization，LP28 只保留 trilayer static-DW layer-decoupling 与 pressure/strain/pump recovery sequence。INSPECTOR 要求拆分 predictor 与 outcome：`I_phi = E_z2*C_phi/(kBT+hbar Gamma_phi+E_floor)` 预测，`B_bulk=f_shield/Meissner/THz` 验证。Round 3 必须产出阈值表：W_z2单位协议、适用域、压力/应变/温度窗口、Delta W_c下限、shielding fraction门槛、Hall/domain/pump-heating排除条件。

## AHA 检查

本轮有新洞察但不是立即切换北极星：`phase bus` 已从类比变成工程变量，下一步是阈值化。注册为 AHA 待稳固方向，不触发北极星升级。

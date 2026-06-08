# LP28 PI 最终综合

## 结论类型

**有突破潜力的待验证实验协议 / 技术路线。**

不是已验证机制，不是可直接写成 “I_phi predicts superconductivity” 的理论结论。

## 最终北极星表述

> 镍酸盐高温超导的材料设计顺序可能需要反转：不应只按“压低 DW / 搜索 Tc”推进，而应先判断材料是否同时满足三门控：pairing reservoir、recoverable orbital phase bus、independent bulk phase output。

## 最小理论增量

LP28 的理论增量不是 interlayer coherence 或 dz2 hybridization 的发现；这些已有先发。增量在于把 DW-SC 关系拆成：

1. static DW partition：切断或削弱 dz2/apical-O/dz2 phase bus；
2. dynamic fluctuation reservoir：仍可能支持 local pairing；
3. independent bulk output：只有 phase bus recovery 与 bulk phase stiffness 同时通过，才进入 bulk SC。

这把“DW 是敌是友”的二分法改写为“static/dynamic 功能分离 + phase-bus recovery”的可实验问题。

## 核心协议

Input-side predictor:

```
I_phi = E_z2 * C_phi / (k_B*T + hbar*Gamma_phi + E_floor)
```

Output-side validation:

```
B_bulk = shielding / Meissner / vortex / THz / Josephson phase-stiffness evidence
```

禁止：

- 用 shielding/Tc/zero resistance 反推 `I_phi`。
- 用 DW disappearance 单独判成功。
- 用 zero resistance 单独判 bulk。

## 单实验优先级

**最高优先实验：** 同一样品 pressure-tuned La4Ni3O10。

沿同一 pressure axis：

1. 先验测 `E_z2`、`C_phi`、`Gamma_phi`、`E_floor`。
2. 独立测 shielding/Meissner/vortex/THz/Josephson。
3. 同步控制 Hall、ab Drude、domain/structure、oxygen/disorder。

成功：

- `I_phi` 先于或同步于 `B_bulk` 跨阈值；
- bandwidth/Hall/domain/oxygen 不能单独解释。

失败：

- `B_bulk` 出现但 `I_phi` 不动；
- `I_phi` 明显提升但无 independent bulk output。

## 当前不可越界声明

- `I_phi` 未验证。
- 现有数据只支持 ambient DW layer-decoupling baseline 和 pressure-SC 邻近性。
- 阈值表是工作协议，不是已校准常数。
- 若要进入下一窗口，优先追 LP28-S1：`I_phi` 是否能独立于 bulk output 预注册。

## 下一步

下一研究窗口应启动 LP28-S1，而不是继续泛泛讨论 LP28：

> `I_phi` 是否能由 input-side spectroscopy/structure/dephasing 独立预注册，并在同一样品 pressure axis 上预测 independent bulk output？

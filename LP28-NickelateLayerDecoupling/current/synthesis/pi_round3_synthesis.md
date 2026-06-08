# PI Round 3 综合

## 汇合判断

Round 3 已经把 LP28 从“机制解释”落成了一个可杀死的工程反馈协议。

核心突破候选：

> 对 trilayer RP nickelates，不再把 pressure、DW collapse、rho_c/rho_ab 或 pairing glue 当作直接设计目标，而是用非循环的 `I_phi` phase-bus predictor 驱动调控；再用独立 bulk output 验证。若成立，高温镍酸盐超导优化从“找配对胶水”转成“保留涨落胶水 + 恢复 dz2 phase bus”的双目标工程。

## 当前最强协议

**Predictor**

```
I_phi = E_z2 * C_phi / (k_B*T + hbar*Gamma_phi + E_floor)
```

或 B 的等价工程写法：

```
I_phi = E_z2*C_phi/max(k_B*T + hbar*Gamma_phi, E_floor)
```

PI 采纳 A 的加法形式作为主文本，因为它在低温/低退相干下更保守；B 的 max 形式作为敏感性对照。

**输入侧只允许：**
- `E_z2`: dz2/apical-O/dz2 c-axis coherent spectral weight converted to energy scale.
- `C_phi`: domain/registry/kz/structural phase-connectivity factor.
- `Gamma_phi`: dephasing/linewidth.
- `T`, `E_floor`.

**输出侧只允许：**
- shielding/Meissner/vortex/THz/Josephson phase-stiffness evidence.
- zero resistance 只能作辅助，不可单独判 bulk。

## GO/NO-GO 核心阈值

工作阈值，不是自然常数：

- `I_phi < 0.3`: no-go。
- `0.3 <= I_phi < 1.0`: ambiguous。
- `1.0 <= I_phi < 2.0`: go candidate。
- `I_phi >= 2.0`: strong go。
- `Delta W_c/W_c_ref >= 0.25`：最低 c-axis recovery。
- shielding fraction `>=0.20`：A 的 bulk go；B 给的 `>=0.10` 是最低探索门槛。PI 暂定：
  - `>=0.10` = exploratory bulk signal；
  - `>=0.20` = working bulk gate；
  - `>=0.50` = strong bulk gate。
- Hall number 需匹配 `<=15%`（A）；B 的 selector 路线要求 `<=5%` 用于强匹配。
- domain fraction `>=0.70`（A）或 selector `>=0.80`（B）。
- oxygen stoichiometry uncertainty `<=0.01 / formula unit`。

## 单实验建议

如果只做一个实验：

> 同一样品 pressure-tuned La4Ni3O10，沿 DW-collapse/SC-emergence 窗口同步测输入侧 `E_z2/C_phi/Gamma_phi` 与输出侧 shielding + THz/Josephson，外加 Hall、ab Drude、domain/structure、oxygen/disorder controls。

判定：
- 成功：`I_phi` 先于或同步于 bulk output 跨阈值，且 bandwidth/Hall/domain/oxygen 不能单独解释。
- 失败：bulk output 出现但 `I_phi` 不动；或 `I_phi` 明显提升但没有 bulk output。

## 剩余警告

1. `E0 = 10 meV` 是工作校准，不是材料常数。
2. `E_floor` 必须预声明并做 0.25/0.5/1.0 meV 敏感性扫描。
3. `Gamma_phi` 需固定角频率/能量 linewidth 协议，避免重复乘 `hbar` 或漏掉 `2pi`。
4. “tracks more strongly” 必须在后续实验分析中定义统计模型。
5. 现有文献足以支持 baseline 和动机，不足以验证机制。

## 突破潜力判断

🔥 突破潜力，但尚未验证。

如果该 protocol 成立，它不是一篇边际论文，而是可改变镍酸盐高温超导设计路线的工程原则：从 hydrostatic pressure brute-force search 转到 phase-bus feedback optimization。它也会把“DW 是竞争序还是前体”的二分法替换成“static DW partition vs dynamic pairing fluctuation”的可调控分解。

## REVIEWER 输入核心结论

1. LP28 不声称 interlayer coherence 概念首创；先发已覆盖组织参数和 bilayer dz2-pz-dz2 hybridization。
2. LP28 的剩余核心声张是：trilayer La4Ni3O10/Pr4Ni3O10 中 static DW-induced dz2 layer decoupling 可被转化为可工程化 phase-bus recovery protocol。
3. 非循环 predictor `I_phi = E_z2*C_phi/(kBT+hbar Gamma_phi+E_floor)` 只使用输入侧谱权重/结构/退相干变量；bulk output 独立用 shielding/Meissner/vortex/THz/Josephson 验证。
4. 最小突破实验是同一样品 pressure-tuned La4Ni3O10，在同一 tuning axis 上测 `I_phi` 与 bulk output，并控制 Hall、ab Drude、domain、oxygen/disorder。
5. 当前结论未被现有数据验证；现有数据只支持 ambient DW layer-decoupling baseline 和 pressure-SC 邻近性。

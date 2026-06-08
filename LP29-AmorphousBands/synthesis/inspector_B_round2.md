# INSPECTOR Report: LP29 B Round 2

输入文件：`D:\Claude\ai-reservations\LP29-AmorphousBands\current\B\round2.json`

角色：INSPECTOR  
检查对象：B 博士 Round 2  
结论：未发现致命量纲错误或核心代数错误；Round 1 的主要警告已被文本层面修复。但 toy 数值表未能证明来自实际离散图计算，边数与密度只能按四舍五入解释；非自证验证链已经在方案上打断循环，但尚未落地执行；controls 可执行性明显增强，仍需把“匹配/回归/kill condition”推进到数据表或脚本。

## 0. 机械检查

`D:\Claude\ai-reservations\LP29-AmorphousBands\validation` 不存在，不能运行 `validation/validate.py` 或 `validation/quantum.py`。

本报告降级为手工执行 Q1-Q5，并标注：`validate.py` 不可用。

## Round 1 B 警告复查

1. `lambda/beta/alpha/P(r)/edge density` 量纲：已基本修复。Round 2 明确 `lambda` 为长度，`beta/alpha_edge/alpha_corner` 为无量纲，`beta>0`，`P(r)` 为归一化概率密度，peak area 为概率质量，`rho_E_atom` 与 `rho_E_vol` 分开定义。
2. 低于阈值 numerical test：已修复。`S_GC=0.42, S_c=0.60` 给出 `S_GC-S_c=-0.18`，方向为 below-threshold。
3. 循环论证：方案层面已修复。Round 2 明确 `M(X)` 只作结构解释变量，验证标签来自 Hall/Drude/Wannier/spectral 或 matched controls，不能由同一 edge-weight proxy 生成。
4. 替代解释：已显著补齐。carrier density/O vacancy、onsite disorder、m*/tau、finite size、EF-Ec fitting error 都给出 controls 与 kill conditions。
5. 落地计算：部分修复。给出 toy ensemble 规则和最小表格，但没有坐标文件、脚本、随机种子或实际离散边计数，因此仍是半成品数值产品。

## Q1. 量纲校对

### F1: `S_GC - S_c`

- `S_GC`：最大连通分量占比，无量纲。
- `S_c`：阈值，无量纲。
- 左右匹配：通过。
- 数值例：`0.42 - 0.60 = -0.18`，无量纲，方向正确。

### F2: `t0*exp(-(r_ij-r0)/lambda)*(1+alpha_edge*I_edge+alpha_corner*I_corner)*exp(-beta*f_OO)`

- `t0` 为 eV，整体应为 eV。
- `-(r_ij-r0)/lambda`：`r_ij/r0/lambda` 均为长度，指数自变量无量纲。
- `(1+alpha_edge*I_edge+alpha_corner*I_corner)`：`alpha_edge/alpha_corner/I_edge/I_corner` 均无量纲。
- `-beta*f_OO`：`beta` 与 `f_OO` 均无量纲，指数自变量无量纲。
- `beta>0` 已声明，O-O defect 增大时 hopping 下降。
- 判定：通过。

### `P(r)`, peak area, edge density

- `P(r)` 定义为 `integral P(r) dr = 1`，单位 `length^-1`，通过。
- `A_[a,b]=integral_a^b P(r) dr`，无量纲，过。
- `rho_E_atom=2E/N_In`，平均每 In 边数，无量纲，通过。
- `rho_E_vol=E/V_cell`，单位 `length^-3`，通过。
- 警告：minimal_table 的 `rho_E_atom` 与 `rho_E_vol` 反推的 `E` 不是整数，只能解释为四舍五入后的目标均值，而不是单个离散图的精确计算输出。

## Q2. 符号/方向校对

- `t_min` 方向：Round 2 明确保留 `abs(t_ij)>t_min`，提高 `t_min` 删除弱边，因此 `S_GC/rho_E_atom/z_eff` 不应增加。通过。
- `beta` 方向：`beta>0`，`f_OO` 增大导致 `exp(-beta*f_OO)` 降低。通过。
- below-threshold 方向：`S_GC-S_c<0` 对应低 mobility/Drude/ridge coherence。通过。
- 警告：P1 的英文句子写成 “mobility or Drude weight decreases with structure-derived z_eff and S_GC”，按字面是随 connectivity 增大而降低；其 `expected_direction` 又写 “Lower S_GC and z_eff -> lower mu_H and Drude weight”。应改为 “decreases as z_eff and S_GC decrease” 或 “increases with z_eff/S_GC”。

## Q3. 循环论证校对

Round 2 将对象拆成：

- 结构输入：`X -> M(X)`，其中 `M={S_GC,z_eff,A_peak,rho_E,R_edge,R_corner,f_OO,betweenness_damage}`。
- 独立标签：`Y_independent={Hall/Drude/Wannier/spectral labels}`。
- 判定：`Y_independent ~ M + controls` 必须优于 `Y_independent ~ controls`。

这在逻辑上打断了 Round 1 的循环：不再允许只用同一个 proxy graph Hamiltonian 同时定义指标和生成验证 observables。

剩余警告：当前仍只是 protocol，没有实际 DFT/Wannier/实验标签，也没有 matched-control residual 表。因此“循环被打断”目前是设计层面的，不是实证完成。

## Q4. 数量级/数值一致性

### edge-weight sanity check

代入：

`exp(-(3.50-3.30)/0.55) * 1.30 * exp(-2.0*0.04)`

计算：

- 距离项：`exp(-0.363636) ~= 0.695`
- motif 项：`1.30`
- defect 项：`exp(-0.08) ~= 0.923`
- 乘积：`0.695*1.30*0.923 ~= 0.834 eV`

Round 2 写 `0.831 eV`，偏差约 0.4%，可归为四舍五入，通过。

### edge density table

`L=18 Å`，体积 `V=5832 Å^3`，`N_In=64`。

- G: `rho_E_atom=5.8` 反推 `E=5.8*64/2=185.6`；`rho_E_vol=0.0318` 反推 `E=185.46`。
- BD: `rho_E_atom=4.1` 反推 `E=131.2`；`rho_E_vol=0.0225` 反推 `E=131.22`。
- BA: `rho_E_atom=2.6` 反推 `E=83.2`；`rho_E_vol=0.0143` 反推 `E=83.40`。

两种密度彼此一致到四舍五入，但 `E` 不是整数。若这是单个 toy cell 输出，则不可能；若是多 seed ensemble 均值，则需要声明 seed 数、均值/方差/置信区间。当前判定为警告，不阻断。

### F3 vulnerability

`b_e*abs(t_e)/t0 = 0.20*0.80/1.00 = 0.16`，落在 `[0,1]`，通过。

## Q5. 代数与极限退化

- F1 无复杂代数，极限 `S_GC -> 0` 给负 margin，`S_GC -> 1` 给正 margin，方向正确。
- F2 极限：
  - `beta -> 0`：O-O penalty 消失，正确。
  - `f_OO -> infinity` 且 `beta>0`：hopping 衰减至 0，正确。
  - `lambda -> infinity`：距离衰减消失，正确。
  - `r_ij` 增大且 `lambda>0`：hopping 降低，正确。
- F3 极限：
  - `b_e -> 0` 或 `abs(t_e)/t0 -> 0`：vulnerability 归零，正确。

未发现代数展开、符号或极限退化错误。

## Q6. 综合判定

### Q6.3 声张缩水

相对 B Round 1，Round 2 有明显降级：从“graph threshold/graph-spectral transition”降为“non-self-certifying measurement protocol”。这是合理修复而非错误，但需要 PI 在矩阵评分中按“证明性降低、可证伪性提高”处理。

判定：警告，非阻断。

### Q6.4 替代解释

Round 2 已列出五类替代解释，每类都有 control 和 kill condition：

- carrier density / oxygen vacancy
- onsite disorder variance
- effective mass / scattering time
- finite-size threshold artifact
- EF-Ec definition or mobility-edge fitting error

这些 controls 足够进入下一轮执行，但仍需量化标准，例如 bin 宽、样本数、回归指标、交叉验证划分、finite-size convergence 判据。

判定：通过但需落地。

### Q6.5 落地计算

Round 2 不再是纯蓝图，已经给出 toy ensemble 参数、生成规则、阈值、最小表格和校准路径。

但当前文件没有实际 `XYZ` 坐标、随机种子、生成脚本、边列表或计算日志；minimal_table 的边数反推不是整数，说明它尚不能作为已执行的离散图计算记录。按 Q6.5 不是“空白无落地”，但属于“落地过弱/半成品”。

判定：警告，非阻断。下一轮必须物化 toy ensemble 或改为真实坐标/DFT/Wannier 数据，不应继续只增加 protocol 文本。

## INSPECTOR 结论

⚠️ INSPECTOR 警告：B Round 2 可继续，但必须显式标注 toy 表为未物化/未复现实算的半成品数值产品。当前没有阻断级量纲错误、方向错误或代数错误。

--- 投喂下一轮 ---

必须修正（阻断级）：

无。

建议修正（警告级）：

1. 修正 P1 方向措辞：不要写 “mobility decreases with z_eff/S_GC”；应写 “mobility decreases as z_eff/S_GC decrease” 或 “mobility increases with z_eff/S_GC after controls”。
2. toy minimal_table 必须补 seed 数、坐标/脚本/边列表或均值方差；否则 `rho_E_atom/rho_E_vol` 反推非整数边数，只能作为目标表，不是计算产物。
3. 非自证验证链已经设计正确，但下一轮必须至少落地一个外部标签或 matched-control residual 表；proxy Hamiltonian 只能作诊断，不能作唯一验证。
4. controls 需要量化执行标准：carrier-density bin、EF-Ec posterior、onsite variance 定义、m*/tau 来源、finite-size convergence 标准、交叉验证指标。
5. 声张已从“证明/判据”降为“measurement protocol”。PI 应在北极星矩阵中显式登记该缩水，但可因可证伪性增强继续推进。

---

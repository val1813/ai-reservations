# INSPECTOR Report: LP29 B Round 3

输入文件：`D:\Claude\ai-reservations\LP29-AmorphousBands\current\B\round3.json`

角色：INSPECTOR  
检查对象：B 博士 Round 3  
结论：未发现阻断级量纲、方向或代数错误。B Round 2 的 P1 方向措辞、controls 定量化、自证循环和声张边界基本修复；toy ensemble 表的均值/密度在 JSON 内部一致。但 Round 3 仍没有 seed-level CSV、脚本、边列表或外部 Hall/Drude/Wannier/spectral 标签，因此“toy 已执行”和“非自证验证链”仍只达到 protocol/表内自洽层级，不能作为材料实证。

## 0. 机械检查

`D:\Claude\ai-reservations\LP29-AmorphousBands\validation` 不存在，不能运行 `validation/validate.py` 或 `validation/quantum.py`。本报告降级为手工执行 Q1-Q6，并显式标注 `validate.py` 不可用。

项目中也未发现 `D:\Claude\ai-reservations\LP29-AmorphousBands\current\B\inputs`。因此 Round 3 的 toy ensemble 无法从本地脚本、坐标或 seed-level edge list 复现；只能校对 `round3.json` 内给出的均值表是否自洽。

## Round 2 警告复查

1. P1 方向措辞：已修复。Round 3 多处写为 “decrease as z_eff and S_GC decrease” 与 “increase with z_eff and S_GC after controls”，并在 `expected_direction` 中写明 `Lower S_GC and z_eff -> lower mu_H/Drude/ridge`。
2. toy 表非整数边数：部分修复。Round 3 明确 `n=32`、非整数 `E_raw_mean/E_kept_mean` 是 seed ensemble 均值，并给出 sample sd。密度均值与 `E_raw_mean` 的算术关系成立。剩余警告是没有 seed-level 整数边数、脚本或边列表，无法独立复现。
3. 非自证验证链：方案层面修复。Round 3 明确 proxy Hamiltonian 只能诊断，不能作为唯一验证；`Y_independent` 必须来自 Hall/Drude/Wannier/spectral 或 matched-control residual。
4. controls 量化：已修复到 protocol 层。Round 3 给出 CV R2/RMSE、bootstrap CI、AIC/BIC、Spearman、permutation p、Cohen d、系数 shrinkage、finite-size drift、Kendall tau、EF-Ec posterior 等 pass/fail 数值阈值。
5. 声张缩水：已明确。Round 3 写明不是 material discovery，toy 数值不是测量/DFT/Wannier，当前产物是 measurement protocol plus synthetic toy benchmark。

## Q1. 量纲校对

### F1: `rho_E_atom=2*E/N_In`

- `E`：边数，无量纲。
- `N_In`：原子数，无量纲。
- `rho_E_atom`：每 In 平均边数，无量纲。
- 判定：通过。

### F2: `rho_E_vol=E/L^3`

- `E`：边数，无量纲。
- `L^3`：体积，单位 `angstrom^3`。
- `rho_E_vol`：`angstrom^-3`。
- 判定：通过。

### F3: `t_ij=t0*exp(-(r_ij-r0)/lambda)*(1+alpha_edge*I_edge+alpha_corner*I_corner)*exp(-beta*f_OO,ij)`

- `t0`：eV，因此 `t_ij` 为 eV。
- `(r_ij-r0)/lambda`：长度/长度，无量纲。
- `alpha_edge, alpha_corner, I_edge, I_corner`：无量纲。
- `beta*f_OO`：无量纲。
- 判定：通过。

### F4: `Delta R2_CV` 与 `Delta BIC`

- `R2`、`Delta R2`：无量纲。
- `AIC/BIC/Delta BIC`：信息准则差值，无量纲比较量。
- 判定：通过。

## Q2. 符号/方向校对

- `beta>0` 且 `exp(-beta*f_OO)`：`f_OO` 增大时 hopping 下降，方向正确。
- `abs(t_ij)>t_min`：提高 `t_min` 只会删除或保持边，不会在固定图上增加 `S_GC/rho_E_atom/z_eff`，方向正确。
- P1：Round 3 正确写成 mobility/Drude/ridge coherence 随 `z_eff` 和 `S_GC` 降低而降低，等价于受控后随 `z_eff` 和 `S_GC` 增大而增大。
- P2：high-betweenness O-O damage 比 random O-O motifs 产生更负 residual，方向与 bridge-edge vulnerability 假说一致。
- P3：onsite-only disorder 若不降低 motif-aware connectivity，不应复现同样 collapse，方向与 B claim 一致。

判定：方向通过。Round 2 的 P1 反向英文措辞已修复。

## Q3. 循环论证校对

Round 3 将结构 proxy 与验证标签分开：

- 解释变量：`M(X)={S_GC,z_eff,R_edge,R_corner,f_OO,high_betweenness_damage}`。
- 独立标签：Hall mobility、optical Drude weight/scattering rate、DFT/QSGW/Wannier hoppings、spectral ridge coherence、matched-control residuals。
- 明确规则：若 `Y` 只由同一 `t_ij` proxy 生成，则标为 diagnostic-only，不能 pass B claim。

判定：循环论证在 protocol 层面已打断。剩余警告：Round 3 仍没有外部标签或 matched-control residual 数据表，所以非自证链尚未实证执行。

## Q4. toy ensemble means 内部一致性

使用 `N_In=64`、`L=18 angstrom`、`V=5832 angstrom^3` 手工复算：

| ensemble | `2*E_raw_mean/64` vs reported `rho_E_atom_mean` | `E_raw_mean/5832` vs reported `rho_E_vol_mean` | 其他一致性 |
|---|---:|---:|---|
| G_good | `2.61523` vs `2.6152` | `0.0143497` vs `0.01435` | `R_edge+R_corner=1.0000`, `E_kept<E_raw` |
| BD_borderline | `2.08106` vs `2.0811` | `0.0114187` vs `0.01142` | `R_edge+R_corner=1.0000`, `E_kept<E_raw` |
| BA_bad | `1.42871` vs `1.4287` | `0.0078393` vs `0.00784` | `R_edge+R_corner=1.0000`, `E_kept<E_raw` |

单调性也一致：

- `E_raw_mean`: G `83.6875` > BD `66.5938` > BA `45.7188`
- `E_kept_mean`: G `66.2188` > BD `50.4063` > BA `33.5938`
- `S_GC_mean`: G `0.7373` > BD `0.4136` > BA `0.1455`
- `z_eff_mean`: G `2.1849` > BD `1.8862` > BA `1.3679`
- `f_OO_target`: G `0.00` < BD `0.04` < BA `0.10`

判定：表内均值与密度关系通过；Round 2 的“非整数边数不可能是单图输出”已被 ensemble mean 解释修复。剩余警告：没有 seed-level 整数 `E_s`、脚本或边列表，不能验证 sample sd 或 deterministic seed rule 是否真实执行。

## Q5. 控制项 pass/fail 与非自证性

Round 3 的 controls 已从 qualitative list 升级为量化 protocol：

- primary model: `Delta R2_CV >= +0.10` 或 RMSE 降低 `>=15%`，bootstrap 95% CI 全部大于 0；fail 条件也给出。
- information criteria: `Delta AIC <= -6` 或 `Delta BIC <= -4` pass；`Delta AIC > -2` 且 `Delta BIC > -2` fail。
- matched residual: `|Spearman rho|>=0.35` 且 permutation `p<0.05`，或 `Cohen d>=0.50`；fail 有 sign flip、`|rho|<0.20`、`|d|<0.20`。
- carrier/vacancy control: 加入 Hall n、O vacancy proxy、anneal batch 后保留 `>=70%` standardized magnitude；低于 `30%` 或 sign-unstable fail。
- onsite disorder: matched variance 后 `Delta CV R2>=0.08` 或 `d>=0.50` pass；onsite-only 与 network 差距 `Delta CV R2<0.03` 且 `Delta BIC<2` fail。
- finite size: `S_c` drift `<0.08`、Kendall tau `>=0.6` pass；drift `>=0.15` 或 ordering sign change fail。
- EF-Ec: posterior draws 中 sign preserved `>=80%` 且 median `Delta CV R2>=0.08` pass；EF-Ec alone 达到同等解释且 `Delta CV R2<0.03` fail。

判定：controls pass/fail 已量化，且非自证边界明确。剩余警告：这些标准尚未应用到真实或独立标签数据，不能把 protocol pass 写成 scientific pass。

## Q6. 综合判定

### Q6.3 声张缩水

Round 3 明确承认缩水/降级：

- `product_type` 是 “protocol plus reproducible synthetic toy benchmark”。
- `has_real_material_measurements=false`。
- `has_real_dft_wannier_data=false`。
- guardrail 明确 toy 数值不是 amorphous In2O3 measurement、不是 Nature Physics extracted data、不是 DFT/Wannier result。
- `findings` 写明 “does not claim material discovery”。

相对 Round 2，没有进一步把 claim 从 protocol 降到更弱对象；但相对原始 B 路线，“network threshold/graph-spectral transition” 仍是 measurement protocol，不是已证明机制。判定：声张缩水明确，警告保留，非阻断。

### Q6.4 替代解释

Round 3 接受 A objection 作为 null model，并要求在 carrier density、EF-Ec、onsite variance、oxygen vacancy、m*/tau、finite size 等控制后才允许 B pass。判定：通过；剩余风险进入实际数据执行阶段。

### Q6.5 落地计算

Round 3 有 toy benchmark 表和 seed/pseudocode 规范，不是“完全无落地”。但本地没有 `current/B/inputs/toy_ensemble_v1`、脚本、坐标、edge list 或 seed-level CSV；Round 3 的 `next_plan` 也承认这些还需要 materialize。判定：落地过弱警告，非阻断。下一步不能继续只增加 protocol 文本，必须产出可复现 artifact 或真实坐标/标签表。

## INSPECTOR 结论

⚠️ INSPECTOR 警告：B Round 3 可继续；当前没有阻断级量纲错误、方向错误、代数错误或循环论证硬伤。Round 2 的关键警告大多修复到 protocol/JSON 表内自洽层级，但尚未完成可复现文件级落地或外部标签验证。

--- 投喂下一轮 ---

必须修正（阻断级）：

无。

建议修正（警告级）：

1. toy ensemble 需要物化：写出脚本、seed-level CSV、边列表或坐标文件，使 `E_s/E_kept_s/S_GC_s/z_eff_s` 和 sample sd 可复算。
2. 非自证验证链需要至少一个外部或 matched-control residual 表；proxy Hamiltonian 仍只能作 diagnostic-only。
3. 继续保留声张缩水标注：B 当前是 measurement protocol plus synthetic toy benchmark，不是材料发现或机制证明。
4. controls 已量化，但必须在下一步应用到真实/独立标签；否则只能说 protocol 合格，不能说 B claim pass。
---

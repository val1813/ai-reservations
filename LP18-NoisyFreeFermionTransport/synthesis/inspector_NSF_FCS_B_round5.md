# INSPECTOR NSF-FCS-1 Round 5 - B博士校对

输入：
- `current/B/NSF_FCS_round5_B.md`
- `synthesis/PI_NSF_FCS_exclusion_ledger_result.md`
- 必要实现参照：`scripts/nsf_fcs_transport_ledger.py`

校对范围：只做量纲、符号/方向、循环论证、数量级、代数/极限校对。

## 综合判定

**INSPECTOR 警告，非阻断。**

B 的主判断在机械层面通过：`FDT_residual_R2=lambda_T''-2G_T` 在 count 视为无量纲的 Markov-FCS convention 下量纲一致；NESS、非 LDB、activity forcing、有限频/高阶 cumulants 作为“离开 equilibrium zero-frequency second-order FDT”的方向没有发现反号。

需要显式标注的警告有四项：

1. finite-frequency resolvent 公式必须写明 row-generator 下的投影/伪逆 convention；
2. activity forcing 若只乘到 `k(e,x;nu)` 会改变正反 rate ratio，不是纯 time-symmetric activity；
3. “non-symmetric affinity split 不破坏 FDT”依赖 `F=eta_R-eta_L` 是 total entropy affinity，且 `G_T` 对同一个 total `F`、同一个 conjugate physical current 求导；
4. `ldb_mismatch` 在 `F=0` 可为零，若要检出 `a+b != 1`，应同时报告 affinity-derivative mismatch。

以上均为实现/规范警告，不构成阻断。

## Q1. 量纲校对

### `lambda_T''=2G_T`

B 行 24 给出：

- `F`、`chi`：无量纲；
- `J_T`：`count/time`；
- `G_T=dJ_T/dF|0`：`count/time`；
- `lambda_T(chi)`：`time^-1`；
- `lambda_T''(0)`：`count^2/time`。

若 count increment 按 FCS 标准作为无量纲整数，则 `count^2/time` 与 `count/time` 都退化为 `time^-1`，所以

`lambda_T''(0)=2G_T`

左右量纲匹配。行 55、178、197 的

`FDT_residual_R2=lambda_T_second_NESS-2*G_T_NESS`

同为 `time^-1`，量纲通过。

警告：若后续把 count 当成带物理单位的 transported charge，则右边应含一个单位 charge 因子，或统一把 current 写成 charge/time 而非 count/time。当前文本已显式假设 dimensionless count，因此不阻断。

### `S_T`

行 15 使用 `S_T=lambda_T''/G_R ~= 2`，行 48 使用 `S_T_NESS=lambda_T_second_NESS/G_T_NESS`。在 dimensionless count convention 下 `S_T` 无量纲，量纲通过。

记号警告：文本在 `G_R` 与 `G_T` 间切换。若 `G_R` 是同一个 transport conductance 的旧 ledger 名称，则无量纲比值通过；若后续引入 reservoir-specific `G_R` 与 transport `G_T` 两个对象，必须统一 residual 的分母对象。

### `ldb_mismatch`

行 113、178：

`ldb_mismatch_nu(x)=log(k(e,x;nu)/k(x,e;nu))-[log(rho_nu/(1-rho_nu))+eta_nu]`

两个 `log` 自变量均为 rate ratio 或 density ratio，无量纲；`eta_nu` 无量纲。量纲通过。

### finite-frequency formula

行 123、178：

`S_T(omega)=<a_T>_pi + 2 Re <h_T, (i omega - L_0)^(-1) h_T>_pi`

`a_T` 单位 `count^2/time`；`h_T` 单位 `count/time`；`(i omega-L_0)^(-1)` 单位 `time`；二次型单位为 `count^2/time`。量纲通过。

## Q2. 符号/方向校对

### NESS density bias

行 36 声称 `rho_L != rho_R` 时通常 `J_T(0;rho_L,rho_R) != 0`。在当前 left_transport_current convention 中，若 `rho_R>rho_L`，右端注入、左端抽取占优，左端抽取计数为正，所以 `J_T>0`。方向与行 43-45 的 `delta_rho=rho_right-rho_left` 扫描自洽。

行 38、58 的方向结论也自洽：NESS 背景噪声与在 NESS 上的微分响应不再由 equilibrium Einstein relation 机械绑定。无反号。

### non-symmetric affinity split

行 66：

`eta_R=aF`, `eta_L=-(1-a)F`, `eta_R-eta_L=F`

代入任意 `a` 均保持 total affinity 为 `F`。若每个 channel 的 LDB ratio 保持，且 conductance 对同一个 total `F` 求导，则行 70 的

`lambda_T''(0)=2 dJ_T/dF|0`

方向正确。极限检查：`a=1/2` 回到 symmetric gauge；`a=1` 为 right-only placement；`a=0` 为 left-only placement；三者 total entropy affinity 均为同一 `F`，纯 split 不应改变 FDT identity。

警告：这个“不破坏”判断只在 total entropy affinity normalization 下成立。若脚本把 `F` 当作某一端的 local field，而不是 `eta_R-eta_L`，或 current 不是 conjugate transport current，则该结论不能直接套用。

### activity forcing

行 76 写：

`k(e,x;nu) -> k(e,x;nu) exp(theta_nu F)`

行 78 又说 `theta_nu` 不改变正反跳的 entropy ratio。这里存在实现警告：若只给 injection rate `k(e,x;nu)` 乘 `exp(theta_nu F)`，则

`log[k(e,x;nu)/k(x,e;nu)]`

会增加 `theta_nu F`，并非 time-symmetric activity，而是改变 entropy ratio / LDB 的一部分。要保持“activity forcing”方向自洽，应对同一 channel 的正反两个方向同时乘相同 barrier/activity 因子，例如 injection 与 extraction 都乘 `exp(theta_nu F)`，再另行保留 thermodynamic antisymmetric part。

在该修正下，行 78、91 的方向正确：time-symmetric/frenetic perturbation 可改变 response 中的 frenetic term，从而让 `lambda_T''=2G_T` 不再由 equilibrium entropy cocycle 锁定。

### non-LDB

行 101-105：

`k_in=rho r exp(+a eta)`, `k_out=(1-rho)r exp(-b eta)`

给出

`log(k_in/k_out)=log(rho/(1-rho))+(a+b)eta`.

与 LDB 目标 `log(rho/(1-rho))+eta` 比较，mismatch 为 `(a+b-1)eta`。因此 `a+b != 1` 破坏 entropy-affinity normalization 的方向正确。

实现警告：在 `eta=0` 处，行 113 的 `ldb_mismatch` 数值本身为 0，即使 `a+b != 1`。若要在 FDT derivative 附近检出该破坏，应报告

`d/deta ldb_mismatch |0 = a+b-1`

或在小非零 `eta` 上报告 mismatch。

### finite-frequency / higher cumulants

行 121-129 的方向正确：zero-frequency second-order FDT 配对的是 DC conductance；若改成 `S_T(omega)/G_T(0)`，则该 ratio 是 diagnostic，不是 equilibrium FDT 的正确配对对象。若同步使用 `G_T(omega)`，equilibrium dynamic FDT 可能再次消去新标度。

行 131-151 对高阶 cumulants 的方向也通过：二阶 FDT 不固定单独的 `lambda_T'''`、`lambda_T''''`；time-reversal 对称点奇阶 current cumulant 可因反对称性为 0。B 已说明这不是原二阶标度本身，方向自洽。

## Q3. finite-frequency resolvent convention

现有脚本 `generator_from_edges` 使用 row-generator convention：`mat[src,dst] += rate`，平稳分布满足 `pi @ L = 0`。在这种 convention 下，若 `h` 是 column observable，则 backward generator 作用为 `L @ h`，所以 resolvent 可写在 observable space 上，不需要转置。

但行 123 的表达必须补上以下实现条件：

- `h_T` 必须已中心化：`<h_T>_pi=0`；
- `omega=0` 时 `L_0` 有零模，必须使用投影后的 resolvent / Drazin inverse / Moore-Penrose on zero-mean subspace；
- 可写为 `P0 (i omega-L_0)^(-1) P0` 或明确“在 `<1>_pi` 正交的 zero-mean 子空间上取逆”；
- 若实现者改用 column-generator (`p' = L p`) 或用右平稳向量，则公式需要转置为对应的 backward generator；
- 非自伴 generator 下，`<h,(i omega-L_0)^(-1)h>_pi` 的左右向量 convention 不能混用。

符号检查：对单一 relaxation mode `L=-gamma`，B 的 `(i omega-L)^(-1)` 给出实部 `gamma/(gamma^2+omega^2)`，DC 极限为 `1/gamma`，与 `(-L)^(-1)` 的 Poisson convention 同号。因此没有发现全局负号错误；问题是投影/左右 convention 必须显式写出。

## Q4. 循环论证校对

B 使用 PI ledger 的结果作为动机：ledger 给出 `lambda_T''` 与 `G_R` 同斜率、`S_T~=2`，然后提出候选解释为 equilibrium LDB FDT/Ward identity。该步骤是解释性假设，不是用同一数据证明定理；未发现阻断级循环论证。

警告：行 190 “证明 `S_T~=2` 不是数值偶然”作为 Tier 0 目的表述过强。affinity split sanity ledger 只能做 regression / convention check，不能单独证明有限体积 FDT theorem。若后续把 Tier 0 数值零当作 Ward identity 的证明，会形成过度外推。

## Q5. 数量级与数值来源

未出现 `10^N` vs `10^M` 的数量级比较；无数量级鸿沟。

PI exclusion ledger 的数值摘要给出：

- `alpha=0.5`: `S_T=1.999999949..1.999999957`
- `alpha=1.0`: `S_T=1.999999976..1.999999999`
- `alpha=1.5`: `S_T=1.999999974..2.000000054`

B 行 26 使用该摘要为 `S_T~=2`，数量级吻合。PI ledger 已标注这是小系统数值证据、不是 thermodynamic-limit theorem；B 的后续方向判断没有把它机械升级成定理，未构成数量级错误。

## Q6. 代数/极限校对

### non-LDB mismatch

由行 101-103：

`log(k_in/k_out)=log(rho/(1-rho))+a eta+b eta`

所以行 113 的 mismatch 代数为

`(a+b-1)eta`.

符号和系数正确。极限：

- `a+b=1`：mismatch 为 0，回到 LDB；
- `eta -> 0`：mismatch 数值为 0，但导数 mismatch 仍可非零。

因此非 LDB 方向通过，带上面 derivative-report 警告。

### affinity split

`eta_R=aF`, `eta_L=-(1-a)F` 直接给

`eta_R-eta_L=aF+(1-a)F=F`.

极限 `a=0,1/2,1` 均保持 total affinity。代数通过。

### residual

`FDT_residual_rel = |lambda_T_second-2G_T|/max(1,|lambda_T_second|,|2G_T|)`

在当前 dimensionless count convention 下为无量纲。警告：若 `lambda_T_second` 和 `G_T` 在大 `L` 下很小，固定 `max(1,...)` 会把 relative residual 变成 absolute residual 的数值版本；这不是量纲错误，但若要比较跨 `L` 的相对误差，建议用物理尺度或 `max(eps,...)`。

## 最终判定

⚠️ **INSPECTOR警告：可继续，但需显式标注。**

通过项：
- `FDT_residual_R2=lambda_T''-2G_T` 量纲一致；
- NESS、非 LDB、activity forcing、有限频、高阶 cumulants 作为破坏/转向方向无反号；
- pure affinity split 与 equilibrium random reservoir 不单独破坏 zero-frequency second-order FDT 的方向自洽；
- 未发现阻断级循环论证、数量级鸿沟或代数系数错误。

警告项：
- finite-frequency resolvent 必须补投影/伪逆与 row/column convention；
- activity forcing 公式需同时作用于正反 rate 才是 time-symmetric activity；
- pure affinity split 的“不破坏”结论依赖 total entropy affinity 与 conjugate current 规范；
- non-LDB ledger 应报告 derivative mismatch，不能只在 `F=0` 读 `ldb_mismatch` 数值。

当前没有阻断项。

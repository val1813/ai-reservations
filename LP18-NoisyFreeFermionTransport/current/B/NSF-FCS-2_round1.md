# NSF-FCS-2 Round 1 B Side Attack: long-jump open exclusion NESS FDT residual

角色声明：B 博士（野路子）。本轮不读取 current/A 或 A 输出，只攻击当前解释的脆弱点。目标不是证明 `R2=lambda_T''-2G_T` 漂亮，而是给 PI 一个最小 kill ledger：哪几个数值实验能最快把 reservoir-tail / fractional conductance 解释杀死、降级，或逼它区分 thermodynamic NESS residual 与 kinetic residual。

## 0. B 侧总判断

当前证据最强的部分是：

- `R2` 在 NESS density bias 下稳定非零。
- 固定 `L=8` 时 `R2 ~ delta^2` 几乎完美。
- bias 反向后 `R2` 与 `S_T` 不变到数值精度。
- `R2` 的 `L` 斜率按 alpha 分组稳定：`alpha=0.5 -> 1.009`, `alpha=1.0 -> 0.621`, `alpha=1.5 -> 0.279`。

B 侧的攻击点：这组现象仍可能是三种东西之一：

1. thermodynamic NESS residual：由 density-affinity / entropy forcing 产生，携带 reservoir-tail scaling。
2. kinetic residual：由 escape traffic、activity、non-LDB rate shaping 产生，不一定是热力学 FDT 破缺。
3. finite-size eigenvalue / tilted-generator artifact：二阶 tilt 在小 `L=4..8` 下给出稳定假斜率。

所以 Round 1 的 kill criterion 必须把“非零 + delta^2”升级为“可分解、可反演、可被非 LDB 扰动区分”。

---

## 1. 最小数值 kill tests

### 1.1 更大 L：不要只加点，要设计会杀解释的 L-grid

建议先不追大而全，而用 alpha 分层的最小扩展：

- `alpha=0.5`: `L=4..11` 或至少 `L=8,9,10,11`。理由：当前 `R2` 斜率约 1，增长最快，最容易暴露 finite-size crossover 或 overflow/eigenvalue instability。
- `alpha=1.0`: `L=4..12`，因为当前斜率 0.621 最像非平凡 fractional exponent，需要确认不是 `L=4..8` 的局部曲率。
- `alpha=1.5`: `L=4..12` 或更高，因当前斜率 0.279 最弱，容易被常数项污染。

最小判据：

- 对每个 alpha，在 sliding windows `L=4..8`, `5..9`, `6..10`, `7..11` 上拟合 `log |R2|`。
- 如果 slope 漂移超过 `0.15`，则 reservoir-tail exponent 解释降级为 finite-size trend。
- 如果 `alpha=1.5` 的 slope 趋向 0 或变号，则说明该 residual 可能只是小 L correction，不是 robust scaling。

关键预测 P1：若 reservoir-tail 解释成立，则 `B2(L,delta,alpha)=R2(L,delta,alpha)/delta^2` 的 local slope 应在加大 L 后按 alpha 分组收敛，而不是按 `rho_left,rho_right` 或数值 eps-grid 分组。这里 `delta` 无量纲，所以 `B2` 仍是 residual rate，单位为 `1/time`；若要做无量纲幅度比较，用 `B2/G_T`。

--- INSPECTOR_CHECK ---
[公式] `p_eff(L1,L2;alpha)=log(|R2(L2,alpha)|/|R2(L1,alpha)|)/log(L2/L1)`，无量纲；`R2=lambda_T''-2G_T`，在当前 ledger 中 `lambda_T''` 与 `G_T` 都按无量纲 tilt/affinity 求导，单位同为 `1/time`。
[方向] 若 `p_eff` 在滑动窗口中不稳定，当前 fractional reservoir-tail scaling 解释被 kill 或降级。
[数据] 已有 `current/plan/nsf_fcs_tier1_ness_*.csv`；需要新增 `L=9..12` ledger。
[假设] tilted-generator 二阶导数和 finite-difference response 在新增 L 上仍能通过 `ROW_VALID` 稳定性检查。

### 1.2 反向 bias：已过 sanity，但还没杀掉“热力学 vs 动力学”

已有 `rho_left=0.6,rho_right=0.4` 对 `0.4,0.6` 的反向检查，`R2` 偶函数成立。B 侧建议把反向 bias 扩展为非对称基点：

- `0.30 -> 0.50` vs `0.50 -> 0.30`
- `0.20 -> 0.40` vs `0.40 -> 0.20`
- `0.55 -> 0.75` vs `0.75 -> 0.55`

理由：当前所有 density pair 以 0.5 为中心，可能隐藏 particle-hole 对称保护。离开 0.5 中心后，若 `R2` 仍只看 `delta^2`，解释更强；若出现奇次项或 base-density dependence，则当前“delta^2 near-equilibrium”只能写成中心对称特例。

最小判据：

- 定义 `B2(rho_bar,delta)=R2(rho_bar-delta/2,rho_bar+delta/2)/delta^2`。`B2` 不是无量纲量；在当前 ledger 下单位仍为 `1/time`。
- 检查 `B2(0.4,0.2)`, `B2(0.5,0.2)`, `B2(0.65,0.2)` 是否同指数同符号。
- 如果 `B2` 的 `L` 指数随 `rho_bar` 改变，则 alpha exponent 不是单纯 reservoir-tail 指数，而混入 density mobility curvature。
- 同时记录无量纲版本 `b2_rel=B2/G_T`，用于跨 alpha 或跨密度的相对幅度比较。

关键预测 P2：如果 residual 是 thermodynamic NESS residual，反向 bias 的二阶偶性保留，但 `B2` 允许依赖 `rho_bar`；如果它是 particle-hole artifact，则离开 `rho_bar=0.5` 后二阶纯净性会破裂，三阶项会出现。

--- INSPECTOR_CHECK ---
[公式] `R2(rho_bar,delta)=a2(rho_bar,L,alpha) delta^2 + a3(rho_bar,L,alpha) delta^3 + O(delta^4)`；`delta` 无量纲，`R2,a2,a3,B2` 在当前 ledger 下单位均为 `1/time`。无量纲比较量可取 `a2/G_T`、`a3/G_T` 或 `B2/G_T`。
[方向] `a3` 是 `1/time` 的奇次 residual-rate 系数；`a3 != 0` 或 `a2/G_T` 的 alpha-slope 随 `rho_bar` 强漂移，会杀死“仅由 reservoir tail 决定”的强解释。
[数据] 当前只有以 0.5 为中心的 density pairs 和一组反向 sanity；需要 off-center density pairs。
[假设] reservoir density 参数仍在 exclusion 稳定区间，且边界注入/抽出 rate 没有进入近零奇异区。

### 1.3 不同 alpha：选临界附近，而不是再扫 0.5/1.0/1.5

当前 alpha 太整齐。B 侧建议加三个“刺点”：

- `alpha=0.25`：长尾最强，若 exponent 继续增大，应出现最强 R2 scaling；若数值不稳，也能暴露 tail truncation `m_tail` 敏感性。
- `alpha=0.75`：检验 `0.5 -> 1.0` 间是否平滑，排除人为三点拟合。
- `alpha=2.0`：短尾更近局域，若 residual 仍非零且有强 L 增长，则 reservoir-tail 解释可疑。

最小判据：拟合 `p(alpha)`，检查是否单调下降。当前三点为 `1.009, 0.621, 0.279`，看起来单调。若 `alpha=2.0` 不接近 0 或负值，说明 residual 可能来自 kinetic activity 而不是 long-tail conductance。

### 1.4 换诊断量：`R2` 不够，必须同时看两个归一化和三阶 cumulant

建议新增 ledger 列：

- `R2_over_G = R2/G_T = S_T-2`
- `tau_J = R2/J0^2`，其中 `J0` 是 NESS density-bias 下未 tilt 的 stationary left transport current；`tau_J` 的单位是 `time`，只作时间尺度诊断。
- `Q_JG = R2*G_T/J0^2`，这是对应 `tau_J` 的无量纲版本，要求 `J0 != 0` 且 `G_T` 与 `R2` 使用同一 ledger 的 `1/time` 单位。
- `lambda_tilt_third` 或 `C3=lambda_T'''`。

杀伤逻辑：

- 若 `R2/G_T` 的 L-slope 比 `R2` 更稳定，说明 residual 是 conductance correction 的相对破缺。
- 若 `tau_J=R2/J0^2` 的 L 依赖等价于一个平坦时间尺度，或无量纲 `Q_JG=R2*G_T/J0^2` 平坦，说明 `R2 ~ J0^2/G_T` 或 `R2 ~ J0^2 tau_ref`，更像 generic near-equilibrium nonlinear response，不是新 reservoir-tail 标度。
- 若 `C3` 在中心 bias 下对反向 bias 为奇函数，并且 `C3/delta` 或 `C3/J0` 携带同一 alpha exponent，则支持 thermodynamic expansion；若 `C3` 不跟 bias parity 走，则怀疑 kinetic traffic。

关键预测 P3：若当前 `R2 ~ delta^2` 只是近线性响应的平方电流效应，则 `tau_J=R2/J0^2` 应表现为一个平滑时间尺度，且 `Q_JG=R2*G_T/J0^2` 应比 `R2` 本身更接近 L-independent；若 `Q_JG` 仍按 alpha 有非平凡幂律，才值得说它携带 reservoir-tail/fractional conductance 的新标度。

--- INSPECTOR_CHECK ---
[公式] `Q_G=R2/G_T=S_T-2`，无量纲；`tau_J=R2/J0^2`，单位 `time`；`Q_JG=R2*G_T/J0^2`，无量纲；`C3=lambda_T'''(0)`，单位 `1/time`，`C3/J0` 无量纲。
[方向] `tau_J` 平滑且 `Q_JG` 平坦会把强 claim 降级为 generic quadratic-current residual；`C3/J0` 的 bias parity 可区分 thermodynamic 与 kinetic forcing。
[数据] 需要 ledger 记录 NESS stationary current `J0`，并把 tilted eigenvalue finite-difference 扩展到三阶。
[假设] `J0` 不为零且远离数值噪声；三阶 finite difference 的 eps-grid 误差可控，需要至少两个 eps-grid consistency diagnostics。

---

## 2. non-LDB / activity / frenetic forcing 的最小 ledger 修改

### 2.1 原则：先分清 reversible activity control 和真正 non-LDB forcing

当前 reservoir edge rate 近似形如：

`k_e(F)=k_e(0) exp[g_e eta/2]`

这属于 LDB-style affinity tilt。B 侧原先想在 reservoir edges 上加 time-symmetric activity multiplier：

`k_e(F,A)=k_e(0) exp[g_e eta/2] exp[A h_e]`

其中：

- `eta` 是 thermodynamic affinity，反向边符号相反。
- `A` 是 activity forcing，`h_e` 无量纲。

但 INSPECTOR 指出的关键点成立：如果在 `delta=0` 且两端 reservoir density 相同的情况下，同侧入射/出射 rates 同乘一个 factor，那么同侧 in/out ratio 不变，通常仍是 detailed-balance process。此时 `R2≈0` 应该作为 equilibrium FDT sanity control，而不能被解释成 kinetic residual 证据。

### 2.2 reversible activity control：应该不产生 NESS residual

最小实现：

- 在 `ReservoirSpec` 加 `activity_bias: float = 0.0` 和 `activity_mode="reversible_side"`。
- left rates `left_in,left_out` 同乘 `exp(+A/2)`。
- right rates `right_in,right_out` 同乘 `exp(-A/2)`。

这改变左右 reservoir traffic，但不改变同侧 ratio：

`left_in/left_out = rho_left/(1-rho_left) * exp(eta_left)`

`right_in/right_out = rho_right/(1-rho_right) * exp(eta_right)`

因此在 `delta=0,A!=0` 时，预期是 `R2≈0`、`S_T≈2`。若出现非零 `R2`，优先解释为 implementation/FDT-response mismatch、tilt pairing 错误、finite-difference instability，或该 multiplier 实际破坏了 LDB，而不是 kinetic residual。

### 2.3 真正 non-LDB/activity forcing：必须破坏 closed-cycle LDB

要产生可控 kinetic residual，不能只乘同侧 in/out rates。最小 non-LDB 方案是在 reservoir flip 的入射和出射之间加入空间奇函数 skew，使它不能被任何单一 reservoir chemical potential 或 state potential 吸收：

`left_in(x)  *= exp(+A phi_x/2)`

`left_out(x) *= exp(+A phi_x/2)`

`right_in(x) *= exp(-A phi_x/2)`

`right_out(x)*= exp(-A phi_x/2)`

这仍只改 traffic，不改同侧 in/out ratio；因此若只看单个 reservoir flip pair，它仍像 reversible activity。它的危险之处在于与 bulk long jumps 组合后可能形成空间依赖 escape landscape。为了确保真正 non-LDB，必须加入一个 forward/backward asymmetry，最小取：

`left_in(x)  *= exp(+A phi_x/2)`, `left_out(x) *= exp(-A phi_x/2)`

`right_in(x) *= exp(-A phi_x/2)`, `right_out(x)*= exp(+A phi_x/2)`

其中 `phi_x=x/L-1/2` 无量纲。这样同侧 in/out ratio 变为：

`left_in/left_out = [rho_left/(1-rho_left)] exp(eta_left + A phi_x)`

`right_in/right_out = [rho_right/(1-rho_right)] exp(eta_right - A phi_x)`

这个 ratio 依赖 site `x`。它不能等价为单个左/右 reservoir chemical potential 重定义，因为一个 reservoir chemical potential 不应随耦合 site 变化。它破坏的 LDB 条件是：reservoir flip edge 的 log forward/backward ratio 不再等于同一 reservoir 的常数 chemical affinity 加上状态能差；沿 `empty -> x -> y -> empty` 的闭合环，`sum log(k_forward/k_backward)` 可以非零且依赖 `x,y`。

### 2.4 四象限实验：区分 thermodynamic residual、reversible traffic control、non-LDB kinetic residual

设 density bias `delta` 与 activity forcing `A` 分开扫：

| case | density bias delta | activity A | 目的 |
|---|---:|---:|---|
| E0 | 0 | 0 | equilibrium FDT baseline |
| E1 | delta | 0 | 当前 NESS thermodynamic residual |
| C1 | 0 | A, reversible_side | equilibrium activity control，预期 `R2≈0` |
| K1 | 0 | A, nonLDB_site_skew | pure non-LDB kinetic residual |
| M1 | delta | A, reversible_side 或 nonLDB_site_skew | mixed entropic-frenetic residual |

拟合：

`R2(delta,A)=c20 delta^2 + c02 A^2 + c11 delta A + c30 delta^3 + ...`

最小 kill 判据：

- 在 `reversible_side` 的 C1 中，`c02` 应为 0 到数值精度；若非零，先判 ledger/FDT/tilt 实现有问题。
- 在 `nonLDB_site_skew` 的 K1 中，`c02` 是真正 kinetic residual 候选，单位 `1/time`。
- 如果 non-LDB 的 `c02` 与 thermodynamic `c20` 同阶且同 alpha exponent，则 current claim 不能叫纯 thermodynamic NESS residual，最多是 entropic + kinetic residual family。
- 如果 `delta != 0` 下的 `c11` 非零，说明 density bias 与 activity forcing 不是正交方向，A 侧任何 McLennan 解释必须含 frenetic term。`c11` 单位也是 `1/time`。

关键预测 P4：reversible activity control 的 `delta=0,A!=0` 应给 `R2≈0`；真正 non-LDB `site_skew` 的 `delta=0,A!=0` 才允许给出 kinetic residual。若 non-LDB `c02` 复制 thermodynamic `c20` 的同一个 `p(alpha)`，reservoir-tail scaling 可能是边界 traffic 的几何放大，而不是单纯 FDT thermodynamic residual。

--- INSPECTOR_CHECK ---
[公式] reversible control: `k_e(delta,A)=k_e(0) exp[s_e eta(delta)/2] exp[A h_e]` 且同侧 in/out 同乘；non-LDB site skew: `left_in/left_out=[rho_left/(1-rho_left)] exp(eta_left+A phi_x)`, `right_in/right_out=[rho_right/(1-rho_right)] exp(eta_right-A phi_x)`，`phi_x=x/L-1/2`。`k_e,c20,c02,c11,R2` 单位为 `1/time`，`A,delta,phi_x,eta` 无量纲。
[方向] reversible C1 中 `R2≈0` 是 sanity control；non-LDB K1 中 `c02` 的存在和 alpha-slope 才是 kinetic residual 证据。
[数据] 需要修改 ledger 增加 `activity_mode, activity_bias`，新增 `reversible_side` 与 `nonLDB_site_skew` 两套四象限 CSV。
[假设] non-LDB site skew 的 site-dependent in/out ratio 不能被单个 reservoir chemical potential 或 equilibrium state potential 吸收。

---

## 3. 跨学科跳跃：信息论的 KL / traffic 分解

本轮选择的信息论结构不是“噪声像信息”这种比喻，而是 Markov path measure 的可测分解：两个路径测度之间的 KL divergence 可以拆成 current-like antisymmetric part 和 traffic-like symmetric part。这个结构直接对应 stochastic thermodynamics 里的 entropy production 与 dynamical activity。

本轮的跨学科跳跃：信息论 -> KL divergence / traffic -> NESS FDT residual ledger

借来的结构：

`D(P || P^R)` 不是只由平均流决定；两个过程即使有相同 stationary current，也可以因为 escape rates / waiting-time statistics 不同而有不同 path KL。

物理翻译：

- antisymmetric 信息量：边流 `j_e = pi_i k_{ij} - pi_j k_{ji}`，对应 entropy / thermodynamic force。
- symmetric 信息量：traffic `t_e = pi_i k_{ij} + pi_j k_{ji}` 或 escape `a_i=sum_j k_{ij}`，对应 frenetic forcing。
- FDT residual `R2` 如果只看 `lambda''` 与 `G_T`，可能把 `j_e` 与 `t_e` 混在一起。

可测物理量：

- `J0=sum_e pi_src(e) k_e g_e`，单位 `1/time`。
- `Traffic_left=sum_{e in left} pi_src(e) k_e`，`Traffic_right=sum_{e in right} pi_src(e) k_e`，单位 `1/time`。
- `Traffic_asym=(Traffic_right-Traffic_left)/(Traffic_right+Traffic_left)`，无量纲。
- `Escape_var=Var_pi[a_i]`，其中 `a_i=sum_j k_ij`，单位 `1/time^2`；可用无量纲 `Escape_cv2=Escape_var/(mean_pi a_i)^2`。
- `KL_rate_forward_reverse=sum_e pi_i k_{ij} log(k_{ij}/k^R_{ji})`，在可配对边上计算，单位 `1/time`。

奇怪但可检验预测 P5：在 reversible activity control 的 `delta=0,A!=0` 中，即使 `Traffic_asym` 非零，也应有 `R2≈0`，这是 equilibrium FDT control。只有在 `nonLDB_site_skew` 中，若 `R2/G_T` 与 `Traffic_asym^2`、`Escape_cv2` 或 `KL_rate/G_T` 同标度，而与 `Q_JG=R2*G_T/J0^2` 不同标度，才说明 NSF-FCS-2 的残差含有信息论 traffic/frenetic 成分。

--- INSPECTOR_CHECK ---
[公式] `T_c=sum_{e in channel c} pi_src(e) k_e`; `Theta_T=(T_R-T_L)/(T_R+T_L)`; `D_rate=sum_e pi_i k_ij log(k_ij/k^R_ji)`；`T_c,D_rate,J0,G_T,R2` 单位 `1/time`，`Theta_T,R2/G_T,D_rate/G_T,Escape_cv2` 无量纲。
[方向] reversible activity control 中 `R2≈0` 是 sanity check；non-LDB skew 中若 `R2/G_T` 与 `Theta_T^2` 或 `D_rate/G_T` 同标度，则 current-only thermodynamic 解释被 kill 或至少降级。
[数据] 需要 stationary distribution `pi`、edge rates、edge channel labels；当前脚本已有 edges 和 generator，可增列计算。
[假设] reverse edge pairing 明确；对 reservoir injection/extraction 需要以 same-site empty/occupied flip 配对。

### 深化 1：从 KL 到 Fisher information metric

更深一层的数学对象是 path-space Fisher information。这里不把它当作已证明的物理曲率，只把它定义成可测 ledger：

`I_ab = partial_a partial_b D_rate(P_theta || P_{theta+dtheta}) |_{dtheta=0}`

把参数取为 `theta=(delta,A)`，则有一个二维信息几何 metric：

`I = [[I_delta_delta, I_delta_A], [I_A_delta, I_A_A]]`

单位：因为 `D_rate` 是 `1/time`，而 `delta,A` 无量纲，`I_ab` 的单位也是 `1/time`。无量纲比较用 `I_ab/G_T` 或 `I_ab/(mean_pi a_i)`。

翻译回物理：

- `I_delta_delta` 是热力学 bias 方向的路径可分辨性。
- `I_A_A` 在 reversible control 中是 activity 方向的路径可分辨性，但不应单独产生 `R2`；在 non-LDB skew 中才是 kinetic forcing 方向的路径可分辨性。
- `I_delta_A` 衡量 entropy forcing 与 frenetic forcing 是否正交。

response observable 定义：用 `Y(theta)=R2(theta)/G_T(theta)` 作为无量纲 residual response；同时记录有量纲 `R2(theta)`。可测预测：如果 `I_delta_A/G_T` 随 L 的 exponent 与 `Y` 的 mixed finite difference 相同，说明 current residual 位于 entropic 与 frenetic 的混合方向，不是单一 thermodynamic 标量。

### 深化 2：从 Fisher metric 到曲率/holonomy

再深一层：在参数平面 `(delta,A)` 上做小闭合回路：

`(0,0) -> (delta,0) -> (delta,A) -> (0,A) -> (0,0)`

若 response 是梯度场，闭合回路的积分应为 0。要让这句话可检验，先定义 response observable：

`Y(delta,A)=R2(delta,A)/G_T(delta,A)`，无量纲。

`G_delta = partial_delta Y`，`G_A = partial_A Y`，两者对无量纲参数求导，仍无量纲。

`Omega_deltaA = partial_delta G_A - partial_A G_delta`

在光滑标量 `Y` 上混合偏导应交换，所以真正的 `Omega_deltaA` 应为 0；若有限差分闭合回路非零，首先把它解释为 nonlinearity、数值误差或路径定义不闭合。更稳妥的 B 侧可测量是 mixed finite difference：

`M_R(delta,A)=R2(delta,A)-R2(delta,0)-R2(0,A)+R2(0,0)`

`M_Y(delta,A)=Y(delta,A)-Y(delta,0)-Y(0,A)+Y(0,0)`

`M_R` 单位 `1/time`，`M_Y` 无量纲。物理翻译：不同 forcing 方向在 residual 中有非加性混合项。这不是已证明的 holonomy，只是一个可测 response non-additivity。

可测预测 P6：若 `M_Y/(delta A)` 的 L exponent 在 non-LDB skew 中非零，而 reversible control 中为 0 到误差内，说明 entropic/frenetic 混合项被 reservoir tail 放大。

--- INSPECTOR_CHECK ---
[公式] `M_R(delta,A)=R2(delta,A)-R2(delta,0)-R2(0,A)+R2(0,0) ~= c11 delta A`，单位 `1/time`；`Y=R2/G_T`；`M_Y=Y(delta,A)-Y(delta,0)-Y(0,A)+Y(0,0)`，无量纲；`G_delta=partial_delta Y`, `G_A=partial_A Y`, `Omega_deltaA=partial_delta G_A-partial_A G_delta`，无量纲但对光滑标量理论上为 0。
[方向] 非零 `M_R` 或 `M_Y` 表明 density bias 与 activity forcing 在 residual 中不可加；只有 non-LDB skew 中的稳定非零混合项才支持 frenetic/kinetic residual。
[数据] 同四象限 activity ledger，必须分别跑 reversible control 与 non-LDB skew。
[假设] `delta` 与 `A` 足够小，使二阶截断有效；需要至少两个幅度确认 `M_R ~ delta A`，且 `G_T != 0` 才能使用 `Y`。

---

## 4. A 博士可能反对点

1. A 可能说 activity forcing 不是原北极星问题，属于换题。B 回应：reversible activity 是 FDT sanity control，non-LDB site skew 是 falsifier；若无法区分 entropic residual、reversible traffic control 与 non-LDB kinetic residual，原解释没有可证伪内容。
2. A 可能说 off-center density 会引入 mobility curvature，污染 reservoir-tail exponent。B 回应：正是要测这个污染；若 claim 只能在 `rho_bar=0.5` 成立，需要降级为 particle-hole-centered observation。
3. A 可能说三阶 cumulant 数值不稳。B 回应：不用把 C3 当最终证据，只用它检查 bias parity；若 parity 都不稳，二阶 residual 的解释也不能太强。
4. A 可能说 KL/traffic 太抽象。B 回应：这里的 `Traffic_left/right`、`Escape_var`、`KL_rate` 都是 edge ledger 上直接可算的量，不是比喻。

---

## 5. 本轮失败记录

- 图论 max-flow/min-cut 类比一开始很诱人：long-jump reservoir tail 像 complete weighted graph 的边界 cut conductance。但失败点是 exclusion 的 FCS residual 不是单纯 cut capacity；它依赖 stationary measure、tilted eigenvalue 和 occupancy constraints，max-flow 没法自然给出 `lambda''-2G_T`。
- 经济学市场清算类比也可用：density bias 像价格差，activity 像交易量补贴。但失败点是可测量翻译容易退化成口号，除非引入 excess volume / order-flow imbalance。相比之下，信息论 KL/traffic 已经有 Markov path measure 的严格对象。
- 本轮没有实际运行更大 L，因为用户任务要求 B 侧攻击设计，且唯一写入文件限定为 B 报告。数值执行应由 PI 或专门 ledger runner 接手。

---

## 6. 下一步计划

最小可执行顺序：

1. 扩展 baseline L-grid：`alpha=0.5,0.75,1.0,1.5,2.0`，`L` 到可稳定上限，先保留 centered density pairs。
2. 加 off-center reverse bias：至少 `rho_bar=0.4,0.65`，同 `delta=0.2`。
3. ledger 增列 `J0`, `R2/G_T`, `tau_J=R2/J0^2`, `Q_JG=R2*G_T/J0^2`，并尝试 `lambda_tilt_third`。
4. 先加 reversible activity control：`activity_mode=reversible_side`, `A=+/-0.05,+/-0.10`，要求 `delta=0,A!=0` 下 `R2≈0`。
5. 再加真正 non-LDB forcing：`activity_mode=nonLDB_site_skew`, `phi_x=x/L-1/2`，输出四象限表。
6. 拟合 `c20,c02,c11` 的 L-slope 和 alpha-slope；这些系数单位均为 `1/time`，无量纲比较用除以 `G_T`。
7. 若 non-LDB 的 `c02` 或 `c11` 成立，再做 traffic/KL ledger：`Traffic_left/right`, `Traffic_asym`, `Escape_cv2`, `KL_rate_forward_reverse`。

---

## 7. 需要 PI 投喂的文献方向

- stochastic thermodynamics 中 frenetic contribution / traffic term / dynamical activity correction to response。
- McLennan ensemble 和 nonequilibrium response 中 entropic-frenetic 分解。
- Markov jump process path-space KL divergence、Fisher information metric、thermodynamic length。
- Long-range exclusion process / fractional boundary reservoirs 的 conductance scaling。
- Full counting statistics 三阶 cumulant 与 nonlinear response / fluctuation theorem parity。

---

## 8. B_AGENT 格式总表

本轮的跨学科跳跃：信息论 -> path KL / traffic decomposition -> NESS FDT residual ledger。

这个结构的数学对象：Markov path measure 的 KL divergence、traffic observable、二维 Fisher information metric `I_ab(delta,A)`，以及 residual response `Y=R2/G_T` 的 mixed finite difference `M_Y`。`Omega_deltaA` 只作为对 `Y` 的导数检查量；对光滑标量理论上应为 0，不能当作已证明物理曲率。

如果这个同构成立，最奇怪的可检验预测是：reversible activity control 中 `Traffic_asym` 可以非零但 `R2≈0`；真正 non-LDB site skew 中才可能出现 kinetic residual。此时无量纲 `R2/G_T` 应跟 `Traffic_asym^2`、`Escape_cv2` 或 `KL_rate/G_T` 标度，而不是跟 `Q_JG=R2*G_T/J0^2` 标度。

A 博士最可能反对的点：activity forcing 是外加 non-LDB 控制，不属于原 density-bias NESS；off-center density 会污染漂亮的 `delta^2`；C3 数值不稳；KL/traffic 看似离题。

本轮失败记录：图论 cut capacity 和经济学 market clearing 都尝试过，但前者不能自然生成 tilted-eigenvalue FCS residual，后者可测量翻译不如 KL/traffic 直接。

下一步计划：先做更大 L 与 off-center density 的 kill grid，再做 `J0/R2/G_T/C3/tau_J/Q_JG` 诊断，最后加入 reversible activity control 和 non-LDB site-skew 四象限 ledger 区分 `c20,c02,c11`。

需要 PI 投喂的文献方向：frenetic response、traffic term、path-space Fisher information、long-range exclusion conductance、FCS nonlinear response parity。

---

## 9. 修正记录

本节响应 `synthesis/inspector_NSF_FCS2_B_round1.md` 的 BLOCKED 点。

1. 量纲修正：`R2`、`B2=R2/delta^2`、`a2/a3`、`M_R`、`c20/c02/c11` 在当前 ledger 下均明确为 `1/time`；`delta,A,eta,phi_x` 无量纲。无量纲比较改用 `B2/G_T`、`a2/G_T`、`R2/G_T`、`M_Y`。
2. `R2/J0^2` 修正：原先不能作为无量纲诊断。现改名为 `tau_J=R2/J0^2`，单位 `time`，只作时间尺度诊断；新增无量纲组合 `Q_JG=R2*G_T/J0^2`，并要求 `J0 != 0`。
3. pure activity 修正：同侧 in/out 同乘的 `reversible_side` activity 在 `delta=0` 下通常仍满足 detailed balance，预期 `R2≈0`；它现在被定义为 equilibrium/FDT sanity control，而不是 kinetic residual 证据。
4. non-LDB 最小方案修正：新增 `nonLDB_site_skew`，令 `left_in/left_out` 与 `right_in/right_out` 获得 site-dependent `±A phi_x`。它破坏“同一 reservoir chemical potential 给出 site-independent forward/backward ratio”的 LDB 条件，并可在 `empty -> x -> y -> empty` 环上产生非零 log-rate circulation。
5. KL/traffic/Fisher/curvature 修正：补全 `J0`、`Traffic_left/right`、`Traffic_asym`、`Escape_var/Escape_cv2`、`KL_rate` 的单位；Fisher metric `I_ab` 定义为 path KL rate 的二阶导，单位 `1/time`；response observable 明确定义为 `Y=R2/G_T`。`Omega_deltaA` 只作为导数一致性检查，真正可测对象改为 `M_R` 与 `M_Y`。

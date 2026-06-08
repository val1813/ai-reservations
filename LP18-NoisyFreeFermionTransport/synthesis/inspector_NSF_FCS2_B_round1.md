# INSPECTOR 校对：NSF-FCS-2 B Round 1

结论：BLOCKED

范围：只核查 `current/B/NSF-FCS-2_round1.md`。未读取 A 文件或 `current/A`。

## Q1 量纲校对

### 1. `p_eff`

公式：`p_eff(L1,L2;alpha)=log(|R2(L2,alpha)|/|R2(L1,alpha)|)/log(L2/L1)`

- 左边单位：无量纲。
- 右边单位：`log(rate/rate)/log(length/length)`，无量纲。
- 判定：PASS。
- 保留条件：`L1,L2` 必须使用同一 `delta,rho_bar,alpha,eps-grid,T/ledger` 定义；否则不是同一物理量的比值。

### 2. `R2=lambda_T''-2G_T`

- `lambda_T''` 若是单位时间 cumulant，则单位为计数流方差率，通常可视作 `1/time`。
- `G_T` 若是对无量纲 affinity 的线性响应，也应为 `1/time`。
- 判定：WARNING。B 文件写成“同一 ledger 单位”可以接受，但必须在 ledger 中显式规定 affinity/tilt 均为无量纲，否则 `lambda_T''` 与 `G_T` 的可减性没有被证明。

### 3. `B2=R2/delta^2`

B 文件将展开写作 `R2(rho_bar,delta)=a2 delta^2+a3 delta^3+...` 并标注“无 SI 单位”。

- 左边 `R2` 单位：`1/time`。
- `delta` 为 density difference，无量纲。
- 因此 `a2,a3,B2` 单位仍为 `1/time`。
- 判定：BLOCKED。
- 必须修正：不得把 `R2` 展开系数或 `B2` 写成无量纲；若要做无量纲比较，应改用 `B2/G_T`、`B2/J_ref`，或明确乘以一个时间标尺。

### 4. `Q_G=R2/G_T=S_T-2`

- 若 `S_T=lambda_T''/G_T`，则 `R2/G_T=lambda_T''/G_T-2=S_T-2`。
- 单位：无量纲。
- 判定：PASS，条件是 `G_T != 0` 且 `S_T` 的定义确为 `lambda_T''/G_T`。

### 5. `Q_J=R2/J0^2`

- `R2` 单位：`1/time`。
- `J0` 单位：`1/time`。
- `R2/J0^2` 单位：`time`，不是无量纲。
- 判定：BLOCKED。
- 必须修正：将 `Q_J` 改名为有量纲诊断，或改为 `R2/(J0^2 tau_ref)`、`R2 G_ref/J0^2`、`R2/(J0^2/G_T)` 等明确无量纲组合。

### 6. `C3=lambda_T'''(0)`

- 若 tilt 参数无量纲，`C3` 单位仍为 cumulant rate，即 `1/time`。
- `C3/delta` 单位为 `1/time`；`C3/J0` 无量纲。
- 判定：WARNING。B 的“无 SI 单位或按 ledger 归一化”过松，需指定每个比值的实际单位。

### 7. `k_e(delta,A)=k_e(0) exp[s_e eta(delta)/2] exp[A h_e]`

- `k_e` 单位：`1/time`。
- `eta,A,h_e,s_e` 必须无量纲，指数自变量无量纲。
- 判定：PASS，条件是 `h_e` 无量纲。若取 `h_e=(x/L-1/2)` 可通过；若取 `log r_side(x)`，`r_side` 必须先无量纲化。

### 8. `R2(delta,A)=c20 delta^2+c02 A^2+c11 delta A+...`

- `R2` 单位：`1/time`。
- `delta,A` 无量纲。
- `c20,c02,c11` 单位均为 `1/time`。
- 判定：WARNING。公式可用，但系数不能当作无量纲。

### 9. Traffic/KL observables

- `T_c=sum pi_src k_e`：`1/time`，PASS。
- `Theta_T=(T_R-T_L)/(T_R+T_L)`：无量纲，PASS。
- `D_rate=sum pi_i k_ij log(k_ij/k^R_ji)`：`1/time`，PASS，条件是 reverse pairing 明确且 log 自变量为 rate ratio。

### 10. `M(delta,A)`

公式：`M=R2(delta,A)-R2(delta,0)-R2(0,A)+R2(0,0) ~= c11 delta A`

- 左边单位：`1/time`。
- 右边单位：`c11`，因此 `c11` 为 `1/time`。
- B 文件标注“无 SI 单位”错误。
- 判定：BLOCKED。
- 必须修正：`M` 是 residual rate，不是无量纲量；若要比较 exponent 可以用 `M/(delta A)`，但其单位仍为 `1/time`，除非再归一化。

## Q2 符号/方向校对

### 1. sliding-window slope kill

方向：`p_eff` 不稳定则 reservoir-tail exponent 解释降级。

- 极限检查：若真实幂律成立，窗口斜率应收敛；若 finite-size crossover 存在，窗口斜率漂移。
- 判定：PASS。

### 2. off-center density

方向：离开 `rho_bar=0.5` 后若出现 `a3 != 0` 或 `a2` exponent 随 `rho_bar` 强漂移，则“仅由 reservoir tail 决定”的强解释降级。

- 极限检查：在 particle-hole 对称中心，奇次项可被对称性压掉；off-center 释放奇次项是合理 kill test。
- 判定：PASS。

### 3. `R2/J0^2` 平坦的解释

方向：若 `R2/J0^2` 比 `R2` 更平坦，则 residual 更像 generic quadratic-current residual。

- 方向本身合理。
- 但当前比值有量纲，且 `J0` 接近 0 时会奇异。
- 判定：WARNING。必须加 `J0 != 0`、误差传播和无量纲化。

### 4. pure activity `delta=0,A!=0` 的方向

B 文件预测 pure activity 下 `J0` 可接近 0 但 `R2` 仍可能非零，并把 `c02` 作为 kinetic residual kill 关键。

- 方向问题：按 B 文件定义，side/occupancy activity 同乘同侧 in/out rates，保持同侧 entropy ratio；若 `delta=0` 且左右 reservoir density 相同，这通常仍是详细平衡 Markov jump process，只改变等待时间/traffic，不应产生 NESS FDT residual。
- 因此 `c02 != 0` 在该实现下更可能指向：ledger 的 FDT 响应定义不一致、activity 实现实际破坏了 LDB、reverse pairing/tilt 选择错误，或数值误差；不能直接解释为 kinetic residual family。
- 判定：BLOCKED。
- 必须修正：将 pure-activity kill criterion 改成 equilibrium control：`delta=0,A!=0` 应检验 `R2≈0`。若要制造 kinetic nonequilibrium residual，必须定义真正破坏 detailed balance 但可控的 non-LDB forcing，并明确哪些 rate ratios 被改变。

### 5. `c11` 混合项方向

方向：`c11 != 0` 表明 density bias 与 activity forcing 非正交，需要 frenetic term。

- 在 `delta != 0` 的 NESS 背景下，time-symmetric activity 改变 traffic 并影响 response 是合理方向。
- 判定：PASS，但前提是 pure-activity baseline 先通过 equilibrium control。

### 6. KL/traffic kill 方向

方向：若 pure activity 下 `R2 ~ Theta_T^2`，则 current-only thermodynamic 解释被 kill。

- 因 pure activity baseline 方向错误，此处也被牵连。
- 判定：BLOCKED。
- 必须修正：在 `delta=0` 的 reversible activity control 中，`Theta_T` 可非零但 `R2` 应仍满足 equilibrium FDT；更合适的 kill test 是在 `delta != 0` 下比较 `R2` 与 `Traffic_asym/Escape_var/KL_rate` 的变化，或改用真正 non-LDB activity。

## Q3 循环论证校对

未发现明显“用输入假设生成验证数据再验证输入假设”的循环论证。B 报告多数 kill tests 是新增 ledger 设计，而非宣称已经验证。

需要保留的弱点：

- `R2/G_T`、`R2/J0^2`、`C3` 若只在同一 tilted-generator finite-difference 框架中生成，最多是内部一致性检查；要避免循环，需要独立 eps-grid、response finite difference 与 stationary-current ledger。
- `KL/traffic/Fisher/curvature` 目前是可测 ledger 提案，不是已经建立的同构。若后续只按这些量拟合再反证 thermodynamic 解释，必须先定义 null model 和误差阈值。

判定：WARNING。

## Q4 数量级鸿沟标记

B 文件中出现的数量级比较主要是：

- 当前 slopes：`1.009, 0.621, 0.279`。
- slope drift threshold：`0.15`。
- 新增 `A=0.05,0.10`。
- `alpha=0.25,0.75,2.0`。

未发现 `10^N` vs `10^M` 且 `|N-M|>10` 的量级鸿沟。

判定：PASS。

## Q5 代数验算与极限退化

### 1. `p_eff`

若 `R2(L)=C L^p`，则

`log(|R2(L2)|/|R2(L1)|)/log(L2/L1)=log((L2/L1)^p)/log(L2/L1)=p`

判定：PASS。

### 2. density expansion

`R2(rho_bar,delta)=a2 delta^2+a3 delta^3+...`

- 在反向 bias 对称且 `rho_bar=0.5` 时，奇次项应受 particle-hole / reversal symmetry 限制。
- off-center 后 `a3` 可出现，方向合理。
- 系数单位错误已在 Q1 标记。

判定：WARNING。

### 3. activity expansion

`R2(delta,A)=c20 delta^2+c02 A^2+c11 delta A+...`

- 代数形式作为局部 Taylor 展开可接受。
- 但在 B 定义的 activity multiplier 下，`delta=0` 很可能仍是 equilibrium detailed-balance process，因此 `c02` 应作为 implementation/FDT sanity check，而不是 kinetic NESS residual 证据。

判定：BLOCKED。

### 4. KL rate

`D_rate=sum_e pi_i k_ij log(k_ij/k^R_ji)`

- log 自变量无量纲。
- 若 `k^R_ji` 为 time-reversed paired rate，公式单位为 `1/time`。
- 对 reservoir injection/extraction 必须配对 empty/occupied flip，否则 KL ledger 不闭合。

判定：PASS with WARNING。

### 5. Fisher metric 与 curvature

`I_ab`、`Omega_deltaA=partial_delta G_A-partial_A G_delta` 当前没有给出 `G_A` 的可测定义。

- Fisher metric 可以从 path KL 二阶导定义，物理上可测。
- `Omega_deltaA` 需要先定义 `G_delta,G_A` 是哪个 response observable 的分量，单位也随 `G` 而定。
- `M(delta,A)` 可测，但它只是 residual 的 mixed finite difference；称为 curvature/holonomy 仍是类比，尚未严格推出。

判定：WARNING。

## Q6 综合判定

BLOCKED。

必须修正后才能把 B Round 1 的 kill ledger 交给 PI 执行：

1. 修正所有把 `R2`、`B2`、`M` 或 Taylor 系数写成“无 SI 单位”的地方；它们在当前 ledger 下是 `1/time`，除非明确无量纲化。
2. 修正 `Q_J=R2/J0^2` 的量纲；当前单位为 `time`，不能作为无量纲诊断直接比较。
3. 将 `delta=0,A!=0` pure activity 从“可能产生非零 R2 的 kinetic residual”改为 equilibrium detailed-balance control；在保持同侧 in/out entropy ratio 且 reservoir density 相同的实现下，预期应为 `R2≈0`。
4. 若仍要测试 kinetic/non-LDB residual，必须另行定义真正破坏 detailed balance 的 non-LDB forcing，并写清楚哪些 forward/reverse rate ratio 被改变。
5. KL/traffic/Fisher/curvature 类比中，`Traffic_left/right`、`Theta_T`、`Escape_var`、`KL_rate` 已落到可测物理量；但 `Fisher metric` 与 `Omega_deltaA` 还需补全 response observable 和单位定义，不能直接作为已证明的物理曲率。

可保留的有效部分：

- 更大 `L` sliding-window `p_eff` kill test。
- off-center density 检查 `a3` 与 `a2(rho_bar)` 漂移。
- `R2/G_T` 与 `C3` bias parity 作为诊断。
- `c11` 在 `delta != 0` 背景下作为 entropic/frenetic 混合项的候选测试。
- traffic/KL ledger 作为后续可测补充，但需避开 pure-activity equilibrium 方向错误。

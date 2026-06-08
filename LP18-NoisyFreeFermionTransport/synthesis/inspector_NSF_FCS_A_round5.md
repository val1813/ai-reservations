# INSPECTOR NSF-FCS-1 Round 5 - A博士校对

范围：仅按 `ai/INSPECTOR.md` 做量纲、符号/方向、循环论证、数量级、代数/极限校对。未评价新意、文献覆盖或科研策略。

## 结论

⚠️ INSPECTOR警告：核心恒等式在自洽的 counting-field / affinity 约定下通过；但 A稿第 56-58 行把示例 affinity 写成 `A=logit(rho_L)-logit(rho_R)`，而当前台账脚本的正向 transport current 与中心差分参数对应的是 `F=logit(rho_R)-logit(rho_L)`。若直接把 A稿这个 `A` 同台账 `G_R` 相连，会产生整体号向反转风险。

非阻断：同时翻转 `Q_T` 与 `A` 后，GC symmetry、`lambda_chichi=2 lambda_chiA`、`lambda_T''=2G_R` 仍成立；台账中的 `S_T≈2` 与脚本自身规范一致。建议后续引用时显式写：台账 `G_R` 使用 `A_ledger=F=eta_R-eta_L`，并且 `Q_T` 为左端 out-in 计数。

## Q1. 量纲校对

1. `lambda(chi,A)=lim t^{-1} log E_A exp[chi Q_T(t)]`
   - `Q_T`：无量纲计数。
   - `chi`：无量纲，故 `chi Q_T` 无量纲。
   - `log` 自变量为期望值，整体无量纲；乘 `t^{-1}` 后单位为 `s^-1`。
   - 匹配：✅

2. `lambda(chi,A)=lambda(-A-chi,A)`
   - `A`：entropy affinity，无量纲。
   - `chi`：无量纲。
   - `-A-chi`：无量纲。
   - 两边均为 `s^-1`。
   - 匹配：✅

3. `lambda_T''(0;A)=partial_chi^2 lambda(0,A)=lim t^{-1} Var_A Q_T(t)`
   - `partial_chi^2` 不改变单位，因为 `chi` 无量纲。
   - `Var Q_T` 为计数平方，仍按 counting convention 视作无量纲二阶 cumulant；除以时间为 `s^-1`。
   - 匹配：✅
   - 注：若以后改为物理电荷 `e Q_T`，则二阶 cumulant 会带 `charge^2/s`，不能再直接写成当前单位。

4. `G_R=partial_A J_T=partial_A partial_chi lambda(0,0)`
   - `J_T=partial_chi lambda` 单位 `s^-1`。
   - `A` 无量纲，故 `partial_A J_T` 单位仍为 `s^-1`。
   - 与 `lambda_T''` 单位匹配：✅

5. `lambda_T''=2G_R`
   - 左右均为 `s^-1`。
   - 系数 `2` 无量纲。
   - 匹配：✅

## Q2. 符号 / 方向校对

1. GC symmetry 符号：
   - 在本项目普通 SCGF 约定 `lambda=lim t^{-1} log E exp[chi Q]` 下，若 fluctuation theorem 为 `P_A(Q)/P_A(-Q) asymp exp(A Q)`，则
     `M_A(chi)=sum_Q exp(chi Q)P_A(Q)=M_A(-A-chi)`。
   - 因而 `lambda(chi,A)=lambda(-A-chi,A)`。
   - A稿第 68 行符号：✅

2. 从 symmetry 推导二阶关系：
   - 令 `F(chi,A)=lambda(chi,A)-lambda(-A-chi,A)`。
   - `partial_chi F=lambda_chi(chi,A)+lambda_chi(-A-chi,A)`。
   - 再对 `A` 求导并取 `(0,0)`：
     `0=lambda_chiA(0,0)-lambda_chichi(0,0)+lambda_chiA(0,0)`。
   - 得 `lambda_chichi(0,0)=2 lambda_chiA(0,0)`。
   - A稿第 72-78 行无缺负号、无缺因子：✅

3. 台账方向：
   - 脚本 `eta_values(F,"two_terminal_symmetric")` 返回 `eta_left=-F/2`, `eta_right=+F/2`。
   - 脚本 `left_transport_current` 取 `g_left_in=-1`, `g_left_out=+1`。
   - 因此 `F>0` 时右端化学势高，正向计数是从右端经系统到左端的 left-out 方向；台账 conductance 是 `partial_F J`。
   - 所以台账的共轭 affinity 是 `A_ledger=eta_R-eta_L=F`，不是 A稿第 56 行字面写法 `eta_L-eta_R`。
   - 方向风险：⚠️

## Q3. 循环论证校对

A稿的 `lambda_T''=2G_R` 主要由 GC symmetry 代数推出；台账 `S_T≈2` 被用作数值规范校准与一致性说明，不是该恒等式的唯一输入。因此未发现“用同一假设生成数据再验证同一假设”的阻断性循环。

判断：✅ 无阻断循环。

## Q4. 量级鸿沟标记

本轮核心论证没有使用新的 `10^N` vs `10^M` 数量级估算。台账摘要只给 `S_T range` 接近 2 与斜率相同；没有发现超过 10 个数量级的比较。

判断：✅ 无量级鸿沟。

## Q5. 代数 / 极限校对

1. 平衡极限 `A=0`：
   - symmetry 退化为 `lambda(chi,0)=lambda(-chi,0)`。
   - 因而 `lambda_chi(0,0)=0`，平衡平均电流为零。
   - 与 finite-state detailed balance 预期一致：✅

2. 线性响应极限：
   - 由 Q2 链式法则得 `lambda_chichi=2lambda_chiA`。
   - 因 `J_T(A)=lambda_chi(0,A)`，所以 `partial_A J_T|0=lambda_chiA(0,0)`。
   - 得 `lambda_T''=2G_R`。
   - 代数正确：✅

3. 台账 `G_R` 规范：
   - `conductance()` 用 `(J(+delta)-J(-delta))/(2 delta)`，其中 `delta` 是脚本 affinity 参数 `F`，不是裸 `rho_L-rho_R`。
   - reservoir rates 使用 `exp(±eta/2)`，`eta` 无量纲；在 `rho0=1/2` 附近等价于 logit 化学势变量。
   - 因此台账 `G_R` 与 `partial_A J` 一致，但这里的 `A` 必须取 `A_ledger=F=eta_R-eta_L`。
   - 与 A稿抽象公式一致；与 A稿第 56 行示例号向不一致：⚠️

4. `lambda_T''=2G_R` 的 count convention：
   - 脚本 tilted generator 使用 `exp(chi * edge.g)`，`edge.g` 为无量纲计数增量。
   - `lambda_tilt_second` 对 `chi` 做二阶中心差分，输出计数方差率。
   - 因此 `lambda_T''/G_R≈2` 的单位与计数规范成立：✅

## Q6. 综合判定

⚠️ INSPECTOR警告，可继续但需显式标注：

1. A稿第 68-86 行的 GC symmetry 与 `lambda_chichi=2lambda_chiA` 推导通过。
2. `G_R=partial_A partial_chi lambda` 与台账规范一致的条件是：`A` 取台账脚本参数 `F=eta_R-eta_L`，`Q_T` 取左端 out-in 正向计数。
3. A稿第 56-58 行的 `A=logit(rho_L)-logit(rho_R)` 与当前台账正向 `G_R` 差一个整体负号；这是符号/方向警告，不是恒等式本身的代数阻断。

最终状态：⚠️ 警告通过。PI 可继续，但后续 synthesis 不应同时使用 A稿第 56 行的 `A=logit(rho_L)-logit(rho_R)` 和台账正向 `G_R>0`，除非同步翻转 `Q_T` 的正方向。

# INSPECTOR B Round2 Recheck

检查对象：`current/B/round2_B.md`

复查基准：`synthesis/inspector_B_round2.md` 的阻断项。

限制记录：本次只读取了项目 `AGENTS.md`、`ai/INSPECTOR.md`、`current/B/round2_B.md`、`synthesis/inspector_B_round2.md`。未读取 A 文件。

## Q1. 量纲校对

### 主候选式

`Delta lambda_hol(s,theta)=eta_l W_ell F_hol(s)[cos(theta)-1] + O(eta_l^2/r) + O(eta_l J/gamma)`

其中 `eta_l=|J_l|^2/gamma`，`r=2|J|^2/gamma`。

逐项量纲：

- 左边 `Delta lambda_hol`：`s^-1`。
- `J,J_l,gamma`：文中按角频率/率处理，均为 `s^-1`。
- `eta_l=|J_l|^2/gamma`：`(s^-1)^2/(s^-1)=s^-1`。
- `r=2|J|^2/gamma`：`s^-1`。
- `W_ell`：在 `L,ell` 为格点数的约定下无量纲。
- `F_hol(s)`：文中声明为无量纲。
- `[cos(theta)-1]`：无量纲，`theta` 为 Peierls holonomy/相位。
- `O(eta_l^2/r)`：`(s^-1)^2/(s^-1)=s^-1`。
- `O(eta_l J/gamma)`：`(s^-1)(s^-1)/(s^-1)=s^-1`。

判定：旧稿中的 `O(eta_l^2)`、`O(gamma^-2)` 量纲阻断已修复。当前余项量纲闭合。

### 相对误差写法

`Delta lambda_hol = K eta_l W_ell [cos(theta)-1] [1+O(eta_l/r)+O(J/gamma)]`

逐项量纲：

- `K`、`W_ell`、`cos(theta)-1`：无量纲。
- `eta_l`：`s^-1`。
- `eta_l/r`：无量纲。
- `J/gamma`：无量纲。

判定：相对误差写法量纲闭合。

### Conductance-residual 判据

`Q(s,theta)=Delta lambda(s,theta)-(partial_D lambda_SSEP)(s;D_0) Delta D(theta)`

逐项量纲：

- `Delta lambda`：`s^-1`。
- 若 `D` 为扩散常数，则 `partial_D lambda_SSEP` 为 `(s^-1)/[D]`。
- `Delta D` 为 `[D]`。
- 乘积为 `s^-1`，故 `Q` 为 `s^-1`。

判定：量纲匹配。

### `Delta_pi` 判据

`Delta_pi(s)=-2 eta_l W_ell F_hol(s)+O(eta_l^2/r)+O(eta_l J/gamma)`

判定：主项与余项均为 `s^-1`，量纲闭合。

### 超越函数自变量

- `cos(theta)`、`exp(i theta)`：`theta` 无量纲，合法。
- `log <exp(s Q_t)>`：文中采用 counting field 约定，`s` 与计数电荷归一化后无量纲，合法。

Q1 结论：通过。

## Q2. 符号/方向校对

极限代入：

- `theta=0 mod 2pi`：`cos(theta)-1=0`，相对无相位基线消失。
- `theta=pi`：`cos(pi)-1=-2`，故候选二阶式给出 `Delta_pi=-2 eta_l W_ell F_hol(s)`。
- `theta -> -theta`：`cos(theta)-1` 不变，偶性成立。
- `theta -> theta+2pi`：周期性成立。
- `J_l -> 0`：`eta_l -> 0`，shortcut 相位项消失。
- `gamma -> infinity` 且 `J_l` 固定：候选主项消失，符合强退相干抑制相干效应的方向。

方向风险复查：当前 B 明确说明 `[cos(theta)-1]` 的符号可吸收到 `F_hol` 或幅值定义中，`theta=pi` 相对 `theta=0` 的物理增减依赖 `F_hol(s)` 或各 cumulant 系数符号。没有把负号本身冒充为确定物理增减方向。

Q2 结论：通过。

## Q3. 循环论证校对

旧阻断点是：把 ansatz 自身当成已验证结论。

当前文本已经作出三处降级：

- 明确说 `|J_l|^2/gamma` 只是“候选最低阶”。
- 明确说若二阶 Zeno population generator 抹掉 Peierls 相位，则 holonomy 项必须升为更高阶闭合路径项。
- 明确说当前是判据设计，无实测数据，需要通过 `theta`、`J_l`、`gamma`、`ell/L`、`s` 或 cumulant order 扫描来判定。

可检验判据保留为：

- 偶周期相位结构。
- `theta=0 mod 2pi` 退化到无 holonomy 基线。
- 扣除由平均电流拟合出的 `D_eff(theta)` 后，高阶 cumulants 或完整 `s` 依赖中仍有非零偶周期残差 `Q(s,theta)`。
- 幅值对 `|J_l|` 与 `gamma` 的幂律决定真实最低阶。

判定：当前版本没有再把 `|J_l|^2/gamma` 的 holonomy 阶数作为已证结论；判据本身仍是可检验的，不构成循环论证阻断。

Q3 结论：通过。

## Q4. 量级鸿沟标记

本轮仍没有具体 `10^N` vs `10^M` 的数值量级比较，因此无传统数值量级鸿沟。

阶数鸿沟方面，当前 B 已显式标记：

- `eta_l=|J_l|^2/gamma` 是普通 shortcut incoherent rate，也是 holonomy 的候选最低阶。
- 若二阶投影只保留实跳率并抹掉相位，则真正 holonomy 幅值应替换为更高阶闭合路径速率，例如含 shortcut 与链段传播的 `J_l^2 J^m/gamma^{m+1}` 型项，或等价最短闭合相干路径阶数。
- 即使阶数升级，偶性、周期性、`theta=0` 退化和 conductance-residual 判据仍保留。

判定：旧稿的“未证明阶数”阻断已降级为明确待检假设；阶数鸿沟已被显式标记。

Q4 结论：通过。

## Q5. 代数验算与极限退化

### 小相位展开

`cos(theta)-1=-theta^2/2+theta^4/24+...`

代入：

`Delta lambda_hol=-0.5 eta_l W_ell F_hol(s) theta^2 + O(eta_l theta^4) + O(eta_l^2/r) + O(eta_l J/gamma)`

判定：符号、系数、量纲均正确。

### `theta=pi`

`cos(pi)-1=-2`

代入：

`Delta_pi(s)=-2 eta_l W_ell F_hol(s)+O(eta_l^2/r)+O(eta_l J/gamma)`

判定：代数正确；物理增减仍由 `F_hol` 或 cumulant 系数符号决定。

### 几何权重

`W_ell=(ell/L)(1-ell/L)L^-1`

在 `L,ell` 为格点数的约定下无量纲；`0<ell<L` 时为正，靠近边界或退化长度时变小。文本已说明该权重是候选访问/重合权重，不伪装成定理，并允许被 Green function 或 leverage score 替换。

判定：作为候选权重可接受。

### 强退相干极限

按候选二阶项，`gamma -> infinity` 给出 `eta_l -> 0`，相位项消失。文本没有用该极限证明首个非零阶必为 `gamma^-1`，而是要求用投影推导或数值幂律扫描判定。

判定：极限退化正确，未越界证明阶数。

Q5 结论：通过。

## Q6. 综合判定

✅ INSPECTOR 复审通过。

旧阻断项复查结果：

1. 余项量纲已闭合：`O(eta_l^2/r)` 与 `O(eta_l J/gamma)` 均为 `s^-1`，相对误差 `O(eta_l/r)`、`O(J/gamma)` 均无量纲。
2. `|J_l|^2/gamma` 阶数已从结论降级为候选最低阶/待检假设，并明确给出若 Zeno 投影抹掉相位则需升级到更高阶闭合路径速率。
3. 可检验判据得到保留：偶周期性、`theta=0` 退化、conductance-residual `Q(s,theta)`、`J_l/gamma` 幂律扫描、高阶 cumulants 或完整 `s` 依赖。
4. 当前文本没有把 conductance-residual 判据或二阶幅值冒充为已证实测结论；它们被表述为数值/投影推导需要检验的结构。

剩余非阻断警告：

- `W_ell` 的无量纲性依赖 `L,ell` 为格点数的约定；若后续改用物理长度，需补入 lattice spacing 或重定义权重。
- “holonomy correction 不能被单参数 conductance renormalization 完全吸收”这类表述应继续保持条件式：只有当 `Q(s,theta)` 在数值或推导中非零时才成立。

最终结论：B Round2 已修复 INSPECTOR 旧阻断，可继续推进；后续不得把 `eta_l=|J_l|^2/gamma` 阶数当作已证定理，只能作为待检最低阶候选使用。

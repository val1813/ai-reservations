# INSPECTOR B Round2

检查对象：`current/B/round2_B.md`

限制记录：本次只读取了项目 AGENTS、`ai/INSPECTOR.md`、`current/B/round2_B.md`。未读取 A 文件。

## Q1. 量纲校对

### 公式 1

`Delta lambda_hol(s,theta)=eta_l W_ell F_hol(s;rho_L,rho_R)[cos(theta)-1]+O(eta_l^2)+O(gamma^-2)`

`eta_l=|J_l|^2/gamma`

逐项量纲：

- 左边 `Delta lambda_hol`：`s^-1`，因为 `lambda=t^-1 log <exp(s Q_t)>`。
- `J_l`：若按角频率/跃迁振幅计，为 `s^-1`。
- `gamma`：退相干率，为 `s^-1`。
- `eta_l=|J_l|^2/gamma`：`(s^-1)^2/(s^-1)=s^-1`。
- `W_ell`：按文中定义 `(ell/L)(1-ell/L)L^-1`。若 `L,ell` 是无量纲格点数，则 `W_ell` 无量纲；若 `L` 是物理长度，则 `W_ell` 带 `length^-1`，会导致量纲错误。B 文中显然把 `L,ell` 当格点数，故在该约定下匹配。
- `F_hol`：声明为无量纲。
- `[cos(theta)-1]`：无量纲，且 `theta` 无量纲。

判定：主体乘积 `eta_l W_ell F_hol[cos(theta)-1]` 的量纲可为 `s^-1`，前提是 `L,ell` 为格点数且 `F_hol` 真为无量纲。

问题：

❌ 量纲错误：`O(eta_l^2)` 若按字面理解单位为 `s^-2`，不能直接加到 `Delta lambda_hol` 上。应写为 `O(eta_l^2/r_*)`、`O(|J_l|^4/gamma^3)`、或显式给出能把二阶小量恢复为 `s^-1` 的率标度。

❌ 量纲错误：`O(gamma^-2)` 若按字面理解单位为 `s^2`，不能直接加到 `Delta lambda_hol` 上。应写成带有相应振幅/率因子的项，例如 `O(J^4/gamma^3)`、`O(|J_l|^2 J^2/gamma^3)`，或改写为相对误差 `1+O((J/gamma)^2)`。

### 公式 2

`Q(s,theta)=Delta lambda(s,theta)-(partial_D lambda_SSEP)(s;D_0)Delta D(theta)`

量纲：

- `Delta lambda`：`s^-1`。
- 若 `D` 为扩散常数，则 `partial_D lambda_SSEP` 的单位为 `(s^-1)/[D]`。
- `Delta D` 的单位为 `[D]`。
- 乘积单位为 `s^-1`。
- `Q` 单位为 `s^-1`。

判定：量纲匹配。

### 公式 3

`Delta_pi(s)=-2 eta_l W_ell F_hol(s)+O(eta_l^2)`

判定：主项单位可匹配为 `s^-1`；但同公式 1，`O(eta_l^2)` 按字面量纲不匹配，需要补齐率标度。

### 超越函数自变量

- `cos(theta)`：`theta` 声明为 Peierls holonomy/相位，无量纲，匹配。
- `exp(i theta)`、`exp(-i theta)`：`theta` 无量纲，匹配。
- `log <exp(s Q_t)>`：若 `Q_t` 是计数电荷数或以基本电荷归一化的计数，则 `s Q_t` 无量纲，匹配。若 `Q_t` 保留物理电荷单位，则 `s` 必须有反电荷单位；B 文采用计数字段无量纲约定，可接受。

## Q2. 符号/方向校对

### `cos(theta)-1` 的方向

极限代入：

- `theta=0 mod 2pi`：`cos(theta)-1=0`，相对同强度 `theta=0` shortcut 基线消失。方向正确。
- `theta=pi`：`cos(pi)-1=-2`，所以 `Delta_pi=-2 eta_l W_ell F_hol(s)`。若 `eta_l>0` 且 `W_ell>=0`，方向完全由 `F_hol(s)` 的符号决定。
- 小相位：`cos(theta)-1=-theta^2/2+O(theta^4)`，故 `Delta lambda_hol=-0.5 eta_l W_ell F_hol theta^2+O(theta^4)`。该展开符号正确。
- `J_l -> 0`：`eta_l -> 0`，主项消失。
- `gamma -> infinity` 且 `J_l` 固定：`eta_l -> 0`，主项消失。

判定：

⚠️ 方向警告：B 文把 `[cos(theta)-1]` 的符号说成可吸收到 `F_hol`，这对形式书写可以，但不能同时给出确定的增减方向。`theta=pi` 相对 `theta=0` 是负主因子，最终增减取决于 `F_hol(s)` 或具体 cumulant 系数 `a_n` 的符号。当前文本中“同号残差”等方向性表达不能作为已证明结论。

### 偶性与周期性

- `cos(theta)-1` 是偶函数，满足 `theta -> -theta`。
- 周期为 `2pi`。
- `theta=0` 退化为基线。

判定：方向/对称性在形式上正确。

## Q3. 循环论证校对

检查到的验证链：

- 输入假设：存在 holonomy correction，且最低阶为 `eta_l W_ell F_hol(s)[cos(theta)-1]`。
- 提议验证：扫描 `theta`、`|J_l|`、`gamma`，寻找 `cos(theta)-1`、`|J_l|^2`、`gamma^-1` 标度。
- 当前数据状态：文本明确说“当前为判据设计，无实测数据”。

判定：

⚠️ 循环/未闭合警告：当前 INSPECTOR_CHECK 的“方向”和“最低阶”没有由独立推导或数值数据推出，而是把 ansatz 本身作为待检结构再写成命题。作为实验/数值判据设计可接受；作为 B Round2 的结论不可接受。

## Q4. 量级鸿沟标记

本轮没有具体 `10^N` vs `10^M` 数值比较，因此无传统量级鸿沟。

但存在阶数鸿沟：

- B 主命题采用 `O(|J_l|^2/gamma)`。
- 文末自己承认 A 可能反对：强退相干投影后 Peierls 相位可能在 `|J_l|^2/gamma` 中消失，真正相位依赖也许要到 `J_l^2 J^ell/gamma^ell` 或其他闭环相干传播阶数。

判定：

❌ 阶数鸿沟/未证明阶数：`O(|J_l|^2/gamma)` 是 ordinary incoherent shortcut rate 的自然阶数，但 holonomy 需要闭合路径相干比较。仅凭 `r_l=2|J_l|^2/gamma` 不能推出 AB holonomy 也在同一阶保留。若链段 `p -> q` 的相干振幅在强退相干投影中被压低，则最低非零 holonomy 阶数可能含有链段传播因子，主命题的阶数会改变。

建议修正：把“最低阶为 `|J_l|^2/gamma`”降级为待检假设，写成

`Delta lambda_hol = A_hol(s,L,p,q,gamma,J,J_l)[cos(theta)-1]`

并仅声明

`A_hol` 为偶周期 holonomy 振幅；其对 `J_l,J,gamma` 的最低非零阶数需由投影推导或数值幂律扫描决定。

## Q5. 代数验算与极限退化

### 小相位展开

`cos(theta)-1=-theta^2/2+theta^4/24+...`

代入：

`Delta lambda_hol= -0.5 eta_l W_ell F_hol(s) theta^2 + O(theta^4)`

判定：代数符号正确。

### `theta=pi` 代入

`cos(pi)-1=-2`

代入：

`Delta_pi(s)=-2 eta_l W_ell F_hol(s)+...`

判定：代数正确；但方向仍依赖 `F_hol` 符号。

### 几何权重退化

`W_ell=(ell/L)(1-ell/L)L^-1`

若 `ell=0` 或 `ell=L`，`W_ell=0`。若 `0<ell<L`，`W_ell>0`，中间更大、边界变小。

判定：形式退化合理。但 `ell=L` 对开链 shortcut 的几何含义需谨慎，不能把该猜测权重当定理。

### 强退相干极限

若按 B 的主项，`gamma -> infinity` 给出 `Delta lambda_hol -> 0`。这符合退相干抑制 AB 相干的物理方向。

阻断点：该极限只说明主项会消失，不证明主项的首个非零阶是 `gamma^-1`。强退相干下 holonomy 可能比 ordinary shortcut rate 多受相干闭环传播压制。

## Q6. 综合判定

⛔ INSPECTOR阻断：B Round2 的主公式主体量纲在约定下可自洽，`cos(theta)-1` 的偶性、周期性、`theta=0` 退化和小相位展开也正确；但 `O(eta_l^2)` 与 `O(gamma^-2)` 的写法量纲不合法，且最关键的 `Delta lambda_hol ~ |J_l|^2/gamma [cos theta-1]` 被写成最低阶结论时缺少推导支撑。

必须修正后再继续：

1. 把所有 dimensionful big-O 改成带率标度的表达，或改成明确的相对误差。
2. 把 `O(|J_l|^2/gamma)` holonomy 阶数从“结论”降级为“待检假设/数值判据”。
3. 明确 `theta=pi` 相对 `theta=0` 的增减方向依赖 `F_hol` 或 cumulant 系数符号，不能只由 `[cos theta-1]` 给出物理方向。
4. 在强退相干投影中补充闭环相干路径的阶数推导；若推导不支持 `gamma^-1`，则主命题应改为更一般的 `A_hol[cos(theta)-1]`，再由幂律扫描确定 `A_hol` 的阶数。

结论：不可把当前 B Round2 的 `|J_l|^2/gamma` holonomy 最低阶作为后续推导基础；可保留偶周期、基线消失、conductance-residual 判据作为待检结构。

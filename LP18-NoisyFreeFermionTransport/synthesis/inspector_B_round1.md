# INSPECTOR B round1

检查对象：`current/B/round1_B.md` 中 3 个 `INSPECTOR_CHECK` 块及相关公式/方向结论。

## Q1. 量纲校对

### CHECK 1

- `Phi_C = sum_{e in C} a_e mod 2pi`
  - 左边 SI 单位：无量纲角变量
  - 右边 SI 单位：`a_e` 必须为无量纲角变量，`2pi` 无量纲
  - 匹配：通过
- `Delta lambda(s) = lambda_G(s,Phi_C) - lambda_SSEP(s) = A(G,gamma,J)[1-cos(Phi_C)]F(s)+o(A)`
  - 左边 SI 单位：`s^-1`
  - 右边 SI 单位：`A * 无量纲 * F(s)`；若 `F(s)` 无量纲，则 `A` 必须为 `s^-1`
  - 匹配：条件通过。当前块只声明 `lambda` 与 `Phi_C` 单位，未显式声明 `A` 和 `F(s)` 单位。
- 超越函数：`cos(Phi_C)` 自变量无量纲，通过。

### CHECK 2

- `b1(G)=|E|-|V|+1`
  - 左边 SI 单位：无量纲计数
  - 右边 SI 单位：无量纲计数
  - 匹配：通过，但只对连通图成立；一般图应为 `|E|-|V|+c`。
- `Delta lambda_top(s) ~ L^-1 (ell/L)(1-ell/L)(|J_l|^2/gamma)[1-cos theta]F(s)`
  - 左边 SI 单位：`s^-1`
  - 右边 SI 单位：无量纲几何因子乘 `|J_l|^2/gamma`。若 `J_l` 与 `gamma` 均为速率，则 `|J_l|^2/gamma` 为 `s^-1`，`F(s)` 必须无量纲
  - 匹配：通过。
- 超越函数：`cos(theta)` 自变量无量纲，通过。

### CHECK 3

- `Var_sample[lambda(s)] ~ b1(G) Var(Phi_C)/L^2`
  - 左边 SI 单位：`s^-2`
  - 右边 SI 单位：`b1` 无量纲，`Var(Phi_C)` 无量纲，`L^2` 若为长度计数/系统尺寸因子则无量纲；整体无量纲
  - 匹配：不通过。
  - 阻断：量纲错误。建议修正为带速率幅度平方的形式，例如 `Var_sample[lambda(s)] ~ K^2 b1(G) Var(Phi_C)/L^2`，其中 `K` 的单位为 `s^-1`；或显式说明该式是在归一化后的 `lambda/K` 上成立。
- `chi=b1(G)/N_noise_constraints`
  - 左边 SI 单位：无量纲
  - 右边 SI 单位：无量纲计数/无量纲计数
  - 匹配：通过。

## Q2. 符号/方向校对

- CHECK 1 方向：`Phi_C=0 mod 2pi` 时 `[1-cos(Phi_C)]=0`，修正消失，退回 exact sector/SSEP 等价；非零 holonomy 时修正非负出现。方向与结论一致。
- CHECK 2 方向：`J_l=0` 或 `theta=0 mod 2pi` 时修正为零；弱 shortcut 下最低非零项为 `|J_l|^2` 且对 `theta` 为偶函数，方向一致。
- CHECK 2 多 shortcut 方向：按独立 cycle 数或 cycle basis 加权相加只在弱耦合、cycle 近似独立、交叉项可忽略时成立；当前假设中未充分标注交叉项条件。
- CHECK 3 方向：若补上速率幅度平方，则 `b1` 增大或 `Var(Phi_C)` 增大导致样本方差增大；`b1~L` 时标度为 `1/L`。方向本身一致，但建立在阻断公式修正之后。

## Q3. 循环论证校对

- CHECK 1/2 的验证数据声明主要来自项目已有 R1/C2 边界与本轮 ansatz，没有外部新数据；当前结论是候选理论结构，不是独立验证。未发现把由假设生成的数据反过来当作实证验证的循环论证。
- CHECK 3 明确是跨学科结构映射和弱相关近似假设，不是实测验证。未发现循环论证，但应保持为 ansatz/假说级。

## Q4. 量级鸿沟标记

- 未发现 `10^N` vs `10^M` 的显式数量级比较。
- `b1~L` 导致 `Var~1/L` 的标度推断可读，但受 CHECK 3 量纲错误影响，不能作为未归一化 `lambda` 方差公式使用。

## Q5. 代数验算

- `b1(G)=|E|-|V|+1`：对连通图成立；若 B 文件将其写成任意图公式，需要加连通性条件或改为 `|E|-|V|+c`。
- `1-cos(theta)`：小 `theta` 极限为 `theta^2/2`，满足偶函数、无线性项；`theta=0 mod 2pi` 退化到零修正。
- `Delta lambda_top`：在 `J_l -> 0`、`theta -> 0 mod 2pi`、`ell/L -> 0 or 1` 时均退化为零；方向与公式一致。
- `Var_sample[lambda]`：代数结构的标度方向可行，但未包含 `lambda` 的速率尺度，量纲不闭合。
- 数值来源：无具体数值估算；无需执行数值量级验算。

## Q6. 综合判定

阻断：

- 量纲错误：`Var_sample[lambda(s)] ~ b1(G) Var(Phi_C)/L^2`。左边为 `s^-2`，右边为无量纲。必须补入速率幅度平方、具体 `K_alpha(s)^2` 类型因子，或声明该式适用于归一化后的无量纲 `lambda`。

警告：

- `b1(G)=|E|-|V|+1` 需显式限定 `G` 连通；一般图为 `|E|-|V|+c`。
- CHECK 1 中 `A(G,gamma,J)` 与 `F(s)` 的单位应显式标注：`A` 为 `s^-1`、`F(s)` 无量纲，或给出等价归一化。
- 多 shortcut 修正按 cycle basis 独立相加需要弱耦合/低密度/交叉项可忽略条件。

是否通过：不通过。存在 1 个阻断量纲错误；修正后可重新提交 INSPECTOR。

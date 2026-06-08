# INSPECTOR A Round 1

检查范围：仅检查 `current/A/round1_A.md` 中两个 `INSPECTOR_CHECK` 块及其直接相关公式/方向结论。未读取 B 文件。

## Q1. 量纲校对

### CHECK-1: tilted CGF 边界表达式

公式：
`lambda(s)=sum_sigma Gamma_{R,sigma}(e^{-sigma s}-1)(delta_{sigma,1}-sigma E_infty[(G_s)_{L,L}])`

- 左边 SI 单位：`time^{-1}`，因为 `lambda(s)=lim_{t->infty} t^{-1} log ...`。
- 右边 SI 单位：`Gamma_{R,sigma}` 为 `time^{-1}`；`e^{-sigma s}-1` 无量纲；`delta_{sigma,1}`、`sigma`、`E[(G_s)_{L,L}]` 无量纲。因此右边为 `time^{-1}`。
- 匹配：通过。
- 超越函数自变量：`-sigma s` 必须无量纲；counting field `s` 无量纲，`sigma=+-1` 无量纲，通过。

关于 `tilde lambda=(gamma L/2)lambda`：若 `gamma` 表示 dephasing rate，SI 单位通常为 `time^{-1}`，则 `(gamma L/2)lambda` 的单位为 `time^{-2}`，不是无量纲。若 R1 采用的是在重标度时间/无量纲 rate 下定义的 `lambda`，需要显式说明该约定；否则该句存在量纲风险。

### CHECK-2: long-range Zeno 有效跃迁率

公式：
`r_{j,k} ~ |J_{j,k}|^2/gamma = J0^2/(gamma |j-k|^{2alpha})`

- 左边 SI 单位：`time^{-1}`。
- 右边 SI 单位：若 `J_{j,k}` 是 Hamiltonian hopping amplitude，取 `hbar=1` 时单位为 `time^{-1}`；`gamma` 为 `time^{-1}`，故 `|J|^2/gamma` 为 `time^{-1}`。
- 匹配：通过。
- 超越函数自变量：无。

二阶矩条件：
`sum_r r^2 r^{-2alpha}<infty` 等价于 `sum_r r^{2-2alpha}<infty`。一维无穷和收敛要求 `2-2alpha < -1`，即 `alpha>3/2`。通过。

## Q2. 符号/方向校对

### CHECK-1

方向结论：transport CGF 从 reservoir counting field 降为 tilted correlation matrix 的边界密度问题；有限 `L` 仍未闭合。

- 极限 `s->0`：`e^{-sigma s}-1 -> 0`，因此 `lambda(0)=0`，符合 CGF 基本要求。
- 有限 `L`：公式依赖 `E_infty[(G_s)_{L,L}]`，而 A 文件已声明 `G_s` obeys nonlinear SDE/moment hierarchy，有限 `L` 的 `lambda(s)` 仍需解 hierarchy。方向“有限 L 仍未闭合”正确。
- 降维方向：表达式把 trace growth/CGF 写为右边 reservoir 边界占据 `G_LL` 的函数；方向正确。

未发现方向反转。

### CHECK-2

方向结论：长程 hopping 的最小增量先改变 hydrodynamic universality class：diffusive Laplacian -> fractional generator。

- `alpha>3/2`：`sum_r r^2 r^{-2alpha}` 收敛，有限二阶矩，预期普通扩散/Laplacian 标度可保留。
- `1<alpha<3/2`：二阶矩发散；按 long-jump exclusion 传统写法 `p(r)~|r|^{-1-mu}`，由 `2alpha=1+mu` 得 `mu=2alpha-1`，于是 `1<mu<2`，对应 superdiffusive/fractional generator。
- `alpha<=1`：`mu<=1`，非局域性更强，局域 bond-current gauge 描述更可疑。

方向与极限检验一致，未发现方向反转。

## Q3. 循环论证校对

CHECK-1 的验证数据来自 R1 Eq. (5)-(9) 与 standard Markovian Lindblad counting-field construction；其结论是把 R1 公式链重述为边界密度表达，并承认有限 `L` 未闭合。未发现用结论生成验证数据的循环。

CHECK-2 的验证数据来自 R1 quasi-local/open-question 声明、R8 的 `alpha_c approx 1.5` 数值结果，以及 R9/R10 long-jump exclusion/fractional hydrodynamics 文献。`r_eff~|J|^2/gamma` 是输入假设之一，不是已由 A 文件独立证明的结果；但 A 文件已在 `[假设]` 中显式标明。未构成循环论证，但该假设是后续必须证明或校准的关键前提。

## Q4. 数量级鸿沟标记

- CHECK-1：未给出 `10^N` vs `10^M` 类型数量级比较。
- CHECK-2：未给出 `10^N` vs `10^M` 类型数量级比较。

无数量级鸿沟标记。

## Q5. 代数验算

### 5a. 逐步展开

CHECK-1：
- `lambda(0)=0`：直接由指数因子为零得到，正确。
- 量纲展开正确，除 `tilde lambda=(gamma L/2)lambda` 的“无量纲”说法需澄清归一化约定。

CHECK-2：
- `J_{j,k}=J0/|j-k|^alpha`。
- `|J_{j,k}|^2/gamma=J0^2/(gamma |j-k|^{2alpha})`，指数与系数关系正确。
- 二阶矩：`sum_r r^2 p(r)` with `p(r)~r^{-2alpha}` gives `sum_r r^{2-2alpha}`；收敛条件 `2-2alpha<-1` gives `alpha>3/2`，正确。
- 与 `p(r)~|r|^{-1-mu}` 对齐：`2alpha=1+mu`，故 `mu=2alpha-1`，正确。

### 5b. 极限退化

CHECK-1：
- `s=0` 退化到 `lambda(0)=0`，通过。
- 有限 `L` 极限不闭合，因为仍依赖 tilted hierarchy 的边界期望，方向通过。

CHECK-2：
- `alpha->infty`：长跳快速衰减，二阶矩有限，退回 quasi-local/diffusive 方向。
- `alpha=3/2`：`sum_r r^{-1}` 临界发散，应为边界临界情形；A 文件把硬阈值写为 `alpha>3/2`，正确。
- `alpha<3/2`：二阶矩发散，fractional/superdiffusive 方向成立。

### 5c. 数值量级验证

CHECK-1：无具体数值估算。

CHECK-2：`alpha_c approx 1.5` 与二阶矩阈值 `alpha=3/2` 同一数量级且数值一致。该比较依赖 R8 的数值临界和 Zeno rate 假设，适合作为方向支持，不是完整证明。

### 5d. 引用数值来源级别

- `alpha_c approx 1.5`：已标注 R8 arXiv:2310.01323v2 / PRB 109, 165408，来源充分。
- `alpha>3/2`：由本地代数收敛条件推出，不需要外部数值来源。
- R9/R10 作为 fractional/long-jump exclusion 背景来源已标注。

## Q6. 综合判定

阻断：无。

警告：
1. `tilde lambda=(gamma L/2)lambda` 被称为“无量纲”存在量纲约定不清。若 `gamma` 和 `lambda` 都按物理时间计量，该组合不是无量纲；需要改写为“在 R1 的重标度时间/无量纲 rate 约定下为 rescaled CGF”，或明确 `lambda` 已按相反时间单位归一化。
2. `r_{j,k}~|J_{j,k}|^2/gamma` 是合理的 strong-dephasing Golden-rule/Zeno 标度，但当前 A 文件只是把它列为假设，尚未在本轮证明。可继续，但 Round 2 若以此为核心，应先从 microscopic tilted generator 或 Schrieffer-Wolff/Zeno projection 推导。

结论：INSPECTOR 警告通过。A Round 1 可继续，但上述两个点必须显式标注；不存在需要阻断后续推导的量纲、方向或代数错误。

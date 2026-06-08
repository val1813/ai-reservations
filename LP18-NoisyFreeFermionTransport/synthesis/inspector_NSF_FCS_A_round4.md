# INSPECTOR NSF-FCS-1 Round 4 - A博士校对

输入文件：`current/A/NSF_FCS_round4_A.md`

校对范围：量纲、符号/方向、循环论证、数量级、代数/极限。

## 1. `A_R(L)=kappa sum d^(-alpha)` 渐近

结论：通过。

- 公式行 26：`A_R(L)=sum_x r_R(x)=kappa sum_{d=1}^L d^(-alpha)`。若 lattice distance `d` 无量纲，则 `kappa` 单位为 `s^-1`，左右均为 `s^-1`。
- 行 30：`alpha>1` 时
  `sum_{d=1}^L d^(-alpha)=zeta(alpha)-L^(1-alpha)/(alpha-1)+O(L^(-alpha))`。
  符号正确，因为尾和 `sum_{d>L} d^(-alpha) ~ L^(1-alpha)/(alpha-1)` 被从 `zeta(alpha)` 中减去。
- 行 31：`alpha=1` 给 `log L+O(1)`，要求 `L` 作为 lattice site count 无量纲；自洽。
- 行 32：`0<alpha<1` 给 `L^(1-alpha)/(1-alpha)+O(1)`，主阶正确。
- 方向行 34、122：未缩放且 `alpha>1` 时 activity 为 `O(1)`，不随一个趋零的 `G_R(L)` 自动变小；方向正确。

## 2. bare right reservoir exchange 的 coboundary

结论：通过。

采用 A 文中的约定 `q_R(R,x)=+1`、`q_R(x,R)=-1`，并取 `psi(R)=1`、`psi(x)=0`：

- 对 `R -> x`：`q_R+psi(x)-psi(R)=1+0-1=0`。
- 对 `x -> R`：`q_R+psi(R)-psi(x)=-1+1-0=0`。

因此 `q_R(i,j)=psi(i)-psi(j)`，行 54 的
`Q_t=psi(X_0)-psi(X_t)` 符号正确。有限状态下 `Q_t` 有界，所以行 58 的
`lambda_R''(0)=lim_{t->infty} t^(-1) Var(Q_t)=0`
方向正确。该结论只适用于 A 明确限定的 bare/right-only exchange 计数；若另行定义 transported current，则不是同一个 observable。

## 3. 加远端 Dirichlet sink 后的 `D_R` 与 capacity

结论：警告。

行 74 的
`D_R(L)=sum_x r_R(x)[1-u(x)]^2`
若 `u(R)=1,u(0)=0`，且 `1-u(x)` 表示从 landing site 先到远端 `0` 的 harmonic escape probability，则量纲为 `s^-1`，平方项无量纲。

行 78-88 的方向：`D_R(L) <= Cap(R,0)=E(u,u)` 在同一 Dirichlet-form 归一化下方向正确，因为 `D_R` 只是 reservoir-edge energy contribution，而 `E(u,u)` 还包含 bulk-edge 非负贡献。注意若 Dirichlet form 使用有向边 `1/2` 约定，等式/不等式可差一个固定因子；不影响方向和标度判断。

但不能机械推出等号，也不能机械推出同阶。极限反例：单位 conductance 的一维串联链 `R-1-2-...-n-0` 中，harmonic slope 为 `1/(n+1)`，右端 reservoir-edge energy 为 `D_R=1/(n+1)^2`，而 `Cap(R,0)=1/(n+1)`，故 `D_R/Cap=1/(n+1)->0`。所以行 90、112、136 的 `D_R asymp Cap` 只能作为额外 lemma/条件，不能由 Dirichlet 原理本身推出。

符号补充：若继续使用 `u(R)=1,u(0)=0`，escape-to-sink weight 是 `1-u(x)`；写成 `u(x)^2` 只有在同时交换边界值定义、令新势为 sink potential 时才等价。单纯反转 current 符号只会改变 residual 的正负，不会把 `1-u` 变成同一 `u`。

## 4. KILL / CONDITIONAL KEEP 逻辑

结论：通过但带条件警告。

- 行 104-108 的 KILL bare 强命题不循环：输入是显式计数约定，输出是 telescoping coboundary，独立于 `G_R` 假设。
- 行 110-114 的 CONDITIONAL KEEP 没有被当作已证明定理；A 已显式写出依赖未证 lemma。因此当前文本不构成循环论证。
- 但若后续 PI 把 `lambda_transport''(0) asymp D_R(L) asymp Cap(R,0)` 当作已验算事实使用，而没有独立证明/数值台账验证 `D_R/Cap` 稳定，则会变成循环使用目标结论。

## 5. 数量级与极限

- 未出现 `10^N` vs `10^M` 的具体量级比较；无数量级鸿沟可标。
- 关键极限 `alpha>1`、`alpha=1`、`0<alpha<1` 退化正确。
- `G_R(L)->0` 而 `A_R(L)=O(1)` 的方向不冲突；它只说明若 FCS 二阶量缩小，必须来自 corrector residual/cancellation，而不是 activity 小。

## 综合判定

⚠️ INSPECTOR警告，可继续。

通过项：`A_R(L)` 渐近正确；bare right exchange 作为 occupation coboundary 的符号和 `lambda_R''=0` 自洽；KILL bare 强命题不循环。

警告项：远端 Dirichlet sink 后只能机械保证 `D_R(L)` 是 `Cap(R,0)=E(u,u)` 的 reservoir-edge 非负部分，方向为 `D_R <= Cap`（至多差固定归一化因子）。`D_R asymp Cap` 和 `lambda_transport'' asymp Cap` 必须保留为未证 conditional lemma，不能写成已由 Dirichlet 原理推出的等号或自动同阶。

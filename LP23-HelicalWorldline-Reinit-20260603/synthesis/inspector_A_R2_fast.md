# INSPECTOR_A R2 快通道校对

## Q1 量纲校对

- `B_ab=q_a^c q_b^d nabla_d k_c`：若 `k^a=dx^a/dlambda` 且 `lambda` 取长度量纲，则 `nabla k` 为 `m^-1`，投影张量 `q` 无量纲，故 `B_ab` 为 `m^-1`。匹配。
- `B_ab = theta q_ab + sigma_ab + omega_ab`：`q_ab` 无量纲，因此 `theta, sigma_ab, omega_ab` 均需为 `m^-1`。匹配。
- `A'=A+dpsi`：`psi` 是角变量，`dpsi` 作为 1-form 与 `A` 同量纲；沿路径积分后为无量纲角度 rad。匹配。
- `Delta chi'=Delta chi+psi_f-psi_i`：三项均为角度 rad。匹配。

## Q2 符号/方向校对

- `A'=A+dpsi` 的正号依赖 screen basis 旋转约定和连接定义。例如若采用 `e_1+i e_2 -> e^{i psi}(e_1+i e_2)` 且 `A=e_1·nabla e_2`，正号可成立；若旋转矩阵或连接定义反向，则变为 `A-dpsi`。
- “未固定端点 tetrad 的 holonomy 是 screen SO(2) 规范项，不能自然唯一等同 optical twist”方向正确。

## Q3-Q5

- 未发现循环论证。
- 无数量级估算。
- 极限退化通过：`psi=const`、闭合回路 `psi_f=psi_i`、Minkowski 直线 `omega=0` 下结论方向正确。

## Q6 综合判定

警告，无阻断。

需显式固定：

1. `theta` 是 `1/2 q^{ab}B_ab` 还是 `q^{ab}B_ab`。
2. screen 旋转与连接 `A=e_1·nabla e_2` 的符号约定。

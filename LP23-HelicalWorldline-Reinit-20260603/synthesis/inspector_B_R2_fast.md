# INSPECTOR_B R2 快通道校对

## Q1 量纲校对

- `O_beta[gamma] = F_beta(H[gamma])`：`H[gamma]` 为无量纲/群值 holonomy，`F_beta` 输出到 observable 空间。匹配。
- `R_{beta beta'}[gamma] = O_beta[gamma] - O_beta'[gamma]`：有条件通过。必须显式要求 `O_beta` 与 `O_beta'` 已投到同一 observable 空间/同一分量/同一校准约定下。
- `rad` 在 SI 中无量纲但可作为角变量标记；Stokes 参数需使用归一化或同一强度归一约定。

## Q2-Q5

- 方向结论为条件命题：若 `beta` 改变导致不可规范消去的 `R != 0`，则唯一自然桥失效。逻辑方向成立。
- 未发现循环论证。
- 无数量级估算。
- `beta=beta'` 与 `F_beta=F_beta'` 极限下 `R=0`，退化正确。

## Q6 综合判定

警告，无阻断。

需补充：`O_beta` 与 `O_beta'` 的差值默认经过同一实验校准和公共 observable 空间中的比较；若读出空间不同，应先引入比较映射后再定义 `R`。

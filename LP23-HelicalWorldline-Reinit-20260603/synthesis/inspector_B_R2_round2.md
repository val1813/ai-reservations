# INSPECTOR_B R2 Round2 校对

判定：警告，不阻断。

主要警告：

1. `T_standard` 模板列来自不同特征量，脚本未显式记录列系数单位或归一化约定；作为“列空间模板”可用，但不能把列数值幅度解释为物理强度。
2. endpoint invariance check 只验证 endpoint 扰动，不验证 spinoptics/local template 的物理完备性。
3. `orthonormal_column_basis()` 用固定绝对阈值 `1e-12` 且无 pivot/reorthogonalization；当前 toy 可用，但不能作为病态矩阵下的稳健 rank-revealing 证明。
4. 报告中 `projection_residual` 有时指 norm，脚本变量中指 residual vector；需用 `projection_residual_norm` 表示 norm。

无量纲、方向、循环、代数阻断。

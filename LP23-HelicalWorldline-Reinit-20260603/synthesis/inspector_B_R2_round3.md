# INSPECTOR_B R2 Round3 校对

判定：警告，不阻断。

主要警告：

1. random nuisance adversarial test 无循环。
2. `nonlocal_history_template` 部分使用 residual 构造 history 列，因此是后验 adversarial counterexample，不是独立预注册物理模板。
3. rank/residual/tolerance 方向正确；`k=1` random nuisance 与 nonlocal_history 将 residual 压到机器精度零的代数通过。

无阻断。

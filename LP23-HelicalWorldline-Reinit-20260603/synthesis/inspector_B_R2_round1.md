# INSPECTOR_B R2 Round1 校对

判定：警告通过，不阻断。

- `S_{beta beta'}(Gamma)=sum_e s_e R_{beta beta'}[e]` 量纲通过，`S` 与 `R` 同量纲。
- endpoint calibration `r_e -> r_e + a_target(e)-a_source(e)` 在闭合回路中严格抵消。
- `H^1(network,O)=ker d_1 / im d_0` 写法在有 2-cells 时完整；纯图时应理解为 `C^1/im d_0`。
- `||B r||` 与 `||(I-DD^+)r||` 都可检测非 coboundary，但数值不一定等价，除非 `B` 行为左零空间正交归一基。
- 非交换版本中 `log Omega_Gamma` 只适用于近恒等、固定 log 分支或 Abelian 极限；一般应保留 `Omega_Gamma`、`Tr(Omega_Gamma)` 或 eigenphase。

修正要求：显式说明 cycle 矩阵符号约定和归一化；后续脚本优先输出正交投影残差 `||(I-DD^+)r||`；非交换模型暂不取 `log` 作为主对象。

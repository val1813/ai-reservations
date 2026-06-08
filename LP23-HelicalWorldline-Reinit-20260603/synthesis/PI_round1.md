# PI 综合 round1

## 输入

- A博士：`current/A/round1.md`
- B博士：`current/B/round1.md`
- INSPECTOR(A)：`synthesis/inspector_A_round1.md`，通过，无阻断；警告：可成立重表述依赖 `rho=ct`，不能反写成固定半径螺旋生成光锥。
- INSPECTOR(B)：`synthesis/inspector_B_round1.md`，通过，无阻断；警告：spinor 二次量需物理定标，contact form 需归一化，3+1 维数论证不能误用于 2+1。

## 汇合判断

A/B 独立汇合：原始 LP23-S1 按“单位/固定半径螺旋包络面严格等价光锥”表述被击穿。

共同理由：

1. 单条螺旋是 1D 曲线，不是光锥面。
2. 固定半径螺旋族给出圆柱 `X^2+Y^2=ell^2`，不是光锥 `X^2+Y^2=c^2t^2`。
3. 即使切向速度满足 null 条件，也只得到 null 曲线，不得到整个 null cone。
4. `Re/Im` 是无量纲相位分量，必须额外给长度尺度；尺度如何给出决定命题真假。

## 互补判断

A 给出的可存活重表述：

> 在 2+1 平坦 Minkowski 中，若 `e^{i alpha}` 只作为 null 方向标签，并额外设 `rho=ct`，映射 `(t,alpha)->(t,ct cos alpha,ct sin alpha)` 的像严格等于未来光锥。若写 `alpha=omega t+phi`，`omega` 只是坐标剪切；null 母线仍是 `alpha` 常数。

B 给出的可存活重表述：

> 在 3+1 中，光锥可由二分量 spinor 的 Hopf/null-spinor 映射 `k^mu=xi^\dagger sigma^mu xi` 严格生成；整体 `U(1)` 相位是纤维冗余或 connection holonomy，不是物理横向坐标。

两者互补：A 是 2+1 光锥截面的最低维严谨版本；B 是 3+1 Lorentz 协变版本的自然数学语言。

## K 条目

K1（否定）：固定半径单位螺旋或其相位平移族不等价于光锥；其自然集合是圆柱，除非额外把半径改为 `rho=ct`。

K2（边界）：`e^{iθ}` 可作为 null 方向标签或 `U(1)` 纤维变量保留，但不能直接把 `Re/Im` 当作物理空间坐标；必须声明尺度、截面和 Lorentz 变换规则。

K3（新方向）：LP23 的更可存活主线应从“螺旋包络”切换为“相位纤维/自旋子商空间导出光锥”：2+1 用 `rho=ct` 的相位方向圆；3+1 用 `k^mu=xi^\dagger sigma^mu xi`。

K4（下一轮卡点）：普通量子相位 `θ=(Et-p·x)/hbar` 是 Lorentz 标量，而 null 方向角 `alpha` 在 boost 下发生 aberration。若 LP23 要把两者识别，必须给出额外结构 `alpha=f(θ,p^mu,e_a^mu)` 或承认相位只作为 connection/holonomy。

## 停止条件检查

- 当前轮次：第1轮。
- 是否硬停止：否。原始 S1 被击穿，但 A/B 同时给出可存活重表述，不满足“无路可走”的硬停止。
- N<3 且未硬停止：禁止收官，继续第2轮。

## 第2轮指令

A博士第2轮：

- 检验 `θ=(Et-p·x)/hbar` 与 null 方向角 `alpha` 的 Lorentz 变换兼容性。
- 在 2+1 或 3+1 明确 boost 下写出 aberration 公式，并判断是否存在自然映射 `alpha=f(θ,p^mu,e_a^mu)`。
- 必须保持 round1 边界：不允许把固定半径螺旋重新写成光锥。

B博士第2轮：

- 转向 twistor/null geodesic congruence/contact lift。
- 检验“螺旋”是否可解释为 null congruence 的 Reeb/contact lift，而不是 spacetime 曲线本体。
- 给出可检验判据：整体 `U(1)` 相位不改变 null 方向；只有 holonomy/相对相位/spinor bilinear 改变可观测量。

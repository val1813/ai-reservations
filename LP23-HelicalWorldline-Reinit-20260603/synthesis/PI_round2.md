# PI 综合 round2

## 输入

- A博士：`current/A/round2.md`
- B博士：`current/B/round2.md`
- INSPECTOR(A)：`synthesis/inspector_A_round2.md`，通过，无阻断；警告：`omega` 的频率尺度约定需澄清，且后续必须统一 `(+---)` 与 `(-+++)` 号差。
- INSPECTOR(B)：`synthesis/inspector_B_round2.md`，通过，无阻断；警告：Pauli bilinear 的 `n_y` 符号依赖 `sigma_y/phi` 约定，后续涉及手征/旋转方向前必须补约定。

## 汇合判断

A/B 独立汇合：LP23 的强版本 `θ=α` 被证伪。

- A 路线：量子动力学相位 `θ=(Et-p·x)/hbar` 是 Lorentz 标量；null 方向角 `alpha` 在 boost 下按 aberration 变换。无额外结构的 `alpha=f(theta)` 不协变。
- B 路线：整体 `U(1)` 相位是 spinor/twistor/contact 总空间的纤维变量；它不改变 null 方向。若改动相对相位，则改变 null direction，但平直自由 null geodesic 条件会失败，除非引入联络/外场/曲率。

## 互补判断

两条路径共同给出 LP23-S1' 的可存活形式：

> 光锥不是 spacetime 固定半径螺旋的包络，也不是量子相位值 `θ` 的直接投影；它由 null vector/projective spinor/contact lift 给出。`e^{iθ}` 若要进入物理，只能通过 `dθ -> p_mu/hbar`、spinor bilinear、相对相位或 connection holonomy。

## 新 K 条目

K5（否定）：`θ=α` 不协变。`θ` 是 Lorentz 标量，`α` 是 observer celestial angle；boost 下 `α` obeys aberration。

K6（边界）：`α` 可由 `p_mu` 与 observer tetrad 读出，例如 `atan2(p·e_2,p·e_1)`，但实际用的是相位梯度/四动量，不是相位值。

K7（contact/twistor 存活版）：整体 `U(1)` 相位不改变 `k^mu=xi^dagger sigma^mu xi`；可观测方向由 projective spinor `[xi]` 或 bilinear 决定。局部整体相位只有作为 holonomy/相对相位时可能进入可观测量。

K8（下一轮卡点）：如果“螺旋/扭转”还要保留，必须从 spacetime 螺旋改写为 null congruence 的 optical twist、spin connection curvature 或 twistor/contact holonomy。

## 停止条件检查

- 当前轮次：第2轮。
- 是否硬停止：否。强版本已证伪，但 weak/contact/twistor 版本仍有可探索方向。
- N<3 且未硬停止：禁止收官，继续第3轮。

## 第3轮指令

A博士第3轮：

- 检验“螺旋/扭转”能否被严格改写为 null congruence 的 optical scalar（twist/expansion/shear）。
- 写出 `B_ab = q_a^c q_b^d nabla_d k_c` 的分解，判断 twist 是否可由平直自由 single null generator 产生。
- 重点判定：LP23 是否至少需要 congruence、联络或曲率，才能保留“螺旋”物理含义。

B博士第3轮：

- 从 contact/twistor holonomy 继续，寻找“相位联络曲率 = congruence twist/optical data”的可检验映射或强反例。
- 若无法建立映射，给出最小降级命题。

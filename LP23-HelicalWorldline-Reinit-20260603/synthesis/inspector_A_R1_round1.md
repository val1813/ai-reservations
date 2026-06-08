# INSPECTOR_A R1 Round1

检查对象：`current/A/R1_round1.md`

## Q1. 量纲校对

- `k^{AA'}=\xi^A\bar\xi^{A'}`：纯相位变换 `\xi^A \mapsto e^{i\phi}\xi^A` 下 `k^{AA'}` 不变，代数正确。
- `S=k^\perp/\langle k\rangle`、`B_{AB}=q_A{}^a q_B{}^b\nabla_b k_a`、`\omega_{AB}=B_{[AB]}`：对象分层一致；若 `k^a` 取 affine 规范，则 `\omega_{AB}` 量纲为 `L^{-1}`，成立。
- 对 `F_{AB}=\chi\omega_{AB}` 的量纲核对：若 `A` 取常见无量纲 `U(1)` connection 规范，则 `F=dA` 为 `L^{-2}`，需额外 `\chi` 才可能与 `\omega_{AB}` 比较。本文“强版不闭合”的判断可成立。

## Q2. 符号/方向校对

- `k^a \mapsto f k^a` 下，screen-projected optical tensor 的 `(\nabla f)\otimes k` 项被投影杀掉，故 `B_{AB}` 与 `\omega_{AB}` 按 `f` 缩放；文中方向判断正确。
- 反例 A：`k=\partial_t+\partial_z` 在 Minkowski 中 twist-free，且给定 `A=(B/2)(x\,dy-y\,dx)` 时 `F=B\,dx\wedge dy\neq 0`，故可得 `F\neq 0` 而 `\omega_{AB}=0`；方向判断正确。

## Q3. 循环论证校对

- 未发现“先假设 phase curvature = optical twist，再用其自身验证”的循环。
- 论证链条是“对象分层不同/量纲不同/反例存在”推出强版不成立，结构上非循环。

## Q4. 量级鸿沟标记

- 未见 `10^N` 级别估算，因此无量级鸿沟阻断项。

## Q5. 代数验算

- `d[(B/2)(x\,dy-y\,dx)] = B\,dx\wedge dy`，正确。
- `\omega_{AB}=\varpi\,\varepsilon_{AB}` 在 2d screen 上是标准写法，正确。

## 警告项

1. `WARNING` [106-166]：`F_{AB}` 的记号把 `U(1)` curvature 写成了与 screen tensor 同型的 `AB` 分量，容易掩盖“先选基/先 pullback/先给 bundle morphism”这一步。这里不构成代数错误，但建议在正式稿中显式声明“这是待检命题的记号，而非已定义好的同类对象”。
2. `WARNING` [109-121]：量纲反驳依赖于对 `A`/`F` 所在基空间与规范的选择。本文已意识到这一点，但表述中“`F` 通常为 `L^{-2}`”最好改成条件句，以免被读成无条件 SI 断言。
3. `WARNING` [199-204]：Hopf curvature 反例目前是方向性说明，没有在文内写出与具体 spacetime congruence 的显式映射；可作为警告，不足以单独承担阻断。

## Q6. 综合判定

- `PASS WITH WARNING`
- 阻断错误：0
- 警告：3

结论：本文对 `current/A/R1_round1.md` 的机械校对未发现会推翻主结论的公式/符号/方向/代数阻断错误；“强版 `F_{AB}=\chi\omega_{AB}` 当前不成立、弱版仅退到 polarization/screen-frame transport”这一主判定可通过，但应保留上述 3 条警告。

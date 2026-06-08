# INSPECTOR_A | LP23-R1 Round2

结论：`阻断`

阻断项 2 条；警告项 2 条。

## 阻断项

1. `A_a := - i \bar m_b \nabla_a m^b` 被直接宣称为由 `H_K = K^\perp / K` 上 Levi-Civita “诱导”的 screen connection 1-form，这一步缺少对 lift 不变性的校对，现写法不成立。见 [current/A/R1_round2.md](D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\current\A\R1_round2.md:106) 与 [current/A/R1_round2.md](D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\current\A\R1_round2.md:135)。
   机械核对：`H_K` 中的类只定义到 `m -> m + \alpha k`。在此变换下
   `A'_a - A_a = - i \bar \alpha\, m_b \nabla_a k^b`
   一般不为零，因此 `A_a` 不是仅由 quotient class `[m]` 决定的 1-form。要把它当作 screen connection，需要额外给定 screen complement / projector（常见做法是引入辅助 null `\ell` 或等价 splitting）。当前文本据此推出“最小结构只需 `K + oriented H_K + L`”的方向判断过强。

2. `Delta phi = \oint_\gamma A` 量纲与积分对象写错。见 [current/A/R1_round2.md](D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\current\A\R1_round2.md:163) 与 [current/A/R1_round2.md](D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\current\A\R1_round2.md:180)。
   机械核对：`A_a` 是 1-form 分量，SI 量纲为 `L^{-1}`；闭路相位应写成 pullback 积分
   `Delta phi = \oint_\gamma A_a dx^a`
   或 `\oint_\gamma \gamma^* A`，这样整体才无量纲。现式缺少 `dx^a`，按字面既不是标准线积分写法，也使量纲检查无法通过。

## 警告项

1. `k^b \partial_b \phi = - i \bar m_a k^b \nabla_b m^a = A_b k^b` 作为“沿光线 pullback”是可过的，但它只校对了 `A` 沿 `k` 的收缩，不足以推出一个定义在全邻域上的 screen-bundle connection 1-form。见 [current/A/R1_round2.md](D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\current\A\R1_round2.md:122)。这条式子本身通过，不应被直接升级为全空间结论。

2. `twist = B_[ab]` 写法过粗。见 [current/A/R1_round2.md](D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\current\A\R1_round2.md:239) 与 [current/A/R1_round2.md](D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\current\A\R1_round2.md:300)。
   机械核对：`B_[ab]` 是 screen 上的反对称 2-tensor；若要和“twist scalar”比较，通常还需用 `\varepsilon^{ab}` 再降成伪标量。当前方向“`A_a` 与 twist 属于不同层级对象”是对的，但记号层面建议显式区分“twist 2-form”与“twist scalar”。

## 通过项

- `H_K := K^\perp / K` 作为 4d null congruence 的 screen quotient，量纲与类型均正确。见 [current/A/R1_round2.md](D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\current\A\R1_round2.md:93)。
- `k^b \nabla_b f^a = 0` 与 `f^a = e^{i\phi} m^a` 推出 `k^b \partial_b \phi = - i \bar m_a k^b \nabla_b m^a` 的代数步骤成立；这里 `\phi` 无量纲，`k^b \partial_b \phi` 与 `A_b k^b` 量纲匹配。见 [current/A/R1_round2.md](D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\current\A\R1_round2.md:122)。
- `B_ab := q_a{}^c q_b{}^d \nabla_d k_c` 与“optical twist 来自其反对称部分”的方向判断成立。见 [current/A/R1_round2.md](D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\current\A\R1_round2.md:201)。
- “phase/screen holonomy 不等于 optical twist” 的总方向，在对象类型区分层面通过；阻断不在这一步，而在前面对 `A_a` 的全空间定义与最小结构声称过强。

## 综合判定

当前稿件不能以“`K + oriented H_K + L` 已足够定义全空间 screen `U(1)` connection，并与 polarization phase connection 严格同一”通过机械校对。若把结论收缩为“沿 geodesic ray 的 pullback/contracted connection 可与相位输运对应”，则主方向可保留；若坚持当前“最小结构”表述，则需先补足 quotient-lift 不变性或显式加入辅助 screen splitting 结构。

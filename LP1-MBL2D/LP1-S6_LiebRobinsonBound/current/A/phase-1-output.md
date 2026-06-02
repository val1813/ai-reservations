# A博士 Phase 1 — LP1-S6_LiebRobinsonBound

## 基本结构

对有限范围相互作用量子格点系统，Lieb-Robinson 界给出：

`|| [A_x(t), B_y] || <= C ||A_x|| ||B_y|| exp[-mu(d(x,y) - v_LR t)]`

其中 `A_x` 与 `B_y` 是相距 `d(x,y)` 的局域算符。

---

## 对 2D extended Hubbard 的翻译

在 2D extended Hubbard 中，`v_LR` 取决于：

- 跳跃幅度 `t`
- 相互作用强度 `U, V`
- 有效局域范数上界
- 作用半径（短程/有限范围）

因此可写成：

`v_LR(W,g) <= c0 * J_eff(W,g)`

其中 `c0` 只依赖几何和相互作用范围，`J_eff` 是局域传播的有效耦合尺度。

---

## 可写结论

1. `v_LR` 是严格上界，不是平均速度。
2. 一旦 `v_LR` 被显式给出，`blocked` 可定义为“在 `tau_th` 内无法被该光锥影响到的格点”。
3. 这比 `tau_th < tau_local` 更适合论文正文，因为它把判据锚定在通用传播不等式上。


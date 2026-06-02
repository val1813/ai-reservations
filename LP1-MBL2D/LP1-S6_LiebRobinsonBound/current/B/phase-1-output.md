# B博士 Phase 1 — LP1-S6_LiebRobinsonBound

## 独立判断

最稳妥的转译方式不是把 `blocked` 说成“完全不传播”，而是说：

`site j is blocked` 当且仅当其到潜在热区边界的传播时间下界超过观测窗口 `tau_th`。

---

## 结构化判据

令 `d_j` 为格点 `j` 到最近热区边界的距离，则可定义：

`j blocked <=> d_j > v_LR * tau_th`

更稳妥的写法是使用保守常数：

`d_j > (v_LR + eps) tau_th`

这样 `blocked` 判据直接继承 LR 光锥，不再依赖局部经验阈值。

---

## 当前判断

1. 这只是常数层面的强化，不改渗流图景。
2. `p_block(W)` 的定义会更清晰，但不会改变“子临界/超临界”的结构。


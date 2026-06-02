# A博士 Phase 3 — 与渗流框架一致性

## 目标

证明 LR 判据不会推翻原渗流框架。

---

## 逻辑

原框架中：

`p_block(W) = P(site j is blocked under local threshold)`

新框架中：

`p_block^LR(W,tau_th) = P(d(j,∂H) > v_LR(W,g) tau_th)`

两者差异是阈值函数的替换：

`W_th -> W_th^LR(tau_th, v_LR)`

只要 `W_th^LR(W)` 是单调函数，`p_block^LR(W)` 仍是 `W` 的单调函数，并且仍然存在临界条件：

`p_block^LR(W) = p_c`

---

## 结论

LR 判据把原先的经验阈值换成了传播速度阈值，因此：

1. 渗流变量仍是 `p_block`。
2. 临界条件仍是 `p_block = p_c`。
3. 相边界数值会重标定，但普适结构不变。


# A 博士任务书 — Phase 6

**课题：** Hawking-Encoding v1
**Phase：** 6（宽/窄边界代数分离定理 — 正面表述）
**日期：** 2026-06-01
**价值分类：** [核心] — 将 Phase 5 结果整理为可投稿命题

---

## 攻击目标

把 Phase 5 的结论写成一个清晰的 proposition/theorem：

> 在 SYK/JT post-Page code subspace 中，M.B 是否成立取决于 boundary algebra 的定义。对窄 `A_bdy^narrow=SYK single-trace` 可有 O(1) Petz gap；对宽 `A_bdy^wide=SYK∨bath/radiation`，gap 被 entanglement-wedge / Petz recovery error 控制，无 O(1) 新机制。

你的任务是给出严格假设、结论、证明骨架和可失败点。

---

## 必须输出的定理格式

### Proposition 6A（候选）

假设：

1. post-Page code subspace `H_code` 有 semiclassical island；
2. `A_full` 含 island effective field algebra；
3. `A_bdy^wide` 包含 SYK boundary 与 radiation/bath algebra；
4. EW reconstruction / Petz recovery 在 `H_code` 上误差为 `ε(N)`；
5. `ω0,ω1` 为 code subspace 内 reference/excited state。

结论：

`0 <= S_{A_full}(ω1||ω0)-S_{A_bdy^wide}(ω1||ω0) <= f(ε(N))`。

因此宽代数下 M.B 不给出 O(1) independent dynamical mechanism。

同时给出窄代数 corollary：

若 `A_bdy^narrow` 不含 radiation/bath decoder，存在态对使 `Δ_Petz^narrow=O(1)`。

---

## 禁止

- 不要声称全 Hilbert space theorem。
- 不要把 `f(ε)` 的具体形式编造成已知结果；可以写成 monotone function with `f(ε)->0`。
- 不要忽略 canonical/microcanonical 差异；定理只在指定 code subspace 和 algebra definition 下成立。

---

## 产出格式

```
⚡ 审核入口：
  定理名称：[一句话]
  假设清单：[编号]
  宽代数结论：[一句话]
  窄代数 corollary：[一句话]
  不能声称的内容：[一句话]
  K1.10 状态：[维持/升级/降级]

正文：定理陈述 + 证明骨架 + 失败点 + 投稿价值。
```

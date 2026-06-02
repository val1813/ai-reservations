# A博士 Phase 5 作业 — Petz strict gap / relative entropy 判据

## ⚡ 审核入口（PI 只读）

Δ_Petz^narrow：O(1) 倾向成立，因窄 SYK single-trace 代数不含完整 radiation/bath 解码资源。  
Δ_Petz^wide：无 O(1) strict gap；在 code subspace 与 post-Page EW reconstruction 成立时，gap 至多为 recovery error 控制的小量。  
Δ_Petz^micro：trace-window 条件下同样无 O(1) gap；更适合写成 conditional approximate sufficiency。  
strict O(1) gap 是否存在：仅窄定义下成立；物理宽边界代数下不成立或未见证据。  
K1.10 升级判定：不升级；反而将宽定义 no-go 强化为 ⚠️L1。  
最脆弱步骤：approximate recovery 的误差 bound 仍依赖 code subspace 与 leading saddle 精度，不能写成全 Hilbert space theorem。

---

## §1 代数分支

本阶段必须区分三个代数：

1. `A_bdy^narrow = A_SYK,single-trace`；
2. `A_bdy^wide = A_SYK ∨ A_bath/radiation`；
3. `A_bdy^micro = A_bdy ⋊ R`。

`A_full` 取为包含 island bulk effective operators 的物理代数或 code algebra。Petz 单调性给出：

`S_{A_full}(ω1||ω0) >= S_{A_bdy}(ω1||ω0)`。

M.B 非平凡的 relative entropy 版本要求严格 gap。

## §2 态对

取：

- `ω0`：Page time 后 evaporating black hole 的 reference state，或等价的 TFD/KMS code reference；
- `ω1 = U_q ω0 U_q†`：一个 infallen qubit excitation，位于 post-Page island 的 entanglement wedge 中。

若只看窄 `SYK single-trace`，qubit 对 boundary single-trace 可见度被 scrambling 与 typicality 压低。若看宽 `SYK ∪ radiation/bath`，post-Page island 已在 radiation wedge 中，QEC/Petz recovery 应能恢复。

## §3 窄边界代数

对 `A_bdy^narrow`：

- `A_full` 含 qubit-local bulk operator，可 O(1) 区分 `ω1` 与 `ω0`；
- `A_bdy^narrow` 不含 bath/radiation decoder；
- Hayden-Preskill typicality 给出可见度指数小或至少非 O(1)。

因此：

`Δ_Petz^narrow = S_{A_full} - S_{A_bdy^narrow} = O(1)` 倾向成立。

但这只是人为窄代数下的 M.B。它不回答岛屿公式是否提供新动力学机制，因为 Page curve 的物理解码对象通常正是 radiation/bath。

## §4 宽边界代数

对 `A_bdy^wide = SYK ∨ bath/radiation`，post-Page 阶段 entanglement wedge reconstruction 给出 recovery map：

`R: A_bdy^wide -> A_full`

在 code subspace 上误差 `ε(N)`。若 `ε(N)` 小，则 relative entropy monotonicity 的近似可逆性给出：

`0 <= Δ_Petz^wide <= f(ε(N))`

其中 `f(ε)->0`。在 Phase 1/3 既有记录中，目标精度为 perturbative-in-1/N + leading saddle，`ε(N)` 被认为指数小或非微扰小。

因此宽边界代数下没有 O(1) strict gap。更准确地说：

`Δ_Petz^wide = O(f(ε(N)))`

而不是 `O(1)`。

这强化了 no-go 方向：岛屿 reconstruction 在宽代数下是 QEC/Petz recovery，不是新动力学搬运机制。

## §5 microcanonical crossed product

Microcanonical Type II_infinity crossed product 中 trace 存在，projection 与 trace-window norm 更清楚。该设置对 GKRR/Petz sufficiency 最友好。

在此分支：

- recovery 更容易表述；
- relative entropy equality/approximate equality 更自然；
- 没有证据支持 O(1) gap。

因此：

`Δ_Petz^micro = O(f(ε_trace))`

是当前最稳妥判断。

## §6 与 K1.10 的关系

K1.10 原本是 no-go：存在 boundary operator sequence 逼近 island operator，误差 `ε(N)` 小。

Phase 5 A 线没有把它升级为 ✅L2，因为：

1. 仍依赖 code subspace；
2. 仍依赖 EW reconstruction / leading saddle；
3. 仍未处理全 Hilbert space；
4. canonical Type III_1 与 microcanonical Type II_infinity 的差异仍在。

但它支持一个更清楚的表述：

> M.B 的 O(1) gap 只在窄代数定义下成立；在物理宽边界代数下，Petz strict gap 被 approximate recovery 压到小量。

## §末 结果登记建议

- K5.1：窄代数下 `Δ_Petz=O(1)` 倾向成立。
- K5.2：宽代数下无 O(1) strict gap，gap 受 recovery error 控制。
- K5.3：microcanonical crossed product 支持 approximate sufficiency。
- CP-009：不能完全关闭，但 "宽代数下 canonical no-go" 明显增强。
- K1.10：维持 ⚠️L1，不升级。

# A博士 Phase 4 作业 — Takesaki 条件 / conditional expectation

## ⚡ 审核入口（PI 只读）

E:A_full->A_bdy 存在性：条件性否定；在 `A_full = B(H_phys)` 且 `A_bdy` 为 canonical Type III_1 的分支中，不支持存在 faithful normal expectation。  
Takesaki 条件：依赖 `A_full` 定义；若 island/global 模式不被 boundary KMS modular flow 保持，则失败。  
Minimal index 推论：条件性倾向 `∞`，但不能无条件写成定理。  
Petz sufficiency：未判定；存在 `E` 也不自动推出 Petz equality。  
K1.10 升级判定：维持 ⚠️L1。  
最脆弱步骤：`A_full` 的物理代数定义仍未闭合，不能把 `B(H_phys)` 分支当作唯一分支。

---

## §0 声明强度

本 Phase A 线把 Phase 3 的 exact index 问题改写为 conditional expectation 问题。结论比 Phase 3 更尖锐，但仍不是最终定理：

- 若 `A_full = B(H_phys)`，而 `A_bdy` 保持 canonical Type III_1，则 `E:B(H_phys)->A_bdy` 的存在性极不自然，且不满足通向 index=1 的结构条件。
- 若 `A_full` 不是 `B(H_phys)`，而是由引力约束压缩出的 Type III algebra，则必须逐案检查 Takesaki 条件。
- Microcanonical crossed product 中的 expectation 不能反推 canonical Type III_1 中的 expectation。

## §1 inclusion 与态的固定

本阶段必须区分三种 inclusion：

1. `A_bdy(Type III_1) ⊂ B(H_phys)(Type I)`。
2. `A_bdy(Type III_1) ⊂ A_full(Type III)`。
3. crossed product 后的 `A_bdy ⋊ R ⊂ A_full ⋊ R`，通常进入 Type II_infinity 语言。

Phase 3 的错误风险在于把第 1 类当成默认事实。Phase 4 不能这么做。`A_full` 在引力理论中可能不是全体 bounded operators，而是受 Hamiltonian / diffeomorphism constraints 约束后的物理可观测代数。

## §2 Takesaki 条件

Takesaki 定理给出可操作入口：若 `N ⊂ M`，且 faithful normal state/weight `φ` 的 modular automorphism group 满足

`σ_t^φ(N) = N`

则存在保持 `φ` 的 normal conditional expectation `E_φ:M->N`。

代入本问题：

- `M = A_full`
- `N = A_bdy`
- `φ = canonical TFD/KMS state`

如果 island/global/edge 模式在 `A_full` 的 modular flow 下把 `A_bdy` 带出自身，则 `E_φ` 不存在。反之，若 `A_full` 的 modular flow 对 `A_bdy` invariant，则 expectation 可能存在，但还要检查它是否 faithful、normal、物理态保持。

## §3 canonical Type III_1 分支

在 canonical SYK/JT 标准 Page-curve 设置中，`A_bdy` 是 Type III_1。此时：

- `A_bdy` 没有有限投影；
- vacuum-like/KMS modular flow 一般是 outer；
- centralizer 与 crossed-product structure 不等于普通 Type I coarse-graining；
- 从 `B(H_phys)` onto Type III_1 subfactor 的 faithful normal expectation 不是自然结构。

因此在 `A_full=B(H_phys)` 分支中，`E` 的存在性不支持。若硬要保留 `E`，必须给出一个保持 TFD/KMS weight 的显式 modular-invariant inclusion。当前文件系统内的 Phase 1-3 产出没有提供这种构造。

结论：该分支给出 `Ind(E)` 非有限 / minimal index 倾向 `∞` 的强压力，但仍是条件性结论。

## §4 Type III -> Type III 分支

若 `A_full` 也是 Type III，则不能只靠 type mismatch 排除 `E`。此时关键变为：

`σ_t^{A_full,φ}(A_bdy) = A_bdy ?`

若引力约束把 island/global 模式编码进同一 Type III algebra，`A_bdy` 可能是 modular-invariant 子代数，expectation 可能存在。

但存在 expectation 也只表示存在一种 coarse-graining，不等于 `A_bdy=A_full`，更不等于 M.B 失败。要推出 M.B 失败还需要 Petz sufficiency：

`S_{A_full}(ω1||ω0) = S_{A_bdy}(ω1||ω0)`。

Phase 4 A 线没有证明这个 equality。

## §5 microcanonical crossed product 分支

Microcanonical Type II_infinity 是 GKRR 最有利设置：

- finite trace projection 可用；
- crossed product 允许把部分 canonical 不可见结构转写为 trace-window algebra；
- conditional expectation 在 semifinite algebra 中更容易存在。

但这不能反推 canonical setting。原因是 crossed product 引入了 modular clock/weight 结构，改变了代数类型。它能说明 microcanonical pressure test 下 K1.10 未被击穿，却不能关闭 canonical CP-009。

## §6 Petz sufficiency

即使存在 `E:M->N`，还需检查对两态 `ω0,ω1` 是否满足 sufficiency：

`S_M(ω1||ω0) = S_N(ω1||ω0)`。

若 strict inequality：

`S_M(ω1||ω0) > S_N(ω1||ω0)`

则 `A_full` 比 `A_bdy` 能区分更多信息，M.B 可改写为 relative entropy gap。这个方向不依赖 exact Jones index，但需要实际构造态对与相对熵估计。

当前能说的是：expectation 的存在性不足以杀死 M.B；Petz equality 才是杀死 M.B 的强条件。

## §末 结果登记建议

- `E` 不存在：在 `A_full=B(H_phys)` 分支中为强条件性结论。
- Takesaki 条件：canonical Type III_1 下依赖 `A_full` modular flow；当前无证据支持无条件满足。
- Minimal index：条件性倾向 `∞`，但 exact index 未闭合。
- Petz sufficiency：未判定，应进入下一 Phase 或 B 线交叉检查。
- K1.10：维持 ⚠️L1，不升级 ✅L2。

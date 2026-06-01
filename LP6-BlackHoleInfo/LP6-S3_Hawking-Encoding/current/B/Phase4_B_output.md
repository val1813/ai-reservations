# B博士 Phase 4 作业 — commutant / split property / relative entropy gap

## ⚡ 审核入口（PI 只读）

非平凡 commutant：表示依赖；GNS 中有 Tomita mirror，但不能自动当作物理自由度。  
split property 判定：canonical 引力设置中存在 failure 压力，但不足以单独推出 exact `[A_full:A_bdy]>1`。  
relative entropy gap：可作为更稳健的下一判据，但本 Phase 未得到显式正下界。  
对 A 线 expectation 的反击：`E` 不存在若只来自 `A_full=B(H)` 假设，则不是无条件结论；`E` 存在也不推出 Petz equality。  
K1.10 升级判定：维持 ⚠️L1。  
最脆弱步骤：commutant 的表示空间不同，GNS commutant 与 physical commutant 不能混同。

---

## §1 commutant 的表示依赖

`(A_bdy)'` 只有在指定表示空间后才有意义。至少有四个不同对象：

1. `H_TFD` 上的 GNS commutant；
2. `H_code` 上的 code-subspace commutant；
3. `H_phys` 上满足引力约束的 physical commutant；
4. crossed product 表示中的 semifinite commutant。

Phase 3 的 commutant 压力必须在 Phase 4 中拆开。否则会把 Tomita-Takesaki 的标准形式误读成新物理自由度。

## §2 候选 commutant 检查

### 2.1 Tomita mirror algebra

在 cyclic separating state 下，`J A_bdy J` 给出 commutant 的标准形式。这在数学上非平凡，但它未必是独立物理可观测量。它可能只是同一 GNS representation 的 mirror copy。

结论：Tomita mirror 可支持 "boundary algebra 不是普通 Type I 完整矩阵代数" 的结构判断，但不能单独证明 island 新自由度存在。

### 2.2 left/right boundary algebra

双侧 TFD 中，另一侧 boundary algebra 与单侧 algebra 对易，是最直接的 commutant 候选。但这通常反映双侧系统的 tensor-like 表示，而不是单侧 radiation/boundary 是否已包含 island 的问题。

结论：可作为 sanity check，不能关闭 CP-010。

### 2.3 gravitational edge/global modes

Edge/global modes 是真正有希望的物理 commutant 候选。若存在算符 `X` 满足：

- `[X,O]=0` for all `O in A_bdy`；
- `X notin C*1`；
- `X in A_full`；

则 `A_bdy` 不可能等于 `A_full`。

当前问题：SYK/JT 中这个 `X` 尚未被显式构造。Donnelly-Wall 型 edge mode 提供跨域动机，但还不是 JT/SYK 里的闭合证明。

## §3 split property 路线

Split property 若成立，则存在 Type I factor `F`：

`A_bdy(region1) ⊂ F ⊂ A_full(region2)`。

这给出近似 factorization，削弱 "commutant 非平凡 -> 真扩张" 的直接性。

若 split property 失败，则说明没有这样的 Type I 中间因子。失败可能来自：

- QFT UV entanglement 的普通 Type III 现象；
- 引力 Gauss law / Hamiltonian constraint；
- large N generalized free field 的径向不可分解；
- island/radiation 的 state-dependent reconstruction。

关键桥梁是：split failure 只说明不能 Type I factorize，不自动等于 `[A_full:A_bdy]>1`。要推出 index 结论，还需证明 `A_full` 中存在 `A_bdy` 不可生成的物理 observable。

结论：split failure 是强结构压力，不是 exact index 定理。

## §4 relative entropy gap

若 commutant 不能闭合，可转向态区分：

`Δ_rel = S_{A_full}(ω1||ω0) - S_{A_bdy}(ω1||ω0)`。

若 `Δ_rel > 0`，则 `A_full` 对 infallen-qubit excited state 的可区分能力强于 `A_bdy`，M.B 非平凡成立为 relative entropy no-go。

但 Phase 1 的相对熵方向曾经有符号笔误，Phase 4 必须谨慎：Petz monotonicity 给出 restriction 后相对熵不增。也就是说更大的 algebra 能看到更多区分度：

`S_{A_full} >= S_{A_bdy}`。

真正需要的是严格不等式，而不是单调性本身。

当前没有显式计算给出 strict lower bound，因此不能升级 K1.10。

## §5 对 A 线的反向攻击

若 A 线声称 `E` 不存在：

- 如果其论证依赖 `A_full=B(H_phys)`，则结论只是分支性；
- 如果能证明 modular flow 不保持 `A_bdy`，则结论更强；
- 但 `E` 不存在本身仍需连接到 physical information gap。

若 A 线声称 `E` 存在：

- 还需检查是否保持 `ω0,ω1`；
- 还需检查 Petz equality；
- `E` 存在但 Petz equality 失败时，M.B 仍可非平凡。

## §6 microcanonical 压力

Microcanonical Type II_infinity 中 trace-window 结构让 expectation/trace norm 更容易定义。它对 GKRR 友好，但无法消除 canonical Type III_1 的结构问题。

因此 microcanonical 分支只能说明：K1.10 在最有利 GKRR 设置下未被击穿。它不能反证 canonical no-go。

## §末 结果登记建议

- 非平凡 commutant：表示依赖，未闭合成物理构造。
- split property：failure 压力存在，但不足以单独给出 exact index。
- relative entropy gap：是下一步最干净的判据；本 Phase 未得显式正下界。
- 对 CP-009/CP-010：进一步压缩，但不关闭。
- K1.10：维持 ⚠️L1。

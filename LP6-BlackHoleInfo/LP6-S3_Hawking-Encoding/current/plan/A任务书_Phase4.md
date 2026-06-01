# A 博士任务书 — Phase 4

**课题：** Hawking-Encoding v1
**Phase：** 4（路径 C — Takesaki 条件 / conditional expectation）
**日期：** 2026-06-01
**价值分类：** [核心] — 将 Phase 3 的 subfactor 结构压力转化为可判定命题

---

## 攻击目标

**主攻**：判定是否存在 normal faithful conditional expectation

`E: A_full -> A_bdy`

并要求它与 canonical Type III_1 boundary algebra 的 modular structure 相容。

如果你证明不存在这样的 `E`，则 Kosaki-Longo minimal index 倾向 `∞`，`[A_full : A_bdy] = 1` 被排除，CP-010 显著推进。

如果你证明 `E` 存在，则必须进一步判断它是否给出 Petz sufficiency。若 `E` 存在但 Petz sufficiency 失败，则 M.B no-go 可转写为 relative entropy gap，而不是 index no-go。

---

## 背景（Phase 3 产出 + PI 裁决）

Phase 3 的最强结论：
- canonical Type III_1 中，`A_bdy` 的 modular / centralizer / split-property 结构对 `A_full = A_bdy` 不友好；
- 若 `A_full = B(H_phys)` 且 `A_bdy` 仍是 Type III_1，则 index 不可能为 1；
- 但 `A_full` 的物理定义未闭合，exact `[A_full : A_bdy]` 未算出；
- K1.10 维持 ⚠️L1，不能升级 ✅L2。

Phase 4 A 线的任务不是重复 index 猜测，而是检查 index 理论中更可操作的入口：conditional expectation。

---

## 具体推导任务

### 步骤 1：固定 inclusion 与态

明确三种可能设置：

1. **Type-changing inclusion**：`A_bdy` 为 canonical Type III_1，`A_full = B(H_phys)` 为 Type I。
2. **Type-preserving inclusion**：`A_bdy ⊂ A_full` 均为 Type III，但 `A_full` 含 island/global/edge 模式。
3. **Microcanonical crossed product**：`A_bdy` 经 modular crossed product 升级到 Type II_infinity。

每一类都要单独判断 `E` 的存在性，不能把 canonical 与 microcanonical 混用。

### 步骤 2：使用 Takesaki 定理

Takesaki 条件：给定 faithful normal state/weight `φ`，若 `N ⊂ M` 且 `σ_t^φ(N) = N` 对所有 `t` 成立，则存在保持 `φ` 的 normal conditional expectation `E_φ: M -> N`。

你的任务：
- 令 `M = A_full`，`N = A_bdy`；
- 判定 canonical TFD/KMS state 的 modular flow 是否把 `A_bdy` 保持为 invariant subalgebra；
- 判定 island/global/edge 模式是否在同一 modular flow 下闭合；
- 若不闭合，说明 `E_φ` 不存在，而不是泛泛说 "Type III 很复杂"。

### 步骤 3：Kosaki-Longo index 连接

若不存在 faithful normal conditional expectation：
- 说明 minimal index 不能由有限 Pimsner-Popa bound 实现；
- 在目标物理设置中给出 `[A_full : A_bdy] = ∞` 或至少 `>1` 的条件性结论；
- 标明这是否足以关闭 CP-010。

若存在 `E`：
- 判断 `Ind(E)` 是否有限；
- 判断 `E` 是否唯一；
- 判断 `E` 是否对应一个 physically admissible coarse-graining，而不是任意数学投影。

### 步骤 4：Petz sufficiency 检查

对 reference state `ω0` 与 infallen-qubit excited state `ω1`，检查：

`S_M(ω1 || ω0) = S_N(ω1 || ω0)`

是否成立。

若 equality 成立，则 `E` 或 restriction map 对这对态是 sufficient，island 信息在 `A_bdy` 上无损。

若 strict inequality 成立，则存在 relative entropy gap，可作为 M.B 非平凡性的替代表述。

### 步骤 5：做出判定

输出必须给出：
- `E` 存在性：[不存在 / 存在 / 仅在 microcanonical 中存在 / 不确定]
- Takesaki 条件状态：[满足 / 失败 / 依赖 A_full 定义]
- Minimal index 推论：[=1 / >1 / ∞ / 不确定]
- Petz sufficiency：[成立 / 失败 / 未能判定]
- K1.10 升级判定：[可升级 ✅L2 / 维持 ⚠️L1]

---

## 必须回答的问题

1. canonical Type III_1 中，`A_bdy` 是否被 `A_full` 上的 modular flow 保持？
2. 若 `A_full = B(H_phys)`，是否可能存在 faithful normal expectation `B(H_phys) -> A_bdy`？
3. 若 `A_full` 也是 Type III，Takesaki 条件是否仍失败？
4. Microcanonical crossed product 中的 expectation 是否能反推 canonical setting？
5. `E` 的存在是否等价于 M.B 失败？还是还需要 Petz sufficiency？

---

## 禁止

- 不要默认 `A_full = B(H)`；必须把它作为一个分支。
- 不要把 "存在抽象 conditional expectation" 与 "物理上可接受的 coarse-graining" 混同。
- 不要用 microcanonical Type II_infinity 的结论直接覆盖 canonical Type III_1。
- 不要在未检查 Petz equality 时声称 M.B 被排除。

---

## 产出格式

```
⚡ 审核入口（PI 只读）：
  E:A_full->A_bdy 存在性：[不存在 / 存在 / 条件性 / 不确定]
  Takesaki 条件：[满足 / 失败 / 依赖定义]
  Minimal index 推论：[=1 / >1 / ∞ / 不确定]
  Petz sufficiency：[成立 / 失败 / 未判定]
  K1.10 升级判定：[可升级 ✅L2 / 维持 ⚠️L1]
  最脆弱步骤：[一句话]
  
然后 §0/§1/§2/§N/§末 完整作业。
```

## 关键文献

- Takesaki, Theory of Operator Algebras II（conditional expectation theorem）
- Kosaki, "Extension of Jones' theory on index to arbitrary factors"
- Longo, "Index of subfactors and statistics of quantum fields"
- Petz 1986 sufficiency theorem
- CPW 2209.10454（large N algebras / crossed product）
- Leutheusser-Liu 2110.05497（SYK Type III_1）
- Penington-Witten 2306.03999（JT gravity algebras）

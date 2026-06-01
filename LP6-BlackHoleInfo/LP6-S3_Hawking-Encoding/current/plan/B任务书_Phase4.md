# B 博士任务书 — Phase 4

**课题：** Hawking-Encoding v1
**Phase：** 4（路径 C — commutant / split property / relative entropy gap）
**日期：** 2026-06-01
**价值分类：** [核心] — 以 commutant 与 split failure 攻击 CP-009/CP-010

---

## 攻击目标

**主攻**：构造或排除 SYK/JT 表象中的非平凡 commutant

`(A_bdy)'`

并判断 split property 是否失败到足以推出 `A_bdy ⊂ A_full` 是 proper inclusion。

**副攻**：如果 commutant 路线不能闭合，则检查 relative modular sufficiency / Petz equality 是否失败，从而给出 relative entropy 版本的 M.B no-go。

---

## 背景（Phase 3 产出 + PI 裁决）

Phase 3 已确认：
- canonical Type III_1 结构不支持轻率声称 `A_full = A_bdy`；
- exact index 未闭合；
- 下一步尖锐化为两个问题：
  1. 是否存在 modular-compatible conditional expectation `E:A_full->A_bdy`；
  2. 是否能构造 `(A_bdy)'` 非平凡，或证明 split failure 对应 proper inclusion。

B 线负责第二个问题，并对 A 线的 expectation 结论做反面攻击。

---

## 具体推导任务

### 步骤 1：定义 commutant 的表示空间

分别在以下空间中讨论：

1. GNS Hilbert space `H_TFD`；
2. code subspace `H_code`；
3. physical Hilbert space `H_phys`（含引力约束）；
4. microcanonical crossed-product representation。

必须说明 `(A_bdy)'` 是在哪个表示中取的。不同表示下 commutant 可完全不同。

### 步骤 2：寻找非平凡 commutant 候选

候选对象：
- right/left boundary 的另一侧 algebra；
- gravitational edge mode / center-like mode；
- modular conjugation `J A_bdy J` 生成的 mirror algebra；
- island 内对 boundary single-trace algebra 不可见的 dressed operator；
- microcanonical energy-window projector 或 clock mode。

对每个候选判断：
- 是否真的与 `A_bdy` 对易；
- 是否不是 `C*1`；
- 是否属于 `A_full`；
- 是否只是 Tomita mirror，而非新的物理可观测量。

### 步骤 3：split property 路线

检查是否存在 Type I factor `F` 使得

`A_bdy(region1) ⊂ F ⊂ A_full(region2)`

若 split property 成立，则可近似 factorization，commutant 路线不自动推出 proper inclusion。

若 split property 失败，则说明 boundary/island 的径向或引力约束结构不能以 Type I 中间因子分离，可支持 `A_bdy` 不是 full algebra。

需要区分：
- QFT UV entanglement 导致的普通 Type III split 问题；
- 引力约束导致的全局 non-factorization；
- SYK/JT large N 极限中的 generalized free field factorization。

### 步骤 4：relative entropy / Petz sufficiency 副攻

若 commutant 不能给出闭合定理，转向态区分判据。

对 `ω0 = TFD/KMS` 与 `ω1 = TFD + infallen qubit`，判断：

`S_{A_full}(ω1 || ω0) - S_{A_bdy}(ω1 || ω0)`

是否严格为正。

如果 strict gap 存在，则 M.B 非平凡可用 Petz sufficiency failure 表述，即使 exact index 未算出。

### 步骤 5：对 A 线的反面攻击

如果 A 线声称 `E` 不存在：
- 检查是否只是因为 `A_full` 定义过强；
- 检查 microcanonical crossed product 是否给出反例；
- 检查 `E` 不存在是否足以推出物理 no-go。

如果 A 线声称 `E` 存在：
- 检查该 `E` 是否保持物理态；
- 检查 Petz equality 是否成立；
- 若 equality 失败，则即使 `E` 存在，M.B 仍可能非平凡。

---

## 必须回答的问题

1. `(A_bdy)'` 在 GNS / code / physical Hilbert space 中分别是什么？
2. Tomita mirror algebra 是否能作为物理 commutant 证据？
3. split property failure 是否推出 `A_bdy ⊂ A_full` proper？还是只说明 factorization 失败？
4. relative entropy gap 是否能绕过 exact Jones index？
5. microcanonical Type II_infinity 中的 trace-window 结论是否削弱 canonical no-go？

---

## 禁止

- 不要把 Tomita mirror 自动当作独立物理自由度。
- 不要把 split property failure 直接等同于 `[A_full:A_bdy]>1`，中间要给出 algebraic bridge。
- 不要混淆 GNS commutant 与 physical commutant。
- 不要只重复 Phase 3 的 "结构压力"，必须给出更尖锐判定。

---

## 产出格式

```
⚡ 审核入口（PI 只读）：
  非平凡 commutant：[构造成功 / 排除 / 表示依赖 / 不确定]
  split property 判定：[成立 / 失败 / 不足以判定 / 表示依赖]
  relative entropy gap：[存在 / 不存在 / 未判定]
  对 A 线 expectation 的反击：[一句话]
  K1.10 升级判定：[可升级 ✅L2 / 维持 ⚠️L1]
  最脆弱步骤：[一句话]
  
然后 §1/§2/§N/§末 完整作业。
```

## 关键文献

- Doplicher-Longo, "Standard and split inclusions of von Neumann algebras"
- Takesaki, Tomita-Takesaki modular theory
- Witten, "Notes on Some Entanglement Properties of Quantum Field Theory"
- CPW 2209.10454
- Penington-Witten 2306.03999
- Petz 1986 sufficiency theorem
- Almheiri-Dong-Harlow 1411.7041

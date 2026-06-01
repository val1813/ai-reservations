# B 博士任务书 — Phase 2

**课题：** Hawking-Encoding v1
**Phase：** 2（AHA-001 驱动 — 反面攻 GKRR completeness）
**日期：** 2026-06-01
**价值分类：** [核心] + [副攻：CP-008 setup 变体]

---

## 攻击目标

**反面立场**：证明 — GKRR completeness 至多是 *conjecture*，存在隐含假设或显式反例使其在 SYK/JT 中**不严格成立**。

如果你成功（找到反例或致命隐含假设）→ GKRR 是 conjecture → Phase 1 K1.9-K1.13 (no-go 路径) 全部 conditional → M.B 在 SYK/JT 中是否成立 = 真正开放。
如果你失败 → GKRR 强论据成立 → Phase 1 升级 ✅L2。

**副攻**：在 *动力学曲率 setup*（collapse 形成黑洞、R(x) 不恒定）中，B 自己 Phase 1 §4.2 论证（"JT 半经典 R 恒定 → ACMP localizer 塌缩"）是否仍成立？

---

## 背景（你不知道 Phase 1 A 博士的细节，仅知北极星 + AHA-001）

Phase 1 双博士独立得出 M.B 在 SYK/JT 不成立（B 自己的 §5 no-go + ε(N) ~ e^{−cN}）。但 PI 现在指出：你（B 博士）的论证有一个 *hidden* 共同脖子——**GKRR completeness**。如果 GKRR 实际是 conjecture 而非 theorem，你 Phase 1 的 no-go 定理就只是 conditional。

**你的 Phase 2 任务**：
1. **主攻**：寻找 GKRR completeness 的隐含假设或反例（**对自己 Phase 1 结论也提供反向 stress test**）
2. **副攻**：检验 Phase 1 §4.2 论证（"R 恒定 → ACMP 塌缩"）在 collapse / 动力学曲率 setup 中是否仍成立

---

## 具体推导任务（主攻：GKRR completeness 反例）

### 步骤 1：跨域同构（B 博士特有）

GKRR completeness 在数学上等价于哪类已知结构？候选：
- **Reeh-Schlieder 定理**（QFT 中真空在任何 wedge algebra 上 cyclic）→ 但 Reeh-Schlieder 给的是 *cyclic*，不是 *factorized completeness*
- **Type III_1 factor 的 standard form**（生成元集生成算符代数）→ 但 standard form 不保证 *物理* 算符可达性
- **Voiculescu 自由概率论中的 GFF GNS construction** → 单迹 algebra 在 large N 是 *generalized free field*，其 GNS rep 完整覆盖 Fock space
- **Connes' embedding problem** 的反面（如果它本来是 conjecture / 已证伪）

**你的任务**：在每个候选同构下，问 — 该数学结构的 *已知漏洞* 是否对应 GKRR completeness 的潜在漏洞？

### 步骤 2：跨域反例（GKRR 在 *相邻数学结构* 中的反例）

- **Quantum field theory 中 split property 的失败案例**：split property 保证 algebra 沿空间分割时 factorize；某些 QFT (如 conformal nets) split fails →  对应 boundary algebra 的"沿径向 factorize" claim 在某些 setup 下也可能 fails
- **Algebraic QFT in curved spacetime** 中 "asymptotic completeness" 的 known counterexamples（如 long-range interactions, infrared divergences）
- **C* algebra 的 simple closure vs ultraweak closure** 区别——GKRR 用哪个？这两个 closure 给不同 completeness

### 步骤 3：寻找 SYK/JT 中的具体反例

候选反例方向：
- **Wormhole saddle 给的 *non-trivial center***（Type II_∞ vs Type III_1 区别）—— Type II_∞ 有 trace，但 trace 是 boundary algebra 没有的"额外结构"。这是 GKRR completeness 的反例吗？
- **Grand canonical ensemble vs microcanonical**：CPW 用 microcanonical 给 Type II_∞，grand canonical 给 Type II_1。两者 boundary algebra 完备性不同？
- **Topological / global mode**：JT 中 holonomy 等 global 自由度是否真的可被 boundary local data 完全决定？
- **Edge mode in entanglement entropy**：Donnelly-Wall 论证 gauge theory 的 EE 含 edge mode，不能完全由 bulk algebra 给出——是否对应 island 中的 "edge mode" 不在 boundary algebra 中？

### 步骤 4：ACMP 2025 反例的 *跨域升级*

Phase 1 §4.2 你说 "JT 半经典 R 恒定 → ACMP 用 R 做 localizer 失效"。但 ACMP 不一定要用 R。

**升级问题**：在 *任何* gauge-invariant scalar invariant 中（不限于 R），是否都可被 boundary algebra 重构？
- 候选 scalars：(a) Riemann 张量缩并 R_{abcd} R^{abcd}；(b) matter field 复合算符 (φ²)(x)；(c) topological invariants（但 JT 是 2D，topology 受限）
- B 博士跨域思考：在更高维 holographic CFT (e.g. 4d N=4 SYM) 中，曲率不变量可成为非平凡 localizer——是否给出 GKRR completeness 的高维反例？

### 步骤 5：副攻 — collapse / 动力学曲率 setup 中的 ACMP 命运

**Phase 1 §4.2 论证**：JT 半经典 R(x) = -2/L² 恒定 → 曲率 scalar 不能区分 bulk 点 → ACMP 塌缩。

**但**：在 collapse 形成黑洞的 setup 中，R(x) 不恒定（horizon 形成动力学）。这时：
- ACMP 用 R 做 localizer **可以工作**？
- 还是 dilaton 仍 boundary-reconstructable，B 论证仍成立？
- collapse setup 的 boundary algebra 是否 *也* 包含 horizon formation 的所有信息（即使 boundary 在 t=−∞ 时 horizon 还不存在）？

具体细分：
- (Sub-1) Vaidya AdS_2 collapse + JT：dilaton 仍渐近发散，但 R(x) 不恒定 → ACMP localizer 是否可用？
- (Sub-2) 在 sub-1 的 boundary algebra 是否 *包含* 完整 collapse 信息？
- (Sub-3) Phase 1 §4.2 论证如何修正？

### 步骤 6：QEC × completeness（跨域）

Phase 1 §6.1 B 用 QEC 等价 ([[5,1,3]] code) 论证 "A_island = A_bdy 的不同 code-word 表示"。

**升级问题**：QEC 在 *finite-dimensional* code 中等价 ⟹ infinite-dimensional algebraic 等价吗？
- Quantum error correction 在 infinite-dim 中 *不一定* 给出 algebra 等价（仅 von Neumann algebra subfactor）
- Subfactor index [M : N]：若 [M : A_island] > 1，则 A_island ⊊ M 真扩张 → 不仅是 code 等价
- 在 JT 中 [A_island : A_bdy] 的具体值？是 1（trivial subfactor）还是 > 1（真扩张）？

### 步骤 7：BFV × Yang-Yang 升级

Phase 1 §6.3 你用 BFV 1910.14646 + Yang-Yang 2211.05491 论证 polynomial decoder 不存在。

**升级问题**：复杂性下界 ↔ algebra 真扩张 之间是 *单向* 还是 *双向* 关联？
- 若 polynomial decoder 不存在 ⟹ A_island ⊋ A_bdy（真扩张）？这是 Yang-Yang 的隐含主张。
- 若是 → BFV/Yang-Yang 反过来支持命题 A（M.B 满足）—— 这与你 Phase 1 §6.3 的解读相反
- 若不是双向 → 你 Phase 1 §6.3 的结论需要重审

---

## 必须回答的问题

1. GKRR completeness 在 *相邻数学结构*（QFT split property, Connes' embedding, AQFT asymptotic completeness）中的对应物，其已知漏洞是否对应 GKRR 的潜在漏洞？
2. JT 中 holonomy / topological mode / edge mode 是否真的可被 boundary local data 完全决定？
3. Subfactor index [A_full : A_bdy] 在 JT 中的具体值？
4. 在 *动力学曲率* setup 中，Phase 1 §4.2 论证（"R 恒定 → ACMP 塌缩"）是否仍成立？
5. BFV/Yang-Yang 复杂性下界 ↔ algebra 真扩张 是单向还是双向关联？

---

## 禁止

- 不要重复 Phase 1 已做的论证 — 必须 *推进* 或 *攻自己 Phase 1 结论的 hidden assumption*
- 不要遗忘"自我反向攻击" — 你的 Phase 1 no-go 定理本身可能依赖 GKRR completeness conjecture，必须 stress test
- 不要满足于"在 setup A 中..."论证 — 必须考虑 *相邻* setup（collapse, 高维, non-perturbative）
- 不要把 Phase 1 自承的"承认边界 (1)(2)(3)"草率扩展为新结论 — 那些是 *待解决的开放问题*，不是已知结果

---

## 产出格式

```
⚡ 审核入口（PI 只读）：
  GKRR 反例发现：[是 / 否 / 部分]
  最强反例：[一句话]
  自我反向攻击结果：[Phase 1 §X 论证是否需要修正？]
  collapse setup 中 §4.2 论证状态：[仍成立 / 修正 / 失效]
  跨域同构最有力的：[Reeh-Schlieder / split property / Connes / AQFT / 其他]
  最脆弱步骤：[一句话]
  
然后 §1/§N/§末 完整突击作业。
```

---

## 关键文献

- arXiv:2012.05770 (Raju, 必读 §6 algebra of observables)
- arXiv:2602.06543 (GKRR — 必读全文，特别 §4 holography of information 论证)
- arXiv:2506.04311 (ACMP — 必读 §3-4)
- arXiv:2209.10454 (CPW Type II_∞)
- Doplicher-Longo "Standard and split inclusions of von Neumann algebras", Inventiones 1984
- Connes 1976 classification of injective factors
- Donnelly-Wall "Entanglement entropy of electromagnetic edge modes", PRL 2015
- Yoshida 2017 "Soft mode and interior operator in Hayden-Preskill thought experiment", arXiv:1812.07353

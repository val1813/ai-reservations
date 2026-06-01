# A 博士任务书 — Phase 2

**课题：** Hawking-Encoding v1
**Phase：** 2（AHA-001 驱动 — 攻 GKRR completeness 真实强度）
**日期：** 2026-06-01
**价值分类：** [核心] — 直接决定 Phase 1 结论是否升级为 ✅L2

---

## 攻击目标

**正面立场**：证明或构造 — GKRR completeness（"boundary algebra of observables at infinity is complete"）在 SYK/JT 中作为 *theorem* 成立，且其论证在 perturbative + leading replica saddle 精度下严格闭合。

如果你成功 → Phase 1 的 K1.10 (no-go 定理) 升级为 ✅L2 → 命题 B 在 SYK/JT 中决定性获胜。
如果你失败（发现隐含假设或反例）→ GKRR 是 conjecture → Phase 1 双博士所有结论都 conditional → 问题保持开放。

---

## 背景（来自 Phase 1 双博士共同发现 + AHA-001）

Phase 1 A 博士走"ACMP 前提违反 + 相对熵"路径，B 博士走"JT 半经典 + dilaton HKLL 塌缩 + QEC等价"路径。两路径独立推得 M.B 在 SYK/JT 不成立——但**两个路径都通过 GKRR completeness 这个共同脖子**：

- A 路径：宽 A_bdy = SYK + bath 下，GKRR completeness ⟹ A_island ⊆ A_bdy_wide ⟹ Δ_M.B = 0
- B 路径：HKLL + EW reconstruction 给出 ε(N) ~ e^{−cN} no-go，依赖单迹 algebra Type III_1 *完备* 描述 GFF GNS rep

**关键问题**：GKRR completeness 论证（含 Raju 2012, 2020, GKRR 2026 主张 "algebra of observables at infinity is complete"）——其严格性如何？依赖什么隐含假设？

---

## 具体推导任务

### 步骤 1：解构 GKRR completeness 的论证链

GKRR (arXiv:2602.06543) + Raju (arXiv:2012.05770) 主张：
- AdS 中 boundary algebra 包含所有 gauge-invariant observables
- Asymptotically flat 中 algebra at null infinity 同样完备
- 因此 *任何* bulk operator（包括 island 内的）都可被 boundary data 重构

**你的任务**：把这个 claim 拆成可验证的子命题：
- (G1) 在 perturbative gravity 中，每个 bulk gauge-invariant operator 都可以被表为 boundary algebra 元素的（可能复杂的）函数
- (G2) (G1) 中的"函数"在适当 Banach norm 或 weak-* 拓扑下良定义
- (G3) 此重构在 large diffeomorphism quotient 下保持
- (G4) Non-perturbative（off-shell saddle）配置不破坏 (G1)-(G3)

**你需要回答**：每个 (G1)-(G4) 是 *theorem*（已有严格证明）还是 *conjecture*（强论据但未严格）？

### 步骤 2：定位 SYK/JT 中的具体形式

- (G1) JT 版本：bulk matter scalar + dilaton + graviton mode → 都可被 boundary Schwarzian + 单迹算符 + bath 重构？
- (G2) JT 版本：HKLL kernel 是否在 island 内 well-defined（不止 perturbative）？
- (G3) JT 版本：JT 中"large diff"是 Schwarzian symmetry 的 SL(2,ℝ)，已知 quotient 良定义
- (G4) JT 版本：复制虫洞 saddle 是 off-shell 配置，是否破坏 (G1)？

### 步骤 3：识别隐含假设

**特别关注**：
- "no algebraic split along radial direction"（GKRR 用语）—— 这在 JT 中意味着什么？是数学 fact 还是依赖额外条件？
- Boundary algebra 的 *闭包* 选择（norm closure / weak-* closure / strong closure）—— 不同 closure 给出不同 completeness
- Perturbative vs non-perturbative completeness 的精确分界
- Hilbert space *factorization* 在 GKRR 框架下的角色（GKRR 主张不需要严格 factorize，仅需 algebra completeness——验证这点）

### 步骤 4：与 ACMP 2025 主张的张力

ACMP 2025 (arXiv:2506.04311) 反驳 GKRR 立场。关键点：在 *无背景 isometry* 时存在 *gauge-invariant compactly supported operators* 不在 boundary HKLL 范围。

**这构成 GKRR completeness 的反例吗？**
- 选项 1：是 — ACMP 算符独立于 boundary algebra → GKRR completeness 失败 → Phase 1 结论 conditional
- 选项 2：否 — ACMP 算符虽 compactly supported，但其期望值仍可由 boundary correlation 函数完全决定 → GKRR completeness 不被破坏
- 选项 3：在 setup 边界（无 isometry, 无 reservoir）上 ACMP 适用，在 SYK/JT (有 Killing + 有 bath) 上 GKRR 适用 → 两者各自的 setup 内成立，不冲突

### 步骤 5：做出判定

写出明确的 *条件* judgment：
- "GKRR completeness 在 SYK/JT 至 perturbative-in-1/N 精度成立 ⟺ [显式条件 X1, X2, ...]"
- 其中 (X_i) 必须是可独立验证的子命题
- 标注每个 (X_i) 当前的状态（theorem / conjecture / open）

---

## 必须回答的问题

1. GKRR completeness 是否依赖 *Hilbert space factorization*？若是 → 与"no algebraic split along radial direction"如何调和？
2. ACMP 2025 的 compactly supported gauge-invariant operators 是否给出 GKRR completeness 的反例？还是它们的 *期望值* 仍可由 boundary correlators 决定？
3. 在 JT 中，boundary algebra 的 weak-* closure 是否包含 *所有* island operators？还是仅在 perturbative 精度下包含？
4. Non-perturbative replica wormhole saddle 是否引入 boundary algebra 之外的新算符？

---

## 禁止

- 不要假设 GKRR completeness 成立或不成立——你的任务是 *判定* 它的状态
- 不要混淆"completeness in expectation values" 和 "completeness in algebra"
- 不要忽视 ACMP 2025 的反例 —— 它是必须正面处理的对手
- 不要满足于"GKRR 主张..."—— 必须深挖到具体引理和定理层
- **特别警告**：不要假装 GKRR 是已证 theorem 然后绕过 ACMP——这是叙事退让

---

## 产出格式

```
⚡ 审核入口（PI 只读）：
  GKRR completeness 状态：[theorem / conjecture / open / setup-dependent]
  关键隐含假设清单：[3-5 条，每条一句话]
  ACMP 反例处理：[option 1/2/3]
  Phase 1 K1.10 升级判定：[可升级 ✅L2 / 维持 ⚠️L1 / 需降级]
  最脆弱论证步骤：[一句话]
  
然后 §0/§0.5/§1/§2/§N/§末 完整作业。
```

---

## 关键文献

- arXiv:2012.05770 (Raju "Lessons from the information paradox" — 必读 §3-5)
- arXiv:2602.06543 (GKRR "Seeing Page Curves with Blinders On" — 必读全文)
- arXiv:2506.04311 (ACMP "Apologia for islands" — 必读 §3-4)
- arXiv:2209.10454 (CPW Type II_∞)
- arXiv:2306.03999 (Penington-Witten "Algebras and States in JT gravity")
- arXiv:2110.05497 (Leutheusser-Liu Type III_1 → Type II)
- arXiv:1402.6334 (Almheiri-Polchinski JT HKLL)
- arXiv:2107.03390 (Geng-Karch "Inconsistency of Islands in Long-Range Gravity")

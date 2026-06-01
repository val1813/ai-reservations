# B博士 Phase 2 作业 — Hawking-Encoding v1: 反面攻 GKRR Completeness

**日期**: 2026-06-01
**任务**: AHA-001 驱动 — 寻找 GKRR completeness 的反例/隐含假设
**角色**: 突击队（B博士，独立作业，零上下文）

---

## ⚡ PI审核入口

- ⚡ **本Phase推进了什么**: 从"GKRR completeness 是定理"推到了"GKRR completeness 至少依赖三个未声明的隐含假设，其中两个在 SYK/JT 中已被文献证伪或未定义，故其严格数学地位退化为 conjecture"
- ⚡ **最关键的跨域连接**: Connes 嵌入问题在 2020 年被 MIP* = RE 证伪 → GKRR completeness 必定在 von Neumann 代数层面依赖于可近似性假设（finite-rank approximation → ultrapower of hyperfinite II₁），该假设对"wild" Type II₁ 因子不成立。在 JT 大 N 情境中，若 boundary algebra 的结构映射到 non-hyperfinite II₁ 因子，GKRR 的 finite-rank 构造（Xₙ P₀ Xₘ†）无法覆盖全部 bulk 算符
- ⚡ **预测 vs 实际**: 预测能找到至少一个致命隐含假设 → 实际找到三个，其中"Type III₁ 不含有限投影 → P₀ ∉ 𝒜_ε"最为致命。结论方向一致但力度超预期——从"可能不严格"升级为"在 canonical ensemble 中直接不成立"
- ⚡ **卡在哪里**: P₀ ∈ 𝒜_ε 的争论在 microcanonical 变体（CPW Type II∞ crossed product）中似乎可修复——GKRR completeness 在 crossed product 语言中是否以"trivial subfactor index"形式复活？需要进一步厘清 crossed product algebra 的 subfactor 结构。当前暂判定为"未解决但有强烈反证压力"

---

## §1 结论预测

### 命题方向
本 Phase 攻击的命题（"GKRR completeness 是 conjectural 而非 rigorous theorem"）若成立，则：

- **方向**: GKRR completeness 的证明在严谨数学物理标准下存在缺口——该缺口在纯 JT 拓扑理论中可闭合，但在 JT + matter / SYK 大 N 中不可闭合
- **量级**: 非"致命反例"（不是显式构造一个 bulk operator φ̂ 同时证明 φ̂ ∉ 𝒜_bdy），而是"隐含假设暴露"（证明 GKRR 的三个关键步骤各自依赖 ensemble-dependent 或 closure-dependent 的假设）
- **后果**: 如果成功 → Phase 1 K1.9-K1.13 全部 conditional → M.B 在 SYK/JT 中不成立的论证需要 ensemble 限定

### 最可能被证伪的环节
- **Step 3（P₀ ∈ 𝒜_ε）**: 在 Type III₁ 代数中不存在有限投影，而 P₀ 是秩-1 投影（有限）。GKRR 必须论证含 H 的 time-band algebra 已非 Type III₁（即已升级为 Type II∞ via crossed product），但这一升级在规范性质上仅在 microcanonical ensemble 中成立，在 canonical (固定 T) 中不成立。SYK/JT 的标准 description 是 canonical（固定 β）→ P₀ ∉ 𝒜_ε。

---

## §2 推导步骤 1：跨域同构 — GKRR completeness 的数学等价物

### 2.1 Reeh-Schlieder → cyclic ≠ complete

[步骤描述]: GKRR Step 2 "∀ |n⟩, ∃ Xₙ ∈ 𝒜_ε: ||Xₙ|0⟩ − |n⟩|| < δ" 本质上是在断言真空对 time-band algebra 是 cyclic 的——这正是 Reeh-Schlieder 定理的内容（在 QFT 中，真空对任意 open region 的 algebra 是 cyclic 且 separating）。

**学科工具**: AQFT (Algebraic Quantum Field Theory) — Reeh-Schlieder theorem (1961)

**依据**:
- Reeh-Schlieder: 对任意开集 O ⊂ Minkowski（或 AdS 边界），代数 𝒜(O) 有真空 |Ω⟩ 为 cyclic vector，即 𝒜(O)|Ω⟩ 在 ℋ 中稠密
- 但这只是 STATE APPROXIMATION（任意态可由 𝒜_ε 作用于真空逼近），不是 OPERATOR EQUALITY（任意 bulk 算符 ∈ 𝒜_ε）

**GKRR 的关键缝合**: GKRR 用 Step 3（P₀ ∈ 𝒜_ε）缝合这个缺口：Q ≐ Xₙ P₀ Xₘ†。没有 Step 3，Reeh-Schlieder 只给出真空 cyclic→ state approximation → 对 bulk 算符的弱近似，但不给出算符本身的代数包含关系。

**反驳检验**: 最易被质疑的是"cyclic = operators can be represented"。Reeh-Schlieder 定理本身不保证 operator representation，只保证 state approximation。这在 AdS/CFT 中尤其关键：bulk 算符的 HKLL reconstruction 给出的是 smeared boundary operator，其误差项在某些 regime 下非零。**不成立条件**: 若 𝒜_ε 不含 P₀，则 GKRR 缝合失败，Reeh-Schlieder 不能升级为 operator completeness。

### 2.2 Type III₁ standard form → completeness ≠ factorized completeness

[步骤描述]: GKRR completeness 声称的是"factorized completeness"——不仅 boundary algebra 作用于 vacuum 生成整个 Hilbert space（standard form），而且所有 bulk 算符都是 boundary algebra 的元素。这就是要求 boundary algebra = B(ℋ)（所有 bounded operators）或至少 B(ℋ) 的某个 dense subalgebra。

**学科工具**: Tomita-Takesaki modular theory, Takesaki duality (1973)

**依据**:
- 在 Tomita-Takesaki standard form 中，一个 von Neumann algebra ℳ 加 cyclic-separating vacuum 自动给出 ℳ|Ω⟩ dense in ℋ（standard form 条件）
- 但这仅保证 ℳ 在 Hilbert space 上的作用是"大"的（cyclic），不保证 ℳ 本身"大"到等于 B(ℋ) 或其 weak closure
- ℳ = B(ℋ) 只在 Type I 因子中可能——这是 trivial 的 QM 情况
- GKRR completeness 要求 ℳ 可以正交投影到任意态矢量上（P₀ 的存在性），这意味着 ℳ 包含所有秩-1 投影 → ℳ = B(ℋ)（Type I）或至少包含 all finite projections（Type II）

**反驳检验**: 若 boundary algebra 是 Type III₁（AQFT 的典型结果），它不含任何有限投影 → P₀ ∉ ℳ → GKRR completeness 不可能以 claimed form 成立。**为什么不成立**: 引入 H 能否将 Type III₁ 升级？理论上 Takezaki duality 使 Type III₁ ≅ (Type II∞) ⋊_θ ℝ，含 H 的 algebra 在 crossed product 意义上等于 Type II∞。但这要求: (a) 正确识别 modular automorphism group；(b) 正确选取 weight/ensemble。这两个选择在物理上不对应唯一方案——存在不同的 crossed product 给出不同 algebra。

### 2.3 Connes embedding problem → wild factors 阻挡 finite-rank approximation

[步骤描述]: GKRR 的构造 Q ≐ Xₙ P₀ Xₘ† 本质上是 rank-1 算符的有限线性组合（或弱极限）。这假定 boundary algebra 的有限秩算符弱闭包 = 整个 algebra。对于 hyperfinite II₁ 因子此假设成立（由定义），但对 non-hyperfinite 因子不成立。

**学科工具**: Connes classification (1976), Connes embedding problem (1976-2020)

**依据**:
- Connes embedding problem (CEP): 是否所有 separable II₁ 因子都可嵌入超幂 R^ω（hyperfinite II₁ 的超积）？
- 2020 年 Ji-Natarajan-Vidick-Wright-Yuen 证明 MIP* = RE，直接推得 CEP 为 FALSE
- **这意味着**: 存在 separable II₁ 因子 ℕ 满足 ℕ ⊄ R^ω → ℕ 中有 finite-rank 算符极限不能逼近的元素
- 在 GKRR 语言中: 若 boundary algebra ≅ ℕ（wild factor），则 Xₙ P₀ Xₘ† 型算符（有限秩组合）不能稠密覆盖 ℕ → 存在 bulk 算符不被任何序列 Xₙ^{(k)} P₀ Xₘ^{(k)†} 弱逼近

**反驳检验**: 最易被质疑的是"boundary algebra 是否真的是 wild factor"——对 SYK at large N（Type III₁ → crossed product → Type II∞），结果 factor 是 hyperfinite 还是 non-hyperfinite？大 N 极限下，SYK 边界 algebra 的超有限性在 current literature 中尚未被澄清。**不成立条件**: 若 SYK/JT boundary algebra 恰好是 hyperfinite（如在 integrable 子扇区），CEP 不提供反例。

### 2.4 四个候选跨域同构的结论

| 候选同构 | 对应 GKRR 的哪个步骤 | 已知漏洞 | 漏洞是否可传递到 GKRR? |
|---------|-------------------|---------|---------------------|
| Reeh-Schlieder | Step 2 (cyclic vacuum) | 给 cyclic 不给 factorized completeness | **是** — Step 2 本身不够，依赖 Step 3 缝合 |
| Type III₁ standard form | 整体框架 | 没有有限投影 | **是** — P₀ ∉ Type III₁，需 crossed product 升级 |
| Connes embedding | Finite-rank 近似 | CEP 为假 → wild II₁ 不可被有限秩逼近 | **部分** — 取决于 SYK boundary algebra 的类型 |
| Voiculescu free prob. GFF GNS | 整体框架 | GFF GNS 覆盖 Fock，但 SYK 有 interaction | **否** — free prob 描述 Gaussian 部分，SYK 有非 Gaussian |

---

## §3 推导步骤 2：跨域反例 — 相邻数学结构中的 failures

### 3.1 Split property 的 failure

[步骤描述]: Split property 保证沿空间分割时，区域代数 tensor-factorize（之间无纠缠的代数意义）。部分 conformal nets 中 split property fails → boundary algebra 沿径向的 "factorization" 可能在部分 setup 中也 fails。

**学科工具**: Doplicher-Longo "Standard and split inclusions of von Neumann algebras" (Inventiones 1984), Buchholz-D'Antoni-Longo (1990)

**依据**:
- Split property 要求区域 A ⊂ B（having non-empty causal complement between them）时存在 Type I 因子 N 满足 𝒜(A) ⊂ N ⊂ 𝒜(B)
- 在 conformal nets 的 diff-covariant 表示中，split property 等价于 trace class condition（D'Antoni-Longo-Radu 2002）
- **部分非有理 conformal nets 中 split property fails**——因为 𝒜(A) 和 𝒜(B) 之间的相对 commutant 为 trivial，但不存在插入的 Type I 因子
- 这是一个已知的"algebra fails to factorize"案例

**对 GKRR 的映射**: GKRR completeness 声称 "bulk Hilbert space does not factorize along radial direction"。这是把 split-property failure 视为 feature 而非 bug。但如果将 GKRR 的结论反向：split property 的 failure 是特殊 setup（高对称 / CFT 特定性质）的特例，而非一般量子引力的普适性质？那 GKRR completeness 在 split property 成立的 setup（generic non-CFT QFT in curved spacetime）中就不成立。

**反驳检验**: 最易被质疑的是 GKRR 是否在 claim "not factorize"（反对 split）还是"completeness"（更强）。这两者不等价。在 split property fails 的 setup 中，依然可以有"boundary algebra 不包含所有 bulk 算符"。

### 3.2 AQFT 中 asymptotic completeness 的已知反例

[步骤描述]: 在弯曲时空中，asymptotic completeness（散射态的 Fock 空间描述是否完整覆盖物理 Hilbert space）已知在 long-range 相互作用和红外发散下 fails。

**学科工具**: AQFT in curved spacetime (Brunetti-Fredenhagen-Verch, Hollands-Wald)

**依据**:
- 在 massless QFT 中，红外发散阻止定义标准的 LSZ 散射矩阵——不存在标准的 in/out Fock space
- 在 de Sitter 时空中，infrared 效应产生 asymptotic symmetry 代数，其对物理态的表示可能不覆盖完整 Hilbert space
- 这些 failure 的数学原因是：某些"软"自由度（soft modes）不能用 asymptotic 算符的 algebra 捕获

**对 GKRR 的映射**: GKRR 在 flat space 的论证使用 ℐ⁺ 上的 asyptotic algebra（𝒜_ε near past boundary of ℐ⁺）。若 asymptotic completeness in 弯曲时空以已知方式 fails for soft modes → 这些 soft modes 的对应物在 GKRR setup 中可能同样不能被 𝒜_ε 捕获 → Yohsida 的"soft modes"恰好是需要额外 early radiation 才能恢复的模式。

**反驳检验**: ℐ⁺ 的 asymptotic algebra 与 flat-space AQFT 中 asymptotic completeness 不是同一结构——前者是 algebra 定义，后者是粒子解释。该类比可能是"表面类比"而非"结构同构"。

### 3.3 C* closure vs ultraweak closure

[步骤描述]: GKRR 构造用的是范数逼近 ("||...|| < δ", i.e., norm topology) 还是弱算子逼近 (ultraweak topology)？C* 代数（范数闭包）与 von Neumann 代数（超弱闭包）有本质不同的 completeness 性质。

**学科工具**: Operator algebra — C* vs von Neumann algebra closure

**依据**:
- C* 闭包（norm closure）: 不保证含所有 spectral projections，不保证含 P₀
- von Neumann 闭包（ultraweak closure）: 保证含 spectral projections of affiliated operators → P₀ ∈ 𝒜_ε''（double commutant, von Neumann closure）但未必 ∈ 𝒜_ε（原 C* 代数）
- GKRR 的 notation ||Xₙ|0⟩ − |n⟩|| < δ 使用 HILBERT SPACE norm，暗示他们考虑的是 𝒜_ε 在 ℋ 上的 action 的弱闭包
- 但"算符在代数中"这一问题，使用 weak closure ℳ = 𝒜_ε'' 时 P₀ ∈ ℳ（if H affiliated to ℳ），使用 norm closure 时则不保证

**结论**: GKRR 混淆了"算符在 von Neumann algebra 中"（P₀ ∈ 𝒜_ε''）和"算符在 C* algebra 中"（P₀ ∈ 𝒜_ε），后者在一般 Type III₁ 中不成立。Completeness 声称必须明确代数类型。

---

## §4 推导步骤 3：SYK/JT 中的具体反例候选

### 4.1 Wormhole saddle → non-trivial center (Type II∞ vs Type III₁)

[步骤描述]: CPW (arXiv:2209.10454) 构造 Type II∞ algebra for JT in microcanonical ensemble via crossed product ℳ_R,0 ⋊_ℝ_h。但在不同 ensemble 下 type 不同——grand canonical 是 Type III₁。

**学科工具**: CPW crossed product, Takesaki duality, Connes type classification

**依据**:
| Ensemble | Algebra Type | 中心 | P₀ 在 algebra 中? |
|----------|-------------|------|------------------|
| Microcanonical (窄能量带) | Type II∞ | trivial (# center) | 是 (有限迹投影) |
| Canonical (固定 T, N=∞) | Type III₁ | trivial | 否 (无能有限投影) |
| Grand canonical (N=∞) | 取决于 scaling | 可能 non-trivial | 取决于 |

- CPW 明确指出: canonical ensemble at N=∞ has divergent energy fluctuations → ˆa = (H−E₀)/N commutes with everything → Type III₁ with infinite-dimensional center
- 构造 Type II∞ 需选择 microcanonical（finite energy window）→ 这是一个具体的物理选择，不是 universal

**对 GKRR 的反驳**:
- GKRR 的 proof 不指定 ensemble → 隐式假定 energy fluctuations 使 H 可观测量 well-defined 且 P₀ 在 algebra 中
- 在 canonical SYK（这是实验设置——固定温度的黑洞）中，Type III₁ 不含 P₀ → GKRR Step 3 fails
- 若坚持 GKRR 成立必须切换到 microcanonical → 那 GKRR completeness 不是普适定理，而是 "在特定 ensemble 选择下成立"

**反驳检验**: 最易被质疑的是 GKRR 可能可以反驳"我们从来都是在 microcanonical 意义下陈述"——但他们的论文（2602.06543）中并无此限定。他们论证"Page curves require removing Hamiltonian"是 module-free 的声称，不存在微正则限定。

### 4.2 Holonomy / topological mode in JT

[步骤描述]: 在 JT gravity 中，bulk 几何由 dilaton + holonomy 沿 non-contractible cycles 分类。这些 holonomy 是 global/topological 自由度。问题是：它们是否真的能被 boundary local data 完全决定？

**学科工具**: JT as BF theory (SL(2,ℝ) gauge), holonomy conjugacy classes, 边界 Schwarzian

**依据**:
- 纯 JT（无 matter）: 约束 F = 0 消除所有 local bulk 自由度 → 物理完全由边界 reparameterization mode确定。Holonomy conjugacy class 由 boundary condition（ADM mass）唯一确定。**Boundary algebra IS complete in pure JT**
- JT + matter: matter fields 引入额外自由度。bulk matter field configurations 不能仅由边界数据确定（unless HKLL reconstruction works for all points）
- 具体构造: 考虑 JT 中两个 spacelike separated bulk 点 x, y 上的 matter 算符 φ(x)φ(y)。在 GKRR completeness 下，存在 boundary time-band operator O ∈ 𝒜_ε 满足 ||O − φ(x)φ(y)|| < ε。但在 JT + matter 中，matter 在 bulk 满足标准的微扰 QFT 性质——若 φ(x)φ(y) ∈ 𝒜_ε，则 bulk lightcone 的因果结构与 boundary algebra 的代数结构之间存在 un-natural 约束

**反驳检验**: JT 是 2D toy model——matter 的 HKLL reconstruction 在 2D 中可能确实 trivial。这是"玩具模型的 artifact"而非普适反例。

### 4.3 Edge modes in entanglement entropy as boundary-external degrees

[步骤描述]: Donnelly-Wall (PRL 2015, PRD 2016) 论证 gauge theory 的 entanglement entropy 包含 edge mode 贡献——这些 edge mode 不在 bulk algebra 中，但也不在"naive boundary algebra"中。如果 island 计算需要这些 edge modes，它们是否对应 GKRR completeness 的一个盲点？

**学科工具**: Donnelly-Wall 2015, 边界对称性代数

**依据**:
- 在 Maxwell theory 中，entanglement entropy 含 boundary edge mode 贡献——来源是 entangling surface 上的 gauge transformation
- 在 JT 的 island setup 中，QES (quantum extremal surface) 类似 entangling surface——island 的 boundary 存在"edge mode"贡献
- 如果这些 edge modes 本质上是非局部的（需要 both boundary + island data 才能定义）→ 它们不单独在 boundary algebra 中

**对 GKRR 的反驳**: GKRR 否定 island 需要额外 bath。但 Donnelly-Wall 的 edge modes 提供了一个具体的反构造——存在物理自由度（edge modes）需要 island boundary 数据（非纯 boundary 数据）才能定义。

**反驳检验**: 这不直接 attack GKRR completeness（GKRR 可以回应: edge modes 也在 boundary algebra 中，只是通过非局部的 reconstruction）。该反例只是间接暗示"bulk 数据 → boundary 数据"的映射可能比 GKRR 声称的更复杂。

---

## §5 推导步骤 4：ACMP 2025 反例的跨域升级

### 5.1 ACMP localizer 不限于 R

[步骤描述]: Phase 1 §4.2 论证"JT 半经典 R 恒定 → ACMP localizer 塌缩"。但 ACMP 的 compactly supported gauge-invariant operator 构造不限于 curvature scalar R 作为 localizer。

**学科工具**: ACMP §4, BBPSV (arXiv:2022/2023), Geng-Karch 引力约束 dressing

**依据**:
- ACMP localizer 的核心机制是对称性破缺 (broken isometries): 任何 background 中的非对称特征都可以作为 gravitational dressing 的 anchor
- 候选 localizer: (a) Riemann 缩并 R_{abcd} R^{abcd} — 在 2D JT 中此 = R²（因为所有曲率由 single scalar capture），所以与 R 等效；(b) matter composite (φ²)(x) — 在 generic background 中提供额外标量场，可区分 bulk 点；(c) dilaton Φ (JT 特有) — 比 R 更强：Φ(x) 的梯度提供"directional localizer"
- **关键升级**: 在 JT 中，dilaton Φ(x) 在经典解上是 spacetime 坐标的单调函数（Φ ~ r²），因此 Φ(x) 本身可作为 localizer——比 R(x) = constant 更有效！ACMP 在 JT 中可用 Φ(x) 而非 R(x) 做 localizer

**反驳 Phase 1 §4.2**: "ACMP 用 R 做 localizer 失效"在 JT 中成立，但"ACMP 用 Φ 做 localizer 有效"同时成立。Phase 1 §4.2 的论证不应被解读为"ACMP 整体在 JT 中失效"，而应解读为"ACMP 在 JT 中需要一个不同的 localizer"。

**结论**: Phase 1 §4.2 需要修正其结论范围——从"ACMP 塌缩"改为"ACMP 需要切换到 dilaton localizer"。

### 5.2 高维 holographic CFT 中的反例

[步骤描述]: 在 4d N=4 SYM 中，边界 CFT 包含 local gauge-invariant operators (e.g., Tr(F²)(x))。这些 operator 的 bulk reconstruction 通过 HKLL 进行——smeared boundary operators。问题是：是否存在 bulk 点 x 上的 local operator φ(x) 不能被边界 CFT algebra 的任何 smeared operator 精确重构？

**学科工具**: HKLL reconstruction, entanglement wedge reconstruction, holographic error correction

**依据**:
- 在 AdS/CFT 中，bulk local operators 的重构在微扰 G 级成立（HKLL），但在非微扰层面有 subtlety
- 具体障碍: 在 bulk 中，gauge-invariant local operator 需要 gravitational dressing to boundary。不同的 dressing choice 给出 operator 的不同"frame"——没有唯一的 bulk local operator
- 这是 GKRR completeness 与 bulk locality 之间的 tension——如果 boundary algebra 完全包含所有 bulk 算符，那么 bulk 中"沿径向"的不同 dressing 对应 boundary algebra 中的不同元素——但这会导致 operator redundancy（多个 boundary 算符对应"同一个"bulk operator in different frames）
- **这本身不构成反例，但指出**: GKRR completeness 要求 bulk 算符与 boundary dressing choice 之间存在高度非平凡的一一映射——这个映射在更高维中的显式构造尚未完成

---

## §6 推导步骤 5：副攻 — collapse / 动力学曲率 setup 中 §4.2 论证的状态

### 6.1 Vaidya AdS₂ collapse + JT: dilaton 仍渐近发散, R 不恒定

[步骤描述]: 在 Vaidya 型 AdS₂ collapse 中，注入物质壳层使时空从纯 AdS₂ 崩塌为 AdS₂ 黑洞。过程中 metric 无时间平移不变性，R(x) 在壳层附近非恒定。检验 ACMP localizer 在此 setup 中的可操作性。

**学科工具**: Vaidya metric in 2D, JT gravity with shockwave, dilaton equation

**依据 (理论推导)**:
- JT action: S = (1/16πG) ∫ d²x √−g Φ (R + 2/L²) + boundary terms
- EOM: R = −2/L² (from Φ variation) — **即使在 collapse 过程中，曲率 scalar R 仍是常数！** 这是 JT 的独特性质：Φ 的 EOM 强制 R 恒等于 cosmological constant。
- 在 Vaidya-type 注入中: 物质应力张量 T_{μν}^{matter} 非零 → dilaton EOM 变成 ∇_μ ∇_ν Φ − g_{μν} □Φ + g_{μν} Φ/L² = −8πG T_{μν}^{matter} → **DILATON 而非 R 携带 collapse 的动力学信息**
- 因此 R(x) = −2/L² 恒成立（即使在 collapse 中），Phase 1 §4.2 的论证"R 恒定 → ACMP 塌缩"**在 JT 中无论是否 collapse 都成立**

**关键领悟**: 在 JT 中，"collapse 让 R 非恒定"这个直觉是错的！JT 的 R 永远是常数。动力学曲率信息被编码在 dilaton Φ 中，不是 R。

### 6.2 Dilaton boundary-reconstructibility 与 ACMP 的 dilaton localizer

[步骤描述]: 既然 ACMP 可以用 dilaton Φ 做 localizer（如 §5.1 所述），那么在 collapse setup 中，Φ 是否 boundary-reconstructible？

**学科工具**: JT dilaton boundary condition, HKLL for dilaton

**依据**:
- Dilaton 在边界发散: Φ(r_bdy) = Φ_b (常数，boundary condition)
- 内部 dilaton profile Φ(r) 由 boundary 数据（reparameterization mode f(τ)，aka Schwarzian mode）确定
- 但这是纯 JT 的情况。加入 matter 后，matter stress tensor 的 backreaction 影响 Φ(r) via dilaton EOM
- 在 collapse setup 中，infalling matter shell 改变 Φ(r) 的 profile——这个变化是否可被 boundary 完全重构？
- **HKLL for dilaton**: 在 JT 中，dilaton 不是 propagating degree of freedom（没有 kinetic term），而是 constraint。因此 dilaton 全由 boundary sources + matter 确定。若 matter 的 boundary data (extrapolated) 已知 → dilaton 可被完全重构
- **反论证**: 若 matter 在 bulk 深部的构型不能由 boundary 推得（GKRR completeness 失效的后果），则 dilaton 也不能被 boundary 完全重构 → ACMP dilaton localizer 同步失效

**结论**: collapse setup 中 §4.2 论证状态 = **仍成立但限定更精细**。R(x) 永远是常数这一事实让 ACMP 的 curvature-based localizer 在 JT 中失效，无论 collapse 与否。但 ACMP 切换到 dilaton localizer 后可以修复——前提是 dilaton 本身 boundary-reconstructible。这形成一个循环依赖: dilaton reconstructibility ⇔ GKRR completeness。

### 6.3 Phase 1 §4.2 修正建议

原: "JT 半经典 R 恒定 → ACMP 用 R 做 localizer 失效"
修正: "JT 中 R 恒为 −2/L²（即使 collapse），ACMP curvature-based localizer 失效。可用 dilaton Φ 做 localizer，但 Φ 的 boundary-reconstructibility 依赖 GKRR completeness——形成自洽性循环。因此 §4.2 的结论在限定为'curvature-based localizer'时成立，在扩展为'ACMP 整体塌缩'时不成立"

---

## §7 推导步骤 6：QEC × completeness — Subfactor 分析

### 7.1 Finite-dim QEC → infinite-dim algebra: the gap

[步骤描述]: Phase 1 §6.1 用 [[5,1,3]] code 论证量子纠错码等价性。但 finite-dim QEC 的等价性不一定推广到 infinite-dim von Neumann algebra。

**学科工具**: Subfactor theory (Jones 1983), von Neumann algebra subfactor, Kosaki-Longo index

**依据**:
- 在 finite dim 中，QEC 等价于互补信道 correctability → algebra isomorphism (up to isometry)
- 在 infinite dim (von Neumann algebra) 中，QEC 对应 subfactor inclusion N ⊂ M，其 Jones index [M:N] 量化 N 在 M 中的"大小"
- [M:N] = 1 ⟺ N = M (trivial subfactor) ⟺ 无信息丢失
- [M:N] > 1 ⟺ N 是 M 的真子代数 ⟺ 存在 N 不可访问的 M 中操作

### 7.2 Subfactor index in JT: 𝒜_bdy vs 𝒜_island

[步骤描述]: 定量估计 [𝒜_full : 𝒜_bdy] 在 JT 中的值。

**学科工具**: Jones index theory, 大 N 代数结构

**依据**:
- 若 GKRR completeness 成立 → 𝒜_bdy = B(ℋ)（或至少 ≡ 𝒜_island）→ [𝒜_full : 𝒜_bdy] = 1
- 若 GKRR completeness 不成立 → 𝒜_bdy ⊊ 𝒜_full → [𝒜_full : 𝒜_bdy] > 1
- 在 JT + N 个 matter fields 中: 𝒜_bdy 由边界 extrapolated operators 生成 (c.a. N² 个 single-trace operators in SYK)，𝒜_full 包括所有 bulk matter operators at arbitrary points
- The dimension count: dim(boundary single-trace sector) ~ N²。bulk 算符空间 (smeared matter fields over bulk region) 在连续极限下是无限维。但 SYK 的大 N Hilbert space 本就是有限维 for 有限 β。在 S_BH ~ N 时 dim(ℋ) ~ e^N。所有 possible operators ~ e^{2N}
- Boundary single-trace 算符数量 ~ N² << e^N（所有可能算符）。但 single-trace 算符的 *多项式* （即 boundary algebra）可以生成指数多的独立算符
- **关键问题**: 边界 single-trace 算符的多项式代数是否 complete (generate all operators) modulo center？这与"single-trace algebra 是否就是 all gauge-invariant operators"等价
- 在 SYK 中，所有 gauge-invariant operators 都可用 single-trace operators 的多项式表示吗？对于 Majorana fermions ψ_i，所有偶多项式（gauge invariant = 偶个 ψ's） = 单迹算符的多项式吗？
- SYK 中 single-trace 是 O_J = i^{q/2} ∑ J_{i₁...i_q} ψ_{i₁}...ψ_{i_q}（对于 q-body interaction）。这些算符的泛函生成不一定覆盖所有偶多项式——存在 non-Gaussian 算符不被 single-trace 捕获

**结论**: 存在 plausible 的理由认为 [𝒜_full : 𝒜_bdy] > 1 在 SYK/JT 中。严格值无法从现有文献直接得出，但 non-trivial subfactor 的可能性很高。

---

## §8 推导步骤 7：BFV × Yang-Yang 升级 — 单向 vs 双向

### 8.1 核心逻辑图

```
复杂度下界 (no polynomial decoder)
    ↓ ?
代数真扩张 (𝒜_island ⊋ 𝒜_bdy, subfactor index > 1)
```

这两个命题之间的关系不是逻辑等价的。

### 8.2 方向 1: 复杂度下界 ⟹ 代数真扩张? → NO (不能保证)

[步骤描述]: 不存在多项式 decoder 不移除代数同构的可能性——可能存在指数复杂的 isomorphism。

**依据**:
- 例: 两个不同的 Type III₁ 因子 ℳ, 可以代数同构（都是唯一的 hyperfinite Type III₁ factor，by Haagerup 1987的所有 Type III₁ hyperfinite factors are isomorphic or by uniqueness theorem），但它们之间的映射（作为 acting on different Hilbert spaces）可能需要复杂的 Connes cocycle
- 更简单的类比: 两个不同的矩阵表示 of the same algebra——表示之间的 unitary 可能指数复杂（由 scrambling 决定）
- Yang-Yang 的结果: "no polynomial decoder for island ⟹ island info not accessible in poly-time from boundary" ——这是 computational 声称，非代数声称

**结论**: Yang-Yang 不支持 𝒜_island ⊋ 𝒜_bdy（真扩张声称）。它们仅支持"access complexity is exponential"。

### 8.3 方向 2: 代数真扩张 ⟹ 复杂度下界? → YES (但 trivial)

[步骤描述]: 若 𝒜_bdy ⊊ 𝒜_island 严格 → 存在 𝒜_bdy 中的算符无法模拟的部分 island 操作 → reconstruction 要求 infinite precision / 不可能 → 当然不会有 polynomial decoder。

**依据**:
- 这是 trivial 的: 如果代数维度不同，任何映射都会丢失信息
- 但反过来——如果找不到 polynomial decoder → 不能推得代数不同

**结论**: BFV/Yang-Yang 与代数真扩张之间的关联是:
- 代数同构 ⇏ polynomial decoder 存在（可能指数复杂）
- 代数真扩张 ⇒ no decoder at all（更别提 polynomial）
- No polynomial decoder ⇏ 代数真扩张（可能是指数复杂 decoder）

### 8.4 Phase 1 §6.3 的解读问题

Phase 1 §6.3 用 BFV + Yang-Yang 论证 "polynomial decoder 不存在 ⟹ A_island ⊋ A_bdy"。如上述分析，这是**逻辑跳跃**——前项只能推出 complexity gap，不能推出 algebraic gap。Phase 1 §6.3 需要修正这个推理。

---

## §末 结论对比

### 预测 vs 实际

- **预测**: GKRR completeness 有隐含假设，最可能被证伪的环节是 Step 3 (P₀ ∈ 𝒜_ε)
- **实际**: 
  1. **确认 Step 3 是致命弱点**——P₀ ∈ 𝒜_ε 在 Type III₁ (canonical ensemble) 中直接不成立。这是最清晰的数学缺口
  2. **额外发现**: (a) Connes embedding false → finite-rank approximation 可能失败；(b) split property 的反面可能不被 universal；(c) edge modes (Donnelly-Wall) 提供额外自由度
  3. **力度超预期**: 原预测"可能不严格"→ 实际为"canonical ensemble 中直接不成立，microcanonical 中待定"

### 5 个必须回答的问题

1. **GKRR completeness 在相邻数学结构中的对应物漏洞是否对应 GKRR 的潜在漏洞？**
   → **是**。Reeh-Schlieder 只给 cyclic（非 completeness），Connes embedding 后 finite-rank 近似 fail，split property fails 在某些 setup 中（split fails 的区域中 GKRR completeness 需要额外的辩护）

2. **JT 中 holonomy / topological mode / edge mode 是否真的可被 boundary local data 完全决定？**
   → **纯 JT: 是**（topological theory，boundary data 完全）。**JT + matter: 不一定**——matter 的自由度提供额外数据，是否 boundary-reconstructible 依赖 HKLL reconstruction（已知在微扰 level 成立，非微扰 level 未证明）

3. **Subfactor index [A_full : A_bdy] 在 JT 中的具体值？**
   → **无法从现有文献确定**。但结构性论证指出 [A_full : A_bdy] > 1 的可能性很高（SYK single-trace algebra 不必然覆盖所有奇偶多项式）。需要显式计算来确定。

4. **在动力学曲率 setup 中，Phase 1 §4.2 论证是否仍成立？**
   → **"R 恒定 → ACMP curvature-based localizer 塌缩"仍成立**（R 在 JT 中永远是 −2/L²）。但 ACMP 整体不塌缩——可切换到 dilaton localizer。§4.2 的结论需要限定为"curvature-based localizer only"。

5. **BFV/Yang-Yang 复杂性下界 ↔ algebra 真扩张是单向还是双向关联？**
   → **单向**（代数真扩张 ⇒ 无 decoder），反向不成立（无 polynomial decoder ⇏ 代数真扩张）。Phase 1 §6.3 的推理需要修正。

### 自我反向攻击结果

| Phase 1 论证 | 是否需要修正 | 修正程度 |
|------------|-----------|--------|
| §4.2 "R 恒定 → ACMP 塌缩" | 是 | 限定为 curvature-based localizer，不排除 dilaton localizer |
| §5 no-go ε(N) ~ e^{-cN} | 部分 | no-go 的有效性现在 conditional on GKRR completeness (微正则限定) |
| §6.1 QEC [[5,1,3]] code 等价 → algebra 等价 | 是 | finite-dim QEC 不等价于 infinite-dim algebra 等价 |
| §6.3 BFV/Yang-Yang → 真扩张 | 是 | 逻辑跳跃——复杂度下界不能推出代数真扩张 |
| K1.9-K1.13 no-go 路径 | 部分 | 现在皆是 conditional 声明，unconditionally 成立仅在 microcanonical + GKRR completeness 假设下 |

### 最终判决

**GKRR completeness 的法律地位**: 在微观正则 (microcanonical + Type II∞ crossed product) 构架下，GKRR completeness 的数学核心 (P₀ ∈ 𝒜_ε) 可能成立。在正则 (canonical + Type III₁) 中，**不成立**。GKRR 的原始文献 (arXiv:2602.06543) 未指定 ensemble，使其声称的范围模糊。

**严格意义上**: GKRR completeness 是 **conjecture**（非定理），其成立依赖于特定的 ensemble 选择和代数 closure 约定（C* vs von Neumann）。在这些选择明确化之前，Phase 1 的 no-go 定理应被标识为 conditional on GKRR completeness。

**推进建议**: 下一步 (Phase 3) 应在 microcanonical Type II∞ crossed product 构架中重新检验 Phase 1 no-go——这是在"最有利 GKRR"的框架下进行压力测试，若 no-go 通过此测试则无条件成立。

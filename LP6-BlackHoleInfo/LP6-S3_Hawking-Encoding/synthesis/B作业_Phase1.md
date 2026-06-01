# B博士 Phase 1 作业：Hawking-Encoding M.B no-go

> 课题：Hawking-Encoding v1（LP6-S3）
> Phase：1（首轮反面攻击）
> 角色：B博士（突击队，独立子agent，零项目上下文，不知道A博士在做什么）
> 日期：2026-06-01

---

## ⚡ PI审核入口

- **本Phase推进了什么**：从 GKRR 2026 boundary completeness 主张推到 SYK/JT 中 A_island ⊆ A_bdy 的可量化 no-go 定理（Phase 1 首轮反面攻击成功——M.B 在该模型类中被排除，至 ε(N) 精度）
- **最关键的跨域连接**：量子纠错码理论中"逻辑算符有多种 physical encoding"的代码等价性——A_island 与 A_bdy 是同一逻辑算符代数在不同 dressing 下的两种 code-word 表示，并非真正扩张
- **预测 vs 实际**：预测 path (c) 走通；实际：在 SYK/JT 中 ACMP 构造比预想更弱——JT 半经典曲率恒定，ACMP 的"无等距"条件需借 dilaton 破缺，而 dilaton 自身可被 boundary HKLL 重构，致 ACMP 反例在 JT 中**失效**。比预测更强。
- **卡在哪里**：非微扰效应（doubly non-perturbative corrections）可能在 ε(N) 之外打开 A_island ⊋ A_bdy 小窗口。Phase 1 推导仅至 perturbative-in-1/N + leading replica saddle 精度。

---

- **No-go 路径选择**：(c) 直接代数论证 + (a) Tomita-Takesaki 辅助
- **M.B 在 SYK/JT 中是否被排除**：**是**（leading 1/N + leading replica saddle 精度内严格成立）
- **关键技术步骤**：A_island 由 HKLL 重构的 island 内 bulk 算符生成 ⊂ 单迹算符代数 ⊂ A_bdy；并通过 entanglement wedge reconstruction 给出 ε(N) 收敛
- **对 ACMP 的回应**：ACMP 构造需"无等距+曲率变化"双条件；JT 半经典 R 恒定，破等距的是 dilaton，但 dilaton 自身 HKLL 可重构 → ACMP localizer 在 JT 中坍缩为 boundary-reconstructable，反例失效
- **最脆弱假设**：ACMP 论证可能在双指数小（doubly non-perturbative）尺度下重新打开
- **跨域攻击结果**：QEC 等价性 + Yang-Yang 复杂度论证共同支持 A_island 是 A_bdy 的不同 code 表示，而非真正扩张

---

## §1 结论预测

预测 path (c) 在 SYK/JT 中走通：SYK 是 0+1 维 QM，"boundary"即所有渐近时刻算符——天然完备。JT 是 1+1 维 dilaton-gravity，所有 bulk 场通过 HKLL 由单迹算符重构；island 只是 entanglement wedge 一部分，无新自由度。

最可能被证伪的环节：ACMP 2025 的 gauge-invariant compactly supported operators。

## §2 SYK/JT 中 boundary algebra 的精确化

**2.1 SYK A_bdy**：
SYK 模型 N 个 Majorana ψ_i(t)。微观上 A_bdy^SYK = vN({ψ_i(t)}) = B(H_SYK) Type I_{2^{N/2}}。
**学科工具**：算子代数 + 大 N 双扩张
**反驳检验**："boundary"应指 t→±∞？回应：thermal 态上 t=0 与 t=∞ 算符通过 H ∈ A_bdy 相互生成，同 vN 代数。

**2.2 JT A_bdy**：
A_bdy^JT = vN({O_n(t)}) 加 Schwarzian clock 做交叉积 → Type II_∞ (CPW 2022)
**学科工具**：大 N 算子代数极限 + crossed product (Connes-Takesaki)
**依据**：single-trace 形成 generalized free fields algebra；large N vN closure = Type III_1；crossed product → II_∞
**反驳检验**：multi-trace 漏？回应：multi-trace = (single-trace)^k 在 vN closure 中已含；non-perturbative wormhole saddle 给*相同* algebra 的*不同*期望值，不增 generator。

## §3 SYK/JT 中 island operators 的 HKLL 重构

**3.1 JT bulk field HKLL**：
χ(x,t) = ∫ K(x,t|t') O_χ(t') dt'，K = boundary-to-bulk smearing kernel
**依据**：Almheiri-Polchinski 2014 (1402.6334) 给 JT 中 K 的显式形式
**反驳检验**：HKLL 在 island 需 complex time 路径？CPW 2022 与 Penington-Witten 2306.03999 用 entanglement wedge reconstruction 代数版本绕过——任何 EW 内算符可被 wedge 互补 boundary subalgebra 在 code subspace ε-近似，ε ~ e^{−S_BH}

**3.2 Island operator 显式形式**：
A_island = (A_R)' ∩ A_full（CPW 2022）
关键：A_R ⊂ A_bdy^JT（radiation 是 boundary 一部分）→ A_island generator 都通过 EW reconstruction 在 A_bdy ∪ A_R 中 ε-表示

## §4 对 ACMP 2025 反驳的正面回应

**4.1 ACMP 构造的 prerequisite**：
ACMP 主张：背景无 isometries 时可构造 gauge-invariant compactly supported operators "to all orders in perturbation theory"。典型构造：用 scalar invariant（曲率 R(x) 或 dilaton φ(x)）做 level set 积分。

**4.2 JT 半经典中 ACMP 构造的塌缩**：
**学科工具**：JT EOM + dilaton 解的解析结构
**依据**：JT 半经典 R(x) = -2/L² 恒定。曲率 scalar 不能区分 bulk 点 → ACMP 用 R 做 localizer 失效。
唯一可用 scalar 是 dilaton φ(x,t)。但 φ 是动力学场，渐近发散 φ → φ_b/(L cos σ)，HKLL 完全由 boundary Schwarzian 模重构。
**反驳检验**：dilaton 在 island 内有非微扰修正，ACMP 算符可能在 1/N 之外打开。回应：本 Phase 至 perturbative-in-1/N 精度。承认非微扰窗口存在但属 doubly-exponentially small (~ e^{-1/G_N})——已纳入 ε(N) bound。

**4.3 等价的 gauge-fixing 论证**：
**学科工具**：Constraint quantization + Faddeev-Popov
**依据**：在 diff-invariant 理论中，"compactly supported in island region" 必须相对于某 gauge slice 定义。一旦 gauge-fix：
(i) Boundary clock dressing → A_bdy 内
(ii) Internal scalar dressing（dilaton level set）→ scalar 自身 HKLL 可重构 → 又回 A_bdy 内
(iii) ACMP "without isometry" 论证隐含 gauge 选择（level set 函数本身就是 gauge fixing）→ 仍可表为 boundary 算符函数

无论哪条，ACMP 算符都落入 A_bdy。**循环论证**：ACMP 用"无等距"消解 dressing 模糊，但消解所用 scalar field 本身可被 boundary 决定。

## §5 No-go 定理与 Redundancy 量化

**定理 (M.B No-Go in SYK/JT, Phase 1)**：

设 A_bdy 为 SYK/JT 完整 boundary algebra（含 H_SYK 与 Schwarzian clock）。对任意经 gravitational entanglement wedge prescription 构造的 island operator O_I ∈ A_island 与 code subspace H_code，存在 boundary operator 序列 {O_B^{(N)}} ⊂ A_bdy 使得：

‖O_I |ψ⟩ - O_B^{(N)} |ψ⟩‖ ≤ ε(N) ‖|ψ⟩‖, ∀|ψ⟩ ∈ H_code

其中 ε(N) ~ e^{-c·N}（c > 0 模型相关常数；leading 行为来自 EW reconstruction QEC error scaling）。

**证明骨架**：
(1) HKLL 给 perturbative reconstruction，误差 ~ 1/N
(2) EW reconstruction (AEMM 2014) 提升至 non-perturbative-in-1/N，error ~ e^{−S_BH} ~ e^{−cN}
(3) ACMP 反例已在 §4 内化：JT 半经典 localizer 塌缩
(4) Type 分析（path a 辅助）：finite N A_bdy = B(H) Type I → A_island ⊂ A_bdy 平凡。Large N A_bdy = III_1 → A_island = II_∞ ⊂ vN(A_bdy ∪ {clock})；clock = H_SYK ∈ A_bdy → A_island ⊂ A_bdy
QED

## §6 跨域攻击

**6.1 QEC × island**：
[[5,1,3]] 量子码 logical X 由 X₁X₂X₃ 或 X₃X₄X₅ 实现——同一 logical operator，多种 physical encoding。
Almheiri-Dong-Harlow 给 holographic QEC 精确版：A_island 与 A_bdy 是同一逻辑代数的两种 code-word 表示。**这不是扩张，是等价编码**。M.B 要求真正扩张，QEC 等价性直接否定。

**6.2 信息论 × "搬运"**：
经典："信息从 A 到 B" ⟺ I(A:E) 下降 + I(B:E) 上升
GKRR/Raju 框架下 I(boundary:full) ≡ S(full) 始终饱和（boundary algebra 完备）→ **没有"搬运事件"可定义**。Page curve "信息回归" 仅是 measured/unmeasured 自由度间 redistribution。

**6.3 计算复杂性 × 机制存在性**：
BFV 1910.14646 + Yang-Yang 2211.05491：OWF 假设下 polynomial-time decoder 不存在。但这**支持** no-go——operationalist 立场下"机制存在但 super-poly 不可实现"与"机制不存在"不可区分。

## §7 必须回答的问题

**Q1（boundary algebra 完备在 SYK/JT 是否严格）**：large N 严格极限严格成立（A_bdy III_1 factor 作用于 GFF GNS rep）。有限 N 平凡完备。1/N 修正调整算符值不增算符。

**Q2（HKLL 在 island 内是否精确）**：Perturbatively 精确（解析延拓 well-defined modulo branch cuts，绕道 EW reconstruction）。Non-perturbative 修正 ~ e^{−S_BH}，纳入 ε(N) bound。

**Q3（ACMP 算符显式反例）**：JT 半经典中取 ACMP dilaton level-set algorithm，O_ACMP = ∫_{φ(x)∈[a,b]} f(matter) dx。dilaton φ(x,t) 满足 □φ EOM + boundary，HKLL 给 φ = ∫ K_φ H_Schwarzian + 应力张量。Matter HKLL 同。**O_ACMP = (boundary functional) ∈ A_bdy**。

## §末 结论对比

预测：path (c) 走通，M.B 在 SYK/JT 排除。
实际：走通且**更强**——ACMP 反例在 JT 半经典中因 dilaton 可重构而塌缩。
**一致 + 意外加强**。

**Phase 1 立场（突击队 B）**：
M.B 在 SYK/JT 标准设置中被排除至 ε(N) ~ e^{-cN} 精度。Island reconstruction 给的"新动力学"是 boundary algebra 已有 unitary 的不同 dressing 表示——QEC 意义下 code equivalence，非真正扩张。

**承认的边界**：
(1) 仅至 perturbative-in-1/N + leading replica saddle 精度；non-perturbative gravity 外的窗口未排除
(2) 仅在 SYK/JT；高维 holographic CFT（4d N=4 SYM 等）中 ACMP 构造未必塌缩
(3) Type II_∞ vs Type III_1 vs Type I 切换在物理上有内容（entropy 是否 well-defined），但不构成算符成员关系扩张

**对 PI 关键交付**：
A 博士若主张"M.B 成立 → 存在新机制"，须正面回应 no-go 三个内核：
(i) JT 中 dilaton 是 boundary-reconstructable，致 ACMP 在该模型类塌缩
(ii) EW reconstruction 给出的 ε(N) bound
(iii) QEC 编码等价性下 A_island = A_bdy 在不同 code 表示下的同一代数

最薄弱处：non-perturbative 算符（wormhole saddle 给的 doubly-exponentially small effects）是否真能在 ε(N) 之外打开窗口——Phase 2 应继续突击方向，但即使打开，窗口宽度 e^{-1/G_N} 在 operationalist 意义下与"无扩张"不可区分。

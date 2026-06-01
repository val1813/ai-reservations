## v8 收官 恶意审稿人报告 — Nature Physics 匿名审稿

> 审稿人立场：根本性怀疑。零项目上下文。仅基于上述十条结论与公开文献。
> 审稿日期：2026-05-30。审稿目标期刊：Nature Physics。

---

### 第一步：查重结果

按结论核心声张分别核查（Semantic Scholar / OpenAlex / arXiv）。

| 结论 | 关键词 | 查重结果 |
|---|---|---|
| **v8-K1** | "bath internal entropy production" + reference Gibbs + finite unitary | 查重通过，未发现完全相同的"任意 β 参考态闭式恒等式"表述。但浴侧 D(ρ_B‖ρ_B^{ref}) 单调性失败已有相关讨论（Strasberg–Winter 2021, PRX Quantum 2, 030202；Esposito–Lindenberg–Van den Broeck 2010, NJP 12, 013013）。 |
| **v8-K2** | Spohn inequality violation strong coupling | ⚠️ **接近重复**：Pucci–Esposito–Peliti 2013, J. Stat. Mech. P04005 (arXiv:1210.4111) 明确指出强耦合下"ideal canonical equilibrium of the bath is violated"，并比较 ELB 与 Poised 两种熵产生定义。Spohn 三层前提的失效在 Strasberg–Winter 2021 中已系统讨论。**独特贡献需澄清**：v8-K2 是否仅复述既有失效列表？|
| **v8-K3** | Jaynes-Cummings negative entropy production rate | ⛔ **重复造轮子警告级别 = 中**：Aoki–Matsuzaki–Hakoshima 2021 (arXiv:2103.05308, PRA 103, 052208) 已给出有限谐振子星型构型下"GKSL Markovian 子动力学却出现总熵产生率负值"的数值反例。v8-K3 自称"在 JC 模型上的精化闭式"——但需明确闭式表达式 −βωg 是否真为新结果，还是只是 Aoki 设置的最简退化。 |
| **v8-K4** | Nakagawa structural theorem CP-divisibility | 查重命中：arXiv:2602.09054 (Nakagawa 2026) 主题为 TC/TCL 框架下信息回流的结构理论，**未在摘要层面**直接论及"两条充分前提在偏迹幺正下系统性失效"。v8-K4 对 Nakagawa 工作的限制性陈述尚未发表，**形式独特**，但需确认 Nakagawa 原文是否已隐含此条件破坏。 |
| **v8-K5** | gauge identity dI/dt + βdC − Σ_B^{int} | 查重通过，未发现完全相同的 gauge 分解恒等式。Esposito 2010 (NJP 12, 013013) 的 σ = I(S:B) + D(ρ_B‖ρ_B^{eq}) 是其浅版本。 |
| **v8-K6'** | passive state + modular flow second law | 查重通过，未发现"passive ⊕ modular 同号 ⟹ Σ_B≥0"的双重充分条件文献。Pusz–Woronowicz 1978 + Lenard 1978 是 passive-only 路线。 |
| **v8-K7** | BKM second-order kernel KMS susceptibility | 查重通过。BKM kernel + KMS 在 Landi–Paternostro 2021 (Rev. Mod. Phys. 93, 035008) 的弱耦合熵产生章节有相关讨论，但 dephasing g² vs dissipative g⁴ 的二分**未见独立闭式定理**。 |
| **v8-K8** | "北极星 r(β) = 1 − (4/π)arccot(e^{βω₀/2})" | 查重通过，未发现该闭式公式。但"温度依赖的有效性区域"在 Cresser–Anders 2021 强耦合 mean-force 文献中有定性讨论。 |
| **v8-K9** | N_I^{(S)} = 2 ln 2 几何不变量 | 查重通过，未见耦合无关的 g-不变 entropy integral 闭式。 |
| **v8-K10** | c(β) = −ln cosh(βω₀/2)/(2 ln 2) 复合身份定理 | 查重通过，未发现该闭式比值定理。但"信息回流主导 vs inherent 浴熵"的概念二分在 Breuer–Laine–Piilo 2009/2016 与 Strasberg–Winter 2021 中有定性区分；v8-K10 把它定量化到 toy 模型——需警惕"toy 闭式 ⟹ 物理普适性"的过度推广。 |

**总结**：K3 接近 Aoki 2021 的 JC 退化版本，需明显划清贡献边界；其余八条形式上未撞车，但**多条声张依赖单一 N=2 双模 JC toy**，普适性不足以支撑 Nature Physics。

---

### 五条拒稿理由

#### 1. 核心假设的最简反例 —— 攻击 v8-K10 c(β) 闭式定理 [致命]

v8-K10 给出 ∫_{T_<^B} Σ_B^{int} dt = −ln cosh(βω₀/2) 与北极星 N_I^{(S:B)} = 2 ln 2 的比值闭式。但该恒等式**完全寄生于** N=2 双模 JC + 真空浴 + 共振 + 对称耦合的极简 toy。一旦把浴扩到 N=3 模（保持共振），双模回流的 Rabi 周期性变成 quasi-period，T_<^B 的截断时间不再唯一定义；passive 浴+真空初态在 N≥3 仍成立，但 modular phase-lock 因模间 commensurability 失败，Σ_B^{int} 的累积积分不再有 ln cosh 闭式。换言之，c(β) 不是温度的函数，而是"温度 × 浴维度 × 谱密度"的函数；把 c(β) 写成温度的单变量函数误导读者以为这是普适标度。**作者需证明**：c 在 N→∞ 极限下有良定义、且与 toy 的 −ln cosh(βω₀/2)/(2 ln 2) 至少在 leading order 一致；否则"复合身份定理"应降级为"N=2 toy 现象"。

#### 2. 推导链最薄弱一步 —— v8-K6' 必要性 vs 充分性的逻辑混乱 [严重]

v8-K6' 表述"passive ∧ modular-同号 ⟹ Σ_B^{int}≥0；passive failure 是 sufficient 但非 necessary 的破坏路径，modular phase-lock failure 是 necessary 但非 sufficient 的破坏路径"。这两句并存逻辑可疑：若 passive failure 是充分的破坏路径（passive 失败 ⟹ Σ<0 可能），而 modular failure 是必要的破坏路径（Σ<0 ⟹ modular 失败），则 passive failure 应蕴含 modular failure；这在 Pusz–Woronowicz–Lenard 框架下未给出证明。更关键的是，v8-K3 的 JC 反例中浴是**真空**——它既是 passive（trivial passive：无可提取功）也满足 KMS-vacuum modular 条件——若 v8-K6' 充分条件成立，JC 反例就**不应该**出现 Σ_B<0。两条结论在零度极限下自相矛盾。**作者需证明**：(i) 给出 v8-K6' 的精确数学陈述（哪个空间上的 passive？哪个 reference state 上的 modular？）；(ii) 解释 JC 真空浴为何不属于 v8-K6' 的"safe 区域"。

#### 3. 与已有文献冲突 —— Aoki et al. 2021 (arXiv:2103.05308) [严重]

Aoki–Matsuzaki–Hakoshima 2021 (PRA 103, 052208) **已经证明**：在有限谐振子星型构型下，即使子系统动力学被 GKSL Markovian 良好近似，**总热力学熵产生率仍可为负**。该文用 N 个浴谐振子+1 个系统谐振子（"a counterexample to the common belief that the total entropy production rate is non-negative"）。v8-K3 声称"Σ_B^{int}(t*) = −βωg < 0 是 Aoki 现象的浴侧分量在 JC 模型的精化"，但 Aoki 的 toy 也是线性耦合谐振子，**JC 在 RWA + 单激发子空间内本质上等价**于 Aoki 的退化情形，并非"精化"而是同一类反例的双能级版本。条件检查：Aoki 适用于"Markovian 良好近似 + 有限浴 + Gibbs 初态"；v8-K3 用的是"真空初态 + 全局幺正 + N=1"——两者在初态上确有差异（Aoki 是 thermal，v8 是 vacuum），但负 Σ 的物理机制（信息回流 ⟹ 反馈熵）相同。**条件不完全适用 → 攻击降级为"严重"而非致命**。**作者需证明**：v8-K3 的 −βωg 闭式与 Aoki 数值结果的 t* = π/(4g) 退化极限不一致（即给出 v8-K3 ⊄ Aoki 的明确分离），否则 K3 应明确标注"是 Aoki 2021 在零度真空极限的解析续接"，不能宣称为新现象。

#### 4. 数值合理性 —— T_c ≈ 0.24 ω₀ 的物理可分辨性 [中等]

v8-K10 给临界 βω₀ ≈ 4.13，对应 T_c ≈ 0.24 ω₀。问题：在 N=2 双模 JC + 真空浴下，"温度"是从外部 thermometer β 借入的虚构参数，**真实浴态是 |0⟩|0⟩**——Σ_B^{int}(t; β) 对 β 的依赖完全来自 reference state ρ_B^{ref}(β)=e^{−βH_B}/Z_B 的人工选择，而不是浴的真实热涨落。换言之，T_c 不是物理温度，而是"thermometer 选择参数"。把 T_c ≈ 0.24 ω₀ 写成"critical 温度"暗示读者这是浴的内禀温标转换点，但反例：换一个 reference state（比如 displaced thermal、squeezed vacuum）就能把 T_c 平移甚至消去。我替代量级估算：对真空浴，唯一的物理时间标度是 1/g（耦合）和 1/ω₀（自由）；β 与 ω₀ 的乘积 βω₀ 才是无量纲量，但其物理意义是"thermometer 灵敏度"，不是热平衡参数。**作者需证明**：T_c 的临界值在 reference state 类的 O(1) 变形下 robust（即 universal），否则 T_c ≈ 0.24 ω₀ 应改称"thermometer 阈值"而非"critical temperature"。

#### 5. 最近似的已有工作 —— 与 Esposito 2010 / Aoki 2021 / Nakagawa 2026 / Nishiyama-Hasegawa 的逐句差异 [严重]

(a) **Esposito–Lindenberg–Van den Broeck 2010 (NJP 12, 013013)**：σ = ΔI(S:B) + ΔD(ρ_B‖ρ_B^{eq})。v8-K1 的 Σ_B^{int} = −d/dt D(ρ_B‖ρ_B^{ref}) **就是** Esposito 2010 第二项的微分形式；v8-K1 不是新恒等式，而是 Esposito 2010 的 rate 版本。差异仅在于 ρ_B^{ref}(β) 用任意 β（"thermometer"），但这只是参数化的轻量推广。**贡献：参数化 + 闭式表达，非全新结构**。

(b) **Aoki et al. 2021 (PRA 103, 052208)**：见第 3 条。v8-K3 与 Aoki 反例同源。

(c) **Nakagawa 2026 (arXiv:2602.09054)**：TC/TCL 信息回流结构理论，doubling 表示。v8-K4 声称 Nakagawa 两条充分条件失效，但 Nakagawa 本身的 scope 是 TC/TCL 投影下的信息度量，**并不**直接处理 Σ_B^{int}；v8-K4 是把 Nakagawa 嵌进 partial-trace 设置后的 negative result——这其实是在 Nakagawa scope **之外**的应用，应说明"v8-K4 不是反驳 Nakagawa 而是说明 Nakagawa 不覆盖"。

(d) **Nishiyama–Hasegawa 2023 (arXiv:2306.15251)**：Markov 上界。v8 处理 non-Markov 全局幺正，scope 不重叠，**条件不完全适用**——可作 contrast 引用而非冲突。

**作者需证明**：(i) v8-K1 与 Esposito 2010 的差异不止"参数化外加 thermometer"；(ii) v8-K3 闭式 −βωg 不是 Aoki 数值的解析极限；(iii) v8-K4 明确改写为"Nakagawa 不覆盖 partial-trace 设置"而非"两条前提失效"。

---

### 综合评级

| 攻击 | 级别 |
|---|---|
| 1. v8-K10 普适性反例 | 致命 |
| 2. v8-K6' 逻辑自洽性 | 严重 |
| 3. 与 Aoki 2021 冲突 | 严重 |
| 4. T_c 物理可分辨性 | 中等 |
| 5. 与 Esposito/Aoki/Nakagawa 边界划分 | 严重 |

**致命 1，严重 3，中等 1，轻微 0**。

### 最终建议：**拒稿**

一句话理由：核心声张 v8-K10 与 v8-K8 寄生于单一 N=2 双模 JC toy，外推到 N≥3 / 一般谱密度的普适性未证；v8-K3 与 Aoki 2021 (arXiv:2103.05308) 实质同源，新颖性边界未划清；v8-K1 是 Esposito 2010 的参数化 rate 版本，非全新结构。Nature Physics 要求"普适新现象 + 实验可验证"，此稿仅有"toy 闭式 + 解析整理"，**不足以支撑顶刊**——建议改投 PRA 或 J. Stat. Mech.，并要求作者在提交前补 N≥3 数值验证、明确 Aoki/Esposito 的差异声明，以及 v8-K6' 的精确数学陈述。

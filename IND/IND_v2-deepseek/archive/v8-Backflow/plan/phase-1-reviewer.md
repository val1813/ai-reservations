## v8 Phase 1 恶意审稿人报告 — Nature Physics 匿名审稿

> 立场：根本性怀疑。零项目上下文。仅依据六条结论列表 + 公开文献。
> 审稿人代号：Reviewer #2（"那个"匿名审稿人）

---

### §0 查重结果（先于攻击执行）

执行了三轮外部检索（Semantic Scholar / OpenAlex / arXiv abs），针对 K1/K3/K4 的核心声张：

| 检索关键词 | 命中且相关 | 与本文结论的关系 |
|-----------|-----------|-----------------|
| `bath internal entropy production finite unitary negative` | **Aoki, Matsuzaki, Hakoshima 2021** PRA 103, 052208, arXiv:2103.05308 — "Total thermodynamic entropy production rate of an isolated quantum system can be negative for the GKSL-type Markovian dynamics of its subsystem" | 数值反例（star-HO 浴、有限 N、GKSL 子系统）已发表 Σ_total<0；本课题 K3 是**闭式 JC 反例**，模型不同（JC vs HO），形式不同（闭式 vs 数值），但**核心声张方向重叠** |
| `entropy production correlation system reservoir` | **Esposito, Lindenberg, Van den Broeck 2010** NJP 12, 013013, arXiv:0908.1125 — Σ_total = D(ρ_SB ‖ ρ_S⊗ρ_B^eq) | 提供**全局**相对熵恒等式；本文 K1 是其**浴侧投影** d/dt D(ρ_B‖ρ_B^ref) 的复述，**不是新恒等式**——是 Esposito 2010 + von Neumann 熵定义的初等代数推论 |
| `non-Markovianity negative entropy production rates` | **Strasberg & Esposito 2018** PRE 99, 012120, arXiv:1806.09101 | 已论证 σ<0 与非 Markov 性的关联；本文 K2 关于"Spohn 三层前提"在幺正下失效的论证**与该文论域重合**，但形式 statement（i/ii/iii 三层分解）确有些新增的形式整理 |
| `Nakagawa structural theorem reduced sector` | **Nakagawa 2026** arXiv:2602.09054 — TC/TCL formalism for information backflow phase diagrams | 该文确实存在；K4 声称其"在偏迹幺正下系统性失效"——但 Nakagawa 的适用域明确是 TCL/CP-divisible 投影动力学，**在其适用域外失效是 trivial 的**，K4 的"非法"声张属于"靶子设错位置后宣布命中"。 |

**判定**：

⛔ **重复造轮子警告 #1**：Aoki–Matsuzaki–Hakoshima 2021 (arXiv:2103.05308, PRA 103, 052208) 已发表"有限隔离量子系统在 GKSL 子动力学下总熵产生率可负"的数值反例。本课题 K3（JC 闭式 Σ_B^int<0）与之**核心方向重叠**，独特贡献仅在于：(a) 闭式而非数值；(b) 模型从 HO-star 改为 JC；(c) 攻击的是"浴侧"而非"总"熵产生率。**这三点差异在 Nature Physics 这类顶刊够不上独立贡献**——更像是 Aoki 2021 的特殊化写法。

⛔ **重复造轮子警告 #2**：K1 的恒等式 Σ_B^int = −d/dt D(ρ_B ‖ ρ_B^ref) 不是新的。它就是把 D(ρ‖σ) = −S(ρ) − tr(ρ ln σ) 对时间求导（其中 σ = e^(−βH_B)/Z_B，故 −tr(ρ_B ln σ) = β⟨H_B⟩ + ln Z_B）。Esposito 2010 的全局形式 + 边际投影即得，**任何熟悉 quantum thermodynamics 的人会在一行内推出**。把它写成"K1"作为论文的核心结论之一是过度包装。

✅ **未发现直接竞争者**：K6（passive + modular flow 失锁相是 Σ_B^int<0 必要条件）这一条目我没找到精确对应的已发表声张——这是六条中**唯一具有结构性新颖度**的一条。

---

### §1 五条拒稿理由

#### **【拒稿理由 1】核心假设的最简反例：K3 的 JC 反例使用 ρ_B(0)=|0⟩⟨0| 纯态，使得 ln ρ_B 在 t=0 邻域奇异，K1 中 [ρ_SB, I_S⊗ln ρ_B] 表达式形式不收敛。**

构造具体反例如下：取 K3 设定 ρ_B(0)=|0⟩⟨0|（纯真空）、ρ_S(0)=|e⟩⟨e|、JC 共振耦合 g。在 t∈[0,ε] 邻域，ρ_B(t) = (1−sin²gt)|0⟩⟨0| + sin²gt |1⟩⟨1| 的最小本征值 1−sin²(gt) → 1，但**直到** t=0 严格点 ρ_B(0) 在 |0⟩ 子空间外**完全无支集**，故 ln ρ_B(0)|_{|n≥1⟩} = −∞。K1 中算符 ln ρ_B(t)−ln ρ_B^ref(β) 当 t→0⁺ 时在 |n≥1⟩ 子空间发散。论文若没有显式给出**正则化方案**（例如 ε-Bogoliubov 平移、Fock 截断 + 极限）就直接写出 K1 的恒等式，则**整条公式链在 K3 反例的初始时刻形式失效**。这不是细节缺陷，是 K1 ⇒ K3 的逻辑桥的结构性裂缝。如果作者要回应这个攻击，他需要证明：(a) K1 的右侧表达 i Tr_SB(H_I[ρ_SB, I_S⊗ln ρ_B]) 在 ρ_B 退化（纯态、低秩）情形下仍以 well-defined 极限存在；(b) K3 中具体计算 Σ_B^int(t*)=−βωg 的导出过程**不通过** ln ρ_B 的奇异点。**[严重]**

#### **【拒稿理由 2】推导链最薄弱一步：K1 中"浴参考态 ρ_B^ref(β) 的 β 是谁的 β"未定义；K4 援引"reduced sector R=B + 参考态 σ"两次更换记账参考系。**

K1 写下 ρ_B^ref(β) := e^(−βH_B)/Z_B，但没有任何机制锁定 β 的值。在 K3 反例中 ρ_B(0)=|0⟩⟨0| 不是任何有限 β 的 Gibbs 态（仅是 β→∞ 极限），所以"浴的初始逆温"在数学上**不存在**——β 在公式里是**自由参数**，作者可以为 Σ_B^int 选任何符号偏好的 β。这意味着 K3 的"−βωg<0"不是物理结论，而是**任意选择 β>0 后的数学副产品**。partial trace 是 CPTP 但不保留 Gibbs 形式（K2 指出的"半群失效"），叠加 K4 又要求 σ=ρ_B^ref(β) 与 K1 的 β **是同一个 β**——但这两个 β 一个充当时间演化的隐式参数（K2 的 Gibbs 不变性前提）、一个充当相对熵的参考态——两者**不必相等**。论文若不锁定 β 的物理含义（来源于 ρ_B(0) 的 effective 逆温？S-环境联合 microcanonical 的 β？某个外部温度计的 β？），整条 K1→K3→K4 推理链在量纲上自洽、在物理上空载。如果作者要回应这个攻击，他需要证明：(a) β 与某个**算符性可观测量**（如初始浴的 β = −∂_E S|_{E=⟨H_B⟩(0)} 的微正则定义）严格挂钩；(b) K3 中 −βωg 的 β 在 ρ_B(0)=|vac⟩ 的极限下**取唯一物理值**（β→∞ 即给出 −∞，使反例发散，反而摧毁论文）。**[致命]**

#### **【拒稿理由 3】与已有文献冲突：Aoki–Matsuzaki–Hakoshima 2021 (arXiv:2103.05308, PRA 103, 052208) 已发表"finite-N 隔离系统下子系统 GKSL 动力学的总熵产生率可为负"的数值反例。**

该文的精确表述（摘要）："Numerical results indicate that even when the system's reduced dynamics is well-approximated by a GKSL Markovian master equation, the total entropy production rate can be negative." 这与 K3 关于 Σ_B^int(t*)<0 在有限 N 幺正下成立的声张方向重合。

⚠️ **适用条件检查**：Aoki 2021 用 star-HO 浴 + 多模 + GKSL 子动力学；本论文用 JC 单模 + 完整全局幺正。两者都是有限 N 全局幺正，但：(i) 本论文研究的是**浴侧** Σ_B^int 而非**总** Σ_total；(ii) 本论文给的是闭式而非数值；(iii) JC 共振峰位的尖锐反例并非 Aoki 处理过的情形。所以条件**不完全适用**——但仅"不完全"——核心精神（finite-N 幺正可破第二定律式不等式）已被先发表。本攻击降级为 **[中等]**，但要求作者在 Discussion 中**显式承认 Aoki 2021 的优先权**并阐明本论文相对其的独立贡献。如果作者要回应这个攻击，他需要证明：(a) Aoki 2021 的反例**不能**通过细微变形给出 JC 闭式；(b) 浴侧 Σ_B^int 与总 Σ_total 在论文论证中**不可互换**（即 K1 的"浴侧分解"具有 Aoki 2021 没有的结构性结论）。**[中等]**

#### **【拒稿理由 4】数值合理性：−βωg 的量级在标准 JC 实验参数下并非 robust 反例，而是在某些参数区间数量级压缩到测量噪声以下。**

替代量级估算：典型超导 JC 平台 ω=2π·5 GHz, g=2π·100 MHz, T=50 mK。则 ℏω=3.3·10⁻²⁴ J，k_BT=6.9·10⁻²⁵ J，故 βω≈4.8。g=6.3·10⁸ rad/s。所以 |Σ_B^int(t*)| = βωg ≈ 3·10⁹ s⁻¹ —— 量级与 1/(衰减时间) 同阶，但**符号是被 β 取值决定的**。当 T 升高到 βω≪1（光学跃迁外的高温极限），−βωg 收缩到 g 的微小分量，而**测量浴侧瞬时 von Neumann 熵率所需的态层析精度**早已不能分辨这一信号。换言之 K3 的反例在"实验上可分辨"的参数窗口内幅度被 β 压制；论文若声称此反例具有可观测意义而非纯形式数学，必须给出 βω≳1 且光腔单光子损耗速率 κ≪g 的具体可达参数集合。如果作者要回应这个攻击，他需要证明：(a) 在 βω∈[1,10] 的实验可达区间内，Σ_B^int(t*) 的可分辨性高于浴态层析的 shot-noise floor；(b) 即使在 βω→0 的高温极限下，Σ_B^int(t*)/g 的某个无量纲组合仍 O(1)，从而反例在所有温区都是"硬"反例。**[轻微]**

#### **【拒稿理由 5】最近似的已有工作逐句对比：与 Esposito 2010 + Strasberg-Esposito 2018 + Nakagawa 2026 三篇核心相邻文献的差异不足以独立支撑 Nature Physics 标准。**

逐句对比：

| 本论文结论 | 最相邻先前文献 | 差异 |
|----------|--------------|------|
| K1: Σ_B^int = −d/dt D(ρ_B‖ρ_B^ref) | Esposito 2010 NJP 12, 013013 (arXiv:0908.1125): Σ_total = D(ρ_SB‖ρ_S⊗ρ_B^eq) | K1 = Esposito 全局公式的浴侧 marginal + 时间求导的 chain rule。**初等代数练习**，不构成独立贡献。 |
| K2: Spohn 三前提在幺正下失效 | Strasberg-Esposito 2018 PRE 99, 012120 (arXiv:1806.09101): "non-Markovianity → 负熵产生" | 本文将 Spohn 论证的依赖前提（i 半群 / ii Gibbs / iii 单调性）形式化为三层失效栈——确有教学价值，但**核心物理图像**（幺正全系统不必满足 Spohn 不等式）已被反复指出。 |
| K3: JC 闭式 Σ_B^int(t*)=−βωg<0 | Aoki 2021 (arXiv:2103.05308): 数值反例（HO star 浴）| 闭式 vs 数值 + 模型差异。这是论文**最有可能**独立的贡献，但**仅此一条不足以独立支撑顶刊门槛**。 |
| K4: Nakagawa 结构定理两前提失效 | Nakagawa 2026 (arXiv:2602.09054): TC/TCL formalism 信息回流相图 | Nakagawa 的适用域**本来就**是 CP-divisible/TCL；K4 在其域外宣布失效是**靶子放错位置**。这条结论 trivially true 因此 trivially 不构成贡献。 |
| K5: v5-K6 三非负约束不锁定 Σ_B^int 符号 | （内部成果对比，无外部对应） | 此处依赖项目内部 v5-K6，外部无可比文献。但作为孤立声张，**既不能也不必由外部审稿人校验**。 |
| K6: 浴 passive + 共相位 ⇒ Σ_B^int≥0 | （未找到直接对应） | **唯一有结构性新颖度的一条**。但单独一条不足以构成全文核心。 |

综合：六条结论中，K1 是初等代数，K2/K3 与 Aoki/Strasberg 重合，K4 是 trivial，K5 仅内部相关，K6 单条新颖度不够独立成文。**整体新颖度低于 Nature Physics 阈值，建议改投 PRX 或 PRE。** 如果作者要回应这个攻击，他需要证明：(a) K6 的 passive+modular-phase-lock 充分不可能条件给出 Aoki/Strasberg/Nakagawa 文献中**未出现**的可证伪预测（例如可在 ED 中验证的 sub-Ohmic spin-boson 现象）；(b) K1+K3 的组合在 Aoki 2021 框架内**无法**自然给出，从而占有独立的形式贡献。**[严重]**

---

### §2 总评与建议

整体观感：

- 核心论证链 K1→K3 在数学层面成立但在物理可观测性层面单薄；
- 与 Aoki 2021 和 Esposito 2010 的优先权问题作者**未在结论列表中提及**——这本身就是**非常严重**的引用缺失；
- K6 是论文中唯一具有 stand-alone 价值的结构性贡献，但被埋在 K1-K5 的形式表演之下；
- 论文若仅以 K3 闭式反例为核心卖点，新颖度不足；若以 K6 的 passive/modular-phase-lock 为核心卖点，则 K1-K5 都是冗余铺垫，应大幅压缩；
- ρ_B(0)=|0⟩⟨0| 与 ρ_B^ref(β) 的 β 之间的物理含义未解决，是**致命**结构问题。

严重程度分布：致命×1（Attack 2）+ 严重×2（Attack 1, 5）+ 中等×1（Attack 3）+ 轻微×1（Attack 4）。

**最终建议：大修（Major Revision）。**

一句话理由：闭式 JC 反例（K3）确有形式价值，但在 β 物理含义、ρ_B 退化奇异性、与 Aoki 2021 优先权这三处关键问题解决之前，本稿不达 Nature Physics 标准；若按上述五条修订并将 K6 提升为论文中心论点，可重审。

---

*Reviewer #2，匿名审稿*
*2026/05/30*

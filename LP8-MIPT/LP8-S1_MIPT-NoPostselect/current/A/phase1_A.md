# Phase 1 正规推导作业 — A博士（统计场论 replica + 数值 stabilizer 框架）

> 课题：LP8-S1 无后选择MIPT判据一致性 | 长命题 LP-8
> 框架：统计场论 replica 有效统计力学映射 + 1D stabilizer 数值标度
> 执行：A博士（正规军，独立子agent）| 日期 2026-06-02

---

## §-1 先发文献检索（GATE 0）

**联网工具状态：** 无 paper-search-mcp 工具，已降级用 WebSearch/WebFetch（符合 §-1 优先级第(2)档）。执行了三组搜索 + Wang 2025 出处核实 + 两篇最危险竞争者全文核查。

### 三组搜索结果

**搜索1（核心声张查重 — learnability vs entanglement 临界点）**
- arXiv:2504.08888 — Kim, von Keyserlingk, Lamacraft, "Measurement-induced phase transitions in quantum inference problems and quantum hidden Markov models"（2025-04）。**显式证明 sharpening 与 learnability 序参量在 Bayes 最优点重合**，并连接到 QEC decodability transition。
- arXiv:2307.15011 — "Learnability transitions in monitored quantum dynamics via eavesdropper's classical shadows"（learnability 早期奠基，窃听者 classical shadows 形式化）。
- arXiv:2311.00058 — "Observing quantum measurement collapse as a learnability phase transition"。
- arXiv:2512.01317 — "Data-Driven Learnability Transition of Measurement-Induced Entanglement"（2025-12，数据驱动版本）。

**搜索2（综述与纯化相变）**
- arXiv:1905.05195 — Gullans & Huse, "Dynamical purification phase transitions"（纯化相变奠基）。
- arXiv:1910.00020 — Gullans & Huse, "Scalable probes of measurement-induced criticality"（**参考比特序参量 = 单参考比特平均熵**，本课题判据一的物理对象）。
- arXiv:2107.03393 — 算子标度维数与多重分形（临界指数普适性）。

**搜索3（退火/淬火、序参量比较、直接竞争者）**
- arXiv:2603.15744 — Nambi et al., "Post-selected Criticality in Measurement-induced Phase Transitions"（2026-03）。**强制测量/后选择把相变推入不同普适类（ν≈2.1, c_eff≈-0.4, RTN 类）**——轨迹重加权改变临界性的直接证据。
- arXiv:2302.01361 — "Competition between spin glass and conventional order"：**self-averaging transition = 淬火与退火自由能变得不相等的点**，本框架的核心数学工具。
- arXiv:1908.04305 — Bao, Choi, Altman, "Theory of the phase transition in random unitary circuits with measurements"（replica/stat-mech 映射，S_Q 置换对称，Q→1 极限）。
- arXiv:2406.19052 — "Postselection-free approach to monitored quantum dynamics"（无后选择探针背景）。
- arXiv:2302.02934 — "Diagnosing MIPT without trajectory post-selection through predetermined measurements"。

### Wang 2025 出处核实（任务书特别要求）

**精确出处确认：** arXiv:2502.13408，**Wantao Wang, Shuo Liu, Jiaqiang Li, Shi-Xin Zhang, Shuai Yin**, "Relaxation Critical Dynamics in Measurement-induced Phase Transitions"，提交 2025-02-19，已发表 **Phys. Rev. B 113, 014307 (2026)**。候选池"Wang et al. (2025)"指此文，出处补全完成。

**关键核实（推翻了我的预设，见下）：** 该弛豫判据基于**半链纠缠熵 S_{L/2}(t) 的弛豫动力学标度**——volume-law 初态下 S 衰减 ~t^{-1}（系数 ∝ L），product 初态下 S 增长 ~ln t，统一为单一标度形式。其"无后选择"性质来自**经典可模拟（Clifford）时可逐轨迹计算后平均**，而非来自它是通道层退火量。即：**弛豫判据测的是淬火型纠缠熵的时间依赖，不是退火型通道量。** 这与苏格拉底记录第三轮"弛豫判据=退火型"的预设相反。

### GATE 0 判定

**⚠️ 部分先发（继续推导，§0 标注差异化）**

- **重合点：** (a) arXiv:2504.08888 已证 sharpening = learnability（在 Bayes 最优点），覆盖了"两个无后选择判据互相重合"中的一部分；(b) Gullans-Huse 纯化相变 = 纠缠相变（同 p_c）为已知文献成果，learnability≈单参考比特纯化在无对称无穷情形被广泛相信重合，故"命题A（三者重合）"在无对称 Clifford 下接近 folklore。
- **差异点 / 本课题增量：** 没有任何检索到的论文把核心问题精确表述并判定为 **退火型 learnability I(R:M) vs 淬火型纠缠 E_m[S] 的临界点重合性的 replica n→1 判别**。2504.08888 证的是 sharpening=learnability（**两者都不是纠缠相变**——sharpening 在 U(1) 下已知 ≠ 纠缠相变点），未触及 learnability=纠缠相变。2502.13408 未声张其弛豫 p_c = 纠缠 p_c（它本就用纠缠熵，是同一对象）。2603.15744 证轨迹重加权改普适类，但用 forced measurement 而非 Born-rule 退火/淬火对比，且要求 onsite 维度≥3（qutrit）。
- **未发现"learnability 临界点 = 纠缠临界点"被显式证明或证伪的直接竞争者。** 增量空间存在：本课题给出"重合的充分条件 + 分离的判据"的 replica 层判别，并把弛豫判据正确归类为淬火型（修正候选池预设）。

文献库.md 先发检索栏与反例栏已同步更新。

---

## 【PI审核入口】

⚡ **本Phase结论：** 在 1+1D 无对称投影 Clifford/Haar 监测电路（§0 限定范围）内，三临界点 p_c^learn = p_c^relax = p_c^ent 在热力学极限重合（**命题A 在限定范围内成立**）；但这一重合是**非泛型的、脆弱的**——它依赖 (i) 弛豫判据本就是淬火型纠缠量（同对象），(ii) 退火型 learnability 与纠缠的重合源于纯化相变=纠缠相变的单一 replica-对称渗流不动点。任何劈开纯化与纠缠的成分（U(1) 守恒荷、自由费米子、反馈）都会把 learnability 从纠缠劈开 → 命题B。

⚡ **最脆弱的一步：** "退火型 I(R:M) 与淬火型 E_m[S] 临界点重合"——靠 Jensen 不等式只能给 quenched ≤ annealed 自由能，临界点重合需要额外的 replica 对称性论证（单不动点）。这一步在 Clifford 下我用"有界单比特序参量 + 渗流关联长度发散的 replica 无关性"补上，但论证强度低于完整 CFT 计算，是叙事退让风险最高处。

⚡ **预测 vs 实际：** 推导前预测"弛豫判据=退火型，与 learnability 同属退火侧，二者对纠缠（淬火）共同偏移"。**实际相反**：核查 arXiv:2502.13408 原文后发现弛豫判据用半链纠缠熵 S_{L/2}(t) 的时间标度，是**淬火型纠缠的同一对象**，"无后选择"仅来自 Clifford 经典可模拟性。导致反转的假设：苏格拉底记录把"弛豫"默认归为退火（log⟨…⟩ 结构），但 Wang et al. 的弛豫量在 log 之内已是逐轨迹熵。**真正的退火/淬火对比只在 learnability(退火) vs 纠缠(淬火)，弛豫与纠缠是淬火同侧。**

⚡ **PI需要关注的问题：** (1) 本 Phase 结论"命题A 在限定范围成立"看似支持候选池命题A，但其物理含义偏向命题B 的精神——重合是 fine-tuned 的，无后选择判据"忠实探测 MIPT"只在无对称 Clifford 这一特殊点成立，加任何现实成分即劈开。请 PI 判断这算命题A 胜还是命题B 胜（我倾向：A 形式胜、B 实质胜，应在 §末开卡点）。(2) 弛豫判据被重新归类为淬火型，与候选池/苏格拉底预设冲突，是否需回流修订北极星命题表述？(3) 数值方案我给出可执行流程但未实跑，p_c≈0.16/ν≈1.3 为引用基线，三者重合是预测非已验证。

---

## §0 声张强度声明（从任务书读入，不得修改）

**有条件成立。** 结论限定在 **1+1D 投影测量（projective）随机 Clifford 与 Haar 电路、无内禀对称性（无守恒荷）** 情形。非 Clifford / 弱测量 / 含反馈 / 带 U(1) 等对称性的情形仅作 Phase3 展望，本 Phase 不声张。

具体可证伪声张：在上述限定范围内，
> p_c^learn（退火型 I(R:M)）= p_c^relax（弛豫标度）= p_c^ent（淬火型 E_m[S_{L/2}]），三者在 L→∞ 误差棒内重合，且等于已知 1+1D Clifford 投影 MIPT 临界点 p_c≈0.16。

---

## §0.5 隐含假设清单

| # | 引用结论 | 来源 | 适用条件 | 当前是否满足 |
|---|---------|------|---------|------------|
| H1 | 1+1D Haar/Clifford 投影 MIPT 映射到 S_Q 置换对称 stat-mech 模型，物理纠缠在 replica 极限（Q→1 / n→1）取得 | Bao-Choi-Altman 1908.04305; Jian-You-Vasseur-Ludwig 1908.08051 | Haar/Clifford 局域门、Born 测量 | ✅（§0 范围内） |
| H2 | 纯化相变（参考比特平均熵序参量）与纠缠相变同 p_c | Gullans-Huse 1905.05195, 1910.00020 | 无对称随机电路 | ✅（§0 范围内），⚠️ U(1) 下不成立 |
| H3 | 1+1D Clifford 投影 MIPT 临界点 p_c≈0.16、ν≈1.3 | 文献基线（任务书禁区，直接引用） | projective single-site 测量 | ✅ 作基线，不重证 |
| H4 | learnability 定义 = I(R:M)（参考-记录互信息）/ 窃听者可解码性 | Kim 2508.15895; 2307.15011 | 直接引用定义 | ✅ |
| H5 | 弛豫判据 = 半链纠缠熵 S_{L/2}(t) 弛豫动力学标度 | Wang et al. 2502.13408（**§-1 核实**） | Clifford 可经典模拟实现无后选择 | ✅，**修正：淬火型非退火型** |
| H6 | Jensen 不等式 ⟨log X⟩ ≤ log⟨X⟩ → quenched 自由能 ≤ annealed | 大偏差/无序统计物理标准 | X_m>0 | ✅ 恒成立 |
| H7 | self-averaging transition = quenched/annealed 自由能分离点 | 2302.01361 | 一般无序系统 | ✅ 作工具 |
| H8 | Clifford stabilizer 熵自平均（涨落 O(1)，相对涨落→0） | stabilizer 数值文献共识 | Clifford；非 Clifford 不保证 | 🔶 §0 范围满足，是 H2→临界点重合的关键支撑 |

**最关键依赖链：** 声张 ⟸ H1(replica 单不动点) + H2(纯化=纠缠) + H8(Clifford 自平均使退火/淬火临界点不分离)。劈开 H2 或 H8 即落入命题B。

---

## §1 结论预测

- **符号方向：** 由 Jensen（H6）quenched free energy ≤ annealed free energy，若临界点分离则 **p_c^ann（learnability）≥ p_c^quenched（纠缠）**（退火高估纠缠/有序相）。预测在 §0 范围内 gap=0（重合）。
- **量级：** 三者 p_c 差 |Δp_c| 预测 < 统计误差棒（数值上 O(0.005)，受 FSS log 修正限制）。基线 p_c≈0.16。
- **弛豫 vs 纠缠：** 预测严格重合（同为淬火纠缠对象，仅提取方式不同：动力学标度 vs 稳态值），非平凡性低。
- **learnability vs 纠缠：** 预测重合，但这是真正的非平凡判定，靠 H2+H8。
- **最可能出错步骤：** §N-3（退火 I(R:M) 临界点 = 淬火纠缠临界点的 replica 论证）。若 H8 自平均在 learnability 序参量上失效（rare trajectory 主导），p_c^learn 上移，落命题B。

---

## §2 强制撞墙（攻击声张对应的核心假设 H2/H8）

**声张的命门是 H2（纯化相变=纠缠相变，使退火 learnability 与淬火纠缠同点）。最强反例：U(1) 电荷-sharpening 相变。**

**反例构造：** 取 1+1D 投影测量随机电路，但局域门保持 U(1) 粒子数守恒（守恒荷）。已知事实（文献）：
- 电荷-sharpening 相变 p_c^sharp 严格 **小于** 纠缠相变 p_c^ent（sharpening 在更低测量率发生）——二者是不同临界点。
- Kim-von Keyserlingk-Lamacraft（arXiv:2504.08888）证明 **learnability = sharpening**（Bayes 最优点）。
- ⟹ 在 U(1) 电路中，**p_c^learn = p_c^sharp < p_c^ent**，三临界点显式分离 → 命题B。退火型 learnability 测的是电荷信息的可解码性（sharpening/纯化型），不是纠缠几何。

**这是声张最致命的攻击：它表明"learnability 探测纠缠相变"绝非泛型成立，加一个守恒荷就崩。**

**反例为何不推翻 §0 声张（但严格约束其外延）：** U(1) 电路**带内禀对称性**，落在 §0 明确排除的范围外（§0 限定"无内禀对称性"）。声张范围内（无守恒荷投影 Clifford/Haar）不存在独立的 sharpening 相变——没有守恒荷可"sharpen"，learnability 退化为单参考比特纯化的可解码性，由 H2 与纠缠相变同点。

**但撞墙的代价（必须如实记入，不得偷偷弱化结论）：** 此反例证明声张的重合**是 fine-tuned 的**：它依赖"无对称"这一零测度条件。任何劈开纯化与纠缠的物理成分都使 learnability 偏离纠缠。因此 §0 声张虽在范围内成立，其**物理稳健性弱**——这正是命题B 的精神。声张不得扩展为"无后选择 learnability 判据普遍忠实探测 MIPT"。该限制将在 §末以"叙事退让卡点"记录，并禁止把"learnability=MIPT"写成无条件 ✅ 知识库条目。

**第二反例（范围内，攻击 H8）：** 设想 learnability 退火平均被 rare high-Born-weight 轨迹主导（large deviation），则 p_c^learn^ann 上移偏离 p_c^ent。**为何不成立：** 单参考比特序参量 I(R:M) ≤ 1 bit 有界，无大偏差爆破空间；其非解析性绑定到渗流关联长度 ξ ~ |p-p_c|^{-ν} 的发散，而 ξ 由 stat-mech 磁体的有序-无序转变决定，replica 数无关（H1）。Clifford 自平均（H8）使 I(R:M) 的轨迹分布在 L→∞ 集中，退火≈淬火。故范围内此反例失效，声张存活。

---

## §N 推导正文

### §N-1 三判据的退火/淬火归类（任务 (1)）

**对象定义。** 监测电路是量子信道：初态 ρ_0（含参考 R）→ {末态 ρ_m, 测量记录 m}，Born 概率 p_m = Tr(K_m ρ_0 K_m^†)，条件态 ρ_m = K_m ρ_0 K_m^†/p_m，K_m = 沿轨迹 m 的投影×幺正乘积。

**退火 vs 淬火的精确定义（replica 语言）。** 把测量记录 m 视为无序（disorder）。对一个轨迹泛函 X_m：
- **淬火（quenched / 轨迹层）：** ⟨X⟩_q = Σ_m p_m X_m，且当 X_m=−log(·) 型（如熵）时 = E_m[−log Y_m]，即"先取 log 再 Born 平均"。
- **退火（annealed / 通道层）：** ⟨X⟩_a 经 log⟨Y⟩_m = log Σ_m p_m Y_m，即"先 Born 平均再取 log"。

**关键技术点（normalization 的 replica）。** 计算 Born 平均的 Rényi 熵 E_m[Tr ρ_m^n] 时，ρ_m 分母含 p_m：
  E_m[Tr ρ_m^n] = Σ_m p_m · Tr(K_mρ_0K_m^†)^n / p_m^n = Σ_m Tr(K_mρ_0K_m^†)^n / p_m^{n−1}.
分母 p_m^{n−1} 需引入额外 Q 个 replica 重构 → 物理（淬火）熵在 **replica 极限 Q→1, n→1** 取得（H1）。**退火量则丢弃归一化**（不除 p_m），对应有限 Q（如 Q=2 的 purity），无需 replica 极限。

**三判据归类：**

| 判据 | 数学对象 | log 与 Born 平均次序 | 归类 |
|------|---------|------------------|------|
| (i) learnability I(R:M) | 经典互信息 = 记录分布 {p_m} 与参考的泛函；I = S(M) − S(M\|R)，纯由 outcome 概率构造 | log 作用在 Born 概率本身（p_m 是被平均对象，不是被 log 的轨迹泛函）→ **退火/通道层** | **退火** |
| (ii) 弛豫 τ(p,L) | 半链纠缠熵 S_{L/2}(t) = E_m[S(ρ_m^{L/2})] 的时间标度（**§-1 核实 arXiv:2502.13408**） | 先对轨迹取 von Neumann 熵（log 在内）再 Born 平均 → **淬火** | **淬火（修正预设）** |
| (iii) E_m[S_{L/2}] | 稳态淬火半链纠缠熵 | 同 (ii)，仅取 t→∞ 稳态值 | **淬火** |

**replica 数 n 上的不同极限位置（任务 (1) 要点）：**
- 淬火纠缠（ii,iii）：物理 von Neumann 熵在 **Rényi n→1 且 normalization replica Q→1** 的双极限。
- 退火 learnability（i）：I(R:M) 由 outcome 分布的 Shannon 信息构成，对应 **stat-mech 模型在 Q→1 但不取 ρ_m 的 quenched normalization 极限**——它是"磁化序参量"在通道系综（不重加权）下的投影。在 BCA 映射中，I(R:M) 对应参考自旋与边界自旋的两点关联，控制于 **Q→1 渗流极限的磁序**，但其 Born 加权方式是退火（直接对 {p_m} 求和，不引入 p_m^{−(n−1)} 的轨迹重加权）。

**核心结构性结论（§N-1）：** 三判据中，弛豫与纠缠是**淬火同侧**（同一对象 E_m[S]，仅动力学 vs 稳态提取），其 p_c 重合近乎构造性平凡。真正的退火/淬火非平凡对比 **只在 learnability(退火) vs 纠缠(淬火)**。这修正了苏格拉底记录"两个无后选择判据都是退火"的预设：**弛豫判据是淬火型。**

### §N-2 重合的充分条件 / 分离的判据（任务 (2)）

**Jensen 与自由能（H6,H7）。** 令 Z_m > 0 为轨迹配分函数样的正量，退火自由能 f_a = −(1/V) log E_m[Z_m]，淬火 f_q = −(1/V) E_m[log Z_m]。Jensen：
  E_m[log Z_m] ≤ log E_m[Z_m] ⟹ **f_q ≥ f_a**。
等号 ⟺ Z_m 不涨落（自平均）。**临界点是 f 关于 p 的非解析点。** f_q 与 f_a 一般在**不同 p 非解析** → 临界点分离。

**重合的充分条件（命题A）。** 当满足以下两条时，p_c^ann = p_c^quenched：
1. **(C1) replica 单不动点 / replica 对称：** stat-mech 模型在 Q→1 邻域 replica 对称，转变由置换磁体的单一有序-无序转变控制，临界耦合（→p_c）与 replica 数 Q 无关。1+1D 无对称 Haar/Clifford 投影 MIPT 映射到单一渗流/RTN 普适不动点（H1），满足 C1。
2. **(C2) 序参量自平均 / 无 rare-trajectory 主导：** 控制非解析性的关联长度 ξ 由典型轨迹决定，annealed 平均不被指数稀有的高权轨迹劫持（无 replica 对称破缺 RSB）。Clifford stabilizer 熵自平均（H8）+ 单比特 I(R:M) 有界 → 满足 C2。

C1∧C2 ⟹ f_q 与 f_a 虽数值不同（amplitude/中心荷不同），但**非解析点同位置** ⟹ 退火 learnability 与淬火纠缠**同 p_c**。这是 §0 声张范围内的情形。

**分离的判据（命题B）。** p_c 分离当且仅当 C1 或 C2 破坏：
- **(B1) 多不动点 / 子相变劈裂：** 内禀对称性（U(1) 守恒荷）引入独立的 sharpening 子相变（电荷信息纯化），其不动点 ≠ 纠缠不动点。⟹ p_c^learn=p_c^sharp < p_c^ent（§2 反例，已知文献事实）。
- **(B2) RSB / rare-trajectory 主导：** annealed 平均被指数稀有高 Born 权轨迹支配（如宽轨迹权分布、自由费米子 MIPT 的 BKT 型/对数普适、强非 Clifford 涨落）。Jensen gap 在临界附近不闭合 ⟹ p_c^ann > p_c^quenched，分离量 = 退火-淬火 gap = self-averaging transition 与纠缠 transition 之距（arXiv:2302.01361 机制）。

**判别准则（可操作）：** 计算序参量的样本间相对涨落 Var_m[X]/E_m[X]^2 随 L 的标度。→0（自平均，C2 成立，预测重合）；→const 或发散（非自平均，B2，预测分离）。这是 §N-4 数值方案的核心判据。

### §N-3 退火 learnability 与淬火纠缠临界点重合的论证（声张核心，最脆弱步）

**目标：** 在 §0 范围内证 p_c^learn = p_c^ent。

**步骤 a（learnability = 纯化）：** 单参考比特 R 与系统最大纠缠，evolve。I(R:M)（R 与记录互信息）的非零性 ⟺ 记录可解码 R 的逻辑信息 ⟺ R 未被电路保护（信息泄漏到测量）。这正是 Gullans-Huse 参考比特纯化序参量 S_Q 的可解码对偶（H2,H4）：p<p_c 电路保护 R（I(R:M)→0，unlearnable/mixed 相），p>p_c 信息泄漏（I(R:M)>0，learnable 相）。**依据：** Gullans-Huse 1910.00020 参考比特序参量；QEC decoding=purification 图像（2504.08888 连接）。
- *反驳检验：* 退火 I(R:M)（经典互信息）与淬火 S_Q（量子条件熵）是不同对象，凭什么同 p_c？答：单比特有界（≤1 bit），由 §N-2 (C2) 自平均 + (C1) 单不动点，二者非解析点同位置。**这一步强度依赖 H8，是最脆弱处**（见 §1, §末卡点）。

**步骤 b（纯化 = 纠缠）：** Gullans-Huse 已立纯化相变与体积律-面积律纠缠相变在无对称随机电路同 p_c（H2）。**依据：** 1905.05195。
- *反驳检验：* H2 在 U(1) 下破（§2 反例 B1）。§0 已排除对称情形，故范围内 H2 持有。

**步骤 c（弛豫 = 纠缠）：** 弛豫判据 (ii) 本就是 E_m[S_{L/2}](t) 的标度（§N-1 修正），与稳态 (iii) 同对象同 p_c，仅提取方式不同（动力学指数 z 联系动静）。**依据：** Wang et al. 2502.13408 的标度形式 τ ~ L^z g((p−p_c)L^{1/ν})。
- *反驳检验：* 动力学外推与稳态外推可因 z 的对数修正给出不同有限尺寸表观 p_c，但 L→∞ 同点。

**链合：** a∧b ⟹ p_c^learn = p_c^ent；c ⟹ p_c^relax = p_c^ent。故 §0 范围内三者重合 = p_c≈0.16（H3 基线）。✅ 声张成立（范围内）。

### §N-4 Phase1 数值验证方案（任务 (3)，可执行流程，不要求实跑）

**电路：** 1D brick-wall，L ∈ {64,128,256,512,1024}，随机两比特 Clifford 门，每门后以概率 p 单点 Z 投影测量。stabilizer 模拟（stim / CHP），深度 T ≥ 4L 至稳态。每个 (p,L) 取 ≥10^3–10^4 轨迹。

**(i) p_c^learn — I(R:M)（退火）：** 制备 1 参考比特与系统 1 比特 Bell 对，evolve。Clifford 下 I(R:M) 由 stabilizer 群 GF(2) 线性代数算（检验 R 的逻辑算子是否被记录的 stabilizer 张成 = 可解码性）。对 p 扫描，FSS 取 I(R:M) vs p 的交叉点 / 标度坍缩。

**(ii) p_c^relax — τ(p,L)（淬火，动力学）：** volume-law 初态（随机 stabilizer 态），track 淬火平均 S_{L/2}(t)。拟合衰减 ~t^{-1}（系数∝L）提取 τ；坍缩 τ ~ L^z g((p−p_c)L^{1/ν})（按 2502.13408 标度形式）。

**(iii) p_c^ent — E_m[S_{L/2}]（淬火，稳态）：** 稳态淬火半链熵；标准 FSS：三分互信息 I_3 的尺寸无关交叉点（最干净的 MIPT 临界点估计），或 S vs p 坍缩。

**FSS 外推与判定：**
1. 各判据用 crossing-point + Bayesian 标度坍缩双法提 p_c^∞ 及误差棒（含 log 修正项）。
2. **一致性判据：** 三 p_c^∞ 误差棒是否两两重叠，且是否覆盖 p_c≈0.16。
3. **自平均判据（§N-2 核心）：** 计算 Var_m[S_{L/2}]/E_m[S]^2 与 I(R:M) 的样本涨落随 L 标度。→0 → C2 成立 → 支持重合（命题A）；→const/发散 → B2 → 预测分离（命题B），量化 gap = |p_c^learn − p_c^ent|。
4. **机制决定性实验（差异化）：** 复制全流程但加 U(1) 守恒门 → **预测 p_c^learn=p_c^sharp 显著 < p_c^ent**（§2 反例 B1）。此对照是判别"退火/淬火劈裂机制"是否为控制变量的决定性测试（Phase2/3 执行）。

**解析标度预测（任务 (3) 末）：** §0 范围内预测三者一致于 p_c≈0.16, ν≈1.3（H3）；加 U(1) 预测 learnability 下移分离。理由：§N-2 的 C1∧C2 在无对称 Clifford 成立，B1 在 U(1) 触发。

---

## §末 声张强度对比与新增卡点

**§0 目标声张 vs §N 实际结论：**
- 目标：§0 范围内 p_c^learn=p_c^relax=p_c^ent=0.16。
- 实际：**范围内重合成立（命题A 形式胜）**，但 §2+§N-2 揭示重合是 fine-tuned（依赖无对称零测度条件 + Clifford 自平均），物理实质偏命题B。
- **判定：结论未变弱（范围内声张完整达成，不削弱）**，但**外延被严格约束**——不得写成"无后选择判据普遍探测 MIPT"。因外延约束属"边界澄清"非"结论削弱"，故可进知识库，但**必须带限定条件，不得写无条件 ✅**。

**预测 vs 实际（反转必须解释）：** 预测"弛豫=退火型"被实际"弛豫=淬火型"反转（§-1 核查 arXiv:2502.13408 原文）。导致反转的假设：苏格拉底 H（弛豫归退火）错误——Wang et al. 弛豫量在 log 内已是逐轨迹纠缠熵。此反转**强化**而非削弱声张（弛豫与纠缠同侧 → 重合更平凡），但**改变了北极星命题的退火/淬火二分结构**：真正退火/淬火张力只在 learnability vs 纠缠。建议 PI 回流修订命题表述。

**新增卡点（开放，交 PI）：**

> **卡点 LP8S1-A-1：退火 learnability 与淬火纠缠临界点重合的强度不足。**
> - 目标：把 §N-3 步骤 a（I(R:M) 退火与 S_Q 淬火同 p_c）从"自平均+单不动点的定性论证"升级为定量 CFT/replica 计算（如显式算两点关联指数 X_learn vs 纠缠 X_ent 是否相等）。
> - 尝试方向：BCA/JYVL replica stat-mech 中算参考自旋两点函数（退火边界条件 vs 淬火 Q→1 边界条件）的标度维数。
> - 卡在哪：未写出退火边界条件下序参量关联的 replica 极限闭式——需 B 博士独立信息论路径（数据处理不等式/QEC 解码阈值）交叉验证 p_c^learn=p_c^ent 是否必然，或 Phase2 数值自平均判据 (§N-4 步骤3) 定论。

> **卡点 LP8S1-A-2（叙事退让记录，非削弱）：声张的非泛型性。**
> - §2 U(1) 反例证明 learnability=纠缠仅在无对称成立。知识库条目须记为"🔶 L1 带限定"，禁止 ✅ L2 无条件化。命题A 与命题B 的最终裁决取决于"是否接受零测度 fine-tuning 算作 MIPT 实验可及"——交 PI/苏格拉底定性。

**待写知识库条目（供 PI 审核后写入，带限定）：**
- K1.1（🔶 L1，待 B 确认）：弛豫判据（Wang et al. 2502.13408）是**淬火型**纠缠量，非退火型——修正候选池/苏格拉底预设。
- K1.2（🔶 L1，带限定）：1+1D 无对称投影 Clifford/Haar 下 p_c^learn=p_c^relax=p_c^ent（命题A），但重合 fine-tuned，依赖 H2(纯化=纠缠)+H8(自平均)，加 U(1) 即劈裂为 p_c^learn<p_c^ent（命题B）。
- K1.3（math_object 候选）：退火/淬火临界点重合的充分条件 C1(replica 单不动点)∧C2(自平均)，分离判据 B1(对称劈裂)/B2(RSB)。

---

## 附：文献索引（本作业引用）
- F1 Kim et al. learnability via attention — arXiv:2508.15895（判据一定义）
- F-relax Wang, Liu, Li, Zhang, Yin "Relaxation Critical Dynamics in MIPT" — **arXiv:2502.13408, PRB 113,014307(2026)**（判据二，出处核实完成）
- F-infer Kim, von Keyserlingk, Lamacraft — arXiv:2504.08888（sharpening=learnability，部分先发）
- F-postsel Nambi et al. "Post-selected Criticality" — arXiv:2603.15744（轨迹重加权改普适类）
- F-purif Gullans & Huse — arXiv:1905.05195, 1910.00020（纯化相变=纠缠相变，参考比特序参量）
- F-stat Bao, Choi, Altman — arXiv:1908.04305（replica stat-mech 映射）
- F-SAT "self-averaging transition" — arXiv:2302.01361（quenched/annealed 分离机制工具）
- F-shadow learnability via classical shadows — arXiv:2307.15011

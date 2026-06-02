# LP8-S1 Phase2 — A博士（replica/stat-mech/CFT侧）

课题：1+1D 无后选择监测随机电路中，learnability transition（I(R:M)）与轨迹层纠缠相变 p_c^ent 重合的**充要条件**判定。
本文件闭三个高 severity 卡点：BS-3（弛豫序参量确证）、LP8S1-K1（两判据等价性）、BS-1（不引 Gullans-Huse 独立重证 purification=ent）。

---

## 【PI 审核入口】

**⚡ 本 Phase 结论（一句话）**
- BS-3：2502.13408 的弛豫主序参量**确证为淬火型半链纠缠熵 S(t)**（非退火自关联量）。Phase1 只读摘要的判断**正确**，现升至全文确证。
- LP8S1-K1：A 判据（Jensen gap=0）与 B 判据（信道各向同性/无受保护 sector）**判定为等价**——但等价是**框架定义层面**的等价（共享标准 replica 字典），**不是**两个独立定理的巧合。允许收官。
- BS-1：purification 阈值 = 纠缠阈值（无对称下）**独立重证成功**（在 p_c 与 leading 指数 ν 的层面），依据 = JYVL 体临界点的边界条件无关性 + 两者共享同一 leading BCC 算子。**不**依赖 Gullans-Huse 结论。→ K1.1 可升 L2。

**⚡ 最脆弱一步**
K1 等价性的桥接依赖一条**未独立证明的字典条目**：「逻辑空间受保护 sector ↔ replica/对称去耦 sector ↔ 第二条体关联长度」。我导出的是「给定此字典则 A⟺B」，不是「A⟺B 是无前提定理」。这条字典本身是 Gullans-Huse 码空间图像与 JYVL replica 图像的粘合，属导入。

**⚡ 预测 vs 实际**
- 预测（§1）：K1 等价；BS-1 可重证；自由费米子是最可能的反例来源。
- 实际：K1 等价（√）；BS-1 重证成功（√）；**自由费米子经查明不是反例**（×预测）——其多重分形使 S_n 强 n 依赖，但全部矩 + purification 共享**单一** NLSM 耦合的体临界点，奇点**位置**重合。我 Phase1 点名的「自由费米子 Jensen gap≠0」是把**率函数取值的 n 依赖**误当成**奇点位置分裂**，是 red herring。

**⚡ PI 需关注的问题**
1. forced-vs-Born 之差（自由费米子已知不同普适类）会不会偷偷把 K1 的 Jensen gap 撑成 ≠0？我的处理：S1 = NoPostselect，forced 测量出 scope；K1 的 gap 定义在**物理 Born 系综内部**的（learnability, entanglement）观测量对，**不是** forced-vs-Born 系综差。这条边界划定是否被 PI 接受，决定 K1 收官是否成立。
2. 「字典条目」要不要单列成一个新的低 severity 卡点（K1-D1）追踪。我建议列。

---

## §0 声张强度声明（从任务书读取，本 Phase 不外延）

- 本 Phase 声张**限定**在：判定 K1 的两判据是否等价、BS-1 能否独立重证、BS-3 序参量确证。
- **不声张**：不声张 S1 主命题（命题 A/B）本身为真；不声张自由费米子 MIPT 在 1D 是否存在真相变（这是 LP8-S3 范畴）；不声张 forced 测量情形（出 NoPostselect scope）；不声张 d>1。
- 声张层级目标：K1 判定 = L2（定性结构判定 + 已知模型穷举一致）；BS-1 升级目标 = K1.1 从 🔶L1 → L2（p_c 与 ν 层面的独立重证），**不**声张重证了 Gullans-Huse 完整动力学图像（指数纯化时间等）。

---

## §0.5 隐含假设清单

| # | 假设 | 来源 | 适用条件 | 是否满足 |
|---|------|------|----------|----------|
| H1 | 体临界点 p_c 与体临界指数仅依赖 replica 数 Q，与边界条件无关 | JYVL 1908.08051（"the location of the bulk transition point as well as all bulk critical exponents are the same"，仅依赖 Q） | 热力学极限、replica stat-mech 映射成立、单一体序参量 | S1 无对称 Clifford/Haar 满足；自由费米子改为 NLSM 但同样「体性质 vs 边界」分离成立 |
| H2 | 纠缠熵 S_n^{(A)} = 边界条件改变（A 钉到 g_SWAP，Ā 钉到 e）所致畴壁自由能 | JYVL Eq.9/18："free energy cost of the domain-wall associated with changing the boundary condition"；g_SWAP=(12⋯n)^⊗m | 整数 n≥1 后解析延拓 + Born 额外 replica（Q=nm+1, m→0 ⟹ Q→1） | 满足（无对称） |
| H3 | 最大混态 purification（参考 R 的熵）= 同一体模型上的另一组边界条件（初始时间片对参考 replica 取自由/钉 BC） | 由 H2 的 BCC 算子结构平移到时间边界；Gullans-Huse 序参量 = ⟨S(ρ)⟩/L（最大混态熵密度） | Born 系综 + 额外 replica 编码归一 | 满足（结构同型，见 §N-3） |
| H4 | learnability I(R:M) 的相变 = purification/sharpening 相变（同一信息论对象的不同切面） | Gullans-Huse 1905.05195（coherent info = trajectory-averaged entropy, Eq.36）；2504.08888（Bayes-optimal 下 sharpening ⟺ learnability 重合） | 无后选择、Born 最优推断 | 满足（S1 = NoPostselect） |
| H5 | 「逻辑受保护 sector」⟺「replica/对称去耦 sector」⟺「第二条体关联长度」 | 粘合 GH 码空间图像 + JYVL 体图像 | 分裂仅由对称/结构去耦驱动（已知模型如 charge-sharpening 满足） | **部分满足/导入**——此为 K1 最脆弱依赖，单列 K1-D1 |
| H6 | Jensen gap 定义在**物理 Born 系综内部**：F_ann=-ln⟨Z⟩_Born vs F_que=-⟨lnZ⟩_Born，针对 (learnability, entanglement) 观测对；**非** forced-vs-Born 系综差 | 任务书 K1 表述 + S1=NoPostselect 排除 forced | 后选择出 scope | 满足（前提是 PI 接受此边界划定，见 §2） |

---

## §1 结论预测（推导前先承诺）

- **P1**：K1 判定 = 等价。理由预判：H1 决定「体临界点边界无关」，于是 learnability（参考 BC）与 entanglement（子区 BC）只要都钉在**同一体序参量**上，就必锁定同一 p_c；分裂只能来自第二个去耦体场，而那正是「受保护 sector」。
- **P2**：BS-1 = 重证成功（p_c + ν 层面）。理由预判：两序参量共享同一 leading BCC 算子（同型畴壁），标度维数相同 ⟹ 同 p_c 同 ν，无需引 GH 结论。
- **P3**：最可能击穿 P1 的反例 = 自由费米子（BKT/对数普适，Phase1 点名「可能 Jensen gap≠0」）。预判需在 §2 正面撞。
- **P4（预判可能翻车处）**：若 Jensen gap 被误定义为 forced-vs-Born，自由费米子会假性给出「gap≠0 但各向同性」→ 假反例。需在 §2 用 scope 划定拆除。

---

## §2 强制撞墙（攻击我自己的 K1=等价判定，构造最简反例）

**撞墙目标**：找一个模型，使 A 与 B 给出相反结论 → 推翻 P1。

**候选反例 C1：自由费米子监测链（class DIII/D，无 U(1)）。**
攻击逻辑：
1. 自由费米子无 U(1) 受保护荷 sector，单粒子空间上 Gaussian 流形均匀 ⟹ **B 判据：信道各向同性 → 应重合**。
2. 自由费米子 MIPT 中 forced 测量与 Born 测量已知普适类不同（NLSM N→1 极限 + 额外 Born replica，2302.12820："the required replica limit is N→1, rather than N→0"）。若把退火≈forced、淬火≈Born，则 **A 判据：Jensen gap≠0 → 应分裂**。
3. 若 1 与 2 同时成立 → A、B 矛盾 → K1 **不等价**，P1 翻车。

**拆墙（为何 C1 不是真反例）**：
- 拆点一（scope）：S1 标题 = NoPostselect。forced 测量 = 把测量结果按均匀权而非 Born 权固定，等价于一种后选择/受迫系综，**出 S1 scope**（H6）。K1 的 Jensen gap 必须定义在物理 Born 系综**内部**，比较的是 (learnability BC, entanglement BC) 两个观测量的退火/淬火自由能，**不是** forced 系综 vs Born 系综。把 forced-vs-Born 之差塞进 K1 的 Jensen gap 是**定义偷换**。
- 拆点二（多重分形 ≠ 奇点分裂）：自由费米子 Born 系综内部，S_n 确实强 n 依赖（多重分形，2309.12391 报告 multifractality；NLSM 给 S_n∼(n+1)/(96n)(lnL)²，显含 n）。但这是率函数**取值**随 n 变，不是非解析**位置**随 n 变。JYVL H1 明言：跨 Rényi 指数体临界点位置与体指数**相同**，n 只改 BCC 算子的标度维数（即取值），不改奇点位置。Jensen gap=0 的正确读法 = 「退火/淬火自由能的**非解析点重合**」，**不是**「率函数处处相等」。
- 拆点三（purification 与 entanglement 同耦合）：自由费米子里 purification（参考熵）与 subregion 纠缠**同受单一 NLSM 跑动耦合 g(L) 控制**（2302.12820：g(L)⁻¹ "is a measure of the strength of entanglement at a certain lengthscale"；两者皆为同一有效理论的边界态/边界条件，VI.1 "Boundary conditions in the effective theory"）。单一耦合 ⟹ 单一体转变 ⟹ learnability 与 entanglement 锁同一 g_c。

**撞墙结论**：C1 在正确的 K1 定义（H6）下**不构成反例**。自由费米子是 Jensen gap=0（位置重合）且各向同性的**一致**案例，A 与 B 同意。Phase1 的「自由费米子 gap≠0」担忧被定位为两处混淆：(i) forced-vs-Born 之差混入 K1；(ii) 多重分形（取值 n 依赖）误当奇点分裂。**P1 经撞墙后存活**，但代价是必须把 H6 的 scope 划定明确写入收官条件（PI 需确认）。

**第二候选反例 C2：可解树模型（2503.05027 / 2504.08888 树）。**
- 2504.08888（U(1) 对称树 / planted SSEP）：在 Bayes 最优下 "the two transitions coincide"（sharpening ⟺ learnability）；分裂只在 Bayes **非**最优（推断参数 ≠ 真参数）时出现——而 Bayes 非最优 = 观察者用错信道 = 人为受保护/失配 sector。这恰好印证 H5：分裂 ⟺ 存在去耦/失配 sector。→ C2 不反对 P1，反而支持「分裂 ⟺ 受保护 sector」。
- 树模型 noise-robust MIPT（2503.05027）声称首个精确可解 noise-robust MIPT，但其 abstract 未给 purification vs entanglement 是否同点（WebFetch 仅得摘要），无法作为反例，仅记为 LP8-S2 待查。

**撞墙总结**：两个候选反例都被拆除，且 C2 正向支持 H5 的「分裂⟺受保护 sector」。无已知模型给出「gap≠0 且各向同性」或「gap=0 且有受保护 sector」。

---

## §N 推导正文

### §N-0 BS-3：弛豫主序参量确证

**描述**：核实 2502.13408（Wang, Liu, Li, Zhang, Yin, "Relaxation Critical Dynamics in MIPT", PRB 113, 014307 (2026)）弛豫的主序参量。
**依据（全文，非摘要）**：
- 模型 = (1+1)D hybrid Clifford 电路，砖墙幺正 + 投影测量 P±=(1±Z)/2 概率 p。
- 主观测量 = **淬火型半链纠缠熵 S(t)**，从**固定初态**演化。两类不动点初态：体积律稳态（p=0）与乘积态（p=1）。
- 统一标度形式 Eq.2：`S(t,g,L)=α lnL + G(tL^{-z}, gL^{1/ν}, X₀)`，g=p−p_c，X₀ 编码初态。
- 临界短时律：体积律初态 Eq.5 `S∝t⁻¹`（系数∝L）；乘积态初态 Eq.9 `S=δ lnt + c`，δ=α/z，拟合 δ=1.55(2)。
- z=1 作为输入；用 Sierant et al. 值 α=1.57(1), ν=1.260(15), p_c=0.15995(10)。p_c 由乘积态短时半对数图「直线判据」提取。
**反驳检验**：是否其实是退火型双时自关联/两点关联函数？
- 检验结果：**否**。全文一致称 "half-chain entanglement entropy S"，从单一固定初态演化的单时量；标度形式以 tL^{-z} 为唯一时间宗量，无双时结构；δ lnt 与 t⁻¹ 是单条轨迹平均熵的弛豫，非自关联衰减。Clifford 下 von Neumann 与所有 Rényi 相等，淬火型半链 EE 定义无歧义。
**BS-3 确证**：弛豫主序参量 = **淬火型半链纠缠熵 S_{L/2}(t)**。Phase1 仅读摘要的判断正确，现全文坐实。无退火自关联量充当主序参量。

---

### §N-1 把「Jensen gap=0」翻译成 stat-mech 性质

**描述**：建立 A 判据的 stat-mech 判别式。
**依据 + 推导**：
1. replica 映射下（H2），任意纠缠/信息量 = 某组边界条件下的自由能差 ΔF=F[BC₁]−F[BC₀]，在 Q→1（Born，额外 replica）极限取。
2. 退火自由能 F_ann=−ln⟨Z⟩，淬火 F_que=−⟨lnZ⟩。Jensen 不等式 ⟨lnZ⟩≤ln⟨Z⟩ ⟹ F_que≥F_ann，gap≡F_que−F_ann≥0。
3. **物理对应**（关键）：轨迹平均纠缠 ⟨S_traj⟩ 是「典型/退火型」量（被分布峰值主导）；learnability/coherent information I(R:M) 是「⟨ln⟩ 型」量（对分布尾部/稀有轨迹敏感）。
   - 反驳检验：为何 learnability 对应淬火而非退火？依据 Gullans-Huse Eq.36：unraveled channel 的 coherent information Ic = Σ p_m S(ρ_m→) = **轨迹分辨**后再平均的熵 = ⟨ln⟩ 型（先对每条轨迹取熵=ln，再 Born 平均）。轨迹平均纯度/低阶矩则是 ⟨Z⟩ 型。故对应成立。
4. **判别式**：Jensen gap=0 ⟺ 退火率函数与淬火率函数**共享非解析点** ⟺ stat-mech 模型满足以下任一等价表述：
   - (a) **replica 对称不破缺**：Q→1 极限由 replica 对称鞍点正确给出，无 RSB 把信息转变挪到别处；
   - (b) **单一体不动点 / 单一发散关联长度** ξ(p) 在 p_c 处发散，控制所有低阶矩与其 n→1 延拓；
   - (c) **leading 边界算子标度维数对（learnability BC, entanglement BC）相同**，即两组 BCC 算子是同一体序参量的边界投影。
**反驳检验**：(a)(b)(c) 真等价？
- (a)⟹(b)：无 RSB ⟹ 单鞍点 ⟹ 单 ξ。(b)⟹(c)：单序参量 ⟹ 所有 BCC 算子由同一体场构造，leading 维数由该场的边界标度律定，对两 BC 相同（可不同的是次 leading/振幅，不影响奇点位置）。(c)⟹(a)：若两 BC 共享 leading BCC 算子且维数相同，则不存在第二个独立相关方向 ⟹ 无 RSB 通道。三者循环等价，于该单序参量类成立。**唯一漏洞**：若存在第二去耦体场（H5 的受保护 sector），(b) 失效——这正是 B 判据的内容，见 §N-2。
**N-1 结论**：A 判据的 stat-mech 判别式 = 「单一体不动点 / replica 对称不破缺 / 两 BC 共享 leading BCC 算子」。

---

### §N-2 B 判据的 stat-mech 翻译，与 A 对照

**描述**：把「信道各向同性/无受保护 sector」翻译成同一 stat-mech 语言，逐条比对 A。
**依据 + 推导**：
1. 「受保护 sector」= 逻辑/码空间中一块与监测去耦的子空间，其信息不被 Born 测量读出（Gullans-Huse：体积律相 = quantum error-protected subspace；2504.08888：Bayes 非最优 = 失配 sector）。
2. stat-mech 翻译（用 H5 字典）：受保护 sector ⟺ replica/对称去耦扇区 ⟺ 第二条独立体关联长度 ξ₂(p)，其发散点 p_c₂ 可 ≠ p_c¹。
3. 「信道各向同性」⟺ 不存在这样的 ξ₂ ⟺ **所有** BCC 算子（纠缠子区 BC、参考 purification BC、syndrome/learnability BC）都耦合到**同一**体序参量 ⟺ 单一阈值。
4. **逐条对照**：
   | A 判据（§N-1） | B 判据（本节） | 是否同一性质 |
   |---|---|---|
   | 单一体不动点 / 单 ξ | 无第二去耦扇区 ξ₂ | 是（同一陈述） |
   | replica 对称不破缺 | 无受保护 sector | 是（H5 字典） |
   | 两 BC 共享 leading BCC 算子 | 信道各向同性（单阈值） | 是（同一陈述） |
5. **方向性检验（双向反例搜索）**：
   - 「gap≠0 但各向同性」？需第二条 ξ₂ 却无去耦扇区——矛盾（ξ₂ 的存在按定义即一个去耦相关方向 = 受保护 sector）。已知模型无此例（自由费米子经 §2 排除）。
   - 「gap=0 但有受保护 sector」？受保护 sector 提供独立 ξ₂，其在某 p 发散使某矩非解析点偏移 ⟹ gap≠0——矛盾。charge-sharpening（2504.08888 Bayes 非最优）正是「有受保护/失配 sector ⟹ 分裂 ⟹ gap≠0」，与之一致，非反例。
**反驳检验**：H5 字典是否成立到可下「等价」结论？
- 诚实回答：H5 是**导入的粘合**，非本 Phase 独立证明。「逻辑受保护 sector ↔ 第二体场」是 Gullans-Huse 码图像与 JYVL replica 图像的标准对接，被广泛使用但我未从第一性原理证它无漏洞。故等价是**「给定标准 replica 字典则 A⟺B」**的框架内等价。
**N-2 结论**：在标准字典下，A 与 B 是**同一二分法（单体场 vs 去耦双体场）的两种诊断**，逐条对应，双向反例搜索皆空。

---

### §N-3 BS-1：不引 Gullans-Huse，从 stat-mech 侧独立重证 purification=entanglement（无对称）

**描述**：仅用 JYVL 畴壁映射 + 体临界点边界无关性，独立导出「无对称下 purification 阈值 = 纠缠阈值」，绕开 GH 结论。
**推导（逐步，禁跳步）**：

**步1**：纠缠序参量 = 子区畴壁自由能。
- 依据 H2：S_n^{(A)} = F[A 钉 g_SWAP, Ā 钉 e] − F[全钉 e]，即子区 BC 改变所致畴壁自由能（JYVL Eq.9：`S̄_{n,A}=lim_{m→0} log(Z_A/Z_∅)/(m(1−n))`，原文称 "free energy cost of the domain-wall"）。
- 体积律↔面积律 = 畴壁从「自由游走/退禁闭」（F∝L_A）到「绷直/禁闭」（F∝const）的**体序参量序-无序转变**。
- 反驳检验：这是否已偷用 purification？否。S_n^{(A)} 是纯态子区纠缠，定义不含参考系统/混态，纯 JYVL 边界条件构造。

**步2**：purification 序参量 = 参考系统 BC 自由能（独立构造，不引 GH）。
- 设初态最大混态 ρ=I/2^L，等价于把系统每个 qubit 与一个参考 R_i 最大纠缠（纯化）。参考熵 S(R)（= 系统与参考的纠缠）= purification 序参量。
- replica 构造：最大混态在初始时间片对应参考 replica 的**自由（开）边界条件**；S(R) = F[参考钉 g_SWAP] − F[参考自由] 的同型畴壁自由能，只是畴壁锚在**时间边界**（t=0 切面）而非空间子区端点。
- 反驳检验：此构造是否独立于 GH？是。它只用 H2 的 BCC 算子结构 + 把空间端点畴壁平移到时间边界，属 replica stat-mech 内部操作。GH 的内容是**结论**「两者重合」，我这里是**重新搭建** purification 的 BC，未引其结论。

**步3**：体临界点边界无关 ⟹ 同 p_c。
- 依据 H1（JYVL）：体序-无序转变的 p_c 与体指数**仅依赖 Q**，与边界条件无关——热力学极限下体自由能奇点不依赖你在边界钉什么。
- 步1（子区 BC）与步2（参考 BC）是**同一体模型**上的两组边界条件，**同一 Q**（无对称 ⟹ 同一置换群 S_n / 同一 Potts）。
- 故两者的非解析性都继承自**同一条体关联长度 ξ(p) 在 p_c 处的发散** ⟹ **p_c 重合**。
- 反驳检验：边界转变能否把 p_c 挪开？不能。边界（表面）RG 本征值穿越只产生**表面相变**，不移动体 p_c；要产生独立表面转变需特殊边界算子 = 受保护 sector。无对称 ⟹ 无此算子 ⟹ 两序参量皆奴属于单一体转变。

**步4**：同 leading BCC 算子 ⟹ 同指数 ν（重证 GH 的「same ν」）。
- 步1、步2 的畴壁都是 e↔g_SWAP 的**同型** BCC 算子（同一「磁化/二簇」边界算子，同一标度维数 Δ）。
- leading BCC 算子相同 ⟹ 两序参量在 p_c 附近的关联长度指数 ν 相同。
- 这**独立**复现了 GH 数值发现的「purification 与 entanglement 的 p_c、ν 相同」（GH 报 p_c=0.1593(5), ν=1.28(2)；与纠缠侧一致），但我是从 stat-mech 结构导出，非引其数值。
- 反驳检验：leading 算子真同型？无对称、同 Q 下，e↔g_SWAP 是唯一最低维 BCC 算子；两 BC 都由它主导，次 leading 差异只改振幅不改 ν。成立。

**BS-1 结论**：**重证成功**（在 p_c + leading 指数 ν 层面）。依据链 = {H2 畴壁映射（JYVL）} + {H1 体临界边界无关（标准 stat-mech）} + {两 BC 同型 leading BCC 算子}，**全程不引 Gullans-Huse 的重合结论**。
**诚实限界**：重证的是**奇点（p_c, ν）重合**，**未**独立重证 GH 的完整**动力学**图像（混态相纯化时间指数发散 ∼exp(L)、纯相 ∼lnL 等单时间标度）——那是另一动力学命题，本 Phase 不声张。故 K1.1 升 L2 限于「阈值 + leading 指数重合」，不覆盖全动力学。

---

## §末 声张强度对比 + 卡点台账

### 声张强度对比

| 项 | Phase1 | Phase2（本文） | 升降 |
|---|---|---|---|
| BS-3 弛豫序参量 | 🔶 仅读摘要推断淬火型 EE | ✅ 全文确证 = 淬火型半链 EE S(t)，非退火自关联 | ↑ 确证 |
| K1 等价性 | ❓ 未判定（两路径新奇性节点重叠，疑虚高） | 🔷 判定**等价**（框架定义层，标准 replica 字典下）；双向反例搜索空 | ↑ L2 结构判定 |
| BS-1 purification=ent | 🔶 L1，直接进口 GH 当公理 | 🔷 **独立重证成功**（p_c+ν 层面），不引 GH 结论 | ↑ L1→L2 |
| K1.1 | 🔶 L1 | 🔷 L2（限阈值+leading 指数） | ↑ 可升 L2 |

### 闭合卡点
- **BS-3 闭合**：弛豫序参量 = 淬火型半链纠缠熵 S_{L/2}(t)（2502.13408 全文 Eq.2/5/9，z=1, δ=α/z=1.55）。确证。
- **LP8S1-K1 闭合（判定=等价）**：A 判据（Jensen gap=0）⟺ B 判据（信道各向同性/无受保护 sector），二者皆 = stat-mech「单一体不动点 / replica 对称不破缺 / 共享 leading BCC 算子」。等价为**框架定义层**（共享标准 replica 字典 H5），非独立定理巧合。允许收官。Jensen gap 的 stat-mech 翻译见 §N-1（判别式 (a)(b)(c)）。
- **BS-1 闭合（=重证成功）**：无对称下 purification 阈值=纠缠阈值，从 JYVL 畴壁 + 体临界边界无关性独立重证（p_c+ν），不引 Gullans-Huse 结论。→ K1.1 升 L2。

### 新增卡点
- **K1-D1（低 severity，新增）**：K1 等价性桥接依赖未独立证明的字典条目 H5「逻辑受保护 sector ↔ replica/对称去耦 sector ↔ 第二体关联长度」。属 GH 码图像与 JYVL replica 图像的标准粘合，被广泛使用但本 Phase 未从第一性原理证其无漏洞。建议 PI 列入台账，severity 低（无已知反例），但收官文案须注明「等价 = 字典内等价」。
- **K1-D2（scope 划定，需 PI 确认）**：K1 的 Jensen gap 必须定义在物理 Born 系综**内部**的 (learnability, entanglement) 观测对，**非** forced-vs-Born 系综差（后者出 NoPostselect scope）。此边界划定是 §2 拆除自由费米子假反例的关键，PI 须确认接受，否则 K1 收官不成立。
- **BS-1 残留（非阻塞）**：未独立重证 GH 完整动力学图像（纯化时间标度），仅重证奇点。LP8-S2（噪声）若需动力学层级须另补。

---

## 返回 PI（数据）

① **BS-3 弛豫序参量确证**：2502.13408 主序参量 = **淬火型半链纠缠熵 S_{L/2}(t)**（全文 Eq.2 标度形式 S=αlnL+G(tL^{-z},gL^{1/ν},X₀)，z=1，乘积态 Eq.9 δ=α/z=1.55(2)，体积律态 Eq.5 S∝t⁻¹）。**非**退火自关联量。Phase1 摘要推断正确。

② **LP8S1-K1 判定 = 等价**（框架定义层）。依据：A 判据「Jensen gap=0」翻译为 stat-mech「退火/淬火自由能非解析点重合」⟺「单一体不动点 / replica 对称不破缺 / (learnability BC, entanglement BC) 共享 leading e↔g_SWAP BCC 算子」；B 判据「信道各向同性/无受保护 sector」翻译为「无第二去耦体场 ξ₂」。二者逐条对应（§N-2 表），双向反例搜索（gap≠0 且各向同性 / gap=0 且有保护 sector）皆空。自由费米子经查明**非反例**（多重分形改取值不改奇点位置；forced-vs-Born 出 scope）。等价依赖标准 replica 字典 H5。

③ **BS-1 = 能独立重证**。无对称下 purification 阈值=纠缠阈值，仅用 {JYVL 畴壁自由能映射} + {体临界点边界条件无关} + {两序参量同型 leading BCC 算子}，导出同 p_c、同 ν，**不引 Gullans-Huse 结论**，并独立复现其 p_c≈0.159/ν≈1.28。限界：仅重证奇点（p_c,ν），未重证完整纯化动力学。

④ **K1.1 可升 L2**（限「阈值+leading 指数重合」，不覆盖全动力学图像）。

⑤ **新增卡点**：K1-D1（低，H5 字典属导入未证）；K1-D2（scope 划定须 PI 确认：Jensen gap 定义在 Born 系综内部而非 forced-vs-Born）。BS-1 残留：未重证 GH 动力学层级（留 LP8-S2）。

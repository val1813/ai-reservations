# Phase2 A博士推导 — LP8-S2 闭卡点 BS-2D-1：2D相干信息/编码转变阈值「内禀 vs 工程化」

> 执行者：A博士（电路→统计力学映射 + Nishimori线/随机场RG框架）。零项目上下文独立续推。
> 日期：2026/06/02。续 phase1_A.md。
> 任务：判定 2D 噪声下相干信息/编码转变的有限阈值 p_c^{coh}>0 是**内禀**（generic局域去极化 + 仅Born测量、无主动前馈，就自动 p_c>0）还是**需工程化纠错**（须显式 syndrome+前馈 / quantum-enhanced 操作）。

---

## 【PI审核入口】

**⚡本Phase结论（一句话）：**
2D噪声监测电路（仅recorded Born测量 + 被traced-out的bulk局域去极化、**无主动前馈**）的稳态相干信息/编码阈值 **p_c^{coh}(2D, passive) = 0 ⟹ BS-2D-1判定 = 需工程化纠错（NOT内禀）**。有限阈值 p_c^{coh}=0.214（2406.14109）**仅在加入 quantum-enhanced(QE) 操作把噪声的均匀场分量抵消到净场=0时出现**；裸被动情形任意 p>0 即面积律。物理根由：被discard的环境注入的熵在 t→∞ 无界累积，而2D无自纠错（Bravyi-Terhal no-go），被动Born record无法移除该熵。**与B博士主结论汇合。**

**⚡最脆弱一步：** §N.4 "discard噪声 = 带**非零均值**(uniform)场分量；QE = 把该均匀分量对称化到零均值随机场" 这一映射归属。若noise实际只贡献零均值随机场（而非含均匀偏置），则3D-RFIM在 d=3>d_lc=2 下随机场irrelevant，p_c>0 可内禀成立，**判定翻转为内禀**。此步直接决定 BS-2D-1。已用 2406.14109 的"net external field=0 才有转变 / 无穷小噪声即面积律"严格佐证均匀分量存在（§N.4反驳检验），但未独立重算去极化信道的Kraus→场分解确认均匀分量系数。**此步若错，判定翻转。**

**⚡预测vs实际：** Phase1预测"2D命题A(p_c>0存活)"。实际：**2D被动 p_c=0（命题B式），与Phase1主线§N.2.2相反。** Phase1 §N.2.2 我用"3D-RFIM有限场阈值"推 2D命题A时，**默认了净场=0这一只有QE才能达成的有利点**——这是叙事越界（为保2D命题A而隐含假设了工程化）。B博士的纠正**实质成立，如实承认**（详§N.1）。

**⚡PI需关注：**
1. S2与S1同病：2D被动情形三序参量(算符纠缠/纠缠熵/相干信息)阈值**全=0**，有限阈值=已发表的QEC阈值物理(Dennis-Kitaev-Landau-Preskill 2002 / 2406.14109)，**S2在2D也大概率重复造轮子**。是否仍按"真MIPT=编码转变"立题？
2. B博士的三序参量**严格分离**假说 (p^{op}=0 < p^{ent} ≲ p^{coh}) **只半对**：op-ent确在0分离，但 ent-entropy 与 coh-info **重合**（2406.14109的CEE转变=同一个QE保护转变，均在0.214），非严格 ≲。需PI裁定是否据此修订B的命题。
3. 唯一可能残留增量：在被动2D**证明三阈值共同坍缩到零**（"no-separation in passive 2D"定理）或刻画**最小工程化资源**(ancilla密度/前馈率)把p_c抬离零的资源阈值。是否重立题于此？

---

## §0 声张强度声明（严格限定）

**本Phase只判定一件事：** 2D噪声**监测电路**（unitary + recorded Born测量 + unrecorded bulk去极化噪声）在 L→∞, t→∞ 稳态下，相干信息/编码阈值 p_c^{coh} 是内禀还是需工程化。

**不外延：**
- 不判 1D（Phase1已结：p_c=0，已发表）。
- 不判非Clifford门/真实器件噪声谱（Phase3）。
- 不重判算符纠缠 p^{op}（2510.12743已发表=0）。
- 不声张"2D存在真MIPT"——本Phase恰恰部分**否证**该乐观展望（被动情形）。
- "内禀"的定义本Phase锁死为：**generic局域去极化 + 仅Born测量 + 无主动前馈/syndrome提取**下自动 p_c>0。"工程化"=须显式加 syndrome测量+前馈 或 retained-controllable ancilla(QE)。

A博士对本Phase声张：**可达成判定（内禀 vs 工程化二选一有明确答案=工程化），且与B独立汇合；但该判定本身的科学新颖性弱（落入已知QEC阈值物理）。**

---

## §0.5 隐含假设清单

| # | 假设 | 来源 | 适用条件 | 是否满足 |
|---|------|------|----------|----------|
| G1 | recorded测量 ↔ discarded噪声 二分：前者=可条件化的quenched disorder(Nishimori线)，后者=不可条件化的熵注入 | 标准(测量=信息增益 vs 退相干=信息丢失) | 噪声环境被trace out且不记录 | ✅ |
| G2 | discard的局域去极化在stat-mech映射中贡献**含非零均值(uniform)的场**，非纯零均值随机场 | 2406.14109("net field≠0除非加QE"；无穷小噪声即面积律) | 去极化偏置向trivial/I方向 | ⚠️核心(§N.4)，未独立重算Kraus→场系数 |
| G3 | 均匀场 h̄≠0 在(任意维)有序相中=显式对称破缺场 ⟹ 摧毁自发有序于任意场强 | 平衡统计力学标准 | 序参量耦合到该场 | ✅ |
| G4 | 零均值随机场下临界维 d_lc=2；d=3(2+1D电路)随机场irrelevant，有限场阈值 | Imry-Ma/Aizenman-Wehr | 短程、净场=0 | ✅(净场=0前提下) |
| G5 | 2402.16937 的内禀有限阈值(p_c=0.109, RBIM/Nishimori)隐含**code的stabilizer=syndrome已被测量** | 该文用toric code结构 | 单次退相干于已成形码 | ✅(其Nishimori线=optimal decoder条件) |
| G6 | bulk噪声每层注入熵，t→∞累积 ~ p·T 无界；被动无熵移除机制 | 熵守恒/数据处理 | 无reset/无syndrome+前馈 | ✅ |
| G7 | 2D无有限温自纠错(Bravyi-Terhal no-go)；被动保信息需≥4D或主动解码 | 严格no-go定理 | 2D局域stabilizer码 | ✅ |
| G8 | 2406.14109是(2+1)D=3D stat-model；其p_c=0.214(2),ν=0.9(1)在net-field=0(QE对称)下取得 | 该文(本Phase精读) | aAEE对称, q_n=q_e | ✅(精读确认) |

最脆弱：**G2**。它是"内禀/工程化"判定的唯一支点。G2成立⟹工程化；G2失败(噪声只贡献零均值随机场)⟹内禀。

---

## §1 结论预测（符号/量级/最易错步）

1. **方向预测：** p_c^{coh}(2D, passive)=0 ⟹ **需工程化**。源于 G2(均匀场) + G6(熵累积) + G7(无2D自纠错)三重独立。
2. **量级预测：** 被动情形，编码相"深度窗口" d* ~ 1/p（2510.07512），固定 p>0 则 t>d* 后 I_c<0；稳态(t→∞)阈值=0。加QE后(净场=0)：3D-RFIM临界，p_c=0.214(2), ν=0.9(1)（2406.14109）。
3. **最易错步：** 把 2402.16937 的**内禀** p_c=0.109（单次退相干于已成形toric code, RBIM/Nishimori）误当作**监测电路稳态**的内禀阈值。二者不同对象：前者code的syndrome(stabilizer)已测=隐含工程化结构(G5)；后者bulk噪声每层累积无syndrome提取。**此混淆=Phase1 §N.2.2的越界根源。**
4. **与B分歧预测：** B的严格三序参量分离 p^{op}<p^{ent}≲p^{coh}；我预测 p^{ent} 与 p^{coh} **重合**(同=QE保护转变)，非严格小于。

---

## §2 强制撞墙（攻击本Phase自己的"工程化"判定）

**撞墙靶心：攻击"p_c^{coh}(2D,passive)=0=需工程化"。构造"内禀 p_c>0"的最强辩护并检验。**

**反例候选IN-1（最强内禀辩护）：**
"clean监测电路的编码/纯化转变(Gullans-Huse)**本就是被动内禀**的——recorded Born outcomes即syndrome，条件于全record的相干信息在体积律相>0，无需任何主动前馈，'decoder'只是对record的最优贝叶斯推断(信息论操作非物理干预)。由2309.02863，Born规则**自动**把有效stat模型锁在Nishimori线**无需fine-tuning**。2D电路=3D stat模型，3D Nishimori RBIM/RPGM有有限阈值。故2D应内禀 p_c>0，**无需工程化**。"

**检验/反驳：IN-1混淆了"recorded测量"与"discarded噪声"——这是G1的要害。**
- 2309.02863的Nishimori自动性，quenched disorder = **recorded measurement outcomes**（"the auxiliary qubits play the role of quenched disorder by being measured"，syndrome被keep）。bulk **decoherence** 是被**trace out**的环境，**不可条件化**。
- 关键：2309.02863自己说有序相"**unveiled only after using a decoder**"，且额外dephasing下GHZ纠缠被破坏。即便recorded情形，跨阈值的有序也需**主动解码**揭示。
- 对discarded噪声：2406.14109严格显示——裸噪声(无QE)下"**even with infinitesimal rate of dephasing/resetting noise, the state obeys an area law**"。即被动情形 p_c=0，**不是**有限。IN-1的"3D-RFIM有限阈值"只在**净场=0**时成立，而净场=0**恰恰需要QE把discard噪声的均匀分量抵消**(§N.4)。
- ⟹ IN-1被驳。recorded-syndrome的内禀性**不**自动延拓到discarded-noise稳态。命题(工程化)经受撞墙。

**反例候选IN-2（搬2402.16937的内禀阈值）：**
"2402.16937严格证 2D toric code相干信息有限阈值 p_c=0.109，**intrinsic information-theoretic transition, independent of decoding protocol**，是ρ的性质。这就是内禀有限阈值，**直接反驳工程化判定**。"

**检验：IN-2换了对象，不构成反驳(G5)。**
- 2402.16937是**单次**(finite)退相干作用于**已成形的toric code**。其RBIM正好落在**Nishimori线**，因为toric code的**stabilizer结构=syndrome本身**——optimal decoder条件于stabilizer测量结果。即该"内禀"阈值**隐含了code的syndrome已被测量**(G5)。
- 监测电路稳态(t→∞)中要维持此结构=**每层重复测stabilizer(syndrome提取)** = 主动syndrome = 工程化。
- 且2402.16937是单次噪声(总噪声有限)，不存在bulk每层累积(G6)。监测电路 t→∞ 累积熵 ~ p·T 无界，超任何有限单次阈值，除非主动移除。
- ⟹ IN-2的内禀阈值是"单次退相干于带syndrome的码"的性质，**不等于**"裸监测动力学稳态"的性质。判定不翻转。**但此点暴露"内禀"一词的二义性，须在§N.3显式拆分两个对象。**

**反例候选IN-3（攻击G2，唯一能真翻转判定者）：**
"若局域去极化在stat映射中**只**贡献零均值随机场(无均匀偏置)，则d=3随机场irrelevant，被动 p_c>0 内禀成立。2406.14109的'均匀场'可能是其**特定QE构造的产物**，非去极化本身固有。"

**检验：未能翻转，但标记为最脆弱残留(=⚡最脆弱步)。**
- 去极化信道 N(ρ)=(1-p)ρ + (p/3)(XρX+YρY+ZρZ) 把任意态拉向 I/2（最大混态），这是一个**确定性的、向trivial方向的偏置**——对应序参量空间一个**非零均值**的drift，非零均值random。2406.14109的"无穷小噪声即面积律"正是此均匀drift的体现(zero-mean random场不会在d=3于无穷小强度破坏有序)。
- 故G2有强物理与文献佐证。**但**A博士本Phase未独立从Kraus算符重算映射后场的均值系数 h̄(p)，仅据2406.14109现象学推断。**保留为卡点K-G2(若h̄=0则判定翻转为内禀)。**
- ⟹ IN-3不翻转当前判定，但定义了判定的"脆弱根"。诚实标记。

**GATE2撞墙产出：** IN-1(驳，recorded≠discarded)、IN-2(驳，换对象/单次vs累积)、IN-3(未翻转但=最脆弱残留)。工程化判定经受撞墙，**条件**=G2(均匀场分量存在)成立。

---

## §N 推导正文

### §N.1 先核实 F4(2406.14109) 与 2408.16267：Phase1是否误读（任务子任务1）

**N.1.1 2406.14109「Protect MIPT from Noise」精读结论（本Phase WebFetch HTML v3）：**

| 核查项 | 结论 | 依据(精读引文要点) |
|--------|------|-----|
| 维度 | **2D**：(2+1)D电路, L×L方格, 映射到**3D** stat模型 | "directly simulate the (2+1)-d quantum circuit with L×L qubits on a square lattice" |
| 裸噪声是否存活 | **否**。无穷小噪声即面积律 | "the state obeys an area law even with an infinitesimal rate of dephasing noise or resetting noise in the circuit's bulk" |
| 存活是否需QE | **是，必须**。QE=相干耦合到**保留的可控ancilla**，镜像噪声信道 | "QE operations…applying a unitary U_SA to entangle the system with the ancilla qubits", "the ancilla qubits remain under our control" |
| QE的本质 | **非**主动syndrome+前馈纠错；是retained-controllable环境(ancilla)+对称化场 | 要求 U_SE=U_SA, q_n=q_e=q/2, ρ_E=ρ_A |
| Imry-Ma作用 | **否定2D**统计模型，迫使升3D | "Considering the absence of phase transitions in the 2D random field Ising model due to Imry-Ma argument" ⟹ 模拟(2+1)D |
| 存活条件 | **净外场=0**(zero-net-field)才有 vol→area转变；此时aAEE对称使CEE为有效探针 | "A transition…becomes possible only when the net external field vanishes" |
| 阈值 | p_c=0.214(2), ν=0.9(1)（在净场=0下） | 精读数值 |

**⟹ B博士对F4的两点纠正全部成立：(a) Imry-Ma是否定2D迫升3D（非"2D存活"）；(b) 存活依赖工程化QE操作。**

**N.1.2 Phase1是否误读？——诚实自审(禁叙事退让)：**
- Phase1 §-1 的 F2 条目(行55-58)**已正确**记录："用Imry-Ma论证2D随机场Ising无相变…故需模拟(2+1)D…其'保护'靠加QE操作(平衡场)"。**此处无误。**
- **但** Phase1 §N.2.2 主线推导(行188)写："d=3(2+1D电路)…随机场irrelevant…3D随机场Ising有有限场阈值h_c ⟹ p_noise^c(2D)>0。命题A(2D)。" —— 此处**把2D存活当作内禀**(只凭"3D-RFIM有限场阈值")，**丢失了"净场=0只有QE才能达成"这一前提**。即主线推导把"3D随机场irrelevant"误当成"任意去极化噪声→随机场→存活"，**隐含默认了净场=0的有利点**。
- **判定：Phase1主线§N.2.2对2D构成实质误读/越界**（§-1脚注对、主线错；以主线对外声张2D命题A）。B博士纠正成立，**如实承认，不为保Phase1的2D命题A辩护**。本Phase修正：2D被动 p_c=0，存活需QE工程化。

**N.1.3 2408.16267「Coherent Information Phase Transition」精读（本Phase WebFetch HTML v3）：**

| 核查项 | 结论 | 依据 |
|--------|------|-----|
| 维度 | **1D**(1+1D)，**非2D** | "we perform large-scale numerical simulations in a (1+1)-d quantum circuit"；brick-wall |
| 是否需QE | **是**。裸噪声=不可恢复相 | "negative coherent information is expected in noisy circuits involving random unitary gates and measurements"；QE后才"reliable transmission" |
| QE本质 | 引入**保护ancilla**(隔离、假定无噪)，US A=SWAP | "introduces ancilla qubits…then isolated and left untouched until the end"；"USA=SWAP" |
| 控制参量 | q=q_n/q_t(噪声占噪声+QE比)，**非裸噪声率**；q_c^reset=0.5, q_c^depo=0.36 | 精读 |
| 裸噪声(q→1)极限 | 不可恢复相，I_C<0 | "for large q, bulk spins align with I" |
| stat映射 | 置换群S(Q)自旋+双向随机场(honeycomb)，"reminiscent of 2D Ising"，一阶变号 | 精读(**非**RBIM/Nishimori) |

**⟹ 关于2408.16267的两点重要校正：(a) 它是1D不是2D**（任务背景/B假说若把它当2D coh-info的2D证据，则误置）；**(b) 它确加QE操作**(SWAP到保护ancilla)，裸噪声下负相干信息。**故2408.16267不提供"被动2D有限coh阈值"的任何证据，反而印证裸噪声破坏、需QE。**

**N.1.4 子任务1小结(返回PI①)：**
- F4(2406.14109)：**加QE**，Imry-Ma**否定**2D，Phase1主线**误读**(已承认修正)。
- 2408.16267：**加QE**，且是**1D非2D**。
- 两文均**不支持**"被动2D内禀有限阈值"，**均支持工程化**。

### §N.2 子任务2：从相干信息stat-mech侧判定（被动监测能否提供有限阈值）

**N.2.1 recorded vs discarded 二分（G1，核心）。**
监测电路有两类"环境耦合"，stat-mech地位**根本不同**：
- **recorded Born测量**：结果被记录，可条件化。在replica/stat映射中=**quenched disorder**，且由Born规则 P(outcome)=|ψ|² **自动落在Nishimori线**（2309.02863: "locking the effective temperature and disorder…Born's rule…naturally enforces…Nishimori physics"，无需fine-tuning）。Nishimori线上，3D RBIM/RPGM(对应2D电路)有有限多临界点，相干信息(条件于record)可>0。
- **discarded bulk噪声(去极化/dephasing)**：环境被trace out，**不可条件化**。它**不**贡献Nishimori-disorder，而是贡献一个耦合序参量的**额外场**，且(G2)含**非零均值(uniform)分量**（向trivial/I）。

**N.2.2 被动情形(只Born测量+discard噪声，无前馈)的稳态判定。**
设映射后有效自由能含：(i) recorded测量→Nishimori随机键(零均值, 在Nishimori线)，(ii) discard噪声→场 h(x)=h̄+δh(x), h̄≠0(G2,G3)。
- 由G3，**非零均匀场 h̄≠0 = 显式对称破缺场**，在任意维度摧毁自发有序于**任意场强**（无 spontaneous magnetization）。
- ⟹ 序参量(体积律/编码相)被 h̄ 单调压向 disorder(面积律/不可恢复)，**任意 p>0(⟹h̄>0)即无有序** ⟹ **p_c^{coh}(2D, passive)=0**。
- 这正是2406.14109"无穷小噪声即面积律"的stat-mech翻译，与F5(2510.07512)"固定p, 编码深度 d*~1/p, t→∞不存活"一致(深度=时间方向, 稳态=t→∞=超临界深度⟹I_c<0)。

**N.2.3 加QE后(净场=0)。**
QE操作(2406.14109)=保留并控制环境ancilla, 镜像噪声(U_SE=U_SA, q_n=q_e)，在场语言中**加一个反向均匀分量抵消 h̄ ⟹ 净均匀场=0**，只剩零均值随机场 δh(x)。
- 此时(G4)在 d=3(2+1D电路)>d_lc=2，**随机场irrelevant**，弱随机场下有序存活 ⟹ 有限阈值 p_c=0.214(2)（2406.14109, G8）。
- **QE把"discarded不可条件化"转回"retained可控"**——这正是把熵注入(G6)堵住的工程化动作。

**N.2.4 熵累积 + 2D自纠错no-go(G6,G7)——独立第二支柱。**
即便忽略均匀场细节，第二条独立论证：
- bulk噪声每层注入熵，t→∞ 累积无界(G6)。被动Born record移除的是"测量算符方向"的熵，**无法移除discard环境的熵**(无syndrome+前馈)。
- 2D局域stabilizer码**无有限温自纠错**(Bravyi-Terhal no-go, G7)：anyon在2D自由扩散，被动无能垒约束。故 t→∞ 信息必失于任意有限噪声密度。**保信息需主动解码(syndrome+前馈)或≥4D。**
- ⟹ 独立给出 p_c^{coh}(2D, passive)=0，**需工程化**。两支柱(均匀场 / 熵累积+no-go)**冗余确证**。

**N.2.5 与2402.16937内禀阈值的对账(G5，消歧)。**
2402.16937 p_c=0.109(内禀, ρ性质, RBIM/Nishimori)看似反例，实为**不同对象**：
- 它是**单次**退相干(总噪声有限)作用于**已成形toric code**；toric code的**stabilizer=syndrome**结构内建，optimal decoder条件于此⟹落Nishimori线。
- 监测动力学稳态要复制此=**每层主动测stabilizer(syndrome提取)** + 总噪声需有界(否则G6累积) ⟹ 这**就是**工程化(主动QEC)。
- ⟹ 2402.16937的"内禀"是"带syndrome的码在单次有限噪声下的optimal-decoder阈值"，**印证**"有限阈值绑定syndrome结构"，**不**反驳被动监测稳态 p_c=0。

**N.2.6 子任务2小结(返回PI②)：** 被动监测(无前馈)在2D **不提供**有限阈值，p_c^{coh}(2D,passive)=0；有限阈值**需工程化**(QE/主动syndrome+前馈)。两条独立stat-mech论证(均匀场 + 熵累积/no-go)汇合。

### §N.3 "内禀"二义性的显式拆分（消除全场混淆）

| 对象 | 阈值 | 内禀? | 关键 |
|------|------|-------|------|
| (O1) 单次有限退相干于**已成形码**(2402.16937, toric) | p_c=0.109>0 | **是(信息论, ρ性质)** | 但隐含stabilizer=syndrome已测(G5) |
| (O2) clean监测电路编码转变(无噪, recorded) | 有限(Gullans-Huse) | **是(被动, record=syndrome)** | 仅recorded测量, 无discard噪声 |
| (O3) **被动**噪声监测稳态(recorded测量 + discard bulk噪声, 无前馈) | **=0** | **否** | discard均匀场+熵累积(G2,G6,G7) |
| (O4) 加QE/主动syndrome+前馈的噪声监测稳态(2406.14109) | 0.214>0 | **否(需工程化)** | QE抵消均匀场/移熵 |

**BS-2D-1 问的是 O3**(裸监测+局域去极化+只Born+无前馈)：**答案=0=需工程化**。O1/O2的内禀性**不延拓**到O3(对象不同：O1单次+带syndrome；O2无discard噪声)。

### §N.4 ⚡最脆弱步的反驳检验（G2，判定支点）

**主张：** discard局域去极化贡献**非零均值**场 h̄≠0（不仅是零均值随机场）。
**反驳检验1（信道结构）：** 去极化 N(ρ)=(1-p)ρ+(p/3)ΣσρσΣ 把任意态**确定性**拉向 I/2(最大混)，是向trivial不动点的**单向drift**。映射到序参量空间=对"有序(编码)方向"的**均匀偏置**，非对称涨落 ⟹ h̄≠0。
**反驳检验2（文献现象学）：** 若 h̄=0(纯零均值随机场)，则 d=3 随机场irrelevant，无穷小噪声**不应**破坏有序——但2406.14109明证"infinitesimal noise ⟹ area law"。**故必有 h̄≠0**(否则与该严格数值矛盾)。
**反驳检验3（QE的作用反推）：** QE的全部功能就是"使net external field vanish"(2406.14109原文)——若本无均匀场需抵消，QE的"零净场"条件将无意义。QE存在的必要性**反证** h̄≠0。
**残留风险（诚实标记）：** 三检验均为现象学/文献推断，A博士**未**独立从Kraus→replica作用量重算 h̄(p) 的解析系数。若严格重算得 h̄≡0(例如去极化的均匀分量在replica极限n→1精确消去)，判定翻转为内禀。**列为卡点K-G2(severity:中高, 判定支点)。** 但当前三独立佐证 + 与F5/no-go的冗余一致性，使翻转概率低。

### §N.5 与B博士汇合度核对（返回PI③）

| 命题 | B博士假说 | A博士本Phase | 汇合? |
|------|-----------|--------------|-------|
| 主判定 BS-2D-1 | 真MIPT(coh-info)有限阈值需工程化/QE | **需工程化(p_c^{passive}=0)** | **✅汇合** |
| F4解读 | A可能误读(Imry-Ma否定2D/需QE) | **承认误读, 修正** | **✅汇合** |
| 算符纠缠 | p^{op}=0 | p^{op}=0(2510.12743) | ✅ |
| 三序参量关系 | **严格分离** p^{op}=0 < p^{ent} ≲ p^{coh} | **半驳**：p^{op}=0✓; 但 p^{ent} 与 p^{coh} **重合**(2406.14109 CEE转变=同一QE保护转变, 均0.214; 被动均0), 非严格 ≲ | **⚠️部分汇合** |

**汇合结论：** 主判定(需工程化)与F4纠正**完全汇合**；B的**严格三序参量分离**假说**部分被驳**(中间项与上项重合而非严格小于)。这是A对B的**反向校正**(B校正了A的F4, A校正了B的严格分离)。

### §N.6 可执行数值方案（子任务3，不要求实跑）

**目标：** 数值确证 O3(被动2D)=0 且 O4(加QE)>0，并测 G2 的均匀场系数 h̄(p)。

**N.6.1 被动2D Clifford+去极化(stabilizer高效)。**
- 模型：L×L方格 brick-wall随机Clifford两比特门 + 概率 p_meas 单比特Z投影测量 + 概率 p 单点去极化噪声(discard, **不记录**)。混合态稳定子模拟(稳定子秩/CHP+混态扩展, e.g. Aaronson-Gottesman + 混态稳定子formalism或mixed stabilizer via stabilizer group rank)。L≤64(2D), T~O(L)。
- 序参量(三个分别测, 检B的分离假说)：
  (a) **相干信息** I_c(R:S)=S(R)-S(RS)，参考R与系统最大纠缠, 跟踪符号。
  (b) **态纠缠熵** S(A)半系统标度(vol vs area)。
  (c) **算符纠缠/三分互信息** I_3(对照2510.12743)。
- 扫描(p_meas, p)网格。**预测：** 固定任意 p>0，三序参量稳态(T→∞外推)**全→area/不可恢复, p_c=0**；窗口 Δp_meas(L)→0 当 L→∞。验证 O3=0。

**N.6.2 加QE对照(确证O4>0)。**
- 同模型但每个噪声事件配一个 retained-controllable ancilla(SWAP/U_SA镜像), 保持 q_n=q_e。**预测：** 出现有限阈值 p_c≈0.214(复现2406.14109), ν≈0.9。**O3=0 与 O4>0 的对比即BS-2D-1的数值判定。**

**N.6.3 直接测均匀场 h̄(p)（闭K-G2）。**
- 在映射后的3D stat模型(或直接测序参量对小噪声的**线性响应**)：测 ⟨序参量⟩ 对 p 的**一阶导**在 p→0⁺。
- **判定：** 若 ∂⟨O⟩/∂p|_{0⁺}≠0(线性、无阈值塌缩)⟹ h̄≠0 ⟹ 确证工程化判定；若 ⟨O⟩ 在小 p 有有限plateau(零响应)⟹ h̄=0 ⟹ 判定翻转内禀。**这是单点可证伪K-G2的实验。**

**N.6.4 资源：** Clifford+Pauli噪声严格高效(O(L²)/层稳定子)，2D L≤64、T~L、~10²轨迹，单机/小集群可行。

---

## §末 声张强度对比 + BS-2D-1判定 + 新增卡点

**声张目标 vs 实际：**

| 维度 | 本Phase目标 | A博士实际 | 变化 |
|------|------------|-----------|------|
| BS-2D-1判定(内禀/工程化) | 给明确二选一 | ✅ **工程化**(p_c^{passive}=0)，双独立论证(均匀场/熵累积+no-go) | 达成 |
| F4/2408.16267核实 | 确认是否误读 | ✅ 两文均加QE; F4 Imry-Ma否定2D; **承认Phase1主线§N.2.2误读并修正** | 达成(诚实退让) |
| 与B汇合 | — | ✅主判定汇合; ⚠️B的严格分离假说部分被驳 | 互校 |
| 新颖性 | (限定不外延) | ❌ 工程化阈值=已发表QEC物理(DKLP2002/2406.14109); 被动=0与1D同型 | 弱 |

**预测vs实际：** Phase1预测"2D命题A(存活)"。本Phase**反转**：2D**被动 p_c=0**(命题B式)，存活需工程化。无残留方向相反未解项——IN-3/K-G2是唯一能翻转的脆弱根，已显式标记+给单点证伪实验(N.6.3)。

**━━━ BS-2D-1 判定（高severity卡点闭合）━━━**
> **判定 = 需工程化纠错（NOT内禀）。**
> 2D噪声监测电路(generic局域去极化 + 仅recorded Born测量 + 无主动前馈)的稳态相干信息/编码阈值 **p_c^{coh}(passive)=0**。有限阈值 p_c>0 须显式加 QE操作(retained-controllable ancilla, 抵消均匀场到净场=0) 或 主动syndrome提取+前馈。
> **条件**：依赖 G2(discard去极化含非零均值场分量)——已三重佐证(信道drift/2406.14109无穷小即面积律/QE零净场必要性)，残留风险见K-G2。
> **冗余支柱**：即便绕开G2，熵累积(G6)+2D无自纠错(Bravyi-Terhal, G7)独立给出同结论。

**新增/更新卡点：**

- **K-G2-均匀场系数(severity:中高, 判定支点)：** 未独立从Kraus→replica作用量重算 discard去极化的均匀场均值 h̄(p)。关闭条件：解析重算 h̄(p) 或跑 N.6.3 线性响应数值。若 h̄≡0 则判定翻转内禀。**当前低翻转概率(三佐证+F5/no-go冗余)，但这是唯一支点，PI须知。**

- **K-S2-重复造轮子(severity:高, 同S1型)：** 被动2D三序参量阈值全=0(与1D同型, 2510.12743/2510.07512已发表); 工程化有限阈值=已发表QEC阈值物理(Dennis-Kitaev-Landau-Preskill 2002; 2406.14109)。**S2在2D无清晰新增量。** 关闭条件：PI决策——(i)判S2亦⛔(2D也重复造轮子)，或(ii)重立题于K-S2'。

- **K-S2'-潜在增量入口(severity:中)：** 被动2D是否可**严格证明三阈值共同坍缩到零**("no-separation in passive 2D"定理, 校正B的严格分离)，或刻画**最小工程化资源**(ancilla密度/前馈率 vs p_c抬升)的**资源阈值**(I_c>0所需 retained-fraction f_c(p))。后者(资源阈值)可能是唯一未被直接发表的薄增量。关闭条件：PI判断是否值得重立题。

- **K-B分离(severity:中, 与B交叉项)：** B的 p^{ent} ≲ p^{coh} 严格分离 vs A的"二者重合(同QE保护转变)"。关闭条件：N.6.1三序参量数值分别外推, 看 p^{ent} 与 p^{coh} 是否数值可分。**留待与B博士独立推导交叉。**

**GATE末：本Phase不标✅(新颖性弱+K-G2脆弱根+K-B待交叉)。主判定(需工程化)稳健且与B汇合，可供PI据以裁S2去留。**

---

## 返回PI 五问速答

①**F4/2408.16267是否加QE / Phase1是否误读：** 两文**均加QE**。F4(2406.14109)是2D, Imry-Ma**否定**2D迫升3D, 存活**必须**QE(retained-controllable ancilla, 净场=0), 无穷小噪声即面积律。2408.16267实为**1D非2D**且加QE(SWAP到保护ancilla)。**Phase1 §-1脚注对、但主线§N.2.2误读(把2D存活当内禀, 隐含默认净场=0)——如实承认并修正。**

②**BS-2D-1判定：** **需工程化纠错**。p_c^{coh}(2D, 被动)=0；有限阈值须QE或主动syndrome+前馈。双独立支柱(均匀场 / 熵累积+Bravyi-Terhal no-go)。

③**与B是否汇合：** 主判定(需工程化)+F4纠正**完全汇合**；但B的**严格三序参量分离** p^{ent}≲p^{coh} **部分被驳**(二者重合=同一QE保护转变, 非严格小于)。互为反向校正。

④**S2能否提供真增量：** **大概率2D也重复造轮子**(被动三阈值全0=1D同型; 工程化阈值=已发表QEC物理)。唯一可能薄增量=被动"no-separation"定理 或 最小工程化**资源阈值** f_c(p)(retained-fraction)。建议PI判S2去留。

⑤**新增卡点：** K-G2(均匀场系数, 判定支点, 可单点证伪)、K-S2(重复造轮子, 高)、K-S2'(资源阈值增量入口)、K-B分离(待与B交叉)。

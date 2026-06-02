# LP8-S3 Phase1 — B博士（突击队/独立子agent）作业

课题: LP8-S3 相互作用费米子MIPT普适类（长命题LP-8，依赖S1已收官）
核心问题: 相互作用在Altland-Zirnbauer各对称类的监测费米子MIPT中是 **relevant**（改普适类，命题B）还是 **irrelevant**（=自由费米子，命题A，Foster在DIII猜的）?
B身份: 零项目上下文独立agent。禁用A的框架（CFT/ε展开 + DMRG数值）。本作业框架: **AZ十重对称类拓扑分类 + Anderson局域化相互作用稳定性结构类比**，辅以 **SYK/随机矩阵高斯吸引域** 作第二条独立腿做交叉验证。

---

## 【PI审核入口】速读区

| 项 | 内容 |
|---|---|
| ⚡B独立结论 | **守恒流判据**: 相互作用relevant ⟺ 自由不动点存在超出复本置换对称的连续守恒流(Noether流)。据此: **命题A(irrelevant)=D, DIII, BDI, AII, AI**(无连续守恒荷的Majorana/实类); **命题B(relevant)=A, AIII**(U(1)荷) **及 C, CI, CII**(SU(2)自旋)。 |
| ⚡框架 | AZ拓扑分类 + Anderson相互作用稳定性类比(主)；SYK高斯吸引域(交叉验证副腿)。**完全不用**CFT/ε展开/DMRG。 |
| ⚡与A关系 | **部分汇合**: 与Foster(DIII→A)汇合，与Poboiko-Mirlin(AIII→B)汇合。**新增可证伪预测**: C/CI/CII因SU(2)守恒流→命题B(A的DIII-only框架很可能未覆盖)。 |
| ⚡Q2先发查重 | 端点已发表(DIII=A: Foster 2510.23706; AIII=B: Poboiko-Mirlin 2410.07334/07317)。**系统性十重相互作用relevance表未发表**(2412.06133明言相互作用是future work)。C类预测+统一守恒流判据=未占坑。 |
| ⚡苏格拉底⭐前三 | (1)危险无关→有限尺寸DMRG是否落在crossover误读ν? (2)复本R→1极限下mass relevance是否与ε=2−R解析延拓自洽(序极限/RSB)? (3)A是否对荷守恒类纳入流-流通道,否则会错判AIII为自由? |

---

## §0 框架声明

A本Phase用: **CFT/ε展开 + DMRG数值**（算各类Δ_int标度维数 + DMRG验DIII）。

B禁止用上述两者。本作业采用两条独立腿:
- **主腿**: 十重Altland-Zirnbauer对称类拓扑分类（K理论/分类空间），结合 Anderson局域化中"相互作用对各类非相互作用不动点稳定性"的已知结构（Finkel'stein NLSM / Foster-Ludwig多分形传统）。
- **副腿（交叉验证）**: SYK/随机矩阵高斯不动点对非高斯（相互作用）微扰的吸引域，按对称类分。

不重叠声明: B不计算任何ε=2−R展开下的标度维数，不做任何DMRG/数值张量网络。B的判据来自对称群表示论 + 拓扑分类空间的同伦结构 + 守恒流计数，是A的解析微扰论之外的正交方法。

---

## §0.5 前置三问（先发查重 / 防造轮子）

> ⚠️ S1/S2教训: 同长命题已两次因"核心结论已发表"判重复造轮子。MIPT是密集发表热点。本节为硬门。

### Q1. 核心前提是否成立? 有无文献否定?

核心前提: "自由费米子监测MIPT在AZ十重类下与Anderson局域化转变统一分类，相互作用作为微扰其relevance可由对称类结构判定。"

- **前提成立，且是当前共识**。
  - 自由费米子监测动力学↔Anderson局域化的AZ统一: Jian-Shapourian-Bauer-Ludwig (2302.09094), Fava-Piroli-Swann-Bernard-Nahum NLSM (2302.12820), 以及 2412.06133 (Table 1: 复本Kraus算符的TRS/PHS/CS → 十重分类空间，时间方向↔转移矩阵空间方向)。**无文献否定此映射**。
  - "相互作用作为微扰判relevance"的范式在平衡态Anderson问题中是标准的(Finkel'stein)，迁移到监测情形是合理类比。**无否定**。
- **唯一警告**: 拓扑θ项类(BDI ℤ, D ℤ₂)的自由不动点本身非平庸(c≠0的θ项NLSM/WZW型)，"对自由Gaussian不动点的微扰"叙事在这些类需要修正——见§N步骤6与苏格拉底Q4。这是前提的边界，非否定。

### Q2. 有无先发论文已做"对称类相互作用费米子MIPT普适类"?（重点搜索词已用）

搜索词覆盖: "interacting fermion MIPT universality symmetry class", "Altland-Zirnbauer monitored transition", "interaction relevant irrelevant nonlinear sigma model symmetry class"。结果:

**已占坑的端点（必须如实记录，不可造轮子）:**
1. **DIII = 命题A**: Foster, arXiv **2510.23706** (2025)。"我们猜测此情形MIPT就是非相互作用DIII的；体积律相通过危险无关(dangerously irrelevant)的mass出现。" 明确限定"arguments specific to class DIII (and possibly class D)"，并警告不外推到有额外守恒律的类。
2. **AIII (U(1)荷守恒) = 命题B**: Poboiko-Mirlin 等, arXiv **2410.07334** + **2410.07317** (2024)。荷守恒监测相互作用费米子→主手征模型(PCM, class AIII)，"quartic interaction is relevant"，相互作用诱导"information-charge separation"，且 **AIII无相互作用时根本无MIPT**——相互作用是transition存在的必要条件。
3. **D类**: Foster点名为future work(连surface code)。
4. **十重系统分类**: 2412.06133明言"将多体相互作用纳入框架...是significant的[未来工作]"——**自由费米子分类，相互作用未做**。

**未占坑（B的潜在贡献 / 不是造轮子）:**
- 横跨全部十类的 **统一relevance判据** 尚未发表。
- **C/CI/CII（SU(2)自旋守恒）的相互作用relevance** 未见论文。这是B的可证伪新预测的着力点。
- Dirac vs Majorana的对照(2305.10363: Dirac IRFP相互作用irrelevant，Majorana"largely open")旁证了"守恒荷区分relevance"的逻辑，但未在监测MIPT语境系统化。

**Q2结论**: 端点(DIII,AIII)已发，**不可重做这两点的推导当原创**；但统一守恒流判据 + C类预测 = 未占坑，可做。B的价值定位为"系统化 + C类新预测 + 与两组端点结果的独立汇合检验"。

### Q3. A最可能在哪步叙事退让?

预判A的退让点（供苏格拉底）:
- **退让1（最可能）**: A用CFT/ε=2−R展开算"mass算符"Δ_int得"所有类Δ>d⇒irrelevant"，但若A未单独纳入**荷守恒类的流-流(current-current)通道**，会对AIII也得"irrelevant"，与Poboiko-Mirlin的"relevant且必需"直接冲突。A可能用"我们聚焦无额外守恒律的类"来叙事退让，悄悄把AIII排除出claim范围。
- **退让2**: DMRG只验了DIII。A可能从"DIII数值支持irrelevant"滑向"故各类皆irrelevant"的过度推广，而把C/A/AIII含糊带过。
- **退让3**: "危险无关"需λ精调到临界面，A可能不报crossover标度，使有限尺寸DMRG的ν读数的可信区间被高估。

---

## §1 预测（B独立给出，落判到每个AZ类）

**核心判据（B独立提出）**: 监测自由费米子不动点的复本NLSM具有对称群 G。相互作用以两种算符进入:
- (i) **置换破缺mass算符** O_M（破 S_R×S_R 或连续复本旋转 → 对角 S_R）: 这是体积律/纠缠的来源，在所有类都存在，但维度高 → **强无关**(危险无关)。
- (ii) **守恒流-流算符** J·J（仅当G含超出复本置换的连续守恒子群时存在）: 守恒流维度受保护(Δ_J=d，不重整)，故 J·J 在 d=1 为**边缘/相关**。

⇒ **相互作用relevant ⟺ 自由不动点存在连续守恒流(U(1)荷或SU(2)自旋)。**

| AZ类 | 连续守恒流? | B预测 | 物理说明 |
|---|---|---|---|
| **A** | U(1)荷 | **B (relevant)** | 复类，粒子数守恒→流-流通道 |
| **AIII** | U(1)荷(手征) | **B (relevant)** | =Poboiko-Mirlin: 无相互作用无MIPT，相互作用必需 |
| **AI** | 无(实,无荷) | **A (irrelevant)** | 仅置换mass，危险无关 |
| **BDI** | 无(Majorana) | **A (irrelevant)** | 注: 带ℤ拓扑θ项，见警告 |
| **D** | 无(Majorana) | **A (irrelevant)** | Foster点名,与其D猜测一致 |
| **DIII** | 无(Majorana) | **A (irrelevant)** | =Foster主结论，B独立汇合 |
| **AII** | 无(Majorana,Kramers) | **A (irrelevant)** | 自旋轨道但无连续守恒荷 |
| **C** | SU(2)自旋 | **B (relevant)** ⭐新 | SU(2)守恒流→流-流相关 |
| **CI** | SU(2)自旋 | **B (relevant)** ⭐新 | 同上 |
| **CII** | SU(2)自旋 | **B (relevant)** ⭐新 | 同上 |

**分界线**: 复类(A,AIII)+辛/自旋类(C,CI,CII) = 命题B; 实/Majorana主序列(AI,BDI,D,DIII,AII) = 命题A。

**最尖锐可证伪预测**: C/CI/CII（A的DIII-only框架最可能未覆盖）应为命题B。若A或后续数值在C类发现相互作用irrelevant，B的守恒流判据被证伪。

---

## §2 苏格拉底问题（与推导并行记录，A未问自己的）

⭐ = top优先。前三⭐供PI。

- **⭐Q-S1 [crossover误读]**: "危险无关"定义即λ须精调到临界面。有限尺寸下存在crossover长度 ξ_×(λ)，L<ξ_× 时看到的是相互作用(体积律张力)行为，L>ξ_× 才是自由费米子临界。A的DMRG(典型L~数百)是否落在crossover内而把ν读成中间值? A是否报告了 ξ_×(λ) vs L 的分离判据? 若未报，"DIII=自由费米子ν"的数值证据不充分。

- **⭐Q-S2 [复本R→1序极限]**: Foster的ε=2−R展开是从R=2向下解析延拓。mass算符的relevance(乃至符号)在 R→1(测量物理极限) 与 R≥2 之间可能不连续(类比自旋玻璃复本对称破缺/序极限问题)。A是否论证了irrelevance在R→1鲁棒，而非ε展开的光滑性假象? 这是A整个"危险无关"claim的命门。

- **⭐Q-S3 [守恒流通道遗漏]**: A的框架是否对荷守恒类(AIII/A)单独计入流-流算符 J·J? 若A只算置换破缺mass的Δ_int，会对所有类得"irrelevant"，从而**错判AIII为自由费米子普适类**——与Poboiko-Mirlin"AIII相互作用必需"硬冲突。A的claim范围是否诚实地把AIII排除? 这是检验A是否过度推广的关键。

- Q-S4 [拓扑θ项类]: BDI(ℤ)、D(ℤ₂)的自由不动点本身由拓扑θ项NLSM(非平庸CFT)主宰。"相互作用对Gaussian不动点微扰"的维度计数在此处用的是θ项CFT的标度维数而非自由场维数。A是否区分了θ项类与非拓扑类的mass维度?

- Q-S5 [转变两侧对称性]: 体积律侧mass相关、面积律侧mass无关、临界点mass恰好边缘——则转变对算符内容是否真对称? A的"危险无关"图像在面积律侧与体积律侧的mass算符是否同一个,符号如何?

- Q-S6 [SYK副腿一致性]: 单点SYK中q=4(相互作用)对q=2(自由Gaussian)是IR相关的——若naive照搬,所有类相互作用都该relevant。为何监测MIPT中无守恒荷类却irrelevant? 答案在"局域(spatially local)"vs"全连接(all-to-all)"差异——A的框架是否澄清了这一点?(B在§N步骤7处理)

---

## §N 独立推导

> 每步: [描述] / [框架工具] / [依据] / [最易错处]。禁引用A替代自己，禁"显然"。

### 步骤1 — 建立"监测自由费米子↔AZ类Anderson问题"映射

- **描述**: 监测费米子轨迹的复本平均生成一个(d+1)维复本NLSM，时间方向扮演平衡态Anderson转移矩阵的空间方向；单粒子Kraus算符K_t的TRS/PHS/CS决定其落入十重AZ类之一。
- **框架工具**: AZ十重分类 + 转移矩阵/Lyapunov谱类比。
- **依据**: 2412.06133 Table 1给出 L_t(生成元)与 H̄_t 的分类空间(C_s/R_s)及关系 H̄_t∈C_{s-1}/R_{s-1}; 纯化时间 τ_p=2/min|η_n| 对应局域长度 ξ=1/min|γ_n|。Fava-Nahum NLSM(2302.12820)给Majorana链class D/BDI/DIII的NLSM target。
- **最易错处**: 复本极限。测量物理要求 R→1(或Born规则的特定复本结构)，而NLSM的对称群G在R一般值与R→1时不同。错把R≥2的对称群当物理对称群会误判可用算符集合。

### 步骤2 — 列出每个AZ类的自由不动点对称群G与target manifold

- **描述**: 自由(无相互作用)NLSM的连续对称群G。复类: G含U(N)型复本旋转 + U(1)荷; 实类: G含O(N)/Sp(N)型; 自旋(C)类含SU(2)。
- **框架工具**: 分类空间(C_0=∪U/U×U; R_0..R_7的实/辛Grassmannian)。
- **依据**: 2412.06133表; Poboiko-Mirlin明确AIII自由理论=U(R) PCM(主手征模型),对称群SU(R)×SU(R)×U(1)×U(1)。
- **最易错处**: 把"target manifold的等距群"误当"可写相互作用算符的对称群"。真正控制relevance的是 **保留在复本场论中、且对应物理守恒量(Noether)** 的连续子群——不是manifold全部等距。

### 步骤3 — 把相互作用分解为对称破缺算符,按其破缺的子群归类

- **描述**: 四费米相互作用在复本NLSM中投影为两族算符: (i) O_M 置换破缺mass(破连续复本旋转→对角S_R); (ii) O_J 守恒流双线性 J·J(只在G含连续守恒荷时存在,不破该守恒荷但耦合不同复本的流)。
- **框架工具**: 算符内容的对称表示论分解。
- **依据**: Poboiko-Mirlin 2410.07334: "interaction-induced terms reduce NLSM symmetry → information-charge separation"; SU(R)→S_R×[U(1)]^{R-1}。流-流项=Noether current perturbation(tree-level marginal); 四次项=mass(off-diagonal涨落质量)。
- **最易错处**: 漏掉 O_J。若只保留 O_M,对所有类都得"高维→irrelevant"。O_J 是荷守恒类与Majorana类分野的全部物理所在。

### 步骤4 — relevance维度计数(不用ε展开,用守恒流维度保护)

- **描述**: O_M 维度 Δ_M: 由破缺连续对称的高阶不变量构成,典型 Δ_M ≥ (大),> d+1 ⇒ irrelevant。O_J 维度: 守恒流 J 维度受Ward恒等式保护 Δ_J = d(不重整),故 J·J 的 Δ ≈ 2(d) - (空间积分) → 在1+1d为**边缘**,且复本结构使其在 R→1 转为**边缘相关**。
- **框架工具**: 守恒流的非重整(Δ_J=d严格); 复本极限下边缘项的符号。
- **依据**: 守恒流维度保护是CFT/NLSM普适事实(独立于具体模型); Poboiko-Mirlin得"quartic relevant"且AIII相互作用必需,与此一致。Foster得DIII的O_M危险无关(Δ_M>2),与"无O_J时只剩高维mass"一致。
- **最易错处**: (a)边缘项符号——边缘相关 vs 边缘无关由单圈β函数系数定,B在此只能定"边缘",符号需具体计算(诚实标注:这是B此腿的精度上限)。(b)R→1下 J·J 是否仍存在: 需要 ≥2复本才有"流-流"交叉项,R→1的解析延拓是潜在漏洞(记入苏格拉底Q-S2)。

### 步骤5 — 落判每类(守恒流计数)

- **描述**: 逐类查"是否有连续守恒流":
  - A, AIII: U(1)粒子数 → 有 O_J → **B**。
  - C, CI, CII: SU(2)自旋(PHS²=−1源于自旋旋转) → 有非阿贝尔 O_J → **B**。
  - AI, BDI, D, DIII, AII: 无连续守恒荷(Majorana/实,粒子数非守恒或无U(1)) → 仅 O_M → **A**。
- **框架工具**: AZ类的物理实现(复类有U(1); C类有SU(2); 实Majorana类无连续荷)。
- **依据**: 标准AZ字典(复类↔U(1)荷; C/CI/CII↔BdG+自旋SU(2); D/DIII/BDI↔BdG无自旋守恒)。
- **最易错处**: AII。AII有Kramers TRS(自旋轨道),易误以为有自旋SU(2)→B; 但自旋轨道耦合**破坏**SU(2),AII无连续自旋守恒荷 → 正确归 **A**。这是C类(守SU(2))与AII(破SU(2))的关键区分。

### 步骤6 — 拓扑θ项类的修正(BDI/D)

- **描述**: BDI(1+1d ℤ,θ项)、D(ℤ₂)的自由不动点非平庸,O_M维度应在θ项NLSM(WZW型,c≠0)上计,非自由场。
- **框架工具**: θ项NLSM的临界标度。
- **依据**: 2412.06133: β(t)=d−1−4t³+O(t⁴),d≤1时β<0,转变须靠θ项而非标准NLSM。
- **最易错处**: θ项CFT中算符维度可低于自由场估计,理论上可能把某"A类"拉向边缘。**诚实标注**: BDI/D的"A"判定置信度低于DIII/A/AIII; 需θ项CFT显式维度才能锁定。这是B独立推导承认的不确定带。

### 步骤7 — SYK/随机矩阵副腿(交叉验证)

- **描述**: 自由费米子=Gaussian(q=2)不动点; 相互作用=非高斯(q=4)微扰。问各类Gaussian不动点对q4的吸引域大小。
- **框架工具**: SYK的q-标度 + 随机矩阵系综(GUE/GOE/GSE↔AZ)。
- **依据**: 单点SYK中q4对q2是IR相关(q2 SYK不稳定)。但关键差异: 监测MIPT是**空间局域**的,q4的相关性被对称性筛选——当对称禁止低维不变量(无守恒流类),局域q4只能生成高维O_M ⇒ Gaussian吸引域**大**(irrelevant); 当有守恒流(U(1)/SU(2)),局域q4可经流-流生成边缘算符 ⇒ 吸引域**小**(relevant)。
- **结论**: SYK副腿与主腿(守恒流判据)**自洽**——吸引域大小由"对称允许的最低维非高斯不变量"决定,正是守恒流的有无。Dirac(有U(1))IRFP相互作用irrelevant vs Majorana"open"(2305.10363)是旁证: 提示即便有U(1)的具体不动点也可能irrelevant,即守恒流是**必要非充分**条件(见汇合卡点)。
- **最易错处**: 全连接SYK ≠ 局域MIPT,不可直接搬q4相关结论。must经"空间局域+对称筛选"中介。

### 步骤8 — 综合:守恒流判据的逻辑地位

- 守恒流存在 = 相互作用relevant 的 **必要条件**(无守恒流 ⇒ 只剩高维mass ⇒ 必irrelevant ⇒ 命题A 稳)。
- 守恒流存在是否**充分**? 步骤4的"边缘"项符号未定 + 步骤7的Dirac IRFP反例 ⇒ 守恒流类**可能**relevant(边缘相关)但需逐类验符号。AIII已被Poboiko-Mirlin证relevant(且必需),故U(1)类充分性在AIII坐实; C类(SU(2))为B的**预测**(充分性待验)。
- **B的稳健claim**: 命题A集合(AI,BDI*,D*,DIII,AII)逻辑上稳(*BDI/D有θ项不确定带); 命题B集合中AIII坐实、A高置信、C/CI/CII为可证伪预测。

---

## §末 汇合检验（B vs A）+ 苏格拉底清单

### B vs A 汇合表

| AZ类 | B结论(守恒流判据) | A相关结论(据A摘要,CFT/ε+DMRG) | 汇合? |
|---|---|---|---|
| DIII | A (irrelevant) | A用ε展开+DMRG验DIII为irrelevant(Foster猜想) | ✅ 汇合 |
| D | A | A可能(Foster点名future) | ✅ 预期汇合 |
| AIII | B (relevant,必需) | ❓ A是否单独纳入流-流通道? | ⚠️ 待A澄清(潜在卡点) |
| A | B | ❓ | ⚠️ 待澄清 |
| C/CI/CII | **B (新预测)** | ❓ A的DIII-only框架很可能未覆盖 | 🔶 开卡点(B的独立增量) |
| AI,BDI,AII | A | ❓ | 待对照 |

### 汇合卡点（开卡点,供PI/汇合会）

- **卡点-1 [AIII一致性,severity高]**: 若A的ε展开框架对所有类只算置换mass的Δ_int,A会得"AIII也irrelevant"——与Poboiko-Mirlin(已发表,AIII相互作用必需)硬冲突,也与B的守恒流判据冲突。**必须核对A是否纳入流-流通道**。这是B与A最可能的实质分歧点。

- **卡点-2 [C类预测分歧,severity中]**: B预测C/CI/CII为命题B(SU(2)守恒流)。若A框架覆盖到C类并得irrelevant,则两腿冲突,需第三方(显式β函数符号或数值)裁决。若A未覆盖C类,则B提供独立增量,无冲突但需PI决定是否纳入命题范围。

- **卡点-3 [BDI/D拓扑带,severity中]**: B承认BDI/D因θ项而置信度低。若A的DMRG/CFT在D类(Foster future work)给出明确结论,可填B的不确定带——此处A可能反向补B。

### 苏格拉底清单（前三⭐已置§2顶部）

1. ⭐ Q-S1 crossover误读ν(有限尺寸DMRG是否落crossover内)
2. ⭐ Q-S2 复本R→1序极限(ε=2−R延拓到R→1是否鲁棒,RSB风险)
3. ⭐ Q-S3 守恒流通道遗漏(A是否对荷守恒类计J·J,否则错判AIII)
4. Q-S4 拓扑θ项类mass维度(θ-CFT vs自由场)
5. Q-S5 转变两侧mass算符对称性
6. Q-S6 SYK全连接vs局域的relevance差异澄清

### B自我攻击（按记忆feedback_self_attack）

- 自攻1: 守恒流判据是否只是把Poboiko-Mirlin(AIII)与Foster(DIII)的已知结论"事后合理化"? — 反驳: 判据是从对称表示论独立导出(步骤3-4),且产出**两组结果未覆盖的C类新预测**,非纯事后。但C类预测的充分性(边缘项符号)是真未证,如实标注。
- 自攻2: R→1极限漏洞(Q-S2)同样威胁B自己的步骤4(J·J需≥2复本)。— 承认: 此漏洞对A和B**对称**,是整个领域的公共风险,非B独有缺陷。
- 自攻3: AII归类。自旋轨道是否残留某连续守恒荷? — 核查: AII的Kramers TRS不含连续生成元,自旋轨道破坏SU(2),无连续守恒荷,归A正确(步骤5最易错处已处理)。

---

## 引用（背景,非前提）
- Foster, arXiv 2510.23706 (2025) — DIII危险无关,命题A端点
- Poboiko-Mirlin等, arXiv 2410.07334 / 2410.07317 (2024) — AIII荷守恒,相互作用relevant且必需,命题B端点
- 2412.06133 — 监测动力学AZ十重对称/拓扑分类(自由,相互作用=future work)
- Fava-Piroli-Swann-Bernard-Nahum, 2302.12820 — 自由费米子监测NLSM
- Jian-Shapourian-Bauer-Ludwig, 2302.09094 — 非相互作用费米子监测纠缠转变
- 2305.10363 — Dirac IRFP相互作用irrelevant vs Majorana open(守恒荷区分relevance旁证)
- S1/S2教训 — MIPT密集发表,先发查重为硬门

*B博士 Phase1 完。框架: AZ拓扑分类+守恒流判据(主) / SYK吸引域(交叉验证)。完全独立于A的CFT-ε-DMRG。*

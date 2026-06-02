# LP8-S5 Phase1 — A博士 (CFT/replica场论 + 数值协议)
## MIPT多体纠缠层级：k-party GME标度指数是普适特征(命题A)还是模型/度量artifact(命题B)

---

## 【PI审核入口】

- **⚡结论**：**有条件命题A**。在1D MIPT最小模型(measurement-only / percolation类)，k-party GME标度指数层级 αk=2k 是**非幺正CFT的解析定理**(Allen-Witczak-Krempa已证)，且因其本质是 minimal-cut/几何上界，对GME度量选择鲁棒——这是命题A的最强单点证据。但"丰富层级"(严格次可加、非线性αk)只在generic/Haar类出现，而恰恰在该类，GME(尤其GMN负值)指数**跨研究不收敛**(α2在三篇文献中=9 / 7.1 / 6.2)，且2602.04969自承GMN"对电路细节与有限尺寸高度敏感"。因此**命题A在percolation类成立、在generic类未决**，区分A/B的判决性实验(独立CFT提取αk vs 直接GME测量比对)**至今无人执行**——这是本Phase开出的核心卡点。

- **⚡最脆弱步**：§N-3。假设"genuine-k-party GME幂律指数 αk = 单个BCC算符标度维数(或其固定线性组合)"。若不同GME单调量(负值/multi-entropy/GMN)探测的是融合通道中不同算符 → αk度量依赖 → 直接坍向命题B。这是A/B分界的唯一支点。

- **⚡预测vs实际**：CFT/replica预测 percolation类 αk=2k(次可加饱和=无反常融合) ✅与seed解析结果一致；generic类严格次可加(α4<2α2) ✅与2602.04969数值(α2≈9,α3≈11,α4>12)定性一致。**但**预测的"度量无关性"**未经检验**，且generic类α2的绝对值在文献间分散40% ⚠️。

- **⚡PI需关注**：(1) GATE0判定为**部分先发**——seed的GME层级+三猜想已发表且已在两个模型确认，本Phase增量必须严格限定在"普适性判据(独立CFT提取vs直接GME坍缩)"，不可重推层级本身。(2) 我**未运行**ED/TDVP(本agent无可靠算力)，§3给出完整可执行数值协议并开卡点K-S5-1。(3) Polaris"三等价"需修正读法：αk、CFT BCC谱、多重分形τ_q 不是数值相等，而是**同一非幺正CFT算符内容的三个投影**——详§N-5。

---

## §-1 GATE0 先发查重（判定：⚠️ 部分先发 / 无致命冲突）

三组检索全部执行(联网)，命中谱系如下：

### 核心组
- **arXiv:2509.12109v2** Allen, Witczak-Krempa, *Spatial structure of multipartite entanglement at MIPT*(seed/禁区)。确证精确结论：MIPT具长程k-party GME，**k≥2无限层级指数**；三猜想关系：①classical dominance ②monotonicity ③subadditivity；1D measurement-only→2D percolation **解析**得指数(非幺正CFT)，2D→3D percolation仅**数值**得"前几个"指数。**未列具体数值于摘要**，普适性明示为motivation而非已决。
- **arXiv:2602.04969v1** *Taming multiparty entanglement at MIPT*(2026-02，**晚于seed**)。trapped-ion MMS门(Haar非幺正CFT类)。**关键数值**：GMN指数 α2≈9(−0.2/+1.0)、α3≈11(−0.3/+2.0)、α4>12；MI指数 αkMI=k+2(=4,5,6)。三猜想"对所有N成立"，严格次可加 α4<2α2、α3<(3/2)α2。pc(∞)=0.142(3)，ν=1.34(6)≈4/3。**自承**：GMN"对电路细节、有限尺寸、统计高度敏感"，MI标度相对稳定；**明示开问**："能否从底层CFT预测GME与MI指数？"——**即本Phase判据，未决**。

### 出发点+综述组
- **arXiv:2107.03393** Li-Vasseur-Fisher-Ludwig (PRL 128,050602) *Operator scaling dimensions and multifractality at MIPT*。generic MIPT具**连续标度维数谱=多重分形**；generic / Clifford / percolation **三个不同普适类**。transfer-matrix提c_eff与低位算符维数。
- **arXiv:2310.03078v2** *Boundary transfer matrix spectrum of MIPT*。提BCC算符维数：MOIM(=percolation,pc=0.5) c_eff=0.96(1)，h_{f|a}=0.048(6)，h_{a|b}=0.097(2)；**纠缠熵对数系数 γ=2h_{a|b}**；谱**类依赖**(不同普适类谱不同)。

### 竞争者组
- **arXiv:2511.08690v1** *Fractal structure of multipartite entanglement in monitored circuits*(2025-11，**晚于seed**)。1D Clifford,L≤240。最大纠缠簇分形维 d∈(0,1)，**随p连续可调(非普适)**；临界点depth指数γ≠分形维d(归于对数修正/有限尺寸)；**未连CFT/τ_q**；单模型。
- arXiv:2404.16095(long-range multipartite near MIPT)、2305.10209(collective spin三regime)、2302.10132(metrology/QFI)：均为GME witness/QFI视角，非层级标度指数坍缩，无致命重叠。

### 判定
**⚠️ 部分先发**。被占领地：(a) k-party GME层级的存在+三猜想关系；(b) percolation类解析指数；(c) Haar类GMN指数数值；(d) generic类多重分形连续谱；(e) BCC边界谱。**未被占领(本Phase合法增量)**：① 层级普适性的**判决性区分**(独立CFT提取αk ⊗ 直接GME测量的坍缩检验)——2602.04969明示为开问；② αk的**度量无关性**检验(GMN vs 负值 vs multi-entropy同指数？);③ αk / CFT-BCC谱 / 多重分形τ_q 三者的**统一投影关系**形式化。**无先发冲突**(无人已判A或B)。GATE0通过，增量存活但显著收窄。

---

## §0 声张（本Phase，有条件）

限定域：**1D MIPT最小模型**(measurement-only Ising→percolation；及作对照的generic/Haar、Clifford类)，k=2–5的genuine k-party GME标度指数 {αk}。

声张：{αk} 是否为**普适**(命题A：由底层非幺正CFT算符内容唯一决定，类内坍缩、跨类按CFT可预测地不同)，抑或**artifact**(命题B：依赖GME度量选择与电路微观细节/有限尺寸，无度量无关的收敛值)。

本Phase**不**声张generic类的绝对指数值(算力不足、文献未收敛)；**不**重推层级本身(禁区)。

---

## §0.5 隐含假设（显式列出，逐条标风险）

1. **(H1)** GME幂律假设：临界点处 GME_k(L) ~ L^{−αk}，单一幂律主导。[风险：中。对数修正可掩盖幂律，2511.08690正遇此(γ≠d)。]
2. **(H2)** BCC对应假设：k-party配置的GME映为k个边界条件改变(BCC)算符的关联函数，αk由相关算符标度维数决定。[风险：高——见§N-3，本Phase最脆弱支点。]
3. **(H3)** replica-S_n假设：MIPT纠缠量来自置换对称群S_n的replica场论，n→1(熵类)或解析延拓(矩类)。[风险：低，已是领域共识。]
4. **(H4)** 度量无关性(命题A的必要条件)：任意genuine-k-party GME单调量给出相同主导αk。[风险：高，**未经检验**，正是判据核心。]
5. **(H5)** 最小模型代表性：measurement-only percolation类捕获1D MIPT的GME层级本质。[风险：中。percolation层级"平凡线性"(αk=2k)，丰富结构在generic类，故最小模型可能**不代表**丰富层级。]

---

## §1 预测（可证伪，CFT/replica导出）

**P1（percolation/最小模型类）**：αk=2k，次可加**饱和**(αk+ℓ=αk+αℓ)。物理：BCC算符在该通道**无反常融合**(类高斯/对数CFT)，每party贡献固定维数2，可加。→ 与seed解析结果一致(引用，非重推)。

**P2（generic/Haar类）**：αk**严格次可加**(αk+ℓ<αk+αℓ)，binding维数δk=Σαℓ−αk>0。物理：BCC算符融合产生反常维数,k-party关联坍向更低维通道→genuine多体关联超越成对。→ 与2602.04969(α4<2α2,α3<1.5α2)定性一致。

**P3（判决性，本Phase核心）**：若命题A为真，则存在**与GME计算无关**的CFT提取 αk^CFT = f(transfer-matrix BCC谱)，满足 αk^GME = αk^CFT(在数值误差内)，且**对GME度量选择不变**。若命题B为真，则αk^GME 随度量(GMN/负值/multi-entropy)与电路微细节漂移，且不匹配任何独立CFT提取。

**P4（多重分形交叉，§N-5）**：generic类的αk与多重分形谱τ_q同源于S_n算符内容；具体 αk 对应"k-fold linked"通道维数，τ_q对应q-replica对称矩维数——二者**不数值相等**但**同一CFT数据的两个投影**。可证伪点：若generic类αk能由独立测得的τ_q通过replica字典预测，则统一成立；若不能，Polaris三等价被削弱为"各自独立的标度律"。

---

## §2 强制撞墙 → 文献库反例栏

主动搜寻**反驳本Phase倾向(命题A)**的证据，逐条登记：

| # | 反例/张力 | 来源 | 对A/B的指向 | 我的回应 |
|---|---|---|---|---|
| W1 | 同一bipartite负值指数α2跨文献=9/7.1/6.2，分散~40% | 2602.04969自引prior works | **强B**(若真artifact) | 可能有限尺寸+度量定义差异；但**未被排除**为真度量依赖→进卡点 |
| W2 | GMN"对电路细节高度敏感"，MI"稳定" | 2602.04969 App.D | **B(对GMN)** | 暗示αk^GME的鲁棒性是**度量特异**的；MI(αkMI=k+2)更可能普适→A仅对"对的度量"成立 |
| W3 | 分形维随p**连续可调**,非普适 | 2511.08690 | 表面B | 但那是**area-law相**的离临界结构,非临界指数;临界点单独讨论(γ≠d未决)→不直接反驳临界αk普适 |
| W4 | 临界点depth指数γ≠分形维d | 2511.08690 | **方法论警告** | H1(单幂律)在临界点被对数修正污染→直接拟合αk有系统偏差,需transfer-matrix而非实空间拟合 |
| W5 | generic/Clifford/percolation是**三个不同普适类** | 2107.03393 | 中性偏A | 跨类αk不同是**预期**(各有各的CFT);A只需类**内**坍缩,不需跨类相同 |
| W6 | percolation αk=2k**平凡线性**,无"丰富层级" | seed + P1 | **削弱H5** | 最小模型可能不展示丰富层级→"普适性"判据须在generic类做,而那里恰恰最不收敛(循环困境) |

**撞墙结论**：W1+W2构成命题B的实质威胁,且**集中于GMN度量**;W6揭示方法论困境(丰富层级↔不收敛同处generic类)。无单条反例**证伪**命题A,但联合表明:命题A即便成立,也只对"几何/最小割型"GME度量(负值上界、MI)鲁棒,对GMN这类高阶度量普适性存疑。这迫使声张进一步收窄(见§末)。

---

## §N 推导

### §N-1 replica场论骨架（H3，依据：Jian-You-Vasseur-Ludwig replica构造，领域共识）
MIPT的纠缠/信息量由n-replica场论描述,有效自由度取值于置换群S_n,临界由S_n置换对称**自发破缺**控制(2410.07317确认:replica permutation symmetry+其破缺govern MIPT)。物理量经解析延拓:von Neumann熵 n→1,概率/矩 n→0或q-延拓。
**反驳检验**:若S_n描述失败,则c_eff、ν等不应跨模型一致——但2602.04969 ν=1.34≈4/3、2107.03393区分三类,均与S_n场论的类结构吻合。通过。

### §N-2 k-party配置 → BCC算符关联（H2）
取k个区域A1..Ak,两两间隔L。genuine k-party GME要求**不可约**于任何二分,对应replica场论中实现"k-fold循环链接"置换σ_k的BCC算符 O_{σk} 插在区域边界。
GME_k(L) = ⟨O_{σk}(x1)...O_{σk}(xk)⟩_replica延拓 ~ L^{−αk}。
**依据**:1+1D MIPT的纠缠熵已知由BCC算符维数控制(γ=2h_{a|b},2310.03078);本步将之推广到k-party(seed的1D解析即此类计算)。
**反驳检验**:"genuine"要求关联不可分解为低阶——若O_{σk}可OPE分解为成对算符乘积,则非genuine。S_n中循环置换(k-cycle)的不可约性保证genuine性。通过(形式上)。

### §N-3 αk = 单算符维数？（**最脆弱步**，H2+H4）
设O_{σk}的领头标度维数Δ_k。朴素地 αk = (k个BCC算符的领头融合通道维数)。
- **饱和情形**(percolation):融合无反常,Δ_k=k·Δ_1,得αk=2k(Δ_1=2)。次可加饱和⟺Gaussian/log-CFT。
- **严格情形**(generic):融合通道含低于Σ的反常维数,αk<kΔ_1...(实则Haar Δ_1~4.5,见α2≈9)。
**致命疑点**:不同GME度量(负值N、GMN、multi-entropy)是O_{σk}关联的**不同泛函**。若它们的领头幂由**同一**Δ_k控制→度量无关→A;若不同度量挑出融合通道中**不同**算符(如GMN含高阶replica结构,挑更高维算符)→αk度量依赖→B。
W1/W2正是此疑点的实证投影:GMN(高阶)漂移,MI(二阶,αkMI=k+2稳定)。
**判定**:本步**无法在纯推导内闭合**。命题A当且仅当H4(度量无关)成立。H4是**经验问题**,需P3的判决性数值。→ 开卡点K-S5-1。
**反驳检验已执行**:我主动假设H4为假(命题B),发现与"MI稳定/GMN漂移"完全自洽——故**不能**先验排除B。诚实记录:本Phase无法单凭CFT判A。

### §N-4 次可加=融合/OPE界（依据：算符乘积展开）
Δ_{k+ℓ} ≤ Δ_k + Δ_ℓ 是BCC算符OPE的标准界(融合通道含恒等约化)。饱和⟺仅恒等通道贡献(自由理论);严格⟺存在反常融合(相互作用CFT)。
这给seed三猜想中"subadditivity"一个**CFT机制解释**(增量,非重推数值):次可加性是**通用CFT定理**,故其成立**不能**区分A/B——A/B区别在**饱和与否的具体值**是否由CFT唯一定。
**反驳检验**:monotonicity(αk+1≥αk)对应k-cycle维数随k单增——percolation 2k✅,Haar 9<11<12✅。一致。

### §N-5 Polaris三等价的修正读法（αk / CFT-BCC谱 / 多重分形τ_q）
- **多重分形τ_q**(2107.03393):波函数/关联矩 |·|^{2q} 的标度=q-replica**对称**算符维数Δ(q),连续q→连续谱(generic类)。
- **k-party αk**:k-fold**循环链接**算符维数,整数k索引。
- 二者**同源**于S_n算符内容,但取**不同切片**:τ_q取对称(q-th power)方向,αk取循环链接(k-cycle)方向。
**修正**:Polaris原"三等价"应读作——{αk}、BCC谱、{τ_q}**三者皆可由单一普适非幺正CFT的算符内容导出**(命题A的内涵),**非**数值相等。
**可证伪强化**:命题A ⟺ 存在replica字典使 αk^GME、τ_q、c_eff/h_{a|b} 互相**约束一致**(同一c_eff下)。若generic类测得的τ_q连续谱**无法**与{αk}经字典对账→A被削弱、B加强。

### §N-6 现有证据的A/B记分（综合)
| 证据 | 指向A | 指向B |
|---|---|---|
| percolation αk=2k为CFT解析定理 | **强** | — |
| 三猜想对所有N成立(2602.04969) | 中 | — |
| MI指数αkMI=k+2稳定、跨尺寸一致 | **强** | — |
| ν≈4/3跨模型一致 | 中(类结构) | — |
| GMN α2跨文献9/7.1/6.2分散 | — | **强** |
| GMN"对细节高度敏感" | — | 中 |
| 分形维随p可调(area-law) | — | 弱(离临界) |
| 临界γ≠d(对数修正) | — | 方法警告 |
**净判**:几何/低阶度量(MI、负值上界、percolation解析)**强A**;高阶度量(GMN)在generic类**未决偏B**。

---

## §末 声张对比 + 新增卡点

### 声张对比（§0 → 结论）
| 维度 | §0原声张 | Phase1后修正 |
|---|---|---|
| 域 | 1D最小模型k=2-5 GME普适性 | **收窄**:命题A仅对"几何/最小割型"度量(MI、负值上界)及percolation类**支持**;GMN类generic普适性**未决** |
| 强度 | 判A还是B | **有条件A**+判决性测试未做(K-S5-1) |
| Polaris三等价 | αk=CFT维数=τ_q | **修正**为"三者皆同一CFT算符内容的不同投影",非数值相等 |

### 本Phase结论
**有条件命题A**。MIPT的k-party GME标度层级在percolation最小模型是CFT解析定理(强A),其普适机制(BCC算符维数+OPE融合界)已形式化。但**区分A/B的判决性证据缺失**:(i)αk的度量无关性(H4)从未检验;(ii)独立CFT提取αk与直接GME坍缩比对(P3)无人执行(2602.04969明示开问)。现有最强B-信号(GMN指数跨文献分散40%)集中于单一高阶度量,与有限尺寸混淆,**不足以判B**,但**足以阻止判纯A**。

### 最脆弱步(重申)
§N-3 / H4:αk=单BCC算符维数 ⟺ 度量无关。这是A/B唯一支点,纯推导无法闭合,需数值判决。

### 新增卡点
- **K-S5-1（severity: HIGH，开）判决性度量无关性测试**。协议:1D measurement-only Ising(percolation类,可与αk=2k解析对账)+generic Haar类。对k=2,3,4,5用**至少三种**genuine-k-party GME单调量(对数负值N、GMN、genuine multi-entropy)各自拟合αk^(measure)。判据:三度量αk在误差内一致→H4成立→A;系统分裂→B。**必须用transfer-matrix/边界谱独立提取αk^CFT**(规避W4对数修正),与αk^GME对账(P3)。
- **K-S5-2（severity: MED，开）多重分形对账**。generic类独立测τ_q(q∈[0,3]),经replica字典(§N-5)预测{αk},与直接测GME比对。验证Polaris统一投影。
- **K-S5-3（severity: MED，开）算力执行**。本agent未运行ED/TDVP(诚实记录)。需:percolation类L≤512 stabilizer(Gottesman-Knill,可达大L)+generic类TDVP/ED L≤24,临界点pc(class)处,≥10^3实现平均,steady-state。**注意**:GMN对k≥3在stabilizer需genuine multipartite negativity专用算法(非平凡)。

### 返回PI四问
1. **GATE0**:⚠️**部分先发**(seed层级+三猜想+两后续模型数值已发表;增量限"普适性判决+度量无关性",2602.04969明示此为开问)。无先发冲突。关键文献:2509.12109(seed/禁区)、2602.04969、2511.08690(二者晚于seed)、2107.03393、2310.03078。
2. **本Phase结论**:**有条件命题A**(percolation/低阶度量强A;generic/GMN未决,最强B信号=GMN指数跨文献分散但与有限尺寸混淆)。
3. **最脆弱步**:§N-3/H4——αk=单BCC算符维数⟺度量无关,纯推导不可闭合。
4. **是否开卡点**:**是**,开3个(K-S5-1 HIGH度量无关性判决测试 / K-S5-2 MED多重分形对账 / K-S5-3 MED算力执行)。

---
*A博士 Phase1。框架:CFT/replica场论+(数值协议待执行)。诚实声明:本Phase未运行ED/TDVP,数值为协议规格;结论基于CFT推导+文献交叉核验。*

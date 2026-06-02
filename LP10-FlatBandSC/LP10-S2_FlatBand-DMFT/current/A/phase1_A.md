# LP10-S2 Phase 1 — A博士（正规军）冷启动推导
## 课题：DMFT（含全部局域关联）下，S1几何下界 √det D_s ≥ c·Δ·π|C_tot| 的存活性

---

## ⚡ PI审核入口（最高优先级，先读这里）

- **⚡本Phase结论**：**有边界（bounded survival）**。S1的几何下界在**单点DMFT（single-site DMFT，含全部局域关联、有限温度）**下以**重整化形式** √det D_s ≥ c'·Δ_DMFT·π|C| **存活**，条件四条（见§末裁决表）。命题A在**对称等价Wyckoff**模型（pyrochlore、纯Lieb平带支撑）上胜出；命题B1在**非等价Wyckoff**模型（修饰Lieb、α-T₃、sawtooth）上成立，把系统推入S1反例D扇区，下界退化为 √det D_s ≥ c·min_α(Δ_α)·π|C|。**命题B2（朴素版"局域自能⇒丢几何"）被证伪**；其精炼版（DMFT用裸度规、漏非局域/团簇修正）是真实边界。

- **⚡最脆弱一步**：§N-步7。声称"平均场下界不等式结构（D_s^geom ∝ ∫g → π|C|）逐字搬到DMFT的D_s、仅前因子重整化"——这要求自能Σ(iω)对谱权的重分布**不引入新的k依赖加权**去破坏 metric-Chern 不等式 ∫√det g ≥ π|C|。有限温下相干因子在BZ上非均匀 → 严格不等式可能退化为 √det D_s ≥ c·(min_k 权重)·Δ·π|C|。这正是2603.08791"BZ分布关键"洞见的费米子对应，**我没有完全堵死，标记为门槛条件3**。

- **⚡预测vs实际**：§1预测"局域自能不破坏拓扑标度、只重整c/Δ"——§N实际推导**支持该预测**，但发现朴素B2的失败机制（几何藏在裸流顶点∂h(k)里，不在自能里）比预想更干净；Khurana定理（DMFT横向流顶点修正为零）是关键支柱，§1未预见到要用它。

- **⚡PI需关注问题**：
  1. **先发风险偏高（⚠️部分先发）**：F2(2404.12993)已用DMFT算修饰Lieb平带超流权重+把量子度规当有限T指标；2506.18969已给"严格"超流刚度下界（bootstrap，非DMFT）。我的**增量**=把"下界存活"归因到 Khurana零顶点修正 + Wang-Zhang拓扑哈密顿量 + Wyckoff对称裁决三件套，并明确B2证伪。请PI核实F2是否已显式写出 π|C| 拓扑标度形式的下界（我读到的是"good indicator"措辞，非严格bound）。若F2已写严格bound，本S2降级为复现+边界细化。
  2. 几处 arXiv/卷期号标了"需PI核实"（Wang-Zhang PRX、F2确切页码），不编造。
  3. 是否接受"单点DMFT"作为"含全部局域关联"的操作化定义？非局域关联（团簇DMFT/D-TRILEX）超出本Phase，是门槛条件3的失效区。

---

## §-1 先发文献检索（GATE 0，推导前强制）

**检索环境**：WebSearch（US-only，2026-06；本环境 paper-search-mcp 不可用）。执行四组检索 + 五篇精读。

### 检索命中（真实arXiv号，下载/精读核实）
| 编号 | 文献 | arXiv / 出处 | 方法 | 与本课题关系 |
|------|------|-------------|------|-------------|
| P1 | Penttilä, Huhtinen, Törmä, "Flat-band ratio and quantum metric in SC of modified Lieb lattices" | **2404.12993**, Commun. Phys. **8**, 50 (2025)〔页码需PI核实，文献库记8,19〕 | **DMFT** | ⚠️**最高重叠**：DMFT算修饰Lieb吸引Hubbard的Δ、Tc、D_s、T_BKT；量子度规作有限T**指标**。结论："孤立平带量子几何是有限T超导良好指标"。 |
| P2 | Iskin, "Cooper pairing, flat-band SC & quantum geometry in pyrochlore-Hubbard" | **2403.04270**, PRB **109**, 174508 (2024) | 精确两体谱 + 数值 | 命题A主参照：**显式证四带pyrochlore配对序参量均匀**（Δ_α相等）。 |
| P3 | Jiang & Barlas, "Geometric superfluid weight of composite bands" | **2405.11260**, PRB **109**, 214518 (2024) | 平均场BdG | **S1先发**，复合带下界 √det D_s ≥ cΔπ|C_tot|（本S2验证对象）。 |
| P4 | Huhtinen, Dürrnagel, Peri, Huber, "Interplay of local & global quantum geometry in stability of flat-band superfluids" | **2603.08791** (2026-03) | 玻色 Bogoliubov（超MF含涨落） | ⚠️**B2机制的玻色对应**："积分量子度规不充分，BZ分布关键"；明确指出**玻色情形拓扑下界不成立**，反衬费米子情形拓扑给下界。 |
| P5 | Mojarro & Ulloa, "SC & geometric superfluid weight of tunable flat band system（α-T₃）" | **2512.09901** (2025-12) | 平均场 | 命题B1参照：**三个非等价子格上Δ_α强烈不均匀**（但平均场，非DMFT）。 |
| P6 | "Bootstrapping Flat-band Superconductors / Rigorous lower bounds on superfluid stiffness" | **2506.18969** (2025) | 量子bootstrap（超MF严格） | ⚠️**严格下界先发**：强耦合区超流刚度严格下界（非DMFT，非π|C|拓扑形式）。 |
| P7 | Herzog-Arbeitman et al.（Törmä组）, "Superfluid weight bounds from symmetry & quantum geometry in flat bands" | **2110.14663** | 平均场+对称 | 对称强制的下界（S1背景）。 |
| P8 | Peotta & Törmä, "Superfluidity in topologically nontrivial flat bands" | **1506.02815**, Nat. Commun. **6**, 8944 (2015) | 平均场 | 几何超流权重 + D_s ≥ |C| 原始下界。 |

### 判定（三选一）
**⚠️ 部分先发** —— 理由：
- DMFT 计算平带Hubbard超流权重+量子几何，**已被 P1(2404.12993) 做**（修饰Lieb，含有限T、Δ、D_s、T_BKT）。本S2若仅"用DMFT复现D_s"则**无增量**。
- "超MF严格超流刚度下界"**已被 P6(2506.18969) 做**（bootstrap，但非π|C|拓扑标度，非DMFT解析）。
- "积分度规不足、BZ分布关键"的B2式洞见**已被 P4(2603.08791) 在玻色情形做**，且P4明确说费米子情形拓扑下界**仍成立**——这反而支持命题A。

**本S2尚未被先发的增量（继续推导的合法性）**：
1. 把"S1的**拓扑标度 π|C_tot| 形式**的几何下界在DMFT下存活"显式归因到三机制——(i) **Khurana定理**：单点DMFT横向流顶点修正为零 → 几何由裸顶点∂h(k)携带、不被局域Σ抹掉；(ii) **Wang-Zhang拓扑哈密顿量** h_t=h+Σ(0)：局域Σ(0)不改C除非关隙；(iii) **Wyckoff对称裁决**：等价→均匀Δ（A），非等价→非均匀Δ落S1反例D（B1）。三者组合的解析裁决，文献未见整合。
2. **朴素B2的证伪**（局域自能≠丢几何），文献未明确反驳过这个直觉错误。

→ 差异点充分，**继续推导**（不停交PI），但§末结论须诚实标注P1/P6的先发边界。

---

## §0 声张强度声明（推导前填，不得改）

> **声张（claim）**：**有条件成立**——在**单点DMFT（含全部局域关联、有限温度）**下，S1的几何下界 √det D_s ≥ c·Δ·π|C_tot| 的**存活性**，条件按本任务书：
> (C1) 平带子格 Wyckoff 等价（对称强制均匀 Σ_α、Δ_α）；
> (C2) DMFT能隙保持张开（无关联诱导拓扑相变使Green函数Chern数改变）；
> (C3) 单点（局域）DMFT 充分，非局域/团簇关联可略；
> (C4) 裸 Chern 数 |C|≠0（或受对称保护的 obstructed/Euler 类，且Σ(0)保对称）。
> 满足(C1)-(C4)时下界以重整形式 √det D_s ≥ c'·Δ_DMFT·π|C| 存活（c'=c·Z·(min_k相干权重)）。

**强度自评**：中等-偏强。不是"恒成立"（朴素A），也不是"被关联证伪"（朴素B），而是**给出精确边界**。最可能被攻破处：(C3)的"min_k相干权重>0"在band-touching/非孤立平带处失效。

---

## §0.5 隐含假设清单（每条：来源／适用条件／是否满足）

| # | 假设 | 来源 | 适用条件 | 本课题是否满足 |
|---|------|------|---------|---------------|
| H1 | S1-K1.1：孤立复合平带+均匀配对 Δ̂=ΔÎ_orb ⇒ √det D_s ≥ cΔπ|C_tot|（平均场BdG） | P3 Jiang-Barlas 2405.11260；P8 Peotta-Törmä | 孤立平带、均匀配对、平均场 | 作背景直接引用，**不重推**；S2检验它在DMFT下是否存活 |
| H2 | S1-K1.3：UPC的G-不变靠"单位算符Î_orb"；轨道非等价则失对称保护 | S1 | 平带轨道对称性 | 本Phase§2核心判据 |
| H3 | S1-K1.6/反例D：物理均匀U在非等价Wyckoff（N_A≠N_B局域DOS）给非均匀Δ_α；非Kähler→校准失效 | S1 | 非等价子格 | B1扇区入口 |
| H4 | DMFT定义性近似：自能局域、**动量无关** Σ(k,iω)=Σ(iω)（d→∞精确） | P_RMP Georges et al. RMP 68,13 (1996) | 局域关联主导、非局域弱 | (C3)；band-touching处可疑 |
| H5 | Khurana定理：单点DMFT中由k无关Σ导致的**横向电流顶点修正为零**（∂Σ/∂k=0），光电导/Drude无顶点修正 | Khurana PRL 64, 1990；Georges RMP 1996 §VII | 单点DMFT、横向响应 | 满足（关键支柱，§N-步4） |
| H6 | Wang-Zhang拓扑哈密顿量：有能隙相互作用系统拓扑数 = h_t(k)≡−G(k,iω=0)^{−1} 本征态的Chern数 | Wang & Zhang, PRX 2, 031008 (2012)〔确切号需PI核实〕；Volovik格林函数拓扑 | 有能隙、绝热连通到非相互作用 | (C2)；关隙处失效 |
| H7 | metric-Chern不等式：∫_BZ √det g(k) d²k ≥ π|C|（量子度规-Berry曲率本征不等式 g ≥ |F|/2 的det形式积分） | P8；Roy 2014；Peotta-Törmä | 任意Bloch丛 | 满足（裸丛性质，关联不改） |
| H8 | 序参量自洽 Δ_α = U·T Σ_n F_αα(iω_n)，F=局域反常Green函数 | DMFT-Nambu标准式 | 吸引Hubbard、s波局域配对 | 满足 |

---

## §1 结论预测（推导前的赌注）

预测：**命题A在拓扑标度上胜出，但带边界**。具体赌：
1. 局域自能 Σ_α(iω) **携带轨道指标**（每个非等价子格一个杂质问题），但**不携带动量**。
2. **对称等价**子格（pyrochlore四子格 T_d、纯Lieb平带的B/C子格 C4）⇒ 对称强制 Σ_α、Δ_α 均匀 ⇒ 命题A。**非等价**（修饰Lieb、α-T₃、sawtooth）⇒ 非均匀 Δ_α ⇒ 命题B1。
3. 拓扑标度 π|C| **存活**：局域Σ不改Green函数Chern数（除非关隙）。关联只进 c（经Z）、Δ。
4. 朴素B2（"局域Σ⇒漏几何"）**会被证伪**：几何是流顶点∂h(k)的性质，自能局域不抹掉顶点。

赌注下完，进入撞墙。

---

## §2 强制撞墙（攻击声张命门，找具体反例）

声张的命门 = (C1)-(C4)。逐个找反例：

**撞墙1（攻C1，B1实现）**：修饰Lieb / α-T₃。三子格局域DOS不等（N_A≠N_B≠N_C）→ 即使裸U均匀，DMFT自洽 Δ_α = U·TΣ_n F_αα ∝ 局域配对极化率，子格依赖 → **Δ_A≠Δ_B≠Δ_C**（P5 Mojarro-Ulloa 平均场已显式见到三子格Δ_α强不均匀；DMFT只会更强，因Σ_α(0)进一步劈裂有效轨道能级）。→ 非均匀配对 → S1的Î_orb对称保护失效（H2/H3）→ S1主定理前提失效。**这是真反例，但落在(C1)排除域内**，故声张在C1下不被攻破，只是适用域缩小。

**撞墙2（攻C2，关联诱导拓扑相变）**：强U下 Σ_α(0) 的轨道劈裂可能闭合平带与相邻带的能隙 → Wang-Zhang h_t=h+Σ(0) 的Chern数跳变（C→C'或C→0）→ π|C|标度改变。Mott相变（U>U_c）杀死相干准粒子（Z→0）→ D_s^coherent→0 而下界右端 cΔπ|C| 不一定同步→0。**潜在真反例**：在Mott临界点附近 Z→0 但 Δ_DMFT 有限，则 c'=cZ→0，下界右端坍缩为0，下界变平庸（vacuous）。→ 声张需(C2)排除关隙+(隐含)避开Mott相。**这暴露了c'→0的平庸化风险，记入§末卡点。**

**撞墙3（攻C3，最危险，B2精炼版）**：非孤立平带 / band-touching。平带与色散带在某k₀触碰 → 该处带间几何g(k)发散式增强（P4：BZ分布关键）。单点DMFT用**裸**g(k)、局域Σ无法重整该处几何；但真实非局域关联Σ(k,iω)会在k₀附近显著重整速度顶点 → DMFT的D_s^geom在k₀的加权与真值偏离。更糟：有限T相干因子 tanh(βE_k/2)/E_k 在BZ上非均匀，在平带极小色散处 E_k≈Δ 但在触碰带处 E_k 大 → g(k)的有效加权 w(k) 非均匀 → metric-Chern不等式 ∫w(k)√det g ≥ (min w)·π|C| 只给退化下界。**这是声张最脆弱处，对应⚡最脆弱一步，无法完全堵死，转为门槛条件3。**

**撞墙4（攻C4）**：纯Lieb裸 C=0（M点二次触碰，需flux/SOC才C≠0）。则π|C|=0，下界右端=0，平庸成立但无信息。→ 必须考虑 Lieb+SOC/flux、pyrochlore+SOC 等 C≠0 版本，或S1的C=0三分类（obstructed/Euler）。**这不是反例，是适用前提澄清**，记入(C4)。

撞墙结论：声张在(C1)-(C4)的**交集**上未被攻破；撞墙2、3暴露了平庸化（c'→0）和退化（min_k权重）两个真实门槛，必须写进边界。继续正文推导建立正面论证。

---

## §N 推导正文

### 步1：平带吸引Hubbard的多轨道哈密顿量与Nambu结构
**步骤**：设多子格吸引Hubbard
$$H=\sum_{\mathbf k}\sum_{\alpha\beta\sigma} h_{\alpha\beta}(\mathbf k)\,c^\dagger_{\mathbf k\alpha\sigma}c_{\mathbf k\beta\sigma}-U\sum_{i\alpha}n_{i\alpha\uparrow}n_{i\alpha\downarrow},\quad U>0,$$
α,β=子格/轨道指标，Bloch矩阵 h(k) 的最低本征带为平带 ε_FB(k)=ε_0（k无关）。引入Nambu旋量 Ψ_{kα}=(c_{kα↑},\,c^\dagger_{-kα↓})^T。BdG/Nambu Green函数
$$\hat G(\mathbf k,i\omega_n)^{-1}=i\omega_n\hat 1-\hat H_{\rm BdG}(\mathbf k)-\hat\Sigma(i\omega_n),$$
其中轨道-Nambu自能
$$\hat\Sigma_\alpha(i\omega_n)=\begin{pmatrix}\Sigma_\alpha(i\omega_n)&S_\alpha(i\omega_n)\\ S_\alpha^*(i\omega_n)&-\Sigma_\alpha(-i\omega_n)^*\end{pmatrix},$$
Σ_α=正常自能，S_α=反常（配对）自能（动力学能隙）。

**依据**：标准多轨道Nambu-DMFT（H4,H8；Georges et al. RMP 1996）。
**反驳检验**：此处尚未做任何近似（除写下吸引s波局域U）。非s波/非局域配对超出范围，已在§0.5限定。✓

### 步2：DMFT自洽——自能局域、轨道依赖、动量无关
**步骤**：DMFT把晶格问题映为（每个非等价子格一个）Anderson杂质问题。定义性近似：
$$\boxed{\hat\Sigma_{\alpha\beta}(\mathbf k,i\omega_n)=\delta_{\alpha\beta}\,\hat\Sigma_\alpha(i\omega_n)}\quad\text{（局域：k无关；轨道对角）}.$$
自洽条件：局域Green函数=k求和的晶格Green函数，且等于杂质Green函数
$$\hat G_{{\rm loc},\alpha}(i\omega_n)=\frac1N\sum_{\mathbf k}\big[\hat G(\mathbf k,i\omega_n)\big]_{\alpha\alpha}\stackrel!=\hat G_{{\rm imp},\alpha}(i\omega_n).$$
配对自洽（任务问题1的答案）：
$$\boxed{\Delta_\alpha=U\langle c_{\alpha\downarrow}c_{\alpha\uparrow}\rangle=U\,T\sum_n F_{\alpha\alpha}(i\omega_n)},\quad F_{\alpha\alpha}=\big[\hat G_{{\rm loc},\alpha}\big]_{12}\ (\text{反常分量}).$$

**轨道指标α是否进入Σ？**——**进入**。每个非等价子格有独立的杂化函数 Δ_hyb,α(iω)（局域环境/局域DOS不同），故 Σ_α、S_α、Δ_α **轨道依赖**。但**动量不进入**Σ（这是B2的攻击面，步4处理）。

**依据**：H4；自洽方程为DMFT教科书式（Georges RMP 1996 §III,§VII）。
**反驳检验**：有人或问"Σ能否含轨道非对角 Σ_{αβ}, α≠β？"——单点DMFT中不同子格在不同实空间位点，局域（同一位点）自能对角化于子格基；轨道非对角项需位点间（非局域）关联→属团簇DMFT→(C3)失效区。本Phase限单点，Σ对角。✓

### 步3：Wyckoff对称裁决——哪些模型强制均匀Δ_α（任务问题2）
**步骤**：配对自洽 Δ_α∝F_αα 由局域环境决定 ⇒ Δ_α的均匀性 = 子格的局域环境是否被点群对称联系。判据 = **平带轨道的Wyckoff等价性**（H2）。逐模型：

| 模型 | 维度 | 子格/Wyckoff | 点群联系 | 对称强制Δ_α均匀? | 裸C | 裁决 |
|------|------|-------------|---------|-----------------|-----|------|
| **Pyrochlore** | 3D | 4子格（16d/8b），T_d四面体群 | 四子格互为T_d像 | **是**（全部等价） | ≠0（需SOC） | **A** |
| **纯Lieb** | 2D | A角(1a) + B,C边心(2c/2f)；平带权重**仅在B,C** | C4联系B↔C；A孤立 | **是**（在平带支撑B,C上；A无平带权重不参与） | 0（M点二次触碰，需flux/SOC→C≠0） | **A**（须加SOC使C≠0） |
| **修饰/decorated Lieb** | 2D | 引入非等价装饰，破坏B-C等价 | 无 | **否** | 可调 | **B1** |
| **α-T₃** | 2D | 3非等价子格（on-site不对称） | 无 | **否**（P5：Δ_α强不均匀） | 可调 | **B1** |
| **Sawtooth** | 1D | apex+base 非等价 | 无 | **否** | n/a（1D无Chern） | **B1**（但1D无π|C|下界，仅作B1解析玩具） |

**pyrochlore的均匀性**与 P2 Iskin 2403.04270 精确结果"四带配对序参量均匀"**独立一致**（交叉验证✓）。**α-T₃非均匀**与 P5 Mojarro-Ulloa 2512.09901 平均场三子格Δ_α强依赖α**一致**（DMFT只会经Σ_α(0)劈裂更强）。

**依据**：群论（位置算符在Wyckoff轨道上的表示）+ H2 + P2/P5交叉验证。
**反驳检验**：纯Lieb的A子格虽Wyckoff不等价于B,C，是否破坏均匀？——平带Bloch态在A上**零权重**（紧束缚平带本征矢），故平带投影的配对只感受B,C，而B,C被C4联系等价 → 平带支撑上Δ均匀。但**带间几何**（步5）涉及A↔B,C跃迁矩阵元，A的Δ_A≠Δ_B**会**影响几何贡献的细节——这是非孤立耦合修正，归入(C3)。✓（部分，标记）

### 步4：关键裁决——DMFT是否捕获几何贡献（任务问题3，命题B2正面处理）
**步骤**：超流权重由 phase-twist 下自由能二阶导（=电流-电流关联）给出
$$D_{s,\mu\nu}=\frac1V\Big[\langle -K_{\mu\nu}\rangle-\Lambda_{\mu\nu}(\mathbf q\to0,i\omega=0)\Big],$$
顺磁关联 Λ 与抗磁项 K 都用**裸流顶点** $j_\mu=\sum_{\mathbf k}\sum_{\alpha\beta}(\partial_\mu h_{\alpha\beta}(\mathbf k))\,c^\dagger_\alpha c_\beta$ 构造。

**核心论证（B2朴素版的证伪）**：几何贡献 D_s^geom∝∫g(k) 的来源是流顶点里的 **∂_μh(k)** 的**带间（轨道非对角）矩阵元**——这是动量空间、多带量，**藏在顶点里，不在自能里**。DMFT把Σ做成局域(k无关)，**不触碰** ∂_μh(k)。在保守(Baym-Kadanoff)框架，流顶点须被顶点修正Γ_μ缀饰满足Ward恒等式；而单点DMFT的顶点修正
$$\delta\Gamma_\mu\propto\frac{\partial\Sigma(i\omega)}{\partial k_\mu}=0\quad(\text{Σ与k无关})$$
——**Khurana定理**（H5）：横向电流响应的顶点修正在单点DMFT中**恒为零**。故
$$\boxed{D_{s,\mu\nu}^{\rm geom,DMFT}=\frac{e^2}{\hbar^2}T\sum_n\frac1N\sum_{\mathbf k}\mathrm{Tr}\big[\partial_\mu h(\mathbf k)\,\hat G(\mathbf k,i\omega_n)\,\partial_\nu h(\mathbf k)\,\hat G(\mathbf k,i\omega_n)\big]_{\rm inter\text{-}band}}$$
**裸顶点 ∂h(k)** × **缀饰传播子** Ĝ(含局域Σ)。几何**未被抹掉**，B2朴素版**证伪**。

自能的作用 = 重整三件：(i) 准粒子权重 $Z=[1-\partial_\omega\Sigma|_0]^{-1}$；(ii) 有效能隙 $\Delta_{\rm eff}=Z\,S(0)$（反常自能）；(iii) 有效轨道能级 $\varepsilon_\alpha\to\varepsilon_\alpha+\mathrm{Re}\Sigma_\alpha(0)$。平带投影后
$$D_s^{\rm geom,DMFT}\;\approx\;c\,Z\,\Delta_{\rm DMFT}\int_{\rm BZ}\!w(\mathbf k)\,g_{\mu\nu}^{\rm bare}(\mathbf k)\,\frac{d^2k}{(2\pi)^2},$$
$w(k)$=有限T相干加权（含 tanh(βE_k/2)/E_k 与Z）。

**精炼B2（真实边界）**：DMFT用**裸度规** $g^{\rm bare}(k)$，**不重整几何本身**。真实非局域关联 Σ(k,iω) 会重整速度顶点 → 单点DMFT在 band-touching/非孤立平带处偏离真值（撞墙3）。故DMFT**不是系统性低估**几何（朴素B2错），而是**用裸几何+局域谱重整**——在(C3)满足时这是好近似，在(C3)失效时偏离。

**依据**：H5（Khurana）+ 线性响应 + 平带投影。
**反驳检验**：质疑"抗磁项K是否也无修正"——K=⟨∂²h⟩，二阶导顶点同样裸（局域Σ不产生∂²Σ/∂k²）。✓ 质疑"反常顶点S_α(iω)的频率依赖是否破坏积分"——S_α(iω)进入Ĝ的反常分量，在Matsubara求和后给Δ_eff=Z·S(0)的重整，不改∂h(k)的k结构。✓

### 步5：混合态拓扑——Wang-Zhang/Volovik不变量是否仍量子化为C（任务问题4）
**步骤**：相互作用系统的拓扑数由Green函数给出。Wang-Zhang（H6）：有能隙系统的Chern数 = **拓扑哈密顿量**
$$h_t(\mathbf k)\equiv-\hat G(\mathbf k,i\omega=0)^{-1}=h(\mathbf k)+\Sigma(i\omega=0)$$
的占据本征态的Chern数。DMFT中 Σ(0)=diag(Σ_α(0)) **k无关**：
$$h_t(\mathbf k)=h(\mathbf k)+\mathrm{diag}(\mathrm{Re}\Sigma_\alpha(0)).$$
- **对称等价子格**（C1）：Σ_α(0)全相等 ⇒ h_t(k)=h(k)+const·Î ⇒ **本征矢与h(k)完全相同** ⇒ **C不变**。拓扑标度 π|C| **精确存活**，关联只进 c(经Z)、Δ。
- **非等价子格**：Σ_α(0)劈裂轨道能级 ⇒ 形变能带；若劈裂未关隙 → C仍量子化（同伦不变）；若强U关隙（撞墙2）→ **关联诱导拓扑相变**，C→C'，下界标度改变（**(C2)失效边界**）。

**依据**：H6（Wang-Zhang PRX 2,031008，号需PI核实）+ Volovik格林函数缠绕数。
**反驳检验**：Wang-Zhang要求 h_t 有能隙且G(iω=0)无零点/极点病态；Mott相G(0)发散（Luttinger surface）→ h_t病态，拓扑分类需Volovik N₃缠绕数推广。Mott区超出(C2)，标记。✓ C=0模型（纯Lieb）→π|C|=0下界平庸，须C≠0版本或S1的obstructed/Euler类（H7的Euler数推广），且Σ(0)须保护对称（等价子格自动满足）。✓

### 步6：组装——重整化下界
**步骤**：合并步4(几何存活+裸度规)+步5(C量子化)+H7(metric-Chern):
$$\sqrt{\det D_s^{\rm DMFT}}\;\ge\;c\,Z\,(\min_{\mathbf k}w_{\rm norm}(\mathbf k))\,\Delta_{\rm DMFT}\int_{\rm BZ}\sqrt{\det g^{\rm bare}}\;\ge\;\underbrace{c\,Z\,(\min_{\mathbf k}w_{\rm norm})}_{\equiv\,c'}\,\Delta_{\rm DMFT}\,\pi|C|.$$
$$\boxed{\sqrt{\det D_s^{\rm DMFT}}\ \ge\ c'\,\Delta_{\rm DMFT}\,\pi|C_{\rm tot}|,\qquad c'=c\,Z\,\min_{\mathbf k}w_{\rm norm}(\mathbf k)>0\ \text{当(C1)-(C4)成立}}$$
**依据**：步4(D_s^geom形式)+H7(∫√det g≥π|C|)+步5(C量子化)。
**反驳检验**：不等式右端用 min_k w 是为把BZ非均匀加权下放成均匀常数——这是把"BZ分布"问题(P4)显式承认进 c' 的代价。若 min_k w_norm→0（band-touching处相干权重塌陷）则 c'→0，下界平庸。**这就是⚡最脆弱一步**，明确写出，不藏。✓

### 步7（最脆弱，正面标注）：平均场不等式结构搬到DMFT的合法性
**步骤**：H1/H7的 metric-Chern 不等式 ∫√det g ≥ π|C| 是**裸Bloch丛**的本征性质，关联不改 g^bare 与 C（步4,5已立）。**搬运的唯一缺口** = 步6里 D_s^geom 对 g(k) 的**加权** w(k) 是否处处≥正常数。
- 若平带孤立、低T：E_k≈Δ 近均匀 → w(k)≈const → 不等式紧，下界=cZΔπ|C|，命题A**干净胜出**。
- 若非孤立/band-touching/高T：w(k)在BZ非均匀，min_k w 可→0 → 退化下界。
**结论**：搬运合法**当且仅当** min_k w_norm 有正下界，即(C3)+(平带孤立度)。这是诚实的最脆弱环，**未完全堵死**，作为门槛条件3移交Phase 2/3数值检验（P1 2404.12993 的有限T D_s数据可校准 w(k)）。
**依据**：H7+步6。**反驳检验**：见上，已承认退化风险。✓

---

## §末 声张对比 + 预测vs实际 + 新增卡点

### 裁决表（精确边界）
| 命题 | 条件 | 裁决 |
|------|------|------|
| **A**（下界存活，重整c,Δ） | (C1)等价Wyckoff ∧ (C2)能隙开 ∧ (C3)单点DMFT充分 ∧ (C4)C≠0 | ✅ **成立**：√det D_s^DMFT ≥ c'Δ_DMFT π|C|，c'=cZ·min_k w>0。代表：pyrochlore+SOC、纯Lieb+SOC（B,C等价支撑） |
| **B1**（非均匀Δ_α→落S1反例D） | ¬(C1) 非等价Wyckoff | ✅ **成立**：DMFT自洽给Δ_α不均匀（Σ_α(0)劈裂强化平均场效应），S1主定理前提失效，下界退化为 √det D_s ≥ c·min_α(Δ_α)·π|C|（接S1-K1.6夹逼下界）。代表：修饰Lieb、α-T₃、sawtooth |
| **B2朴素**（局域Σ⇒丢几何） | —— | ❌ **证伪**：几何在裸流顶点∂h(k)，Khurana定理保横向顶点零修正，DMFT不抹几何 |
| **B2精炼**（DMFT用裸度规、漏非局域修正） | ¬(C3) band-touching/非孤立 | ⚠️ **真实边界**：单点DMFT用g^bare，非局域关联Σ(k,iω)重整几何被漏；min_k w→0时下界平庸 |

**总裁决：有边界（bounded）**。S1几何下界在单点DMFT下以重整形式存活于(C1)-(C4)交集；命题A胜出于对称等价模型，B1占据非等价扇区，朴素B2证伪、精炼B2界定失效区。

### 预测vs实际
| §1预测 | §N实际 | 一致? |
|--------|--------|------|
| Σ_α携带轨道指标、不携带动量 | 步2确认 | ✅ |
| 等价Wyckoff→均匀Δ→A；非等价→B1 | 步3裁决表+P2/P5交叉验证 | ✅ |
| π|C|标度存活（除非关隙） | 步5 Wang-Zhang h_t=h+Σ(0)确认 | ✅ |
| 朴素B2被证伪 | 步4 Khulana定理确认，机制比预想更干净（几何在顶点） | ✅（且更强） |
| （未预见）需用Khurana零顶点修正作支柱 | 步4 | ⚠️ §1未预见的关键引理 |

### 新增卡点（移交Phase 2/3 / PI）
1. **c'→0平庸化**（撞墙2,3）：Mott临界 Z→0 或 band-touching min_k w→0 时下界右端坍缩，需Phase 3用P1(2404.12993)有限T D_s数据定量校准 w(k) 与 Z(T)。
2. **关联诱导拓扑相变边界**（C2）：Σ_α(0)劈裂关隙的临界U_c，需Phase 2算 h_t=h+Σ(0) 的Chern数随U的跳变。
3. **非局域关联**（C3）：单点DMFT在非孤立平带失效，团簇DMFT/D-TRILEX的顶点修正∂Σ/∂k≠0会重整几何——超出本Phase，是B2精炼版的真正战场。
4. **先发核实（PI）**：F2/P1(2404.12993)是否已显式写出 π|C| 拓扑标度形式的严格下界（非"indicator"）？P6(2506.18969)的bootstrap严格下界与本DMFT下界的关系？Wang-Zhang确切arXiv/PRX号、F2确切页码 — 需PI核实，未编造。
5. **C=0模型**（C4）：纯Lieb裸C=0落S1三分类，需obstructed/Euler类下界（H7的Euler推广），DMFT经等价子格Σ(0)保对称→obstruction存活，但需S1的C=0分支结论支撑。

---

## Sources（§-1检索用到的真实链接）
- P1: https://arxiv.org/abs/2404.12993 （Penttilä-Huhtinen-Törmä, modified Lieb DMFT）
- P2: https://arxiv.org/abs/2403.04270 （Iskin, pyrochlore-Hubbard, PRB 109,174508）
- P3: https://arxiv.org/abs/2405.11260 （Jiang-Barlas, composite bands, PRB 109,214518）
- P4: https://arxiv.org/html/2603.08791v1 （Huhtinen-Dürrnagel-Peri-Huber, local vs global geometry）
- P5: https://arxiv.org/abs/2512.09901 （Mojarro-Ulloa, α-T₃ geometric SW）
- P6: https://arxiv.org/abs/2506.18969 （Bootstrapping flat-band SC, rigorous stiffness bounds）
- P7: https://arxiv.org/abs/2110.14663 （Herzog-Arbeitman/Törmä, symmetry+geometry bounds）
- P8: https://ar5iv.labs.arxiv.org/html/1506.02815 （Peotta-Törmä, D_s≥|C|原始下界）

# LP9-S1 Phase 1 推导作业（A博士 / 正规军）

**子命题 LP9-S1：** 强希尔伯特空间碎片化(strong HSF)保护的离散时间晶体(HSF-DTC)，在热力学极限下是真正非平衡相（真相），还是预热瞬态/初态依赖的scar-like现象（赝象）？

**框架（本Phase规定，不更换）：** 群论 / commutant代数（von Neumann双交换子）+ 微扰论 / Fermi黄金规则(FGR)。

---

## 先发检索栏（GATE 0 结论摘要）

完整检索见 `plan/文献库.md`。判定：**⚠️ 部分先发**。

- 直接对象 **Tang, Li, Z.D. Wang, D.-W. Zhang, arXiv:2512.14182**（v1 2025-12-16 / v2 2026-05-07，kicked XXZ链）提出了"强HSF稳定DTC"的**机制**，但：(i) 仅具体XXZ模型；(ii) 有限尺寸数值 + 寿命∝exp(L)的finite-size scaling；(iii) 自述守恒为"**近似**守恒"（磁化、畴壁数）。**未**用commutant代数给热力学极限稳定性判据，**未**显式判别真相/瞬态，**未**对破坏HSF约束的一般局域微扰做FGR寿命估计。
- 本课题增量明确：把判别提升为 commutant代数 + 算符值域依赖性 的一般性论证，并给出 exp(L) 寿命应被读作"有限尺寸/微调"信号的物理论证。
- 旁证：arXiv:2605.18119 直接报告"weak HSF 并不阻止量子混沌或热化"，支持碎片化保护非鲁棒。
- 工具根基：Moudgalya-Motrunich, arXiv:2108.10324（commutant定义HSF；强HSF ⟺ dim C ~ exp(L)）。

未发现已在commutant框架下完成"真相/瞬态"判别的直接竞争者，继续推导。

---

## 【PI审核入口】

⚡**本Phase结论：** HSF-DTC作为"热力学极限下、对一般局域微扰鲁棒、对generic初态成立"的真非平衡相 **不成立**——它是预热/微调现象（**命题B方向**）；仅在 fine-tuned 点(λ=0)+frozen/special初态下存在**精确**次谐波（弱意义"真实"，但本质scar-like/初态依赖）。命题A的两条代数premise(i)(ii)在λ=0**确实成立且被精确实现**，但A从"premise在λ=0成立"跳到"无τ_pre天花板→真相"的推理无效：premise仅在测度零的微调流形上成立，commutant在λ≠0坍缩。

⚡**最脆弱的一步：** §N步5的FGR率标度——断言破坏约束的微扰给出**intensive（与L无关）**的序参量衰减率 Γ~λ²。它依赖"碎片化系统中破坏约束算符V的跨Krylov块矩阵元服从Krylov-ETH式标度"，这一点对fragmented系统只是conjecture而非定理（见卡点1）。若该矩阵元反常地随L指数压低，则τ可随L增长，B的强结论会被削弱为"无法判别"。

⚡**预测vs实际：** 推导前预测B方向、τ~1/λ²（L无关天花板）；实际推导得到一致结论。**一个意外**：命题A的premise(ii) "D_max/D_tot→0" 经正确解读后**反而支持B**（generic初态对frozen子空间的overlap~2^{-L}指数小→无局域DTC信号），即A把对自己有利的条件用反了。

⚡**PI需要关注的问题：**
1. 卡点1的FGR矩阵元标度未被严格证明，是B强结论的命门。建议Phase2用具体模型(t-Jz或偶极spin-1)数值验证 Γ 是否intensive。
2. SLIOM（statistically localized integrals of motion）是否有perturbatively-stable子集？若有，可能残存一个**更弱**的DTC，需排查（卡点3）。
3. 命题A的最强steelman——"HSF约束当作protecting symmetry，则HSF-DTC是约束系综内的SPT-like相"——我在§2给了反驳（约束非fundamental group对称），但此反驳依赖"偶极/pattern守恒不可精确强制"的物理判断，PI应复核是否接受。

---

## §0 声张强度声明（推导前填，事后不改）

本Phase目标结论的声张强度：**有条件成立，条件是：**

> "HSF-DTC 不是热力学极限下的鲁棒真非平衡相（即命题B方向成立）"——条件为：(a) 判据采用"对**一般**局域微扰鲁棒 + 热力学极限 L→∞ + **generic**初态"三要件；(b) 所考虑模型的HSF约束是哈密顿量H的精确（fine-tuned）性质，而非来自fundamental gauge对称的守恒律。在排除上述条件后的 fine-tuned点(λ=0) + frozen/special初态 子情形下，存在**精确**次谐波响应（此为弱意义"真实"，不与主结论冲突）。

（声明锁定。推导中若发现新条件，只能开卡点，不得追加到此处削弱声张。）

---

## §0.5 隐含假设清单

| # | 引用结论 | 来源 | 适用条件 | 当前是否满足 |
|---|---------|------|---------|------------|
| H1 | commutant代数定义HSF；强HSF ⟺ dim C 随L指数增长 | Moudgalya-Motrunich arXiv:2108.10324 | 有限维局域*-代数；finite L后取标度 | ✅ 满足（t-Jz/偶极模型为标准例） |
| H2 | 双交换子定理 A''=A；H=⊕(M_{d_λ}⊗I_{m_λ}) Wedderburn分解 | von Neumann / Artin-Wedderburn | 有限维含1的*-代数 | ✅ 满足 |
| H3 | Krylov-restricted ETH：大Krylov块内部热化 | Moudgalya et al (编号未经本次搜索确认) | 块维数大、块内无额外结构 | ⚠️ 对大块满足；对frozen/小块不适用（正是关键） |
| H4 | FGR连接率 Γ=2π λ²Σ_f|⟨f|V|i⟩|²δ(E_f−E_i) | 标准微扰论 | λ小、目标谱稠密、Markov(无早期recurrence) | ⚠️ 稠密性满足；矩阵元标度=卡点1 |
| H5 | 高频Floquet预热定理 τ_heat~exp(cω/J) | Abanin-De Roeck-Ho-Huveneers (编号未经本次搜索确认) | 高频、局域有界H | ✅ 作为第二道天花板引用 |
| H6 | MBL l-bit 对小局域微扰**鲁棒**（相有有限外延） | Imbrie (编号未经本次搜索确认) | 1D强无序 | 仅作**对照**使用（非本系统premise） |
| H7 | 强碎片化 D_max/D_tot→0（指数）；frozen态数指数增多 | Sala et al / Khemani et al (编号未经本次搜索确认) | 偶极守恒/pattern约束模型 | ✅ 模型已知性质 |

---

## §1 结论预测（推导前）

- **方向：** 命题B（赝象/预热）。HSF的守恒量虽指数多，但是H的**精确性质**而非鲁棒涌现性质；一般局域微扰使commutant坍缩。
- **量级：** 序参量寿命 τ ~ 1/λ²（约束违反强度λ），**与L无关**，热力学极限有限。第二道天花板 τ~exp(cω/J)（驱动加热）。Tang-Li的exp(L)是λ=0清洁点/有限尺寸效应，被任意λ>0在大L时压过：τ~min(exp(cL),1/λ²)→1/λ²。
- **最可能出错的步骤：** (a) FGR率的intensive性（卡点1）；(b) 把Tang-Li的exp(L)归因为有限尺寸而非真相——若其exp(L)源于某种鲁棒拓扑保护则预测错。

---

## §2 强制撞墙（攻击我自己的B结论，即steelman命题A）

我倾向B，故必须攻击"HSF-DTC是赝象"这一声张所依赖的假设。最强反例如下。

**反例（steelman A）：** "HSF约束应被当作 **protecting symmetry**。正如拓扑相只在给定保护对称性时才是相，HSF-DTC在**保持约束的微扰系综**内是一个真正的相：限制V只取保约束项（如保偶极的关联跳跃），则commutant稳定、Z₂半直积结构鲁棒、次谐波刚性永恒。因此在'约束类'内它是真相，正如SPT在其对称类内是真相。"

这是真正有力的反对，不是弱反例（它直击我声张的核心假设——"判据要求对*一般*微扰鲁棒"）。

**反例为何不成立（反驳）：**
1. **保护结构的代数类型不同。** SPT的保护对称性是一个**群**（有限群或李群的幺正表示）——闭合、鲁棒、可在实验中精确强制（如U(1)电荷来自规范对称，是fundamental守恒律）。HSF约束**不是**群对称：它等价于"H中某些项被精确调到零"（pattern守恒/偶极守恒），或等价地一个**非群**的巨大算符代数。两者在稳定性上有本质区别。
2. **偶极/pattern守恒不可精确强制。** 偶极矩 P=Σ_j j·n_j 仅当H恰好取特定形式时守恒；没有fundamental守恒律强制它（不像电荷U(1)来自规范不变性）。任何杂散场梯度、长程跳跃即破坏之。故"约束类"本身在物理上不是一个鲁棒类——它是测度零的调参流形。
3. **退到真正fundamental的对称(U(1)电荷)不够。** 若只强制U(1)（可精确强制），则被保护的次谐波退化为"π脉冲翻转一个守恒磁化 ⟨S^z_tot(nT)⟩=(−1)^n⟨S^z_tot⟩"——这是**任何**U(1)对称模型(含完全热化模型)都有的trivial响应，**不依赖HSF**，且任何保U(1)但破坏pattern守恒的微扰会令局域序热化。HSF-specific的刚性需要**完整pattern守恒**，而那是fine-tuned的。
4. 故steelman失败：HSF不是鲁棒protecting symmetry而是fine-tuning。"约束类内为真相"在物理上等于"测度零流形上为真相"，与"热力学极限鲁棒相"判据相悖 → 维持B。

**附：另一常见"救A"的反例及反驳（frozen态）。** "取frozen态(如某模型中Néel态)，U_F每周期精确翻转、永恒振荡，岂非完美DTC？"——反驳：(a) 单个product态、初态特异（scar-like），相必须对generic/有限比例初态成立；(b) frozen态仅在λ=0是本征态，generic λV令其以率λ²退相；(c) 即便λ=0，单product态永恒振荡是trivial(单自旋Rabi)极限，非多体相。此"反例"恰恰例示了scar-like/初态依赖 → 支持B。

---

## §N 推导正文

### 步骤1：选定具体Floquet强HSF模型

**模型（t-Jz链 + 全局π脉冲）。** 取无双占据的自旋-1/2费米子链（Gutzwiller投影P禁双占），

H_HSF = −t Σ_j P( c†_{j,σ} c_{j+1,σ} + h.c. )P  +  J_z Σ_j S^z_j S^z_{j+1}.

Floquet驱动一个周期 T：

U_F = X · exp(−i H_HSF T),  其中 X = exp(−i (π/2) Σ_j X_j) = (−i)^L ∏_j σ^x_j （理想π脉冲/全局自旋翻转）。

**约束/守恒（t-Jz的HSF）：** 受限跳跃移动粒子位置但**保持占据位上自旋的有序序列（spin pattern）不变**。例：构型(空格用·) `↑·↓↑` 跳跃后仍读出pattern `↑↓↑`。每个不同pattern + 粒子数 标定一个动力学不连通的Krylov块。

**依据：** t-Jz是commutant框架下的标准强HSF例（Moudgalya-Motrunich H1）。pattern数随L指数增长。

**反驳检验：** 易质疑"t-Jz是否强HSF而非弱"。t-Jz的Krylov块数（=center(C)维数）随L指数增长且 D_max/D_tot→0，属强碎片化（H7）；非弱碎片化（弱碎片化中D_max/D_tot→const>0）。当前选模型满足强HSF前提。

### 步骤2：求commutant C 及其标度

局域键代数 A = ⟨{h_{j,j+1}}⟩（h为上面H_HSF的局域项）。commutant

C = A' = { O : [O, h_{j,j+1}]=0, ∀j }.

由双交换子定理(H2)，A''=A，且 H = ⊕_λ (M_{d_λ}⊗I_{m_λ})（Wedderburn）。Krylov块 ↔ λ标号；每块由pattern K标定。center Z(C)=span{P_K}（块投影子），dim Z(C)=#Krylov块。

**标度：** #Krylov块(K) ~ exp(s·L)（s>0，pattern组合熵），故

dim C = Σ_λ m_λ² ≥ #块 ~ exp(s L)  →  **强HSF（指数增长）**。✓ 命题A premise的"指数增长"在此精确成立。

**守恒量性质判定：** Z(C)的生成元P_K是**全局pattern投影子**（高度非局域），不是l-bit式局域守恒量。粗粒化函数总S^z_tot=Σ_j S^z_j（pattern的函数）守恒。故HSF守恒量 = {全局(总S^z、粒子数)} ∪ {非局域pattern投影/SLIOM}，**无**类l-bit的局域守恒量。这一点是后文判别的关键。

**依据：** H1, H2；Wedderburn分解。

**反驳检验：** 易质疑"dim C指数增长是否等同强HSF（而非简单对称性如U(1)的多重简并）"。Moudgalya-Motrunich判据(H1)正是用 dim C 的**指数 vs 多项式**标度区分HSF与常规对称：常规对称(U(1)、平移)给多项式增长，pattern碎片化给指数增长。当前为指数 → 真HSF，非伪装的常规对称。

### 步骤3：驱动对Krylov块的作用 —— Z₂半直积，刚性来源

考察X如何作用于center。X=∏σ^x_j 翻转每个物理自旋(↑↔↓)，把pattern K映到其**补pattern K̄**（逐位取反）。这是pattern集合上的对合双射。故

X P_K X† = P_{K̄}.

于是 {P_K}（abelian）与 Z₂=⟨X⟩（按 K↔K̄ 作用）生成

**结构：Z(C) ⋊ Z₂**（abelian代数 半直积 Z₂）。✓ **命题A premise(i) 精确成立。**

**次谐波刚性来源（严格）。** U_F=X e^{−iHT}。算符O被U_F守恒 ⟺ U_F O U_F†=O。对O∈Z(C)（[O,H]=0 ⇒ e^{−iHT}O e^{iHT}=O）：

U_F O U_F† = X O X†.

- X-偶组合 O^+_K = P_K + P_{K̄}：U_F O^+_K U_F† = O^+_K（守恒，周期T）。
- X-奇组合 O^−_K = P_K − P_{K̄}：U_F O^−_K U_F† = X(P_K−P_{K̄})X† = P_{K̄}−P_K = **−O^−_K**。

故 ⟨O^−_K(nT)⟩ = (−1)^n ⟨O^−_K(0)⟩：**精确period-2T次谐波**，刚性来自精确守恒量(P_K)与精确Z₂(X)。**在λ=0这是真实的、无τ_pre天花板的次谐波。** 命题A在清洁点胜出——但见步骤5。

**[π脉冲, commutant生成元]对易关系（题目要求严格分析）：** [X, P_K] = X P_K − P_K X = (P_{K̄}−P_K)X ≠ 0（除非K=K̄）。即X与pattern投影子**不对易**，而是按对合**配对**。这正是Z₂配对（非自映射、非混合）：X把块K整体映到同维块K̄，**不在块内/跨无关块混合**。这是DTC刚性的代数核心，也是命题A(i)成立的精确陈述。

**依据：** 步骤2的Wedderburn结构 + X对center的对合作用；直接代数计算。

**反驳检验：** 易质疑"O^−_K是否局域可观测——experimental DTC测局域⟨σ^z_j⟩"。**关键**：O^−_K=P_K−P_{K̄}是**全局pattern投影子**，高度非局域。局域⟨σ^z_j⟩在t-Jz中**不**单独守恒（粒子跳跃），仅当态frozen(位置冻结)时局域磁化才守恒。故HSF-specific的**局域**次谐波只存在于frozen态——埋下scar-like伏笔（步骤4、5展开）。这一反驳检验**未被清洁点的刚性消除**，反而指向B。

### 步骤4：最大块标度 D_max/D_total 及其对genericity的真实含义

强碎片化(t-Jz/偶极spin-1)的已知结果(H7)：

D_max(L)/D_total(L) → 0  指数地（最大Krylov块占总维数的比例指数小）；同时frozen(1维)块数指数多。

命题A premise(ii)成立。**但A对其含义的解读用反了。** 正确推论：

- generic初态(Haar随机/随机product)在各块上的权重 ~ (块维/总维)。它落在frozen块的总overlap ~ (#frozen块)×2^{−L} 量级，对随机product态**指数小**（frozen块虽指数多，单块维=1，权重各~2^{−L}；而大热化块虽单个占比指数小，但"中等大小块"集合占据measure主体）。
- 故generic态的**局域**DTC信号(来自frozen/小块的贡献) ~ 指数小 → **generic初态无局域时间晶体序**；仅fine-tuned(frozen/特定pattern)初态显示。
- 这正是 **初态依赖 / scar-like** 的定量表述。

**结论：** premise(ii) "D_max/D_tot→0" 经正确解读后**支持命题B**（初态依赖），不支持A。A误以为"块都小→都frozen-like→都刚性"，实则"块小但generic态散布于热化块、对frozen块overlap指数小"。

**依据：** H7（强碎片化标度）+ 随机态在块上的权重计数 + H3（大块Krylov-ETH→块内热化、局域序衰减）。

**反驳检验：** 易质疑"是否存在一个有限比例的初态集合显示DTC"。frozen块总维 D_frozen=Σ_{frozen}1=#frozen块。若 D_frozen/D_total→const>0，则有限比例初态可显示DTC（弱化B）。但已知强碎片化中 D_frozen/D_total→0（frozen态熵密度 < 总熵密度，Sala et al H7）→ 仍指数小 → 维持"初态依赖"。该比例的精确标度依模型，列为定量化方向（不改变定性结论）。

### 步骤5：扰动稳定性 —— commutant坍缩、FGR、τ_pre天花板（判别核心）

DTC**作为相**要求次谐波对U_F的generic小扰动鲁棒。两条扰动通道：

**通道(a) 不完美π脉冲：** X → exp(−i(π/2−ε)Σ_j X_j) = e^{+iε Σ_j X_j}·X。额外转动 e^{iεΣX_j} 含单自旋翻转σ^x_j；σ^x_j翻转占据位j的自旋 → 把pattern K变到**不同**pattern K' → **直接连接不同Krylov块**。对commutant：[Σ_j X_j, P_K]≠0，单点翻转将振幅每周期以 ~ε² 概率泄漏出{P_K,P_{K̄}}对到邻近块。n周期累积衰减 ~ exp(−c ε² n) → **寿命 τ ~ 1/ε² 周期（有限）**。

> 对照MBL-DTC：脉冲误差被**谱配对刚性**吸收——MBL本征态为局域cat态 |ψ⟩±X|ψ⟩，π-paired quasienergy受局域化拓扑保护，ε只dressing本征态、不能unpair（除非穿过相变）。其保护是**稳定RG不动点**(H6 Imbrie)。HSF**无**此机制：大块内态由Krylov-ETH是热化的(H3)，ε误差不被吸收为刚性局域结构，而引发真实跨/内块跃迁 → 无刚性 → 有限τ。

**通道(b) 破坏约束的H项：** H_HSF → H_HSF + λV，V为不在A中的generic局域算符(如非受限跳跃、场)。[V,P_K]≠0 → V连接块。commutant坍缩：

C(H_HSF+λV) = {与H_HSF+λV对易的全部算符} —— 对generic V**坍缩到平凡对称**(仅U(1)、平移)，dim从exp(sL)掉到poly(L)。

**FGR连接率：**

Γ = 2π λ² Σ_f |⟨f|V|i⟩|² δ(E_f − E_i).

序参量(系于守恒pattern)是**局域弱破坏积分**型可观测。按弱破坏可积性/memory-matrix标准论证，其弛豫率

**Γ ~ λ² × (局域态密度) = intensive，与L无关。**

故 **τ ~ 1/Γ ~ 1/λ²（有限，L无关）**。

**判别（题目(a) vs (b)）：** commutant在λ≠0**不是**U_F的精确对称(它坍缩) → 不是结构性永恒 → 落入(a)：存在天花板，序最终衰减 → **赝象（预热）**。综合两道天花板与清洁点效应：

**τ ~ min( exp(cω/J),  1/(λ²+ε²),  exp(c'L) ).**

热力学极限 L→∞、固定 λ,ε>0、固定ω：exp(c'L)→∞ 被压过，τ → min(exp(cω/J), 1/(λ²+ε²)) = **有限**。

**与Tang-Li(arXiv:2512.14182) exp(L) 的调和：** 其报告寿命∝exp(L)且守恒为"近似"。在预热读法下：exp(L)是**λ=0清洁点/有限尺寸**信号(清洁点泄漏为高阶/边界过程，率~exp(−c'L))；一旦加generic局域λV，τ~1/λ² 在 L > (1/c')ln(1/λ²) 时压过exp(c'L)。故L→∞固定λ>0时寿命**饱和到有限值1/λ²** → 赝象。这正是Tang-Li未做的判别，构成本课题增量。

**关键回答（题目"现实模型中HSF约束是Hamiltonian精确性质还是仅近似？"）：** 是**H的精确(fine-tuned)性质**——pattern/偶极守恒来自把特定项调到零，无fundamental守恒律强制(§2步3已论)。这与MBL l-bit的**微扰稳定性**(H6)本质不同。故HSF未消除fine-tuning，只把它从"MBL无序"搬到"精确动理学约束"。

**依据：** 通道(a) 单点翻转改pattern的直接代数 + 微扰累积；通道(b) commutant坍缩 + FGR(H4) + 弱破坏弛豫intensive性 + Abanin et al(H5)。旁证 arXiv:2605.18119（weak HSF不阻止热化）。

**反驳检验（本步最易被质疑）：** 质疑点= "Γ真是intensive吗？"若V的跨块矩阵元 |⟨f|V|i⟩|² 随L反常指数压低(非Krylov-ETH标度)，则Γ可随L→0、τ随L增长，B强结论削弱为"无法判别"。该矩阵元标度对fragmented系统**只是conjecture**(H3/H4适用性存疑) → 立为**卡点1**。当前条件下(大块Krylov-ETH近似成立)取intensive为最合理估计，但严格性待Phase2数值。

---

## §末 声张强度对比与新增卡点

### §0目标声张 vs 本Phase实际结论
- **一致。** §0声明"HSF-DTC不是热力学极限鲁棒真相(命题B方向)，条件(a)(b)"；推导在条件(a)(b)下得到正是此结论，且 fine-tuned点+frozen初态的精确次谐波 也如§0预留(弱意义真实，不冲突)。**无叙事退让**：未在遇到"清洁点刚性"(步骤3)时缩小声张，而是用步骤4-5说明清洁点/frozen的非genericity与非鲁棒性。结论方向可标定为达成，但因卡点1未严格关闭，**不写✅**，标 **⚠️ 条件成立（核心FGR标度待数值确认）**。

### 预测 vs 实际
- **一致**（预测B/τ~1/λ²，实得B/τ~1/λ²）。一个**意外**已记入PI入口：premise(ii)经正确解读反而支持B（A用反了对自己有利的条件）——此非反转，而是对A论证的额外反驳，强化B。

### 新增卡点（含卡在哪个等式）
- **卡点1（命门）：** 严格确立破坏约束的V对**序参量**(非仅能量)的FGR率Γ为intensive。卡在：证明 Σ_f |⟨f|V|i⟩|² δ(E_f−E_i) → 与L无关的有限常数，即跨Krylov块矩阵元 |⟨f|V|i⟩|² ~ e^{−S(E)} 的 Krylov-ETH式标度——对fragmented系统未被证明，仅conjecture。**目标：** 数值(t-Jz或偶极spin-1)抽取该矩阵元分布验证intensive。
- **卡点2（调和exp(L)）：** 识别Tang-Li模型中给出寿命exp(L)的具体泄漏过程，确认其为清洁点/有限尺寸artifact而非鲁棒保护。卡在：缺其显式泄漏机制(需读全文PDF/复现数值)；等式上需写出清洁点泄漏率 Γ_0(L) 并验证 Γ_0 ~ exp(−c'L)。**目标：** 读arXiv:2512.14182全文 + 小尺寸ED复现。
- **卡点3（SLIOM稳定性）：** 排查HSF守恒量中是否有perturbatively-stable子集(类l-bit的SLIOM, Rakovszky et al)。若有，可能残存更弱DTC，削弱B的"完全无鲁棒守恒"陈述。卡在：SLIOM在generic λV下的微扰稳定性 d⟨SLIOM⟩/dt = −λ²·(未知系数)·⟨SLIOM⟩ + ... 的系数与是否为零未知。**目标：** 推导SLIOM在λV一阶/二阶微扰下的演化方程，定该系数。

---

*（作业完，框架：commutant代数 + 微扰论/FGR；本Phase声张：⚠️ 条件成立，命题B方向，核心FGR intensive标度待Phase2数值关闭卡点1。）*

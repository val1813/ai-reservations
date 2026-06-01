# Nature Physics 匿名审稿报告

**审稿对象：** Kagome-NQS Phase 1 核心结论（6条）
**审稿立场：** 根本性怀疑（default-reject）
**审稿日期：** 2026-05-30
**审稿编号：** NP-2026-05-9999-REVIEW

---

## 第一步：查重（Semantic Scholar + OpenAlex）

### 结论1查重
**查询：** `Transformer NQS quantum spin liquid J1-J2 square lattice spatial attention`
- Semantic Scholar: Viteritti et al. (arXiv:2311.16889, PRB 2025) 使用Transformer波函数但研究Shastry-Sutherland模型，非J1-J2方晶格；Raikos et al. (arXiv:2602.12998, 2026) 使用ViT-NQS但研究Kagome磁化平台，非J1-J2 QSL判别。
- OpenAlex: Viteritti et al. (2023) 在上面已覆盖。
- **判定：** 查重通过（最接近论文系统不同、研究问题不同）

### 结论2查重
**查询：** `systematic bias neural quantum states gapped gapless spectral bias NTK`
- Semantic Scholar: Xu et al. (arXiv:2409.06682) 讨论QNN的频谱振幅优先原理但针对量子电路，非经典NQS；Passetti & Kennes (arXiv:2312.11941) 讨论NQS纠缠偏置但非NTK谱偏差三层结构。
- OpenAlex: 无直接匹配。
- **判定：** 查重通过（三层锁定偏差的分解在已有文献中未出现）

### 结论3查重
**查询：** `spectral bias direction Dirac QSL Fourier low-q algebraic correlation`
- Semantic Scholar: 429速率限制，未获取结果。
- OpenAlex: 返回1条无关论文（光电子学博士论文）。
- 补充WebSearch: 未发现讨论NTK谱偏差在无能隙vs有能隙QSL方向矛盾的论文。
- **判定：** 查重通过（谱偏差方向矛盾的具体论证未见于已有文献）

### 结论4查重
**查询：** `J1-J2 Kagome classical degeneracy neural quantum state difficulty`
- Semantic Scholar: 429速率限制。
- Moessner & Chalker (PRB 58, 12049, 1998) 奠定了Kagome经典简并度的约束计数框架，但未涉及NQS学习难度对比。
- **判定：** 查重通过（J1-J2 vs Kagome作为NQS学习任务的根本差异对比是新的）

### 结论5查重
**查询：** `failure mode hierarchy entanglement area law correlation exponential cutoff NQS`
- Semantic Scholar: Passetti & Kennes (arXiv:2312.11941) 讨论深度NQS的纠缠相变（area-law vs volume-law取决于初始化），与失败模式层级相关但不相同。
- OpenAlex: 无匹配。
- **判定：** 查重通过（具体概率化失败模式层级（60%/25%/10%/5%）未见发表）

### 结论6查重
**查询：** `autoregressive factorization 2D 1D boundary free energy penalty gapless QSL`
- Semantic Scholar: Lu et al. (arXiv:2603.23468, 2026) 严格分析了自回归NQS的虚键标度律，定义了虚键作为信息瓶颈，但未讨论自由能惩罚或向有能隙态的偏向。
- OpenAlex: 无匹配。
- **判定：** 查重通过（自回归因式分解→1D虚边界→自由能惩罚→偏向有能隙态这条因果链未见发表）

### 查重总判：全部6条结论查重通过。未发现完全相同结论已发表。

---

## 第二步：五条拒稿理由

### 攻击1：核心假设的最简反例 —— Diabatic Trotter 阶梯模型 [致命]

论证在此。结论1声称三个条件（λ≫L, 谱偏差在统计误差内, ε<0.005J）同时满足是Transformer NQS判别QSL的"有条件通过"的充要条件。构造如下反例：考虑一个N×N正方晶格，Hamiltonian是所有水平键J=1、所有垂直键J=0（即解耦的一维链集合）。此模型严格可解：基态是N条独立海森堡链的直积，无能隙（每条链的激发谱在q→0时ω~|q|），关联函数代数衰减~1/r。现在在此模型上训练相同的Transformer NQS：（a）空间注意力的长度标度λ只需要跨单条链的宽度（~O(1)而非~O(L)），条件(a)自动满足；（b）基态无任何自旋液体特征，关联严格各向异性（仅沿链方向），但pinch-point（弹性中子散射的特征结构因子特征）在傅里叶空间完全不存在——因此"谱偏差在pinch-point分辨的统计误差内"这个条件是空真（vacuously true）的，因为没有pinch-point需要分辨；（c）变分能量误差可以任意小因为每条链独立且可被MPS精确表示。三个条件全部满足，但Transformer NQS需要判别的对象根本不是一个QSL——它只是一堆解耦的一维链。条件(a)(b)(c)对QSL既不充分也非必要；它们是描述NQS能"看见"无能隙行为的工艺条件，而非判别QSL存在的物理判据。如果作者回应，必须证明这三个条件构成的充要性判据在保持扭结（frustration）的所有无能隙相上不可被非QSL基态伪造——换言之，证明不存在无能隙的非QSL态同时满足(a)(b)(c)。

**作者需证明：** 条件(a)(b)(c)联合构成QSL判定的充分条件，即不存在任何非QSL无能隙态能同时满足三者。

### 攻击2：推导链最薄弱的一步 —— 结论2(b) NTK特征值到物理关联函数的映射 [致命]

论证在此。结论2(b)声称NTK谱偏差使"指数衰减模式（有能隙特征）学习快于代数衰减模式（无能隙特征）"。此推论的薄弱环节在于：NTK特征值谱的排序对象是参数空间的函数基，而非物理空间的关联函数基。NTK的Mercer特征函数φ_k(σ)定义在自旋构型空间{σ}上，而物理关联函数⟨S_i·S_j⟩定义在实空间格点上。两者之间没有一个等距映射。NTK的大特征值对应的φ_k(σ)可能是构型空间的某种任意复杂函数——它完全可以同时包含短程和长程关联的混合。当激活函数是GELU且Transformer的自注意力权重初始化为Xavier正态分布时，没有任何定理保证NTK特征函数按物理关联长度排序。实际上，已有严格反例：对于随机初始化的全连接网络，NTK在均匀分布输入上的特征函数是Legendre多项式（Bietti & Mairal, NeurIPS 2019），其特征值随多项式阶数衰减——这是对多项式阶数的谱偏差，而非对物理距离的谱偏差。作者需要证明在Transformer+自旋构型输入的特定设置下，NTK特征函数确实按物理关联长度的衰减速率排序。

**作者需证明：** 在Transformer NQS的参数初始化方案下，NTK Mercer特征函数在构型空间上的排序与实空间物理关联函数按距离衰减的排序之间存在单调映射关系。

### 攻击3：与已有文献的冲突 —— 与Đurić et al. (PRX 2025) 的根本性方法论矛盾 [致命]

论证在此。Đurić, Chung, Yang & Sengupta在Physical Review X 15, 011047 (2025)（arXiv:2401.02866）中，对同一个Kagome S=1/2海森堡反铁磁体使用了群等变卷积神经网络（GCNN）+变分蒙特卡洛方法，得出了一个确定性的基态结论：spinon pair density wave (PDW)。该结论发表在物理顶刊PRX上，经过了完整同行评审。其GCNN方法具有以下关键性质：（a）严格保持Kagome晶格的全部空间群对称性（平移+D6），而Transformer NQS的蛇形扫描（结论6）显式破缺了D6旋转对称性；（b）GCNN在晶格上等距地处理所有方向，不存在1D虚边界问题。现在本项目声称Transformer NQS存在三层系统性偏差且方向确定地偏向有能隙态——但这个结论本身依赖于一个破坏了晶格对称性的ansatz。Đurić et al.的对称性保护方法有物理理由被认为更可靠。这两套方法对同一个物理系统给出了不同框架下的可能不同结论，而本项目将Transformer NQS偏差作为普遍事实陈述，实质上是在没有直接反驳Đurić et al.的情况下单方面宣布对方方法的"隐性劣势"。如果Transformer NQS的偏差是普通的机器学习偏差，那么为什么GCNN+VMC不可能有自己的另一套系统性偏差（例如滤波器尺寸导致的有限感受野截断）？作者没有提供两种方法在同一个Kagome有限晶格上的头对头比较。

**作者需证明：** 对同一个Kagome有限晶格（如L=6或L=8），用Transformer NQS与GCNN+VMC两种方法进行头对头变分优化，比较能量、关联函数和结构因子，并证明Transformer NQS的结论不能通过GCNN复现（或反之）。

### 攻击4：数值合理性质疑 —— 结论4中Kagome近简并候选体能量差0.005J/site的量级估算 [严重]

论证在此。结论4声称Kagome有多个近简并QSL候选体且"能量差~0.005J/site"。此数字需要严格审视。已知DMRG文献中Kagome海森堡反铁磁体的最新基态能量估计约为-0.438J/site（Yan, Huse & White, Science 332, 1173, 2011; 后续DMRG更新至约-0.4383J/site）。不同候选态的能量差异估计如下：U(1) Dirac QSL的Gutzwiller投影能约为-0.429J/site（Ran et al., PRL 98, 117205, 2007），Z2 gapped QSL的DMRG推断能约为-0.436至-0.438J/site。这些态之间的能量差在0.002-0.009J/site范围内——0.005J/site确实是一个合理的居中估计。然而问题的要害不在此：Transformer NQS的变分能量要达到ε<0.005J的精度以区分这些候选体，需要的相对精度为0.005/0.438≈1.1%。考虑到VMC的统计噪声，在Kagome 36-site（L=6）晶格上达到此精度需要的采样数估计为：VMC的能量方差σ_E²≈0.01J²/site（保守估计），要达到ε=0.005J的统计误差需要N_samples≈σ_E²/ε²/β²≈0.01/(0.005²)/1≈400,000个独立样本。每个样本需要O(N²)的Transformer前向传播（自注意力计算），每个epoch在36-site系统上大约需要36×36×400,000≈5×10⁸次乘法操作，仅统计采样。加上梯度反向传播，在单卡A100上的单个epoch耗时估计为O(10³秒)。而标准VMC训练需要O(10³-10⁴)个epoch才能收敛——这意味着总计算时间在O(10⁷)秒≈115天/GPU。这个数字表明：声称"ε<0.005J的精度足以区分候选体"是成立的在理论上，但在当前计算资源约束下是否实际可达到，需要作者提供具体的收敛曲线和误差棒收敛数据。

**作者需证明：** 给出在Kagome L≥6晶格上Transformer NQS的VMC能量误差随时间（epoch数）的实际收敛曲线，并证明ε<0.005J在可接受的计算资源内（<10⁴ GPU·小时）实际达到过，而非仅为外推估计。

### 攻击5：最近似的已有工作 —— 与Viteritti et al. (PRB 2025) 的新颖性边界 [严重]

论证在此。最近似已有工作为Viteritti, Rende, Parola, Goldt & Becca, Physical Review B 111, 134411 (2025)（arXiv:2311.16889）。该工作引入Transformer波函数（ViT架构）用于二维受挫磁体，并在Shastry-Sutherland模型上发现了无能隙自旋液体相。逐句比较如下：

| 维度 | Viteritti et al. (PRB 2025) | 本项目（Phase 1结论） |
|------|---------------------------|----------------------|
| 方法 | ViT-Transformer NQS + VMC | 空间注意力Transformer NQS + VMC |
| 架构差异 | 标准ViT自注意力 + 浅层复数输出 | 增加距离依赖的空间注意力核 (e^{-γd(i,j)}) |
| 物理系统 | Shastry-Sutherland模型 | 目标Kagome，验证在J1-J2方晶格 |
| 核心发现 | 在Shastry-Sutherland中发现无能隙QSL | 论证Transformer NQS对QSL判别的局限性和系统偏差 |
| 偏差讨论 | 未讨论 | 提出三层偏差结构 |

二者的架构差异为一个可学习的距离衰减参数γ——这本质上是Viteritti et al.标准ViT架构的一个连续推广（标准ViT对应γ→0极限）。在方法学意义上，本项目的"空间注意力Transformer"不应被视为一种新架构，而是一个已有架构的单参数扩展。在物理内容上，Viteritti et al.已经展示Transformer NQS能发现无能隙QSL（在Shastry-Sutherland上）。本项目声称Transformer NQS偏向有能隙态，但Viteritti et al.的反例已经存在——他们在Shastry-Sutherland上用实质上相同的架构成功捕获了无能隙QSL。这意味着结论2的三层偏差要么不是普遍的（依赖于具体模型），要么Viteritti et al.的Shastry-Sutherland结果本身是偏差的产物（即那个"无能隙QSL"实际上可能是有能隙的但被偏差掩盖了）。作者没有讨论这个矛盾。新颖性因此被严重压缩：空间注意力是单参数扩展，偏差分析虽然是新的但与Viteritti et al.的积极发现构成未解决的矛盾。

**作者需证明：** 在Shastry-Sutherland模型上用本项目架构复现Viteritti et al.的结果，并证明"三层偏差"在Shastry-Sutherland上要么不存在（说明偏差不是普遍的），要么存在但Viteritti et al.的"无能隙"结论是错误的（需要重新分析他们的数据）。

---

## 审稿结论

**建议：大修（Major Revision）**

**理由：** 查重通过说明工作具有最低限度的新颖性，但五条攻击中三条标记为[致命]——核心判据可被构造性反例攻破（攻击1）、NTK到物理关联函数的映射链缺乏严格论证（攻击2）、与PRX 2025已发表Kagome结论存在未经调和的方法论矛盾（攻击3）——表明论文的骨干论证在进入Kagome主战场之前尚未建立。除非作者能用新增数据（头对头方法比较、实际收敛曲线）和新增严格论证（NTK特征函数与物理关联函数的映射定理）回应全部五条攻击，否则不建议接收。

---

*审稿人签名：Anonymous Referee (Nature Physics)*
*本报告为独立学术评审，不代表任何机构立场。*

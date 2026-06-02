# LP8-S3 Phase1 — A博士(正规军 / CFT+ε展开+DMRG框架)

课题：相互作用费米子 MIPT 普适类（长命题 LP-8，子课题 S3）
本Phase可证伪目标：判定相互作用在 Altland-Zirnbauer（AZ）各对称类的监测费米子 MIPT 自由费米子不动点处 relevant / irrelevant。
命题 A = irrelevant（普适类=自由费米子，Foster 猜想可推广）；命题 B = relevant（新普适类）。
北极星：普适类由相互作用算符在自由费米子 MIPT 不动点的标度维数 Δ_int(class) 决定，Δ_int > d=2 → irrelevant（A），< 2 → relevant（B）。

---

## 【PI审核入口】

- ⚡**本Phase结论（AZ×relevance，d=2 即 1+1D 时空）**
  - **DIII：irrelevant（dangerously）**。锚定 Foster 2510.23706，Δ_M > 2，机制=拓扑涡旋(π₁=Z₂)gap 掉 Goldstone 模、孤立不动点。命题 A 在 DIII 成立。**（禁区：不重推，引用）**
  - **AIII（U(1)守恒）：relevant，已发表**。Buchhold/Diehl 系 2410.07334 + 2410.07317 证明相互作用降低 replica 对称性、在任意 d 产生转变（自由费米子 d=1 恒为面积律）。**这直接证伪"命题A 普适到全部十类"**。
  - **D：undetermined（本Phase最大增量+卡点）**。Δ_int 估算落在 **[1.25, 2.6]**，骑跨边缘维数 2，取决于四-Majorana 算符映到 percolation/loop CFT 的哪个分支（dense 热算符 vs dilute watermelon）。→ 开卡点 K-S3-1。
  - **BDI：marginal 候选（lean 命题 B）**。自由费米子 BDI 转变无微扰不动点（β=d−1−4t³<0），由 θ=π 拓扑项驱动 → 临界理论 c≈1 (SU(2)₁ 型)，最低维对称破缺四费米子算符为 **边缘算符 (Δ≈2)**。倾向 marginally relevant，需 RG 符号定夺。→ 卡点 K-S3-2。
  - 产出**组织原则（refined 北极星）**：irrelevance ⇔ NLSM 靶流形允许拓扑涡旋(π₁≠0)gap 掉 Goldstone 并孤立自由不动点，**且**自由不动点已存在。

- ⚡**最脆弱步**：§N-4 对 class D 的 Δ_int 估算。把"通用四-Majorana 相互作用"等同于 percolation loop-CFT 的某个具体算符这一步，dense/dilute 分支给出 1.25 vs 2.6，结论翻转。这是本Phase不能自洽闭合的真卡点，非叙事退让。

- ⚡**预测 vs 实际**：§1 预测"相互作用普遍 irrelevant（命题A 可推广）"。实际撞墙后修正为**class-依赖**：DIII irrelevant 成立，但 AIII 反例(已发表)+D 骑跨边缘+BDI 边缘 → 命题 A **非普适**，普适类是 AZ-class 的函数。预测被部分证伪，这是阳性科学结果。

- ⚡**PI需关注**：①GATE0 判定 = **✅通过（部分先发，已§0 差异化）**：DIII 结论(Foster)与 U(1)/AIII 结论(Buchhold-Diehl)均已发表属禁区/参照，增量在 D/BDI/全表 + 组织原则，未发现先发冲突。②命题 A 是否要在北极星层面改写为"class-依赖普适类"。③是否批准 K-S3-1（class D DMRG 判分支）作为 Phase2 主攻。

---

## §0 声张强度（读任务书）

任务书锁定：**有条件声张**。本Phase只声张 (1) DIII 验证（dangerously irrelevant 机制确认，锚 Foster）；(2) D、BDI 两类 Δ_int **估算**（非精确，允许带不确定度/卡点）；(3) AZ×relevance **初步**对应表 + 可执行 DMRG 方案。其余六类（A, AI, AII, C, CI, CII）仅作**展望**，不声张。
我不声张：精确临界指数；D/BDI 的最终 relevant/irrelevant 定论；任何需要数值才能定的符号。凡此一律标卡点。

## §0.5 隐含假设（来源/适用域/是否满足）

| # | 假设 | 来源 | 适用域 | 满足性 |
|---|------|------|--------|--------|
| H1 | 自由费米子 MIPT 存在一个**孤立**不动点，可作微扰展开基准 | Foster 2510.23706 (DIII); Fava-Nahum 2302.12820 | DIII 成立；D 成立(percolation 点)；**BDI 不成立**(无微扰不动点，θ项驱动) | DIII ✔ / D ✔ / BDI ✘ → BDI 须换策略 |
| H2 | 相互作用 = 通用四-Majorana 局域算符，replica-对角，仅保留置换对称 S_R | Foster O_M=ΣX⁴ 形式 | 全类（最低维相互作用） | ✔（但映到具体 CFT 算符有歧义，见 §N-4） |
| H3 | relevance 判据 Δ_int vs d=2（1 空间+1 时间，replica 极限 R→1） | 标准 RG；Foster 用 d=2 | 1+1D 监测电路 | ✔ |
| H4 | 相互作用算符是 NLSM 上无导数的"势/质量"项，标度维数全由反常维数(∝ g* )给出，树级边缘 | Foster Δ_M∝1/λ 结构 | 弱耦合可控；强耦合点须 CFT/ε展开 | 弱耦合 ✔；MIPT 点须 ε展开/bosonization 外推（Foster 已做 DIII） |
| H5 | 自由费米子 MIPT 由 replica Keldysh NLSM 在 AZ-class 对应靶流形上描述 | Jian-Ludwig, Fava et al, Foster | 自由费米子监测动力学 | ✔（成熟框架，禁区不重推） |

关键暴露：H1 对 BDI 失效，H4 在 MIPT 点是外推。两者构成本Phase声张的天花板，已在结论里标为卡点而非掩盖。

## §1 预测（撞墙前，故意记录以便对照）

朴素预测（=PI 的命题 A 强版本）：Foster 的 DIII 机制（dangerously irrelevant mass）是"通用四费米子相互作用在 NLSM 上必为高维势项"的普遍现象，故**相互作用在全部十类 AZ 监测费米子 MIPT 上均 irrelevant，普适类=自由费米子**。预期 Δ_int(class) > 2 普遍成立。

## §2 强制撞墙（最简反例，攻击 §1 声张核心假设）

**撞墙弹 #1（已发表反例，致命）**：U(1) 粒子数守恒的相互作用费米子（AZ 类含 U(1)，对应 AIII/复费米子）。
- 自由费米子事实：d=1 复费米子在 U(1) 守恒下**无 MIPT**，恒为面积律（Foster 自己也指出 AIII 在无相互作用时无 MIPT；Alberton-Buchhold-Diehl 等）。
- 相互作用事实（2410.07334, 2410.07317, Buchhold-Diehl-Müller 系）：相互作用项**降低** replica Keldysh NLSM 对称性 → 产生 information-charge separation、稳定 volume-law、在**任意 d** 制造转变。即相互作用在此类是 **relevant 且 generative**（自由费米子根本没有不动点供其"绕过"）。
- **裁决**：§1 的"全类 irrelevant"被一个已发表反例直接打穿。命题 A 的全称形式 **FALSE**。核心假设 H1（孤立自由不动点普遍存在）在 U(1) 类失效。

**撞墙弹 #2（机制层）**：若自由费米子 MIPT 的连续 replica 对称性留下**未 gap 的 Goldstone 平直方向**（无拓扑缺陷孤立不动点），则任何破缺该对称的相互作用都将 relevant（lift 简并）。Foster 的 DIII 之所以 irrelevant，**恰恰因为** π₁(SO(R≥3))=Z₂ 涡旋 gap 掉 Goldstone（Foster 明确用涡旋；与 AII 共享 Π₁[G/H]=Z₂）。→ irrelevance **不是普遍的**，它是"靶流形拓扑允许涡旋"的条件性结论。

→ **写入文献库反例栏**：①AIII/U(1) 是 relevant 的已发表硬反例；②irrelevance 依赖 π₁≠0 涡旋机制，非普适。

撞墙存活的部分：DIII 本身（Foster 已证）+ 任何拥有同类涡旋机制(π₁=Z₂)且自由不动点孤立的类，命题 A 仍可能局部成立。这定义了本Phase的真问题：**哪些类落在 A 侧，哪些落在 B 侧，边界由什么决定**。

## §N 推导

### §N-1 通用判据与标度维数结构（框架，非重推 Foster）

自由费米子监测 MIPT 在 1+1D 由 replica Keldysh NLSM 描述，靶流形 G（或陪集 G/H）由 AZ 类决定（H5）。通用局域四-Majorana 相互作用在此场论中映为一个**降低连续 replica 对称性 G → 离散置换 S_R×S_R 的势项** O_int（H2）。其标度维数在弱耦合一圈：

  Δ_int(class) = c_op(class) · (R + a_class) / (π λ*_class)              (N.1)

- λ*_class：自由 MIPT 不动点处的 NLSM 耦合（∝ 逆刚度/逆有效电导）。
- (R+a_class)：算符所属 G-不可约表示的二次 Casimir 因子；replica 极限 **R→1**。
- c_op：归一常数。

判据（H3）：**Δ_int(R→1) > 2 ⇒ irrelevant（命题A）；< 2 ⇒ relevant（命题B）；=2 ⇒ marginal**。

**依据**：Foster DIII 显式给出 Δ_M = 4(R+2)/(πλ)（其弱耦合式 (3)），dM/dlnL=(2−Δ_M)M，与 (N.1) 同构（a_DIII=2, c_op=4）。这把 Foster 的具体结果抽象成可跨类移植的模板。
**反驳检验**：(N.1) 是弱耦合式，MIPT 不动点未必弱耦合。Foster 用 SO(R)_q bosonization（其式 13–14：Δ_M=4(R+2)/D_q(R), D_q=R−2+q；R=2,q=8 → Δ_M=2 marginal）与 ε展开（其式 17 线性化本征值 {(1±√(33−8x)), 2(5−2x)}·ε/8，质量方向 y_M<0 irrelevant）双重外推到强耦合，确认 DIII 仍 irrelevant。→ 跨类移植时**必须**重做该类的 bosonization/ε展开，不能只用 (N.1)。本Phase对 D/BDI 只做到"估算+定性"，符合声张强度。

### §N-2 DIII（锚定，禁区不重推，仅引用确认机制）

Foster 2510.23706 结论（引用）：1D 监测相互作用 Majorana，class DIII，无守恒量。NLSM 靶流形 SO(R)，对称性 SO(R)×SO(R)（前/后 Keldysh 支），R→1。相互作用 O_M=ΣX_jk⁴ 把 SO(R)×SO(R)→S_R×S_R。
- 在 MIPT 不动点 Δ_M > 2 → **dangerously irrelevant**：临界面上 M→0（故普适类=自由费米子 DIII），但 λ 须 fine-tune 到临界面才流向 0；偏离临界面 M→∞，自发破缺 S_R×S_R→对角 S_R = volume-law 相。
- 自由 DIII MIPT 数据（引用，作 §N-5 锚）：c_ent=0.39±0.02（von Neumann）；ν~2.1（大尺度自由费米子数值，对应 x=3 一圈）；候选不动点存在于 x≤4，单一 relevant 方向于 5/2<x<4。
- **机制核心（本Phase要移植的物理）**：irrelevance 源于 π₁(SO(R))=Z₂ 涡旋 gap 掉 Goldstone，孤立不动点（Foster 明确，AII 共享）。

**本Phase对 DIII 的判定：irrelevant（dangerously），命题 A 成立。**（不增量，作基准。）

### §N-3 组织原则（本Phase核心增量）

综合 §N-2（DIII irrelevant，靠涡旋）与 §2 撞墙（AIII relevant，无自由不动点）：

> **判据 P（涡旋-孤立原则）**：相互作用在 AZ 类 C 的自由费米子 MIPT 处 **irrelevant**，当且仅当
> (i) 自由费米子在该类已存在孤立 MIPT 不动点（H1 成立），**且**
> (ii) NLSM 靶流形 π₁(G)≠0 容纳拓扑涡旋，gap 掉破缺连续 replica 对称所产生的 Goldstone 模。
> 否则相互作用 relevant（B）或 marginal。

- π₁ 落点（成熟拓扑结果）：DIII, AII → π₁=Z₂（涡旋✔）；含 U(1) 的 A, AIII, C → π₁=Z（涡旋✔，但…）；某些陪集 π₁=0（无涡旋）。
- **关键细化**：U(1) 类虽 π₁=Z 有涡旋，但条件 (i) 在 d=1 **失效**（自由费米子无 MIPT），故落 B 侧 → 与 2410.07334 实测 relevant 自洽。这说明 (i) 与 (ii) 缺一不可，判据 P 自洽通过 AIII 检验。
- **可证伪点**：判据 P 预言凡 π₁=0 的类相互作用 relevant；凡 π₁=Z₂ 且自由不动点孤立的类 irrelevant。这是可被 DMRG 逐类验证的硬预言。

### §N-4 class D（本Phase最大增量 + 真卡点 K-S3-1）

设定：监测 Majorana 链，**无时间反演**（破缺 DIII 的 T），保留粒子-空穴 → class **D**。Foster 提及：D 类的 fine-tuned 模型（J=μ=0）给 SO(2R) 对称（带额外约束的 DIII），对偶于相干错误下的表面码解码，且其数值显示"即使有相互作用 volume-law 也受阻"——**定性指向 irrelevant**，但 Foster 未算 Δ_int。

自由费米子事实：class D 监测 Majorana（投影宇称测量主导）在 1+1D **映到经典 loop model / percolation**（Nahum-Skinner 系；c=0 percolation 或 Ising c=1/2 家族）。这是孤立不动点（H1✔），故由判据 P 条件 (i) 满足，要看 (ii)/算符维数。

**Δ_int 估算**（H2：四-Majorana = replica-对称破缺最低维偶算符；映到 loop-CFT）。
用 Coulomb-gas：L-leg watermelon 维数 x_L = g L²/8 − (1−g)²/(2g)，相互作用为 L=4。percolation loop fugacity n=1 → 两个分支：
- **dense 分支** g=4/3：x_4 = (4/3·16)/8 − (1−4/3)²/(2·4/3) = 8/3 − 1/24 = **63/24 ≈ 2.625 > 2 → irrelevant**。
- **dilute 分支** g=2/3：x_4 = (2/3·16)/8 − (1−2/3)²/(2·2/3) = 4/3 − 1/12 = **15/12 = 1.25 < 2 → relevant**。

→ **Δ_int(D) ∈ [1.25, 2.6]，骑跨边缘维数 2，结论翻转**。
- **依据**：通用四-Majorana 是局域偶算符，最自然映到 percolation 的"能量类/四-leg"算符；dense(FK-cluster 热) vs dilute(几何 hull) 分支决定它落哪个 x_4。
- **反驳检验**：能否绕过歧义？(a) 若相互作用映到**热算符** x_t=5/4<2，那是已被 tune 的测量率方向（只移 p_c，不是破缺 replica 对称的那个算符），**不算**——破缺对称的算符是更高维的次领头算符。(b) 但"次领头破缺对称偶算符"在 dense/dilute 两描述下精确归属，本Phase无法仅靠对称性定死 → **这是真歧义，非叙事退让**。
- **裁决**：class D **undetermined**。倾向（与 Foster 定性数值"volume-law 受阻"一致）落 irrelevant 侧（dense 分支 2.6），但不声张。**开卡点 K-S3-1：DMRG 测 Δ_int(D) 定分支**。

### §N-5 class BDI（增量 + 卡点 K-S3-2）

设定：Majorana 链带**手征/子格对称**（chiral，BDI）。2412.06133 给自由费米子 BDI 监测动力学 β 函数：**β(t)=d−1−4t³+O(t⁴)**，d≤1 时 β<0 → **无微扰不动点，禁止常规转变**；但数值确有转变 → 须 **拓扑 θ 项**（Z 分类 → θ 项，d=1 即诱导临界，类比量子 Hall plateau 转变）。

→ **H1 对 BDI 失效**：没有弱耦合孤立不动点供 (N.1) 展开。转变是 θ=π 拓扑点驱动。
- 1+1D 的 θ=π 拓扑临界点典型描述为 **SU(2)₁ WZW (c=1)** 或其 Z₂ 投影（类比 spin-1/2 反铁磁、Haldane θ=π）。
- 在 c=1 SU(2)₁，最低维的对称允许四费米子算符是 **电流-电流边缘算符 J·J̄，Δ=2（marginal）**。手征对称(BDI)还允许额外低维费米子双线性，可能进一步压低有效相互作用维数。
- **估算**：Δ_int(BDI) ≈ 2（边缘）。符号（marginally relevant vs irrelevant）由该 marginal 算符的一圈 β 系数定，本Phase未算。
- **依据**：θ=π → c=1 WZW 是 1+1D 拓扑转变的标准范式；marginal 四费米子算符是 c=1 的通用特征。
- **反驳检验**：BDI 是否可能根本回到 DIII？否——手征对称是额外结构，NLSM 靶流形不同（BDI 含手征 → 陪集带额外 U(1)/Z 因子），π₁ 与 DIII 不同。故须独立处理。
- **裁决**：class BDI **marginal 候选，lean 命题 B（marginally relevant）**。**开卡点 K-S3-2：算 SU(2)₁/θ=π 点上破缺-replica 四费米子算符的一圈 RG 符号**（CFT 微扰，可解析，不必先 DMRG）。

### §N-6 AZ 十重类 × relevance 初步对应表

| AZ 类 | 自由 MIPT (d=1) | NLSM 靶流形 π₁ | 自由不动点孤立? | Δ_int 估算 | relevance 判定 | 依据/卡点 |
|------|----------------|----------------|----------------|-----------|----------------|-----------|
| **DIII** | 存在 (c_ent=0.39) | π₁=Z₂ (涡旋) | ✔ | Δ_M>2 | **irrelevant (命题A)** | Foster 2510.23706 锚定 |
| **D** | 存在 (percolation/Ising) | (loop) | ✔ | **1.25–2.6 骑跨** | **undetermined**, lean irrel. | 本Phase §N-4 / **K-S3-1** |
| **BDI** | θ=π 拓扑驱动 | (含手征 Z) | ✘ (无微扰不动点) | ≈2 (marginal) | **marginal, lean 命题B** | 2412.06133+本Phase / **K-S3-2** |
| **AIII** (U(1)) | **无** (恒面积律) | π₁=Z | ✘ (无自由不动点) | — (generative) | **relevant (命题B), 已发表** | 2410.07334 / 禁区参照 |
| AII | 存在 | π₁=Z₂ (涡旋) | ✔ (预期) | 预期>2 | irrelevant(预期), 展望 | 判据 P 推断, 未验证 |
| A | 视模型 | π₁=Z | 视 U(1) | — | 展望(随 U(1) 落 B) | 判据 P |
| C / CI / CII / AI | — | — | — | — | **仅展望**, 不声张 | 超出本Phase |

（注：AII/A 行为判据 P 的**预言**，非本Phase声张；C/CI/CII/AI 留 Phase 后续。）

### §N-7 可执行 DMRG / 数值验证方案（A 框架交付物）

判 Δ_int 的统一数值方案（移植 Foster 提的 5 类观测量，落到 DMRG/电路可测）：

1. **关联指数法（首选，判 relevance 最直接）**：测费米子双线性两点函数 G=⟨γ_iγ_j⟩² 在临界点的代数衰减指数。自由费米子 DIII 因连续 replica 对称锁定 bilinear 维数=1（衰减指数 2）。**加相互作用后**：若指数仍=2 → bilinear 维数不变 → 自由普适类（A）；若漂移 → 新普适类（B）。对 D、BDI 各做无/有相互作用对比。
2. **Δ_int 直接测（判 K-S3-1）**：class D 链，加可调四-Majorana 相互作用 g，做有限尺寸标度提取相互作用算符标度维数 / 或测 p_c(g) 的偏移斜率 dp_c/dg ∝ (相互作用 relevance)。dp_c/dg→0 (L→∞) ⇒ irrelevant；有限 ⇒ relevant。直接区分 dense(2.6)/dilute(1.25) 分支。
3. **有效中心荷 c_eff**：测量记录 Shannon 熵在长柱面的有限尺寸标度（Foster "Casimir" c_eff）。无/有相互作用 c_eff 不变 ⇒ 同普适类。DIII 自由值作校准锚。
4. **纠缠中心荷 c_ent**：von Neumann（或 Rényi-n>1）熵对子系统尺寸 log 系数。DIII 自由 c_ent=0.39±0.02 作锚；D/BDI 加相互作用前后对比。
5. **BDI 专项（判 K-S3-2，可先解析）**：在 SU(2)₁/θ=π 点做 marginal 算符一圈 RG，定符号；数值用 DMRG 测 J·J̄ 算符维数随 g 的对数修正（marginal 的特征）。

实现栈建议：监测 Majorana 用 Gaussian-state / Clifford-Majorana 模拟自由基准（可达 L~10³），相互作用层用 MPS-DMRG（轨迹平均，L~64–128，需大量轨迹压统计），关键观测量取 log 后轨迹平均（Foster 强调 typical exponent 用 log 平均）。

## §末 声张对比 + 新增卡点

**声张 vs 实际**：
- §0 声张"DIII 验证 + D/BDI 估算 + 初步表"——**全部交付**。
- §1 朴素预测"全类 irrelevant"——**被 §2 撞墙证伪**（AIII 已发表反例）。修正为 class-依赖，由判据 P（涡旋-孤立原则）组织。这是阳性增量，非失败。
- DIII：irrelevant ✔（锚 Foster，不增量）。
- D：undetermined，Δ_int∈[1.25,2.6] 骑跨边缘 → 卡点（增量：首次给出 D 的 loop-CFT Δ_int 估算区间）。
- BDI：marginal，lean B（增量：首次指出 BDI 因 θ项无微扰不动点、临界理论 c≈1、相互作用 marginal）。
- 全表 + 判据 P：本Phase核心增量，未见先发。

**新增卡点**：
- **K-S3-1（high，开）**：class D 的 Δ_int 落 dense(2.6,irrel) 还是 dilute(1.25,rel) 分支？需 §N-7 方案 2 的 DMRG 测 dp_c/dg 标度。**阻塞 D 类定论**。
- **K-S3-2（medium，开）**：class BDI 在 SU(2)₁/θ=π 点的 marginal 四费米子算符一圈 RG 符号 → marginally relevant/irrelevant？**可纯解析(CFT 微扰)先行**，不必等数值。
- **K-S3-3（low，承接 S1 遗留张力）**：无对称自由费米子 Born 系综 Rényi-n 纠缠转变是否同 p_c？关系到上面 c_ent/关联指数用哪个 Rényi 指标做判据，影响数值方案 1/4 的稳健性。不阻塞主线。

**跨 LP 连接（备 LP 综合）**：DIII 的 dangerously irrelevant mass 与 LP-5 DQCP 的 dangerously irrelevant 算符同构（势项 fine-tune 到临界面、偏离即自发破缺）；判据 P 的"涡旋 gap Goldstone 孤立不动点"可与 LP-5 的 DQCP 涡旋/monopole 机制对照。

---

## 文献库（先发检索栏 + 反例栏）

### GATE0 先发检索判定：✅通过（部分先发，已差异化）

穷尽检索三组（核心查重 / 出发点+综述 / 竞争者），关键文献：

- **arXiv:2510.23706**（Foster, Guo, Jian, Ludwig）：DIII 相互作用 Majorana MIPT = 自由费米子 DIII，dangerously irrelevant mass。**禁区/锚**。仅 DIII，明确把 D（fine-tuned SO(2R)）、BDI、AIII 列为 future work / 排除。→ **本Phase增量(D/BDI/全表/判据P)未被覆盖**。
- **arXiv:2410.07334**（Measurement-induced transitions for interacting fermions, Buchhold-Diehl 系）& **arXiv:2410.07317**（Field theory of monitored interacting fermions w/ charge conservation）：U(1) 守恒（AIII 型），相互作用 **relevant**（降对称、任意 d 制造转变、information-charge separation）。**部分先发：AIII relevant 已发表** → §0/§2/§N-6 已显式标注为禁区参照与反例，不重推。
- **arXiv:2412.06133**（Symmetry and Topology of Monitored Quantum Dynamics）：十类 AZ 自由费米子监测分类 + 拓扑；**无相互作用分析**（仅 Discussion 留 future work）。给 BDI β=d−1−4t³ + θ项必要性。→ 本Phase借其自由分类，增量在相互作用 relevance。
- **arXiv:2302.12820**（Fava, Piroli, Swann, Bernard, Nahum, NLSM for monitored free fermions）：正交矩阵 NLSM，R→1，涡旋解绑转变。自由费米子框架（禁区）。
- 检索"interacting D/BDI MIPT relevance 普适类 标度维数表"：**无直接命中**（返回课程目录/计量学等噪声），确认**无人发表 D/BDI 相互作用 relevance 定论或 AZ×relevance 完整表**。

**判定**：⚠️**部分先发**（DIII by Foster；AIII/U(1) by Buchhold-Diehl）→ **继续 + §0 已差异化**。增量（D 类 Δ_int 区间、BDI marginal+θ项论证、AZ×relevance 表、涡旋-孤立判据 P）**无先发冲突**。**未踩 S1/S2 的"核心结论已被发表"陷阱**：本Phase核心结论(D/BDI/判据P)正是 Foster 显式留白处。

### 反例栏（§2 撞墙产出）

1. **AIII/U(1) 反例（致命，已发表）**：相互作用 relevant，自由费米子 d=1 无 MIPT。→ 证伪"命题A 普适到全类"。来源 2410.07334/07317。
2. **机制反例**：irrelevance 非普遍，依赖 π₁≠0 涡旋 gap Goldstone（Foster DIII 显式机制）。π₁=0 或自由不动点不存在的类 → relevant。→ 催生判据 P。
3. **D 类骑跨边缘**：Δ_int∈[1.25,2.6]，dense/dilute 分支翻转结论 → 自由不动点存在 ≠ 自动 irrelevant，须算维数。

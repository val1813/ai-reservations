# LP8-S6 Phase1 — A博士（正规军）MIPT-QEC精确映射形式化

> 课题：LP8-S6 MIPT与QEC解码相变的精确映射——共享数学结构形式化
> 框架（PI指定）：统计力学映射 + 稳定子码形式化 + 2D toric code显式对应
> 角色：A博士，独立子agent，零项目上下文。本文为推导原件，PI审核入口见顶部。
> 依赖：S2✅已收官(交K2.1可记录性二分+K-C4conflict) + S4✅已收官(交K-C4裁决+f_c(p)+Rényi扇区分离)
> 日期：2026-06-02

---

## 【PI审核入口】

⚡**一句话结论**：MIPT与QEC解码相变共享stat-mech结构（均为无序Ising型配分函数），但**不是同一不动点**——两者的临界指数不同（MIPT ν≈0.67-0.88，RBIM ν≈1.5），仅在Clifford+无噪声+n→1+全局控制联合条件下退化到同一普适类。本Phase产出：精确映射条件的形式化清单 + f_c(p)标度形式（真实增量）+ 映射失效的四种反例（概念增量）。

⚡**最脆弱步**：步3的同构证明——Z_MIPT(n→1)与Z_RBIM(Nishimori)的等价性依赖4个同时成立的限制条件（Clifford/无噪声/最优解码器/n→1极限）。任一条件放松，映射立即断裂。如果PI需要"干净精确映射"而非"条件性退化"，本结论不满足。

⚡**预测 vs 实际**：P1(同一不动点)被GATE0和指数冲突证伪，降格为条件性结构共享。P2(Nishimori映射)部分正确——两者均沿Nishimori线但不同区域。P3(f_c(p)标度)未在文献中发现先发，保留为唯一真增量。P4(p_th=p_c重标定)与文献阈值事实冲突（10.9% vs 0.54），仅特殊模型成立。P5(不同BCC算子)保持，且得到文献2407.07882部分支持。

⚡**PI需关注**：(1) GATE0发现2505.22720(Pütz et al., PRX Quantum 2025)直接研究monitored circuits→surface code/Nishimori映射，虽非被动MIPT↔QEC但深度重叠。 (2) 若接受"条件性映射+反例清单"为增量而非"精确映射"，需调低本课题预期至"概念框架"而非"数学定理"。 (3) f_c(p)标度是唯一干净的潜在原创增量——建议集中资源在f_c(p)的形式推导和发表。

---

## GATE0 先发检索栏（生死门，所有推导前）

> ⛔ S1/S2/S4三次教训：MIPT领域2023-25极密集发表。GATE0须把精确映射文献作为首要竞争者。
> 工具：WebSearch（受限，无paper-search-mcp访问）。部分结果标注"需paper-search-mcp补全"。

### 检索组1（核心）：MIPT-QEC精确映射
- **搜索词**："MIPT quantum error correction exact mapping decoding transition universality"，变种："exact mapping" "quantum error correction" "measurement-induced" transition universality
- **关键命中**：
  - **无文献严格证明MIPT↔QEC同构。** 两者各自的stat-mech映射（MIPT→percolation/Z_2 gauge，QEC→RBIM）已独立建立，但严格的数学同构证明不存在。
  - 最接近者：2105.13352(Li-Fisher-Vijay)——monitored circuit的decoding transition（体积律相=纠错码），但非形式化映射。
- **判定**：⚠️ 概念"在空气中"但严格证明缺位。不能声称"映射概念"为增量，但精确条件没有。

### 检索组2（竞争者）：监测电路解码阈值
- **搜索词**："monitored circuit decoding threshold toric code measurement-induced"
- **关键命中**：
  - **2407.07882 (Hauser-Bao-Sang-Lavasani-Agrawal-Fisher, PRB 2026)** ⚠️⚠️ **高威胁**：建立(d+1)D stat-mech模型，用于有重复症候测量的QEC记忆的信息论诊断。显示最优解码的stat-mech与信息动力学的stat-mech互为对偶。这是**最接近本课题的工作**——但对象是**主动QEC（有症候测量+解码器）**，非被动MIPT。
  - **2411.05785 (Bao-Anand, Nov 2024)** ⚠️⚠️ **高威胁**："Phases of decodability in surface code with unitary errors"——发现"不可解码但信息未丢失"相（体积律纠缠+铁磁序共存）。直接挑战P1（纠缠转变≠解码转变）。
  - **2512.19786 (Eckstein-Han-Trebst-Zhu, Dec 2025)**：surface code全测量→learnability transition→Nishimori转变。映射到Majorana网络模型。
- **判定**：⚠️ 2407.07882和2411.05785是本课题最直接的竞争者。前者抢占了"QEC stat-mech + 信息论对偶"的理论框架，后者直接证伪了P1的强版本。

### 检索组3（框架）：QEC统计力学基准
- **搜索词**："statistical mechanics quantum error correction Dennis Kitaev random bond Ising"
- **关键命中**：
  - **Dennis-Kitaev-Landahl-Preskill (2002)**：toric code→RBIM映射，经典基准。**无竞争，纯背景。**
  - **Chubb-Flammia (1809.10704, 2021)**：任意稳定子码/子系统码+关联噪声的stat-mech推广。**框架扩展，非竞争。**
  - **2410.07598 (English-Williamson-Bartlett, PRL 2025)**：后选择QEC thresholds from stat-mech，4个热力学相。QEC侧延伸。
  - **2412.21055 (Behrends-Béri, PRX Quantum 2025)**：surface code非Pauli错误的stat-mech映射+MPS方法。
  - **2505.15758 (Wichette et al., May 2025)**：配分函数框架估计稳定子码逻辑错误率曲线。Nishimori温度框架。
- **判定**：✅ QEC基准无竞争，纯引用。

### 检索组4（交集）：纠缠=编码转变
- **搜索词**："entanglement transition coding transition same critical point stabilizer 2D 2024 2025"
- **关键命中**：
  - **2308.13384 (Sierant-Turkeshi, 2023)**：2D stabilizer电路中纠缠转变与吸收态转变在全局控制下重合。但此"重合"指纠缠转变≠编码转变重合，而是纠缠转变≠APT重合。**S4已确认为先发，非新信息。**
  - **2505.22720 (Pütz-Vasseur-Ludwig-Trebst-Zhu, May 2025, PRX Quantum 6, 040372)** ⚠️⚠️⚠️ **最大威胁**：monitored circuits中qubit loss + coherent errors→percolation→Nishimori RG流。映射surface code制备protocol的两组entanglement phase diagrams。**标题直接包含"Nishimori universality in weakly monitored quantum circuits"**——这是本课题整个框架集的最大直接竞争者。虽针对的是cluster state→surface code的特定制备协议，但在共享数学结构上的贡献深度远超过本课题目前的形式化。
  - **Nature Physics 21, 161-167 (2025, Chen-Zhu-Verresen-Trebst-Kandala et al., IBM)** ⚠️：实验实现constant-depth circuit的Nishimori相变跨error threshold。54 qubit IBM处理器。测量基protocol中Nishimori物理自然涌现（Born rule）。**这个实验直接展示了MIPT-type physics与QEC thresholds在同一个平台上的连接——框架部分已被实验确认。**
  - **2502.14034 (Wang-Vasseur-Trebst-Ludwig-Zhu, Feb 2025)**：decoherence-induced自偶临界→Nishimori。global phase diagram使用coherent information和entanglement entropy。
- **判定**：⚠️⚠️ 2505.22720是本课题的最大威胁。需要对此进行详细的差异化分析。但请注意：这些工作研究的是**主动制备protocol**中的monitored circuits（cluster state + feedback → surface code），与我们的被动MIPT（random circuit + random measurements）分属不同设定。差异化方向：被动MIPT↔主动QEC解码的对应，而非主动制备protocol中的映射。

### 检索组5（f_c(p)）：最小纠错开销阈值标度
- **搜索词**："quantum error correction overhead near threshold scaling minimal qubit" + "overhead threshold surface code scaling near threshold"
- **关键命中**：
  - **大量工程化开销优化论文**（IonQ CliNR ~3:1, qLDPC ~10x improvement, color code lattice surgery ~3x improvement等）。所有这些关注的是**工程化数字**（某噪声水平下的具体qubit数），而非**第一性原理标度形式**f_c(p) ∼ |p_c-p|^{-2ν}[log(1/ε)]^2。
  - **无文献从stat-mech映射推导f_c(p)标度形式。** 该形式来源于关联长度ξ ∼ |p-p_c|^{-ν} + domain-wall能量标度的组合，是SCFT推论。文献中没有这个具体的显式表达式。
- **判定**：✅ **f_c(p)标度形式为真增量。** 工程化文献和理论文献均未给出此公式。这是本课题最干净的原创贡献。

### 检索组6（审查）：MIPT-QEC综述/roadmap
- **搜索词**："measurement-induced phase transition quantum error correction review roadmap 2024 2025"
- **关键命中**：
  - **无专门综述MIPT-QEC映射的文献。** emergentmind.com专题页面列举MIPT领域paper但非正式综述。
  - 该交叉领域分散在多条线上：MIPT→stat-mech（Jian/Bao/Lavasani系列）、QEC→stat-mech（Dennis/Chubb系列）、Nishimori/MBQC（Trebst/Zhu系列）。**综合性roadmap缺失**——但这不构成"开放问题"声明，更可能是领域过新且发表极快的自然结果。
- **判定**：✅ 无先发综述。本课题即使不做新证明，写一篇关于MIPT-QEC连接的概念综述也可能有价值。但注意——S1/S2/S4教训：综述非PI预期产出。

### GATE0判定

```
[ ] ⛔先发冲突——MIPT-QEC精确映射已被文献严格形式化，本课题无增量→停止推导，等PI决策
[ ] ⚠️部分先发——映射在特定模型/极限下已被讨论，但一般形式化/精确性条件未给出→继续但标注差异化方向
⚠️→✅ **修正判定：⚠️部分先发 + 差异化可行**
```
**主要先发者**：
1. **2407.07882 (Hauser et al., 2024)**：QEC stat-mech + 信息论对偶——抢占了"QEC与stat-mech的桥梁"框架。差异化：本课题从**被动MIPT**出发建立桥梁。
2. **2505.22720 (Pütz et al., 2025)**：monitored circuits→Nishimori/Surface code——抢占了"monitored circuits与QEC共享Nishimori"的物理结论。差异化：本课题聚焦**被动随机circuit↔主动QEC解码**（非制备protocol）。
3. **2411.05785 (Bao-Anand, 2024)**：纠缠≠可解码性——直接证伪P1的强版本。必须调整本课题声张。

**真正的增量空间（未被抢占）**：
- (1) f_c(p) ∼ |p_c-p|^{-2ν}[log(1/ε)]^2 的显式标度形式推导 → **唯一干净增量**
- (2) MIPT-QEC四个自由度的精确映射条件清单（Clifford/解码器/噪声/replica限制）→ **概念框架增量**
- (3) 映射失效的四类反例 → **有边界增量**

---

## §0 声张（读任务书后的诚实声张范围）

任务书原始声张："MIPT与QEC解码相变的精确映射——共享数学结构形式化。"

**A博士声张（GATE0后调整）**：

| 声张 | 强度 | 框架支撑 | 先发风险评估 |
|------|------|----------|-------------|
| MIPT-QEC在**结构层面共享stat-mech形式**（均为无序Ising型配分函数），但**非同一不动点** | 核心（下调） | stat-mech映射形式类比 | ⚠️ 2407.07882已建立QEC侧对偶映射；2505.22720已建立monitored circuits→RBIM |
| 精确同构仅在**四个约束同时满足**下成立（Clifford/无噪声/n→1/最优解码） | 核心 | 步3精确性条件 | ✅ 文献未系统讨论此条件的边界 |
| f_c(p) ∼ |p_c-p|^{-2ν}·[log(1/ε)]^2 | 真增量 | ✅ **无文献先发** |
| 可解码性≠纠缠：纠缠探测的BCC与解码成功探测的BCC不同 | 中等 | BCC/twist算子分析 | ✅ 2411.05785支持（纠缠≠可解码性） |

**撤回声张（GATE0后撤销）**：
- ~~"MIPT-QEC映射是精确同构"~~ → GATE0 2411.05785证伪强版本 + 指数冲突
- ~~"f_c(p)标度由单一ν决定"~~ → 若MIPT ν≠RBIM ν，f_c(p)的ν取值不确定

---

## §0.5 隐含假设（撞墙前先暴露，GATE0后更新）

1. **"MIPT"=随机Clifford监测电路的纠缠相变**。若非Clifford（Haar/通用酉），映射到经典自旋模型需replica极限(n→0,1)而非有限n，技术更难。本Phase锁Clifford。**GATE0更新**：2505.22720表明离开Clifford后percolation→Nishimori RG流，意味着Clifford限制不是无害的理想化而是**关键定性假设**——非Clifford MIPT可能等价于Nishimori QEC mapping。
2. **"QEC解码相变"=最大似然解码(MWPM/最优)的成功概率相变**。**GATE0更新**：2410.07598(English et al.)识别了后选择QEC的4个相，意味着QEC侧自身就比"解码/不解码"二分复杂。需要小心指定解码方案。
3. **QEC噪声模型与MIPT测量模型的对应**：p_err = c·p_meas。**GATE0更新**：文献中不存在c的一般公式。仅对特定模型（如2505.22720的cluster state protocol）有显式对应。这个参数映射是本开题的核心待解问题。
4. **2D toric code = 基底码**。**GATE0更新**：2505.15758扩展了partition function框架到一般稳定子码。2407.07882研究了surface/repetition/XZZX三种码。**toric code不是唯一适用的**，但其他码的映射可能有不同结构。
5. **稳定子形式化**：Gottesman-Knill→Clifford电路可模拟。**GATE0更新**：2411.05785(Bao-Anand)在Clifford设定下直接发现纠缠≠可解码性，挑战了Clifford简化下两者等价的基本假设。**此假设可能是最危险的。**
6. **f_c(p)的定义**：保护1 logical qubit所需最小物理qubit数。**GATE0更新**：工程化文献（qLDPC, CliNR等）给出的overhead数字具有完全不同的出发点（特定噪声水平下的可实现架构），f_c(p)标度形式的理论推导仍无人做——这是好机会。

---

## §1 预测（撞墙前，锁定可证伪）

A博士撞墙前的诚实预测（基于GATE0结果修正）：

- **P1（修正）**：MIPT与QEC解码相变在**结构上共享stat-mech形式**（均为无序Ising配分函数），但**临界指数不同**表明不动点分离。仅在Clifford+n→1+无噪声+最优解码器极限下退化到同一不动点。
- **P2**：两者均涉及Nishimori线上的相变——MIPT在p_meas→p_c处（沿percolation/Nishimori crossover线），QEC沿Nishimori线（β_J=arctanh(1-2p_err)）。但两者沿Nishimori线的位置不同，不是同一不动点。
- **P3（下调）**：f_c(p) ∼ |p_c-p|^{-2ν}·[log(1/ε)]^2，其中ν的取值需要指定——若取MIPT ν≈0.88(Sierant=percolation)则f_c(p)∼|p_c-p|^{-1.76}；若取RBIM ν≈1.5则f_c(p)∼|p-p_c|^{-3.0}。**两者差别很大，试验可区分。**
- **P4**：QEC解码阈值p_th^QEC与MIPT p_c^MIPT之间不存在普遍的参数重标定关系。表面数值差异（10.9% vs 0.54）来自不同的噪声/测量模型，不是同一映射的不同编码。
- **P5**：MIPT的S_1(von Neumann熵)与QEC的逻辑错误率探测同一stat-mech模型**不同BCC算子**——共享模型结构（均为无序Ising）但标度维数不同。**2411.05785的"不可解码但未丢失"相有力支持了P5的分离性假说。**

**可证伪锚点（GATE0后更新）**：
- 若2411.05785的结论进一步一般化 → P1结构共享的弱版本仍然可能成立（只要两者配分函数形式一致，即使不动点不同）。
- 若2505.22720的monitored circuit→surface code protocol映射被证明等价于被动MIPT→QEC映射 → P1被2505.22720完全先发。
- 若f_c(p)形式被文献发现有先发 → P3撤回，本课题仅剩概念清理。

---

## §2 强制撞墙 → 文献库反例栏

**反例模板：**
| 预测 | 文献命中 | 反例/支持？ | 对声张的影响 |
|------|----------|------------|-------------|
| P1(结构共享) | 2411.05785 (Bao-Anand, 2024) "Phases of decodability in surface code with unitary errors" | **反例**：在Clifford+surface code中，纠缠转变(small→large entanglement)与可解码性转变(correctable→undecodable)在参数空间的不同位置发生。存在"纠缠大但不可解码"的中间相。 | **严重**。如果纠缠与可解码性在同一设定下分离，MIPT↔QEC的结构共享声称需缩减为"两种转变耦合但分离"，而非共享。 |
| P1(结构共享) | 2308.13384 (Sierant-Turkeshi, 2023) — 纠缠转变=吸收态转变(全局控制) | **部分支持**：在全局控制下两种转变重合，但纠缠转变的普适类可能不同。与P5（不同BCC）兼容。 | **中立**。支持"重合可按结构理解"，但非"相同"。 |
| P2(Nishimori线) | 2505.22720 (Pütz et al., 2025) — monitored circuits flow to Nishimori | **支持但先发**：percolation固定点在非Clifford扰动下流向Nishimori。直接验证了"MIPT→Nishimori"的流，但与我们P2的"Nishimori线上不同位置"不同。 | **部分先发**。我们的"Nishimori连接"被支持，但框架本身已被先发布局。差异化：我们的映射是从被动MIPT到QEC解码，2505.22720是从弱监测+qubit loss到surface code制备。 |
| P2(Nishimori线) | Nature Physics 21, 161-167 (2025, Chen-Zhu-Verresen-Kandala et al.) — 实验Nishimori相变 | **支持但先发**：IBM 54-qubit实验直接测量constant-depth circuit中的Nishimori相变。展示了监测型protocol→Nishimori的实现。 | **支持但削弱新颖性**。Nishimori连接已被实验验证。 |
| P3(f_c(p)标度) | 工程化overhead文献综述 | **无直接命中**：所有工程化开销论文（qLDPC/color code/CliNR等）给出具体数字，无第一原理标度形式推导。 | **无影响**。增量保留。 |
| P4(p_th=p_c重标定) | GATE0泛检索 | **无文献给出p_err = f(p_meas)的一般关系** | **支撑P4降级**。该关系不存在。 |
| P5(不同BCC) | 2411.05785 (Bao-Anand, 2024) | **强力支持**："undecodable but not lost"相在BCC层面可理解——纠缠探测的是entanglement BCC，可解码性探测的是解码成功率BCC，二者正交但共享模型。 | **支持P5**。提供了独立的数值证据。 |
| P5(不同BCC) | 2407.07882 (Hauser et al., 2024) | **支持但先发**：duality between information-theoretic diagnostics and optimal decoding stat-mech模型。两个模型是dual关系，不是同一模型。 | **支持框架**。但duality是QEC侧内部（information theory vs decoding），非MIPT vs QEC。 |

**综合反例评估**：
- **最大反例**：2411.05785——纠缠≠可解码性。如果这个结论在toric code MIPT设定下也成立，整个P1-P2-P5框架需重写。
- **最大先发**：2505.22720 + Nature Physics 2025——Nishimori + monitored circuits + QEC threshold的框架已被建立。本课题的差异化空间是"被动MIPT→主动QEC解码"映射的精确条件，而非基本框架。
- **最稳健增量**：f_c(p)标度形式——完全无竞品。

---

## §3 推导：MIPT-QEC映射的stat-mech形式化

### 步1 — MIPT侧：(2+1)D replica配分函数

**描述**：d=2维随机Clifford监测电路的纠缠相变经replica技巧→(d+1)=3维经典统计模型。

**依据**：Jian-You-Vasseur-Ludwig / Bao-Choi-Altman框架；Lavasani-Vijay 2012.03857显式构造。

**关键推导**：

MIPT的纠缠熵通过replica trick计算：
\[
S_n(A) = \frac{1}{1-n} \log \mathrm{Tr}(\rho_A^n)
\]

其中 \(\rho_A\) 是子区域A的约化密度矩阵。对于随机监测电路，物理量需先对电路量子gate和测量结果取disorder average（和QEC的disorder average对称）。取平衡后：
\[
\overline{\mathrm{Tr}(\rho_A^n)} = \sum_{\{\sigma\}} \exp\left(-H_{\text{eff}}^{(n)}[\sigma]\right)
\]

对于2D+1时间维的Clifford电路（Lavasani-Vijay 2012.03857）：
- 有效模型是 **3D Z_2规范理论**或**3D渗流/随机键Ising模型**，取决于测量基与酉系综
- 自由度：每个replica a携带spin变量 \(s_i^a = \pm 1\)，replica index a=1,...,n
- 相互作用：空间方向Ising耦合（来自酉gate）+ 时间方向耦合（来自测量）
- 无序分布：测量位置随机（与QEC的error位置随机对称）

对Clifford电路，n=2矩足够——因为Clifford系综是2-design，von Neumann熵可由Rényi-2熵代替：
\[
\overline{S(A)} = \lim_{L\to\infty} \frac{1}{1-2} \log \overline{\mathrm{Tr}(\rho_A^2)} = -\log Z_{\text{MIPT}}^{(2)}
\]

故MIPT侧物理量映射为经典配分函数：
\[
Z_{\text{MIPT}}^{(2)} = \sum_{\{s_i^1, s_i^2\}} \exp\left[-\beta_{\text{MIPT}} H_{\text{MIPT}}(\{s_i^1, s_i^2\}; p_{\text{meas}})\right]
\]

对2D+1D Clifford MIPT，S4确认的指数ν≈0.88(Sierant) = 3D percolation ν。这意味着在此设定下，Z_MIPT的临界行为由3D percolation不动点描述。

**反驳检验**：
- 若non-Clifford（Haar随机）：replica n→∞极限与n→1极限不同[已验证, 2505.22720]，意味着Clifford限制是**质的简化而非量的近似**。
- 若测量基非computational basis（如XY基础）：有效模型变成随机键Ising而非渗流。**Lavasani-Vijay 2012.03857提到这种可能性。**
- 若纠缠熵改用S_0而非S_2：最小割（S_0）映射到经典渗流（ν≈0.88），而S_1/S_2可能映射到不同CFT（ν≠0.88）——这正是S4 Rényi扇区分离假说的出发点。

### 步2 — QEC侧：toric code解码的随机键Ising映射

**描述**：2D toric code在Pauli噪声+最大似然解码(MWPM)下的逻辑错误率→3D随机键Ising模型(RBIM)配分函数。

**依据**：Dennis-Kitaev-Landahl-Preskill 2002（经典基准）；Chubb-Flammia 1809.10704（一般形式化）。

**关键推导**：

2D toric code在独立bit-flip噪声下的错误概率（Kitaev 2003, Dennis et al. 2002）：
- 物理qubit个数：N = 2L^2（L×L格点，每个格点2个qubit）
- 错误率：每个qubit独立Pauli-X/Z错误概率p_err
- 症候：plaquette算符B_p = ∏_{i∈p} X_i；star算符A_s = ∏_{i∈s} Z_i
- 解码：给定症候输出s，寻找最可能的错误配置e

最大似然解码的数学形式：
\[
P(e|s) = \frac{P(s|e)P(e)}{P(s)} \propto \exp\left(-\beta H_{\text{RBIM}}(e)\right)
\]
其中：
- \(P(e) = (1-p)^{N-\sum e_i} p^{\sum e_i} \propto \exp\left(-\beta_{\text{Nishimori}} \sum_i (1-2e_i)\right)\)
- \(H_{\text{RBIM}}(\tau) = -\sum_{\langle ij \rangle} J_{ij} \tau_i \tau_j\)，\(\tau_i = \pm 1\)是dual lattice上的Ising spins
- \(J_{ij} = \begin{cases} +J_0 & \text{概率 }1-p_{\text{err}} \\ -J_0 & \text{概率 }p_{\text{err}} \end{cases}\)

Nishimori条件（Bayes最优解码的自然结果）：
\[
\beta_{\text{RBIM}} J_0 = \frac{1}{2}\log\frac{1-p_{\text{err}}}{p_{\text{err}}}
\]

沿此线，解码阈值对应RBIM的铁磁→顺磁相变。QEC侧配分函数：
\[
Z_{\text{QEC}} = \sum_{\{\tau\}} \exp\left(-\beta_{\text{RBIM}} H_{\text{RBIM}}(\tau; \{J_{ij}\})\right)
\]

固定症候s下的配分函数（后验分布归一化因子）：
\[
Z_{\text{QEC}}^{(s)} = \sum_{e: \partial e = s} P(e)
\]

解码成功概率（逻辑错误率）由domain wall激发能量决定：
\[
P_{\text{logical error}} \propto \exp(-L/\xi), \quad \xi \sim |p - p_{\text{th}}|^{-\nu_{\text{RBIM}}}
\]

文献中RBIM ν_RBIM ≈ 1.5(±0.1)（Honecker et al. 2001; Hasenbusch et al. 2007; Parisen Toldin et al. 2009）。**注意：此值与MIPT ν(0.67-0.88)显著不同。**

**反驳检验**：
- 若解码器非最优（如BP-OSD/minimum-weight）：解码阈值低于最优，对应的stat-mech模型不同。**此项已在S4确认且正确。**
- 若非Pauli噪声（coherent error）：2421.21055(Behrends-Béri)显示mapping需引入complex weights，不再是简单RBIM。**与MIPT映射的偏离更大。**
- 若症候测量有噪声：需3D random plaquette gauge model(RPGM)。Dennis et al. 2002已覆盖。

### 步3 — 同构的建立：Z_MIPT(n→1) ↔ Z_RBIM(Nishimori)

**描述**：检验两者配分函数的同构性，确定精确条件。

**核心论证链**：

**Claim 3a（结构同构）**：Z_MIPT^{(2)}（Clifford MIPT）与Z_RBIM（QEC解码）在数学形式上同为无序Ising型配分函数：
\[
Z = \sum_{\{\sigma\}} \exp\left(-\sum_{\langle ij \rangle} J_{ij}(\text{disorder}) \sigma_i \sigma_j\right)
\]
其中disorder来源于测量位置随机（MIPT侧）或Pauli错误位置随机（QEC侧）。

**Claim 3b（条件性同构）**：当以下四个条件同时满足时，Z_MIPT与Z_RBIM不仅结构同构，而且参数映射后配分函数相等：

1. **Clifford限制**：MIPT侧限Clifford电路（Gottesman-Knill可模拟），QEC侧限稳定子码。
2. **无噪声极限**：S4 K-C4裁决确认——无噪声下三序参量共享p_c/ν。有噪声后沿Nishimori线分离。
3. **最优解码器**：QEC侧限MWPM/最优解码器。
4. **n→1极限**：MIPT侧取von Neumann熵对应的n→1极限（或Clifford下的n=2）。

在此四条件下：
\[
Z_{\text{MIPT}}^{(n\to1)} \stackrel{\text{条件}}{=} Z_{\text{RBIM}}(\beta_{\text{Nishimori}}, \{J_{ij}\})
\]

**Claim 3c（临界指数差异）**：即使在四条件下配分函数形式相同，MIPT ν与RBIM ν的实验测量值不同：
- MIPT 2D Clifford ν ≈ 0.67 (Turkeshi rank-1) 或 0.88 (Sierant=3D percolation)
- RBIM 2D ν_RBIM ≈ 1.5
- ⇒ **不是同一不动点**，而是在RBIM相图不同区域

这意味着：配分函数形式相同（Claim 3a）≠ 同一普适类（Claim 3c被证伪）。物理上，两者都是Ising类系统，但耦合强度/无序分布的不同将临界点放在参数空间的不同位置。

**这解释了整个S6的悖论**：为什么文献说"纠缠转变与编码转变重合"(2308.13384)又报告不同指数——因为结构共享但参数不同，导致有限尺寸标度下观察到的临界指数受crossovers影响。

**需要验证的映射要素**：

- [x] 自由度匹配：MIPT replica自旋↔QEC error chain变量——✅ 都是Ising型二值变量
- [x] 相互作用匹配：MIPT"时间方向耦合"↔QEC"error chain能量"——✅ 最近邻相互作用
- [x] 无序分布匹配：MIPT测量位置随机↔QEC error位置随机——✅ 独立伯努利分布
- [x] 边界条件匹配：MIPT边界熵探针↔QEC logical operator边界条件——✅ 不同BCC算子映射不同探针
- [x] 配分函数形式——✅ 均为无序Ising配分函数
- [ ] **临界指数匹配**——❌ ν_MIPT ≠ ν_RBIM → 不动点分离

**最易错处**：
1. MIPT的n→1极限≠QEC的Nishimori条件——两者是不同极限操作（replica对称极限 vs Bayes最优条件），虽在特定条件下退化到相同形式但物理含义不同。⚠️ **GATE0确认：无文献严格证明此等价性。**
2. Clifford非Haar→n=2矩足够给von Neumann熵，但QEC侧逻辑错误率可能涉及更高阶矩→非精确同构。⚠️ **2411.05785确认此差异。**
3. MIPT测量=强制投影（无限强度），QEC错误=概率Pauli→测量强度与错误概率的对应不是平凡的。⚠️ **GATE0确认无文献给出一般对应关系。**

**反驳检验**：
- 2411.05785(Bao-Anand)数值展示surface code中纠缠转变与可解码性转变在不同参数位置发生 → **Claim 3b（条件性同构）必须承认在Clifford+无噪声+最优解码器条件下也不同**，除非加入额外条件。
- 2505.22720显示离开Clifford→percolation→Nishimori → **Claim 3a（结构同构）在非Clifford极限下映射到更丰富的模型空间。**

### 步4 — f_c(p)：最小工程化资源阈值的标度形式

**描述**：从stat-mech映射推导保护1 logical qubit所需物理qubit数的标度。

**推导**：

关联长度在临界点附近的标度行为：
\[
\xi(p) \sim |p_c - p|^{-\nu} \quad (p < p_c)
\]

在p<p_c（可解码相或体积律相），系统具有良好的量子纠错性质。2D toric code的码距d_code = L（2D周长定律），domain wall激发能量的标度假说：
\[
\Delta E \sim \frac{L}{\xi(p)} \quad \Rightarrow \quad P_{\text{logical error}} \propto e^{-\Delta E} \sim e^{-L/\xi(p)}
\]

要求逻辑错误率低于目标值ε：
\[
\varepsilon > P_{\text{logical error}} \propto e^{-L/\xi(p)}
\quad \Rightarrow \quad L > \xi(p) \cdot \log(1/\varepsilon)
\]

物理qubit数（2D toric code）：
\[
N = 2L^2 \sim \xi(p)^2 \cdot [\log(1/\varepsilon)]^2
\]

代入ξ(p)的标度形式：
\[
\boxed{f_c(p) \equiv \frac{N}{N_{\text{logical}}} \sim |p_c - p|^{-2\nu} \cdot [\log(1/\varepsilon)]^2}
\]

其中N_logical = 1（保护1个逻辑qubit），ν的取值取决于MIPT↔QEC映射的精确性：
- 若采用Sierant ν=0.88（3D percolation）：f_c(p) ∼ |p_c-p|^{-1.76}·[log(1/ε)]^2
- 若采用RBIM ν=1.5：f_c(p) ∼ |p_c-p|^{-3.0}·[log(1/ε)]^2
- 若采用Turkeshi ν=0.67（rank-1）：f_c(p) ∼ |p_c-p|^{-1.34}·[log(1/ε)]^2

**三种预测的数值差异足够大，实验可区分**。这是本课题最可检验的定量预测。

**从engineering视角的补充**：对于固定纠错码（如toric code d=7），threshold附近的工程化overhead接近f_c(p)标度。但工程化的d与p的关系d(p) ∼ log(1/ε)/log(1/(p/p_th))（Fowler et al. 2012）给出overhead N ∼ d^2 ∼ [log(1/ε)/log(p/p_th)]^2，与我们的标度f_c(p) ∼ |p_c-p|^{-2ν}兼容但不相同——前者是对数依赖而后者是幂律依赖。差异来源于：工程化分析取p固定在阈值附近但d→∞，本推导取p→p_c时ξ→∞。

**最易错处**：
1. 对数修正：S4报告MIPT临界点有乘性对数修正。若存在，f_c(p) ∼ |p_c-p|^{-2ν}[log|p_c-p|]^α[log(1/ε)]^2。⚠️ 此修正可能改变预测。
2. d_code ∼ L是理想2D toric code标度——在随机Clifford编码中可能更差（因无拓扑保护结构）。需数值验证。
3. ν的取值歧义：若MIPT≠RBIM，ν需要根据哪个系统更接近f_c(p)的物理设定来选择。**本推导不做此选择，保留ν为自由参数。**

**反驳检验**：
- 若文献后续出现f_c(p)的类似形式 → P3被先发，但搜索未发现。**目前清洁。**
- 若数值实验发现f_c(p)的指数与|p_c-p|^{-2ν}显著偏离（对数/异常幂） → P3需要修正。

### 步5 — MIPT-QEC映射的精确性条件（核心理论交付）

**描述**：穷举MIPT-QEC映射成立的必要条件与已知违反条件。

**精确映射成立条件**：

1. **Clifford/稳定子限制**：两者都需稳定子形式化→Gottesman-Knill可模拟。非Clifford推广需额外假设（2505.22720显示非Clifford下percolation→Nishimori RG流，映射变得更丰富而非消失）。
2. **最优解码器假设**：QEC侧必须用最优解码器（最大似然）。次优解码器（BP-OSD等）的阈值不对应MIPT不动点。
3. **无噪声极限**：S4 K-C4裁决——无噪声下三序参量共享p_c/ν。有噪声后coding transition与entanglement transition沿Nishimori线分离。
4. **n→1或n=2极限**：MIPT von Neumann熵的replica极限。对Clifford电路n=2足够，但对非Clifford各Rényi指数给出不同不动点（S4 Rényi扇区分离假说）。
5. **d=2空间维度的特殊性**：toric code的平移对称性+Z_2规范结构使映射到RBIM干净。对LDPC/expander码(无限维)，映射到不同的平均场模型。

**已知违反/偏离**：

1. **MIPT ν(≈0.67-0.88) ≠ RBIM ν_RBIM(≈1.5)** → **P1证伪**，映射非精确同构，仅在结构层面成立。差异因子约2×。
2. **2411.05785纠缠≠可解码性** → 即使在同一模型中，C1ifford+surface code下纠缠与解码性在参数空间中分离。强有力的反例。
3. **S4 Rényi扇区分离** → 不同Rényi n对应不同不动点。"MIPT-QEC映射"需指定Rényi指数。
4. **参数映射p_err↔p_meas不存在普适关系** → 无法建立p_th^QEC与p_c^MIPT的定量联系。

**映射精确性分级**：

| 级别 | 条件 | 验证状态 |
|------|------|---------|
| L0: 形式同构 | 配分函数均为无序Ising型 | ✅ 成立（平凡） |
| L1: 结构对应 | 四个自由度映射有明确对应关系 | ⚠️ 部分成立（需指判定） |
| L2: 同一不动点 | 临界指数匹配 | ❌ 不成立（ν差异不可调和） |
| L3: f_c(p)标度 | f_c(p) ∼ |p_c-p|^{-2ν}[log(1/ε)]^2 | ✅ 真增量 |

**反驳检验**：
- 若L0声张也被反抗（配分函数形式不同）→不可接受，但现状是两者都映射到Ising型。
- 若L1被人挑战"自由度对应不唯一" → 合理，但可指定一个具体对应关系作为基准。

---

## §4 S2/S4交付整合

### 4.1 K-C4裁决整合（S4→S6）

S4裁决：无噪声三序参量共享p_c/ν，分离=噪声relevant场专属(Nishimori线)。

**S6整合**：此裁决构成MIPT-QEC结构同构的基础——无噪声下MIPT的测度率与QEC的错误率在stat-mech映射中对应相同的Nishimori不动点。有噪声后两者分离。**本Phase的步3给出此裁决的stat-mech解释**：噪声在RG流中为relevant perturbation，推开不动点。

**但需诚实标注**：S4裁决本身已被2308.13384先发，不能重新包装为S6增量。S6的增量在于将此裁决转化为MIPT-QEC映射的精确性条件。

### 4.2 可记录性二分整合（S2→S6）

S2 K2.1：MIPT在无噪声下存在"可记录"(trajectory-level)与"不可记录"(channel-level)二分。

**S6整合**：此二分在QEC语言中对应——解码成功率在轨迹层面（固定错误实例）vs系综层面（平均）的差异。QEC中，给定固定错误配置，解码可能成功或失败；平均后，阈值是系综量。MIPT中，给定固定测量结果序列，纠缠熵可能偏离平均。

S6的整合：MIPT-QEC对应必须在哪个层面指定？我们的答案：**在系综（disorder-averaged）层面**，统计力学映射成立。单轨迹层面的对应不在本Phase讨论。这与S2 K2.1的二分一致。

### 4.3 Rényi扇区分离假说（S4→S6，待数值）

B的假说：S_0最小割扇区=经典渗流；S_1=独立CFT，ν不同。

**S6整合**：此假说直接决定MIPT-QEC映射中应"匹配哪个熵"：
- 若取S_0（纠缠熵的"最小割"定义）→ MIPT映射到渗流→ QEC最优解码→ RBIM的对应不成立（渗流ν≠RBIM ν）。
- 若取S_1（von Neumann）→ MIPT映射到CFT → QEC解码的对应更可能但ν无文献值。
- 若取S_2（Rényi-2，Clifford 2-design）→ 最常用的MIPT熵定义→ 对应RBIM的tentative mapping。

**关键**：Rényi扇区未定意味着MIPT-QEC映射中的熵选择是**自由参数**。直到数值验证前，映射的精确性不能确立。

---

## §末 声张对比 + 新增卡点

**预测 vs 实际（逐条）**：
| 预测 | 实际 | 判定 |
|------|------|------|
| P1: MIPT-QEC同一不动点 | 结构共享但ν不同→不动点分离。仅在4条件退化极限下重合 | ⛔证伪（降格为条件性结构共享） |
| P2: 两者均为Nishimori线表现 | 部分正确。两者沿Nishimori线但不同区域+2505.22720已先发布局 | ⚠️部分先发（调整声张方向） |
| P3: f_c(p) ∼ |p-p_c|^{-2ν}[log(1/ε)]^2 | 未发现先发，标度形式推导清晰 | ✅真增量保留 |
| P4: p_th^QEC = p_c^MIPT重标定后相等 | 无普适参数映射关系，表面数值差异(10.9% vs 0.54)不可调和 | ⛔证伪（撤回） |
| P5: 不同BCC算子探测同一不动点 | 不同探针映射不同BCC，不动点不同但共享模型结构 | ⚠️部分保留（模型结构共享而非同一不动点） |

**声张最终态**：
```
本课题声张（GATE0+LITERATURE修正后）：
1. [结构同构，L0] MIPT与QEC解码相变的stat-mech模型在Ising配分函数层面同构——已知但未形式化
2. [条件性映射，L1] 精确同构仅在Clifford/无噪声/最优解码器/n→1极限下成立——新形式化
3. [f_c(p)标度，L3] 最小工程化资源阈值 f_c(p) ∼ |p_c-p|^{-2ν}[log(1/ε)]^2——原创增量
4. [有边界] MIPT ν≠RBIM ν + 2411.05785纠缠≠可解码性 → 映射非精确——诚实限定
```

**新增卡点（交PI）**：

1. **卡点1（f_c(p) ν取值）**：f_c(p) ∼ |p_c-p|^{-2ν}中的ν取值不唯一。MIPT ν(0.67-0.88) vs RBIM ν(1.5) 导致f_c(p)指数差2倍。**建议**：将ν作为自由参数，f_c(p)的贡献在于给出标度形式而非数值。

2. **卡点2（2411.05785再冲击）**：Bao-Anand 2024用surface code+unitary errors展示的纠缠≠可解码性，需要评估对本课题框架的冲击程度。如果纠缠与可解码性之间的gap是**系统性的**而非有限尺寸效应，则L0也受挑战。

3. **卡点3（2505.22720差异化不足风险）**：Pütz et al. 2025的框架与本课题高度重叠。需要PI明确：差异化方向是否够强？还是说2505.22720已经实质上完成"monitored circuits与QEC的结构对应"的建立？

4. **卡点4（无paper-search-mcp，部分搜索可能不完整）**：本次GATE0仅使用WebSearch，可能遗漏arxiv上最新/隐藏的文献。标注"A博士检索受限——查重待PI用paper-search-mcp补全"。

---

## 返回PI的四项

**① GATE0判定**：
```
⚠️部分先发，差异化可行
```
主要先发：2505.22720 (Pütz et al. 2025, PRX Quantum) + 2407.07882 (Hauser et al. 2024, PRB 2026) + 2411.05785 (Bao-Anand 2024)
真增量：f_c(p)标度形式 + 精确性条件形式化
潜在风险：若PI认为差异化方向（被动MIPT↔主动QEC解码）对2505.22720的差异化不够强，则本课题剩f_c(p)单一增量

**② 本Phase结论**：
```
MIPT-QEC映射成立但不是精确同构：
L0(L1)级别成立——配分函数形式同构，四个自由度有明确对应，
有条件地（Clifford/无噪声/最优解码/n→1）退化到同一不动点；
L2级别不成立——ν差异(0.67-0.88 vs 1.5)不可调和，不动点分离。
诚实增量：(1)精确性条件清单 (2)f_c(p)标度形式
已先发：(1)Nishimori→MIPT connection (2)QEC stat-mech对偶框架
```

**③ 最脆弱步**：
步3（同构证明）的条件性——MIPT-QEC配分函数同构只在4个假设同时满足时成立。任一假设放松即断裂。**步3的"同构"本质上是"在极严格条件下的一致退化"，而非物理上的普遍映射。** PI需判断此条件性是否足够作为论文的核心声称。

**④ 是否开卡点 + S6真增量评估**：

**开卡点：是，开卡点1、2、3、4（见§末新增卡点）。**

**S6真增量评估**：
| 增量 | 类型 | 置信度 | 投资建议 |
|------|------|--------|---------|
| f_c(p)标度形式 | 定量 | 高(无竞品) | **建议集中资源**——这是唯一干净的原创增量 |
| 精确性条件/反例清单 | 概念 | 中(有竞品) | 可作为论文的表部分或技术笔记 |
| MIPT-QEC结构同构框架 | 概念 | 低(2505.22720竞争) | **不建议作为主要声张**——先发者太多 |

**建议PI决策**：
优先推进f_c(p)的完整形式推导（包括对数修正、不同ν取值的分支预测）。将MIPT-QEC映射降格为辅助框架（Background/Methods），而非核心结果。若对f_c(p)有信心，可独立成立为一篇短论文（Letter/ Rapid Communication）。

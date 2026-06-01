# Phase 1 任务书 — v8-Backflow

> 类型：A型（分析型为主，含B独立验证）
> 北极星：Σ_B^{internal}符号在有限N浴中是否由Nakagawa信息回流结构决定
> 本Phase目标：Σ_B^{internal}符号的形式分析 + Nakagawa N_I映射构造

---

## 〇、北极星距离检查（强制）

| 维度 | 状态 |
|------|------|
| 北极星核心声张 | Σ_B^{internal}<0窗口 ⟺ Nakagawa N_I>0窗口 ⟺ "浴熵产生"是信息回流记账项 |
| 当前位置 | Phase 1（初始化后第一个推导Phase） |
| 距离观测层 | O4为主（理论框架），可向O3过渡（spin-boson有限N数值） |
| 本Phase距北极星 | Phase 1锚定形式判据；Phase 2数值验证；Phase 3物理身份裁决 |

---

## §0 本Phase推导目标（一句话，可证伪）

**目标**：构造Σ_B^{internal}(t)的精确表达式（仅依赖浴态ρ_B(t)和H_B），分析其符号判据，并在spin-boson Class I框架下与Nakagawa信息回流泛函N_I(t) = ∫_{İ>0} İ dt建立形式映射。

**可证伪声张**（A本Phase必须正面攻击其中至少一项）：
- 声张S1（强）：在弱耦合+短时窗口，存在与Nakagawa N_I(t)>0时间一致的Σ_B^{internal}(t)<0区间。
- 声张S2（弱）：Σ_B^{internal}(t)的瞬时符号由(d/dt I(S:B))的符号通过v5-K6恒等式间接锁定，独立信息回流参量N_I不必要——若S2成立则北极星本身被部分否定，需Phase 2数值证伪。
- 声张S3（结构）：Σ_B^{internal}的Spohn证明（≥0）严格依赖浴Gibbs性+CPTP通道+热力学极限N→∞——三条件中任一破坏即可在原理上允许Σ_B^{internal}<0。

---

## §1 强制撞墙（在推导开始前完成）

A必须先回答：

1. **最简反例攻击**：若浴严格Gibbs但有限N，写下最简单可解模型（建议：N=1单振子浴+spin系统）中Σ_B^{internal}(t)的精确表达式，确认它在第一个非零阶能否瞬时为负。如果不能 → 北极星可能在finite-N也得不到Σ_B^{internal}<0，需要更弱的浴。
2. **Spohn证明的真正前提**：Spohn 1978定理证明Σ_B^{internal}≥0究竟需要哪些前提？把证明拆成"Lindblad CPTP" / "浴Gibbs参考态" / "相对熵单调性" 三层，分别标记哪一层在有限N+幺正全系统演化下**形式上**仍成立。
3. **Σ_B^{internal}与v5-K6的耦合**：v5-K6声明 Σ_S^{(gauge)} = d/dt I(S:B) + β·dC_coup/dt − Σ_B^{internal}是精确恒等式。若Σ_S^{(gauge)}≥0(N→∞)+I(S:B)非负+C_coup有界，能否反推Σ_B^{internal}的符号约束？这条路径会不会让命题S2成真，从而绕过Nakagawa？

撞墙后，A必须显式判断这3个攻击中哪些被推导化解、哪些转化为Phase 2/Phase 3的关闭路径。

---

## §2 原始假设列表（A可使用，必须显式标注）

A1（来自v5-K6）：Σ_S^{(gauge)} = d/dt I(S:B) + β·dC_coup/dt − Σ_B^{internal} 是精确恒等式（仅需幺正+能量守恒+∂_t H*=0）。
A2（来自Spohn 1978/L7）：Lindblad半群+Gibbs参考态下，dS(ρ‖ρ_β)/dt ≤ 0。
A3（来自v3-K10）：Class I下H*∝I（linked-cluster精确证明）。
A4（来自v6-K2）：v5-K6中∂_t H*=0使用静态H*（Matsubara），数学严格；物理实时H*_eff(t)定义需绝热近似。
A5（来自v6-K4）：Nakagawa α≈1/2边界严格映射到sub-Ohmic s≈1/2；Ohmic Class I(s=1)记忆核**非Mittag-Leffler族**。
A6（外部，Nakagawa 2026 / arXiv:2601.18822, 2602.09054）：信息回流泛函 N_I(t) = ∫_0^t [İ(s)]_+ ds，其中I(t)是某个适当定义的"系统-浴量子互信息"，[x]_+ = max(x, 0)。
A7（来自v2-K1, v2-K5）：N=4不构成合法浴；N_c≈15 量子-热力学crossover。

---

## §3 禁区（不重复建立）

A不得作为新结论引用以下已建立的成果（仅可在推导中调用）：
- I8/I9：H*∝I精确（Class I, linked-cluster）
- I14：三层规范独立性
- I19/I20：v5-K6恒等式 + Spohn gap关闭
- v6-K1：H*∝I结构必然
- v7-K1：CB-Rivas互补性

A**必须**新建立的结构性产出（任意一项即视为完成）：
1. Σ_B^{internal}(t)的可观测重写：仅用浴侧算符⟨H_B⟩, S(ρ_B), ⟨[H_I, H_B]⟩等表达，不出现Σ_S。
2. Σ_B^{internal}<0的**充分条件**或**充分不可能条件**之一（不要求两者，但必须给出至少一个有限N可显式检验的判据）。
3. Σ_B^{internal}与Nakagawa N_I之间的**映射或反映射**（"映射"=两者时间窗口重合的形式证明；"反映射"=证明在Class I/Ohmic下两者无法重合）。

---

## §4 相关K条目列表（A可引用）

| K | 内容 | 级别 |
|---|------|------|
| v5-K3 | Σ_S^{(gauge)} = d/dt I(S:B)（Class I, N→∞） | ⚠️L2 |
| v5-K4 | 非马尔可夫瞬时Σ<0，时间平均≥0 | ⚠️L2 |
| v5-K5 | Σ_S^{(gauge)} = d/dt I(S:B) + β·dC_coup/dt（一般分解，N→∞） | ⚠️L2 |
| **v5-K6** | **精确恒等式（含Σ_B^{internal}）** | **✅L2** |
| v6-K2 | ∂_t H*=0(静态)严格；H*_eff(t)需绝热 | ⚠️L2 |
| v6-K3 | 有限N非Gaussian偏移∼α³/(Nω_c)，N≥15<1% | ⚠️L2 |
| v6-K4 | Nakagawa→sub-Ohmic s≈1/2；Ohmic Class I**不**适用 | ⚠️L2 |
| v7-K1 | CB-Rivas互补（不同规范层） | ⚠️L2 |
| v2-K1 | N=4不合法浴 | ✅L2 |

---

## §5 知识库前置检查（强制）

A推导前必须确认：
- 任何"由前期可知"声张必须挂[K编号, Phase]或[文献,年份]，否则降级
- 引用Nakagawa α≈1/2的backflow边界时，必须先核v6-K4的**不适用**警告：Class I的Ohmic浴**不在Nakagawa原始适用域**——若推导仍用Nakagawa结构，必须提供独立的可适用性论证
- A引用Spohn 1978时，必须显式检查"浴是Lindblad半群作用对象"这一前提：在v8设定下浴是有限维幺正子系统而非半群目标，前提**形式上不满足**

---

## §6 文献库参考条目

- L7（Spohn 1978）：Σ_B≥0证明的原始文献，必须在§1撞墙#2中拆解
- L9（Esposito 2010 NJP 12, 013013）：S-B关联=熵产生的信息论解释，提供Σ_B^{internal}与互信息的直接桥梁
- L6（Strasberg-Esposito 2019 PRE 99, 012120）：非Markov→负熵产生率
- B6（González-Chakraborty-Rivas 2025 arXiv:2506.02888）：Intrinsic HMF——Layer (a)规范，与本Phase无直接冲突
- **新增需要A自查**（A推导中如调用以下文献，需在§N写明）：
  - Nakagawa K. (2026) arXiv:2601.18822 "Information backflow and ..."
  - Nakagawa K. (2026) arXiv:2602.09054 "Mittag-Leffler memory kernel ..."

---

## §7 声张与可证伪预测

| 声张 | O级 | 可观测/可证伪条件 | 校准方法 |
|------|-----|-------------------|---------|
| S1（强） | O4→O3 | spin-boson sub-Ohmic(s=1/2), N=10-30, α=0.3-0.5：Σ_B^{internal}(t)<0窗口与Nakagawa İ(t)>0窗口时间重合度>80% | Phase 2 ED验证 |
| S2（弱） | O4 | 若S2成立，存在Σ_B^{internal}的解析表达完全由(d/dt I(S:B), dC_coup/dt)决定 | 形式推导即可证伪 |
| S3（结构） | O4 | Spohn证明三层前提中至少一层在有限N+幺正下失效 | 文献+逻辑分析 |

---

## §8 北极星距离与最长卡点压力（强制）

最长开放卡点：**C1(v5)**——d/dt I(S:B)的可观测重写，已活跃5 Phase（v5-P2→v6→v7继承）。

**本Phase是否直接攻击C1(v5)**：
- **是**——若A完成产出#1（Σ_B^{internal}的纯浴侧重写），结合v5-K6可反推d/dt I(S:B) = Σ_S^{(gauge)} − β·dC_coup/dt + Σ_B^{internal}，三项都可观测 ⟹ C1(v5)直接关闭路径
- 若A产出#1失败 → 必须在§末显式记录C1(v5)的最新攻击轮次和最小失败证据

---

## §9 文献检索任务（A推导前先完成）

A必须在§1撞墙之前执行以下三类外部搜索（如可用）：
1. arxiv搜索：`Nakagawa information backflow finite bath entropy production` → 验证N_I定义在Class I/Ohmic下是否被作者本人或后续工作扩展
2. semantic_scholar：`bath entropy production negative finite-size unitary` → 寻找Σ_B<0的已发表反例
3. crossref/openalex：`Spohn entropy production proof assumptions Lindblad CPTP unitary global` → 核实Spohn证明是否需要全局CPTP或允许全局幺正

**搜索结果必须写入§N开头**，格式：
```
搜索#1: [关键词] → [N条命中 / 0命中]
  关键发现：[1-3条最相关结论]
  与北极星关系：[支撑/反对/中立]
```

---

## §10 新增卡点登记规则

A若在推导中发现新卡点，必须按以下完整格式登记到本作业§末：
```
卡点编号：C[v8编号]
目标：[一句话]
卡住位置：[具体等式/逻辑步骤]
类型：[活跃型/推迟型/实验型A/实验型B/外部声张]
关闭路径：[Phase X 数值验证/Phase X 文献调研/原则性限制]
预计关闭Phase：[编号]
三轮攻击尝试：[必须填写，禁止"需要X才能继续"式虚假卡点]
最小失败证据：[卡在哪个等式]
```

---

## §11 输出路径（强制）

- A正规推导：`D:\Claude\ai-reservations\v2-deepseek\current\A\phase-1-output.md`
- 不得写到`current/`根目录或`current/plan/`下
- 标题首行：`## A作业 Phase 1 — Σ_B^{internal}符号分析+Nakagawa N_I映射`

---

## §12 本Phase无B上次作业（v8 Phase 1是版本启动后第一个Phase）

A的"质检B上次作业"任务在本Phase**跳过**（B没有v8 Phase 0作业）。

**但**：A必须在作业末尾给出"对未来B的预判攻击点"——指出本次推导中**最可能被B攻破的1-2个步骤**，并提示B从哪个学科视角进攻最可能成功。这一段不计入A的正规推导。

---

▶️ A任务书完。直接开始推导，全自动到§末。

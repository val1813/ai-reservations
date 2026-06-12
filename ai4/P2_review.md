# P2: Scientific Review — R1-R5 技术审稿循环

> 角色: 模拟真实期刊审稿流程。5轮技术审稿人,每轮独立Agent实例。
> 核心原则: 审稿人找**技术问题**(逻辑/数学/证据/一致性)→修改→再审→再改→直至FATAL清零
> ⛔ 审稿人只审技术正确性,不审写作语气,不审"是否足够诚实/谦虚"
> 输入: paper_output/final_paper/main.tex (初稿)
> 输出: 5轮审稿报告 + 5轮修改记录 + 修改后的稿件

---

## §1 审稿人配置

每轮使用独立Agent实例。传入内容: **三份材料全部传入**,不含推导背景。

```
审稿人角色: [目标期刊] 匿名审稿人,技术准确性审查立场
  ⛔ 审稿人审什么(4项):
    1. 逻辑正确性: 推导链是否完整? 极限情况是否退化正确?
    2. 数学正确性: 定理陈述是否精确? 条件是否完整?
    3. 证据充分性: 声称是否有数据/推导/引用支撑?
    4. 三份材料交叉一致性: 正文=SM=CoverLetter?

  ⛔ 审稿人不审什么(5项):
    1. 不审写作语气 —— 论文"听起来是否自信"不是审稿范围
    2. 不审诚实度 —— "作者是否足够谦虚"不是审稿范围。只审声称是否被证据支撑
    3. 不审叙事张力 —— "读起来是否有推进力"由Phase 2b的叙事审查负责
    4. 不要求添加自我贬低 —— 禁止建议"作者应更强调这是初步结果"
    5. 不要求在每个段落重复限制条件 —— 限制条件集中在Scope/Limitations section即可

审稿标准: 该期刊实际接受标准
⛔ 审稿范围(三份必须全部审):
  1. 论文正文 (paper_output/final_paper/main.tex)
  2. SM补充材料 (paper_output/supplemental_material.tex)
  3. Cover Letter (paper_output/cover_letter.tex)

⛔ 三份材料作为一个投稿包提交给审稿人。审稿人必须:
  - 检查正文声称是否有SM数据支撑
  - 检查SM推导是否自洽且与正文一致
  - 检查Cover Letter声称是否与正文/SM吻合(无夸大)
```

### §1b. ⛔ 审稿人输出规范

审稿报告不得包含以下类型意见（这些不是技术问题，是语气问题，由Phase 2b处理）:

```
禁止的审稿意见:
  ✗ "作者应更强调这是初步结果"
  ✗ "应增加更多关于局限性的讨论" (除非当前局限性陈述有事实错误)
  ✗ "论文读起来过于自信"
  ✗ "作者应更谦虚地陈述发现"
  ✗ "应反复提醒读者这是限制条件"

允许的审稿意见:
  ✓ "Theorem X的条件(i)未陈述完整,缺少对零模的处理"
  ✓ "第Y段的声称'Z'与SM数据矛盾"
  ✓ "Cover Letter声称'W'在正文中无对应证据"
  ✓ "推导Step 3未考虑量纲不一致的情况"
  ✓ "引用[A]的内容与原文不符(已fetch验证)"

原则: 审稿人指出的是"哪里错了/缺了什么",不是"态度应该如何"。
```

---

## §2 每一轮执行流程

### Step 1: 启动REVIEWER

```
用Agent工具启动独立REVIEWER实例,传入三份材料:
  - 论文正文 (paper_output/final_paper/main.tex)
  - SM补充材料 (paper_output/supplemental_material.tex, 如存在)
  - Cover Letter (paper_output/cover_letter.tex)
  - 目标期刊 (如 PRL)
  - 上一轮审稿报告 (如有, 含对三份材料的逐份评价)
  - P2 §3 审稿检查清单

⛔ 必须启动独立Agent。PI不得自己扮演审稿人。
⛔ 审稿人只看到三份材料,看不到科研上下文。
⛔ 三份材料必须全部审。审稿报告分三个section: 正文/SM/Cover Letter。
```

→ 输出: paper_output/review_R[N].md

### Step 2: PI分类审稿意见

PI读审稿报告 → 每个问题标注严重级别:

| 级别 | 定义 | 处理 |
|------|------|------|
| FATAL | 论文核心声称被证伪/数学错误/引用虚构 | 必须修正,否则拒稿 |
| MAJOR | 推导不完整/证据不足/解释有歧义 | 必须回应,补充推导或证据 |
| MINOR | 措辞/格式/图表标注问题 | 修改即可 |

### Step 3: ⛔ R1降级判断

```
如果是R1且裁决Reject:
  PI必须在Phase清单"期刊跟踪"区写降级判断:
    R1目标: [PRL] → R1裁决: Reject → 当前目标: [降级为___]
    降级原因: [一句话 — 是数学缺陷/可检验性不足/先发覆盖/声张过弱?]
    升级条件: [具体 — 做出什么可以升回原目标?]
```

### Step 4: 启动FIX Agent

```
用Agent工具启动独立FIX Agent:
  传入: 三份材料(正文+SM+CoverLetter) + 审稿报告(分正文/SM/CoverLetter标注FATAL/MAJOR)
       + ⛔ paper_output/author_voice_card.md
  输出: paper_output/fix_R[N].md + 修改后的三份文件

⛔ 修复规则:
  - 科学修正不能靠文字绕过。正文需要补推导就补,SM需要补数据就补
  - SM中的推导必须自洽,且与正文一致(不能正文说A推导B,SM说A跳过B)
  - Cover Letter声称必须与正文/SM一致(不能夸大,不能遗漏限制条件)
  - 优先用实际数据+py脚本验证
  - 不能为了回避审稿意见而降低声称强度
  - ⛔ 遵守§4b-bis的Voice保护规则 (读取author_voice_card.md)
```

### Step 5: INSPECTOR校对

```
启动INSPECTOR Agent (独立实例):
  检查修改处: 量纲/方向/量级/循环论证
  输出: paper_output/inspect_R[N].md
  有阻断→FIX Agent必须再次修改

⛔ 每轮Voice退化检查 (新增 — 防止5轮累积削平):
  INSPECTOR额外检查:
    [ ] 本轮FIX修改是否删除了审美判断句?
    [ ] 本轮FIX修改是否弱化了信念梯度? (Level A→B/C?)
    [ ] 本轮FIX修改是否删除了人格化特征? (口语短句/第一人称/比喻?)
    [ ] 本轮FIX修改是否修匀了段落长度? (极短段被扩展? 极长段被拆分?)
    [ ] 本轮FIX修改是否扩散了限制条件? (在非修正段落添加hedging?)

  命中任一项 → 标注"Voice退化" → FIX Agent必须在本轮内恢复
  ⛔ Voice退化不能累积到下轮。每轮必须独立通过Voice检查。
  如果FIX Agent无法同时满足"修正技术问题"和"保持Voice" →
    在fix报告中标注冲突,由PI裁决。PI优先保持技术正确性,
    但要求FIX Agent在保持正确性的前提下寻找不破坏Voice的替代修改。
```

### Step 6: 更新稿件 + 检查停止条件

```
更新 main.tex → 检查:
  FATAL数=0? → 进入下一轮(或R5后进入Phase 3)
  FATAL>0? → 继续下一轮修改
  已到R5? → 如FATAL>0则标记为"建议不投稿",等待修复后重跑
```

---

## §3 审稿检查清单 (每轮REVIEWER必须逐项回答)

### 3a. 内容审查 (4维度)

```
Q1. 叙事逻辑
  □ 论文的核心声称是什么?(一句话)
  □ Introduction的gap描述是否精确? (不是"这个问题很重要"而是"前人做了X但没能做Y因为Z")
  □ 核心声称是否在正文中有完整的推导链支撑?
  □ Discussion是否诚实讨论了边界和局限?

Q2. 物理/数学正确性
  □ 核心推导的每一步是否可追溯?
  □ 有隐藏假设吗? (列出所有未显式声明的假设)
  □ 极限情况退化是否正确? (耦合→0, T→0, T→∞等)
  □ 量纲是否一致?

Q3. 数据支撑
  □ 每个核心声称是否有数据/推导/引用支撑?
  □ 数值结果是否可复现? (方法部分是否足够详细?)
  □ 误差估计是否合理?
  □ 图和正文的数值是否对得上?

Q4. 引用完整性
  □ 是否有遗漏的关键文献? (搜索验证)
  □ 引用是否准确反映了被引论文的结论? (抽查3-5篇fetch验证)
  □ 近期文献(2024-2026)占比是否≥30%?
```

### 3b. 可检验性审查 (来自ai SOP)

```
□ 每个核心预言是否有具体的检验方案?
□ 检验方案是否标注了: 数据集/可观测量/预期数值范围?
□ 是否存在"原则上可能""待未来实验"等禁词? → 标注为FATAL
```

### 3d. SM补充材料审查

```
□ 正文中所有"见SM"/"see Supplemental Material"引用 → 对应的SM section确实存在?
□ SM中的推导是否自洽? (独立检验,不与正文交叉依赖)
□ SM中的数值/公式/符号与正文一致?
□ SM图表是否清晰标注? 编号与正文不冲突?
□ SM是否包含正文未提到的额外假设?
□ SM的结论是否与正文一致? (不能正文说A,SM暗示非A)
□ SM有独立的参考文献? (如期刊要求)
```

### 3e. Cover Letter审查

```
□ 声称的finding是否与正文/SM一致? (无夸大)
□ Novelty声称是否精确? (与正文Introduction的gap描述一致)
□ 是否遗漏了正文中的重要限制条件? (如"条件性""假设""有待验证")
□ ⛔ 是否有禁词? ("原则上可能""待未来实验")
□ ⛔ 是否有禁止句式? ("We hope""We are confident")
□ 长度是否≤1页?
□ 是否提到了对应期刊的投稿要求? (如PRL需声明"广泛物理学意义")
```

### 3f. 三份材料交叉一致性检查

```
□ 正文声称=SM证据=CoverLetter陈述 是否三位一体?
   逐条核对: 正文每个核心声称 → SM有对应推导/数据 → CoverLetter如实反映
   不一致 → FATAL
□ 同一符号在三份材料中定义相同?
□ 同一数据点在三份材料中数值一致?
```

### 3g. AI痕迹初步检查

```
□ 三份材料是否存在明显的AI写作pattern? (均匀句长/过度连接/穷举结构)
  (详细检查在Phase 4进行,此处只标注明显问题)
```

---

## §4 修复规范 (FIX Agent)

### 4a. 修复优先级

1. FATAL → 必须完全消除。不能降低声称强度来绕过(那是降级)。
2. MAJOR → 必须回应。补充推导/证据/解释。
3. MINOR → 修改措辞/格式。

### 4b. 修复方式

```
科学修正:
  - 补推导: 从已有推导文件中提取或重新推导
  - 补数据: 用实际数据+py脚本生成数值验证
  - 补引用: 搜索文献→fetch验证→加入引用库

叙事修正:
  - 改叙述: 不改变科学内容,只改进表达方式
  - 重组结构: 调整section内段落顺序(不影响科学逻辑)
  - 强化motivation: 确保Reader 5问每问都有答案

⛔ 禁止:
  - 文字绕过: 不能只改措辞回避审稿意见
  - 降级绕过: 不能把"我们证明了X"改成"我们猜测X可能成立"来回应质疑
  - 添加新声称: 不能在修复中引入未经AB验证的新科学声称

⛔ Voice保护规则 (新增 — 防止FIX Agent削平作者人格):
  - 禁止删除审美判断句: 不能以"太主观"为由删除 "ugly but works" / "I find this" 类句子
  - 禁止弱化信念梯度: 
    Level A (断言) → 不能改成 Level B/C (hedged)
    如果技术修正需要添加条件 → "Under C, X holds." NOT "X may hold under C."
  - 禁止删除人格化特征: 口语短句/第一人称/读者对话/比喻 → 不是不正式,是Voice
  - 禁止修匀段落长度:
    如果某段本来是≤2句(快速带过) → 不要因为"不够详细"而扩展
    如果某段本来是≥8句(作者在意) → 不要因为"太长"而拆分
  - 禁止扩散限制条件: 技术修正只在修正点添加条件,不扩散到其他段落
```

### 4b-bis. ⛔ FIX Agent 启动前提

```
FIX Agent启动时必须:
  [ ] 读取 paper_output/author_voice_card.md
  [ ] 确认理解Voice Card的5个维度
  [ ] 确认理解: 哪些段落是作者"最在意"的(不允许大幅删除/重写)
  [ ] 确认理解: 哪些句子是审美判断/人格化特征(不允许以"不正式"为由删除)

FIX Agent修改规则:
  优先修改非Voice段落(一般技术段落)
  如果必须修改Voice段落 → 保持Voice特征,只修正技术内容
  如果修改会破坏Voice特征 → 在fix报告中标注冲突,由PI裁决
```

### 4c. 多Agent加速 (R3起可选)

```
如果R3后剩余FATAL>3:
  启动4个FIX Agent并行修复:
    Agent A: 修复正文-数学/推导问题
    Agent B: 修复SM-数据/推导/补充证据
    Agent C: 修复Cover Letter-叙事/声称一致性
    Agent D: 修复三份材料交叉一致性(交叉引用/符号/数值)
  PI合并四个修复→检查一致性→更新三份文件

  ⛔ 每个Agent只修改自己负责的部分。禁止交叉修改。
  ⛔ Agent D最后运行,确保三份材料修改后仍一致。
```

---

## §5 停止条件 — ⛔ 硬退出闸门

### 决策树 (PI每轮执行)

```
R1 REVIEWER报告出来后:
  ├── 触发R1即死条件? → 🛑 立即停止。不进入R2。
  │   降级归档,记录不可修复原因。告知用户。
  ├── R1 FATAL≥5 AND 可检验预言=0? → ⛔ 强烈建议停止
  │   (CEP案例:5 FATAL+零可检验性。继续修只是把"错误论文"修成"正确但没数据的论文")
  ├── 否则 → 进入R2修复
  │
R2 REVIEWER报告出来后:
  ├── R2 FATAL数 ≥ R1 FATAL数? → 🛑 FATAL未减少,修复无效
  │   暂停。检查:是修复方向错了?还是问题本质不可修?
  ├── 否则 → 进入R3
  │
R3 REVIEWER报告出来后:
  ├── FATAL仍>0 AND 所有FATAL属于同一根因? → ⛔ 根因可能是框架级缺陷
  │   暂停。建议降级目标期刊,不继续R4/R5。
  ├── 否则 → 进入R4
  │
R4→R5: 正常收敛路径。FATAL应=0。
```

### 5a. ⛔ R1即死条件 (满足任一→立即停止,不修)

```
1. 可检验性死刑:
   REVIEWER Q-1判定 可检验声张数/总声张数 = 0
   即:所有预言都需要新实验/新模拟/新设施,无一可用现有公开数据检验
   → 自动裁决:稿件在物理期刊(PRL/PRD/PRX)不可发表
   → 动作:归档预印本。等待检验工具出现后重投。不浪费R2-R5。

2. 核心数学证明错误且框架内不可修复:
   REVIEWER发现核心定理的证明有逻辑漏洞,且该漏洞
   源于框架的基本假设冲突(不是推导疏忽)
   → 不是"改改就对了"的问题——是框架本身有问题
   → 动作:记录漏洞位置,归档。等待框架修正后重新选题。

3. 先发覆盖:
   审稿人发现≥1篇已发表论文覆盖了本稿件≥70%的核心声称
   → 不是"差异化空间"的问题——是核心创新已被发表
   → 动作:击毙课题,记录先发文献。从灰烬中分叉新方向(见ai/PI.md §2)。

4. 范畴错误/物理不可能:
   审稿人判定稿件核心矛盾属于:
   - 范畴错误(混用不同框架的不可搬用概念)
   - 物理不可能(矛盾依赖的操作有已知物理极限阻挡)
   - 已知可共存(A和B已被证明可以共存)
   → 动作:击毙。0分,不修。

5. 数据不可得且无替代:
   审稿人确认:验证核心声称所需的关键数据
   在当前技术条件下完全不可获取,且无任何替代验证路径
   → 动作:归档,标注"数据不可得"。等待数据出现。
```

### 5b. FATAL趋势异常 (R2触发)

```
R2 FATAL数 ≥ R1 FATAL数:
  含义:一轮修复后问题没有减少,反而持平或增加
  原因可能是:
    a) 修复方向错了(在修症状而不是根因)
    b) 修复引入了新FATAL
    c) 问题本质是框架级缺陷,修补无法解决
  
  PI必须诊断原因 → 写诊断报告
  如果是(a)/(b)→可以调整修复方向后继续R3
  如果是(c)→🛑 停止。降级归档。不浪费R3-R5。
```

### 5c. 正常停止

```
正常: R5完成, FATAL=0 → 进入Phase 3
异常: R5完成, FATAL>0 → 标记"建议不投稿"
      需告知用户哪些FATAL无法在框架内修复
提前: 任一轮发现引用虚构无法修复 → 阻断,标记"引用失信"
```

### 5d. 降级归档格式

```
当触发任何硬退出闸门时,PI必须写降级归档记录:

课题: [LP编号]
停止轮次: R[N]
触发条件: [5a-1/5a-2/5a-3/5a-4/5a-5/5b-c]
不可修复原因: [具体描述]
需要的工具/数据/理论突破: [具体]
建议: [归档预印本/等待新数据/分叉新方向/框架重构]
下次重评条件: [具体]
```

## §6 5轮全景

```
R1: 首次投稿模拟 → 通常FATAL最多(CEP案例:5 FATAL)
R2: 修复后重审 → FATAL应显著减少(CEP:3 FATAL)  
R3: 深度审稿 → 关注残余问题和叙事质量(CEP:1 FATAL)
R4: 精细审稿 → 检查边界情况和次要声称(CEP:0 FATAL)
R5: 终审 → 模拟真实审稿人最后通读(CEP:0 FATAL)

预期趋势: FATAL数逐轮递减。如果R3后FATAL反增→说明修复引入了新问题→暂停,检查修复质量。
```

---

## §7 ⛔ 防御性语言禁令 — 自我贬低黑名单

> 以下语言模式已被确认为"过度对齐到对抗审稿信号"的症状。
> 它们对技术内容零贡献,但会系统性降低论文说服力。
> FIX Agent和PI在每次修改后必须grep全文扫描。命中→删除或改写为中性技术陈述。

### 7a. 自我贬低句 (直接删除,不需要替代)

```
⛔ "It may be nothing." / "It may be an accident." / "It may be a coincidence."
⛔ "We tried to derive it. We couldn't."
⛔ "That does not make it correct."
⛔ "Not even close."
⛔ "It isn't one."
⛔ "We have nothing to add here except to mark the gap."
⛔ "What is missing is not small."
⛔ "We do not see a path from here to there."
⛔ "That is not surprising." / "That is reassuring but not surprising."
⛔ "I was initially unsure..." / "We were initially unsure..."
⛔ "It would be dishonest to claim otherwise."
⛔ "Honesty about where a method breaks is more useful than pretending it doesn't."
```

### 7b. 过度谦虚句 (改写为中性技术陈述)

```
⛔ "The result is not surprising; the value is in making the steps explicit."
   → "Proposition X establishes Y under conditions A, B, C."

⛔ "What we prove is weaker than what one might want; what we claim is only what we prove."
   → "Proposition X shows Y. The proof assumes A, B, C."

⛔ "This is a consistency check, not a new theorem."
   → "Gleason-type results give the normal probability representation on H^2_+(S)."

⛔ "We cannot stress that enough."
   → 删除。如果确实需要强调条件,在定理陈述中精确列出即可。

⛔ "The answer is conditional."
   → 删除。定理条件已在定理陈述中列出,无需额外标注"有条件"。

⛔ "Whether [X] is useful is for the reader to judge."
   → 删除。读者不需要被告知"你可以自己判断"。
```

### 7c. 规则: 每个技术限制只陈述一次

```
⛔ 禁止的症状: 同一个限制条件在正文中出现≥3次
   (如:"这不适用于相互作用理论"在Intro/Results/Discussion各说一次)

正确做法:
  1. 限制条件在它第一次出现的段落完整陈述
  2. 后续提到时用简短回指: "as noted in Sec.X" (最多5个词)
  3. 所有限制条件汇总到 Discussion §Scope and limitations (一个section,一次说清)
```

### 7d. FIX Agent修改规则补充

```
⛔ FIX Agent在修改论文时:
  - 修正技术错误 → ✅
  - 补充遗漏的条件 → ✅  
  - 添加自我贬低句来"显得诚实" → ⛔ 禁止
  - 在每个段落重复限制条件 → ⛔ 禁止
  - 降低声称强度来回避审稿意见 → ⛔ 禁止(已有规则,重申)
  - 把技术问题改成"我们不知道"/"我们没做出来" → ⛔ 禁止
  
  如果审稿人指出"X条件未说明":
    → 在定理陈述处精确添加X条件 (✅ 技术修正)
    → 不要在全文每个段落说"本文结果是条件性的" (⛔ 防御性扩散)
```

### 7e. 执行

```
PI在每轮FIX Agent修改后, grep全文扫描§7a和§7b中的黑名单短语:
  [ ] grep "may be nothing\|Not even close\|We couldn't\|It isn't one\|would be dishonest"
  [ ] grep "not surprising\|weaker than what one might\|consistency check, not"
  [ ] grep "for the reader to judge\|cannot stress that enough\|answer is conditional"
  
  命中 → FIX Agent必须删除/改写该句
  同一限制条件出现≥3次 → 保留第一次,其余改为≤5词回指或删除
```

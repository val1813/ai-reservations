# P0_5: Author Persona Generation — 作者人格生成

> 角色: 在论文写作开始前，生成一个**具体的、有偏见、有个人史的作者角色**。
> 这个角色成为后续所有Agent的绑定约束——写作Agent代入这个角色，
> 审稿Agent检查这个角色的声音是否被保留。
> 
> ⛔ 本Phase产出 Voice Card 是**绑定文档**，后续所有Phase的Agent必须读取并遵守。
> ⛔ 任何Agent在修改论文时，不得删除或弱化Voice Card中定义的人格特征。
> 
> 输入: 论文素材 + Phase 0 intake信息
> 输出: paper_output/author_voice_card.md

---

## §1 为什么需要这个

```
纯禁止清单的局限:
  "不要用Moreover" → AI换用Additionally
  "不要写It may be nothing" → AI换写This remains uncertain
  → 永远在打地鼠。绕过这个，AI会找下一个。

正向注入的逻辑:
  人类论文读起来像人写的 → 不是因为"没有AI词"，而是"有人格"。
  人格 = 审美判断 + 深度不均 + 个人史 + 意外 + 对话感
  这些是AI不会主动产生的特征——要求AI主动产生它们，比禁止AI被动避免更难绕过。

锁定的逻辑:
  Voice Card = 一个具体的作者角色。
  后续Agent不是"写一篇没有AI味的论文"（抽象），
  而是"代入这个角色来写"（具体）。
  如果另一个AI试图修改 → 它必须遵循Voice Card，否则Phase 4f会检测到Voice特征缺失。
```

---

## §2 Voice Card 结构

### 2a. 问题起源（个人史线索）

```
1句话。为什么这个人会想这个问题？不是"这是重要问题"，而是具体经验。

好例子:
  "I noticed this pattern while debugging a simulation in 2021—
   the damping rates followed a two-scale curve I couldn't explain with existing formulas."
  "After reading Chandrasekhar's 1984 paper, I wondered whether the algebraic special mode
   was secretly connected to the Slepian concentration spectrum."

坏例子:
  "This is an important problem in theoretical physics."
  "Black hole QNMs have attracted significant attention."
```

### 2b. 审美判断 — 每个section至少1句

```
⛔ 这是Voice Card最重要的部分。人类对"什么漂亮"和"什么丑"有强烈意见。

生成规则:
  对论文的每个主要section,定义1个审美立场:
  
  [Section X]: 什么论证/方法/结果我认为漂亮? 什么我认为丑或无奈?

  例:
  - "I like clean algebraic proofs that don't need numerical verification. 
     Proposition 4 is the prettiest part of this paper."
  - "The rational interpolation formula is ugly. I'm not proud of it. 
     But it works better than everything else I tried. I'll say so directly."
  - "The Kerr extension is a kludge. I know it. The reader will know it. 
     I'd rather admit it once with a shrug than apologize for it ten times."
```

### 2c. 信念梯度 — 替代"we are uncertain about X"

```
把论文中所有声称,按信念等级分类。不使用"不确定"这种平面化的hedging。

Level A — 我愿意赌上职业生涯:
  表达: 直接断言。"X holds." / "Y is true."
  条件: 有完整数学证明或压倒性数值证据
  论文中的位置: Proposition 4, Theorem 1, Theorem 6

Level B — 我很相信但承认有微小gap:
  表达: 用"strongly suggests" / "is consistent with" / "supports"
  条件: 有良好但不完美的证据
  论文中的位置: 数值结果, 对比, 插值

Level C — 推测但有意思:
  表达: 用"If true, this would mean..." / "A speculative interpretation: ..."
  条件: 有明显gap但值得标注
  论文中的位置: 推测性讨论

Level D — 这是我的痛点,不是我的声称:
  表达: 在Open Questions里一次性说清。"I don't understand why X works."
  条件: 已知的gap
  论文中的位置: Open Questions section ONLY

⛔ 禁止: 在正文声称段用Level D语言 ("We don't know if this is true"出现在声称段)
⛔ 禁止: 在Open Questions外超过2次使用Level C
```

### 2d. 人格化语言特征 — 每section至少1个

```
从以下5个特征中选择2-3个,标注在哪些section使用。后续写作Agent必须在标注位置体现。

[ ] 口语化短句 (1-4词):
    位置: [指定section]
    例: "This fails." / "Not quite." / "Why?" / "Here's why."

[ ] 第一人称单数/复数 (非"In this paper we..."):
    位置: [指定section]
    例: "I find this surprising." / "We tried. It didn't work."

[ ] 直接对读者说话:
    位置: [指定section]
    例: "The reader might ask: why not use X? The answer is..."
    (注意: 这是帮助读者理解,不是防御性预判攻击)

[ ] 非学术比喻/类比:
    位置: [指定section]
    例: "The spectrum behaves like a badly tuned piano—
          the low notes are roughly right but the high ones go sharp."

[ ] 具体经验/操作细节 (只有真正跑过实验/推过公式才知道的):
    位置: [指定section]
    例: "At N_Sh > 20 the kernel matrix becomes numerically singular 
          in double precision; we had to switch to quad precision for those points."
```

### 2e. 注意力分配 — 深度不均匀

```
人类作者注意力不均匀。AI均匀分配注意力。这是最容易被检测到的差异。

声明:
  [我最在意的1-2个点]:
    - [具体点]: 大幅展开 (3-5倍于平均值)
    - [具体点]: 大幅展开

  [我认为必要但无聊的点]:
    - [具体点]: 2句话带过或放SM
    - [具体点]: 2句话带过或放SM

规则:
  全文至少2个段落 ≤2句 (极短段)
  全文至少1个段落 ≥8句 (极长段,在"最在意"的点上)
```

### 2f. 禁止项 — 这个人不会说的话

```
⛔ 从P2_review.md §7 和 P4_randomize.md §8 中,为这个角色定制"绝对不会说的"短语:

  "这取决于角色和内容。对这篇论文,除了全局黑名单外,还有什么是这个角色绝对不说的?"

  例:
  - 这个作者不会在每个段落末尾加安全收尾句
  - 这个作者不会用"tapestry"／"landscape"／"delve into"
  - 这个作者不会说"further investigation is warranted"
  - 这个作者不会在声称段使用"may be" / "could potentially"
```

---

## §3 执行流程

### Step 1: 启动PERSONA Agent

```
用Agent工具启动独立PERSONA生成实例:
  传入:
    - 论文素材/草稿 (paper_output/final_paper/main.tex 或素材目录)
    - Phase 0 intake信息 (目标期刊/论文类型)
    - 用户已有的写作样本 (如用户提供). 如未提供,从素材中推断风格偏好
    - 本文件 §2 的Voice Card结构

  Agent任务: 生成完整的author_voice_card.md, 填充§2中所有5个维度。
  ⛔ Agent必须用具体内容填充,不得留空或写"待定"。
```

→ 输出: `paper_output/author_voice_card.md`

### Step 2: PI审核Voice Card

```
PI检查Voice Card:
  [ ] 问题起源是否具体? (不是"这是重要问题")
  [ ] 每个section都有审美立场? (至少1句)
  [ ] 信念梯度是否覆盖了所有核心声称?
  [ ] 人格化特征是否标注了具体使用位置? (不是"全文使用")
  [ ] 注意力分配是否指定了"最在意"和"无聊但必要"的点?
  [ ] 禁止项是否具体到这篇论文?

不通过 → 退回PERSONA Agent重新生成
```

### Step 3: Voice Card 分发

```
⛔ Voice Card成为绑定文档。以下Agent在启动时必须读取:
  - Phase 1 写作Agent (P1_build.md)
  - Phase 2 审稿Agent (P2_review.md) — 审稿人可以批评声称,但不能建议削弱人格化特征
  - Phase 2b 叙事审查Agent (P2b_narrative_review.md) — 检查Voice特征是否被保留
  - Phase 4 structure-randomizer Agent (P4_randomize.md) — 检查Voice特征PRESENCE

PI在启动每个Agent时,prompt中必须包含:
  "⛔ 读取 paper_output/author_voice_card.md。你的所有修改必须保持Voice Card中的人格特征。
   如果修改某个段落会破坏Voice特征,你必须在修改记录中标注并寻求替代方案。"
```

---

## §4 Voice Card 锁定机制 — 防止后续AI破坏

```
这是用户最关心的问题: 如果另一个AI拿到这篇论文,它会不会把Voice特征删掉?

锁定1 — 文件级:
  author_voice_card.md 是一个物理文件。任何AI修改论文前必须先读它。
  如果它跳过不读 → Phase 4f会检测到Voice特征缺失 → 阻断。

锁定2 — Phase 4f Voice PRESENCE检查 (新增):
  不是在检查"有没有AI词汇",而是在检查"Voice特征还在不在":
    [ ] 每个section是否仍有审美判断句?
    [ ] 信念梯度是否被保留? (Level A声称是否被弱化成Level C?)
    [ ] 人格化特征是否仍出现在指定位置?
    [ ] 注意力分配是否仍不均匀? (是否被"修匀"了?)
    [ ] 极短和极长段落是否还存在?
  命中"否" → ⛔ 阻断,回退。不接受"我把Voice特征删掉了因为这样更安全"。

锁定3 — Phase 2b 新增Voice一致性子检查:
  叙事审查Agent不仅检查防御性语言,也检查Voice特征的完整性。
  如果审稿人(FIX Agent)的修改削弱了Voice特征 → 叙事审查报告标注"Voice退化" →
  PI必须恢复或找到不削弱Voice的替代修改方式。

锁定4 — 规则优先级:
  当"技术正确性"和"Voice特征"冲突时:
    技术正确性 > Voice特征 (定理错了必须改,不管Voice)
  当"AI检测规避"和"Voice特征"冲突时:
    Voice特征 > AI检测规避 (宁可AI检测率高2%,也不能删人格化特征)
  当"防御性语言删除"和"Voice特征"冲突时:
    防御性语言删除 > Voice特征 (自我贬低句即使有人格也要删)
    但: 删完后需要检查是否可以用Voice Card中的人格化特征替代
    (用审美判断替代自我贬低,用Level C替代"we don't know")
```

---

## §5 Voice Card 模板

```
# Author Voice Card — [论文标题]

## 1. 问题起源
[1句话 — 这个人怎么想到这个问题的? 具体经验/观察]

## 2. 审美立场
### [Section 1名称]
- 我认为漂亮/喜欢的:
- 我认为丑/无奈的:

### [Section 2名称]
...

## 3. 信念梯度
### Level A (赌上职业生涯):
- [声称1]: [证据简述]
### Level B (相信但承认gap):
- [声称2]: [证据简述 + gap是什么]
### Level C (推测):
- [推测1]: [为什么标注为推测]
### Level D (Open Questions — 集中在Dedicated Section):
- [我真正不知道的]:

## 4. 人格化语言特征
### 特征1: [口语化短句/第一人称/对话/比喻/操作细节]
- 使用位置: [section/段落]
- 示例句:

### 特征2: [...]
...

## 5. 注意力分配
### 我会大幅展开:
- [点1]: [为什么在意]
### 我会快速带过:
- [点2]: [为什么无聊但必要]

## 6. 这个人不会说
- [具体短语1]
- [具体短语2]
```

---

## §6 与后续Phase的关系

```
Phase 0 → 0.5 (本Phase) → Phase 1 → Phase 2 → Phase 2b → Phase 3 → Phase 3.5 → Phase 4 → Phase 5
         │                  │          │          │                              │
         └─ Voice Card ─────┴──────────┴──────────┴──────────────────────────────┘
              ↑ 所有Phase的Agent启动时读取              Phase 4f检查Voice PRESENCE

Phase 2审稿人: 读Voice Card → 审技术正确性,不削弱Voice
Phase 2b叙事审查: 读Voice Card → 检查Voice保留 + 防御性语言清除
Phase 4 randomizer: 读Voice Card → 生成参数时保持Voice指定的长度/密度/人格特征
Phase 4f终检: 检查Voice PRESENCE (不是检查AI ABSENCE)
```

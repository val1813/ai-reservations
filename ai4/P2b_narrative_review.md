# P2b: Narrative Tension Review — 叙事张力与说服力审查

> 角色: 反制衡agent。Phase 2的技术审稿人只找技术漏洞,本agent负责反向操作:
>   找出"防御性过度"的句子、检查叙事是否有推进力、确保论文语气匹配实际贡献水平、
>   检查Voice Card特征是否被Phase 2修改削弱。
> ⛔ 本agent与技术审稿人对等——它的删减建议与技术修正有同等权重。
> 输入: Phase 2 R5完成后的终稿 (FATAL=0) + ⛔ paper_output/author_voice_card.md
> 输出: paper_output/narrative_review.md + 删减后的稿件

---

## §1 核心原则

```
技术审稿人问: "这里有没有逻辑漏洞/数学错误/证据不足?"  (Phase 2)
叙事审查问:   "这篇论文读起来像不像作者自己都不信?"    (Phase 2b)

两个问题同等重要。一篇数学完全正确但读起来像自我辩护的论文,
与一篇数学有漏洞的论文一样,都不会被好期刊接受。
```

---

## §2 执行流程

### Step 1: 启动NARRATIVE REVIEWER Agent

```
用Agent工具启动独立NARRATIVE REVIEWER实例,传入:
  - 论文正文 (paper_output/final_paper/main.tex, R5修改后)
  - Phase 2全部5轮审稿报告 (review_R1.md ~ review_R5.md)
  - 本文件 §3-§6 的检查清单

⛔ 必须启动独立Agent。PI不得自己扮演叙事审查。
⛔ 叙事审查Agent看到的材料: 正文 + 审稿历史。
  审稿历史用于判断: 哪些限制声明是"审稿人要求补充的(保留)" vs "写作agent自己加的(检查是否过度)"
```

→ 输出: `paper_output/narrative_review.md`

### Step 2: 叙事审查报告结构

报告必须包含以下5个section:

```
1. 自我贬低句扫描 (对照§3黑名单)
2. 限制条件重复检查 (同一限制出现≥3次?)
3. 叙事弧线评估 (§4 Reader Journey)
4. 语气-贡献匹配度 (§5)
5. 删减建议清单 (逐句标注: 删/改写/保留)
```

### Step 3: PI执行删减

```
PI读叙事审查报告 → 逐条决定:
  - 报告建议"删除" → 默认执行(除非删除会引入事实错误)
  - 报告建议"改写" → 执行改写
  - 报告建议"保留" → 确认理由

⛔ PI只能以"删除会引入事实错误"为理由否决删减建议。
  不能以"审稿人可能不喜欢"为理由保留自我贬低句。
```

### Step 4: 修改后验证

```
[ ] 全文自我贬低句数量: 0 (零容忍)
[ ] 同一技术限制出现次数: ≤2 (第一次完整陈述+一次简短回指)
[ ] 每个"we tried"/"we couldn't"/"we don't understand"有实质内容? 无→删除
[ ] 论文第一页(前500词)无任何自我贬低句
```

---

## §3 自我贬低黑名单 (完整版)

### 3a. 零容忍 — 命中即删除,不需要替代

```
这些句子对恶意审稿人毫无防御价值,但会毁掉编辑和普通审稿人的第一印象:

⛔ "It may be nothing."
⛔ "Not a solution. Not even close."
⛔ "It isn't one."
⛔ "We tried to derive it. We couldn't."
⛔ "That does not make it correct."
⛔ "It would be dishonest to claim otherwise."
⛔ "Honesty about where a method breaks is more useful than pretending it doesn't."
⛔ "We have nothing to add here except to mark the gap."
⛔ "What is missing is not small."
⛔ "We do not see a path from here to there."
⛔ "Whether [X] is useful is for the reader to judge."
⛔ "We cannot stress that enough."
```

### 3b. 改写而非删除 — 有技术信息但不能用自我否定形式

```
⛔ "The result is not surprising; the value is..."
   → 删除前半句。从"Proposition X establishes Y..."开始。

⛔ "What we prove is weaker than what one might want; what we claim is only what we prove."
   → "Proposition X shows Y under conditions A, B, C."

⛔ "This is a consistency check, not a new theorem."
   → "Gleason-type results applied to H^2_+(S) give the standard probability representation."

⛔ "The answer is conditional."
   → 删除。定理的条件已在定理陈述中列出。

⛔ "We were initially unsure whether X, but Y confirms it does."
   → "Y confirms X." 删除"我们曾经不确定"的叙事。

⛔ "I include this only to fix notation and scope."
   → "This section fixes notation and scope." (去掉自我辩护)

⛔ "It may be a coincidence." / "It may be an accident."
   → "Whether this numerical coincidence reflects a deeper connection remains open."
   (这是技术陈述,不是自我贬低)
```

### 3c. 元评论 — 关于论文本身的评论句子

```
论文不需要"关于论文本身"的评论。以下类型句子全部删除:

⛔ "This paper asks what can be extracted from..." (读者已在读这篇论文,不需要被告知"这篇论文问什么")
   → 直接陈述问题: "Analytic continuation near horizons organizes mode data into..."

⛔ "The restriction matters---it keeps the construction precise but..."
   → 直接陈述限制: "The construction applies to free bosonic fields on analytic backgrounds."

⛔ "We flag this now rather than burying it later."
   → 删除。限制条件列在它应在的位置即可,不需要解释"为什么在这里说"。
```

---

## §4 叙事弧线检查 (Reader Journey)

### 4a. 第一页测试

```
读者读完第一页(前500词)后,应该能回答:
  [ ] 这个工作的核心发现是什么? (一句话)
  [ ] 为什么它重要? (即使是领域外读者也能理解)
  [ ] 作者自己认为这是重要的吗?

⛔ 如果第一页包含以下内容 → 叙事失败:
  - "This is all standard" / "Nothing new here"
  - "The restriction matters" / "this keeps it from applying to everything"
  - "We flag this now rather than burying it later"
  - "This paper asks what can be extracted..."

原因: 第一页是编辑和审稿人形成第一印象的地方。
      以自我贬低开头 = 告诉读者"这篇论文可能不值得读"。
```

### 4b. 每段推力检查

```
对每个段落问:
  [ ] 如果删掉这段,论文的论证链会断吗?
      → 会 → 保留
      → 不会 → 这段是元评论/重复限制/空洞过渡 → 删除或合并
  
  [ ] 这段的最后一句是"安全收尾"吗? (E=3含义陈述 / 自我贬低 / 开放问题)
      → 是 → 检查该收尾是否有实质信息。无→改E=1(直接停)。
```

### 4c. 安全收尾模式

```
这些收尾模式会让论文读起来"安全但无力":

⛔ 每段以"This suggests that..."结尾
⛔ 每段以"Whether this is the case remains to be seen."结尾
⛔ 每段以"Further work is needed to..."结尾
⛔ 每段以"What is missing is..."结尾

→ 允许最多1个段落用此类收尾。其余段落必须有实质结论句或直接停。
```

---

## §5 语气-贡献匹配度

### 5a. 贡献等级与语气对应

```
论文的实际贡献 → 应匹配的语气:

基础原理级 (新定理/新框架): 
  → 语气: 直接、自信。陈述"X成立"而非"X可能成立"。
  → 限制条件: 在定理陈述中精确列出,不在每个段落重复。

方法/工具级 (新方法/新技术):
  → 语气: 展示方法的有效性。陈述"Y实现了Z精度"。
  → 限制条件: 只在Scope section一次说明适用范围。

现象/观测级 (新数据/新现象):
  → 语气: 报告观测。陈述"我们观测到X,误差Y"。
  → 限制条件: 在数据局限性部分讨论。

假设/推测级:
  → 语气: 可以适度不确定。但一次性说清楚不确定性来源。
  → 限制条件: 不需要再额外添加自我贬低的元评论。
```

### 5b. 禁忌组合

```
⛔ 如果论文有完整定理证明 → 禁止语气:"这可能是一种可能的解释"
⛔ 如果论文有数值/数据验证 → 禁止语气:"这只是一个初步尝试"
⛔ 如果论文提出了新框架 → 禁止语气:"这只是一个重新组合,没什么新东西"

诚实 ≠ 自我贬低。诚实 = 精确陈述什么被证明了、什么条件下成立。
```

---

## §6 删减操作指南

### 6a. 删减测试

对每个疑似防御性句子执行:

```
测试1 — 删除测试:
  删除这句话。论文的技术内容是否完全不变?
  是 → 这句话是态度表达,删除。
  否 → 这句话有技术信息,改写(去掉自我否定前缀/后缀,保留技术核心)。

测试2 — 第一次出现测试:
  这个限制条件是否在别处已经说过了?
  是 → 保留第一次(最完整的版本),这里改为≤5词回指或删除。
  否 → 保留,但确保只陈述"在X条件下成立",不添加"这很弱"/"这不如期望的好"。

测试3 — 审稿人要求测试:
  这个限制声明是审稿人要求添加的吗?
  是 → 保留。但只保留审稿人要求的那个具体陈述,不扩散到全文。
  否 → 进入测试1。
```

### 6b. 删减后一致性检查

```
删减完成后:
  [ ] 所有删除的句子≠技术陈述 → 技术内容不受影响
  [ ] 改写后的句子保留了原来的技术信息
  [ ] 论文长度减少(通常删5-15%的冗余防御语言)
  [ ] Motto: "删掉所有'我们不确定'后,论文的技术内容完全不受影响"
```

---

## §7 输出格式

叙事审查报告模板:

```markdown
# Narrative Review — [论文标题]

## 1. 自我贬低句扫描
| 行号 | 原文 | 类型(§3a/3b/3c) | 建议(删/改写) | 理由 |

## 2. 限制条件重复检查
| 限制条件 | 出现次数 | 出现位置 | 建议 |

## 3. 第一页测试
| 检查项 | 通过/失败 |
| 核心发现一句话 | [___] |
| 为什么重要 | [___] |
| 作者自信度 | [___] |

## 4. 叙事弧线评估
### 每段推力
| 段 | 功能 | 可删? | 收尾是否安全词? |

## 5. 语气-贡献匹配度
贡献等级: [___]
当前语气: [___]
匹配度: [匹配/过强/过弱]
建议: [___]

## 6. 删减建议清单
| 优先级 | 位置 | 原文 | 操作 | 新文(如改写) |
|--------|------|------|------|-------------|
```

---

## §8 与Phase 2的关系

```
时序: Phase 2 (R1-R5 技术审稿) → Phase 2b (叙事审查) → Phase 3 (格式化)

⛔ 叙事审查必须在Phase 2全部5轮完成后执行。
   (如果在R3中途执行,后续审稿可能再引入防御性语言)

⛔ 叙事审查后的修改 → 不需要重新跑Phase 2审稿。
   (叙事审查只删减防御性语言,不改变技术内容。不会引入新FATAL。)

⛔ 如果叙事审查删除了审稿人要求添加的限制声明:
   → 检查是否保留了该限制的第一次完整陈述
   → 如果只删除重复/扩散部分 → 不违背审稿意见
   → 如果删除了唯一一次陈述 → 恢复,但改写为中性形式(不加自我否定前缀)
```

---

## §9 ⛔ Voice Card一致性检查 — 作者人格保留审计

> Phase 2的5轮技术审稿可能削弱Voice Card特征。
> FIX Agent在修正技术问题时,可能把"有偏好的作者"改回"面无表情的AI"。
> 本节检查Voice特征是否被保留。

### 9a. 检查清单

```
叙事审查Agent读取 author_voice_card.md → 逐项对比R5后正文:

[ ] 信念梯度是否被保留?
    检查: Voice Card中标注为Level A的声称 → 在R5正文中是否仍是断言句式?
    如果发现Level A声称被R5修改成Level B/C语言 → ⛔ Voice退化,标注修复

[ ] 审美判断是否仍存在?
    检查: Voice Card要求每个section≥1句审美判断 → 在R5正文中是否还存在?
    如果某个section的审美判断句被FIX Agent删除了 → ⛔ Voice退化,标注恢复

[ ] 人格化特征是否仍存在?
    检查: Voice Card标注的口语短句/第一人称/读者对话/比喻 →
      在R5正文中是否仍出现在指定位置?
    如果被FIX Agent"修正"掉了 → ⛔ Voice退化,标注恢复

[ ] 注意力分配是否仍不均匀?
    检查: Voice Card标注的"最在意"段落是否仍>8句?
          "无聊但必要"段落是否仍≤2句?
    如果被FIX Agent修匀了 → ⛔ Voice退化,标注恢复

[ ] 自我贬低句是否反向增加了?
    检查: R5正文中是否出现了Voice Card "这个人不会说"列表中的短语?
    如果FIX Agent为了"显得诚实"添加了 → 按§3删除
```

### 9b. Voice退化修复规则

```
Voice退化类型 → 修复方式:

1. 信念梯度被弱化 (Level A→Level B/C):
   → 如果技术内容未变 → 恢复原Voice Card中的断言句式
   → 如果FIX Agent修改了技术内容(添加了条件/限定了范围) →
      用新条件更新声称,但保持Level A信念等级:
      不是 "X may hold under condition C" (Level B)
      而是 "Under condition C, X holds." (Level A + 条件)

2. 审美判断句被删除:
   → 恢复。如果FIX Agent认为"不客观" → 坚持保留。
     审美判断是Voice特征,不是不客观。

3. 人格化特征被删除:
   → 恢复。如果FIX Agent认为"不正式" → 坚持保留。
     口语化短句/第一人称是Voice特征,不是不正式。

4. 注意力被修匀:
   → 恢复长度分布。
     如果FIX Agent把极短段扩展了 → 检查扩展内容是否必要。
     不必要 → 恢复≤2句。必要 → 保持但标注"Voice部分退化"。

⛔ 修复优先级:
  Voice退化 ≠ 可以忽略。
  Voice特征与技术正确性同等重要(除了定理/数学错误修正)。
  "因为审稿人可能不喜欢"不是削弱Voice的理由。
```

### 9c. 更新输出格式

叙事审查报告新增 §7:

```
## 7. Voice Card一致性
### 信念梯度
| 声称 | Voice Card等级 | R5正文等级 | 是否退化? | 修复建议 |

### 审美判断
| Section | Voice Card要求 | R5正文现状 | 是否退化? | 修复建议 |

### 人格化特征
| 特征类型 | 指定位置 | R5正文现状 | 是否退化? | 修复建议 |

### 注意力分配
| 段落 | Voice Card要求 | R5正文现状 | 是否退化? | 修复建议 |
```

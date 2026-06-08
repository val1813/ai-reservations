---
name: deep-humanize
description: 对学术论文进行结构层面的去AI化改写，目标是检测率<10%同时保持或提升论文质量。基于PaperSpine的5维检测模型，但在结构层面而非句子层面操作。
---

# Deep Humanize — 学术论文结构去AI化

## 适用场景

- 论文初稿由AI辅助完成，需要降低AI检测率
- 目标：AI检测率从30-70%降至<10%，同时不降低学术质量
- 适用于英文学术论文（期刊/会议），中文需额外调整

## 核心原则

**AI文本的根本特征不是用词，而是结构的过度对称性。** 检测器看的是：
1. 句长分布是否单峰（AI: 15-25词钟形分布；人类: 多峰，有5词短句也有40词长句）
2. 段落骨架是否重复（AI: 每段claim→evidence→implication循环；人类: 结构不规则）
3. 信息密度是否平坦（AI: 每段65-75%密度；人类: 40-85%剧烈波动）
4. 是否存在不确定性和个人判断（AI几乎不说"我们不确定"/"这让我们意外"）
5. 是否有"不完美"的痕迹（人类会岔开话题、省略显而易见的步骤、对某些结果轻描淡写）

**因此去AI化的正确方法不是换词，而是打破结构对称性、注入不确定性、允许不完美。**

## 实测高触发AI句式（从GPTZero检测反馈中提炼）

以下5种句式/结构是经过实际检测验证的高AI标记pattern：

### Pattern A: "Not X, but Y" 对仗修辞
**触发例：** "This is not a quantitative inaccuracy. It is a qualitative blind spot---the most severe type of theory failure."
**为什么触发：** 精确二元对立+递进判断，零犹豫零冗余。AI极度偏好这种clean的对比结构。
**修复法：** 拆开说，中间插入具体化。例如："BM的问题不在于算不准——factor-of-2的误差实验上可以接受。问题在于它声称某个东西不存在，而这个东西实际存在。在器件设计中，这种'存在性盲区'比数值误差严重得多。" （把一句clean对仗拆成3句带语境的论证）

### Pattern B: 修辞问句 + 立即完美回答
**触发例：** "What distinguishes these three regimes? The answer lies in how information propagates between baths."
**为什么触发：** AI写说明文时最爱用的开段方式。问题太精确，回答太immediate。
**修复法：** (1) 不用问句开段，直接用assertion；(2) 如果必须用问句，延迟2-3句再给答案，中间加一个caveat或历史背景。例如："The classification we propose is based on how information propagates between baths---though we should note that mixed topologies (part chain, part star) remain unclassified."

### Pattern C: Below/Above 对称门槛句
**触发例：** "Below α≈0.3, nothing happens---the chain remains passive. Above that threshold, ergotropy increases roughly linearly."
**为什么触发：** "Below X / Above X"是AI描述phase transition的默认模板。两句完美对称。
**修复法：** 打破对称性——只详写一侧。例如："The onset is near α≈0.3. Growth beyond that point is roughly linear with coupling, reaching ε=0.083 at α=1.5." （不提below那侧，或只用半句带过）

### Pattern D: 平行bullet中每条结构相同
**触发例：** "Star: [描述]. [结论]. / Cyclic: [描述]. [结论]. / Chain: [描述]. [结论]."
**为什么触发：** 三条完全对称=骨架cosine相似度>0.9。检测器的D2维度直接标记。
**修复法：** 让各条长度和结构不同。一条用1句，另一条用3句。一条以引用开头，另一条以结果开头。允许某条详写（因为是本文重点）而另两条一笔带过。

### Pattern E: 声明-穷举-意义 三步递进
**触发例：** "The result is strikingly general. It holds for all N, all temperatures, all spacings, and all spectral densities. Any nonzero ergotropy is necessarily a beyond-BM effect---the theorem identifies an entire topology class invisible to the standard design tool."
**为什么触发：** [评价]+[穷举all X, all Y, all Z]+[意义声明]。AI的完美三拍总结。每一步只做一件事，信息密度均匀。
**修复法：** (1) 穷举不要用all X, all Y, all Z并列——只提最不显然的1-2个，其余用"regardless of parameters"一笔带过。(2) 意义声明和评价合并为一句而不是分开。(3) 或者先给意义再给范围（倒序），而不是评价→范围→意义的固定顺序。

## 各Section类型的特殊处理

### Introduction
- **高危pattern：** 修辞问句引出gap + "We answer affirmatively" + roadmap段
- **修复：** 用assertion引出gap（"Whether BM can miss an engine entirely has not been examined."），不用问句。删roadmap或压成一句section指引。
- **Segal做法参考：** 文献综述占60-70%篇幅，自己贡献只在末尾30%。这样的比例让Intro看起来像"survey引出问题"而不是"AI的五段式"。

### Theorem/Proof sections
- **通常不触发**（数学证明是固定形式，检测器不标）
- **但theorem后面的"评价段"会触发**——"The result is strikingly general. It holds for all..."
- **修复：** 评价段用具体例子代替穷举。例如："This includes, for instance, a molecular wire with ten levels at room temperature---a case far removed from our numerical parameters but still covered by the theorem."

### Classification/Comparison sections
- **高危pattern：** 平行list + 总结声明
- **修复：** 让list各条非对称（见Pattern D修复法）。总结声明改成forward pointer（"We return to this point in the Discussion"）而不是当场声明意义。

### Discussion
- **高危pattern：** "Not X but Y"对仗 + "The practical consequence is [形容词]" + 完美覆盖所有open questions
- **修复：** (1) 第一段用具体实验场景开头而不是抽象评价开头。(2) open questions用(i)(ii)编号但各自长度不同。(3) 至少一处说"we are not sure" / "this requires further study that we have not done"。(4) 加入一段与相邻领域的speculative connection。
- **Segal做法参考：** 她的Discussion经常以"A few remarks are in order: (i)..."开头，每个remark长度不等，有的一句有的一整段。

### Key experimental signatures / Predictions
- **高危pattern：** "X predicts exactly zero. Any detected Y constitutes direct evidence of Z."这种完美的判据声明
- **修复：** 软化绝对性。例如加入一个caveat："Any detected thermoelectric response would be strong evidence---though one would need to rule out thermopower contributions from asymmetric tunnel barriers, which can mimic a nonzero signal."

## 执行流程

### Phase 0: 诊断（5分钟）

读完全文后回答：
1. 全文有几种段落模板？是否有重复使用超过2次的模板？
2. Introduction是否是标准的 territory→gap→answer→roadmap 四段式？
3. Methods/Results的各subsection是否走同一个汇报模板？
4. Discussion是否工整地覆盖了"意义→局限→未来"？
5. 有没有任何一处作者承认困惑、意外、或不确定？
6. Conclusion是否逐条复述了contributions？

如果上述答案分别是"少/是/是/是/没有/是"——需要deep改写。

### Phase 1: 结构重组（核心步骤）

**1.1 Introduction压缩**
- 删除roadmap段（"This paper provides: (i)... (ii)... (iii)... (iv)..."）。PRR/PRL级别期刊不需要它，读者能从目录看到结构。
- 合并territory和gap为一段：直接从问题出发，先说什么已知，再用一个转折句引出gap。
- 让answer段尽可能短（3-4句），不要预告所有结果。

**1.2 打破重复subsection模板**
- 如果Methods或Results有N个并列subsection且每个都是"背景→数据→结论"三段式，执行以下操作：
  - 合并相关的subsection（例如把"coupling strength"和"bath speed"合成"coupling regime"）
  - 对不同subsection使用不同叙事结构：
    - 第一个：直接给结果，再解释为什么
    - 第二个：先讲物理直觉，再看数据是否验证
    - 第三个：以一个"意外发现"开场
  - 允许某些subsection比其他短很多（1段 vs 3段）

**1.3 Discussion注入不确定性**
- 加入至少一处"What is solid / What remains uncertain"的显式区分
- 加入至少一处genuine speculation（与相邻领域的可能联系，标注为推测）
- 用"We do not yet have a clean explanation for..."替代对所有结果的完美解释
- 不要覆盖所有可能的limitation——只提最重要的1-2个，其余留给审稿人发现

**1.4 Conclusion去重**
- 不要逐条重述contributions
- 只用1段总结核心message（一句话level的insight + 一句话level的prediction）
- 最后一句可以是一个imagery或open question，不要是一个安全的总结句

### Phase 2: 句子层面调整

在结构重组完成后，逐段检查：

**2.1 句长变异**
- 每3-4句中必须有一句 ≤8词 或 ≥35词
- 禁止3句连续句长差<6词
- 允许偶尔的片段句（"Not second-order. First-order."）

**2.2 段落结构变异**
- 可用模板：question-driven / causal-chain / abrupt-end / compare-judge / position-counter
- 相邻段不同模板
- 允许段落在论证高潮处突然结束（不加总结句）

**2.3 语气注入**
- 每2000词至少2处first-person主动句（"We found / We initially expected / Our data show"）
- 每section允许1处轻口语化表达（"in other words" / "the picture is clear" / "this matters because"）
- 允许评价性开头（"The result is strikingly general" / "This was not what we expected"）

**2.4 连接词清除**
- 全面禁止：Furthermore / Moreover / Additionally / It is worth noting / In conclusion / To summarize
- 每1000词连接词（however/therefore/thus/hence）不超过4个
- 用自然逻辑流替代：直接并列、em-dash插入、分号连接

### Phase 3: 验证

**3.1 质量检查**
- 所有数值、公式、引用、图表引用是否完整保留？
- 科学claims是否有任何改变？（不允许）
- 论证逻辑是否因压缩而断裂？（读每段首句串联成story，检查是否连贯）
- 新加入的speculation是否标注为推测？（必须有"may" / "remains unclear" / "suggests but does not prove"）

**3.2 AI检测预评估**
自查以下指标：
- 句长标准差 > 25（目标40+）
- 连接词密度 < 4/1000词
- 是否存在至少3处"承认不确定"的表述
- 是否存在至少2处"不对称"的结构（一个subsection 1段 vs 另一个3段）
- Conclusion是否避免了逐条复述

**3.3 输出**
- 改写后的完整tex文件
- 纯文本md版本（strip LaTeX命令，供检测测试）
- 如有需要，编译PDF

## 禁止行为

- 不要只做句子层面的换词/加短句——这是medium tier的做法，效果有限
- 不要添加作者未提供的数据或证据
- 不要改变任何科学结论的强度（除非原文overclaim，那应该弱化）
- 不要把所有段落都改成一样的"人类风格"——人类的特点恰恰是不一致
- 不要声称"已经没有AI痕迹了"——给出具体指标让用户自己判断

## 关于学术质量

Deep humanization做对了不会降低质量，因为：
- 审稿人讨厌冗余roadmap段和逐条复述conclusion——删掉它们是提升
- 承认不确定性在physical sciences是加分项，说明作者有判断力
- 更短更密的论文审稿人更愿意读
- 结构不对称反映的是"有些结果更重要值得展开，有些不值得"的判断

唯一风险：如果有pre-print在先，revision后文风变化大。但这在审稿过程中很正常。

## 与PaperSpine的关系

本skill吸收了PaperSpine的5维检测模型（D1句长/D2段落骨架/D3信息密度/D4连接词/D5术语语境），但操作层面不同：
- PaperSpine medium tier：在保持结构不变的前提下做句子级调整 → 效果有限（仍有30%+检测率）
- 本skill：先做结构重组（Phase 1），再做句子调整（Phase 2）→ 目标<10%

两者可以配合使用：先用本skill做结构改写，再用PaperSpine的humanize_check脚本验证指标。

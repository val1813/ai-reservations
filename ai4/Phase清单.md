# AI4 Phase 执行清单

> 每个Phase开始前读取此文件。每完成一步，把 `[ ]` 改成 `[✅]`。
> ⛔ 严格顺序执行。前一步未全部✅，禁止进入下一步。

---

## Phase 0: Intake — 收稿与配置

```
[ ] 确认论文素材完整性:
    [ ] 论文草稿/素材目录存在?
    [ ] 已确认目标期刊? (PRL/PRD/PRX/Nature Physics/...)
    [ ] 已确认论文类型? (research/hypothesis/methods/algorithmic/review)
    [ ] 已确认输出语言? (English/Chinese)
[ ] 读 P1_build.md → 确认build模式 (rewrite_existing / build_from_materials)
[ ] ⛔ 术语提取: 从素材提取核心术语 → 建立术语分类账 (见 P1_build.md §术语分类账)
    [ ] 每个术语: 规范形式 + 首次展开 + 来源变体
    [ ] 检查冲突: 同一概念多个名称? 同一名称两个概念?
    [ ] 锁定: 后续所有Agent只使用规范形式
[ ] 创建输出目录: paper_output/
[ ] 写 paper_output/paper_spine_config.json (目标期刊+类型+语言+深度)
```

---

## Phase 0.5: Author Persona Generation — 作者人格生成 ⛔ 新增

```
[ ] 读 P0_5_author_persona.md → 执行作者人格生成

[ ] 启动PERSONA Agent (独立实例):
    传入素材/草稿 + Phase 0配置信息
[ ] PERSONA Agent 输出 → 写 paper_output/author_voice_card.md
    ⛔ Voice Card必须填充全部5个维度,不得留空

[ ] PI审核Voice Card:
    [ ] 问题起源是否具体? (非"这是重要问题")
    [ ] 每个section有审美立场? (至少1句美/丑判断)
    [ ] 信念梯度覆盖所有核心声称?
    [ ] 人格化特征标注了具体使用位置?
    [ ] 注意力分配指定了"最在意"和"无聊但必要"?
    [ ] 禁止项具体到这篇论文?

[ ] ⛔ Voice Card成为绑定文档:
    后续所有Agent启动时必须读取 author_voice_card.md
    PI在启动每个Agent时在prompt中注入:
    "读取 author_voice_card.md。你的所有修改必须保持Voice特征。
     如果修改会破坏Voice特征,标注并寻求替代方案。"
```

## Phase 1: PaperSpine Build — Motivation驱动构建

```
[ ] 读 P1_build.md → 按步骤执行

### 1a. 研究与学习
[ ] 调研目标期刊要求 (读 journal_configs/[期刊].md)
[ ] 收集3-6篇目标期刊近两年优秀范文 (paper-search-mcp)
[ ] 读范文 → 提取: 结构模板 + 叙述弧线 + 引用密度 + 图表规范
[ ] 写 paper_output/research_dossier.md
[ ] 写 paper_output/exemplar_learning_dossier.md

### 1b. Motivation确认
[ ] 从素材提取核心motivation → 写 paper_output/confirmed_motivation.md
    格式: 一句话motivation + 三段论证(问题→现状→为何现在可解)
[ ] ⛔ Reader 5问检验 (来自nature-skills):
    Q1 Relevance: 第一段能让非本领域读者理解为什么重要?
    Q2 Novelty: 摘要能清晰区分"前人做了什么"和"我们做了什么新东西"?
    Q3 Trust: 每个核心声称有≥1种独立验证方式?
    Q4 Reuse: 方法和数据是否足够让同行复现?
    Q5 Meaning: 是否诚实讨论了边界和局限?

### 1c. 引用支持库
[ ] 启动引用Agent (P1_build.md §引用支持库)
    候选池: 目标引用数×3 (默认20×3=60)
    近期占比: ≥80%来自近三年(2024-2026)
[ ] 每个候选引用绑定到具体claim → 写 paper_output/citation_support_bank.md
[ ] ⛔ Fetch验证: 逐一验证引用真实性。幻觉引用→阻断。

### 1d. 写作思路矩阵
[ ] 为论文每个section/段落写写作理由:
    该单元承担什么功能? 服务哪个motivation?
    学习了哪些范文? 使用什么证据?
    预期通过什么检查?
[ ] 写 paper_output/writing_rationale_matrix.md

### 1e. 构建/重写论文
[ ] 根据writing_rationale_matrix逐段生成正文
    ⛔ 术语锁定: 只使用Phase 0确认的规范术语
    ⛔ 引用锁定: 只引用citation_support_bank中已验证的文献
[ ] 写 paper_output/final_paper/main.tex (初稿)
[ ] ⛔ 禁词扫描: grep初稿 → "原则上可能"等→修正
[ ] ⛔ 数据优先: 有实际数据可验证的声称→用py脚本验证后再写入
```

## Phase 2: Scientific Review — R1-R5 技术审稿循环 (含每轮Voice保护)

```
[ ] 读 P2_review.md → 按步骤执行

每一轮 (R1→R2→R3→R4→R5):
  [ ] 启动REVIEWER Agent (独立实例, P2_review.md prompt)
      传入三份材料: 正文(main.tex) + SM(supplemental_material.tex) + CoverLetter(cover_letter.tex)
      ⛔ REVIEWER只审技术正确性,不审语气/诚实度/叙事(见P2 §1)
  [ ] PI过滤审稿意见: 如果REVIEWER提出语气/态度类意见 → 驳回,不传给FIX Agent
      + 目标期刊 + 上一轮审稿报告(如有)
  [ ] REVIEWER输出 → 写 paper_output/review_R[N].md
      (报告必须分三个section: 正文审稿/SM审稿/CoverLetter审稿)
  [ ] PI读审稿报告 → 分类: FATAL/MAJOR/MINOR (三份材料分别标注)
  [ ] ⛔ 如果是R1且裁决Reject:
      必须在Phase清单"期刊跟踪"区写降级判断
  [ ] 启动FIX Agent (独立实例) → 修改三份文件
      ⛔ FIX Agent启动时必须读取 author_voice_card.md (Voice保护规则见P2 §4b-bis)
      ⛔ 正文/SM/CoverLetter都必须修改到审稿意见全部回应
      ⛔ 科学修正不能靠文字绕过。SM需要补数据就补数据
      ⛔ CoverLetter声称必须与正文/SM一致,不能夸大
  [ ] INSPECTOR校对修改处 (量纲/方向/量级/循环论证)
  [ ] ⛔ INSPECTOR每轮Voice退化检查:
      [ ] 本轮是否删除了审美判断句? → 标注Voice退化 → 本轮内恢复
      [ ] 本轮是否弱化了信念梯度(Level A→B/C)? → 标注→本轮内恢复
      [ ] 本轮是否删除了人格化特征? → 标注→本轮内恢复
      [ ] 本轮是否修匀了段落长度? → 标注→本轮内恢复
      [ ] 本轮是否扩散了限制条件? → 标注→本轮内恢复
      ⛔ Voice退化不能累积。每轮独立通过。
  [ ] 写 paper_output/fix_R[N].md (分正文/SM/CoverLetter三个section)
  [ ] 更新三份文件: main.tex + supplemental_material.tex + cover_letter.tex

每轮REVIEWER后检查硬退出闸门 (详见 P2_review.md §5):
  [ ] ⛔ R1: 触发即死条件? (可检验性=0/核心证明错误/先发覆盖/范畴错误/数据不可得)
      → 🛑 立即停止。降级归档。不浪费R2-R5。
  [ ] ⛔ R2: FATAL数≥R1? → 🛑 修复无效。诊断原因,必要时降级归档。
  [ ] ⛔ R3: FATAL仍>0且同根因? → ⛔ 框架级缺陷。降级目标期刊,停止R4/R5。

R5完成后:
  [ ] 累积FATAL数=0? → 进入Phase 2b
  [ ] 否则→检查是否所有FATAL已修复
```

---

## Phase 2b: Narrative Tension Review — 叙事张力审查 ⛔ 新增

```
[ ] 读 P2b_narrative_review.md → 执行叙事审查

[ ] 启动NARRATIVE REVIEWER Agent (独立实例):
    传入R5修改后的正文 + 全部5轮审稿报告
[ ] REVIEWER输出 → 写 paper_output/narrative_review.md

[ ] PI执行删减:
    [ ] 自我贬低句删除 (对照P2b §3a黑名单,零容忍)
    [ ] 限制条件重复检查 (同一限制≥3次→保留首次+汇总,其余删)
    [ ] 元评论删除 ("This paper asks..."等关于论文本身的评论)
    [ ] 第一页测试: 前500词无任何自我贬低句
    [ ] 同一技术限制出现次数≤2

[ ] 删减后验证:
    [ ] grep "may be nothing\|Not even close\|We couldn't\|would be dishonest"
    [ ] grep "not surprising\|weaker than what one might\|consistency check, not"
    [ ] grep "for the reader to judge\|cannot stress that enough\|It isn't one"
    [ ] 命中→继续删除

[ ] ⛔ 零容忍终检: 全文自我贬低句数=0 → 进入Phase 3
    (叙事审查只删减防御性语言,不改变技术内容 → 不需重新跑Phase 2)
```

## Phase 3: Journal Format — 目标期刊格式化

```
[ ] 读 P3_format.md + journal_configs/[期刊].md
[ ] 格式校验:
    [ ] 字数在期刊限制内? (正文/摘要/图表标题各不超过上限)
    [ ] Section结构符合期刊要求?
    [ ] 图表格式符合期刊规范? (分辨率/字体/标注)
    [ ] 引用格式符合期刊要求?
    [ ] SM补充材料完整?
[ ] ⛔ 图表核验:
    [ ] 所有图由Python生成(非LLM生成)?
    [ ] 图和正文数值对得上?
    [ ] 误差棒合理?
    [ ] 审稿人只看图能理解论文创新点?
[ ] 写 Cover Letter:
    [ ] 用P3_format.md §Cover Letter格式
    [ ] 一句话finding + 一句话novelty + 一句话cross-disciplinary significance
    [ ] ⛔ 不出现"We hope" / "We are confident"
[ ] 更新 paper_output/final_paper/main.tex
```

## Phase 3.5: Competitive Benchmark — 同期录用论文PK

```
[ ] 读 P3_5_benchmark.md → 执行竞争力评估
[ ] 用 paper-search-mcp 搜索目标期刊最新录用/发表论文 → 选3篇最有可比性的
[ ] 6维加权评分: 问题重要性(×3)+证据强度(×3)+叙事质量(×2)+新颖性(×2)+受众广度(×1)+技术深度(×1)
[ ] 裁决:
    我们 > 对手×1.1 → ✅ 进入Phase 4
    我们 ≈ 对手(±10%) → ⚠️ 优化弱项后重PK(最多2次)
    我们 < 对手×0.9 → 🛑 必须优化。2次后仍不达标→降级期刊
[ ] ⛔ 如果触发内容修改 → 修改后必须重新跑Phase 4
```

## Phase 4: AI Detection — Structure Randomizer 重构

```
[ ] 读 P4_randomize.md → 严格按流程执行
[ ] ⛔ 确认: Phase 2和3的所有内容修改都已完成。此步之后禁止任何内容修改!

### 4a. Deep-Humanize 结构诊断
[ ] 启动 deep-humanize Agent (独立实例, P4_randomize.md §Phase 0)
    诊断6个致命对称 + 结构重组(删roadmap/合并section)
    输出: paper_output/restructured_draft.tex

### 4b. Structure Randomizer 生成Blueprint
[ ] ⛔ 先分类每段: 去掉公式后计算formula_ratio
    Type T(<30%公式)→完整14维 | Type M(30-60%)→6维 | Type E(>60%)→仅2维
    (详见P4_randomize.md §7a。公式段落的句长/密度参数无意义)
[ ] 为目标期刊计算W_total (总词数上限)
[ ] 确定section列表和各section段落数
[ ] 为全文所有段落一次性生成14维参数: [S,T,P,K,W,E,D,C,R,V,F,B,L,H]
    Type E段只生成T,V。Type M段跳过S/K/W/D/F/L/H。
[ ] ⛔ 全局约束校验 (只对Type T段落):
    S std>2.5 / W std>4.0 / S range≥6 / W range≥10
    相邻T不同 / 连续H≤2 / T值无一占>35% / E=3≤3次 / V=1≤70%
    AI Pattern检测: Pattern B/D/E风险 → 自动修正
    无周期≤4的重复pattern
    不通过→整体重新生成(不是修补)
[ ] 写 paper_output/blueprint.md

### 4c. 按Blueprint逐段重写
[ ] 每段严格服从14维参数(弹性: S±1, W±3, 其余精确)
[ ] 特别注意: F(冗余句) B(逻辑断裂) L(列举限制) H(句长分散)
[ ] 输出: paper_output/final_draft.tex

### 4d. 去AI处理 — SM补充材料
[ ] 只对文字说明段执行8维简化参数(去掉R/P)
    Derivation和表格不参与
    检查: ①各subsection引言句是否重复 ②结尾是否都用相同句式 ③说明段长度是否不等

### 4e. 去AI处理 — Cover Letter
[ ] 执行3维轻量参数(W_sentence/V_sentence/Break逐句控制)
    检查: ①contribution list各条长度不等 ②无"We hope/We are confident" ③最后一句不是安全收尾句

### 4f. AI Pattern 终检 (结构+词汇+Voice PRESENCE)

#### 4f-1. AI缺失检查 (原有 — 底线扫描)
[ ] 结构扫描: 对仗禁止/分号对仗/sentence frame重复→REJECT
[ ] 穷举扫描: "spanning A,B,C,and D"全文≤1次
[ ] ⛔ 去AI词汇扫描 (详见P4_randomize.md §8):
    禁止连接词(Moreover/Furthermore/Nevertheless/In conclusion等10个)
    禁止句式(Not X;it is Y/分号对仗/穷举)
    禁止hedging(6个禁句)
    连接词密度≤4/1000词
[ ] 不确定性表达: V=3的2-3次使用必须来自不同子类(3a/3b/3c/3d)
[ ] Abstract特殊规则: 禁"Here we present"/contribution list不等长/最后句非安全收尾

#### 4f-2. ⛔ Voice PRESENCE检查 (新增 — Voice特征存在于否)

```
⛔ 这不是"有没有AI词汇"的检查。这是"作者人格还在不在"的检查。
⛔ 如果Voice特征在Phase 4随机化过程中被削弱 → ⛔ 阻断,必须恢复。

[ ] 读取 paper_output/author_voice_card.md → 逐项对比终稿:

[ ] 信念梯度 PRESENCE:
    [ ] Level A声称(断言句式)是否仍存在且未被弱化?
        检查: grep Voice Card中的Level A声称关键词 → 确认句式仍是断言
        如果发现 "X may hold" / "X might be" 替代了 "X holds" → ⛔ Voice退化
    [ ] Level B声称是否仍使用supported句式?
    [ ] Level D痛点是否只出现在Open Questions?

[ ] 审美判断 PRESENCE:
    [ ] 每个section是否仍有≥1句审美判断?
        检查: 逐个section扫描 → 是否有 "This is ugly but" / "I like" / "prettiest" 类句子
        如果某个section完全没有 → ⛔ Voice退化,该section需注入1句审美判断

[ ] 人格化特征 PRESENCE:
    [ ] Voice Card标注的特征是否仍存在?
        检查: 口语短句/第一人称/读者对话/比喻 → 在指定位置搜索
        如果全部被删除 → ⛔ Voice退化

[ ] 注意力分配 PRESENCE:
    [ ] "最在意"段落是否仍>8句?
    [ ] "无聊但必要"段落是否仍≤2句?
    [ ] 全文极短段(≤2句)是否≥2段?
    [ ] 全文极长段(≥8句)是否≥1段?
    如果被Phase 4 randomizer修匀了 → ⛔ Voice退化

[ ] 禁止项 PRESENCE:
    [ ] Voice Card中"这个人不会说"的短语是否确实未出现?

⛔ 任一项Voice退化 → 必须修复后再进入Phase 4g
   Voice修复优先级:
     审美判断缺失 → 注入 (不改变技术内容,只在现有段落加1句立场)
     人格化特征缺失 → 恢复 (简单)
     注意力被修匀 → 调整段落划分 (可能涉及结构)
     信念梯度退化 → 恢复原有断言句式 (关键,不能接受Level A变Level C)
```

### 4g. 输出三份LaTeX文件
[ ] ⛔ 确认三份.tex文件均存在且已去AI处理:
    [ ] paper_output/final_paper/main.tex
    [ ] paper_output/final_paper/supplemental_material.tex
    [ ] paper_output/final_paper/cover_letter.tex
```

## Phase 5: Final Audit — 完整性验证与输出

```
[ ] 读 P5_audit.md → 执行审计
[ ] 文献核验: 逐一fetch验证引用真实性 → 幻觉引用清单
[ ] ⛔ AI致谢检查: grep全文+致谢+CoverLetter →
    "Claude"|"AI辅助"|"LLM"|"ChatGPT"|"Anthropic"|"人工智能辅助写作"
    命中→⛔阻断,必须删除。AI4是写作工具不是作者。
[ ] 数据核验: 数据可由代码复现? 非随机生成/经验复用?
[ ] ⛔ LaTeX编译: 每份执行 pdflatex→bibtex→pdflatex→pdflatex (2遍才解析引用!)
    ⛔ 只跑1遍→引用全部[?]。必须2遍。
    [ ] main.tex → paper.pdf (4步: pdflatex+bibtex+pdflatex+pdflatex)
    [ ] supplemental_material.tex → supplemental_material.pdf (同上)
    [ ] cover_letter.tex → cover_letter.pdf (pdflatex×2,通常无引用)
    [ ] grep "[?]" 或 "Citation.*undefined" → 引用未解析→⛔阻断
[ ] 最终禁词扫描: 全文grep禁词 → 命中→回Phase 4重写
[ ] 最终格式核验: 逐项对照期刊要求
[ ] 写 paper_output/final_artifact_manifest.md (完整产物清单)
[ ] ⛔ 完整性检查: 以下文件全部存在?
    [ ] paper_output/final_paper/main.tex
    [ ] paper_output/final_paper/supplemental_material.tex
    [ ] paper_output/final_paper/cover_letter.tex
    [ ] paper_output/final_paper/references.bib
    [ ] paper_output/final_paper/figures/ (所有图)
    [ ] paper_output/final_paper/paper.pdf (正文PDF,编译成功)
    [ ] paper_output/final_paper/supplemental_material.pdf (SM PDF,编译成功)
    [ ] paper_output/final_paper/cover_letter.pdf (CoverLetter PDF,编译成功)
    [ ] paper_output/citation_support_bank.md
    [ ] paper_output/writing_rationale_matrix.md
    [ ] paper_output/blueprint.md
    [ ] paper_output/review_R1.md ~ review_R5.md
    [ ] paper_output/fix_R1.md ~ fix_R5.md
    [ ] paper_output/narrative_review.md (叙事审查报告)
[ ] 输出: 告知用户投稿包路径
```

---

## 禁止事项

```
⛔ 禁止跳过Phase顺序 (0→1→2→2b→3→3.5→4→5严格顺序)
⛔ 禁止在Phase 4(randomizer)后修改论文内容 (改后必须重新跑Phase 4)
⛔ 禁止REVIEWER不独立启动Agent (PI扮演审稿人=违规)
⛔ 禁止引用未fetch验证的文献
⛔ 禁止图表由LLM生成 (必须Python/matplotlib等)
⛔ 禁止论文中致谢AI工具 (Claude/AI辅助/LLM/ChatGPT等)
⛔ 禁止禁词出现在终稿中
⛔ 禁止跳过AI检测重构就投稿
⛔ 禁止跳过Phase 2b叙事审查 (即使Phase 2 FATAL=0也必须执行,防御性语言是独立问题)
```

## 期刊跟踪区

```
(由PI在R1 REVIEWER后填写, 每轮更新)

目标期刊: [___]
R1裁决: [___] → 降级? [是/否] → 如是: 新目标[___]
R2裁决: [___]
R3裁决: [___]
R4裁决: [___]
R5裁决: [___]
最终投稿期刊: [___]

SM检查: [通过/未通过]
Cover Letter检查: [通过/未通过]
AI检测预期: [预计检测率<__%]
```

## 容错

```
Agent超时/格式错误 → 自动重试1次 → 仍失败 → PI手动接管 + 记录到卡点登记册
Phase清单.md 就是状态管理器。断点重开 → 读清单 → 从第一个 [ ] 继续
```

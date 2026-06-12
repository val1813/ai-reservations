# AI4 — 论文写作自动化引擎 v1.2

> **定位**: 从"课题组确认可发表"到"投稿就绪"的完整自动化流水线
> **上游依赖**: ai2 (SELECTOR选题) → ai (research-group科研推进) → 产出论文素材
> **触发条件**: 课题组确认论文可投稿，用户说"开始写论文"/"投稿准备"/"ai4"
> **输出**: 投稿就绪的LaTeX论文包 + SM + Cover Letter

---

## 架构原则

```
科研产出(ai/ai2) → AI4写作引擎 → 投稿就绪
                      │
          ┌───────────┼───────────────┐
          │           │               │
     Author Persona  技术审稿+叙事审查  structure-randomizer
     (Voice Card)    (科学质量+人性)   (结构随机化+Voice PRESENCE检查)
```

**四个核心洞察:**
1. **作者人格先行** — Phase 0.5生成Voice Card,所有后续Agent代入这个具体角色写作
2. **motivation驱动** — 确认论文核心动机再写正文 (来自PaperSpine)
3. **对抗+制衡** — 5轮技术审稿(R1-R5)+1轮叙事审查(P2b)+每轮Voice退化检查→对抗过度保守
4. **去AI = 禁止底线 + Voice要求** — 双轨制:不做什么(8a-8k)+必须做什么(8l),Voice PRESENCE检查

**⛔ 关键顺序**: Author Persona → 科学审稿(每轮含Voice检查) → 叙事审查 → 格式化 → AI检测重构。
  Voice Card贯穿全流程,Phase 4f检查Voice PRESENCE而非仅AI ABSENCE。

---

## 流水线总览

```
Phase 0: Intake — 收稿+配置
  ├── Phase 0.5: Author Persona — 作者人格生成 (Voice Card绑定文档)
  ├── Phase 1: PaperSpine Build — motivation+Voice驱动写论文
  ├── Phase 2: Scientific Review — R1-R5技术审稿 (每轮含Voice退化检查)
  ├── Phase 2b: Narrative Tension Review — 防御性语言清除+Voice一致性审计
  ├── Phase 3: Journal Format — 目标期刊格式化
  ├── Phase 3.5: Competitive Benchmark — 同期录用论文PK
  ├── Phase 4: AI Detection — structure-randomizer (双轨:禁止+Voice要求)
  └── Phase 5: Final Audit — 完整性验证+输出
```

每个Phase的详细流程在对应子文件中。

---

## ⛔ 全局硬规则

```
1. 顺序不可变: 0→0.5→1→2→2b→3→3.5→4→5 严格顺序。前一步未完成禁止进入下一步。
2. Voice Card绑定: 所有Agent启动时必须读取 author_voice_card.md,修改必须保持Voice特征。
3. 审稿人独立: 每轮REVIEWER必须用Agent工具启动独立实例,禁止PI扮演审稿人。
4. 数据优先: 能用实际数据+py验证的→优先跑。可验未验=不可检验。
5. 禁词阻断: 全流程禁止"原则上可能""待未来实验"等。见ai/PI.md §0.5。
6. 文献真实性: 所有引用必须fetch验证,幻觉引用→阻断级错误。
7. 图表生成: 所有图必须Python生成(matplotlib/seaborn等)。严禁LLM生成图像。
8. ⛔ 禁止致谢AI: 论文正文/致谢/Cover Letter中不得出现"Claude""AI辅助""LLM"
   "ChatGPT""Anthropic""人工智能辅助写作"等任何AI工具致谢字样。
9. AI检测最后: structure-randomizer必须在所有内容修改完成后执行。
10. ⛔ 禁止跳过Phase 0.5和Phase 2b: Voice Card和叙事审查是强制步骤。
11. 每轮Voice退化检查: Phase 2每轮INSPECTOR检查Voice是否被FIX Agent削弱,发现→本轮内恢复。
12. Voice > AI禁止: 当Voice特征与AI禁止清单冲突时,Voice优先(除非涉及防御性语言或技术错误)。
```

---

## 文件索引

| 文件 | 内容 | 行数限制 |
|------|------|---------|
| `README.md` (本文件) | 入口+架构+规则 | ≤120 |
| `Phase清单.md` | 执行清单(PI逐项勾选) | ≤350 |
| `P0_5_author_persona.md` | 作者人格生成(Voice Card绑定文档) | ≤250 |
| `P1_build.md` | PaperSpine build: motivation+Voice+引用库 | ≤350 |
| `P2_review.md` | R1-R5技术审稿(只审逻辑/数学/证据,含Voice保护) | ≤400 |
| `P2b_narrative_review.md` | 叙事张力审查+防御性清除+Voice一致性 | ≤400 |
| `P3_format.md` | 期刊格式化(PRL/PRD/Nature等) | ≤200 |
| `P3_5_benchmark.md` | 同期录用论文PK(6维加权对比) | ≤200 |
| `P4_randomize.md` | structure-randomizer 14维+双轨(禁止+Voice要求) | ≤550 |
| `P5_audit.md` | 完整性验证+最终检查 | ≤150 |
| `journal_configs/` | 各期刊配置(格式/字数/章节要求) | 每文件≤100 |

---

## 与 ai/ai2 的关系

```
ai2/SELECTOR → 选题 → ai/research-group → 科研推进 → 论文素材
                                                      ↓
                                                  AI4 ← 开始写作
```

AI4不负责选题和科研推进。它假设输入的是"已经过ai2选题+ai科研推进验证过的论文素材"。

---

## 快速启动

```
新对话:
1. 读 ai4/Phase清单.md → 从第一个[ ]开始执行
2. 按需读对应子文件(P0_5, P1-P5)
3. 全部[✅]后输出投稿包
```

---

## 版本

v1.2 — Phase 0.5 Author Persona(Voice Card)+P2/P2b/P4全流程Voice保护+双轨制(禁止+要求)+每轮Voice退化检查
v1.1 — 新增Phase 2b叙事张力审查(反制衡恶意审稿人保守化),P1/P2/P4防御性语言禁令
v1.0 — 吸收PaperSpine(motivation驱动)+structure-randomizer(14维参数)+5轮审稿人

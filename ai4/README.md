# AI4 — 论文写作自动化引擎 v1.0

> **定位**: 从"课题组确认可发表"到"投稿就绪"的完整自动化流水线
> **上游依赖**: ai2 (SELECTOR选题) → ai (research-group科研推进) → 产出论文素材
> **触发条件**: 课题组确认论文可投稿，用户说"开始写论文"/"投稿准备"/"ai4"
> **输出**: 投稿就绪的LaTeX论文包 + SM + Cover Letter

---

## 架构原则

```
科研产出(ai/ai2) → AI4写作引擎 → 投稿就绪
                      │
          ┌───────────┼───────────┐
          │           │           │
     PaperSpine   恶意审稿人   structure-randomizer
     (motivation  (科学质量)   (AI检测规避)
      驱动写作)
```

**三个核心洞察:**
1. **motivation先行** — 确认论文核心动机再写正文 (来自PaperSpine)
2. **科学质量靠对抗** — 5轮恶意审稿人模拟真实审稿流程 (来自现有SOP)
3. **AI检测靠统计方差** — 随机化段落参数,不靠换词 (来自structure-randomizer)

**⛔ 关键顺序**: 科学审稿 → 期刊格式化 → AI检测重构。randomizer必须在最后!
  (因为randomizer打乱的是表层结构,不影响科学内容,但会影响审稿人看到的文本)

---

## 流水线总览

```
Phase 0: Intake — 收稿+配置
  ├── Phase 1: PaperSpine Build — motivation驱动写论文
  ├── Phase 2: Scientific Review — R1-R5恶意审稿人循环
  ├── Phase 3: Journal Format — 目标期刊格式化
  ├── Phase 4: AI Detection — structure-randomizer重构
  └── Phase 5: Final Audit — 完整性验证+输出
```

每个Phase的详细流程在对应子文件中。

---

## ⛔ 全局硬规则

```
1. 顺序不可变: Phase 0→1→2→3→4→5 严格顺序。前一步未完成禁止进入下一步。
2. 审稿人独立: 每轮REVIEWER必须用Agent工具启动独立实例,禁止PI扮演审稿人。
3. 数据优先: 能用实际数据+py验证的→优先跑。可验未验=不可检验。
4. 禁词阻断: 全流程禁止"原则上可能""待未来实验"等。见ai/PI.md §0.5。
5. 文献真实性: 所有引用必须fetch验证,幻觉引用→阻断级错误。
6. 图表生成: 所有图必须Python生成(matplotlib/seaborn等)。严禁LLM生成图像。
7. ⛔ 禁止致谢AI: 论文正文/致谢/Cover Letter中不得出现"Claude""AI辅助""LLM"
   "ChatGPT""Anthropic""人工智能辅助写作"等任何AI工具致谢字样。
   这是学术诚信红线——AI4是写作工具,不是作者。
8. AI检测最后: structure-randomizer必须在所有内容修改完成后执行。
   任何在randomizer之后的内容修改→必须重新跑randomizer。
7. 上下文管理: 每个子文件≤400行。Agent启动时只传对应子文件,不传全文。
8. MCP搜索: 文献搜索必须先用paper-search-mcp,失败才降级WebSearch。
```

---

## 文件索引

| 文件 | 内容 | 行数限制 |
|------|------|---------|
| `README.md` (本文件) | 入口+架构+规则 | ≤100 |
| `Phase清单.md` | 执行清单(PI逐项勾选) | ≤250 |
| `P1_build.md` | PaperSpine build: motivation+rationale+引用库 | ≤300 |
| `P2_review.md` | 5轮恶意审稿人循环 | ≤250 |
| `P3_format.md` | 期刊格式化(PRL/PRD/Nature等) | ≤200 |
| `P4_randomize.md` | structure-randomizer 14维参数+全局约束 | ≤350 |
| `P5_audit.md` | 完整性验证+最终检查 | ≤150 |
| `journal_configs/` | 各期刊配置(格式/字数/章节要求) | 每文件≤100 |
| `scripts/` | Python验证脚本 | N/A |

---

## 与 ai/ai2 的关系

```
ai2/SELECTOR → 选题 → ai/research-group → 科研推进 → 论文素材
                                                      ↓
                                                  AI4 ← 开始写作
```

AI4不负责选题和科研推进。它假设输入的是"已经过ai2选题+ai科研推进验证过的论文素材"。
素材可以是: LaTeX草稿、markdown笔记、实验数据、推导文件、文献库等。

---

## 快速启动

```
新对话:
1. 读 ai4/Phase清单.md → 从第一个[ ]开始执行
2. 按需读对应子文件(P1-P5)
3. 全部[✅]后输出投稿包
```

---

## 版本

v1.0 — 吸收PaperSpine(motivation驱动)+structure-randomizer(14维参数)+5轮审稿人

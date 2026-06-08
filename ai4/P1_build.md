# P1: PaperSpine Build — Motivation驱动论文构建

> 角色: 论文建筑师。不润色句子，而是确认"为什么这样写"后再动笔。
> 核心原则: Motivation先行 → 结构设计 → 引用支撑 → 逐段构建
> 输入: 科研素材(草稿/数据/推导/文献)
> 输出: paper_output/final_paper/main.tex (初稿) + 完整写作轨迹

---

## §1 两种模式

根据输入类型选择:

```
模式A — rewrite_existing: 已有完整草稿 → 基于motivation重写
模式B — build_from_materials: 只有散装素材 → 从零构建论文

两种模式共用 research → citation → rationale → build 流程。
```

---

## §2 研究与学习

### 2a. 目标期刊调研

读 `journal_configs/[期刊].md` 获取:
- 字数限制(正文/摘要/图表)
- Section结构要求
- 引用格式 + 图表规范
- 投稿checklist

### 2b. 范文学习

用 paper-search-mcp 搜索目标期刊近两年论文:
- flash模式: 3篇范文
- pro模式: 6篇范文

读每篇范文 → 提取:
- 结构模板: section顺序+段落数+每段功能
- 叙述弧线: Introduction如何从broad→narrow→specific gap
- 引用密度: 每段引用数 + 自引比例
- 图表规范: 图类型/分辨率/配色/标注格式

→ 写 paper_output/exemplar_learning_dossier.md (每篇范文学习笔记)
→ 写 paper_output/research_dossier.md (综合调研发现)

---

## §3 Motivation确认

### 3a. 提取核心Motivation

从素材中提取 → 写成三段式:

```
1. 问题: [一句话 — 什么物理问题/矛盾?]
2. 现状: [前人尝试了什么? 为什么不够? 具体引用支撑]
3. 窗口: [为什么现在可解? 新工具/新数据/新视角是什么?]
```

### 3b. Reader 5问检验 (来自nature-skills)

```
Q1. Relevance: 第一段能让非本领域读者理解为什么重要?
   检验: 给你隔壁领域的同事读第一段→他能说出"为什么重要"吗?
Q2. Novelty: 摘要能清晰区分"前人做了什么"和"我们做了什么新东西"?
   检验: 画一条线,线左边是前人工作,线右边是本文贡献→两边不能重叠
Q3. Trust: 每个核心声称有≥1种独立验证方式?
   检验: 列出所有声称→每个旁边标注验证方式(数据/推导/引用/数值实验)
Q4. Reuse: 方法和数据是否足够让同行复现?
   检验: 假设你删除了自己所有记忆→只看方法和数据部分能复现吗?
Q5. Meaning: 是否诚实讨论了边界和局限?
   检验: 列出所有假设→每个旁边标注"如果这个假设不成立会怎样?"
```

→ 写 paper_output/confirmed_motivation.md

---

## §4 术语分类账 (来自nature-skills)

### 4a. 提取

扫描素材 → 提取所有反复出现的领域术语:
- 方法名/数据集名/基因名/度量名/缩写/核心概念

### 4b. 建立规范

每个术语记录:
| 规范形式 | 首次展开 | 来源变体 |
|---------|---------|---------|
| DGF | Discrete Graph Framework | DGF/离散图框架/图框架 |

### 4c. 检查冲突

- 同一概念用了不同名称? → 统一为规范形式
- 同一名称指代两个概念? → 拆分命名

### 4d. 锁定

⛔ 后续所有Agent的prompt中注入术语分类账作为硬约束。
术语一致性优先于词汇多样性。

---

## §5 引用支持库

### 5a. 参数

- 目标引用数: 20 (默认,可根据期刊调整)
- 候选池: 目标引用数×3 = 60
- 近期占比: ≥80%来自近三年(2024-2026)

### 5b. 构建流程

1. 从confirmed_motivation中提取所有需要引用支撑的claims
2. 对每个claim用 paper-search-mcp 搜索候选文献
3. 每个候选包含: BibTeX信息 + 年份 + 来源 + 1-2句可支撑正文论述的句子

### 5c. Fetch验证

⛔ 逐一Fetch验证引用真实性。幻觉引用→阻断级错误。
未能fetch的→列出清单交用户手工核验。

→ 写 paper_output/citation_support_bank.md

---

## §6 写作思路矩阵

为论文每个section/段落写写作理由。格式:

```
## [Section Name]
### [Paragraph N]
- 功能: 该段在论文中承担什么功能?
- 服务Motivation: 该段回答Reader 5问中的哪一问?
- 范文参考: 学习了哪篇范文的哪个段落?
- 证据: 使用了什么证据?(引用/数据/推导/数值)
- 来源: 证据来自素材的哪个文件?
- 检查: 预期通过什么检查?
```

→ 写 paper_output/writing_rationale_matrix.md

---

## §7 构建/重写论文

### 7a. 逐段构建

按writing_rationale_matrix逐段生成正文:
1. 读取该段的rationale
2. 读取对应的引用(citation_support_bank中已验证的)
3. 读取对应的数据/推导(素材中)
4. 生成正文 → 写入 main.tex

⛔ 术语锁定: 只使用术语分类账中的规范形式
⛔ 引用锁定: 只引用citation_support_bank中已验证的文献
⛔ 禁词: 不使用"原则上可能""待未来实验"等

### 7b. 初稿后检查

- 禁词扫描: grep初稿 → 命中即修正
- 数据优先: 有实际数据可验证的声称 → 用py脚本验证结果再写入
- 引用一致性: 所有\cite{}都在references.bib中有对应条目

→ 输出 paper_output/final_paper/main.tex (初稿)

## 策略 S2：近两年实验-理论张力扫描（最高优先级）

核心逻辑：找近两年实验论文里已有真实数据但理论解释不完整的矛盾。不需要GPU，不需要数值计算，做的是理论分析解释已有实验数据。这是最接近爱因斯坦模式的路径：实验数据已经在那里，你给出解释。

搜索工具：paper-search-mcp（主）→ web_search（降级）

第一步：扫描近两年实验异常论文（2024-2026）
  搜索1（明确承认解释不了的）：
    paper-search-mcp: "origin unclear mechanism unknown experiment 2024 2025 2026"
    paper-search-mcp: "calls for theoretical explanation measurement 2024 2025"
    paper-search-mcp: "puzzling anomalous unexpected experiment condensed matter 2025 2026"
  搜索2（定量偏离类）：
    paper-search-mcp: "inconsistent with theory discrepancy factor experiment 2024 2025"
    paper-search-mcp: "cannot be explained standard model measurement physical review 2024 2025"
    paper-search-mcp: "deviation prediction observation 2024 2025 PRL PRB"
  搜索3（争议类，多个实验组数据不一致）：
    paper-search-mcp: "contradicts previous measurement debate 2024 2025"
    paper-search-mcp: "in contrast to conflicting experimental results 2024 2025"
  ↓ paper-search-mcp无结果 → web_search: "[同关键词] site:arxiv.org"

第二步：初筛（只看摘要，快速过滤）
  对每篇命中论文，读摘要，判断以下4个初筛条件：
    □ 有具体数值（不是只有定性描述）
    □ 数值和理论预测有明显偏离（摘要里提到了偏离或矛盾）
    □ 近两年发表（2024-2026）
    □ 至少一个独立实验组确认（不只是一篇单一实验室的论文）
  全部满足 → 进入第三步（全文核查）
  任一不满足 → 丢弃，继续下一篇

第三步：实验全文核查门（⛔强制，不可跳过）
  ⚠️ 必须读实验论文全文，不允许只读摘要。
  ⚠️ 用WebFetch读取论文全文（arXiv HTML版优先，PDF降级）。

  WebFetch: "https://arxiv.org/html/[arXiv号]"（HTML版，可读性更好）
  ↓ 无HTML版 → WebFetch: "https://arxiv.org/abs/[arXiv号]"（摘要+引用信息）
  ↓ 无法访问 → web_search: "[论文标题] full text" → WebFetch命中URL

  全文核查必须回答以下5个问题（任何一个回答"不确定"→该论文不可用）：

  Q1. 实验条件精确核查：
    样品制备方法是什么？测量条件是什么？
    如果"矛盾"来自两篇论文，两篇的样品和测量条件是否可以直接比较？
    条件不可比 → 矛盾可能是虚假的 → 标注，慎用

  Q2. 数值定义核查：
    论文里用的物理量有没有非标准定义？
    两个"矛盾"数值的定义是否完全相同？
    定义不一致 → 矛盾可能是虚假的 → 标注，慎用

  Q3. 误差棒核查：
    两个"矛盾"数值的误差棒是多少？
    误差棒内相容（偏离<2σ）→ 不是矛盾 → 丢弃
    偏离≥3σ → 真实矛盾信号 → 继续

  Q4. 作者自己的解释核查：
    论文Discussion部分有没有对这个异常提出过解释？
    如果已有合理解释 → 不是开放矛盾 → 丢弃
    如果解释不令人满意 → 继续

  Q5. 独立重复核查：
    有没有第二个独立实验组（不同机构）看到了同样的异常？
    只有一个实验室 → 可能是系统误差 → 标注⚠️高风险
    两个以上独立实验组 → 可靠性高 → 通过

  全文核查输出（写入候选条目的"实验全文核查"字段）：
    Q1-Q5的逐条回答
    核查结论：✅可用 / ⚠️高风险（说明原因）/ ❌虚假矛盾（说明原因）

第四步：矛盾精确化（全文核查通过后）
  从全文里提取：
    实验数值A：[具体数值 ± 误差] （来自正文Figure X / Table X）
    理论预测B：[具体数值 ± 来源] （来自引用文献正文，不是AI印象）
    偏离量：[σ数] （A-B的统计显著性）
    偏离方向：[A>B / A<B / 方向随参数变化]

  构造驱动矛盾：
    命题A（现有理论）：[理论预测X在系统参数范围P内成立]
    命题B（实验数据）：[实验测量Y，与X偏离Nσ，在相同参数范围P内]
    为什么不能同时为真：[一句话，精确]

第五步：L0自过滤（全部通过才输出）
  □ 全文核查通过（Q1-Q5全部✅或可接受的⚠️）
  □ 实验数值有具体来源（正文Figure/Table编号）
  □ 理论预测有文献支撑（不是AI印象）
  □ 偏离≥3σ
  □ 可以在不做数值计算的情况下推进理论分析（不需要GPU）
  □ 近两年发表（2024-2026）
  □ ⛔ 可检验性底线: ≥1个子命题可用现有公开数据2周内检验
    (全部依赖未实现工具→⚠️"可检验性赤字"，优先级降两级)

输出进入领域密度扫描（和S1-S8一样，先扫描领域密度再分解子命题）

⛔ 执行前必须确认 paper-search-mcp 可用。不可用→WebSearch兜底，产出中标注。

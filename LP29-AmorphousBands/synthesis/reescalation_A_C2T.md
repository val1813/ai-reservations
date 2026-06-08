# LP29-C2T Re-escalation 草案（A）

角色边界：A 博士草案；未读取 B 输出。  
对象：LP29-C2T / provenance-complete external joined table construction。  
触发：原 C2T 声张从“构建 provenance-complete external joined table”收缩为“构建 witness/executor blocker infrastructure；当前五个候选全 BLOCK”。

## 被杀死的声张

1. 原声张 X：现有来源足以构建 provenance-complete same-sample joined rows。  
   被证伪点：当前候选只有材料名、组成、来源族、报告值或候选标签；没有可审计的 same-sample crosswalk。`sample_id`、`structure_id`、`snapshot_id_or_window`、`label_provenance_id` 不能同时落在同一行/同一结构/同一样品上。

2. 原声张 Y：Round 3 blocker audit 足以作为收尾边界产物。  
   被证伪点：BLOCK/WARN/PASS 不能只是 CSV 或文字状态；必须由 witness payload 和 executor 从字段重新计算。否则 blocker audit 只是人工裁决，不是可复现对象。

3. 原声张 Z：schema/source inventory 本身足以让 BLOCK/WARN/PASS 可复现。  
   被证伪点：schema 和 source inventory 只能列出“需要什么”和“可能在哪里”，不能证明字段存在、同源、同样品、先于标签锁定、非泄漏、非合成、非同靶反演。可复现性需要机器可读 witness，而不是目录。

## 更大的声张

新的可成立声张不是“C2T 有边界”，而是：

**C2T 证明了外部材料验证中的 joined row 不是文献检索对象，而是 witness-executor 可判定对象；在非同一样品、多来源、图特征-输运标签拼接的无定形材料问题中，样品身份、外部标签独立性、图协议先验锁定、禁用控制和基线复现共同构成验证变量本身。没有这些 witness 时，验证对象并不存在，而不是数据暂缺。**

这比原声张更大。原声张只说“我们能不能从现有来源拼出一张 provenance-complete same-sample 表”。新声张说的是：**任何声称可外部验证的 graph/materials 结论，若依赖跨文献拼接，都必须先通过一个 witness-executor admissibility calculus；否则它不是低质量样本，而是未定义验证对象。** 换言之，C2T 从一个数据准备任务上升为材料信息学外部验证的可判定性协议。

## 为什么它不只是降级版边界

当前五个候选全 BLOCK 并不只是“没有找到好数据”。五个 BLOCK 的共同结构显示，失败不是偶然缺字段，而是同一个更深层约束反复出现：

- 材料名或组成相同不能生成 `sample_id`。
- 报告的 OI/O_s 或 transport label 不能自动生成 same-sample row。
- Srivastava/OI 的 `OI_norm` 不能替代 raw sum、normalization rule、pair cutoff、structure mapping。
- 图特征不能在标签之后选择 cutoff、Laplacian convention、rho budget normalization 或 attack protocol。
- carrier density、effective mass、mobility-edge、family/batch 等字段若与目标同源或同靶反演，就不是控制变量，而是泄漏路径。

这些不是普通 provenance 附注，而是变量定义条件。若 witness 不存在，`external validation row` 这个数学对象就不成立；executor 输出 BLOCK 是对象不存在证明，而不是保守人工判断。

## 可检验表述

新的声张可以被写成一个可证伪命题：

> 对 LP29-C2 类无定形材料图谱-输运外部验证任务，任一候选 joined row 只有在通过 witness payload schema 和 executor gates 后，才有资格进入 material validation；若 required joined fields、same-sample crosswalk、graph convention lock、external label independence、forbidden-control audit、以及适用的 OI/Srivastava reproduction gate 中任一项为 BLOCK，则该行不是失败样本，而是无效验证对象。

这个命题允许未来被反驳：只要找到一个候选 row，它在不满足这些 witness 条件的情况下仍能给出非泄漏、同样品、可复现、外部独立的材料验证，C2T 新声张就失败。反之，若所有可审计验证都必须经由这些 gates 才能成立，则 C2T 得到的是一个通用 admissibility theorem/protocol。

## 比原声张大的地方

原声张的影响范围是单个 joined table：能否把 Jankousky/Srivastava/Furubayashi 等来源拼成可验证行。

新声张的影响范围是外部验证方法论：它规定什么才算一行可验证材料数据。它覆盖：

- provenance-complete joined table 是否存在；
- BLOCK/WARN/PASS 是否可复现；
- baseline reproduction 是否可声张；
- graph-vs-baseline 或 graph-vs-label 结果是否有资格进入材料验证；
- 当前五个候选为何全部不能进入 validation。

因此，新声张至少与原声张同级，实际更大：原声张是“构建数据表”；新声张是“定义外部验证对象存在性的判定规则”。如果成立，它会改变后续 LP29-C2 乃至同类材料信息学论文中所有跨来源验证的准入标准。

## A 侧最强注册版本

**LP29-C2T-ReEsc-A：在无定形材料 graph-to-transport 外部验证中，provenance-complete row 的存在性可由 witness-executor gate system 判定；没有 machine-reviewable same-sample、graph-lock、label-independence、forbidden-control 和基线复现 witness 的候选，不是低置信验证行，而是未定义验证对象。当前五个候选全 BLOCK 是该判定系统的首个负例集，不是收尾边界。**

该命题保留当前事实边界：不声称 Srivastava 已复现，不声称 material validation 已执行，不声称图特征优于 OI/baseline。它把失败转化为更大的正面命题：C2T 给出了外部验证可成立之前必须满足的对象存在性条件。

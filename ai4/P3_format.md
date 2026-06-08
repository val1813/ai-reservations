# P3: Journal Format — 目标期刊格式化

> 角色: 期刊格式适配器。将论文从通用格式转换为目标期刊的精确格式。
> 输入: Phase 2审查通过的稿件
> 输出: 符合期刊格式要求的稿件 + Cover Letter

---

## §1 期刊配置读取

读 `journal_configs/[期刊].md` 获取完整格式要求。

如果目标期刊不在预设列表中:
- 用 WebSearch 搜索 "[期刊名] submission guidelines format requirements"
- 用 WebFetch 读取期刊官网的投稿指南
- 提取: 字数限制/section结构/引用格式/图表规范

---

## §2 格式校验清单

### 2a. 字数限制

```
□ 正文总词数 ≤ [期刊上限]?
□ Abstract ≤ [期刊上限]词?
□ 每个图表标题 ≤ [期刊上限]词?
□ SM补充材料有单独字数限制吗?
```

### 2b. Section结构

```
□ Section命名符合期刊要求? (如PRL不需要"Introduction"标题)
□ Section顺序符合期刊要求?
□ 是否包含该期刊要求的所有section? (如Data Availability/Author Contributions)
```

### 2c. 图表规范

```
□ 图分辨率 ≥ [期刊要求]dpi?
□ 图字体大小 ≥ [期刊要求]pt?
□ 配色适合黑白打印? (如期刊要求)
□ 图表标题格式: Figure X. / Fig. X. / FIG. X.?
□ ⛔ 所有图由Python生成? (matplotlib/seaborn/plotly等 — 非LLM生成)
□ 图和正文数值对得上?
□ 误差棒表示方式符合期刊要求?
```

### 2d. 引用格式

```
□ 引用格式: [1] / 作者-年份 / 上标数字?
□ .bib文件格式正确?
□ 引用顺序: 按出现顺序 / 按字母?
```

### 2e. SM补充材料

```
□ SM section结构清晰?
□ SM中的公式/图表编号与正文不冲突?
□ SM有独立的参考文献列表? (部分期刊要求)
```

---

## §3 图表生成规范

### 3a. ⛔ 强制规则

```
所有图必须用Python生成。严禁LLM生成图像/手绘示意图。
允许: matplotlib, seaborn, plotly, mayavi, pyvista
禁止: 任何AI绘图工具(DALL-E/Midjourney等), LLM直接输出图像, 手绘扫描
```

### 3b. Python科学绘图最佳实践

```
1. 数据驱动: 所有数据点来自实际计算/实验,不凭空捏造
2. 可复现: 每张图对应一个独立.py脚本,脚本命名对应Figure编号
3. 分辨率: plt.savefig('figure1.pdf', dpi=300, bbox_inches='tight')
4. 字体: plt.rcParams['font.size'] = 10 (PRL要求≥8pt)
5. 配色: 使用色盲友好配色 (seaborn.color_palette('colorblind'))
   或灰度兼容: plt.style.use('grayscale')
6. 误差棒: plt.errorbar(x, y, yerr=sigma, capsize=3, fmt='o')
7. 数学符号: r'$\alpha$' 格式,与正文符号一致
8. 图例: 置于图内不遮挡数据,字体与坐标轴一致
```

### 3c. 常见图类型及模板

```
概念示意图:
  import matplotlib.patches as mpatches
  使用箭头/矩形/圆形组合,不用手绘

数据对比图(本文vs前人):
  fig, ax = plt.subplots(figsize=(8,5))
  ax.plot(x, y_ours, 'o-', label='This work', color='C0')
  ax.plot(x, y_prior, 's--', label='Prior work', color='gray', alpha=0.7)
  ax.legend(frameon=False)

相图/参数扫描:
  fig, ax = plt.subplots(figsize=(6,5))
  im = ax.pcolormesh(X, Y, Z, cmap='RdYlBu', shading='auto')
  plt.colorbar(im, label=r'Order parameter $\phi$')
```

### 3d. 审稿人看图测试

```
只用图表和标题 → 审稿人能理解论文创新点?
  能 → 通过
  不能 → 补图(Python生成):
    - 概念示意图(解释核心机制)
    - 对比图(本文vs前人)
    - 相图/流程图(系统行为全景)
```

---

## §4 Cover Letter

### 4a. 结构 (来自nature-skills triage公式)

```
第一段: Finding — 一句话核心发现
  "[具体发现], which demonstrates [物理意义]"

第二段: Novelty — 与已有工作的本质区别
  "Unlike prior work that [前人做了什么], we [我们做了不同的事],
   revealing [新认知]"

第三段: Cross-disciplinary Significance — 跨领域影响
  "This result has implications beyond [本领域]:
   [领域A] because [原因A]; [领域B] because [原因B]"

第四段: 声明 (标准格式)
  - 原创性声明
  - 所有作者同意投稿
  - 未在其他期刊审稿中
```

### 4b. ⛔ Cover Letter禁词和禁止句式

```
禁止:
  - "We hope this work will..." (AI标准收尾)
  - "We are confident that..." (AI自我评价)
  - "This paper presents X, Y, and Z" (穷举——只点最核心1个,其余用"among other results")
  - Contribution list各条完全等长平行对称
```

### 4c. Cover Letter AI检测处理 (Phase 4会详细处理)

P4_randomize.md 包含Cover Letter的3维轻量参数处理(W_sentence/V_sentence/Break逐句控制)。
此处只需确保: ①contribution list各条长度不等 ②无禁止句式 ③最后一句不是安全收尾句。

---

## §5 格式自检

完成格式化后, PI逐项检查 §2 的每个checkbox。
全部通过后 → 进入Phase 4。

# P5: Final Audit — 完整性验证与投稿输出

> 角色: 最后一道闸门。投稿前全面审计。
> 输入: Phase 4 AI检测处理后的终稿
> 输出: 投稿就绪的完整文件包

---

## §1 文献核验

```
[ ] 逐篇fetch验证引用真实性:
    [ ] 所有引用都成功fetch? → 记录通过
    [ ] 有无法fetch的? → 列出清单,告知用户手工核验
    [ ] 有引用内容与原文不符? → 阻断,回Phase 2修复
[ ] 近期文献占比≥30%? (2024-2026)
[ ] 自引适度? (无过度自引)
```

## §2 数据核验

```
[ ] 所有图由Python生成? (matplotlib/seaborn等 — 非LLM)
[ ] 图中数值与正文一致?
[ ] 误差棒来源明确且合理?
[ ] 数据可复现? (代码可运行 + README说明数据与代码对应关系)
[ ] ⛔ 数据非随机生成/经验复用?
```

## §3 LaTeX编译 — ⛔ 三份全部编译

```
[ ] 编译 main.tex → paper_output/final_paper/paper.pdf
[ ] 编译 supplemental_material.tex → paper_output/final_paper/supplemental_material.pdf
[ ] 编译 cover_letter.tex → paper_output/final_paper/cover_letter.pdf
[ ] 三份均编译无错误? → 通过
[ ] 任一份编译有Warning? → 检查是否影响排版
[ ] 任一份编译失败? → ⛔ 阻断,修复后重试
[ ] 图表正确嵌入PDF?
[ ] 引用和交叉引用正确解析? (正文+SM各自独立编译)
```

⛔ 三个PDF缺一不可。投稿时大多数期刊要求SM和CoverLetter也是PDF格式。

## §4 最终格式核验

```
[ ] 逐项对照 journal_configs/[期刊].md 的所有要求
[ ] 字数在限制内?
[ ] Abstract格式正确?
[ ] 引用格式正确?
[ ] 图表分辨率达标?
[ ] SM补充材料完整?
```

## §5 最终禁词扫描

```
[ ] grep全文(正文+致谢+CoverLetter+SM):
    "原则上可能"|"in principle"|"待未来实验"|"awaits future"
    命中 → ⛔ 阻断,回Phase 4修改被标记段落
[ ] ⛔ AI致谢扫描 (正文+致谢+CoverLetter):
    "Claude"|"AI辅助"|"LLM"|"ChatGPT"|"Anthropic"|"人工智能"|
    "AI-assisted"|"language model"|"generative AI"
    命中 → ⛔ 阻断,必须删除。AI是写作工具不是作者。
[ ] grep Cover Letter: "We hope"|"We are confident"
    命中 → ⛔ 修改Cover Letter
```

## §6 完整性检查

```
⛔ 以下文件必须全部存在,缺一不可:

[ ] paper_output/final_paper/main.tex (论文正文)
[ ] paper_output/final_paper/references.bib (引用文献)
[ ] paper_output/final_paper/figures/ (所有图文件)
[ ] paper_output/final_paper/paper.pdf (编译成功的PDF)
[ ] paper_output/cover_letter.tex (Cover Letter)
[ ] paper_output/supplemental_material.tex (如有SM)
[ ] paper_output/citation_support_bank.md (引用支持库)
[ ] paper_output/writing_rationale_matrix.md (写作思路)
[ ] paper_output/blueprint.md (AI检测蓝图)
[ ] paper_output/confirmed_motivation.md (确认motivation)
[ ] paper_output/review_R1.md ~ review_R5.md (5轮审稿报告)
[ ] paper_output/fix_R1.md ~ fix_R5.md (5轮修改记录)
[ ] paper_output/final_artifact_manifest.md (本清单)
```

## §7 输出

```
[ ] 写 paper_output/final_artifact_manifest.md
    列出所有产物及其路径
[ ] 告知用户:
    - 投稿包路径: paper_output/final_paper/
    - Cover Letter: paper_output/cover_letter.tex
    - SM: paper_output/supplemental_material.tex (如有)
    - 建议的投稿期刊 (根据R5裁决+降级历史)
    - 需要手工核验的事项 (无法fetch的引用等)
```

## §8 投稿后

```
投稿完成后:
[ ] 更新 shared/知识库汇总.md (追加本课题发表信息)
[ ] 更新项目/北极星队列.md (标记课题状态为"已投稿")
[ ] 归档完整paper_output/到安全位置
```

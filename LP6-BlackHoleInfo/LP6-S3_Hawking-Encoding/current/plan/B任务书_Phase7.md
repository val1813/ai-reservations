# B 博士任务书 — Phase 7

**课题：** Hawking-Encoding v1
**Phase：** 7（论文骨架 — 恶意审稿人反驳清单）
**日期：** 2026-06-01
**价值分类：** [防守/核心] — 确保论文骨架能承受审稿人攻击

---

## 攻击目标

任务分两部分：

### 第一部分：审稿人反驳清单

以恶意审稿人的身份，逐条攻击 A 博士论文骨架中的每一处声张。对每条攻击，判断：
- **致命（fatal）**：论文在当前形式下无法防御 → 必须修改声张
- **严重（major）**：可以防御但需要额外推导/引用 → 标注防御路径
- **轻微（minor）**：措辞/表述问题 → 标注修改建议

### 第二部分：论文 caveat 完整列表

列出论文中每一处需要审稿人接受的假设、每一处定理不覆盖的空白、每一处 "可能被未来工作推翻" 的依赖。

---

## 必须攻击的十大方向

### 攻击 1：code subspace triviality
- "Proposition 1 只在 code subspace 成立。code subspace 是人为定义的。如果选不同的 code subspace，结论是否翻转？"
- "在 Hilbert space 的其他 sector 中 M.B 可能有 O(1) gap——论文不能声称全局结论。"
- 裁决：致命/严重/轻微？

### 攻击 2：EW reconstruction circularity
- "Proposition 1 的 Step 3 假设 EW reconstruction 成立 → 推出无 O(1) gap。但 EW reconstruction 的物理基础正是需要被 'mechanism' 解释的东西——这是循环论证。"
- "如果 EW reconstruction 就是 mechanism，那么说 'mechanism 不存在' 是 self-contradictory。"
- 裁决：致命/严重/轻微？

### 攻击 3：f(ε) 空洞
- "Proposition 1 的 f(ε(N)) 没有具体形式。'f(ε)→0' 不是 theorem——是 qualitative statement。"
- "如果 f(ε) ~ 1/log(1/ε)，即使 ε=10^{-100}，f 仍可能是 O(1)。论文没有给出 bound。"
- 裁决：致命/严重/轻微？

### 攻击 4：窄代数的人为性
- "A_bdy^narrow（不含 bath decoder）的人为定义是什么物理意义？自然界中 observer 总是能访问辐射。"
- "在窄代数中找到 O(1) gap 等价于说 '如果你故意不用可用的 decoder，你会找不到信息'——这是 trivial。"
- 裁决：致命/严重/轻微？

### 攻击 5：Type III₁ 未充分处理
- "canonical Type III₁ 中 P₀ 不存在（K2.1），论文是否依赖 Type II∞ crossed product 的 ensemble 选择？"
- "论文说 'approximate sufficiency 控制 gap'，但在 Type III₁ 中 approximate recovery 的数学基础不明确。"
- 裁决：致命/严重/轻微？

### 攻击 6：复制虫洞的角色被低估
- "Penington-Shenker-Stanford-Yang 1911.11977 的复制虫洞计算显示 island 的出现等价于 replica wormhole 主导 saddle。这本身就是一个 Lorentzian mechanism：island = replica wormhole = 信息通过拓扑相变从内部转移到外部。"
- "论文把岛屿降级为 'bookkeeping' 未经充分论证。"
- 裁决：致命/严重/轻微？

### 攻击 7：Hayden-Preskill / Python's lunch 未充分处理
- "即使 entropy-level bookkeeping 不给出 mechanism，Hayden-Preskill scrambling + Python's lunch complexity 协议确实给出了一个可操作的 decoding 程序。"
- "论文未区分 'algebraic (in-principle) recovery' 和 'computational (efficient) recovery'——但两者都是 mechanism。"
- 裁决：致命/严重/轻微？

### 攻击 8：高维推广被过度限制
- "论文声称 '只在 SYK/JT 中成立'——如果高维 holographic CFT（如 N=4 SYM）中复制虫洞有完全相同的数学结构，为什么定理不推广？"
- "这不是 scope limitation，而是逃避最难的问题。"
- 裁决：致命/严重/轻微？

### 攻击 9：doubly non-perturbative 窗口
- "论文承认 doubly non-perturbative 窗口（~e^{-1/G_N}）未被覆盖。如果这个窗口正是 mechanism 存在的地方，论文的 'no mechanism' 结论只是 pertubative artifact。"
- 裁决：致命/严重/轻微？

### 攻击 10：Geng/Raju/ACMP 被过度依赖
- "论文大量依赖 ACMP 2025 (Geng-Karch-Randall-Tajdini arXiv:2506.04311) 的论证。ACMP 自身是 preprint，尚未经过同行评审。在 eternal AEMM setup 中 ACMP 的适用性已被 K1.1/K1.2 限定。"
- "如果 ACMP 在审稿过程中被推翻或大幅修改，论文的论证链是否断裂？"
- 裁决：致命/严重/轻微？

---

## 必须输出的 caveat 清单

整理论文中每一处 "审稿人必须接受的假设" 和 "定理不覆盖的空白"：

1. **假设依赖：** code subspace 定义、algebra 定义、ensemble 选择、EW reconstruction 有效性、recovery error 的存在性
2. **空白区：** 高维 holographic CFT、渐近平坦黑洞、de Sitter、doubly non-perturbative 窗口、canonical ensemble 的 GKRR 修复
3. **外部依赖：** ACMP 2025 的同行评审状态、CPW 2022 Type II∞ crossed product 框架的接受度
4. **计算空白：** exact [A_full:A_bdy] index 未计算、f(ε) 的具体 bound 未给出

---

## 禁止

- 不要提新的正面构造——你的角色是攻击者
- 不要重复 Phase 5 commutant 候选清单
- 不要把 "攻击" 升级为 "推翻"——判断 severity 即可
- 不要忽略 A 线论文骨架的具体措辞——攻击必须针对具体声张

---

## 产出格式

```
⚡ 审核入口：
  A 论文骨架可否投稿：[可以 / 需大修 / 需重写]
  最致命攻击：[攻击编号 + 一句话]
  必须修正的声张：[列表]
  建议的投稿期刊：[PRD / JHEP / ...]
  GATE 2 前置条件：[列出缺失项]

正文：逐条攻击（致命/严重/轻微 + 防御路径）+ caveat 完整列表 + 最终建议。
```

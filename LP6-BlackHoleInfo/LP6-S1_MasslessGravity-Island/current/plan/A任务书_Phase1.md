# A 博士任务书 — Phase 1 (MasslessGravity-Island v1)

**课题：** MasslessGravity-Island v1
**Phase：** 1（文献检索 + 命题精化 + 第一步推导）
**日期：** 2026-06-01
**价值分类：** [核心] — 苏格拉底已精化北极星为 C1/C2/C3 三条件，需文献验证+第一步推导

---

## 任务

### 第一步：文献检索（必须用 paper-search-mcp）

搜索以下内容验证文献库中的引用，补全确切的 arXiv 编号和发表信息：

1. Antonini-Sasieta-Swingle 关于 flat space / cosmological island 的确切论文
2. Geng-Karch-Randall-Tajdini-Raju (arXiv:2506.04311) 的核心声张确认
3. 3D flat gravity + island 或 Page curve 的相关文献
4. BMS supertranslation 与 entanglement entropy 的交叉文献
5. Celestial holography 中 island formula 的任何讨论

### 第二步：推导 C1（BMS-invariant QES）

**命题 C1：** 渐近平坦时空中的 QES 条件是否在 BMS supertranslations 下不变？

具体推导路径：
1. 回忆 AdS 中 QES 的定义：S_gen = Area(∂Σ)/(4G) + S_bulk(Σ)，对 Σ 的边界 ∂Σ 变分
2. 在 flat space 中，Area term → 需在 Bondi gauge 下写 ∂Σ 的面积
3. 关键问题：supertranslation 使 Bondi 时间 u → u + f(θ,φ)，这如何影响 ∂Σ 的定位？
4. 如果 ∂Σ 的位置依赖 supertranslation frame → QES 不是 BMS-invariant → island 位置是规范 artifact

### 第三步：判断三个子命题的可解性

苏格拉底分解为 S1a（BMS-invariant QES）、S1b（flat space replica wormhole）、S1c（3D flat gravity 验证）。判断哪个最可解且产出最高，给出优先攻打顺序。

---

## 禁止
- 不要声称已在 flat space 中找到 island
- 不要忽略 LP6-S3 已发现的 GKRR/ACMP 局限
- 文献检索必须用 paper-search-mcp，不可只凭记忆

## 产出格式

```
⚡ 审核入口：
  文献检索结果：[找到/未找到 各关键文献]
  C1 初步结论：[BMS-invariant? 是/否/不确定]
  最可解子命题：[S1a/S1b/S1c]
  PI需要关注的问题

正文：文献检索结果 + C1 推导 + 子命题优先顺序
```

# B 博士任务书 — Phase 3 (MasslessGravity-Island v1)

**课题：** MasslessGravity-Island v1
**Phase：** 3（命题B 精化——Geng et al. + C1-C2 互斥的统一框架）
**日期：** 2026-06-01
**价值分类：** [核心] — 命题B 的正面表述

---

## 攻击目标

将命题B（"无质量引力中岛屿不成立"）精化为一个正面表述的理论框架，合并两个独立的攻击线：
1. Geng et al. (2602.06543): 规范不变算符不能局域化到岛屿区域
2. 本课题 Phase 2: C1-C2 互斥——dressing 使 Q_f 中心化 vs replica trick 需要 Q_f 非平凡谱

---

## 两条攻击线如何统一

### 统一论题

Geng et al. 从 QFT 代数层面论证：规范不变算符的局域化在无质量引力中面临微分同胚障碍。本课题从 replica/QES 层面论证：BMS-invariance 的恢复与 replica structure 互斥。

两者攻击的是同一个目标——"flat space 中能否定义 operational 的岛屿概念"——但来自不同层级：
- Geng et al. 攻击的是 **单个算符级别的局域化**（能否写入 O_island 且 [O_island, diffeo] = 0）
- 本课题攻击的是 **路径积分/鞍点级别的 well-definedness**（Z_n 是否在 supertranslation 下 unambiguous）

### 统一命题

> 无质量引力中岛屿公式面临双重障碍：单算符级别（Geng et al. 的规范障碍）和路径积分级别（本课题的 C1-C2 互斥）。两者独立存在且相互强化——任一障碍单独成立就足以排除 operational 岛屿概念。

---

## 推导任务

### 第1步：精确重述 Geng et al. 2602.06543 的核心论证

用 paper-search-mcp 或 WebFetch 读取 2602.06543，提取 3-5 条核心论证（不要引整篇）。

### 第2步：展示 Geng 论证与 C1-C2 互斥的互补性

- Geng 论证覆盖了什么？→ 单算符的规范不变局域化
- C1-C2 互斥覆盖了什么？→ 路径积分的 supertranslation 依赖
- 两者是否有重叠？是否有任一缺口？

### 第3步：写出统一命题

Proposition B (unified): 渐近平坦时空中，不存在同时满足以下三者的 operational 岛屿定义：
(B1) 规范不变性：岛屿内局域算符是 diffeomorphism-invariant
(B2) QES 良定义：存在 BMS-invariant QES 条件
(B3) Page 曲线：replica trick 给出 well-defined entropy

其中 B1 被 Geng et al. 攻击，B2+B3 被 C1-C2 互斥攻击。

---

## 产出格式
```
⚡ 审核入口：
  统一命题：[一句话]
  Geng vs 本课题的互补性：[一句话]
  命题B 的最强形式：[定理陈述]
  PI 需要裁决的问题
```

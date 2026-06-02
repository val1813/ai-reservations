# B 博士任务书 — Phase 1 (MasslessGravity-Island v1)

**课题：** MasslessGravity-Island v1
**Phase：** 1（跨域攻击 + 文献独立检索）
**日期：** 2026-06-01
**价值分类：** [防守/核心] — 从跨域角度攻击 Antonini et al. 的推广声张

---

## 任务

### 攻击 1：Supertranslation 对局域化的原理性障碍

从 QFT 代数的角度：在渐近平坦时空中，局域代数（algebra of local observables）的定义依赖 background structure。BMS supertranslation 会改变 null infinity 上的 "time" slicing → 改变哪些 bulk 点是 "同时的"。

**攻击目标：** 即使 Antonini et al. 找到了一个看起来 BMS-invariant 的 QES 定义，它可能只是用"隐藏的 supertranslation frame"（如 Bondi frame 的特定选择）伪装成 invariant 的。参考 Geng-Raju 对 AdS/CFT 中 "bulk locality = gauge artifact" 的论证（LP6-S3 K1.1/K1.2）。

### 攻击 2：IR 灾难

Flat space 中 massless graviton 的 IR 发散使 S-matrix 需要 IR 截断。Replica trick（折起时空 manifold）在 flat space 中是否 well-defined？

**攻击目标：** replica manifold 的边界条件在 I⁺ 上需要指定 fall-off。不同的 supertranslation frame 给出不同的 fall-off → replica partition function 依赖于 frame → Page 曲线不唯一。

**跨域工具：** QED 中软光子散射的 IR 结构（Kulish-Faddeev, Chung dressing）→ 引力中的 soft graviton dressing 会使 bare 态变成 dressed 态 → dressing 改变了态的 entanglement structure。

### 攻击 3：3D flat gravity 的 Toy Model 限制

如果 3D flat gravity（BMS₃/Carrollian CFT）是唯一可计算的 toy model，问：3D 中的结果在多大程度上向 4D 推广？

**攻击目标：** 3D gravity 没有 propagating 引力子（只有边界模式）→ 3D 中 island 的存在性不能证明 4D 中也存在（4D 有 propagating 引力子，规范障碍更强）。

**跨域工具：** 3D → 4D 中 gravitational degree-of-freedom counting 的差异。

### 攻击 4：LP6-S3 继承——规范不变算符局域化的代数障碍

从 LP6-S3 Hawking-Encoding 的 K2.1 (Type III₁ 不含 P₀) 和 K2.5 (ACMP dilaton localizer) 出发：flat space 中，asymptotic symmetry（BMS）的角色类似于 AdS 中的 boundary isometry。BMS 的无限维性质是否使 Type III₁ 问题更严重（超 Type III₁）？

---

## 禁止
- 不要只做文献评论——每条攻击需要具体的数学障碍
- 不要重复 LP6-S3 的 QEC 分析（那是信息侧，不是引力侧）
- 不要声称"已推翻 Antonini"——找最锐利的攻击点即可

## 产出格式

```
⚡ 审核入口：
  最锐利的攻击：[攻击编号 + 一句话]
  3D/4D 推广性判断：[有/无 原理性障碍]
  建议的攻打顺序：[S1a/S1b/S1c 的优先排序]
  需要 PI 裁决的问题

正文：四条攻击的详细推导 + 跨域工具连接
```

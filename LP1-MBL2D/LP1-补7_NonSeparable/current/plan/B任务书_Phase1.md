# B 博士任务书 — LP1-补7 Phase 1

**课题：** LP1-补7 非可分离势
**Phase：** 1（攻击 A 博士的 WPL 分析 — 找最坏情形非可分离势）
**价值分类：** [防守/核心]

---

## 攻击目标

从攻击者角度，找能让"数论保护"在非可分离势中失效的最坏情形。

---

## 三条攻击链

### 攻击 1：构造真正无限长的 WPL
- 选择 β_x/β_y = 有理数（如 β_x=1, β_y=2）→ V 在格点上周期重复 → WPL 为无限长的精确零线
- 反驳 A："实际实验中 β 是无理数"
- 但：如果 β 的 Diophantine 类型足够差（如 Liouville 数）→ WPL 虽非严格无限，但宽度 >> ξ_perc
- 问：实验中的 β 的 Diophantine 类型是什么？能否保证足够良好？

### 攻击 2：2D 与 1D 的本质差异
- 1D 准周期势中，"接近0"的条件是 ‖kβ - π/2‖ mod π < ε → 单个 Diophantine 条件
- 2D 非可分离势中，条件是 ‖β_x·x + β_y·y - 1/2‖ mod 1 < ε → 二维联立问题
- 2D 中是否有类似于 "simultaneous Diophantine approximation" 的定理保证 WPL 宽度有限？
- 如果 β_x, β_y 联立时可能比各自单独的逼近更差 → WPL 可能更宽

### 攻击 3：Štrkalj et al. (2022) 的精确结论
- 用 paper-search-mcp 搜索 Štrkalj et al. 2022 关于 Weak Potential Lines 的确切结论
- 他们是否给出了 WPL 长度的显式 bound？还是仅指出存在？
- 如果 Štrkalj et al. 已经给出了 bound：检查该 bound 在 LP-1 参数域（V₀, W, L）下是否 < ξ_perc

---

文件：D:\Claude\ai-reservations\LP1-MBL2D\LP1-补7_NonSeparable\current\B\Phase1_B_output.md

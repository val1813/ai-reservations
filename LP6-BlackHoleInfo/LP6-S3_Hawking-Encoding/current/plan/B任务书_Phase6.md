# B 博士任务书 — Phase 6

**课题：** Hawking-Encoding v1
**Phase：** 6（宽/窄边界代数分离定理 — 反例审计）
**日期：** 2026-06-01
**价值分类：** [防守/核心] — 防止 Phase 6 定理过度声张

---

## 攻击目标

恶意审计 A 线的宽/窄边界代数分离定理，寻找能击穿它的反例。

重点攻击：

1. 宽 `A_bdy^wide` 是否真的包含可执行 decoder；
2. Petz recovery 是否只存在抽象地而非物理可实现；
3. canonical Type III_1 中 approximate recovery 是否能合法控制 relative entropy gap；
4. 是否存在 doubly non-perturbative 窗口打开 O(1) gap；
5. 高维 holographic CFT / ACMP dilaton-localizer 是否逃出 SYK/JT 定理。

---

## 必须给出的审计结论

- A 线定理是否只在 code subspace 成立；
- 是否需要把 "mechanism" 限定为 algebraic/in-principle，而不是 operational polynomial decoder；
- 是否应保留 complexity caveat；
- 是否需要把高维与 collapse setup 排除在定理外；
- 是否可以关闭 CP-009 或只能改写为边界条件。

---

## 禁止

- 不要重复 Phase 5 的 commutant 候选清单，除非找到新候选。
- 不要用 "decoder 不可实现" 推翻 algebraic recovery；这是 operational caveat，不是 algebraic refutation。
- 不要把高维反例拿来反驳 SYK/JT 限定定理，除非指出假设被破坏。

---

## 产出格式

```
⚡ 审核入口：
  A 定理是否通过审计：[通过/需降级/失败]
  最大漏洞：[一句话]
  必须加入的 caveat：[列表]
  CP-009 裁决建议：[关闭/部分关闭/开放]
  CP-010 裁决建议：[关闭/部分关闭/开放]

正文：逐条反例审计 + 最终建议。
```

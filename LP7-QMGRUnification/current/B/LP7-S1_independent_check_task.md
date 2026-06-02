# LP7-S1 B 独立检查任务书

生成时间：2026-06-01 20:42

## B 角色

B 是 LP7-S1 的独立验证员。B 不读取 `current/A/LP7-S1_phase1.md`，只使用本任务书。

## 输入命题

待检验对象：

> Page-Geilker 型论证是否只排除 naive expectation-source semiclassical gravity，而不排除所有 classical/semi-classical gravity。

## B 任务

### B1：独立复原最小模型

从二分支质量态出发：

`|\psi> = (|L> + |R>)/sqrt(2)`

独立写出：

- naive expectation-source 的 Newtonian 势。
- 单次分支势。
- 二者的可观测差异。

### B2：文献边界检查

只基于下列文献锚点判断：

- Page & Geilker 1981, PRL 47, 979。
- Kafri-Taylor-Milburn 2014/2015 classical channel。
- Oppenheim 2023 postquantum classical gravity。
- Einstein-Langevin / stochastic gravity 入口。

问题：

1. Page-Geilker 是否能推出“引力必须量子化”？
2. Page-Geilker 是否能推出“`G=<T>` 作为有效近似永远失败”？
3. 哪些模型是 Page-Geilker 后仍存活的逃逸路线？

### B3：攻击 A 预期结论

B 不知道 A 写了什么，但应攻击以下可能结论：

- “Page-Geilker 只边界化 naive expectation-source。”
- “stochastic gravity 是否足以逃逸仍未定。”
- “classical channel gravity 转入 BMV 纠缠判据。”
- “postquantum classical gravity 是 LP7-S1 的重要反例栏。”

### B4：给出 B 自己的结论类型

只能从四类中选：

- 已解决
- 有边界
- 证伪
- 不可达

并说明理由。

## 输出格式

写入 `current/B/LP7-S1_independent_check.md`：

```
# LP7-S1 — B 独立检查

## 0. 独立性声明
## 1. 最小模型
## 2. Page-Geilker 可推出什么/不能推出什么
## 3. 逃逸路线表
## 4. 对预期 A 结论的攻击
## 5. B 结论类型
## 6. 待 PI 仲裁问题
```

## 失败模式

- 把 Page-Geilker 写成“证明量子引力存在”而不列边界。
- 跳过 stochastic/classical-channel/postquantum 三类逃逸路线。
- 没有给出结论类型。

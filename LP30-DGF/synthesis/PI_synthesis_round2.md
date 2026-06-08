# PI 综合 Round 2

## 当前北极星

DGF-N4：独立干涉坐标 `q∈[0,1]` 控制质量映射 `m(q)=(2m_p/pi)sin(pi q/2)`，边界 `m*=13.85 microgram`；GUP/退相干核若属于 DGF，必须由同一个 q 的涨落驱动。

## A/B 汇合判断

汇合类型：强互补，并且方向一致。

- A 给出标准实验统计路线：`q` 应通过干涉可见度、Wigner/奇偶振荡幅度或相干峰面积读出，而不是由质量反推。`m>m*` 不观测“虚 q”，而是做约束模型 likelihood failure。
- B 给出数学结构路线：`q=1` 是一维质量映射的 fold-type critical endpoint；`m>m*` 表示实 q 模型流形外侧，可能表现为边界钉扎、固定符号残差、单侧似然。

共同进展：

1. Round 1 的“非实 q 是什么”已被正确降级：它不是物理量，而是 constrained model mismatch。
2. 独立 q 的候选 readout 从“质量反演”转移到“相干可见度/相位空间干涉幅度”。
3. 实验路线更清楚：重分析 16 microgram mechanical cat，比较环境/null 与 DGF constrained model。

## INSPECTOR 后的硬修正

Round 3 必须修：

1. 不能用 `clip(V/V_ref,0,1)` 定义 q。应使用潜变量 `q∈[0,1]` 和 likelihood。
2. 必须明确区分 `q_visibility` 与 `q_DGF_mass`；若设为同一物理变量，需要桥接假设。
3. 必须给出具体读出 likelihood，例如二项分布、正态 visibility 似然或连续 quadrature 似然。
4. “fold caustic”降级为 `fold-type critical endpoint`，除非给出观测投影密度/Jacobian 奇性。
5. 必须补最小落地表：`t, V_obs, sigma_V, V_env_best, V_DGF_best, residual, chi2 contribution`。

## 声张保真度

声张没有被完全推翻，但明显收窄：

原声张：`q` 是基础干涉坐标且给出质量上界。  
当前声张：如果 `q_visibility` 与 `q_DGF_mass` 可桥接，则 `m*` 是约束模型边界，可通过 likelihood 失配检验。

声张保真度从 1.0 下调到 0.7。

## 突破方向检查

本轮更接近突破。原因不是理论更漂亮，而是从不可观测“虚 q”变成了可操作统计问题：

```text
H0: environment/null visibility model
H1: DGF constrained model with q∈[0,1] and m(q)
```

若 16 microgram 数据显示环境模型优于 DGF constrained model，DGF-N4 被快速击毙；若出现边界钉扎/固定符号残差且环境模型不能解释，则打开新的质量-相干边界方向。

## AHA 检查

有 AHA，但不切换北极星。

新候选：`DGF-N4e`，把 DGF-N4 改写为约束统计模型，而非本体质量上界。

一句话：

> DGF-N4e: `2m_p/pi` 不是“自然禁止质量超过边界”，而是 `q_visibility=q_DGF_mass` 约束模型的可拒绝边界；核心实验是环境/null 与 DGF constrained likelihood 的模型比较。

该候选是当前北极星的统计化版本，不超过当前×1.3，不切换。

## 下一轮摘要（≤300字）

Round2把非实q问题正确降级为统计模型失配：`m>13.85μg` 不代表观测虚q，而是 DGF 约束模型 `q∈[0,1], m(q)` 对数据不可行。A给出visibility/Wigner幅度readout，B给出fold-type critical endpoint与边界钉扎语言。但INSPECTOR要求Round3硬修：禁止clip定义q；区分`q_visibility`和`q_DGF_mass`并给桥接假设；写出具体likelihood `P(data|q)`；把caustic降级；补最小数据表/χ²或LLR。

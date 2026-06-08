# 矛盾图深化 | LP23-R2

日期：2026-06-03

## 核心矛盾

R2 试图把“桥接结构选择”提升为新物理自由度，但三轮后发现：只要允许模板、nuisance、history、response kernel 或系统辨识空间扩张，所谓 `I_bridge` 就变成相对于某个模板库的模型失配残差。

## 五个为什么

1. 为什么 `I_bridge` 不是物理 invariant？  
因为它依赖 `Pi_standard` 的模板空间定义；模板空间扩张后残差可消失。

2. 为什么模板空间可以扩张？  
因为 screen/observer/medium/splitting/history/kernel 都不是由 R2 内部自然给定，而是外部桥接/读出/建模选择。

3. 为什么外部选择不能直接算新物理？  
因为若没有预注册独立约束，它们只是 nuisance/model class；残差非零只说明当前模型族不完备。

4. 为什么这反复杀死 S1/R1/R2？  
因为三者都把某个截面选择、相位选择、读出选择或模板缺口误认为自然几何对象。

5. 为什么仍能产生 R3？  
因为共同失败指向更深原则：可观测新自由度必须是取商后仍非零的 obstruction class，而不是某个选择下的代表元。

## 基础原则层

LP23 系列的根本矛盾不是“哪一个连接正确”，而是：

> 代表元不是不变量；截面不是自然连接；模板残差不是新自由度。只有在所有允许的 gauge/template/bridge/nuisance/history 作用取商后仍非零的 obstruction class，才可能承载新物理。

这给出项目内新候选 LP23-R3，但也带来强先发风险：该原则可能已被 naturality、moduli space、cohomology obstruction、gauge quotient、statistical nuisance projection 等成熟框架覆盖。

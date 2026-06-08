# LP23-R2 Round3（A路）: Bridge quotient diagnostic 生死检验
日期: 2026-06-03

## §0 框架声明

本轮只检验一件事: `I_bridge = ||(I-Pi_standard) r||^2` 是否仍然承载“北极星价值”，还是已经被既有框架完全覆盖。

这里的 `Pi_standard` 不是任意投影，而是把以下标准空间并入后的联合模型空间:
`model selection + nuisance regression + matched filtering + system identification + local/ nonlocal electrodynamics fitting`.

因此，本轮不是问“残差是否可能非零”，而是问:
1. 这个残差是否只是统计学/系统辨识的正交补;
2. 非局域电动力学是否已经提供了同构的核参数拟合语法;
3. 若仍保留，最小可发表命题是否还能高于一个普通投影诊断。

结论先行: 这条线不再有独立北极星地位，只能降级成诊断工具。

## 1. 既有框架是否已完整覆盖 `I_bridge`

### 1.1 统计模型选择 / nuisance regression / matched filtering

`I_bridge` 的形式本身就是线性模型中的正交残差范数。
若把 `r` 写成
`r = X beta + Z gamma + eps`,
其中 `Z gamma` 是 nuisance/template space，那么在广义最小二乘、似然比检验、AIC/BIC 型模型选择里，消去 nuisance 后得到的就是投影残差。

这与 `I_bridge = ||(I-Pi_standard)r||^2` 完全同型:
`Pi_standard` 就是联合模板空间的投影算子，`I-Pi_standard` 就是标准空间的正交补。

同一结构也出现在:
1. residual-based model checking;
2. chi-square veto / null-stream 类检验;
3. template-bank matched filtering 的 fitting-factor 语言;
4. whitened residual 的统计判别。

所以，只要 `r` 仍被解释为“对给定标准模板族的偏离”，它就已经是统计模型选择问题，不是新物理命题。

### 1.2 system identification / subspace methods

系统辨识里，子空间方法直接做的就是:
从观测输出中剥离已知输入/已知动态子空间，保留不可解释部分作为 innovation/residual。

`I_bridge` 与这个语法完全一致:
`r` 是观测输出,
`Pi_standard` 是已知模型子空间,
`I-Pi_standard` 给出的就是未解释能量。

因此它在方法论上已经被 subspace identification、projection theory、model validation 吸收。
它可以做诊断指标，但不能自称新类结构。

### 1.3 结论

统计模型选择、nuisance regression、matched filtering、system identification 对 `I_bridge` 的覆盖是完整的。
我这里的判断是一个基于文献覆盖面的推断，不是哲学性断言。

## 2. 非局域电动力学参数拟合是否也已覆盖

### 2.1 `chi(omega,k)` / `K(x,x')` 的覆盖边界

Local constitutive electrodynamics 处理的是 `chi^{abcd}(x)` 或其频散版 `chi^{abcd}(omega,k)`。
Nonlocal electrodynamics 处理的是历史核:
`H^{ab}(x)=1/2 ∫ K^{abcd}(x,x') F_cd(x') dV_{x'}`。

这一步并没有留下一个“桥残差”的独立地位。
因为一旦 `K` 被允许作为参数核，它就已经进入了标准 inverse problem / response-function fitting / kernel identification。

Mashhoon 系列工作已经把 accelerated systems 的非局域响应写成 Volterra 型核。
Hehl-Obukhov / spatial dispersion 一线则把局域/频散响应的参数化空间讲得很清楚。

所以，如果 `I_bridge` 只是“某个核参数拟合后还剩的余差”，它不是超出非局域电动力学的活口，而是非局域模型拟合质量的指标。

### 2.2 真正可能未覆盖的只剩装置核

唯一可能逃逸的，不是物理核本身，而是 measurement protocol kernel:
filter, reconstruction, environment, trace-out, path weighting。

但这类对象属于仪器与读出建模，不属于“基础新物理”。
一旦把它写清楚，问题就退回到实验系统辨识。

## 3. 若保留，最小可发表命题是什么

不能再写成:
“模板投影残差非零。”

最小可发表命题只能降到下面这个层级:

**命题**: 在给定 endpoint-calibrated 标准空间
`span(D, L_chi, L_spin, L_M, L_disp)` 之后，某些 path-family observable 仍表现出不可被单一模板族吸收的正交残差，因此 `I_bridge` 可作为标准模型失配的分层诊断量。

这个命题仍然有限，因为它只是在说:
1. 现有模板族不够全;
2. 残差能帮助区分哪一层失配在主导;
3. 它是诊断工具，不是新定律。

要达到可发表，至少还要补两样:
1. 一个明确的 null model;
2. 一个能区分 `D + L_chi + L_spin + L_M + L_disp` 与更高层读出核的 toy benchmark。

## 4. INSPECTOR_CHECK

--- INSPECTOR_CHECK ---
[公式] `I_bridge = ||(I-Pi_standard)r||^2`, 其中 `Pi_standard` 是联合标准空间投影；未白化时单位为 `[r]^2`。若推广到白化形式，应写为 `I_bridge = ||(I-Pi_white) C^{-1/2} r||^2`，其中 `Pi_white` 是白化后标准子空间 `C^{-1/2}S_standard` 上的欧氏正交投影。
[方向] 该量是标准模板失配的正交残差, 方法论上落在 model selection / matched filtering / system identification / inverse kernel fitting.
[数据] 已检索文献: model selection, GW matched filtering, LIGO analysis, subspace identification, nonlocal electrodynamics, spatial dispersion.
[假设] `r` 是对既定模板族的观测残差; `Pi_standard` 已包含 nuisance/template 子空间; 非局域核若被参数化, 其拟合亦属于标准 inverse problem.

## 5. 生死判定

**A路判定: 硬停止北极星叙事, 降级为诊断工具, Round3 只做收尾。**

理由很直接:
1. 在给定标准联合子空间定义下，`I_bridge` 是统计模型选择中的模型失配诊断量;
2. matched filtering / subspace identification 已提供等价语言;
3. nonlocal electrodynamics 也已覆盖核参数拟合;
4. 剩余内容若要保留, 只能变成“标准空间失配诊断器”, 不再是独立发现线。

## 6. 关键文献

- [Dolan 2018](https://doi.org/10.1142/S0218271818430101)
- [Bliokh 2009](https://doi.org/10.1088/1464-4258/11/9/094009)
- [Frolov & Shoom 2011](https://doi.org/10.1103/physrevd.84.044026)
- [Frolov 2024](https://doi.org/10.1103/physrevd.110.064020)
- [Frolov & Shoom 2024](https://doi.org/10.1088/1475-7516/2024/10/039)
- [Oancea et al. 2020](https://doi.org/10.1103/physrevd.102.024075)
- [Shoom 2024](https://doi.org/10.1103/physrevd.110.024029)
- [Hehl & Obukhov 2003](https://doi.org/10.1007/978-1-4612-0051-2)
- [Rubilar, Obukhov & Hehl 2002](https://doi.org/10.1142/S0218271802002190)
- [Muench, Hehl & Mashhoon 2000](https://doi.org/10.1016/S0375-9601(00)00316-9)
- [Mashhoon 2003](https://doi.org/10.1002/andp.20035151002)
- [Mashhoon 2020](https://doi.org/10.3390/universe6120229)
- [LIGO noise and extraction review 2020](https://doi.org/10.1088/1361-6382/ab685e)
- [Detection methods for stochastic GW backgrounds 2017](https://doi.org/10.1007/s41114-017-0004-1)
- [Subspace model identification chapter 2007](https://doi.org/10.1017/cbo9780511618888.011)
- [Projection theory / model-based processing](https://doi.org/10.1002/9781119457695.app2)

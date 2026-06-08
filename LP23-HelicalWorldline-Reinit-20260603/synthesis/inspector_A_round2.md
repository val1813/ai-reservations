# INSPECTOR_A_round2

输入文件：`D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\current\A\round2.md`

协议：按 `INSPECTOR.md` 的 Q1-Q6，仅做量纲、符号/方向、循环论证、量级鸿沟、代数验算、综合判定。

## INSPECTOR_CHECK 1：量子动力学相位 Lorentz 标量

对应公式：\(\theta=p_\mu x^\mu/\hbar\)，\(\theta'=\theta\)，\(\partial_\mu\theta=p_\mu/\hbar\)。

### Q1 量纲校对

- \(p_\mu x^\mu=Et-\mathbf p\cdot\mathbf x\)：左边 SI = J s，右边 SI = J s，匹配 ✅
- \(\theta=p_\mu x^\mu/\hbar\)：左边 SI = 1，右边 SI = (J s)/(J s)=1，匹配 ✅
- \(p'_\mu x'^\mu=p_\rho x^\rho\)：左边 SI = J s，右边 SI = J s，匹配 ✅
- \(\partial_\mu\theta=p_\mu/\hbar\)：若 \(x^\mu=(ct,x,y,z)\) 均为长度坐标，左边 SI = m\(^{-1}\)，右边 SI = (kg m s\(^{-1}\))/(J s)=m\(^{-1}\)，匹配 ✅
- 超越函数：本检查块内无 exp/sin/log/sinh 需要校对。

### Q2 符号/方向校对

- Lorentz 标量方向结论：\(\theta'(x',p')=\theta(x,p)\)。代入 \(\Lambda=I\) 得恒等；代入任意 boost 时协向量按逆变换，\((\Lambda^{-1})^\nu{}_\mu\Lambda^\mu{}_\rho=\delta^\nu{}_\rho\)，结论保持 ✅
- “方向信息属于 \(p_\mu\) 或 \(d\theta\)，不属于相位值本身”：同一 \(\theta\in S^1\) 可对应不同 \(p_\mu\) 与 \(x^\mu\) 组合；方向不能由单个标量值恢复，方向判断正确 ✅

### Q3 循环论证校对

- 检验数据来源：Lorentz 张量变换律与平面波相位定义。
- 输入假设：平坦时空、全局惯性系、协向量与向量按对偶表示变换。
- 是否循环：未用待证的“方向由相位值给出”作为输入；不是循环论证 ✅

### Q4 量级鸿沟

- 无 \(10^N\) vs \(10^M\) 量级比较。✅

### Q5 代数验算

- 展开：\(p'_\mu x'^\mu=p_\nu(\Lambda^{-1})^\nu{}_\mu\Lambda^\mu{}_\rho x^\rho=p_\nu\delta^\nu{}_\rho x^\rho=p_\rho x^\rho\)。系数与指标收缩正确 ✅
- 极限退化 1：\(\Lambda=I\) 时 \(\theta'=\theta\)。✅
- 极限退化 2：\(p_\mu=0\) 时 \(\theta=0\)，\(\partial_\mu\theta=0\)，公式退化一致。✅
- 数值量级：无具体数值估算。
- 引用数值来源：无具体数值。

结论：本检查块通过，无阻断。

## INSPECTOR_CHECK 2：null 方向角 aberration

对应公式：\(\cos\alpha'=(\cos\alpha-\beta)/(1-\beta\cos\alpha)\)，\(\sin\alpha'=\sin\alpha/[\gamma(1-\beta\cos\alpha)]\)。

### Q1 量纲校对

- \(k^\mu=\kappa(1,\cos\alpha,\sin\alpha)\)：各分量 SI = \(\kappa\) 的单位；\(\cos\alpha,\sin\alpha\) 无量纲，匹配 ✅
- \(k'^0=\gamma(k^0-\beta k^x)\)：左边 SI = \(\kappa\)，右边 SI = \(\kappa\)，匹配 ✅
- \(\cos\alpha'=k'^x/k'^0\)：左边 SI = 1，右边 SI = \(\kappa/\kappa=1\)，匹配 ✅
- \(\sin\alpha'=k'^y/k'^0\)：左边 SI = 1，右边 SI = \(\kappa/\kappa=1\)，匹配 ✅
- \(\tan\alpha'=\sin\alpha/[\gamma(\cos\alpha-\beta)]\)：左边 SI = 1，右边 SI = 1，匹配 ✅
- 超越函数：\(\sin,\cos,\tan\) 的自变量 \(\alpha,\alpha'\) 均为角变量/无量纲，匹配 ✅

### Q2 符号/方向校对

- 极限 \(\beta\to0\)：\(\cos\alpha'\to\cos\alpha\)，\(\sin\alpha'\to\sin\alpha\)，方向不变 ✅
- 极限 \(\alpha=0\)：\(\cos\alpha'=1\)，\(\sin\alpha'=0\)，沿 boost 轴共线方向保持共线 ✅
- 极限 \(\alpha=\pi\)：\(\cos\alpha'=-1\)，\(\sin\alpha'=0\)，反向共线方向保持共线 ✅
- 非共线例：\(\alpha=\pi/2,\beta>0\) 时 \(\cos\alpha'=-\beta\)，\(\sin\alpha'=1/\gamma\)，所以 \(\alpha'\ne\alpha\)。因此 \(\alpha=f(\theta)\Rightarrow\alpha'=\alpha\) 与 aberration 冲突的方向结论正确 ✅
- 比值高危项：分母 \(1-\beta\cos\alpha\) 与被动 boost 约定一致；输入块已显式声明该约定。✅

### Q3 循环论证校对

- 检验数据来源：直接 Lorentz 变换 \(k^\mu\to k'^\mu\)。
- 输入假设：future null 向量、被动坐标 boost、\(\alpha\) 为 observer 方向角。
- 是否循环：未把 aberration 结论作为输入；由分量比值得到，不循环 ✅

### Q4 量级鸿沟

- 无 \(10^N\) vs \(10^M\) 量级比较。✅

### Q5 代数验算

- 展开：\(k'^x/k'^0=\gamma(k^x-\beta k^0)/[\gamma(k^0-\beta k^x)]\)。代入 \(k^x=k^0\cos\alpha\)，得 \((\cos\alpha-\beta)/(1-\beta\cos\alpha)\)。✅
- 展开：\(k'^y/k'^0=k^0\sin\alpha/[\gamma k^0(1-\beta\cos\alpha)]\)，得 \(\sin\alpha/[\gamma(1-\beta\cos\alpha)]\)。✅
- 极限退化 1：\(\beta=0\) 退化为恒等方向变换。✅
- 极限退化 2：\(\alpha=0,\pi\) 退化为共线方向不变。✅
- 数值量级：无具体数值估算。
- 引用数值来源：无具体数值。

结论：本检查块通过，无阻断。

## INSPECTOR_CHECK 3：tetrad 与 spinor 表述

对应公式：\(k^\mu=\omega(u^\mu/c+n^ie_i{}^\mu)\)，\(\alpha=\operatorname{atan2}(n^2,n^1)\)，\(k_{A\dot A}=\lambda_A\bar\lambda_{\dot A}\)，\(\zeta'=(S_1{}^0+S_1{}^1\zeta)/(S_0{}^0+S_0{}^1\zeta)\)。

### Q1 量纲校对

- \(u^\mu/c\)：SI = 1；\(e_i{}^\mu\) 作为正交空间标架取无量纲；\(n^i\) 无量纲。因此括号内无量纲 ✅
- \(k^\mu=\omega(u^\mu/c+n^ie_i{}^\mu)\)：左边 SI = \(k^\mu\) 的单位；右边 SI = \(\omega\) 的单位。若 \(\omega=-k\cdot u/c\)，则 \(\omega\) 与 \(k^\mu\) 同为波数/动量尺度，匹配 ✅
- \(n^in_i=1\)：左边 SI = 1，右边 SI = 1，匹配 ✅
- \(\alpha=\operatorname{atan2}(n^2,n^1)\)：atan2 两参数均无量纲，输出角无量纲，匹配 ✅
- \(k_{A\dot A}=k_\mu\sigma^\mu_{A\dot A}\)：\(\sigma^\mu\) 无量纲，左/右 SI = \(k\) 的单位，匹配 ✅
- \(k_{A\dot A}=\lambda_A\bar\lambda_{\dot A}\)：\(\lambda\) 携带 \(k^{1/2}\) 单位，乘积 SI = \(k\) 的单位，匹配 ✅
- \(\zeta=\lambda_1/\lambda_0\) 与 Möbius 变换：\(\zeta,\zeta'\) 无量纲，匹配 ✅
- 超越函数：本检查块无 exp/sin/log/sinh。

### Q2 符号/方向校对

- tetrad 方向：在 observer rest tetrad 中 \(u^\mu/c=(1,0,0,0)\)，\(e_i{}^\mu\) 为空间基，\(k^\mu\propto(1,\mathbf n)\)。当 \(\mathbf n\) 改变时 \(\alpha=\operatorname{atan2}(n^2,n^1)\) 改变；方向结论正确 ✅
- null 性极限：\((-+++)\) 下 \(k^2=\omega^2[-1+n^in_i]=0\)，要求 \(n^in_i=1\)，方向一致 ✅
- spinor 整体相位：\((e^{i\chi}\lambda_A)(e^{-i\chi}\bar\lambda_{\dot A})=\lambda_A\bar\lambda_{\dot A}\)，所以整体 \(U(1)\) 相位不改变 null vector，方向结论正确 ✅

### Q3 循环论证校对

- 检验数据来源：tetrad 分解和 rank-one spinor 分解。
- 输入假设：future null vector、非零 spinor、局部 patch \(\lambda_0\ne0\)。
- 是否循环：未用“相位等于方向角”作为输入；相反检查了整体相位不改变方向，不循环 ✅

### Q4 量级鸿沟

- 无 \(10^N\) vs \(10^M\) 量级比较。✅

### Q5 代数验算

- 展开 \(k^2\)：\(\omega^2[(u/c)^2+2n^i(u/c)\cdot e_i+n^in^j e_i\cdot e_j]=\omega^2[-1+0+n^in_i]=0\)。系数和符号在 \((-+++)\) 约定下正确 ✅
- 展开 Möbius：\(\lambda'_1/\lambda'_0=(S_1{}^0\lambda_0+S_1{}^1\lambda_1)/(S_0{}^0\lambda_0+S_0{}^1\lambda_1)=(S_1{}^0+S_1{}^1\zeta)/(S_0{}^0+S_0{}^1\zeta)\)。✅
- 极限退化 1：\(S=I\) 时 \(\zeta'=\zeta\)。✅
- 极限退化 2：\(\lambda\mapsto e^{i\chi}\lambda\) 时 \(k_{A\dot A}\) 不变。✅
- 数值量级：无具体数值估算。
- 引用数值来源：无具体数值。

### 警告

- ⚠️ 记号警告：文中称 \(\omega=-k\cdot u/c\) 为“频率尺度”。按该定义其 SI 与 \(k^\mu\) 相同，更准确是波数尺度或频率除以 \(c\)。若后续把 \(\omega\) 当作角频率 s\(^{-1}\)，则 \(k^\mu=\omega(u^\mu/c+n^ie_i{}^\mu)\) 会缺少一个 \(1/c\) 因子。

结论：本检查块无阻断；有 1 条可继续的记号警告。

## INSPECTOR_CHECK 4：自然映射 \(\alpha=f(\theta,p^\mu,e_a{}^\mu)\)

对应公式：\(\alpha=f(\theta)\Rightarrow\alpha'=\alpha\) 与 aberration 冲突；\(\alpha=\operatorname{atan2}(p\cdot e_2,p\cdot e_1)\)。

### Q1 量纲校对

- \(\alpha=f(\theta)\)：\(\theta\) 无量纲，\(\alpha\) 为角变量/无量纲，形式量纲匹配 ✅
- \(k^\mu\propto u^\mu/c+\hat{\mathbf p}^{\,i}e_i{}^\mu\)：右边括号无量纲，比例因子提供 \(k^\mu\) 单位，匹配 ✅
- \(\alpha=\operatorname{atan2}(p\cdot e_2,p\cdot e_1)\)：两参数 SI 均为动量单位，atan2 只取比值，输出无量纲，匹配 ✅
- \(p^\mu=\hbar k^\mu\)：若 \(k^\mu\) 为波矢，右边 SI = (J s)(m\(^{-1}\)) = kg m s\(^{-1}\)，匹配动量 ✅
- 超越函数：atan2 两输入同量纲；无 exp/sin/log/sinh。

### Q2 符号/方向校对

- \(\alpha=f(\theta)\)：因 \(\theta'=\theta\)，任意不含 observer/boost 结构的 \(f\) 给出 \(\alpha'=\alpha\)。代入非共线例 \(\alpha=\pi/2,\beta>0\)，aberration 给 \(\cos\alpha'=-\beta\)，故一般 \(\alpha'\ne\alpha\)。冲突方向判断正确 ✅
- \(\alpha=\operatorname{atan2}(p\cdot e_2,p\cdot e_1)\)：若 \(p\) 沿 \(e_1\)，角为 0；若 \(p\) 沿 \(e_2\)，角为 \(\pi/2\)。方向读数正确 ✅
- projective 尺度：\(p\mapsto\lambda p\) 且 \(\lambda>0\) 时 atan2 不变；方向不依赖频率/动量尺度，正确 ✅
- massive 情形：\(p^2=m^2c^2\) 不是 null generator，需另给 null 投影规则；方向边界判断正确 ✅

### Q3 循环论证校对

- 检验数据来源：第 1-3 节的 Lorentz 标量、aberration、tetrad 读角公式。
- 输入假设：\(\alpha\) 是 observer celestial angle；\(p^\mu\) 为 massless 时可代表 null direction；massive 时需额外投影。
- 是否循环：结论不是用待证映射生成的模拟数据恢复输入，而是比较两个变换律；不循环 ✅

### Q4 量级鸿沟

- 无 \(10^N\) vs \(10^M\) 量级比较。✅

### Q5 代数验算

- 展开 \(\alpha=f(\theta)\) 的变换：\(\theta'=\theta\Rightarrow f(\theta')=f(\theta)\Rightarrow\alpha'=\alpha\)。与检查块 2 的非共线 aberration 结果矛盾，代数链条正确 ✅
- 展开 atan2 尺度不变性：\(\operatorname{atan2}(\lambda p\cdot e_2,\lambda p\cdot e_1)=\operatorname{atan2}(p\cdot e_2,p\cdot e_1)\) 对 \(\lambda>0\) 成立。✅
- 极限退化 1：\(p\parallel e_1\Rightarrow \alpha=0\)。✅
- 极限退化 2：\(p\parallel e_2\Rightarrow \alpha=\pi/2\)。✅
- 数值量级：无具体数值估算。
- 引用数值来源：无具体数值。

### 警告

- ⚠️ 符号约定警告：第 1 节采用 \((+---)\)，第 3 节显式切换到 \((-+++)\)。第 4 节的 \(p\cdot e_i\) 必须固定在同一度规/标架约定下使用；否则空间分量可能整体或局部带符号差，导致 \(\alpha\) 发生 \(\pi\) 位移或象限误判。当前结论“需要 tetrad 和 null/massless 结构”不受影响，但后续若要给出数值角度必须统一约定。

结论：本检查块无阻断；有 1 条可继续的符号约定警告。

## Q6 综合判定

阻断：无。

警告：

1. ⚠️ \(\omega=-k\cdot u/c\) 的 SI 更像波数尺度或频率除以 \(c\)，后续不得把它直接当作 s\(^{-1}\) 角频率使用，除非补上 \(1/c\) 约定。
2. ⚠️ 文中混用 \((+---)\) 与 \((-+++)\) 两套号差；第 4 节以后涉及 \(p\cdot e_i\)、atan2 象限和空间分量符号时必须显式固定同一约定。

最终判定：

⚠️ INSPECTOR警告：存在上述两个记号/符号约定风险。可继续，但需显式标注。

✅ 最终是否通过：通过（有警告，无阻断）。A 博士 round2 的核心推导在量纲、方向、循环论证、量级鸿沟与代数验算层面未发现阻断错误。

## 改动文件路径

- `D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\synthesis\inspector_A_round2.md`

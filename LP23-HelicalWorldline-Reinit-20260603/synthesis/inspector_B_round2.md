# INSPECTOR_B_round2

输入文件：`D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\current\B\round2.md`

校对范围：仅按 `D:\Claude\ai-reservations\ai\INSPECTOR.md` 的 Q1-Q6 协议检查推导中的量纲、符号/方向、循环论证、量级鸿沟、代数验算与综合判定。不评价发表价值，不做 REVIEWER 工作。

## INSPECTOR_CHECK 1：Pauli bilinear / projective spinor

位置：`round2.md` 第 34-37 行。

Q1 量纲校对：

- `xi = sqrt(rho) e^{i psi} (...)`：若 `rho` 为 spinor bilinear 尺度，则 `xi` 单位为 `sqrt([rho])`；`psi, chi, phi` 必须无量纲。`exp(i psi)`, `cos(chi/2)`, `sin(chi/2)`, `exp(±i phi/2)` 的自变量均无量纲。匹配：✅
- `k^mu = xi^\dagger sigma^mu xi`：左边单位 `[k]`；右边单位 `[xi]^2 = [rho]`，故 `[k]=[rho]`。匹配：✅
- `k_mu k^mu = rho^2(1-|n|^2)=0`：左边单位 `[rho]^2`；右边单位 `[rho]^2`。`|n|^2=1` 无量纲。匹配：✅
- `rho` 若进一步解释为能量、波矢尺度、长度倒数或其他物理量，必须额外定标；原文已显式标注。✅

Q2 符号/方向校对：

- 整体相位极限：`psi -> psi + alpha`，`xi -> e^{i alpha}xi`，`xi^\dagger sigma^mu xi` 中相位抵消，`k^mu` 不变。方向结论“整体 `U(1)` 相位不改变 null 方向”成立。✅
- 相对相位极限：固定 `chi != 0, pi`，改变 `phi`，`n(phi)` 在天球上改变；`phi=0` 与 `phi=pi/2` 给出不同空间方向。方向结论“`phi` 改变 null 方向”成立。✅
- ⚠️ 警告：按标准 Pauli 矩阵 `sigma_y=[[0,-i],[i,0]]` 和文中 spinor 参数化 `(cos(chi/2)e^{i phi/2}, sin(chi/2)e^{-i phi/2})`，计算得到 `n_y=-sin chi sin phi`，而文中写为 `+sin chi sin phi`。若作者采用相反的 `sigma_y` 约定或把 `phi` 定义为反向方位角，则可消解；否则这是 y 分量符号约定未明。该符号不改变本块核心方向结论，但需要显式说明。

Q3 循环论证校对：

- 本块无实验检验数据；使用参数化与 bilinear 定义推出结论。未发现用生成数据回证输入假设的循环。✅

Q4 量级鸿沟标记：

- 无 `10^N` vs `10^M` 量级比较。✅

Q5 代数验算：

- 相位抵消：`(e^{i psi}u)^\dagger sigma^mu (e^{i psi}u)=u^\dagger sigma^mu u`。✅
- 标准 Pauli 逐项验算：`n_x=2cs cos phi=sin chi cos phi`；`n_z=c^2-s^2=cos chi`；`n_y` 的符号依赖 `sigma_y` 与 `phi` 约定，见 Q2 警告。
- null 验算：`|n|^2=sin^2 chi(cos^2 phi+sin^2 phi)+cos^2 chi=1`，故 `k^2=rho^2(1-|n|^2)=0`。✅

本块结论：⚠️ 通过但有符号约定警告。

## INSPECTOR_CHECK 2：contact lift / null geodesic 条件

位置：`round2.md` 第 94-97 行。

Q1 量纲校对：

- `dx^mu/ds=lambda k^mu`：左边单位 `[x]/[s]`；右边单位 `[lambda][k]`，故需 `[lambda]=[x]/([s][k])`。文中称 `lambda` 随 `s` 单位调整，成立但应理解为由 `k` 定标共同决定。✅
- `theta=p_mu dx^mu`：单位 `[p][x]`，即作用量单位或自然单位下的无量纲相位尺度；contact projectivization 中只需其核/比例类。✅
- `theta(gamma')=p_mu x'^\mu=lambda p_mu p^\mu=lambda p^2=0`：左边单位 `[p][x]/[s]`；右边单位 `[lambda][p]^2`，在 `x'^\mu=lambda p^\mu` 的单位定义下匹配。✅

Q2 符号/方向校对：

- 极限 1：`d[xi]/ds=0`，则 `k` 方向固定，`x^mu=x_0^mu+K(s)k_0^mu`，为空间投影固定方向的 null generator。✅
- 极限 2：仅 `xi(s)=e^{i psi(s)}xi_0`，`[xi]` 与 `k` 不变，spacetime 投影仍不出现横向圆周运动。✅
- `x'^\mu || p^\mu` 且 `p^2=0` 时 `theta(gamma')=0`，符号方向无反转。✅

Q3 循环论证校对：

- 无实验检验数据；contact 判据由标准 null cotangent/contact 结构推出。未发现循环。✅

Q4 量级鸿沟标记：

- 无量级比较。✅

Q5 代数验算：

- 代入 `x'^\mu=lambda p^\mu`：`p_mu x'^\mu=p_mu lambda p^\mu=lambda p_mu p^\mu=lambda p^2`。在 null 条件 `p^2=0` 下为 0。✅
- geodesic 退化：平直自由 null geodesic 的非仿射形式允许 `dk^mu/ds=alpha(s)k^mu`；方向不变只差重参数化，和文中表述一致。✅

本块结论：✅ 通过。

## INSPECTOR_CHECK 3：twistor incidence / projective equivalence

位置：`round2.md` 第 118-121 行。

Q1 量纲校对：

- `omega^A=i x^{AA'}pi_{A'}`：左边单位 `[omega]`；右边单位 `[x][pi]`，故需 `[omega]=[x][pi]`。twistor incidence 关系可定义该单位关系。匹配：✅
- `Z~lambda Z`：`lambda` 为 projective 缩放参数，应无量纲。匹配：✅
- `k^{AA'}=pi^A \bar pi^{A'}`：左边单位 `[k]`；右边单位 `[pi]^2`，故 `[pi]=sqrt([k])`。匹配：✅

Q2 符号/方向校对：

- `pi -> e^{i alpha}pi` 时，`pi^A \bar pi^{A'}` 相位抵消，null 方向不变。✅
- `Z -> lambda Z` 在 projective twistor 中为同一点，故整体相位/缩放不产生 spacetime 坐标。✅
- 尺度部分 `|lambda|` 会改变非 projective spinor 定标，但 projective null direction 不变；原文已提醒需区分尺度、相位和物理定标。✅

Q3 循环论证校对：

- 无实验数据；使用 incidence relation 与 projective equivalence。未发现循环。✅

Q4 量级鸿沟标记：

- 无量级比较。✅

Q5 代数验算：

- projective 等价：`Z` 与 `lambda Z` 在 `PT` 中同类；若 `lambda=e^{i alpha}`，相位属于同一 projective 类。✅
- null bilinear 退化：相位乘法不改变 `pi \bar pi`；模长缩放只改尺度，不改方向。✅

本块结论：✅ 通过。

## INSPECTOR_CHECK 4：U(1)/C* 商、connection/holonomy

位置：`round2.md` 第 160-163 行。

Q1 量纲校对：

- `(C^2\{0})/U(1) ~= R_+ x S^2`：拓扑/商空间关系，无 SI 量纲冲突；`R_+` 表示剩余尺度。✅
- `D_s xi=d_s xi+iA_s xi`：左边单位 `[xi]/[s]`；`d_s xi` 单位 `[xi]/[s]`；故 `A_s` 单位 `1/[s]`。匹配：✅
- `Hol=exp(i integral A)`：指数自变量 `integral A` 必须无量纲；文中标注 `A_s ds` 无量纲。匹配：✅

Q2 符号/方向校对：

- 局部规范变换可移动 `psi(s)`；闭合回路 `exp(i∮A)` 或相干比较中的相对相位才可能可观测。方向结论与 gauge/holonomy 判据一致。✅
- `D_s=d_s+iA_s` 的正负号是联络约定；只要规范变换规则同步选择，不影响“局部相位非观测、holonomy 可观测”的方向结论。✅

Q3 循环论证校对：

- 无实验数据；从主丛/联络定义推出可观测对象。未发现循环。✅

Q4 量级鸿沟标记：

- 无量级比较。✅

Q5 代数验算：

- 商空间维数：`C^2\{0}` 为 4 实维，商 `U(1)` 后为 3 实维；`R_+ x CP^1` 为 `1+2=3` 实维。✅
- holonomy 指数：若 `A=A_s ds`，则 `∫A` 无量纲，`exp(i∫A)` 合法。✅

本块结论：✅ 通过。

## INSPECTOR_CHECK 5：projective ratio / alpha-equivalence 类比落回 spinor

位置：`round2.md` 第 188-191 行。

Q1 量纲校对：

- `z_2/z_1 = tan(chi/2)e^{-i phi}`：左边为同类 spinor 分量比值，无量纲；右边 `tan` 与 `exp` 自变量均无量纲。匹配：✅
- `n=(sin chi cos phi, sin chi sin phi, cos chi)`：各分量无量纲；`sin/cos` 自变量无量纲。匹配：✅

Q2 符号/方向校对：

- `xi -> e^{i psi}xi` 时，`z_2/z_1` 中整体相位抵消。方向结论“整体相位不可观测”成立。✅
- `phi` 改变时，`z_2/z_1` 的相位改变，`n` 的天球方向改变。方向结论成立。✅
- 同 INSPECTOR_CHECK 1：若采用标准 `sigma_y` 与文中 spinor 参数化，`n_y` 正负号需约定说明；但 `phi` 改变方向这一结论不受影响。⚠️

Q3 循环论证校对：

- 类比只用于发现结构，物理判断落回 spinor bilinear/contact quotient；未用类比本身回证物理结论。未发现循环。✅

Q4 量级鸿沟标记：

- 无量级比较。✅

Q5 代数验算：

- 分量比值：`z_2/z_1 = [sqrt(rho)e^{i psi}sin(chi/2)e^{-i phi/2}]/[sqrt(rho)e^{i psi}cos(chi/2)e^{i phi/2}] = tan(chi/2)e^{-i phi}`。✅
- `phi` 极限：`phi=0` 与 `phi=pi/2` 给出不同 `z_2/z_1` 相位与不同天球方位。✅

本块结论：⚠️ 通过但继承 y 分量符号约定警告。

## INSPECTOR_CHECK 6：相对相位旋转反例 / geodesic 破坏

位置：`round2.md` 第 223-226 行。

Q1 量纲校对：

- `phi(s)=Omega s`：`phi` 无量纲，故 `[Omega]=1/[s]`。文中已标注。✅
- `n(s)` 各分量无量纲；`Omega s` 是 `sin/cos` 自变量，必须无量纲。匹配：✅
- `|dn/ds|^2=Omega^2 sin^2 chi`：左边单位 `1/[s]^2`；右边单位 `1/[s]^2`。匹配：✅
- `k^mu=rho(1,n)`：单位 `[rho]`；`k^2=0` 单位 `[rho]^2`。匹配：✅

Q2 符号/方向校对：

- 极限 1：`Omega=0` 或 `chi=0,pi` 时 `|dn/ds|=0`，方向不变，退化为 geodesic 允许情形。✅
- 极限 2：`Omega != 0` 且 `chi != 0,pi` 时 `|dn/ds|=|Omega sin chi|>0`，方向改变。✅
- `dk^mu/ds=(0,rho dn/ds)`；若 `dk^mu/ds=alpha k^mu`，时间分量给出 `alpha rho=0`，故 `alpha=0`，但空间分量非零，矛盾。因此不是只差重参数化比例项。✅
- 方向结论“相对相位旋转给出 null curve，但不给出平直自由 null geodesic”成立。✅

Q3 循环论证校对：

- 显式参数化反例，不依赖实验数据；推导没有用结论生成检验数据再回证结论。✅

Q4 量级鸿沟标记：

- 无量级比较。✅

Q5 代数验算：

- `dn/ds=(sin chi(-Omega sin Omega s), sin chi(Omega cos Omega s), 0)`，故 `|dn/ds|^2=Omega^2 sin^2 chi(sin^2 Omega s+cos^2 Omega s)=Omega^2 sin^2 chi`。✅
- `k^2=rho^2(1-|n|^2)=0`；但 `dk/ds` 不平行于 `k`，故非平直自由 null geodesic。✅

本块结论：✅ 通过。

## 阻断 / 警告汇总

阻断：

- 无 INSPECTOR 阻断错误。

警告：

- ⚠️ `round2.md` 第 25-35 行、第 189 行附近：spinor 参数化与 `n_y=+sin chi sin phi` 的符号需要明确 Pauli `sigma_y` 或方位角约定。按标准 Pauli `sigma_y=[[0,-i],[i,0]]`，文中参数化会给出 `n_y=-sin chi sin phi`。这是轻微符号/约定警告，不改变本轮核心方向结论。

## Q6 综合判定

⚠️ INSPECTOR警告：Pauli bilinear 的 y 分量符号依赖未声明约定。可继续，但需在后续推导中显式标注 `sigma_y`/`phi` 约定，避免把旋转方向或手征方向误用。

最终判定：有警告通过。B博士 round2 可继续；PI 不应把未声明的 y 方向正负号用于后续定向/手征结论，除非先补充约定。

## 本次改动文件

- `D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\synthesis\inspector_B_round2.md`

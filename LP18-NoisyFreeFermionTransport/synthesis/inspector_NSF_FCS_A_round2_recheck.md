# INSPECTOR recheck - NSF_FCS Round2 A

输入文件：
- `current/A/NSF_FCS_round2_A.md`
- `synthesis/inspector_NSF_FCS_A_round2.md`

未读取 B 文件。

## 复查目标

复查 A 是否修复上一轮阻断。重点检查：

`lambda''=<a>+2<B phi>=<a>+2<h,phi>+2<C>`

的符号、单位、两态校验，以及 `H_-1` 上界降级是否自洽。

## Q1. 量纲校对

A 当前定义：

- `b(eta)=L'_0 1=sum_z c(eta,z) q_R(eta,z)`，单位 `s^-1`。
- `a(eta)=L''_0 1=sum_z c(eta,z) q_R(eta,z)^2`，单位 `s^-1`。
- `J=<b>_pi`，单位 `s^-1`。
- `h=b-J`，单位 `s^-1`。
- `B f=L'_0 f=sum_z c(eta,z) q_R(eta,z) f(eta^z)`。
- Poisson 方程固定为 `L phi=-h`，`<phi>_pi=0`。

逐项检查：

- `lambda_R''(0)`：未缩放物理时间下的 SCGF 二阶导，单位 `s^-1`。
- `<a>_pi`：rate 加权的 `q_R^2`，`q_R` 为计数增量无量纲，因此单位 `s^-1`。
- `phi`：由 `L phi=-h` 得出，`L` 与 `h` 同为 `s^-1`，所以 `phi` 无量纲。
- `<B phi>_pi`：`B` 对无量纲函数输出 rate，单位 `s^-1`。
- `<h,phi>_pi`：`h` 为 `s^-1`，`phi` 无量纲，单位 `s^-1`。
- `C=sum_z c q_R[phi(eta^z)-phi(eta)]`：rate 乘无量纲差分，单位 `s^-1`。

结论：`lambda''=<a>+2<B phi>=<a>+2<h,phi>+2<C>` 的各项单位一致，均为 `s^-1`。本轮未发现该核心公式的量纲错误。

超越函数自变量：A 当前核心公式中未发现 `exp`、`log`、`sin`、`sinh` 等带量纲自变量问题。`L_s` 中 `exp(s q_R)` 要求倾斜参数 `s` 与计数增量配对；这里的 `s` 是 FCS counting field，不是 SI 时间秒，作为无量纲 counting field 使用时合格。为避免符号混淆，后续可把 counting field 改记为 `theta`，但这不是阻断。

## Q2. 符号与方向校对

### tilted-generator 二阶扰动

A 当前推导：

`L_s r_s = lambda(s) r_s`

其中 `r_s=1+s phi+O(s^2)`，`lambda(s)=s J+s^2 lambda''(0)/2+O(s^3)`。

一阶：

`L phi+L'_0 1=J`

即

`L phi=-(b-J)=-h`。

二阶对左稳态 `pi` 取平均：

`lambda''(0)=<L''_0 1>_pi+2<L'_0 phi>_pi=<a>_pi+2<B phi>_pi`。

符号检查通过。这里 `B phi=L'_0 phi` 是 jump-tilt 的一阶算子作用在 corrector 上，不是乘法内积 `<h,phi>`。上一轮阻断的根源正是把 jump-current FCS 误降为纯 additive functional 的正 `H_-1` 二次型；A 当前稿已经修正。

### 展开为 `<a>+2<h,phi>+2<C>`

A 定义：

`C(eta)=sum_z c(eta,z) q_R(eta,z)[phi(eta^z)-phi(eta)]`

则

`B phi(eta)=sum_z c q_R phi(eta^z)`

而

`b(eta) phi(eta)=sum_z c q_R phi(eta)`。

因此

`B phi=b phi+C`。

稳态平均下 `<b phi>_pi=<h phi>_pi+J<phi>_pi=<h,phi>_pi`，因为 `<phi>_pi=0`。故

`<B phi>_pi=<h,phi>_pi+<C>_pi`

并得到

`lambda_R''(0)=<a>_pi+2<h,phi>_pi+2<C>_pi`。

符号检查通过。尤其 `2<C>` 没有固定正号，可为负，并可抵消 `<a>` 与 `2<h,phi>` 的 `O(1)` 部分；这与 jump-current martingale/corrector 交叉变差解释一致。

## Q3. 两态校验

A 的两态交替链：

- 状态 `0 <-> 1`，两方向 rate 均为 `c`。
- `0->1` 记 `q=+1`，`1->0` 记 `q=-1`。
- 长时净 current 只等于终态与初态差，因此 `lambda''(0)=0`。

A 的计算：

- `pi(0)=pi(1)=1/2`。
- `b(0)=c`，`b(1)=-c`，`J=0`，`h=b`。
- `a(0)=a(1)=c`，所以 `<a>=c`。
- 解 `L phi=-h` 得 `phi(0)=1/2`，`phi(1)=-1/2`。
- `B phi(0)=c phi(1)=-c/2`，`B phi(1)=(-c) phi(0)=-c/2`，所以 `<B phi>=-c/2`。

代入完整公式：

`lambda''=c+2(-c/2)=0`。

检查通过。该校验直接击中上一轮阻断：若错误使用 `<a>+2<h,phi>`，则 `<h,phi>=c/2`，给出 `2c`，与精确结果 `0` 矛盾。A 当前完整公式能给出正确零方差。

补充检查 `C`：

- 状态 0：`C(0)=c[phi(1)-phi(0)]=-c`。
- 状态 1：`C(1)=c(-1)[phi(0)-phi(1)]=-c`。
- `<C>=-c`。
- `<a>+2<h,phi>+2<C>=c+2(c/2)+2(-c)=0`。

因此 `<a>+2<B phi>` 与 `<a>+2<h,phi>+2<C>` 两种写法在两态模型中一致。

## Q4. `H_-1` 上界降级检查

上一轮阻断要求 A 不得继续声称 jump-current FCS 二阶项等于正的

`<a>+2<h,(-L)^-1h>`

或由此推出与 conductance 同标度。

A 当前修正：

1. 明确写出纯 additive functional 的 `2<h,phi>` 是正 `H_-1` 项，但 reservoir jump-current 不是纯 additive functional。
2. 明确 `lambda_R''=<a>+2<h,phi>+2<C>`，其中 `2<C>` 是 martingale cross term。
3. 明确不再声称 `lambda_R''` 有正的 `+2||h||_{-1}^2` 上界。
4. 将 `||h||_{-1}` 的角色降级为控制 Poisson corrector `phi` 的能量，而不是直接给出 FCS 方差。
5. 将 `lambda_R''=O(G_R(L))` 降级为必须证明完整组合 `<a>+2<B phi>` cancellation 的待证命题。

该降级自洽。

A 给出的保守上界：

`lambda_R'' <= 2<a>_pi+2<Gamma phi>_pi`

并使用 `<Gamma phi>_pi=2<h,phi>_pi`，得到

`lambda_R'' <= 2<a>_pi+4 C_sec ||h||_{-1,S,L}^2`

这来自

`Var(M_Q+M_phi) <= 2 Var(M_Q)+2 Var(M_phi)`

的粗 Cauchy-Schwarz 型估计，而不是把 `lambda''` 本身误认为正 `H_-1` 二次型。系数虽粗，但方向安全。

需保留的警告：该上界通常远弱于 conductance 标度，因为 `<a>_pi` 可能为 `O(1)`。A 已明确把三段标度表降级为“待验证候选”，并写明必须证明 `<a>+2<B phi>` 的 cancellation 后才可声称 `lambda_R''~G_R(L)`。因此不再构成阻断。

## Q5. 循环论证与数量级风险

未发现 A 当前稿把 fractional Fick law 或 mean conductance 直接当作 jump-current variance 的证明。

A 当前逻辑是：

- fractional trace / `H_-1` 估计可用于控制 corrector；
- 但 corrector 控制不自动推出 `<a>+2<B phi>` 与 `G_R(L)` 同标度；
- 真正需要的是 activity 与 cross term 的组合估计；
- 在证明或数值确认前，`lambda_R''~G_R(L)` 不可写成结论。

该逻辑避免了上一轮指出的循环风险。

数量级警告仍存在但已被显式标注：endpoint activity `<a>` 通常 `O(1)`，而 `G_R(L)` 随 `L` 衰减；若要得到 conductance 标度，必须有精确负交叉项抵消。这是后续研究难点，不是本轮公式阻断。

## Q6. 综合判定

INSPECTOR 复审通过。A 已修复上一轮阻断。

通过理由：

1. 核心二阶公式已从错误的正 `H_-1` 二次型修正为完整 tilted-generator 公式：
   `lambda_R''(0)=<a>_pi+2<B phi>_pi`。
2. 展开式
   `lambda_R''=<a>+2<h,phi>+2<C>`
   的符号、单位、常数规范均自洽。
3. 两态交替链给出精确校验 `lambda''=0`，完整公式通过，旧公式失败。
4. `H_-1` 的角色已正确降级为 corrector/能量控制工具，不再直接承载 jump-current variance 或 conductance 同标度结论。
5. `lambda_R''=O(G_R(L))` 已被降级为待证 cancellation statement，没有被当作已证结论。

剩余警告：

- continuous trace 变分式必须继续显式写出有单位的边界线性泛函与时间归一化；不能使用裸的 `2 f(1)` 与有单位 Dirichlet form 混写。
- spectral gap 标度若用于严格上界，仍需补充 long-jump exclusion with reservoirs 的 gap 下界引用或证明。
- Round 3 若继续推进，应优先输出 `<a>`、`2<h,phi>`、`2<C>`、`2<B phi>` 与总和的 exact Poisson decomposition，以验证 cancellation 是否真实达到 `G_R(L)` 标度。

最终结论：解除阻断；A 可进入下一轮，但后续不得把 `H_-1` trace bound 单独等同于 reservoir jump-current FCS 方差标度。

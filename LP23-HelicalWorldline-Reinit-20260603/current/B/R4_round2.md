# LP23-R4 Round2 - B博士报告

日期：2026-06-03

## §0 框架声明

本轮我仍沿用计算机科学的 proof-carrying code / capability security 框架，但把 Round1 的“手写 constrained columns”升级为“列 + witness + checker”。

借来的结构不是“程序像物理”这种表面类比，而是：一个扩展列不能只因为它能在事后吸收 residual 就被接纳；它必须携带可检查的 witness，说明它来自预注册协议、局部支撑、无未来依赖、被动衰减历史核。物理翻译是：

\[
C_W(P)=\operatorname{span}\{D_0,g_i:\operatorname{check}(g_i,w_i)=\mathrm{PASS}\}.
\]

判据因此分成两层：

1. 代数层：若允许 residual-shaped oracle column，则 residual 必然可被吸收。
2. witness 层：该 oracle column 是否有资格进入闭包。若它无 witness 或 witness 失败，则不进入 \(C_W(P)\)。

本轮新增脚本：

`D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\scripts\r4_witness_checker_toy.py`

实现的自动检查器：

- support-locality：列的实际非零支撑必须匹配 witness，且边邻接图支撑直径不超过 toy 局部阈值。
- protocol partial order / no future dependence：witness 中每个 target 只能依赖协议序上不晚于 target 的 source。
- passive/decaying history kernel：history kernel 必须非负、单调衰减，且 witness 权重匹配列幅度。
- measurement-source / pre-registration：oracle/residual-shaped source 禁止，未预注册列禁止。

## 关键运行输出

命令：

```powershell
python D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\scripts\r4_witness_checker_toy.py
```

关键输出：

```text
R4 witness-checker toy
D0 shape=(9, 5) D1 shape=(1, 9) ||D1@D0||=0
candidate closedness=4.16e-17
candidate residual=[-0.088173 -0.088173  0.176347  0.412578  0.148057 -0.560635 -0.279182
  0.42951   0.42951 ]

witness checks for legal columns:
  local_loop       PASS
  history_fast     PASS

witness checks with residual-shaped oracle column:
  local_loop       PASS
  history_fast     PASS
  residual_oracle  FAIL
    - nonlocal support diameter=2 max=1
    - future dependence e0 <- e1
    - oracle/residual-shaped source is not an allowed measurement source

closure comparison:
legal_only:WITNESS_OBSTRUCTION               rank= 6 residual_norm=0.8971489604 accepted=['local_loop', 'history_fast'] rejected=[]
with_residual_oracle:WITNESS_OBSTRUCTION     rank= 6 residual_norm=0.8971489604 accepted=['local_loop', 'history_fast'] rejected=['residual_oracle']
algebraic_open_if_oracle_ignored_checks       rank= 7 residual_norm=5.240587849e-16

verdict=TOY_SURVIVES_CHECKER: oracle would absorb algebraically, but fails locality/order/source witnesses before entering closure
```

结论：若忽略 checker，residual-shaped oracle column 把 residual norm 降到 \(5.24\times10^{-16}\)，即代数吸收成功；但 witness checker 拒绝它进入闭包，所以 witness closure 的 rank 保持 6，residual norm 保持 \(0.8971489604\)。本 toy 没有判死；它说明判死条件被推迟到“是否能给 residual-shaped column 构造合法 witness”。在当前 checker 下不能，因为 oracle 同时违反局部性、协议偏序和预注册来源。

--- INSPECTOR_CHECK ---
[公式] \(C_W(P)=\operatorname{span}(D_0,\{g_i:\operatorname{check}(g_i,w_i)=\mathrm{PASS}\})\)，\(n_W(r)=\|(I-\Pi_{C_W(P)})r\|_{\Sigma^{-1}}\)。脚本输出 \(n_W=0.8971489604\)，若绕过 checker 加入 oracle 列则 \(n_{\rm open}=5.240587849\times10^{-16}\)。无 SI 单位，有限矩阵 toy。
[方向] residual-shaped column 代数上可吸收 residual，但因 witness 失败不进入协议闭包；合法局部列和被动衰减历史核列通过。
[数据] 本地脚本 `scripts/r4_witness_checker_toy.py`，无外部实验数据。
[假设] 固定 5 节点 9 边有限链复形，\(D_1D_0=0\)，固定协议序 \(e0<...<e8\)，局部性阈值为边邻接直径 1，history kernel 只检查非负衰减 FIR toy。

## 深挖1：更深层数学结构

Round1 的结构是“可生成子空间”；Round2 的更深层结构是“带证明对象的可生成子空间”。对象不只是 \(g\in C_1\)，而是 pair \((g,w)\)。闭包函子先经过 checker：

\[
(g,w)\mapsto \begin{cases}
g,& \operatorname{check}(g,w)=\mathrm{PASS},\\
\varnothing,& \operatorname{check}(g,w)=\mathrm{FAIL}.
\end{cases}
\]

这把 R4 的问题从普通商空间

\[
\ker D_1 / \operatorname{span}(D_0,G)
\]

推进到 capability-filtered quotient：

\[
[r]_W\in \ker D_1 / C_W(P).
\]

深层同构是 proof-carrying code 中“字节串能执行”与“字节串有权限执行”的分裂。residual oracle 是能执行的字节串，但没有 capability。R4 若要活，必须证明物理 protocol 自然给出这种 capability filter，而不是人为加权限表。

## 深挖2：原学科下一层推广

proof-carrying code 的下一层不是单个 proof，而是 proof checker 的可信计算基。映射回 R4：真正重要的不是某列是否附带 witness，而是 checker 本身是否来自独立协议合同。

当前 toy checker 的可信计算基包括：

- 支撑局部性来自固定边邻接图和直径阈值。
- 协议偏序来自预先给定的边时间序。
- 被动核来自非负、单调衰减 FIR 权重。
- 来源检查来自“oracle source 禁止、必须预注册”的规则。

这层推广给出一个更尖锐的失败靶：如果这些 checker 规则只是 PI/B 手写，那么 R4 仍只是人为限制下的 obstruction；如果这些 checker 能从真实测量协议、因果响应和局域 EFT 生成规则独立推出，R4 才有进入 Round3 的资格。

## 失败记录

失败1：当前 witness checker 仍是 toy 可信计算基，不是物理定理。它证明了“可执行 checker 可以阻止 residual oracle”，没有证明真实光学/介质/测量协议必须采用这些 checker。

失败2：support-locality 用的是有限边邻接直径 1。真实局域性应当有尺度、坐标、边界条件和 coarse-graining，不应只是图直径阈值。

失败3：passive kernel 只检查非负衰减 FIR。真实被动响应还需要解析性、正实性、能量不等式或 Kramers-Kronig/Herglotz 类约束。

失败4：protocol order checker 只发现显式 future dependence。它没有处理隐藏状态、滤波器内部记忆、估计器回填、后验模型选择等更隐蔽的未来泄漏。

## 本轮产出格式

本轮的跨学科跳跃：计算机科学 -> proof-carrying code / capability security -> 物理扩展列必须携带可验证 witness。

这个结构的数学对象：带证明对象的扩展列 \((g,w)\)、checker-filtered closure \(C_W(P)\)、以及 quotient class \([r]_W\in\ker D_1/C_W(P)\)。

如果这个同构成立，最奇怪的可检验预测是：同一个 residual 在“代数开放模型”中消失，但在“带 witness 的局部-因果-被动协议闭包”中保持非零；差别不来自线性代数，而来自列的准入证明。

A 博士最可能反对的点：checker 规则仍是人为 toy，尚未从成熟 EFT/operator closure、causal response realization 或真实 measurement protocol 中自然推出。

本轮失败记录：见上。核心失败是 checker 的物理来源仍未建立。

下一步：把 checker 的可信计算基物理化。优先尝试三条硬化路线：

1. 用正实/被动实现理论替换非负衰减 FIR toy。
2. 用局域算符生成与冗余消去替换图直径 locality。
3. 用预注册测量 DAG / causal model identifiability 替换手写 protocol order。

需要 PI 投喂的文献方向：positive-real functions passive realization Herglotz response；local EFT operator basis redundancy EOM IBP field redefinition；causal DAG pre-registration post-treatment bias system identification residual modeling。

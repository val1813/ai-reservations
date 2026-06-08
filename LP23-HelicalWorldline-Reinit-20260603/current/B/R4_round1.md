# LP23-R4 Round1 - B博士报告

日期：2026-06-03

## §0 框架声明

我的框架：计算机科学。

借来的结构不是“程序像物理”这种表面类比，而是**类型系统/编译器中的生成语法闭包**：一个表达式是否可用，不由它是否能事后拼出目标字节串决定，而由它是否能被 grammar/type rules 在有限步内合法生成决定。

物理翻译：R3 的任意补列等价于 untyped escape hatch：只要 residual 存在，就把 residual 本身塞进 template/nuisance/history。R4 必须改成 typed protocol closure：

\[
C_R(P)=\operatorname{span}\{D_0,\ g_1,\ldots,g_m:\ g_i\ \text{由规则 }R\text{ 有限生成}\}.
\]

判据不是“存在某列能吸收 residual”，而是：

\[
\|(I-\Pi_{C_R(P)})r\|_{\Sigma^{-1}}>0,\quad \|D_1 r\|\approx 0.
\]

若开放规则 \(R_{\rm open}\) 允许 oracle residual column，则 obstruction 必死；若受限规则 \(R_{\rm constrained}\) 只允许局域/因果/响应生成列，且 residual 仍非零，才有 protocol-closure obstruction 的 toy witness。

## 可执行压力测试

新增脚本：

`D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\scripts\r4_protocol_closure_toy.py`

它沿用 R3 的有限复形：

\[
C_0 \xrightarrow{D_0} C_1 \xrightarrow{D_1} C_2,\quad D_1D_0=0.
\]

但把扩张合同拆成两类：

1. open closure：允许 arbitrary residual-direction column。此规则故意是 oracle/open 合同，应吸收 residual。
2. constrained closure：只允许两个 toy 生成列：
   - `local_loop`：固定邻接局域 loop stencil；
   - `history_fast`：固定协议顺序上的非负衰减 FIR history kernel。

明确声明：这些 constrained rules 只是 toy 人工限制，不是从 Maxwell、EFT、真实介质响应或真实测量协议推导出的物理定律。

## 关键运行输出

命令：

```powershell
python D:\Claude\ai-reservations\LP23-HelicalWorldline-Reinit-20260603\scripts\r4_protocol_closure_toy.py
```

关键输出：

```text
R4 protocol-closure obstruction toy
D0 shape=(9, 5) D1 shape=(1, 9) ||D1@D0||=0

constrained generated columns:
  local_loop       closedness=0 support=[3, 4, 5]
  history_fast     closedness=0 support=[6, 7, 8]

candidate residual:
  closedness=4.16e-17
  residual=[-0.088173 -0.088173  0.176347  0.412578  0.148057 -0.560635 -0.279182
  0.42951   0.42951 ]

closure comparison:
constrained_closure    label=CONSTRAINED_OBSTRUCTION   rank= 6 closedness=4.16e-17 residual_norm=0.8971489604 column_closedness=0
open_closure           label=OPEN_ABSORBED             rank= 7 closedness=4.16e-17 residual_norm=5.240587849e-16 column_closedness=2.78e-17
```

结论：同一个 closed residual 在 open closure 下被吸收到机器精度零；在 constrained closure 下保留非零 residual norm \(0.8971489604\)。这不是证明物理 obstruction 存在，只证明“任意补列吸收”与“合法生成闭包吸收”在有限 toy 中可以分裂。

--- INSPECTOR_CHECK ---
[公式] \(C_R(P)=\operatorname{span}(D_0,G_R)\)，\(n_R(r)=\|(I-\Pi_{C_R(P)})r\|_{\Sigma^{-1}}\)。本脚本输出 \(n_{\rm constrained}=0.8971489604\)，\(n_{\rm open}=5.240587849\times10^{-16}\)。无 SI 单位，有限矩阵 toy。
[方向] open/oracle 合同吸收 residual；受限 toy grammar 保留 closed nonzero quotient class。
[数据] 本地脚本 `scripts/r4_protocol_closure_toy.py`，无外部实验数据。
[假设] \(D_1D_0=0\)；whitened metric 由固定 \(\Sigma\) 给定；constrained grammar 的 locality/causality/passivity 是人工 toy 限制，不是真实物理推导。

## 深挖1：更深层数学结构

第一层同构：类型系统中的“well-typed term”对应物理中的“合法扩张列”。R3 的漏洞是把任意 byte string 当成 well-typed term。

第二层同构：这不是普通线性代数，而是**可生成子对象的商空间**。同一个 residual 是否为 obstruction 取决于生成规则 \(R\)，即

\[
[r]_R\in \ker D_1 / C_R(P).
\]

更深的对象是“规则范畴中的可达子空间”：若规则变换 \(R\to R'\) 是保守扩张，则 \(C_R(P)\subseteq C_{R'}(P)\)，residual class 只能变小；若任意 \(R'\) 都能加入 oracle residual column，则 obstruction 概念坍缩。

## 深挖2：原学科下一层推广

计算机科学里的下一层不是 grammar，而是**proof-carrying code / capability security**：代码不仅要能运行，还要携带可验证证明，说明它没有越权访问。

物理翻译：一个补列不能只声称“局域/因果/响应”，还必须携带 witness：

- locality witness：支持集如何由邻域规则生成；
- causality witness：列的时间/协议偏序没有反向依赖；
- response witness：核满足被动性、稳定性、Kramers-Kronig 或相应真实响应约束；
- measurement witness：该列来自允许的测量协议改写，而不是事后拟合。

若 R4 进入 Round2，toy 应从“人工列列表”升级为“列 + witness checker”。没有 witness 的列即使能吸收 residual，也应判为非法扩张。

## 本轮失败记录

失败1：第一次 constrained grammar 给了过多生成列，和 \(D_1\) 闭合约束一起压满 9 维空间，无法构造 closed-but-unabsorbed witness。这说明 toy grammar 过宽会让 R4 退化成 R3。

失败2：当前 constrained rules 仍只是手工规则。它们证明了逻辑可能性，不证明真实光学/介质/测量协议会给出同样闭包。

失败3：脚本只检查有限维线性 span，没有检查非线性响应、频域解析性、真实能量条件或 gauge/naturality。

## §末 产出格式

本轮的跨学科跳跃：计算机科学 → 类型系统/生成语法闭包/proof-carrying code → 物理扩张列必须由合法协议规则生成并携带 witness。

这个结构的数学对象：有限链复形上的规则生成子空间 \(C_R(P)=\operatorname{span}(D_0,G_R)\)，以及商类 \([r]_R\in\ker D_1/C_R(P)\)。

如果这个同构成立，最奇怪的可检验预测是：同一 residual 在“开放模型补列”中消失，但在带 witness 的局域-因果-响应闭包中保持非零；真实检验应寻找这种 closure-dependent residual splitting。

A博士最可能反对的点：constrained grammar 是人工选择，尚未从 EFT/operator basis、causal response 或 system identification 的成熟闭包理论中自然推出。

本轮失败记录：见上；核心失败是 toy 规则未物理化，且有限线性模型过窄。

下一步计划：把 constrained grammar 改成 witness checker，而不是手写列；至少实现 support-locality、protocol partial order、passive kernel 三个自动检查器。

需要PI投喂的文献方向：proof-carrying code/type systems as grammar closure；causal response passivity Kramers-Kronig constraints；local EFT operator generation with redundancy removal；system identification with structured residual model sets。

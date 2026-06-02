# A博士 Phase 1 — 相图坐标系构造

## 目标

把 LP4-S1 与 LP4-S2 的结论放入同一坐标系，形成可继续推进的 NHSE 存活/抑制相图。

## 三轴定义

### 轴 1：结构层 `M`

描述 Lindbladian/postselected 是否可由同一母框架追踪。

取值：
- `M=0`：局域格点耗散，不能反转 NHSE。
- `M=1`：非局域 jump operator 可写成结构层母框架。
- `M=mix`：母空间有限尺寸/OBC 效应与 N 维 bulk 公式不同步。

### 轴 2：填充/sector 层 `R`

描述 DR-NHDD 的方向性分段。

取值：
- `R_low`：低填充率区，DR-NHDD 多为正方向。
- `R_high`：高填充率区，DR-NHDD 多为负方向。
- `R_cross`：`rho≈0.75` 附近，freeze/边界依赖显著。

### 轴 3：边界/实现层 `B`

描述 PBC/OBC、finite-size、physical jump 实现是否改变可观测结论。

取值：
- `B_bulk`：bulk 公式可靠。
- `B_obc`：OBC 有限尺寸主导。
- `B_impl`：非局域 jump operator 的物理实现/相位锁定主导。

## 相图区域

### 区域 I：局域耗散抑制区

条件：

`M=0`

结论：

局域耗散只改变 NHSE 的存在性或衰减尺度，不产生方向反转。此区由 LP4-S1 的否定性定理控制。

### 区域 II：非局域 jump 方向反转区

条件：

`M=1`, `B_bulk`

结论：

非局域 `L_j ~ c_j + i c_{j+1}` 可产生方向反转。bulk 判据由

`gamma_c = 1 - (t_L - t_R)/G`

控制。此区是 LP4-S1 的主正结果。

### 区域 III：填充率分段诊断区

条件：

`R_low` 或 `R_high`

结论：

NHSE 方向性可由 DR-NHDD 做经验诊断，但不能上升为 sector-independent 拓扑不变量。此区由 LP4-S2 控制。

### 区域 IV：混合边界区

条件：

`R_cross` 或 `B_obc` 或 `B_impl`

结论：

不能写成单一相图判据。需要分层显示：

1. 母框架结构层。
2. DR-NHDD 诊断层。
3. 实现/边界层。

## A侧判定

LP4-S3 可以推进，但完整相图应是“三层叠加图”，不是单一拓扑相图。

可写的强结论：

**NHSE 存活/抑制边界可由结构层、填充诊断层和边界实现层三者共同刻画。**

不可写的强结论：

**存在单一 sector-independent 拓扑不变量统一整个 HN-Hubbard 相图。**

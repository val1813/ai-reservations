# LP10-S6：准晶中flux-space量子度量与超流权重

**所属长命题：** LP-10 量子几何平带超导

**子命题北极星（候选池原文）：** 准晶无平移对称性→动量空间量子几何张量无法定义。flux-space（相位空间）量子度量是否提供几何下界的推广？

**依赖：** 无（与S1并行，处理准晶；S1处理晶体）。可引用S1晶体结论作对照。

**驱动矛盾（PI苏格拉底精确化，见研究计划.md）：**
- 命题A（flux-space推广成立）：准晶虽无布洛赫动量k，但可用twisted boundary conditions的相位φ(flux)作参数，定义flux-space量子度量 g_φ。超流权重 D_s∝∂²E/∂φ² 与 g_φ 关联，几何下界以 D_s≥(flux-space几何量)推广。Sun-Guo-Yang 2025(arXiv:2507.20540)方向。
- 命题B（推广失败/平凡）：(B1) flux-space只有d个分量(d=维数)，是零维"动量"——g_φ是单点量非BZ积分，无拓扑不变量(无Chern数类比，∫只在d维flux环面)；(B2) 准晶的拓扑来自高维母空间(超空间cut-and-project)，flux-space几何丢失这个信息→下界要么平凡(=0)要么需高维超空间几何而非flux-space。

**运行模式：** v3.1 纯推导（twisted boundary phase形式体系+Fibonacci/Penrose准晶解析+Sun-Guo-Yang 2025文献）

**目录：** current/plan, current/A, current/B, synthesis

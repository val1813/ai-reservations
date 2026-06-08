# INSPECTOR_A R2 Round2 校对

判定：警告，不阻断。

主要警告：

1. `I_K=||r_perp||^2` 的单位是 `[r]^2`；相位情形为 `rad^2`，不是自动无量纲。若要跨实验比较，应做噪声协方差白化。
2. `r_perp` 应使用联合模板空间的一次正交投影：`Pi_standard = Pi_span(D,L_chi,L_spin,L_M,L_disp)`，不能写成多个投影直接相减，除非证明子空间正交且投影可交换。
3. 4D `K`、`chi(omega,k)`、worldline kernel 的测度和 delta 单位需要显式约定；Mashhoon kernel 嵌入 4D 时应写明 `d tau' delta_V(x',z(tau')) M(tau,tau')`。

无阻断项。当前文件没有把条件性活口误当成已证明存在。

# B博士 Phase 2 作业 — CooperativeAvalanche 反向审查

## 审查问题

Phase 1 中 B 侧有三个需要修复的点：

1. avoided crossing 角度误用了 `delta_single / Delta_E`。
2. k-core 映射容易被误读为严格动力学定理。
3. Liouville `beta` 与串行级联可能逃逸。

## 修复结论

### B2.1 avoided crossing 降格

原先的 avoided crossing 概率论证不能作为独立主证据，因为热化通道能级密度极高，问题不在“是否能量匹配”，而在“有效矩阵元是否足够大”。

修正后：

`|V_coop|^2 ~ prod_i |V_i|^2`

这与 A 侧 ETH-FGR 的二阶/高阶矩阵元压制一致。因此角度2应降格为旁证，不能列为独立三角验证主支柱。

### B2.2 k-core 映射的正确强度

k-core 映射给出的是必要图论条件，不是从量子 Liouville 方程推出的严格等价定理。

可保留的强表述：

若有效耦合图在 `d_c = zeta ln W` 尺度下无 k-core，则同时协同参与集合不存在。

不可保留的强表述：

k-core 阈值完全等价于量子协同雪崩阈值。

### B2.3 Liouville 与 badly approximable 分界

Liouville `beta` 下 `L_max` 和低无序区域密度可失控，单区域前提已经失败，因此不能用本题结论排除协同。

这不是本题的新反例，而是 LP1-S3 Diophantine 分类的既有边界：

- badly approximable：本题结论适用。
- Liouville：数论保护不成立，本题不适用。

### B2.4 串行级联

串行级联不是“同时协同”。它的安全性取决于每一步激活后的有效尺寸、尾巴长度和相边界余量，不能由本题的一阶正交性定理排除。

因此 B 侧建议把串行级联写成开放 caveat，而不是继续补做成同一题内结论。

## B侧最终判决

允许本题以“有边界”收官：

- 主结论：同时协同不会推翻 badly approximable 准周期势下的数论稳定性。
- 限定：不覆盖串行级联、Liouville `beta`、WPL 单区域尾巴和相边界临界余量。
- avoided crossing 角度降格为旁证。

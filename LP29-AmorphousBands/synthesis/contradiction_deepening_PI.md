# LP29 矛盾深挖：五个为什么

## 表面矛盾

为什么 a-In2O3 无长程周期仍能出现 band-like transport，而传统判据和局域结构判据都看似能解释？

## Five Whys

1. 为什么 mobility-edge/Ioffe-Regel 与 graph/connectivity 会竞争？
   因为一个在动量/输运参数空间描述扩展态边界，另一个在实空间结构网络描述可传播通道。

2. 为什么两个描述都可能有效？
   因为它们可能是同一无序哈密顿量的不同投影: 结构权重决定谱与自能，谱与自能又决定 IPR、linewidth、Drude weight 与 mobility edge。

3. 为什么 prior art 会吞掉“新机制”声张，却没有直接结束 LP29？
   因为 prior art 已说明多种投影各自有解释力，但未必在同一样品、同一外部标签、同一 controls 下检验投影临界面是否同步。

4. 为什么同步性比单个指标更基础？
   若存在同一传播算子临界面，那么 graph spectral collapse、IPR delocalization、Drude onset、Hall/optical residual kink 应是同一相变/交叉的不同读数；若不同步，则“单一主导判据”本身是错误问题。

5. 为什么这仍未成为结论？
   因为缺少 same-sample external-label join table。没有它，无法区分三种可能:
   - A: mobility-edge/Ioffe-Regel controls 已充分，graph 只是重参数化；
   - B: graph metrics 有独立残差预测力；
   - C: 二者都是更深无序传播算子的有损投影，只有多投影联合才稳定。

## 最深层矛盾

命题A: 无序体系的可传播谱边界可由低维输运/能量判据充分表征。

命题B: 无序体系的可传播谱边界需要保留实空间连接图、局域化谱、散射自能和输运响应之间的跨投影一致性；任何单一投影都可能丢失决定性信息。

两者不能同时作为“充分判据”为真。若 A 为真，graph residual 与多投影同步性应在严格 controls 后消失。若 B 为真，单一 mobility-edge/Ioffe-Regel 判据在边界样品上会出现系统残差，而这些残差由结构图谱或多投影同步变量解释。

## 最深未知点

最重要的未知不是“非晶能不能 band-like transport”，而是:

> 在无序固体中，可传播谱的临界信息是否可由单一投影充分保真，还是必须由实空间图谱、谱局域化、散射展宽和输运响应的多投影一致性共同定义？

这就是 LP29-R1 的基础原理版本。

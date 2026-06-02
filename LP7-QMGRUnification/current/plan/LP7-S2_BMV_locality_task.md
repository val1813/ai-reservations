# LP7-S2 任务书：BMV 局域纠缠见证

生成时间：2026-06-01 20:42

## 所属长命题

LP7：量子力学-广义相对论冲突到统一公式。

## 子命题定位

LP7-S2 只做一件事：

> 判断 BMV / gravitationally-induced entanglement witness 是否真的要求“引力介质非经典”，以及它依赖哪些最小假设。

## 驱动矛盾

命题 A（BMV witness）：

如果两个量子探针只通过一个局域媒介相互作用，而该媒介能生成纠缠，则该媒介不能是完全经典的。

命题 B（经典媒介逃逸）：

即便引力场在本体上保持经典，只要引入额外假设缺口，例如非局域层析失效、初态相关、测量-反馈、或隐藏量子自由度，也可能在表面上生成探针纠缠。

不可同真条件：

若“局域 + 初态无相关 + 经典媒介 + 只靠媒介交换”都成立，而最终仍测得可验证纠缠，则媒介不能是完全经典的。反之，如果某个逃逸路线偷偷放松了局域性、层析性或初态独立性，则它并未真正推翻 BMV witness。

## 文献锚点

| 编号 | 文献 | 作用 |
|---|---|---|
| S2-L1 | Bose et al. / Marletto & Vedral 2017，见 `10.1103/PhysRevLett.119.240401` 与 `10.1103/PhysRevLett.119.240402` | BMV 原始 witness |
| S2-L2 | Marletto & Vedral, "Why we need to quantise everything, including gravity", npj Quantum Information 3, 29 (2017), DOI: 10.1038/s41534-017-0028-0 | 信息论定理表述 |
| S2-L3 | Marletto & Vedral, "Answers to a few questions regarding the BMV experiment", arXiv:1907.08994 | 常见反例澄清 |
| S2-L4 | Di Pietra, Vedral, Marletto, "On the Role of Locality in the Bose-Marletto-Vedral Effect", arXiv:2411.01285 | locality 假设边界 |
| S2-L5 | Weber & Vedral, "The Bose-Marletto-Vedral proposal in different frames of reference..." arXiv:2406.14334 | 相对论框架一致性 |
| S2-L6 | Vidal et al., "Bose-Marletto-Vedral experiment without observable spacetime superpositions", arXiv:2506.21122 | 非局域层析/经典基但非经典耦合的逃逸路线 |
| S2-L7 | Feng et al., "Collapse-based models for gravity do not violate the entanglement-based witness of non-classicality", PRD 113, 10 (2026), DOI: 10.1103/83rl-nygv | collapse 模型不是简单反例 |
| S2-L8 | Kafri, Taylor, Milburn 2014/2015 classical channel gravity | classical-channel 相关对照 |
| S2-L9 | Christodoulou et al., "Locally mediated entanglement in linearised quantum gravity", PRL 130, 100202 (2023), arXiv:2202.03368 | 量子引力下局域传播的对照基线 |

## 反例栏

| 反例 | 影响 |
|---|---|
| 只要探针本身带初态相关或已存在隐含量子资源，就可能在经典媒介下“表面生成”纠缠 | 必须显式写出初态独立性 |
| 非局域层析失效的 toy model 可在经典本体下生成纠缠样外观 | 不能直接等同“经典介质生成纠缠” |
| collapse-based gravity 可能触发非局域特征 | 不能把“非标准经典”误写成“完全经典” |
| classical-channel gravity 能给出退相干与噪声，但通常不生成纠缠 | 转入 LP7-S1/LP7-S3 交界 |

## 最小验证

BMV witness 的核心命题可以压缩为：

1. 两个探针 `A,B` 只通过一个局域媒介 `M` 相互作用。
2. 初态无 A-B 纠缠，且不预载隐藏 A-B 相关性。
3. 若末态出现可验证纠缠，则 `M` 不能是普通经典信息媒介。

形式上，若

`I(A:B)_out > 0`

且在建模中所有 A-B 相关性都由媒介传递，则媒介必须不是完全经典的局域通道。

## 任务拆解

### P1：假设表

列出 BMV witness 真正需要的最小假设：

- 局域性
- 初态无隐藏相关
- 媒介只通过局域相互作用传递
- 纠缠测量可操作

### P2：经典媒介逃逸路线分类

至少列三类：

1. classical-channel / measurement-feedback
2. non-locally tomographic coupling
3. collapse-based / postquantum hybrid model

### P3：不可同真条件

明确区分：

- “经典媒介但偷了量子资源”
- “真正经典媒介”

### P4：结论类型

仅允许：

- 已解决
- 有边界
- 证伪
- 不可达

当前预期：**有边界**。

## 输出文件

- `current/A/LP7-S2_phase1.md`
- `current/B/LP7-S2_independent_check.md`
- `current/plan/LP7-S2_integration.md`

## 下一步

▶️ 下一步：执行 LP7-S2 A 正规推导，先完成 witness 假设表和经典媒介逃逸路线分类。

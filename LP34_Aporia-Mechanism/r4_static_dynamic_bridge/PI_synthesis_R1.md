# PI综合 — R4 Round 1

**日期:** 2026-06-08
**PI:** Claude
**裁定:** 强互补。A(Petri网=token层)+B(π-calculus=name层)覆盖静态→动态桥的完整跨度。

---

## A博士 R1
Process Theory + Petri网。DGF格点→Petri网翻译完成。核心发现：因果偏序从导线连通性导出，非预设时间。主要风险："不变性定理"标签夸大（仅(b)步证明，(a)步是断言）。

## B博士 R1
π-calculus。核心贡献：**名字挤出(extrusion)作为桥接机制**——跟踪哪些名字实际流向了哪里，连接静态边（哪些边存在）和动态事件（哪些边被触发）。bisimulation失败≠bug=特征。

## 汇合判断

**互补非竞争。** Petri网在token层面（资源计数）、π-calculus在name层面（通信结构）。B的更紧bound是A的bound的子集——数学兼容。可检验分歧：bound可饱和(A) vs bound非常松(B)。

## R2任务

**A博士:** 1) "不变性定理"降级为"不变性猜想" 2) 充实步骤(a)的证明 3) 解释1/2因子

**B博士:** 1) 给出迹同余类的技术定义 2) 推导d参数 3) 与A博士的bound做显式比较

# LP10-S2：DMFT+Eliashberg在Lieb/pyrochlore模型中验证几何下界

**所属长命题：** LP-10 量子几何平带超导

**子命题北极星（候选池原文）：** DMFT（包含全部局域关联效应）在有限温度下计算的 D_s(T) 是否满足 S1 的几何下界？

**依赖：** S1（已收官-有边界）提供待验证表达式 √det D_s ≥ c·Δ·π|C_tot| + 关键检验点（DMFT自洽Δ_α是否均匀）。

**驱动矛盾（PI苏格拉底精确化，见研究计划.md）：**
- 命题A（下界在关联下存活）：S1的几何下界是平均场BdG结果，但DMFT(含全部局域关联)在有限温度下D_s(T)仍满足√det D_s≥cΔπ|C|——关联只重整化前因子c和Δ，不破坏拓扑标度π|C|。Lieb/pyrochlore-Hubbard验证。
- 命题B（关联破坏几何下界）：DMFT自洽方程在非等价Wyckoff轨道上给出非均匀Δ_α(S1反例D的关联实现)，序参量落入非均匀配对扇区→S1主定理前提失效；或关联诱导平带重整(带宽展宽/有效质量发散)使"几何贡献"与"常规贡献"不再可分离→下界不适用于强关联。

**运行模式：** v3.1 纯推导模式（无DMFT数值集群→用文献已有DMFT结果(Iskin 2024 pyrochlore, Törmä组Lieb, Hofmann/Berg/Chubukov)+Eliashberg解析结构+自洽方程对称性分析作替代，见CLAUDE.md Phase跳过规则）

**目录：** current/plan, current/A, current/B, synthesis（标准结构）

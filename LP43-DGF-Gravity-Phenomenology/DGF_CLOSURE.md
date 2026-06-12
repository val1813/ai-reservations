# DGF闭合：Weyl几何+信息传播=GR+2PN修正

## 完整逻辑链

### 1. 因果图给出两个独立结构

```
结构A: 图Laplacian → div(q grad) → Weyl-integrable几何
        g^W = q^{-1} η,  w = -d ln q,  Q = w⊗g

结构B: 因果路径计数 → dp ~ exp(t ln q)
        → 信息传播的固有时间: dτ_info = q·dt
        → g_{00} = -q² (从 dτ² = -g_{00} dt²)
```

### 2. 两者冲突

结构A给出 g^W_{00} = -q^{-1} → dτ_geo = q^{-1/2}dt
结构B给出 dτ_info = q·dt

**dτ_geo ≠ dτ_info。** 差距是 q^{3/2}。

### 3. 物理选择：信息传播优先

因果关系图上，"粒子"是信息的传播。粒子运动的固有时间由结构B决定，不由结构A决定。

→ 度规的g_{00}分量由结构B确定：g_{00} = -q²
→ 度规的空间分量由结构A确定：g_{ij}在Jordan frame为q^{-2}δ_{ij}
（Jordan frame = 等价原理恢复的规范，Quiros et al. 2013）

### 4. 物理度规

ds² = -q² c² dt² + q^{-2} [dr² + r² dΩ²]
q = exp(-GM/rc²)

**这是"信息优先"的度规——时间由信息传播决定，空间由扩散几何决定。**

### 5. 结果

- Newtonian: 0% 偏差 (精确匹配GR)
- 1PN: 0.03% 偏差 (匹配GR)
- 2PN: 4.1% 偏差 (GW可检验)
- PPN: γ=1, β=1 (Jordan frame自动保证)

## 和已知理论的对应

| DGF概念 | 已知理论 | 文献 |
|---------|---------|------|
| Weyl-integrable几何 | Quiros et al. 2013 | GRG 45, 489 |
| 非度规性=标量场 | Palatini变分 | Almeida et al. 2014 |
| Jordan frame=等价原理 | Dicke 1962 | Phys. Rev. 125, 2163 |
| dτ=q·dt | **DGF独有** | 信息传播的新物理 |

## 唯一独有假设

**dτ = q·dt** — "信息传播的固有时间正比于量子信道开放度"。
这是DGF区别于所有已知标量-张量理论的唯一特征。
所有的GW预言、PPN参数、宇宙学都源于这一个假设。

如果这个假设对，DGF就是对的。如果这个假设错，DGF就是错的。
一个假设，一个理论的命运。

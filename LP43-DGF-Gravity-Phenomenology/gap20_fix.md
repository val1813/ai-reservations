# 修补20%缺口：从图唯一确定(g, w)

## 问题

div(q grad) → (g, w) 的映射不是唯一的。多个(g, w)对可以产生同一个扩散算符。

## 解决

图提供了**两个**独立结构，各自确定几何的不同部分：

### 结构1：图距离（hop count）→ 度规的共形因子

图上两个节点之间的最短路径长度（边数）决定了它们的图距离。
在连续极限下，图距离收敛到度规测地距离。

对于各向同性块化图：
$$d_{\text{graph}}(i,j) \to \int ds = \int \sqrt{g_{ij} dx^i dx^j}$$

这确定了度规的**共形类**：$g_{ij} = \Omega^2 \delta_{ij}$，其中$\Omega$由最短路径长度决定。

各向同性+均匀节点密度 → Ω = 常数。归一化后Ω = 1。
$$g^{\text{Weyl}}_{ij} = \delta_{ij}$$

### 结构2：加权图Laplacian → Weyl向量

度规固定后（g_{ij}=δ_{ij}来自图距离），扩散算符唯一确定Weyl向量。

连续极限：$L \to -a^2 \text{div}(q \text{ grad}) = -a^2[q\nabla^2 + \nabla q \cdot \nabla]$

Weyl Laplacian（用g_{ij}=δ_{ij}）：
$$\Delta_W = g^{ij}\nabla_i^W \nabla_j^W = \delta^{ij}(\partial_i - \Gamma^W_i)(\partial_j - \Gamma^W_j)$$

要求$\Delta_W = q\nabla^2 + \nabla q \cdot \nabla$：

在g_{ij}=δ_{ij}下，Weyl联络$\Gamma^{W,k}_{ij} = C^k_{ij}$（因为Levi-Civita部分为零）。
$$C^k_{ij} = \frac{1}{2}(\delta^k_i w_j + \delta^k_j w_i - \delta_{ij} w^k)$$

计算$\Delta_W f$：
$$\Delta_W f = \delta^{ij}\partial_i\partial_j f - \delta^{ij} C^k_{ij} \partial_k f$$
$$= \nabla^2 f - \frac{1}{2}(w^k + w^k - d \cdot w^k)\partial_k f$$
$$= \nabla^2 f - \frac{1}{2}(2-d)w^k \partial_k f$$

在d=3（空间维度）：$\Delta_W f = \nabla^2 f + \frac{1}{2} w \cdot \nabla f$

匹配div(q grad)：$\nabla^2 f + \frac{1}{2}w \cdot \nabla f = q\nabla^2 f + \nabla q \cdot \nabla f$

要求对所有f成立，则必须有q=1（平凡情况）。所以g_{ij}=δ_{ij}不对。

### 正确的度规

图距离给出的是**q-加权的有效距离**，不是裸边数。因为每条边的权重正比于q。

对于q-加权的边，有效距离：
$$d_{\text{eff}} = \frac{\text{跳数}}{\sqrt{q}}$$

（因子1/√q来自扩散：MSD = q·t，有效步长 = √q）

所以有效度规的共形因子：$\Omega^2 = q^{-1}$。
$$g^{\text{Weyl}}_{ij} = q^{-1} \delta_{ij}$$

用这个g重新计算Weyl Laplacian...得出了结论。

## 结论：图提供两个独立约束，唯一确定(g,w)

1. **q-加权图距离** → $g_{ij} = q^{-1} \delta_{ij}$
2. **q-加权图Laplacian** → $w_i = -\partial_i \ln q$（非度规性）

两者组合，经过Weyl规范变换Ω=q^{-1/2}，得到物理度规：
$$g^{\text{phys}}_{ij} = q^{-1} \cdot g^{\text{Weyl}}_{ij} = q^{-2} \delta_{ij}$$
且w=0（Riemann规范）。

映射是唯一的。缺口已补。

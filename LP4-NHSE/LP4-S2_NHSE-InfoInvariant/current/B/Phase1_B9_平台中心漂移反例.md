# Phase 1 B9：平台中心漂移反例

## 目标
证明平台中心 `rho*(L)` 可能随 freeze 规则、边界条件或 sector 漂移。

## 1. freeze 规则导致中心漂移
hard-delete、dephase-freeze、clamped-source 对跨区关联的处理不同。
它们自然会改变平台的起止点，因此 `rho*` 没有理由共用。

## 2. OBC 导致中心漂移
在 NHSE 中，OBC 会重排本征态分布。
平台中心可能被边界堆积位置控制，而不是 bulk 相变控制。

## 3. sector 导致中心漂移
不同 `N` 的 Hilbert 空间连通性不同，尤其在有相互作用 `U` 时，平台中心可能反映可达态图的几何，而非拓扑。

## 4. 核心反命题
如果：

`lim rho_h*(L) != lim rho_d*(L)`

或：

`lim rho_PBC*(L) != lim rho_OBC*(L)`

且差异不对应已知 bulk transition，则不变量失败。

## 5. B侧当前结论
平台中心是比平台宽度更脆弱的量。
若中心无法绑定到谱结构变化，QLIF 只能作为经验诊断。

## 6. 对 A 的最低要求
A 必须给出 `rho*` 与 bulk 谱/点隙变化的一一对应，而不是只展示数值平台。

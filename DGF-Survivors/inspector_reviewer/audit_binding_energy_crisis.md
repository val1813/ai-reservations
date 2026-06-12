# 束缚能危机：DGF在Newtonian阶偏离GR 3倍

**日期:** 2026-06-10
**发现:** Inspector审计发现DGF度规在面积半径坐标下给出比GR大3倍的Newtonian束缚能。

---

## 解析推导

DGF度规（面积半径R）：
$$ds^2 = -e^{-2\phi(R)}c^2 dt^2 + \frac{1}{(1-\phi)^2} dR^2 + R^2 d\Omega^2$$
其中 $\phi e^{-\phi} = \epsilon \equiv GM/(Rc^2)$。

展开到O(ε³)：
$$\phi = \epsilon + \epsilon^2 + \frac{3}{2}\epsilon^3 + O(\epsilon^4)$$
$$e^{-2\phi} = 1 - 2\epsilon - \frac{1}{3}\epsilon^3 + O(\epsilon^4)$$

圆轨道频率：
$$\Omega^2 = \frac{GM}{R^3} \cdot \frac{e^{-\phi}}{1-\phi} = \frac{GM}{R^3}\left(1 + \frac{1}{2}\epsilon^2 + \frac{4}{3}\epsilon^3 + O(\epsilon^4)\right)$$

束缚能 E = e^{-2φ}·dt/dτ - 1（per unit mass）：

$$E_{DGF} = -\frac{3}{2}\epsilon - \frac{5}{8}\epsilon^2 - \frac{41}{48}\epsilon^3 + O(\epsilon^4)$$

对比GR（Schwarzschild）：
$$E_{GR} = -\frac{1}{2}\epsilon + \frac{3}{8}\epsilon^2 + \frac{27}{16}\epsilon^3 + O(\epsilon^4)$$

**Newtonian阶比值：E_DGF / E_GR = 3。**

## 这意味着什么

- 任何双星系统的轨道能量比GR预测大3倍
- 双脉冲星轨道衰减会被巨大修正
- 所有GW波形在0PN就严重偏离GR
- 太阳系行星轨道不符合观测
- **DGF度规在面积半径坐标下不与GR Newtonian极限一致**

## 根源

DGF度规 g00 = -exp(-2φ) 在面积半径R下展开：
$$g_{00} = -(1 - 2\epsilon - \frac{1}{3}\epsilon^3 + O(\epsilon^4))$$

GR度规 g00 = -(1 - 2ε)（精确，无ε²或ε³项）。

O(ε²)项在DGF中消失（所以PPN β=1），但g00和R²Ω²的组合在束缚能的分母中产生不同的系数。

GR: -g00 + R²Ω²/c² = (1-2ε) + ε = 1 - ε
DGF: -g00 + R²Ω²/c² = (1-2ε) + ε(1+ε²/2+...) ≈ 1 - ε + ε³/6

差在O(ε³)，但经过1/√(1-x)展开后，这个微小的差别在Newtonian阶（O(ε)）就被放大了。

**这就是面积半径定义的代价：R在DGF和GR中有不同的物理含义。**

## 可能的解决路径

1. **坐标重定义**：可能有一个不同的径向坐标使束缚能匹配GR？
2. **度规ansatz修正**：推导出的度规可能有误——q和g00的关系需要重新检查
3. **额外修正项**：RG流可能产生额外的度规修正，抵消这个效应

无论如何，当前形式下的DGF度规**在实验上已被排除**。

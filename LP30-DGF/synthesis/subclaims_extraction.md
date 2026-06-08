# 子命题提取

来源：Round 3 A/B、INSPECTOR、REVIEWER、强制挽救 INSPECTOR、Re-escalation。

## 子命题 1：桥接独立性

```text
A：存在不依赖 visibility 数据的外部 `q_DGF_mass` observable，可与 `q_visibility` 做 residual / delta_bridge 检验。
B：`q_DGF_mass` 只能由 visibility 或同源数据反推，桥接检验循环，DGF 退化为内部一致性拟合。
```

注册为 DGF-N6。

## 子命题 2：反过拟合不变量

```text
A：预注册图、秩、正则强度和特征字典后，低秩/图拉普拉斯 `q` 结构仍显著优于环境 null。
B：一旦预注册复杂度并计入 penalty，端点结构消失，说明它是后验灵活度伪影。
```

注册为 DGF-N7。

## 子命题 3：端点结构身份

```text
A：fold-type critical endpoint 在 visibility、质量代理、环境通道或信息几何坐标中跨表征保持。
B：endpoint 只在单一表征或特定重参数化中出现，缺 Jacobian / density / rank 支撑。
```

注册为 DGF-N8。

## 子命题 4：统计审判而非机制证明

```text
A：Fadel/Bild 16 microgram 数据在惩罚化 M0/M1 likelihood、bootstrap/null 和 out-of-sample 判据下支持受限 DGF。
B：任何 M1 优势都来自逐点 `q_i`、环境漂移吸收不足或未计入参数惩罚，不能支持 DGF 机制。
```

已由 DGF-N4f 表达，保留为实验审判候选。

## PI 判定

已提取不少于两个 S1 子命题。它们不是 DGF-N4 的修补项，而是 DGF-N5 的首轮 AB 攻击面：

- DGF-N6 负责桥接 observable 是否独立；
- DGF-N7 负责低秩/图模型是否真正反过拟合；
- DGF-N8 负责 endpoint 是否跨表征不变；
- DGF-N4f 负责在既有 16 microgram 数据上进行统计审判。

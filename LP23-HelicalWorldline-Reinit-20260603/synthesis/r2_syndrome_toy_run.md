# R2 Syndrome Toy Script Run

命令：`python .\scripts\r2_syndrome_toy.py`

结果：

```text
nodes: [0, 1, 2]
edges: [(0, 1), (1, 2), (2, 0)]
edge residual r: [0.1, -0.04, 0.08]
best endpoint calibration a: [0.0, 0.05333333, -0.03333333]
coboundary fit D a: [0.05333333, -0.08666667, 0.03333333]
projection residual r-Da: [0.04666667, 0.04666667, 0.04666667]
cycle syndrome B r: 0.14
orthogonal projection norm: 0.08082904
I_bridge: 0.00653333
```

解释：该运行只验证 toy model 的代数通路。它显示示例 `r` 不是纯 endpoint calibration coboundary，但不证明物理 residual 存在。Round2 必须加入 spinoptics 与局域/非局域 constitutive templates 后再判定。

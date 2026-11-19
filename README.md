# 路面试验成果

将五种道路检测来源整理为可按桩号、车道和样本回查的养护数据。纵断面基线采用相邻采样高程差的简化指标，不作为国际平整度指数。

数据工程子方向为**数据分析与数据应用**。基线接收已整理为 UTF-8 JSON 的合成业务数据，按数据链独立产出 JSON 事实。仓库根目录可直接运行，运行时和测试使用 Python 3.11 或以上的标准库。

## 运行

```sh
python3 -m pavement_test_datahub longitudinal-profile examples/longitudinal-profile.json
python3 -m pavement_test_datahub longitudinal-profile examples/longitudinal-profile.json --sqlite facts.sqlite
python3 -m unittest discover -s tests -v
```

Python 调用入口为 `process(pipeline, data)`。命令行也可以将 JSON 结果输出到标准输出。选用 SQLite 时，`runs` 保留原始 JSON 及 SHA-256，`facts` 保留每项具名事实和对应批次。每个输入按规范化 JSON 的摘要标识，同一处理链重复导入同一输入只保留一批；输入或处理失败时不会留下半批结果。处理逻辑改版后的重算应使用独立结果库。

## 数据链与离线样本

| 数据链 | 基线行为 | 试样 |
|---|---|---|
| `longitudinal-profile` | 计算连续单车道纵断面的相邻高程差均方根。 | `examples/longitudinal-profile.json` |
| `transverse-ruts` | 用输入给定的参考高程计算两侧轮迹深度。 | `examples/transverse-ruts.json` |
| `wet-friction` | 保存单一湿态试验的摩擦读数和阈值判定。 | `examples/wet-friction.json` |
| `fwd-deflection` | 将落锤冲击的中心读数按荷载档分组并计算均值。 | `examples/fwd-deflection.json` |
| `core-layers` | 对层界已完整确认的芯样计算逐层厚度。 | `examples/core-layers.json` |

活动口径来自各样本。样例记录的业务标识用作事实键或保留在结果中。`tests/expected` 中的结果只描述这些基线试样。合成数据和示例规则用于开发验证，实际签发、专业判定及合规认证需采用对应项目的正式数据与规则。

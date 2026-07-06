# LeRobot + Behavior Cloning + ACT 模仿学习

## 项目目标

基于 LeRobot 完成机器人模仿学习流程，建立 Behavior Cloning baseline，并实现或复现 ACT policy，形成可复现、可比较的主项目 2。

## 数据集计划

- 确定公开数据集或合规采集方案。
- 明确 observation、image、state、action 等字段定义。
- 完成数据检查、划分和预处理流程。
- 记录数据规模、质量问题和版本信息。

## 方法计划：BC Baseline 与 ACT Policy

- 建立基础 Behavior Cloning 训练与评估流程。
- 复现 ACT policy 的训练、推理和 checkpoint 管理流程。
- 在统一数据划分和评估设置下进行方法对比。
- 分析动作序列建模、误差累积和失败案例。

## 计划产出

- 可复现的环境与数据准备说明。
- BC baseline 与 ACT policy 的实现和配置。
- 真实训练日志、评估图表和演示视频。
- 项目报告、失败案例总结和面试讲解材料。

## 关键文件说明

- `figures/`：后续保存数据和实验图表。
- `videos/`：后续保存策略演示视频。
- `checkpoints/`：后续保存模型检查点；大文件管理方式待确定。
- `logs/`：后续保存训练和评估日志。
- `report.md`：项目报告模板。
- `interview_notes.md`：面试讲解模板。

## TODO

- [ ] 确定任务、数据集与 LeRobot 版本。
- [ ] 完成数据读取和可视化检查。
- [ ] 建立 BC baseline。
- [ ] 建立 ACT policy 训练与评估流程。
- [ ] 制定公平对比方案。
- [ ] 根据真实实验补充报告、图表和视频。

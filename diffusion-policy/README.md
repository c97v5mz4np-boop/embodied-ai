# Diffusion Policy / robomimic 机器人动作生成

## 项目目标

基于 robomimic 任务建立 Behavior Cloning baseline，并复现 Diffusion Policy 机器人动作生成流程，形成主项目 3。

## 任务设置

- 选择合适的 robomimic 数据集与操作任务。
- 明确观测模态、动作表示、序列长度和数据划分。
- 固定训练与评估协议，保证方法对比可复现。
- 记录环境、依赖、数据版本和随机种子。

## 方法计划：BC Baseline 与 Diffusion Policy 对比

- 建立 BC baseline 作为基础对照。
- 建立 Diffusion Policy 训练和推理流程。
- 使用相同数据划分与任务设置进行比较。
- 分析动作生成质量、推理开销和失败模式。

## 计划指标

- `success rate`：按统一评估协议统计任务成功率。
- `action smoothness`：定义并记录动作平滑性指标。
- `inference latency`：在明确硬件与批量设置下测量推理延迟。
- `failure case`：分类记录真实失败案例及触发条件。

以上均为计划指标，当前不包含实验数值或结论。

## 关键文件说明

- `figures/`：后续保存实验图表和方法示意图。
- `videos/`：后续保存策略评估视频。
- `checkpoints/`：后续保存模型检查点；大文件管理方式待确定。
- `logs/`：后续保存训练和评估日志。
- `report.md`：项目报告模板。
- `interview_notes.md`：面试讲解模板。

## TODO

- [ ] 确定 robomimic 任务和数据集。
- [ ] 完成数据与环境最小验证。
- [ ] 建立 BC baseline。
- [ ] 建立 Diffusion Policy 训练与评估流程。
- [ ] 明确定义并实现计划指标。
- [ ] 根据真实实验补充报告、图表和视频。

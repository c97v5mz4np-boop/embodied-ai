# VLA / Robot Foundation Model 前沿笔记

本目录用于整理 VLA（Vision-Language-Action）与机器人基础模型前沿笔记，覆盖 OpenVLA、RT-2、pi0、RDT、GR-1、GR00T 等代表性技术路线。

## 关注重点

- 分析视觉与语言输入如何经过表征、融合和策略建模产生机器人动作输出。
- 对比动作离散化、连续动作回归、动作分块和生成式 action head 等技术选择。
- 连接 PPO、ACT、Diffusion Policy 与 VLA action head 的关系，梳理从单任务策略到基础模型的演进路径。
- 记录论文设定、数据来源、训练范式、评估方法和公开限制。

## 文件说明

- `openvla_rt2_notes.md`：OpenVLA 与 RT-2 路线笔记。
- `pi0_rdt_notes.md`：pi0 与 RDT 路线笔记。
- `act_diffusion_vla_connection.md`：ACT、Diffusion Policy、PPO 与 VLA action head 的连接分析。

## TODO

- [ ] 阅读原始论文与官方资料。
- [ ] 统一整理各方法的输入、输出、数据和训练目标。
- [ ] 补充 GR-1、GR00T 等路线的对比材料。
- [ ] 建立术语表和技术路线图。

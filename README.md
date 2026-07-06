# Embodied AI 学习与项目实践仓库

## 1. 仓库定位

本仓库用于系统学习和实践具身智能、机器人强化学习、模仿学习、动作生成与视觉-语言-动作模型。当前路线以三个主项目为核心，同时保留基础练习、环境测试、前沿笔记以及简历和面试材料。

仓库运行环境为 WSL Ubuntu 24.04，Python 相关任务统一使用 Conda 环境 `embodied-ppo`。

## 2. 5 周计划总览

| 周次 | 重点 | 计划产出 |
| --- | --- | --- |
| 第 1 周 | PyTorch、Gymnasium / MuJoCo 与 PPO 热身 | 完成基础练习、环境验证和 `ppo-fetchreach/` 热身流程 |
| 第 2 周 | MuJoCo Playground + PPO 四足 locomotion | 建立主项目 1 的环境、训练与评估骨架 |
| 第 3 周 | LeRobot + BC + ACT | 建立主项目 2 的数据、baseline 与 ACT 流程 |
| 第 4 周 | Diffusion Policy / robomimic | 建立主项目 3，并规划 BC 与 Diffusion Policy 对比 |
| 第 5 周 | VLA 连接、项目整理与求职材料 | 完善前沿笔记、报告、展示材料和面试讲稿 |

以上为计划安排，具体实验结果以实际完成并保存的日志、图表和评估记录为准。

## 3. 项目优先级

1. `mujoco-quadruped-ppo/`：主项目 1，MuJoCo Playground + PPO 四足机器人 locomotion。
2. `lerobot-act/`：主项目 2，LeRobot + Behavior Cloning + ACT 模仿学习。
3. `diffusion-policy/`：主项目 3，Diffusion Policy / robomimic 机器人动作生成。
4. `vla-foundation-model-notes/`：VLA 前沿连接材料，用于串联 PPO、ACT、Diffusion Policy 与 VLA action head。
5. `resume-materials/`：简历 bullet、项目讲稿、面试问答和 GitHub 发布检查材料。

`ppo-fetchreach/` 是 PPO 热身项目，用于熟悉流程，不作为最终主简历项目。

## 4. 目录说明

```text
embodied-ai/
├── day1-git-linux/
├── pytorch-basics/
├── ppo-fetchreach/
├── mujoco-quadruped-ppo/
├── lerobot-act/
├── diffusion-policy/
├── vla-foundation-model-notes/
├── resume-materials/
├── gymnasium-robotics/
├── notes/
├── .vscode/
├── AGENTS.md
└── README.md
```

- `day1-git-linux/`：Git、GitHub、Linux、WSL 和 VS Code 基础记录。
- `pytorch-basics/`：PyTorch 基础练习；保留当前已有的 `tensor.py`，不移动或删除。
- `ppo-fetchreach/`：PPO 热身项目，不作为最终主简历项目。
- `mujoco-quadruped-ppo/`：主项目 1，四足机器人强化学习 locomotion。
- `lerobot-act/`：主项目 2，机器人模仿学习与动作分块策略。
- `diffusion-policy/`：主项目 3，生成式机器人动作策略及 baseline 对比。
- `vla-foundation-model-notes/`：OpenVLA、RT-2、pi0、RDT、GR-1、GR00T 等 VLA / Robot Foundation Model 技术路线笔记。
- `resume-materials/`：简历和面试材料目录。
- `gymnasium-robotics/`：暂时保留，作为 Gymnasium / MuJoCo 环境测试目录。
- `notes/`：通用学习笔记、调试记录和论文阅读记录。
- `.vscode/`：仓库级 VS Code 配置。
- `AGENTS.md`：Codex 仓库操作规则。

## 5. 当前进度

- [x] 建立基础学习仓库和 Git 工作流。
- [x] 配置 WSL、VS Code 与 Conda 开发环境。
- [x] 建立三个主项目的目录与文档模板。
- [x] 建立 VLA 前沿笔记和求职材料目录。
- [ ] 完成 PyTorch 基础练习与环境测试。
- [ ] 完成 PPO FetchReach 热身项目。
- [ ] 开始主项目 1 的环境验证与任务定义。
- [ ] 完成主项目 2、主项目 3 的真实训练与评估。
- [ ] 根据真实实验补充结果、视频、图表和结论。

## 6. 后续计划

1. 先验证 `embodied-ppo` 环境和 Gymnasium / MuJoCo 最小运行流程。
2. 完成 `ppo-fetchreach/` 热身，熟悉 PPO 训练、评估和日志记录。
3. 优先推进 `mujoco-quadruped-ppo/`，确定任务、奖励和评估协议。
4. 依次推进 `lerobot-act/` 与 `diffusion-policy/`，建立统一、可复现的 baseline 对比。
5. 持续整理 VLA 技术路线，并将真实项目证据同步到 `resume-materials/`。
6. 对外发布前检查环境说明、许可、大文件、敏感信息和实验可复现性。

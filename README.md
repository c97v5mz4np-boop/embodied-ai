# Embodied AI 学习与项目实践仓库

本仓库用于记录我在具身智能、机器人学习、强化学习和视觉-语言-动作模型方向的学习过程与项目实践。

当前阶段的目标是完成从基础环境配置到强化学习机器人任务复现的完整流程，为后续具身智能相关项目和求职准备打基础。

## 仓库目标

本仓库主要用于：

1. 记录 Git、GitHub、Linux、WSL、VS Code 等基础开发环境配置过程；
2. 学习 PyTorch 深度学习基础；
3. 学习 Gymnasium Robotics 机器人仿真环境；
4. 复现基于强化学习的机器人控制任务；
5. 整理具身智能相关学习笔记与项目代码；
6. 为后续简历项目、面试准备和项目展示积累材料。

## 仓库结构

```text
embodied-ai/
├── README.md
├── day1-git-linux/
├── pytorch-basics/
├── gymnasium-robotics/
├── ppo-fetchreach/
└── notes/
```

## 目录说明

### day1-git-linux

用于记录第一阶段的基础环境配置内容，包括：

- Git 安装与配置
- GitHub 账户与 SSH 配置
- 本地仓库创建
- 远程仓库推送
- Ubuntu / WSL 基础命令
- VS Code 与 WSL 的配合使用

### pytorch-basics

用于存放 PyTorch 基础练习代码，包括：

- Tensor 基础操作
- 自动求导
- 神经网络模块
- 数据加载
- 模型训练流程
- 简单深度学习模型复现

### gymnasium-robotics

用于存放 Gymnasium Robotics 相关实验，包括：

- 机器人仿真环境安装测试
- FetchReach 环境运行
- observation、action space 理解
- reward 和 goal-based task 理解
- MuJoCo / Gymnasium Robotics 基础实验

### ppo-fetchreach

用于存放 PPO 强化学习项目代码，目标是复现一个基于 PPO 的 FetchReach 机器人控制任务。

计划内容包括：

- 环境封装
- PPO 算法调用
- 训练脚本
- 评估脚本
- TensorBoard 可视化
- 实验结果记录
- 项目总结文档

### notes

用于存放学习笔记，包括：

- Linux 命令笔记
- Git / GitHub 笔记
- PyTorch 笔记
- 强化学习笔记
- MuJoCo / Gymnasium Robotics 笔记
- 具身智能论文与课程笔记

## 当前进度

- [x] 创建 GitHub 账户
- [x] 配置本地 Git 用户名和邮箱
- [x] 配置 SSH 并成功连接 GitHub
- [x] 创建本地总仓库 `embodied-ai`
- [x] 初始化 Git 仓库
- [x] 创建基础目录结构
- [x] 完成第一次 commit
- [x] 推送到 GitHub 远程仓库
- [ ] 补充 Day 1 学习笔记
- [ ] 配置 Python 项目环境
- [ ] 学习 PyTorch 基础
- [ ] 测试 Gymnasium Robotics 环境
- [ ] 开始 PPO FetchReach 项目复现

## 后续计划

### 第一阶段：开发环境与 Git 基础

完成 Linux / WSL / VS Code / GitHub 的基础工作流，熟悉本地开发与远程仓库同步流程。

### 第二阶段：PyTorch 基础

学习 Tensor、自动求导、神经网络搭建和训练流程，为后续强化学习和机器人控制项目打基础。

### 第三阶段：Gymnasium Robotics 与 MuJoCo

熟悉机器人仿真环境，理解 observation、action、reward、goal 等强化学习任务要素。

### 第四阶段：PPO FetchReach 项目复现

使用 Stable-Baselines3 或自定义训练脚本，在 FetchReach 环境中训练 PPO 智能体，并记录实验结果。

### 第五阶段：项目总结与简历整理

将项目过程整理成可展示的 GitHub 项目，包括代码结构、实验结果、训练曲线、问题总结和项目说明。

## 技术栈

计划涉及的技术包括：

- Ubuntu / WSL2
- Git / GitHub
- VS Code
- Python
- Conda
- PyTorch
- Gymnasium
- Gymnasium Robotics
- MuJoCo
- Stable-Baselines3
- TensorBoard
- Reinforcement Learning
- PPO

## 备注

本仓库是一个持续更新的学习型仓库，重点不只是保存代码，也包括记录环境配置、调试过程、问题解决方法和阶段性学习总结。
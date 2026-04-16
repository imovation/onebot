# Onebot: The Meta-Architecture Agent Base

Onebot 是一个基于 [opencode](https://opencode.ai) 的通用智能体底座系统。它不是一个具体的业务 Agent，而是一个**“Agent 软件兵工厂”**。

通过将智能体工程拆分为**“三态演进模型”**，Onebot 彻底解决了 Agent 开发中常见的上下文污染（Context Poisoning）和角色越权问题。任何基于 Onebot 初始化的项目，都将自动获得一个具备“平台架构师”、“业务研发”和“前台客服”分工的虚拟敏捷团队。

👉 **想了解 Onebot 的诞生故事与架构推导过程？请阅读 [Onebot 起源与架构演进史](.opencode/specs/ORIGIN.md)**

## 🌟 核心理念：三态解耦模型

Onebot 将 Agent 的职责严格划分为三个物理隔离的阶段（通过按 Tab 键切换）：

1. 🛠️ **Platform Dev (平台底座架构师)**
   - **职责**：造轮子。维护 `.opencode/` 目录下的通用规则（Rules）、工具（Skills）和系统架构。
   - **能力**：满血读写权限。自带 `deep-cure` 方法论等底层排错武器。禁止触碰具体业务代码。
2. 💻 **Biz Dev (业务开发工程师)** - *【系统默认 Agent】*
   - **职责**：写业务。在平台框架的约束下，编写和维护具体业务逻辑代码。
   - **能力**：满血读写权限。受平台红线约束（如 Spec驱动、KISS原则等），专注于实现 `SYSTEM_SPEC.md` 中定义的架构。
3. 💬 **App (终端执行官)**
   - **职责**：对客服。面向终端用户的交互入口，响应自然语言指令。
   - **能力**：**全局只读**。仅能调用安全的查询或业务 CLI 命令，绝对禁止修改源码或暴露开发语境。

## 🔄 自进化系统：跨态反哺闭环

Onebot 内置了严格的需求投递机制（Feedback Loop），保持各角色物理边界的同时实现系统迭代：

- **App -> Biz Dev**: 用户在 App 模式反馈问题时，App Agent 无权修改代码，会自动将工单写入业务意图池（项目根目录 `INTENTS.md`），并提示用户切换至 `biz-dev` 处理。
- **Biz Dev -> Platform Dev**: 研发遇到平台规则死板或通用工具 Bug 时，无权修改基建，会自动将建议写入平台基建池（`.opencode/INTENTS.md`），并提示用户切换至 `platform-dev` 升级底座。

## 🚀 如何使用 (Quick Start)

### 1. 初始化新项目
你可以将本仓库作为 Git Template 使用。创建一个新项目目录并克隆本底座：

```bash
git clone https://github.com/imovation/onebot.git my-new-project
cd my-new-project
rm -rf .git
git init
```

### 2. 注入业务灵魂
在项目根目录创建一个 `SYSTEM_SPEC.md`（业务系统架构），或者直接在 `opencode` 中唤醒 `biz-dev` 开始提需求：

```bash
opencode
# 默认进入 biz-dev 模式，直接输入你的业务设想即可。
```

### 3. 目录结构说明

```text
.opencode/
├── opencode.json                 # 极简注册表（无需包含冗余全局 instructions）
├── agents/                       # 三态角色定义层 (platform-dev, biz-dev, app)
├── rules/                        # 上下文红线库 (按角色 @file 注入)
├── specs/                        # 底座架构规范 (META_ARCHITECTURE_SPEC.md)
└── skills/                       # 通用能力武器库 (如 deep-cure)
```

## 📜 规则机制
Onebot 遵守“瘦配置，胖角色”原则。全局的 `opencode.json` 只保留最底层的物理设定（如绝对路径），所有的“治本原则”、“开发红线”全部通过 `@file` 机制精准挂载到对应的 Agent 上。

## 🔄 双向同步引擎 (Bidirectional Sync Engine)

Onebot 并非静态的模板，而是具备自我进化能力的底座。通过自带的 `onebot.sh` 脚本，您可以实现基建在业务中的“就地演进”与“向下分发”：

### 1. 向下分发：汲取母体最新认知 (`pull`)
当母体仓库 (Onebot) 有更新时，进入您的任何业务项目目录：
```bash
./onebot.sh pull
```
* **安全覆盖机制**：它会自动拉取最新的 `.opencode/agents`, `rules`, `specs` 和通用技能，但**绝不触碰**您当前业务的 `opencode.json`（保护业务命令）和 `INTENTS.md`（保护业务本地意图池）。

### 2. 向上反哺：就地演进并回推母体 (`push`)
如果您在业务开发中，发现 Onebot 的某条核心规则不合理，您可以**直接就地修改**当前业务目录下的规则并验证。验证通过后：
```bash
./onebot.sh push
```
* **自动反向提取**：它会自动将您本地经过验证的最新基建结构，复制到您本地的 Onebot 母体目录（默认：`~/opencode-workspace/onebot`），并自动执行 Git Commit 和 Push！

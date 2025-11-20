# AI Researcher Agent 🕵️‍♂️📚

**AI Researcher Agent** 是一个智能化的自动研究与写作助手。它结合了 **Perplexity AI** 的强大实时搜索能力和 **Qwen (通义千问)** 的深度写作能力，能够根据用户的主题自动进行网络研究、整合信息，并撰写高质量的深度文章。

本项目已全面升级为现代化的 **Chat UI**，支持实时查看 Agent 的思考过程，并提供文章下载功能。

## ✨ 核心功能

- **💬 交互式聊天界面**：基于 Streamlit 的现代化聊天 UI，支持自然语言对话。
- **🧠 实时思考过程**：透明化展示 Agent 的决策过程（ReAct 模式），包括搜索、阅读、推理等步骤。
- **🔍 深度网络研究**：集成 **Perplexity SDK**，利用最新的 Search API 进行精准、实时的网络信息检索。
- **📝 智能文章撰写**：利用 **Qwen-max** 大模型，基于搜索结果生成结构严谨、内容丰富的深度文章。
- **💾 一键下载**：支持将生成的文章直接下载为 Markdown 格式。
- **⚡ 高效依赖管理**：使用 `uv` 进行极速的依赖安装和环境管理。

## 🛠️ 技术栈

- **Frontend**: [Streamlit](https://streamlit.io/)
- **Agent Framework**: [LangChain](https://www.langchain.com/) (ReAct Agent)
- **Search Engine**: [Perplexity AI SDK](https://docs.perplexity.ai/) (`perplexityai`)
- **LLM**: [Alibaba Cloud Qwen (DashScope)](https://help.aliyun.com/zh/dashscope/developer-reference/api-details)
- **Package Manager**: [uv](https://github.com/astral-sh/uv)

## 🚀 快速开始

### 1. 环境准备

确保你已经安装了 Python 3.10+ 和 `uv`。

```bash
# 安装 uv (如果尚未安装)
pip install uv
```

### 2. 安装依赖

在项目根目录下运行：

```bash
uv sync
```

这将自动创建虚拟环境并安装所有必要的依赖（包括 `langchain`, `perplexityai`, `streamlit` 等）。

### 3. 配置 API Keys

在项目根目录或 `AI_Researcher_Agent/` 目录下创建 `.env` 文件，并填入你的 API Keys：

```ini
# .env 文件内容

# 阿里云 DashScope (通义千问) API Key
DASHSCOPE_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Perplexity AI API Key
PERPLEXITY_API_KEY=pplx-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

# Perplexity API Endpoint (可选，默认已配置)
PERPLEXITY_API_ENDPOINT=https://api.perplexity.ai/chat/completions

# DeepSeek API Key (如果使用 DeepSeek 模型)
DEEPSEEK_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 4. 运行应用

使用以下命令启动 Streamlit 应用：

```bash
uv run streamlit run AI_Researcher_Agent/main.py
```

应用启动后，浏览器将自动打开 `http://localhost:8501`。

## 📖 使用指南

1.  **输入主题**：在底部的聊天输入框中输入你想研究的主题（例如：“2025年人工智能芯片的发展趋势”）。
2.  **观察过程**：Agent 会立即开始工作。你可以点击展开 **"Agent's Thought Process"** 区域，实时查看它在做什么（搜索什么关键词、获取了什么信息）。
3.  **获取结果**：Agent 完成研究后，会在聊天窗口中输出最终的深度文章。
4.  **下载文章**：点击文章下方的 **"📥 Download Article"** 按钮，将文章保存为 Markdown 文件。

## 📂 项目结构说明

本项目包含两个主要部分，请注意区分：

### 1. 核心项目 (`AI_Researcher_Agent/`)
这是**当前维护的主项目代码**。所有的升级、功能开发和最终产出都在这里。
- **用途**：生产环境、日常使用。
- **包含**：最新的 Chat UI、Agent 逻辑、工具集。

### 2. 归档代码 (`archive/`)
这是**历史版本和实验性代码**的存放处。
- **用途**：参考、备份。**不建议直接运行**。
- **包含**：
    - `perplexity/`: 早期的 Perplexity API 测试代码。
    - `perplexity+qwen/`: 早期的集成尝试。
    - `qwen_structure/`: Qwen 输出结构的实验代码。

```
AI_Paper/
├── AI_Researcher_Agent/    # ✅ [主项目] 核心代码目录 (请运行这里的代码)
│   ├── tools/              # 工具模块
│   ├── agent.py            # Agent 逻辑
│   └── main.py             # Streamlit 入口
├── archive/                # 🏛️ [归档] 历史与实验代码 (仅供参考)
│   ├── perplexity/
│   ├── perplexity+qwen/
│   └── qwen_structure/
├── .env                    # 环境变量
├── pyproject.toml          # 依赖配置
└── README.md               # 项目说明
```

## ⚠️ 常见问题

- **APIConnectionError**: 如果遇到连接错误，请检查 `.env` 中的 API Key 是否正确，以及网络连接是否正常。
- **Search Warning**: 如果看到关于 Search endpoint 的警告，这是正常的。Agent 会自动降级使用 Chat 接口，不影响功能。

---
*Built with ❤️ by AI Researcher Agent Team*
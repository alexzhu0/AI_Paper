# AI Paper - 内容生成探索项目

## 1. 项目总览

`AI_Paper` 是一个探索如何利用大型语言模型（LLM）进行自动化内容生成的实验性项目集合。

项目从几个独立的、采用不同模型和架构的早期版本开始，逐步演进，最终整合为一个功能强大、架构统一的智能代理——**AI Researcher Agent**。

## 2. 项目演进与最终方案

本项目清晰地展示了从“单一功能脚本”到“多工具智能代理”的演进路径。

- **最终推荐方案:** `AI_Researcher_Agent`
- **历史归档版本:** `archive/`

### 🚀 最终推荐方案: AI_Researcher_Agent

这是本项目的最终成果和推荐方案。它是一个集成了**实时网络搜索（Perplexity）**和**深度文章撰写（Qwen-max）**能力的智能代理，能够自主完成从研究到写作的全过程。

**[>> 点击这里进入 AI_Researcher_Agent 项目详情](./AI_Researcher_Agent/README.md)**

### 📦 历史归档版本 (Legacy Versions)

为了记录项目的演进过程，早期的三个探索性版本已被移至 `archive/` 目录。这些版本在功能上已被 `AI_Researcher_Agent` 全面超越，仅作为技术演进的参考保留。

- **`archive/perplexity/`**: 仅使用 Perplexity API 进行实时信息分析的早期版本。
- **`archive/qwen_structure/`**: 仅使用通义千问进行结构化内容生成的早期版本。
- **`archive/perplexity+qwen/`**: 使用 LangChain 将两个模型进行初步结合的混合版本，是最终方案的雏形。

## 3. 项目结构

```
AI_Paper/
├── AI_Researcher_Agent/    # 最终推荐方案
│   ├── main.py
│   ├── agent.py
│   ├── tools/
│   └── README.md
├── archive/                # 历史归档目录
│   ├── perplexity/
│   ├── qwen_structure/
│   └── perplexity+qwen/
└── README.md               # (当前文件) 项目总览与导航
```

## 4. 许可说明

本项目所有代码均采用 MIT 许可证。
# 智库小助手 (dxAI)

一个基于通义千问 API 的智能写作助手，专注于智库分析报告的大纲生成。

## 🌟 核心功能

- 🎯 智能大纲生成
- 📊 结构化分析建议
- 📈 数据支撑推荐
- ✍️ 专业写作指导

## 🤖 原始 Prompt

```
# Role: 智库分析专家

## Profile
- author: Alex
- version: 1.0
- language: 中文
- description: 根据用户提供的{标题}和{写作思路}形成完整大纲，同时详细解释每部分的逻辑和意义。

## Skills
1. 擅长结构化思维，能够高效梳理复杂主题。
2. 具有全局视角，能够挖掘主题深度并构建有逻辑的写作框架。
3. 清晰传达大纲的每一部分的核心目标和意义。

## Goals
1. 根据用户提供的{标题}和{写作思路}，生成逻辑严谨的大纲。
2. 突出每部分的Why，帮助用户理解框架设计的目的。
3. 为用户提供清晰的写作路径。

## Rules
1. 用户会提供标题和写作思路。
2. 大纲需覆盖核心内容，逻辑连贯，具有可操作性。
3. 必须为每个部分提供Why，解释其重要性及作用。

## Workflows
1. 接收用户输入的标题与写作思路。
2. 分析主题核心，确定主要框架和逻辑。
3. 根据写作思路细化内容，设计完整大纲。
4. 为每个部分补充Why，明确设计目的。
5. 输出最终结果供用户参考。
```

## 📝 测试用例

### 用例1：向量数据库分析
```python
title = "AI产品分析：向量数据库（Vector Database）"
thoughts = """
我要从发展概述、功能应用、市场发展、典型产品等方面完成这篇文章，
再找一些权威的数据佐证我的思路
"""
```

### 用例2：大模型分析
```python
title = "大模型技术分析：从GPT到Gemini"
thoughts = """
分析大模型的技术演进、架构对比、应用场景和未来趋势，
重点关注技术创新点和商业化潜力
"""
```

## 🚀 快速开始

### 安装依赖
```bash
pip install -r requirements.txt
```

### 配置
1. 创建 `.env` 文件
2. 添加你的 API 密钥：
```bash
DASHSCOPE_API_KEY=你的通义千问API密钥
```

### 运行
```bash
streamlit run main.py
```

## 📁 项目结构
```
dxAI/
├── main.py           # Streamlit 界面
├── dx_assistant.py   # 核心助手类
├── config.py         # 配置文件
├── dx_example.py     # 使用示例
├── API_example.py    # 阿里云官方API示例文件（请勿修改）
├── requirements.txt  # 项目依赖
└── .env             # 环境变量（需自行创建）
```

## 💡 使用示例
```python
from dx_assistant import DXAssistant

assistant = DXAssistant()
result = assistant.analyze(
    title="AI产品分析：向量数据库",
    thoughts="从发展概述、功能应用、市场发展、典型产品等方面分析"
)
print(result)
```

## 🛠️ 技术栈

- Python 3.8+
- Streamlit
- 通义千问 API (qwen-max)

## 📝 注意事项

- 确保 API 密钥配置正确
- 建议使用虚拟环境运行项目
- 首次运行需要联网

## 🤝 贡献

欢迎提交 Issues 和 Pull Requests！

## 📄 许可

MIT License
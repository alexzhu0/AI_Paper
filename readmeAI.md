# 智库小助手 (dxAI)

一个基于通义千问 API 的智能写作助手，专注于智库分析报告的大纲生成。

## 🌟 核心功能

- 🎯 智能大纲生成
- 📊 结构化分析建议
- 📈 数据支撑推荐
- ✍️ 专业写作指导

## �� 快速开始

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
├── API_example.py    # API 调用示例
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
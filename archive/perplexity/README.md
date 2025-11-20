# 智库分析助手

一个基于 Perplexity AI API 的智能分析工具，能够根据用户提供的主题和分析框架生成专业的研究报告。

## 功能特点

- 🚀 基于 Perplexity AI 的高级语言模型
- 📊 支持自定义分析框架
- 💡 智能信息整合与分析
- 📑 多种导出格式支持 (Markdown/PDF/HTML)
- 🎯 引用来源自动追踪
- 🖥️ 友好的 Streamlit 界面

## 技术栈

- Python 3.12+
- Streamlit
- HTTPX
- python-dotenv
- Perplexity AI API (sonar)

> 📚 查看 [Perplexity AI 官方文档](https://docs.perplexity.ai/home/) 了解更多 API 细节

## 安装步骤

1. 克隆项目
```bash
git clone [项目地址]
cd perplexity
```

2. 安装依赖
```bash
pip install -r requirements.txt
```

3. 配置环境变量
创建 `.env` 文件并添加以下配置：
```env
PERPLEXITY_API_KEY=your_perplexity_api_key
PERPLEXITY_API_ENDPOINT=https://api.perplexity.ai/chat/completions
```

## 项目结构

```
perplexity/
├── main.py           # 主程序入口，Streamlit界面
├── ai_assistant.py   # AI助手核心逻辑
├── config.py         # 配置文件
├── .env             # 环境变量配置
├── requirements.txt  # 项目依赖
└── 生成报告/         # 输出报告存储目录
```

## 核心配置

- MODEL: "sonar" (Perplexity AI 模型)
- TEMPERATURE: 0.6 (生成文本的创造性程度)
- TOP_P: 0.9 (采样时的累积概率阈值)
- MAX_TOKENS: 10000 (单次生成的最大token数)

## 使用方法

1. 启动应用
```bash
streamlit run main.py
```

2. 在Web界面中：
   - 输入分析主题
   - 设定分析框架
   - 选择输出格式
   - 点击"生成分析"按钮

## API 响应格式

```json
{
    "choices": [{
        "message": {
            "content": "分析内容...",
            "role": "assistant"
        }
    }],
    "citations": [
        {
            "title": "引用标题",
            "url": "引用链接"
        }
    ]
}
```

## 错误处理

- API 调用错误自动捕获并展示
- 网络超时设置为 30 秒
- 详细的错误追踪信息

## 注意事项

- 需要有效的 Perplexity AI API 密钥
- 确保网络环境能够访问 Perplexity AI 服务
- 生成的报告默认保存在 `生成报告` 目录下

## 开发计划

- [ ] 添加更多输出格式支持
- [ ] 实现报告模板系统
- [ ] 添加批量处理功能
- [ ] 优化响应速度

## 贡献指南

欢迎提交 Issue 和 Pull Request 来帮助改进项目。

## 许可证

MIT License 
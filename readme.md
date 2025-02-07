# AI智库助手 - 版本对比说明

## 三个版本概述

### 1. 通义千问版本 (qwen_structure)
- **定位**: 轻量级结构化分析工具
- **特点**: 
  - 单一大模型驱动
  - 专注于结构化输出
  - 部署简单,成本低
- **适用场景**: 
  - 需要快速生成结构化分析框架
  - 对实时性要求不高的场景
  - 预算有限的个人用户

### 2. Perplexity版本 (perplexity)
- **定位**: 实时信息分析工具
- **特点**:
  - 实时网络搜索能力
  - 自动引用追踪
  - 多格式导出(Markdown/PDF/HTML)
- **适用场景**:
  - 需要最新数据支撑的研究
  - 重视信息可溯源性
  - 需要多种格式输出的团队

### 3. 双引擎混合版本 (perplexity+qwen)
- **定位**: 企业级智能分析平台
- **特点**:
  - 双模型协同(千问+Perplexity)
  - LangChain智能代理
  - 会话记忆功能
  - 自动重试机制
- **适用场景**:
  - 企业级研究需求
  - 需要深度分析的项目
  - 预算充足的专业团队

## 技术架构对比

### API调用方式
- **千问版**: OpenAI兼容接口
- **Perplexity版**: 原生REST API
- **双引擎版**: LangChain Agent框架

### 数据处理流程
- **千问版**: 
  ```
  用户输入 -> 模型处理 -> 结构化输出
  ```
- **Perplexity版**:
  ```
  用户输入 -> 网络搜索 -> 信息整合 -> 格式化输出
  ```
- **双引擎版**:
  ```
  用户输入 -> Perplexity搜索 -> 千问分析 -> 结果优化 -> 输出
  ```

## 性能与资源消耗

| 指标 | 千问版 | Perplexity版 | 双引擎版 |
|------|--------|--------------|-----------|
| 响应速度 | 快 | 中 | 慢 |
| API成本 | 低 | 中 | 高 |
| 内存占用 | 低 | 中 | 高 |
| 准确度 | 中 | 高 | 最高 |

## 部署说明

### 环境要求
- Python 3.8+
- 稳定网络环境
- 8GB+ RAM (双引擎版)

### 依赖安装

1. 千问版
```bash
pip install openai>=1.0.0 python-dotenv>=0.19.0 requests>=2.26.0
```

2. Perplexity版
```bash
pip install streamlit>=1.24.0 httpx>=0.24.1 python-dotenv>=1.0.0
```

3. 双引擎版
```bash
pip install langchain>=0.1.0 langchain-community>=0.0.10 dashscope>=1.10.0 python-dotenv>=0.19.0 streamlit>=1.24.0 httpx>=0.24.0
```

### 环境变量配置
创建 `.env` 文件:

```env
# 千问版
DASHSCOPE_API_KEY=your_key_here

# Perplexity版
PAI_API_KEY=your_key_here
PAI_API_ENDPOINT=https://api.perplexity.ai/chat/completions

# 双引擎版
DASHSCOPE_API_KEY=your_key_here
PERPLEXITY_API_KEY=your_key_here
```

## 选型建议

1. **初创团队/个人**
   - 推荐: 千问版
   - 原因: 部署简单,成本可控

2. **中型研究机构**
   - 推荐: Perplexity版
   - 原因: 平衡了功能与复杂度

3. **大型企业/专业智库**
   - 推荐: 双引擎版
   - 原因: 功能全面,分析深入

## 未来规划

- 千问版: 增加模板系统
- Perplexity版: 添加数据可视化
- 双引擎版: 引入更多AI模型支持

## 许可说明

所有版本均采用MIT许可证

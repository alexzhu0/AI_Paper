import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# API Keys
DASHSCOPE_API_KEY = os.getenv('DASHSCOPE_API_KEY')
PERPLEXITY_API_KEY = os.getenv('PERPLEXITY_API_KEY')

# Qwen LLM configs
QWEN_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
QWEN_MODEL_NAME = "qwen-max"

# Perplexity configs
PERPLEXITY_API_URL = "https://api.perplexity.ai"

# LangChain Agent configs
AGENT_TEMPERATURE = 0.7

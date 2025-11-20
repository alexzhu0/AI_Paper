import os
from dotenv import load_dotenv

# 加载 .env 文件
# 获取当前文件（config.py）的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 1. 尝试加载当前目录 (AI_Researcher_Agent/) 下的 .env
load_dotenv(os.path.join(current_dir, '.env'))
# 2. 尝试加载项目根目录下的 .env
load_dotenv(os.path.join(os.path.dirname(current_dir), '.env'))

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

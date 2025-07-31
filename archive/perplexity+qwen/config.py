import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
DASHSCOPE_API_KEY = os.getenv('DASHSCOPE_API_KEY')
PERPLEXITY_API_KEY = os.getenv('PERPLEXITY_API_KEY')

# DashScope configs 
BASE_URL = "https://dashscope.aliyuncs.com/v1/services/aigc/text-generation/generation"
MODEL_NAME = "qwen-max"

# Perplexity configs
PERPLEXITY_BASE_URL = "https://api.perplexity.ai"

# LangChain configs
TEMPERATURE = 0.5
MAX_TOKENS = 8000
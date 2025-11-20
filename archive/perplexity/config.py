import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# API Key
API_KEY = os.getenv('PERPLEXITY_API_KEY')
API_ENDPOINT = os.getenv('PERPLEXITY_API_ENDPOINT')
# Model configs
MODEL = "sonar"
TEMPERATURE = 0.6
TOP_P = 0.9 
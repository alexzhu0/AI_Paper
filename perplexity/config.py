import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()

# API Key
API_KEY = os.getenv('PAI_API_KEY')
API_ENDPOINT = os.getenv('PAI_API_ENDPOINT')
# Model configs
MODEL = "sonar-reasoning-pro"
TEMPERATURE = 0.6
TOP_P = 0.9 
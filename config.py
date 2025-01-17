import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('DASHSCOPE_API_KEY')
BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
MODEL_NAME = "qwen-max"  
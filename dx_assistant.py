from openai import OpenAI
from config import OPENAI_API_KEY, BASE_URL, MODEL_NAME

class DXAssistant:
    def __init__(self):
        self.client = OpenAI(
            api_key=OPENAI_API_KEY,
            base_url=BASE_URL
        )
        self.model = MODEL_NAME
        
    def analyze(self, title, thoughts):
        prompt = self._build_prompt(title, thoughts)
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "你是一个专业的智库分析专家"},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
        
    def _build_prompt(self, title, thoughts):
        return f"""
标题：{title}
写作思路：{thoughts}

请按照以下结构输出：
1. 整体框架
2. 各部分详细大纲
3. 数据支撑建议
4. 写作要点
        """ 
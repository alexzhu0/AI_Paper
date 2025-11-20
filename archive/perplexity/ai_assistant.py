import httpx
from typing import Optional, Dict, Any
from config import MODEL, TEMPERATURE, TOP_P, API_KEY  # 导入配置
import os

class AIAssistant:
    def __init__(self, api_key: str = API_KEY):
        self.api_key = api_key
        self.api_url = os.getenv('PERPLEXITY_API_ENDPOINT')  # 从环境变量获取
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
    def analyze(self, title: str, thoughts: dict) -> str:
        try:
            # 调用 AI API
            payload = {
                "model": MODEL,
                "messages": [
                    {
                        "role": "system",
                        "content": """Be precise and concise."""
                    },
                    {
                        "role": "user",
                        "content": f"主题：{title}\n要求：{thoughts}\n请根据以上信息，搜罗全网最新咨询生成一篇完整的分析文章。"
                    }
                ],
                "temperature": TEMPERATURE,
                "top_p": TOP_P,
                "max_tokens": 10000,
                "citations_options": {
                    "max_citations": 99,
                    "show_all": True
                }
            }
            
            response = httpx.post(
                self.api_url,
                headers=self.headers,
                json=payload,
                timeout=30
            )
            
            response.raise_for_status()
            data = response.json()
            
            if 'error' in data:
                raise ValueError(f"API Error: {data['error']}")
                
            content = data['choices'][0]['message']['content']
            
            # 打印完整的响应数据，用于调试
            print("API Response:", data)
            
            # 添加引用来源列表
            if 'citations' in data:
                content += "\n\n引用来源：\n"
                for i, citation in enumerate(data['citations'], 1):
                    # 检查 citation 的类型和内容
                    print(f"Citation {i}:", citation)
                    if isinstance(citation, dict):
                        url = citation.get('url', 'No URL available')
                        title = citation.get('title', 'No title available')
                        content += f"[{i}] {title}\n    {url}\n"
                    else:
                        content += f"[{i}] {str(citation)}\n"
            
            return content
            
        except Exception as e:
            import traceback
            return f"分析生成失败: {str(e)}\n{traceback.format_exc()}" 
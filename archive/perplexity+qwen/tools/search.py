from langchain.tools import BaseTool
from typing import Optional, Any
import httpx
from pydantic import Field

class PerplexitySearchTool(BaseTool):
    name: str = "perplexity_search"
    description: str = "搜索最新的网络信息"
    return_direct: bool = False
    api_key: str = Field(description="Perplexity API key")
    
    def __init__(self, api_key: str):
        super().__init__(api_key=api_key)
        
    def _run(self, query: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        try:
            response = httpx.post(
                "https://api.perplexity.ai/chat/completions",
                headers=headers,
                json={
                    "model": "sonar",
                    "messages": [{
                        "role": "user", 
                        "content": f"""请详细搜索并提供以下内容的相关信息：
1. {query}
2. 包含具体数据、案例和最新进展
3. 提供可靠来源的引用
4. 重点关注实际影响和未来趋势"""
                    }]
                },
                timeout=30.0
            )
            
            response.raise_for_status()
            data = response.json()
            
            if 'error' in data:
                return f"搜索错误: {data['error']}"
                
            if not data.get('choices'):
                return "未找到相关信息"
                
            return data['choices'][0]['message']['content']
            
        except Exception as e:
            return f"搜索失败: {str(e)}"
        
    async def _arun(self, query: str) -> str:
        raise NotImplementedError("异步搜索暂不支持") 
from typing import Any, List, Optional
from langchain.llms.base import LLM
from dashscope import Generation
from dashscope.api_entities.dashscope_response import GenerationResponse
from langchain.callbacks.manager import CallbackManagerForLLMRun

class QwenLLM(LLM):
    model_name: str = "qwen-max"
    temperature: float = 0.5
    max_tokens: int = 8000
    
    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        generation = Generation()
        response = generation.call(
            model=self.model_name,
            messages=[{
                "role": "system",
                "content": "你是一个专业的智库分析专家"
            }, {
                "role": "user",
                "content": prompt
            }],
            result_format='message',
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=0.8,
            enable_search=True
        )
        
        if not isinstance(response, GenerationResponse):
            raise ValueError(f"Unexpected response type: {type(response)}")
            
        if response.status_code != 200:
            raise ValueError(f"API call failed: {response.code} - {response.message}")
            
        if not response.output or not response.output.choices:
            raise ValueError("No output generated")
            
        return response.output.choices[0].message.content
        
    @property
    def _llm_type(self) -> str:
        return "qwen"
        
    @property
    def _identifying_params(self) -> dict:
        return {
            "model_name": self.model_name,
            "temperature": self.temperature,
            "max_tokens": self.max_tokens
        } 
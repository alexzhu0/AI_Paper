from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from tools.search import PerplexitySearchTool
from llm.qwen import QwenLLM
from config import *

class DXAssistant:
    def __init__(self):
        # 初始化 QWen
        self.llm = QwenLLM(
            model_name=MODEL_NAME,
            temperature=TEMPERATURE,
            max_tokens=MAX_TOKENS
        )
        
        # 初始化工具
        self.search_tool = PerplexitySearchTool(PERPLEXITY_API_KEY)
        
        # 初始化记忆
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        
        # 初始化 agent
        self.agent = initialize_agent(
            tools=[self.search_tool],
            llm=self.llm,
            agent=AgentType.CHAT_CONVERSATIONAL_REACT_DESCRIPTION,
            memory=self.memory,
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=3,
            early_stopping_method="generate"
        )
    
    def analyze(self, title: str, thoughts: str) -> str:
        try:
            # 1. 先用 sonar 搜索 title 相关内容
            search_result = self.search_tool.run(title)
            
            # 2. 让 qwen 根据 thoughts 框架来处理搜索结果
            prompt = self._build_prompt(title, thoughts, search_result)
            result = self.agent.run(prompt)
            
            if not result:
                return "抱歉，分析生成失败，请重试。"
            return result
        except Exception as e:
            return f"分析生成过程中遇到问题：{str(e)}\n请尝试重新运行或调整输入。"
        
    def _build_prompt(self, title: str, thoughts: str, search_result: str) -> str:
        return f"""你是一个专业的智库分析专家。请基于以下信息和框架，生成一篇完整的分析文章：

主题: {title}

搜索到的相关信息:
{search_result}

参考框架:
{thoughts}

文章要求：
1. 严格按照参考框架组织文章结构
2. 充分利用搜索结果中的数据和信息
3. 观点客观、论述严谨
4. 适当引用数据和案例支撑论点
5. 语言专业、流畅

直接输出完整文章内容，不要包含大纲或写作建议。确保文章的每个观点都有数据或案例支撑。
""" 
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from typing import Dict, List
import streamlit as st

class DXAssistant:
    def __init__(self):
        self.llm = ChatOpenAI(
            temperature=0.5,
            openai_api_key="sk-0e07f342b25c4d6cae2ba1e54393b7ba",
            model_name="qwen-turbo",
            base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
        )
        
        self.outline_prompt = PromptTemplate(
            input_variables=["title", "thoughts"],
            template="""
            你是一位智库分析专家，专注于生成针对用户提供的标题和写作思路完成整片文章的纲要梳理。
            你擅长结构化思维，具有全局视角，能够挖掘主题深度并构建有逻辑的写作框架。

            请根据以下信息生成详细大纲:
            
            标题: {title}
            写作思路: {thoughts}
            
            请提供:
            1. 完整的结构化大纲(包含章节标题和子标题)
            2. 确保逻辑连贯,覆盖核心内容
            
            规则:
            大纲需覆盖核心内容，逻辑连贯，具有可操作性
            整体大纲具有创意性，具有网络传播效应，注意SEO传播，不要太过于复杂。
            注意：用户不是要写论文，而是一个简单的公众号文章，整体结构不要太过于复杂
            
            """
        )
        
        self.chain = LLMChain(llm=self.llm, prompt=self.outline_prompt)
        
    def generate_outline(self, title: str, thoughts: str) -> str:
        """生成大纲和解释"""
        result = self.chain.run({
            "title": title,
            "thoughts": thoughts
        })
        return result
    
    def format_output(self, outline: str) -> str:
        """美化输出格式"""
        formatted_output = ""
        sections = outline.split("# ")
        
        for section in sections:
            if not section.strip():
                continue
            
            title, *content = section.split("\n", 1)
            title = title.strip()
            
            # 主标题
            if title in ["大纲结构", "设计说明"]:
                formatted_output += f"\n## {title}\n{'_'*50}\n"
            # 章节标题
            elif title.startswith(("第", "引言", "结论")):
                formatted_output += f"\n### {title}\n"
            # 子标题
            else:
                if content:
                    formatted_output += f"#### {title}\n"
                    for line in content[0].split('\n'):
                        if line.strip() and not line.startswith(('#', '-', '*', '**Why**')):
                            formatted_output += f"- {line.strip()}\n"
        
        return formatted_output 
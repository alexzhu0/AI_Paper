
from langchain_openai import ChatOpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain.prompts import PromptTemplate
from tools.web_searcher import web_searcher
from tools.article_writer import article_writer
from config import DASHSCOPE_API_KEY, QWEN_BASE_URL, QWEN_MODEL_NAME, AGENT_TEMPERATURE

# 1. Initialize the LLM
llm = ChatOpenAI(
    model_name=QWEN_MODEL_NAME,
    openai_api_base=QWEN_BASE_URL,
    openai_api_key=DASHSCOPE_API_KEY,
    streaming=True,
    temperature=AGENT_TEMPERATURE
)

# 2. Define the tools
tools = [web_searcher, article_writer]

# 3. Create the prompt template
prompt_template = """
Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}
"""

prompt = PromptTemplate.from_template(prompt_template)

# 4. Create the agent
agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

# 5. Create the agent executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    handle_parsing_errors=True
)

def run_agent(user_query: str):
    """Runs the agent with the given user query and returns the result."""
    return agent_executor.invoke({"input": user_query})

if __name__ == '__main__':
    # For testing the agent directly
    test_query = "What are the latest trends in the semiconductor industry regarding AI chips, and what is their market impact?"
    result = run_agent(test_query)
    print(result)

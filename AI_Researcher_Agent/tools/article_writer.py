
from langchain.tools import tool
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from config import DASHSCOPE_API_KEY, QWEN_BASE_URL, QWEN_MODEL_NAME

@tool
def article_writer(context: str) -> str:
    """
    A tool for writing a well-structured and in-depth article based on the provided context.
    It uses the Qwen-max model to generate a high-quality article.
    """
    llm = ChatOpenAI(
        model_name=QWEN_MODEL_NAME,
        openai_api_base=QWEN_BASE_URL,
        openai_api_key=DASHSCOPE_API_KEY,
        streaming=False,
        temperature=0.7
    )

    prompt_template = """
    As a professional writer and analyst, please write a comprehensive and insightful article based on the following information.
    The article should be well-structured, with a clear introduction, body, and conclusion.
    Please ensure the language is fluent and the analysis is deep.

    **Provided Information:**
    {context}

    **Article:**
    """

    prompt = PromptTemplate(template=prompt_template, input_variables=["context"])
    chain = LLMChain(llm=llm, prompt=prompt)

    try:
        article = chain.run(context=context)
        return article
    except Exception as e:
        return f"An error occurred while generating the article: {e}"

if __name__ == '__main__':
    # For testing the tool directly
    test_context = """
    Recent advancements in AI chips include the development of 3nm process technology, which significantly increases transistor density and power efficiency. 
    Major players like NVIDIA, Google, and startups are competing fiercely. 
    NVIDIA's H100 GPU remains a market leader, while Google's TPU v5 shows strong performance in specific AI workloads. 
    The market is seeing a trend towards specialized chips (ASICs) for AI, designed to accelerate specific neural network models efficiently.
    """
    generated_article = article_writer.run(test_context)
    print(generated_article)

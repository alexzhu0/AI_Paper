from dx_assistant import DXAssistant

def example():
    assistant = DXAssistant()
    
    title = "AI产品分析：向量数据库（Vector Database）"
    thoughts = """
    我要从发展概述、功能应用、市场发展、典型产品等方面完成这篇文章，
    再找一些权威的数据佐证我的思路
    """
    
    result = assistant.analyze(title, thoughts)
    print(result)

if __name__ == "__main__":
    example() 
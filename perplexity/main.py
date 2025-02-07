import streamlit as st
from ai_assistant import AIAssistant
from config import API_KEY

def main():
    st.title("智库分析助手")
    
    # 创建两列布局
    col1, col2 = st.columns(2)
    
    with col1:
        title = st.text_input("分析主题", 
            help="输入你想要分析的主题，AI将搜索相关最新信息")
        
        thoughts = st.text_area("分析框架", 
            height=200,
            help="输入分析框架，比如：背景分析、现状、问题、对策等")
        
        output_format = st.selectbox(
            "输出格式",
            ["Markdown", "PDF", "HTML"]
        )
    
    if st.button("生成分析"):
        if title and thoughts:
            with st.spinner("正在分析中..."):
                assistant = AIAssistant(API_KEY)
                result = assistant.analyze(title, thoughts)
                
                # 展示结果
                st.markdown("## 分析结果")
                st.markdown(result)
                
                # 下载按钮
                if output_format != "Markdown":
                    st.download_button(
                        f"下载{output_format}",
                        result,
                        f"report.{output_format.lower()}"
                    )
        else:
            st.warning("请输入分析主题和框架")

if __name__ == "__main__":
    main() 
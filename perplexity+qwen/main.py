import streamlit as st
from dx_assistant import DXAssistant
import json

st.set_page_config(page_title="智库小助手", layout="wide")

def main():
    st.title("智库小助手 2.0")
    
    col1, col2 = st.columns(2)
    
    with col1:
        title = st.text_input("文章标题")
        thoughts = st.text_area("写作思路", height=200)
        
        output_format = st.selectbox(
            "输出格式",
            ["Markdown", "PDF", "HTML"]
        )
    
    if st.button("生成分析"):
        if title and thoughts:
            with st.spinner("正在分析中..."):
                assistant = DXAssistant()
                result = assistant.analyze(title, thoughts)
                
                # 展示结果
                st.markdown("## 分析结果")
                st.markdown(result)
                
                # 下载按钮
                if output_format != "Markdown":
                    # TODO: 实现格式转换
                    st.download_button(
                        f"下载{output_format}",
                        result,
                        f"report.{output_format.lower()}"
                    )
        else:
            st.warning("请输入标题和写作思路")

if __name__ == "__main__":
    main() 
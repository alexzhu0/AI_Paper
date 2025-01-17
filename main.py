import streamlit as st
from dx_assistant import DXAssistant

st.set_page_config(page_title="智库小助手")

def main():
    st.title("智库小助手")
    
    title = st.text_input("文章标题")
    thoughts = st.text_area("写作思路", height=200)
    
    if st.button("生成分析"):
        if title and thoughts:
            with st.spinner("正在分析中..."):
                assistant = DXAssistant()
                result = assistant.analyze(title, thoughts)
                st.markdown(result)
        else:
            st.warning("请输入标题和写作思路")

if __name__ == "__main__":
    main() 
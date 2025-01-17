import streamlit as st
from dx_assistant import DXAssistant

st.title("大纲生成助手")

title = st.text_input("输入标题", placeholder="请输入文章标题...")
thoughts = st.text_area(
    "输入写作思路",
    placeholder="请输入写作思路，比如：\n发展概述：...\n功能应用：...\n市场发展：...\n典型产品：...",
    height=300  # 设置高度
)

if st.button("生成大纲"):
    assistant = DXAssistant()
    outline = assistant.generate_outline(title, thoughts)
    formatted = assistant.format_output(outline)
    st.markdown(formatted) 
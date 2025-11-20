import streamlit as st
from langchain_community.callbacks import StreamlitCallbackHandler
from agent import run_agent

st.set_page_config(page_title="AI Researcher Agent", page_icon="🤖")

st.title("🤖 AI Researcher Agent")
st.caption("An intelligent agent that researches the web and writes deep articles for you.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hello! I am your AI Researcher. What topic would you like me to research and write about today?"}]

# Display chat messages from history on app rerun
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Handle user input
if prompt := st.chat_input("Enter your research topic (e.g., 'The future of quantum computing')"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    st.chat_message("user").write(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st_callback = StreamlitCallbackHandler(st.container())
        
        try:
            # Run the agent with the callback
            response = run_agent(prompt, callbacks=[st_callback])
            output_text = response["output"]
            
            st.markdown(output_text)
            
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": output_text})

            # Provide a download button for the generated article
            st.download_button(
                label="📥 Download Article",
                data=output_text,
                file_name="research_article.md",
                mime="text/markdown"
            )
            
        except Exception as e:
            st.error(f"An error occurred: {e}")

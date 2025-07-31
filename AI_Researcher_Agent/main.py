
import streamlit as st
from agent import run_agent

st.title("AI Researcher Agent")
st.caption("An intelligent agent for web research and article writing.")

# User input
user_query = st.text_area(
    "Enter your research topic:",
    height=100,
    placeholder="e.g., Analyze the impact of quantum computing on cryptography."
)

if st.button("Start Analysis"):
    if not user_query:
        st.warning("Please enter a research topic.")
    else:
        with st.spinner("Agent is thinking and working..."):
            try:
                st.subheader("Agent's Thought Process & Actions")
                # The agent_executor in agent.py is set to verbose=True, 
                # so the thought process will be printed to the console where streamlit is running.
                # For a more advanced UI, one could capture stdout to display it in the web app.
                
                # For now, we will just show a message and the final result.
                st.write("The agent is now performing research and writing. You can see its detailed actions in the console.")

                # Run the agent
                result = run_agent(user_query)

                st.subheader("Final Result")
                st.markdown(result['output'])

            except Exception as e:
                st.error(f"An error occurred: {e}")

import os
import streamlit as st
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="🤖 AI Agent Pro",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for ChatGPT-like interface
st.markdown("""
<style>
    .main {background-color: #0e1117;}
    .stTextInput>div>div>input {background-color: #262730; color: white;}
    .chat-message {padding: 1.5rem; border-radius: 1rem; margin-bottom: 1rem; display: flex}
    .chat-message.user {background-color: #2b313e;}
    .chat-message.bot {background-color: #475063;}
    .chat-message .avatar {width: 20%;}
    .chat-message .message {width: 80%; padding-left: 1rem;}
    .stButton>button {background-color: #4CC9F0; color: white; border-radius: 20px; border: none; padding: 0.5rem 1rem; font-weight: bold;}
    .stButton>button:hover {background-color: #3A86FF;}
    .typing-indicator {display: inline-block; height: 1em; font-size: 10px;}
    .typing-indicator span {height: 10px; width: 10px; background-color: #fff; display: inline-block; border-radius: 50%; margin: 0 1px; animation: typing 1.4s infinite;}
    .typing-indicator span:nth-child(2) {animation-delay: 0.2s;}
    .typing-indicator span:nth-child(3) {animation-delay: 0.4s;}
    @keyframes typing {0%, 60%, 100% {transform: translateY(0);} 30% {transform: translateY(-5px);}}
    .stSpinner {color: #4CC9F0 !important;}
</style>
""", unsafe_allow_html=True)

# Initialize agent (cached for performance)
@st.cache_resource
def get_agent():
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    tools = [DuckDuckGoSearchRun(name="Search")]
    agent = create_openai_functions_agent(llm, tools, "You are a helpful AI assistant that uses web search to answer questions.")
    return AgentExecutor(agent=agent, tools=tools, verbose=False, handle_parsing_errors=True)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar
with st.sidebar:
    st.title("🤖 AI Agent Pro")
    st.markdown("---")
    st.markdown("### How it works")
    st.markdown("""
    1. Ask any question
    2. Agent searches the web in real-time
    3. Get accurate, up-to-date answers
    """)
    st.markdown("---")
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
    st.markdown("---")
    st.caption("Powered by LangChain + OpenAI + DuckDuckGo")

# Main chat interface
st.title("💬 AI Agent Chat")
st.caption("Ask me anything - I search the web for real-time answers!")

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to know?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Display assistant response with typing indicator
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Show thinking indicator
        with st.spinner("🔍 Searching the web..."):
            try:
                # Get agent response
                agent = get_agent()
                response = agent.invoke({"input": prompt})
                full_response = response['output']
                
                # Simulate typing effect
                for chunk in full_response.split():
                    full_response += chunk + " "
                    time.sleep(0.05)
                    message_placeholder.markdown(full_response + "▌")
                message_placeholder.markdown(full_response)
                
            except Exception as e:
                full_response = f"❌ Error: {str(e)}"
                message_placeholder.markdown(full_response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Footer
st.markdown("---")
st.caption("💡 Tip: Ask about current events, sports scores, or latest news for real-time web search results!")

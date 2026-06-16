# Import magic libraries
import antigravity  # This is the fun part!
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
import os

print("🚀 Initializing AI Brain...")

# 1. Setup the brain (The AI)
# You need an OpenAI API Key for this to work!
llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

# 2. Give it superpowers (Tools)
# It can now look at the internet using DuckDuckGo!
tools = [DuckDuckGoSearchRun(name="Search")]

# 3. Create the agent
prompt = create_openai_functions_agent(llm, tools, "You are a helpful space explorer AI.")
agent_executor = AgentExecutor(
    agent=prompt,
    tools=tools,
    verbose=True
)

print("🤖 AI Agent is ready! Ask me anything or type 'quit' to stop.")

while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ['quit', 'exit']:
        print("🔌 Powering down...")
        break
    
    # Run the search
    try:
        response = agent_executor.invoke({"input": user_input})
        print(f"\n🤖 AI Agent: {response['output']}\n")
    except Exception as e:
        print(f"💥 Oops! Something went wrong: {e}")

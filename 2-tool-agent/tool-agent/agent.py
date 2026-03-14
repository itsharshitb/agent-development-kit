from google.adk.agents import Agent
from google.adk.tools import google_search

root_agent = Agent(
    name="tool_agent",
    description="Tool agent",
    instruction="""
    You are a helpful assistant that can use the following tools:
    - google_search 
    """,
    model="gemini-2.0-flash",
    tools=[google_search],
)

# root_agent.run("What is the capital of France?")
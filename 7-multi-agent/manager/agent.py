from google.adk.agents.llm_agent import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.agent_tool import AgentTool
from datetime import datetime

from .sub_agents.funny_nerd.agent import funny_nerd
from .sub_agents.news_analyst.agent import news_analyst
from .sub_agents.stock_analyst.agent import stock_analyst


def get_current_time() -> dict:
    """Get the current date and time."""
    return {"current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}


root_agent = LlmAgent(
    name="root_agent",
    model=LiteLlm(model="openrouter/arcee-ai/trinity-large-preview:free"),
    description="Manager Agent that delegates tasks to specialized sub-agents",
    instruction="""
    You are a manager agent that oversees a team of specialized agents.
    Always delegate tasks to the most appropriate agent.

    You can TRANSFER tasks to these sub-agents (they take over the conversation):
    - stock_analyst: For stock prices and financial market questions
    - funny_nerd:    For jokes and fun nerdy content

    You can CALL these as tools (they return a result to you):
    - news_analyst:  For fetching and summarizing the latest news
    - get_current_time: To get the current date and time

    IMPORTANT: news_analyst is a tool you call directly — do NOT try to transfer to it.
    For everything else, transfer to the appropriate sub-agent.
    """,
    sub_agents=[stock_analyst, funny_nerd],
    tools=[
        AgentTool(news_analyst),
        get_current_time,
    ],
)

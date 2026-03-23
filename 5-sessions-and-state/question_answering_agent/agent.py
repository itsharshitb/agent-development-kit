from google.adk.agents import Agent
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

#Create a new agent
question_answering_agent = LlmAgent(
    name="question_answering_agent",
    model=LiteLlm(model="openrouter/arcee-ai/trinity-large-preview:free"),
    description="Question Answering Agent",
    instruction="""
        You are a helpful assistant that answers questions about the user's preferences.

        Here is some information about the user:
        Name: {user_name}
        Preferences: {user_preferences}
    """
)
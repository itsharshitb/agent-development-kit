from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

root_agent = LlmAgent(
    name = "greeting_agent",
    model = LiteLlm(model="openrouter/arcee-ai/trinity-large-preview:free"),
    description = "Greeting agent",
    instruction = """
    You are a helpful assistant that greets the user.
    Ask for the user's name and greet them by name."""
)
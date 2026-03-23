from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from googlesearch import search


def google_search(query: str) -> list[dict]:
    """Search Google and return top 5 results.

    Args:
        query: The search query string.

    Returns:
        A list of dicts with 'title', 'url', and 'description' for each result.
    """
    results = []
    for result in search(query, num_results=5, advanced=True):
        results.append({
            "title": result.title,
            "url": result.url,
            "description": result.description,
        })
    return results


root_agent = LlmAgent(
    name="tool_agent",
    model=LiteLlm(model="openrouter/arcee-ai/trinity-large-preview:free"),
    description="Tool agent",
    instruction="""
    You are a helpful assistant that can search the web to answer questions.
    When the user asks something that requires up-to-date or factual information,
    use the google_search tool to find relevant results, then summarize the answer.
    """,
    tools=[google_search],
)
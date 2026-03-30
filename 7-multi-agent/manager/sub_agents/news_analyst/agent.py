from google.adk.agents.llm_agent import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from duckduckgo_search import DDGS
from datetime import datetime


def search_latest_news(query: str, max_results: int = 5) -> list[dict]:
    """Search for the latest news articles on a given topic.

    Args:
        query: The topic or keywords to search for.
        max_results: Maximum number of news articles to return (default: 5).

    Returns:
        A list of dicts with 'title', 'url', 'source', 'published' and 'summary' for each article.
    """
    print(f"--- Tool: search_latest_news called for query: '{query}' ---")
    try:
        with DDGS() as ddgs:
            raw_results = list(ddgs.news(
                keywords=query,
                region="wt-wt",      # worldwide
                safesearch="off",
                timelimit="d",        # past 24 hours — use "w" for past week, "m" for past month
                max_results=max_results,
            ))

        if not raw_results:
            return [{"error": f"No news found for query: '{query}'"}]

        articles = []
        for item in raw_results:
            articles.append({
                "title": item.get("title", "No title"),
                "url": item.get("url", ""),
                "source": item.get("source", "Unknown source"),
                "published": item.get("date", "Unknown date"),
                "summary": item.get("body", "No summary available"),
            })

        return articles

    except Exception as e:
        return [{"error": f"Failed to fetch news: {str(e)}"}]


news_analyst = LlmAgent(
    name="news_analyst",
    model=LiteLlm(model="openrouter/arcee-ai/trinity-large-preview:free"),
    description="A news analyst agent that fetches and summarizes the latest news articles on any topic",
    instruction="""
    You are a helpful news analyst that fetches and summarizes the latest news.

    When asked about news:
    1. Use the search_latest_news tool to fetch recent articles on the topic.
    2. Summarize the key points from the results in a clear, concise format.
    3. Always mention the source and published date for each article.
    4. If the user asks for "today's" news, remember today's date is provided in the conversation context.
    5. If no results are found, let the user know and suggest a different query.

    Format your response like:
    📰 **[Article Title]**
    🔗 Source: [Source Name] | 🕒 Published: [Date]
    📝 [Brief summary of the article]
    ---
    """,
    tools=[search_latest_news],
)
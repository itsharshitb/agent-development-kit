from datetime import datetime
import yfinance as yf
from google.adk.agents.llm_agent import LlmAgent
from google.adk.models.lite_llm import LiteLlm

def get_stock_price(ticker: str) -> dict:
    """Retrieves current stock price and saves to session state."""
    print(f"--- Tool: get_stock_price called for ticker: {ticker} ---")
    
    try:
        #fetch stock data
        stock = yf.Ticker(ticker)
        current_price = stock.info.get("currentPrice")  

        if current_price is None:
            return {
                "status": "error",
                "error_message": f"Could not fetch price for {ticker}",
            }
        
        #get time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return {
            "status": "success",
            "ticker": ticker,
            "current_price": current_price,
            "timestamp": current_time,
        }
    except Exception as e:
        return {
            "status": "error",
            "error_message": f"Error fetching stock data: {str(e)}",
        }
        
#Create a root agent
stock_analyst = LlmAgent(
    name="stock_analyst",
    model=LiteLlm(model="openrouter/arcee-ai/trinity-large-preview:free"),
    description="An agent that can look up stock prices and track them over time.",
    instruction="""
    You are a helpful stock market assistant that helps users track their stocks of interest.
    
    When asked about stock prices:
    1. Use the get_stock_price tool to fetch the latest price for the requested stock(s)
    2. Format the response to show each stock's current price and the time it was fetched
    3. If a stock price couldn't be fetched, mention this in your response
    
    Example response format:
    "Here are the current prices for your stocks:
    - GOOG: $175.34 (updated at 2024-04-21 16:30:00)
    - TSLA: $156.78 (updated at 2024-04-21 16:30:00)
    - META: $123.45 (updated at 2024-04-21 16:30:00)"
    """,
    tools=[get_stock_price],
)

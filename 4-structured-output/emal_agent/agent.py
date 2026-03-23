from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm
from pydantic import BaseModel, Field


#----Define output schema-----
class EmailContent(BaseModel):
    subject: str = Field(
        description="The subject line of the email. Should be concise and descriptive"
    )
    body: str = Field(
        description="The main content of the email. Should be well-formatted with proper greetings, paragraphs and closing"
    )

#----Define Agent-----
root_agent = LlmAgent(
    name="email_agent",
    model=LiteLlm(model="openrouter/arcee-ai/trinity-large-preview:free"),
    instruction="""
    You are an email generator assistant. Your task is to compose a professional email based on the user's request.
    
    Follow these guidelines:
    1. Create an appropriate subject line.
    2. Write a well structured email body with:
        * Profssional greating
        * Clear and concise message
        * Appropriate closing
        * Your name as signature
    3. Suggest relevant attachment if applicable (empty list if none needed)
    4. Email tone should match the purpose of the email (Formal for business, casual for colleagues)
    5. Keep email concise but complete


    IMPORTANT: Your response MUST be in JSON format with the following schema:
    {
        "subject": "subject line here",
        "body": "email bosy here with proper paragraphs and formatting"
    }   
    """,
    description="Generates a professional email with structured subject and body",
    output_schema=EmailContent,
    output_key="email",
)
import uuid

from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

from question_answering_agent import agent

load_dotenv()

# Create new session service to store state

session_service = InMemorySessionService()

initial_state = {
    "user_name": "Harshit",
    "user_preferences": """
        I like to play valorant, badminton, football
        My favourate food is biryani
        My favourate series is the Harry Potter
        My favourate movie is the Dark Knight
        My favourate actor is the Tom Holland
        """
}

# Create a new session
APP_NAME = "Harshit Bot"
USER_ID = "Harshit_Bhatt"
SESSION_ID = str(uuid.uuid4())
stateful_session = session_service.create_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID,
    state=initial_state
)

print("CREATED A NEW SESSION")
print(f"\tSession ID: {SESSION_ID}")

# Create a runner for the agent
runner = Runner(
    agent=agent.question_answering_agent,
    app_name=APP_NAME,
    session_service=session_service
)

new_message = types.Content(role="user", parts=[types.Part(text="What is Harshit's Favourate sports")])

for event in runner.run(
    user_id=USER_ID,
    session_id=SESSION_ID,
    new_message=new_message
):
    print(f"event: {event}")
    if event.is_final_response():
        if event.content and event.content.parts:
            print(f"final response: {event.content.parts[0].text}")

print("====Session Event Exploration====")

session = session_service.get_session(
    app_name=APP_NAME,
    user_id=USER_ID,
    session_id=SESSION_ID
)

#log final session state
print("====Final Session State====")

for key, value in session.state.items():
    print(f"{key}: {value}")
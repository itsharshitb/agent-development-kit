import asyncio
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService
from memory_agent.agent import memory_agent
from utils import call_agent_async

load_dotenv()

#======= init persistent storage service ===========
# using sql database for persistance storage
db_url = "sqlite:///my_agent_data.db"

# create session service
session_service = DatabaseSessionService(db_url=db_url)

#===========Define initial state===========
#This will only be used when creating a new sessoin

initial_state = {
    "user_name": "Harshit Bhatt",
    "reminders": []
}

#Create a new session if we are running this for the first time
# else pull out the last session
async def main_async():
    #setup constants
    APP_NAME = "memory_agent"
    USER_ID = "aiwithharshit"

    #session management - find or create one
    #check for existing sessions for this existing user
    existing_sessions = session_service.list_sessions(
        app_name=APP_NAME,
        user_id=USER_ID
    ).sessions  # .sessions gives the actual list from the ListSessionsResponse object
    #if there is existing session use it, else create a new one
    if existing_sessions and len(existing_sessions) > 0:
        SESSION_ID = existing_sessions[0].id
        print(f"Continuing existing session: {SESSION_ID}")
    else: #create a new one
        new_session = session_service.create_session(
            app_name=APP_NAME,
            user_id=USER_ID,
            state=initial_state
        )
        SESSION_ID = new_session.id
        print(f"Created new session: {SESSION_ID}")

    #create runner setup
    runner = Runner(
        agent=memory_agent,
        session_service=session_service,
        app_name=APP_NAME,
    )

    #======interactive conversation loop=======
    print("\n Welcome to memory agent chat!")
    print("Your reminders will be reminded across the conversation")
    print("Type 'exit' or 'quit' to end conversation")

    while True:
        #Get user input
        user_input = input("\nYou: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Ending conversation. Your data has been saved to the database.")
            break
        
        #call agent/ process the user query
        response = await call_agent_async(
            runner=runner,
            user_id=USER_ID,
            session_id=SESSION_ID,
            query=user_input
        )
        # print(f"Agent: {response}")

if __name__ == "__main__":
    asyncio.run(main_async())

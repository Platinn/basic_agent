from phospho import Agent, Message
from dotenv import load_dotenv
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from langchain.chat_models import ChatOpenAI
import os 

# Load your environment variables
load_dotenv()

open_ai_key = os.getenv("OPEN_AI_KEY")

# Initialize the agent
agent = Agent()

def ph_agent(input : str):
    response = f"John asked : {input} {open_ai_key}"
    return response 

# Define your routes
# you don't have to implement both routes
"""
@agent.ask()
def myask(message):
    print(f"Your message was {message.content}, now I can do stuff in the background")
"""

@agent.chat()
def mychat(message):
    response = ph_agent(message.content)
    return Message(response)

# That's it, you're done!
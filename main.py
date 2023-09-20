from phospho import Agent, Message
from dotenv import load_dotenv

from langchain.chat_models import ChatOpenAI
from langchain.utilities import SerpAPIWrapper
from langchain.agents import Tool, initialize_agent, AgentType
from langchain.schema import SystemMessage, HumanMessage

# Load your environment variables
load_dotenv()

# Agent Logic with Langchain 
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo-0613")

search = SerpAPIWrapper()
tools = [Tool(name="SERPAPI", func=search.run, description="Search the web")]

search_agent = initialize_agent(tools=tools, llm=llm, agent=AgentType.OPENAI_MULTI_FUNCTIONS, verbose=True)

#print(agent.run("Hello, what is the weather in Paris ?"))

# Agent Logic embedded in a function
def my_agent(input):
    messages = [
        SystemMessage(content="You are an helpful assistant named phospho agent. You can help me to find information on the web"),
        HumanMessage(content=input),
    ]
    
    response=search_agent.run(messages)

    return response

# Package it into a phospho agent
agent = Agent()

@agent.chat()
def my_chat(message):
    # Use our agent logic to generate a response
    response = my_agent(message)
    # Return the response in a Message object
    return Message(response)

#print(my_chat("what is the weather in Paris ?"))
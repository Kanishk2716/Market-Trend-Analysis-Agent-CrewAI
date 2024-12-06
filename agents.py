from crewai import Agent , LLM
import litellm
import os
from dotenv import load_dotenv
from tools import tool

load_dotenv()

# Configure litellm
litellm.set_verbose=True
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Create LLM

llm = LLM(
    model = "gemini/gemini-1.5-flash" ,
    api_key= os.getenv("GOOGLE_API_KEY")
)

# Agents

market_researcer = Agent(
    role = "Market Trend Analyst" ,
    goal = "Identify emerging trend in the {industry}" ,
    verbose = True ,
    memory = True , 
    backstory="Strategic thinker with a knack for spotting market shifts and opportunities" ,
    tools = [tool] ,
    llm = llm ,
    allow_delegation=True
)

# Trend Summarizer Agent

trend_summarizer = Agent(
    role = "Trend Communication Specialist" ,
    goal = "Create digestable summaries of complex market trends" ,
    verbose = True ,
    memory = True ,
    backstory="Expert at transforming complex data into clear, actionable insights" ,
    tools = [tool] ,
    llm = llm ,
    allow_delegation=False
)

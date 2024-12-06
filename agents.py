from crewai import Agent , LLM
import litellm
import os
from dotenv import load_dotenv
from tools import tool

load_dotenv()

# Configure liteLLM
litellm.set_verbose = True
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Create LLM
llm = LLM(
    model = "gemini/gemini-1.5-flash" ,
    api_key = os.getenv("GOOGLE_API_KEY")
)

# AGENTS

# researcher agent
tech_researcher = Agent(
    role = "Tech Product Analyst" ,
    goal = "Conduct Comprehensive research on {product}" ,
    verbose = True ,
    memory = True ,
    backstory= (
        "Seasoned tech enthusiast with a passion for dissecting product specs and analyzing market trends."
        "Provides deep insights to navigate the tech landscape."
    ) ,
    tools = [tool] ,
    llm = llm ,
    allow_delegation = True

)

# Writer Agent
tech_writer = Agent(
    role = "Tech review writer" ,
    goal = "Create engaging and informative product reviews" ,
    verbose = True ,
    memory = True ,
    backstory=(
        "Skilled communicator who translates technical details into reader-friendly content."
        "Bridges the gap between tech experts and the broader audience."
    ) ,
    tools = [tool] ,
    llm = llm ,
    allow_delegation= False
)


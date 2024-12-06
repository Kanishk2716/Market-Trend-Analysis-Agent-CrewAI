from crewai import Task
from agents import trend_summarizer , market_researcer
from tools import tool
# Research Task  
trend_research_task = Task(
    description="Conduct in-depth research on current and emerging trends in {industry}" ,
    expected_output="Comprehensive Trend analysis report" ,
    tools = [tool] ,
    agent = market_researcer
)

# Summarization Task
trend_summarize_task = Task(
    description="Develop an easily understandable summary of market trends" ,
    expected_output = "A concise, engaging trend report in markdown format" ,
    tools = [tool] ,
    agent = trend_summarizer ,
    async_execution=False ,
    output_file = "trend_summary.md" #Example of output customization
)

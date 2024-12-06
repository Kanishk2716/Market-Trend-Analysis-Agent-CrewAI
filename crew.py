from crewai import Crew , Process
from agents  import trend_summarizer , market_researcer
from task import trend_research_task , trend_summarize_task

# Forming a crew
crew = Crew(
  agents = [trend_summarizer , market_researcer] ,
  tasks = [trend_research_task , trend_summarize_task ],
  process = Process.sequential          

)

## Starting the task execution process with enhanced feedback
result = crew.kickoff(inputs = {"industry" : "Renewable Energy"})
print(result)
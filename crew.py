from crewai import Crew , Process
from agents import tech_researcher , tech_writer
from tasks import research_task , writer_task

# Forming a Crew

crew = Crew(
    agents= [tech_researcher , tech_writer] ,
    tasks = [research_task , writer_task] ,
    process = Process.sequential
)

## starting the task execution process with enhanced feedback
result = crew.kickoff(inputs={'product':'Latest AI Smartphone'})
print(result)
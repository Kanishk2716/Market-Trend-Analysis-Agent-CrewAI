from crewai import Task
from agents import tech_researcher , tech_writer
from tools import tool

# Research Task
research_task = Task(
    description=(
        "Gather  information about atleast 7 {product},"
         "including features, pricing, and market comparison" 
     ),
     expected_output= "A detailed research report with key product insights" ,
    tools = [tool] ,
    agent = tech_researcher
)

# Writing Task
writer_task = Task(
    description="Compose a compelling and informative product review based on  research findings",



    expected_output=(
    "A well-structured, markdown-formatted product review article"
    "that highlights key features, benefits, and comparisons with competitors" 
    ),
    tools = [tool] ,
    agent = tech_writer ,
    async_execution=False ,
    output_file ="tech_review.md" #Example of output customization
)
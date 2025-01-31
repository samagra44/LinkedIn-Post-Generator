import os
from crewai import Task
from dotenv import load_dotenv
from crewai_tools import SerperDevTool
from src.agents.blog_writer_agent import blog_writer_agent

load_dotenv()

os.environ['SERPER_API_KEY'] = os.getenv("SERPER_API_KEY")
tools = SerperDevTool()

blog_writer_agent_task = Task(
    description="Write a comprehensive blog post based on the 1 article provided by the Topic Researcher. The article must include an introduction, step-by-step guides and conclusion. The overall content must be about 400 words long.",
    expected_output="A comprehensive and well-written blog post with an outline and audience analysis and resources. Each section should have 2 or 3 paragraphs",
    agent=blog_writer_agent,
    tools=[tools]
)
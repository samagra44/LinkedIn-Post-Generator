import os
from crewai import Task
from dotenv import load_dotenv
from crewai_tools import SerperDevTool
from src.agents.linkedin_post_agent import linkedin_post_agent

load_dotenv()

os.environ['SERPER_API_KEY'] = os.getenv("SERPER_API_KEY")
tools = SerperDevTool()

linkedin_post_agent_task = Task(
    description="Create a LinkedIn post summarizing the key points from the transcription provided by the Topic Researcher, including relevant hastags.",
    expected_output="A well written blog post in markdown-format ready for publication. Each section should have 2 or 3 paragraphs with resources.",
    agent=linkedin_post_agent,
    tools=[tools]
)
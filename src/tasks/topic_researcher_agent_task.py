import os
from crewai import Task
from dotenv import load_dotenv
from crewai_tools import SerperDevTool
from src.agents.topic_researcher_agent import topic_researcher_agent

load_dotenv()

os.environ['SERPER_API_KEY'] = os.getenv("SERPER_API_KEY")
tools = SerperDevTool()

topic_researcher_agent_task = Task(
    description="Identify and analyze only 1 content or article on the {topic} from the web.",
    expected_output="A complete word-by-word report on the most relevant post or article found on the topic {topic}.",
    agent=topic_researcher_agent,
    tools=[tools]
)
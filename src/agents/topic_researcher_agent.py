import os
from crewai import Agent
from dotenv import load_dotenv
from crewai_tools import SerperDevTool
from langchain_together import ChatTogether

load_dotenv()

os.environ['SERPER_API_KEY'] = os.getenv("SERPER_API_KEY")
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

llm = ChatTogether(
    model=os.getenv("MODEL_NAME")
)
tools = SerperDevTool()

topic_researcher_agent = Agent(
    role="Topic Researcher",
    goal="Search for only 1 relevant resource on the topic {topic} from the web.",
    backstory="Expert in finding and analyzing relevant content from web.",
    tools=[tools],
    llm=llm,
    allow_delegation=True
)
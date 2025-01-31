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

linkedin_post_agent = Agent(
    role="LinkedIn Post Creator",
    goal="Create a concise LinkedIn post summary from the transcription provided by the Topic Researcher.",
    backstory="Expert in crafting enagaging LinkedIn posts that summarizes complex topics and include trending hastags for maximum visibility.",
    tools=[tools],
    llm=llm,
)
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

blog_writer_agent = Agent(
    role="Blog Writer",
    goal="Write a comprehensive blog post from the only 1 article provided by the Topic Researcher, covering all necessary sections.",
    backstory="Experienced in creating in-depth, well-structured blog posts that explain technical concepts clearly and engage readers from introduction to conclusion.",
    tools=[tools],
    llm=llm,
    allow_delegation=True,
)
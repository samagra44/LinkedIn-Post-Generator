from crewai import Crew, Process

from src.agents.topic_researcher_agent import topic_researcher_agent
from src.agents.blog_writer_agent import blog_writer_agent
from src.agents.linkedin_post_agent import linkedin_post_agent

from src.tasks.topic_researcher_agent_task import topic_researcher_agent_task
from src.tasks.blog_writer_agent_task import blog_writer_agent_task
from src.tasks.linkedin_post_agent_task import linkedin_post_agent_task

crew = Crew(
    agents=[topic_researcher_agent, blog_writer_agent, linkedin_post_agent],
    tasks=[topic_researcher_agent_task, blog_writer_agent_task, linkedin_post_agent_task],
    process=Process.sequential,
)
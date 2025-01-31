import os
import streamlit as st
from dotenv import load_dotenv
from src.crews.mycrews import crew

load_dotenv()

os.environ['LANGSMITH_TRACING'] = "true"
os.environ['LANGSMITH_ENDPOINT'] = os.getenv("LANGSMITH_ENDPOINT")
os.environ['LANGSMITH_API_KEY'] = os.getenv("LANGSMITH_API_KEY")
os.environ['LANGSMITH_PROJECT'] = os.getenv("LANGSMITH_PROJECT")

st.set_page_config("LinkedIn Post Generator 📝")

st.sidebar.title("LinkedIn Post Generator 📝")

st.sidebar.image("assests\image.png")

st.header("Automatic LinkedIn Post Generator 📃📝")

st.caption("Made by Samagra Shrivastava with ♥")

topic = st.sidebar.text_input("Enter the topic you are interested")

if topic:
    inputs = {"topic": topic}
    with st.spinner("Crew's 👷‍♂️ are actively working to generate your post...⏳⏲"):
        result = crew.kickoff(inputs=inputs)
        st.subheader(result)
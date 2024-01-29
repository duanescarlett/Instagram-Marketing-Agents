from crewai import Agent
from langchain.agents import Tool 
from langchain.utilities import GoogleSerperAPIWrapper
from dotenv import load_dotenv

load_dotenv()

class SearchTools:
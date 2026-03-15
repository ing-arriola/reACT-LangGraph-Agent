import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

load_dotenv()

@tool
def triple(num:float) -> float:
    """ 
    param num: a number to be tripled
    returns: the tripled number
    """
    return num *3


tools = [triple,TavilySearch(max_results=1)]

llm = ChatGroq(model="llama-3.3-70b-versatile",api_key=os.getenv("GROQ_API_KEY")).bind_tools(tools)
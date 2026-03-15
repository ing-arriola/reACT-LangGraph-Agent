from dotenv import load_dotenv
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode
from urllib3 import response

from react import llm,tools

load_dotenv()

SYSTEM_PROMPT = """
You are a helpful assistant than can use tools to answer questions and help the user.
"""

def run_agent_reasoning(state:MessagesState) -> MessagesState:
    """
    Run the agent reasoning node.
    """
    response = llm.invoke([{"role":"system","content":SYSTEM_PROMPT},*state["messages"]])
    return {"messages":response}

tool_node = ToolNode(tools)
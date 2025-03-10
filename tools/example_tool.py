
# Load environment variables
from dotenv import load_dotenv
import requests


from langchain_openai import AzurechatopenAI
from langchain_core.tools import tool


from langchain_openai.embeddings import AzureopenAIEmbe
from langchain_core.agents import AgentAction


from langchain_core.messages import BaseMessage
from langchain_cpre.messages import HumanMessage


from langgraph.graph import END, StateGraph, START
from langgraph.graph import MessagesState
from langgraph.prebuilt import tools_condition, ToolNode
from langchain_core.runnables.config import RunnableConfig
from langchain_core.runnables import Runnable, RunnableConfig
from langchain_core.messages import ToolMessage
from langgraph.graph.message import AnyMessage, add_message
from langgraph.checkpoint.memory import MemorySaver


@tool("example_tool")
def example_tool(config: RunnableConfig, **kwargs) -> str:
    """
    This is an example tool.

    Args:
        param1 (str): Description of param1.
      param2 (str):Description of param2

    Returns:
        A string result.

    Raises:
        ValueError
    """


    try:
        response = requests.get("https://api.example.com/data", params=kwargs)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        raise ValueError(str(e))


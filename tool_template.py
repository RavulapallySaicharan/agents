tool_template = """
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
from langchain_core.runnables.config import RunnableConf
from langchain_core.runnables import Runnable, RunnableC
from langchain_core.messages import ToolMessage
from langgraph.graph.message import AnyMessage, add mess
from langgraph. checkpoint.memory import MemorySaver


@tool("{tool_name}")
def {tool_name}(config: RunnableConfig, **kwargs) -> {return_type}:
    \"""
    {tool_description}

    Args:
        {kwargs_description}

    Returns:
        {return_description}

    Raises:
        {error_type}
    \"""


    try:
        response - requests.get("{api_url}", params=kwargs)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        raise {error_type}(str(e))

"""
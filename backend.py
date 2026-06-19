from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_openai import ChatOpenAI 
from langgraph.checkpoint.memory import MemorySaver
from typing import List
from langgraph.graph.message import add_messages
from dotenv import load_dotenv

load_dotenv()

class ChatState(TypedDict):
    messages: Annotated[List[BaseMessage], add_messages]

llm = ChatOpenAI()

def chat_node(state: ChatState):
   
    #take user query from state
    messages = state['messages']

    #send to llm
    response = llm.invoke(messages)

    #response store state
    return {'messages': [response]}

check_pointer = MemorySaver()

graph = StateGraph(ChatState)

graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile(checkpointer=check_pointer)


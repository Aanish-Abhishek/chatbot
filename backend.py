from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_openai import ChatOpenAI 
from langgraph.checkpoint.sqlite import SqliteSaver
from typing import List
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
import sqlite3

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


def retrieve_all_threads():
    all_threads = set()
    for checkpoint in check_pointer.list(None):
        all_threads.add(checkpoint.config['configurable']['thread_id'])

    return list(all_threads)

#using same db in different thread
conn = sqlite3.connect(database='chatbot.db', check_same_thread=False)

check_pointer = SqliteSaver(conn=conn)

graph = StateGraph(ChatState)

graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot = graph.compile(checkpointer=check_pointer)

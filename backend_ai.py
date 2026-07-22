import os
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph , START , END
from typing import TypedDict, Annotated
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from dotenv import load_dotenv


load_dotenv()

class ChatState(TypedDict):
    messages : Annotated[list[BaseMessage] , add_messages]

llm = ChatMistralAI(
    model_name= "open-mistral-7b",
    temperature=0,
    api_key=os.getenv("MISTRAL_API_KEY")
)

def chat_node(state : ChatState):
    msg = state["messages"]
    response = llm.invoke(msg)
    return {"messages" : response}

checkpointer = MemorySaver()

graph = StateGraph(ChatState)
graph.add_node("chat_node" , chat_node)


graph.add_edge(START , "chat_node")
graph.add_edge("chat_node" , END)

aibot = graph.compile(checkpointer=checkpointer)
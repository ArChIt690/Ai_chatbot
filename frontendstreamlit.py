import streamlit as st
from backend_ai import aibot
from langchain_core.messages import HumanMessage

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []
CONFIG = {"configurable" : {"thread_id" : "thread1"}}

for message in st.session_state['message_history']:
    with st.chat_message(message["role"]):
        st.text(message["content"])

user_input = st.chat_input('Enter your input here:')

if user_input:
    st.session_state['message_history'].append({"role" : "user", "content" : user_input})
    with st.chat_message('user'):
        st.text(user_input)

    response = aibot.invoke({'messages' : [HumanMessage(content=user_input)]} , config=CONFIG)
    ai_message = response['messages'][-1].content
    st.session_state['message_history'].append({"role" : "assistant" , "content" : ai_message})
    with st.chat_message('assistant'):
        st.text(ai_message)
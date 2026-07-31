import streamlit as st
from backend_ai import aibot,retreive_threads
from langchain_core.messages import HumanMessage
import uuid

#*********************************utility functions ************************************
def session_tokens():
    thread_id= uuid.uuid4()
    return thread_id

def reset_chat():
    thread_id = session_tokens()
    add_thread(st.session_state['thread_id'])
    st.session_state['thread_id'] = thread_id
    st.session_state['message_history'] = []

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_thread']:
        st.session_state['chat_thread'].append(thread_id)

def load_conversation(thread_id):
    state= aibot.get_state(config = {"configurable" : {"thread_id" : thread_id}})
    return state.values.get('messages', [])

#*********************************Session ui********************************************
if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = session_tokens()

if 'chat_thread' not in st.session_state:
    st.session_state['chat_thread'] = retreive_threads()

#*********************************sidebar ui********************************************
st.sidebar.title('Ai Bot')

if st.sidebar.button('New Chat'):
    reset_chat()

st.sidebar.header('My conversations')

for thread in st.session_state['chat_thread'][::-1]:
    if st.sidebar.button(str(thread)):
        st.session_state['thread_id'] = thread
        messages = load_conversation(thread)

        temp_msg = []
        for msg in messages:
            if isinstance(msg , HumanMessage):
                role = 'user'
            else:
                role = 'assistant'

            temp_msg.append({
                'role' : role , 'content' : msg.content
            })

        st.session_state['message_history'] = temp_msg

#*********************************Main ui***********************************************
for message in st.session_state['message_history']:
    with st.chat_message(message["role"]):
        st.text(message["content"])

user_input = st.chat_input('Enter your input here:')

if user_input:
    st.session_state['message_history'].append({"role" : "user", "content" : user_input})
    with st.chat_message('user'):
        st.text(user_input)

    CONFIG = {"configurable" : {"thread_id" : st.session_state['thread_id']}}

    with st.chat_message('assistant'):
        ai_message = st.write_stream(
        message_chunk.content for message_chunk, meta_data in aibot.stream(
            {'messages' : [HumanMessage(content=user_input)]},
            config = CONFIG,
            stream_mode="messages",
        )
        )
    st.session_state['message_history'].append({'role' : 'assistant', 'content' : ai_message})
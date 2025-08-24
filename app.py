import streamlit as st
from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain_community.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()

## Streamlit UI
st.set_page_config(page_title='Chit Chat')
st.header('Hey,Whats up')

chat = ChatOpenAI(temperature=0.5)
if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [
        SystemMessage(content='You are a comedian AI assisstant')
    ]

##Fuction to load OpenAI model and get responses

def get_chatmodel_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

input = st.text_input('input: ',key='input')
response = get_chatmodel_response(input)

submit = st.button('Ask the question')

#If ask button is clicked

if submit:
    st.subheader('The response is')
    st.write(response)
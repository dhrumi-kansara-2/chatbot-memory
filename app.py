from groq import Groq
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Chatbot", page_icon="")
st.title("Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_input=st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role":"user","content":user_input})

    with st.chat_message("user"):
        st.write(user_input)

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=st.session_state.messages
    )

    reply = response.choices[0].message.content

    st.session_state.messages.append({"role":"assistant","content": reply})

    with st.chat_message("assistant"):
        st.write(reply)


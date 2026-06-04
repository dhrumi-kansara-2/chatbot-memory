from groq import Groq
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Chatbot", page_icon="")
st.title("Chatbot")

with st.sidebar: 
    st.title("Settings")

    system_prompt=st.text_area(
        "System Prompt",
        value="You are a helpful assistant",
        height=150
    )
    st.caption("Give the bot a role or personality.")


    temperature=st.slider("Temprature",
                          min_value=0.0,
                          max_value=1.0,
                          value=0.7,
                          step=0.1
                          )
    st.caption("Use low values for factual tasks, higher for creative writing.")

    
    if st.button("Clear chat history"):
        st.session_state.messages=[]
        st.rerun()

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

    with st.chat_message("assistant"):
        placeholder=st.empty()
        reply=""

        stream=client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role":"system","content":system_prompt}]+st.session_state.messages,
            temperature=temperature,
            stream=True
        )

        for chunk in stream:
            token = chunk.choices[0].delta.content or ""
            reply +=token
            placeholder.write(reply)

    st.session_state.messages.append({"role":"assistant","content": reply})




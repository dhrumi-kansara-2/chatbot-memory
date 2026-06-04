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

    max_messages=st.slider(
        "Max messages to remember",
        min_value=2,
        max_value=20,
        value=10,
        step=2
    )
    st.caption("Older messages beyond this limit will be forgotten.")

    
    if st.button("Clear chat history"):
        st.session_state.messages=[]
        st.rerun()

    st.divider()
    st.markdown("**Usage**")
    token_count=st.empty()

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
            messages=[{"role":"system","content":system_prompt}]+st.session_state.messages[-max_messages:],
            temperature=temperature,
            stream=True
        )

        for chunk in stream:
            token = chunk.choices[0].delta.content or ""
            reply +=token
            placeholder.write(reply)

    st.session_state.messages.append({"role":"assistant","content": reply})
    total_tokens=sum(len(m["content"].split()) for m in st.session_state.messages)
    token_count.caption(f"Estimated tokens used: ~{total_tokens}")




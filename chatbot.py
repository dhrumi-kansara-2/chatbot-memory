from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

messages=[]

print("Chatbot ready! Type 'quit' to exit.\n")

while True:
    user_input=input("You: ")

    if user_input.lower()=="quit":
        break

    messages.append({"role":"user","content":user_input})

    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=messages
    )

    reply=response.choices[0].message.content

    messages.append({"role":"assistant","content":reply})

    print(f"\nBot: {reply}\n")

    print(f"[Tokens used -- Input: {response.usage.prompt_tokens} \n Output:{response.usage.completion_tokens} \n Total:{response.usage.total_tokens}]")
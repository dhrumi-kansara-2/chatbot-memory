from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()


client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": "What is a context window?"}
    ]
)
 
print(response.choices[0].message.content)
print(f"\n--- Usage ---")
print(f"Input tokens:  {response.usage.prompt_tokens}")
print(f"Output tokens: {response.usage.completion_tokens}")
# 🤖 Chatbot with Conversation Memory

A simple AI chatbot built with Python, Groq, and Streamlit that remembers your entire conversation.

---

## ✨ Features

- 💬 **Conversation memory** : the bot remembers everything you said in the session
- ⚡ **Streaming responses** : replies appear word by word in real time
- 🎭 **Custom personas** : give the bot any personality via the system prompt
- 🌡️ **Temperature control** : adjust how creative or focused the responses are
- ✂️ **Smart trimming** : control how many messages the bot remembers
- 🗑️ **Clear history** : start fresh anytime with one click

---

## 🛠️ Tech Stack

- **Python** : core language
- **Groq API** : free, fast LLM inference (Llama 3.1)
- **Streamlit** : browser UI
- **python-dotenv** : manage API keys locally

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/chatbot-memory.git
cd chatbot-memory
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate       # Mac/Linux
venv\Scripts\activate          # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Get a free Groq API key

1. Go to [console.groq.com](https://console.groq.com)
2. Sign up and create an API key
3. No credit card needed

### 5. Create a `.env` file

```
GROQ_API_KEY=gsk_...
```

### 6. Run the app

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501` in your browser.

---

## 🎮 How to Use

| Setting | What it does |
|---|---|
| **System prompt** | Give the bot a role e.g. "You are a Socratic tutor" |
| **Temperature** | 0 = focused and precise, 1 = creative and unpredictable |
| **Max messages** | How many messages the bot remembers before forgetting older ones |
| **Clear history** | Wipe the conversation and start fresh |

---

## 📁 Project Structure

```
chatbot-memory/
├── .env                  # your API key (never commit this)
├── .gitignore            # ignores .env and .venv
├── app.py                # main Streamlit app
├── chatbot.py            # terminal chatbot (Day 2)
├── test.py               # first API call script (Day 1)
└── requirements.txt      # dependencies
```

---

## 🌐 Live Demo

👉 [your-app-name.streamlit.app](https://your-app-name.streamlit.app)

---

## 💡 How Memory Works

LLMs have no built-in memory : they are stateless. Every time you send a message, the entire conversation history is sent to the API as a list of messages. The model reads all of it from scratch and replies in context. What feels like memory is just that growing list being passed on every call.

---

## 📦 Dependencies

```
groq
streamlit
python-dotenv
```

---

## 🙌 Acknowledgements

Built as part of a 7-day learning project to understand how LLMs, context windows, and API calls actually work.
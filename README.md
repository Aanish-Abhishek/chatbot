# 🤖 Chatbot — Persistent Multi-Session AI Chat Application

A production-ready AI chatbot built with **LangGraph** and **OpenAI**, featuring persistent conversation memory across sessions using **SQLite**. Users can create multiple independent chat sessions, converse with the AI, and return later to resume any previous conversation with full history intact.

---

## ✨ Features

- 💬 **Multi-session chat** — create and manage multiple independent conversations
- 🧠 **Persistent memory** — conversation history saved to SQLite, survives app restarts
- ↩️ **Resume anytime** — return to any previous chat and pick up exactly where you left off
- 🔄 **Stateful conversation flow** — powered by LangGraph for reliable turn-by-turn state management
- ⚡ **OpenAI GPT integration** — intelligent, context-aware responses
- 🖥️ **Clean Streamlit UI** — simple and intuitive chat interface

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| AI Framework | LangGraph |
| LLM | OpenAI GPT (via OpenAI API) |
| Frontend | Streamlit |
| Database | SQLite |
| Language | Python |

---

## 🏗️ Architecture

```
User (Streamlit UI)
       │
       ▼
  Session Manager
  (Create / Load / Resume Chat Sessions)
       │
       ▼
  LangGraph State Machine
  (Manages conversation turns and state)
       │
       ▼
  OpenAI GPT
  (Generates AI responses)
       │
       ▼
  SQLite Database
  (Persists messages and session history)
```

### How It Works

1. User creates a new chat session or selects an existing one from the sidebar
2. Each session has a unique ID stored in SQLite
3. On every message, LangGraph manages the conversation state and routes to OpenAI
4. The AI response and full message history are persisted back to SQLite
5. When a user returns to an old session, the full history is loaded from the database and conversation resumes seamlessly

---

## 📁 Project Structure

```
chatbot/
│
├── frontend.py               # Streamlit UI
├── backend.py                # LangGraph and OpenAI logic
├── .gitignore.py
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- OpenAI API Key

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/your-username/chatbot.git
cd chatbot
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**
```bash
cp .env.example .env
```
Open `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

**5. Run the application**
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

---

## 💡 Usage

1. **Start a new chat** — click "New Chat" in the sidebar to create a fresh session
2. **Type your message** — enter your message in the chat input and press Enter
3. **Get AI response** — the assistant replies with full context of your conversation
4. **Switch sessions** — click any previous chat in the sidebar to resume it
5. **Resume anytime** — close the app and reopen it; all your chats are saved

---

## 📦 Dependencies

```txt
streamlit
langgraph
langchain
langchain-openai
openai
python-dotenv
```

---

## 🔑 Environment Variables

| Variable | Description | Required |
|---|---|---|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |

---

## 🗺️ Roadmap

- [ ] Add support for multiple AI models (Anthropic Claude, Gemini)
- [ ] Add chat export (PDF / Markdown)
- [ ] Add conversation search
- [ ] Deploy to Streamlit Community Cloud
- [ ] Add user authentication for multi-user support

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👤 Author

**Aanish**

---

## ⭐ If you found this useful, please consider giving it a star!

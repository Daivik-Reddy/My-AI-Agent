# 🤖 AI Agent Pro

> **A modern AI-powered chatbot built with Streamlit, LangChain, OpenAI, and DuckDuckGo Search.**
> Get real-time answers by combining the power of Large Language Models with live web search.

---

## ✨ Features

* 💬 **ChatGPT-like Interface** with a clean and responsive UI
* 🌐 **Real-Time Web Search** using DuckDuckGo
* 🧠 **Powered by OpenAI GPT Models**
* ⚡ **Fast Performance** with Streamlit resource caching
* 📝 **Conversation History** maintained during the session
* 🧹 **One-Click Chat Reset**
* 🎨 **Custom Dark Theme UI**
* 🔍 **Live Information Retrieval** for current events, news, sports, and more
* ❌ **Graceful Error Handling**

---

## 🛠️ Tech Stack

| Technology            | Purpose                         |
| --------------------- | ------------------------------- |
| **Python**            | Core Programming Language       |
| **Streamlit**         | Interactive Web Application     |
| **LangChain**         | AI Agent Framework              |
| **OpenAI API**        | Large Language Model            |
| **DuckDuckGo Search** | Real-Time Web Search            |
| **python-dotenv**     | Environment Variable Management |

---

## 📂 Project Structure

```text
AI-Agent-Pro/
│
├── app.py                 # Main Streamlit application
├── .env                   # OpenAI API Key (Ignored)
├── .gitignore             # Git ignored files
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

---

## 🚀 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Daivik-Reddy/AI-Agent-Pro.git
cd AI-Agent-Pro
```

---

### 2️⃣ Create a Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Create a `.env` File

```env
OPENAI_API_KEY=your_openai_api_key
```

---

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

---

## 📦 Required Packages

```text
streamlit
langchain
langchain-openai
langchain-community
python-dotenv
duckduckgo-search
openai
```

Or install everything using:

```bash
pip install -r requirements.txt
```

---

## 💻 How It Works

1. User enters a question.
2. LangChain creates an AI agent.
3. The agent searches the web using DuckDuckGo.
4. OpenAI processes the search results.
5. The AI generates an accurate, real-time response.
6. The response is displayed in a ChatGPT-style interface.

---

## 📸 Application Preview

```
🤖 AI Agent Pro

💬 Ask me anything!

👤 Who won the latest Formula 1 race?

🤖 Searching the web...

🏁 Max Verstappen won...
```

## 🔒 Environment Variables

Never commit your API keys.

Your `.gitignore` should include:

```gitignore
.env
__pycache__/
*.pyc
.DS_Store
```

---

## 🎯 Future Improvements

* ✅ Streaming responses
* ✅ Multiple LLM support (OpenAI, Gemini, Claude)
* ✅ Voice input/output
* ✅ Chat history database
* ✅ File upload support
* ✅ PDF & Document Q&A
* ✅ Image generation support
* ✅ User authentication
* ✅ Dark/Light theme switch

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Added awesome feature"
```

4. Push to GitHub

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## ⭐ Support

If you found this project helpful, please consider giving it a **⭐ Star** on GitHub.

It motivates further development and improvements!

---

## 📜 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

Daivik V Avalapati

GitHub: https://github.com/Daivik-Reddy

---

> **"Bringing AI and Real-Time Search Together for Smarter Conversations."** 🚀

<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">AI Chatbot</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Python](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/streamlit-1.60%2B-ff4b4b.svg)](https://streamlit.io/)

</div>

---

<p align="center"> A conversational AI web application built with Streamlit, LangGraph, and Mistral AI.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

AI Chatbot is a Streamlit-based chat application that uses Mistral AI to generate responses. LangGraph manages the conversation workflow, while SQLite checkpoints preserve chat threads so they can be reopened from the sidebar.

Each message is sent to the `open-mistral-7b` model through LangChain. The application keeps the active conversation in the Streamlit session and stores message history locally in `chatbot.db`.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get a local copy of the project running for development and testing purposes.

### Prerequisites

Install Python 3.12 or later and create a Mistral API key. You can verify the installed Python version with:

```
python --version
```

### Installing

Clone the repository and move into the project directory.

```
git clone <repository-url>
cd Ai_chatbot
```

Create and activate a virtual environment.

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the project dependencies.

```
pip install -r requirements.txt
```

Create a `.env` file in the project root and provide your Mistral API key.

```
MISTRAL_API_KEY=your_mistral_api_key
```

Start the application.

```
streamlit run frontendstreamlit.py
```

Open the local URL printed by Streamlit, normally `http://localhost:8501`, and send a message to begin a chat.

## 🔧 Running the tests <a name = "tests"></a>

This project does not currently include an automated test suite. Verify the application manually by starting Streamlit, sending a message, creating a new chat, and reopening a previous thread from the sidebar.

## 🎈 Usage <a name="usage"></a>

Enter a prompt in the chat input and submit it to receive a streamed response from Mistral AI. Select **New Chat** in the sidebar to begin another conversation. Existing conversation IDs appear under **My conversations** and can be selected to reload their saved message history.

Conversation checkpoints are stored in the local `chatbot.db` SQLite database. Removing this file clears all saved chat history.

## 🚀 Deployment <a name = "deployment"></a>

For deployment, configure `MISTRAL_API_KEY` as an environment variable on the host platform, then run the application with:

```
streamlit run frontendstreamlit.py --server.address 0.0.0.0
```

Persist `chatbot.db` on durable storage if conversation history should survive redeployments. Do not commit the `.env` file or expose API keys in client-side code.

## ⛏️ Built Using <a name = "built_using"></a>

- [Streamlit](https://streamlit.io/) - Web interface
- [LangChain](https://www.langchain.com/) - LLM application framework
- [LangGraph](https://langchain-ai.github.io/langgraph/) - Conversation workflow and checkpointing
- [Mistral AI](https://mistral.ai/) - Language model provider
- [SQLite](https://www.sqlite.org/) - Local conversation persistence

## ✍️ Authors <a name = "authors"></a>

- Project contributors - Initial work and development

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Mistral AI for language model access
- LangChain and LangGraph for the application framework
- Streamlit for the chat interface



# 🤖 AI Chatbox (LangChain + OpenAI)

A simple **terminal-based AI chatbox** built with **LangChain (v1+)** and **OpenAI**.
The chatbot behaves as a configurable **AI agent** using a system prompt and maintains conversation context during runtime.

---

##  Features

*  **Agent-based behavior** using a system prompt
*  **Conversation memory** (in-session)
*  **LangChain v1+ compliant**
*  **Fast and minimal setup**
*  **Terminal-based chat UI -- still no professional UI such as React or Vue JS avaliable**
*  **Customizable temperature & model**

---

## Tech Stack

* **Python 3.13.1+**
* **LangChain v1+**
* **OpenAI API**
* **python-dotenv**

---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/ai-agent-chatbox.git
cd ai-agent-chatbox
```



## Environment Setup

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

> ⚠️ Never commit your API key to version control.



## ▶️ Create a virtual environment


```bash
python3 -m venv venv
```


## ▶️ Activate the virtual environment

```bash
source venv/bin/activate

```

## ▶️ Install dependencies

```bash
pip install -r requirements.txt


```

## ▶️ Run the Chatbox





```bash
python3 agent.py
```



## To run without creating a virtual environment :

### Install dependencies

```bash
pip install langchain langchain-openai python-dotenv
```



## ▶️ Run the Chatbox



```bash
python3 agent.py
```

You should see:

```text
  Chatbot running. Type 'exit' to stop.
```



## Chatbox Behavior (System Prompt)

The chatbot is initialized with a **system message** that defines its personality and rules.

Example:

```text
You are a professional AI assistant.
You answer clearly and concisely.
You explain step by step when needed.
You are friendly and honest.
```

You can fully customize this prompt inside `agent.py`.



## Example Interaction

```text
You: What is LangChain?




Bot: LangChain is a framework for building applications powered by large language models...
```

> The chatbox intentionally adds **4 blank lines** between the user message and the AI response for readability.



#Project Structure

```text
AI-ChatBox/
│
├── agent.py          # Main chatbox logic
├── .env              # API key (ignored by git)
├── README.md         # Project documentation

```



## Customization

You can easily:

* Change the **AI personality**
* Adjust **temperature**
* Switch **OpenAI models**
* Add **streaming responses**
* Integrate **memory, tools, or RAG**



## LangChain v1 Notes

This project uses the **new LangChain architecture**:

* `langchain_core.messages`
* `ChatOpenAI.invoke()` instead of calling the model directly



## Future Improvements

* FastAPI backend
* WebSocket streaming
* Persistent memory
* Document-based Q&A (RAG)
* Multi-agent routing


## Acknowledgments

* [LangChain](https://www.langchain.com/)
* [OpenAI](https://openai.com/)

## github : ahmed3alali -- don't forget to follow me for more ! 
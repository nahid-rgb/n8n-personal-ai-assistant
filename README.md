# n8n Personal AI Assistant

A personal AI assistant built with **n8n, Streamlit, and Google Gemini**.

The assistant can understand user requests and use different tools to perform tasks such as managing calendars, emails, tasks, notes, and expenses.

## Features

* Answer general questions
* Search the web for current information
* Create and manage Google Calendar events
* Read and send Gmail messages
* Create, read, and delete Google Tasks
* Create and update notes in Google Docs
* Add and retrieve expenses using Google Sheets
* Perform calculations

## Tech Stack

* **n8n** — Workflow automation and AI Agent
* **Streamlit** — Chat interface
* **Google Gemini** — AI model
* **Python** — Frontend application
* **Docker** — Local n8n setup
* **Google APIs** — Calendar, Gmail, Tasks, Docs, and Sheets
* **SerpApi** — Google Search

## Project Structure

```text
n8n-personal-assistant/
├── app.py
├── main.py
├── test_webhook.py
├── sysprompt.md
├── pyproject.toml
├── uv.lock
├── .gitignore
└── README.md
```

## How It Works

```text
Streamlit
    ↓
n8n Webhook
    ↓
AI Agent
    ↓
Choose the required tool
    ↓
Google Calendar / Gmail / Tasks / Docs / Sheets / Search
    ↓
Response
    ↓
Streamlit
```

## Run the Project

### 1. Start n8n

Run n8n using Docker:

```cmd
docker run -it --rm --name n8n -p 5678:5678 -e GENERIC_TIMEZONE="Asia/Dhaka" -e TZ="Asia/Dhaka" -e N8N_ENFORCE_SETTINGS_FILE_PERMISSIONS=true -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

### 2. Install Python Dependencies

This project uses `uv`.

```cmd
uv sync
```

### 3. Start Streamlit

```cmd
uv run streamlit run app.py
```

## Note

The n8n workflow must be running and the required Google/Gemini credentials must be configured for the assistant to work.

This project is currently designed to run locally.

# LLM Search Agent Middleware

A flexible middleware layer between an LLM engine (currently **Ollama**) and a search engine (currently **SearxNG**). It provides:

- **Intent extraction** via LangChain's `LLMChain`
- **Web search retrieval** via LangChain's `SearxSearchWrapper`
- **Result filtering, scoring, and accumulation**
- **Answer synthesis** via LangChain's `LLMChain`
- **Multiple transport connectors**: CLI, HTTP REST API, WebSocket

This is **not** a standalone search engine. It acts as the glue between your preferred LLM backend and web search, making it easy to integrate dynamic search-driven capabilities into any application.

## Project Structure
```markdown
# LLM Search Agent Middleware

Aninterface that implements a **middleware layer** between an LLM engine (currently **Ollama**) and a search engine (currently **SearxNG**). It orchestrates:

This tool is **not** a standalone search engine. It acts as the glue between your LLM and your search backend, making it easy to integrate web search capabilities into conversational agents or other applications.

Performs an intent‑driven web search and generates answers via:

- **LangGraph** for stateful orchestration
- **LangChain** for LLM prompt handling & SearxNG tool
- **BFS/DFS** iterative retrieval with SearxNG suggestions

## Setup
1. Clone the repo
2. Copy `.env` as provided and adjust URLs if needed
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
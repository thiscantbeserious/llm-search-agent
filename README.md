# LLM Search Agent Middleware

> **WARNING**: This is currently being crafted, I will remove this message as soon as I consider it usable / shareable.

A flexible middleware layer between an LLM engine and a search engine.

Performs an agent‑driven web search and generates better answers as a knowledge base for LLMS.

### Supported LLMs:
 - Ollama (tested) 
 - OpenAI (untested)

### Supported Search-Engines:
- SearXNG

## Description:

This tool was created because I was frustrated with the quality of current attempts of a "web-search" in the LLM sector (not just Open-Source). It aims to generate a better web search experience to provide a better knowledge base for LLMs to generate their answers.

For example when you search for a specific package in Python, or even better provide a direct link it should be able to scan that link and follow it properly with specific agents that properly extract information from git-repos or documentation, not just randomly google stuff. Furthermore it should answer just as intended in the prompt, not just random informations that make non sense.

**Performs an intent‑driven web search and generates answers via:**

- **LangGraph** for stateful orchestration
- **LangChain** for LLM prompt handling & SearxNG tool
- **BFS/DFS** iterative retrieval with SearxNG suggestions


## Usage (CLI, mainly for testing):
```bash
   # either via poetry
   poetry run cmd "<your prompt here>"
   
   # or via python
   python cmd.py "<your prompt here>"
```

## Functionality:

- **Intent extraction** via LangChain's `LLMChain`
- **Web search retrieval** via LangChain's `SearxSearchWrapper`
- **Result filtering, scoring, and accumulation**
- **Answer synthesis** via LangChain's `LLMChain`
- **Multiple transport connectors**: CLI, HTTP REST API, WebSocket

## Setup
1. Clone the repo
2. Adjust `.env` as required (check `config.pg` for possible config)
3. Install:
   ```bash
   poetry install
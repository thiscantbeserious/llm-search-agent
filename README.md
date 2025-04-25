# LLM Search Agent

![CodeRabbit Pull Request Reviews](https://img.shields.io/coderabbit/prs/github/thiscantbeserious/llm-search-agent?utm_source=oss&utm_medium=github&utm_campaign=thiscantbeserious%2Fllm-search-agent&labelColor=171717&color=FF570A&link=https%3A%2F%2Fcoderabbit.ai&label=CodeRabbit+Reviews)

Performs an agent‑driven web search, that can be used both for the user as well as provide a knowdlege base for LLMs to provide answers that are not accessible trough sheer training alone.

This tool was created because I was frustrated with the quality of current attempts of a "web-search" in the LLM sector (not just Open-Source). It aims to generate a better web search experience to provide a better knowledge base for LLMs to generate their answers.

For example when you search for a specific package in Python, or even better provide a direct link it should be able to scan that link and follow it properly with specific agents that properly extract information from git-repos or documentation, not just randomly google stuff. Furthermore it should answer just as intended in the prompt, not just random informations that make non sense.

(Could also be seen as a flexible middleware layer between an LLM engine and a search engine).

**Performs an intent‑driven web search and generates answers via:**

- **LangGraph** for stateful orchestration
- **LangChain** for LLM prompt handling & SearxNG tool
- **BFS/DFS** iterative retrieval with SearxNG suggestions

> **WARNING**: This is currently being crafted, I will remove this message as soon as I consider it usable / shareable.

## Supported Technologies

<table border="0" cellspacing="0" cellpadding="5" style="border-collapse:collapse;border:none">
  <tr style="border:none">
    <td valign="top" style="border:none">
      <table>
        <thead>
          <tr><th >LLM</th><th>Status</th></tr>
        </thead>
        <tbody>
          <tr>
            <td><a href="https://github.com/ollama/ollama">ollama</a></td>
            <td><code>working</code></td>
          </tr>
          <tr>
            <td><a href="https://platform.openai.com">OpenAI API</a></td>
            <td><code>implemented</code>, <code>unverified</code></td>
          </tr>
        </tbody>
      </table>
    </td>
    <td valign="top" style="border:none">
      <table>
        <thead>
          <tr><th>Search Engine</th><th>Status</th></tr>
        </thead>
        <tbody>
          <tr>
            <td><a href="https://github.com/searxng/searxng">SearXNG</a></td>
            <td><code>development</code></td>
          </tr>
        </tbody>
      </table>
    </td>
    <td valign="top" style="border:none">
      <table>
        <thead>
          <tr><th>Transport Layer</th><th>Status</th></tr>
        </thead>
        <tbody>
          <tr><td>CLI Conversations</td><td><code>working</code></td></tr>
          <tr><td>HTTP REST API</td><td><code>implemented</code>, <code>testing</code></td></tr>
          <tr><td>WebSocket-Server</td><td><code>implemented</code>, <code>testing</code></td></tr>
        </tbody>
      </table>
    </td>
  </tr>
</table>

## Application Flow
<img src="flowchart.svg" alt="Flowchart" width="auto"/>

## Functionality

- **Intent extraction** via LangChain's `LLMChain`
- **Web search retrieval** via LangChain's `SearxSearchWrapper`
- **Result filtering, scoring, and accumulation**
- **Answer synthesis** via LangChain's `LLMChain`
- **Multiple transport connectors**: CLI, HTTP REST API, WebSocket

## Setup
1. Clone the repo
2. Adjust `.env` as required (check `config.py` for possible config)
3. Run `poetry install` in Terminal


## Usage via Terminal
| Command              | Description        |
|----------------------|--------------------|
| `poetry run cli`     | Start all Services |
| `poetry run cli cmd` | Commandline REPL   |
| `poetry run cli api` | HTTP REST API      |
| `poetry run cli ws`  | WebSocket API      |

<p align="center">
  <img src="lsa_icon_round.svg" width="220" height="220" alt="LMM Search Agent">
</p>

# LLM Search Agent

![CodeRabbit Pull Request Reviews](https://img.shields.io/coderabbit/prs/github/thiscantbeserious/llm-search-agent?utm_source=oss&utm_medium=github&utm_campaign=thiscantbeserious%2Fllm-search-agent&labelColor=171717&color=FF570A&link=https%3A%2F%2Fcoderabbit.ai&label=CodeRabbit+Reviews)

Performs an agent-driven web search that can be used both by the user and to provide a knowledge base for LLMs, delivering answers that are not accessible through sheer training alone (aka answers that are not constantly outdated).

It could also be seen as "Deep Research," but I refuse to call something "Deep Research" if we haven’t even solved the basics correctly yet.

This tool was created because I was frustrated with the quality of current attempts at a "web search" in the LLM sector (not just, but especially when looking at open source).

For example, when you search for a specific package in Python—or even better, provide a direct link—it should be able to scan that link and follow it properly with specific agents that accurately extract information from git repos or documentation, not just randomly Google stuff. Furthermore, it should answer exactly as intended in the prompt, not just provide random information that makes no sense.

(It could also be seen as a flexible middleware layer between an LLM engine and a search engine.)

**Performs an intent-driven web search and generates answers via:**

- **LangGraph** for stateful orchestration
- **LangChain** for LLM prompt handling & SearxNG tool
- **BFS/DFS** iterative retrieval with SearxNG suggestions

> **WARNING**: This is currently just a very basic prototype. I will remove this message as soon as I consider it usable/shareable. For example, right now it is aimed at one LLM engine, which will change in the future, enabling the capability to combine various sorts of LLM engines, local or remote alike. But that’s not going to come in the first version most likely (not sure about that).

## Supported Technologies

<table border="0" cellspacing="0" cellpadding="5" style="border-collapse:collapse;border:none">
  <tr style="border:none">
    <td valign="top" style="border:none">
      <table>
        <thead>
          <tr><th>LLM Engine</th><th>Status</th></tr>
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
            <td><a href="https://github.com/searxng/searxng">SearxNG</a></td>
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
          <tr><td>WebSocket Server</td><td><code>implemented</code>, <code>testing</code></td></tr>
        </tbody>
      </table>
    </td>
  </tr>
</table>

## Application Flow
<img src="flowchart.svg" alt="Flowchart" width="auto"/>

## Current Planning and Outlook

> I just want to have one prompt and get the results aggregated, cleaned up, and spoon-fed—reliably (because I’m lazy).

The basic idea behind this is pipelines: one pipeline per intent. So, say you want to search for code—you have a Code Pipeline. If you search for technical documentation, you will have a Tech-Doc Pipeline. If you search for research papers, you will have a Research-Paper Pipeline. Each is a specific pipeline. That given, this does sound complex, and theoretically you could already do it by manually controlling the search engines, but it should be as transparent and as easy as possible.

My idea is to implement that first in a specific way that works automatically via intent extraction from the user prompt and, afterwards, move toward giving users the ability to create their own pipelines for very specific tasks tailored to their workflow and use case (likely via .yml or .toml). Technically speaking, it might be smart not to connect to just one engine on both ends but rather to enable combinations of local and remote LLM engines in parallel.

We should not blind-fool ourselves into proprietary (LLM) search engines because we’re then very fragile with the outcome—not on a day-by-day basis but rather minute by minute. The model changes, they filter stuff, making matters worse—having the reliability that the functionality would not change or break completely. I will likely not implement a frontend for this. What I want to do is implement this first into something like [open-webui](https://github.com/open-webui/open-webui), for example through a simple function against our API.

I basically created this because I’ve been genuinely interested in this topic for a long time and feel like I can learn something from it.

## Features in a Nutshell

- **Intent extraction**
- **Web search retrieval**
- **Result filtering, scoring, and accumulation**
- **Answer synthesis**
- **Multiple transport connectors**: CLI, HTTP REST API, WebSocket

## Setup
1. Clone the repo
2. Adjust `.env` as required (check `config.py` for possible config)
3. Run `poetry install` in the terminal

## Usage via Terminal
| Command              | Description        |
|----------------------|--------------------|
| `poetry run cli`     | Start all services |
| `poetry run cli cmd` | Command-line REPL  |
| `poetry run cli api` | HTTP REST API      |
| `poetry run cli ws`  | WebSocket API      |

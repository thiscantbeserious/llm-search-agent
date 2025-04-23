# Agentic Web Search CLI Application

A standalone Python CLI for an intent-driven web search pipeline using LangGraph and LangChain.

## Project Structure
```
llm-agent-search/
├── .env                  # Configuration
├── README.md
├── requirements.txt
├── main.py               # CLI launcher
├── prompts/              # Customizable prompt overrides
│   ├── intent_extraction.prompt
│   └── answer_generation.prompt
├── templates/            # Default prompt templates
│   ├── intent_extraction.prompt
│   └── answer_generation.prompt
└── llm_search_agent/     # Main package
    ├── config.py
    ├── prompt_manager.py
    ├── orchestrator.py
    ├── pipeline/
    │   └── agents/
    │       ├── intent_agent.py
    │       ├── search_agent.py
    │       ├── filter_agent.py
    │       ├── scoring_agent.py
    │       └── answer_agent.py
    └── llm/
        └── ollama.py
```

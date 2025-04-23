import warnings
from langchain_openai import OpenAI
from llm_search_agent.config import Settings

cfg = Settings()


def get_openai_llm() -> OpenAI:
    """Return a configured OpenAI LLM."""
    return OpenAI(
        base_url=cfg.openai_api_url or None,
        api_key=cfg.openai_api_key,
        model=cfg.intent_model,
        temperature=cfg.intent_temperature,
    )

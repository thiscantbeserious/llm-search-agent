from langchain.llms.base import LLM

from llm_search_agent.config import Config
from llm_search_agent.llm.openai import OpenAIFactory
from llm_search_agent.llm.ollama import OllamaFactory

cfg = Config()


def load_llm_with_model(model: str, temperature: float = 1.0) -> LLM:
    """
    Load and return a cached LLM instance for the given model.
    Right now, this will return either an OpenAI or Ollama LLM based on the config.
    Later on we might want to refactor this to enable mixing instead.
    """
    if cfg.ollama_url:
        factory_cls = OllamaFactory
    elif cfg.openai_api_url:
        factory_cls = OpenAIFactory
    else:
        raise ValueError("No LLM factory available. Please either set OLLAMA_URL or OPENAI_API_URL in the config.")

    return factory_cls.get_llm(model, temperature)

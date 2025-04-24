from langchain_openai import OpenAI
from llm_search_agent.config import Config
from llm_search_agent.logger import get_logger
from llm_search_agent.llm.abstract_llm import AbstractLLMFactory

cfg = Config()
logger = get_logger(__name__)


class OpenAIFactory(AbstractLLMFactory[OpenAI]):
    @classmethod
    def _create_llm(cls, model: str, temperature: float) -> OpenAI:
        """Return a configured OpenAI LLM for the given model."""
        logger.debug("Loading OpenAI LLM against %s with model: %s", cfg.openai_api_url, model)
        return OpenAI(
            base_url=cfg.openai_api_url,
            api_key=cfg.openai_api_key,
            model=model,
            temperature=temperature,
        )

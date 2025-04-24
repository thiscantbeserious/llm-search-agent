from langchain_ollama import OllamaLLM
from llm_search_agent.config import Config
from llm_search_agent.logger import get_logger
from llm_search_agent.llm.abstract_llm import AbstractLLMFactory

cfg = Config()
logger = get_logger(__name__)


class OllamaFactory(AbstractLLMFactory[OllamaLLM]):
    @classmethod
    def _create_llm(cls, model: str, temperature: float) -> OllamaLLM:
        """Return a configured Ollama LLM for the given model."""
        logger.debug("Loading Ollama LLM against %s with model: %s", cfg.ollama_url, cfg.intent_model)
        return OllamaLLM(
            base_url=cfg.ollama_url,
            api_key=cfg.openai_api_key,
            model=model,
            temperature=temperature,
        )

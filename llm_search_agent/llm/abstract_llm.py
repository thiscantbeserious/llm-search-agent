from abc import ABC, abstractmethod
from functools import lru_cache
from typing import TypeVar, Generic
from langchain.llms.base import LLM

T = TypeVar("T", bound=LLM)


class AbstractLLMFactory(ABC, Generic[T]):
    """
    Cached Factory for LLMS - this is a singleton for each model.
    Subclasses should implement the _create_llm method to create the LLM.
    """

    @classmethod
    @lru_cache(maxsize=None)
    def get_llm(cls, model: str, temperature: float = 1.0) -> T:
        """ Get a cached LLM instance for the given model. """
        return cls._create_llm(model, temperature)

    @classmethod
    @abstractmethod
    def _create_llm(cls, model: str, temperature: float) -> T:
        """Implement this method to create the LLM, should return the LLM instance."""
        pass

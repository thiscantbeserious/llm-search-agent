from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Config(BaseSettings):
    # LMM Backend (either OLLAMA_URL or OPENAI_API_URL has to be specified - not both)
    ollama_url: str | None = Field(None, env="OLLAMA_URL")
    openai_api_url: str | None = Field(None, env="OPENAI_API_URL")
    openai_api_key: str | None = Field(None, env="OPENAI_API_KEY")

    # Search
    searxng_url: str = Field(..., env="SEARXNG_URL")
    max_depth: int = Field(3, env="MAX_DEPTH")
    max_width: int = Field(5, env="MAX_WIDTH")

    # Models
    intent_model: str = Field(..., env="INTENT_MODEL")
    intent_temperature: float = Field(1.0, env="INTENT_TEMPERATURE")

    answer_model: str = Field(..., env="ANSWER_MODEL")
    answer_temperature: float = Field(1.0, env="ANSWER_TEMPERATURE")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_ignore_empty=True,
    )

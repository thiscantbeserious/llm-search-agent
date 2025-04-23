from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    # Required fields
    openai_api_url: str = Field(..., env="OPENAI_API_URL")
    intent_model: str = Field(..., env="INTENT_MODEL")
    answer_model: str = Field(..., env="ANSWER_MODEL")
    searxng_url: str = Field(..., env="SEARXNG_URL")

    # Optional fields
    openai_api_key: str = Field("EMPTY_API_KEY", env="OPENAI_API_KEY")
    intent_temperature: float = Field(1.0, env="INTENT_TEMPERATURE")
    answer_temperature: float = Field(1.0, env="ANSWER_TEMPERATURE")
    max_depth: int = Field(3, env="MAX_DEPTH")
    max_width: int = Field(5, env="MAX_WIDTH")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_ignore_empty=True,
    )

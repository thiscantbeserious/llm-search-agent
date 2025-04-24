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

    # Extraction Model
    intent_model: str = Field(..., env="INTENT_MODEL")
    intent_temperature: float = Field(1.0, env="INTENT_TEMPERATURE")

    # Refinement Model
    refinement_model: str = Field(..., env="REFINEMENT_MODEL")
    refinement_temperature: float = Field(1.0, env="REFINEMENT_TEMPERATURE")

    # API
    api_host: str = Field("0.0.0.0", env="API_HOST")
    api_port: int = Field(8888, env="API_PORT")

    # Socket
    socket_host: str = Field("0.0.0.0", env="SOCKET_HOST")
    socket_port: int = Field(8765, env="SOCKET_PORT")

    # Model Config for Pydantic
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_ignore_empty=True,
    )

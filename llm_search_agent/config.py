from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    txt_server_url: str = Field(..., env="TXT_SERVER_URL")
    intent_model: str = Field(..., env="INTENT_MODEL")
    answer_model: str = Field(..., env="ANSWER_MODEL")
    searxng_url: str = Field(..., env="SEARXNG_URL")
    results_per_round: int = Field(..., env="RESULTS_PER_ROUND")
    max_depth: int = Field(..., env="MAX_DEPTH")
    max_queries: int = Field(..., env="MAX_QUERIES")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

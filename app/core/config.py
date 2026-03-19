from functools import lru_cache

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    app_name: str = "PimEyes"

    gpt_api_key: str

    rate_limit_per_minute: int = 10
    rate_limit_block_seconds: int = 60

    log_file: str = "logs/app.log"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


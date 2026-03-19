from functools import lru_cache

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    app_name: str = "PimEyes"

    gpt_api_key: str

    log_file: str = "logs/app.log"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


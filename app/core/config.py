from functools import lru_cache

from pydantic.v1 import AnyHttpUrl, BaseSettings, Field


class Settings(BaseSettings):
    app_name: str = "PimEyes"

    gpt_api_key: str = Field("ch", env="GPT_API_KEY")

    rate_limit_per_minute: int = 10
    rate_limit_block_seconds: int = 60

    AWS_ACCESS_KEY: str = "ch"
    AWS_SECRET_KEY: str = "ch"
    AWS_REGION: str = "ch"
    AWS_BUCKET_NAME: str = "ch"

    AWS_ENDPOINT_URL: str | None = None
    AWS_PUBLIC_BASE_URL: str | None = None

    log_file: str = "logs/app.log"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings() -> Settings:
    return Settings()


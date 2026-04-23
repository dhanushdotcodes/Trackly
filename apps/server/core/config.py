from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None

    model_config = SettingsConfigDict(
        # Loads from .env file if it exists
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    """
    Returns a cached instance of the Settings object.
    Using lru_cache ensures settings are only loaded once.
    """
    return Settings()


# Singleton instance for easy access outside of FastAPI dependencies
settings = get_settings()

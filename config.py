
import os

from pydantic.v1 import BaseSettings


class Settings(BaseSettings):
    TOKEN: str
    OPENAI_API_KEY: str

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), '.env')
        extra = "forbid"


config = Settings()

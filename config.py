from pydantic import SecretStr
from pydantic_settings import BaseSettings,  SettingsConfigDict

class Settings(BaseSettings):
    model_config= SettingsConfigDict(env_file=".enve", env_file_encoding="utf-8")
    secret_key : SecretStr
    algo : str = "HS256"
    expire_min : int = 30

setting = Settings()
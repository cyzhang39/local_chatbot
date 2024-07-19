from pydantic import BaseSettings
from core import constants

class Settings(BaseSettings):
    MODEL_URL: str
    
settings = Settings(_env_file=constants.DEFAULT_ENV_FILE,
                    _env_file_encoding='utf-8')
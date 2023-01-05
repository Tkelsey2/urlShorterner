#we can use LRU (Least Recently Used) strategy to optimise functions like "get_settings()" 
# by caching the loaded data once it is called, as it will not change.
from functools import lru_cache

#pydantic is installed as part of FastAPI
from pydantic import BaseSettings

#Creating a subclass of BaseSettings to manipulate the environmental variables
class Settings(BaseSettings):
    #setting variable value to local environment
    env_name: str = "local"
    #setting the websites domain
    base_url: str = "http://localhost:8000"
    #setting the databases address
    db_url: str = "sqlite:///./shortener.db"

    #as the values exist above, they are now used as a fallback from the external .env file, should that file corrupt etc.
    class Config:
        env_file = ".env"

#funtion returns an instance of the Settings class
@lru_cache
#^ decorator allows to cache the result of get_settings()
def get_settings() -> Settings:
    settings = Settings()
    print(f"loading settings for: {settings.env_name}")
    return settings
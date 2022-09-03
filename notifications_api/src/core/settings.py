from functools import lru_cache

from pydantic import BaseSettings


class RabbitMQSettings(BaseSettings):
    host: str = '127.0.0.1'
    port: int = 5672

    class Config:
        env_prefix = 'RABBITMQ_'


class Settings(BaseSettings):
    rabbitmq: RabbitMQSettings = RabbitMQSettings()


@lru_cache
def get_settings():
    return Settings()

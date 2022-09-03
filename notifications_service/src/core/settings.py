from functools import lru_cache

from pydantic import BaseSettings


class EmailSettings(BaseSettings):
    gmail_username: str
    gmail_password: str

    class Config:
        env_prefix = 'EMAIL_'


class RabbitMQSettings(BaseSettings):
    host: str = '127.0.0.1'
    port: int = 5672

    class Config:
        env_prefix = 'RABBITMQ_'


class Workers(BaseSettings):
    low_priority_email_n_workers: int = 1
    medium_priority_email_n_workers: int = 1
    high_priority_email_n_workers: int = 1

    class Config:
        env_prefix = 'WORKERS_'


class Settings(BaseSettings):
    email: EmailSettings = EmailSettings()
    rabbitmq: RabbitMQSettings = RabbitMQSettings()
    workers: Workers = Workers()


@lru_cache
def get_settings() -> Settings:
    return Settings()

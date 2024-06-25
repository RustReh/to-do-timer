from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # POSTGRES_USER: str = 'postgres'
    # POSTGRES_PASSWORD: str = 'password'
    # POSTGRES_PORT: str = '5436'
    # POSTGRES_DB: str = 'pomodoro'
    DB_NAME: str = 'pomodoro_db'
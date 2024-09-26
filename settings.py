from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_USER: str = 'postgres'
    DB_PASSWORD: str = '1111'
    DB_PORT: int = 5432
    DB_NAME: str = 'pomodoro_db'
    DB_HOST: str = 'localhost'
    CACHE_HOST: str = 'localhost'
    CACHE_PORT: int = 6379
    CACHE_DB: int = 0
    DB_DRIVER: str = 'postgresql+psycopg2'
    JWT_SECRET_KEY: str = 'secret_key'
    JWT_ENCODE_ALGORITHM: str = 'HS256'

    @property
    def DB_URL(self):
        return f'{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'
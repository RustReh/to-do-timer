from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:1111@localhost/pomodoro_db"


engine = create_engine(DATABASE_URL)

Session = sessionmaker(engine)


def get_db_session() -> Session:
    return Session

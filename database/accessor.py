from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import sessionmaker

from settings import Settings



engine = create_async_engine(Settings().DB_URL, future=True, echo=True, pool_pre_ping=True)

AsyncSessionFactory = async_sessionmaker(engine,
                                         autoflush=False,
                                         expire_on_commit=False
                                         )


async def get_db_session() -> AsyncSession:
    async with AsyncSessionFactory() as session:
        yield session

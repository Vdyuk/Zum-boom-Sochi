from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

# DB_URL_ASYNC = "postgresql+asyncpg://postgres:postgres@db:5432/postgres"
DB_URL_ASYNC = "postgresql+asyncpg://postgres:postgres@db:3389/postgres"

async_engine = create_async_engine(DB_URL_ASYNC, future=True, echo=True)
async_session = async_sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)


async def get_db() -> AsyncGenerator:
    session: AsyncSession = async_session()
    try:
        yield session
    finally:
        await session.close()
from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from .config import get_settings

settings = get_settings()

# Create async engine
if settings.DATABASE_URL is None:
    raise ValueError("DATABASE_URL is not set in environment variables")

engine = create_async_engine(settings.DATABASE_URL)


# Create async session factory
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """
    Dependency for FastAPI that provides an async database session.
    """
    async with AsyncSessionLocal() as session:
        yield session

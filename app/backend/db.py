from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from app.backend.db_config import settings


engine = create_async_engine(settings.DATABASE_URL, echo=True)
AsyncSessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as db:
        yield db


async def check_db_connection():
    try:
        async with engine.connect():
            return True
    except Exception:
        return False

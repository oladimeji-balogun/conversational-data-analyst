
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from ..core import get_settings 


Base = declarative_base()

settings = get_settings()
engine = create_async_engine(settings.database_url)
SessionLocal = async_sessionmaker(bind=engine, autoflush=False, autocommit=False, class_=AsyncSession)

async def get_db(): 
    async with SessionLocal() as session: 
        yield session


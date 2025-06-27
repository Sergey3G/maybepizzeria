from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


database_url = "sqlite:///./some_database.db"
engine = create_async_engine(database_url, echo=True)

AsyncSessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()


class Person(Base):
    __tablename__ = "people"

    user_id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String)
    age: int = Column(Integer)

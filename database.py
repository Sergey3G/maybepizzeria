from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

from custom_types.users import UserID, UserAge, UserName, UserEmail


database_url = "sqlite+aiosqlite:///./database.db"
engine = create_async_engine(database_url, echo=True)

AsyncSessionLocal = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id: UserID = Column(Integer, primary_key=True, index=True)
    name: UserName = Column(String)
    age: UserAge = Column(Integer)
    email: UserEmail = Column(String)

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String


SQLALCHEMY_DATABASE_URL = "sqlite:///./some_database.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})


class Base(DeclarativeBase):
    pass


class Person(Base):
    __tablename__ = "people"

    user_id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String)
    age: int = Column(Integer)


SessionLocal = sessionmaker(autoflush=False, bind=engine)

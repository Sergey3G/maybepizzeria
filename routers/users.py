from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import cast

from database import User

from dependecies import get_db

from models.users import UserCreate, UserDelete, UserUpdate

router = APIRouter()


@router.get("/api/users/{user_id}")
async def get_person(user_id, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(cast("ColumnElement[bool]", User.user_id == user_id)))
    person = result.scalars().first()
    if person is None:
        return JSONResponse(status_code=404, content={"message": "User is not found."})
    return person


@router.post("/api/users")
async def create_person(data: UserCreate, db: AsyncSession = Depends(get_db)):
    person = User(name=data.name, age=data.age, email=data.email)
    db.add(person)
    await db.commit()
    await db.refresh(person)
    return person


@router.put("/api/users")
async def edit_person(data: UserUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(cast("ColumnElement[bool]", User.user_id == data.user_id)))
    person = result.scalars().first()
    if person is None:
        return JSONResponse(status_code=404, content={"message": "User is not found."})
    person.age = data.age
    person.name = data.name
    await db.commit()
    await db.refresh(person)
    return person


@router.delete("/api/users")
async def delete_person(data: UserDelete, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(cast("ColumnElement[bool]", User.user_id == data.user_id)))
    person = result.scalars().first()
    if person is None:
        return JSONResponse(status_code=404, content={"message": "User is not found."})
    await db.delete(person)
    await db.commit()
    return person

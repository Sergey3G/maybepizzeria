from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from database import Person

from dependecies import get_db

from models.users import PersonCreate, PersonDelete, PersonUpdate, PersonOut

router = APIRouter()


@router.get("/api/users/{user_id}")
async def get_person(user_id, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Person).where(Person.user_id == user_id))
    person = result.scalars().first()
    if person is None:
        return JSONResponse(status_code=404, content={"message": "User is not found."})
    return person


@router.post("/api/users")
async def create_person(data: PersonCreate, db: AsyncSession = Depends(get_db)):
    person = Person(name=data.name, age=data.age)
    db.add(person)
    await db.commit()
    await db.refresh(person)
    return person


@router.put("/api/users")
async def edit_person(data: PersonUpdate, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Person).where(Person.user_id == data.user_id))
    person = result.scalars().first()
    if person is None:
        return JSONResponse(status_code=404, content={"message": "User is not found."})
    person.age = data.age
    person.name = data.name
    await db.commit()
    await db.refresh(person)
    return person


@router.delete("/api/users")
async def delete_person(data: PersonDelete, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Person).where(Person.user_id == data.user_id))
    person = result.scalars().first()
    if person is None:
        return JSONResponse(status_code=404, content={"message": "User is not found."})
    await db.delete(person)
    await db.commit()
    return person

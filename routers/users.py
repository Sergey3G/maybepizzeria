from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from database import Person

from dependecies import get_db

from models.users import PersonCreate, PersonDelete, PersonUpdate, PersonOut

router = APIRouter()


@router.get("/api/users/{user_id}")
async def get_person(user_id, db: Session = Depends(get_db)):
    person = db.query(Person).filter(Person.user_id == user_id).first()
    if person is None:
        return JSONResponse(status_code=404, content={"message": "User is not found."})
    return person


@router.post("/api/users")
async def create_person(data: PersonCreate, db: Session = Depends(get_db)):
    person = Person(name=data.name, age=data.age)
    db.add(person)
    db.commit()
    db.refresh(person)
    return person


@router.put("/api/users")
async def edit_person(data: PersonUpdate, db: Session = Depends(get_db)):
    person = db.query(Person).filter(Person.user_id == data.user_id).first()
    if person is None:
        return JSONResponse(status_code=404, content={"message": "User is not found."})
    person.age = data.age
    person.name = data.name
    db.commit()
    db.refresh(person)
    return person


@router.delete("/api/users")
async def delete_person(data: PersonDelete, db: Session = Depends(get_db)):
    person = db.query(Person).filter(Person.user_id == data.user_id).first()
    if person is None:
        return JSONResponse(status_code=404, content={"message": "User is not found."})
    db.delete(person)
    db.commit()
    return person

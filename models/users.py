from pydantic import BaseModel
from custom_types.users import PersonAge, PersonName, PersonID


class PersonBase(BaseModel):
    name: PersonName
    age: PersonAge


class PersonCreate(PersonBase):
    pass


class PersonUpdate(PersonBase):
    user_id: PersonID


class PersonDelete(PersonBase):
    user_id: PersonID


class PersonOut(PersonBase):
    user_id: PersonID

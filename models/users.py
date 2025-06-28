from pydantic import BaseModel
from custom_types.users import (UserID, UserAge, UserName, UserEmail, UserCity, UserStreet, UserApartment,
                                UserHouseNumber)


class UserBase(BaseModel):
    name: UserName
    age: UserAge
    email: UserEmail
    city: UserCity
    street: UserStreet
    house_number: UserHouseNumber
    apartment: UserApartment


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    user_id: UserID


class UserDelete(UserBase):
    user_id: UserID

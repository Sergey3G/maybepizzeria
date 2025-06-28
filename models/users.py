from pydantic import BaseModel
from custom_types.users import UserAge, UserName, UserID, UserEmail


class UserBase(BaseModel):
    name: UserName
    age: UserAge
    email: UserEmail


class UserCreate(UserBase):
    pass


class UserUpdate(UserBase):
    user_id: UserID


class UserDelete(UserBase):
    user_id: UserID

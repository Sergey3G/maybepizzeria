from typing import Annotated
from pydantic import Field, EmailStr

from custom_types.general import PositiveInt


UserName = Annotated[str, Field(..., min_length=1, max_length=20, description="user's name", example="Ivan")]
UserAge = Annotated[int, Field(..., ge=0, le=150, description="user's age", example=18)]
UserID = Annotated[int, Field(..., description="user's id", example=1)]
UserEmail = Annotated[EmailStr, Field(..., description="user's email", example="ivan@example.com")]
UserCity = Annotated[str, Field(...,min_length=2, description="user's city", example="Moscow")]
UserStreet = Annotated[str, Field(...,min_length=2, description="user's street", example="Tverskaya")]
UserHouseNumber = Annotated[PositiveInt, Field(..., description="user's house number", example=1)]
UserApartment = Annotated[PositiveInt | None, Field(description="user's apartment", example=1)]

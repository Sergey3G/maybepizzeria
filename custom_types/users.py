from typing import Annotated
from pydantic import Field, EmailStr


UserName = Annotated[str, Field(..., min_length=1, max_length=20, description="user's name", example="Ivan")]
UserAge = Annotated[int, Field(..., ge=0, le=150, description="user's age", example=18)]
UserID = Annotated[int, Field(..., description="user's id", example=1)]
UserEmail = Annotated[EmailStr, Field(..., description="user's email", example="ivan@example.com")]

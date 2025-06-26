from typing import Annotated
from pydantic import Field


PersonName = Annotated[str, Field(..., min_length=1, max_length=20, description="person's name", example="Sergey")]
PersonAge = Annotated[int, Field(..., ge=0, le=150, description="person's age", example=18)]
PersonID = Annotated[int, Field(..., description="person's id", example=1)]

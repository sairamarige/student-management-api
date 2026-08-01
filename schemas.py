from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class StudentCreate(BaseModel):
    name: str
    age: int = Field(gt=0)
    email: EmailStr
    course: str


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    email: Optional[EmailStr] = None
    course: Optional[str] = None


class StudentResponse(BaseModel):
    id: int
    name: str
    age: int
    email: EmailStr
    course: str

    class Config:
        from_attributes = True
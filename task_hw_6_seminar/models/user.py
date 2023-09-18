from pydantic import BaseModel, Field, EmailStr


class UserIn(BaseModel):
    firstname: str
    lastname: str
    email: EmailStr = Field(max_length=45)
    password: str = Field(min_length=6)

class User(BaseModel):
    id: int
    firstname: str
    lastname: str
    email: EmailStr = Field(max_length=45)

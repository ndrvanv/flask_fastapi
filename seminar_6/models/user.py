from pydantic import BaseModel, Field, EmailStr


class UserIn(BaseModel):
    username: str
    email: EmailStr = Field(max_length=45)
    password: str = Field(min_length=6)

class User(BaseModel):
    id: int
    username: str
    email: EmailStr = Field(max_length=45)

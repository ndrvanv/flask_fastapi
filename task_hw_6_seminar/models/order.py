from pydantic import BaseModel, Field, EmailStr
import datetime

class OrderIn(BaseModel):
    status: str


class Order(BaseModel):
    id: int
    user_id: int
    order_id: int
    order_date: str

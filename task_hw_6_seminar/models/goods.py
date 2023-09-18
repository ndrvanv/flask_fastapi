from pydantic import BaseModel, Field


class GoodsIn(BaseModel):
    name: str
    description: str = Field(min_length=496)
    price: float

class Goods(BaseModel):
    id: int
    name: str
    description: str = Field(min_length=496)
    price: float

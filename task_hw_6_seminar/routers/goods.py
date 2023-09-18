from fastapi import APIRouter, HTTPException
from task_hw_6_seminar.db import database, goods
from task_hw_6_seminar.models.goods import Goods, GoodsIn

router = APIRouter()


@router.get("/fake_goods/{count}")
async def create_note(count: int):
    for i in range(count):
        query = goods.insert().values(name=f'name{i}',
                                      description=f'description{i}@mail.ru',
                                      price=f'price{i}')
        await database.execute(query)
    return {'message': f'{count} fake users create'}


@router.post("/goods", response_model=GoodsIn)
async def create_goods(user: GoodsIn):
    query = goods.insert().values(name=goods.name, description=goods.description, price=goods.price)
    last_record_id = await database.execute(query)
    return {**goods.dict(), "id": last_record_id}


@router.get("/goods/", response_model=list[Goods])
async def read_goods():
    from sqlalchemy import select
    query = select(goods.c.id, goods.c.name, goods.c.description, goods.c.price)
    return await database.fetch_all(query)

@router.get("/goods/{goods_id}", response_model=Goods)
async def read_user(user_id: int):
    query = goods.select().where(goods.c.id == user_id)
    if not query:
        raise HTTPException(status_code=404, detail="Goods not found")
    return await database.fetch_one(query)

@router.delete("/goods/{goods_id}")
async def delete_user(user_id: int):
    query = goods.delete().where(goods.c.id == goods_id)
    await database.execute(query)
    return {'message': 'Goods deleted'}


from fastapi import APIRouter, HTTPException
from task_hw_6_seminar.db import database, users
from task_hw_6_seminar.models.user import User, UserIn

router = APIRouter()


@router.get("/fake_users/{count}")
async def create_note(count: int):
    for i in range(count):
        query = users.insert().values(firstname=f'firstname{i}',
                                      lastname=f'lastname{i}',
                                      email=f'mail{i}@mail.ru',
                                      password=f'password{i}')
        await database.execute(query)
    return {'message': f'{count} fake users create'}


@router.post("/users", response_model=UserIn)
async def create_user(user: UserIn):
    query = users.insert().values(firstname=user.firstname, lastname=user.lastname, email=user.email, password=user.password)
    last_record_id = await database.execute(query)
    return {**user.dict(), "id": last_record_id}


@router.get("/users/", response_model=list[User])
async def read_users():
    from sqlalchemy import select
    query = select(users.c.id, users.c.firstname, users.c.lastname, users.c.email)
    return await database.fetch_all(query)


@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    if not query:
        raise HTTPException(status_code=404, detail="User not found")
    return await database.fetch_one(query)


@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {'message': 'User deleted'}

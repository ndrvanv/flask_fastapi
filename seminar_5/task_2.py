from enum import Enum

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
# Создать API для получения списка фильмов по жанру. Приложение должно
# иметь возможность получать список фильмов по заданному жанру.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Movie с полями id, title, description и genre.
# Создайте список movies для хранения фильмов.
# Создайте маршрут для получения списка фильмов по жанру (метод GET).
# Реализуйте валидацию данных запроса и ответа.

app = FastAPI()
movies = []

class Movie(BaseModel):
    id: int
    title: str
    description: str
    genre: str

class MovieIn(BaseModel):
    title: str
    description: str
    genre: str

@app.get("/movies/{genre}", response_model=list[Movie])
async def get_movie(genre: str):
    result = []
    for movie in movies:
        if movie.genre == genre:
            result.append(movie)
    return result

@app.post("/movies/", response_model=Movie)
async def create_movie(new_movie: MovieIn):
    movies.append(
        Movie(id=len(movies) + 1, title=new_movie.title, description=new_movie.description, genre=new_movie.genre)
    )
    return movies[-1]


if __name__ == '__main__':
    uvicorn.run("task_2:app", host="127.0.0.1", port=8000, reload=True)
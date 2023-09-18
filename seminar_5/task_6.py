import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

# Создать веб-страницу для отображения списка пользователей. Приложение
# должно использовать шаблонизатор Jinja для динамического формирования HTML
# страницы.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте HTML шаблон для отображения списка пользователей. Шаблон должен
# содержать заголовок страницы, таблицу со списком пользователей и кнопку для
# добавления нового пользователя.
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja.


app = FastAPI()
templates = Jinja2Templates(directory="templates")


class UserOut(BaseModel):
    id: int
    name: str
    email: str

class UserIn(BaseModel):
    name: str
    email: str
    password: str

class User(UserIn):
    id: int

users = []
for i in range(10):
    users.append(User(
        id=i + 1,
        name=f'name_{i + 1}',
        email=f'email_{i + 1}',
        password='123'
    ))

@app.get("/users", response_class=HTMLResponse)
async def get_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

if __name__ == "__main__":
    uvicorn.run("task_hw_6_seminar:app", host="127.0.0.1", port=8000, reload=True)

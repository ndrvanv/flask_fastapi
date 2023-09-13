import logging
from typing import Optional
import uvicorn
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Создать API для управления списком задач. Приложение должно иметь
# возможность создавать, обновлять, удалять и получать список задач.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс Task с полями id, title, description и status.
# Создайте список tasks для хранения задач.
# Создайте маршрут для получения списка задач (метод GET).
# Создайте маршрут для создания новой задачи (метод POST).
# Создайте маршрут для обновления задачи (метод PUT).
# Создайте маршрут для удаления задачи (метод DELETE).
# Реализуйте валидацию данных запроса и ответа.

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


app = FastAPI()
tasks = []


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: str


class TaskIn(BaseModel):
    title: str
    description: Optional[str]
    status: str


@app.get("/task_1", response_model=list[Task])
async def root():
    return tasks


@app.post("/tasks/", response_model=list[Task])
async def create_task(new_task: TaskIn):
    tasks.append(
        Task(id=len(tasks) + 1,
        title=new_task.title,
        description=new_task.description,
        status=new_task.status
    ))
    return tasks

@app.put("/task_1/", response_model=Task)
async def edit_task(task_id: int, new_task: TaskIn):
    for i in range(0, len(tasks)):
        if tasks[i].id == task_id:
            current_task = tasks[task_id - 1]
            current_task.title = new_task.title
            current_task.description = new_task.description
            current_task.status = new_task.status
            return current_task
        raise HTTPException(status_code=404, detail="Task not found")



@app.delete("/task_1/", response_model=dict)
async def delete_task(task_id: int):
    for i in range(0, len(tasks)):
        if tasks[i].id == task_id:
            tasks.remove(tasks[i])
            return {'message': 'The task was deleted successfully'}
        raise HTTPException(status_code=404, detail="Task not found")

if __name__ == "__main__":
    uvicorn.run("task_1:app", host="127.0.0.1", port=8000, reload=True)

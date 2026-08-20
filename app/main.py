from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid
from datetime import datetime

app = FastAPI(
    title="Task Management API",
    description="Enterprise sample application for CI/CD + GitOps demonstration",
    version="1.0.0"
)

# In-memory storage (for demo purposes)
tasks_db = []

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

class Task(TaskCreate):
    id: str
    created_at: str

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "task-api"}

@app.get("/")
def root():
    return {"message": "Task Management API is running"}

@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task: TaskCreate):
    new_task = Task(
        id=str(uuid.uuid4()),
        title=task.title,
        description=task.description,
        completed=task.completed,
        created_at=datetime.utcnow().isoformat()
    )
    tasks_db.append(new_task)
    return new_task

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks_db

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: str):
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: str, updated_task: TaskCreate):
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db[index] = Task(
                id=task_id,
                title=updated_task.title,
                description=updated_task.description,
                completed=updated_task.completed,
                created_at=task.created_at
            )
            return tasks_db[index]
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: str):
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db.pop(index)
            return
    raise HTTPException(status_code=404, detail="Task not found")
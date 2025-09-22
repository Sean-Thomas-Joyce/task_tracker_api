from fastapi import FastAPI

app = FastAPI()

tasks = []


@app.get("/tasks")
async def list():
    return tasks


@app.post("/tasks")
async def create(task: dict):
    tasks.append(task)
    return task


@app.get("/tasks/{task_id}")
async def retrieve(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return {"error": "Task not found"}, 404


@app.put("/tasks/{task_id}")
async def update(task_id: int, updated_task: dict):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks[index] = updated_task
            return updated_task
    return {"error": "Task not found"}, 404


@app.delete("/tasks/{task_id}")
async def delete(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[index]
            return {"message": "Task deleted"}
    return {"error": "Task not found"}, 404

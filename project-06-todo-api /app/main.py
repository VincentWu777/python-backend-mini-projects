from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory storage
todos = []
next_todo_id = 1


class CreateTodoRequest(BaseModel):
    title: str

class UpdateTodoRequest(BaseModel):
    title: str



@app.post("/todos")
def create_todo(request: CreateTodoRequest):
    global next_todo_id

    todo = {
        "id": next_todo_id,
        "title": request.title,
        "completed": False,
    }

    todos.append(todo)
    next_todo_id += 1

    return todo


@app.get("/todos")
def list_todos():
    return todos


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, request: UpdateTodoRequest):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["title"] = request.title
            return todo

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )


@app.patch("/todos/{todo_id}/complete")
def complete_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            if todo["completed"]:
                return todo

            todo["completed"] = True
            return todo

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo["id"] == todo_id:
            deleted_todo = todos.pop(index)
            return deleted_todo

    raise HTTPException(
        status_code=404,
        detail="Todo not found"
    )




from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()

# In-memory todos for demonstration
todos = [
    {"id": 1, "title": "Learn FastAPI", "completed": False},
    {"id": 2, "title": "Build Todo API", "completed": True},
    {"id": 3, "title": "Study Pagination", "completed": False},
    {"id": 4, "title": "Write README", "completed": True},
    {"id": 5, "title": "Refactor Code", "completed": False},
]


@app.get("/todos")
def list_todos(
    completed: Optional[bool] = Query(default=None),
    limit: int = Query(default=10, ge=1, le=100),
    offset: int = Query(default=0, ge=0)
):
    filtered_todos = todos

    if completed is not None:
        filtered_todos = [
            todo for todo in filtered_todos
            if todo["completed"] == completed
        ]

    return filtered_todos[offset : offset + limit]
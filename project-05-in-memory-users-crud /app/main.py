from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# In-memory storage
users = []
next_user_id = 1


class CreateUserRequest(BaseModel):
    name: str
    email: str

class UpdateUserRequest(BaseModel):
    name: str
    email: str

@app.post("/users")
def create_user(request: CreateUserRequest):
    global next_user_id

    user = {
        "id": next_user_id,
        "name": request.name,
        "email": request.email
    }

    users.append(user)
    next_user_id += 1

    return user


@app.get("/users")
def list_users():
    return users


@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


@app.put("/users/{user_id}")
def update_user(user_id: int, request: UpdateUserRequest):
    for user in users:
        if user["id"] == user_id:
            user["name"] = request.name
            user["email"] = request.email
            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user["id"] == user_id:
            deleted_user = users.pop(index)
            return deleted_user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )
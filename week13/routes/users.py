# routes/users.py
# file contains all user related API endpoints

from fastapi import APIRouter, HTTPException
from schema import User, UserCreate
import json
import os

router = APIRouter()

DATA_FILE = "users.txt"

# Helper Functions
# Read users from file
def read_users():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        content = file.read()
        if content:
            return json.loads(content)
        return []

# Write users to file
def write_users(users):
    with open(DATA_FILE, "w") as file:
        json.dump(users, file)


# Generate next user ID
def get_next_id(users):
    if not users:
        return 1
    return max(user["id"] for user in users) + 1

# Routes
# POST /users and Create user
@router.post("/")
def create_user(user: UserCreate):
    users = read_users()
    new_id = get_next_id(users)

    new_user = {
        "id": new_id,
        "name": user.name,
        "email": user.email
    }

    users.append(new_user)
    write_users(users)

    return new_user


# GET /users then Get all users
@router.get("/")
def get_users():
    return read_users()

# IMPORTANT: Define /search BEFORE /{id}
# GET /users/search?q=
@router.get("/search")
def search_users(q: str):
    users = read_users()
    results = [user for user in users if q.lower() in user["name"].lower()]

    return results


# GET /users/{id}
@router.get("/{id}")
def get_user_by_id(id: int):
    users = read_users()

    for user in users:
        if user["id"] == id:
            return user

    raise HTTPException(status_code=404, detail="User not found")


# PUT /users/{id}
@router.put("/{id}")
def update_user(id: int, updated_user: UserCreate):
    users = read_users()

    for user in users:
        if user["id"] == id:
            user["name"] = updated_user.name
            user["email"] = updated_user.email
            write_users(users)
            return user

    raise HTTPException(status_code=404, detail="User not found")


# DELETE /users/{id}
@router.delete("/{id}")
def delete_user(id: int):
    users = read_users()

    for user in users:
        if user["id"] == id:
            users.remove(user)
            write_users(users)
            return {"message": "User deleted successfully"}

    raise HTTPException(status_code=404, detail="User not found")
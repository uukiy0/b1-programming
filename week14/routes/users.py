from fastapi import APIRouter, HTTPException
from user_store import UserStore

#Create a router instance for user related endpoints
router = APIRouter()

#initialize the UserStore with the file that will store user data
store = UserStore("users.txt")


# GET /users
# Returns all users stored in the file
@router.get("/users")
def get_users():
    #Load all users from the file and return them
    return store.load()


# POST /users
# Create a new user
@router.post("/users")
def create_user(user: dict):
    # Load existing users from the file
    users = store.load()

    #Check if a user with the same ID already exists
    if store.find_by_id(user["id"]):
        raise HTTPException(status_code=400, detail="User already exists")

    #add the new user to the list
    users.append(user)

    #Save updated user list back to the file
    store.save(users)

    return {"message": "User created"}


# PUT /users/{user_id}
# Updates an existing user by ID
@router.put("/users/{user_id}")
def update_user(user_id: int, updated_data: dict):
    # Call the UserStore update method
    success = store.update_user(user_id, updated_data)

    # If no user was found with that ID return 404
    if not success:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User updated"}


# DELETE /users/{user_id}
# Deletes a user by ID
@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    # Call the UserStore delete method
    success = store.delete_user(user_id)

    # If no user was found with that ID return 404
    if not success:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted"}
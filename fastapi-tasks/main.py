#import FastAPI framework to build the API 
# and import BaseModel to create data models for validation 
#import helper functions from controllers.py
from fastapi import FastAPI, HTTPException


from pydantic import BaseModel


from controllers import load_tasks, save_tasks, get_task, generate_new_id


#create the FastAPI application
app = FastAPI()


# This model represents a FULL task and is used when returning data
# Unique task ID
# Task title required
# Optional description
# Task status default = False

class Task(BaseModel):
    id: int                     
    title: str                   
    description: str | None = None  
    completed: bool = False      

#this model is used when CREATING a new task (POST request)
#(id is auto generated)
class TaskCreate(BaseModel):
    title: str
    description: str | None = None


#Root endpoint check if API is running
@app.get("/")
def root():
    return {"message": "FastAPI Task Manager is running"}


#get all tasks
#optional query parameter ?completed=true
@app.get("/tasks")
def get_tasks(completed: bool | None = None):

    #Load all tasks from file
    tasks = load_tasks()

    #If user adds ?completed=true or false then filter results
    if completed is not None:
        tasks = [task for task in tasks if task["completed"] == completed]

    return tasks


#Get statistics about tasks
@app.get("/tasks/stats")
def get_stats():

    tasks = load_tasks()

    #count total tasks
    total = len(tasks)

    #count completed tasks
    completed = len([task for task in tasks if task["completed"]])

    #count pending tasks
    pending = total - completed

    #calculate completion percentage
    percentage = (completed / total * 100) if total > 0 else 0

    return {
        "total_tasks": total,
        "completed_tasks": completed,
        "pending_tasks": pending,
        "completion_percentage": percentage,
    }


#Get a single task by ID
@app.get("/tasks/{task_id}")
def get_single_task(task_id: int):

    #Uses helper function (returns 404 if not found)
    return get_task(task_id)


# Create a new task
@app.post("/tasks")
def create_task(task: TaskCreate):

    # Load existing tasks
    tasks = load_tasks()

    # Create a new task dictionary
    # Auto-generate ID
    # Default value
    new_task = {
        "id": generate_new_id(tasks),   
        "title": task.title,
        "description": task.description,
        "completed": False,             
    }

    #Add new task to list
    tasks.append(new_task)

    # Save updated list back to file
    save_tasks(tasks)

    return new_task


# Update an existing task
@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: TaskCreate):

    tasks = load_tasks()

    # Find the task by ID
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated_task.title
            task["description"] = updated_task.description
            save_tasks(tasks)
            return task

    # If task not found return 404 error
    raise HTTPException(status_code=404, detail="Task not found")


# Delete a single task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):

    tasks = load_tasks()

    #Create new list without the deleted task
    new_tasks = [task for task in tasks if task["id"] != task_id]

    # If no task was removed ID didnt exist
    if len(tasks) == len(new_tasks):
        raise HTTPException(status_code=404, detail="Task not found")

    #Save updated list
    save_tasks(new_tasks)

    return {"message": "Task deleted successfully"}


# Delete ALL tasks
@app.delete("/tasks")
def delete_all_tasks():

    # Save empty list (clears file)
    save_tasks([])

    return {"message": "All tasks deleted successfully"}
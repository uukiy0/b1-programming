#convert Python dictionaries to JSON and back
import json

#work with file paths and check if files exist
import os

#return proper HTTP error messages (like 404 Not Found)
from fastapi import HTTPException


# get the absolute path of this files folder
#makes sure Python always finds tasks.txt 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#create the full path to tasks.txt inside this folder
FILE_NAME = os.path.join(BASE_DIR, "tasks.txt")


def load_tasks():
    """
    This function reads all tasks from tasks.txt.
    It returns a list of tasks (as dictionaries).
    """

    #if the file does not exist yet return an empty list
    if not os.path.exists(FILE_NAME):
        return []

    tasks = []

    #open the file in read mode
    with open(FILE_NAME, "r") as file:

        #read the file line by line
        for line in file:

            #remove extra spaces and newline characters
            line = line.strip()

            #only process non empty lines
            if line:
                #convert JSON text into a Python dictionary
                tasks.append(json.loads(line))

    #return the list of tasks
    return tasks


def save_tasks(tasks):
    """
    This function saves all tasks back to tasks.txt.
    It overwrites the entire file each time.
    """

    #open file in write mode to clear old content
    with open(FILE_NAME, "w") as file:

        #loop through each task in the list
        for task in tasks:

            #Convert dictionary to JSON and write one task per line
            file.write(json.dumps(task) + "\n")


def get_task(task_id: int):
    """
    This function finds a task by its ID.
    If the task exists, it returns it.
    If not, it raises a 404 error.
    """

    #Load all tasks from file
    tasks = load_tasks()

    #Search for the matching task
    for task in tasks:
        if task["id"] == task_id:
            return task

    #if not found return HTTP 404 error
    raise HTTPException(status_code=404, detail="Task not found")


def generate_new_id(tasks):
    """
    This function generates the next task ID.
    IDs start from 1 and increase by 1.
    """

    #if there are no tasks yet start with ID 1
    if not tasks:
        return 1

    #or else find the highest ID and add 1
    return max(task["id"] for task in tasks) + 1
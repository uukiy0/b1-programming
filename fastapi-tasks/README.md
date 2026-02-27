Final Project
Isabelle Humaloja Skarsten
email: 
Isabelle.HumalojaSkarsten@Student.HTW-Berlin.de

Final FastAPI project: Build a complete FastAPI backend that manages tasks
through a RESTful API, storing all data in a plain text
file for persistence across server restarts.
Uses JSON Lines format in a simple .txt file4one task
per line, easy to read, parse, and understand whilst
learning backend fundamentals.

The application allows users to:

- Create tasks
- View all tasks
- View a single task
- Update tasks
- Delete tasks
- Filter tasks by completion status
- Delete all tasks
- View task statistics


install dependencies by 
pip install fastapi uvicorn

run:
uvicorn main:app --reload

Swagger URL:
http://127.0.0.1:8000/docs
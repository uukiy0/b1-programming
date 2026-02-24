# week14/main.py

from fastapi import FastAPI
from routes.users import router

# Create the main FastAPI application instance
app = FastAPI()

# Include the user router so all user related endpoints
# GET, POST, PUT, DELETE become part of this app
app.include_router(router)
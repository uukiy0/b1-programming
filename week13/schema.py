# schema.py
# This file contains our data models using Pydantic

from pydantic import BaseModel


# Model for creating a user (input model)
class UserCreate(BaseModel):
    name: str
    email: str


# Model for returning a user (output model)
class User(BaseModel):
    id: int
    name: str
    email: str
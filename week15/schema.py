# week14/schema.py

from pydantic import BaseModel, EmailStr


# UserCreate model chooses the structure of data
# required when creating a new user
# validates incoming request data automatically
class UserCreate(BaseModel):
    # Name must be a string
    name: str

    # Email must be a valid email address (validated by Pydantic)
    email: EmailStr
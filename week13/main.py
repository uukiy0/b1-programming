# main.py
# This is the main entry point of our FastAPI application

from fastapi import FastAPI
from routes import users  # Import users router

# Create FastAPI app instance
app = FastAPI(
    title="User Management API",
    description="Simple API for managing users using FastAPI",
    version="1.0.0"
)

# Include user routes
app.include_router(users.router, prefix="/users", tags=["Users"])


# Root endpoint,,sbasic health check
@app.get("/")
def root():
    return {"status": "healthy", "message": "API is running"}


# Extra health endpoint
@app.get("/health")
def health():
    return {"status": "OK", "details": "Everything is working fine"}
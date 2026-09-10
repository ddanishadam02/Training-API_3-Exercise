from fastapi import FastAPI

# Initialize FastAPI app
app = FastAPI(
    title="My CRUD API",
    description="API to manage user data with POST, GET, PUT, and DELETE methods.",
    version="0.1.0",
)

# main.py
from fastapi import FastAPI

app = FastAPI()

@ app.get("/")
def read_root():
    return {
        "success": True,
        "message": "Welcome to Sling Academy Public API"
    } 

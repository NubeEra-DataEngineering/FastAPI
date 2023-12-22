# File: main.py
from fastapi import FastAPI, BackgroundTasks
import time

app = FastAPI()

def background_task(message: str):
    time.sleep(5)
    print(f"Background Task Completed: {message}")

@app.get("/")
async def read_root(background_tasks: BackgroundTasks):
    background_tasks.add_task(background_task, "Hello from the background!")

    return {"message": "Hello, World!"}

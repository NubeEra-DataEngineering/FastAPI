# File: background_task.py
import time

def background_task(message: str):
    time.sleep(5)
    print(f"Background Task Completed: {message}")

if __name__ == "__main__":
    message = "Hello from the background!"
    print(f"Triggering Background Task: {message}")
    background_task(message)
    print("Main Program Completed")

# File: main.py
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Mount the 'static' folder to serve static files (e.g., style.css)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize Jinja2Templates for HTML rendering
templates = Jinja2Templates(directory="templates")

# Counter variable
counter = 0

# Routes
@app.get("/", response_class=HTMLResponse)
async def read_counter(request: Request):
    return templates.TemplateResponse("counter.html", {"request": request, "count": counter})

from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()
templates = Jinja2Templates(directory = BASE_DIR / "templates")
app.mount("/static", StaticFiles(directory = BASE_DIR / "static"), name="static")

items = ["사과", "바나나", "오렌지"]


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request, message: str = "Home!"):
    return templates.TemplateResponse(request, "index.html", {"title": "home", "message": message, "items": items})


@app.get("/tomato", response_class=HTMLResponse)
def read_tomato(request: Request, message: str = "Tomato!"):
    return templates.TemplateResponse(request, "index.html", {"title": "tomato", "message": message, "items": items})


@app.get("/tomato/{message}", response_class=HTMLResponse)
def read_tomato_path(request: Request, message: str):
    return templates.TemplateResponse(request, "index.html", {"title": "tomato", "message": message, "items": items})

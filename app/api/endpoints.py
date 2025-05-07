from fastapi import APIRouter
from app.models.schemas import LogEntry
from app.services.log_handler import save_log
from fastapi.responses import HTMLResponse
from fastapi import Form
from fastapi.responses import FileResponse
import os
from datetime import datetime
from app.models.schemas import MealLog
from app.services.log_handler import save_meal_log

router = APIRouter()

@router.get("/home")
def serve_home():
    path = os.path.join("static", "home.html")
    return FileResponse(path, media_type="text/html")


@router.post("/log", response_class=HTMLResponse)
def post_log(
    bg: float = Form(...),
    trend: str = Form(...),
    notes: str = Form(...)
):
    now = datetime.now()
    log = LogEntry(
        timestamp=now,  # <- handled here
        bg=bg,
        trend=trend,
        notes=notes
    )
    save_log(log)
    return """
    <html>
        <head><title>Logged</title></head>
        <body>
            <h2>Logged! Thank you.</h2>
            <a href="/home">Log another</a>
        </body>
    </html>
    """


@router.get("/meal", response_class=FileResponse)
def serve_meal_form():
    return FileResponse("static/meal_log.html", media_type="text/html")

@router.post("/log-meal", response_class=HTMLResponse)
def log_meal(
    meal: str = Form(...),
    carbs: int = Form(...),
    protein: int = Form(...),
    fats: int = Form(...),
    pre_bg: float = Form(...),
    notes: str = Form(...)
):
    now = datetime.now()
    meal_log = MealLog(
        date=now.strftime("%Y-%m-%d"),
        time=now.strftime("%H:%M"),
        meal=meal,
        carbs=carbs,
        protein=protein,
        fats=fats,
        pre_bg=pre_bg,
        notes=notes
    )
    save_meal_log(meal_log)
    return """
    <html>
        <head><title>Meal Logged</title></head>
        <body>
            <h2>Meal Logged! Thank you.</h2>
            <a href="/meal">Log another meal</a>
        </body>
    </html>
    """
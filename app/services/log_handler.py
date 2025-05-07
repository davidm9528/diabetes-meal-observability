import os
import json
from datetime import datetime
from app.models.schemas import LogEntry, MealLog

# --- Utility ---
def _timestamped_filename():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def _write_json(log_obj, path):
    with open(path, "w") as f:
        json.dump(log_obj.dict(), f, indent=2)

def _write_txt(content, path):
    with open(path, "w") as f:
        f.write(content)

# --- CGM Log ---
from fastapi.encoders import jsonable_encoder

def save_log(log: LogEntry):
    log_dir = "logs/cgm"
    os.makedirs(log_dir, exist_ok=True)

    log_date = log.timestamp.strftime("%Y-%m-%d")
    file_path = os.path.join(log_dir, f"{log_date}.json")

    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(jsonable_encoder(log))

    with open(file_path, "w") as f:
        json.dump(logs, f, indent=2)


# --- Meal Log ---
def save_meal_log(log: MealLog):
    log_dir = "logs/meals"
    os.makedirs(log_dir, exist_ok=True)

    filename = f"{log.date}.json"
    file_path = os.path.join(log_dir, filename)

    # If file exists, load it; else start a new list
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    # Append the new log
    logs.append(log.dict())

    # Save updated log list
    with open(file_path, "w") as f:
        json.dump(logs, f, indent=2)

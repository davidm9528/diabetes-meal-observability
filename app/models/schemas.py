from pydantic import BaseModel
from datetime import datetime

class LogEntry(BaseModel):
    timestamp: datetime
    bg: float
    trend: str
    notes: str

from pydantic import BaseModel

class MealLog(BaseModel):
    date: str
    time: str
    meal: str
    carbs: int
    protein: int
    fats: int
    pre_bg: float
    notes: str

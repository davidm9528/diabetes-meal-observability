from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.endpoints import router

app = FastAPI()

app.include_router(router)
app.mount("/static", StaticFiles(directory="static"), name="static")

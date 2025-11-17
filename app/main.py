from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .controllers import router as web_router
from .models import init_db

app = FastAPI(title="Cupcakes Gourmet App")

init_db()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(web_router)

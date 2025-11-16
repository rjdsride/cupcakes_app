from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .controllers import router as web_router

app = FastAPI(title="Cupcakes Gourmet App")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(web_router)


# uvicorn app.main:app --reload

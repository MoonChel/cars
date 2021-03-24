from fastapi import FastAPI

from . import handlers
from .models import db
from .settings import DB_URL


app = FastAPI()

app.include_router(handlers.router)


@app.on_event("startup")
async def startup():
    print("DB started")
    await db.set_bind(DB_URL)
    await db.gino.create_all()


@app.on_event("shutdown")
async def shutdown():
    print("DB exit")
    await db.pop_bind().close()

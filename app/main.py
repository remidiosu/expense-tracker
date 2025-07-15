from fastapi import FastAPI
from fastapi.security import HTTPBearer
from contextlib import asynccontextmanager

from prometheus_client import start_http_server
from app.routes import router
from app.db import init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router)

start_http_server(9100)  # Prometheus on separate port


@app.get("/")
def read_root():
    return {"status": "ok"}

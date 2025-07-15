import time
from contextlib import asynccontextmanager

from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.db import init_db
from app.metrics import REQUEST_COUNT, REQUEST_LATENCY
from app.routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router)

Instrumentator().instrument(app).expose(app)


@app.middleware("http")
async def metrics_middleware(request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    path = request.url.path
    REQUEST_COUNT.labels(method=request.method, endpoint=path).inc()
    REQUEST_LATENCY.labels(endpoint=path).observe(process_time)

    return response


@app.get("/")
def read_root():
    return {"status": "ok"}

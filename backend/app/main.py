from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1.market import router as market_router
from app.api.v1.stocks import router as stocks_router
from app.api.websockets import router as ws_router
from app.core.config import settings
from app.services.market_data import market_data_service


@asynccontextmanager
async def lifespan(_: FastAPI):
    await market_data_service.start()
    yield


app = FastAPI(title=settings.app_name, version=settings.app_version, lifespan=lifespan)
app.include_router(stocks_router, prefix="/api/v1")
app.include_router(market_router, prefix="/api/v1")
app.include_router(ws_router)


@app.get("/health")
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}

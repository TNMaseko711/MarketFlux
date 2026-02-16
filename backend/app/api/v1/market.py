from fastapi import APIRouter

from app.services.market_data import market_data_service

router = APIRouter(prefix="/market", tags=["market"])


@router.get("/overview")
def market_overview():
    return market_data_service.overview()

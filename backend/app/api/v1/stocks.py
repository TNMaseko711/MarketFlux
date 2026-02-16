from fastapi import APIRouter, HTTPException

from app.services.market_data import market_data_service

router = APIRouter(prefix="/stocks", tags=["stocks"])


@router.get("")
def list_stocks() -> list[str]:
    return market_data_service.symbols()


@router.get("/{symbol}/price")
def current_price(symbol: str):
    tick = market_data_service.latest_price(symbol.upper())
    if not tick:
        raise HTTPException(status_code=404, detail="Symbol not found")
    return tick


@router.get("/{symbol}/history")
def price_history(symbol: str, limit: int = 120):
    symbol = symbol.upper()
    data = market_data_service.history(symbol=symbol, limit=limit)
    if not data:
        raise HTTPException(status_code=404, detail="Symbol not found")
    return data


@router.get("/{symbol}/indicators")
def stock_indicators(symbol: str):
    metrics = market_data_service.indicators(symbol.upper())
    if not metrics:
        raise HTTPException(status_code=404, detail="Symbol not found")
    return metrics

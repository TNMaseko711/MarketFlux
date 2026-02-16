import asyncio

from fastapi import APIRouter, WebSocket

from app.services.market_data import market_data_service

router = APIRouter(tags=["websockets"])


@router.websocket("/ws/stocks/{symbol}")
async def stream_symbol(websocket: WebSocket, symbol: str) -> None:
    symbol = symbol.upper()
    await websocket.accept()
    try:
        while True:
            tick = market_data_service.latest_price(symbol)
            metrics = market_data_service.indicators(symbol)
            await websocket.send_json(
                {
                    "tick": tick.model_dump(mode="json") if tick else None,
                    "indicators": metrics.model_dump(mode="json") if metrics else None,
                }
            )
            await asyncio.sleep(0.5)
    finally:
        await websocket.close()

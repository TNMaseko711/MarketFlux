from datetime import datetime
from pydantic import BaseModel, Field


class PriceTick(BaseModel):
    symbol: str
    timestamp: datetime
    price: float = Field(..., gt=0)
    volume: int = Field(..., ge=0)


class IndicatorSnapshot(BaseModel):
    symbol: str
    timestamp: datetime
    sma_20: float | None
    ema_20: float | None
    rsi_14: float | None
    z_score: float | None
    anomaly: bool = False


class MarketOverview(BaseModel):
    tracked_symbols: int
    latest_prices: dict[str, float]
    anomaly_count: int

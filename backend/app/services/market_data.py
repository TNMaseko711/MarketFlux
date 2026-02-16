from __future__ import annotations

import asyncio
import random
from collections import defaultdict, deque
from datetime import UTC, datetime

from app.core.config import settings
from app.models import IndicatorSnapshot, MarketOverview, PriceTick
from app.services.indicator_engine import RollingIndicatorEngine


class MarketDataService:
    def __init__(self) -> None:
        self._history: dict[str, deque[PriceTick]] = defaultdict(lambda: deque(maxlen=2000))
        self._indicators: dict[str, IndicatorSnapshot] = {}
        self._engines = {symbol: RollingIndicatorEngine() for symbol in settings.symbols}
        self._prices = {symbol: random.uniform(80, 300) for symbol in settings.symbols}
        self._running = False

    async def start(self) -> None:
        if self._running:
            return
        self._running = True
        asyncio.create_task(self._stream_prices())

    async def _stream_prices(self) -> None:
        while self._running:
            for symbol in settings.symbols:
                drift = random.uniform(-1.2, 1.2)
                self._prices[symbol] = max(1, self._prices[symbol] + drift)
                tick = PriceTick(
                    symbol=symbol,
                    timestamp=datetime.now(UTC),
                    price=round(self._prices[symbol], 2),
                    volume=random.randint(10_000, 1_000_000),
                )
                self._history[symbol].append(tick)
                stats = self._engines[symbol].update(tick.price)
                self._indicators[symbol] = IndicatorSnapshot(
                    symbol=symbol,
                    timestamp=tick.timestamp,
                    sma_20=stats["sma_20"],
                    ema_20=stats["ema_20"],
                    rsi_14=stats["rsi_14"],
                    z_score=stats["z_score"],
                    anomaly=bool(stats["anomaly"]),
                )
            await asyncio.sleep(settings.update_interval_seconds)

    def symbols(self) -> list[str]:
        return settings.symbols

    def latest_price(self, symbol: str) -> PriceTick | None:
        if symbol not in self._history or not self._history[symbol]:
            return None
        return self._history[symbol][-1]

    def history(self, symbol: str, limit: int = 120) -> list[PriceTick]:
        return list(self._history[symbol])[-limit:]

    def indicators(self, symbol: str) -> IndicatorSnapshot | None:
        return self._indicators.get(symbol)

    def overview(self) -> MarketOverview:
        latest = {
            symbol: self._history[symbol][-1].price
            for symbol in settings.symbols
            if self._history[symbol]
        }
        anomaly_count = sum(1 for value in self._indicators.values() if value.anomaly)
        return MarketOverview(
            tracked_symbols=len(settings.symbols),
            latest_prices=latest,
            anomaly_count=anomaly_count,
        )


market_data_service = MarketDataService()

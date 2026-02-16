"""Kafka producer stub for real-time stock prices."""

from dataclasses import asdict, dataclass
from datetime import UTC, datetime
import json
import random
import time


@dataclass(slots=True)
class Tick:
    symbol: str
    timestamp: str
    price: float
    volume: int


def generate_tick(symbol: str, base_price: float) -> Tick:
    return Tick(
        symbol=symbol,
        timestamp=datetime.now(UTC).isoformat(),
        price=round(max(1.0, base_price + random.uniform(-1.5, 1.5)), 2),
        volume=random.randint(1000, 1000000),
    )


if __name__ == "__main__":
    symbols = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA"]
    prices = {symbol: random.uniform(80, 300) for symbol in symbols}

    while True:
        for symbol in symbols:
            tick = generate_tick(symbol, prices[symbol])
            prices[symbol] = tick.price
            print(json.dumps(asdict(tick)))
        time.sleep(0.5)

from __future__ import annotations

from collections import deque
from statistics import mean, pstdev


class RollingIndicatorEngine:
    def __init__(self, max_points: int = 200) -> None:
        self.prices: deque[float] = deque(maxlen=max_points)
        self.gains: deque[float] = deque(maxlen=14)
        self.losses: deque[float] = deque(maxlen=14)
        self._ema20: float | None = None

    def update(self, price: float) -> dict[str, float | bool | None]:
        last_price = self.prices[-1] if self.prices else None
        self.prices.append(price)

        sma_20 = mean(list(self.prices)[-20:]) if len(self.prices) >= 20 else None

        multiplier = 2 / (20 + 1)
        if self._ema20 is None:
            self._ema20 = price
        else:
            self._ema20 = (price - self._ema20) * multiplier + self._ema20

        if last_price is not None:
            delta = price - last_price
            self.gains.append(max(delta, 0))
            self.losses.append(abs(min(delta, 0)))

        rsi_14 = None
        if len(self.gains) == 14 and len(self.losses) == 14:
            avg_gain = mean(self.gains)
            avg_loss = mean(self.losses)
            if avg_loss == 0:
                rsi_14 = 100.0
            else:
                rs = avg_gain / avg_loss
                rsi_14 = 100 - (100 / (1 + rs))

        z_score = None
        anomaly = False
        if len(self.prices) >= 30:
            sample = list(self.prices)[-30:]
            std_dev = pstdev(sample)
            if std_dev > 0:
                z_score = (price - mean(sample)) / std_dev
                anomaly = abs(z_score) >= 3

        return {
            "sma_20": sma_20,
            "ema_20": self._ema20,
            "rsi_14": rsi_14,
            "z_score": z_score,
            "anomaly": anomaly,
        }

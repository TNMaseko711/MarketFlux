from app.services.indicator_engine import RollingIndicatorEngine


def test_indicator_engine_generates_values() -> None:
    engine = RollingIndicatorEngine()
    result = None
    for i in range(1, 50):
        result = engine.update(float(i))

    assert result is not None
    assert result["ema_20"] is not None
    assert result["sma_20"] is not None
    assert result["rsi_14"] is not None

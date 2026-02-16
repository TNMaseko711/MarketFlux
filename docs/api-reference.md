# API Reference (Current MVP)

## Stocks

- `GET /api/v1/stocks`: List tracked symbols.
- `GET /api/v1/stocks/{symbol}/price`: Latest price tick.
- `GET /api/v1/stocks/{symbol}/history?limit=120`: Recent ticks.
- `GET /api/v1/stocks/{symbol}/indicators`: Latest indicator snapshot.

## Market

- `GET /api/v1/market/overview`: Tracked count, latest prices, anomaly count.

## WebSocket

- `WS /ws/stocks/{symbol}`
  - Returns `{ tick, indicators }` payload every 0.5s.

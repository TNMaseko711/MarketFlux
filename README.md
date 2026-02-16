# MarketFlux - Real-Time Financial Data Pipeline & Streaming Analytics

MarketFlux is an end-to-end starter implementation of a real-time financial data platform for streaming stock updates, calculating technical indicators, and exposing data through a low-latency API and WebSockets.

## What is implemented now

- **Live market simulator** for configurable symbols (default: AAPL, MSFT, GOOGL, AMZN, TSLA).
- **FastAPI backend** with REST endpoints and WebSocket streaming.
- **Real-time indicator engine** with SMA(20), EMA(20), RSI(14), and z-score anomaly detection.
- **Docker Compose baseline** including Kafka, Zookeeper, Redis, and API service.
- **Unit tests** for core indicator logic.

## Architecture (current baseline)

```text
Simulated Tick Stream -> In-Memory MarketDataService -> Indicator Engine
                                         |                    |
                                         v                    v
                               REST API (/api/v1/*)    WebSocket (/ws/stocks/{symbol})
```

## Quick Start (under 5 minutes)

### Option 1: local Python

```bash
cd backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

Then open:
- API docs: `http://localhost:8000/docs`
- Health: `http://localhost:8000/health`

### Option 2: Docker Compose

```bash
docker compose up --build
```

## API Endpoints

- `GET /api/v1/stocks`
- `GET /api/v1/stocks/{symbol}/price`
- `GET /api/v1/stocks/{symbol}/history?limit=120`
- `GET /api/v1/stocks/{symbol}/indicators`
- `GET /api/v1/market/overview`
- `WS /ws/stocks/{symbol}`

## Current Performance Targets (dev baseline)

- Tick frequency: every 0.5s per symbol.
- Typical response latency: in-memory lookup (single-digit ms in dev).
- Stream update delay: 0.5-1.0s in local tests.

## Next Steps to Reach Production-Grade Scope

1. Replace simulated generator with Polygon/IEX/Yahoo connectors.
2. Add Kafka producers/consumers and Flink/Spark streaming jobs.
3. Persist bars and indicators in TimescaleDB.
4. Add Redis cache for hot state and alerts.
5. Build React dashboard with market heatmap and candlestick charts.
6. Add Airflow DAGs for backfill and model retraining workflows.
7. Add Prometheus/Grafana metrics and alerting.
8. Harden auth, RBAC, rate limiting, and audit logging.

## Repository Layout (implemented subset)

```text
backend/                 FastAPI app + indicator engine + tests
data-ingestion/          Producer scaffolding
stream-processing/       Indicator operator stubs
docs/                    Architecture/API/deployment/user guides
monitoring/              Prometheus config placeholder
```

## License

MIT (add `LICENSE` file as needed).

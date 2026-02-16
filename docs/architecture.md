# Architecture Overview

## Current State

The current implementation provides a working vertical slice:

- Synthetic tick generation in-process.
- Stateful indicator computation per symbol.
- REST + WebSocket serving layer.

## Target State

The target production architecture follows a canonical streaming stack:

1. Multi-provider ingestion (WebSocket + REST polling).
2. Kafka topics per cadence/domain (`stock.prices.raw`, `stock.prices.1m`, `stock.events`, `stock.news`).
3. Stream jobs for aggregation, indicators, and anomaly scoring.
4. TimescaleDB + Redis + object storage.
5. FastAPI + React real-time dashboard.
6. Observability via Prometheus/Grafana + centralized logging.

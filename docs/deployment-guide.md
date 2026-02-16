# Deployment Guide

## Local

```bash
make api
```

## Compose

```bash
make up
```

## Production Roadmap

- Introduce Kubernetes manifests + Helm chart.
- Externalize config/secrets.
- Use managed Kafka + PostgreSQL/TimescaleDB.
- Configure autoscaling and rolling deployments.

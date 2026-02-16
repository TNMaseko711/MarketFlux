.PHONY: api test up

api:
	cd backend && uvicorn app.main:app --reload --port 8000

test:
	cd backend && pytest -q

up:
	docker compose up --build

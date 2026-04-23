DOCKER_COMPOSE := docker-compose -f infra/docker-compose.yaml

.PHONY: help docker-up docker-down docker-build server-dev web-up

help:
	@echo "Available commands:"
	@echo "  make docker-up   - Start infrastructure"
	@echo "  make docker-down - Stop infrastructure"
	@echo "  make docker-build- Rebuild infrastructure"
	@echo "  make server-dev  - Start FastAPI server in dev mode"
	@echo "  make web-up     - Start Next.js web app in dev mode"

docker-up:
	$(DOCKER_COMPOSE) up -d

docker-down:
	$(DOCKER_COMPOSE) down

docker-build:
	$(DOCKER_COMPOSE) build

server-dev:
	cd apps/server && uv run python -m fastapi dev main.py

web-dev:
	cd apps/web && bun run dev

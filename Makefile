DOCKER_COMPOSE := docker-compose -f infra/docker-compose.yaml

.PHONY: help docker-up docker-down docker-clean docker-build server-dev web-up server-typecheck server-lint server-fix web-lint web-typecheck

help:
	@echo "Available commands:"
	@echo "  make docker-up    - Start infrastructure"
	@echo "  make docker-down  - Stop infrastructure"
	@echo "  make docker-clean - Remove everything (volumes, images, orphans)"
	@echo "  make docker-build - Rebuild infrastructure"
	@echo "  make server-dev   - Start FastAPI server in dev mode"
	@echo "  make web-up      - Start Next.js web app in dev mode"
	@echo "  make server-typecheck - Type check FastAPI server"
	@echo "  make server-lint    - Lint FastAPI server"
	@echo "  make server-fix     - Fix FastAPI server"
	@echo "  make web-lint       - Lint Next.js web app"
	@echo "  make web-typecheck  - Type check Next.js web app"


docker-up:
	$(DOCKER_COMPOSE) up -d

docker-down:
	$(DOCKER_COMPOSE) down

docker-clean:
	$(DOCKER_COMPOSE) down -v --rmi all --remove-orphans

docker-build:
	$(DOCKER_COMPOSE) build

server-dev:
	cd apps/server && uv run python -m fastapi dev main.py

web-dev:
	cd apps/web && bun run dev

server-typecheck:
	cd apps/server && uv run mypy .

server-lint:
	cd apps/server && uv run ruff check .

server-fix:
	cd apps/server && uv run ruff check --fix .

server-test:
	cd apps/server && PYTHONPATH=.. uv run pytest tests/

web-lint:
	cd apps/web && bun run lint

web-typecheck:
	cd apps/web && bun run typecheck

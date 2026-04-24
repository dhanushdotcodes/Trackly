# --- Base ---
FROM python:3.13-alpine AS base
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
WORKDIR /app
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# --- Development ---
FROM base AS development
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project

COPY . /app/server
# Ensure scripts are executable
RUN chmod +x /app/server/scripts/prestart.sh

EXPOSE 8000
# Run migrations then start the server in dev mode
CMD ["sh", "-c", "/app/server/scripts/prestart.sh && uv run fastapi dev server/main.py --host 0.0.0.0 --port 8000"]

# --- Production Builder ---
FROM base AS builder
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

# --- Production Final ---
FROM python:3.13-alpine AS production
WORKDIR /app
COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

COPY . /app/server
RUN chmod +x /app/server/scripts/prestart.sh

EXPOSE 8000
# Run migrations then start the server in prod mode
CMD ["sh", "-c", "/app/server/scripts/prestart.sh && uvicorn server.main:app --host 0.0.0.0 --port 8000"]

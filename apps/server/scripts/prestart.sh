#!/bin/sh

set -e

# The DATABASE_URL is expected to be in the environment
echo "Running database migrations..."

# Navigate to the server directory where alembic.ini lives
cd /app/server

# Follow the project rule for running alembic
# Rule: PYTHONPATH=..:.:$PYTHONPATH uv run alembic
export PYTHONPATH="/app:/app/server:$PYTHONPATH"

# Run migrations
uv run alembic upgrade head

echo "Migrations completed successfully."

# Decisions

## 2026-04-22: Running Alembic Correctly

### Context
Running Alembic commands often fails due to missing environment variables, incorrect working directories, or `PYTHONPATH` issues, especially in a monorepo/multiproject setup using `uv`.

### Correct Usage
To run Alembic successfully in this project, follow these rules:

1.  **Always use `uv run`**: Since dependencies are managed by `uv`, use `uv run alembic <command>`.
2.  **Work from `apps/api`**: Always execute commands from the `apps/api` directory where `alembic.ini` is located.
3.  **Set `PYTHONPATH`**: The `api` package needs to be discoverable. Set `PYTHONPATH` to include the `apps` directory (parent of `api`).
4.  **Set `DATABASE_URL`**: Ensure the database URL is available, either via a `.env` file in `apps/api` or as an environment variable.

### Recommended Command Pattern:
```bash
# From the project root
cd apps/api
PYTHONPATH=..:.:$PYTHONPATH DATABASE_URL=your_db_url uv run alembic current
```

### Why this works:
- `PYTHONPATH=..` allows `from api.models import Base` to work correctly.
- `uv run` ensures the virtual environment managed by `uv` is used.
- Running from `apps/api` ensures `alembic.ini` is found and `script_location` is correctly resolved.

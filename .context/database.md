# Database Context

This document provides essential context for the database architecture, ORM usage, and migration workflows within the Trackly project.

## 🛠 Tech Stack
- **Framework**: FastAPI
- **ORM**: SQLAlchemy 2.0+ (Declarative Mapping)
- **Migrations**: Alembic
- **Driver**: Typically PostgreSQL (configured via `DATABASE_URL`)

---

## 📂 Key Files & Directories

- `apps/api/core/database.py`: Core database configuration (Engine, SessionLocal).
- `apps/api/models/`: SQLAlchemy model definitions.
  - `base.py`: Contains the `Base` class and global Enums.
  - `__init__.py`: **CRITICAL** - All models must be imported here to be recognized by Alembic.
- `apps/api/schemas/`: Pydantic models for API requests and responses.
- `apps/api/alembic/`: Alembic migration environment.
  - `env.py`: Configured to use `api.models.Base.metadata`.
- `apps/api/alembic.ini`: Alembic configuration file.

---

## 🏗 Database Configuration (`core/database.py`)

The project uses `sessionmaker` to create a `SessionLocal` class. Database connection parameters are pulled from the application settings.

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import get_settings 

settings = get_settings()
engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```

### Dependency Injection
To use the database in FastAPI endpoints, use a dependency to manage session lifecycle:

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

---

## 📝 Models & Schema (`models/`)

### Base Class
All models MUST inherit from `api.models.base.Base`, which uses SQLAlchemy's `DeclarativeBase`.

### Model Registration
For Alembic's `autogenerate` feature to work, every model file must be imported in `apps/api/models/__init__.py`. 

**Current Models:**
- `User`: User accounts and authentication.
- `Organisation`: Tenant entities.
- `OrgMembership`: Junction table for Users and Organisations (Org Roles).
- `DeptMembership`: Junction table for Users and Departments (Dept Roles).
- `Department`: Groups within an Organisation.
- `Task`: Core task entity.
- `TaskCategory`, `TaskAssignee`, `TaskComment`: Task-related metadata and relationships.

---

## 🚀 Migrations Workflow (Alembic)

Alembic is configured to run from the `apps/api` directory.

### Running Alembic Correctly
To avoid import errors and environment issues, use the following pattern:

```bash
cd apps/api
PYTHONPATH=..:.:$PYTHONPATH uv run alembic <command>
```

### Common Commands
1. **Create a new migration (Autogenerate):**
   ```bash
   PYTHONPATH=..:.:$PYTHONPATH uv run alembic revision --autogenerate -m "description_of_changes"
   ```
   *Note: Always review the generated script in `alembic/versions/`.*

2. **Apply migrations:**
   ```bash
   PYTHONPATH=..:.:$PYTHONPATH uv run alembic upgrade head
   ```

3. **Rollback last migration:**
   ```bash
   PYTHONPATH=..:.:$PYTHONPATH uv run alembic downgrade -1
   ```

### Troubleshooting `env.py`
The `apps/api/alembic/env.py` is configured to import `Base` from `api.models`. If you add new models, ensure they are imported in `api.models/__init__.py` so `Base.metadata` includes them.

---

## 💡 Best Practices for AI Tools
1. **Always check `apps/api/models/__init__.py`** when adding or modifying models to ensure they are exported correctly.
2. **Prefer SQLAlchemy 2.0 style queries** (using `select()`, `execute()`, etc.) over the legacy `Query` API.
3. **Check `api.models.base`** for existing Enums (`OrgRole`, `DeptRole`, `TaskStatus`, `TaskPriority`) before creating new ones.
4. **When generating migrations**, ensure you are in the `apps/api` directory and have the `PYTHONPATH` set as shown above.
5. **Always update `docs/DB_SCHEMA.md` and this file (`.context/database.md`)** when making changes to the database models to keep documentation in sync.

----
name: handle-db
description: Handles database creation, schema definition, and asynchronous migrations using SQLAlchemy 2.0 and Alembic.
----

# Skill: Handle Database Operations

## When to Use
Use this skill when:
- Creating, modifying, or deleting database tables or schemas.
- Working with SQLAlchemy 2.0 ORM models.
- Running, generating, or managing database migrations with Alembic.
- Designing or implementing asynchronous database operations.

Do NOT use when:
- Creating purely in-memory data structures.
- Interacting with APIs that don't involve the project's SQLAlchemy DB setup.

---

## Input
- Specific details on the required database schema (columns, types, relationships).
- `apps/api/models/*.py` files if working with existing tables.
- Migration history in `apps/api/alembic/versions/` to avoid conflicts.

---

## Steps to Execute

1. **Understand Database Architecture and Conventions**
   - The framework is FastAPI with SQLAlchemy 2.0+ (Declarative Mapping).
   - All database operations **MUST** be asynchronous.
   - All models MUST inherit from `api.models.base.Base`.

2. **Create or Modify SQLAlchemy Models**
   - Add new or update existing model definitions inside `apps/api/models/`.
   - Ensure the models use SQLAlchemy 2.0 styling (e.g., `Mapped[int] = mapped_column(primary_key=True)`).
   - Check `api.models.base` for existing Enums before creating new ones.
   - **CRITICAL**: Import any new models in `apps/api/models/__init__.py` so Alembic can detect them for migrations (`Base.metadata`).
   - Provide corresponding Pydantic 'Read' and 'Write' schemas in `apps/api/schemas/` for the models.

3. **Handle Service Layer Operations**
   - Use asynchronous database queries (`select()`, `execute()`) over legacy `Query` API.
   - Service methods must use atomic transactions via `async with session.begin():` or inject `get_db` dependency properly.
   - **Never** call `.commit()` manually inside a service method.

4. **Manage Alembic Migrations**
   - Ensure you are in the `apps/api` directory before running Alembic.
   - To generate a new migration after updating models:
     ```bash
     cd apps/api
     PYTHONPATH=..:.:$PYTHONPATH uv run alembic revision --autogenerate -m "description_of_changes"
     ```
   - Review the generated script inside `alembic/versions/` to ensure accuracy.
   - Apply migrations to the database:
     ```bash
     cd apps/api
     PYTHONPATH=..:.:$PYTHONPATH uv run alembic upgrade head
     ```
   - Do NOT modify or delete existing historical migration files unless explicitly instructed.

5. **Ensure Data Safety**
   - Do not drop tables or clear data unless explicitly requested by the user.
   - When altering columns, handle potential data migrations if needed.

6. **Update Documentation**
   - Whenever you add, modify, or remove models or columns, you MUST update `docs/DB_SCHEMA.md` and `.context/database.md` to reflect these changes.

---

## Output Format
- SQLAlchemy model definitions updated in `apps/api/models/`.
- Pydantic schemas updated in `apps/api/schemas/`.
- Newly generated Alembic migration file inside `apps/api/alembic/versions/`.
- Updated `apps/api/models/__init__.py`.

---

## Checklist
- [ ] Model uses SQLAlchemy 2.0 Declarative Mapping.
- [ ] Model inherits from `api.models.base.Base`.
- [ ] Model is imported into `apps/api/models/__init__.py`.
- [ ] Database operations and service methods are fully asynchronous.
- [ ] No manual `.commit()` calls exist in service methods.
- [ ] Alembic migration has been successfully generated and reviewed.
- [ ] `uv run alembic upgrade head` has been run and validated.
- [ ] Database documentation (`docs/DB_SCHEMA.md` and `.context/database.md`) has been updated to reflect the schema changes.

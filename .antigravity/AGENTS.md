# AGENTS.md

## Project
- Full-stack application with Next.js frontend and FastAPI backend.
- Frontend and backend are developed independently but must share stable API contracts.
- Limit refactoring to the immediate scope of the task. Do not modify more than 20 lines of existing code for "cleanliness" unless specifically requested. If a change affects >3 files or >20% of a file, pause and confirm the scope.

## Stack
- Web: Next.js, React, TypeScript with strict mode
- API: FastAPI, Python 3.12+, SQLAlchemy 2.0, Alembic
- Database: PostgreSQL
- Testing: pytest for backend, frontend tests using the repo-standard toolchain

## Shared Engineering Rules
- Prioritize patterns defined in .antigravity/ files over local file patterns. If the existing code conflicts with these rules, follow the rules and notify the user of the inconsistency.
- Business logic MUST reside in the /services (backend) or /hooks or /logic (frontend) directories. Route handlers and UI components are strictly for I/O: validation, calling services, and returning/rendering data.
- Prefer explicit types and clear interfaces over implicit behavior.
- Do not hardcode secrets, tokens, connection strings, or environment-specific values.
- Do not perform destructive database actions without explicit confirmation.
- Do not introduce large refactors unless requested or clearly necessary.

## Quality
- New business logic should include tests.
- Bug fixes should include or update regression tests where practical.
- Reuse existing utilities and patterns before creating new abstractions.

## Git
- Keep diffs focused and reviewable.
- Match the repository’s linting, formatting, and naming conventions.
----
name: full-stack-development-conventions
description: Master the core conventions and architectural principles for both backend (FastAPI) and frontend (Next.js) development in the Trackly repository.
----

# Skill: Full-Stack Development Conventions

## When to Use
Use this skill when:
- Implementing or modifying any part of the Trackly repository (including FastAPI backend, Next.js frontend, database migrations, and testing).
- Creating or editing files to ensure architecture, naming, and TypeScript safety rules are strictly upheld.
- Resolving any ambiguity about folder layout, framework conventions, and testing/debugging workflows.

Do NOT use when:
- Performing non-code administrative or pure operational tasks that fall entirely outside the code and directory structure of the project.

---

## Input
- **Core Principle**: Separation of concerns followed globally. MVP first, without over-engineering.
- **FastAPI (Backend)**: FastAPI, async routines, Pydantic models for validation, dependency injection with `get_` prefix.
- **Next.js (Frontend)**: App Router (lowercase/kebab-case URLs), Server Components by default, Server Actions for mutations.
- **Database**: SQLAlchemy 2.0+, declarative mapping, async DB sessions, Alembic for migrations.
- **TypeScript**: Strict typing (`strict: true`), no `any`, proper error handling.

---

## Steps to Execute

### 1. General Workflow & AI Behavior
- **Explain Logic**: Always explain technical logic before writing code.
- **Minimize Scope**: Do not generate large files blindly. Refactorings should be strictly limited to the immediate task scope (do not change > 20 lines for cleanliness).
- **Early Validation**: If a change affects >3 files or >20% of a file, pause and confirm the scope with the user.

### 2. Architectural Structure

#### FastAPI (Backend)
- **Separation of Concerns**: Keep route handlers thin; all business logic must reside in `/services`.
- **Files & Modules**: Routes in `api/` (plural names like `users.py`, `posts.py`), Services in `services/`, Models in `models/`, Pydantic Schemas in `schemas/`.
- **Naming Conventions**:
  - Folders & files: `snake_case`
  - Classes / Schemas / Enums: `PascalCase`
  - Functions & Variables: `snake_case`
  - Constants & Env vars: `UPPER_SNAKE_CASE`
  - Router instances: must be named `router`
- **Imports & Limits**: Use the full path for all package imports (e.g., `server.packagename.filename`). Service files must not exceed 300 lines; functions must be ≤ 40 lines.

#### Next.js (Frontend)
- **Separation of Concerns**: Use Server Components by default; push `'use client'` strictly to leaf nodes. Never put `'use client'` at the top of `page.tsx`.
- **Files & Modules**: All routes must use standard App Router files without renaming (`page.tsx`, `layout.tsx`, `loading.tsx`, `error.tsx`, `not-found.tsx`, `route.ts`). Private route files must be prefixed with an underscore (e.g., `_components`, `_lib`).
- **Naming Conventions**:
  - Route folders: lowercase / `kebab-case`
  - Components & Component files: `PascalCase` (must match their file names)
  - Functions & Variables: `camelCase`
  - Hooks: `useSomething` pattern
  - Types & Interfaces: `PascalCase`
  - Constants: `UPPER_SNAKE_CASE`
- **Component Props**: Explicit interfaces for component props are required. Never use `any` or `Record<string, any>`.

### 3. Database & Migration Procedures
- **Async & Declarative**: Use SQLAlchemy 2.0+ declarative mappings and execute queries asynchronously. All models must inherit from `server.models.base.Base` and be imported in `apps/server/models/__init__.py`.
- **Atomic Sessions**: All service methods must use `async with session.begin():` for atomic operations. Never invoke `.commit()` manually inside a service method.
- **Alembic**: All DB migrations must use Alembic. Run from `apps/server` using `PYTHONPATH=..:.:$PYTHONPATH uv run alembic`.

### 4. TypeScript Safety & Quality Standards
- **Strict Checks**: Ensure `strict: true` is enabled. Never use `any`. Use `unknown` or Type Guards to narrow uncertain types.
- **Error Handling**: Follow RFC 7807 for API error responses. Raise errors explicitly at point of failure. Never throw strings; always throw `Error` objects. Use exhaustiveness checks in all switch statements.
- **Styling Rules**: Avoid using `bg-gradient-to-br` for CSS gradients; use `bg-linear-to-br` for Tailwind v4.

### 5. Verification & Git
- **Lint & Typecheck Commands**:
  - Backend: `uv run ruff check`
  - Next.js: `bun run lint && bun x tsc --noEmit`
- **Git Rules**: Conventional commits only (`feat:`, `fix:`, `docs:`). Atomic commits. Maintain focused pull requests (≤ 400 lines of diff).

---

## Output Format
- Code fully aligned with architectural layers.
- Strict conformance to backend (`snake_case`) and frontend (`camelCase`, `PascalCase`, `kebab-case`) naming standards.
- Detailed JSDoc and Python docstrings for all exported/public functions.

---

## Checklist
- [ ] Logic explained clearly before writing code
- [ ] Code follows separation of concerns strictly (Handlers -> Services/Actions -> Models)
- [ ] Component names match their file names exactly
- [ ] Strict TypeScript (`strict: true`) applied without `any` types
- [ ] Functional components and leaf node client files used in Next.js
- [ ] Full path used for in-house imports (e.g. `server.packagename.filename`)
- [ ] No manual `.commit()` inside SQLAlchemy service methods
- [ ] Linting and typechecks run successfully on both layers
- [ ] Atomic and conventional commits used

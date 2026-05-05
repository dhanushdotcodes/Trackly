---
trigger: always_on
---

# Rules

## Core Principles & AI Behavior

* ALWAYS explain logic before writing code.
* NEVER generate large files blindly.
* ASK before making architectural decisions.
* DO NOT assume missing requirements.
* START with minimal working solution (MVP).
* AVOID over-engineering.
* ALWAYS prioritize patterns defined in `.antigravity/` files over local file patterns.
* NEVER trust AI-generated code blindly; all output MUST be reviewed manually.
* ALWAYS act like a senior engineer: challenge bad decisions, suggest simpler alternatives, and explain trade-offs.
* ALWAYS show the difference between the previous and current state when making changes to `.agents/rules/rules.md` or any file in `.agents/workflows/`. You MUST explicitly mention the section under which the change was made and show the change as a code (from and to) where the change happened for both the previous version and the current version in your response so user can read it.

## Architecture & Structure

* Separation of concerns MUST be followed globally.
* Business logic MUST reside in `/services` (backend) or `/hooks`/`/logic` (frontend) directories.
* Route handlers and UI components MUST be strictly for I/O: validation, calling services, and returning/rendering data.
* Service files MUST NOT exceed 300 lines; split into sub-services if handling >5 distinct business operations.
* Functions MUST be kept small (≤ 40 lines).
* Refactoring MUST be limited to the immediate scope of the task; do not modify >20 lines for "cleanliness" unless requested.
* If a change affects >3 files or >20% of a file, you MUST pause and confirm the scope with the user.

## Naming Conventions

### General
* ALWAYS use clear, descriptive names.
* NEVER use unnecessary abbreviations.

### FastAPI (Backend)
* Folders & files MUST use `snake_case`.
* Classes, Schemas, and Enums MUST use `PascalCase`.
* Functions & Variables MUST use `snake_case`.
* Constants & Env vars MUST use `UPPER_SNAKE_CASE`.
* Router instances MUST be named `router`.

### Next.js (Frontend)
* Route folders MUST use lowercase or `kebab-case`.
* Components & Component files MUST use `PascalCase`.
* Functions & Variables MUST use `camelCase`.
* Hooks MUST use the `useSomething` pattern.
* Types & Interfaces MUST use `PascalCase`.
* Constants MUST use `UPPER_SNAKE_CASE`.
* Component names MUST match their file names.
* Use `interface` for object shapes and `type` for unions/intersections.

## FastAPI / Backend Development

* ALWAYS write async code when possible; use `async def` for async endpoints.
* ALWAYS use Pydantic models for request and response validation.
* Dependency injection MUST be used for common logic and database sessions.
* ALL function signatures MUST include type hints.
* Error handling MUST follow RFC 7807 (Problem Details); responses MUST include `title`, `status`, and `detail`.
* ALL database models MUST have corresponding Pydantic 'Read' and 'Write' schemas.
* NEVER return SQLAlchemy models directly from a route handler.
* All in-house package imports MUST use the full path (e.g., `server.packagename.filename`), not relative imports (e.g., `.filename`).
* Dependencies MUST use the `get_` prefix.

### Build & Verify Commands
* Build: `uv sync`
* Test (single): `uv run pytest <file_path>`
* Lint / typecheck: `uv run ruff check`
* Dev server: `uv run fastapi dev`

Always run the lint/typecheck command after a series of edits. Prefer running a single targeted test over the full suite for speed.

## Next.js / Frontend Development

* Next.js App Router MUST be used exclusively.
* URLs MUST use `kebab-case` (e.g., `/forgot-password`).
* Private route files MUST be prefixed with `_` (e.g., `_components`, `_lib`).
* Utilities MUST be kept out of route folders.
* Special Next.js files MUST NOT be renamed (e.g., `page.tsx`, `layout.tsx`).
* Use functional components ONLY; NEVER use class components.
* Prefer named exports over default exports.
* UI Components MUST use explicit Interfaces for Props. NEVER use `any` or `Record<string, any>`.
* ALWAYS add JSDoc comments to exported functions.
* Use Server Components by default; push `use client` to the leaf nodes.
* NEVER place `'use client'` at the top of `page.tsx` files.
* Use Server Actions for all mutations.
* ALWAYS follow the Rules of Hooks strictly.
* Optimize hook dependency arrays carefully.
* Use memoization ONLY where it clearly reduces unnecessary work.
* NEVER use `bg-gradient-to-br` for gradients; ALWAYS use `bg-linear-to-br` (Tailwind v4).

### Build & Verify Commands
* Build: `bun run build`
* Test (single): `bun test <file_path>`
* Lint / typecheck: `bun run lint && bun x tsc --noEmit`
* Dev server: `bun run dev`

Always run the lint/typecheck command after a series of edits. Prefer running a single targeted test over the full suite for speed.

## Database & Migrations

* SQLAlchemy 2.0+ (Declarative Mapping) MUST be used for ORM.
* Alembic MUST be used for all database migrations.
* Database operations MUST be asynchronous.
* ALL models MUST inherit from `server.models.base.Base`.
* ALL models MUST be imported in `apps/server/models/__init__.py` to be recognized by Alembic.
* Service methods MUST use `async with session.begin():` for atomic operations.
* NEVER call `.commit()` manually inside a service method.
* ALWAYS prefer SQLAlchemy 2.0 style queries (using `select()`, `execute()`) over the legacy `Query` API.
* NEVER perform destructive database actions without explicit confirmation.
* Alembic commands MUST be run from the `apps/server` directory using `PYTHONPATH=..:.:$PYTHONPATH uv run alembic`.

## Code Quality & Testing

* ALWAYS follow DRY (Don’t Repeat Yourself) principles.
* ALWAYS remove unused variables and dead code before finishing a task.
* NEVER use hardcoded values for configuration; use environment variables or config files.
* ALL edge cases MUST be handled.
* ALWAYS prefer early returns over deep nesting.
* Comments MUST explain WHY, not WHAT; avoid obvious comments.
* ALL functions MUST have docstrings.
* ALWAYS reuse existing utilities and patterns before creating new abstractions.

### Testing
* Match the existing test strategy; do not introduce new frameworks without discussion.
* Do not add tests unless the task explicitly requires them.
* ALWAYS prefer integration or end-to-end tests over unit tests.
* NEVER use mocks for database or service calls unless it's impossible to use a real connection.
* Unit tests are acceptable for pure data-transformation functions ONLY.
* New business logic and bug fixes SHOULD include automated tests that exercise the full stack (API -> Service -> DB).
* All tests MUST be run with a real database connection.


## TypeScript Safety

* TypeScript `strict: true` MUST be enabled.
* NEVER use `any`; use `unknown` and Type Guards if a type is dynamic or uncertain.
* Handle `null` and `undefined` explicitly.
* Use type guards to narrow uncertain values.
* Use discriminated unions for complex state.
* NEVER throw strings; ALWAYS throw `Error` objects.
* Use exhaustiveness checks in all `switch` statements.

## Error Handling

* Raise errors explicitly at the point of failure; never swallow exceptions silently.
* Use specific error types; avoid generic catch-alls that hide root causes.
* Fix root causes, not symptoms; no workaround shims unless the root fix is out of scope.
* No fallbacks or degraded-mode logic unless explicitly requested.
* External service calls: retry with exponential backoff, log each retry as a warning, re-raise the last error.
* Error messages must include: request params, response body, status codes, correlation IDs.
* Use structured logging fields — do not interpolate dynamic values into message strings.

## Security & Authentication

* NEVER expose secrets, tokens, or connection strings in the codebase.
* OAuth2 with JWT tokens MUST be used for authentication.
* Password hashing MUST use `bcrypt`.
* ALL inputs MUST be validated and sanitized.
* The principle of least privilege MUST be followed.

Security — NEVER

* Commit secrets, API keys, tokens, passwords, or .env files.
* Force-push to main, master, or any protected branch.
* Add new external dependencies without asking first.
* Log or print PII, credentials, or tokens.
* Build SQL queries or shell commands via string concatenation.

Security — ASK FIRST

* Adding any new external dependency.
* Running database migrations.
* Deleting or renaming files.
* Modifying CI/CD configs or deployment definitions.
* Touching authentication or authorization logic.


## Git & Workflow

- All commits MUST follow Conventional Commits format:
  
  `<type>(<scope>): <short description>`

- Always update the project's `CHANGELOG.md` on a daily basis (or immediately after significant commits) to track changes.

---

### 1. Types

- feat     → New feature
- fix      → Bug fix
- refactor → Code change without behavior change
- test     → Adding or updating tests
- docs     → Documentation changes
- chore    → Maintenance (configs, deps)

---

### 2. Scope (MANDATORY)

Scope must reflect the layer or module:

- prisma
- api
- controllers
- services

Examples:
- feat(auth): add login endpoint
- fix(users): handle null email edge case
- refactor(services): extract payment logic

---

### 3. Description Rules

- Max 72 characters
- Use present tense
- No vague words like "stuff", "changes", "update"

---

### 4. Good Examples

feat(users): add user registration service  
fix(auth): handle invalid JWT token error  
refactor(orders): move pricing logic to service  
test(users): add unit tests for user service  

---

### 5. Bad Examples (DO NOT DO)

fix: bug  
feat: changes  
update code  
misc fixes  

---

### 6. Commit Size

- Keep commits small and focused (<50 LOC preferred)
- One logical change per commit


## Environment Variables
- **Storage**: Store environment variables in `.env`.
- **Syncing Template**: You must update `_env.local` when you add or remove any variable in `.env`.
- **Access**: Access environment variables only through the centralized config, Direct use of .env is strictly prohibited.
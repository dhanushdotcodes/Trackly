----
name: skill-name
description: Brief description of what the skill does in one sentence.
----

# Skill: Name of the Skill

## When to Use
Use this skill when:
- Trigger condition 1
- Trigger condition 2

Do NOT use when:
- Anti-trigger condition 1
- Anti-trigger condition 2

---

## Constraints and Guidelines

* ALWAYS write async code when possible; use `async def` for async endpoints.
* ALWAYS use Pydantic models for request and response validation.
* Dependency injection MUST be used for common logic and database sessions.
* ALL function signatures MUST include type hints.
* Error handling MUST follow the request and response format in `docs/API_SPEC.md`.
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

---

## Constraints and Guidelines

* Follow the existing testing patterns and project structure.
* Prefer API-level integration tests over unit tests.
* ALWAYS test through the HTTP layer using `TestClient`.
* NEVER mock:
  - database sessions
  - ORM queries
  - service layer calls
* All tests MUST use a real database connection.
* Tests MUST validate:
  - status codes
  - response structure
  - important response fields
  - expected error responses
* Cover:
  - success cases
  - validation failures
  - not-found cases
  - duplicate/conflict scenarios
  - authorization/authentication failures when applicable
* Keep tests isolated and deterministic.
* Avoid shared mutable state between tests.
* Prefer reusable fixtures for setup and cleanup.
* Do NOT test implementation details or SQLAlchemy internals.
* Do NOT modify production code unless explicitly requested.
* Keep test names descriptive and behavior-focused.
* Ensure tests pass with:
  - `pytest`
  - `ruff`
  - existing CI checks

---

## Input
- Tech stack, parameters, architecture info, etc.
- Example inputs or user parameters required.

---

## Steps to Execute

1. Step One
   - Detail about step one.
   - Any specific sub-actions or tools to use.

2. Step Two
   - Detail about step two.

3. Step Three
   - Detail about step three.

---

## Output Format
- Expected output, files created, or structure.
- Details of how artifacts are formatted and shared.

---

## Checklist
- [ ] Requirements and scope are fulfilled
- [ ] No hardcoded configuration has been introduced
- [ ] Tests or validation steps have been executed
- [ ] Code follows project standards and rules
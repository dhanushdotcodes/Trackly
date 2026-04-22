# AI Naming & Structure Rules (FastAPI + Next.js)

Use this as the **single source of truth** for naming and structure.
Prioritize **consistency over preference**.

---

## Core Principle

* Follow existing project conventions if consistent
* Otherwise, use the rules below everywhere
* Do not mix styles within the same layer

---

## FastAPI (Backend)

### Naming

* **Folders & files:** `snake_case`
* **Classes / Schemas / Enums:** `PascalCase`
* **Functions / Variables:** `snake_case`
* **Constants / Env vars:** `UPPER_SNAKE_CASE`
* **Router variable:** `router`

### Files & Modules

* Routes → `users.py`, `posts.py`
* Services → `user_service.py`
* Repositories → `user_repository.py`
* Tests → `test_users.py`

### Structure

```
app/
├── main.py
├── core/          # config, security, db
├── api/           # routes & deps
├── models/        # ORM models
├── schemas/       # Pydantic models
├── services/      # business logic
├── repositories/  # DB access
├── utils/
└── tests/
```

### Rules

* Keep route handlers thin
* Move logic to `services/`
* Use `get_` prefix for dependencies
* Import routers via modules:

```python
from .routers import users
app.include_router(users.router)
```

---

## Next.js (Frontend - App Router)

### Naming

* **Route folders:** lowercase / `kebab-case`
* **Components & files:** `PascalCase`
* **Functions / variables:** `camelCase`
* **Hooks:** `useSomething`
* **Types / Interfaces:** `PascalCase`
* **Constants:** `UPPER_SNAKE_CASE`

### Required Files (DO NOT RENAME)

* `page.tsx`
* `layout.tsx`
* `loading.tsx`
* `error.tsx`
* `not-found.tsx`
* `route.ts`

### Structure

```
src/
├── app/
├── components/
├── hooks/
├── lib/
├── types/
├── constants/
└── styles/
```

### Rules

* Use `kebab-case` for URLs → `forgot-password`
* Use `_components` / `_lib` for private route files
* Keep utilities out of route folders
* Match component name with file name

---

## Final Defaults (Strict)

### FastAPI

* snake_case everywhere (except classes)
* PascalCase for classes
* plural route files
* `router` instance name
* business logic in services

### Next.js

* App Router only
* kebab-case routes
* PascalCase components
* camelCase logic
* `use*` hooks
* exact special file names

---

## Short Rule Block (for AI tools)

```md
FastAPI:
- snake_case (files, funcs, vars)
- PascalCase (classes)
- UPPER_SNAKE_CASE (constants)
- routes: users.py, posts.py
- router = APIRouter()
- business logic → services

Next.js:
- App Router
- routes: lowercase/kebab-case
- special files unchanged
- components: PascalCase
- functions: camelCase
- hooks: useSomething
- types: PascalCase
- constants: UPPER_SNAKE_CASE

Rule:
Follow project conventions if consistent, else use this.
```
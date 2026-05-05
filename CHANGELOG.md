# Changelog

All notable changes to this project will be documented in this file.

## [2026-05-05]

### Added
- **api**: Added `password` and `is_verified` fields to `User` model, schemas, and database migration.
- **models**: Added `DeptMembership` model and `DeptRole` enum to separate department-level roles.
- **skills**: Added `handle-db` and `containerise-app` agent skills.

### Changed
- **docs**: Updated DB schema documentation to include the new User columns.
- **docs**: Updated `PRD.md`, `DB_SCHEMA.md`, and `.context/database.md` to reflect separated membership roles.
- **agents**: Enforced line number diffs for rules/workflows updates and documentation syncs on DB schema changes.
- **skills**: Added Alembic command quick-reference to `handle-db` skill and prohibited manual migration file edits.
- **architecture**: Updated PRD and ARCHITECTURE documentation to clarify RBAC and department workflows.
- **models**: Refactored `OrgMembership` to solely handle organization-level roles by removing `department_id`.
- **models**: Renamed `UserRole` enum to `OrgRole` and removed `Viewer` role at the org level.

### Removed
- **agents**: Removed obsolete context files (`api.md`, `current-status.md`) and updated agent rules.

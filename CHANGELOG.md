# Changelog

All notable changes to this project will be documented in this file.

## [2026-05-05]

### Added
- **api**: Added `password` and `is_verified` fields to `User` model, schemas, and database migration.
- **models**: Added `DeptMembership` model and `DeptRole` enum to separate department-level roles.
- **models**: Added `OrgInvite` model to handle organization invitations.
- **models**: Added `department_id` to `TaskCategory` for department-specific categorization.
- **skills**: Added `handle-db` and `containerise-app` agent skills.

### Changed
- **docs**: Updated DB schema documentation to include the new User columns, `org_invites` table, and `TaskCategory` updates.
- **docs**: Updated `PRD.md`, `DB_SCHEMA.md`, and `.context/database.md` to reflect separated membership roles.
- **docs**: Finalized `api_design_plan.md` after clarifying task visibility and department categories.
- **agents**: Enforced line number diffs for rules/workflows updates and documentation syncs on DB schema changes.
- **skills**: Added Alembic command quick-reference to `handle-db` skill and prohibited manual migration file edits.
- **architecture**: Updated PRD and ARCHITECTURE documentation to clarify RBAC and department workflows.
- **models**: Refactored `OrgMembership` to solely handle organization-level roles by removing `department_id`.
- **models**: Renamed `UserRole` enum to `OrgRole` and removed `Viewer` role at the org level.
- **db**: Consolidated Alembic migrations into a single clean `initial_schema.py` after local database reset.

### Removed
- **agents**: Removed obsolete context files (`api.md`, `current-status.md`) and updated agent rules.

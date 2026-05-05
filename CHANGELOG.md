# Changelog

All notable changes to this project will be documented in this file.

## [2026-05-05]

### Added
- **api**: Added `password` and `is_verified` fields to `User` model, schemas, and database migration.
- **skills**: Added `handle-db` and `containerise-app` agent skills.

### Changed
- **docs**: Updated DB schema documentation to include the new User columns.
- **agents**: Enforced line number diffs for rules/workflows updates and documentation syncs on DB schema changes.
- **architecture**: Updated PRD and ARCHITECTURE documentation to clarify RBAC and department workflows.

### Removed
- **agents**: Removed obsolete context files (`api.md`, `current-status.md`) and updated agent rules.

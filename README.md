# Trackly

A robust, multi-tenant task management system designed for organizations and departments to efficiently track and collaborate on tasks.

## Tech Stack

- **Frontend**: Next.js (App Router), React 19, Tailwind CSS v4, Bun
- **Backend**: FastAPI, Python 3.13, Pydantic, UV
- **Database**: PostgreSQL, SQLAlchemy 2.0 (Declarative Mapping), Alembic
- **Authentication**: OAuth2 with JWT tokens, Bcrypt password hashing
- **Deployment**: FastAPI Cloud
- **Other tools**: Ruff (linting), Pytest (testing)

## Features

- **Multi-Tenant Architecture**: Support for multiple Organisations and Departments within a single instance.
- **Role-Based Access Control**: Secure user management with roles like Admin and Member.
- **Advanced Task Management**: Track tasks with statuses, priorities, and categories.
- **Collaborative Workflow**: Assign tasks to team members and communicate through task comments.
- **Modern UI/UX**: A responsive and high-performance interface built with the latest Tailwind CSS v4.

## Project Preview

We are still in the building phase, will update the preview soon.

## Installation

1. **Clone the repo**:
   ```bash
   git clone <repo-url>
   cd Trackly
   ```

2. **Install dependencies**:
   - **Backend**:
     ```bash
     cd apps/server
     uv sync
     ```
   - **Frontend**:
     ```bash
     cd apps/web
     bun install
     ```

3. **Add environment variables**:
   - Create `.env` files in `apps/server/` and `apps/web/` following the structure in `_env.local`.
   - Configure your `DATABASE_URL` and `JWT_SECRET`.

4. **Run the app**:
   - **Backend**: `uv run fastapi dev`
   - **Frontend**: `bun run dev`

## Usage

1. **Onboard**: Sign up and create your first Organisation.
2. **Organize**: Create Departments and invite team members to join.
3. **Track**: Create tasks, set priorities, and assign them to members.
4. **Collaborate**: Update task statuses and leave comments to keep everyone in sync.

## Folder Structure

```bash
Trackly/
├── apps/
│   ├── server/      # FastAPI Backend (Python)
│   └── web/         # Next.js Frontend (TypeScript)
├── .agents/         # AI configuration and project rules
├── .context/        # Project documentation and context
└── README.md        # Project Overview
```

## Developer

Built by [Dhanush Draksharapu](https://dhanush.codes)

- [GitHub](https://github.com/dhanushdotcodes)
- [LinkedIn](https://www.linkedin.com/in/dhanushdotcodes/)
- [Portfolio](https://dhanush.codes)

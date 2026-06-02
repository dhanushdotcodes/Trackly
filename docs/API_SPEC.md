# API Specification
---
Base URL: /api/v1

All endpoints return JSON responses:
```
{
  "data": {},
  "error": null,
  "message": "success"
}
```
Error response:
```
{
  "data": null,
  "error": "VALIDATION_ERROR",
  "message": "Email is required"
}
```

## Authentication & User Management
---
POST /api/auth/signup — create a new user account.

POST /api/auth/login — authenticate a user and return a JWT token.

POST /api/auth/logout — invalidate the current session.

POST /api/auth/forgot-password — send a password reset link to user's email.

POST /api/auth/reset-password — reset password using token provided via email.

GET /api/auth/verify-email — verify user's email address.

GET /api/users/me — get current logged-in user profile.

PATCH /api/users/me — update user profile details.

## Organisation Management
---
POST /api/orgs — create a new organisation.

GET /api/orgs — list organisations current user is a member of.

GET /api/orgs/:org_id — get details of a specific organisation.

PATCH /api/orgs/:org_id — update organisation details.

DELETE /api/orgs/:org_id — delete the organisation.

PATCH /api/orgs/:org_id/transfer-ownership — transfer ownership to another user.

GET /api/orgs/:org_id/members — list all members of an organisation.

PATCH /api/orgs/:org_id/members/:user_id/role — update a member's role.

DELETE /api/orgs/:org_id/members/:user_id — remove a member from the organisation.

## Organisation Invites
---
POST /api/orgs/:org_id/invites — send an email invite to join the organisation.

GET /api/users/me/invites — list pending organisation invites for current user.

POST /api/invites/:invite_id/accept — accept an invite and join the organisation.

POST /api/invites/:invite_id/reject — reject an invite.

## Department Management
---
POST /api/orgs/:org_id/departments — create a new department or sub-department.

GET /api/orgs/:org_id/departments — list departments within an organisation.

GET /api/orgs/:org_id/departments/:dept_id — get specific department details.

PATCH /api/orgs/:org_id/departments/:dept_id — update department details.

DELETE /api/orgs/:org_id/departments/:dept_id — delete a department.

GET /api/orgs/:org_id/departments/:dept_id/members — list members in a department.

POST /api/orgs/:org_id/departments/:dept_id/members — add an org member to the department.

PATCH /api/orgs/:org_id/departments/:dept_id/members/:user_id/role — update department role.

DELETE /api/orgs/:org_id/departments/:dept_id/members/:user_id — remove member from department.

## Task Management
---
POST /api/orgs/:org_id/tasks — create a new task.

GET /api/orgs/:org_id/tasks — list tasks with optional filtering.

GET /api/orgs/:org_id/tasks/:task_id — get details of a single task.

PUT /api/orgs/:org_id/tasks/:task_id — update task details.

PATCH /api/orgs/:org_id/tasks/:task_id/status — update task status.

DELETE /api/orgs/:org_id/tasks/:task_id — delete a task.

## Comments Management
---
POST /api/orgs/:org_id/tasks/:task_id/comments — add a comment to a task.

GET /api/orgs/:org_id/tasks/:task_id/comments — list comments for a task.

PUT /api/orgs/:org_id/tasks/:task_id/comments/:comment_id — update comment content.

DELETE /api/orgs/:org_id/tasks/:task_id/comments/:comment_id — delete a comment.

## Task Categories
---
POST /api/orgs/:org_id/categories — create an org-level category.

POST /api/orgs/:org_id/departments/:dept_id/categories — create a department-specific category.

GET /api/orgs/:org_id/categories — list org-level categories.

GET /api/orgs/:org_id/departments/:dept_id/categories — list department-specific categories.

PUT /api/orgs/:org_id/categories/:category_id — update a category.

DELETE /api/orgs/:org_id/categories/:category_id — delete a category.

## Health Check
---
GET /health — check the status of the API and its database connection.
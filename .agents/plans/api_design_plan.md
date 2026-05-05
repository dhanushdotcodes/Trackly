# Trackly API Implementation Plan

This document outlines the API design for the Trackly task management application based on the provided Product Requirements and Database Schema. It details the routes, their responsibilities, and the access control mechanisms required.

## Understanding Access Control: RBAC vs ABAC

To meet the requirements of Trackly, we need a hybrid approach to access control combining Role-Based Access Control (RBAC) and Attribute-Based Access Control (ABAC).

### Role-Based Access Control (RBAC)
Access is granted based on the user's explicit role within a specific context (Organisation or Department).
- **Org Roles**: `Owner`, `Admin`, `Member`.
  - *Example*: Only an `Owner` or `Admin` can update organisation details. Only an `Owner` can delete the organisation.
- **Dept Roles**: `Manager`, `Member`, `Viewer`.
  - *Example*: Only a `Manager` can perform full CRUD operations on tasks within a department. A `Viewer` can only read them. A `Member` can only update task status or priority for tasks assigned to them and comment under them.

### Attribute-Based Access Control (ABAC)
Access is granted based on specific attributes of the user, the resource, or the environment, providing finer-grained control than just roles.
- **Task Assignee**: A `Dept Member` might only be allowed to update a task's status or priority or comment under it *if they are assigned to it*. He can create more sub tasks and can assign them to people including himself who are working with him, in this particular task. The system must check if `task.assignees` contains `current_user.id`.
- **Comment Ownership**: A user can only edit or delete a comment if they created it (`comment.user_id == current_user.id`), regardless of their role.
- **Data Filtering based on Role**: An `Org Member` calling `GET /api/orgs/{org_id}` might receive a response with sensitive fields (like total billing or contact info) omitted, whereas an `Org Owner` receives the full payload.

---

## API Routes & Design

### 1. Authentication & User Management
These routes handle user lifecycle and do not require Org/Dept specific access control.

- `POST /api/auth/signup`: Create a new user account.
- `POST /api/auth/login`: Authenticate a user and return a JWT token.
- `POST /api/auth/logout`: Invalidate the current session.
- `POST /api/auth/forgot-password`: Send a password reset link to the user's email.
- `POST /api/auth/reset-password`: Reset the password using the token provided via email.
- `GET /api/auth/verify-email`: Verify the user's email address.
- `GET /api/users/me`: Get the current logged-in user's profile information.
- `PUT /api/users/me`: Update user profile details (name, profile image).

### 2. Organisation Invites
Routes to handle bringing users into an organisation via the `org_invites` table.

- `POST /api/orgs/{org_id}/invites`: Send an email invite to join the organisation.
  - **Access (RBAC)**: Org Owner, Org Admin.
- `GET /api/users/me/invites`: List pending organisation invites for the current user.
  - **Access**: Authenticated User.
- `POST /api/invites/{invite_id}/accept`: Accept an invite and create an `org_memberships` record.
  - **Access**: Authenticated User (must match invite email).
- `POST /api/invites/{invite_id}/reject`: Reject and delete an invite.
  - **Access**: Authenticated User.

### 3. Organisation Management
Routes for managing the top-level tenant.

- `POST /api/orgs`: Create a new organisation. Automatically assigns the `Owner` role to the creator.
  - **Access**: Authenticated User.
- `GET /api/orgs`: List all organisations the current user is a member of.
  - **Access**: Authenticated User.
- `GET /api/orgs/{org_id}`: Get details of a specific organisation.
  - **Access (RBAC + ABAC)**: All Org Members. Members receive limited details. Owners/Admins receive all details.
- `PUT /api/orgs/{org_id}`: Update organisation details (name, website, logo).
  - **Access (RBAC)**: Org Owner, Org Admin.
- `DELETE /api/orgs/{org_id}`: Delete the organisation entirely.
  - **Access (RBAC)**: Org Owner.
- `POST /api/orgs/{org_id}/transfer-ownership`: Transfer ownership to another user. Demotes the current owner to Admin.
  - **Access (RBAC)**: Org Owner.

#### Organisation Members
- `GET /api/orgs/{org_id}/members`: List all members of an organisation.
  - **Access (RBAC)**: All Org Members.
- `PUT /api/orgs/{org_id}/members/{user_id}/role`: Update a member's role (e.g., Member -> Admin).
  - **Access (RBAC)**: Org Owner, Org Admin. (Admins cannot promote to Owner or demote an Owner).
- `DELETE /api/orgs/{org_id}/members/{user_id}`: Remove a member from the organisation.
  - **Access (RBAC)**: Org Owner, Org Admin.

### 4. Department Management
Routes for managing sub-units within an organisation.

- `POST /api/orgs/{org_id}/departments`: Create a new department (or sub-department if `parent_id` is provided).
  - **Access (RBAC)**: Org Owner, Org Admin.
- `GET /api/orgs/{org_id}/departments`: List departments within an organisation.
  - **Access (RBAC)**: All Org Members.
- `GET /api/orgs/{org_id}/departments/{dept_id}`: Get specific department details.
  - **Access (RBAC)**: All Org Members.
- `PUT /api/orgs/{org_id}/departments/{dept_id}`: Update department details.
  - **Access (RBAC)**: Org Owner, Org Admin, Dept Manager.
- `DELETE /api/orgs/{org_id}/departments/{dept_id}`: Delete a department (must not contain tasks or sub-departments).
  - **Access (RBAC)**: Org Owner, Org Admin, Dept Manager.

#### Department Members
- `GET /api/orgs/{org_id}/departments/{dept_id}/members`: List members in a department.
  - **Access (RBAC)**: All Org Members.
- `POST /api/orgs/{org_id}/departments/{dept_id}/members`: Add a user (who is already an Org Member) to the department.
  - **Access (RBAC)**: Org Owner, Org Admin, Dept Manager.
- `PUT /api/orgs/{org_id}/departments/{dept_id}/members/{user_id}/role`: Update department role (Manager, Member, Viewer).
  - **Access (RBAC)**: Org Owner, Org Admin, Dept Manager.
- `DELETE /api/orgs/{org_id}/departments/{dept_id}/members/{user_id}`: Remove member from the department.
  - **Access (RBAC)**: Org Owner, Org Admin, Dept Manager.

### 5. Task Management
Routes for managing units of work. **Task Visibility Rule**: Tasks are strictly visible only to members/viewers of that specific department or its sub-departments.

- `POST /api/orgs/{org_id}/tasks`: Create a new task.
  - **Access (RBAC)**: Dept Manager (if assigning to a dept), Org Owner, Org Admin.
- `GET /api/orgs/{org_id}/tasks`: List tasks. Supports filtering by `department_id`, `status`, `assignee`, etc. Enforces visibility.
  - **Access (RBAC)**: Strictly visible only to members/viewers of that specific department or tasks in sub-departments.
- `GET /api/orgs/{org_id}/tasks/{task_id}`: Get details of a single task.
  - **Access (RBAC)**: Dept Members (including viewers/managers), Org Owner/Admin.
- `PUT /api/orgs/{org_id}/tasks/{task_id}`: Update task (title, description, assignee, priority, category).
  - **Access (RBAC)**: Dept Manager, Org Owner/Admin.
- `PATCH /api/orgs/{org_id}/tasks/{task_id}/status`: Update task status specifically.
  - **Access (RBAC + ABAC)**: Dept Manager, or Dept Member *only if they are an assignee of the task*.
- `DELETE /api/orgs/{org_id}/tasks/{task_id}`: Delete task (must not have subtasks or comments).
  - **Access (RBAC)**: Dept Manager, Org Owner/Admin.

### 6. Comments Management
Routes for communication on tasks.

- `POST /api/orgs/{org_id}/tasks/{task_id}/comments`: Add a comment to a task.
  - **Access (RBAC + ABAC)**: Dept Manager, or Dept Member who is an assignee.
- `GET /api/orgs/{org_id}/tasks/{task_id}/comments`: List comments for a task.
  - **Access (RBAC)**: Anyone who can view the task (Dept Viewers, Members, Managers).
- `PUT /api/orgs/{org_id}/tasks/{task_id}/comments/{comment_id}`: Update comment content.
  - **Access (ABAC)**: Only the comment creator (`user_id` matches).
- `DELETE /api/orgs/{org_id}/tasks/{task_id}/comments/{comment_id}`: Delete a comment.
  - **Access (RBAC + ABAC)**: Comment creator OR Dept Manager / Org Owner.

### 7. Task Categories (Org and Department Level)
Departments can have their own specific categories different from the org level.

- `POST /api/orgs/{org_id}/categories`: Create an org-level category.
- `POST /api/orgs/{org_id}/departments/{dept_id}/categories`: Create a department-specific category.
- `GET /api/orgs/{org_id}/categories`: List org-level categories.
- `GET /api/orgs/{org_id}/departments/{dept_id}/categories`: List department-specific categories.
- `PUT /api/orgs/{org_id}/categories/{category_id}`: Update category (works for both, depending on category ownership).
- `DELETE /api/orgs/{org_id}/categories/{category_id}`: Delete category.
  - **Access (RBAC)**: Org Owner/Admin for Org-level, Dept Manager for Dept-level.

---

## Next Steps
Now that the plan is finalized, we will proceed with implementing the Service layer logic and API Routers to enforce these RBAC/ABAC checks and fulfill these requirements.

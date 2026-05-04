# Product Requirements Document

## Trackly

Trackly is a multi-tenant task management application designed for professional organizations. It provides a structured way to manage work across different departments and teams.

## Core Modules
- **Authentication**: User signup, login, logout, password reset, email verification.
- **Authorization**: Role-based access control (Owner, Admin, Member and Viewer).
- **Organisation Management**: Create, invite members, update organisation info, update member roles, remove members, delete organisation. 
  - Owner can delete organisation. Admin can remove members and update member roles. Member and Viewer cannot delete or update organisation info or members or roles. Viewer can only view the organisation info.
  - Owner can transfer ownership from one person to another person and demote himself to admin.
- **Department Management**: 
  - Create, update, delete departments.
  - Add members to departments, update member roles in departments, remove members from departments.
    - Owner can delete department, add, update department and sub department info, add, remove members, update member roles in departments.
    - Admin can add, update department and sub department info, add, remove members, update member roles in departments.
    - Member and Viewer can only view the department info.
- **Task Management**: 
  - Create, update, delete, list tasks.
  - Add Sub tasks.
  - Assign tasks to users.
  - List tasks by assignee, status, priority, etc.
  - Update task status, priority, assignee, etc.
- **Comment Management**: 
  - List comments on a task.
  - Create a comment on a task.
  - Update a comment on a task.
  - Delete a comment on a task.

## Core Entities
- **Organisations**: The top-level tenant.
- **Departments**: Sub-units within an organisation and it can have sub departments (e.g., Engineering, Marketing).
- **Users**: Users who belong to organisations and departments with specific roles (i.e a Owner or Admin or Member or Viewer).
- **Tasks**: The primary unit of work, featuring statuses, priorities, and assignments with comments as a way of communicating.
- **Categories**: A way to organise tasks. A organisation can have custom categories that they choose or accept the default system categories.

## Success Metrics
- Successfully create and handle user signup, login, logout, password reset, email verification.
- Successfully create and handle organisation creation, update organisation core values, 
    - Add, update or remove departments and sub-departments, 
    - Manage user roles across the organisation, 
    - Add, update or remove members from departments,
    - Manage tasks and task categories across the organisation.
- Successfully create, update, delete, list tasks an sub tasks with statuses, priorities, assignees and comments.
- Successfully create, update, delete, list comments on a task.
- Successfully handle creation, updation, deletion, listing of task categories of a organisation.
- Successfully handle RBAC for organisations, departments, tasks and task categories.

## Key Workflows
1. **Onboarding**: Create an organisation and set up departments.
2. **Team Management**: Invite users and assign roles (Admin, Member).
3. **Task Lifecycle**: Create, assign, comment on, and complete tasks.
4. **Collaboration**: Real-time status updates and team-wide visibility.
5. **Role Management**: Manage user roles across the organisation and departments.
6. **Department Management**: Create, update, delete departments and sub departments.

## User Flows
### User Onboarding
- User gets on to user sign up/sign in page.
- User enters his email, name and password.
- User clicks on sign up button.
- System validates the user credentials and creates a new user.
- System sends a verification email to the user.
- User clicks on the verification link in the email.
- System verifies the user and logs him in.

### Organisation creation
- User logs in and is redirected to the organisation dashboard.
- User can create a new organisation by clicking on the create organisation button and
    - providing the organisation name and description.
    - User can provide organisation logo.
    - User can add website URL of the organisation.
    - User can add email domain of the organisation.
- User can choose to add departments or skip this step.
- User can choose to add members to the organisation or skip this step.
- User can choose to add task categories or accept the default system task categories.
- System creates the organisation and adds the user as an owner.
- System redirects the user to the organisation dashboard.

### Organisation Management
- User logs in and is redirected to the organisation dashboard.
- User can see a list of organisations he is a member of.
- If user is owner or admin of an organisation they can invite members to an organisation by providing their email addresses.
- If user is owner or admin of an organisation they can update the organisation information by providing the new information in organisation settings.
- If user is owner or admin of an organisation they can remove members from an organisation by going to the members tab in the organisation and remove members.
- If user is owner of an organisation they can delete an organisation by providing the organisation name.
  - User must give a confirmation by typing the organisation name.

### Department Management
- User logs in and is redirected to the organisation dashboard.
- User clicks on a organisation from the list of organisations.
- User can see a list of departments in the organisation.
- If user is owner or admin of an organisation they can add a new department by clicking on the add department button and 
    - providing the department name and description.
    - They can choose to add members to the department or skip this step.
    - They can choose to add task categories to the department or accept the default system task categories.
- If user is owner or admin of an organisation they can update a department by clicking on the edit button in the department card and 
    - providing the new department information.
- If user is owner of an organisation they can remove a department by clicking on the delete button in the department card and 
    - providing the department name for confirmation.

### Department lifecycle
- User is logged in and he clicks on a organisation he is part of.
- User is either owner or admin of an organisation.
- User can see a "Add Department" button if he is owner or admin of the organisation.
- User clicks on "Add Department" button.
- User is redirected to a new page where he can add a new department.
- User provides the department information.
- User clicks on the save button.
- System validates the department information.
- System creates the department and adds it to the organisation.
- System redirects the user to the department list.
- Adding a sub department in case it is needed and owner or admin can add sub departments to a department.
- Adding members to a department and owner or admin can add members to a department.
- Removing members from a department and owner or admin can remove members from a department.
- Deleting a department and owner or admin can delete a department.
  - if user tries to delete a department which has sub departments, system should show an error and ask user to delete sub departments first.
  - if user tries to delete a department which has members, system should show an error and ask user to remove members first.
  - if user tries to delete a department which has tasks, system should show an error and ask user to move tasks to another department or delete tasks first.

### Task lifecycle with comment
- User creates task
  - User can add title, description, assignee, due date, priority, status.
  - User can add sub tasks to a task or skip this step.
  - User can add comments to a task or skip this step.
  - Tasks can be optionally under a category or can be without category.
  - Tasks can optionally belong to a department or can be without department or sub department.
- User updates task
  - User can update task title, description, assignee, due date, priority, status.
  - User can add, update or delete sub tasks in a task created by him.
  - User can add, update or delete comments in a task created by him.
  - User can move a task to another category or can move it to be without category.
  - User can move a task to another department or can move it to be without department or sub department.
- User deletes task
  - User can delete task.
    - if user tries to delete a task which has sub tasks, system should show an error and ask user to delete sub tasks first. Task can be deleted only if it doesn't have any sub tasks
    - if user tries to delete a task which has comments, system should show an error and ask user to delete comments first. Task can be deleted only if it doesn't have any comments.

## Milestone

| Milestone | Description |
| - | - |
| **M1** | User authentication and user management. |
| **M2** | Organisation management and department management. |
| **M3** | Task management and task sub tasks. |
| **M4** | Task comments. |
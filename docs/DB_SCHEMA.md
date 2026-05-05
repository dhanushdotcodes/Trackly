# Database Schema
---
## Core Tables
---

users

| Column | Type | Notes | Description |
| :--- | :--- | :--- | :--- |
| id | uuid | PK | Unique identifier for the user |
| name | varchar(255) | | Full name of the user |
| email | varchar(255) | Unique, Index | Email address used for identification |
| password | varchar(255) | | Hashed password for authentication |
| profile_image_url | text | | URL to the user's profile picture |
| is_verified | boolean | | Indicates if the user is verified via email |
| created_at | timestamp | | Record creation timestamp |
| updated_at | timestamp | | Last update timestamp |

organisations

| Column | Type | Notes | Description |
| :--- | :--- | :--- | :--- |
| id | uuid | PK | Unique identifier for the organisation |
| name | varchar(255) | | Name of the organisation |
| website_url | text | | Direct link to the organisation website |
| logo_url | text | | URL to the organisation logo |
| created_at | timestamp | | Record creation timestamp |
| updated_at | timestamp | | Last update timestamp |

org_memberships

| Column | Type | Notes | Description |
| :--- | :--- | :--- | :--- |
| id | uuid | PK | Unique identifier for the membership |
| user_id | uuid | FK (`users.id`) | Reference to the user |
| org_id | uuid | FK (`organisations.id`) | Reference to the organisation |
| role | enum | `'Owner', 'Admin', 'Member'` | Role of the user in the organisation |
| joined_at | timestamp | | Timestamp when the user joined the organisation |

dept_memberships

| Column | Type | Notes | Description |
| :--- | :--- | :--- | :--- |
| id | uuid | PK | Unique identifier for the membership |
| user_id | uuid | FK (`users.id`) | Reference to the user |
| department_id | uuid | FK (`departments.id`) | Reference to the department |
| role | enum | `'Manager', 'Member', 'Viewer'` | Role of the user in the department |
| joined_at | timestamp | | Timestamp when the user joined the department |

departments

| Column | Type | Notes | Description |
| :--- | :--- | :--- | :--- |
| id | uuid | PK | Unique identifier for the department |
| org_id | uuid | FK (`organisations.id`) | Reference to the organisation |
| parent_id | uuid | FK (`departments.id`) | Reference to the parent department (optional) |
| name | varchar(255) | | Name of the department |
| created_at | timestamp | | Record creation timestamp |
| updated_at | timestamp | | Last update timestamp |

task_categories

| Column | Type | Notes | Description |
| :--- | :--- | :--- | :--- |
| id | uuid | PK | Unique identifier for the task category |
| org_id | uuid | FK (`organisations.id`) | Reference to the organisation |
| name | varchar(255) | | Name of the category |
| color | varchar(50) | | Hex color code for the category |
| created_at | timestamp | | Record creation timestamp |
| updated_at | timestamp | | Last update timestamp |

tasks

| Column | Type | Notes | Description |
| :--- | :--- | :--- | :--- |
| id | uuid | PK | Unique identifier for the task |
| org_id | uuid | FK (`organisations.id`) | Reference to the organisation |
| department_id | uuid | FK (`departments.id`) | Reference to the department (optional) |
| category_id | uuid | FK (`task_categories.id`) | Reference to the category (optional) |
| parent_id | uuid | FK (`tasks.id`) | Reference to the parent task (optional) |
| title | varchar(255) | | Task title |
| description | text | | Detailed task description |
| status | enum | `'To Do', 'Acknowledged', 'In Progress', 'In Review', 'Blocked', 'Completed', 'Cancelled'` | Current task status |
| priority | enum | `'Blocker', 'Critical', 'Ex. Important', 'In. Important', 'Minor'` | Task priority level |
| created_by | uuid | FK (`users.id`) | User who created the task |
| assigned_by | uuid | FK (`users.id`) | User who assigned the task (optional) |
| due_date | timestamp | | Task completion deadline (optional) |
| created_at | timestamp | | Record creation timestamp |
| updated_at | timestamp | | Last update timestamp |

task_assignees

| Column | Type | Notes | Description |
| :--- | :--- | :--- | :--- |
| id | uuid | PK | Unique identifier for the assignee record |
| task_id | uuid | FK (`tasks.id`) | Reference to the task |
| user_id | uuid | FK (`users.id`) | Reference to the user |
| assigned_at | timestamp | | Timestamp when the user was assigned the task |

task_comments

| Column | Type | Notes | Description |
| :--- | :--- | :--- | :--- |
| id | uuid | PK | Unique identifier for the comment |
| task_id | uuid | FK (`tasks.id`) | Reference to the task |
| user_id | uuid | FK (`users.id`) | Reference to the user who wrote the comment |
| content | text | | Comment message content |
| created_at | timestamp | | Record creation timestamp |
| updated_at | timestamp | | Last update timestamp |

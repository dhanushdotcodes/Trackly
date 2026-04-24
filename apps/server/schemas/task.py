from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict
from server.models import TaskStatus, TaskPriority

class TaskCategoryBase(BaseModel):
    name: str
    color: Optional[str] = None

class TaskCategoryResponse(TaskCategoryBase):
    id: UUID
    org_id: UUID
    created_at: datetime
    
    model_config = ConfigDict(from_attributes=True)

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: TaskStatus = TaskStatus.TO_DO
    priority: TaskPriority = TaskPriority.MINOR
    due_date: Optional[datetime] = None
    department_id: Optional[UUID] = None
    category_id: Optional[UUID] = None
    parent_id: Optional[UUID] = None

class TaskCreate(TaskBase):
    org_id: UUID
    created_by: UUID
    assigned_by: Optional[UUID] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
    due_date: Optional[datetime] = None
    department_id: Optional[UUID] = None
    category_id: Optional[UUID] = None
    parent_id: Optional[UUID] = None

class TaskResponse(TaskBase):
    id: UUID
    org_id: UUID
    created_by: UUID
    assigned_by: Optional[UUID] = None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class TaskCommentBase(BaseModel):
    content: str

class TaskCommentCreate(TaskCommentBase):
    task_id: UUID
    user_id: UUID

class TaskCommentResponse(TaskCommentBase):
    id: UUID
    task_id: UUID
    user_id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

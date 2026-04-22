from datetime import datetime
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel, ConfigDict

class DepartmentBase(BaseModel):
    name: str
    parent_id: Optional[UUID] = None

class DepartmentCreate(DepartmentBase):
    org_id: UUID

class DepartmentUpdate(BaseModel):
    name: Optional[str] = None
    parent_id: Optional[UUID] = None

class DepartmentResponse(DepartmentBase):
    id: UUID
    org_id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

from datetime import datetime
from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel, ConfigDict, HttpUrl
from api.db.models import UserRole

class OrganisationBase(BaseModel):
    name: str
    website_url: Optional[str] = None
    logo_url: Optional[str] = None

class OrganisationCreate(OrganisationBase):
    pass

class OrganisationUpdate(BaseModel):
    name: Optional[str] = None
    website_url: Optional[str] = None
    logo_url: Optional[str] = None

class OrganisationResponse(OrganisationBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

class OrgMembershipResponse(BaseModel):
    id: UUID
    user_id: UUID
    org_id: UUID
    department_id: Optional[UUID] = None
    role: UserRole
    joined_at: datetime

    model_config = ConfigDict(from_attributes=True)

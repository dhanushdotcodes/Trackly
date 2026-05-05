from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, ConfigDict
from server.models import OrgRole, DeptRole

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
    role: OrgRole
    joined_at: datetime

    model_config = ConfigDict(from_attributes=True)

class DeptMembershipResponse(BaseModel):
    id: UUID
    user_id: UUID
    department_id: UUID
    role: DeptRole
    joined_at: datetime

    model_config = ConfigDict(from_attributes=True)

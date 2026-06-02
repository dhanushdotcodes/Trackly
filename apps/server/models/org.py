import uuid
from datetime import datetime
from typing import List, Optional, TYPE_CHECKING
from sqlalchemy import String, DateTime, Text, ForeignKey, func, Enum, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base, OrgRole, DeptRole

if TYPE_CHECKING:
    from .user import User
    from .task import Task, TaskCategory

class Organisation(Base):
    __tablename__ = "organisations"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    website_url: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    logo_url: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relationships
    members: Mapped[List["OrgMembership"]] = relationship("OrgMembership", back_populates="organisation")
    departments: Mapped[List["Department"]] = relationship("Department", back_populates="organisation")
    tasks: Mapped[List["Task"]] = relationship("Task", back_populates="organisation")
    categories: Mapped[List["TaskCategory"]] = relationship("TaskCategory", back_populates="organisation")

class OrgMembership(Base):
    __tablename__ = "org_memberships"
    __table_args__ = (UniqueConstraint("user_id", "org_id", name="uq_user_org"),)

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    org_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("organisations.id"), nullable=False)
    
    role: Mapped[OrgRole] = mapped_column(Enum(OrgRole), default=OrgRole.MEMBER, nullable=False)
    joined_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="org_memberships")
    organisation: Mapped["Organisation"] = relationship("Organisation", back_populates="members")

class DeptMembership(Base):
    __tablename__ = "dept_memberships"
    __table_args__ = (UniqueConstraint("user_id", "department_id", name="uq_user_dept"),)

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    department_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("departments.id"), nullable=False)
    
    role: Mapped[DeptRole] = mapped_column(Enum(DeptRole), default=DeptRole.MEMBER, nullable=False)
    joined_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())

    # Relationships
    user: Mapped["User"] = relationship("User", back_populates="dept_memberships")
    department: Mapped["Department"] = relationship("Department", back_populates="members")

class Department(Base):
    __tablename__ = "departments"
    __table_args__ = (UniqueConstraint("org_id", "name", name="uq_org_dept_name"),)

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    org_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("organisations.id"), nullable=False)
    parent_id: Mapped[Optional[uuid.UUID]] = mapped_column(ForeignKey("departments.id"), nullable=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relationships
    organisation: Mapped["Organisation"] = relationship("Organisation", back_populates="departments")
    parent: Mapped[Optional["Department"]] = relationship("Department", remote_side=[id], back_populates="sub_departments")
    sub_departments: Mapped[List["Department"]] = relationship("Department", back_populates="parent")
    members: Mapped[List["DeptMembership"]] = relationship("DeptMembership", back_populates="department")
    tasks: Mapped[List["Task"]] = relationship("Task", back_populates="department")

class OrgInvite(Base):
    __tablename__ = "org_invites"
    __table_args__ = (UniqueConstraint("org_id", "email", name="uq_org_invite_email"),)

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    org_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("organisations.id"), nullable=False)
    email: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[OrgRole] = mapped_column(Enum(OrgRole), default=OrgRole.MEMBER, nullable=False)
    token: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    expires_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())

    # Relationships
    organisation: Mapped["Organisation"] = relationship("Organisation")

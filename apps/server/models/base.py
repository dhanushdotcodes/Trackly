import enum
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class UserRole(str, enum.Enum):
    OWNER = "Owner"
    ADMIN = "Admin"
    MEMBER = "Member"
    VIEWER = "Viewer"

class TaskStatus(str, enum.Enum):
    TO_DO = "To Do"
    ACKNOWLEDGED = "Acknowledged"
    IN_PROGRESS = "In Progress"
    IN_REVIEW = "In Review"
    BLOCKED = "Blocked"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class TaskPriority(str, enum.Enum):
    BLOCKER = "Blocker"
    CRITICAL = "Critical"
    EX_IMPORTANT = "Ex. Important"
    IN_IMPORTANT = "In. Important"
    MINOR = "Minor"

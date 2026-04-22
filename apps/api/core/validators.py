import re
from datetime import datetime, timezone
from typing import Optional

# --- User Validators ---

def validate_email(email: str) -> bool:
    """Simple regex to validate email format."""
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(email_regex, email))

def validate_name(name: str) -> bool:
    """Ensure name is not empty and has a reasonable length."""
    return 1 <= len(name.strip()) <= 255

# --- Organization Validators ---

def validate_org_name(name: str) -> bool:
    """Ensure organization name is valid."""
    return 1 <= len(name.strip()) <= 255

# --- Task Validators ---

def validate_task_title(title: str) -> bool:
    """Ensure task title is valid."""
    return 1 <= len(title.strip()) <= 255

def validate_due_date(due_date: Optional[datetime]) -> bool:
    """Ensure due date is in the future if provided."""
    if due_date is None:
        return True
    
    # Ensure due_date is timezone-aware if comparing with now()
    if due_date.tzinfo is None:
        due_date = due_date.replace(tzinfo=timezone.utc)
    
    now = datetime.now(timezone.utc)
    return due_date > now

# --- Role & Permission Validators ---

def can_create_task(role: str) -> bool:
    """Only OWNER, ADMIN, and MEMBER can create tasks."""
    return role.upper() in ["OWNER", "ADMIN", "MEMBER"]

def can_assign_task(role: str) -> bool:
    """Only OWNER, ADMIN, and potentially MANAGERS (ADMIN role) can assign tasks."""
    return role.upper() in ["OWNER", "ADMIN"]

def can_manage_departments(role: str) -> bool:
    """Only OWNER and ADMIN can manage departments."""
    return role.upper() in ["OWNER", "ADMIN"]

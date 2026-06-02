from typing import Sequence, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from server.models.user import User

async def get_all_users(db: AsyncSession) -> Sequence[User]:
    """
    Fetches all users from the database.
    """
    async with db.begin():
        result = await db.execute(select(User))
        return result.scalars().all()

async def get_user_by_email(db: AsyncSession, email: str) -> Optional[User]:
    """
    Fetches a user by their email address.
    """
    async with db.begin():
        result = await db.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

async def create_user(db: AsyncSession, user_data: dict) -> User:
    """
    Creates a new user in the database.
    """
    user = User(**user_data)
    async with db.begin():
        db.add(user)
    await db.refresh(user)
    return user

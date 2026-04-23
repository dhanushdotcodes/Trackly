from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from sqlalchemy import select
from server.core.database import get_db
from server.models import User
from server.schemas.user import UserResponse

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=List[UserResponse])
async def get_users(db: AsyncSession = Depends(get_db)):
    """
    Fetch all users from the database.
    """
    async with db.begin():
        result = await db.execute(select(User))
        return result.scalars().all()

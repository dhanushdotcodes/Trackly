from typing import Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from server.models.user import User

async def get_all_users(db: AsyncSession) -> Sequence[User]:
    """
    Fetches all users from the database.
    Following the rule to use 'async with db.begin():' for transactions.
    """
    async with db.begin():
        result = await db.execute(select(User))
        return result.scalars().all()

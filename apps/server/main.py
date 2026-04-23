from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import text
from .core.database import engine
from .api.v1 import users

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Connect to db and verify connection before starting
    async with engine.connect() as conn:
        await conn.execute(text("SELECT 1"))
    yield
    # Cleanup: close connection pool
    await engine.dispose()

app = FastAPI(
    title="Trackly API",
    lifespan=lifespan
)

# Include routers
app.include_router(users.router, prefix="/api/v1")

@app.get("/")
def main():
    return {"message": "Hello World"}

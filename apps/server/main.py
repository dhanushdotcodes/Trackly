from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import text
from fastapi.middleware.cors import CORSMiddleware
from server.core.database import engine
from server.api.v1 import users, auth, health

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

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth.router, prefix="/api/v1")
app.include_router(users.router, prefix="/api/v1")
app.include_router(health.router, prefix="/api/v1")

@app.get("/")
def main():
    return {"message": "Hello World"}

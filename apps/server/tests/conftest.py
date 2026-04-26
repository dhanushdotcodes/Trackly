import pytest
from fastapi.testclient import TestClient

@pytest.fixture
def client():
    """
    Fixture for FastAPI TestClient using the real application and database.
    The application lifespan in main.py will handle database connectivity checks.
    """
    from server.main import app
    try:
        with TestClient(app) as c:
            yield c
    except Exception as e:
        pytest.exit(f"Failed to start TestClient: {e}. Ensure your database is running.")

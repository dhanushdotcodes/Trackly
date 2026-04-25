import pytest
from unittest.mock import patch, AsyncMock
from fastapi.testclient import TestClient

@pytest.fixture(autouse=True)
def mock_db_engine():
    """
    Mock the database engine to prevent connection attempts during tests.
    """
    with patch("server.core.database.engine") as mock_engine:
        # Mock the connect method which is used in lifespan
        # It needs to return a context manager that returns an AsyncMock
        mock_conn = AsyncMock()
        mock_engine.connect.return_value.__aenter__.return_value = mock_conn
        
        # Mock dispose as an AsyncMock
        mock_engine.dispose = AsyncMock()
        
        yield mock_engine

@pytest.fixture
def client(mock_db_engine):
    """
    Fixture for FastAPI TestClient.
    """
    from server.main import app
    with TestClient(app) as c:
        yield c
